// Builder — Ensemble, still-v3 (CONCEPT)
// House law: "pixels, not propositions." Decodes the rendered PNGs directly
// (pngjs, no CSS values consulted) and reports what is actually on the
// frame: the count and share of saturated #A8201A-family pixels, the share
// of ink pixels, and a stroke/anti-aliasing readout at both device scales
// as a proxy for legibility (final legibility judgement is left to a human
// eye — this only reports what can be measured).

const fs = require('fs');
const path = require('path');
const { PNG } = require('pngjs');

const GROUND = [0xed, 0xeb, 0xe4];
const INK = [0x17, 0x17, 0x1a];
const SAT = [0xa8, 0x20, 0x1a];

function dist(a, b) {
  return Math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2);
}

// Nearest-of-three-anchors classification is unusable at 9px: most glyph
// pixels are anti-aliased blends of ink/sat into the paper colour, not
// solid fills, so a forced 3-way nearest-centroid pick is dominated by
// where each blend pixel happens to fall and swings wildly between 1x and
// 2x renders of the *same* content purely from how the rasteriser
// distributes sub-pixel coverage — a first pass of this script reported
// satShare > inkShare at 1x and the reverse at 2x, which is a measurement
// artefact, not a real difference (confirmed by reading both PNGs
// directly). Thresholded classification below fixes it: a pixel only
// counts as ink/sat if it is close to that anchor AND clearly closer to it
// than to ground; a "near-ground" pixel is classified as ground even if
// technically nearer to ink/sat than to the other anchor. Everything else
// (the anti-aliased transition halo) is its own bucket, reported
// separately rather than forced into ink or sat.
const GROUND_R = 40; // pixels within this of ground are paper, full stop
const MARK_R = 140; // pixels within this of ink/sat AND outside GROUND_R count as that mark

function classify(r, g, b) {
  const px = [r, g, b];
  const dG = dist(px, GROUND);
  const dI = dist(px, INK);
  const dS = dist(px, SAT);
  if (dG <= GROUND_R) return 'ground';
  if (dI < dS && dI <= MARK_R) return 'ink';
  if (dS <= dI && dS <= MARK_R) return 'sat';
  return 'edge'; // anti-aliased transition pixel, not close to any anchor
}

function analyse(file) {
  const png = PNG.sync.read(fs.readFileSync(file));
  const { width, height, data } = png;
  let ground = 0,
    ink = 0,
    sat = 0,
    edge = 0;
  // Strict counts: pixels within a tight radius of the exact palette value
  // (i.e. solid glyph fill / solid rule, not anti-aliased edge halos) —
  // this is the number that actually tracks device scale factor honestly,
  // since a thin 9px stroke has almost no fully-solid interior pixel at
  // dSF1 and gains real solid pixels at dSF2 (see README).
  let strictInk = 0,
    strictSat = 0;
  for (let i = 0; i < data.length; i += 4) {
    const r = data[i],
      g = data[i + 1],
      b = data[i + 2];
    const c = classify(r, g, b);
    if (c === 'ground') ground++;
    else if (c === 'ink') ink++;
    else if (c === 'sat') sat++;
    else edge++;
    if (dist([r, g, b], INK) < 12) strictInk++;
    if (dist([r, g, b], SAT) < 12) strictSat++;
  }
  const total = width * height;
  return {
    file,
    width,
    height,
    total,
    ground,
    ink,
    sat,
    edge,
    groundShare: +(ground / total).toFixed(4),
    inkShare: +(ink / total).toFixed(4),
    satShare: +(sat / total).toFixed(4),
    edgeShare: +(edge / total).toFixed(4),
    satOfMarkShare: +(sat / (ink + sat)).toFixed(4), // sat as a share of ink+sat only (excludes paper/edge)
    strictInkPixels: strictInk,
    strictSatPixels: strictSat,
    strictSatShare: +(strictSat / total).toFixed(6),
    strictInkShare: +(strictInk / total).toFixed(6),
  };
}

// Anti-aliasing / stroke-contrast readout: scan a horizontal line through a
// known line of 9px body text and report the run-lengths and intermediate
// (non-pure) grey levels encountered — a proxy for "is a 9px stroke built
// from one crisp pixel or a blur of half-tones."
function scanLine(file, y, xStart, xEnd) {
  const png = PNG.sync.read(fs.readFileSync(file));
  const { width, data } = png;
  const row = [];
  for (let x = xStart; x < Math.min(xEnd, width); x++) {
    const i = (y * width + x) * 4;
    row.push([data[i], data[i + 1], data[i + 2]]);
  }
  // count transitions and distinct luminance buckets (0-255 -> 16 buckets)
  const buckets = new Set();
  let darkRuns = 0;
  let inRun = false;
  for (const [r, g, b] of row) {
    const lum = 0.3 * r + 0.59 * g + 0.11 * b;
    buckets.add(Math.floor(lum / 16));
    const isDark = lum < 190; // below ~paper luminance
    if (isDark && !inRun) {
      darkRuns++;
      inRun = true;
    } else if (!isDark) {
      inRun = false;
    }
  }
  return { file, y, xStart, xEnd, distinctLumBuckets: buckets.size, darkRuns, sampleWidth: row.length };
}

// Hue-based classification, added after the anchor-distance classifier
// above turned out to disagree with itself between 1x and 2x (satOfMark
// share 0.70 at 1x vs 0.33 at 2x, on the same content) — see README "what I
// fixed" for the full account. Anchor-distance is unreliable for 9px
// anti-aliased type because a partially-covered red glyph pixel blended
// with the paper colour can land numerically nearer the ink anchor than
// the saturated anchor, and how often that happens shifts with device
// scale factor. Ink (#17171A) and paper (#EDEBE4) are both close to
// neutral grey; saturated (#A8201A) is the only anchor with a distinctly
// higher red channel than green/blue. So: any admixture of the saturated
// colour into paper raises R faster than G/B, in proportion to coverage,
// regardless of scale — "reddish" is a much more stable test than
// "nearest of three points" for exactly this palette.
function classifyHue(r, g, b) {
  const maxGB = Math.max(g, b);
  const reddish = r - maxGB > 18;
  if (reddish) return 'sat';
  const lum = 0.3 * r + 0.59 * g + 0.11 * b;
  if (lum < 225) return 'ink'; // paper luminance is ~234; anything visibly darker and non-red is ink
  return 'ground';
}

function analyseHue(file) {
  const png = PNG.sync.read(fs.readFileSync(file));
  const { width, height, data } = png;
  let ground = 0,
    ink = 0,
    sat = 0;
  for (let i = 0; i < data.length; i += 4) {
    const c = classifyHue(data[i], data[i + 1], data[i + 2]);
    if (c === 'ground') ground++;
    else if (c === 'ink') ink++;
    else sat++;
  }
  const total = width * height;
  return {
    file,
    total,
    ground,
    ink,
    sat,
    inkShare: +(ink / total).toFixed(4),
    satShare: +(sat / total).toFixed(4),
    satOfMarkShare: +(sat / (ink + sat)).toFixed(4),
  };
}

function main() {
  const dir = __dirname;
  const report = {};
  for (const f of ['still-1x.png', 'still-2x.png']) {
    const full = path.join(dir, f);
    report[f] = analyse(full);
    report[f].hue = analyseHue(full);
  }
  // Scan a row through the top-block entries (saturated dockets), e.g. at
  // frame y ~ 8 (well within the first visible line's x-height), scaled by
  // device scale factor for the 2x file. Docket text starts at x=380.
  report.scan_1x_docket_row = scanLine(path.join(dir, 'still-1x.png'), 6, 380, 460);
  report.scan_2x_docket_row = scanLine(path.join(dir, 'still-2x.png'), 12, 760, 920);
  // Scan the Court's sentence row (larger type, frame y ~256+12=268, x2 for 2x)
  report.scan_1x_sentence_row = scanLine(path.join(dir, 'still-1x.png'), 268, 392, 700);
  report.scan_2x_sentence_row = scanLine(path.join(dir, 'still-2x.png'), 536, 784, 1400);

  console.log(JSON.stringify(report, null, 2));
  fs.writeFileSync(path.join(dir, 'measured.json'), JSON.stringify(report, null, 2));
  return report;
}

if (require.main === module) main();
module.exports = { main, analyse, scanLine };
