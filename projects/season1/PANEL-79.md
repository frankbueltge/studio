# PANEL 79 — 2026-08-09 — the raw answers, verbatim and unedited

Four severed readers, two arms, each arm severed again across the render and the
extraction. Every reader answered alone, saw no other reader's answer, revised nothing,
was given ONE arm's material and was told nothing about a second arm, a change, or this
house. Pre-registration frozen before dispatch: `STAGING-79.md`, sha256
`2034a80004e831b8416d8acdcda6cd1927fd02fd3a165e7b4de6b901b770cc12`, sealed
2026-08-09T00:05:05Z, **verified unmoved before these answers were read**.

**Arm STOP's material ends at the lede** — not by instruction but because
`render.mjs --stop-after=#sd-lede` removed everything after it from the rendered document
before the screenshot and the extraction were taken. S1 received a 1400 × 900 image
holding a title, a sub-line and two sentences; S2 received 262 bytes of text.

---

## S1 — arm STOP, sighted (`staging-79/stop/render-1400.png`)

> **Q1:** This page reports on a shipping/vessel-tracking record for August 4, 2026, noting
> how many ships known to have been at sea that day were already listed as of that date
> versus how many were added to the record afterward.
>
> **Q2:** "this record" — it's unclear what tracking system or dataset is being referred to.

## S2 — arm STOP, words only (`staging-79/stop/STATE-1.txt`)

> **Q1:** It's a short note reflecting on how, on 4 August 2026, only part of the full
> picture of ships at sea for that day was actually known/recorded at the time, since many
> arrived and were logged later.
>
> **Q2:** "this record" — the text refers to a record/list of ships that tracks their
> arrival dates, but doesn't say what that record is or where it comes from.

## C1 — arm CUT, sighted (`staging-79/cut/render-1400.png`, `render-900.png`)

> **Q3:** This page tracks fishing vessels that went dark (disabled AIS tracking) around 4
> August 2026, and the share of that day's darkness confirmed as "knowable" has been
> falling as more late-arriving reports get added.
>
> **Q4:** The repeated "SOURCED / DERIVED / OBSERVED" method notes and the raw fetch-log
> table (timestamps, byte counts, sha256 hashes) feel like debug output left in front of
> readers rather than something a general audience needs.
>
> **Q5:** I'd cross-check a few vessel names and dark-period dates against the linked
> source (frankbueltge.de/ghost-fleet/) and compare the listed sha256/content hashes in the
> "OBSERVED" table against the actual saved captures to confirm the page's numbers match
> its own logged data.

## C2 — arm CUT, words only (`staging-79/cut/STATE-1.txt`)

> **Q3:** This page measures how much of one day's "dark fleet" (ships that vanished from
> ship-tracking for 12+ hours, 50+ nautical miles offshore) could actually be known on the
> day itself versus how much only became known later, and that knowable share is falling as
> more ships get added retroactively.
>
> **Q4:** nothing
>
> **Q5:** Check the OBSERVED table of saved copies (fetch timestamps, status codes, byte
> counts, body sha256 hashes) against the live source at
> https://frankbueltge.de/ghost-fleet/, and rerun the cited command (`python3
> projects/season1/capture/day.py 2026-08-04`) to reproduce the counts independently.

---

## The scoring, against the marks frozen before the answers existed

**The severance check first, because it can void the night.** Arm STOP's material contains
no ship name, no percentage, no table and no command, and **neither S1 nor S2 named one**.
Both answers are confined to the 262 bytes they were given. **The instrument is valid, and
it is the first first-encounter measurement in this project's life that is.**

**Q1 — 0 of 2 against a pass mark of 2 of 2. FAILED, exactly as this house predicted in
writing before dispatch.**
- (i) *the mechanism* — **0 of 2.** Neither reader names a transponder, a switch, going
  dark, a disappearance or tracking. Worse than absent: **both readers took the page to be
  about ships that were PRESENT.** S1: *"ships known to have been at sea that day"*. S2:
  *"the full picture of ships at sea"*, and *"many arrived and were logged later"* — read
  as ships arriving, when the sentence means their entries arrived in a list.
- (ii) *the lateness* — **2 of 2.** Both have it, and have it cleanly.
- So the lede transmits the SHAPE of the finding and not its SUBJECT. A stranger leaves the
  first encounter believing this is a page about shipping records, not about ships hiding.

**Q2 — CORROBORATED, 2 of 2.** Both readers, severed and unprompted, named the same
referent — ***"this record"*** — and both named it as the thing they could not resolve.
`DRAMATURG-77.md` §1 named four unearned referents on judgement and put *this record*
first; a real first encounter has now returned one of the four from both senses.

**Q3 — 2 of 2. The finding survives the cut.** Both readers name the share of one day's
darkness knowable on the day itself and both name the direction, unprompted: *"has been
falling"*, *"is falling"*. C2, from words alone, reproduced the instrument's own thresholds.

**Q4 — the hoist ADOPTED, the ledger's move ADOPTED, both on a weak comparison and
published as weak.**
- *The repeated OBSERVED line:* **0 of 2**, against 2 of 4 naming it on the uncut page one
  night ago. Neither reader named the block-level line that replaced it either. **Hoist
  adopted.**
- *The ledger and the terminal block:* **1 of 2**, against 3 of 4 on the uncut page. The
  rule set at most 1 of 2 as adoption. **The move is adopted, deletion does not go to a
  reading tonight, and C1's answer is on the record against it.**
- *Two readers against a four-reader baseline is weak evidence.* It cannot prove a cut; it
  can only fail one, and it failed neither.
- **NEW, and banked rather than acted on:** C1 named the ***SOURCED / DERIVED / OBSERVED***
  legend as debug output — a target no reader had named before, and the same element
  `DRAMATURG-77.md` §2 called *"a key printed above a chart the reader has not seen"*. It
  goes to a later pre-registration. Nothing is cut on one reader.

**Q5 — 2 of 2. The guard holds and the move is not reverted.** Both readers, asked how they
would check the numbers, named things ON the page: the OBSERVED table and the linked source
(C1), the OBSERVED table and the printed command, quoted exactly (C2). The element one
reader would cut as debug output is the element both reached for when asked to doubt the
page. **That tension is the finding of Q4 and Q5 read together, and it is the reason the
ledger was moved and not deleted.**
