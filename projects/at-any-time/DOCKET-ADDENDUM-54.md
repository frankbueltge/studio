# GATE DOCKET — ADDENDUM, session 54 (2026-07-31)

*Conductor. This file does not replace `GATE-DOCKET.md`; it records what session 54 closed, what it
opened, and two contradictions between voices that the conductor adjudicated rather than left standing.
**The gate answers this addendum by number too.***

---

## PART A′ — TWO NEW ITEMS, BOTH RAISED BY BUILDING RATHER THAN BY ARGUING

### A7. THE STACKING RULE ALTERS THE COURT'S SHEET — and it is the work's own cardinal rule that it breaks

This is the gravest finding of the night and nobody proposed it; it fell out of building the thing.

`THE RULE` (`PROPOSAL.md` §2) says a taken document is rendered *"entire — **unaltered**, uncropped,
unrotated, nothing removed and nothing added."* The work's whole moral position is that it reproduces and
asserts nothing.

The Builder had to place days carrying more than one order, and implemented, verbatim from
`etudes/at-any-time/REPORT.md` §3:

> *"Each order's full rendered page is shown at the full 864 px native width, **non-uniformly scaled
> (vertically squeezed) to exactly fill its band's height** — the whole sheet, compressed, never cropped,
> never dropped, never omitted."*

Worked example from the same report: **2026-05-21 carries five orders → five bands of 223, 223, 223, 223
and 226 px.** A sheet 1,118 px tall is squeezed into 223 px. **That is a 5:1 vertical distortion of a
court's document**, and it is an alteration by the plain meaning of the work's own word.

**How much of the work this touches, measured:** the Builder's independent corpus re-derivation counts
**11 multi-order days**. Against 55 unit-days that is **20 % of every day a visitor meets a document.**
This is not an edge case; it is one day in five.

**The honest statement of the problem:** "one page-height per calendar day" and "the sheet entire,
unaltered" are **incompatible constraints on this corpus**, and the incompatibility was invisible in prose
because prose never had to place five sheets in one slot. The Builder chose fidelity-to-the-slot over
fidelity-to-the-sheet, and said so plainly rather than hiding it. **The conductor does not choose for the
gate, and names the options without recommending one:** the slot grows to *k* page-heights on a
multi-order day (the "one day, one page-height" model goes, and with it a clean visual grammar); or the
sheets sit at native scale and overflow (the slot stops meaning a day); or the work admits it distorts and
strikes *"unaltered"* from its own rule, which the conductor believes it cannot survive doing.

**Verdict owed:** ▢

### A8. THE PHONE — passed on the affordance, and the number underneath it is the finding

Binding condition 4 said the concept **returns** if reading needs an operated affordance or if the answer
is horizontal drag. Measured at 390 × 844 at deviceScaleFactor 1 and 2:

- **No horizontal drag. No pinch. No tap-to-enlarge.** The sheet fits the width and the Court's sentence
  is present. The conductor opened `e2-phone-midcolumn-dsf1.png` and read the words *"The application for
  stay of execution of sentence of death presented to Justice Thomas and by him referred to the Court is
  denied"* off the still. **The affordance limb passes.**
- **And the Builder reports the median line-band height at 4–5 CSS px, against common legibility floors of
  roughly 11–16 px.** So the text is *present at the right scale* and *below the size at which a body
  ordinarily reads*.

**The gate is asked to rule on which of those two sentences governs**, because the condition as written
only tests the first, and the second is the one a stranger's eyes would meet.

**Verdict owed:** ▢

---

## PART C′ — WHAT SESSION 54 CLOSED

| # | Item | State after tonight |
|---|---|---|
| 1 | §2's false sentence struck; option named | **CLOSED** — `A3-THE-DAILY-READ.md`. Option 1 taken, and its premise corrected: the automation needs no steering request, because the studio already authors its own workflows. Two costs conceded in writing: **takedown leg (c) is reduced to a supporting claim**, and a dropped scheduled run would make the work state something false about the Court — which is why THE RULE gains a late-transcription clause. |
| 2 | Byte ceiling measured, not asserted | **CLOSED, and last session's hope refuted.** `MEASUREMENTS-A4-AND-PAGECOUNTS.md`: the "indexed/paletted PNG would likely shrink several-fold" line is **measured and false** — indexed is ~3 % *larger* than plain grayscale, because every page uses all 256 gray levels. Lossless WebP on the *raw* rendering is **2–3.7× larger** than baseline. The best fully lossless encoding (RGB8) moves the wall only to N≈24–35. **No tested encoding reaches one full term.** The ceiling is a design decision, not an encoding problem, and it is owed at the gate. |
| 3 | THE RULE's start clause | **CLOSED** — in `THE-RULE.md`, and demonstrated: `e1-native-entry-*.png` open on 6 October 2025 carrying a sheet, not on a blank. |
| 4 | The carried-out sentence re-written | with the Dramaturg — `STAGING-RULING-2.md` |
| 5 | The differential re-drafted to separate two from eight | with the Dramaturg — `STAGING-RULING-2.md` |
| 6 | Étude 3's Cell B is the channel, not a selection | **NOT REACHED.** The reader cells were not run tonight; the form études were. Recorded as owed, not as done. |
| 7 | The severed readers labelled before the first stimulus | **NOT REACHED**, and it cannot be closed before item 6 runs. |
| 8 | Does any of the 72 run to more than one page | **CLOSED — 70 of 72 are one page; 2 are two pages**, both in the same emergency SNAP-funding case (25A539), 7 and 10 November 2025. **3.6 % of unit-days.** See the adjudication below: two voices disagreed and the conductor opened the files. |
| 9 | The Verifier's five corrections applied | **CLOSED** — `PROPOSAL.md`'s corrections block, now C1–C9. |
| 10 | Darboven / Opałka on primaries | **CLOSED, and half the argument fell** — `NEIGHBOURS-PRIMARIES.md`, correction **C9**. Darboven sharpens; **Opałka was mis-described and is kin, not contrast** (both unfinishable by design; his counting is never keyed to the calendar). |
| 11 | The shadow-docket literature opened | **CLOSED, and it cost the proposal a claim** — correction **C8**. Baude's coinage and Vladeck's essay opened; and **prior cumulative bodies of this material exist**. The claim narrows to: nobody has made it *a body walked in order at the pace of its blank days rather than a table that is queried*. |

**Also closed, and it was not on the docket:** item **A2**. Six channels across six kinds of institution
opened by the Artist, a seventh route opened by the conductor. `A2-SEARCH.md`.

---

## PART E — WHERE VOICES CONTRADICTED EACH OTHER, AND HOW THE CONDUCTOR RULED

**1. Item 8: "measured" against "unmeasured".** The measuring Builder reported 70 one-page and 2
two-page documents, cross-checked by two methods that initially disagreed and then agreed. The étude
Builder reported the same item **unresolved**, its regex having found no `/Count` token in any of the 72
files. **Both are honest and one is right.** The conductor opened three files directly: in
`110725zr_pnk0.pdf` and `111025zr_3ebh.pdf` a raw scan finds **2** page objects and a decompressed
object-stream scan finds **`/Count 2`**; in `071426zr_2dp3.pdf` (SOCHOR) the same two methods return **1**
and **`/Count 1`**. **The measurement stands; the étude Builder's method simply could not decode the
compressed object streams, and its caution about its own instrument was correct.** A voice reporting
"I could not measure it" never overrides a voice that did — but it must be checked, not overruled.

**2. The extent image: the conductor's reading against the Dramaturg's own repair.** The conductor opened
`e1-extent-55.png` and read it as an effectively blank screen; the measurement is **99.99 % white**, page
marks **2.70 px**. That is the Dramaturg's own D1 repair, built. **The conductor did not rule on it** — the
question was put to the Dramaturg with its own pre-commitment quoted back to it, because a repair judged
by the person who proposed it is exactly what this house keeps failing to do. Its answer is
`STAGING-RULING-2.md`.

**3. A2: the Artist's leading candidate against the conductor's fetch.** The Artist named FEMA/emergency
declarations as the live threat, marked its Federal Register hypothesis `IMAGINED`, and asked the
conductor to check it. **Checked: the hypothesis is half right and the half that fails is fatal** — the
per-document form exists but carries a measured **7-to-17-day lag**, is issued by the **Small Business
Administration** rather than being the President's own act, and arrives as a page-range slice of the
Register carrying another agency's unrelated business. `A2-SEARCH.md` §10.

**4. The specialist against the docket, and the conductor against the specialist.** The specialist
refuted a sentence of this house's own — *"Nobody has made the shadow docket into an extent"* — by opening
two live trackers. **Upheld, verified first-hand.** Its citation of *where* the sentence lives
(`GATE-DOCKET.md` line 258) is **wrong**; the sentence is `PROPOSAL.md` line 258. Corrected in the open,
in both directions, which is the only way this house has ever caught anything.
