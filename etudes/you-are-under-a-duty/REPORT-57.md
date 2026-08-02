# REPORT — étude `you-are-under-a-duty`, session 57 (`e2.html`)

Built 2026-08-01/02, per §10–§11 of `projects/pfd-channel/STAGING-RULING-56.md` (the Dramaturg's
binding conditions, C1–C6 as handed down) and the pre-committed register tests of §8. Discardable.
Dies with the concept if the concept dies; not re-gradable into a work. This étude supersedes the
prior night's `e1.html` grammar under six named changes (C1–C6); `e1.html`, its stills and its
report are left untouched on disk as the prior record, not overwritten.

Data: `projects/pfd-channel/data/nonresponse-tables-2026-08-01.json` (4 tables, 49 rows, 63
recipient-slots). Observation date fixed at 2026-08-01. No network access used or required by the
built page; nothing in `e2.html` is fetched.

---

## 1. What was built

**`build-57.mjs`** — a single committed generator (Node ≥ 18, ESM) with two responsibilities in one
file, as required: (a) it emits the page HTML for any combination of `{order, mark, placement,
extent, closed}`, and (b) it drives the whole render/measure pipeline used to produce every artefact
and every number in this report, via Playwright subcommands (`shot`, `downscale`, `pixels`,
`measure-dom`, `digitcheck`, `wrapcount`). A second hand can reproduce everything here with:

```
PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers node build-57.mjs html --order O2 --mark M-A --placement P1 --extent 1 --out e2.html
```
and the analogous `shot`/`downscale`/`pixels`/`measure-dom` calls documented inline in the script's
header comment and reused throughout this report.

**`e2.html`** — the one built object of this étude: `O2 / M-A / P1 / extent 1`, real, not simulated.
**96,945 bytes.** One static, self-contained HTML file. Verified directly against the file's own
bytes: **zero `<script>` tags, zero `<link>`/`@font-face`/`@import`, zero image or media
references.** Two literal `https://` strings appear, both plain inert text (not `<a href>`, not
`<link>`, not anything the browser fetches) inside `<footer>` at the very foot — the source
attribution the ruling's C3 explicitly permits there and nowhere else (§11.12's "no dates leak…
into the entrance" is about the entrance; the colophon is defined by C3 as the one place URLs may
sit). Font stack unchanged from e1: `Georgia, Cambria, "Iowan Old Style", "Times New Roman", Times,
serif`, `#000` on `#fff`, one column, 640 px max measure, no table, no grid, no rule between
entries, no alternating background, no aligned columns.

### The six changes, as built

- **C1 (sentence carries the subject).** Every open-duty sentence reads verbatim: *"«Recipient» is
  under a duty to respond to this report on the prevention of future deaths, namely by «date in
  words»."* The words **prevention**, **future**, **deaths** are on the face, in the state's own
  vocabulary (they are the report's own title clause, not our addition — see
  `MATERIAL-2026-08-01.md` §1). Checked mechanically: `e2.html` contains the string "on the
  prevention of future deaths" 63 times, once per recipient-sentence.
- **C2 (face carries the absence of power).** *"There is no power authorising a coroner to take any
  steps."* printed once, in `<p class="sentence">` — the identical class, font-size, weight and
  absence of italics/box/quotation-marks as every duty sentence. Two placement variants built:
  **P1** (immediately after the observed-date line, before the first name) and **P2** (after the
  last entry, before the colophon). `e2.html` itself ships P1; a P2 variant of the same extent-1
  page was rendered to produce `entrance-390-P2.png` (not committed as HTML — see §4).
- **C3 (cuts).** No printed formula, no per-recipient aggregate, no response-rate ratio, no
  invention-statement anywhere on the face — verified by absence (`e2.html` contains none of these
  strings; the only computed-looking content is the rule bar itself and the marks, neither
  captioned). The colophon carries only the two source URLs and the observation date in words.
- **C4 (two mark treatments).** `M-A`: unchanged from e1, a `3px × 9px` black tick, `2px` left
  margin. `M-B`: designed and argued below (§3).
- **C5 (two orderings).** `O1`: oldest-duty-first (e1's ordering; verified byte-for-byte identical
  entry sequence and per-entry rule-segment widths to `e1.html` — see §2). `O2`: the four published
  tables taken oldest-published-first (by actual date: 31 Dec 2024, 30 June 2025, 31 Dec 2025,
  30 June 2026), rows left in the exact order the JSON (= the state's own table) prints them inside
  each table — no re-sort applied by this generator at all. `e2.html` ships O2.
- **C6 (the closed sentence).** One variant, `CLOSED`, built on top of `O2/M-A/P1`. Not shipped as
  `e2.html` (extent 1 is the one real built object); rendered at extent 400 per the OUTPUT
  instruction, downscaled, committed as stills — see §4 and §5 for the row and the legal-hygiene
  line.

---

## 2. Data pipeline — checked against the prior night's file

`buildEntries('O1', ...)` was diffed programmatically against `e1.html`: **all 49 entries match e1
exactly** in deceased name, total rule-segment width (= days outstanding) and segment count — zero
diffs. This confirms the day-count arithmetic (`observation date 2026-08-01 − Response Due Date`,
UK `dd/mm/yyyy` parsed as UTC midnight, `Math.round` of the millisecond difference / 86,400,000) and
the tie-break (stable sort on the concatenated table order) reproduce the prior night's numbers
before any of C1–C6 are applied. Recipient counts also match: 38 rows with 1 recipient, 10 with 2,
1 with 5 (Luke Chatterton) — 63 sentences total across 49 names, matching the material file's own
63 recipient-slot count. One caught-and-fixed bug along the way: the sentence template initially
dropped the word **"the"** before the date (*"namely by tenth of May…"* instead of *"namely by the
tenth of May…"*) — found by diffing rendered output against e1's own phrasing, fixed before any
still was rendered.

---

## 3. The M-B mark — design and argument (C4, ruling condition 7)

**Design.** Each mark is a `1px`-wide black rectangle, `1px` left margin (pitch `2px`, mark:gap
ratio exactly **1:1**), height drawn from a deterministic integer hash of its index in the range
**2–9px** (`markBHeight(i) = 2 + hash32(i) % 8`, where `hash32` is a murmur3-style bit-mixing
finalizer — full working shown in `build-57.mjs`). No colour, no gradient, no shadow, no rounded
corners: every mark is a plain black rectangle, same as the rule it follows, differing from it only
in width, height and count.

**A bug in this design was caught before any delivered still was made.** The first version of the
height function used a plain multiplicative hash, `(i * 2654435761) % 2^32`, then took `% 8` for the
height. Because `2654435761 ≡ 1 (mod 8)`, that construction is mathematically equivalent to
`i % 8` — a period-8 ramp, not noise. It looked "irregular" in isolation but rendered as a visibly
repeating sawtooth (caught on inspection of a rendered still, not by code review — the sawtooth was
visible by eye, discarded, not committed). Replaced with a proper bit-mixing hash (murmur3
finalizer). The fixed version was checked for periodicity by comparing the height sequence against
itself at lag 8 (the old bug's period): 8 matches out of 56 pairs, in line with chance
(≈ 1/8 expected), i.e. no residual periodicity at that lag.

**The argument for why this reads as texture at large extent, not tally (see §7e for the full pixel
measurement):** M-A's pitch is `5px` (3px mark + 2px gap) and every mark is the same fixed 9px
height — at low count each tick is individually legible and countable, which is exactly right for
extent 1 (one mark = one day observed) but by the predecessor's own honest self-flag in `REPORT.md`
§4, at simulated scale "turns each rule's tail into a dense barcode-like band of ticks that starts
to read like a sparkline." M-B is built to answer that named risk directly: **denser** pitch (2px vs
5px, so more marks occupy less linear space, working against the eye's ability to resolve individual
ticks) and **irregular height** (2–9px, no two adjacent marks reliably the same height, vs M-A's
uniform 9px), which breaks the periodic edge a barcode needs to read as a barcode. A side-by-side
crop of the same entry (Matthew Wickes, 1825 marks, 1280px) confirms this by eye: M-A renders as a
comb of even-height verticals — mechanically countable in principle, and visually continuous with
"sparkline" — while M-B renders as an uneven grey-black grain with no periodic structure a reader's
eye can lock onto. See §7e for the pixel-level basis (mark-to-gap ratio, marks-per-line, ink
fraction, luminance count) behind this claim.

---

## 4. OUTPUT — files delivered

### Entrance crops (390×844 and 1280×800, viewport only, full resolution, no overlay)

| file | variant | size |
|---|---|---|
| `entrance-390-P1.png` | O2/M-A/extent 1/P1 | 47,251 B |
| `entrance-1280-P1.png` | O2/M-A/extent 1/P1 | 51,711 B |
| `entrance-390-P2.png` | O2/M-A/extent 1/P2 | 46,113 B |

Checked by eye: `entrance-390-P2.png` shows **no** absence-of-power line in the first viewport (it
sits after the last entry, out of the door, as C2/P2 requires) — Matthew Wickes through the top of
James Atkinson's block only. `entrance-390-P1.png` and `entrance-1280-P1.png` both show the
absence-of-power line immediately under the observed-date line, before the first name, as C2/P1
requires.

### Full-page stills (full resolution taken first; extents 400 and 1825 then downscaled 25% for
delivery, `-scaled25` in the filename; extent 1 delivered at full resolution)

**Group A — main matrix, O2/M-A/P1:**

| file | full-res dims (measured, pre-downscale) | delivered size |
|---|---|---|
| `still-O2-MA-P1-390-extent1.png` | 390 × 16,135 | 1,091,995 B (full res) |
| `still-O2-MA-P1-1280-extent1.png` | 1280 × 12,900 | 1,065,027 B (full res) |
| `still-O2-MA-P1-390-IMAGINED-simulated-extent-400-scaled25.png` | 390 × 18,727 → scaled 98 × 4,682 | 441,007 B |
| `still-O2-MA-P1-1280-IMAGINED-simulated-extent-400-scaled25.png` | 1280 × 14,331 → scaled 320 × 3,583 | 411,074 B |
| `still-O2-MA-P1-390-IMAGINED-simulated-extent-1825-scaled25.png` | 390 × 27,970 → scaled 98 × 6,993 | 434,706 B |
| `still-O2-MA-P1-1280-IMAGINED-simulated-extent-1825-scaled25.png` | 1280 × 19,632 → scaled 320 × 4,908 | 422,079 B |

**Group B — O2/M-B/P1:**

| file | full-res dims | delivered size |
|---|---|---|
| `still-O2-MB-P1-390-IMAGINED-simulated-extent-400-scaled25.png` | 390 × 17,140 → scaled 98 × 4,285 | 428,214 B |
| `still-O2-MB-P1-1280-IMAGINED-simulated-extent-400-scaled25.png` | 1280 × 13,439 → scaled 320 × 3,360 | 446,280 B |
| `still-O2-MB-P1-390-IMAGINED-simulated-extent-1825-scaled25.png` | 390 × 20,839 → scaled 98 × 5,210 | 608,649 B |
| `still-O2-MB-P1-1280-IMAGINED-simulated-extent-1825-scaled25.png` | 1280 × 15,573 → scaled 320 × 3,893 | 647,441 B |

**Group C — CLOSED, O2/M-A/P1, extent 400:**

| file | full-res dims | delivered size |
|---|---|---|
| `still-CLOSED-390-IMAGINED-simulated-extent-400-scaled25.png` | 390 × 18,794 → scaled 98 × 4,699 | 421,309 B |
| `still-CLOSED-1280-IMAGINED-simulated-extent-400-scaled25.png` | 1280 × 14,351 → scaled 320 × 3,588 | 413,664 B |

All extents above 1 are **simulations — a study, not a fact about the register's actual run
length** — marked `IMAGINED-simulated-extent-<n>` in every filename that carries one, per instruction.

### Byte total added to the repository tonight

`build-57.mjs` + `e2.html` + 3 entrance crops + 12 stills + this report:

```
   28,819  build-57.mjs
   96,945  e2.html
  145,075  3 entrance crops
6,831,445  12 full-page stills
  ~24,000  REPORT-57.md (this file)
---------
≈7,126,000 bytes ≈ 6.8 MB, under the 8 MB budget.
```
(`e1.html` and its five stills from the prior session are untouched and not counted here — they
were not added tonight.)

---

## 5. The CLOSED row — which, and why

**Row: Janet Harrison → Southampton City Council**, response due 18 December 2024, **591 days**
outstanding at 2026-08-01.

**Why this row.** Restricted the choice to the 38 single-recipient rows first — closing a
multi-recipient row (e.g. Luke Chatterton's five) would close five sentences at once from one
simulated event, overstating what a single acknowledged response actually settles. Within the 38,
sorted by days outstanding, Janet Harrison sits at **index 19 of 38 (0-indexed)** — almost exactly
the median (591 days; the 38-row range runs 166 to 869 days). Deliberately not the oldest
(Matthew Wickes, 869 days — closing the single worst-looking row first reads as "the register fixes
its most damning case," a claim this study has no standing to make) and not the newest
(Winifred Wardle, 166 days — closing only the freshest, least-aged duty trivialises what closure
would mean). The median single-recipient row was chosen precisely because it is not the case that
makes the best story either way.

**Closure day.** The CLOSED variant is rendered at extent 400 (per OUTPUT). Closure is drawn at
**day 200 of that 400-day simulated run** — the midpoint, chosen for the same reason as the row: not
at the very start (which would barely distinguish CLOSED from OPEN) and not at the very end (which
would barely show the "marks stop" effect). Day 1 of the simulated run = 2026-08-01; day 200 =
**16 February 2027**. The sentence for this row alone switches to past tense and is dated: *"Southampton
City Council responded to this report on the prevention of future deaths, on the sixteenth of
February, two thousand and twenty-seven."* Verified in the rendered DOM: this row's mark count is
exactly 200 (`min(closureDay=200, extent=400)`), every other row in the same document carries the
full 400. The rule bar (591px, the historical accusation) is untouched — identical segment widths to
the same row's OPEN rendering.

**Legal hygiene.** The CLOSED variant's colophon carries, and only there, out of the entrance:
*"The closure shown here is simulated for study; no response has been received in this row as at the
first of August, two thousand and twenty-six."* Checked: this string appears in the CLOSED variant's
source HTML (scratch, not committed) and nowhere in `e2.html`, which has no closed row at all.

**Naming gap, flagged rather than quietly patched:** the OUTPUT instructions ask for
`IMAGINED-simulated-closure` in the CLOSED stills' filenames; I named them
`still-CLOSED-…-IMAGINED-simulated-extent-400-scaled25.png`, which correctly marks the *extent* as
simulated (400 is indeed simulated) but does not separately carry the string
`IMAGINED-simulated-closure`. The colophon-text legal-hygiene line itself is present and correct;
the filename only flags the extent, not the closure, as imagined. See §8.

---

## 6. Register tests — §8, run on the actual rendered geometry, O1 vs O2 side by side

**Method.** Per test, per width, per order, per extent, using `measure-dom` (Chromium's own layout
engine, `Range.getClientRects()` for text lines, `getBoundingClientRect()` grouped by rendered
flex-line for rule segments) against the live-rendered page at the same viewport width as the
corresponding still — this is the identical geometry the still is a raster of, read from the layout
tree instead of re-derived from pixels. One real bug was caught and fixed while building this:
`.rule-line` uses `align-items:flex-end`, so a flex line mixing a 2px `.seg` and an up-to-9px
`.mark`/`.markb` shares a **bottom** edge but not a **top** one — the first version of the
line-grouping code grouped by rounded `top`, which overcounts lines whenever heights differ on a
shared row. Fixed to group by `bottom` before any number below was taken. T3a (total rule ink vs
row index) is computed analytically from the data (`ink = days`, by construction, order-dependent
only, extent-invariant) and cross-checked: not re-derived from pixels because the ruling itself
already established that "days outstanding" *is* the rule length in px.

**Pre-commitment, restated: ANY ONE of the five trips the ruling, at that width.**

### 1280 px

| test | threshold | O1 / extent 1 | O1 / extent 400 | O2 / extent 1 | O2 / extent 400 |
|---|---|---|---|---|---|
| T1 left-edge histogram | ≥80% on ≤3 x-values | 100% @ x=344 → TRIPS | 100% @ x=344 → TRIPS | 100% @ x=344 → TRIPS | 100% @ x=344 → TRIPS |
| T2 row-pitch CV (38 single-recipient blocks) | <10% → trips | 75.4% → no | 72.3% → no | 67.9% → no | 65.2% → no |
| T3 staircase, total-ink Spearman | \|r\|≥0.90 → trips | −0.9998 → TRIPS | −0.9998 → TRIPS | −0.9987 → TRIPS | −0.9987 → TRIPS |
| T3 staircase, longest-rendered-segment Spearman | (same test, by eye) | −0.9312 | −0.9312 | −0.9306 | −0.9306 |
| T4 shared right terminus | present → trips (see note) | x=936, 33.8% of 74 rights, 45 distinct | same | same | same |
| T5 line-count uniformity | ≥70% identical → trips | 38.8% @ 5 lines → no | 49.0% @ 9 lines → no | 38.8% @ 5 lines → no | 49.0% @ 9 lines → no |
| **verdict at 1280px** | | **TRIPS (T1, T3)** | **TRIPS (T1, T3)** | **TRIPS (T1, T3)** | **TRIPS (T1, T3)** |

### 390 px

| test | threshold | O1 / extent 1 | O1 / extent 400 | O2 / extent 1 | O2 / extent 400 |
|---|---|---|---|---|---|
| T1 left-edge histogram | ≥80% on ≤3 x-values | 100% @ x=24 → TRIPS | 100% @ x=24 → TRIPS | 100% @ x=24 → TRIPS | 100% @ x=24 → TRIPS |
| T2 row-pitch CV | <10% → trips | 80.9% → no | 76.3% → no | 72.3% → no | 68.3% → no |
| T3 staircase, total-ink Spearman | \|r\|≥0.90 → trips | −0.9998 → TRIPS | −0.9998 → TRIPS | −0.9987 → TRIPS | −0.9987 → TRIPS |
| T3 staircase, longest-rendered-segment Spearman | (by eye) | −0.6870 | −0.6870 | −0.6864 | −0.6864 |
| T4 shared right terminus | present → trips (see note) | x=360, **53.3%** of 105 rights, 43 distinct | same | same | same |
| T5 line-count uniformity | ≥70% identical → trips | 34.7% @ 7 lines → no | 36.7% @ 13 lines → no | 34.7% @ 7 lines → no | 36.7% @ 13 lines → no |
| **verdict at 390px** | | **TRIPS (T1, T3, and T4 by majority-share reading)** | same | same | same |

**T4 note, stated plainly rather than smoothed.** The ruling gives T4 no numeric threshold — "if the
rules are drawn to a shared right terminus… that terminus is an axis," present/absent, not a
percentage. Every rule that wraps necessarily ends at least one of its lines exactly at the content
edge (that is what wrapping means), so *some* degree of shared right-terminus is structurally
guaranteed by the wrap mechanic itself, at any width, for any order. I report the raw numbers rather
than assert a threshold I would be inventing: at 1280px the dominant edge (x=936, the content
boundary) accounts for a third of all seg-line right edges — a real but minority share, alongside 44
other distinct values (mostly non-wrapping rules' own varying endpoints). At 390px the same
content-edge x accounts for a majority (53.3%) because far more rules wrap at the narrow measure
(38 of 49, vs 25 of 49 — see §7c), mechanically producing more full lines that all terminate at the
same edge. I have marked 390px as tripping T4 under a "majority of all right edges" reading, and
flagged that this reading is mine, not the ruling's — the predecessor's own conductor took the same
posture last night ("partial — reported, not adjudicated") and I am not resolving that ambiguity
here either, only reporting the measurement it is ambiguous about.

**The question the studio needs answered: does adopting the state's own printed order (O2) change
the verdict against O1?** **No.** At both widths and both extents tested, O1 and O2 trip the
identical tests (T1 and T3, plus the T4 note at 390px) by nearly identical margins (T3 Spearman
−0.9998 vs −0.9987 — the ruling's own §8 prediction, "the source's own order is barely better," is
confirmed to four figures rather than merely re-asserted). **Both orderings are registers, on the
pre-committed pixel tests, at both widths, at both extents measured.** Switching to O2 does not
repair the form; it was never going to, because T1 and T3 are properties of a single-column,
left-flush, length-encoded rule bar — of the *encoding*, not the *ordering*. Reordering the rows
cannot move where the rule bars start (T1) or stop encoding a length that correlates with row
position under **any** near-monotone order (T3, since the underlying due dates are themselves
strongly time-ordered whichever printed order is kept close to it).

---

## 7. Other measurements

### (b) Ground-domain test, 390px, largest extent (1825, `O2/M-A/P1`)

Run on the full-resolution still before downscaling (`390 × 27,970`):

| | value |
|---|---|
| longest run of consecutive all-white rows | **180 rows** |
| location | rows 27,790–27,969 of 27,970 — **the last 180 rows of the image: the bottom page margin**, not inside the body |
| as a fraction of an 844px phone screen | **180 / 844 = 0.2133** |
| distinct luminance values inside that run | **1** (pure white, RGB 255,255,255 throughout) |
| rows containing ink | 18,227 / 27,970 = 65.2% |

Cross-checked on the M-B/extent-1825 still (180 rows, same location, 1 luminance value) and the
CLOSED/extent-400 still (180 rows, same location, 1 luminance value) — the bottom-margin blank run
is a structural constant of the page's own padding (`main { padding: 72px 24px 160px }`), not an
artefact of any one variant. **No hole; a void, and it sits in the margin, not the register**,
consistent with the prior night's finding on `e1.html` and with the standing house test this
concept was previously killed for failing (9,588 rows / 11.36 screens on the prior material — this
page's longest blank run is a fortieth of that, and outside the body entirely).

### (c) Wrapping — how many of the 49 rules wrap, by width, by extent

Rule-segment wrapping is determined purely by the cumulative width of `.seg` elements (the rule
bar) against the content measure; `.mark`/`.markb` elements are appended after all segments in DOM
order, so they cannot change where a segment wraps. Measured directly (`wrapcount`), confirmed
identical at extent 1, 400 and 1825:

| width | content measure | rules that wrap (of 49) |
|---|---|---|
| 1280px | 592px | **25** |
| 390px | 342px | **38** |

(Matches `e1.html`'s own count exactly — expected, since wrap depends only on days-outstanding and
content width, both unchanged by C1–C6.)

### (d) Condition 12 — no dates leak into the served bytes of the entrance

Checked directly against `e2.html`'s bytes (not against a description of them), at both entrance
viewports (390×844, 1280×800):

- **`<title>`**: `YOU ARE UNDER A DUTY` — **zero digit characters, zero month names.**
- **`<meta>` tags** (2 total): `<meta charset="utf-8">` and `<meta name="viewport" content="width=device-width, initial-scale=1">`.
  **Digit characters found: one `8` (in `utf-8`), one `1` (in `initial-scale=1`).** Reported
  verbatim per the instruction to check bytes, not intent — **neither is a date or a day-count**;
  both are standard HTML boilerplate present on essentially every modern web page, not content this
  house authored. No month names in either.
- **HTML comments**: none exist in the file (checked with a literal `<!--` search: zero matches).
- **First-viewport text** (390×844): `YOU ARE UNDER A DUTY / Observed the first of August, two
  thousand and twenty-six. / There is no power authorising a coroner to take any steps. / Matthew
  Wickes / University of Southampton is under a duty to respond to this report on the prevention of
  future deaths, namely by the fifteenth of March, two thousand and twenty-four. / James Atkinson /
  Newcastle City Council is under a duty to respond to this report on the prevention of future
  deaths, namely by the twenty-second of March, two thousand and twenty-four.` — **zero digit
  characters.** Month names present (August, March, March) — expected and endorsed by the ruling
  itself ("dates spelled out in words… I endorse it"); the test is for digits, not for the concept
  of a date. Same result at 1280×800 (one further entry visible, Mark Pryor / Ministry of Justice /
  "April" — again zero digits).

**Verdict: no date and no day-count appear as a digit anywhere in the checked bytes.** The only
digit characters in the checked surfaces are inside standard `<meta>` boilerplate unrelated to any
date.

### (e) The M-B judgement, extent 1825

Measured on the un-downscaled `full-B-390-e1825.png` / `full-B-1280-e1825.png`, on the first entry
(Matthew Wickes, 1825 marks), via DOM geometry for the structural numbers and pixel readback for
the luminance numbers:

| measure | 390px | 1280px |
|---|---|---|
| mark width : gap | 1px : 1px (**1:1**, by construction) | 1px : 1px (**1:1**) |
| marks per full rendered line | **171** (content 342px ÷ 2px pitch) | **296** (content 592px ÷ 2px pitch) |
| mark-band ink fraction (pixel-measured) | **25.3%** (11,066 / 43,680 px) | **13.7%** (11,738 / 85,760 px) |
| distinct luminance values in the mark band | **2** (0 and 255 — sharp black/white, no antialiasing grey, no gradient) | **2** (0 and 255) |
| M-A comparison, marks per full line (same widths) | 68 (342 ÷ 5px pitch) | 118 (592 ÷ 5px pitch) |

**By eye:** a side-by-side crop of the identical entry (Matthew Wickes, 1280px, extent 1825) shows
M-A as an unbroken comb of even 9px verticals — a countable-in-principle, sparkline-like barcode,
exactly the risk the prior night's report named against itself — and M-B as an uneven grey-black
grain with no periodic edge for the eye to lock onto. **Verdict: at extent 1825, M-B reads as
texture, not tally**, on both the measurable basis (denser pitch, irregular height, no dominant
periodicity after the hash fix, 2-valued but non-uniform ink coverage well short of either a solid
fill or a sparse countable row) and by eye.

---

## 8. What I would flag against myself

1. **The CLOSED stills' filenames only carry `IMAGINED-simulated-extent-400`, not a separate
   `IMAGINED-simulated-closure` marker**, as noted in §5. The simulated-closure legal-hygiene
   sentence is correctly present in that variant's colophon and nowhere else, and "closed" is not a
   quantity that varies the way extent does, so there was no natural second number to hang a second
   filename tag on — but the brief asked for the string and I did not put it in the filename. I am
   naming this now rather than letting it be found.

2. **T4 has no numeric threshold in the ruling, and I supplied my own (majority share) to produce a
   trips/no-trips line in the summary table.** That threshold is mine, not the Dramaturg's. I have
   tried to be honest about this inline (§6), but the summary table still prints "TRIPS" at 390px
   under a rule I invented; a stricter reading would leave T4 as "reported, not adjudicated" at
   both widths, exactly as the predecessor's conductor left it. Either reading leaves the overall
   390px verdict unchanged (T1 and T3 already trip it independently), but the T4 line specifically
   should not be read as a Dramaturg-sanctioned number.

3. **Two real bugs were caught only by rendering and looking, not by reasoning about the code first**
   — the mod-8 periodicity in the first M-B hash (§3) and the top-vs-bottom flex-line grouping bug
   in the register-test measurement (§6). Both are fixed and the numbers above reflect the fixed
   code, but their existence means I do not have full confidence that every corner of a
   ~730-line generator handling wrapping flexbox geometry across five orders of magnitude of extent
   is bug-free — only that the specific numbers reported here were checked against a rendered
   artefact, not merely computed and trusted.

4. **T1 and T3 trip for what may be a structural reason inherent to *any* single-column, length-
   encoded, left-flush rule form** — not specific to a fixable choice this étude made. Both C5
   orderings trip both tests by nearly the same margin (§6), and the ruling's own arithmetic
   predicted this before any pixel was rendered. If the studio's actual question is "can this form
   ever pass T1/T3 at 1280px," the honest answer this étude's numbers point to is **not by
   reordering alone** — T1 is tripped by having one left margin at all (true of prose too, which is
   presumably not meant to be disqualified), and T3 is tripped by the fact that "days outstanding"
   is both the sort key's near-neighbour and the rule's rendered length, which no reordering that
   stays close to the source's own near-monotone due-date order can avoid. Breaking T3 without
   breaking C5's requirement that O2 be "the state's own printed order, unmodified" would need a
   change to the *encoding* (what the rule bar's length represents), which is out of this étude's
   remit and is named here, not solved.

5. **The register tests were run at extent 1 and extent 400 "at minimum," as instructed — not at
   1825.** I do not know whether the verdict changes at 1825 (T2 and T5 are extent-sensitive; T1,
   T3, T4 are not, by construction, so I expect no change, but this is inference from the mechanism,
   not a fourth measurement taken).

---

## 9. Files added to the repository

```
etudes/you-are-under-a-duty/build-57.mjs
etudes/you-are-under-a-duty/e2.html
etudes/you-are-under-a-duty/entrance-390-P1.png
etudes/you-are-under-a-duty/entrance-1280-P1.png
etudes/you-are-under-a-duty/entrance-390-P2.png
etudes/you-are-under-a-duty/still-O2-MA-P1-390-extent1.png
etudes/you-are-under-a-duty/still-O2-MA-P1-1280-extent1.png
etudes/you-are-under-a-duty/still-O2-MA-P1-390-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/still-O2-MA-P1-1280-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/still-O2-MA-P1-390-IMAGINED-simulated-extent-1825-scaled25.png
etudes/you-are-under-a-duty/still-O2-MA-P1-1280-IMAGINED-simulated-extent-1825-scaled25.png
etudes/you-are-under-a-duty/still-O2-MB-P1-390-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/still-O2-MB-P1-1280-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/still-O2-MB-P1-390-IMAGINED-simulated-extent-1825-scaled25.png
etudes/you-are-under-a-duty/still-O2-MB-P1-1280-IMAGINED-simulated-extent-1825-scaled25.png
etudes/you-are-under-a-duty/still-CLOSED-390-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/still-CLOSED-1280-IMAGINED-simulated-extent-400-scaled25.png
etudes/you-are-under-a-duty/REPORT-57.md
```

`e1.html`, its five stills and `REPORT.md` from the prior session are unmodified. All other HTML
variants (O1 comparisons, the M-B/CLOSED/P2 scratch HTML, the full-resolution pre-downscale PNGs,
the register-test analysis script) were built and measured in the session scratch directory and
deleted before finishing — none are part of this étude's committed object.

No commit was made to git.
