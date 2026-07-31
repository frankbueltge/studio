// Validates png-codec-lib.js's OUTPUT files against an independent decoder:
// Chromium's own <img>/<canvas> PNG decoder (not the hand-rolled one this
// session's own decodePng() uses) -- so a bug shared between our decoder
// and encoder cannot silently pass. Loads each candidate PNG in the browser,
// reads pixels back via getImageData, and compares against the known-good
// source pixel data computed directly in Node.
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { decodePng, encodeGray8, encodeIndexed, encodeBilevel1, encodeRGB8 } = require('./png-codec-lib.js');

async function loadInBrowser(browser, pngBuffer) {
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
    const d = c.getImageData(0, 0, canvas.width, canvas.height).data;
    return { width: canvas.width, height: canvas.height, data: Array.from(d) };
  }, `data:image/png;base64,${b64}`);
  await ctx.close();
  return result;
}

async function main() {
  const rawPath = process.argv[2];
  const buf = fs.readFileSync(rawPath);
  const img = decodePng(buf);
  const { width, height, pixels } = img;
  const n = width * height;

  function luminance(r, g, b) { return Math.round(0.299 * r + 0.587 * g + 0.114 * b); }
  const gray = Buffer.alloc(n);
  const rgb = Buffer.alloc(n * 3);
  for (let i = 0; i < n; i++) {
    const r = pixels[i*4], g = pixels[i*4+1], b = pixels[i*4+2];
    gray[i] = luminance(r, g, b);
    rgb[i*3]=r; rgb[i*3+1]=g; rgb[i*3+2]=b;
  }
  const present = [...new Set(gray)].sort((a,b)=>a-b);
  const bitDepth = present.length<=2?1:present.length<=4?2:present.length<=16?4:8;
  const palette = present.map(v=>[v,v,v]);
  const idxMap = new Map(present.map((v,i)=>[v,i]));
  const indices = Buffer.alloc(n);
  for (let i=0;i<n;i++) indices[i]=idxMap.get(gray[i]);

  const gray8Png = encodeGray8(width, height, gray);
  const indexedPng = encodeIndexed(width, height, indices, palette, bitDepth);
  const rgb8Png = encodeRGB8(width, height, rgb);
  const bits = new Uint8Array(n);
  for (let i=0;i<n;i++) bits[i] = gray[i] > 150 ? 1 : 0;
  const bilevelPng = encodeBilevel1(width, height, bits);

  const browser = await chromium.launch({ headless: false });

  async function check(name, encodedBuf, expectedPixel) {
    const rt = await loadInBrowser(browser, encodedBuf);
    let maxDiff = 0, nDiff = 0;
    for (let i = 0; i < n; i++) {
      const exp = expectedPixel(i);
      const got = [rt.data[i*4], rt.data[i*4+1], rt.data[i*4+2]];
      for (let ch = 0; ch < 3; ch++) {
        const d = Math.abs(exp[ch] - got[ch]);
        if (d > maxDiff) maxDiff = d;
        if (d > 0) nDiff++;
      }
    }
    console.log(`${name}: browser-decoded ${rt.width}x${rt.height}, maxDiff=${maxDiff}, pixelsDiffering=${nDiff}/${n*3} -- ${maxDiff===0 ? 'EXACT MATCH (valid, lossless-encoded-as-claimed)' : 'MISMATCH'}`);
  }

  await check('gray8', gray8Png, (i) => [gray[i], gray[i], gray[i]]);
  await check('indexed', indexedPng, (i) => [gray[i], gray[i], gray[i]]);
  await check('rgb8', rgb8Png, (i) => [pixels[i*4], pixels[i*4+1], pixels[i*4+2]]);
  await check('bilevel1', bilevelPng, (i) => { const v = bits[i] ? 255 : 0; return [v, v, v]; });

  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
