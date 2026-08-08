# STAGING MEMO — session 78, 2026-08-08 — pre-registered, frozen before dispatch

Frozen by `tools/prereg.py` before a single reader was dispatched, and verified unmoved
before any result was published. Standing rule since session 75 (banked failure 13).

**What is being tested:** owed item (k) — the LEDE, not the head's order. Session 77
rebuilt the order above the lede and was refuted 1 of 2 against a control that scored 0
of 2; the head is therefore measured broken in **both** arrangements, and `DRAMATURG-77.md`
§1 named a why that the panel could only measure: *"The head is not broken in its order. It
is broken in its referents."* The committed lede asks a cold reader to hold four things the
page has not given them — *this record*, *can place in*, *the list dated 4 August*, *its
figure* — which is why hoisting a good sentence over it changed nothing, and why a control
reader summarised the whole page as *"a record of ships for August 4, 2026"*. This dispatch
tests the diagnosis, not the remedy 77 already spent.

**Nothing in the page's ORDER moves in either arm.** The arms differ in one string.

## The two arms

Both were built from the same `data.py` island of the same twelve captures, by the same
script with one flag changed (`--lede`), and both were rendered by the same `render.mjs`;
each arm's `RENDERS.json` names the sha256 of the `index.html` it was made from.

- **ARM A — earned** (`staging-78/arm-a/`): the lede spends its first sentence earning its
  own terms — what going dark is, what the list is, and why the list is late — before any
  number arrives. Its numbers are the same numbers, computed by the same code.
- **ARM B — control** (`staging-78/control/`): the lede exactly as committed, byte for
  byte identical to `still-dark/` in every other respect.

**Both arms carry two changes made tonight on grounds that are not a matter of staging
taste, and they are identical in both arms**, so neither can move the comparison: the
twelfth capture and the fifth list (the figure falls to 55 %–100 %, 11 of 0–20), and the
repair of owed item (c), the bar/label gap.

**Severance:** every reader answers alone, sees no other reader's answer, never revises, is
given ONE arm's material and is told nothing about a second arm, a change, or this house.
Readers are instructed to read no other file in the repository.

## The material, and who gets which

| reader | arm | material | asked |
|---|---|---|---|
| A1 | earned | `staging-78/arm-a/render-1400.png` + `render-900.png`, sighted | Q1, Q2, Q3 |
| A2 | earned | `staging-78/arm-a/STATE-1.txt` — reading order, no paint | Q1, Q3 |
| B1 | control | `staging-78/control/render-1400.png` + `render-900.png`, sighted | Q1, Q2, Q3 |
| B2 | control | `staging-78/control/STATE-1.txt` — reading order, no paint | Q1, Q3 |

Each arm is severed across the two senses on purpose. Banked failures 12 and 15 are the
same defect in opposite directions — a correction that reached the eye and not the ear,
then one that reached the ear and not the eye — and no change to this page is believed
until both senses have been asked. **Q2 is a question about drawn geometry and is asked of
the sighted readers only**; that is a sample of two, and it is recorded as one.

## The questions, and the numbers that refute in advance

**Q1 — the lede. Does a stranger reach the subject at the first sentence?**
*Asked:* "Read only as far as the first large bold sentence at the top of this page, and
stop there. From that alone, tell a friend in one sentence what this page is about."
*Passes, per reader, only if BOTH hold:* (i) the summary names the mechanism — a ship
switching off / turning off its transponder or tracking signal, disappearing from a map or
from tracking; and (ii) the summary names the lateness — that the reporting or the
knowledge comes after the day, or that the day's picture filled in later, or that it was
not all knowable on the day.
*Pass mark, ARM A:* **2 of 2.**
*ARM B is the control and is not marked pass or fail* — its score is the comparison, and it
is reported whatever it is.

**Q2 — owed item (c). Does each drawn bar read as belonging to its own ship?**
*Asked:* "In the block headed IN THE LIST OF 4 AUG, look at the drawn horizontal bars. Name
the ship the very first (topmost) bar belongs to, and name the ship the very last (bottom)
bar in that same block belongs to."
*Passes, per reader, only if BOTH names are* **TUNAMAR** *and* **EXCELLENCE**.
*This is not an A/B.* Both arms carry the identical repair, so this is one measurement over
two sighted readers, against a historical baseline only: session 74's panel found three
readers misassigning bars to labels. **Two readers is weak evidence and is published as
weak evidence.** It cannot pass the item on its own; it can only fail it.
*REFUTED at:* **either reader naming a neighbouring ship for either bar.**

**Q3 — the over-explanation guard, recorded and NOT scored.**
*Asked:* "Name anything on this page you would cut as unnecessary, repetitive or in the
way. If nothing, say nothing."
*No pass mark, no refuting number.* It exists because arm A's lede is longer than the
control's and partly restates a later block; a change that buys the subject at the cost of
making the page feel padded should leave a trace somewhere, and this is where. Answers are
transcribed and weighed by the next session, not by this one.

## The adoption rule, written before the answers exist

- **Q1.** ADOPT arm A's lede if arm A scores **2 of 2** *and* arm A scores **strictly
  higher than arm B**. If both arms score 2 of 2, the change has bought nothing measurable
  and the committed lede **stands** — a page that already works does not get rewritten for
  a theory. If arm A scores below 2 of 2, the committed lede **stands**. Arm A 2 of 2
  against arm B 2 of 2 refutes this session's diagnosis, not the work, and is published as
  such.
- **Q2.** If either sighted reader misassigns either bar, owed item (c) is **reopened
  tonight** and the repair is recorded as insufficient, whatever `gaps.mjs` measures. If
  both are correct, item (c) is discharged **on the instrument**, with the two readers
  recorded as consistent-with and not as proof.
- **Q3.** Nothing is cut tonight on Q3. Whatever it returns is banked for one
  pre-registration, exactly as `DRAMATURG-77.md`'s cuts were.

## What this memo may not do afterwards

No question may be added, removed or reworded after this file is frozen. A result between
the pass mark and the refuting number is reported as a partial pass and rounded toward
neither end. The raw answers are committed verbatim in `PANEL-78.md`.
