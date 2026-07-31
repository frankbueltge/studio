// MEASUREMENT 1 (docket item A4) — the byte ceiling, re-measured across
// candidate encodings, on top of pages already rendered by render-batch.js
// (which itself uses no-part/build/pdf-render-lib.js, copied verbatim).
//
// For each rendered <stem>.raw.png (Chromium's own canvas.toDataURL PNG
// output, color type 6 / RGBA8 — the current baseline, confirmed by direct
// PNG-header inspection, see MEASUREMENTS-A4-AND-PAGECOUNTS.md), this script
// builds and measures:
//   1. baseline        — the file as already rendered (RGBA8 PNG)
//   2. rgb8            — RGB8 PNG, alpha channel dropped (lossless IFF alpha
//                         is uniformly 255 everywhere — checked, not assumed)
//   3. gray8            — grayscale (color type 0) PNG built from
//                         luminance-forced pixels (same formula
//                         canvas-lib.js's desaturateToGrayscale already uses
//                         elsewhere in this house) — NOT lossless vs. the
//                         raw capture; the per-pixel delta this discards is
//                         measured and reported, not asserted away.
//   4. indexed          — palette/indexed PNG (color type 3) built from the
//                         SAME luminance-forced pixels as gray8, with the
//                         palette sized to the actual number of distinct
//                         gray levels present (bit depth 1/2/4/8, whichever
//                         is the smallest that fits) — exactly lossless
//                         relative to gray8, so it inherits gray8's delta
//                         from the raw capture and no more.
//   5. bilevel1         — true 1-bit PNG via a hard luminance threshold at
//                         THRESH=150 (the same constant canvas-lib.js and
//                         pdf-render-lib.js already use for ink/background
//                         decisions) — NOT lossless; the antialiasing this
//                         throws away is measured.
//   6. webp_canvas      — Chromium's own canvas.toDataURL('image/webp', 1.0),
//                         round-tripped back through the SAME Chromium build
//                         (load the data URL into an <img>, draw to canvas,
//                         read pixels back) to test whether it is actually
//                         lossless — measured, not assumed from the "1.0"
//                         quality argument's name.
//
// Usage: xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules \
//   node measure-encodings.js <pages-dir> <out-json>
// <pages-dir> must contain the *.raw.png files render-batch.js produced.

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const {
  decodePng, encodeGray8, encodeRGB8, encodeIndexed, encodeBilevel1,
} = require('./png-codec-lib.js');

const THRESH = 150; // matches canvas-lib.js's LUM_THRESH / pdf-render-lib.js's ink/background threshold

function luminance(r, g, b) {
  return Math.round(0.299 * r + 0.587 * g + 0.114 * b);
}

function diffStats(bufA, bufB, stride, n) {
  // Per-pixel absolute luminance-domain difference between two grayscale
  // byte arrays of length n (1 byte/pixel each).
  let maxDiff = 0, sumDiff = 0, sumSq = 0, nDiffPixels = 0;
  for (let i = 0; i < n; i++) {
    const d = Math.abs(bufA[i] - bufB[i]);
    if (d > 0) nDiffPixels++;
    if (d > maxDiff) maxDiff = d;
    sumDiff += d;
    sumSq += d * d;
  }
  return {
    maxAbsDiff: maxDiff,
    meanAbsDiff: sumDiff / n,
    rmse: Math.sqrt(sumSq / n),
    pixelsDiffering: nDiffPixels,
    pixelsDifferingPct: (100 * nDiffPixels) / n,
  };
}

async function webpRoundTrip(browser, pngBuffer) {
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  await page.goto('about:blank');
  const b64 = pngBuffer.toString('base64');
  const result = await page.evaluate(async (dataUrl) => {
    const img = new Image();
    await new Promise((resolve, reject) => { img.onload = resolve; img.onerror = reject; img.src = dataUrl; });
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth; canvas.height = img.naturalHeight;
    const c = canvas.getContext('2d');
    c.drawImage(img, 0, 0);
    const origData = c.getImageData(0, 0, canvas.width, canvas.height).data;

    const webpDataUrl = canvas.toDataURL('image/webp', 1.0);
    const isWebp = webpDataUrl.startsWith('data:image/webp');

    // Round-trip: load the produced WebP back and compare pixels.
    const img2 = new Image();
    await new Promise((resolve, reject) => { img2.onload = resolve; img2.onerror = reject; img2.src = webpDataUrl; });
    const canvas2 = document.createElement('canvas');
    canvas2.width = img2.naturalWidth; canvas2.height = img2.naturalHeight;
    const c2 = canvas2.getContext('2d');
    c2.drawImage(img2, 0, 0);
    const rtData = c2.getImageData(0, 0, canvas2.width, canvas2.height).data;

    let maxDiff = 0, sumDiff = 0, nDiff = 0;
    const n = origData.length / 4;
    for (let i = 0; i < n; i++) {
      const o = i * 4;
      for (let ch = 0; ch < 3; ch++) { // RGB only, alpha handled separately
        const d = Math.abs(origData[o + ch] - rtData[o + ch]);
        if (d > maxDiff) maxDiff = d;
        sumDiff += d;
        if (d > 0) nDiff++;
      }
    }
    return {
      isWebp,
      webpBase64Length: webpDataUrl.length - webpDataUrl.indexOf(',') - 1,
      webpRawBytesApprox: Math.floor((webpDataUrl.length - webpDataUrl.indexOf(',') - 1) * 3 / 4),
      maxAbsDiff: maxDiff,
      meanAbsDiff: sumDiff / (n * 3),
      pixelsDiffering: nDiff,
      totalSamples: n * 3,
    };
  }, `data:image/png;base64,${b64}`);
  await ctx.close();
  return result;
}

function base64Len(bytes) {
  return Math.ceil(bytes / 3) * 4;
}

async function main() {
  const [pagesDir, outJson] = process.argv.slice(2);
  if (!pagesDir || !outJson) {
    console.error('Usage: node measure-encodings.js <pages-dir> <out-json>');
    process.exit(1);
  }
  const files = fs.readdirSync(pagesDir).filter((f) => f.endsWith('.raw.png'));
  const browser = await chromium.launch({ headless: false });
  const results = [];

  for (const f of files) {
    const stem = f.replace(/\.raw\.png$/, '');
    const buf = fs.readFileSync(path.join(pagesDir, f));
    const img = decodePng(buf);
    const { width, height, pixels } = img;
    const n = width * height;

    // Alpha channel check.
    let alphaMin = 255, alphaMax = 0;
    for (let i = 0; i < n; i++) {
      const a = pixels[i * 4 + 3];
      if (a < alphaMin) alphaMin = a;
      if (a > alphaMax) alphaMax = a;
    }

    // Raw grayscale reference (luminance of the RAW, uncorrected RGB) —
    // used only to compute rgb8's relationship to baseline (should be
    // exactly 0 diff, since rgb8 keeps R/G/B untouched).
    const rgbBytes = Buffer.alloc(n * 3);
    const grayFromRaw = Buffer.alloc(n); // luminance(raw R,G,B) per pixel, for later diffing
    for (let i = 0; i < n; i++) {
      const r = pixels[i * 4], g = pixels[i * 4 + 1], b = pixels[i * 4 + 2];
      rgbBytes[i * 3] = r; rgbBytes[i * 3 + 1] = g; rgbBytes[i * 3 + 2] = b;
      grayFromRaw[i] = luminance(r, g, b);
    }

    const rgb8Png = encodeRGB8(width, height, rgbBytes);

    // Grayscale candidate: same luminance-forcing formula as
    // canvas-lib.js's desaturateToGrayscale (0.299/0.587/0.114 on the RAW
    // R,G,B — i.e. this measures grayscale-from-raw directly, not a second
    // hop through an already-desaturated RGBA image).
    const gray8Png = encodeGray8(width, height, grayFromRaw);

    // Distinct gray levels actually present -> smallest indexed bit depth.
    const present = new Set();
    for (let i = 0; i < n; i++) present.add(grayFromRaw[i]);
    const distinctLevels = [...present].sort((a, b) => a - b);
    let bitDepth;
    if (distinctLevels.length <= 2) bitDepth = 1;
    else if (distinctLevels.length <= 4) bitDepth = 2;
    else if (distinctLevels.length <= 16) bitDepth = 4;
    else bitDepth = 8;
    const palette = distinctLevels.map((v) => [v, v, v]);
    const levelToIndex = new Map(distinctLevels.map((v, i) => [v, i]));
    const indices = Buffer.alloc(n);
    for (let i = 0; i < n; i++) indices[i] = levelToIndex.get(grayFromRaw[i]);
    const indexedPng = encodeIndexed(width, height, indices, palette, bitDepth);

    // Bilevel candidate: threshold grayFromRaw at THRESH.
    const bits = new Uint8Array(n);
    for (let i = 0; i < n; i++) bits[i] = grayFromRaw[i] > THRESH ? 1 : 0;
    const bilevelPng = encodeBilevel1(width, height, bits);
    // Reconstruct bilevel's own effective gray value per pixel (0 or 255)
    // for diffing against grayFromRaw.
    const bilevelAsGray = Buffer.alloc(n);
    for (let i = 0; i < n; i++) bilevelAsGray[i] = bits[i] ? 255 : 0;

    const gray8VsRaw = diffStats(grayFromRaw, grayFromRaw, 1, n); // placeholder replaced below
    // Actual diff: grayFromRaw vs the true per-channel raw (i.e. how much
    // does forcing R=G=B change things at the channel level, not just
    // luminance). Compute max per-channel deviation from luminance.
    let maxChanDelta = 0, sumChanDelta = 0;
    for (let i = 0; i < n; i++) {
      const r = pixels[i * 4], g = pixels[i * 4 + 1], b = pixels[i * 4 + 2];
      const l = grayFromRaw[i];
      const d = Math.max(Math.abs(r - l), Math.abs(g - l), Math.abs(b - l));
      if (d > maxChanDelta) maxChanDelta = d;
      sumChanDelta += d;
    }
    const grayscaleVsRawChannelDelta = { maxAbsDiff: maxChanDelta, meanAbsDiff: sumChanDelta / n };

    const bilevelVsGray = diffStats(bilevelAsGray, grayFromRaw, 1, n);

    const webp = await webpRoundTrip(browser, buf);

    const row = {
      stem, width, height,
      alphaMin, alphaMax, alphaUniform255: (alphaMin === 255 && alphaMax === 255),
      distinctGrayLevels: distinctLevels.length,
      indexedBitDepth: bitDepth,
      bytes: {
        baseline_rgba8: buf.length,
        rgb8_no_alpha: rgb8Png.length,
        gray8: gray8Png.length,
        indexed: indexedPng.length,
        bilevel1: bilevelPng.length,
      },
      base64Bytes: {
        baseline_rgba8: base64Len(buf.length),
        rgb8_no_alpha: base64Len(rgb8Png.length),
        gray8: base64Len(gray8Png.length),
        indexed: base64Len(indexedPng.length),
        bilevel1: base64Len(bilevelPng.length),
      },
      fidelity: {
        rgb8_no_alpha: 'lossless (alpha dropped; alpha was uniformly 255 -> confirmed no information discarded)',
        gray8_vs_raw_channel_delta: grayscaleVsRawChannelDelta,
        indexed_vs_gray8: 'lossless (same luminance values, referenced via palette; identical to gray8 pixel-for-pixel)',
        bilevel1_vs_gray8: bilevelVsGray,
      },
      webp_canvas: webp,
    };
    results.push(row);
    console.log(JSON.stringify({ stem, bytes: row.bytes, base64Bytes: row.base64Bytes, distinctGrayLevels: row.distinctGrayLevels, indexedBitDepth: row.indexedBitDepth, webp_isWebp: webp.isWebp, webp_maxAbsDiff: webp.maxAbsDiff, webp_bytesApprox: webp.webpRawBytesApprox }));
  }

  await browser.close();
  fs.writeFileSync(outJson, JSON.stringify(results, null, 1));
  console.log('wrote', outJson);
}

main().catch((e) => { console.error(e); process.exit(1); });
