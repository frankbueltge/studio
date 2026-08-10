// tiers.mjs — does every number this page prints stand under a tier word?
//
// Why this exists. On 2026-08-10 (session 82) a cut four voices had asked for removed the
// only text on a face that marked the page's largest published number as DERIVED, and the
// tier legend — the authority every other check implicitly trusts — had never named that
// figure either. The cardinal sin of this house was committed BY SUBTRACTION and was caught
// only because a verifying pass happened to be reading that night. `memory/open-questions.md`
// wrote the missing instrument down: *"an instrument that enumerates every numeric figure a
// built face prints and asserts each is inside an element carrying, or governed by, a tier
// word — and exits non-zero otherwise."* This is that instrument.
//
//   NODE_PATH=<global node_modules> node tools/tiers.mjs
//   NODE_PATH=... node tools/tiers.mjs --dir=projects/season1/still-dark --width=1400
//   NODE_PATH=... node tools/tiers.mjs --stop=6      # drive the head to a stop first
//
// WHAT IT CAN AND CANNOT SAY, stated here because an instrument that overclaims is worse
// than none. It can say: this printed number has no tier word anywhere in the block it
// belongs to. That is a fact about the document and it is the failure of session 82. It
// CANNOT say that a tier word which is present is the RIGHT one — the verifying pass of
// session 83 found two columns captioned OBSERVED whose values are SOURCED, and no
// proximity rule can catch that. Governance here is structural: the nearest ancestor that
// is a <section>, or the page root, and the tier word must stand inside it.
//
// Dependencies, named honestly: node >= 18 and playwright (chromium). The house's check on
// itself; the work ships as one self-contained file with no runtime dependency.
import { createRequire } from "node:module";
import { join, resolve } from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const argv = process.argv.slice(2);
const arg = (k, d) => {
  const a = argv.find((x) => x.startsWith(`--${k}=`));
  return a ? a.slice(k.length + 3) : d;
};
const dir = resolve(arg("dir", "projects/season1/still-dark"));
const width = Number(arg("width", 1400));
const stop = arg("stop", null);
const url = "file://" + join(dir, "index.html");

const TIERS = ["VERIFIED", "SOURCED", "DERIVED", "OBSERVED", "IMAGINED"];

const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width, height: 1200 },
  colorScheme: "light",
  reducedMotion: "reduce",
});
const page = await ctx.newPage();
await page.goto(url);
await page.waitForTimeout(400);
if (stop !== null) {
  await page.$$eval(
    "#sd-arrive-ladder button:not(.sd-arrive-replay)",
    (bs, k) => bs[Number(k)].click(),
    stop,
  );
  await page.waitForTimeout(120);
}

const found = await page.evaluate((tiers) => {
  // Every visible text node, in document order. Hidden text is excluded: a figure nobody
  // is shown is not a published figure, and a tier word nobody is shown does not cover one.
  const visible = (el) => {
    const s = getComputedStyle(el);
    if (s.display === "none" || s.visibility === "hidden" || Number(s.opacity) === 0) return false;
    return el.getClientRects().length > 0;
  };
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const nodes = [];
  let n;
  while ((n = walker.nextNode())) {
    const t = (n.textContent || "").trim();
    if (!t) continue;
    const el = n.parentElement;
    if (!el || !visible(el)) continue;
    nodes.push({ text: t, el });
  }
  // A "figure" is a run of digits. Dates and times are numbers a reader reads as numbers
  // and they carry tiers too — the edition dates on this face are SOURCED and were found
  // mis-captioned once already — so nothing is filtered out by shape.
  const scopeOf = (el) => el.closest("section") || document.body;
  const scopeName = (s) => (s === document.body ? "page root" : "#" + (s.id || s.className));
  const out = [];
  for (const { text, el } of nodes) {
    const figs = text.match(/\d[\d.,  ]*\s*%?/g);
    if (!figs) continue;
    const scope = scopeOf(el);
    const scopeText = scope.innerText || "";
    const covering = tiers.filter((t) => scopeText.includes(t));
    // How far the reader is from the word, in pixels, measured to the nearest element that
    // actually carries it. Distance is reported, never judged: this house has no evidence
    // for a threshold and will not invent one.
    let px = null;
    if (covering.length) {
      const r = el.getBoundingClientRect();
      let best = Infinity;
      for (const cand of scope.querySelectorAll("*")) {
        const ct = cand.textContent || "";
        if (!covering.some((t) => ct.includes(t))) continue;
        if (cand.children.length) continue;
        const cr = cand.getBoundingClientRect();
        if (!cr.width && !cr.height) continue;
        const d = Math.round(Math.abs(cr.top - r.top));
        if (d < best) best = d;
      }
      px = best === Infinity ? null : best;
    }
    out.push({
      figures: figs.map((f) => f.trim()).join(" · "),
      snippet: text.length > 68 ? text.slice(0, 68) + "…" : text,
      scope: scopeName(scope),
      covering,
      px,
    });
  }
  return out;
}, TIERS);

await browser.close();

const bare = found.filter((f) => f.covering.length === 0);
console.log(`tiers.mjs — ${url}`);
console.log(`width ${width}${stop !== null ? `, stop ${stop}` : ""} · ${found.length} text node(s) carrying a figure\n`);
for (const f of found) {
  const mark = f.covering.length ? f.covering.join("/") : "— NO TIER WORD IN SCOPE";
  const near = f.px === null ? "" : `  (${f.px} px)`;
  console.log(`  ${f.figures.padEnd(26)} ${mark}${near}`);
  console.log(`      ${f.scope} · “${f.snippet}”`);
}
if (bare.length) {
  console.log(`\nTIERS: ${bare.length} printed figure(s) stand in a scope with no tier word.`);
  process.exit(1);
}
console.log(`\nTIERS: every printed figure stands in a scope carrying a tier word.`);
console.log(`Scope is structural, not semantic: this says a tier word is present, never that it is the right one.`);
