// Supplementary to measure-encodings.js: measures Chromium's own canvas
// lossless WebP (VP8X container wrapping a VP8L payload — confirmed by
// direct RIFF chunk inspection, see MEASUREMENTS-A4-AND-PAGECOUNTS.md) on
// the ALREADY colour-cast-corrected ("desaturated to grayscale", R=G=B
// forced) image, i.e. the *.gray.png files render-batch.js also writes.
//
// Why a second pass, separate from measure-encodings.js: that script tested
// canvas.toDataURL('image/webp', 1.0) on the RAW rendering (with its real,
// measured colour cast, max per-channel delta ~97-98/255) and found the
// result dramatically LARGER than the baseline PNG -- a genuinely
// surprising, measured fact, not an assumption. This script isolates
// whether that blowup is caused by the colour cast defeating WebP's
// cross-channel prediction (VP8L predicts each channel from the others;
// a real, non-trivial decorrelation between channels should hurt it
// specifically), by re-running the identical encode+round-trip on content
// that is already R=G=B everywhere.
//
// Usage: xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules \
//   node measure-webp-on-gray.js <pages-dir> <out-json>
// <pages-dir> must contain the *.gray.png files render-batch.js produced.

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

function base64Len(bytes) { return Math.ceil(bytes / 3) * 4; }

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
      for (let ch = 0; ch < 4; ch++) { // RGBA this time -- gray.png is fully opaque too
        const d = Math.abs(origData[o + ch] - rtData[o + ch]);
        if (d > maxDiff) maxDiff = d;
        sumDiff += d;
        if (d > 0) nDiff++;
      }
    }
    return {
      webpBase64: webpDataUrl.slice(webpDataUrl.indexOf(',') + 1),
      maxAbsDiff: maxDiff,
      meanAbsDiff: sumDiff / (n * 4),
      pixelsDiffering: nDiff,
      totalSamples: n * 4,
    };
  }, `data:image/png;base64,${b64}`);
  await ctx.close();
  return result;
}

async function main() {
  const [pagesDir, outJson] = process.argv.slice(2);
  const files = fs.readdirSync(pagesDir).filter((f) => f.endsWith('.gray.png'));
  const browser = await chromium.launch({ headless: false });
  const results = [];
  for (const f of files) {
    const stem = f.replace(/\.gray\.png$/, '');
    const buf = fs.readFileSync(path.join(pagesDir, f));
    const rt = await webpRoundTrip(browser, buf);
    const webpBuf = Buffer.from(rt.webpBase64, 'base64');
    // Confirm the RIFF/WEBP chunk structure directly, rather than trusting
    // a "1.0 == lossless" assumption.
    let fourccInner = null;
    if (webpBuf.toString('ascii', 0, 4) === 'RIFF' && webpBuf.toString('ascii', 8, 12) === 'WEBP') {
      let off = 12;
      while (off < webpBuf.length) {
        const fourcc = webpBuf.toString('ascii', off, off + 4);
        const size = webpBuf.readUInt32LE(off + 4);
        if (fourcc === 'VP8L' || fourcc === 'VP8 ') { fourccInner = fourcc.trim(); break; }
        off += 8 + size + (size % 2);
      }
    }
    const row = {
      stem,
      grayPngBytes: buf.length,
      webpBytes: webpBuf.length,
      webpBase64Bytes: base64Len(webpBuf.length),
      grayPngBase64Bytes: base64Len(buf.length),
      innerCodec: fourccInner,
      roundTripMaxAbsDiff: rt.maxAbsDiff,
      roundTripMeanAbsDiff: rt.meanAbsDiff,
      roundTripPixelsDiffering: rt.pixelsDiffering,
    };
    results.push(row);
    console.log(JSON.stringify(row));
  }
  await browser.close();
  fs.writeFileSync(outJson, JSON.stringify(results, null, 1));
  console.log('wrote', outJson);
}

main().catch((e) => { console.error(e); process.exit(1); });
