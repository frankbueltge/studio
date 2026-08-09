# VERIFIER 80 — 2026-08-09 — facts and tiers on the running head

Convened because a new element went onto the face and it carries counts, a tier stamp and
an instruction a stranger is told to run. Facts and tiers only; **no vote on form**. The
memo below is the Verifier's own, condensed by the conductor only where it repeats a table
already in this file; **both defects are quoted in the Verifier's words and neither was
softened.** The verdict was **BLOCKED**.

## What passed

- **D1 — the data island matches a fresh build from the captures.** `data.py --check` exits
  0. Session 79's banked failure 19 is not repeated.
- **D2, first half — every figure in the head holds.** The Verifier re-derived all five
  stop totals, every per-stop name and every `days_after` **from the capture JSON with its
  own script, not with `day.py`**, and got 11 / 14 / 16 / 17 / 20 and the same names in the
  same stops, *"identical to the island, name for name."*
- **D3, the uncertainty handling — clean, and it was attacked.** The subject reads *SHIPS
  THE LISTS PUT INTO 4 AUGUST 2026*, not *dark on*, so no certainty the body retracts. The
  gloss's *"not one of these names is certainly dark on this day"* branches on the computed
  certain end, and the Verifier confirmed that end is nought **at every one of the five
  stops**, not only the last — so the sentence is true at all five frames. *"counting the
  lists up to …"* is the accumulation and is never attributed to one list. No claim of
  intent or illegality anywhere in the head.
- **D4 — renders belong to their pages.** All six `RENDERS.json` verify; the five staging
  copies hash identically to the committed `index.html`, as `STAGING-80.md` claims.
- **D5 — `render.mjs --at-step` does what its comment says, proved by making it fail five
  ways.** Out-of-range high, out-of-range low, non-numeric, non-integer, and a page with no
  running head: exit 1 each, **no outputs written into the failing directory**. The five
  step texts show 11 / 14 / 16 / 17 / 20 with the right names — *"the flag genuinely drives
  the head, it is not photographing one state five times."*
- **D6 — standing instruments pass.** `SELFTEST PASSED`; `gaps.mjs` PASS, 20 of 20 rows at
  both widths.
- **D7 — nothing else false or invented.** No head figure is hand-typed; `stage80.py` reads
  the stop count off the island. `STAGING-80.md` verifies UNMOVED against its 04:48:51Z
  freeze and its description matches what is on disk.

## DEFECT 1 (blocking) — the head printed a command that reproduced none of its five stops

> `--as-of` compares against `fetch.fetched_at_utc`, not the edition date, and every edition
> is captured the *following* day. Substituting the stop dates the head itself prints on its
> buttons: **zero of five stops check out — two exit non-zero, three silently return the
> previous stop's total.** This is not fixable by shifting the date a day: edition 4 AUG and
> edition 5 AUG were both captured on 5 August, so **no date-only argument can ever isolate
> stop 0.**

Secondary, same line: even with the right instant, `day.py` prints the count as a band, and
a stranger told to check the head's bare `11` *"gets a band, and must know to read its
upper end. The instruction does not say so."*

**This is the sharpest defect of the night**, and not because it is subtle. This work's
published refutation of its own takedown is *the number is checkable against a committed,
hashed record* — and the first thing the new head did was put a command on the face that
checked nothing. **Both severed readers had already named that exact line** as a developer
note (`PANEL-80.md` Q4, 2 of 2); they were right about it for a reason neither of them and
neither of us could see.

**REPAIRED, at the root.** The command is now **per stop and its argument is an instant**,
read off the captures and never typed, so what a stranger is told to run always reproduces
the state they are looking at; and the line names **which line of the output to read and
which end of its band**, with the certain end a computed branch. Re-checked end to end after
the repair, all five: `0–11 · 0–14 · 0–16 · 0–17 · 0–20`, upper end equal to the count on
the face at that stop.

## DEFECT 2 (blocking) — an unqualified OBSERVED stamp over a DERIVED-gated set

> Which list first carried a name is OBSERVED — true. But **which names are in the set at
> all is not.** Membership in 4 August 2026 comes entirely from the derived return band…
> The head's counts are a DERIVED gate with an OBSERVED grouping, carrying a single
> unqualified OBSERVED mark — and by the block's own argument it stands *above* the legend,
> so a stranger gets the stamp with no key. **The gloss carries the derivation's
> *uncertainty* but the tier line does not carry its *tier*.**

**REPAIRED.** The head's tier line now names both, the gate first: *DERIVED — whether a name
belongs to this day at all… so every count here is a possible and not a certain. OBSERVED —
which saved copy first carried each name.*

**Recorded rather than explained away:** the block was written with a comment claiming
*"Tier: OBSERVED throughout … never a derivation."* This house wrote the right uncertainty
into the head's gloss on the same night, and still stamped the wrong tier one line below it.

## Note (b), adopted rather than argued with

> The head names 20 vessels with flags and stands entirely above the page's closing
> restraint. In the **staged material actually dispatched to readers**, truncated at the
> head, it does not exist at all: five images and five texts naming twenty vessels and flags
> **with no upstream caveat attached.**

**Adopted.** The restraint is now one constant feeding both the head and the foot, so the
two cannot drift, and it travels with the names wherever the head is truncated. **Session
80's readers received the material without it**, and that is on this record, not repaired
out of it.

## What the readers were shown, stated plainly

`PANEL-80.md`'s two readers read the head **carrying both defects**. Neither defect touches
Q1 or Q3 — the mechanism and the count are what those questions measure, and both defects
are in the provenance line below them. **Q4 is a different matter: both readers named that
line, and the line was false.** The answers stand as given; nothing is rescored.
