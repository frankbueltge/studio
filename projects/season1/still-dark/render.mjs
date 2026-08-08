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

const here = dirname(fileURLToPath(import.meta.url));
const page_url = "file://" + join(here, "index.html");

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
  return { ctx, page };
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
  writeFileSync(join(here, "STATE-1.txt"), (await readText(page)) + "\n");
  await page.screenshot({ path: join(here, "render-1400.png"), fullPage: true });
  await ctx.close();
}

// the narrow width the legibility law names
{
  const { ctx, page } = await open(900, 900);
  await page.screenshot({ path: join(here, "render-900.png"), fullPage: true });
  await ctx.close();
}

await browser.close();

// the provenance sidecar: what these outputs were rendered FROM, and what they are.
const sha = (p) => createHash("sha256").update(readFileSync(p)).digest("hex");
const outputs = ["STATE-1.txt", "render-1400.png", "render-900.png"];
const manifest = {
  rendered_from: "index.html",
  index_sha256: sha(join(here, "index.html")),
  outputs: Object.fromEntries(outputs.map((f) => [f, sha(join(here, f))])),
  note:
    "Written by render.mjs. Checked by tools/renders.py, which recomputes every hash " +
    "here from the committed files and exits non-zero if any render was made from a " +
    "different index.html than the one committed beside it.",
};
writeFileSync(join(here, "RENDERS.json"), JSON.stringify(manifest, null, 2) + "\n");

console.log("STATE-1.txt, render-1400.png, render-900.png, RENDERS.json written");
