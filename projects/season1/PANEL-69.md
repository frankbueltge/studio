# PANEL-69 — STILL DARK, increment 1, state 1 REBUILT

**The re-run of the K3 panel.** Three new severed readers, given
`projects/season1/still-dark/STATE-1.txt` and nothing else. Dispatch and all four questions
**verbatim** from `git show 1e84436:…/DRAMATURG-68.md` §B; thresholds and the escalation clause from
`DRAMATURG-69.md` §D (`git show 6dd04f4:projects/season1/DRAMATURG-69.md`), fixed before the rebuild was built. **The void clause did not fire:**
`STATE-1.txt` is now made mechanically by `still-dark/render.mjs` — the browser's own `innerText`
plus the control's own label and value, no editorial word of ours; run against last night's build it
reproduces panel 68's material **byte for byte** (md5 `e4014c75…`). What these readers saw:
`STATE-1.txt` md5 **`8d57c7948bc8e2000220521e8f03c9fa`**, `index.html` md5
**`4d598e571f2e6dcb276b3485aedad41a`** — nothing was edited after they saw it.

## The numbers

| | threshold, pre-registered | session 68 | tonight |
|---|---|---|---|
| **Q1** what does this page show | 2 of 3 name ships dark **and** one named day | PASS 3/3 | **PASS 2 of 3** (A, C). B named the ships and the dark/return dates but no held day |
| **Q2** would you move the control | 3 of 3 "move" | **FAIL 0/3** | **FAIL, 1 of 3** (A moved; B and C stopped) |
| **Q3** what would change | 2 of 3 say what is *known* / the record changes | NOT PASSED 1/3 | **PASS 3 of 3** |
| **Q4** measured vs worked out | 2 of 3 place the count **11** as measured, the bands as worked out, **and do not call `56 d dark` derived** | **FAIL 0/3** | **PASS 2 of 3** (A, C) |

## What was fixed, and it is measurable

**The label no longer misdirects.** Q3 1 → **3 of 3**: nobody thought the day moves, all three said
the *record* grows. (`record as it stood on:` → `drag — this adds the next edition this house
captured; the day itself does not move.`) **The OBSERVED tier reads.** Q4 0 → **2 of 3**: both
passing readers put the count 11 with the timestamps and hashes as this house's measurement, and
**none of the three called `56 d dark` derived** — the tightened clause held, and the column header
did what the footer legend could not. **The ending is no longer given away:** the ceiling sentence
and `100%` are gone from state 1, two blanks stand there, and not one reader said they already knew
what moving the control would do.

## Why it still failed, and it is our sentence again

Both readers who stopped stopped on **one line of ours in the footer**:

> `2026-08-05T19:17:55Z (HTTP 200, 35,485 bytes, same sha256 — the same edition, byte for byte).`

Reader B: *"since this house has only captured one edition of the underlying page so far (5 Aug's
fetch was identical to 4 Aug's, byte-for-byte), moving it would show me the same single data point
again."* Reader C: *"the text notes two of the three captures share the same sha256… implying
little or no change."* The line is true — a night that added nothing, printed, which is exactly
what a work about publication latency owes its reader. Placed at state 1 without naming **which**
edition each capture carries, it reads as *nothing changed*, and a reader who believes that has no
reason to move.

**This is the fourth night running.** A caption (66), a dispatch (67), a methodological sentence
(68), and now an evidence line (69): four different true sentences of ours, each removing the
reader's reason to act before they act. The defect is not the wording. **This house keeps putting
its finding in front of its form.**

**One thing the panel could not see** (the Verifier's, `VERIFIER-69.md` defect 1, disclosed here
too): `STATE-1.txt` is clean of the share and the three names — **the file is not**, and view-source
at state 1 reaches everything the turn withholds. The result is unaffected, every reader received
only what the page renders; but **state 1 is a state of the reading, not of the file**, and no
document said so until tonight.

## Standing — the escalation fires

Q2 at ≤ 1 for the **second** consecutive panel. Under the clause pre-registered in
`DRAMATURG-69.md` §D before tonight's build existed, **the two-stop slider is retired as a
mechanism** — as the return was retired in session 66. It is not restaged a third time.

Retired is the *mechanism*, not the finding: the number, the day-addressed record, the capture chain
and the tier legibility survive it. **Nothing was changed after the readers saw it — the fix is
owed, not made.**
