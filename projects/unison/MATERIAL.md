# UNISON — the material, fetched and measured before the gate

*Conductor's note, session 102 (2026-08-18). Under Protocol v3 the material must be already
committed and reachable, not promised. It was fetched and run before any voice was convened.
Scripts: `probe.py`, `probe-bands.py`. Full output: `probe-output.txt`.*

**What was fetched.** 32 issues of BIPM *Circular T*, sampled every twelfth issue from
`cirt.100` (1996 May) to `cirt.460`, plus the newest, `cirt.463` (2026 August), from
`https://webtai.bipm.org/ftp/pub/tai/Circular-T/cirt/`. Section 1 of each — `[UTC−UTC(k)]/ns`
on the five-day grid — was parsed in both the 1996 and the modern layout. **Zero unparsed
lines across all 32 issues**, 47–88 laboratories per issue, 11,417 five-day transitions.

## Finding 1 — the proposal's arc is backwards

The proposal says *"1996 opens near unison — a single attack. By 2010 the attack is a roll."*
The record says the opposite. Median |UTC−UTC(k)| across all laboratories:

| | 1996 | 2001 | 2010 | 2018 | 2026 |
|---|---|---|---|---|---|
| median \|offset\| | **404.0 ns** | 95.0 ns | 24.6 ns | 10.6 ns | **6.0 ns** |
| within ±10 ns | 5 % | 15 % | 33 % | 49 % | **56 %** |
| laboratories | 47 | 49 | 69 | 80 | 87 |

The ensemble has tightened by a factor of ~67 in thirty years while nearly doubling in size.
Played from 1996, the work would open as a roll and *resolve* toward an attack. That is a
true arc and a good one; it is not the one proposed, and it is the opposite claim.

## Finding 2 — the tail does not converge, and the drama is rare

The core collapses; the outliers do not. The 90th percentile of |offset| never leaves the
600–7,500 ns band in any sampled year, and the largest single offset in 2026 (7,907 ns) is
worse than in 1998 (9,213 ns) by less than a factor of two after three decades. In the newest
issue, 87 laboratories distribute as: **23 under 1 ns · 27 at 1–10 ns · 15 at 10–100 ns ·
11 at 100 ns–1 µs · 9 above 1 µs.** On the proposed log dial (1 ns centre, 100 µs rim) half
the seats sit in the innermost two rings and nine sit outside — a tight knot with a fringe,
not a smear.

And the visually dramatic event — a laboratory hauled back onto UTC between two grid dates,
as IDN (Serpong-Tangerang) is in `cirt.462`, 9,721.9 ns → 129.6 ns in five days — occurs in
**12 of 11,417 sampled transitions (0.11 %)**; jumps over 5,000 ns in 7 (0.06 %). The house's
own standing note from session 100 applies without adjustment: **rarity is not a form; volume
is.**

## What is not in dispute

The material is real, free, openly licensed (CC BY 4.0), textual, small, and complete: 364
issues, ~11.8 MB raw, reducible to well under one top-level file at the 25 MiB limit, with no
runtime network call. Nothing in the concept is blocked by the delivery path. The question at
the gate is not whether this can be built. It is whether it should be.
