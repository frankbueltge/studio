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
// the head must not lose, and whether it is fully inside the viewport. Exits 1 if the
// controls or the state line leave the viewport at any stop at a viewport narrower than
// 481 px; prints and exits 0 otherwise.
//
// REBUILT THE SAME NIGHT IT WAS WRITTEN, because it passed the defect it was built for.
// Session 84 answered item (y) by pinning the controls and the live line to the bottom of a
// phone viewport, and they arrived on screen by being painted over the reserved space the
// whole head exists to reveal — at stop 6 and scroll 0, ten of nineteen name chips painted
// out. This instrument certified that green. Two reasons, and both were holes in the
// instrument and not bad luck: it watched only the elements it was told to KEEP ON SCREEN,
// never the material they might land on, and it sampled two scroll positions out of a head
// that scrolls through more than a thousand pixels. So it now (1) carries a WATCH list of
// material that must not be covered, and asserts by hit-testing that no must-hold element
// is painted over it, and (2) walks the head's whole scroll range in steps rather than
// visiting its ends. **An instrument that has never failed is not an instrument** — this one
// is checked against the withdrawn band, which it now fails, and the check is in the README.
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

  // The head's own scroll range, walked in steps. Two positions were not enough: the
  // verifying pass of session 84 found the controls leaving the viewport from scrollY 1027
  // on a head running to y 1438, a band this instrument never visited.
  const range = await page.evaluate(() => {
    const s = document.getElementById("sd-arrive");
    return Math.max(0, Math.round(s.getBoundingClientRect().bottom + window.scrollY - window.innerHeight));
  });
  const positions = [];
  for (let k = 0; k <= 8; k++) positions.push(Math.round((range * k) / 8));

  for (let i = 0; i < stops; i++) {
    await page.$$eval(
      "#sd-arrive-ladder button:not(.sd-arrive-replay)",
      (bs, k) => bs[k].click(),
      i,
    );
    for (const y of positions) {
      await page.evaluate((yy) => window.scrollTo(0, yy), y);
      await page.waitForTimeout(40);
      const seen = await page.evaluate((watched) => {
        const out = watched.map((w) => {
          const el = document.querySelector(w.sel);
          const r = el.getBoundingClientRect();
          return {
            label: w.label,
            must: w.must,
            sel: w.sel,
            top: Math.round(r.top),
            bottom: Math.round(r.bottom),
            inside: r.top >= 0 && r.bottom <= window.innerHeight,
          };
        });
        // OCCLUSION. Every chip of material is hit-tested at its own centre; if what the
        // browser returns there belongs to a must-hold element, that element is standing on
        // the material. This is the test that was missing, and it is the one that matters:
        // an element brought on screen by covering what it explains has not been repaired.
        const musts = watched.filter((w) => w.must).map((w) => document.querySelector(w.sel));
        const chips = [...document.querySelectorAll("#sd-arrive-names-since li, #sd-arrive-names-then li")];
        let covered = 0;
        for (const c of chips) {
          const q = c.getBoundingClientRect();
          if (q.bottom < 0 || q.top > window.innerHeight) continue;
          const hit = document.elementFromPoint(q.left + q.width / 2, q.top + q.height / 2);
          if (hit && musts.some((m) => m && (m === hit || m.contains(hit)))) covered++;
        }
        return { out, covered, chips: chips.length };
      }, WATCHED);
      const line = seen.out
        .map((s) => `${s.label} ${s.top}–${s.bottom}${s.inside ? "" : " ✗OFF"}`)
        .join(" · ");
      const occ = seen.covered ? `  ✗COVERS ${seen.covered} chip(s)` : "";
      console.log(`  y=${String(y).padStart(4)} stop ${i}: ${line}${occ}`);
      for (const s of seen.out) {
        if (s.must && !s.inside && vp.w <= 480) failures++;
      }
      if (seen.covered && vp.w <= 480) failures += seen.covered;
    }
  }
  await ctx.close();
}

await browser.close();
if (failures) {
  console.log(`\nFOLD: ${failures} failure(s) — a must-hold element off the viewport, or standing on the material, at ≤ 480 px`);
  process.exit(1);
}
console.log("\nFOLD: the controls and the run's line are inside the viewport at every stop");
