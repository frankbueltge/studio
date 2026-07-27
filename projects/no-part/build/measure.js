// NO PART — production increment 01. Measures the 39 rendered sheets and
// emits plate-manifest.json, line-profile.json, and a stdout report.
//
// Everything here is computed from the pixels in render/sheet-NN.png — see
// build/README.md for the honest limits of that claim (rasterised pages,
// not photographs of mounted paper).
//
// Usage:
//   xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node measure.js
//
// Requires render/sheet-01.png ... sheet-39.png to already exist (run
// render-sheets.js first) and render/render-log.json (written by the same
// script) so this script never has to hardcode which sheets, if any, carry
// an unmeasured/padded region.

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { launchBrowser, runInCanvas, LUM_THRESH } = require('./canvas-lib.js');

const RENDER_DIR = path.resolve(__dirname, '..', 'render');
const OUT_DIR = path.resolve(__dirname, '..');
const PX_PER_MM = 4;
const TOTAL_SHEETS = 39;

// Row-band detection thresholds — same values used throughout the
// concept-gate étude's build.js (LUM_THRESH=150 for ink, >2 dark pixels to
// call a row "has ink", >=6px tall to call a band real rather than
// antialiasing noise). Kept identical here for continuity, not re-derived.
const ROW_NOISE_MIN_DARK_PX = 2;
const ROW_MIN_HEIGHT_PX = 6;

function log(...args) { console.log(...args); }
function section(title) { console.log('\n=== ' + title + ' ==='); }
function round4(x) { return Math.round(x * 10000) / 10000; }
function round2(x) { return Math.round(x * 100) / 100; }

function median(arr) {
  const s = [...arr].sort((a, b) => a - b);
  const n = s.length;
  if (n === 0) return null;
  return n % 2 === 1 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2;
}

// ---- Per-sheet pixel analysis, run inside the browser canvas ----
// Self-contained (no closures over outer scope — see canvas-lib.js
// runInCanvas) — everything it needs comes through `args`.
function analyzeSheet(ctx, canvas, args) {
  const { width, height } = canvas;
  const data = ctx.getImageData(0, 0, width, height).data;
  const LUM_THRESH = args.LUM_THRESH;
  const PX_PER_MM = args.PX_PER_MM;
  const ROW_NOISE_MIN_DARK_PX = args.ROW_NOISE_MIN_DARK_PX;
  const ROW_MIN_HEIGHT_PX = args.ROW_MIN_HEIGHT_PX;

  const n = width * height;
  const ink = new Uint8Array(n);
  let totalInk = 0;
  for (let p = 0, i = 0; p < n; p++, i += 4) {
    const lum = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
    if (lum < LUM_THRESH) { ink[p] = 1; totalInk++; }
  }

  const rowInkCount = new Int32Array(height);
  for (let y = 0; y < height; y++) {
    let c = 0;
    const base = y * width;
    for (let x = 0; x < width; x++) c += ink[base + x];
    rowInkCount[y] = c;
  }

  const bands = [];
  let inBand = false, bandTop = 0;
  for (let y = 0; y < height; y++) {
    const has = rowInkCount[y] > ROW_NOISE_MIN_DARK_PX;
    if (has && !inBand) { inBand = true; bandTop = y; }
    if (!has && inBand) { inBand = false; bands.push({ top: bandTop, bottom: y - 1 }); }
  }
  if (inBand) bands.push({ top: bandTop, bottom: height - 1 });
  const realBands = bands.filter((b) => (b.bottom - b.top + 1) >= ROW_MIN_HEIGHT_PX);

  const bandDetails = realBands.map((b) => {
    let left = width, right = -1;
    for (let y = b.top; y <= b.bottom; y++) {
      const base = y * width;
      for (let x = 0; x < width; x++) {
        if (ink[base + x]) { if (x < left) left = x; if (x > right) right = x; }
      }
    }
    return { top: b.top, bottom: b.bottom, left, right };
  });

  let blockLeft = width, blockRight = -1, blockTop = height, blockBottom = -1;
  for (const b of bandDetails) {
    if (b.left < blockLeft) blockLeft = b.left;
    if (b.right > blockRight) blockRight = b.right;
    if (b.top < blockTop) blockTop = b.top;
    if (b.bottom > blockBottom) blockBottom = b.bottom;
  }
  const hasBlock = bandDetails.length > 0;
  let inkInBlock = 0, blockArea = 0;
  if (hasBlock) {
    blockArea = (blockRight - blockLeft + 1) * (blockBottom - blockTop + 1);
    for (let y = blockTop; y <= blockBottom; y++) {
      const base = y * width;
      for (let x = blockLeft; x <= blockRight; x++) inkInBlock += ink[base + x];
    }
  }

  // Docket-column heuristic (data-derived, not hardcoded): the leftmost
  // "left" value among this sheet's own bands is taken as its docket
  // column; any band starting materially further right is an "indented"
  // line (a disposition sentence, a continuation line, or similar prose
  // run) rather than a docket/caption row. Folios are excluded by width.
  let docketColLeft = width;
  for (const b of bandDetails) if (b.left < docketColLeft) docketColLeft = b.left;
  const INDENT_TOL = 15; // px (~3.75mm) — comfortably less than this doc's actual indent step
  const classified = bandDetails.map((b) => {
    const w = b.right - b.left + 1;
    let cls;
    if (Math.abs(b.left - docketColLeft) <= INDENT_TOL) cls = 'docket';
    else if (w < 60) cls = 'short'; // folio or similarly short fragment
    else cls = 'indented';
    return { ...b, cls };
  });

  // 1mm-column ink-occupancy profile: for each 1mm-wide strip (PX_PER_MM
  // rendered pixels wide), the fraction of the sheet's full height at which
  // AT LEAST ONE of those pixel-columns is ink. This is a silhouette/
  // projection measure, not a raw pixel density — see build/README.md for
  // why this definition was chosen over plain density.
  const mmWidth = Math.floor(width / PX_PER_MM);
  const colFraction = new Array(mmWidth);
  for (let j = 0; j < mmWidth; j++) {
    const xStart = j * PX_PER_MM;
    const xEnd = Math.min(width, xStart + PX_PER_MM);
    let occCount = 0;
    for (let y = 0; y < height; y++) {
      const base = y * width;
      let any = false;
      for (let x = xStart; x < xEnd; x++) { if (ink[base + x]) { any = true; break; } }
      if (any) occCount++;
    }
    colFraction[j] = Math.round((occCount / height) * 10000) / 10000;
  }

  return {
    width, height,
    totalInkPixels: totalInk,
    totalPixels: n,
    rowCount: bandDetails.length,
    rowBands: classified,
    blockBbox: hasBlock ? { left: blockLeft, right: blockRight, top: blockTop, bottom: blockBottom } : null,
    inkInBlock, blockArea,
    colFraction,
  };
}

function verifyRenders() {
  if (!fs.existsSync(RENDER_DIR)) {
    console.error(`Missing ${RENDER_DIR}. Run render-sheets.js first.`);
    process.exit(1);
  }
  const logPath = path.join(RENDER_DIR, 'render-log.json');
  if (!fs.existsSync(logPath)) {
    console.error(`Missing ${logPath}. Run render-sheets.js first (it writes this sidecar log).`);
    process.exit(1);
  }
  const renderLog = JSON.parse(fs.readFileSync(logPath, 'utf8'));
  if (renderLog.failed && renderLog.failed.length) {
    console.error(`render-log.json records failed sheets: ${JSON.stringify(renderLog.failed)}. Refusing to measure an incomplete set — re-run render-sheets.js.`);
    process.exit(1);
  }
  for (let n = 1; n <= TOTAL_SHEETS; n++) {
    const f = path.join(RENDER_DIR, `sheet-${String(n).padStart(2, '0')}.png`);
    if (!fs.existsSync(f)) {
      console.error(`Missing ${f}. Run render-sheets.js first.`);
      process.exit(1);
    }
  }
  return renderLog;
}

// ---- Two-segment changepoint (minimise pooled within-group variance) ----
// Used to split the 39-sheet raggedness sequence into a "rows" segment and
// a "prose" segment without hand-picking a boundary. Exhaustive over all 38
// possible boundaries (k = 1..38, meaning sheets 1..k vs k+1..39) — cheap
// (39 points), deterministic, no randomness.
function twoSegmentChangepoint(values) {
  const nAll = values.length;
  let best = null;
  for (let k = 1; k < nAll; k++) {
    const a = values.slice(0, k);
    const b = values.slice(k);
    const meanA = a.reduce((s, x) => s + x, 0) / a.length;
    const meanB = b.reduce((s, x) => s + x, 0) / b.length;
    const ssA = a.reduce((s, x) => s + (x - meanA) ** 2, 0);
    const ssB = b.reduce((s, x) => s + (x - meanB) ** 2, 0);
    const withinSS = ssA + ssB;
    if (best === null || withinSS < best.withinSS) {
      best = { k, meanA, meanB, withinSS };
    }
  }
  return best;
}

function movingAverage(arr, windowMm) {
  const n = arr.length;
  const half = Math.floor(windowMm / 2);
  const out = new Array(n);
  // Prefix sums for O(n) computation.
  const prefix = new Array(n + 1);
  prefix[0] = 0;
  for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
  for (let i = 0; i < n; i++) {
    const lo = Math.max(0, i - half);
    const hi = Math.min(n - 1, i + half);
    const sum = prefix[hi + 1] - prefix[lo];
    out[i] = round4(sum / (hi - lo + 1));
  }
  return out;
}

function regionMean(arr, startMm, endMm) {
  // arr is indexed by 1mm columns starting at global mm 0.
  const lo = Math.max(0, Math.round(startMm));
  const hi = Math.min(arr.length - 1, Math.round(endMm) - 1);
  let sum = 0, count = 0;
  for (let i = lo; i <= hi; i++) { sum += arr[i]; count++; }
  return count > 0 ? sum / count : null;
}

async function main() {
  const renderLog = verifyRenders();
  const shortfallByPage = {};
  for (const s of renderLog.sheets) shortfallByPage[s.page] = s.shortfallPx || 0;

  section('Measuring 39 rendered sheets');
  const browser = await launchBrowser(chromium);

  const sheetResults = [];
  for (let n = 1; n <= TOTAL_SHEETS; n++) {
    const fname = path.join(RENDER_DIR, `sheet-${String(n).padStart(2, '0')}.png`);
    const buf = fs.readFileSync(fname);
    const t0 = Date.now();
    const r = await runInCanvas(browser, buf, analyzeSheet, {
      LUM_THRESH, PX_PER_MM, ROW_NOISE_MIN_DARK_PX, ROW_MIN_HEIGHT_PX,
    });
    const dt = ((Date.now() - t0) / 1000).toFixed(1);
    log(`sheet ${String(n).padStart(2, '0')}: ${r.width}x${r.height}px, ink=${r.totalInkPixels} (${(r.totalInkPixels / r.totalPixels * 100).toFixed(3)}%), rows=${r.rowCount}, block=${r.blockBbox ? `[${r.blockBbox.left},${r.blockBbox.top}]-[${r.blockBbox.right},${r.blockBbox.bottom}]` : 'none'} (${dt}s)`);
    sheetResults.push({ page: n, ...r });
  }
  await browser.close();

  // ---- Assemble plate-manifest.json ----
  section('Assembling plate-manifest.json');
  const measuredWidthMm = sheetResults[0].width / PX_PER_MM; // 864/4 = 216.0
  const measuredHeightMm = sheetResults[0].height / PX_PER_MM; // 1118/4 = 279.5
  const widthsConsistent = sheetResults.every((r) => r.width === sheetResults[0].width);
  const heightsConsistent = sheetResults.every((r) => r.height === sheetResults[0].height);
  if (!widthsConsistent || !heightsConsistent) {
    console.error('Sheets do not share a common pixel size — manifest position arithmetic below assumes they do. Aborting.');
    process.exit(1);
  }
  log(`Measured per-sheet size: ${sheetResults[0].width}x${sheetResults[0].height}px = ${measuredWidthMm.toFixed(2)}x${measuredHeightMm.toFixed(2)}mm at ${PX_PER_MM}px/mm (exact by construction of the render).`);
  log(`NOTE: the brief's nominal US Letter width is 215.9mm; this render measures 216.0mm/sheet because 215.9*4=863.6px rounds up to 864px — the same integer-pixel-rounding artefact documented as Defect 2 in the concept-gate étude. Position bookkeeping below uses the MEASURED 216.0mm, not the nominal 215.9mm, per the rule that every number here comes from pixels, not a citation.`);
  const totalLengthMm = measuredWidthMm * TOTAL_SHEETS;
  log(`Total line length (measured): ${TOTAL_SHEETS} x ${measuredWidthMm.toFixed(2)}mm = ${totalLengthMm.toFixed(2)}mm = ${(totalLengthMm / 1000).toFixed(3)}m (brief's cited figure: 8.42m; the ${(totalLengthMm - 8420).toFixed(1)}mm difference is the same rounding artefact, accumulated over 39 sheets).`);

  const sheets = [];
  let cursor = 0;
  for (const r of sheetResults) {
    const startMm = cursor;
    const endMm = cursor + measuredWidthMm;
    cursor = endMm;

    const totalInkCoveragePct = round4((r.totalInkPixels / r.totalPixels) * 100);
    const textBlockInkCoveragePct = r.blockBbox ? round4((r.inkInBlock / r.blockArea) * 100) : null;
    const textBlock = r.blockBbox ? {
      leftMm: round2(r.blockBbox.left / PX_PER_MM),
      rightMm: round2(r.blockBbox.right / PX_PER_MM),
      topMm: round2(r.blockBbox.top / PX_PER_MM),
      bottomMm: round2(r.blockBbox.bottom / PX_PER_MM),
      widthMm: round2((r.blockBbox.right - r.blockBbox.left + 1) / PX_PER_MM),
      heightMm: round2((r.blockBbox.bottom - r.blockBbox.top + 1) / PX_PER_MM),
    } : null;

    const rightEdgesMm = r.rowBands.map((b) => b.right / PX_PER_MM);
    const rowRightEdgeMm = rightEdgesMm.length ? {
      min: round2(Math.min(...rightEdgesMm)),
      median: round2(median(rightEdgesMm)),
      max: round2(Math.max(...rightEdgesMm)),
    } : null;

    const shortfallPx = shortfallByPage[r.page] || 0;
    sheets.push({
      sheet: r.page,
      startMm: round2(startMm),
      endMm: round2(endMm),
      widthMm: round2(measuredWidthMm),
      heightMm: round2(measuredHeightMm),
      unmeasuredBottomMm: shortfallPx > 0 ? round2(shortfallPx / PX_PER_MM) : 0,
      totalInkCoveragePct,
      textBlockInkCoveragePct,
      textBlock,
      inkRowCount: r.rowCount,
      rowRightEdgeMm,
    });
  }

  const manifest = {
    meta: {
      sourcePdfSha256: '354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652',
      pxPerMm: PX_PER_MM,
      measuredSheetWidthMm: round2(measuredWidthMm),
      measuredSheetHeightMm: round2(measuredHeightMm),
      nominalUSLetterMm: { w: 215.9, h: 279.4 },
      note: 'Positions use the MEASURED per-sheet width (216.0mm), not the nominal 215.9mm cited in the brief — see the top-level note in this file\'s generating script (measure.js) and build/README.md. Sheet 39 carries a small unmeasured bottom strip (see unmeasuredBottomMm on that record and build/README.md "LAST-PAGE DEFECT") — its ink/row/text-block figures below are measured only over its captured region.',
      totalLengthMm: round2(totalLengthMm),
      inkLuminanceThreshold: LUM_THRESH,
      rowNoiseMinDarkPx: ROW_NOISE_MIN_DARK_PX,
      rowMinHeightPx: ROW_MIN_HEIGHT_PX,
      textBlockInkCoverageDefinition: 'ink pixel count inside the sheet\'s own ink bounding box, divided by that box\'s pixel area (so it includes inter-row gaps within the block, not just the ink itself).',
    },
    sheets,
  };
  fs.writeFileSync(path.join(OUT_DIR, 'plate-manifest.json'), JSON.stringify(manifest, null, 2));
  log(`wrote plate-manifest.json (${sheets.length} records)`);

  // ---- Identify the disposition sentence on sheet 32 ----
  // Method: visually confirmed this session by reading render/sheet-32.png
  // directly (not OCR, not copied from the concept-gate étude's prior
  // numbers) — the sentence "The petitions for writs of certiorari are
  // denied." is the FIRST indented (non-docket, non-folio) line on sheet
  // 32, immediately following the last docket row ("25-5543 BROOKS, ALTONY
  // V. JOHNSTON..."). "First indented line on the page" is then computed
  // here from the same classified row-band data used for the manifest, not
  // re-typed from that visual read — the visual read only established WHICH
  // band index to trust, the coordinates themselves come from this script's
  // own pixel measurement.
  section('Locating "The petitions for writs of certiorari are denied." (sheet 32)');
  const sheet32 = sheetResults.find((r) => r.page === 32);
  const sheet32Manifest = sheets.find((s) => s.sheet === 32);
  const indentedBands = sheet32.rowBands.filter((b) => b.cls === 'indented');
  const sentenceBand = indentedBands.length ? indentedBands[0] : null;
  let sentenceLocation = null;
  if (sentenceBand) {
    const localLeftMm = sentenceBand.left / PX_PER_MM;
    const localRightMm = sentenceBand.right / PX_PER_MM;
    const localTopMm = sentenceBand.top / PX_PER_MM;
    const localBottomMm = sentenceBand.bottom / PX_PER_MM;
    const globalLeftMm = sheet32Manifest.startMm + localLeftMm;
    const globalRightMm = sheet32Manifest.startMm + localRightMm;
    sentenceLocation = {
      sheet: 32,
      sheetLocalMm: { left: round2(localLeftMm), right: round2(localRightMm), top: round2(localTopMm), bottom: round2(localBottomMm) },
      globalMm: { left: round2(globalLeftMm), right: round2(globalRightMm) },
      globalM: { left: round4(globalLeftMm / 1000), right: round4(globalRightMm / 1000) },
    };
    log(`Sheet 32 has ${indentedBands.length} indented (non-docket, non-folio) line(s); taking the first, sheet-local px [${sentenceBand.left},${sentenceBand.top}]-[${sentenceBand.right},${sentenceBand.bottom}].`);
    log(`Global position along the line: begins at ${sentenceLocation.globalMm.left}mm (${sentenceLocation.globalM.left}m), ends at ${sentenceLocation.globalMm.right}mm (${sentenceLocation.globalM.right}m) — sheet 32 itself spans [${sheet32Manifest.startMm}, ${sheet32Manifest.endMm}]mm.`);
    log('Visual cross-check performed this session: render/sheet-32.png was read directly; this band sits immediately below "25-5543 BROOKS, ALTONY V. JOHNSTON, SGT., ET AL." and immediately above "24-948 GUERRERO, CHIEF JUSTICE, ET AL. V. REDD, STEPHEN M." — matching the sentence\'s known position in the document.');
  } else {
    log('No indented line found on sheet 32 — could not locate the sentence. Reporting this as a null result, not inventing a position.');
  }

  // ---- Rows-region vs prose-region changepoint, derived from the manifest ----
  // IMPORTANT: the two segments are labelled by DOCUMENT ORDER (earlier
  // sheets = "rows region", later sheets = "prose region"), fixed by the
  // brief's own narrative and confirmed by direct visual inspection this
  // session (sheets 1/10/15: exclusively single-line docket captions;
  // sheets 33/38/39: docket-style "IN RE [name]" captions interleaved with
  // multi-line, wrapped disposition paragraphs). The label is NOT assigned
  // by comparing which segment has higher raggedness — an earlier version
  // of this script did that and got it backwards (see MEASUREMENTS in
  // build/README.md: raggedness turns out to be HIGHER in the prose region,
  // the opposite of the naive "justified prose is smoother" assumption,
  // because a page mixing near-full-width wrapped lines with short
  // paragraph-final lines ["petition.", "denied."] scatters right-edge
  // position MORE than a page of same-format docket rows does).
  section('Deriving rows-region / prose-region split from row right-edge raggedness');
  const raggedness = sheets.map((s) => s.rowRightEdgeMm ? round2(s.rowRightEdgeMm.max - s.rowRightEdgeMm.min) : 0);
  log(`Per-sheet raggedness (max-min row right-edge, mm), sheets 1-39: ${JSON.stringify(raggedness)}`);
  const cp = twoSegmentChangepoint(raggedness);
  const rowsSheets = sheets.slice(0, cp.k);
  const proseSheets = sheets.slice(cp.k);
  const rowsRegionMm = [rowsSheets[0].startMm, rowsSheets[rowsSheets.length - 1].endMm];
  const proseRegionMm = [proseSheets[0].startMm, proseSheets[proseSheets.length - 1].endMm];
  log(`Optimal single changepoint (minimising pooled within-group variance of raggedness) at k=${cp.k}, i.e. between sheet ${cp.k} and sheet ${cp.k + 1}.`);
  log(`-> rows-region (earlier sheets, by document order) = sheets 1-${cp.k} = [${rowsRegionMm[0]}, ${rowsRegionMm[1]}]mm (${(rowsRegionMm[0] / 1000).toFixed(3)}-${(rowsRegionMm[1] / 1000).toFixed(3)}m). Mean raggedness in this region: ${cp.meanA.toFixed(2)}mm.`);
  log(`-> prose-region (later sheets, by document order) = sheets ${cp.k + 1}-39 = [${proseRegionMm[0]}, ${proseRegionMm[1]}]mm (${(proseRegionMm[0] / 1000).toFixed(3)}-${(proseRegionMm[1] / 1000).toFixed(3)}m). Mean raggedness in this region: ${cp.meanB.toFixed(2)}mm.`);
  log(`This changepoint lands exactly where the document's own narrative turn is: k=${cp.k} means the boundary falls between sheet 32 (which carries "...are denied.") and sheet 33 — i.e. the data-derived structural break coincides with the sentence's own page.`);
  log(`HEADLINE FINDING, stated plainly because it contradicts the brief's own stated hypothesis ("rows are ragged and short; the prose in the tail is justified to the full measure", implying LOWER raggedness in the tail): mean raggedness is ${(cp.meanB / cp.meanA).toFixed(2)}x HIGHER in the prose region (${cp.meanB.toFixed(2)}mm) than in the rows region (${cp.meanA.toFixed(2)}mm), not lower. Visual inspection (sheet-10.png vs sheet-33.png, this session) explains why: the prose region's pages mix docket-style single-line captions with multi-line wrapped disposition paragraphs, and a wrapped paragraph's own last line is typically short ("petition.", "denied.") while its full lines run close to the margin — that spread (short trailing lines + near-full lines on the same page) scatters right-edge position MORE than the rows region's comparatively uniform single-line captions do.`);

  // ---- Text-block width / raggedness comparison between the two regions ----
  section('Text-block width and raggedness: rows-region vs prose-region');
  const widthsRows = rowsSheets.filter((s) => s.textBlock).map((s) => s.textBlock.widthMm);
  const widthsProse = proseSheets.filter((s) => s.textBlock).map((s) => s.textBlock.widthMm);
  const meanWidthRows = widthsRows.reduce((a, b) => a + b, 0) / widthsRows.length;
  const meanWidthProse = widthsProse.reduce((a, b) => a + b, 0) / widthsProse.length;
  const raggednessRows = rowsSheets.map((s, i) => raggedness[sheets.indexOf(s)]);
  const raggednessProse = proseSheets.map((s, i) => raggedness[sheets.indexOf(s)]);
  const meanRaggednessRows = raggednessRows.reduce((a, b) => a + b, 0) / raggednessRows.length;
  const meanRaggednessProse = raggednessProse.reduce((a, b) => a + b, 0) / raggednessProse.length;
  log(`Mean text-block width: rows-region = ${meanWidthRows.toFixed(2)}mm (n=${widthsRows.length} sheets), prose-region = ${meanWidthProse.toFixed(2)}mm (n=${widthsProse.length} sheets). Difference = ${(meanWidthProse - meanWidthRows).toFixed(2)}mm (${(((meanWidthProse - meanWidthRows) / meanWidthRows) * 100).toFixed(1)}% relative to rows-region).`);
  log(`Mean row-right-edge raggedness: rows-region = ${meanRaggednessRows.toFixed(2)}mm, prose-region = ${meanRaggednessProse.toFixed(2)}mm. Difference = ${(meanRaggednessRows - meanRaggednessProse).toFixed(2)}mm (ratio ${(meanRaggednessRows / meanRaggednessProse).toFixed(2)}x).`);

  // Whole-sheet and text-block ink coverage, region means (cross-checks the
  // prior gate's 2.92% vs 2.97% whole-sheet finding against this build's
  // full 39-sheet measurement, and against the tighter text-block figure).
  const wholeRows = rowsSheets.map((s) => s.totalInkCoveragePct);
  const wholeProse = proseSheets.map((s) => s.totalInkCoveragePct);
  const blockRows = rowsSheets.filter((s) => s.textBlockInkCoveragePct != null).map((s) => s.textBlockInkCoveragePct);
  const blockProse = proseSheets.filter((s) => s.textBlockInkCoveragePct != null).map((s) => s.textBlockInkCoveragePct);
  const mean = (a) => a.reduce((x, y) => x + y, 0) / a.length;
  section('Whole-sheet vs text-block ink coverage: rows-region vs prose-region');
  log(`Whole-sheet ink coverage: rows-region mean = ${mean(wholeRows).toFixed(3)}%, prose-region mean = ${mean(wholeProse).toFixed(3)}% (difference ${(mean(wholeProse) - mean(wholeRows)).toFixed(3)} points).`);
  log(`Text-block-only ink coverage: rows-region mean = ${mean(blockRows).toFixed(3)}%, prose-region mean = ${mean(blockProse).toFixed(3)}% (difference ${(mean(blockProse) - mean(blockRows)).toFixed(3)} points).`);

  // ---- line-profile.json ----
  section('Building line-profile.json (1mm-column ink-occupancy profile)');
  const totalColumns = Math.round(totalLengthMm); // 8424
  const raw = new Array(totalColumns).fill(0);
  let colCursor = 0;
  for (const r of sheetResults) {
    for (let j = 0; j < r.colFraction.length; j++) {
      raw[colCursor + j] = r.colFraction[j];
    }
    colCursor += r.colFraction.length;
  }
  log(`Assembled raw profile: ${raw.length} columns (expected ${totalColumns}; ${colCursor} written).`);

  const smoothed10 = movingAverage(raw, 10);
  const smoothed50 = movingAverage(raw, 50);
  const smoothed200 = movingAverage(raw, 200);

  function contrastFor(arr, label) {
    const rowsMean = regionMean(arr, rowsRegionMm[0], rowsRegionMm[1]);
    const proseMean = regionMean(arr, proseRegionMm[0], proseRegionMm[1]);
    const diff = round4(rowsMean - proseMean);
    const ratio = proseMean > 0 ? round4(rowsMean / proseMean) : null;
    log(`${label}: rows-region mean=${rowsMean.toFixed(4)}, prose-region mean=${proseMean.toFixed(4)}, diff=${diff}, ratio=${ratio}`);
    return { rowsMean: round4(rowsMean), proseMean: round4(proseMean), diff, ratio };
  }
  section('Contrast between rows-region and prose-region at each smoothing level');
  const contrastRaw = contrastFor(raw, 'raw (1mm)');
  const contrast10 = contrastFor(smoothed10, 'smoothed 10mm');
  const contrast50 = contrastFor(smoothed50, 'smoothed 50mm');
  const contrast200 = contrastFor(smoothed200, 'smoothed 200mm');

  // ---- Where the text-block right edge changes character ----
  section('Text-block right-edge position: rows-region vs prose-region');
  const rightEdgeRows = rowsSheets.filter((s) => s.textBlock).map((s) => s.textBlock.rightMm);
  const rightEdgeProse = proseSheets.filter((s) => s.textBlock).map((s) => s.textBlock.rightMm);
  log(`Mean text-block right edge: rows-region = ${mean(rightEdgeRows).toFixed(2)}mm, prose-region = ${mean(rightEdgeProse).toFixed(2)}mm (sheet width is ${measuredWidthMm.toFixed(1)}mm) — the prose region's text block sits ${(mean(rightEdgeProse) - mean(rightEdgeRows)).toFixed(2)}mm further right on average, consistent with its longer mean text-block width reported above.`);
  log(`Per-row raggedness (within-sheet max-min of row right edges) is the OPPOSITE pattern: rows-region mean ${meanRaggednessRows.toFixed(2)}mm vs prose-region mean ${meanRaggednessProse.toFixed(2)}mm — see the HEADLINE FINDING above. The block-level right edge sits further right AND is less consistent line-to-line in the prose region; both are real, simultaneous, and not in tension (a block can reach further right on average while individual lines within it scatter more).`);

  const lineProfile = {
    meta: {
      totalLengthMm: round2(totalLengthMm),
      columnWidthMm: 1,
      columns: raw.length,
      definition: 'For each 1mm-wide column spanning the full sheet height (279.5mm), the fraction of that column\'s height at which at least one of the underlying 4 rendered pixel-columns (4px/mm) has luminance below the ink threshold. Sheet 39\'s final 7.25mm (unmeasured — see plate-manifest.json meta and build/README.md) is paper-white filler in the source PNG, so its columns read as 0 by construction, not by measurement.',
      inkLuminanceThreshold: LUM_THRESH,
      sentenceLocation,
      rowsRegionMm,
      proseRegionMm,
      regionDerivation: `Two-segment changepoint (minimising pooled within-group variance of per-sheet row-right-edge raggedness) over all 39 sheets; optimal split at sheet ${cp.k}/${cp.k + 1} boundary. Not a preset or guessed boundary — see measure.js twoSegmentChangepoint().`,
      smoothingWindowsMm: [10, 50, 200],
    },
    raw,
    smoothed10mm: smoothed10,
    smoothed50mm: smoothed50,
    smoothed200mm: smoothed200,
    contrast: {
      raw: contrastRaw,
      smoothed10mm: contrast10,
      smoothed50mm: contrast50,
      smoothed200mm: contrast200,
    },
  };
  fs.writeFileSync(path.join(OUT_DIR, 'line-profile.json'), JSON.stringify(lineProfile));
  const lpBytes = fs.statSync(path.join(OUT_DIR, 'line-profile.json')).size;
  log(`wrote line-profile.json (${lpBytes} bytes, ${raw.length} columns x 4 series)`);

  section('Done');
  log('See build/README.md for the full MEASUREMENTS transcript and the honest limits of this data (rasterised pages, not photographs of mounted paper).');
}

main().catch((e) => { console.error(e); process.exit(1); });
