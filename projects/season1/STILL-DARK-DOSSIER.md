# STILL DARK — concept dossier

**Season 1 — Counter-Measurement, Episode 7/7.** Gate: opened with three conditions,
session 66 (`KRITIKER-GATE-66.md`). This dossier is the project's standing record; it is
written to discharge **condition C3** and to hold the arc. *Tier: SOURCED throughout, with a
DERIVED layer whose uncertainty is printed and an OBSERVED layer that is this house's own
record of itself. No VERIFIED-tier claim appears — nothing here draws on a sibling practice.
No IMAGINED element is in the work.*

## 1. The work, in one page

The lab's own instrument **The Ghost Fleet** (`https://frankbueltge.de/ghost-fleet/`) publishes
daily the ships that switched off their AIS transponder on purpose. Its method sheet
(`https://frankbueltge.de/werke/ghost-fleet/`, fetched 2026-08-04, 200) states the window
verbatim: *"Daily. Window: disabling events that ended in the last 7 days (complete
vanish-and-return stories)."* A disappearance therefore enters the record **only when the ship
comes back**. A vessel dark for 56 days is missing from the record for all 56 of them.

So a calendar day of the sea is almost empty on the day itself, and keeps filling for weeks
afterwards. STILL DARK holds one calendar day open and publishes how much of that day's darkness
was knowable on the day itself.

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

run over the capture files committed in `projects/season1/captures/`. Every capture carries the
URL, the UTC fetch time, the HTTP status, the byte count and the **sha256 of the raw body**, so a
stranger can re-fetch the page themselves, hash it, and see whether our parse belongs to those
bytes. `capture.py` is the fetcher; `day.py` is the instrument. Both are ~200 lines and read.

This number exists in no dataset. Upstream publishes a list of **endings**; nobody — upstream
included — keeps a **day-addressed** record of when each ending became knowable. The captures are
that record.

## 3. The three layers, and the line between them

| layer | what it is | example |
|---|---|---|
| **SOURCED** | printed on the page: vessel name, flag, days dark, waters, edition date, aggregates, Global Fishing Watch id | `TUNAMAR (PAN), 56 days, Ecuadorian EEZ (Galapagos)` |
| **DERIVED** | arithmetic on SOURCED, uncertainty carried | an edition holds events that ended within 7 days of its date, so TUNAMAR resurfaced somewhere in **2026-07-28 – 2026-08-04** and went dark somewhere in **2026-06-02 – 2026-06-09** |
| **OBSERVED** | this house's own captures: the first capture naming a vessel is the moment we could first know of it | `first_seen_utc: 2026-08-05T04:39:32Z` |

**Condition C1 is discharged structurally, not by care:** no invented time can be attached to a
vessel name, because no code path produces one. A vessel's timing is either derived from its
published duration — and then it is a band, printed at both ends — or observed from a committed
capture. Session 66's `+2d` stamps have no successor.

## 4. The state of the measurement, honestly

**Night 1 is committed** (`captures/2026-08-05T043932Z.json`): status 200, 35,473 bytes,
sha256 `ed3e54ec…1336e5`, **eleven** named vessels, edition **4 August 2026**.

Two things this house measured tonight and will not overstate:

1. At **04:39 UTC on 5 August 2026** the live page still carried the **4 August** edition,
   byte-identical to the fetch of the night before. That is an observation about publication
   timing, not a fault, and we assert nothing about why.
2. The **OBSERVED** share cannot yet be computed for any past day: our record begins tonight. The
   instrument says so and **refuses to substitute the DERIVED share in its place** — the substitution
   would be exactly the blur the work exists to refuse. The DERIVED share for every day we can reach
   is currently **0 knowable of 2–11 dark**.

## 5. The forward record (amendment rule 3, the ambition audit)

STILL DARK promises, by premiere: one calendar day held open across **at least the seven nights of
its cited window**, publishing the measured share of that day's vessel-days of darkness knowable on
the day itself, checkable against our committed captures. **Below that — a single-sitting screen
with seeded times — is a failed forecast, and the gate has put its own name to it.**

## 6. Neighbours, daylight, takedown

Nearest neighbours and the daylight from them: `ARTIST-66.md` §3 (the Ghost Fleet itself; Paglen,
*The Other Night Sky*; Watch the Med). **The published takedown, which ships with the work whatever
becomes of it:** *"A studio watched a website update for a month and called its own patience a
measurement."* The refutation is the number in §2 — patience produces a figure that is checkable
against a committed, hashed record, or the takedown stands.

**The weakest joint, the Artist's own and confirmed from outside by four of five severed readers:**
a method that counts a disappearance only when the ship returns **cannot see the ships that never
return**. The work inherits that blindness and must print it, not solve it.
