# VERIFIER — session 73

**VERDICT: NO DEFECTS FOUND**

## What was checked and held

1. **`data.py --check`** — `cd projects/season1/still-dark && python3 data.py --check`
   → `island matches the captures`, exit 0. The committed data island is a computed,
   not typed, artifact of the current capture set.

2. **The lede's three numbers.** `word(n_obs)`=eleven, `word(n_hi-n_obs)`=five,
   `word(len(gained))`=two, all read live off `analyse()` — confirmed by re-running
   `python3 projects/season1/capture/day.py 2026-08-04` (matches the printed block
   exactly) and by inspecting `data.py` lines 232–249. "Eleven stood in the list dated
   4 August itself" is `knowable_on_the_day_OBSERVED`, i.e. vessels in an edition dated
   ≤ the held day — not a claim about when that edition was *published*. "Five arrived
   later" = 16−11. "Two of them after this page had printed its figure" = vessels
   gained between `PRIOR_AS_OF` (2026-08-06T04:36:19Z, a real capture) and now; those
   two (ALBACORA CUATRO, BONAMI) entered via the 08:16:42Z capture, which post-dates
   the struck-figure commit's own timestamp (04:57:03Z) — checked against
   `git log -1 --format=%cI 5968048` = `2026-08-06T04:57:03+00:00`. No "published on
   the day itself" language, or any publication-instant claim about the upstream list,
   is present anywhere on the face (`grep` of index.html/STATE-1.txt).

3. **TUNAMAR waters.** The capture that first carried TUNAMAR
   (`captures/2026-08-05T043932Z.json`) has `case_of_the_day.prose` ending "…, in
   Ecuadorian EEZ (Galapagos)." — an exact, verbatim match to the string now on the
   face. `waters_index()` in `data.py` and the mirrored parser change in `capture.py`
   only read this trailing clause; no committed capture's `waters` field was edited
   (`git diff --stat -- projects/season1/captures/` shows only the new, untracked
   2026-08-06T164335Z.json; a per-file `git diff --quiet` loop over every existing
   capture shows zero modified). The value is upstream's own words with only a
   mechanical cut, so it correctly sits in SOURCED under the legend's own definition
   ("name · flag · days dark · waters — printed by the instrument").

4. **Tonight's new capture** (`2026-08-06T164335Z.json`, 7 vessels, edition
   2026-08-06, body sha f673e2f7…, content sha 53114dfe… — identical to the two prior
   2026-08-06 captures). Every dependent figure moved with it and was checked against
   an independent Python tally of the capture directory: 7 captures / 3 editions
   ("7 saved copies of 3 lists"), ledger table gained the new row, "4 distinct
   bod(y/ies)" unchanged (its body hash repeats an existing one). The printed command
   block is the true output of `day.py 2026-08-04` run just now.

5. **Legend line.** "DERIVED the dark-and-return spans — worked out here, printed
   with both ends" (index.html / STATE-1.txt) — accurate: the page's other dates
   (instrument edition dates, OBSERVED fetch times) are not claimed as derived
   anywhere on the face.

6. **Struck figure and its date.** `git log -1 --format=%cI 5968048` =
   2026-08-06T04:57:03+00:00 = 04:57 UTC on 6 August, matching the face exactly.
   `git show 5968048:projects/season1/still-dark/index.html` carries the quoted law
   verbatim ("A ceiling that can only fall. A further night can add a ship to a past
   day...") and the then-current figures (79 %–100 %, 11 of 0–14, 4 captures/2
   editions) that the face now marks as struck.

7. **Restraint language intact**: "'Intentional' is a machine estimate by Global
   Fishing Watch — a probability, not proof; the instrument makes no claim of
   illegality against any vessel or state, and neither do we" — unchanged, present at
   equal prominence (STATE-1.txt last line).

8. **chronicle.json / SITE-API.md / chronicle-check.py.** `"conditions"` is in the
   published enum (`SITE-API.md` line 73: `pass|fail|conditions|graduated|discarded|
   deferred|null`). `python3 toolchain/chronicle-check.py` →
   "72 entries, all valid against the published contract" (exit 0). `git diff
   chronicle.json` shows only the verdict field changed, `""` → `"conditions"`; the
   summary text is untouched and its claims (69–100 %, 11 of 0–16, the Q1 refutation
   at 2 of 3, the four Verifier defects, the 2,991→4,250→2,994 word-count correction)
   all check against `journal/2026-08-06-session-72.md` and the two consolidation
   commits (`e826290`, `d7bbb2c`).

## Not my remit

- Whether `"conditions"` is the *best* word for session 72's outcome versus `"fail"`
  is a characterization/tone judgment, not a fact defect. For the record: house usage
  of `"conditions"` (32 of 72 entries, the most common verdict after `"pass"`) is
  consistently applied to sessions with an outstanding, pre-registered item still
  owed — which matches session 72's shape (3 of 4 thresholds held, the fourth refuted
  and its repair explicitly deferred to the next round, same-night defects corrected
  before landing). I did not find this inconsistent with the record, but I flag that
  I am not the tier to adjudicate the word's aptness, only its enum membership and
  factual fit — both check out.
- Wording, staging, and layout of tonight's changes: no comment, outside remit.
