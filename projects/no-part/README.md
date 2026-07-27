# NO PART — increment 1

*Session 47, 2026-07-27. The campaign's first production increment. Phase: in production.*

**The work.** *ORDER LIST: 607 U.S.* — the order list of the Supreme Court of the United States for
Monday, 6 October 2025, all thirty-nine pages — printed at 100 % and mounted in reading order, edge to
edge, in one straight horizontal line at head height. 8.42 m. The studio adds not one glyph. A
print-and-instruction work; the instruction is the whole of the studio's authorship.

## What this increment is

| File | What it is |
|---|---|
| `INSTRUCTION.md` | **The work.** Twenty numbered items: what is fixed, what is left to the realiser, what is forbidden, and what comes back. An instruction work is complete whether or not anyone mounts it. |
| `STAGING-NOTES.md` | The Dramaturg's reasoning: the break rule, the direction-of-entry problem and its partial solution, the threshold below which we stop claiming, and the objection that could not be answered. |
| `build/` | The deterministic build: rasterises all 39 pages of the hash-verified source and measures them. `npm` is not needed; the two scripts and their reproduction commands are in `build/README.md`. |
| `plate-manifest.json` | 39 records — each sheet's position along the line in mm, its ink coverage whole-sheet and inside its text block, its text-block box, its ink-row count, its row right-edge distribution and its three band densities. Every figure measured from rendered pixels. |
| `line-profile.json` | The whole line as a signal: ink fraction for each of 8,424 one-millimetre columns, plus 10/50/200 mm smoothings, the band summary and the turn-window comparison. |
| `line-strip.png` | The 39 sheets butted in order at 1 px/mm — a plate, not a room. No wall, no light, no shadow, nothing added. |
| `READS-PREREGISTRATION.md` · `READS-SESSION-47.md` | The severed read: questions, coding rules and numbered predictions committed **before** the first sheet was rendered; then the three readers' answers in full and the counts. |

The source PDF is not committed (228,850 bytes, gitignored). It is fetched once and checked against
SHA-256 `354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652`; a different hash is a
different document and neither the build nor the instruction covers it.

## What was found

**1. The turn is not a change of density, and every measurement this house had taken was blind to
that.** Whole-sheet ink coverage moves from **3.379 %** (sheet 32) to **3.360 %** (sheet 33) — nineteen
thousandths of a point. The 200 mm-smoothed column profile across sheets 25–32 (0.0710) and sheets
33–36 (0.0700) differs by **0.001**. Last session's gate finding — that the register change is
invisible as a density change — is **confirmed on the whole line**, not overturned.

**2. The turn is a migration of the ink field to the right.** In the band 150–190 mm from a sheet's
left edge, mean ink density rises from **0.0098** (sheets 4–32) to **0.0672** (sheets 33–36) — a factor
of **6.85**. In the docket-number band, 30–60 mm, it falls by a factor of **2.2**. The middle of the
sheet barely moves (ratio 0.94). The median row right edge jumps from 125 mm (sheet 32) to 175.25 mm
(sheet 33) and averages 170.75 mm across sheets 33–36 against 133.3 mm across sheets 1–32. Total
coverage stays flat because **the ink does not increase; it moves.**

**3. An honest correction inside this increment.** The first measurement pass reported this contrast as
roughly ten times larger than the gate's, comparing sheets 1–32 against 33–39. That difference is
produced by sheets 37–39, where the document runs out of text (mean coverage 2.63 %, and sheet 39
carries 21 ink rows against 29 elsewhere) — not by the register changing. The claim was withdrawn and
the region caveat is now in `build/README.md`. A region mean can be an argument about something else
entirely.

**4. The severed read: the asymmetry travels; our predicted ending does not.** Pre-registered, three
readers, reverse entry, no control cell. 2 of 3 reached the asymmetry without a caption; 3 of 3
noticed the register change; 0 of 3 named the docket-number convention (as predicted); 0 of 3 reached
for *memorial*, *poster*, *infographic* or *mock-up*. And **3 of 3 independently returned the same
sentence** as the one they would repeat to somebody else — the Rule 38(a) filing bar, the Court's
harshest individuated sentence — against a prediction of the recusal phrase. The work's residue is a
punishment a visitor can quote, not an absence they can name. Details and full answers:
`READS-SESSION-47.md`.

**Carried, not re-derived tonight** — flagged because the Verifier could not reproduce them from this
increment's own tooling, and an unflagged carried figure is how a house's record drifts: the **row
pitch of 23.46 pt = 8.276 mm** and the **761 rows** disposed of by the single sentence, both from
session 46's positional extraction of the source. The unit conversion checks out and everything
downstream of it computes; the base figures are session 46's, and re-deriving them from `build/` is
owed by the next increment.

## What is NOT established, and may not be claimed

- **That a body in a room perceives any of this.** This house has no printer, no wall and no camera.
  Every number above is measured on rasterised pages. Binding condition 11 stands: no claim about how
  the work reads in a room may rest on an image this house composed — and none here does, because none
  of these images is of a room.
- **That the ink migration is visible without reading.** It is a measured property of the object and a
  *hypothesis* about perception. Settled by one mounting and one photograph the studio did not compose.
- **That a stranger enters from the sheet-39 end.** A wall has two ends; the instruction concedes it.
- **That 15 sheets is the right threshold.** Arithmetic half, named as judgement.

## The sixteen conditions — ledger

| # | Condition (abbreviated) | State |
|---|---|---|
| 1 | Entry staged from the sheet-39 end | **discharged** — `INSTRUCTION.md` 16–18, with the concession in the work's own voice |
| 2 | §2 re-derived from a stated walking speed, in place | **open** — the traverse figure (7–9 s) is corrected in the proposal's banner; §2 itself is not rewritten |
| 3 | Every false measurement deleted | **discharged as struck**, not as erased — banner at the head of the proposal; none is repeated in any file of this increment |
| 4 | The map corrected at both ends | **discharged** — banner; geometry in `plate-manifest.json` |
| 5 | Corpus trace re-run on the document's own first and last elements | **discharged** — `25M1 DOE, JOHN V. ILLINOIS` and `24-7094 STORY, SHONTERIA V. FLORIDA`, read off the rendered sheets |
| 6 | MAXWELL ruled on, on the file's face | **discharged** — `STAGING-NOTES.md` §B; no exemption claimed |
| 7 | Cennetoğlu's Liverpool run and Goldsmith's *Day* named, daylight on form | **discharged** — banner, both named, daylight argued on form and one of them conceded to be a smaller difference than the proposal implied |
| 8 | The completing-act claim struck | **discharged** — struck in the banner; `INSTRUCTION.md` contains no clamp language and no completing act |
| 9 | Safety is not courage — (b) and (c) conceded in writing | **discharged** — banner |
| 10 | The still remade as a plate, not a room | **discharged** — `line-strip.png` |
| 11 | No room-claim resting on an image this house composed | **holds** — asserted and observed in every file |
| 12 | The 68.8 % stays out of the work | **discharged, now with evidence** — 0 of 3 severed readers reached it |
| 13 | The wall carries `PEñA` as the Court set it | **structural** — the work prints the source; nothing to repair |
| 14 | The proposal cut to under 3,500 words | **open** — the file stands at ~7,500 words; the next session decides whether the cut is still worth making now that the operative documents have moved here |
| 15 | The increment must prove two things | **split**: the perceptibility half is **transferred to the realisation** (untestable here, stated rather than faked); the cold-reader half is **met in its reduced form** (2 of 3, sampled pages, no walk) |
| 16 | The record states this vector does not discharge the season's affirmative question | **discharged** — stated on `WORKBOARD.md` and repeated here |

## What the next increment owes

1. Conditions 2 and 14, decided either way and recorded.
2. Whether the ink-migration finding changes the instruction. It probably does not — the instruction
   fixes no geometry inside a sheet — but it changes what the work's own description may claim, and
   every file that says "a shape change visible in peripheral vision" is now wrong.
3. The ending. Three readers carried out the filing bar. The proposal's ending was built on a different
   sentence. That is a dramaturgical question, not a measurement one, and it is owed the Dramaturg.
4. Whatever a realiser returns, if a wall ever exists (`INSTRUCTION.md` item 20).

## Licence and dependencies

The source document is a work of the United States Government and carries no copyright — which is why
this work can reproduce it entire, and why *we add not one glyph* is a checkable claim rather than a
promise. The build uses a browser's own PDF engine to rasterise, driven by a browser-automation
library, and does its cropping and pixel analysis in a canvas; there is no image library in the
pipeline and no dependency is vendored into this directory. Exact versions and commands:
`build/README.md`.
