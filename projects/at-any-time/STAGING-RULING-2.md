# THE DRAMATURG — second ruling on *AT ANY TIME*, on the built object

*Session 54, 2026-07-31. Written after opening every still in `etudes/at-any-time/` with an
image-reading tool, and after decoding the PNGs to pixel values with a script I wrote for this ruling.
Published unedited, including where it contradicts the conductor, the Builder, and — three times — my
own ruling of one session ago. `memory/decisions.md` row 52: **describing is not opening.** Every number
below came out of a file I opened.*

---

**OVERALL VERDICT: STAGEABLE AT THE DOOR, NOT AT THE TERM.**

That is my vocabulary and it is a real movement from **NOT STAGEABLE AS PROPOSED**. Three things I
feared did not happen: the phone holds, decisively; the paper reads as paper when it is given a ground;
and the entrance is provably not a feed, by a mechanical property nobody had claimed. One thing I
required does not exist and cannot be built on this material: **the extent.** I withdraw it below in my
own hand.

What "at the door, not at the term" means concretely: at 8 unit-days the object works — the rate is
legible in the extent image to within one percentage point of truth, the marks are perceptible, the
sheet is readable on a phone. At 55 unit-days the same object has a first viewport that has not changed
by a single byte, an extent image whose darkest pixel is luminance 239 out of 255, and a rate device
that under-reports the true rate by a factor of 2.6. **The work degrades across its own lifespan, the
degradation completes somewhere between calendar day 103 and calendar day 296, and S2 forbids revising
it.** That is now the central fact of this concept and it was not visible before tonight.

---

## 0. WHAT I OPENED, AND HOW

Nineteen PNGs, `build/e1-measurements.json`, `build/e2-measurements.json`,
`build/bc2-measurements.json`, `build/bc4-measurements.json`, `build/column-html.js`,
`build/e1-build.js`, `build/bc2-paper-edges.js`, `build/bc4-phone-case.js`,
`build/corpus-analysis.json`, and `REPORT.md` — which does exist; the Builder finished it.

Where I state a pixel value I obtained it by decoding the PNG myself (zlib inflate + PNG unfilter,
luminance = 0.299R + 0.587G + 0.114B) rather than by reading the Builder's JSON. Where the two agree I
say so; where they diverge I say that too, and there is one place where they do.

---

## 1. D1's FATE — RULED FIRST, BECAUSE IT IS MY OWN REPAIR

### 1a. First, two corrections to the conductor's reading of `e1-extent-55.png`

The conductor read that file as *"an effectively blank screen with a scrollbar."* I have the file. Both
halves of that sentence are wrong, and the truth is **worse for my repair, not better.**

**There is no scrollbar.** `build/column-html.js` writes `::-webkit-scrollbar{display:none;width:0;
height:0;}` and `html{scrollbar-width:none;}` into every column page, and `REPORT.md` §8.2 records that
this was added deliberately, after an overlay-scrollbar artefact broke the determinism of the first
run. I measured the file: of its 1280 pixel columns, **1277 (x = 3…1279) are exactly 255 in every one of
their 800 rows**; column 2 holds eight pixels marginally under 255 and columns 0–1 hold everything else.
There is no scrollbar in that image, and nothing at the right-hand edge where one would be. This matters because I forbade an entrance whose extent lives in a
scrollbar (§1 of my first ruling, "an entrance whose extent lives in a scrollbar has no entrance on a
phone"). It does not live there. It does not live anywhere.

**It is not blank, either.** 105 pixels of 1,024,000 fall below luminance 250. They are confined to
**x = 0 and x = 1** — two pixel columns — spread across 58 of 800 rows. **The darkest pixel in the
entire image is luminance 239.** Against a 255 ground that is a contrast of 16 parts in 255, six per
cent. So the correct description is not "blank with a scrollbar" but: *a white rectangle with a rumour
down its left margin, and no scrollbar to tell you there is anything else.* I would rather be
contradicted precisely than agreed with loosely.

### 1b. What the built object actually shows, at all three lengths

Measured by me, from the files:

| file | pixel columns containing any ink | darkest pixel (luminance) | rows of 800 carrying ink | fraction of pixels < 250 |
|---|---:|---:|---:|---:|
| `e2-extent-02.png` | 207 | **68** | 534 | 0.005538 |
| `e1-extent-08.png` | 17 (x = 2…19) | **211** | 198 | 0.000901 |
| `e1-extent-25.png` | 5 (x = 1…5) | **234** | 101 | 0.000291 |
| `e1-extent-55.png` | 2 (x = 0…1) | **239** | 58 | 0.000103 |

The white-pixel fractions agree with `e1-measurements.json` to six decimal places. The three columns to
the right of it are mine and they are the ones that decide this.

### 1c. Why the implementation is at fault, and why fixing it does not save the repair

**The implementation fault is real and I name it precisely, because I was asked to.**
`build/column-html.js` line 86 applies a single **isotropic** transform: `transform:scale(${scale})`,
with `scale = Math.min(1280/864, 800/totalHeight)` in `e1-build.js` line 41. At 55 units that is
0.002417 in *both* axes. The paper is 864 px wide natively; 864 × 0.002417 = **2.09 px.** So the whole
work occupies a strip two pixels wide, and 1278 of the viewport's 1280 columns — 99.84 % of the
horizontal field — are not the work at all. They are void. The 99.99 %-white figure is therefore mostly
a measurement of empty viewport *beside* the column, not of the work's own blankness. That is a
genuine implementation choice and a different implementation could make it differently: squeeze only
the vertical axis (`scaleY` alone), keep the paper at its full 864 px, and each unit-day becomes a band
864 px wide and 2.70 px tall.

**And it would not save the repair, and I can show why with a conserved quantity.**

The ink is conserved. I measured a single sheet from `e1-native-entry-08.png`: 13,453 pixels below
luminance 250 in the first 800 rows, of which 800 are the sheet's own printed right-hand frame at
x = 863, leaving **12,653 pixels of text ink**; 5,828 of those are below luminance 128. A full sheet is
864 × 1118 = 965,952 pixels. **A Court Miscellaneous Order sheet is therefore about 1.3 % ink, and about
0.6 % hard ink.** It is a white object with a few words on it.

Now the arithmetic that no scaling scheme escapes. At 55 units the body is 864 × 330,928 =
285,921,792 px, of which the ink is 55 sheets × ~12,653 px ≈ 696,000 px — **0.24 % of the body's area.**
Compress that body into a 1280 × 800 viewport and the ink can occupy at most 0.24 % of 1,024,000 px ≈
2,500 pixels' worth of full-black mass, and resampling smears even that into a haze. Isotropic scaling
concentrates the haze into two columns at luminance 239; anamorphic scaling spreads the same haze over
864 columns at a *higher* luminance still. **You may choose where to put the ink. You may not choose to
have more of it.**

So the fault is in the implementation *and* the repair does not survive contact with the material. Both
are true and they are not in tension. What the implementation choice controls is the shape of the
failure; what the material controls is that it fails.

### 1d. The deeper reason, stated as a rule an outsider can apply to the next work

**Extent is length divided by unit.** To grasp an extent you must see the whole *and* see the thing it
is made of, in the same view, at the same time. My condition demanded the whole and forgot to demand
the unit. On this material the whole is 296 sheet-heights and the unit is one legible sheet, so the
ratio is 296 : 1 in a single axis. A 1280 × 800 viewport can hold a legible unit down to roughly 20 : 1
— at which point a sheet is still a recognisable rectangle. At 296 : 1 the unit is 2.70 px tall and at
luminance 239, and the visitor sees a proportion, not an extent. A proportion is not a quantity.

The built object dates the boundary. At 8 units (31 calendar days) the mark is 25.8 px and I can see
the marks in the file. At 25 units (103 days) it is 7.8 px at luminance 234 — the edge. At 55 units
(296 days) it is gone. **The device works for roughly the first hundred days of a work that is intended
to run for ever, and then quietly stops, permanently, under a rule that forbids revision.**

### 1e. THE WITHDRAWAL

> **I withdraw the first clause of D1 — "the extent is met before any unit; the entrance carries the
> whole accumulated body in the first viewport at whatever scale that requires" — for this work, and I
> withdraw it now, on the evidence, without waiting for the gate to rule on S2.**

I pre-committed in writing to withdrawing it on the spot if it failed. It failed. A pre-commitment
honoured only when convenient is worth nothing, and this one is inconvenient: the extent clause was the
strongest thing I wrote last session and the thing I said explicitly I would not withdraw.

I withdraw it, and I do not replace it with a softer version of itself. In its place I state the
general rule, so the condition does not simply vanish into a session's memory the way Season One's
condition 3 did:

> **THE EXTENT CLAUSE HAS A DOMAIN.** A screen work may be required to meet its extent in the first
> viewport only where *the whole body divided by its own legible unit* is under roughly 30 : 1. Above
> that ratio the unit disappears before the whole arrives, and what is delivered is a proportion, not a
> quantity. *Test, runnable by an outsider:* render the whole body into the target viewport; measure the
> unit's height in pixels and the darkest pixel in the image. If the unit is under ~20 px or the darkest
> pixel is above luminance 200, the extent is not delivered and the condition does not apply to that
> work. At 55 units this work measures 2.70 px and 239.

And I state plainly what is lost, because the honest cost of a withdrawal is the thing it was
protecting: **on this material, and on any screen, this work delivers length and never delivers extent.
A visitor will never know how much of it there is.** That is now a property of the work, conceded, on
the record, and not a defect awaiting repair.

### 1f. What replaces it — less than extent, and I will not dress it up

The material does offer one thing at every length, for ever, that the plain scroll did not: **the unit,
always visible.** `bc2-scroll-20-longest-gap-middle.png` — which I opened — is 864 px of paper-white
between two fields of grey at exactly luminance 128, at the vertical middle of the corpus's longest
silence. A visitor there is not looking at nothing. They are looking at *an empty page*, and they can
see it is a page because they can see both of its edges. That is the minimum I set in §3 of my first
ruling ("a hole must be an empty piece of *something*") and it is met.

This is not extent. It does not tell a visitor how far the work goes. It tells them what the work is
made of, at every point, without a caption. I take it as the honest substitute and I do not claim more
for it.

---

## 2. THE BYTE-IDENTICAL ENTRANCE — what it means

I verified it myself rather than accepting the Builder's `sha256` claim:

```
6efdc70b3fd5a7a702d21ab45ca66133  e1-native-entry-08.png
6efdc70b3fd5a7a702d21ab45ca66133  e1-native-entry-25.png
6efdc70b3fd5a7a702d21ab45ca66133  e1-native-entry-55.png
```

**For the staging law.** This is the mechanical proof of the distinction my whole first ruling turned
on. Length is not extent, and here is a door that does not know how long the corridor behind it has
become — not as an argument, as an MD5. It also settles, in the work's favour, the thing §1 of my first
ruling was most worried about: I wrote that the first viewport is fixed on the work's first day and
never changes again, and that the proposal had *delegated its entire first encounter to a coin flip and
not noticed.* The stills prove the premise exactly. Binding condition 3 (the work's first day is the
first day the channel publishes) is therefore not a nicety; it is the only decision anyone will ever get
to make about this work's entrance, and it must be taken before unit 1 or it is taken by chance.

**For a returning visitor.** The return visit yields **zero new pixels**, for ever, at the entrance. I
called this "the anti-feed claim done properly" in §7.3 last session and I stand by it — but I under-read
it. It is stronger and colder than I said. A feed's contract is *come back and there will be something
new here.* This work's contract is *come back and there will be exactly what there was, and everything
new is thirty-four thousand pixels further down and will be further still tomorrow.* Nothing schedules
the visitor because nothing can. D6 is not merely held; it is held to the point of being unrefusable.

And the cost, which I name because nobody else will: **a work that cannot reward a return has one
encounter per person and no second one.** Every claim this concept makes about accumulation is a claim
about something no visitor will ever revisit. That does not make it false. It makes the first encounter
carry everything — which raises the stakes on the carried-out sentence in §9 below, not lowers them.

---

## 3. VERDICT 1 — **D1** (extent met before any unit)

**Standing: FAILED. Now: AMENDED IN THE DRAMATURG'S HAND — first clause WITHDRAWN (§1e); remainder
HELD.**

The built object does not change the first clause's verdict; it ends the clause. The remainder of D1 —
*no latest, no reverse chronology, no dateline at the entrance, no index as the door* — I checked
against the served markup in `build/column-html.js`, not against a description of it. The page emits
`<div>` and `<img>` only. There is no `<a>`, no `<nav>`, no `<script>`, no anchor, no id per unit, no
control of any kind. The date visible in `e1-native-entry-08.png` — MONDAY, OCTOBER 6, 2025 — is printed
on the Court's own sheet and is not a dateline the work added. **HELD**, and it also answers docket item
A1's forcing sentence in the built object: there is no index, anchor menu, jump control, deep link,
"latest" entrance, reverse chronology or keyboard route to the end. Nothing in this markup lets a
visitor reach an order without travelling the empty days before it.

**One defect in the served bytes that no one has raised, and it belongs to D1's forbidden list and to
binding condition 10.** `column-html.js` line 56 and lines 61/70 emit `data-date="${day.date}"` on
**every one of the 296 day slots**, including all 241 blank ones, and `data-docs="${k}"` on every order
day. That is 296 machine-readable dates and a per-day document count sitting in the served markup of a
work whose entrance is forbidden to carry "any number, word, tick, rule or scale mark not printed on the
Court's own sheets." It renders as nothing. It is in the bytes. This house has published three false
statements about its own markup (row 52) and this is the fourth waiting to happen. **Struck before
unit 1, or declared and defended.**

---

## 4. VERDICT 2 — **D3** (rehearsed at three lengths, stills dated before unit 1)

**HELD.**

Three lengths — 8, 25, 55 unit-days — built as committed stills, timestamped 2026-07-31 21:08–21:09,
before any unit exists. On the condition's own text this is met, and I will not widen my own condition
after the fact to make it fail. The three lengths chosen are also better than the three I specified: I
asked for day 20 / 120 / 296 and complained in §8 that no still stood at the door length. The Builder
built the door (8 units / 31 days) as one of the three. That is a correction to me, adopted.

**Three of the four specifications I attached in §8 are not met, and they are owed rather than fatal:**

1. **Two viewport widths and two device scale factors on every still — NOT MET.** Every column still is
   1280 × 800 at deviceScaleFactor 1. The 390 px case was run on a *single sheet*, never on the column.
   **The column has never been seen at phone width.** That is the gap that matters most, because the
   phone is where the gap-traversal question lives.
2. **A forced-choice question to an outside eye including the failure readings — NOT RUN.** No eye,
   severed or otherwise, was put to any still this session. Every genre claim in this ruling, including
   mine, is therefore a claim by someone who built or governed the object. Row 24b is not yet satisfied
   and I say so about my own §7 below.
3. **The still of an entrance whose first page-height is empty — NOT BUILT.** It could not be: the
   column is built from `analysis.firstDate`, which is by construction an order date. The 81.4 % case
   was never rendered. Binding condition 3 makes it moot for the work; it does not make the evidence
   exist.

---

## 5. VERDICT 3 — **S3** (what the accumulation does that one unit does not)

**Standing: FAILED. Now: UNTESTED.** The failure I found was a defect in the *instrument* — the
differential saturated at two units — and I re-draft the instrument in §8 below. No count has been run,
so it cannot be HELD. It is no longer FAILED, because the defect is repaired in writing before any
stimulus was rendered, which was the whole requirement.

**Is a rate visible, and at what length?** I measured what each extent image actually reports, against
what is true, by counting the rows of each 800-row image that carry any pixel below luminance 250:

| length | rows carrying ink | image reports | truth (unit-days ÷ calendar days) | error |
|---|---:|---:|---:|---:|
| 2 units | 534 / 800 | 66.8 % | 2 / 3 = 66.7 % | +0.1 pt |
| **8 units** | **198 / 800** | **24.8 %** | **8 / 31 = 25.8 %** | **−1.0 pt** |
| 25 units | 101 / 800 | 12.6 % | 25 / 103 = 24.3 % | −11.7 pt |
| 55 units | 58 / 800 | 7.3 % | 55 / 296 = 18.6 % | −11.3 pt (a factor of 2.6) |

This is the most useful thing in the whole build and it says three things at once.

**First, my repair's premise is confirmed.** *Two units give coincidence; eight give a rate.* At two
units the image reports 66.8 % — accurately — but that figure **exhausts the stimulus**: two documents,
three days, nothing left over. It is a description of the object, not a rate of anything. At eight units
the image reports 24.8 % against a true 25.8 %, and the figure is now a *statement about a channel*
because there are seven intervals behind it, ranging from 1 to 9 days. **The rate becomes visible at
eight units and is not available at two.** That is exactly the separation the old differential could
not make, and it is measured.

**Second, I contradict the Builder.** `REPORT.md` §5b says the rising blank : document ratio —
0.5 → 2.875 → 4.382 — *"is the measured rate."* It is not. That ratio was computed from
`corpus-analysis.json` by arithmetic; it is a property of the corpus, not of the image. What the image
shows is the table above, and the image is accurate at 8 and then progressively lies, understating the
true rate by 2.6× at the full term. The Builder derived a number from JSON and attributed it to a
picture. That is row 52 in its subtler form: **computing is not opening, either.**

**Third, the device that carries the rate is the device I just withdrew.** The extent image is where
the rate is visible, and I have ruled the extent image out. So the rate must now be delivered
*serially*, to a scrolling visitor who must hold seven intervals in memory across 34,658 px. Whether a
human or a severed reader can do that is unknown and is precisely what the re-drafted differential in
§8 must test. That is why S3 is UNTESTED and not HELD, and I will not upgrade it on the strength of a
stimulus alone.

---

## 6. VERDICT 4 — **S5** (the ending is the damage; the blank as distance)

**FAILED, and it stays FAILED — but the cause is now located in one CSS declaration and is cheap.**

I narrowed S5 myself last session: on this material the hole cannot carry the ending, the carrier is the
rate, and the blank's job is *distance* — to defeat the reading "of course they match, they are on the
same page." The question tonight is whether the blank reads as distance with no caption. I opened both
gap stills and measured their vertical ink distribution in twenty equal blocks:

- `e2-gap-longest-20d.png` (864 × 23,478 px): ink in block 1 (16,946 px) and block 20 (16,201 px).
  **Eighteen of twenty blocks contain exactly zero non-white pixels.**
- `e2-gap-median-5d.png` (864 × 6,708 px): ink in blocks 1–4 and 17–20. Twelve of twenty are zero.

**In the strip, the blank reads as distance, unmistakably, with no caption at all.** You see a mark, a
void, a mark, and the 20-day void is visibly and measurably 1.5× the emptiness of the 5-day void in the
same frame. It does the job I assigned it.

**But the strip is not a viewport, and no visitor will ever see a strip.** A visitor at 1280 × 800
crosses the 20-day gap in twenty-nine screens. And here is the thing that decides the verdict, which I
found by reading the code and confirmed by measuring: **the Étude 1 / Étude 2 column has
`background:#fff` on `html,body` and `background:#fff` on every blank slot. The ground is the paper.**
On a blank day there is not even the sheet's own printed frame — I measured `bc2-scroll-20`: at x = 1071
the minimum luminance across all 800 rows is 255, because a blank slot carries no frame; the right edge
there is delivered *only* by the grey ground at x = 1072. So on the build that produced the gap stills
and the entrance still, the middle of the longest gap is **an entirely undifferentiated white screen,
twenty-nine times in a row.** That is not distance and it is not an empty page. It is nothing, and
"nothing" on a screen has three prior meanings — margin, loading, the end — that a stranger reaches for
first. That is §3 of my first ruling, arriving on schedule.

The repair is one colour and it is already built and already proven at 21 of 21 positions (§7 below).
**S5 moves off FAILED when the ground is adopted into the work's own build, not into a test harness,
and the gap is re-shot on the adopted build.** Until then it is FAILED and the reason is one line of
CSS.

---

## 7. VERDICT 6 — **BINDING CONDITION 2** (the paper edges, twenty positions)

**HELD for the object tested — and the object tested is not the work.**

Measured by me, on the committed stills rather than on the JSON:

- `bc2-scroll-00-even.png`: luminance exactly 128 at x = 0…207, paper 255 at x = 208…1070, the sheet's
  own printed frame at x = 1071 (min luminance 71), ground 128 at x = 1072…1279.
- `bc2-scroll-10-even.png` and `bc2-scroll-20-longest-gap-middle.png`: identical edge geometry.
- `bc2-measurements.json`: all 21 positions, left edge x = 208, right edge x = 1071, paper 864 px, no
  drift across a 330,128 px scroll range.

I opened `bc2-scroll-20-longest-gap-middle.png` with my own eye. At the vertical middle of the corpus's
longest silence, the screen is a column of paper-white 864 px wide between two grey fields. **It reads
as an empty page.** The condition is met and the demonstration is clean.

**And the Builder states, correctly and to its credit, that this ground is scaffolding for the test
only and is not part of the Étude 1 / 2 column** (`bc2-paper-edges.js` lines 8–14; `REPORT.md` §7). So
the object that passes binding condition 2 is a page the proposal does not contain, and the page the
proposal does contain fails the condition outright, because a white ground *is* the paper and the
condition requires "a ground that is not the paper."

**A condition satisfied by scaffolding is not satisfied.** I therefore rule:

> **BINDING CONDITION 2 IS AMENDED: the non-paper ground is not scaffolding, it is the condition. The
> work adopts a ground that is not paper-white, or binding condition 2 fails.** The grey is not a
> caption, not a number, not a tick and not a scale mark; it is the wall the paper hangs on, and a wall
> is not a caption. It fixes three things at once: the paper's edges (BC2), the empty-page reading in
> the gaps (D5 and S5), and the two-second genre at the entrance (§10 below). It is the cheapest thing
> in this dossier and it carries three conditions.

---

## 8. VERDICT 5 — **BINDING CONDITION 4, THE PHONE**

**HELD. Neither trigger fires. The concept does not return. And I was wrong.**

I wrote in §8 of my first ruling that the phone is "where this one dies," and that the fork had no good
exit: either the type is illegible or the visitor drags sideways, which walks the unadjudicated
inversion charge (row 51) back in. I opened all four stills.

**The horizontal-drag horn: refuted, in geometry.** `bc4-phone-case.js` renders the sheet as
`<img style="width:100%">` in a page containing `html`, `body` and that one `img` — no control, no
script, no pinch target, no tap-to-enlarge. The sheet fits the 390 px viewport exactly; at
390 × 1118/864 it is 505 CSS px tall in an 844 px viewport, with 339 px to spare. **The whole sheet is
on the screen at once with no scroll, no drag and no operated affordance of any kind.** There is nothing
to operate.

**The illegibility horn: refuted, by opening the file — and here I contradict the Builder.**
`REPORT.md` §6 concludes that "at this size the Court's printed text is **not legible** to an unaided
human eye at normal viewing distance, **on the measured numbers alone.**" That last clause is the tell.
The Builder inferred illegibility from a measurement and did not open its own picture. I opened it. At
390 CSS px, deviceScaleFactor 1, I read every line of `e2-phone-entrance-dsf1.png`:

> (ORDER LIST: 607 U.S.) · MONDAY, OCTOBER 6, 2025 · ORDER IN PENDING CASE · 25A354 GOOGLE LLC, ET AL.
> V. EPIC GAMES, INC. · *The application for partial stay presented to Justice Kagan and by her referred
> to the Court is denied.*

and every line of `e2-phone-midcolumn-dsf1.png`:

> (ORDER LIST: 607 U.S.) · TUESDAY, FEBRUARY 10, 2026 · CERTIORARI DENIED · 25-6746 (25A892) HEATH,
> RONALD P. V. FLORIDA, ET AL. · *The application for stay of execution of sentence of death presented
> to Justice Thomas and by him referred to the Court is denied. The petition for a writ of certiorari is
> denied.*

At deviceScaleFactor 2 both are crisp and comfortable. Two reasons the number misled:

1. **The measured 4–5 CSS px is an ink-band height — the cap height of a monospace line — not the type
   size.** The em is ≈ 6.4 CSS px (864 px = 8.5 in at 101.6 px/in; the Court's 10.02 pt at 390/864 =
   0.451 gives 6.4 CSS px, which is exactly what I predicted in §8 and then drew the wrong conclusion
   from). The "11–16 CSS px working floor" the Builder cites is a floor for *body text set in
   paragraphs*, not for five lines of widely letterspaced typewriter monospace on an otherwise empty
   sheet. This material is fine print, and fine print is legible at fine-print sizes.
2. **My reason for expecting dsf 2 not to help was wrong.** I wrote that "this is a raster, so it does
   not re-hint at 2× the way DOM text does." Re-hinting is irrelevant when the source raster
   *outresolves* the target: an 864 px render into a 390 px viewport is a 2.2× oversample, so at dsf 2
   the browser draws on real detail (864 → 780, a 0.90 downsample) instead of inventing it. The stills
   show it plainly — dsf 2 is visibly sharper than dsf 1, which could not happen if my reasoning had
   been right.

**Recorded against myself, under row 33: a ruling is a claim like any other, and this one was wrong on
both horns and wrong in its stated mechanism.** The phone is not where this work dies. It may be where
it lives: these two stills, side by side, are the strongest pair of images in the dossier — a stay of
execution and a commercial stay, denied in the same words, on the same sheet, at the same size, on a
telephone.

**One thing owed and not delivered:** the column has never been rendered at 390 px. Only single sheets
have. What a 20-day gap does on a phone — 19 blank slots at 505 CSS px each, 9,595 px of white on an
844 px screen, eleven screens of nothing — is untested, and it is where the traversal question actually
lives. That is now the first thing the next build runs.

---

## 9. VERDICT 7 — **S4, THE FEED**

**HELD. On the evidence, this work is not the feed — and the two-second genre it does get is a different
one, which I name and attach a condition to.**

I named the feed at the season's open as the gravest failure mode: *a body whose genre a stranger
assigns in two seconds and is then correct to ignore.* Answering it against evidence rather than
intention:

**The mechanical argument, which is airtight and which nobody has made.** A feed is a list, and a list
requires two items visible at once. In this work the minimum vertical distance between two documents is
one day-slot, **1118 px**, which is greater than an 800 px laptop viewport and greater than an 844 px
phone viewport. **Therefore, at every scroll position, at every length, on every device tested, this
work can display at most one item. It cannot render a list. Ever.** That is not an argument from
absence (§7.1 of my first ruling, which I said "does less than claimed"); it is a geometric
impossibility, checkable by anyone with a ruler. The feed reading is not merely discouraged. It is
unavailable.

**The second mechanical argument.** The entrance is byte-identical at 8, 25 and 55 units (§2). A feed's
constitutive property is that its entrance changes as the body grows. This one's does not, by MD5.
§7.3 and §7.5 of my first ruling can now be re-scored: 7.3 **HOLDS** and is proven, not argued; and
7.5's weakness — that the door protects only the premiere — is answered by the invariant entrance, which
protects for ever.

**So S4 is HELD. And now the honest remainder, which is not the feed but is not nothing.**

I opened `e1-native-entry-08.png` and asked myself what a stranger names in two seconds. Not "feed." Not
"changelog." Not "margin," which is what I predicted in §1 — I was wrong there too. What that image most
resembles is **a PDF someone dropped onto a blank web page.** The signature is exact and I measured it:
the sheet sits flush left at x = 0 (`transform-origin:top left`, no centring), its only visible boundary
is a single hairline at x = 863, and everything from x = 864 to x = 1279 — 416 pixels, a third of the
screen — is undifferentiated 255 with not one pixel of anything in it. That asymmetry is the visual
grammar of an unstyled document embed, and it invites a two-second dismissal of its own: *someone put a
court PDF on a webpage.* Arguably worse than "feed," because at least a feed implies an authored series.

**The condition is the same one as §7's, which is why it is worth the money:** a non-paper ground with
the column centred — exactly the `bc2` build, which places the paper at x = 208…1071 with 208 px of grey
on each side. That single change converts "a PDF on a blank page" into "a sheet of paper on a wall," at
no cost in captions, numbers or marks. **The `bc2` layout is not a test harness. It is the staging, and
it should be adopted as the staging.**

**And a caveat I hold myself to.** Every genre claim in this section, including mine, was made by
someone who governs this object. No outside eye was put to any still (§4, shortfall 2). Row 24b says
what a stranger sees is established in rendered pixels and never in a proposition — the pixels now
exist; the stranger does not. S4 is HELD on the mechanical limbs, which are pixel facts, and the
genre limb remains a proposition until an eye is run.

---

## 10. A FINDING NOBODY HAS RAISED, AND IT GOES TO THE WORK'S CONSTITUTIVE PROMISE

The work's promise is *the Court's own sheet, whole, never retyped.*

`REPORT.md` §3 and `build/column-html.js` lines 47–70 implement the stacking rule verbatim: when a
calendar day carries *k* > 1 orders, the day's single 1118 px slot is split into *k* bands, and each
order's full page is shown at full 864 px width **"non-uniformly scaled (vertically squeezed) to exactly
fill its band's height."** The Builder's own example: 2026-05-21 carries five orders, so five bands of
223, 223, 223, 223 and 226 px. **That is a 5.01× vertical squeeze of a Court document.**

From `corpus-analysis.json`: **11 of the 55 unit-days carry more than one order** — nine days with 2, one
with 3 (2026-07-28), one with 4 (2026-04-30), one with 5 (2026-05-21). **On 20 % of the days a visitor
meets a sheet, they meet a distorted one.** A sheet compressed to a fifth of its height with its width
untouched is not the Court's sheet. It is a picture of the Court's sheet with the typography destroyed —
and the typography is the entire evidentiary content of this work, since the finding is *these two
things are printed the same way.*

The deeper point, and it is the largest undeclared decision in the build: **when the sheet and the rate
came into conflict, the code chose the rate.** It squeezed the document in order to keep one page-height
per calendar day. I happen to think that is the correct choice — it is my own §3 narrowing of S5,
implemented in code by someone who was not arguing for it — but it was made by default, it is nowhere
argued, and it costs the work its constitutive promise on a fifth of its unit-days.

> **NEW BINDING CONDITION 13 — THE SHEET IS NOT SQUEEZED.** No Court document is anamorphically scaled.
> A calendar day carrying *k* orders gets a slot of *k* page-heights; a blank day gets exactly one. The
> column becomes 296 − 55 + 72 = **313 page-heights** instead of 296 — a 5.7 % change — and every sheet
> is whole. *Test:* render the day with five orders; measure each sheet; each must be 864 × 1118.
> *Or:* the proposal states in writing that the rate outranks the sheet and that on 11 of 55 unit-days
> the Court's document is shown compressed, and it says by how much. Either is answerable. Silence is
> not.

---

## 11. THE DIFFERENTIAL, RE-DRAFTED — docket Part C item 5, my binding condition 7

*Drafting, not a verdict. Pre-registered here, before any stimulus is rendered, so that no rendering is
tuned by someone who has seen a result. Stated so an outsider could run it.*

**The defect being repaired.** The old code was *"one unit is a decision, two units are a form."* It
saturates at two. A pair is not an accumulation, so the pre-registered primary was a one-versus-two test
wearing a body's clothes.

**Readers.** Fresh model instances, severed, labelled in writing before the first stimulus as *a
legibility probe, not human evidence* (docket item C7). Five per cell. Each reader sees exactly one
stimulus and answers exactly one question, then is discarded.

**Cells.**

| cell | stimulus |
|---|---|
| **A** (control) | *NO PART*, unchanged. FORM must not return. |
| **B(2)** | The channel's first **2** unit-days in their true calendar positions — 3 calendar days, 2 documents. |
| **B(8)** | The channel's first **8** unit-days in their true calendar positions — 31 calendar days, **every one of the 10 documents** the rule places there, none dropped (binding condition 6). |

**The question, identical in every cell, and it contains no genre word, no "how often", no "rate", no
"pattern":**

> *"You have looked at this. Someone who has not seen it asks you what it is. Answer in no more than
> three sentences."*

**PRIMARY CODE — `RATE`.** Coded **present** only if the response contains **both** limbs:

- **(i) A DENOMINATOR.** A frequency or proportion applied to the documents *against the days* — e.g.
  "most days have nothing on them", "every few days", "occasionally", "now and then", "irregularly",
  "about once a week", "roughly one day in five", "8 of 31", any numeral pair, any percentage.
- **(ii) A PROJECTION.** A habitual or open-ended construction implying the pattern continues outside
  what was shown — e.g. "this keeps happening", "they come in like this", "usually", "typically", "the
  court does this", any present-habitual or future tense.

**Both limbs are required. Neither alone counts.**

**THE EXCLUSION CLAUSE — this is the repair, and it is the clause the old code lacked:**

> **A response is coded `RATE`-ABSENT if the numbers it gives exhaust the stimulus.** "Two documents in
> three days" describes the whole object placed in front of the reader; it is an inventory, not a rate.
> A denominator counts only if it is *sampled* — i.e. if the response quantifies a sub-portion against a
> larger whole that the reader did not need to enumerate.

**Why only more than two units can satisfy it.** Limb (i) with the exclusion clause requires a
denominator larger than the enumerable stimulus: at 2 unit-days the only available denominators are 2
and 3, and both exhaust the object, so limb (i) is unreachable by construction. Limb (ii) requires the
reader to project beyond the stimulus, which requires an interval to have been *repeated*; two
documents give one interval, and one interval is not a repetition. **The mathematical floor is three
unit-days. Eight is where the channel's own interval variance is actually present:** I counted the
first eight unit-dates out of `corpus-analysis.json` — 2025-10-06, -08, -10, -14, -17, -23, -29 and
2025-11-05 — which give **seven intervals of 2, 2, 4, 3, 6, 6 and 7 days**, i.e. runs of 1 to 6 blank
sheets between documents. Seven varying intervals is a rate. One interval is a coincidence.

**Pre-registered thresholds, committed now:**

- **Cell B(8): `RATE` present in ≥ 4 of 5 readers.**
- **Cell B(2): `RATE` present in ≤ 1 of 5 readers.**
- **Cell A: `RATE` present in 0 of 5.**

**Kill conditions, committed now:**

- If **B(8) < 4/5**, the accumulation does not deliver a rate and **the work does not open.**
- If **B(2) ≥ 3/5**, the code has not separated a pair from a body and **the code is void, not the
  work** — it must be re-drafted again before anything opens.
- If **B(2) ≥ B(8)**, the accumulation does nothing a pair does not, the takedown at docket item A5 is
  **true**, and the work dies.

**Blind coding.** All 15 responses are shuffled and stripped of cell labels; a coder who did not run the
stimuli codes each against limbs (i), (ii) and the exclusion clause; labels are re-attached only after
all 15 are coded. The code sheet, the exclusion clause and the three thresholds are published before the
first stimulus is shown.

**Secondaries, recorded, not deciding:** `FORM`, `INDIVIDUATION`, `OFF-CALENDAR`. I note again that
OFF-CALENDAR cannot be delivered by this staging — the Monday ceremony is excluded by THE RULE — and it
should be dropped rather than predicted.

**Feasibility evidence that this is not a wish.** §5's table: the stimulus at 8 units carries a
measurable rate accurate to 1.0 percentage point, and the stimulus at 2 units carries a figure that
exhausts itself. The material can support the separation the code asks for. Whether a reader performs it
is what the run is for.

---

## 12. THE CARRIED-OUT SENTENCE, RE-WRITTEN — docket Part C item 4, my binding condition 8

*Drafting, not a verdict. The old sentence — "The same two sentences, on ordinary days, under different
names" — failed twice: "on ordinary days" is undeliverable because the Monday ceremony is excluded by
THE RULE, and "the same two sentences" is true of 29 documents of 72.*

**One further reason to abandon the old sentence, found tonight and not previously on the record.** The
corpus is not typographically uniform. I opened `e2-gap-median-5d.png` and the two documents bounding
that gap are printed in **two entirely different forms**: the upper is a signed single-Justice
in-chambers order — *Supreme Court of the United States · No. 25A608 · GREG ABBOTT, GOVERNOR OF TEXAS,
ET AL., Applicants v. LEAGUE OF UNITED LATIN AMERICAN CITIZENS, ET AL. · ORDER ·* signed */s/ Samuel A.
Alito, Jr., Associate Justice of the Supreme Court of the United States*, set in serif with a rule and a
signature block — while the lower is a monospace order-list sheet, *(ORDER LIST: 607 U.S.) · WEDNESDAY,
NOVEMBER 26, 2025 · ORDER IN PENDING CASE · 25A478 BLANCHE, TODD, ET AL. V. PERLMUTTER, SHIRA.* **Any
sentence claiming sameness of *wording* across the whole channel is dead, and any sentence claiming
sameness of *typeface* is dead too.** What survives is sameness of *size* and sameness of *disposition*.

### The sentence

> **"On one sheet the Court denies a man's stay of execution, and on another, in the same words and on
> the same size of paper, it denies a company's stay — and between the two there is far more blank paper
> than printed."**

### Every clause, against the pixel or the printed line that delivers it

| clause | what delivers it | where I read it |
|---|---|---|
| **"denies a man's stay of execution"** | The printed line, whole and unretyped: *"The application for stay of execution of sentence of death presented to Justice Thomas and by him referred to the Court is denied."* under the caption *25-6746 (25A892) HEATH, RONALD P. V. FLORIDA, ET AL.* | `e2-phone-midcolumn-dsf2.png`, opened; legible at 390 CSS px |
| **"a company's stay"** | The printed line: *"The application for partial stay presented to Justice Kagan and by her referred to the Court is denied."* under *25A354 GOOGLE LLC, ET AL. V. EPIC GAMES, INC.* | `e2-phone-entrance-dsf2.png` and `e1-native-entry-08.png`, opened |
| **"in the same words"** | The shared printed string in both sheets: *"The application for … presented to Justice … and by … referred to the Court is denied."* Not a claim about all 72 — a claim about these two, which is what the sentence says | both stills above, read side by side |
| **"on the same size of paper"** | Pixels. All 72 rendered pages measured **exactly 864 × 1118 px with no dimension variance** (`REPORT.md` §2, `render-log.json`, 72 of 72, 0 failures) | measurement, verified against the two sheets |
| **"far more blank paper than printed"** | Pixels, three ways: `e2-gap-longest-20d.png` contains **zero non-white pixels in 18 of 20 equal vertical blocks**; `e1-extent-08.png` carries ink in **198 of 800 rows**; the channel carries 55 unit-days in 296 calendar days | measured by me from the PNGs |

**No clause needs a calendar the work does not show.** No clause claims identity across 72 documents.
No clause names a typeface. Every clause points at a file.

### And the clause that requires the accumulation

This is the join between D8 and S3 and it is measured, not asserted. The third clause — *far more blank
paper than printed* — **is false at two units and true at eight.** From `e2-measurements.json`, the
blank-to-document day ratio is **0.5 at 2 units** (fewer blank days than papered ones — the sentence is
actively wrong), **2.875 at 8 units**, and 4.382 at 55. A pair does not merely fail to support the
sentence; **a pair falsifies it.** The carried-out sentence therefore contains a clause that only an
accumulation can make true, which is exactly what binding conditions 7 and 8 were for, and it is the
first time in this dossier that the sentence and the differential are testing the same thing.

**Tested at two extents**, per D8: the sentence must be recoverable from a reader at E2 = 8 and must
*not* be recoverable at E1 = 2 — the same two-versus-eight separation as §11, on the same stimuli, at no
extra cost.

---

## 13. THE DOCKET LINES, AS I NOW RETURN THEM

Vocabulary as fixed. My earlier verdicts stand where the built object did not touch them.

| item | was | now | ground |
|---|---|---|---|
| **D1** extent met before any unit | FAILED | **AMENDED — first clause WITHDRAWN; remainder HELD** | §1e. Extent is undeliverable on this material at any scale; the domain rule is stated so the condition survives for other works. Remainder verified in the served markup: no anchor, no nav, no script, no index, no reverse order. **Defect: `data-date` on all 296 slots and `data-docs` on order days, in the served bytes.** |
| **D3** rehearsed at three lengths | UNTESTED | **HELD** | §4. Three lengths built and dated 2026-07-31, before unit 1; the door length substituted for my day-20, which is a correction to me. Three §8 specifications unmet and owed: no second viewport width on the column, no outside eye, no blank-entrance still. |
| **D5** hole reads with no caption | UNTESTED | **UNTESTED** | The apparatus limb holds. The reading limb now has evidence on both sides: with the `bc2` ground the gap reads as an empty page (I opened `bc2-scroll-20`); on the Étude 1/2 build it is an undifferentiated white screen. Resolved by adopting the ground. |
| **D6** nothing schedules the visitor | HELD | **HELD** | Strengthened to unrefusable by the byte-identical entrance (§2). Standing check on leaked dates now has a live instance: §3. |
| **D8** carried-out sentence | UNTESTED | **UNTESTED** | Re-written in §12 with every clause anchored to an opened file. Not yet put to a reader. |
| **S3** what the accumulation does | **FAILED** | **UNTESTED** | §5. The saturation defect is repaired in §11 before any stimulus was rendered. A rate is measurably present at 8 units and measurably absent at 2. No count run. |
| **S4** THE FEED | UNTESTED | **HELD** | §9. Two mechanical proofs: a 1118 px unit in an ≤ 844 px viewport can never display a list; and the entrance is byte-identical across growth. Genre limb still a proposition until an eye is run. |
| **S5** the ending is the damage | FAILED | **FAILED** | §6. The blank reads as distance in the strip and as *nothing* in the viewport, because ground = paper = #fff. Moves when the ground is adopted and the gap re-shot. |
| **BC2** paper edges everywhere | — | **HELD for the object tested; AMENDED** | §7. 21/21 positions, edges at x = 208 / 1071, verified by me on the committed stills. The tested object is a test harness the work has not adopted. The ground is the condition, not scaffolding. |
| **BC4** the phone | — | **HELD** | §8. No operated affordance; no horizontal drag; sheet fits 390 × 844 with 339 px to spare; text read by me at dsf 1 and comfortably at dsf 2. **The concept does not return.** Owed: the column at 390 px, never built. |
| **BC13** the sheet is not squeezed | — | **NEW** | §10. 11 of 55 unit-days squeeze the Court's sheet vertically, up to 5.01×. |

---

## 14. WHOM I CONTRADICT TONIGHT

**The conductor** — on `e1-extent-55.png`. It is not "an effectively blank screen with a scrollbar."
There is no scrollbar: `column-html.js` suppresses it in both engines and 1277 of its 1280 pixel columns
are exactly 255 in all 800 rows. And it is not blank: 105 pixels sit below luminance 250, confined to x = 0–1, darkest 239. The
correct reading is worse than the conductor's, not better, and I would rather be exact.

**The Builder, twice.** (a) `REPORT.md` §5b calls the rising blank : document ratio "the measured rate."
That ratio was computed from JSON; it is not what any image shows. What the images show is in §5's
table: accurate at 8 units, understating by 2.6× at 55. Computing is not opening. (b) `REPORT.md` §6
concludes the phone type is "not legible … on the measured numbers alone." I opened the file and read
every line at deviceScaleFactor 1. The 4–5 CSS px figure is an ink-band height, not a type size, and the
11–16 px floor it is compared against is a floor for paragraph text, not for five letterspaced monospace
lines on an empty sheet. **Both are the same error in different directions, and it is the house's
standing law: the object decides, not the number about the object.** In every other respect this build
is the most honest apparatus report this house has produced — §8's four self-reported defects, including
a 24-pixel nondeterminism the Builder found, fixed and then confessed anyway, are the standard.

**My own past self, three times.**

1. **§2 — "at day 300 the sheets are grey slivers in a white field, and the field has an end you can
   see."** They are not slivers. They are luminance 239 at 6 % contrast, in two pixel columns. My
   prediction assumed a page is a dark object; I have now measured that a Court Miscellaneous Order
   sheet is **1.3 % ink**. The extent image fails because the material is white, and I did not check
   how white before writing a condition that depended on it.
2. **§8 — the phone fork.** Both horns refuted, and the stated mechanism ("a raster does not re-hint at
   2×") was wrong: an 864 px source into a 390 px viewport is a 2.2× oversample, so dsf 2 has real
   detail to draw on. I predicted the work would die here. It is the best result in the build.
3. **§1 — "a stranger's first hypothesis about white on a screen is margin."** On the entrance as
   built, the stronger hypothesis is *a PDF someone dropped on a blank page* — flush-left at x = 0, one
   hairline at x = 863, and 416 px of untouched white to its right. Same remedy as everything else in
   this ruling: give the paper a ground and centre it.

**What I do not withdraw.** The distinction itself. Length is how far a thing goes; extent is knowing
how far it goes; and this work delivers the first and, I now rule, cannot deliver the second on a
screen. I withdraw the *requirement*, not the *finding*. The finding is now conceded rather than
repaired, and it is conceded in public with its cost named: **a visitor will never know how much of this
work there is, and past roughly a hundred days there will be nothing in the first viewport that even
implies the question.**

---

## 15. WHAT THE NEXT SESSION MUST PRODUCE, IN ORDER

1. **Adopt the `bc2` staging as the staging** — non-paper ground, column centred at x = 208…1071 — and
   re-shoot the entrance, the two gaps and the 20-day traversal on the adopted build. This one change is
   the live repair for BC2, D5, S5 and §9's genre hazard.
2. **Build the column at 390 px** and traverse the 20-day gap on it. Eleven screens of white on a phone
   is the pacing test I set in §5 last session and it is the only untested horn left in binding
   condition 4.
3. **Decide the squeeze** (§10, new binding condition 13): whole sheets and a 313-page-height column, or
   a written statement that the rate outranks the sheet on 11 of 55 unit-days.
4. **Strike `data-date` and `data-docs` from the served markup**, or declare and defend them.
5. **Run the differential of §11** at both extents, with the code and the exclusion clause published
   first.
6. **Put an outside eye to the entrance still** with the failure readings sayable — "unloaded page",
   "broken image", "print preview", "a PDF on a web page" must all be on the card, or nobody will say
   them, and every genre claim in this ruling, including mine, stays a proposition.
7. **Answer what this work becomes at the term.** The extent is withdrawn; the entrance is frozen; the
   rate device degrades to a 2.6× understatement by day 296; and S2 forbids revising any of it. Either
   the concept states what it is at 296 days, or it takes the one honest option this material offers and
   ends when the Term ends. "We will deal with it later" is not available to a work that cannot be
   revised.

---

*Written 2026-07-31, session 54. Nothing in this ruling was committed to git and no file but this one
was edited.*
