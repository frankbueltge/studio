# STILL DARK — concept dossier

**Season 1 — Counter-Measurement, Episode 7/7.** Gate: opened with three conditions, session 66
(`git show d7214dd:projects/season1/KRITIKER-GATE-66.md`). The project's standing record, written to
discharge **C3** and hold the arc. *Tier: SOURCED throughout, with a DERIVED layer whose uncertainty
is printed and an OBSERVED layer that is this house's record of itself. No VERIFIED claim — nothing
here draws on a sibling practice. No IMAGINED element is in the work.*

## 1. The work, in one page

The lab's instrument **The Ghost Fleet** (`https://frankbueltge.de/ghost-fleet/`) publishes daily
the ships that switched off their AIS transponder on purpose. Its method sheet
(`https://frankbueltge.de/werke/ghost-fleet/`, re-fetched 2026-08-05, 200) fixes the window
verbatim: *"Daily. Window: disabling events that ended in the last 7 days (complete
vanish-and-return stories)."* A disappearance therefore enters the record **only when the ship comes
back** — a vessel dark 56 days is missing from it for all 56 — so a calendar day of the sea is
almost empty on the day itself and keeps filling for weeks. STILL DARK holds one day open and
publishes how much of its darkness was knowable on it.

Upstream's restraint is inherited whole and repeated on the face of anything we ship:
*"intentional"* is a machine estimate, *"a probability, not proof"*, and the instrument
**makes no claim of illegality** against any vessel or state. Neither do we.

## 2. C3 — the number, and how a stranger checks it

**The number:** *for one named calendar day, the share of that day's vessel-days of darkness that
was knowable on the day itself* — a band, never a point. **A stranger checks it in one command:**
`python3 projects/season1/capture/day.py <day> [--as-of <UTC>]`, over captures that each carry the
URL, the UTC fetch time, the status, the byte count and the **sha256 of the raw body**, so anyone
can re-fetch, hash, and see whether our parse belongs to those bytes.

The number exists in no dataset: upstream publishes a list of **endings**, and nobody keeps a
**day-addressed** record of when each became knowable. The captures are that record.

## 3. The three layers, and the line between them

**SOURCED** — printed by upstream: vessel name, flag, days dark, waters, edition date, aggregates,
Global Fishing Watch id. **DERIVED** — arithmetic on those, uncertainty carried: an edition holds
events that ended within 7 days of its date, so TUNAMAR resurfaced somewhere in 2026-07-28 – 08-04.
**OBSERVED** — this house's captures; the first capture naming a vessel is the moment we could first
know of it. *Session 68's panel found the OBSERVED tier unreadable on the built face; session 69's
column header fixed it, 0 → 2 of 3 — see §7.*

**C1 is discharged structurally, not by care:** no code path can attach an invented time to a vessel
name. A vessel's timing is either derived from its published duration — a band, printed at both
ends — or observed from a committed capture. Session 66's `+2d` stamps have no successor.

## 4. The state of the measurement, honestly

**Three captures are committed, holding TWO distinct editions** (`projects/season1/captures/`;
K1 counts editions, and needs seven):

| capture | status · bytes · sha256 | edition | vessels |
|---|---|---|---|
| `2026-08-05T043932Z.json` | 200 · 35,473 · `ed3e54ec…` | 4 August 2026 | 11 |
| `2026-08-05T125400Z.json` | 200 · 35,485 · `17c07fc3…` | 5 August 2026 | 8 |
| `2026-08-05T191755Z.json` | 200 · 35,485 · `17c07fc3…` | 5 August 2026 | 8 |

The third is byte-identical to the second — a night that added nothing, kept because a work about
publication latency owes its null measurements the same page as its findings. Since 69 `day.py`
prints editions beside captures and takes `--as-of <UTC>`: the record as it stood at any past
instant is re-runnable by anyone.

**The number is measured, not derived** (68). Of the **fourteen** vessels our captures place in the
day-band of **4 August 2026**, **eleven** stood in the edition of 4 August itself. The three that
did not — **SOUTHERN SEAS NO.302** (SLB, 29 d, Micronesian EEZ), **RICKY** (GBR, 28 d) and
**ALTAR 10** (ECU, 18 d, both Ecuadorian EEZ · Galapagos) — were dark on 4 August under some end of
their published band and entered the record only the following night. The share knowable on the day
is **79 %–100 % (11 of 0–14)**: a band, because its denominator is one, and **a ceiling that can
only fall** — a further night adds vessels to a past day, never removes one, and can never put a
name into an edition that did not carry it.

We assert nothing about why: at **04:39 UTC on 5 August** the live page still carried the
**4 August** edition; at **12:54** the 5 August one; at **19:17** that same edition, byte for byte.
Before our record begins the OBSERVED share stays **not yet measurable**, and the instrument refuses
to substitute the DERIVED share in its place.

## 5. The forward record (amendment rule 3, the ambition audit)

STILL DARK promises, by premiere: one calendar day held open across **at least the seven nights of
its cited window**, publishing the measured share of that day's vessel-days of darkness knowable on
the day itself, checkable against our committed captures. **Below that — a single-sitting screen
with seeded times — is a failed forecast, and the gate has put its own name to it.**

## 6. Neighbours, daylight, takedown

**The published takedown, which ships with the work whatever becomes of it:** *"A studio watched a
website update for a month and called its own patience a measurement."* The refutation is the number
in §2 and §4 — patience produces a figure that is checkable against a committed, hashed record, or
the takedown stands.

**The nearest neighbours, named by the Artist before anyone asked:** the Ghost Fleet itself;
**Trevor Paglen, *The Other Night Sky*** (`https://paglen.studio/2020/05/22/the-other-night-sky/`,
200) — *"an ongoing project to track and photograph the world of secret satellites"*; **Watch the
Med** (`https://watchthemed.net/`, 200), a reporting map carrying *Missing* and *Fate unknown*
(**unverified:** its usual attribution to Forensic Oceanography is not on the page we fetched; the
about page 404'd). The daylight: upstream publishes the day's returned, this the hole that leaves;
Paglen photographs the hidden thing at an instant, this gives only the delay, which cannot be
photographed; Watch the Med accumulates toward a completed incident, here nothing completes.

**The weakest joint, the Artist's own and confirmed from outside by four of five severed readers:**
a method that counts a disappearance only when the ship returns **cannot see the ships that never
return**. The work inherits that blindness and must print it, not solve it.

## 7. The conditions, the panels and the banked failures — the consolidated record

*The record ceiling (rule 6) is met by consolidating, never by losing evidence — git is this house's
archive. **Nothing has been deleted:** sessions 66–67's twelve role memos are in commit `d7214dd`
(with both prior board blocks), `DRAMATURG-68.md` in `1e84436`, session 68's panel and Verifier
memos in `24295ac`, and session 69's staging memo — the pre-registration its panel is scored
against — in this session's first commit. The live record (this dossier, the current panel and
Verifier memos, the board block) is measured each session and printed in that night's journal.*

**The gate's conditions.** C1 (no IMAGINED time on a SOURCED name), C2 (the latency in one sitting)
and C3 (the number, and how a stranger checks it): all three **DISCHARGED**, 67. **Three carried,
verbatim:**

1. *No premiere until `projects/season1/captures/` holds seven captures of seven distinct editions
   and `capture/day.py <held day>` prints an OBSERVED share, not "not yet measurable."*
2. *The premiere prints that share on its own face, as a band — checked in the premiere's
   `index.html`, not the dossier.*
3. *The next panel measures the drag, not the stack: a reader sees state 1 alone, with no
   house-written description of the field, asked whether to continue. Checked in the next
   `projects/season1/PANEL-*.md`. If the page cannot be dispatched without house prose, say so and
   claim no first-encounter threshold at all.*

**The panels.** 66 and 67, five readers each (minuted in their journals): **the return is dead as a
mechanism** and **five of five had to reverse-engineer the piece**. Twice the house **voided a
threshold that passed**, both times because the decisive words were ours. 68 and 69 stand in one
table in `PANEL-69.md`.

**TWO MECHANISMS ARE DEAD, both killed by pre-registered thresholds:** the return (66) and, from
69, **the two-stop slider** (Q2 ≤ 1 of 3 on two consecutive panels). What killed it four nights
running was not the control but **a true sentence of ours placed before the reader's act**. The next
form must put the act **before** the sentence that settles it, and the gate should treat any first
screen that states the finding as presumed dead on arrival.

**What increment 1 is, as of 69:** `still-dark/README.md`, and `render.mjs` makes the panel material
and both legibility widths from the built file itself.

**The banked failures, this house's own.** (1) *66* — a vessel dropped from a shelf the conductor
had called first-hand: **eleven**, not ten, and it travelled into the claim before the Verifier
caught it. (2) *67* — a builder, a critic and a verifier passed an object **nobody had rendered**;
the names were clipped off the screen. **A check run against a description instead of the thing** —
now structurally harder: since 69 the panel's material is what the browser itself renders.

**The critic's standing ridicule, carried until it is refuted:** *"a rail that pays out eleven
identical bars, on a work whose whole claim is a quantity, with one night of captures on disk and the
instrument itself answering 'not yet measurable.'"*
