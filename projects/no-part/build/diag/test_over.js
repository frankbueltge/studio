const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const { PDF_PATH, PAGE_MM, dsfForPxPerMm } = require('../pdf-render-lib.js');

async function tryOne(browser, slackCss, frag) {
  const pxPerMm = 4;
  const dsf = dsfForPxPerMm(pxPerMm);
  const pageWCss = (PAGE_MM.w / 25.4) * 96;
  const pageHCss = (PAGE_MM.h / 25.4) * 96;
  const viewportCss = { width: Math.ceil(pageWCss + 260), height: Math.ceil(pageHCss + slackCss) };
  const context = await browser.newContext({ viewport: viewportCss, deviceScaleFactor: dsf });
  const page = await context.newPage();
  await page.goto(`file://${PDF_PATH}${frag}`, { timeout: 20000 });
  await page.waitForTimeout(900);
  try { await page.mouse.click(32, 28); await page.waitForTimeout(300); } catch (e) {}
  await page.waitForTimeout(400);
  // Try nudging further with keyboard End / mouse wheel over the plugin area
  await page.mouse.move(400, 600);
  await page.mouse.wheel(0, 5000);
  await page.waitForTimeout(400);
  await page.keyboard.press('End').catch(()=>{});
  await page.waitForTimeout(400);
  const buf = await page.screenshot();
  await context.close();

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
  console.log(`frag=${frag} slack=${slackCss}: screenshot ${result.width}x${result.height}, transitions=${JSON.stringify(result.transitions)}`);
  return buf;
}

async function main() {
  const browser = await chromium.launch({ headless: false });
  await tryOne(browser, 140, '#page=40&zoom=100');
  const buf = await tryOne(browser, 140, '#page=39&zoom=100');
  fs.writeFileSync(path.join(__dirname, 'raw-page39-afterscroll.png'), buf);
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
