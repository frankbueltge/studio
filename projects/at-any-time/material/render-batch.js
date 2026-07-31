// Driver for MEASUREMENT 1 (docket item A4). Renders page 1 of a list of
// source PDFs at the house's proven 4 px/mm scale, using pdf-render-lib.js
// COPIED VERBATIM from no-part/build/ (see that directory's own file --
// this copy is byte-identical, diffed at copy time). Writes, for each
// document:
//   <outdir>/<stem>.raw.png        -- renderPage()'s own cropped PNG output,
//                                      NO post-processing (this is the
//                                      "baseline PNG" figure this session
//                                      measures against).
//   <outdir>/<stem>.gray.png       -- the same buffer run through
//                                      canvas-lib.js's desaturateToGrayscale
//                                      (no-part's own colour-cast fix),
//                                      recorded separately so this session
//                                      can state plainly which variant its
//                                      numbers are, rather than silently
//                                      picking one.
//
// IMPORTANT — run this from a SCRATCH copy, not in place inside this repo:
// pdf-render-lib.js's PDF_PATH constant resolves to
// path.resolve(__dirname, '..', 'order-list.pdf') -- i.e. one directory
// ABOVE wherever pdf-render-lib.js itself physically sits. This script
// overwrites that path on every call (see below). If you run it with
// these files sitting inside material/, that means it will write/overwrite
// projects/at-any-time/order-list.pdf on every invocation -- a stray,
// untracked PDF landing in the project root. Never committed by this
// session; do not commit it if you reproduce this measurement. The
// original measurement was run by copying this whole directory's contents
// (this file + pdf-render-lib.js + canvas-lib.js, all byte-identical to
// what's committed here) into a scratch build/ directory one level below a
// throwaway parent, e.g.:
//   mkdir -p /tmp/render/build && cp material/{render-batch.js,pdf-render-lib.js,canvas-lib.js} /tmp/render/build/
//   cd /tmp/render/build
//   xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules \
//     node render-batch.js /tmp/render/pages <doc1.pdf> [doc2.pdf ...]
//
// Usage: xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules \
//   node render-batch.js <render-dir> <doc1.pdf> [doc2.pdf ...]
//
// <render-dir> is just where the output PNGs are written -- it need not be
// (and for the reason above, should not be) related to where this script
// and pdf-render-lib.js themselves live. This script copies each input PDF
// to <this-script's-dir>/../order-list.pdf before calling renderPage(),
// exactly mimicking how no-part's own render-sheets.js finds its single
// source file, but swapped per document. This is why the copy of
// pdf-render-lib.js can stay verbatim: nothing in it needed to change to
// serve multiple distinct source PDFs, only the filesystem input feeding
// its hardcoded PDF_PATH constant needed to be swapped between calls.

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { chromium } = require('playwright');
const { renderPage, PDF_PATH } = require('./pdf-render-lib.js');
const { launchBrowser, desaturateToGrayscale } = require('./canvas-lib.js');

const PX_PER_MM = 4;
const MAX_ATTEMPTS = 3;

async function renderWithRetry(browser, pageNum, pxPerMm, maxAttempts) {
  let lastErr;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await renderPage(browser, pageNum, pxPerMm);
    } catch (e) {
      lastErr = e;
      console.error(`  attempt ${attempt}/${maxAttempts} failed (${e.message})`);
      await new Promise((r) => setTimeout(r, 1200));
    }
  }
  throw lastErr;
}

async function main() {
  const [outDir, ...pdfPaths] = process.argv.slice(2);
  if (!outDir || pdfPaths.length === 0) {
    console.error('Usage: node render-batch.js <outdir> <pdf1> [pdf2 ...]');
    process.exit(1);
  }
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await launchBrowser(chromium);
  const results = [];

  for (const pdfPath of pdfPaths) {
    const stem = path.basename(pdfPath, '.pdf');
    const t0 = Date.now();
    try {
      // Swap the source PDF that pdf-render-lib.js's hardcoded PDF_PATH
      // points at. Verified by hash after copy.
      fs.copyFileSync(pdfPath, PDF_PATH);
      const srcHash = crypto.createHash('sha256').update(fs.readFileSync(pdfPath)).digest('hex');
      const copiedHash = crypto.createHash('sha256').update(fs.readFileSync(PDF_PATH)).digest('hex');
      if (srcHash !== copiedHash) throw new Error('copy hash mismatch');

      const { buffer, widthPx, heightPx, shortfallPx } = await renderWithRetry(browser, 1, PX_PER_MM, MAX_ATTEMPTS);
      const rawPath = path.join(outDir, `${stem}.raw.png`);
      fs.writeFileSync(rawPath, buffer);

      const grayBuffer = await desaturateToGrayscale(browser, buffer);
      const grayPath = path.join(outDir, `${stem}.gray.png`);
      fs.writeFileSync(grayPath, grayBuffer);

      const dt = ((Date.now() - t0) / 1000).toFixed(1);
      console.log(`${stem}: ${widthPx}x${heightPx}px raw=${buffer.length}B gray=${grayBuffer.length}B shortfall=${shortfallPx}px (${dt}s)`);
      results.push({
        stem, pdfPath, srcHash, widthPx, heightPx, shortfallPx,
        rawBytes: buffer.length, grayBytes: grayBuffer.length,
        rawPath, grayPath,
      });
    } catch (e) {
      console.error(`${stem}: FAILED - ${e.message}`);
      results.push({ stem, pdfPath, error: e.message });
    }
  }

  await browser.close();
  fs.writeFileSync(path.join(outDir, 'render-batch-log.json'), JSON.stringify(results, null, 2));
  console.log('wrote', path.join(outDir, 'render-batch-log.json'));
}

main().catch((e) => { console.error(e); process.exit(1); });
