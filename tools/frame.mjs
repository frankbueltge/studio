// frame.mjs — can one screen hold the figure and the controls that drive it?
//
// Why this exists. Owed item (y) has been measured for four sessions in a number no
// committed instrument produced: *figure-top to controls-bottom at 390×844*, taken by hand
// with a throwaway script each night. `PROJECT.md` printed 813 · 1,065 · 964 in session 85
// and 1,036 · 1,094 in session 86, and had to say in the record that the two series are not
// comparable, because nobody could re-run the first. A measurement whose instrument is
// unstated is banked failure — this house has one for it (`tools/record_words.py`) — and
// this file ends the same defect for the fold.
//
//   NODE_PATH=<global node_modules> node tools/frame.mjs
//   NODE_PATH=... node tools/frame.mjs --dir=projects/season1/still-dark
//
// To measure the committed page as a control, extract it and point `--dir` at it:
//
//   mkdir -p /tmp/sd && git show HEAD:projects/season1/still-dark/index.html > /tmp/sd/index.html
//   NODE_PATH=... node tools/frame.mjs --dir=/tmp/sd
//
// A `--ref=HEAD` flag stood in this header for one session and was never implemented: the
// tool ignored it and measured the working tree, so an instrument written to end the defect
// *a measurement whose instrument is unstated* would have reported the object under test as
// its own control. Found by `DRAMATURG-87.md` §2 on the night it was committed, before any
// session had quoted a number from it. The flag is not added; the two lines above do the
// job with `git` doing the git.
//
// WHAT IT MEASURES, and why it is not `tools/fold.mjs`. `fold.mjs` asks whether the
// controls and the run's line are inside the viewport at nine scroll positions of every
// stop. That test can be passed only by a bar pinned to the viewport, and a pinned bar over
// a head twice the viewport's height stands on the material at some scroll position — which
// is how session 84's repair passed `fold.mjs` while painting out ten of nineteen name
// chips. Its count is kept and still printed by this house, red, because an instrument is
// not retired for being hard to pass.
//
// This one asks the question the staging voice actually asked: **is there one frame in
// which a reader sees the figure and the buttons together** — that is, is the distance from
// the top of the figure to the bottom of the controls at most the viewport's height. It
// needs no scroll walk and no pinning, it is a property of the head's own length, and it is
// the number the record has been quoting. It also prints the budget: every part of the head
// between those two points, with its height, so a session can see what it is spending the
// frame on before it argues about prose.
//
// Dependencies, named honestly: node >= 18 and playwright (chromium) — the house's check on
// itself, not a dependency of the work. `index.html` ships with no runtime dependency.
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

const VIEWPORTS = [
  { w: 390, h: 844, name: "phone 390×844" },
  { w: 1400, h: 900, name: "wide 1400×900" },
];

// The two ends of the frame, and everything the head puts between them. The parts are named
// as a reader meets them, not as the DOM holds them.
const TOP = "#sd-arrive-count";
const BOTTOM = "#sd-arrive-controls";
// THE SECOND SPAN WAS STRUCK IN SESSION 89, by order of `DRAMATURG-89.md` cut 1, and the
// reason is the only reason an instrument should ever be restated: THE ITEM WAS THE MISTAKE.
//
// Sessions 87 and 88 owed an item stated as *figure-top to hole-BOTTOM at 390×844*, and this
// file measured it from 88: 867 px, then 786 — green for the first time in the work's life,
// bought with 157 px of staging. It survived one night. The ninth list added two ship names,
// the hole grew two rows, and the span read 849 of 844. Rebuilt at n chips it is 23 px per
// row, one row per two names: 26 chips → over by 28, 28 → over by 51, 32 → over by 97.
//
// The hole is this work's SUBJECT — the part of a finished day nobody could have had on it —
// and it grows every night the work succeeds at what it does. An item whose far end is the
// subject therefore goes RED ON SUCCESS, and a house paying it in prose pays 23 px a night
// forever. That is not a frame test; it is a tax on the work's own accumulation.
//
// WHAT REPLACES IT is the bounded fact the struck span was a proxy for, and it is bounded
// because its far end is the VIEWPORT and not the hole: with the whole figure on screen, how
// much of the hole shares the frame with it. Measured across the scroll range at every stop,
// reported at its best position, floored at session 89's own reading — 268 px and 22 of 24
// chips at 390×844. The floor is a number a stranger re-runs, and it cannot drift upward as
// the hole grows: more chips do not move the figure, and the viewport does not change size.
//
// THE SENTENCE ABOVE WAS REFUTED BY THE RECORD IN SESSION 92, and it stands unedited with the
// refutation under it. More chips do not move the figure — true — but the HEADING over the
// hole is generated from the same material, and on the night the tenth list arrived it gained
// one wrapped line at 390 px and pushed the hole 15 px down: the span read 266 against a floor
// of 268 — UNDER, without a single line of layout changing. The floor is
// not hostage only to the chips; it is hostage to every generated string above the hole. What
// this file measures was right and why it thought it was safe was wrong.
//
// Neither span changes this file's exit contract: the frame test still decides the exit code.
// An instrument that failed the build on a measurement no gate has ruled on would be
// legislating — and the gate that ruled on this one ordered it restated, not enforced.
const HOLE_BOTTOM = "#sd-arrive-names-since";
const PARTS = [
  [".sd-arrive-headline", "the frame: both figures and their clauses"],
  ["#sd-arrive-constant", "what the ends of the figure can do"],
  ["#sd-arrive-head-then", "the day's own heading"],
  ["#sd-arrive-names-then", "the names the day itself printed"],
  ["#sd-arrive-head-since", "the hole's heading"],
  ["#sd-arrive-names-since", "the names only later lists gave"],
  ["#sd-arrive-hedge", "the caveat on the names"],
  ["#sd-arrive-controls", "the controls and the run's line"],
];

const browser = await chromium.launch();
let over = 0;

for (const vp of VIEWPORTS) {
  const ctx = await browser.newContext({
    viewport: { width: vp.w, height: vp.h },
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(url);
  await page.waitForTimeout(400);
  const stops = await page.$$eval(
    "#sd-arrive-ladder button:not(.sd-arrive-replay)",
    (b) => b.length,
  );

  // Every stop, because the head reserves its heights from the tallest stop and a
  // reservation that failed would show up here as a frame that changes under the run.
  const frames = [];
  const holes = [];
  for (let i = 0; i < stops; i++) {
    await page.$$eval(
      "#sd-arrive-ladder button:not(.sd-arrive-replay)",
      (bs, k) => bs[k].click(),
      i,
    );
    await page.waitForTimeout(40);
    const span = async (t, b) =>
      await page.evaluate(
        ([t2, b2]) => {
          const el = document.querySelector(b2);
          if (!el) return null;
          const top = document.querySelector(t2).getBoundingClientRect().top;
          const bot = el.getBoundingClientRect().bottom;
          return Math.round(bot - top);
        },
        [t, b],
      );
    frames.push(await span(TOP, BOTTOM));
    // THE SHARED FRAME, at this stop. Scan the scroll range; keep only positions where the
    // WHOLE figure is on screen; among those, take the one showing most of the hole. Chips
    // count only when a chip is wholly inside the viewport — a name cut in half is not a
    // name a visitor read.
    const shared = await page.evaluate(
      ([topSel, holeSel]) => {
        const fig = document.querySelector(topSel);
        const hole = document.querySelector(holeSel);
        if (!fig || !hole) return null;
        const chips = [...hole.querySelectorAll("li")];
        const vh = window.innerHeight;
        const range = Math.max(
          0,
          document.documentElement.scrollHeight - vh,
        );
        const y0 = window.scrollY;
        let best = { px: -1, chips: 0, scrollY: 0 };
        for (let k = 0; k <= 240; k++) {
          window.scrollTo(0, Math.round((range * k) / 240));
          const f = fig.getBoundingClientRect();
          if (f.top < 0 || f.bottom > vh) continue;
          const h = hole.getBoundingClientRect();
          const px = Math.round(
            Math.max(0, Math.min(h.bottom, vh) - Math.max(h.top, 0)),
          );
          const seen = chips.filter((c) => {
            const r = c.getBoundingClientRect();
            return r.top >= 0 && r.bottom <= vh;
          }).length;
          if (px > best.px) best = { px, chips: seen, scrollY: window.scrollY };
        }
        window.scrollTo(0, y0);
        return best.px < 0 ? null : { ...best, of: chips.length };
      },
      [TOP, HOLE_BOTTOM],
    );
    if (shared) holes.push(shared);
  }
  const lo = Math.min(...frames);
  const hi = Math.max(...frames);
  const verdict = hi <= vp.h ? "HOLDS" : `OVER by ${hi - vp.h}`;
  console.log(
    `\n${vp.name} — figure-top to controls-bottom: ${lo === hi ? hi : `${lo}–${hi}`} px ` +
      `of ${vp.h} — ${verdict}`,
  );
  if (hi > vp.h && vp.w <= 480) over = hi - vp.h;

  // The other end of the piece's argument, asked so that the answer is bounded: with the
  // whole figure on screen, how much of the hole is on screen with it. Reported, never
  // enforced — see the note at HOLE_BOTTOM. The floor is session 89's own reading and only
  // the phone carries it; the wide viewport holds the whole hole and has nothing to floor.
  if (holes.length) {
    // The px is the reserved height and is the same at every stop; what grows is the chip
    // count, and it grows to its largest at the LAST stop — the state the run rests on and
    // the one the next list makes bigger. So the floor is read there. The earlier stops are
    // reported as a range so a reservation that failed would show up as a moving number.
    const live = holes[holes.length - 1];
    const pxLo = Math.min(...holes.map((h) => h.px));
    const pxHi = Math.max(...holes.map((h) => h.px));
    const floorPx = vp.w <= 480 ? 268 : null;
    const floorChips = vp.w <= 480 ? 22 : null;
    const under =
      floorPx !== null && (live.px < floorPx || live.chips < floorChips);
    console.log(
      `  the hole sharing a frame with the whole figure: ` +
        `${pxLo === pxHi ? pxHi : `${pxLo}–${pxHi}`} px, ` +
        `${live.chips} of ${live.of} chips at the last stop` +
        (floorPx === null
          ? ""
          : ` — floor ${floorPx} px / ${floorChips} chips — ${under ? "UNDER" : "HOLDS"}`),
    );
  }

  // THE BUDGET, AND WHICH PARTS THE FRAME ACTUALLY CONTAINS. The first version of this
  // report assumed every part listed lies between the two ends and subtracted their sum
  // from the span — which was true of the head it was written against and stopped being
  // true the moment session 87 moved the controls above the material at phone widths: it
  // printed a space of −601 px, a number that describes nothing. A part is now placed by
  // measurement, not by assumption, and the ones outside the frame are named as outside.
  const parts = await page.evaluate(
    ([sel, t, b]) => {
      const top = document.querySelector(t).getBoundingClientRect().top;
      const bot = document.querySelector(b).getBoundingClientRect().bottom;
      const lo = Math.min(top, bot);
      const hi2 = Math.max(top, bot);
      return sel.map(([s, label]) => {
        const el = document.querySelector(s);
        if (!el) return { label, h: null, inside: false };
        const r = el.getBoundingClientRect();
        // Fully inside, not merely touching: a paragraph whose first pixel sits under the
        // controls' last one is below the frame, and counting it as contained is how the
        // budget printed a negative space the first time this was asked.
        return {
          label,
          h: Math.round(r.height),
          inside: r.top >= lo - 2 && r.bottom <= hi2 + 2,
        };
      });
    },
    [PARTS, TOP, BOTTOM],
  );
  const sum = parts.filter((p) => p.inside).reduce((a, p) => a + (p.h || 0), 0);
  for (const p of parts) {
    console.log(
      `  ${String(p.h ?? "—").padStart(5)} px  ${p.label}${p.inside ? "" : "   — outside the frame at this width"}`,
    );
  }
  console.log(`  ${String(hi - sum).padStart(5)} px  the space between them`);
  await ctx.close();
}

await browser.close();
if (over) {
  console.log(
    `\nFRAME: the figure and the controls do not fit one phone screen — over by ${over} px`,
  );
  process.exit(1);
}
console.log("\nFRAME: the figure and the controls fit one screen at every stop");
