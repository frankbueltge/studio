// NO PART — production increment 01. Composes line-strip.png: the 39
// rendered sheets butted edge to edge in order, downsampled to a low, flat
// scale. No wall, no shadow, no invented light, no composed room, no
// annotation, no marker, no colour — just the rendered document at low
// scale, exactly as the brief specifies.
//
// Usage:
//   xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node compose-strip.js
//
// Requires render/sheet-01.png ... sheet-39.png (run render-sheets.js
// first).

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { launchBrowser, runInCanvas } = require('./canvas-lib.js');

const RENDER_DIR = path.resolve(__dirname, '..', 'render');
const OUT_PATH = path.resolve(__dirname, '..', 'line-strip.png');
const TOTAL_SHEETS = 39;
const SOURCE_PX_PER_MM = 4;
const MAX_BYTES = 1.5 * 1024 * 1024;

function log(...args) { console.log(...args); }
function section(title) { console.log('\n=== ' + title + ' ==='); }

// Composite function run inside the browser: draws each source sheet
// (already loaded as Image elements) into one output canvas at the given
// downsample scale, left to right, no gap, no fill colour anywhere except
// the sheets' own rendered pixels.
async function composeAt(browser, sheetBuffers, scalePxPerMm) {
  const ctxPage = await browser.newContext();
  const page = await ctxPage.newPage();
  await page.goto('about:blank');
  const dataUrls = sheetBuffers.map((b) => 'data:image/png;base64,' + b.toString('base64'));
  const outB64 = await page.evaluate(async ({ dataUrls, sourcePxPerMm, scalePxPerMm }) => {
    const imgs = [];
    for (const url of dataUrls) {
      const img = new Image();
      await new Promise((resolve, reject) => { img.onload = resolve; img.onerror = reject; img.src = url; });
      imgs.push(img);
    }
    // Per-sheet output size, computed from each sheet's own measured pixel
    // size (not assumed) — every sheet in this render was confirmed
    // identical (864x1118px) by render-sheets.js, but this loop doesn't
    // assume that, it reads each image's own dimensions.
    let totalW = 0;
    const outSizes = imgs.map((img) => {
      const w = Math.round(img.naturalWidth * (scalePxPerMm / sourcePxPerMm));
      const h = Math.round(img.naturalHeight * (scalePxPerMm / sourcePxPerMm));
      totalW += w;
      return { w, h };
    });
    const outH = Math.max(...outSizes.map((s) => s.h));
    const canvas = document.createElement('canvas');
    canvas.width = totalW;
    canvas.height = outH;
    const c = canvas.getContext('2d');
    c.imageSmoothingEnabled = true;
    c.imageSmoothingQuality = 'high';
    let x = 0;
    for (let i = 0; i < imgs.length; i++) {
      const { w, h } = outSizes[i];
      c.drawImage(imgs[i], 0, 0, imgs[i].naturalWidth, imgs[i].naturalHeight, x, 0, w, h);
      x += w;
    }
    return { png: canvas.toDataURL('image/png').split(',')[1], width: canvas.width, height: canvas.height };
  }, { dataUrls, sourcePxPerMm: SOURCE_PX_PER_MM, scalePxPerMm });
  await ctxPage.close();
  return { buffer: Buffer.from(outB64.png, 'base64'), width: outB64.width, height: outB64.height };
}

async function main() {
  section('Loading rendered sheets');
  const sheetBuffers = [];
  for (let n = 1; n <= TOTAL_SHEETS; n++) {
    const f = path.join(RENDER_DIR, `sheet-${String(n).padStart(2, '0')}.png`);
    if (!fs.existsSync(f)) {
      console.error(`Missing ${f}. Run render-sheets.js first.`);
      process.exit(1);
    }
    sheetBuffers.push(fs.readFileSync(f));
  }
  log(`Loaded ${sheetBuffers.length} sheets.`);

  const browser = await launchBrowser(chromium);

  section('Composing at 1 px/mm');
  let { buffer, width, height } = await composeAt(browser, sheetBuffers, 1);
  log(`1px/mm composite: ${width}x${height}px, ${buffer.length} bytes (${(buffer.length / 1024 / 1024).toFixed(2)}MB).`);

  let finalScale = 1;
  if (buffer.length > MAX_BYTES) {
    log(`Exceeds ${(MAX_BYTES / 1024 / 1024).toFixed(2)}MB budget — rebuilding at 0.5px/mm per the brief's fallback instruction.`);
    section('Composing at 0.5 px/mm');
    ({ buffer, width, height } = await composeAt(browser, sheetBuffers, 0.5));
    finalScale = 0.5;
    log(`0.5px/mm composite: ${width}x${height}px, ${buffer.length} bytes (${(buffer.length / 1024 / 1024).toFixed(2)}MB).`);
  }

  await browser.close();

  fs.writeFileSync(OUT_PATH, buffer);
  section('Done');
  log(`wrote ${OUT_PATH}: ${width}x${height}px at ${finalScale}px/mm, ${buffer.length} bytes (${(buffer.length / 1024 / 1024).toFixed(2)}MB).`);
  log('Nothing added: no wall, no shadow, no annotation, no marker, no colour — this is a straight downsample of the 39 sheets butted in order, sheet 1 at the left.');
}

main().catch((e) => { console.error(e); process.exit(1); });
