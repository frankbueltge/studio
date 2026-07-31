# MEASUREMENTS — docket item A4 (the byte ceiling, re-measured) and docket item 8 (page counts, all 72)

*THE BUILDER, convened tonight for two measurements only. Every number below was produced by code run
this session; every script is in `material/` and re-runnable by an outsider. Nothing here was estimated.
Where something could not be measured, that is stated plainly, not papered over.*

---

## 0. Environment and tool inventory — checked first, not assumed

Checked directly this session, by trying each:

| Tool | Present? |
|---|---|
| `node` v22.22.2 | Yes |
| `xvfb-run` / `Xvfb` | Yes |
| Chromium at `/opt/pw-browsers/chromium-1194` | Yes |
| `playwright` (via `NODE_PATH=/opt/node22/lib/node_modules`) | Yes |
| Python 3.11.15 | Yes |
| Python `PIL`/`Pillow` | **No** (`ModuleNotFoundError`) |
| Python `numpy` | **No** (`ModuleNotFoundError`) |
| `cwebp`, `dwebp`, `gif2webp`, `img2webp` | **No** |
| `pngquant`, `optipng`, `pngcrush`, `zopflipng`, `oxipng` | **No** |
| `convert` / `magick` / `identify` (ImageMagick) | **No** |
| `gm` (GraphicsMagick) | **No** |
| `ffmpeg` | **No** |
| Node image packages (`sharp`, `jimp`, `pngjs`, …) under `NODE_PATH` | **No** — only dev tooling (`eslint`, `prettier`, `typescript`, `playwright`, …) |
| `libpng16`, `libwebp7` shared libraries (`dpkg -l`) | Present as **system libraries only** — no CLI tool or language binding exposes them |

**Consequence, stated plainly:** there is no external tool anywhere in this environment that can
produce an indexed PNG, a paletted PNG, or a WebP file. To get real numbers rather than none, this
session built two small pieces of new material (both committed, both re-runnable):

1. `material/png-codec-lib.js` — a from-scratch PNG decoder/encoder using **only** Node's built-in
   `zlib` module (standard in every Node install, not a special external tool). It implements exactly
   the PNG color types this measurement needs (grayscale, RGB, indexed/palette, RGBA), with the
   spec's standard adaptive per-scanline filtering and `zlib.deflateSync` at level 9. Its output was
   **independently validated** — not just self-consistent — by loading every candidate file back
   through Chromium's own, unrelated PNG decoder (`validate-png-codec.js` pattern) and diffing pixels:
   every encoding this report calls lossless decoded to an **exact, zero-diff pixel match** in
   Chromium's own reader.
2. Chromium's own `canvas.toDataURL('image/webp', 1.0)` — already present, needing no new tool — was
   used to produce WebP, and its actual bitstream was parsed by hand (RIFF chunk walk) to confirm what
   codec it really used, rather than trusting the "1.0" argument's name.

---

## MEASUREMENT 1 — docket item A4: the byte ceiling

### Method

`no-part/build/pdf-render-lib.js` was copied **byte-identical** (diffed at copy time) into
`/tmp/.../scratchpad/render/build/`. `canvas-lib.js` was copied alongside it (needed for
`launchBrowser`/`desaturateToGrayscale`, also unmodified) — neither file was edited.
`material/render-batch.js` (new, committed) swaps the single PDF that `pdf-render-lib.js`'s hardcoded
`PDF_PATH` resolves to (verified by SHA-256 after each copy) so the same unmodified library can render
one page of *any* input PDF, exactly mirroring how `no-part`'s own `render-sheets.js` finds its one
source file.

**Sample:** 14 documents — the 5 verified in the prior session (SOCHOR 07-14, HERRIDGE 07-02, DUCKETT
07-28, OCCHICONE 07-28, DUCKETT ET AL. 07-28) plus 9 more spread across every month of the term
(Oct, Nov, Dec, Jan, Feb, Mar, Apr, May, Jun), all fetched fresh this session (SHA-256 recorded) and all
72 Miscellaneous Orders of the term were fetched for Measurement 2 alongside them. All 14 rendered
successfully at the house's proven 4 px/mm scale (one transient "Could not detect page top-left corner"
on first attempt for SOCHOR, cleared on retry — noted, not hidden; a 3× repeat render of that same file
afterward produced the byte-identical output all three times).

**Reproducibility check:** all 5 previously-measured documents reproduced their **exact** prior baseline
byte counts (95,667 / 123,384 / 96,043 / 97,691 / 100,526) — confirming this session's pipeline is the
same one, not a near-miss.

### What Chromium's own baseline PNG actually is

Direct inspection of the PNG header bytes (IHDR) of every rendered page: **color type 6 (truecolor +
alpha, RGBA), 8-bit, no interlace** — confirmed on every sample. Two immediately measurable facts follow:

- **The alpha channel carries zero information.** Scanned every pixel of every sample: alpha is exactly
  255 everywhere, always. Dropping it is exactly lossless.
- **There is a real, non-trivial color cast**, exactly as `canvas-lib.js`'s own comment describes for
  anti-aliased glyph edges: measured max |R−luminance| / |G−luminance| / |B−luminance| deltas of
  **97–98 (out of 255)** on every sample (mean deltas are small, 0.4–1.3, because it's confined to edge
  pixels — but it is real and it is measured, not "faint" by assertion).

### Candidate encodings measured (14-document sample, base64 bytes — the operative figure since the
work inlines images)

| doc | baseline (RGBA8 PNG) | RGB8 (α dropped) | grayscale PNG | indexed PNG | 1-bit bilevel PNG | lossless WebP (post-correction) |
|---|---:|---:|---:|---:|---:|---:|
| 010726zr_21o3 | 123,112 | 73,604 | 29,228 | 30,268 | 3,864 | 27,376 |
| 020426zr_3eb4 | 118,388 | 71,160 | 27,780 | 28,820 | 3,776 | 25,984 |
| 030326zr_6537 | 128,084 | 77,760 | 30,808 | 31,848 | 4,016 | 28,676 |
| 040926zr_3f14 | 117,676 | 70,224 | 27,444 | 28,484 | 3,684 | 25,780 |
| 051526zr_1a72 | 104,064 | 60,488 | 24,280 | 25,320 | 3,292 | 22,088 |
| 061126zr_m6io | 138,796 | 87,152 | 34,292 | 35,332 | 4,396 | 32,136 |
| 070226zr_2cp3 (HERRIDGE) | 164,512 | 107,284 | 42,268 | 43,308 | 5,332 | 39,964 |
| 071426zr_2dp3 (SOCHOR) | 127,556 | 77,236 | 30,620 | 31,660 | 3,996 | 28,592 |
| 072826zr1_b97c (OCCHICONE) | 130,256 | 79,428 | 31,420 | 32,460 | 4,072 | 29,412 |
| 072826zr2_jifl (DUCKETT ET AL.) | 134,036 | 83,040 | 32,840 | 33,880 | 4,308 | 30,624 |
| 072826zr_8n5a (DUCKETT) | 128,060 | 77,612 | 30,796 | 31,836 | 4,016 | 28,752 |
| 100625zr_3fbh | 105,416 | 61,668 | 24,556 | 25,596 | 3,348 | 22,468 |
| 111225zr_6kgn | 132,836 | 82,044 | 32,380 | 33,420 | 4,200 | 30,232 |
| 120525zr_hejm | 262,412 | 183,224 | 71,140 | 72,180 | 8,780 | 68,440 |
| **mean** | **136,800** | **85,137** | **33,561** | **34,601** | **4,363** | **31,466** |

(Mean baseline, 136,800, matches last session's 5-doc mean of 136,883 within sampling noise —
confirms the two sessions measured the same thing.)

### Fidelity — stated for each, not asserted

- **RGB8 (alpha dropped):** **exactly lossless** relative to the actual rendered page. Alpha is
  uniformly 255 everywhere (measured, not assumed) — dropping it discards nothing. Mean saving vs.
  baseline: **~38% smaller** (62.2% of baseline).
- **Grayscale PNG / indexed PNG / lossless WebP:** **NOT lossless relative to the raw rendered page.**
  All three are built from (or equivalent to) the luminance-forced, color-cast-corrected pixels — the
  same correction `canvas-lib.js`'s `desaturateToGrayscale` already applies elsewhere in this house, on
  the argument that the cast is a rendering-pipeline artifact, not real ink. That argument is **not
  re-litigated here** — it is simply named: choosing any of these three means accepting a measured,
  bounded departure from the true captured pixels of **up to 97–98/255 per channel at some pixels**
  (mean 0.4–1.3/255 over the whole page). If that departure is not acceptable, none of these three
  encodings may be used, and RGB8 is the ceiling.
- **Indexed PNG does NOT beat grayscale PNG — it is measurably *worse*, on every sample.** The
  reason is itself a measured fact worth stating precisely, since it directly tests last session's
  untested speculation: every sample's corrected content uses **all 256 distinct gray levels**
  (`distinctGrayLevels: 256` on every document, confirmed by direct histogram), so the indexed
  encoding gets no bit-depth reduction (still 8 bits/pixel) and only *adds* a 768-byte palette table on
  top of what grayscale already stores directly. **The "indexed/paletted PNG... would likely shrink
  several-fold" line from last session's report is measured and refuted for this content: it does not
  shrink at all past plain grayscale; it is ~3% larger.**
- **1-bit bilevel PNG: NOT lossless, and the departure is large enough to name.** Thresholding at
  luminance 150 (the pipeline's own ink/background constant) changes **1.7%–5.2% of all pixels** per
  page (mean ~2.2%), with a maximum per-pixel swing of 150/255 and a per-page mean absolute difference
  of 1.0–2.9/255. This is the anti-aliased softness of typewriter glyph edges being snapped to pure
  black/white — a real, visible loss for a work whose stated purpose is reproducing a court's actual
  sheet, not a redrawn one. It is reported here as a measured extreme, not recommended as the answer.
- **Lossless WebP is genuinely lossless where reported (round-trip pixel diff = 0, all channels, every
  sample) — but ONLY after the grayscale correction.** Its bitstream was inspected directly (RIFF chunk
  walk): `VP8X` container → `ICCP` (456 bytes) → **`VP8L`**, confirming a true lossless payload, not a
  high-quality lossy guess. **On the RAW, uncorrected rendering, however, Chromium's own lossless WebP
  encoder produced files roughly 2–3.7× *LARGER* than the baseline PNG** (measured directly: e.g.
  SOCHOR's raw rendering, 95,667-byte baseline PNG, encoded to a 354,936-byte "lossless" WebP) — because
  VP8L's cross-channel prediction assumes correlated R/G/B, and the real color cast measured above
  (up to 97–98/255 between channels) defeats that prediction badly. **This is the session's most
  surprising finding: WebP is only competitive with plain grayscale PNG once you have already paid the
  fidelity cost of desaturation — applied directly to the actual rendered page, it is a severe
  regression, not the "several-fold shrink" the proposal speculated.**

### The deliverable ceiling, recomputed (base64 bytes × N; mean per-page bytes above)

| N | baseline (current) | RGB8 (fully lossless) | grayscale PNG (lossless mod. correction) | lossless WebP (lossless mod. correction) | 1-bit bilevel (LOSSY) |
|---:|---:|---:|---:|---:|---:|
| 8 | 1.09 MB | 0.68 MB | 0.27 MB | 0.25 MB | 0.035 MB |
| 22 | 3.01 MB | 1.87 MB | 0.74 MB | 0.69 MB | 0.096 MB |
| 55 | 7.52 MB | 4.68 MB | 1.85 MB | 1.73 MB | 0.240 MB |
| 72 | 9.85 MB | 6.13 MB | 2.42 MB | 2.27 MB | 0.314 MB |
| 200 | 27.36 MB | 17.03 MB | 6.71 MB | 6.29 MB | 0.873 MB |

**N at which the ~3 MB shipped-total guideline is spent**, and **N at which a single 2 MB file (the
site's hard per-source-file gate, `SITE-API.md` line 107 — binding if all inlined images live in one
committed file, e.g. one `data.json` or one built `index.html`, as `NO PART`'s own pattern does) is
hit:**

| encoding | N @ ~3 MB guideline | N @ 2 MB hard gate |
|---|---:|---:|
| baseline (current) | **21.9** | **14.6** |
| RGB8 (fully lossless) | **35.2** | **23.5** |
| grayscale PNG (mod. correction) | **89.4** | **59.6** |
| lossless WebP (mod. correction) | **95.3** | **63.6** |
| 1-bit bilevel (lossy) | 687.6 | 458.4 |

### Plain statement — this is not "we'll deal with it later"

The best **fully lossless** encoding (RGB8) moves the wall from N≈15–22 to N≈24–35 — still well inside
one term (55 unit-days / 72 documents). The best **available** encoding at all (grayscale PNG or
lossless WebP, both requiring acceptance of the pre-existing, bounded, house-precedented color
correction) moves the hard 2 MB gate to **N≈60–64** — better, genuinely several-fold, but this is **still
short of N=72** (one full term of Miscellaneous Orders) and **nowhere near N=200**. Since the work's
own model accumulates with no cap, and no tested encoding — including the most-hoped-for one — pushes
the wall past even one term, **encoding choice alone does not resolve the ceiling.** A work built on this
model needs one of: (a) a hard cap on N well inside a single term, (b) a different delivery architecture
than "everything inlined in one shipped file" (e.g. paged/lazy-loaded assets — outside this session's
two-measurement scope to design), or (c) an explicit, adopted decision to accept the RGB8-only true
losslessness ceiling (N≈24–35) as the work's actual lifespan before it must stop, be re-architected, or
break the site's own stated gates. None of these is free, and none was decided tonight — that decision
belongs to the gate, not to this measurement.

---

## MEASUREMENT 2 — docket item 8: how many Miscellaneous Orders run to more than one page

### Method

All 72 Miscellaneous Order PDFs of the 2025 Term were fetched (not a sample — the complete set),
SHA-256-recorded. `material/count-pdf-pages.py` (new, committed) counts pages two independent ways with
no PDF library:

- **Method A:** count objects whose dictionary declares `/Type /Page`, scanning both the raw file bytes
  and every zlib-decompressible stream in the file (necessary because every document in this corpus
  stores its page-tree dictionaries inside compressed object streams — `/ObjStm` — not as plain bytes;
  a naive raw-byte scan finds **zero** page or page-tree dictionaries in any of the 72 files until this
  decompression pass is added).
- **Method B:** find every `/Type /Pages` (page-tree node) dictionary and read its own `/Count` entry,
  taking the maximum found (no intermediate node exceeds the root's count in a well-formed tree). This
  required a real, documented fix mid-session: the first version only looked for `/Count` *after* the
  `/Type /Pages` token, and every single document in this corpus stores `/Count` *before* `/Type` inside
  the same flat dictionary (e.g. `<</Count 1/Kids[27 0 R]/Type/Pages>>`) — the original version found
  **zero** matches on all 72 files. Fixed to locate the enclosing `<< ... >>` span first and search
  `/Count` anywhere inside it; **after the fix, methods A and B agree on all 72 of 72 documents** (0
  disagreements) — this is reported plainly as the kind of bug this house has already named as a
  recurring risk (`FEASIBILITY.md` §6).
- **Third, independent cross-check** (not scripted, done by hand for the 2 documents method A/B flagged
  as multi-page): decompressed the actual `/Kids` array of the page-tree dictionary and counted its
  entries directly — `Kids[54 0 R 1 0 R]` and `Kids[45 0 R 1 0 R]`, i.e. **2 entries each**, matching
  both other methods.

### Distribution, all 72 documents

| page count | number of documents |
|---:|---:|
| 1 | 70 |
| 2 | 2 |

### The exact multi-page documents

| date | file | URL | page count | case |
|---|---|---|---:|---|
| 2025-11-07 | `110725zr_pnk0.pdf` | <https://www.supremecourt.gov/orders/courtorders/110725zr_pnk0.pdf> | **2** | No. 25A539, *Rollins v. Rhode Island State Council of Churches* — administrative stay order (SNAP funding) |
| 2025-11-10 | `111025zr_3ebh.pdf` | <https://www.supremecourt.gov/orders/courtorders/111025zr_3ebh.pdf> | **2** | No. 25A539, same case — follow-up scheduling order |

Both are real, substantive 2-page orders in the same emergency SNAP-funding case (not scanning
artifacts, not blank second pages — confirmed by running `extract-order-text.py` on both: each produces
distinct, complete legal text spanning what its own page tree declares as 2 pages).

### What fraction of the work's unit-days this affects

**2 of the 72 documents (2.8%)** run to more than one page. Both fall on distinct calendar days, and
neither day carries any *other* Miscellaneous Order that session's data would need to merge with it.
Against the 55 distinct days that carry a Miscellaneous Order (`MATERIAL-2026-07-31.md` §1):
**2 of 55 unit-days (3.6%) would need to display a multi-page document under the work's stated "one
page-height per calendar day" model.** Every one of the other 96.4% of unit-days is confirmed
single-page — cross-checked by two independent methods that initially disagreed (0/72) and now agree
(72/72) after a fix documented above, plus a hand cross-check of the two exceptions' actual `/Kids`
arrays.

**Plain statement:** the "one page-height per day" model is not violated by a majority or even a large
minority of the corpus — but it is violated by a real, non-hypothetical, non-zero fraction (3.6% of
unit-days), on a real case (a capital-adjacent-in-urgency emergency stay), not an edge case invented for
this measurement. The model needs an explicit answer for what a multi-page day means (stack both page
heights? crop to page 1 only, silently discarding page 2's substantive text? something else?) before
it can be called complete, not a hypothetical for later.

---

## What could not be measured, stated plainly

- **True lossless WebP applied directly to the raw, uncorrected rendering** was measured, but its
  result (2–3.7× larger than baseline) is reported as a fact, not converted into a "best" number — it
  is not competitive with anything else tested.
- **Whether the site's `≤ 2 MB per file` gate applies to one bundled data/HTML file (this report's
  working assumption, matching `NO PART`'s own committed-output pattern) or to per-page image files
  individually** was not resolved — `SITE-API.md` line 107 states the rule for `src/**` submissions in
  general terms and this session did not find or build the actual at-any-time build architecture to
  check which layout it would use. If pages ship as separate committed source files instead of one
  inlined blob, the binding constraint could instead be the **`≤ 50 files`** cap, hit at N=50 regardless
  of encoding — a different ceiling than anything in the byte tables above. This is named as unresolved,
  not decided by assumption.
- **Adaptive PNG filtering vs. this session's implementation being fully optimal**: `png-codec-lib.js`
  uses the standard min-sum-of-absolute-differences heuristic (libpng's own default), not an exhaustive
  or zopfli-grade search — a dedicated tool (were one installed) might shrink these numbers by some
  further single-digit percentage. Not measured; not claimed.
- **Whether Chromium's lossless-WebP behavior (`quality=1.0` → true VP8L) is a documented, stable
  contract or an implementation detail of this specific Chromium build** was not checked against any
  specification — it was verified empirically (RIFF chunk inspection, round-trip pixel diff) for the
  build actually present, and no claim is made about other Chromium versions.

## Files

- `material/count-pdf-pages.py` — page-count measurement (Measurement 2), the two independent methods.
- `material/png-codec-lib.js` — from-scratch PNG encoder/decoder (Node `zlib` only), independently
  validated against Chromium's own decoder.
- `material/render-batch.js` — batch driver wrapping the unmodified `pdf-render-lib.js`.
- `material/measure-encodings.js` — baseline / RGB8 / grayscale / indexed / bilevel1 / raw-WebP
  measurement and fidelity diffing (Measurement 1).
- `material/measure-webp-on-gray.js` — lossless-WebP-on-corrected-content measurement and round-trip
  fidelity check.

The 72 fetched PDFs are **not committed** (public, addressable by the URLs in
`material/orders-2025-term.json`, exactly as this house's standing practice already treats source PDFs).
