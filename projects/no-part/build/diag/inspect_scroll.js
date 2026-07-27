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

  // Try to find the scrollable container inside the pdf viewer (may be in a shadow root / extension frame)
  const info = await page.evaluate(() => {
    function describe(el, path) {
      if (!el) return null;
      return { path, tag: el.tagName, id: el.id, scrollTop: el.scrollTop, scrollHeight: el.scrollHeight, clientHeight: el.clientHeight };
    }
    const results = [];
    results.push(describe(document.scrollingElement, 'document.scrollingElement'));
    results.push(describe(document.body, 'document.body'));
    // walk all elements, find those with scrollHeight > clientHeight
    const all = document.querySelectorAll('*');
    for (const el of all) {
      if (el.scrollHeight > el.clientHeight + 5) {
        results.push(describe(el, el.tagName + (el.id ? '#' + el.id : '') + (el.className ? '.' + String(el.className).replace(/\s+/g,'.') : '')));
      }
    }
    return results;
  });
  console.log('main frame scroll info:', JSON.stringify(info, null, 2));

  console.log('frames:', page.frames().map(f => f.url()));

  await context.close();
  await browser.close();
}
main().catch(e => { console.error(e); process.exit(1); });
