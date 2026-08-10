# DRAMATURG 82 — 2026-08-10 — the restaged head, judged on the running object

Convened on a finished object, as the constitution requires. It was given the built page and
told it could drive the page itself; **it did — at six widths, taking its own timings against
`performance.now()` and its own click tests.** It was told what the previous staging voice had
ruled and what this house had built in answer, so that it would not spend its judgement
re-finding what was already found. It was shown **no reader's answer**, and the panel had not
been scored when it wrote. **It judges and it cuts; it does not co-write.** Verbatim, unedited.

---

## 1. FIRST ENCOUNTER

> I drove the built page and timed the mutation of `#sd-arrive-count` against
> `performance.now()`. The first figure changes at **11,530 ms** from navigation. The next three
> land at **13,133 / 14,735 / 16,3xx** — deltas of 1,603 and 1,602 ms. The run ends around
> **17.9 s**.
>
> So: what happens in fifteen seconds?
>
> Seconds 0–11.5, the page is **completely still**. No cue of any kind says a sequence is
> pending — I checked for one and there is none. What a stranger sees is a finished static page:
> a title, a 44-word gloss, `100 %–100 %` in 48 px, eleven bordered ship names, a sentence about
> a hole, a hedge, and **a row of six buttons with the first one already inverted black**.
>
> **Is the eleven-second hold a held beat or a broken page?** Neither. It is a **held beat that
> reads as an invitation**, and that is worse than either.
>
> It does not read as broken, because nothing on screen is empty or spinning or half-drawn — and
> because the reserved block is now *headed*, which is the single best thing this restaging did.
> "NAMED ONLY BY LATER LISTS — nothing yet. The space below is the part of this day that nobody
> could have had on it." That sentence turns 66 px of white into a held breath instead of a
> rendering failure. That is real dramaturgy and it is correctly placed.
>
> But it does not read as a *held beat* either, because a held beat is legible as held. Eleven
> and a half seconds is roughly four times the longest pause an audience will read as intentional
> without a held-ness signal, and this page gives none. What it does give is six clickable stops.
> And the stranger's most available action, staring at `100 %–100 %` next to a button strip, is
> to press a button.
>
> I tested that. **Click "+2 DAYS" at t = 3.0 s and the run is dead.** The count sits at
> `69 %–100 %` unchanged through t = 15.3 s. `halt()` clears both the interval and the beat, so a
> single touch inside the new eleven-second window destroys the only authored sequence the object
> has, permanently, unless the visitor finds "run it again" — a grey button at the end of the
> strip that gives no indication anything was lost.
>
> Before this restaging that window was ~1.6 s. Tonight's fix widened the interval in which the
> piece can be silently cancelled **by a factor of seven**, and put nothing in it. That is the
> cost nobody measured.
>
> Second problem with the beat, arithmetic rather than behavioural. The dwell is 44 words ÷ 238
> wpm = 11,092 ms. But 44 words is the **gloss alone**. Above the buttons a stranger must read:
> subject (9 w) + gloss (44 w) + the figure's own "when" clause (21 w) + eleven chips +
> since-heading (24 w) + hedge (23 w) ≈ **121 words ≈ 30.5 s at the page's own rate.** The derived
> beat covers **36 %** of the text a stranger needs before the controls.
>
> Concretely: at exactly 238 wpm a reader finishes the gloss at 11.09 s and *arrives at the
> number* — which moves 0.4 s later. The 21-word clause that tells them what the number means
> ("of 4 AUGUST 2026's darkness was knowable on the day itself, counting the lists up to 4 AUG")
> takes 5.3 s more, finishing at ~16.4 s. By then frames 1, 2 and 3 have already passed. **The
> sentence that explains the number is rewritten under the reader mid-sentence, three times, on
> first acquaintance.** DRAMATURG-81's defect has not been removed. It has been moved one
> paragraph down and made harder to see.

## 2. THE TURN

> **No. Tonight did not touch it.**
>
> Six frames, six shares, one direction. Every frame says the same thing the caption already said
> in prose before the run began: "That is why the figure above falls, and why it can only go on
> falling." Frame six delivers no information frame two withheld. The chips accumulate; the number
> decreases; the vocabulary is identical at every stop ("— *n* ships dark on that same day that
> nobody could have had on it", six times, one word changed).
>
> Tonight *did* add one candidate. Stop 5's clause gains a sentence no other stop carries:
> **"Only the lower end has moved, and the next list can only lower it again."** That is a turn's
> content. It is not staged as one. It arrives as lines four and five of a paragraph the reader
> has been trained by four repetitions to stop reading, in the same 1.6 s beat as the largest
> chip-fill of the run, in the same grey as the boilerplate around it — and the reader's eye is on
> the chips, because the chips just moved.
>
> And here is what makes that a waste rather than a shortfall. The six shares are:
>
> ```
> 100 %–100 %   79 %–100 %   69 %–100 %   65 %–100 %   55 %–100 %   44 %–100 %
> ```
>
> **The right-hand number never moves.** Across the entire run, one figure falls 56 points and one
> figure does not move at all — because a register that names a ship only when it comes back can
> never rule out a ship that never comes back, so the ceiling is structurally unfallable. That is
> the piece's actual subject. It is present in every frame, on screen for eighteen seconds, and
> **nothing marks it.** Both ends are set in the same weight, the same size, the same colour. The
> page's own most interesting fact is rendered as if it were a repetition.
>
> So: is the form embodying its subject or illustrating it? The *reserved emptiness* embodies — a
> hole sized to exactly what will later fill it, named before it fills, is the whole argument in
> one gesture, and it is excellent. The *falling number* illustrates. It animates a sentence the
> caption already wrote.

## 3. THE COST

> **Was cutting the provenance paragraph right? Yes. Unambiguously.** An unglossed command line
> whose only variable across six frames is a ticking timestamp is not evidence at 1.6 s; it is
> costume. The head is 278 words now and it reads. That paragraph did not leave the page — the
> OBSERVED table is still in the body, seventeen fetch rows with sha256 prefixes, byte counts and
> edition dates, plus the verbatim commands beneath it. Provenance moved to where provenance can
> be read. Correct.
>
> **What the head lost, and should get back in one clause:** the head no longer says *anywhere*
> that this page is reading **saved copies**. The new gloss says what the *source* is ("the daily
> editions of The Ghost Fleet, a public register... which can name a ship only once it has come
> back") — that is a fact about the register, not about this page's evidence. A stranger who never
> scrolls past y=687 has no reason to believe the six frames are anything but the page's own
> assertion. Six words would fix it. That is the whole cost of the cut, and it is worth paying.
>
> **What is said twice.** Three findings, all verified against the source:
>
> 1. **The head's restraint line is a byte-identical duplicate of the body's**
>    (`index.html:758` vs `:570`): *"'Intentional' is a machine estimate by Global Fishing Watch —
>    a probability, not proof..."* — 30 words, printed twice on one page. Worse: **the word
>    "intentional" appears nowhere in the head.** The head disclaims a term it never uses. The term
>    is introduced ~430 px *below* the head's copy of the disclaimer. This is dead weight in the
>    strict sense — a caveat that arrives before its subject and then arrives again, correctly,
>    after it. **Cut the head's copy.** That is 32 px reclaimed at the head's foot and one fewer
>    thing between the buttons and the reader.
>
> 2. **The head's caption is restated in body prose 200 px later.** Head: "A ship reaches the list
>    only after it comes back, so a day that is over keeps being answered." Body: "A ship's
>    disappearance reaches the instrument's daily list only when the ship comes back. So a day of
>    the sea is nearly empty on the day itself and keeps filling for weeks afterwards." Same
>    sentence, twice, in sight of each other. One should go; I would keep the head's, which is
>    tighter.
>
> 3. **"on the day itself" is said three times before the run starts** — in the subtitle, in the
>    section heading, and in the figure's clause — and then six more times, once per frame, since
>    all six `when` strings repeat the same ten words verbatim. The head re-renders an unchanging
>    clause 55 characters long on every beat while the visitor is looking for what changed. **The
>    clause should be static and only the tail should move.** That is not a wording preference; it
>    is what a reader's eye needs in a 1.6 s beat.
>
> **What else I would cut:** the hedge, as placed. "A list gives a ship's return only to the
> nearest week, so not one of these names is certainly dark on this day." Moving it down beside
> the names was right in principle. In practice it now sits at y=466, directly above the button
> row at y=511, and **at stop 0 it sits immediately under 66 px of blank**, where it reads as
> qualifying the emptiness. And read at stop 0 against `100 %–100 %`, it says that not one of the
> names underwriting that 100 % is certain — a full retraction of the figure, set in 12 px grey,
> positioned exactly where the reader is looking past it toward the buttons. Either it belongs
> *inside* the "IN THE LIST DATED 4 AUG" heading where it qualifies the eleven, or it belongs in
> the caption. It does not belong in the gutter above the controls.

## 4. THE WEAK JOINT

> Not the button walk. That is genuinely repaired, and I want it on record: I drove all six stops
> at **six** widths and the ladder's top is at 511 / 511 / 490 / 513 / 649 / 800 px at 1400 / 1100
> / 900 / 700 / 520 / 390, with **spread 0 px at every width** — and the reservation is recomputed
> as the maximum over all six stops, so it holds when the block's tallest state is stop 0's
> heading rather than stop 5's chips. That is careful work done properly.
>
> **The weak joint is that the run is unannounced, uncancellable-by-accident-only-in-one-direction,
> and mute — and the derivation that authorises its length is authority the page has not earned.**
>
> Three measurements, one joint:
>
> - **`document.querySelectorAll('[aria-live],[role=status],[role=alert]').length` returns 0.**
>   The reduced-motion branch is honoured and stop 0 is served at rest with the buttons — good, and
>   correctly reasoned. But `prefers-reduced-motion` is not a screen-reader flag. A screen-reader
>   user who has not set it gets the full run: six DOM rewrites of the figure, the heading and the
>   name list, over eighteen seconds, **with nothing announced**. Their virtual cursor is reading a
>   document that is being rewritten behind it. The page reasoned carefully about one audience and
>   did not check whether that reasoning covered the audience it was actually about.
>
> - **A click at t = 3 s ends the run forever.** Verified above. The piece stages its longest, most
>   deliberate beat inside a window where its own most obvious affordance silently kills the
>   staging. The previous voice said a moving target is "a control in name only"; a control that
>   destroys the performance without saying so is worse than one that moves.
>
> - **The 238 wpm derivation is doing rhetorical work its arithmetic does not support.** It
>   measures 44 of the ~121 words a stranger must read before the controls. It is a *mean* — the
>   page's own source code concedes "this beat is too short for many of the people it is set for" —
>   and a figure that the author knows fails for a large fraction of its audience, presented with a
>   citation and a meta-analysis of 190 studies, is not a measurement, it is a warrant. The
>   nine-word phrase "derived, not chosen" is doing the persuading; 238 is doing none. **On a page
>   whose entire moral subject is the difference between what an instrument can establish and what
>   it merely publishes, this is the one place where the object itself commits the fault it is
>   about.** That is why it is the weak joint and not merely a defect: it is the only seam where
>   the form contradicts the argument.

## 5. VERDICT

> **RETURNS FOR RESTAGING.**
>
> **The weakness:** the head now stages eleven and a half seconds of deliberate stillness inside a
> window in which a single click destroys the performance, with no announcement to anyone using a
> screen reader and no signal to anyone else that a performance exists. Tonight's repair created
> that window; nothing was put in it. The head is well-built and it is one touch from never having
> happened.
>
> **The one change that would most improve it: mark the constant.** Set the right-hand `100 %`
> apart from the left — hold it in the body weight while the left falls in the display weight, or
> grey it, or rule it — so that across eighteen seconds the visitor watches one number fall against
> one that structurally cannot. Do this and frame six's "Only the lower end has moved, and the next
> list can only lower it again" stops being a sentence the page has to say and becomes the
> confirmation of something the visitor has been watching without being told. That is the turn this
> piece has been missing through two stagings, and it is already on screen, in every frame,
> unstyled. It costs one CSS rule.
>
> (Second, and nearly free: delete the head's duplicate restraint line, make the ten unchanging
> words of the figure's clause static so only the tail redraws, and give any stop-button pressed
> during the first beat the behaviour of *entering* the run at that stop rather than killing it.)

---

> **DOES THIS DISCHARGE §5's RESTAGING VERDICT — YES.**
>
> Both limbs were built and both hold under measurement, not assertion. The reservation: the button
> row's top is invariant at 511 / 511 / 490 / 513 / 649 / 800 px across all six stops at 1400 /
> 1100 / 900 / 700 / 520 / 390 wide — spread 0 px at every width, with no overflow of the held
> elements at any of them — and it is computed as the maximum over every stop rather than the last,
> which is the correct reading of what §5 asked for and stricter than the letter of it. The freed
> first beat: the first figure holds for a measured 11,530 ms from navigation before it moves,
> against 1,603 ms for each step after. §5 is discharged.
>
> It is discharged and the head is still returned, because §5 was a prescription for two named
> defects and not a description of a finished piece. The pacing fault it diagnosed has been
> reduced, not removed — the definition is now legible before the number moves, but the clause that
> makes the number *mean* anything is still overwritten under a first-time reader three times — and
> the fix introduced a new fault of its own in the eleven seconds it bought.

---

## What this house did with it tonight, and what it did not

**§3's six words were TAKEN, and they arrived by the same door as a blocking verifying failure.**
The voice asked for one clause saying the page reads **saved copies**; the Verifier, independently
and on a different ground, found that cutting the provenance paragraph had left this work's largest
number with **no tier mark anywhere on its face**. One sentence pays both and is on the committed
page: *"DERIVED — this share is worked out here, from saved copies of those lists. Nobody publishes
it."* It carries the tier word for the figure above it, it names the evidence, it does not move
between stops, and it is not a command.

**§4's first measurement was re-taken by this house before it was believed** — `[aria-live],
[role=status],[role=alert]` returns **0** on the committed page, confirmed first-hand. It is
**banked as an owed item and NOT repaired tonight**, and the reason is stated rather than implied:
a live region rewriting six times in eighteen seconds may be worse for the visitor it is for than
silence, and this house does not ship an accessibility change it has not measured. What would
settle it is named in `PROJECT.md` under owed item (t).

**§5's one change — mark the constant — is NOT taken tonight, and it is the strongest thing said
about this work in three sessions.** It goes to the next pre-registration, in the shape the voice
wrote it, sight unseen of any answer. The house's standing practice since session 80 is that a
staging prescription is built and then measured, not built and then admired; and a fourth change to
this head after tonight's panel has already read it would leave every one of them unattributed.

**§1's second finding — a click during the beat kills the run — is banked as owed item (s), with
the voice's own prescription verbatim.** The house does not take a behaviour change on a voice's
word (banked failure 23), and the alternative it proposes — a press during the beat *entering* the
run rather than halting it — makes the same button mean two different things at two different
moments, which is a decision that deserves a frozen rule and two readers rather than a night's
taste.

**§3's cut of the head's duplicate restraint line is REFUSED tonight, and the refusal is on the
record with its reason.** The voice is right that the head disclaims a term the head never uses —
and two severed readers said the same thing independently on the same night (`PANEL-82.md`). But
the restraint travels with the **names**, by the publishing condition this house accepted, and the
head names twenty-five vessels and their flags. The repair is to **anchor the word**, not to remove
the caveat, and that is owed item (r).
