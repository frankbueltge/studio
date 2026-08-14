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
// HOW LONG TO WATCH IS NOT TYPED HERE — SESSION 94. It was `30000`, set when the run was
// shorter, and every list this work saves makes the run one beat longer. On the night the
// eleventh list arrived the run's closing sentence — the one that speaks the live figure —
// was scheduled at 30,118 ms, 118 ms past that constant, and this file reported it as not
// spoken. (The observed instant is jitter around the schedule: four runs on the frozen
// object gave 30,166 to 30,201 ms. This comment printed "175 ms" for one session, a figure
// no run returns; struck by `VERIFIER-94` blocking 2, which is this file's own subject
// committed by hand in three places.) That is the same defect as the `head -6` that cut the
// band's condition off the face two sessions earlier (banked 56) — a constant a hand has to
// advance, wearing a variable's name. The window is read from the page's own run
// (`window.__sdRun`) and a margin is added to it.
//
// AND THE INSTRUMENT CAN GO RED ABOUT THE RUN AGAIN — `DRAMATURG-94` cut 2, which is the
// cut that returned this work. That stale `30000` was, by accident, the only assertion
// anywhere in this house that the run must fit inside thirty seconds; deriving the window
// from the run turned the alarm into a gauge, and a gauge exits 0 in 2027 while patiently
// watching a four-minute run. So the page publishes the CEILING it is budgeted against and
// this file exits 5 when the run exceeds it. MARGIN_MS is the one duration left here, and
// it is a margin on a measurement, not a length this work promises anyone.
const MARGIN_MS = 2000;
const watchMs = (run) => run.done_ms + MARGIN_MS;

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

// Filled from the page in block 1 and used by block 4, so both blocks watch the same
// derived window and neither one holds a duration of its own.
let RUN = null;
let WATCH_MS = null;

const browser = await chromium.launch();

// ── 1 + 2 + 3 ── the untouched run ────────────────────────────────────────────────────
{
  const { ctx, page } = await openPage(browser, false);
  const regions = await page.evaluate(() =>
    document.querySelectorAll("[aria-live],[role=status],[role=alert]").length);
  RUN = await page.evaluate(() => window.__sdRun);
  if (!RUN) {
    console.error("the page does not publish its run (window.__sdRun) — nothing to derive a window from");
    process.exit(3);
  }
  WATCH_MS = watchMs(RUN);
  console.log(
    `RUN, AS THE PAGE PUBLISHES IT  ${RUN.stops} stops · first dwell ${RUN.first_dwell_ms} ms · ` +
    `beat ${RUN.beat_ms} ms · last state ${RUN.ends_ms} ms · closing sentence ${RUN.done_ms} ms`);
  console.log(
    `THE CEILING ............ ${RUN.ceiling_ms} ms · the run is ${RUN.done_ms} ms · ` +
    `${RUN.ceiling_ms - RUN.done_ms} ms of room · beats ${RUN.beats_ms.join(", ")} ` +
    `(protected: ${RUN.protected_beats.join(", ")})`);
  // The one thing in this work that may fail on a night when nothing was edited: the run
  // outgrowing the length the house published as the one it would defend.
  if (RUN.done_ms > RUN.ceiling_ms) {
    console.error(
      `THE RUN IS LONGER THAN THIS WORK SAYS IT MAY BE: ${RUN.done_ms} ms against a ` +
      `published ceiling of ${RUN.ceiling_ms} ms. The beats cannot be shortened further ` +
      `without cutting the protected ones, which is a staging decision and not a repair.`);
    process.exit(5);
  }
  // THE SENTENCE AGAINST THE RUN — `DRAMATURG-94` cut 3's test. The page promises a visitor
  // a length in words, in `run_states.waiting`, built by the builder; the run is the beats.
  // Nothing before tonight compared them, which is how one beat could have been changed in
  // one file and left the face promising the other number, silently, with every guard green.
  const TENS = ["", "", "twenty", "thirty", "forty", "fifty"];
  const ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  const TEENS = { 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen" };
  const spellOut = (n) => n < 10 ? ONES[n] : n < 20 ? TEENS[n]
    : TENS[Math.floor(n / 10)] + (n % 10 ? "-" + ONES[n % 10] : "");
  const promised = spellOut(Math.round(RUN.done_ms / 1000));
  const waiting = await page.evaluate(() =>
    JSON.parse(document.getElementById("sd-data").textContent).arrive.run_states.waiting);
  if (!waiting.includes(`about ${promised} seconds`)) {
    console.error(
      `THE SENTENCE AND THE RUN DISAGREE: the run is ${RUN.done_ms} ms, so the page owes a ` +
      `visitor "about ${promised} seconds", and it says:\n  ${waiting}`);
    process.exit(6);
  }
  console.log(`THE PROMISE ............ "about ${promised} seconds", and the run is ${RUN.done_ms} ms — they agree`);
  console.log(`WATCHED ................ ${WATCH_MS} ms (the run + ${MARGIN_MS} ms, derived, never typed)`);
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
