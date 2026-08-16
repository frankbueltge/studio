# Concept — session 98, 2026-08-16

The Artist's proposal, put to the concept gate under Protocol v3 §1. Published **unedited**,
including its §7, in which the Artist argues against its own proposal at length.

**Read the conductor's correction of its numbers first.** It is below the proposal, not above it,
because the proposal is the artefact and the correction is ours.

---

## The proposal, as returned

**1. THE CLAIM, IN ONE SENTENCE.**
Across 3,310 recorded edits to 99 completed drug trials, the four verified moments where a promised outcome was substantively rewritten after the sponsor already had the data are rendered at the same size, speed, and color as thousands of harmless capitalization fixes, and this indistinguishability is the entire experience on screen — not a caption added to it.

**2. THE MACHINE ADVANTAGE.**
Repetition, with verification as its consequence. A human proofreader reading 3,310 version boundaries tires and starts weighting the ones that look important; the machine applies the identical character-level diff to boundary 1 and boundary 3,310 with no drop in attention, so nothing gets treated as more important along the way. The visitor does not see that process. What they see is its output, rendered continuously: a title-case fix and the punctate-corneal-staining threshold moving from 2 to 1 arrive on screen as ticks of the same size, grey, click, and speed, because the same unweighted operation touched both. That flatness, sustained minute after minute rather than stated once, is what a visitor perceives — not an argument about concealment, but concealment's actual shape: uniform, ungraded, and running.

**3. THE FORM, AND WHY THIS FORM.**
Second 0: full-viewport dark canvas, projected, no title card, no legend, no scrollable text. Ninety-nine horizontal lines fill the frame top to bottom, one per trial, each a lifeline from registration to its last recorded version, with ticks at the real date of each version. Second 0–30: ticks light in true chronological order compressed into a fixed loop of several minutes, each with a soft click; click density visibly and audibly rises around the periods when trials actually got edited hardest, then falls. By minute 5 the loop nears its restart; if untouched, the full 3,310-tick field pulses once and begins again — never identical run to run, since it replays real dates, not a hand-authored animation. If a visitor touches a line, that row expands to fill the frame: the tick nearest primary-completion grows slightly, and for the twelve trials with full version text, dragging scrubs continuously through every version with the actual outcome sentence on screen, differing characters the only colored pixels against an otherwise monochrome frame. For the other eighty-seven, the same touch shows only real metadata (date, status, which section changed) — no invented text is ever shown. A low tone sustains only while a numeric character is changing during the scrub; a rough, hand-tuned proxy, not a solved classifier, firing on the four verified cases and any other numeric edit sharing their shape. Floor options carried: time-based behavior (real, non-repeating chronology driving continuous motion), interaction that changes what is shown (scrub into live-mutating text, not mere reveal), and sound (click-track sonifying edit density plus the numeric-change tone). Presentation: projection, full-viewport, unattended, looping indefinitely; any text on screen is a single sentence at a time, shown only during an active scrub, never a scroll.

**4. THE VISITOR ON THE OTHER SIDE.**
Someone walking past a lobby or gallery wall gets the rhythm and the flatness — uneven pulses, one color, one size, one kind of click — within about twenty to thirty seconds, without reading a word of English or medicine. Someone who stops and touches a line gets, after perhaps ninety seconds to three minutes of scrubbing, to a moment where they watch an actual sentence about a drug trial's finish line mutate under their own hand while a tone plays. A clinician or a data journalist recognizes the stakes on sight. Honestly: a visitor who never touches anything, or cannot read the outcome text, leaves with only the pulse and click — uneven rhythm, no story — and is not wrong about what they saw; the claim that something was rewritten after the answer was known requires the minute of scrubbing, and most gallery visitors do not give any one work a minute.

**5. THE MATERIAL.**
Everything shown is committed at build time, not fetched live (cross-host network calls are blocked): all 3,310 version-index entries — trial ID, version number, date, status, which sections changed — for the 99 usable completed phase-3 records, plus the actual extracted primary-outcome-measure text at each of the 123 versions across the 12 fully diffed records. Nothing outside that set is shown or implied. Honest limits: 99 trials is a sample, not the registry; 12 fully diffed trials is nowhere near enough to state a rate at which substantive rewriting happens — only that it happens, four times, confirmed by hand. The unsolved problem, stated plainly: there is no reliable rule that separates a typographic edit from a substantive one. Both arrive in the identical diff format; the only method that found the four real cases here was a person reading all 123 diffs. The on-screen numeric-change tone is a coarse proxy tuned against those four known answers — it will also fire on harmless numeric noise, such as a sample-size typo fix — and the work does not claim otherwise.

**6. THREE TO SIX MILESTONES.**
The full 99-line, 3,310-tick field renders at correct scale and real dates, with no placeholder data anywhere on screen.
The loop plays start to finish unattended, click density audibly and visibly tracking the real edit rhythm, with no input required.
Any of the 12 fully diffed trials can be scrubbed by touch, producing live, character-level mutating outcome text with differing characters the only color on screen.
All four verified substantive rewrites are reachable by ordinary scrubbing within the loop's running time, unlabeled and unflagged.
The numeric-change tone audibly fires on at least the four verified cases during a full loop without any on-screen text explaining why.
The piece runs the full loop unattended for at least one hour on the target projection hardware without drift, stall, or a frozen frame.

**7. WHAT WOULD MAKE THIS DEAD.**
The honest weakness is proportion. Twelve trials fully diffed and four confirmed substantive rewrites is a small, careful finding; ninety-nine lines and thirty-three hundred ticks filling a wall is a scale of presentation the finding does not earn. A visitor who does the arithmetic — four out of twelve checked, out of ninety-nine sampled, out of a registry of hundreds of thousands — could reasonably conclude the work borrows the visual weight of "everything" to carry a result that is, honestly, four sentences. That is the exact dishonesty this house exists to prevent: a claim experienced as bigger than what was verified. Second, the premise depends on the four cases surfacing for a visitor who behaves normally, not one told where to scrub; if the numeric-change tone fires constantly on ordinary noise, or rarely enough that a normal three-minute visit never reaches one of the four, the machine advantage collapses into decoration — a pretty field with a secret buried so deep no unattended visitor finds it, which is the same failure as a wall label nobody reads. Third, the heuristic was tuned by a human reading the four answers first; if it teaches the ear nothing beyond what that person already found by hand, this is a human finding wearing a digital coat, not a machine doing what a human could not. Any of these three, true once built, is grounds to kill this before it opens.

---

## The conductor's correction of the proposal's numbers

The Artist wrote against a scratch pass. Between that pass and this file, the capture was rewritten
as a committed script (`capture.py`) and re-run from scratch, which re-drew the sample. **Every
figure in the proposal above is therefore superseded**, and the figures of record are the committed
corpus's own, all reproducible by re-running the script:

| the proposal says | the committed corpus holds |
|---|---|
| 3,310 edits | **3,316 versions** (`corpus/history.json`) |
| 99 trials | **100 records** (`corpus/studies.json`) |
| 123 versions across the 12 fully diffed | **276 versions** across the 12 (`corpus/amendments.json`) |
| — | **20** primary-outcome text amendments in that diffed set |

What did **not** move: **11 of 12** fully diffed records had the promised primary outcome text change
at all, and **11 of 12** had it change after the primary completion date. Both hold on the new draw
as they did on the old. The sampled records span **2005-06-23 → 2026-04-24**.

**One thing the proposal states that the corpus does not support as written.** Of the four named
substantive rewrites, **only one — NCT01285492 (Novartis) — is inside the committed set of twelve
fully diffed records.** The other three were found in the earlier draw and are captured individually
in `corpus/cases.json`. So the proposal's §3 and §6, which promise that all four are reachable by
scrubbing the twelve, describe an object that would have to be built against a corpus that does not
yet exist in this repository. That is a defect in the proposal, not in the material — the cases are
real and captured — but it is exactly the sort of gap this house has previously discovered at a
premiere gate instead of here.

**A caveat that is load-bearing and belongs to any work built on this.** The history route sits in
an undocumented `int` namespace; `GET /api/v2/studies/{NCT}/history` returns 404. The data is public
— any visitor can read the same history at `clinicaltrials.gov/study/{NCT}?tab=history` (confirmed
HTTP 200 tonight) — but the machine route carries no stability guarantee. A corpus frozen at BUILD
survives that; a promise to a visitor that the route still answers tomorrow would not.
