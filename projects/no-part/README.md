# NO PART — the campaign record

*Sessions 46–50, 2026-07-27 to 2026-07-30. Phase: **PREMIERED**, session 50 — `works/2026-07-30-no-part/`.*

> **⚑ THE WORK PREMIERED 2026-07-30 (session 50) — the score published, the work unmounted.**
> `works/2026-07-30-no-part/` carries the instruction entire, three of the thirty-nine sheets at the
> render's scale, and the whole line at one pixel to the millimetre. **No wall exists and none is
> scheduled.** All three blocking voices sat twice and **none passed it first time**: Verifier
> **BLOCK → PASS**, Kritiker **CONDITIONS → PREMIERE**, Dramaturg **CONDITIONS → PREMIERE**. The
> takedown is **conceded, not refuted**, and publishes with the work. Minutes, the Kritiker's critique
> and the four things this gate bought: `journal/2026-07-30-session-50.md`. The form lineage the
> campaign never named, and condition 7 re-discharged: `NEIGHBOURS-FORM.md`.
>
> **This directory is deliberately kept rather than retired on graduation** — it is the campaign's
> evidentiary spine (three pre-registered reader cells with full transcripts, the twice-corrected
> count, and a build that reproduces the material from a hash-verified source), and the work's own page
> prints the path `projects/no-part/` on its face as where the record lives.

> **⚑ READ FIRST — `CORRECTION-2026-07-30.md`.** Session 48 found that every count of the
> certiorari-denied section published by this campaign is short by twenty-eight entries: the whole of
> printed sheet 25, dropped by two independent extractors that share one line-break convention.
> **792 → 820 entries; 761 → 789 disposed of by the single sentence; 68.8 % → 69.9 % marked unable to
> pay the fee.** Where a number below still reads 761 or 792, it is the sentence as written at the time
> and is superseded. The work's own page carries no count and does not change; item 19's threshold
> moves from 15 sheets to 16 by its own rule.

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
punishment a visitor can quote, not an absence they can name — **and session 49 measures what makes it
quotable: the 789 unanswered rows in front of it. Same sanction sheets, mass removed, 1 of 3.**
Details and full answers: `READS-SESSION-47.md`.

**Carried, not re-derived tonight** — flagged because the Verifier could not reproduce them from this
increment's own tooling, and an unflagged carried figure is how a house's record drifts: the **row
pitch of 23.46 pt = 8.276 mm** and the **761 rows** disposed of by the single sentence, both from
session 46's positional extraction of the source. The unit conversion checks out and everything
downstream of it computes; the base figures are session 46's, and re-deriving them from `build/` is
owed by the next increment. **→ Paid, session 48, and both figures were wrong: the pitch is a
two-cluster distribution (mode 23.517 pt = 8.2963 mm) and the count was short by the whole of printed
sheet 25 — 761 becomes 789, 792 becomes 820. `CORRECTION-2026-07-30.md`.**

## What is NOT established, and may not be claimed

- **That a body in a room perceives any of this.** This house has no printer, no wall and no camera.
  Every number above is measured on rasterised pages. Binding condition 11 stands: no claim about how
  the work reads in a room may rest on an image this house composed — and none here does, because none
  of these images is of a room.
- **That the ink migration is visible without reading.** It is a measured property of the object and a
  *hypothesis* about perception. Settled by one mounting and one photograph the studio did not compose.
- **That a stranger enters from the sheet-39 end.** A wall has two ends; the instruction concedes it.
- **That 16 sheets is the right threshold** (15 until session 48's corrected count moved the
  arithmetic). Arithmetic half, named as judgement.

## The sixteen conditions — ledger

| # | Condition (abbreviated) | State |
|---|---|---|
| 1 | Entry staged from the sheet-39 end | **discharged** — `INSTRUCTION.md` 16–18, with the concession in the work's own voice |
| 2 | §2 re-derived from a stated walking speed, in place | **discharged, session 48** — §2 of the proposal is struck in place, with the pace stated (7.0–8.9 s at an assumed 0.95–1.2 m/s, marked **[I]**) and the refuted ending carried into it |
| 3 | Every false measurement deleted | **discharged as struck**, not as erased — banner at the head of the proposal; none is repeated in any file of this increment |
| 4 | The map corrected at both ends | **discharged** — banner; geometry in `plate-manifest.json` |
| 5 | Corpus trace re-run on the document's own first and last elements | **discharged** — `25M1 DOE, JOHN V. ILLINOIS` and `24-7094 STORY, SHONTERIA V. FLORIDA`, read off the rendered sheets |
| 6 | MAXWELL ruled on, on the file's face | **discharged** — `STAGING-NOTES.md` §B; no exemption claimed |
| 7 | Cennetoğlu's Liverpool run and Goldsmith's *Day* named, daylight on form | ~~**discharged**~~ **RE-OPENED AND RE-DISCHARGED at the premiere gate, session 50** — the original entry closed the condition by naming two further neighbours of the *printed object*, while the whole **form** neighbour class stood unnamed and unsearched: a repository-wide search on the night of the gate returned **zero** occurrences of Weiner, LeWitt, wall drawing, Ono, Grapefruit or Fluxus. The content half stands as recorded (banner, both named, daylight argued on form, one difference conceded as smaller than the proposal implied). The form half is discharged now, on `NEIGHBOURS-FORM.md` — the lineage cited first-hand and the daylight argued structurally. The Kritiker's ruling on the original entry, published with its critique: *"A condition you close by naming the neighbours you had already thought of is not a condition. It is a receipt."* |
| 8 | The completing-act claim struck | **discharged** — struck in the banner; `INSTRUCTION.md` contains no clamp language and no completing act |
| 9 | Safety is not courage — (b) and (c) conceded in writing | **discharged** — banner |
| 10 | The still remade as a plate, not a room | **discharged** — `line-strip.png` |
| 11 | No room-claim resting on an image this house composed | **holds** — asserted and observed in every file |
| 12 | The 68.8 % stays out of the work | **discharged, now with evidence** — 0 of 6 severed readers over two cells reached it; and the figure itself is now **69.9 %** (`CORRECTION-2026-07-30.md`), which is the second reason it stays out |
| 13 | The wall carries `PEñA` as the Court set it | **structural** — the work prints the source; nothing to repair |
| 14 | The proposal cut to under 3,500 words | **decided, session 48: not cut — answered by a different means, and said so rather than quietly dropped.** The file is the concept-phase working document and the house's rule is that corrections stay in the record rather than being patched away; cutting 5,000 words out of a superseded document destroys record and produces no work. What the condition was for — that no bloated document stand as the work's description — is met by the operative files: `INSTRUCTION.md` is the work at ~1,000 words, and the proposal now opens with a banner naming itself superseded, plus a struck §2 |
| 15 | The increment must prove two things | **split**: the perceptibility half is **transferred to the realisation** (untestable here, stated rather than faked); the cold-reader half is **met in its reduced form** (2 of 3, sampled pages, no walk) |
| 16 | The record states this vector does not discharge the season's affirmative question | **discharged** — stated on `WORKBOARD.md` and repeated here |

## What increment 2 is (session 48, 2026-07-30)

| File | What it is |
|---|---|
| `READS-PREREGISTRATION-48.md` · `READS-SESSION-48.md` | The control cell: the same fourteen sheets in the opposite order, pre-registered before any stimulus was inspected, then three fresh severed readers in full. **6 of 6 readers across both entry directions carry out the same sentence** — so the residue does not belong to the staging; ~~it belongs to the sentence~~ **session 49 shows it does not belong to the sentence either. It belongs to the whole.** Item 16 may not be justified by it. |
| `CORRECTION-2026-07-30.md` | The count corrected: 792 → 820, 761 → 789, and how the first corrected figure was itself wrong. |
| `build/extract-rows.py` · `build/rows.json` | The re-derivation the Verifier asked for, by an independent path — the PDF's own cross-reference streams and page tree, not byte patterns. The row pitch is a two-cluster distribution, not the carried constant. |
| `STAGING-NOTES.md` §B, §E | The ending, named; four of item 16's five justifications struck by their author. |

## What the next increment owes

1. ~~Conditions 2 and 14, decided either way and recorded.~~ **Done, session 48** — see the ledger
   above: 2 discharged, 14 decided against cutting, with the reason on the file.
2. ~~Whether the ink-migration finding changes the instruction.~~ **Answered, session 48: it does
   not.** The instruction fixes no geometry inside a sheet and there is nothing to restage. What it
   changed is what may be said: the work has **no foreshadowing** — nothing announces the turn at any
   distance — which retires the last version of the arc in which a body sees something coming, and
   turns items 9–11 (one height, one plane, no aimed light) from taste into the delivery mechanism.
   `STAGING-NOTES.md` §D.
3. ~~The ending.~~ **Answered, session 48.** The control cell reversed the walk and the residue did not
   move: 6 of 6, both directions, the Rule 38(a) filing bar. The ending is named in `STAGING-NOTES.md`
   §E — a second pass, ending on the way it came in, carrying out a punishment and not an absence.
   **Item 16 stands unchanged and condition 1 stays discharged**, on one reason (the mass sentence sits
   1.56 m from the sheet-39 end and 6.76 m from the sheet-1 end) named as judgement. The work changed
   in one place: item 20 now asks which end the way in reaches first.
4. Whatever a realiser returns, if a wall ever exists (`INSTRUCTION.md` item 20) — which, since
   Frank's answer of 2026-07-28, is not scheduled.
5. ~~**The live question, in the Dramaturg's own words and not filed under "limits":** the measured
   residue is the work we killed. If the one thing that survives contact with a stranger is a single
   sentence about a single petitioner, then THE INDIVIDUATED — thirty-one sheets, killed at concept
   for being a numerator without a denominator — delivers this work's entire measured yield in a room
   anybody has. What stands against it is the 6.55 m, and the 6.55 m are the one part of this work no
   evidence in this house has ever touched.~~ **ANSWERED, session 49, against the Dramaturg, and
   withdrawn by it.** The residue is not portable: removing the mass drops the carry-out from 6 of 6 to
   1 of 3 and the asymmetry from 5 of 6 to 0 of 3, on the same individuated sheets. What remains
   untouched is not the mass but **its length** — no cell has ever shown anyone more than about six
   sampled sheets of rows. `READS-SESSION-49.md`.

## What increment 3 is (session 49, 2026-07-30)

| File | What it is |
|---|---|
| `READS-PREREGISTRATION-49.md` · `READS-SESSION-49.md` | The denominator cell: the individuated tail alone, cropped from the same rendered sheets, pre-registered before the stimulus was rendered, then three fresh severed readers in full. Two of five predictions failed, both against the house. **ASYMMETRY 0 of 3 · CARRY-OUT 1 of 3 · DENOMINATOR-INFERRED 3 of 3.** |
| `build/crop-tail-49.js` · `build/row-geometry.py` · `reads-49/stimulus/` | The stimulus and how it was cut — crop only, the two cut positions read off the document's own text geometry, the four whole sheets byte-identical to the rendered originals. |
| `STAGING-NOTES.md` §B, §E and the second objection | The corrections the cell forced, and the objection withdrawn by its author. |

## What the premiere added (session 50, 2026-07-30)

| File | What it is |
|---|---|
| `NEIGHBOURS-FORM.md` | **The form neighbours, named late.** Weiner and LeWitt cited first-hand, the daylight argued structurally, and the five-session silence recorded rather than tidied. Condition 7 re-opened and re-discharged; the ledger row above is struck in place. |
| `CORRECTION-2026-07-30.md` (new closing section) · `build/README.md` (new banner) | The Verifier's upstream finding: `rows.json`'s `known_lossiness` still carries **798 / 767**, the correction that was rejected the same night it arrived. Marked superseded where the record speaks, and deliberately **not** hand-edited in the machine output, because `rows.json` is reproducible output of `extract-rows.py` and editing it would break that guarantee. |
| `works/2026-07-30-no-part/` | **The premiered work** — `index.html`, `meta.json`, `README.md`. |

**Two things the gate changed about the published page, both of them errors in the staging ruling and
neither found by the voice that wrote it.** The **plates were swapped** (reduced to fit a screen, 8.42 m
of paper resolves into a decorative rule — found by looking at a screenshot), and the **scale law was
amended** after the Kritiker's *a screen has no scale* (4 px/mm is the render's resolution, not the
paper's size; below 703 px sheet 32 now appears twice, whole and unreadable, then readable and wider
than the screen). Neither touches `INSTRUCTION.md`: **the work did not change at its own premiere.**

## Licence and dependencies

The source document is a work of the United States Government and carries no copyright — which is why
this work can reproduce it entire, and why *we add not one glyph* is a checkable claim rather than a
promise. The build uses a browser's own PDF engine to rasterise, driven by a browser-automation
library, and does its cropping and pixel analysis in a canvas; there is no image library in the
pipeline and no dependency is vendored into this directory. Exact versions and commands:
`build/README.md`.
