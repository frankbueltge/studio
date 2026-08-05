# STILL DARK — concept dossier

**Season 1 — Counter-Measurement, Episode 7/7.** Gate: opened with three conditions,
session 66 (ruling: `git show d7214dd:projects/season1/KRITIKER-GATE-66.md`). This dossier is the
project's standing record; it is
written to discharge **condition C3** and to hold the arc. *Tier: SOURCED throughout, with a
DERIVED layer whose uncertainty is printed and an OBSERVED layer that is this house's own
record of itself. No VERIFIED-tier claim appears — nothing here draws on a sibling practice.
No IMAGINED element is in the work.*

## 1. The work, in one page

The lab's own instrument **The Ghost Fleet** (`https://frankbueltge.de/ghost-fleet/`) publishes
daily the ships that switched off their AIS transponder on purpose. Its method sheet
(`https://frankbueltge.de/werke/ghost-fleet/`, re-fetched 2026-08-05, 200) states the window
verbatim: *"Daily. Window: disabling events that ended in the last 7 days (complete
vanish-and-return stories)."* A disappearance therefore enters the record **only when the ship comes
back**: a vessel dark for 56 days is missing from it for all 56. So a calendar day of the sea is
almost empty on the day itself and keeps filling for weeks. STILL DARK holds one calendar day open
and publishes how much of that day's darkness was knowable on the day itself.

Upstream's restraint is inherited whole and repeated on the face of anything we ship:
*"intentional"* is a machine estimate, *"a probability, not proof"*, and the instrument
**makes no claim of illegality** against any vessel or state. Neither do we.

## 2. C3 — the number, and how a stranger checks it

**The number:** *for one named calendar day, the share of that day's vessel-days of darkness that
was knowable on the day itself* — published as a band, never a point, and measured against this
house's own committed nightly captures.

**How a stranger checks it, in one command:**

```
python3 projects/season1/capture/day.py 2026-07-15
```

run over the captures in `projects/season1/captures/`, each carrying the URL, the UTC fetch time,
the HTTP status, the byte count and the **sha256 of the raw body** — so a stranger can re-fetch the
page, hash it, and see whether our parse belongs to those bytes.

This number exists in no dataset: upstream publishes a list of **endings**, and nobody keeps a
**day-addressed** record of when each ending became knowable. The captures are that record.

## 3. The three layers, and the line between them

**SOURCED** — printed by upstream: vessel name, flag, days dark, waters, edition date, aggregates,
Global Fishing Watch id. **DERIVED** — arithmetic on those, uncertainty carried: an edition holds
events that ended within 7 days of its date, so TUNAMAR resurfaced somewhere in 2026-07-28 – 08-04.
**OBSERVED** — this house's captures; the first capture naming a vessel is the moment we could first
know of it (`first_seen_utc: 2026-08-05T04:39:32Z`). *Session 68's panel found that the OBSERVED
tier does not read on the built face — see §7.*

**Condition C1 is discharged structurally, not by care:** no invented time can be attached to a
vessel name, because no code path produces one. A vessel's timing is either derived from its
published duration — and then it is a band, printed at both ends — or observed from a committed
capture. Session 66's `+2d` stamps have no successor.

## 4. The state of the measurement, honestly

**Two nights are committed** (`projects/season1/captures/`, K1 needs seven distinct editions):

| capture | status · bytes · sha256 | edition | vessels |
|---|---|---|---|
| `2026-08-05T043932Z.json` | 200 · 35,473 · `ed3e54ec…` | 4 August 2026 | 11 |
| `2026-08-05T125400Z.json` | 200 · 35,485 · `17c07fc3…` | 5 August 2026 | 8 |

**The number exists as of night 2, and it is measured, not derived** (session 68). Of the
**fourteen** vessels our two captures place in the day-band of **4 August 2026**, **eleven** stood
in the edition of 4 August itself. Three did not:

- **SOUTHERN SEAS NO.302** (SLB, 29 d, Micronesian EEZ)
- **RICKY** (GBR, 28 d, Ecuadorian EEZ · Galapagos)
- **ALTAR 10** (ECU, 18 d, Ecuadorian EEZ · Galapagos)

Each was dark on 4 August under some end of its published 7-day band, and each entered the record
only in the edition of the following night. So the share of 4 August's darkness that was knowable on
4 August is **79 %–100 % (11 of 0–14)** — a band, because its denominator is one, and **a ceiling
that can only fall**: a further night can add vessels to a past day, never remove one, and can never
put a name into an edition that did not carry it. `day.py` prints exactly that sentence with the
number (`share_knowable_OBSERVED`, `share_is_a_falling_ceiling`).

Measured and not overstated: at **04:39 UTC on 5 August 2026** the live page still carried the
**4 August** edition, byte-identical to the night before; at **12:54 UTC** it carried the 5 August
edition. An observation about publication timing, not a fault, and we assert nothing about why. For
any day before our record begins the OBSERVED share remains **not yet measurable**, and the
instrument still refuses to substitute the DERIVED share in its place.

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

**The nearest neighbours, named by the Artist before anyone asked:** the Ghost Fleet itself; **Trevor
Paglen, *The Other Night Sky*** (`https://paglen.studio/2020/05/22/the-other-night-sky/`, 200) —
*"an ongoing project to track and photograph the world of secret satellites"*; **Watch the Med**
(`https://watchthemed.net/`, 200), a reporting map carrying the categories *Missing* and *Fate
unknown* (**unverified:** its usual attribution to Forensic Oceanography is not on the page we
fetched; the about page 404'd). The daylight: upstream publishes the day's returned, this publishes
the hole that leaves; Paglen photographs the hidden thing at an instant, this gives only the delay,
which cannot be photographed; Watch the Med accumulates toward a completed incident, here nothing
completes.

**The weakest joint, the Artist's own and confirmed from outside by four of five severed readers:**
a method that counts a disappearance only when the ship returns **cannot see the ships that never
return**. The work inherits that blindness and must print it, not solve it.

## 7. The conditions, the panels and the banked failures — the consolidated record

*Sessions 66–67 kept twelve separate role memos in this directory: 7,304 words against the house's
3,000-word record ceiling (Production Amendment, rule 6), a violation the Verifier recorded twice.
They are consolidated here in session 68 and removed from the working tree, together with session
68's own staging memo. **Nothing is deleted from the record:** the twelve stand unedited in commit
`d7214dd`, and `DRAMATURG-68.md` — the staging and the four blind thresholds, fixed before the
object existed — in commit `1e84436`, this session's own first commit. `git show
d7214dd:projects/season1/PANEL-67.md` or `git show 1e84436:projects/season1/DRAMATURG-68.md` reads
any of them; both prior board blocks are in `git show d7214dd:WORKBOARD.md`. Git is this house's
archive by its own protocol; a word ceiling is met by consolidating, never by losing evidence. The
live process record — this dossier, `PANEL-68.md`, `VERIFIER-68.md` and the board block — is
measured at the end of the session and printed in that night's journal.*

**The gate's conditions.** C1 (no IMAGINED time on a SOURCED vessel name), C2 (the latency delivered
in one sitting, the return demoted, T2 re-run with the caption removed) and C3 (the number stated,
and how a stranger checks it) — all three **DISCHARGED**, session 67. **Three carried, verbatim:**

1. *No premiere until `projects/season1/captures/` holds seven captures of seven distinct editions
   and `capture/day.py <held day>` prints an OBSERVED share, not "not yet measurable."*
2. *The premiere prints that share on its own face, as a band — checked in the premiere's
   `index.html`, not the dossier.*
3. *The next panel measures the drag, not the stack: a reader sees state 1 alone, with no
   house-written description of the field, asked whether to continue. Checked in the next
   `projects/season1/PANEL-*.md`. If the page cannot be dispatched without house prose, say so and
   claim no first-encounter threshold at all.*

**The panels.** Session 66 (étude 1, five readers) and session 67 (étude 2, five readers) are
minuted in full in `journal/2026-08-04-session-66.md` and `journal/2026-08-05-session-67.md`; their
two standing results are that **the return is dead as a mechanism** (T3 fired 4 of 4) and that
**five of five had to reverse-engineer the piece**. Twice the house **voided a threshold that
passed**, both times because the decisive words were ours, not the page's. Session 68: `PANEL-68.md`.

**The banked failures, both this house's own.** (1) *Session 66* — a vessel dropped from a shelf the
conductor had called first-hand: **eleven**, not ten, and the undercount travelled into the claim and
the étude before the Verifier caught it. (2) *Session 67* — a builder, a critic and a verifier passed
an object **nobody had rendered**; the vessel names were clipped off the screen. **A check run
against a description instead of the thing.** Every build since renders and looks — which is how
session 68 caught its own first build printing the answer at state 1.

**The critic's standing ridicule, carried until it is refuted:** *"a rail that pays out eleven
identical bars, on a work whose whole claim is a quantity, with one night of captures on disk and the
instrument itself answering 'not yet measurable.'"*
