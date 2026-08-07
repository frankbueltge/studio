# VERIFIER-74 — 2026-08-07

**DEFECTS: 4**, none on the work's face. After the pre-registration was restored,
**D1 is withdrawn; D2–D4 stand and are corrected.**

## The defects

**D1 — WITHDRAWN.** I read `PANEL-74.md` against an indexed `DRAMATURG-74.md` of **five**
questions and two controls, so its Q1–Q6 read as a retired question re-asked. The worktree rules
**six** and three (`git diff --stat`: 118+/85−); against that, PANEL matches question for question.
The memo moved, not the panel.

**D2 — "The four controls held" was false.** LIVE in `PANEL-74.md`, `WORKBOARD.md`. Restored §C:
*"Q1, Q2 and Q4 are the controls … Q3 is not a control."* Both now read three.

**D3 — PANEL's hatch measurement covered 11 of 16 rows, and "crossed" was wrong for those 11.**
LATENT. PANEL: *"the solid segment stops at 1099 … the rule is crossed by the hatching."* Those
eleven are the rows first seen 4 AUG; their hatch ends at **1233.0**, the rule's own left edge — it
abuts, it does not cross. The five later rows hatch past it, to 1248.1 or 1267.1. Corrected.

**D4 — "Every bar sits 2 px from its own label and 5 px from the next" was false.** LIVE in
`PROJECT.md` (owed c), `WORKBOARD.md`. All 16 sit 2.3–2.4 px from their own label; the gap to the
next name is 5.3–5.4 px in **13**, **26.0 px** at the two group breaks, undefined for the last.
Corrected.

## Not checked

- `PANEL-74.md`'s nine reader quotations: the raw answers are not in the repo.
- *"one `render.mjs` run"*: the md5s match; one invocation is unprovable.
- *"four nights running"*: no session→capture map exists.

## How

**Capture 8.** `curl -sS https://frankbueltge.de/ghost-fleet/` → 200, **36071** bytes, sha256
`74f093f7…be1a`: matches the recorded `fetch`. `git status` — prior seven untouched, new one `A`.

**`index()`.** Ran `index()` and `analyse('2026-08-04')` from `git show HEAD:…/day.py` against the new,
over the full record and four `--as-of` slices: **identical dicts, identical key order,
every time.** All 16 rows checked field by field against `first_capture` — **0 bad**.

**The sentence.** `data.py --check` → `island matches the captures`, exit 0. `day.py 2026-08-04` →
band **0–16**, OBSERVED **11**, **69%–100% (11 of 0–16)**. *Sixteen* = `word(band[1])`; *not one of
them certainly* is the `lo == 0` branch on a computed certain-count of 0; *week-wide* is
`method.window_days` = 7 in all eight captures; **11 of 16** = `n/hi`, **11 of 11** = `n/max(lo,n)`.
True, and `fall.band` byte-matches §A's blockquote. `--as-of 2026-08-06T04:36:19Z` → 79%–100%,
11 of 0–14: the struck row.

**Caption.** Computed; bodies per content hash are 2, 2, 1 — two lists, each in more than one set of
bytes. **True.** No "7 saved copies" or "4 distinct bodies" survives on the face or in `README.md`.
`page_assets` moved `TopBar.SLcnmZbT.css` → `Base.BvXYJsAy.css`; 36071−35517 = **554**.

**PANEL's rest.** The four md5s match. HEAD's island `fall.now` = `69 %–100 %` /
`11 of 0–16`: unmoved from 73. `line-through` → one hit, line **267**; `transponder` → 0 in all three
face files; ledger `vessels` 11, 8, 8, 8, 7, 7, 7, 7. Geometry (playwright, 1400 px): TUNAMAR name
**387.7–402.5**, bar **404.9–414.5**, next name **419.9**, rule left **1233** — exact.

**Chronicle**, re-checked after 74 landed: **74 entries**; 74 has six keys, `move` `"build"`, `verdict` `"fail"`; 1–74 contiguous; all moves and verdicts in enum, none empty (54 and 55 omit the
key, permitted).

---

**CONDUCTOR'S NOTE, appended after the pass and changing nothing it measured.** D1's cause is
**failure 13**: the staging memo was rewritten twice while both the readers and this Verifier worked
against it, so the pass compared `PANEL-74.md` against a state the panel was never run on. It
reported the discrepancy correctly and could not have known why. **This pass, not the conductor,
is how the house found that its pre-registration can move.** Two of the three "not checked" are
entered as owed in `PROJECT.md` (f) and (h).
