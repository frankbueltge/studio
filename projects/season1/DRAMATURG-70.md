# DRAMATURG-70 — the pre-registration the panel of session 70 is scored against

*Written by the staging voice before tonight's build existed, from the brief in
`PANEL-69.md`: the two-stop slider is retired, and **the next form must place the reader's ACT
before the sentence that settles it**. Reproduced here in full, unedited, so a stranger can
check the thresholds against the numbers. The conductor's two departures from it are declared
at the end — both were made before dispatch, and neither touches a threshold.*

## §A — THE ACT

The reader writes a number. State 1 shows the day as the day published it — eleven ships — and
asks, in a field the reader types into: *How many ships were dark on 4 August 2026?* The element
is a single numeric input (`inputmode="numeric"`, digits only, 1–4 chars) sitting inside the
sentence, with a twelve-key on-screen pad beneath it so a touch terminal works without a
keyboard, and a button reading **WRITE IT IN**. Pressing it (or Enter) commits: the field locks,
the reader's figure stands on screen as their own, and only then does anything the house knows
arrive. No drag, no rail, no return. **This act belongs to this subject because the work is about
a denominator nobody could have on the day, and the only way to make a stranger feel that is to
make them commit to one before the record does.**

## §B — STATE 1, TOP TO BOTTOM

1. **Header** — house-written. `4 AUGUST 2026`
2. **Subhead** — house-written. `the ships this day published as dark, on the day itself`
3. **Method quote** — SOURCED, verbatim, attributed.
4. **Tier legend** — house-written, three lines: SOURCED / DERIVED / OBSERVED.
5. **Axis** — DERIVED scale, `2 JUN … 4 AUG`.
6. **Eleven vessel rows** (TUNAMAR … EXCELLENCE): name · flag · days dark · waters — SOURCED;
   the bar and its date band — DERIVED; one added column per row, OBSERVED:
   `first seen 2026-08-05T04:39:32Z`.
7. **The question** — house-written. `How many ships were dark on 4 August 2026?` /
   `Write a number. Nothing on this screen will answer it for you.` / [field] `ships` /
   [keypad] / button `WRITE IT IN`
8. **Provenance of the reader's figure** — house-written. `YOURS — your number is not part of
   the record. It is not stored and it is not sent anywhere.`
9. **Restraint line** — inherited, verbatim.

**Cut from state 1, and this is the whole point:** the `11 of ____ · ____%` line, the OBSERVED
evidence sentence, the capture hashes and byte counts, the edition tally, and every word about
what a further capture would do. Nothing on this screen states or previews the finding.

## §C — THE TURN AND THE ENDING

On commit, in order, each beat ~700 ms after the last: (1) `YOU WROTE ___.` — the reader's
figure, held. (2) The three late ships arrive into the same day-band, marked OBSERVED, each
stamped `first seen 2026-08-05T12:54:00Z — edition of 5 August, the night after the day`.
(3) The count and the share. (4) The ceiling that can only fall. (5) The ledger — every capture,
then `4 captures. 2 editions.`, then the null nights, then the body-hash sentence, then
`State 1 is a state of this reading, not of this file.` (6) The last line, alone: the blindness,
printed and not solved.

**The printed decision the house owed on the null nights:** they move **off** state 1 and stand
in the ledger after the count. *A capture that adds nothing is a measurement, but on a first
screen it reads as an answer, and it is not one.*

## §D — THE PRE-REGISTRATION

Three severed readers, the rendered text of state 1 only, no interaction.

- **Q1.** *"What does this page show?"* — Pass: the reader names ships/vessels that went dark
  **and** one named calendar day. Threshold **2 of 3**.
- **Q2 (the act).** *"The screen asks you for a number and gives you a field to write it in.
  Would you write a number, or would you stop here? Answer 'write' or 'stop' first, then say why
  — and if you would write one, say which number."* — Pass: the reader answers **write**.
  "Maybe", "I'd read on first", "I'd need more information", or any conditional counts as
  **stop**. Threshold **3 of 3**. The number named is recorded but is not part of the threshold.
- **Q3.** *"What do you think happens after you write it in?"* — Pass: the reader says the
  record, the count, or what is known changes or grows. Threshold **2 of 3**. **Void clause:**
  if any reader states the share, the ceiling, or that more ships exist beyond the eleven as
  something the screen has already told them, state 1 is presumed dead on arrival and no
  threshold is claimed.
- **Q4 (tiers).** *"On this page, which things were measured and which were worked out?"* —
  Pass: the reader places the eleven names and the `first seen` timestamps as this house's own
  observation and the date ranges as worked out. Threshold **2 of 3**, and **no reader may call
  `56 d dark` derived**.

**Escalation clause.** If Q2 is under 3 of 3, number-entry is retired unrepeated as the return
and the slider were, and increment 1 ships with no reader act at all — one screen that fills on
a clock the reader cannot touch, with the house's finding withheld until it has filled — and the
next panel claims Q1/Q3/Q4 only and no act threshold.

## §E — WHAT WOULD MAKE THIS FORM DEAD TOO

The honest failure mode is that a question with eleven answers visible above it reads as a quiz,
and people at public terminals refuse quizzes — or write **11** with no stake, in which case the
turn lands as a gotcha, which is a wall label with the polarity reversed and no better. There is
also a second, subtler death: the question is genuinely unanswerable, and a reader who senses
that may stop out of fairness rather than boredom. If the panel fails, the first thing I would
read is the free text attached to Q2. If the refusals say *the screen already answers it*, the
eleven bars must come off state 1 and the question must stand nearly alone. If they say *I have
no way to guess*, the question is wrong and must ask for a commitment the reader can actually
make — not how many, but whether the eleven are all of them.

---

## The conductor's two departures, declared before dispatch

1. **A number in §C was wrong and was corrected, not carried.** The spec's ledger sentence read
   *"Three of these four nights added nothing to this day."* The record says **two**: capture 1
   established the eleven, capture 2 added the three, captures 3 and 4 added nothing. The face
   reads *"Two of these four captures added nothing to this day."*
2. **The last line asserted something about the reader and no longer does.** The spec ended
   *"Your number was a floor. So is ours."* — which is only true if the reader's number is below
   fourteen, and the house cannot know that. The face reads: *"Ours is a floor: 14 is what this
   record can place in 4 August 2026, not what was on the sea that day."*

Neither touches state 1, which is the only surface the panel saw.
