// NO PART — production increment 01. Rasterises all 39 pages of the source
// PDF (the U.S. Supreme Court's Order List of Monday 6 October 2025) at
// 4 px/mm into render/sheet-01.png ... render/sheet-39.png.
//
// Method is the concept-gate étude's, unchanged (see build/pdf-render-lib.js
// and its header, copied from etudes/5000-series/still/no-part/): this
// environment has no pdftoppm/pdftocairo/gs/mutool/fitz/pypdfium2, and
// headless Chromium treats a local PDF as a download rather than rendering
// it. A real (non-headless) Chromium under Xvfb, using its own built-in
// PDFium-based PDF viewer, does render it — genuine rasterisation, not a
// reconstruction from text extraction.
//
// Usage:
//   xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node render-sheets.js
//
// Optional: NO_PART_PAGES="1,2,5-8" to render only a subset (for testing);
// default is all 39 pages, 1-39.
//
// Order-list.pdf is verified by SHA-256 at the top of every run; no network
// access happens anywhere in this script.

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { chromium } = require('playwright');
const { PDF_PATH, renderPage } = require('./pdf-render-lib.js');
const { launchBrowser, desaturateToGrayscale } = require('./canvas-lib.js');

const RENDER_DIR = path.resolve(__dirname, '..', 'render');
const EXPECTED_SHA256 = '354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652';
const PX_PER_MM = 4;
const TOTAL_PAGES = 39;
const MAX_ATTEMPTS = 3;

function log(...args) { console.log(...args); }
function section(title) { console.log('\n=== ' + title + ' ==='); }

function verifyPdf() {
  if (!fs.existsSync(PDF_PATH)) {
    console.error(`Missing ${PDF_PATH}.`);
    console.error('This is a one-time, documented, network step (NOT run inside this build) — see build/README.md.');
    process.exit(1);
  }
  const data = fs.readFileSync(PDF_PATH);
  const hash = crypto.createHash('sha256').update(data).digest('hex');
  if (hash !== EXPECTED_SHA256) {
    console.error(`SHA-256 mismatch: got ${hash}, expected ${EXPECTED_SHA256}. Aborting — refusing to build from an unverified source file.`);
    process.exit(1);
  }
  section('PDF verification');
  log(`order-list.pdf: ${data.length} bytes, SHA-256 ${hash} — MATCHES recorded hash.`);
}

function parsePageList(spec) {
  if (!spec) return Array.from({ length: TOTAL_PAGES }, (_, i) => i + 1);
  const out = [];
  for (const part of spec.split(',')) {
    if (part.includes('-')) {
      const [a, b] = part.split('-').map(Number);
      for (let n = a; n <= b; n++) out.push(n);
    } else {
      out.push(Number(part));
    }
  }
  return out;
}

async function renderWithRetry(browser, pageNum, pxPerMm, maxAttempts) {
  let lastErr;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await renderPage(browser, pageNum, pxPerMm);
    } catch (e) {
      lastErr = e;
      log(`  sheet ${pageNum}: attempt ${attempt}/${maxAttempts} failed (${e.message})`);
      await new Promise((r) => setTimeout(r, 1200));
    }
  }
  throw lastErr;
}

async function main() {
  verifyPdf();

  const pages = parsePageList(process.env.NO_PART_PAGES);
  fs.mkdirSync(RENDER_DIR, { recursive: true });

  section(`Rasterising ${pages.length} page(s) at ${PX_PER_MM} px/mm`);
  log('AA-mitigation flags applied at launch (documented in the concept-gate étude as having no measurable');
  log('effect on this Chromium build\'s PDF-viewer glyph path, kept anyway for parity/traceability); the');
  log('operative fix is post-process desaturation to neutral grey, applied below to every sheet.');

  const browser = await launchBrowser(chromium);

  const results = [];
  const failed = [];
  const t0 = Date.now();

  for (const pg of pages) {
    const pageT0 = Date.now();
    try {
      const { buffer, widthPx, heightPx, shortfallPx } = await renderWithRetry(browser, pg, PX_PER_MM, MAX_ATTEMPTS);
      const grayBuffer = await desaturateToGrayscale(browser, buffer);
      const fname = path.join(RENDER_DIR, `sheet-${String(pg).padStart(2, '0')}.png`);
      fs.writeFileSync(fname, grayBuffer);
      const dt = ((Date.now() - pageT0) / 1000).toFixed(1);
      log(`sheet ${String(pg).padStart(2, '0')}: ${widthPx}x${heightPx}px -> ${fname} (${grayBuffer.length} bytes, ${dt}s)`);
      if (shortfallPx > 0) {
        const shortfallMm = (shortfallPx / PX_PER_MM).toFixed(2);
        log(`  ** DEFECT: sheet ${pg}'s bottom ${shortfallPx}px (${shortfallMm}mm) could not be captured from the source screenshot`);
        log(`     (see pdf-render-lib.js "LAST-PAGE DEFECT" comment) — that strip is filled paper-white in the saved PNG,`);
        log(`     not sourced from any rendered pixel. Treat sheet ${pg}'s bottom ${shortfallMm}mm as UNMEASURED, not confirmed-blank.`);
      }
      results.push({ page: pg, widthPx, heightPx, bytes: grayBuffer.length, shortfallPx });
    } catch (e) {
      log(`sheet ${String(pg).padStart(2, '0')}: FAILED after ${MAX_ATTEMPTS} attempts — ${e.message}`);
      failed.push({ page: pg, error: e.message });
    }
  }

  await browser.close();

  const totalDt = ((Date.now() - t0) / 60000).toFixed(1);
  section('Summary');
  log(`Rendered ${results.length}/${pages.length} requested sheets in ${totalDt} min.`);
  if (results.length) {
    const widths = new Set(results.map((r) => r.widthPx));
    const heights = new Set(results.map((r) => r.heightPx));
    log(`Pixel dimensions across rendered sheets: width(s) = ${[...widths].join(',')}px, height(s) = ${[...heights].join(',')}px.`);
    if (widths.size > 1 || heights.size > 1) {
      log('WARNING: not all sheets rendered to the same pixel size — investigate before trusting downstream measurements.');
    }
  }
  const shortfallSheets = results.filter((r) => r.shortfallPx > 0);
  if (shortfallSheets.length) {
    log(`Sheets with an unmeasured bottom strip (see per-sheet DEFECT notes above): ${shortfallSheets.map((r) => `${r.page} (${r.shortfallPx}px / ${(r.shortfallPx / PX_PER_MM).toFixed(2)}mm)`).join(', ')}`);
  }
  if (failed.length) {
    console.error(`FAILED sheets (not filled, not guessed): ${JSON.stringify(failed, null, 2)}`);
    process.exitCode = 1;
  } else {
    log('All requested sheets rendered successfully.');
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
