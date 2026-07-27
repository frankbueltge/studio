// Builder — Ensemble, still-v3 (CONCEPT), VECTOR 3 "THE SAME SENTENCE"
// Renders the first still per VECTOR-3-proposal.md §12.
//
// Method kept from ../still/build.js (session 45's precedent): render real
// HTML from the corpus with Playwright/Chromium, screenshot at
// deviceScaleFactor 1 and 2, then look at the PNG and fix what's wrong.
// Layout differs completely (this is a column of a document, not a wall of
// cards) because the spec differs completely; only the render/inspect/fix
// discipline is inherited.
//
// Usage:  NODE_PATH=/opt/node22/lib/node_modules node build.js
// Output: page.html, still-1x.png (1280x1000 @dSF1), still-2x.png (@dSF2),
//         measured.json (pixel measurements from measure.js, run automatically)

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { main: computeAnalytics } = require('./compute.js');
const tailOrders = require('./tail-orders.js');

const CORPUS = path.join(__dirname, '..', 'corpus', 'entries.json');
const FONT_DIR = path.join(__dirname, 'fonts');
const OUT_HTML = path.join(__dirname, 'page.html');
const OUT_1X = path.join(__dirname, 'still-1x.png');
const OUT_2X = path.join(__dirname, 'still-2x.png');

const SENTENCE = 'The petitions for writs of certiorari are denied.';

// ---- Palette (spec §12, four values, no more) ----
const GROUND = '#EDEBE4';
const INK = '#17171A';
const SAT = '#A8201A';
const RULE_COLOR = 'rgba(23,23,26,0.35)'; // #17171A at 35%

// ---- Type scale: 9 / 11.25 / 14 / 17.6 / 22, ratio 1.25 from 9px base ----
const LEADING = 14; // body entries
const SENTENCE_SIZE = 17.6;
const SENTENCE_LEADING = 24;

// ---- Spacing scale: 4 / 8 / 12 / 20 / 32 / 52 (4 x {1,2,3,5,8,13}) ----
const SPACE = { xs: 4, sm: 8, md: 12, lg: 20, xl: 32, xxl: 52 };

// ---- Frame / column geometry (spec §12) ----
const FRAME_W = 1280;
const FRAME_H = 1000;
const COL_LEFT = 380;
const COL_MEASURE = 520;
const DOCKET_FIELD = 72;

// ---- Two known source corruptions, repaired here per session 45's law ----
// entries.json ITSELF still carries the defect; this repair happens only in
// this script's in-memory copy, right before rendering. See README.md.
const CAPTION_REPAIRS = {
  '25-5182': 'MELNYCHUK-BESELT, RONDA V. WALDORF–ASTORIA MGMT., ET AL.', // en-dash, was "WALDORF=ASTORIA"
  '25-5278': 'PEÑA, REYNALDO A. V. TEXAS', // capital Ñ, was "PEñA"
};

function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function b64font(filename) {
  return fs.readFileSync(path.join(FONT_DIR, filename)).toString('base64');
}

function loadEntries() {
  const all = JSON.parse(fs.readFileSync(CORPUS, 'utf8'));
  const denied = all.filter((e) => e.section === 'CERTIORARI DENIED');
  if (denied.length !== 792) {
    throw new Error('Expected 792 CERTIORARI DENIED entries, got ' + denied.length);
  }
  let repaired = 0;
  const out = denied.map((e) => {
    if (CAPTION_REPAIRS[e.docket]) {
      repaired++;
      return { ...e, caption: CAPTION_REPAIRS[e.docket], _repaired: true };
    }
    return e;
  });
  if (repaired !== 2) {
    throw new Error('Expected exactly 2 caption repairs, applied ' + repaired);
  }
  return out;
}

function entryLine(e, big) {
  const color = e.ifp ? SAT : INK;
  const size = big ? 11.25 : 9;
  return `<div class="entry" style="font-size:${size}px;line-height:${LEADING}px;"><span class="docket" style="width:${DOCKET_FIELD}px;color:${color};">${esc(
    e.docket
  )}</span><span class="caption">${esc(e.caption)}</span></div>`;
}

function tailGroupHtml(group) {
  const dockets = group.dockets.map((d, i) => {
    const caption = group.captions ? group.captions[d] : group.caption;
    // Look up ifp from the real entry so colour follows the same rule as
    // the rest of the column (never hand-set).
    return { docket: d, caption };
  });
  return { dockets, order: group.order };
}

function buildHtml(denied, analytics) {
  const topBlock = denied.slice(analytics.top_block_entry_range[0], analytics.top_block_entry_range[1] + 1);
  if (topBlock.length !== analytics.top_block_line_count) {
    throw new Error('top block length mismatch');
  }

  // full silent mass, entries 0..760 inclusive (761 entries) precede the sentence
  const mass = denied.slice(0, 761);
  if (mass.length !== 761) throw new Error('mass length mismatch: ' + mass.length);

  // build an index for ifp lookup by docket, for the tail groups
  const byDocket = {};
  denied.forEach((e) => (byDocket[e.docket] = e));

  const massHtml = mass.map((e) => entryLine(e)).join('\n');

  const tailHtml = tailOrders
    .map((group, i) => {
      const lines = group.dockets
        .map((d) => {
          const caption = group.captions ? group.captions[d] : group.caption;
          const real = byDocket[d];
          if (!real) throw new Error('tail docket not found in corpus: ' + d);
          if (real.caption !== caption) {
            throw new Error(
              `tail caption mismatch for ${d}: corpus has "${real.caption}", tail-orders.js has "${caption}"`
            );
          }
          return entryLine(real);
        })
        .join('\n');
      // The group immediately before the last (24-7233, before 24-7281) gets
      // a wider gap after it: measured on the rendered pixels, the standard
      // gap left 24-7281's order paragraph landing fully inside the frame
      // (ending at y=990, 10px short of the bottom edge) instead of
      // straddling it as the spec's crop table requires ("cropped mid-
      // sentence by the frame's bottom edge"). See README "what I fixed."
      const isPenultimate = i === tailOrders.length - 2;
      const groupStyle = isPenultimate ? ` style="margin-bottom:${SPACE.xxl}px;"` : '';
      return `<div class="tail-group"${groupStyle}>\n${lines}\n<div class="order" style="font-size:9px;line-height:${LEADING}px;">${esc(
        group.order
      )}</div>\n</div>`;
    })
    .join('\n');

  const fontFaces = `
    @font-face {
      font-family: 'Source Serif 4';
      font-weight: 400;
      src: url(data:font/woff2;base64,${b64font('SourceSerif4-Regular.woff2')}) format('woff2');
    }
    @font-face {
      font-family: 'Source Serif 4';
      font-weight: 700;
      src: url(data:font/woff2;base64,${b64font('SourceSerif4-Bold.woff2')}) format('woff2');
    }
    @font-face {
      font-family: 'IBM Plex Mono';
      font-weight: 400;
      src: url(data:font/woff2;base64,${b64font('IBMPlexMono-Regular.woff2')}) format('woff2');
    }
    @font-face {
      font-family: 'IBM Plex Mono';
      font-weight: 500;
      src: url(data:font/woff2;base64,${b64font('IBMPlexMono-Medium.woff2')}) format('woff2');
    }
  `;

  const html = `<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>still-v3</title>
<style>
  ${fontFaces}
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    background: ${GROUND};
    width: ${FRAME_W}px;
  }
  body {
    font-family: 'Source Serif 4', serif;
    color: ${INK};
  }
  .column {
    position: absolute;
    left: ${COL_LEFT}px;
    top: 0;
    width: ${COL_MEASURE}px;
    /* Buffer so the frame's crop, deep in an ~11,000px column, is never
       clamped by the browser's max-scroll — see README "what I fixed". */
    padding-bottom: 500px;
  }
  .entry {
    display: flex;
    white-space: normal;
  }
  .entry .docket {
    flex: 0 0 ${DOCKET_FIELD}px;
    font-variant-numeric: lining-nums tabular-nums;
  }
  .entry .caption {
    flex: 1 1 auto;
    overflow-wrap: break-word;
  }
  /* The mass (761 entries) sits in ordinary document flow at the top of
     .column, and is exactly 761*14=10654px tall (confirmed below by
     build.js's own measurement pass). Everything after it — the sentence,
     the rule+caret, the tail — is positioned with an explicit "top" in
     document-space, computed once in compute.js and written in below,
     rather than left to stack via margins. Two adjoining empty/zero-height
     boxes (the rule's own row has no border/padding/content) collapse
     their margins in ordinary CSS flow, which silently ate 32px of the
     rule-to-tail gap on the first render of this file — see README "what I
     fixed." Explicit absolute "top" values sidestep that failure mode
     entirely instead of fighting it with collapse-prevention hacks. */
  .sentence {
    position: absolute;
    top: ${analytics.sentence_doc_y}px;
    left: 0;
    padding-left: ${SPACE.md}px;
    font-size: ${SENTENCE_SIZE}px;
    line-height: ${SENTENCE_LEADING}px;
  }
  .rule {
    position: absolute;
    top: ${analytics.rule_doc_y}px;
    left: 0;
    width: ${COL_MEASURE}px;
    border-top: 1px solid ${RULE_COLOR};
  }
  .caret {
    position: absolute;
    top: ${analytics.rule_doc_y}px;
    left: 0;
    width: 1px;
    height: 12px;
    background: ${INK};
  }
  .tail {
    position: absolute;
    top: ${analytics.rule_doc_y + SPACE.xxl}px;
    left: 0;
    width: ${COL_MEASURE}px;
  }
  .tail-group {
    margin-bottom: ${SPACE.xl}px;
  }
  .tail-group .order {
    margin-top: ${SPACE.md}px;
    padding-left: ${SPACE.md}px;
    width: ${COL_MEASURE - SPACE.md}px;
  }
</style>
</head>
<body>
  <div class="column">
    ${massHtml}
    <div class="sentence">${esc(SENTENCE)}</div>
    <div class="caret"></div>
    <div class="rule"></div>
    <div class="tail">
      ${tailHtml}
    </div>
  </div>
</body>
</html>`;

  fs.writeFileSync(OUT_HTML, html, 'utf8');
  console.log('wrote', OUT_HTML);
}

async function shoot(analytics) {
  const browser = await chromium.launch();

  // First pass: load at scale 1, measure real DOM positions before
  // deciding the scroll offset — "confirm on the pixels" rather than
  // trusting the analytic prediction blindly.
  const ctx0 = await browser.newContext({ viewport: { width: FRAME_W, height: FRAME_H }, deviceScaleFactor: 1 });
  const page0 = await ctx0.newPage();
  await page0.goto('file://' + OUT_HTML);
  await page0.evaluate(() => document.fonts.ready);

  const measured = await page0.evaluate((topIdx) => {
    const entries = Array.from(document.querySelectorAll('.entry'));
    const massEntries = entries.slice(0, 761); // the 761-entry mass rendered before .sentence
    const e745 = massEntries[topIdx[0]];
    const e760 = massEntries[topIdx[1]];
    const sentence = document.querySelector('.sentence');
    const rule = document.querySelector('.rule');
    const tailFirst = document.querySelectorAll('.tail-group')[0];
    return {
      entry745Top: e745.getBoundingClientRect().top + window.scrollY,
      entry760Bottom: e760.getBoundingClientRect().bottom + window.scrollY,
      sentenceTop: sentence.getBoundingClientRect().top + window.scrollY,
      ruleTop: rule.getBoundingClientRect().top + window.scrollY,
      tailFirstTop: tailFirst.getBoundingClientRect().top + window.scrollY,
      massEntryCount: massEntries.length,
      // check every mass + tail entry .caption for wrapping (more than one line)
      wrappedCaptions: entries.filter((el) => {
        const cap = el.querySelector('.caption');
        return cap && cap.getBoundingClientRect().height > 14.5;
      }).length,
    };
  }, analytics.top_block_entry_range);

  console.log('MEASURED (pre-scroll, real DOM):', JSON.stringify(measured, null, 2));

  const scrollTop = measured.entry745Top;
  await ctx0.close();

  const results = { scrollTopUsed: scrollTop, measured };

  for (const [scale, out] of [[1, OUT_1X], [2, OUT_2X]]) {
    const ctx = await browser.newContext({
      viewport: { width: FRAME_W, height: FRAME_H },
      deviceScaleFactor: scale,
    });
    const page = await ctx.newPage();
    await page.goto('file://' + OUT_HTML);
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate((y) => window.scrollTo(0, y), scrollTop);
    await page.waitForTimeout(50);

    // Post-scroll confirmation: where do the landmark elements actually
    // land inside the 1280x1000 frame now?
    const postScroll = await page.evaluate(() => {
      const sentence = document.querySelector('.sentence');
      const rule = document.querySelector('.rule');
      const tailGroups = document.querySelectorAll('.tail-group');
      const lastGroup = tailGroups[tailGroups.length - 1];
      const lastOrder = lastGroup.querySelector('.order');
      return {
        sentenceFrameTop: sentence.getBoundingClientRect().top,
        ruleFrameTop: rule.getBoundingClientRect().top,
        tailFirstFrameTop: tailGroups[0].getBoundingClientRect().top,
        lastGroupDocket: lastGroup.querySelector('.docket').textContent,
        lastOrderFrameTop: lastOrder.getBoundingClientRect().top,
        lastOrderFrameBottom: lastOrder.getBoundingClientRect().bottom,
        lastOrderCutByFrame: lastOrder.getBoundingClientRect().bottom > 1000 && lastOrder.getBoundingClientRect().top < 1000,
      };
    });
    if (scale === 1) results.postScroll = postScroll;

    await page.screenshot({ path: out });
    console.log('wrote', out, JSON.stringify(postScroll));
    await ctx.close();
  }

  await browser.close();
  return results;
}

async function main() {
  const analytics = computeAnalytics();
  const denied = loadEntries();
  buildHtml(denied, analytics);
  const results = await shoot(analytics);
  fs.writeFileSync(
    path.join(__dirname, 'render-report.json'),
    JSON.stringify({ analytics, ...results }, null, 2)
  );
  console.log('wrote render-report.json');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
