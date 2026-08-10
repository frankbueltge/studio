// fold.mjs — where the head's parts sit relative to the fold, measured in a browser.
//
// Why this exists. `DRAMATURG-83.md` §4 drove the built page at 390×844 and found the
// figure on screen at y=248 while the ladder (y=938) and the run's own state line (y=991)
// were both below an 844 px fold: a reader on a phone watched the number fall with the
// controls that drive it and the line that announces it off-screen. This house had no
// instrument that could have found that, and no instrument that can say whether a repair
// worked. Item (y) is a measurement, so it gets one.
//
//   NODE_PATH=<global node_modules> node tools/fold.mjs
//   NODE_PATH=... node tools/fold.mjs --dir projects/season1/still-dark
//
// For each viewport it reports, per stop of the run, the top and bottom of every element
// the head must not lose, and whether it is fully inside the viewport — first at scroll 0,
// then scrolled to the bottom of the head's own section, which is where a phone reader is
// while the reserved space fills. Exits 1 if the controls or the state line leave the
// viewport at any stop at a viewport narrower than 481 px; prints and exits 0 otherwise.
// Dependencies, named honestly: node >= 18 and playwright (chromium), the house's check on
// itself, not a dependency of the work — index.html ships with no runtime dependency at all.
import { createRequire } from "node:module";
import { join, resolve } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const argv = process.argv.slice(2);
const dirArg = argv.find((a) => a.startsWith("--dir="));
const dir = resolve(dirArg ? dirArg.slice("--dir=".length) : "projects/season1/still-dark");
const url = "file://" + join(dir, "index.html");

// The two the staging law names, plus the phone the defect was measured on.
const VIEWPORTS = [
  { w: 390, h: 844, name: "phone 390×844" },
  { w: 1400, h: 900, name: "wide 1400×900" },
];

// Everything the head must be able to lose sight of, and the three it must not.
const WATCHED = [
  { sel: "#sd-arrive-count", label: "the figure", must: false },
  { sel: "#sd-arrive-head-since", label: "the hole's heading", must: false },
  { sel: "#sd-arrive-ladder", label: "the controls", must: true },
  { sel: "#sd-arrive-state", label: "the run's line", must: true },
];

const browser = await chromium.launch();
let failures = 0;

for (const vp of VIEWPORTS) {
  const ctx = await browser.newContext({
    viewport: { width: vp.w, height: vp.h },
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(url);
  await page.waitForTimeout(400);
  const stops = await page.$$eval("#sd-arrive-ladder button:not(.sd-arrive-replay)", (b) => b.length);
  console.log(`\n${vp.name} — ${stops} stops`);

  for (const where of ["top", "head-bottom"]) {
    for (let i = 0; i < stops; i++) {
      await page.$$eval(
        "#sd-arrive-ladder button:not(.sd-arrive-replay)",
        (bs, k) => bs[k].click(),
        i,
      );
      if (where === "top") await page.evaluate(() => window.scrollTo(0, 0));
      else {
        await page.evaluate(() => {
          const s = document.getElementById("sd-arrive");
          window.scrollTo(0, s.getBoundingClientRect().bottom + window.scrollY - window.innerHeight);
        });
      }
      await page.waitForTimeout(60);
      const seen = await page.evaluate((watched) => {
        return watched.map((w) => {
          const el = document.querySelector(w.sel);
          const r = el.getBoundingClientRect();
          return {
            label: w.label,
            must: w.must,
            top: Math.round(r.top),
            bottom: Math.round(r.bottom),
            inside: r.top >= 0 && r.bottom <= window.innerHeight,
          };
        });
      }, WATCHED);
      const line = seen
        .map((s) => `${s.label} ${s.top}–${s.bottom}${s.inside ? "" : " ✗OFF"}`)
        .join(" · ");
      console.log(`  scroll:${where.padEnd(11)} stop ${i}: ${line}`);
      for (const s of seen) {
        if (s.must && !s.inside && vp.w <= 480) failures++;
      }
    }
  }
  await ctx.close();
}

await browser.close();
if (failures) {
  console.log(`\nFOLD: ${failures} loss(es) of a must-hold element on a viewport ≤ 480 px`);
  process.exit(1);
}
console.log("\nFOLD: the controls and the run's line are inside the viewport at every stop");
