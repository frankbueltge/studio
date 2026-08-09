// STILL DARK — render the built page and extract what a reader actually gets.
//
// Why this exists: on 2026-08-05 (session 67) a builder, a critic and a verifier all
// passed an object nobody in this house had rendered — the vessel names were clipped off
// the screen. The check had been run against a description instead of the thing. This
// script makes that failure structurally harder: what goes to a panel is extracted BY the
// browser from the built file, and both legibility widths are written to disk as images
// the conductor opens and looks at.
//
// Since 2026-08-06 (session 71) the work has ONE state. The reader act is gone, the
// second state with it, and so is this script's typed `11`.
//
//   node render.mjs            (from this directory)
//   NODE_PATH=<global node_modules> node render.mjs     (if playwright is installed globally)
//
// Writes, beside index.html:
//   STATE-1.txt   the page in DOM/screen-reader order — the panel's material
//   render-1400.png, render-900.png   the two widths the staging law names
//
// Dependencies, named honestly: node >= 18 and playwright (chromium). Neither is a
// dependency of the WORK — index.html is a single self-contained file with no runtime
// dependency at all. They are the house's own check on itself.

// Since 2026-08-08 (session 76) it also writes RENDERS.json: the sha256 of the index.html
// these outputs were made FROM, beside the sha256 of each output. Owed item (i): the renders
// are the only sighted material a panel ever receives, and nothing checked that they belonged
// to the committed page. In session 75 the face moved and the renders were remade by hand;
// had that hand forgotten, the next panel would have been shown a superseded figure and no
// instrument in this house could have said so. `python3 tools/renders.py` is that instrument.
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { writeFileSync, readFileSync } from "node:fs";
import { createHash } from "node:crypto";

// CommonJS resolution, so a globally installed playwright on NODE_PATH is found too.
const { chromium } = createRequire(import.meta.url)("playwright");

// Since 2026-08-08 (session 77) it takes an optional directory, so an A/B arm staged
// beside the work can be rendered by the SAME script that renders the work — a control
// rendered by a second, hand-adjusted copy of this file would differ from its arm in
// whatever that copy got wrong. Outputs are always written next to the index.html read.
//
//   node render.mjs ../staging-77/control
// Since 2026-08-09 (session 79) it takes an optional `--stop-after=<css selector>`, and
// that flag is an instrument, not a staging preference. Banked failure 18: every
// first-encounter question this house has ever asked told a reader to stop somewhere and
// then handed them the whole page, and session 78 proved the instruction is not obeyed —
// both readers of a lede containing no mechanism word reported the mechanism. A stopping
// point a reader is asked to honour is not a stopping point; it has to be a property of
// the material. With the flag, everything after the named element is REMOVED from the
// rendered document before the screenshot and the extraction are taken, so the material
// itself ends there and no instruction is needed. The page is loaded and built first: the
// truncation happens to the SAME DOM the work produces, not to a second, hand-cut copy of
// its markup.
//
//   node render.mjs ../staging-79/stop --stop-after=#sd-lede
//
// Since 2026-08-09 (session 80) it takes an optional `--at-step=<n>`, and that flag
// exists because the page's head now RUNS. A screenshot of a moving element is one
// frame of it, and a frame nobody chose is whatever the clock happened to be showing
// when the shutter fell — which is the same defect as a number reaching a face out of a
// head, with a camera instead of a hand. The flag drives the arrival to a named stop
// through the page's own `window.__sdArrive.show`, so the frame is chosen, stated in
// RENDERS.json, and reproducible. Without the flag nothing is driven: the render
// context asks for reduced motion, the page honours that by showing its last stop, and
// the committed outputs are that state.
//
//   node render.mjs ../staging-80/head --stop-after=#sd-arrive --at-step=0
const here = dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const dirArg = argv.find((a) => !a.startsWith("--"));
const stopArg = argv.find((a) => a.startsWith("--stop-after="));
const stopAfter = stopArg ? stopArg.slice("--stop-after=".length) : null;
const stepArg = argv.find((a) => a.startsWith("--at-step="));
const atStep = stepArg ? Number(stepArg.slice("--at-step=".length)) : null;
if (stepArg && !Number.isInteger(atStep)) {
  console.error(`--at-step must be an integer, got ${stepArg.slice("--at-step=".length)}`);
  process.exit(1);
}
const target = dirArg ? join(here, dirArg) : here;
const page_url = "file://" + join(target, "index.html");

const browser = await chromium.launch();

async function open(width, height) {
  const ctx = await browser.newContext({
    viewport: { width, height },
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await ctx.newPage();
  await page.goto(page_url);
  await page.waitForLoadState("load");
  if (atStep !== null) await drive(page, atStep);
  if (stopAfter) await truncate(page, stopAfter);
  return { ctx, page };
}

// Drive the running head to a chosen stop. Exits non-zero rather than photographing an
// undriven page: a `--at-step` that silently did nothing would put a frame in front of a
// panel under a label naming a different one, and this house has already banked a night
// of readers shown material that was not what its memo said it was.
async function drive(page, n) {
  const result = await page.evaluate((step) => {
    const a = window.__sdArrive;
    if (!a) return "no running head on this page";
    if (step < 0 || step >= a.stops) return `step ${step} is outside 0..${a.stops - 1}`;
    a.show(step);
    return null;
  }, n);
  if (result) {
    console.error(`--at-step=${n}: ${result}`);
    process.exit(1);
  }
}

// Everything after the named element goes, at every level between it and the work's
// root, so what remains is the material a reader receives and nothing follows it. Exits
// non-zero rather than rendering a whole page if the selector matches nothing: a stop
// that silently did not happen would be banked failure 18 a second time.
async function truncate(page, sel) {
  const ok = await page.evaluate((s) => {
    const root = document.querySelector(".sd-root");
    const el = root && root.querySelector(s);
    if (!el) return false;
    for (let n = el; n && n !== root; n = n.parentElement) {
      while (n.nextElementSibling) n.nextElementSibling.remove();
    }
    return true;
  }, sel);
  if (!ok) {
    console.error(`--stop-after=${sel} matched nothing inside .sd-root`);
    process.exit(1);
  }
}

// innerText of the work's root: the browser's own rendering of what is readable.
// No word of this house's is added by this script — the panel's void clause could
// otherwise fire on the extraction rather than on the work.
const readText = (page) => page.evaluate(() => {
  const root = document.querySelector(".sd-root");
  return root.innerText.replace(/\n{3,}/g, "\n\n").trim();
});

{
  const { ctx, page } = await open(1400, 900);
  writeFileSync(join(target, "STATE-1.txt"), (await readText(page)) + "\n");
  await page.screenshot({ path: join(target, "render-1400.png"), fullPage: true });
  await ctx.close();
}

// the narrow width the legibility law names
{
  const { ctx, page } = await open(900, 900);
  await page.screenshot({ path: join(target, "render-900.png"), fullPage: true });
  await ctx.close();
}

await browser.close();

// the provenance sidecar: what these outputs were rendered FROM, and what they are.
const sha = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const outputs = ["STATE-1.txt", "render-1400.png", "render-900.png"];
const manifest = {
  rendered_from: "index.html",
  stopped_after: stopAfter,
  at_step: atStep,
  index_sha256: sha(join(target, "index.html")),
  outputs: Object.fromEntries(outputs.map((f) => [f, sha(join(target, f))])),
  note:
    "Written by render.mjs. Checked by tools/renders.py, which recomputes every hash " +
    "here from the committed files and exits non-zero if any render was made from a " +
    "different index.html than the one committed beside it.",
};
writeFileSync(join(target, "RENDERS.json"), JSON.stringify(manifest, null, 2) + "\n");

console.log("STATE-1.txt, render-1400.png, render-900.png, RENDERS.json written");
