# VERIFIER 79 — 2026-08-09 — facts and tiers only

Checks D1–D5 as charged. Facts and tiers only; no vote on form, staging, wording or taste;
no changes proposed to the work's design. Every figure below was re-derived independently —
against `captures/*.json`, `git log`, and `capture/day.py`/`capture/edition.py` run directly —
not read off `data.py`'s own say-so, except where D2 explicitly asks for `data.py --check`'s
own verdict.

---

## D1 — Tonight's two saved copies

Both new files (`2026-08-08T235735Z.json`, `2026-08-09T000053Z.json`) parse as valid JSON with
the same top-level key set as the immediately preceding capture of the same edition
(`2026-08-08T213719Z.json`): `capture_version, fetch, method, edition_date_printed,
edition_date, case_of_the_day, aggregates, vessels, derived_intervals, page_assets, tiers,
content_sha256`. Diffing each new file against `2026-08-08T213719Z.json` with `fetch.fetched_at_utc`
stripped shows **zero differences** — both are byte-identical copies of that capture except for
their own fetch timestamp:
```
diff <(...213719... minus fetched_at_utc) <(...235735... minus fetched_at_utc)   -> exit 0
diff <(...235735... minus fetched_at_utc) <(...000053... minus fetched_at_utc)   -> exit 0
```
Total capture count: `ls projects/season1/captures/*.json | wc -l` → **14**.
Distinct lists (`content_sha256`, computed via `edition.content_sha256` over all 14 files):
**5** — `{4 Aug, 5 Aug, 6 Aug, 7 Aug, 8 Aug}` editions, unchanged from before tonight.
Distinct raw bodies: 7 (unchanged reasoning: two editions — 5 Aug and 6 Aug — each have 2 body
hashes; tonight's two captures both carry the *same* body hash `4110d2b0…` already on record).

`python3 capture/day.py 2026-08-04` (run directly, no `--as-of`) confirms:
```
day 2026-08-04  ·  14 capture(s) read, 5 distinct edition(s), 5 distinct content(s), 7 distinct bod(y/ies)
  vessels dark on that day .......... 0–20 (certain–possible)
  knowable on the day, OBSERVED ..... 11
  SHARE knowable on the day ......... 55%–100%  (11 of 0–20)
```
This is identical to the share reported before tonight (55%–100%, 11 of 0–20, 5 lists) — the
share did not move.

**Tonight added zero new lists.** Both captures are additional saved copies of the existing
8‑August list (already on record since session 78's 21:37:19Z capture) — copies only, not a
sixth list.

**D1: PASS.**

---

## D2 — The face agrees with the record

`python3 data.py --check` was run in `projects/season1/still-dark/`:
```
$ python3 data.py --check
ISLAND DIFFERS from the captures
exit 1
```
This is a **FAIL of the documented self-check**, not a rumour — reproduced directly. Diffing a
fresh `build()` against the JSON actually embedded in `index.html` (structural diff, not text
diff) isolates the entire disagreement to exactly one thing, repeated once per block:
```
MISSING IN COMMITTED: .field[0].seen_all
MISSING IN COMMITTED: .field[1].seen_all
MISSING IN COMMITTED: .field[2].seen_all
MISSING IN COMMITTED: .field[3].seen_all
MISSING IN COMMITTED: .field[4].seen_all
```
`data.py`'s `build()` now unconditionally emits `"seen_all": seen_all(rows) if CUTS else None`
for every block (added this session, for D3's `--cuts` feature). The committed `index.html` was
last written by `--write` *before* that key existed in the build — it has `"count"` immediately
followed by `"rows"` with no `seen_all` key at all, in all five field blocks. This is schema
drift between the committed data island and the current `data.py`: the island in the work right
now is not what a fresh run of the script that is supposed to have sole authorship of it
produces. It carries no wrong number (the missing key's value would have been `null`, and the
front-end's `if (g.seen_all)` treats absent and `null` identically, so nothing on the rendered
face is visibly wrong) — but the script's own stated purpose is "re-running the script is how
anyone checks that the page belongs to the record," and right now that check does not pass.

Independently of `--check`, every number actually printed on the face (`STATE-1.txt`) was
re-derived and confirmed true of the captures:

- **Saved copies / lists**: 14 saved copies, 5 lists — confirmed under D1.
- **Ledger's 14 rows**: every `fetched_at_utc / http_status / bytes / sha256-prefix / vessels`
  value in the printed table was checked file-by-file against all 14 capture JSONs (script:
  loop over `captures/*.json`, print the same five fields) — all 14 rows match exactly,
  including the two new rows (`23:57:35Z`, `00:00:53Z`, both `36,059` bytes, `4110d2b0…`, 6
  ships, edition "8 August 2026").
- **LIVE figure**: `capture/day.py 2026-08-04` (direct run) → `55%–100% (11 of 0–20)`, 5
  editions, 14 captures. Matches the face exactly.
- **SUPERSEDED figure, date, and provenance — one anchor, checked**:
  `git log -1 --format=%cI 91ee19b` → `2026-08-06T08:36:39+00:00`. That is 08:36 UTC on
  6 August — the date and time printed. `capture/day.py 2026-08-04 --as-of
  2026-08-06T08:36:39Z` (the exact instant read off that same commit, nothing typed) →
  `5 capture(s) read, 3 distinct edition(s) … 69%–100% (11 of 0–16)`. All three —
  date, figure, and the "5 saved copies of 3 lists" provenance — trace to the *same* commit
  and the *same* re-derived instant, closing banked failure 17 (which had the date, the
  figure and the copy-count naming three different moments). They now agree because they are
  read from one place: `data.py`'s `commit_time(PUBLISHED_COMMIT)`, not three separate
  constants.
- **Per-block ship counts**: `capture/day.py 2026-08-04 --json`, grouped by `first_edition_date`
  independently, gives block sizes 11 / 3 / 2 / 1 / 3 (dates 4/5/6/7/8 Aug), sum 20 — matches
  the face's `(11 ships)/(3 ships)/(2 ships)/(1 ship)/(3 ships)` and the printed `0–20` band
  exactly, vessel names and order (by descending `days_dark`) also matching row for row.

**Verdict: FAIL.** The numbers printed on the face are all independently true of the captures —
but the check the session was charged with running, `python3 data.py --check`, does not pass
right now, because the committed `index.html`'s data island was not regenerated with `--write`
after `data.py`'s `build()` gained the `seen_all` key. The face and the record agree in
substance; the file that is supposed to prove that mechanically does not currently say so.

---

## D3 — The staged cut did not lose an observed fact

Independently regrouped all 20 vessels by `first_edition_date` and pulled each one's own
`first_seen_utc[:10]` from `capture.day.index()` (not from `data.py`), block by block:

| block (edition) | rows | distinct first-seen dates in the record |
|---|---|---|
| 4 Aug | 11 | `{2026-08-05}` |
| 5 Aug | 3 | `{2026-08-05}` |
| 6 Aug | 2 | `{2026-08-06}` |
| 7 Aug | 1 | `{2026-08-07}` |
| 8 Aug | 3 | `{2026-08-08}` |

Every block is internally uniform (exactly one date), and matches what every row of that block
carried in the committed page (checked by `grep` over `still-dark/index.html`'s data island:
all 11 four-August rows carry `"first seen 5 AUG"`, all three five-August rows carry
`"first seen 5 AUG"`, both six-August rows carry `"first seen 6 AUG"`, the one seven-August row
carries `"first seen 7 AUG"`, all three eight-August rows carry `"first seen 8 AUG"`).

The arm's hoisted sentences, read from `staging-79/cut/STATE-1.txt`:
- "this page first saw all eleven on 5 AUG" (11-row block) — matches the shared date, 5 AUG.
- "this page first saw all three on 5 AUG" (3-row block) — matches.
- "this page first saw all two on 6 AUG" (2-row block) — matches.
- "this page first saw it on 7 AUG" (1-row block, singular form) — matches.
- "this page first saw all three on 8 AUG" (3-row block) — matches.

No block's hoisted sentence states a date any row of that block did not carry in the committed
page, and no row's own OBSERVED first-seen fact is altered: the arm's data island rows
(`git diff` of `still-dark/index.html` vs `staging-79/cut/index.html`) show each row's other
fields (name, flag, days_dark, waters, band_text, gfw_url) unchanged, only `"seen"` emptied to
`""` — the date itself is not lost, it now lives once in the block header instead of eleven/
three/two/one/three times in the rows, and it is the same date.

**The guard.** Read `seen_all()` in `data.py`:
```python
def seen_all(rows):
    dates = {r["seen"] for r in rows}
    if len(dates) != 1:
        return None
    ...
```
Tested directly:
```
>>> seen_all([{'seen':'first seen 5 AUG'}, {'seen':'first seen 5 AUG'}])
'this page first saw all two on 5 AUG'
>>> seen_all([{'seen':'first seen 5 AUG'}, {'seen':'first seen 6 AUG'}])
None
```
Confirmed: a block whose rows carried different dates would collapse `dates` to a set of size 2,
`seen_all` returns `None`, and in `build()` the line `"seen_all": seen_all(rows) if CUTS else
None` prints nothing for that block while `"rows": [dict(r, seen="") if CUTS and seen_all(rows)
else r for r in rows]` — with `seen_all(rows)` falsy — leaves every row's own `"seen"` text
intact. The hoist is in fact refused when dates differ, not merely claimed to be. (All five of
tonight's real blocks happen to be uniform, so the refusal path is not exercised on this
capture set, but the code was independently exercised above and does what it says.)

**D3: PASS.**

---

## D4 — The reorder moved markup and nothing else

`git diff --no-index projects/season1/still-dark/index.html projects/season1/staging-79/cut/index.html`
was inspected line by line, whole diff quoted below in substance. The only hunks are:

1. **The data island** — each of the 5 field blocks gains a `"seen_all": "..."` key (with the
   text checked under D3), and each row's `"seen"` value changes from `"first seen N AUG"` to
   `""`. No other key in any row (name, flag, days_dark, waters, went_dark_between,
   resurfaced_between, band_text, gfw_url) is touched.
2. **The reorder** — inside `<section class="sd-evidence">`, the block
   `<p id="sd-ledger-cap">` + `<div id="sd-ledger">` (plus its DRAMATURG-76 comment) moves from
   after `<p id="sd-cmds">` + `<div class="sd-raw">` to before it. No sentence, attribute,
   class, or id is added, removed, or reworded anywhere in this hunk — the two blocks are
   moved as units, verbatim, past each other.

Nothing else differs: no CSS rule, no `<script>` logic, no other section's markup, no other
sentence anywhere in the file. (The CSS/JS support for rendering `seen_all` — the
`.sd-seen-all` rule and the `if (g.seen_all)` branch — exists identically in *both* files
already, since `index.html` is written to render both shapes; it therefore does not appear in
this diff at all, matching `data.py`'s own comment that "the arm and the work differ in their
data island and in no line of code" for the `--cuts` question — plus this one additional,
also-markup-only reorder.)

Tier check: both the ledger's caption (`sd-ledger-cap`) and the ledger table (`sd-ledger`)
remain inside the same `<section class="sd-evidence">` as before; neither acquires nor loses a
class that would move it between SOURCED / DERIVED / OBSERVED presentation. The caption element
still immediately precedes its own table element in document order in the arm (`sd-ledger-cap`
then `sd-ledger`) — it moved *with* its table, not away from it — so it still stands above the
table it corrects.

**D4: PASS.**

---

## D5 — Anything false or blurred

Read both `still-dark/STATE-1.txt` and `staging-79/cut/STATE-1.txt` as a hostile checker,
cross-checking every number against independent recomputation (`day.py`, `edition.py`, `git
log`, direct file inspection — see D1–D4 above for the underlying arithmetic):

- Every share is printed as a band (`69 %–100 %`, `55 %–100 %`), never collapsed to a point.
- Every "of N–M" denominator is a band, never a bare single figure.
- "Twenty ships could have been dark … and not one of them certainly" — checked against
  `day.py --json`: `certain: 0`, `possible: 20` for 2026-08-04. Correct; there genuinely are
  zero certain vessels, all 20 are possible-only.
- "It fell fourteen points" — `round(69) - round(55) = 14`. Correct, and it only fires when
  `drop > 0` (branches to "It has not moved since." otherwise) — not a static claim.
- The lede's four counts (eleven / nine / four) all independently reproduce from `day.py`
  (`knowable_on_the_day_OBSERVED = 11`, `band[1] - 11 = 9`, `len(gained) = 4`).
- No SOURCED field (name, flag, days dark, waters) appears anywhere dressed as DERIVED or
  OBSERVED, or vice versa; the legend at the top of both pages states the three tiers plainly
  and the body respects it — `band_text` (DERIVED, both ends printed) is never asserted as a
  single point, and `"first seen …"` / `"this page first saw …"` (OBSERVED) never stands in for
  a SOURCED or DERIVED value.
- The `--cuts` STATE-1.txt (`cut/`) is otherwise textually identical to the committed one except
  for the five hoisted sentences (verified true, D3) and the reordering of the ledger above the
  terminal block (verified markup-only, D4) — it makes no additional claim the committed page
  does not also make.
- The SUPERSEDED row's date/figure/provenance triple was independently checked to trace to one
  commit (D2) — no longer three moments.

**No false claim, no unsupported number, and no tier-blur was found in either `STATE-1.txt`.**
The one defect surfaced this session is not a false sentence on the face — it is the process
fact under D2: `data.py --check` currently fails because the committed data island predates the
`seen_all` key `build()` now always emits. That is a record-hygiene FAIL, not a face FAIL.

**D5: PASS** (nothing false or blurred found on the two faces read).

---

## Overall

| Check | Verdict |
|---|---|
| D1 — tonight's two saved copies | **PASS** |
| D2 — the face agrees with the record | **FAIL** — `python3 data.py --check` reports `ISLAND DIFFERS from the captures` (exit 1) right now; the committed `index.html` data island is missing the `seen_all` key `build()` now always emits, because it was not rewritten with `--write` after that key was added. Every individual number printed on the face was independently re-derived and is true of the captures — this is a self-check/process failure, not a wrong number on the face. |
| D3 — staged cut lost no observed fact | **PASS** |
| D4 — the reorder moved markup and nothing else | **PASS** |
| D5 — anything false or blurred | **PASS**, nothing found |

**Action implied by D2's failure**: run `python3 data.py --write` in `projects/season1/still-dark/`
to bring the committed island back into agreement with the current `build()`, then re-run
`python3 data.py --check` and confirm it reports `island matches the captures` before this
session is banked as clean. That step was not taken by this Verifier — the Verifier checks
facts and tiers, it does not fix the work.
