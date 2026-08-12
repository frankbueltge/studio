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
// THE SECOND SPAN, added in session 88 for the same reason the first one exists. Sessions
// 87 and 88 both owed an item stated as *figure-top to hole-bottom at 390×844* — whether one
// screen can hold the falling number and the space that fills under it, which is the piece's
// own argument in one frame — and both quoted it from a number nobody could re-run. It is
// measured here, at every stop, beside the first. It does NOT change this file's exit
// contract: the frame test still decides the exit code, and this span is reported red or
// green and left to the session to argue. An instrument that failed the build on a
// measurement no gate has ruled on would be legislating.
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
    const h = await span(TOP, HOLE_BOTTOM);
    if (h !== null) holes.push(h);
  }
  const lo = Math.min(...frames);
  const hi = Math.max(...frames);
  const verdict = hi <= vp.h ? "HOLDS" : `OVER by ${hi - vp.h}`;
  console.log(
    `\n${vp.name} — figure-top to controls-bottom: ${lo === hi ? hi : `${lo}–${hi}`} px ` +
      `of ${vp.h} — ${verdict}`,
  );
  if (hi > vp.h && vp.w <= 480) over = hi - vp.h;

  // The same question asked of the other end of the piece's argument: the falling figure and
  // the space that fills under it. Reported, never enforced — see the note at HOLE_BOTTOM.
  if (holes.length) {
    const hLo = Math.min(...holes);
    const hHi = Math.max(...holes);
    console.log(
      `  figure-top to hole-bottom: ${hLo === hHi ? hHi : `${hLo}–${hHi}`} px ` +
        `of ${vp.h} — ${hHi <= vp.h ? "HOLDS" : `OVER by ${hHi - vp.h}`}`,
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
