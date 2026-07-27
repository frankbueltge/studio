const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

async function analyze(browser, fname) {
  const buf = fs.readFileSync(fname);
  const ctxPage = await browser.newContext();
  const p = await ctxPage.newPage();
  await p.goto('about:blank');
  const b64 = buf.toString('base64');
  const result = await p.evaluate(async (dataUrl) => {
    const img = new Image();
    await new Promise((resolve, reject) => { img.onload = resolve; img.onerror = reject; img.src = dataUrl; });
    const canvas = document.createElement('canvas');
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    const { width, height } = canvas;
    const data = ctx.getImageData(0, 0, width, height).data;
    const lumAt = (x, y) => {
      const i = (y * width + x) * 4;
      return 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
    };
    const THRESH = 150;
    const rowAvg = [];
    for (let y = 0; y < height; y++) {
      let sum = 0;
      for (let x = 0; x < width; x++) sum += lumAt(x, y);
      rowAvg.push(sum / width);
    }
    // find all transitions
    const transitions = [];
    let prevBright = rowAvg[0] > THRESH;
    for (let y = 1; y < height; y++) {
      const bright = rowAvg[y] > THRESH;
      if (bright !== prevBright) transitions.push({ y, to: bright ? 'bright' : 'dark' });
      prevBright = bright;
    }
    return { width, height, transitions };
  }, `data:image/png;base64,${b64}`);
  await ctxPage.close();
  return result;
}

async function main() {
  const browser = await chromium.launch({ headless: false });
  for (const f of ['raw-page39-full.png', 'raw-page15-full.png']) {
    const r = await analyze(browser, path.join(__dirname, f));
    console.log(f, 'dims', r.width, 'x', r.height);
    console.log('  transitions:', JSON.stringify(r.transitions));
  }
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
