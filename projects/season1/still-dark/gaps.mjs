// STILL DARK — measure whether every bar stands nearer its own label than the next one's.
//
// Why this exists. Session 74's first sighted panel found that every bar in the time
// field was misaligned with its label; the repair left a residue nobody could measure.
// Owed item (c) has stood unpaid since — "the bar/label gap discriminates by ~3 px in
// thirteen of sixteen rows, and three readers misassigned them" — and three sessions
// running it was deferred because the way to settle it looked like another panel. It is
// not. A bar belongs to the row above it, and whether a reader can see that is a
// question about two distances on a screen, which a browser can be asked directly.
//
// The rule this measures, and the only one: a bar must stand STRICTLY NEARER the label
// it belongs to than the label of the row below it. Where it does not, the layout is
// telling the eye the opposite of what the DOM says, and no amount of reading fixes it.
//
//   NODE_PATH=<global node_modules> node gaps.mjs            (from this directory)
//   NODE_PATH=... node gaps.mjs ../staging-78/control        (any staged arm)
//   NODE_PATH=... node gaps.mjs --json
//
// Exit 0 if every row passes at both widths, 1 if any row fails, 2 on error. Nothing is
// typed: both distances are read off getBoundingClientRect in the rendered page.
//
// Dependencies, named honestly: node >= 18 and playwright (chromium) — the house's own
// check on itself, not a dependency of the work. index.html stays self-contained.
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const { chromium } = createRequire(import.meta.url)("playwright");

const here = dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const asJson = argv.includes("--json");
const dirArg = argv.find((a) => !a.startsWith("--"));
// The work graduated to `works/2026-08-15-still-dark/` at its premiere (session 96); this
// instrument stayed here with the builder, because a guard is this house's check on the work
// and not part of it. The default follows the page; `--dir` still points anywhere.
const WORK = join(here, "..", "..", "..", "works", "2026-08-15-still-dark");
const target = dirArg ? join(here, dirArg) : WORK;
const page_url = "file://" + join(target, "index.html");

const WIDTHS = [1400, 900];

// Session 91, DRAMATURG-91 cut 1. The bar/label rule above is measured at 1400 and 900 —
// and that is exactly why nothing in this house saw the second defect in the same chart for
// three sessions: the time field's DATE AXIS overprinted itself in 8 of its 9 gaps at 360,
// 390 and 414 px, and both committed renders are taken at widths where it comes out clean.
// An instrument that only looks where the pictures are taken is an instrument that agrees
// with the pictures. So the axis is measured on its own, at phone widths first.
//
// The rule, and the only one: no tick label may overlap the next one along. A negative gap
// is ink on ink, and a date axis that prints two dates on top of each other is worse than
// one that prints fewer dates.
const AXIS_WIDTHS = [360, 390, 414, 480, 700, 900, 1400];

// Only labels the browser actually paints are measured: below 700 px the page keeps four of
// the ten and drops the rest, so a display:none label is not ink and does not make a gap.
const measureAxis = () => {
  const vis = Array.from(document.querySelectorAll(".sd-tick"))
    .filter((el) => getComputedStyle(el).display !== "none")
    .map((el) => ({ text: el.textContent.trim(), rect: el.getBoundingClientRect() }))
    .sort((a, b) => a.rect.left - b.rect.left);
  const gaps = [];
  for (let i = 1; i < vis.length; i++) {
    gaps.push({
      left: vis[i - 1].text,
      right: vis[i].text,
      gap: vis[i].rect.left - vis[i - 1].rect.right,
    });
  }
  return { labels: vis.map((v) => v.text), gaps };
};

// Read in the page: for every row, the bottom of its own text line, the top and bottom
// of its bar, and the top of the next row's text line. Group heads count as a next
// label: a bar sitting under the last row of a group is read against whatever text
// comes next, because that is what an eye does.
//
// Both distances are measured GLYPH TO BAR, not box to box. A row's padding is not
// something an eye can see; the ink is. Measuring to the row box understates the gap
// below every bar by one padding-top and would have scored this field kinder than the
// readers did.
const measure = () => {
  const out = [];
  // every line of ink in the field, in document order, so "the next label below this
  // bar" is whatever the eye actually meets — a vessel's name or a group head
  const labels = Array.from(
    document.querySelectorAll(".sd-row .sd-name, .sd-grouphead")
  ).map((el) => ({
    rect: el.getBoundingClientRect(),
    kind: el.classList.contains("sd-grouphead") ? "grouphead" : "row",
  }));
  Array.from(document.querySelectorAll(".sd-row")).forEach((row) => {
    const name = row.querySelector(".sd-name");
    const segs = Array.from(row.querySelectorAll(".sd-seg"));
    if (!name || segs.length === 0) return;
    const textBottom = name.getBoundingClientRect().bottom;
    const barTop = Math.min(...segs.map((s) => s.getBoundingClientRect().top));
    const barBottom = Math.max(...segs.map((s) => s.getBoundingClientRect().bottom));
    // the first line of ink that starts below this bar
    const below = labels
      .filter((l) => l.rect.top >= barBottom - 0.01)
      .sort((a, b) => a.rect.top - b.rect.top)[0];
    out.push({
      name: name.textContent.trim(),
      own_gap: barTop - textBottom,
      next_gap: below ? below.rect.top - barBottom : null,
      next_kind: below ? below.kind : "(end of field)",
    });
  });
  return out;
};

const browser = await chromium.launch();
const report = { page: page_url, widths: {} };
let failures = 0;

for (const width of WIDTHS) {
  const ctx = await browser.newContext({
    viewport: { width, height: 900 },
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(page_url);
  await page.waitForLoadState("load");
  const rows = await page.evaluate(measure);
  await ctx.close();

  const scored = rows.map((r) => {
    // the last bar in the field has nothing below it and cannot be misassigned
    const decided = r.next_gap === null ? true : r.own_gap < r.next_gap;
    return {
      ...r,
      own_gap: round(r.own_gap),
      next_gap: r.next_gap === null ? null : round(r.next_gap),
      margin: r.next_gap === null ? null : round(r.next_gap - r.own_gap),
      pass: decided,
    };
  });
  const bad = scored.filter((r) => !r.pass);
  failures += bad.length;
  report.widths[width] = {
    rows: scored.length,
    failing: bad.length,
    // the narrowest true margin in the field: how much the eye has to go on in the
    // worst row, not the average, which hides exactly the rows that misassign
    tightest_margin: Math.min(
      ...scored.filter((r) => r.margin !== null).map((r) => r.margin)
    ),
    detail: scored,
  };
}

report.axis = {};
let axisFailures = 0;

for (const width of AXIS_WIDTHS) {
  const ctx = await browser.newContext({
    viewport: { width, height: 900 },
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(page_url);
  await page.waitForLoadState("load");
  const a = await page.evaluate(measureAxis);
  await ctx.close();

  const gaps = a.gaps.map((g) => ({ ...g, gap: round(g.gap) }));
  const bad = gaps.filter((g) => g.gap < 0);
  axisFailures += bad.length;
  report.axis[width] = {
    labels: a.labels,
    shown: a.labels.length,
    gaps: gaps.length,
    colliding: bad.length,
    tightest: gaps.length ? Math.min(...gaps.map((g) => g.gap)) : null,
    detail: gaps,
  };
}

await browser.close();

function round(n) {
  return Math.round(n * 100) / 100;
}

if (asJson) {
  console.log(JSON.stringify(report, null, 2));
} else {
  for (const [width, w] of Object.entries(report.widths)) {
    console.log(`\n${width} px — ${w.rows} rows, ${w.failing} failing`);
    console.log(
      "  bar nearer its OWN label in " +
        (w.rows - w.failing) +
        " of " +
        w.rows +
        " rows · tightest margin " +
        w.tightest_margin +
        " px"
    );
    for (const r of w.detail) {
      const flag = r.pass ? "  " : "!!";
      console.log(
        `  ${flag} ${r.name.padEnd(22)} own ${String(r.own_gap).padStart(6)} px` +
          `   next ${String(r.next_gap).padStart(6)} px` +
          `   margin ${String(r.margin).padStart(6)} px`
      );
    }
  }
  console.log("\nTHE DATE AXIS — no tick label may overlap the next one along");
  for (const [width, a] of Object.entries(report.axis)) {
    const flag = a.colliding ? "!!" : "  ";
    console.log(
      `${flag} ${String(width).padStart(4)} px — ${String(a.shown).padStart(2)} labels shown, ` +
        `${a.colliding} of ${a.gaps} gaps colliding · tightest ${a.tightest} px`
    );
    if (a.colliding) {
      for (const g of a.detail.filter((x) => x.gap < 0)) {
        console.log(`       ${g.left} over ${g.right} — ${g.gap} px`);
      }
    }
  }

  console.log(
    failures === 0
      ? "\nPASS — every bar stands nearer its own label at both widths."
      : `\nFAIL — ${failures} row(s) whose bar stands nearer the label below it.`
  );
  console.log(
    axisFailures === 0
      ? `PASS — no tick label overlaps its neighbour at any of ${AXIS_WIDTHS.length} widths.`
      : `FAIL — ${axisFailures} colliding tick-label gap(s).`
  );
}

process.exit(failures === 0 && axisFailures === 0 ? 0 : 1);
