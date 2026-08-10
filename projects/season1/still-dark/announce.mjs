// STILL DARK — what the run announces, and to whom.
//
// Why this exists: session 82 owed item (t) — the largest thing this project owed — was
// that `[aria-live],[role=status],[role=alert]` returned 0 on the committed page, so a
// visitor using a screen reader and no reduced-motion preference had the figure, the
// headings and the name list rewritten six times behind their cursor with nothing
// announced. That defect was found by a voice and confirmed by hand. This house does not
// take a defect on a voice's word (banked failure 23) and it does not take a REPAIR on its
// own word either: what the repair is worth is how many announcements a run actually makes,
// what they say, and whether a stop pressed inside the first beat is now audible instead of
// silent. So the repair ships with the instrument that measures it.
//
//   NODE_PATH=<global node_modules> node announce.mjs
//
// WHAT ITS NUMBERS ARE, EXACTLY. A MutationObserver delivers its records in a microtask
// and this file reads the element's text at delivery, so mutations landing in one tick
// collapse into one entry: the counts below are DISTINCT STATES OBSERVED, not raw DOM
// writes. That is the right count for the question being asked — a reader is exposed to
// states, not to writes — and the page's own load-time measuring loop, which drives every
// stop once to reserve its height, therefore does not appear as seven rewrites. Said here
// rather than left for someone to discover in the number.
//
// It drives the built page in a browser and reports, all measured and none asserted:
//   1. the number of live regions on the page
//   2. every announcement an untouched run makes, with the millisecond it lands on
//   3. every mutation of the figure, with its millisecond — so announcements can be
//      counted AGAINST rewrites rather than in the abstract
//   4. the same page with a stop pressed at t = 3 s: what the run does and what it says
//   5. the resting (reduced-motion) page: what stands there instead
//
// Dependencies, named honestly: node >= 18 and playwright (chromium), neither of which is
// a dependency of the WORK — index.html is one self-contained file with no runtime
// dependency at all. This is the house's own check on itself.
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
import path from "node:path";

const require = createRequire(import.meta.url);
let chromium;
try {
  ({ chromium } = require("playwright"));
} catch {
  console.error("playwright not found — try NODE_PATH=<global node_modules> node announce.mjs");
  process.exit(2);
}

const FILE = pathToFileURL(path.resolve("index.html")).href;
const CLICK_AT_MS = 3000;
const WATCH_MS = 30000;

// The observer is installed before the page's own script runs, so nothing it records is
// reconstructed after the fact: every entry below is a mutation this browser saw happen.
const INSTALL = () => {
  window.__log = { announcements: [], figure: [], t0: performance.now(), loaded: false };
  window.addEventListener("load", () => { window.__log.loaded = true; });
  const at = () => Math.round(performance.now() - window.__log.t0);
  const obs = new MutationObserver((records) => {
    for (const r of records) {
      const el = r.target.nodeType === 1 ? r.target : r.target.parentElement;
      if (!el) continue;
      const live = el.closest("[aria-live],[role=status],[role=alert]");
      if (live) {
        const text = live.textContent.trim();
        const last = window.__log.announcements[window.__log.announcements.length - 1];
        // A live region does NOT announce the content it is born with — only what changes
        // in it after the page has settled. So a write is logged as SPOKEN only if the
        // region already held something (or was already empty on screen) at the load
        // event; a write that lands before `load` is logged as `mute`. The first version
        // of this file logged every write and called them all announcements, and reported
        // a repair working that a screen reader would never have heard. Banked failure 32.
        if (!last || last.text !== text) {
          window.__log.announcements.push({
            ms: at(), text, spoken: !!window.__log.loaded && text !== "",
          });
        }
      }
      const fig = el.closest("#sd-arrive-count");
      if (fig) {
        const text = fig.textContent.trim();
        const last = window.__log.figure[window.__log.figure.length - 1];
        if (!last || last.text !== text) window.__log.figure.push({ ms: at(), text });
      }
    }
  });
  // `document` and not `document.documentElement`: this script is installed before the
  // page's own scripts, at a moment when the document exists and its root element does
  // not. The first version of this file observed the root, threw on null, and reported a
  // page that announced nothing and rewrote nothing — an instrument that returned the
  // very finding it was built to test. Banked as failure 30.
  obs.observe(document, { subtree: true, childList: true, characterData: true });
};

async function openPage(browser, reduced) {
  const ctx = await browser.newContext({
    viewport: { width: 1400, height: 1400 },
    reducedMotion: reduced ? "reduce" : "no-preference",
  });
  const page = await ctx.newPage();
  await page.addInitScript(INSTALL);
  await page.goto(FILE);
  await page.waitForLoadState("load");
  return { ctx, page };
}

const browser = await chromium.launch();

// ── 1 + 2 + 3 ── the untouched run ────────────────────────────────────────────────────
{
  const { ctx, page } = await openPage(browser, false);
  const regions = await page.evaluate(() =>
    document.querySelectorAll("[aria-live],[role=status],[role=alert]").length);
  await page.waitForTimeout(WATCH_MS);
  const log = await page.evaluate(() => window.__log);
  console.log(`LIVE REGIONS ......... ${regions}`);
  console.log(`WRITES TO THE REGION . ${log.announcements.length} in ${WATCH_MS / 1000} s`);
  for (const a of log.announcements) {
    console.log(`  ${String(a.ms).padStart(6)} ms  [${a.spoken ? "spoken" : "mute  "}]  ${a.text}`);
  }
  console.log(`  SPOKEN ............. ${log.announcements.filter((a) => a.spoken).length}`);
  console.log(`FIGURE REWRITES ...... ${log.figure.length}`);
  for (const f of log.figure) console.log(`  ${String(f.ms).padStart(6)} ms  ${f.text}`);
  await ctx.close();
}

// ── 4 ── a stop pressed inside the first beat, which used to kill the run in silence ──
{
  const { ctx, page } = await openPage(browser, false);
  await page.waitForTimeout(CLICK_AT_MS);
  const buttons = page.locator(".sd-arrive-ladder button");
  const label = await buttons.nth(2).textContent();
  await buttons.nth(2).click();
  const rightAfter = (await page.locator("#sd-arrive-state").textContent()).trim();
  await page.waitForTimeout(WATCH_MS - CLICK_AT_MS);
  const log = await page.evaluate(() => window.__log);
  const figureAtEnd = (await page.locator("#sd-arrive-count").textContent()).trim();
  console.log(`\nCLICKED "${label.trim()}" AT ${CLICK_AT_MS} ms`);
  console.log(`  said immediately ... ${rightAfter}`);
  console.log(`  figure at ${WATCH_MS} ms .. ${figureAtEnd}`);
  console.log(`  announcements ...... ${log.announcements.filter((a) => a.spoken).length} spoken`);
  for (const a of log.announcements) {
    console.log(`  ${String(a.ms).padStart(6)} ms  [${a.spoken ? "spoken" : "mute  "}]  ${a.text}`);
  }
  await ctx.close();
}

// ── 5 ── the resting page ─────────────────────────────────────────────────────────────
{
  const { ctx, page } = await openPage(browser, true);
  await page.waitForTimeout(2000);
  const state = (await page.locator("#sd-arrive-state").textContent()).trim();
  const log = await page.evaluate(() => window.__log);
  console.log(`\nRESTING PAGE (reduced motion)`);
  console.log(`  state line ......... ${state}`);
  console.log(`  figure rewrites .... ${log.figure.length}`);
  await ctx.close();
}

await browser.close();
