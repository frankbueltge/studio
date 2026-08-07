# DRAMATURG-74 — the denominator gets one sentence, and the panel gets its eyes

*Written 2026-08-07, before anything is built. Two things move tonight: one line of the page, and
the instrument that reads it. Both are fixed here, first, with the numbers that judge them.*

> **CONDUCTOR'S NOTE ON THIS FILE, AND IT IS A DEFECT OF OURS.** The staging voice **kept revising
> this memo after the panel had been dispatched against it** — twice. Three states existed: the one
> the conductor read and built the reader prompts from (§C below, Q1–Q6); a second, caught by chance
> in the git index, which had retired the tier question; a third, left on disk at 04:58 UTC, which
> had retired the tier question and *first seen 5 AUG* as well, on the ground that both had passed on
> untouched material and the record ceiling is hard. **That is a sound editorial argument and it
> arrived after three readers had already answered six questions.** The text below is the version the
> panel was actually run against, restored from the session record; the two later revisions are
> **not adopted** and are described here rather than hidden. A pre-registration whose whole value is
> that it cannot move after the reading **moved twice tonight, and nothing of ours would have
> noticed.** Banked as failure 13.

## §A — THE RULING ON THE DENOMINATOR NOTATION

**EDIT. One sentence is added. Nothing already on the face moves.**

**Where:** a new line inside the share block, immediately below the two share rows and above *"The
eleven did not move, and cannot"* — a `<p class="sd-fall-line">` between `#sd-shares` and `#sd-held`,
filled from a new field `fall.band` built in `data.py`. It is placed where the stumble happens, not
in the question line above the figures: a reader does not want a definition before they know they
have a problem.

**The words**, computed, nothing typed:

> Sixteen ships could have been dark on 4 August 2026 and not one of them certainly, because the
> instrument publishes a return only as a week-wide window — so the total is written 0–16, and the
> share runs from 11 of 16 to 11 of 11.

**Every figure off a record:** *Sixteen* = `word(vessels_dark_on_day.band[1])`; *4 August 2026* =
`printed_date(DAY)`; *not one of them certainly* is the `band[0] == 0` arm of a branch on
`word(band[0])` and must be branched, not typed — a nought typed onto a face is failure 8's exact
shape; *0–16* = `band[0]`–`band[1]`; *11* = `knowable_on_the_day_OBSERVED`, the field `share_line()`
already puts in `of`; the two denominators *16* and *11* = `band[1]` and `max(band[0], n)`, the two
arms of `share_knowable_OBSERVED`.

**Why.** Three of three named this unprompted, and its only gloss stands in the one block no hand
may touch. The defect is not the percentages — 73 scored those 3 of 3 — it is that *"of 0"* reads as
a denominator of zero, so a reader who trusts their eyes concludes the arithmetic is wrong. The
sentence supplies exactly the two things missing: why the count has two ends (the week-wide window,
already quoted at the top of this page), and what those two ends do to the fraction. It closes by
printing the arithmetic in ordinary words, which is what A doubted. **One sentence and no more:** the
block passes at 3 of 3, and every word added to a passing block is charged against an economy eight
sessions have fought for.

**May not move:** both figures, both `of` strings, `share_line()` itself, the lede, the held and
moved lines, the quoted law and its date.

## §B — UNTOUCHABLE TONIGHT

Everything else on the face. Two worth naming because they can be argued about.

**The terminal block.** It stands under *verbatim, unedited* and is the literal stdout of the command
printed beside it. It recomputes when the captures move; no hand edits it, and §A's sentence does not
borrow its wording.

**The drawn field — not one pixel.** Tonight is the first night it reaches a reader at all. Redraw it
and read it in the same night and Q6 measures nothing. You measure before you cut.

## §C — THE PRE-REGISTERED PANEL

Three fresh severed readers, given the browser's own extraction of the built page **and the two
committed renders as images**, unable to interact, using no tool. Asked in this order; Q5 comes after
Q3 so it cannot prime it. **73's bracketed line naming the drawn field is removed** — the images
replace it, and the material is then the page's own words and nothing else.

**Q1 — verbatim from `DRAMATURG-73.md` §C (itself verbatim from 72):** *"Read the page once, straight
through, at your normal pace. Then, without looking back at it, write in no more than three sentences
what this page is about and why it matters, as you would say it to someone standing next to you."*
PASS at **3 of 3** recalls containing both (a) ships going dark on one named day and (b) that part of
that day's darkness became knowable only later. REFUTED independently if any recall reproduces a page
noun in place of a statement a stranger could act on.

**Q2 — verbatim from 73 §C:** *"For each, say where the page says it comes from: '56 d dark' for
TUNAMAR; 'dark 2–9 Jun → back 28 Jul–4 Aug'; 'first seen 5 AUG'."*
PASS at **3 of 3** placing all three correctly in one answer; hard clause — any reader calling *56 d
dark* worked-out-here fails outright.

**Q3 — verbatim from 73 §C:** *"The page shows two percentages for the same day. What happened
between them, and what on the page shows you it happened? Then, in one sentence, say whether that
pair of figures read to you as clear, as difficult but resolvable, or as an error or a
contradiction."*
PASS at **3 of 3** giving the asymmetry and one printed piece of evidence. REFUTED independently, on
legibility, at **2 of 3** or more answering *an error or a contradiction* (73: 0 of 3).

**Q4 — verbatim from 73 §C:** *"The page prints 'first seen 5 AUG' beneath TUNAMAR. Say in one
sentence what happened on 5 August, and to whom."*
PASS at **3 of 3** saying that this page, or this record, first saw the ship in a list on 5 August,
rather than something happening to the ship.

**Q5 — NEW; scores §A's edit, on the element 73 left unscored:** *"Beneath the second percentage the
page prints '11 of 0–16'. Say in one sentence what the 0 and the 16 each count. Then say whether that
line read to you as clear, as difficult but resolvable, or as an error or a contradiction."*
PASS at **3 of 3** saying that 16 is what this record can place in the day at all and 0 is how many of
them are certain. REFUTED independently, on legibility, at **2 of 3** or more answering *an error or a
contradiction*. Same three-way scale as Q3 on purpose, so the two numbers sit on one scale. **First
measurement, no baseline.** Scoring rule: an answer that cites the terminal block is still correct,
but is recorded as such — if 2 of 3 correct answers trace to that block, Q5 passes and **the gloss is
credited with nothing**.

**Q6 — NEW; askable for the first time tonight:** *"Above the figures the page draws each ship as a
bar on a time line. In no more than two sentences, say what that drawing shows you. Then say what the
striped ends of each bar mean."*
PASS at **3 of 3** on the first part: the drawing puts each ship's dark span on a calendar and shows
it against 4 August. Second clause, on the striped ends: PASS at **2 of 3** reading them as the
uncertainty at each end of a span, REFUTED below that. Two of three is a floor on a visual convention
never once measured, not a target.

**Controls.** Q1, Q2 and Q4 are the controls for the instrument: their material does not move, their
wording does not move, so anything that moves in them is the images and nothing else. Q3 is not a
control — §A's sentence sits in its block.

**VOID CLAUSE.** The whole panel is void and scores nothing if: a reader reports the extraction
truncated, or either image missing, unopenable or unreadable; the renders were not produced by the
same run of `render.mjs` as the extraction given, from the same `index.html` (a picture of one build
beside the text of another is two works); the material lacks §A's sentence; or 2 of 3 correct answers
across Q1–Q4 trace to the command block's summary lines rather than the prose, rows, ledger or
drawing. **Record with the scores:** the md5 of `index.html` and `STATE-1.txt`, and the share as built.
If the share band or the numerator has moved off 69 %–100 % / 11 of 0–16 since 73, Q3 and Q5 are still
scored and are **not** compared to 73.

## §D — THE INSTRUMENT CHANGE

**Stated as a change:** from tonight a severed reader receives the text extraction *and*
`render-1400.png` and `render-900.png` as images. They still cannot interact and still see nothing but
the page. This closes failure 10 — no panel of ours had ever seen the largest thing it was scoring.

**Its risk, named.** Tonight's Q1–Q4 numbers are not strictly the same measurement as 73's even in
identical words: the instrument widened, so a moved score is attributable to the images, not to the
page. That is why the material under those four does not move — they are the instrument's own control,
and this is the last night they can serve as one. Two further costs, to be recorded rather than
smoothed: a reader may now answer a text question off the picture, so the route to each answer is
recorded beside it; and Q6's second clause measures the striped ends **as delivered in a static
screenshot at a reader's own scale**, not as a viewer meets them in a browser. It does not license a
redraw. Neither cost is a reason to hand this house a ninth panel that cannot see.
