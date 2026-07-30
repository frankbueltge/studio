// NO PART — severed-read stimulus, session 49 (the denominator cell).
// Crops sheet 32 from just below the mass sentence to the sheet's own
// bottom edge, and sheet 37 from the sheet's own top edge to just above
// the "HABEAS CORPUS DENIED" heading; copies sheets 33-36 through whole,
// unmodified. No glyph added, nothing re-typeset, nothing re-ordered,
// nothing scaled, no annotation, no border — a crop and a copy, full sheet
// width preserved in every output.
//
// The two cut lines are DERIVED, not chosen by eye: each is the midpoint
// between two printed rows' own PDF baselines, read straight from the
// source PDF's content streams by row-geometry.py (which imports
// extract-rows.py, the committed extractor, and prints the requested
// rows' {x, y} in PDF points — no coordinate here is invented, eyeballed,
// or copied from a prior run's stdout).
//
// Usage:
//   xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node crop-tail-49.js
//
// Requires render/sheet-32.png ... sheet-37.png (run render-sheets.js
// first — see build/README.md).

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');
const { launchBrowser, runInCanvas } = require('./canvas-lib.js');

const RENDER_DIR = path.resolve(__dirname, '..', 'render');
const OUT_DIR = path.resolve(__dirname, '..', 'reads-49', 'stimulus');

const PX_PER_MM = 4;          // the same target scale render-sheets.js rasterised at
const PT_TO_MM = 25.4 / 72;   // 1 pt = 1/72 inch, 1 inch = 25.4mm — the only conversion constant used
const PX_PER_PT = PX_PER_MM * PT_TO_MM;

// The four rows that fix the two cut lines, by row_idx into
// extract-rows.py's own all_lines (the same indices the pre-registration
// cites): 1756 the mass sentence itself (sheet 32); 1757 the first printed
// row after it (sheet 32, docket "24-948", the first of the 31 entries);
// 1953 the last printed row before the heading (sheet 37, the closing line
// of entry 31's disposition); 1954 "HABEAS CORPUS DENIED" itself (sheet 37).
const ROW_INDICES = [1756, 1757, 1953, 1954];

function log(...args) { console.log(...args); }
function section(title) { console.log('\n=== ' + title + ' ==='); }

function getRowGeometry() {
  const out = execFileSync('python3', ['row-geometry.py', ...ROW_INDICES.map(String)], {
    cwd: __dirname,
    encoding: 'utf8',
  });
  return JSON.parse(out);
}

// Read a PNG's own width/height straight from its IHDR chunk (PNG spec:
// 8-byte signature, then a 4-byte length + 4-byte type + data chunk, IHDR
// always first — width at byte offset 16, height at offset 20, both
// big-endian uint32). Plain buffer arithmetic on the file's own bytes, not
// a decode — there is no image library on this machine, and none is needed
// just to read a header.
function pngDims(buf) {
  if (buf.readUInt32BE(0) !== 0x89504e47 || buf.toString('ascii', 12, 16) !== 'IHDR') {
    throw new Error('not a PNG with IHDR as its first chunk');
  }
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
}

// Crop sheet PNG `srcPath` to pixel rows [yTop, yBottom) (0-indexed from
// the sheet's own top edge), full width, no resampling (1:1, source scale
// == dest scale), no fill, no annotation. Writes the result to `destPath`
// and returns its {width, height}.
async function cropSheet(browser, srcPath, destPath, yTop, yBottom) {
  const buf = fs.readFileSync(srcPath);
  const png64 = await runInCanvas(browser, buf, (ctx, canvas, { yTop, yBottom }) => {
    const width = canvas.width;
    const height = yBottom - yTop;
    const out = document.createElement('canvas');
    out.width = width;
    out.height = height;
    const octx = out.getContext('2d');
    octx.drawImage(canvas, 0, yTop, width, height, 0, 0, width, height);
    return out.toDataURL('image/png').split(',')[1];
  }, { yTop, yBottom });
  const outBuf = Buffer.from(png64, 'base64');
  fs.writeFileSync(destPath, outBuf);
  return pngDims(outBuf);
}

async function main() {
  section('Row geometry (row-geometry.py, importing extract-rows.py)');
  const geometry = getRowGeometry();
  log(JSON.stringify(geometry, null, 1));
  const bySheetRow = {};
  for (const r of geometry.rows) bySheetRow[r.row_idx] = r;

  const massRow = bySheetRow[1756];
  const nextRow = bySheetRow[1757];
  const prevRow = bySheetRow[1953];
  const headRow = bySheetRow[1954];

  const pageHeightPt32 = geometry.pages_mediabox_h_pt[String(massRow.sheet)];
  const pageHeightPt37 = geometry.pages_mediabox_h_pt[String(headRow.sheet)];

  // Cut 1 (sheet 32): midpoint, in PDF points, between the mass sentence's
  // own baseline and the next printed row's baseline; converted to a pixel
  // row measured from the sheet's own top edge. Pixel y grows DOWN; PDF y
  // grows UP; hence (pageHeight - y).
  const cut1Pt = (massRow.y + nextRow.y) / 2;
  const cut1Px = (pageHeightPt32 - cut1Pt) * PX_PER_PT;
  const cut1PxRounded = Math.round(cut1Px);

  // Cut 2 (sheet 37): midpoint between the last preceding printed row's
  // baseline and the heading's own baseline.
  const cut2Pt = (prevRow.y + headRow.y) / 2;
  const cut2Px = (pageHeightPt37 - cut2Pt) * PX_PER_PT;
  const cut2PxRounded = Math.round(cut2Px);

  section('Computed cut lines');
  log(`Conversion used: px = (pageHeight_pt - y_pt) * PX_PER_MM(${PX_PER_MM}) * (25.4/72), i.e. px_per_pt = ${PX_PER_PT}`);
  log(`Sheet ${massRow.sheet} MediaBox height: ${pageHeightPt32}pt (read directly, not assumed).`);
  log(`  mass sentence (row ${massRow.row_idx}, ${JSON.stringify(massRow.text)}) baseline y=${massRow.y}pt -> ${(pageHeightPt32 - massRow.y) * PX_PER_PT}px from top`);
  log(`  next row (row ${nextRow.row_idx}, ${JSON.stringify(nextRow.text)}) baseline y=${nextRow.y}pt -> ${(pageHeightPt32 - nextRow.y) * PX_PER_PT}px from top`);
  log(`  midpoint: ${cut1Pt}pt -> ${cut1Px}px -> rounded ${cut1PxRounded}px`);
  log(`Sheet ${headRow.sheet} MediaBox height: ${pageHeightPt37}pt (read directly, not assumed).`);
  log(`  prev row (row ${prevRow.row_idx}, ${JSON.stringify(prevRow.text)}) baseline y=${prevRow.y}pt -> ${(pageHeightPt37 - prevRow.y) * PX_PER_PT}px from top`);
  log(`  heading (row ${headRow.row_idx}, ${JSON.stringify(headRow.text)}) baseline y=${headRow.y}pt -> ${(pageHeightPt37 - headRow.y) * PX_PER_PT}px from top`);
  log(`  midpoint: ${cut2Pt}pt -> ${cut2Px}px -> rounded ${cut2PxRounded}px`);

  fs.mkdirSync(OUT_DIR, { recursive: true });

  const sheet32Path = path.join(RENDER_DIR, 'sheet-32.png');
  const sheet37Path = path.join(RENDER_DIR, 'sheet-37.png');
  for (const p of [sheet32Path, sheet37Path, ...[33, 34, 35, 36].map((n) => path.join(RENDER_DIR, `sheet-${n}.png`))]) {
    if (!fs.existsSync(p)) {
      console.error(`Missing ${p}. Run render-sheets.js first.`);
      process.exit(1);
    }
  }

  const sheet32Dims = pngDims(fs.readFileSync(sheet32Path));
  const sheet37Dims = pngDims(fs.readFileSync(sheet37Path));
  log(`Sheet 32 rendered size: ${sheet32Dims.width}x${sheet32Dims.height}px.`);
  log(`Sheet 37 rendered size: ${sheet37Dims.width}x${sheet37Dims.height}px.`);

  const browser = await launchBrowser(chromium);
  const manifest = [];

  section('Writing stimulus');

  // 01 — sheet 32, from just below the mass sentence to the bottom edge.
  const dims01 = await cropSheet(
    browser, sheet32Path, path.join(OUT_DIR, '01-sheet-32-crop.png'),
    cut1PxRounded, sheet32Dims.height
  );
  log(`01-sheet-32-crop.png: ${dims01.width}x${dims01.height}px (source sheet 32 rows [${cut1PxRounded}, ${sheet32Dims.height}))`);
  manifest.push({ file: '01-sheet-32-crop.png', ...dims01, sourceSheet: 32, sourceYRange: [cut1PxRounded, sheet32Dims.height] });

  // 02-05 — sheets 33-36, whole, unmodified: a straight byte copy (not a
  // canvas round-trip), so nothing about them can change.
  for (const n of [33, 34, 35, 36]) {
    const src = path.join(RENDER_DIR, `sheet-${n}.png`);
    const destName = `0${n - 31}-sheet-${n}.png`;
    const dest = path.join(OUT_DIR, destName);
    fs.copyFileSync(src, dest);
    const dims = pngDims(fs.readFileSync(dest));
    log(`${destName}: ${dims.width}x${dims.height}px, whole sheet ${n}, unmodified (byte-identical copy of render/sheet-${n}.png)`);
    manifest.push({ file: destName, ...dims, sourceSheet: n, sourceYRange: [0, dims.height] });
  }

  // 06 — sheet 37, from the top edge to just above the heading.
  const dims06 = await cropSheet(
    browser, sheet37Path, path.join(OUT_DIR, '06-sheet-37-crop.png'),
    0, cut2PxRounded
  );
  log(`06-sheet-37-crop.png: ${dims06.width}x${dims06.height}px (source sheet 37 rows [0, ${cut2PxRounded}))`);
  manifest.push({ file: '06-sheet-37-crop.png', ...dims06, sourceSheet: 37, sourceYRange: [0, cut2PxRounded] });

  await browser.close();

  section('Done');
  log(`wrote 6 PNGs to ${OUT_DIR}`);
  log(JSON.stringify(manifest, null, 1));
}

main().catch((e) => { console.error(e); process.exit(1); });
