// width.mjs — does the page ever stand wider than the window it is in?
//
// Why this exists, and it is one banked failure of this house written as a machine.
// Session 86 stopped `still-dark/index.html` scrolling sideways inside a 390 px phone and
// scoped the repair to a 480 px media query, writing its reason into the file: *"the desktop
// line is the one the renders and every panel to date have seen, and a repair is not a
// licence to restage what nobody complained of."* The page went on standing 665 px wide at
// every viewport from 481 to 664 px — 184 continuous widths, overflowing by up to 184 px,
// 38 % of the window — for six sessions, until the staging voice of session 92 swept
// 440→1100 px by hand and found it (`DRAMATURG-92.md` cut 1, banked failure 55). Every
// instrument this house owns reads the widths its pictures are taken at: 390 and 1400, plus
// the nine the staging voice boxes elements at. A defect that lives between two measured
// widths is invisible to all of them, and the only reason it was ever found is that one
// voice, once, swept.
//
//   NODE_PATH=<global node_modules> node tools/width.mjs
//   NODE_PATH=... node tools/width.mjs --dir=projects/season1/still-dark --step=5
//   NODE_PATH=... node tools/width.mjs --lo=280 --hi=1920 --step=1     # the whole band, slow
//
// WHAT IT DOES. One page, resized across the band; at every width it asks whether the
// document is wider than the window, and where it is, it names the widest element crossing
// the window's right edge, with that element's computed `min-width`. Boundaries are then
// walked at 1 px so the report gives the band's exact ends, because "somewhere around 480"
// is how a repair gets scoped to the wrong place. It exits 1 if any width overflows.
//
// THE NAMED ELEMENT IS THE WIDEST SYMPTOM, NOT THE PROVEN CAUSE, and this file will not
// pretend otherwise. Run against the object session 92 was frozen on (`git show
// b619af4:projects/season1/still-dark/index.html`), it reproduces that voice's hand sweep
// exactly — **OVERFLOW 481→664 px, 184 widths, worst +184 px** — and names the `table` that
// is 184 px too wide, where the voice, hit-testing every unclipped element, named the
// `span.sd-share-when` with `min-width: 292.089px` INSIDE that table. Both are true and only
// one of them is the thing to edit. A sweep tells a session which widths to look at and what
// is sticking out there; finding what makes it stick out is still reading.
//
// WHAT IT DOES NOT DO. It reads the page at rest, at its first stop. A sideways scroll that
// only a later stop can produce is not in its reach, and this file says so rather than
// leaving the next session to assume a sweep is a proof. The run's own states are swept by
// `frame.mjs`, which drives every stop and measures heights.
//
// Dependencies, named honestly: node >= 18 and playwright (chromium) — the house's check on
// itself, not a dependency of any work. The pages it reads ship with no runtime dependency.
import { createRequire } from "node:module";
import { join, resolve } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const argv = process.argv.slice(2);
const arg = (k, d) => {
  const hit = argv.find((a) => a.startsWith(`--${k}=`));
  return hit ? hit.slice(k.length + 3) : d;
};
// The work graduated to `works/` at its premiere, session 96. The default follows it;
// `--dir=` still points this instrument at any built copy, which is how the retired
// states at earlier hashes are still measurable.
const WORK_DIR = "works/2026-08-15-still-dark";
const dir = resolve(arg("dir", WORK_DIR));
const url = "file://" + join(dir, "index.html");
const LO = Number(arg("lo", 280));
const HI = Number(arg("hi", 1920));
const STEP = Number(arg("step", 5));
const HEIGHT = Number(arg("height", 844));

const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: HI, height: HEIGHT },
  colorScheme: "light",
  reducedMotion: "reduce",
});
const page = await ctx.newPage();
await page.goto(url);
await page.waitForTimeout(300);

// The culprit is asked for by measurement, not by guess: the widest element whose right
// edge stands outside the window. `getBoundingClientRect` on every element is affordable
// once per overflowing width, and only overflowing widths pay for it.
const probe = async (w) => {
  await page.setViewportSize({ width: w, height: HEIGHT });
  await page.waitForTimeout(30);
  return await page.evaluate((vw) => {
    const docW = Math.round(document.documentElement.scrollWidth);
    if (docW <= vw) return { docW, over: 0, who: null };
    let worst = null;
    for (const el of document.querySelectorAll("*")) {
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) continue;
      if (r.right <= vw + 0.5) continue;
      const out = Math.round(r.right - vw);
      if (!worst || out > worst.out) {
        const id = el.id ? `#${el.id}` : "";
        const cls = el.className && typeof el.className === "string"
          ? "." + el.className.trim().split(/\s+/).join(".")
          : "";
        worst = {
          out,
          sel: el.tagName.toLowerCase() + id + cls,
          minWidth: getComputedStyle(el).minWidth,
        };
      }
    }
    return { docW, over: docW - vw, who: worst };
  }, w);
};

const bad = [];
for (let w = LO; w <= HI; w += STEP) {
  const r = await probe(w);
  if (r.over > 0) bad.push({ w, ...r });
}

// The ends of every band, at 1 px. A band reported as "from about 480" is how the defect
// this file exists for was scoped to the wrong width in the first place.
const bands = [];
for (const b of bad) {
  const last = bands[bands.length - 1];
  if (last && b.w - last.hi <= STEP) {
    last.hi = b.w;
    last.worst = Math.max(last.worst, b.over);
    if (b.who && (!last.who || b.over >= last.worstSeen)) {
      last.who = b.who;
      last.worstSeen = b.over;
    }
  } else {
    bands.push({
      lo: b.w,
      hi: b.w,
      worst: b.over,
      worstSeen: b.over,
      who: b.who,
    });
  }
}
for (const band of bands) {
  for (let w = band.lo - 1; w >= LO; w--) {
    const r = await probe(w);
    if (r.over <= 0) break;
    band.lo = w;
    band.worst = Math.max(band.worst, r.over);
  }
  for (let w = band.hi + 1; w <= HI; w++) {
    const r = await probe(w);
    if (r.over <= 0) break;
    band.hi = w;
    band.worst = Math.max(band.worst, r.over);
  }
}

console.log(
  `WIDTH — ${dir.split("/").slice(-2).join("/")}, ${LO}→${HI} px in ${STEP} px steps` +
    `, boundaries walked at 1 px, height ${HEIGHT}`,
);
if (!bands.length) {
  console.log(`  no width holds a document wider than its window. CLEAN.`);
} else {
  for (const band of bands) {
    const n = band.hi - band.lo + 1;
    console.log(
      `  OVERFLOW ${band.lo}→${band.hi} px (${n} width${n === 1 ? "" : "s"}), ` +
        `worst +${band.worst} px` +
        (band.who
          ? ` — widest offender ${band.who.sel}, min-width ${band.who.minWidth}`
          : ""),
    );
  }
}
await browser.close();
process.exit(bands.length ? 1 : 0);
