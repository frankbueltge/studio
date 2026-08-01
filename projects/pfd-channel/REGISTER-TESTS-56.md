# THE PRE-COMMITTED REGISTER TESTS, PUT TO THE BUILT OBJECT

**Conductor, session 56, 2026-08-01.** The Dramaturg published five register tests with numeric
thresholds in `STAGING-RULING-56.md` §8, **before the étude existed**, writing: *"I am not
pre-judging the étude; I am pre-committing so that I cannot un-judge it,"* and making the conditions
*"testable by someone who was not in this session."* The étude was built in parallel the same night.
This file is the conductor running those tests on the built stills, with its own PNG decoder, after
both were finished and neither could be tuned to the other.

**The Dramaturg's rule: ANY ONE of the five trips the ruling at that width.**

---

## THE RESULT — 1280 px, extent 1 (`etudes/you-are-under-a-duty/e1-1280.png`)

| # | test | threshold | measured | verdict |
|---|---|---|---|---|
| **T1** | text lines sharing few left-edge x values | register if **≥ 80 %** on ≤ 3 x values | **237 of 237 text lines = 100 %**, on x ∈ {344, 345, 346} — one edge plus antialiasing | **TRIPS** |
| **T2** | row-pitch coefficient of variation | register if **< 10 %** | not computed — see limits below | **NOT RUN** |
| **T3a** | Spearman(row index, **total** rule ink) | register if **\|r\| ≥ 0.90** | **−0.9639** | **TRIPS** |
| **T3b** | Spearman(row index, **longest rendered segment**) | (same test, as the eye sees it) | **−0.6819** | does not trip |
| **T4** | a shared right terminus on the rules | register if one terminus dominates | 43 distinct right-x over 72 segments; **25 segments share x = 936** (the measure's own right edge). **All 72 segments share ONE left origin, x = 344** | **partial — reported, not adjudicated** |
| **T5** | ≥ 70 % of blocks with identical line count | register if ≥ 70 % | not computed — see limits below | **NOT RUN** |

**Two of the five trip. Under the Dramaturg's own rule, one is enough: the 1280 px still is a
register at that width.** The staging ruling had already returned NOT STAGEABLE AS PROPOSED without
the étude; this converts its §8 prediction — *"likely to trip at least three of the five"* — from a
forecast into a measurement. It trips two on what was run, with a third partial and two not run.

### What T3a and T3b together actually say, because the difference is the finding

The **total** ink of each rule is the duty's age, and against row index it is almost perfectly
monotone: **−0.9639**. That is the sorted-bar-chart signature the Dramaturg derived from the data
alone, and the pixels confirm it.

But **24 of 48 reconstructed rules exceed the 592 px measure and wrap**, so the *longest visible
segment* of half the page is the same 592 px line. Against the eye, the staircase weakens to
**−0.6819**. **The wrapping is what stands between this page and a bar chart** — which is exactly the
Dramaturg's own charge, arrived at independently: *"the phone saves it by wrapping — which means the
wrap, an accident of measure, is doing the artistic work."* The pixels agree with it at the desktop
width too.

---

## 390 px — WHY NO STAIRCASE NUMBER IS REPORTED HERE

At 390 px the conductor's scanline reconstruction found **81 rule segments and could not pair the
wrapped ones** (the phone measure renders at ≈ 336 px, and the pairing threshold missed it). The
Spearman it produces on 81 unpaired segments is **not a measurement of anything** and is therefore
not reported as one. What the phone still does support, measured:

- **all 81 segments share ONE left origin, x = 24;**
- **38 segments share the right terminus x = 360** — the measure's edge again;
- and from the Builder's own DOM measurement, **38 of 49 rules wrap at 390 px** against 25 of 49 at
  the wider measures.

**Stated plainly rather than smoothed:** the register question at the width where most people would
meet this work **has not been answered tonight**, and the ruling's §8 pre-commitment therefore stands
open at 390 px. It is cheap to close and it is owed.

---

## THE GROUND-DOMAIN TEST — the one that killed the previous concept — PASSES

This house's standing runnable test (`memory/decisions.md`): render the longest blank run at the
narrowest target width and count distinct luminance values; if the answer is 1, there is no hole,
there is a void. Run by the Builder and **re-run independently by the conductor with its own
decoder**, both agreeing exactly:

| | `e1-390.png` (extent 1) | `e1-IMAGINED-simulated-extent-400-390.png` |
|---|---|---|
| longest run of all-white rows | **180 rows** | **180 rows** |
| as phone screens (844 px) | **0.213** | **0.213** |
| distinct luminance values in that run | **1** | **1** |
| **where the run is** | **y = 14,227 → 14,406 of 14,407** | **y = 16,819 → 16,998 of 16,999** |
| rows containing ink | 5,345 / 14,407 = **37.1 %** | 7,933 / 16,999 = **46.7 %** |

**The longest blank run is the bottom page margin, and it is the last 180 rows of the image in both
cases. Inside the body there is no blank run at all.** The comparison that matters: the concept
killed on 2026-07-31 measured **9,588 consecutive rows containing no non-white pixel — 11.36 phone
screens — and a midpoint with one distinct value in 329,160 pixels.** This one measures 180 rows of
trailing margin. **The defect that killed the last concept does not exist in this form**, and that is
a result independent of whether this concept survives.

---

## LIMITS OF THIS PASS, NAMED

1. **T2 (row pitch) and T5 (line counts per block) were not run.** They need block segmentation the
   conductor did not write tonight. Recorded as NOT RUN, not as passed — the house's own rule is that
   a condition recorded as untested is recorded, never skipped.
2. **The rule reconstruction paired 48 of 49 rules at 1280 px**, so T3a/T3b are computed on 48. One
   pairing failed, most likely where two wrapped rules abut. The correlation is not sensitive to one
   row, but the count is stated rather than rounded up.
3. **Nothing here is a verdict.** The Dramaturg owns the staging ruling and the Kritiker owns the
   kill. This file supplies the pixels its pre-commitment asked someone else to supply.
