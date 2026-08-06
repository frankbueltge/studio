// STILL DARK — render the built page and extract what a reader actually gets.
//
// Why this exists: on 2026-08-05 (session 67) a builder, a critic and a verifier all
// passed an object nobody in this house had rendered — the vessel names were clipped off
// the screen. The check had been run against a description instead of the thing. This
// script makes that failure structurally harder: every state that goes to a panel is
// extracted BY the browser from the built file, and both legibility widths are written to
// disk as images the conductor opens and looks at.
//
//   node render.mjs            (from this directory)
//   NODE_PATH=<global node_modules> node render.mjs     (if playwright is installed globally)
//
// Writes, beside index.html:
//   STATE-1.txt   the page as it loads, in DOM/screen-reader order — the panel's material
//   STATE-2.txt   the same after the one control is moved one notch (for verification only)
//   render-1400.png, render-900.png   the two widths the staging law names
//
// Dependencies, named honestly: node >= 18 and playwright (chromium). Neither is a
// dependency of the WORK — index.html is a single self-contained file with no runtime
// dependency at all. They are the house's own check on itself.

import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { writeFileSync } from "node:fs";

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

// innerText of the work's root: the browser's own rendering of what is readable,
// with hidden subtrees absent rather than merely invisible.
//
// The one thing innerText cannot carry is the number field: an <input> has a value, not
// text, and at state 1 that value is empty. So before reading, the field's own string —
// its value if the reader has typed one, otherwise its placeholder — is echoed into a
// span at exactly the position the field occupies, and removed again afterwards. The
// string is the page's own; no word of the house's is added by this script, so the
// panel's void clause cannot fire on the extraction.
const readText = (page) => page.evaluate(() => {
  const root = document.querySelector(".sd-root");
  const field = document.getElementById("sd-num");
  let echo = null;
  if (field) {
    echo = document.createElement("span");
    echo.textContent = field.value || field.getAttribute("placeholder") || "";
    field.after(echo);
  }
  const text = root.innerText.replace(/\n{3,}/g, "\n\n").trim();
  if (echo) echo.remove();
  return text;
});

// state 1 — as it loads, untouched
{
  const { ctx, page } = await open(1400, 900);
  writeFileSync(join(here, "STATE-1.txt"), (await readText(page)) + "\n");
  await page.screenshot({ path: join(here, "render-1400.png"), fullPage: true });

  // state 2 — the act performed, the way a hand performs it: a number typed into the
  // field and the button pressed. The figure used here is 11, deterministically: it is
  // the count visible on state 1 and therefore the answer the screen invites. It is this
  // script's choice, not the work's — the work accepts any number of up to four digits.
  await page.locator("#sd-num").fill("11");
  await page.locator("#sd-commit").click();
  await page.waitForSelector("#sd-last:not(:empty)");
  writeFileSync(join(here, "STATE-2.txt"), (await readText(page)) + "\n");
  await page.screenshot({ path: join(here, "render-1400-state2.png"), fullPage: true });
  await ctx.close();
}

// the narrow width the legibility law names
{
  const { ctx, page } = await open(900, 900);
  await page.screenshot({ path: join(here, "render-900.png"), fullPage: true });
  await ctx.close();
}

await browser.close();
console.log("STATE-1.txt, STATE-2.txt, render-1400.png, render-900.png written");
