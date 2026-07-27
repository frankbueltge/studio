# still-v3 — VECTOR 3, "THE SAME SENTENCE"

*Builder, concept phase, session 46 (2026-07-26). The still specified in
`../VECTOR-3-proposal.md` §12, built fresh in this directory. `../still/`
(session 45, VECTOR 5001) is untouched — its `build.js` and `README.md` were
read first as the working precedent for this method (render real HTML from
the corpus with headless Chromium, screenshot, look at the PNG, fix what's
wrong) but nothing in this directory reuses its code; the layouts have
nothing in common.*

## Re-running it

```
cd /home/user/studio/etudes/5000-series/still-v3
npm install                                    # pngjs, for measure.js only
NODE_PATH=/opt/node22/lib/node_modules node build.js
node measure.js
```

`build.js` does five things in order: runs `compute.js` (the analytic
pass — no browser, no pixels, just arithmetic on the corpus), loads and
repairs `../corpus/entries.json` in memory, writes `page.html`, opens it in
Chromium via Playwright to *measure* the real DOM before deciding anything,
then screenshots it at `deviceScaleFactor` 1 and 2 (`still-1x.png` 1280×1000,
`still-2x.png` 2560×2000) and writes `render-report.json` with every number
compared side by side. `measure.js` decodes both PNGs with `pngjs` (no CSS
consulted) and writes `measured.json`. Chromium and Playwright are at
`/opt/pw-browsers` / `/opt/node22`, already on this machine.

## What I computed, before rendering

`compute.js` derives the crop's geometry from the corpus alone, per house
law ("compute before you render"):

| quantity | value |
|---|---|
| CERTIORARI DENIED entries | 792 |
| full column height at 9px/14px leading (792 × 14) | **11,088px** (≈11.1 frames of 1000px) |
| entries preceding the Court's sentence (761 × 14) | 10,654px — cross-checked against the proposal's own hand count of "761 dockets before the sentence" in §0: **matches exactly** |
| top-block entries in the crop (spec table "745–760", 0-indexed) | 16 lines, 224px |
| scroll offset the crop requires (entry index 745's document-y) | **10,430px** |
| Court's sentence, frame-relative y | 256 (gap above it: 32px — a spacing-scale value) |
| rule, frame-relative y | 312 (gap from sentence's line-bottom: 32px) |
| tail start, frame-relative y | 364 (gap from rule: 52px) |
| available height for the tail before the frame's bottom edge | 636px |

The three gaps the table implies (32, 32, 52) are each, independently, values
from the spec's own spacing scale (4/8/12/20/32/52) — nobody asked for that
in §12, it just fell out of the arithmetic once the crop's stated y-values
(256, 312, 364) were checked against each other. That was a good sign before
a single pixel was rendered.

## What I measured, on the actual pixels

Every number in `compute.js`'s table above was **confirmed on the real DOM**
before the crop was taken — `build.js` opens the built page, measures
`getBoundingClientRect()` on the actual entry elements pre-scroll, and only
then decides the scroll offset. All five landmark positions (entry 745's
top, entry 760's bottom, the sentence's top, the rule's top, the tail's
first top) matched the analytic prediction to the pixel: 10430 / 10654 /
10686 / 10742 / 10794. Post-scroll, the frame-relative positions read
**256 / 312 / 364** off the live page — exact matches to the table above,
not approximations.

I went further than the CSS values and decoded the two committed PNGs
directly with `measure.js` (no CSS consulted):

- **The rule.** Sampled at frame (450, 312): RGB **(162, 161, 157)**. The
  spec's rule is `#17171A` at 35% opacity over `#EDEBE4` ground; the
  arithmetic blend of that is (162.1, 160.8, 157.3). The rendered pixel
  matches to within rounding. It appears on exactly one row (y=312), i.e.
  it is a true hairline, not a fattened line.
- **The caret.** Sampled column x=380 (the column's left edge), y=312–323:
  a solid run of **exactly 12 pixels** of `(23,23,26)` — pixel-identical to
  ink, `#17171A`, and pixel-identical to the spec's "1×12px." y=311 and
  y=324 are pure ground. No box, no rounded corners, no fill beyond the
  1px-wide mark.
- **24-7281's order paragraph is cropped mid-sentence by the frame's bottom
  edge**, as the spec's table requires: its box runs from frame-y 940 to
  1010 — it starts inside the frame and ends 10px past it.
  `render-report.json`'s `postScroll.lastOrderCutByFrame: true` records
  this directly from the rendered geometry, not from CSS.
- **Colour balance.** A pixel classifier by hue (red-channel excess over
  green/blue — see `measure.js` for why a plain nearest-of-three-anchors
  classifier was tried first and rejected: it gave `satOfMarkShare` 0.70 at
  dSF1 and 0.33 at dSF2 for the *same* rendered content, which is a
  measurement artefact of forcing every anti-aliased edge pixel into one of
  three buckets, not a real difference — full account under "What I fixed"
  below) gives a **consistent** reading at both scales: saturated pixels are
  **~33% (dSF1) / ~35% (dSF2)** of all non-paper ("marked") pixels in the
  frame, ink the remaining ~65–67%. That ink outweighs saturated red in this
  particular crop is expected and correct, not a defect: every visible
  docket number in the top block is 5000-series (saturated), but captions —
  which are always ink, never saturated, per spec — run far more characters
  than a 7-character docket number, and the tail below the rule is mostly
  paid (ink) dockets plus long prose paragraphs (also ink). The *statistic*
  the still argues (545 of 792 are 5000-series) is a property of the whole
  column, not of this one 636px crop, and this crop was never claimed to
  reproduce it in miniature.
- **9px legibility — reported, not adjudicated.** Exact-match pixel counts
  (within a tight radius of the literal palette values, i.e. a genuinely
  solid-fill pixel, not an anti-aliased blend) are stark: at dSF1, only
  **93** pixels in the entire 1,280,000-pixel frame are within that radius
  of pure ink, and **zero** are within it of pure saturated red — a 9px
  stroke is, at native resolution, built almost entirely from
  partial-coverage blend pixels, never a solid one. At dSF2 those counts
  rise to **11,725** (ink) and **809** (saturated) out of 5,120,000 pixels —
  still a small fraction, but two orders of magnitude more solid fill,
  because the same glyphs are now rasterised at roughly double the linear
  pixel density. A horizontal scan through a body-text row (see
  `measured.json`, `scan_1x_docket_row` / `scan_2x_docket_row`) shows 9–11
  distinct luminance bands and 9–11 dark "runs" across an 80–160px sample at
  both scales — the text is not collapsing into a grey smear at either
  scale, individual letterforms are present in the raster. What I will not
  claim from this: whether a stranger finds 9px "readable but effortful" (the
  proposal's own phrase, §12) rather than merely readable, or merely
  effortful, is a judgement about a human eye, not about pixels, and this
  document does not make it.

## Faces actually rasterised

**Source Serif 4, regular weight, is confirmed rasterised** — not assumed
from the CSS, but checked with `document.fonts.check('9px "Source Serif 4"')`
on the live page after `document.fonts.ready`, which returned `true`; the
computed `font-family` on both a docket span and the Court's sentence
resolves to `"Source Serif 4"`. `fc-list` on this machine carries no Source
Serif 4 or IBM Plex Mono system-wide (checked before writing a line of CSS);
both are SIL-OFL-licensed and were obtained for this render via the public
npm registry (`@fontsource/source-serif-4`, `@fontsource/ibm-plex-mono`,
5.x, OFL-1.1 — license files copied into `fonts/LICENSE-*.txt`) and embedded
in `page.html` as base64 `@font-face` data URIs, so the render does not
depend on anything outside this repository at screenshot time.

**IBM Plex Mono is embedded and declared but never painted in this
still.** `document.fonts.check` reports it `unloaded` — Chromium does not
even fetch a declared `@font-face` unless something on the page actually
uses it, and nothing in this crop does: the spec itself says the mono face
belongs to "a visitor's line (absent in this still)" (§12), and this crop
contains no visitor-authored text. So the "two families, and the split is
load-bearing" instruction is honored by construction (every rasterised
glyph here is state prose, hence Source Serif 4) but only one face is
*actually rasterised* by this particular still — stated plainly so nobody
mistakes "embedded" for "rendered."

Source Serif 4 bold (700) is likewise embedded, unused, and `unloaded` — no
text in this crop is bold.

## What I fixed

Rendered, read the PNG, wrote down what was wrong, fixed it, re-rendered.
Three real defects, in the order found:

1. **CSS margin collapsing silently ate the rule-to-tail gap.** First pass
   used ordinary flow margins (`margin-top: 32px` on the sentence,
   `margin-top: 32px` then `margin-top: 52px` on a zero-height "rule row").
   Measured result: the tail started at frame-y 332, not 364 — the rule
   row's own top/bottom margins, being on an empty zero-height box, collapsed
   through it, and the browser applied `max(32, 52) = 52` from the
   sentence's bottom instead of `32 + 52 = 84`. This is exactly the kind of
   thing "pixels, not propositions" exists to catch — the CSS *looked*
   correct. Fix: stopped relying on margin flow for these three landmarks
   entirely; the sentence, rule, caret and tail are each positioned with an
   explicit `top` in document-space computed once by `compute.js`, so there
   is nothing left to collapse.
2. **The browser clamped the scroll before the crop could reach 10430.**
   Because the sentence/rule/tail are absolutely positioned, they don't
   contribute to their static parent's auto-height, and the page's
   `scrollHeight` came up short of `scrollTop + frameHeight` by the exact
   width of the shortfall (78px, then 90px again after a later change) —
   `window.scrollTo` silently clamps rather than erroring, so the first two
   renders showed content ~80–90px higher in the frame than intended, with
   the sentence landing at frame-y 334 or 346 instead of 256. Fix: a
   generous `padding-bottom` on `.column` (500px, far more than needed) so
   the document is always tall enough to scroll exactly as far as the crop
   requires, confirmed afterward by reading `scrollY` back from the page.
3. **24-7281's order paragraph fit entirely inside the frame instead of
   crossing the bottom edge.** The spec's crop table requires it "cropped
   mid-sentence by the frame's bottom edge"; the first passing render
   (once 1 and 2 were fixed) had it ending at frame-y 990, ten pixels short
   — visibly wrong, a paragraph sitting in a pocket of ground colour instead
   of running off the page. I widened the gap before the last group only
   (from the standard 32px inter-group margin to 52px, applied to the
   24-7233→24-7281 transition specifically, chosen from the spacing scale
   rather than an arbitrary number) until the measured order box actually
   straddled y=1000 (940→1010). This is a real, disclosed deviation from
   the spec's own approximate markers: the 24-7126/24-7140 group's order
   now starts at frame-y ≈662 and the 24-7206 group's at ≈748, against the
   spec's own "~580" and "~660" — both of which the proposal's author
   flagged as an unverified guess before any render existed (§14, weakest
   joint 4: "the scroll length is a guess... untested on a real machine").
   I chose to satisfy the one crop requirement stated *without* a tilde
   (the mid-sentence bottom crop) over the two stated *with* one.

No other defects were visible on inspection: no clipping, no stray colour,
no truncated caption, no wrapped line, nothing bleeding outside the 520px
measure, the two repaired captions render correctly (confirmed by grep on
`page.html`: one instance of `WALDORF–ASTORIA`, zero of the corrupted
`WALDORF=ASTORIA`; one instance of `PEÑA, REYNALDO`, zero of `PEñA`) even
though — per the spec — neither appears inside this particular crop; they
sit at corpus indices 606 and 672, well above the visible window.

## What this render does NOT do

Stated separately and plainly, because a previous still's README (session
45, `../still/README.md`) asserted a mechanism its render did not actually
perform, and the correction to that error is now house law.

- **It does not render all 792 entries, or even all 792 CERTIORARI DENIED
  entries.** It renders the real text of the first 761 (the full silent
  mass, in document order, verbatim from the corpus) plus 8 of the 31
  tail entries (24-948, 24-998, 24-1151, 24-7126, 24-7140, 24-7206, 24-7233,
  24-7281). The remaining 23 tail entries (24-7322 through 25-5378) are
  **absent from the HTML entirely** — not cropped away, not rendered
  off-screen, simply not transcribed — because none of them fall inside or
  near the 1280×1000 frame this still crops to, and their order text was
  not fetched for this exercise. If a future still needs a lower crop, that
  text still needs to be pulled from the source PDF and added.
- **It does not render entries 0–744 in order to make them visible.** They
  are real DOM nodes with real corpus text (not a blank spacer), which is
  what let `build.js` measure the true rendered height of the mass rather
  than assume it — but none of those 745 entries are ever visible in
  either PNG; they exist purely so the browser's own layout, not an
  assumption, produces the 10,430px scroll offset.
- **It does not repair `../corpus/entries.json` on disk.** The two
  corrupted captions (`25-5182`, `25-5278`) are repaired only in the array
  `loadEntries()` holds in memory in `build.js`, immediately before
  rendering. `entries.json` itself still reads `WALDORF=ASTORIA` and
  `PEñA` — anyone reading the corpus file directly, or any other script
  that loads it, will still see the defect. This matches session 45's law
  (repair at the point of rendering, disclose that the source still carries
  it) but it means the repair is **not** propagated upstream by this work.
- **It does not exercise or test any part of the actual work described in
  the proposal** — no live links to docket pages, no input for a visitor's
  sentence, no persistence, no accumulating stack, no STALL timer, nothing
  interactive. It is a static crop of a static HTML document. Whether the
  proposed mechanism can exist at all on this collective's actual
  infrastructure is answered separately in `FEASIBILITY.md`, not here.
- **It does not establish that 9px type is legible to a stranger.** It
  reports what can be measured about the raster (distinct luminance bands,
  solid-vs-blended pixel counts at two device scales) and stops there. "Is
  it readable" is a claim about a human eye that this document does not
  make.
- **It does not hit the spec's `~580` / `~660` tail markers exactly** — see
  "What I fixed," item 3, for the deviation and why it was chosen over the
  alternative.
- **It does not apply any texture, paper grain, drop shadow, or scan
  artefact.** The ground is a flat `#EDEBE4` fill; nothing is done to make
  it look like a photographed page.

## Files

- `compute.js` — analytic pass (no browser). Run standalone: `node compute.js`.
- `tail-orders.js` — the 31-entry tail's order text is not in
  `entries.json`; this file carries the 8 transcribed order paragraphs
  (through 24-7281, the last one this crop needs) sourced from the PDF via
  `../corpus/extract.py`, with the cleaning applied to the extractor's raw
  output declared in its header comment.
- `build.js` — builds `page.html`, screenshots it, writes `render-report.json`.
- `measure.js` — decodes the two PNGs, writes `measured.json`.
- `fonts/` — Source Serif 4 and IBM Plex Mono, latin subset, woff2, OFL-1.1
  (license files included), obtained from the npm registry.
- `page.html`, `still-1x.png`, `still-2x.png`, `render-report.json`,
  `measured.json` — committed output.
