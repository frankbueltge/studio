const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const { PDF_PATH, PAGE_MM, dsfForPxPerMm } = require('../pdf-render-lib.js');

async function main() {
  const pxPerMm = 4;
  const dsf = dsfForPxPerMm(pxPerMm);
  const pageWCss = (PAGE_MM.w / 25.4) * 96;
  const pageHCss = (PAGE_MM.h / 25.4) * 96;
  const viewportCss = { width: Math.ceil(pageWCss + 260), height: Math.ceil(pageHCss + 140) };
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({ viewport: viewportCss, deviceScaleFactor: dsf });
  const page = await context.newPage();
  await page.goto(`file://${PDF_PATH}#page=39&zoom=100`, { timeout: 20000 });
  await page.waitForTimeout(900);
  try { await page.mouse.click(32, 28); await page.waitForTimeout(300); } catch (e) {}
  await page.waitForTimeout(400);
  const buf = await page.screenshot();
  fs.writeFileSync(path.join(__dirname, 'raw-page39-full.png'), buf);
  console.log('wrote raw-page39-full.png, viewport', viewportCss, 'dsf', dsf);
  await context.close();
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
