# NO PART — production increment 01 (measurement)

**These are measurements of RASTERISED PAGES, not photographs of mounted paper.** Nothing here is
evidence about how the work reads in a room, at 8.42m, at head height, walked past by a body. What
follows answers a narrower, honest question: along the 39 pages of the source document, rendered at
100% and butted edge to edge as pixels, what changes, measurably, and by how much.

No glyph, mark or colour was added to the document anywhere in this pipeline. Every number below is
transcribed from this build's own stdout.

## Reproducing it

```
cd projects/no-part

# One-time, documented, network step — NOT run inside the build itself:
curl -sS -o order-list.pdf https://www.supremecourt.gov/orders/courtorders/100625zor_5368.pdf
sha256sum order-list.pdf   # must be 354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652

cd build
xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node render-sheets.js
xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node measure.js
xvfb-run -a env NODE_PATH=/opt/node22/lib/node_modules node compose-strip.js
```

`order-list.pdf` (228,850 bytes) is fetched once, kept out of git, and verified by SHA-256 at the top
of every `render-sheets.js` run — no network access happens inside any of the three scripts. Requires
Playwright + Chromium at `/opt/pw-browsers` and a working Xvfb.

Total run time on this machine: render-sheets.js ≈1.6 min (39 pages, ~2.4s/page), measure.js ≈10s,
compose-strip.js ≈5s.

## What each script does

- **`pdf-render-lib.js`** — copied from the concept-gate étude
  (`etudes/5000-series/still/no-part/pdf-render-lib.js`; see its header for the full account of why
  Chromium's own built-in PDF viewer, headful under Xvfb, is the only rasterisation path that works in
  this environment — no `pdftoppm`/`pdftocairo`/`gs`/`mutool`, no Python PDF library, and headless
  Chromium treats a local PDF as a download rather than rendering it). Two functions
  (`detectPageTopLeft`, `cropPng`) were genuinely changed here to fix a defect the 6-sheet concept gate
  never exercised — see "LAST-PAGE DEFECT" below.
- **`canvas-lib.js`** — shared in-browser `<canvas>` helpers (`runInCanvas`, `desaturateToGrayscale`)
  used by all three scripts. There is no external image library on this machine (`sharp`, `pngjs`,
  `canvas`, `jimp` all absent under `NODE_PATH`), so every pixel operation — decode, crop, measure,
  composite, downsample — runs inside a throwaway Chromium page's `<canvas>`, exactly as the concept
  gate's `build.js` did.
- **`render-sheets.js`** — verifies the PDF hash, then rasterises all 39 pages at 4px/mm into
  `render/sheet-01.png` … `sheet-39.png` (gitignored), desaturating each to neutral grey as a
  post-process (see "AA correction" below). Also writes `render/render-log.json`, a sidecar record of
  each sheet's captured pixel size and any capture shortfall, so `measure.js` never has to hardcode
  which sheet(s), if any, are incomplete.
- **`measure.js`** — reads the 39 rendered sheets and `render-log.json`, and emits `plate-manifest.json`,
  `line-profile.json`, and the full stdout report this file's Measurements section is transcribed from.
- **`compose-strip.js`** — butts the 39 rendered sheets in order at 1px/mm into `line-strip.png`, with
  nothing added.

## Environment quirks

**1. Chromium's PDF-viewer plugin does not scale linearly with `deviceScaleFactor`.** Carried over
unchanged from the concept-gate étude: `actual_px_per_mm = (96/25.4) × dsf²`, not `dsf¹`. Fix:
`dsf = sqrt(pxPerMm / (96/25.4))`. At the 4px/mm target this gives `dsf = 1.028753` and every sheet
measures exactly 864×1118px = 216.00×279.50mm.

**2. LAST-PAGE DEFECT — new, found and fixed in this increment.** The concept gate's 6-sheet frame
(sheets 30–35) never included sheet 39, the actual last page of the 39-page document, so it never hit
this. Chromium's continuous-scroll PDF viewer cannot scroll past the end of the document. Navigating
straight to `#page=39` leaves the TAIL of page 38 still visible above page 39 in the viewport (confirmed
by direct pixel-transition analysis of the raw, uncropped screenshot: three row-luminance transitions
instead of one — toolbar→page-38-tail, tail→divider, divider→page-39). The original "take the first
bright row from the top" crop logic picked page 38's tail as if it were page 39, silently producing a
render that started ~80px too early and consequently ended ~80px too early too — cutting off page 39's
own bottom margin and folio without any error or warning.

**Fix:** `detectPageTopLeft` no longer takes the first dark→bright transition; it takes the first one
whose following bright run is at least 500px long (comfortably between the measured tail-band heights,
66–236px across several tested viewport sizes, and a genuine full page's 1089–1117px). This is a
strictly more general rule, not a page-39 special case — every interior page's first transition already
qualifies, so behaviour there is unchanged (confirmed: sheets 1, 15, 38 all crop identically before and
after this fix).

Even with the correct transition selected, page 39's available room below it falls short of the full
864×1118px target by a small, essentially constant amount (29px / 7.25mm, measured; this held across
every viewport size tested — 140 to 300 CSS px of slack all gave the same ~29–34px shortfall, and mouse
wheel, keyboard `End`, and an out-of-range `#page=40` fragment were all tried and made no difference).
This plugin's internal scroll/layout geometry allocates less vertical space to the document than its
own dsf²-scaled glyph rendering actually draws — a second symptom of defect 1's scaling mismatch. No
scroll position this plugin allows reaches those missing rows.

**Handling, stated plainly:** sheet 39's bottom 7.25mm is filled paper-white in `render/sheet-39.png`,
not sourced from any rendered pixel. Visual inspection (`render/sheet-39.png`, this session) shows the
folio "39" IS captured, well above the cut line — the missing strip appears to be blank margin below
it, but this was **not confirmed**, only inferred by pattern-matching against every other page's margin
proportions, and is reported in `plate-manifest.json` (`unmeasuredBottomMm: 7.25` on sheet 39's record
only) and in `line-profile.json`'s meta as exactly that: unmeasured, not confirmed-blank. Nothing was
invented to fill it — see `pdf-render-lib.js`'s `cropPng`, which fills white specifically so a genuine
gap in the source screenshot doesn't composite as a fabricated black bar (canvas's default), and every
shortfall is logged, never silently absorbed.

**3. Sheet width measures 216.0mm, not the nominal 215.9mm US Letter cited in the brief.**
215.9mm × 4px/mm = 863.6px, which rounds up to 864px = 216.0mm at this render's fixed 4px/mm scale —
the same integer-pixel-rounding artefact documented as Defect 2 in the concept-gate étude (there, it
affected page height; here, because all 39 full pages are rendered rather than a 6-sheet crop, it
shows up on width too). Every position in `plate-manifest.json` and `line-profile.json` uses the
MEASURED 216.0mm/sheet, not the nominal 215.9mm, per this house's rule that every figure comes from
pixels, not a citation. Consequence: total line length measures 39 × 216.0mm = **8424.0mm (8.424m)**,
not exactly the brief's cited 8.42m (8420.1mm at nominal Letter width) — a 3.9mm difference (0.05%)
from the same rounding, accumulated over 39 sheets.

**4. AA correction (carried over from the concept-gate étude, re-verified here).** This Chromium
build's PDF viewer introduces a faint, non-neutral colour cast into anti-aliased glyph edges — not a
property of the source document (every `BT`/text-showing content stream in `order-list.pdf` was
previously confirmed to carry no colour-setting operator; text is drawn at the PDF's DeviceGray
default). Every rendered sheet is desaturated to neutral grey (R=G=B=perceptual luminance) as a
post-process, immediately after Chromium produces it, before anything downstream reads it. This
matters little for the ink-threshold measurements in this increment (luminance-based, not colour-based)
but is kept for consistency and because it is a correction of this house's own instrument, never an
addition to the document.

**5. `line-strip.png` came in at 0.76MB at the full 1px/mm scale** — under the 1.5MB budget, so no
fallback to 0.5px/mm was needed. `compose-strip.js` tries 1px/mm first and only falls back if the
budget is exceeded; this run didn't require it.

**6. All 39 pages rendered and measured successfully on the first attempt of this final run.** No
retries were needed (`render-sheets.js` has a 3-attempt retry per sheet, built in but unused here).

## What was measured, and how

- **Ink threshold:** a pixel counts as ink if `0.299R + 0.587G + 0.114B < 150` (same threshold used
  throughout the concept-gate étude).
- **Ink row:** a contiguous vertical band of rows (in the rasterised page) with more than 2 dark pixels
  per row, at least 6px tall — filters antialiasing noise, catches every real text line including
  short folios.
- **Text block bounding box (per sheet):** the smallest rectangle enclosing every detected ink row on
  that sheet.
- **Text-block ink coverage:** ink pixel count inside that bounding box, divided by the box's own pixel
  area (so it includes the blank gaps between lines within the block, not just the ink itself) — this
  is the "shape-aware" measurement the brief asks for, in contrast to whole-sheet coverage, which is
  diluted by the page's outer margins.
- **Row right-edge raggedness (per sheet):** `max − min` of each row's own rightmost ink pixel,
  converted to mm. High raggedness = lines end at very different horizontal positions on that page; low
  raggedness = lines end close together.
- **Docket vs. indented classification (per sheet, used to find the disposition sentence):** the
  leftmost `left` value among a sheet's own row bands is taken as that sheet's docket column; any band
  starting materially further right (>15px / ~3.75mm tolerance) is "indented" — a disposition sentence
  or continuation line rather than a docket/caption row. Folios are excluded by width (<60px).
- **Line-profile column:** for each 1mm-wide strip of the assembled line (4 rendered pixel-columns
  wide), the fraction of the sheet's full height (not just the text block) at which at least one of
  those pixel-columns is ink — a silhouette/occupancy measure, not raw pixel density.
- **Rows-region / prose-region split:** NOT hand-picked. A two-segment changepoint (minimising pooled
  within-group variance) run over the sequence of all 39 sheets' raggedness values, exhaustive over all
  38 possible boundaries. See `measure.js`'s `twoSegmentChangepoint()`.
- **The disposition sentence's location:** identified by direct visual inspection of
  `render/sheet-32.png` this session (not OCR, not copied from the concept-gate étude's prior numbers)
  — it is the first indented line on sheet 32, immediately after the last docket row
  ("25-5543 BROOKS…") and before the next docket row ("24-948 GUERRERO…"). Its pixel coordinates come
  from this script's own row-band detection, not from the visual read, which only established which
  band to trust.

## MEASUREMENTS (transcribed from `measure.js`'s own stdout; reproduce with the commands above)

### 1. The answer to the register-change question

**Whole-sheet ink coverage**, over the full 39-sheet document (not the 6-sheet subset the prior gate
measured): rows-region (sheets 1–32) mean = **3.539%**; prose-region (sheets 33–39) mean = **3.057%**.
Difference: **0.482 percentage points** — roughly ten times the 0.05-point difference the prior gate
found across its narrower 6-sheet window, and clearly the larger, more real effect once measured over
the whole line rather than a slice of it.

**Text-block-only ink coverage** (excluding outer margins, as this increment set out to test): rows-region
mean = **5.979%**, prose-region mean = **4.611%**. Difference: **1.368 percentage points** — nearly
three times the whole-sheet difference, and the strongest single confirmation in this dataset that
whole-sheet coverage was diluting the real effect. Restricting to the text block, where the register
change actually lives on the page, roughly triples the measured contrast.

**The 1mm-column line-profile contrast** (the full 8.424m line, treating the WHOLE page height as the
denominator, not just the text block) is smaller again: raw = **0.0102** (rows-region mean 0.0738,
prose-region mean 0.0637, ratio 1.16×), essentially unchanged after 10mm and 50mm moving-average
smoothing, and only marginally different after 200mm smoothing (diff 0.0104, ratio 1.16×). **This
contrast survives every level of blur tested, including the coarsest (200mm ≈ what a body walking past
at reading distance could resolve without stopping) — it does not wash out.** It is a real, small,
consistent effect, not merely a whole-page-coverage artefact.

**Row right-edge raggedness — the headline finding of this increment, and it runs the OPPOSITE
direction from the brief's own stated hypothesis.** The brief frames it as "rows are ragged and short;
the prose in the tail is justified to the full measure" — implying LOWER raggedness in the tail. The
measurement shows the opposite: mean raggedness is **70.48mm** in the rows-region and **112.89mm** in
the prose-region — **1.60× HIGHER** in the prose region, not lower. Visual inspection (`sheet-10.png`
vs. `sheet-33.png`, this session) explains why: the prose-region pages mix short, single-line
docket-style captions ("IN RE [name]") with multi-line, wrapped disposition paragraphs, and a wrapped
paragraph's own final line is typically short ("petition.", "denied.") while its full lines run close
to the margin. That spread — short trailing lines next to near-full-width lines, on the same page — 
scatters right-edge position MORE than the rows-region's comparatively uniform single-line captions do.
**This is a real, material change in the text block's shape at the turn (item explicitly asked for by
the brief), just not in the direction anyone assumed before measuring it.**

**Text-block width** also changes materially: rows-region mean = **147.73mm**, prose-region mean =
**162.64mm** — the prose region's text block is **14.92mm (10.1%) wider** on average, and its right
edge sits further right (188.14mm vs. 173.23mm mean, sheet width 216.0mm) — consistent with disposition
paragraphs running closer to the full measure than individual docket captions do, even though (per the
raggedness finding above) they do so less *consistently* line-to-line, not more.

**Where the rows-region/prose-region split falls:** the data-derived changepoint (not hand-picked; see
above) lands exactly at the boundary between sheet 32 and sheet 33 — sheets 1–32 (0–6912mm, 0.000–6.912m)
vs. sheets 33–39 (6912–8424mm, 6.912–8.424m). This is precisely the document's own narrative turn: the
disposition sentence is ON sheet 32, and the structurally-derived break coincides with its own page.

**Where the sentence itself falls:** "The petitions for writs of certiorari are denied." begins at
**6757.75mm (6.7578m)** and ends at **6860.75mm (6.8608m)** along the assembled line — inside sheet 32's
own span of [6696, 6912]mm.

### 2. Per-sheet summary (see `plate-manifest.json` for full per-sheet figures)

39/39 sheets measured. Row count per sheet: 26–29 across sheets 1–38 (sheet 1 measures fewest, 26 —
it carries the masthead/date/section-header lines above its first docket row, which the row-band
detector counts the same as any other line); sheet 39 measures 21 rows, but that count is measured
only over its captured region (see LAST-PAGE DEFECT) and is not directly comparable to the other 38
sheets' counts without that caveat. Whole-sheet ink coverage ranges from 2.291% (sheet 39, again partly
a LAST-PAGE-DEFECT consequence — a shorter captured page has less area to accumulate ink over) — or
2.649% (sheet 37) if sheet 39 is excluded as not fully comparable — to 3.978% (sheet 6).

### 3. Cross-checked, not just carried over

This build's own render-and-measure pipeline is independent of the concept-gate étude's (different
script, all 39 pages instead of 6, a genuinely different row/text-block detection pass) but uses the
same ink threshold and lands on the same sheet 32 sentence position pattern the prior gate found by
hand — both are documented as pixel-measured, not asserted.

## Files produced

- `render/sheet-01.png` … `sheet-39.png` (gitignored) — 864×1118px each, 4px/mm.
- `render/render-log.json` (gitignored) — per-sheet capture metadata, including the sheet 39 shortfall.
- `plate-manifest.json` (committed) — one record per sheet: position, ink coverage (whole-sheet and
  text-block), text-block bbox, row count, row right-edge distribution.
- `line-profile.json` (committed) — the 1mm-column ink-occupancy profile across the full 8424mm line,
  at raw resolution and after 10mm/50mm/200mm moving-average smoothing, plus the rows-region/
  prose-region contrast at each level and the disposition sentence's location.
- `line-strip.png` (committed) — the 39 sheets butted in order at 1px/mm, 8424×280px, 0.76MB. No wall,
  no shadow, no annotation, no colour — the rendered document at low scale, nothing added.
