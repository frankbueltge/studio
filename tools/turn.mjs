// turn.mjs — at the beat where the run turns, what actually moves, and how much of it?
//
// Why this exists. `DRAMATURG-92.md` cut 2 is an order written in arithmetic: at the final
// beat the share is 12,961 px², the new name chips 18,704 px², the fraction 2,774 px², and
// **the count that turns 2,989 px² — 8.0 % of everything that changes** — so the one node in
// twenty-nine seconds that changes KIND is the least emphatic thing in its own frame. Half
// that cut was paid in session 92 and half is owed, and the owed half — *the share gives way
// to it* — is a judgement about proportions that the same night's arithmetic correction
// changed: the upper end of the share, which stood at 100 % through every stop, now falls at
// the last three. A house that answers a measured order with a preference has stopped being
// answerable. This file re-runs that measurement on whatever state it is pointed at, so the
// voice that wrote the order and any voice after it can read the proportions of the object
// in front of them instead of the object the order was written against.
//
//   NODE_PATH=<global node_modules> node tools/turn.mjs
//   NODE_PATH=... node tools/turn.mjs --dir=projects/season1/still-dark --width=390
//
// WHAT IT MEASURES. Every text node inside the head's frame and the two name lists is read
// at the second-to-last stop and again at the last stop; a node whose text differs between
// the two is a node the beat rewrites. Its area is its own bounding box (for the lists, the
// bounding boxes of the chips that are new). The report is those areas, each as a share of
// their sum. Area is a proxy for emphasis and this file does not pretend it is more than
// that: a big pale word and a small black one can carry the same weight on a page. It
// answers the question the memo asked in the units the memo used.
//
// WHAT IT WAS CHECKED AGAINST, and the limit of that check. Run at 1400 px on the last
// committed object before session 92 (`git show b619af4:projects/season1/still-dark/
// index.html`), it returns the share at **12,961 px²** and the fraction at **2,774 px²** —
// both of them `DRAMATURG-92.md`'s figures to the pixel. It does NOT reproduce that memo's
// other two: the object the memo drove was the working tree with the tenth list's island
// already built into it, which was never committed in that state, and on the committed one
// the last beat adds two chips and not seven. Two of four, on the two nodes that did not
// change between the two states, is what this file can honestly claim.
//
// Dependencies, named honestly: node >= 18 and playwright (chromium) — the house's check on
// itself, not a dependency of the work.
import { createRequire } from "node:module";
import { join, resolve } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const argv = process.argv.slice(2);
const arg = (k, d) => {
  const hit = argv.find((a) => a.startsWith(`--${k}=`));
  return hit ? hit.slice(k.length + 3) : d;
};
const dir = resolve(arg("dir", "projects/season1/still-dark"));
const url = "file://" + join(dir, "index.html");
const WIDTHS = (arg("width", "390,1400")).split(",").map(Number);

const NODES = [
  ["#sd-arrive-count", "the share, both ends"],
  ["#sd-arrive-frac", "the falling end as a division"],
  ["#sd-arrive-frac-fixed", "the upper end as a division"],
  ["#sd-arrive-certain", "the count that turns"],
  ["#sd-arrive-standing-fig", "the day's own list, standing"],
  ["#sd-arrive-head-since", "the hole's heading"],
  ["#sd-arrive-state", "the run's line"],
];

const browser = await chromium.launch();
for (const w of WIDTHS) {
  const ctx = await browser.newContext({
    viewport: { width: w, height: w <= 480 ? 844 : 900 },
    colorScheme: "light",
    // THE RUN PLAYS — `DRAMATURG-94` cut 5. This context asked for reduced motion and the
    // instrument then CLICKED its way to the two states it compares, which books a node the
    // automatic run never rewrites: the state line says "Holding +10 DAYS…" under a finger
    // and says nothing at a beat. That voice put a mutation observer on it across a whole
    // unattended run — three writes, at the start, at the run's beginning and at its end,
    // none at the ten beats — and this instrument was reporting it as 21–28 % of the turn's
    // motion. The performance every unattended visitor sees is the one measured here now.
    reducedMotion: "no-preference",
  });
  const page = await ctx.newPage();
  await page.goto(url);
  await page.waitForTimeout(300);
  const stops = await page.$$eval(
    "#sd-arrive-ladder button:not(.sd-arrive-replay)",
    (b) => b.length,
  );
  const read = async () => {
    return await page.evaluate((sel) => {
      const out = {};
      for (const [s, label] of sel) {
        const el = document.querySelector(s);
        if (!el) continue;
        const r = el.getBoundingClientRect();
        out[label] = {
          text: el.textContent.trim(),
          area: Math.round(r.width * r.height),
          size: Math.round(parseFloat(getComputedStyle(el).fontSize) * 10) / 10,
          weight: getComputedStyle(el).fontWeight,
        };
      }
      // The chips of the hole, by name, so that "new at this beat" is a set difference and
      // not a count that a re-ordering could fake.
      out["__chips"] = [...document.querySelectorAll("#sd-arrive-names-since li")].map(
        (li) => {
          const r = li.getBoundingClientRect();
          return { t: li.textContent.trim(), a: Math.round(r.width * r.height) };
        },
      );
      return out;
    }, sel);
  };
  const sel = NODES;
  // The two readings are taken from the running page, on either side of the beat that lands
  // the last state — the page publishes when that is, so neither instant is guessed.
  const run = await page.evaluate(() => window.__sdRun);
  const elapsed = () => page.evaluate(() => performance.now());
  const waitUntil = async (ms) => {
    const now = await elapsed();
    if (ms > now) await page.waitForTimeout(ms - now);
  };
  await waitUntil(run.ends_ms - 250);
  const before = await read();
  await waitUntil(run.ends_ms + 250);
  const after = await read();

  const seen = new Set(before.__chips.map((c) => c.t));
  const fresh = after.__chips.filter((c) => !seen.has(c.t));
  const rows = [];
  for (const [, label] of NODES) {
    const b = before[label];
    const a = after[label];
    if (!b || !a || b.text === a.text) continue;
    rows.push({ label, area: a.area, size: a.size, weight: a.weight, text: a.text });
  }
  if (fresh.length) {
    rows.push({
      label: `the ${fresh.length} name${fresh.length === 1 ? "" : "s"} the beat adds`,
      area: fresh.reduce((s, c) => s + c.a, 0),
      size: null,
      weight: null,
      text: fresh.map((c) => c.t.split("\n")[0]).join(" · ").slice(0, 60),
    });
  }
  const total = rows.reduce((s, r) => s + r.area, 0) || 1;
  rows.sort((x, y) => y.area - x.area);
  console.log(
    `\nTURN — ${w} px, the beat from stop ${stops - 2} to stop ${stops - 1}: ` +
      `${rows.length} node${rows.length === 1 ? "" : "s"} rewritten, ${total} px² in motion`,
  );
  for (const r of rows) {
    const pct = ((r.area / total) * 100).toFixed(1);
    console.log(
      `  ${String(r.area).padStart(6)} px²  ${pct.padStart(5)} %  ` +
        `${r.size ? `${r.size} px/${r.weight}  ` : "              "}${r.label}` +
        (r.text ? `  — “${r.text.replace(/\s+/g, " ").slice(0, 44)}”` : ""),
    );
  }
  // THE MEMO'S OWN BASIS, printed beside the full one so the two numbers are comparable
  // without hand arithmetic. `DRAMATURG-92.md` cut 2 counted four nodes — the share, the new
  // chips, the fraction and the turning numeral, 37,428 px² at 1400 — and did not count the
  // hole's heading or the run's line, both of which the same beat also rewrites. A later
  // percentage taken over seven nodes and compared with that 8.0 % would be a comparison of
  // two different denominators, which is the class of error this project banked at the gate
  // of 92 in a far more expensive form.
  const memoBasis = ["the share, both ends", "the falling end as a division",
    "the count that turns"];
  const four = rows.filter(
    (r) => memoBasis.includes(r.label) || r.label.endsWith("the beat adds"),
  );
  const fourTotal = four.reduce((s, r) => s + r.area, 0);
  const turnRow = rows.find((r) => r.label === "the count that turns");
  if (turnRow && fourTotal) {
    console.log(
      `  on the four nodes DRAMATURG-92 counted (${fourTotal} px²): ` +
        `the count that turns is ${((turnRow.area / fourTotal) * 100).toFixed(1)} % ` +
        `— that memo measured 8.0 % at 1400 px, before its first half was paid.`,
    );
  }
  await ctx.close();
}
await browser.close();
