#!/usr/bin/env node
// build-57.mjs — the étude-57 generator, "YOU ARE UNDER A DUTY", C1–C6 variant.
//
// A single committed file that (a) emits the static HTML page for any combination
// of the binding variables (order, mark treatment, C2 placement, extent, closed/open)
// and (b) drives the rendering/measurement pipeline used to produce and check the
// artefacts in REPORT-57.md, so a second hand can re-run everything from this file
// alone plus the source data JSON.
//
// Requires: node >= 18, and for the render/shot/downscale/pixels/measure-dom/digitcheck
// subcommands, a Playwright Chromium install. Point PLAYWRIGHT_BROWSERS_PATH at the
// browsers directory before running those; do not run `playwright install`.
//
//   PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node build-57.mjs <subcommand> [flags]
//
// Subcommands:
//   html        --order O1|O2 --mark M-A|M-B --placement P1|P2 --extent N [--closed] [--out FILE] [--data FILE]
//   shot        --html FILE --width N --height N --mode full|viewport --out FILE.png
//   downscale   --in FILE.png --out FILE.png --factor 0.25
//   pixels      --in FILE.png --mode groundtest|markband [--band-top N --band-height N]
//   measure-dom --html FILE --width N
//   digitcheck  --html FILE --width N --height N
//   wrapcount   --html FILE --width N
//
// No <script>, no external reference, no web font is ever written into the emitted
// page itself — this generator is a build-time tool, its own tags never ship.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DEFAULT_DATA = path.resolve(
  __dirname,
  '../../projects/pfd-channel/data/nonresponse-tables-2026-08-01.json'
);

// Observation date is fixed by the brief: 2026-08-01. Treated as UTC midnight
// throughout so day-count arithmetic never falls prey to DST.
const OBS_DATE = Date.UTC(2026, 7, 1);

// The one row drawn CLOSED (see CHOSEN_CLOSED_ROW rationale in REPORT-57.md §closed).
const CLOSED_ROW_DECEASED = 'Janet Harrison';
const CLOSED_ROW_RECIPIENT = 'Southampton City Council';
const CLOSED_DAY = 200; // day of the simulated 400-day observation run on which closure is drawn
const CLOSED_DATE = new Date(OBS_DATE + (CLOSED_DAY - 1) * 86400000); // day 1 = 2026-08-01

// ---------------------------------------------------------------------------
// number / date words
// ---------------------------------------------------------------------------

const ORDINAL_DAY = [
  null, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth',
  'ninth', 'tenth', 'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth',
  'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth', 'twentieth', 'twenty-first',
  'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth', 'twenty-sixth',
  'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirtieth', 'thirty-first'
];
const MONTHS = ['January','February','March','April','May','June','July','August',
  'September','October','November','December'];
const MONTHS_ABBR = {jan:0,feb:1,mar:2,apr:3,may:4,jun:5,jul:6,aug:7,sep:8,oct:9,nov:10,dec:11};

const ONES = [null,'one','two','three','four','five','six','seven','eight','nine'];
const TEENS = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
  'seventeen','eighteen','nineteen'];
const TENS = [null,null,'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'];

function cardinal1to99(n) {
  if (n === 0) return 'zero';
  if (n < 10) return ONES[n];
  if (n < 20) return TEENS[n - 10];
  const t = Math.floor(n / 10), o = n % 10;
  return o === 0 ? TENS[t] : `${TENS[t]}-${ONES[o]}`;
}

function yearWords(y) {
  if (y < 2000 || y >= 2100) throw new Error(`yearWords: ${y} outside supported 2000-2099 range`);
  const rem = y - 2000;
  return rem === 0 ? 'two thousand' : `two thousand and ${cardinal1to99(rem)}`;
}

function dateWords(d) {
  return `${ORDINAL_DAY[d.getUTCDate()]} of ${MONTHS[d.getUTCMonth()]}, ${yearWords(d.getUTCFullYear())}`;
}

function parseUKDate(s) {
  const [d, m, y] = s.split('/').map(Number);
  return new Date(Date.UTC(y, m - 1, d));
}

function parsePublished(s) {
  // "30 June 2026" or "31 Dec 2025"
  const m = s.trim().match(/^(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})$/);
  if (!m) throw new Error(`parsePublished: cannot parse "${s}"`);
  const day = Number(m[1]);
  const monKey = m[2].slice(0, 3).toLowerCase();
  const year = Number(m[3]);
  if (!(monKey in MONTHS_ABBR)) throw new Error(`parsePublished: unknown month "${m[2]}"`);
  return Date.UTC(year, MONTHS_ABBR[monKey], day);
}

function daysBetween(fromMs, toMs) {
  return Math.round((toMs - fromMs) / 86400000);
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// ---------------------------------------------------------------------------
// data
// ---------------------------------------------------------------------------

function loadTables(dataPath) {
  return JSON.parse(fs.readFileSync(dataPath, 'utf8'));
}

function buildEntries(order, dataPath) {
  const tables = loadTables(dataPath);
  const enriched = [];
  tables.forEach((t, ti) => {
    const publishedMs = parsePublished(t.published);
    t.rows.forEach((r) => {
      const [deceased, dateOfReport, coroner, area, sentTo, dueStr] = r;
      const dueMs = parseUKDate(dueStr).getTime();
      const days = daysBetween(dueMs, OBS_DATE);
      const recipients = sentTo.split('|').map((s) => s.trim());
      enriched.push({ ti, publishedMs, deceased, dueMs, days, recipients });
    });
  });

  if (order === 'O1') {
    // oldest duty first: days outstanding descending. Array.prototype.sort is
    // stable in node >= 12, so ties keep the original table/row order — this
    // is what produces the exact e1 tie order (verified against e1.html).
    return enriched.slice().sort((a, b) => b.days - a.days);
  }
  if (order === 'O2') {
    // the state's own printed order: the four published tables taken
    // oldest-published-first, rows left exactly as printed inside each table.
    const tableOrder = tables
      .map((t, i) => ({ i, p: parsePublished(t.published) }))
      .sort((a, b) => a.p - b.p)
      .map((x) => x.i);
    const byTable = new Map();
    enriched.forEach((e) => {
      if (!byTable.has(e.ti)) byTable.set(e.ti, []);
      byTable.get(e.ti).push(e);
    });
    const out = [];
    tableOrder.forEach((ti) => out.push(...(byTable.get(ti) || [])));
    return out;
  }
  throw new Error(`buildEntries: unknown order "${order}"`);
}

// ---------------------------------------------------------------------------
// HTML assembly
// ---------------------------------------------------------------------------

const ABSENCE_LINE = 'There is no power authorising a coroner to take any steps.';

function ruleSegmentsHtml(days) {
  const full = Math.floor(days / 16);
  const rem = days % 16;
  let html = '';
  for (let i = 0; i < full; i++) html += '<span class="seg" style="width:16px"></span>';
  if (rem > 0) html += `<span class="seg" style="width:${rem}px"></span>`;
  return html;
}

function markBHeight(i) {
  // deterministic irregular-height sequence — a multiplicative hash, not
  // randomness, so a re-run reproduces pixel-identical marks. Range 2–9px,
  // same scale as M-A's fixed 9px tick, so the two treatments are visually
  // comparable in extent, not just in density.
  const hash = (i * 2654435761) % 4294967296;
  return 2 + (hash % 8);
}

function marksHtml(mark, count) {
  let html = '';
  if (mark === 'M-A') {
    for (let i = 0; i < count; i++) html += '<span class="mark"></span>';
  } else if (mark === 'M-B') {
    for (let i = 0; i < count; i++) html += `<span class="markb" style="height:${markBHeight(i)}px"></span>`;
  } else {
    throw new Error(`marksHtml: unknown mark "${mark}"`);
  }
  return html;
}

function buildHTML(opts) {
  const {
    order, mark, placement, extent, closed = false,
    data = DEFAULT_DATA,
  } = opts;
  if (!['O1', 'O2'].includes(order)) throw new Error(`bad order ${order}`);
  if (!['M-A', 'M-B'].includes(mark)) throw new Error(`bad mark ${mark}`);
  if (!['P1', 'P2'].includes(placement)) throw new Error(`bad placement ${placement}`);
  if (!Number.isInteger(extent) || extent < 1) throw new Error(`bad extent ${extent}`);

  const entries = buildEntries(order, data);

  const entryHtml = entries.map((e) => {
    const isClosedRow = closed && e.deceased === CLOSED_ROW_DECEASED
      && e.recipients.length === 1 && e.recipients[0] === CLOSED_ROW_RECIPIENT;

    const sentences = e.recipients.map((r) => {
      if (isClosedRow) {
        return `<p class="sentence">${escapeHtml(r)} responded to this report on the prevention of future deaths, on ${dateWords(CLOSED_DATE)}.</p>`;
      }
      return `<p class="sentence">${escapeHtml(r)} is under a duty to respond to this report on the prevention of future deaths, namely by ${dateWords(new Date(e.dueMs))}.</p>`;
    }).join('');

    const marksCount = isClosedRow ? Math.min(CLOSED_DAY, extent) : extent;
    const ruleHtml = `<div class="rule-line">${ruleSegmentsHtml(e.days)}${marksHtml(mark, marksCount)}</div>`;

    return `<section class="entry">\n<p class="name">${escapeHtml(e.deceased)}</p>\n${sentences}\n${ruleHtml}\n</section>`;
  }).join('\n');

  const absenceP = `<p class="sentence">${ABSENCE_LINE}</p>`;
  const headerAbsence = placement === 'P1' ? `\n${absenceP}` : '';
  const footAbsence = placement === 'P2' ? `\n${absenceP}` : '';

  const colophonLines = [
    `<p>Source: judiciary.uk, non-responses to Prevention of Future Deaths reports, https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/; Chief Coroner's guidance, chapter sixteen, https://www.judiciary.uk/guidance-and-resources/chapter-16-reports-to-prevent-future-deaths-pfds/; retrieved the first of August, two thousand and twenty-six.</p>`,
  ];
  if (closed) {
    colophonLines.push('<p>The closure shown here is simulated for study; no response has been received in this row as at the first of August, two thousand and twenty-six.</p>');
  }
  const footer = `<footer>\n${colophonLines.join('\n')}\n</footer>`;

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>YOU ARE UNDER A DUTY</title>
<style>
:root { color-scheme: light; }
html, body {
  margin: 0;
  padding: 0;
  background: #ffffff;
  color: #000000;
}
body {
  font-family: Georgia, Cambria, "Iowan Old Style", "Times New Roman", Times, serif;
  font-size: 19px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
main {
  max-width: 640px;
  margin: 0 auto;
  padding: 72px 24px 160px;
  box-sizing: border-box;
}
header {
  margin: 0 0 4.5em;
}
h1 {
  font-size: 1em;
  font-weight: normal;
  letter-spacing: 0.14em;
  margin: 0 0 0.9em;
}
header p {
  margin: 0;
  font-size: 0.92em;
}
header p.sentence {
  font-size: 1em;
  margin-top: 1.2em;
}
.entry {
  margin: 0 0 3.4em;
}
.entry:last-child {
  margin-bottom: 0;
}
p.name {
  font-variant: small-caps;
  font-size: 1.08em;
  letter-spacing: 0.02em;
  margin: 0 0 0.5em;
}
p.sentence {
  margin: 0.35em 0 0;
}
.rule-line {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  margin-top: 1em;
}
.seg {
  display: block;
  height: 2px;
  background: #000000;
  flex: 0 0 auto;
}
.mark {
  display: block;
  width: 3px;
  height: 9px;
  background: #000000;
  flex: 0 0 auto;
  margin-left: 2px;
}
.markb {
  display: block;
  width: 1px;
  background: #000000;
  flex: 0 0 auto;
  margin-left: 1px;
}
footer {
  margin-top: 5em;
  font-size: 0.85em;
}
footer p + p {
  margin-top: 0.6em;
}
</style>
</head>
<body>
<main>
<header>
<h1>YOU ARE UNDER A DUTY</h1>
<p>Observed the first of August, two thousand and twenty-six.</p>${headerAbsence}
</header>
${entryHtml}${footAbsence ? `\n${footAbsence}` : ''}
${footer}
</main>
</body>
</html>
`;
}

// ---------------------------------------------------------------------------
// CLI
// ---------------------------------------------------------------------------

function parseFlags(argv) {
  const out = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next === undefined || next.startsWith('--')) {
        out[key] = true;
      } else {
        out[key] = next;
        i++;
      }
    }
  }
  return out;
}

async function loadPlaywright() {
  const mod = await import('/opt/node22/lib/node_modules/playwright/index.mjs');
  return mod;
}

async function cmdHtml(flags) {
  const html = buildHTML({
    order: flags.order,
    mark: flags.mark,
    placement: flags.placement,
    extent: Number(flags.extent),
    closed: !!flags.closed,
    data: flags.data || DEFAULT_DATA,
  });
  if (flags.out) {
    fs.writeFileSync(flags.out, html);
    console.error(`wrote ${flags.out} (${Buffer.byteLength(html)} bytes)`);
  } else {
    process.stdout.write(html);
  }
}

async function cmdShot(flags) {
  const { chromium } = await loadPlaywright();
  const width = Number(flags.width);
  const height = Number(flags.height || 1000);
  const mode = flags.mode || 'full';
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width, height } });
    await page.goto('file://' + path.resolve(flags.html));
    await page.waitForTimeout(50);
    const buf = await page.screenshot({ fullPage: mode === 'full' });
    fs.writeFileSync(flags.out, buf);
    console.error(`wrote ${flags.out} (mode=${mode}, viewport=${width}x${height})`);
  } finally {
    await browser.close();
  }
}

async function cmdDownscale(flags) {
  const { chromium } = await loadPlaywright();
  const inPath = path.resolve(flags.in);
  const factor = Number(flags.factor || 0.25);
  const tmpHtml = inPath + `.downscale-${Date.now()}.html`;
  const html = `<!doctype html><meta charset="utf-8"><body style="margin:0">
<canvas id="c"></canvas>
<script>
const img = new Image();
img.onload = () => {
  const w = Math.max(1, Math.round(img.naturalWidth * ${factor}));
  const h = Math.max(1, Math.round(img.naturalHeight * ${factor}));
  const c = document.getElementById('c');
  c.width = w; c.height = h;
  const ctx = c.getContext('2d');
  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(img, 0, 0, w, h);
  window.__done = c.toDataURL('image/png');
  window.__w = w; window.__h = h;
};
img.onerror = (e) => { window.__err = String(e); };
img.src = 'file://${inPath}';
</script>`;
  fs.writeFileSync(tmpHtml, html);
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto('file://' + tmpHtml);
    await page.waitForFunction(() => window.__done || window.__err, null, { timeout: 60000 });
    const err = await page.evaluate(() => window.__err);
    if (err) throw new Error('image load failed: ' + err);
    const dataUrl = await page.evaluate(() => window.__done);
    const dims = await page.evaluate(() => ({ w: window.__w, h: window.__h }));
    const b64 = dataUrl.replace(/^data:image\/png;base64,/, '');
    fs.writeFileSync(flags.out, Buffer.from(b64, 'base64'));
    console.error(`wrote ${flags.out} (${dims.w}x${dims.h}, factor=${factor})`);
  } finally {
    await browser.close();
    fs.unlinkSync(tmpHtml);
  }
}

// pixel-level analysis of a rendered PNG still, via chromium's own canvas
// decode/readback (no hand-rolled PNG parser needed — chromium's decoder is
// the ground truth for what a viewer actually sees).
async function cmdPixels(flags) {
  const { chromium } = await loadPlaywright();
  const inPath = path.resolve(flags.in);
  const mode = flags.mode;
  const tmpHtml = inPath + `.pixels-${Date.now()}.html`;
  const html = `<!doctype html><meta charset="utf-8"><body style="margin:0">
<canvas id="c"></canvas>
<script>
window.__result = null;
window.__err = null;
const img = new Image();
img.onload = () => {
  try {
    const w = img.naturalWidth, h = img.naturalHeight;
    const c = document.getElementById('c');
    c.width = w; c.height = h;
    const ctx = c.getContext('2d');
    ctx.drawImage(img, 0, 0);
    const data = ctx.getImageData(0, 0, w, h).data;
    const isWhiteRow = new Uint8Array(h);
    for (let y = 0; y < h; y++) {
      let white = 1;
      const rowStart = y * w * 4;
      for (let x = 0; x < w; x++) {
        const idx = rowStart + x * 4;
        if (data[idx] !== 255 || data[idx+1] !== 255 || data[idx+2] !== 255) { white = 0; break; }
      }
      isWhiteRow[y] = white;
    }
    if ('${mode}' === 'groundtest') {
      let longestRun = 0, longestStart = -1, curRun = 0, curStart = -1;
      for (let y = 0; y < h; y++) {
        if (isWhiteRow[y]) {
          if (curRun === 0) curStart = y;
          curRun++;
          if (curRun > longestRun) { longestRun = curRun; longestStart = curStart; }
        } else {
          curRun = 0;
        }
      }
      // distinct luminance values inside the longest blank run
      const lumSet = new Set();
      for (let y = longestStart; y < longestStart + longestRun; y++) {
        const rowStart = y * w * 4;
        for (let x = 0; x < w; x++) {
          const idx = rowStart + x * 4;
          const lum = Math.round(0.2126*data[idx] + 0.7152*data[idx+1] + 0.0722*data[idx+2]);
          lumSet.add(lum);
        }
      }
      let inkRows = 0;
      for (let y = 0; y < h; y++) if (!isWhiteRow[y]) inkRows++;
      window.__result = { width: w, height: h, longestRun, longestStart,
        distinctLuminance: lumSet.size, luminanceValues: Array.from(lumSet).sort((a,b)=>a-b),
        inkRows, totalRows: h };
    } else if ('${mode}' === 'markband') {
      const top = ${Number(flags['band-top'] || 0)};
      const bandH = ${Number(flags['band-height'] || 0)};
      const lumSet = new Set();
      let inkPixels = 0, totalPixels = 0;
      for (let y = top; y < Math.min(top+bandH, h); y++) {
        const rowStart = y * w * 4;
        for (let x = 0; x < w; x++) {
          const idx = rowStart + x*4;
          const lum = Math.round(0.2126*data[idx] + 0.7152*data[idx+1] + 0.0722*data[idx+2]);
          lumSet.add(lum);
          totalPixels++;
          if (lum < 250) inkPixels++;
        }
      }
      window.__result = { width: w, height: h, band: {top, height: bandH},
        distinctLuminance: lumSet.size, luminanceValues: Array.from(lumSet).sort((a,b)=>a-b),
        inkPixels, totalPixels, inkFraction: inkPixels/totalPixels };
    } else if ('${mode}' === 'dims') {
      window.__result = { width: w, height: h };
    }
  } catch (e) { window.__err = String(e && e.stack || e); }
};
img.onerror = (e) => { window.__err = 'image load error'; };
img.src = 'file://${inPath}';
</script>`;
  fs.writeFileSync(tmpHtml, html);
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto('file://' + tmpHtml);
    await page.waitForFunction(() => window.__result || window.__err, null, { timeout: 120000 });
    const err = await page.evaluate(() => window.__err);
    if (err) throw new Error(err);
    const result = await page.evaluate(() => window.__result);
    console.log(JSON.stringify(result, null, 2));
  } finally {
    await browser.close();
    fs.unlinkSync(tmpHtml);
  }
}

// DOM-geometry based structural measurement (Range.getClientRects gives the
// exact per-visual-line box the layout engine computed — the same geometry
// the still is a raster of, read directly instead of re-derived from pixels).
async function cmdMeasureDom(flags) {
  const { chromium } = await loadPlaywright();
  const width = Number(flags.width);
  const height = Number(flags.height || 2000);
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width, height } });
    await page.goto('file://' + path.resolve(flags.html));
    const result = await page.evaluate(() => {
      function lineRectsOf(el) {
        // one rect per text node child (p.name / p.sentence have a single
        // text node each in this document), via Range.getClientRects()
        const rects = [];
        for (const node of el.childNodes) {
          if (node.nodeType === Node.TEXT_NODE && node.textContent.trim().length) {
            const r = document.createRange();
            r.selectNodeContents(node);
            for (const cr of r.getClientRects()) rects.push({ x: cr.left, y: cr.top, w: cr.width, h: cr.height });
          }
        }
        return rects;
      }
      const entries = Array.from(document.querySelectorAll('.entry'));
      const textLines = []; // {x,y} for every visual line of every p.name/p.sentence, per entry, excluding header/footer
      const nameTops = []; // {top, singleRecipient}
      const blockLineCounts = []; // total visual lines per entry block (name+sentence+rule)
      const ruleInfo = []; // per entry: {days-equivalent via seg count is not known here; widest wrapped line width; wrap line count}

      for (const entry of entries) {
        const nameEl = entry.querySelector('p.name');
        const sentenceEls = Array.from(entry.querySelectorAll('p.sentence'));
        const ruleEl = entry.querySelector('.rule-line');

        const nameRects = lineRectsOf(nameEl);
        nameRects.forEach(r => textLines.push({ x: r.x, y: r.y }));
        nameTops.push({ top: nameRects[0] ? nameRects[0].y : null, singleRecipient: sentenceEls.length === 1 });

        let sentenceLineCount = 0;
        for (const sEl of sentenceEls) {
          const rects = lineRectsOf(sEl);
          rects.forEach(r => textLines.push({ x: r.x, y: r.y }));
          sentenceLineCount += rects.length;
        }

        // rule-line: group .seg (rule ink only, not marks) by rounded top -> one flex line
        const segs = Array.from(ruleEl.querySelectorAll('.seg'));
        const marks = Array.from(ruleEl.querySelectorAll('.mark, .markb'));
        const segLines = new Map();
        for (const s of segs) {
          const r = s.getBoundingClientRect();
          const top = Math.round(r.top);
          if (!segLines.has(top)) segLines.set(top, { left: Infinity, right: -Infinity, width: 0 });
          const g = segLines.get(top);
          g.left = Math.min(g.left, r.left);
          g.right = Math.max(g.right, r.right);
          g.width += r.width;
        }
        const allLines = new Map(); // rule + marks combined, for total wrapped-line count of the rule-line container
        for (const el of [...segs, ...marks]) {
          const r = el.getBoundingClientRect();
          const top = Math.round(r.top);
          allLines.set(top, true);
        }

        const segLineWidths = Array.from(segLines.values()).map(g => g.width);
        const segLineRights = Array.from(segLines.values()).map(g => g.right);
        const segLineLefts = Array.from(segLines.values()).map(g => g.left);

        ruleInfo.push({
          segLineCount: segLines.size,
          segLineWidths,
          segLineRights,
          segLineLefts,
          wrappedLineCountWithMarks: allLines.size,
        });

        blockLineCounts.push(1 + sentenceLineCount + allLines.size);
      }

      return { textLines, nameTops, blockLineCounts, ruleInfo,
        viewport: { width: window.innerWidth, height: window.innerHeight },
        mainContentWidth: (() => {
          const m = document.querySelector('main');
          const cs = getComputedStyle(m);
          return m.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
        })(),
      };
    });
    console.log(JSON.stringify(result));
  } finally {
    await browser.close();
  }
}

async function cmdDigitcheck(flags) {
  const { chromium } = await loadPlaywright();
  const width = Number(flags.width);
  const height = Number(flags.height);
  const raw = fs.readFileSync(path.resolve(flags.html), 'utf8');
  const title = (raw.match(/<title>([\s\S]*?)<\/title>/) || [])[1] || null;
  const metas = Array.from(raw.matchAll(/<meta\b[^>]*>/gi)).map(m => m[0]);
  const comments = Array.from(raw.matchAll(/<!--[\s\S]*?-->/g)).map(m => m[0]);

  const browser = await chromium.launch();
  let firstViewportText = '';
  try {
    const page = await browser.newPage({ viewport: { width, height } });
    await page.goto('file://' + path.resolve(flags.html));
    firstViewportText = await page.evaluate((h) => {
      const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
      let out = '';
      let node;
      while ((node = walker.nextNode())) {
        const txt = node.textContent;
        if (!txt.trim()) continue;
        const range = document.createRange();
        range.selectNodeContents(node);
        const rects = range.getClientRects();
        for (const r of rects) {
          if (r.top < h && r.bottom > 0) { out += txt + '\n'; break; }
        }
      }
      return out;
    }, height);
  } finally {
    await browser.close();
  }

  function scan(label, text) {
    const hits = [];
    const digitRe = /.{0,20}[0-9].{0,20}/g;
    let m;
    while ((m = digitRe.exec(text))) hits.push(m[0]);
    const monthRe = new RegExp('(' + MONTHS.join('|') + ')', 'gi');
    const monthHits = [];
    while ((m = monthRe.exec(text))) monthHits.push(m[0]);
    return { label, digitHits: hits, monthHits };
  }

  const report = {
    title: scan('title', title || ''),
    metas: metas.map((m, i) => scan(`meta[${i}]`, m)),
    comments: comments.map((c, i) => scan(`comment[${i}]`, c)),
    firstViewport: scan('firstViewportText', firstViewportText),
    firstViewportRaw: firstViewportText,
  };
  console.log(JSON.stringify(report, null, 2));
}

async function cmdWrapcount(flags) {
  const data = await (async () => {
    const { chromium } = await loadPlaywright();
    const width = Number(flags.width);
    const browser = await chromium.launch();
    try {
      const page = await browser.newPage({ viewport: { width, height: 2000 } });
      await page.goto('file://' + path.resolve(flags.html));
      return await page.evaluate(() => {
        const entries = Array.from(document.querySelectorAll('.entry'));
        return entries.map((entry) => {
          const segs = Array.from(entry.querySelectorAll('.seg'));
          const tops = new Set(segs.map(s => Math.round(s.getBoundingClientRect().top)));
          return { name: entry.querySelector('p.name').textContent, ruleLineCount: tops.size, wraps: tops.size > 1 };
        });
      });
    } finally {
      await browser.close();
    }
  })();
  const wrapCount = data.filter(d => d.wraps).length;
  console.log(JSON.stringify({ width: Number(flags.width), total: data.length, wrapCount, detail: data }, null, 2));
}

async function main() {
  const [, , cmd, ...rest] = process.argv;
  const flags = parseFlags(rest);
  switch (cmd) {
    case 'html': return cmdHtml(flags);
    case 'shot': return cmdShot(flags);
    case 'downscale': return cmdDownscale(flags);
    case 'pixels': return cmdPixels(flags);
    case 'measure-dom': return cmdMeasureDom(flags);
    case 'digitcheck': return cmdDigitcheck(flags);
    case 'wrapcount': return cmdWrapcount(flags);
    default:
      console.error(`usage: build-57.mjs <html|shot|downscale|pixels|measure-dom|digitcheck|wrapcount> [flags]`);
      process.exit(1);
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
