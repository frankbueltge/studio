# VERIFIER 78 — 2026-08-08 — facts and tiers only, published unedited

Convened because new SOURCED material reached the face tonight (a fifth list, three vessels)
and because this session published a correction to a claim of its own. It judges facts and
tiers only and has no vote on form. It was asked to be adversarial and to check the repair
of banked failure 17 for being *differently* wrong rather than right. Verbatim:

---

All checks are complete and independently verified against the raw capture JSON, `git log`/`git show`, and the live scripts (not just trusting `data.py`'s own output). Here is the memo.

**D1 — SUPERSEDED row. PASS.**
Evidence: `git log -1 --format=%cI 91ee19b` → `2026-08-06T08:36:39+00:00`. `python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-06T08:36:39Z` → `5 capture(s) read, 3 distinct edition(s) … 69%–100% (11 of 0–16)`. Independently listing every capture's `fetch.fetched_at_utc` shows exactly 5 files at or before 08:16:42Z and the 6th (14:22:17Z) falls after the instant — confirming 5 copies / 3 editions is correct for that moment.
String checked: `"SUPERSEDED · as this page published it at 08:36 UTC on 6 August, from 5 saved copies of 3 lists — 69 %–100 %, 11 of 0–16"`. This matches. The prior defect is real and independently confirmed via `git log --all -p -- STATE-1.txt`, which shows a committed ancestor (`8b8e777`, the current HEAD commit) reading `"...from 8 saved copies of 3 lists —"` for this same 08:36 UTC claim — 3 too many. The working tree (uncommitted) has since corrected it to 5, and 5 is what the record and `day.py --as-of` both support. Repair is correct, not merely differently wrong.

**D2 — LIVE row. PASS.**
Evidence: `python3 projects/season1/capture/day.py 2026-08-04` (no `--as-of`, i.e. now) → `12 capture(s) read, 5 distinct edition(s) … 55%–100% (11 of 0–20)`.
String checked: `"LIVE · as this record measures it now, from 12 saved copies of 5 lists — 55 %–100 %, 11 of 0–20"`. Matches exactly.

**D3 — "It fell fourteen points…" sentence. PASS.**
Fall: then-lo 69% − now-lo 55% = 14 points → "fourteen points" correct.
Attribution, checked independently against raw capture JSON (not `data.py`): WANGBIAO-8730 first appears in the capture with `edition_date_printed = "7 August 2026"` (fetched 2026-08-07T18:15:53Z) → 7 Aug − 4 Aug = 3 days → "three days after the day," correct. TUNA PESCA, SAPPHIRE III, MONTECELO all first appear in the capture with `edition_date_printed = "8 August 2026"` (fetched 2026-08-08T21:37:19Z) → 4 days → "four days after the day," correct. These four names are exactly the set difference between the as-of-91ee19b list (16 names) and the current list (20 names) — "four ships this record did not hold when the law below was printed" is correct.
String checked: `"It fell fourteen points. What grew was the total: WANGBIAO-8730 with the list of 7 AUG, three days after the day; and TUNA PESCA, SAPPHIRE III and MONTECELO with the list of 8 AUG, four days after the day — four ships this record did not hold when the law below was printed."` Confirmed correct.

**D4 — Time-field rows, all 20 ships checked (not just 4). PASS.**
Ran an independent script (bypassing `data.py`/`day.py` entirely) that re-derives, from the raw `captures/*.json` alone, each vessel's first-sighting capture, name, flag, days_dark, waters (including the TUNAMAR case-of-the-day prose-recovery), and its group by first edition date. All 20 rows matched the face exactly, e.g.: TUNAMAR/PAN/56/Ecuadorian EEZ (Galapagos)/group "4 AUG"; ALTAR 10/ECU/18/Ecuadorian EEZ (Galapagos)/group "5 AUG"; BONAMI/KOR/22/Marshallese EEZ/group "6 AUG"; WANGBIAO-8730/CHN/19/Tuvaluan EEZ/group "7 AUG"; SAPPHIRE III/USA/27/United States EEZ (Hawaii)/group "8 AUG". Band text (`dark X–Y → back A–B`) recomputed by hand for TUNAMAR and MONTECELO also matched verbatim.

**D5 — This house's own working-nights/counts. PASS.**
The OBSERVED ledger table (fetched time, status, bytes, body sha256, content sha256, edition, ship count for all 12 captures) was recomputed independently using `edition.content_sha256` against the raw files and matches the face row-for-row, byte-for-byte, hash-prefix-for-hash-prefix. The caption "Two lists came back in more than one set of bytes each…" is correct: editions "5 August 2026" and "6 August 2026" each show two distinct `fetch.sha256` values sharing one `content_sha256` — exactly two lists, matching "Two."

**D6 — Points vs. bands / tier-blur / unsupported time attribution. PASS, nothing found.**
- `python3 projects/season1/still-dark/data.py --check` → `island matches the captures` — the committed JSON island backing the face is byte-identical to a fresh computation from the captures right now.
- Every share on the face is printed as a band ("69 %–100 %", "55 %–100 %"), never as a point; every "of N–M" denominator is a band, never a single figure.
- The band sentence ("Twenty ships could have been dark… not one of them certainly… written 0–20… share runs from 11 of 20 to 11 of 11") was hand-recomputed from `bands()`/`band_line()` logic and the live capture's `method.window_days = 7` ("week-wide window") — correct.
- No vessel on the face carries a time that isn't either a raw SOURCED field or a DERIVED band with both ends printed (`dark X–Y → back A–B`), and every "first seen" date traces to a real `fetch.fetched_at_utc` in a committed capture.
- No hidden `title=`/`alt=`/`meta` text carries additional undisclosed claims.

**Overall: no false or unsupported claim found.** The one known prior defect (D1's "8 saved copies" error, still visible in the last commit `8b8e777` via `git log -p`) has been correctly repaired in the current working tree to "5 saved copies of 3 lists," and that repair is verified correct against both `git show 91ee19b` and an independent `day.py --as-of` recomputation — not merely differently wrong.

---

## What the session did with it

**Nothing was changed on the face on this memo, because it ordered nothing changed.** It is
recorded for two things the session cannot claim for itself: that the repair of failure 17
was checked by something other than the hand that made it, and that all twenty rows were
re-derived from the raw captures by a route that does not pass through `data.py` at all —
the first time the face's rows have been checked without using the code that built them.
