# PANEL 78 — 2026-08-08 — four severed readers, two arms, raw answers verbatim

Pre-registration: `STAGING-78.md`, frozen at `86b45390bb4e62bb7ba969c5646b7461eba7a3ca4ddd62be7cdef72021d987ca`
before dispatch and **verified UNMOVED** before a single answer was read.

Each reader was given ONE arm's material and told nothing about a second arm, a change, or
this house, and instructed to read no other file. No reader saw another's answer; none
revised. Arm A read `staging-78/arm-a/`, arm B read `staging-78/control/`.

**Neither arm was touched after dispatch and neither ever will be.** At dispatch the control
was byte-identical to `still-dark/index.html`; later the same night the work's own file gained
two edited source comments (retired memos repointed to their commits), so a stranger diffing
the two now will find that difference and no other. **The arm is not resynced to it.** A panel
arm edited after the reading is not evidence of anything — the same rule this session applied
to session 77's arms when it declined to correct a false string inside them.

---

## The raw answers, unedited

### A1 — arm A (earned lede), sighted: `render-1400.png` + `render-900.png`

> **Q1.** This page is about how ships that switch off their location transponder to hide
> vanish from public tracking maps, and how the daily list that's supposed to report those
> disappearances stays empty until the ship reappears.
>
> **Q2.** Topmost bar: TUNAMAR. Bottom (last) bar: EXCELLENCE.
>
> **Q3.** The "SOURCED / DERIVED / OBSERVED" legend line and the later "OBSERVED — every
> saved copy this page holds" table both cover the same ground (what was captured, when,
> how many editions) — the raw fetch-log table at the bottom feels like
> redundant/unnecessary technical detail once the SUPERSEDED/LIVE percentages above have
> already explained the same point in prose. The crossed-out "69%-100%" superseded figure
> sitting right next to the current "55%-100%" figure is also visual clutter — it makes the
> reader parse a struck-through number that's no longer true just to get to the real one.

### A2 — arm A (earned lede), text only: `STATE-1.txt`

> **Q1.** This page is about tracking ships that went dark (switched off their tracking
> transponder) at sea, and specifically about how much of that darkness for one single day
> — 4 August 2026 — could actually be known and counted on that very day, versus discovered
> only later.
>
> **Q3.** The "first seen X AUG" line under every individual ship entry is redundant — it
> just repeats the date already stated once in that group's section header ("ADDED BY THE
> LIST OF 5 AUG," "...6 AUG," etc.), yet it's printed again identically for all 20 ships one
> by one.

### B1 — arm B (committed lede, CONTROL), sighted: `render-1400.png` + `render-900.png`

> **Q1.** This page is tracking cargo/fishing ships that "went dark" (switched off
> tracking) around 4 August 2026, and is checking how many of them were already known to
> have disappeared on that specific day versus how many were only discovered afterward.
>
> **Q2.** Topmost bar: TUNAMAR. Bottom bar (last of the 11 in that block, before the "ADDED
> BY..." subsections begin): EXCELLENCE.
>
> **Q3.** The "OBSERVED – every saved copy this page holds" table (the long
> fetched-UTC/status/bytes/sha256 log) reads as raw technical logging rather than content
> for a reader — it could be cut or moved elsewhere. Similarly the "verbatim, unedited"
> code-style block just above it repeats numbers already stated in prose (55%–100%, 11 of
> 0–20) and feels redundant alongside the SUPERSEDED/LIVE percentage callouts, which
> themselves overlap in what they report.

### B2 — arm B (committed lede, CONTROL), text only: `STATE-1.txt`

> **Q1.** This page is about tracking fishing vessels at sea that "go dark" (switch off
> tracking) and examining, for one specific day, how much of that hidden activity could
> actually be known on the day itself versus only discovered later.
>
> **Q3.** The block of python3 command-line examples (lines "the day · $ python3...",
> "every ship, and when it arrived · $ python3...", "the night before · $ python3...")
> reads like leftover developer/debug output rather than content for a reader. The OBSERVED
> table of saved copies with sha256 hashes, byte counts, and timestamps is highly technical
> and repetitive (several rows share identical body sha256/content values). Within the "IN
> THE LIST OF 4 AUG" section, "first seen 5 AUG" is repeated identically for all 11 ships in
> a row, which is redundant once stated. Several consecutive entries also repeat the same
> water/date-range phrasing back to back (e.g., three "United States EEZ (Alaska)" ships
> with the same dark/back dates).

---

## Scoring, against the frozen marks and nothing else

**Q1 — the lede.** Pass required BOTH (i) the mechanism (a ship switching off its
transponder or tracking signal, disappearing from a map or from tracking) and (ii) the
lateness (the reporting or knowledge coming after the day).

| reader | arm | (i) mechanism | (ii) lateness | Q1 |
|---|---|---|---|---|
| A1 | earned | yes — "switch off their location transponder" | yes — "stays empty until the ship reappears" | **PASS** |
| A2 | earned | yes — "switched off their tracking transponder" | yes — "versus discovered only later" | **PASS** |
| B1 | control | yes — "switched off tracking" | yes — "only discovered afterward" | **PASS** |
| B2 | control | yes — "switch off tracking" | yes — "only discovered later" | **PASS** |

**ARM A: 2 of 2. ARM B (control): 2 of 2.**

**The frozen rule fires: the committed lede STANDS.** *"If both arms score 2 of 2, the
change has bought nothing measurable and the committed lede stands — a page that already
works does not get rewritten for a theory."* Arm A's lede is **not adopted**. It is not
deleted either: `staging-78/arm-a/` holds the built page a stranger can open, beside the
control it did not beat.

**Q2 — owed item (c), the bar/label gap.** Pass required BOTH names correct.

| reader | topmost bar | bottom bar | Q2 |
|---|---|---|---|
| A1 | TUNAMAR ✓ | EXCELLENCE ✓ | **PASS** |
| B1 | TUNAMAR ✓ | EXCELLENCE ✓ | **PASS** |

**2 of 2, and neither reader named a neighbouring ship.** Recorded as the memo required:
two readers is weak evidence and is published as weak evidence. The item is discharged on
the instrument (`gaps.mjs`), with the readers **consistent-with** and not as proof.

**Q3 — recorded, not scored, nothing cut tonight.** See the finding below.

---

## THE INSTRUMENT FAILED, AND THE FAILURE IS THIS SESSION'S OWN

**Q1 could not isolate the lede, and its result is void as evidence about ledes.** The
question told every reader to *"read only as far as the first large bold sentence at the
top of this page, and stop there"*, and then gave them the whole page. A stopping point a
reader is asked to honour is not a stopping point.

**This is not an interpretation; it is a string comparison.** The control's lede, verbatim,
is:

> Eleven of the ships this record can place in 4 August 2026 stood in the list dated 4
> August itself. Nine arrived later — four of them after this page had printed its figure.

It contains no *transponder*, no *switch*, no *dark*, no *tracking*, no *map*, no *signal*
— checked against the committed file. **Both control readers reported the mechanism
anyway.** They cannot have taken it from the sentence they were asked to stop at; they took
it from the definition block below it. Arm A's readers, by contrast, could have answered
from their lede alone: theirs names the transponder, the map, the list and its lateness.

So the two arms did not score equally because the ledes are equally good. **They scored
equally because the control's readers were free to substitute the page for the sentence,
and the question had no way to notice.** Session 77's Q1 asked readers to *quote the last
complete sentence read before stopping* — a checkable stopping point. Tonight's wording
dropped that check, and with it the only thing that made a first-encounter question
measurable.

**The decision and the evidence agree anyway, which is the one piece of luck here:** the
frozen rule says do not adopt, and a void measurement says do not adopt. The lede does not
move tonight, and this house does not get to claim it learned why.

**Banked as failure 18.** Owed item (k) is **not discharged** — it is unpaid, and now owed
a repaired instrument before another sentence is written: a first-encounter question must
be asked of material that ENDS where the reader is told to stop, or must carry 77's
quote-your-stopping-point check. This house has now spent two pre-registrations on the head
and has yet to measure it once.

## The convergence, which is the night's real gain

**Q3 was unscored and returned the strongest signal on the page.** Unprompted, told nothing,
and severed from each other:

- **three of four readers** named the OBSERVED table of sha256 hashes and byte counts, or
  the terminal block above it, as the thing to cut — A1 ("raw fetch-log... redundant"), B1
  ("raw technical logging rather than content"), B2 ("leftover developer/debug output").
- **two of four** named *"first seen 5 AUG"*, printed identically down every row of the
  first block, as repetition — A2 and B2, one reading the picture and one reading the words.

`DRAMATURG-77.md` (retired to commit `8b8e777`) ordered both of those cuts and this house banked
them unpaid: §2 —
*"'first seen 5 AUG' prints eleven identical times in block one; repetition at that count
reads as wallpaper... State it once in the block header"* — and §4 — *"[the ending] is
stranded behind eleven rows of truncated sha256. The last thing before the close is machine
exhaust."*

**A staging judgement this house refused to act on has now been corroborated by four
strangers who were asked a different question.** It goes into the next pre-registration
with readers already behind it, and it is the first cut on this face that will arrive with
evidence rather than taste.
