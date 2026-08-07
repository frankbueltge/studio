# VERIFIER-73 — STILL DARK, session 73

**CLEAN** — no defect found.

## Noted, not a defect

`PROJECT.md:90` still carries *"Also owed: TUNAMAR's waters, dropped by the parser from the case-of-the-day block."* That is now discharged on the object. The file is untouched this session; it falls to consolidation. Flagged so it is not carried forward as still owed.

## What was checked, and how

**The seventh capture is real.** I fetched `https://frankbueltge.de/ghost-fleet/` live: 35,517 bytes, sha256 `f673e2f7…` — byte-identical to `captures/2026-08-06T152800Z.json`'s recorded fetch. That capture differs from the 14:22 one in `fetched_at_utc` alone. `git status` and `git diff --stat` show **no committed capture modified**; the new file is the only addition to `captures/`.

**Every count that should have moved, moved.** `capture/edition.py` → 7 captures, 3 editions, 3 contents, 4 bodies. `day.py 2026-08-04` → 0–16, 11 knowable, 69 %–100 %. `--as-of 2026-08-06T04:36:19Z` → 4 copies, 2 lists, 79 %–100 %, 11 of 0–14. All four figures stand on the face verbatim (`STATE-1.txt:133–138, 151–156`). `data.py --check` exits 0: the island is a byte-equal rebuild from the captures, so lede, waters, ledger and counts are all computed. No stale "6" survives in `index.html` or `STATE-1.txt`. `index.html`'s diff is 13/4 lines, entirely inside the island.

**The lede's two namings are computed.** `data.py:216–219` builds them from `printed_date(DAY)` and the new `day_month(DAY)`; `DAY = "2026-08-04"` is the day `day.py` holds and the day the headline prints. Nothing typed into the sentence.

**TUNAMAR's waters are SOURCED, and only that.** The 4 August capture's `case_of_the_day.prose` ends *"…, in Ecuadorian EEZ (Galapagos)."*; `case_waters()` returns that string unaltered — no part inferred. I confirmed upstream's mechanism against live bytes: the case of the day is printed once, as prose, with no list row and no waters column. The warrant in `edition.py:83–92` is exactly as stated and no larger — MICRONESIA103 is a 4 August list row reading "Marshallese EEZ" and the 5/6 August case with prose ending "in Marshallese EEZ"; one vessel, and the comment says so and declines to assert the two fields share a referent. The row prints in the ordinary cell under a legend that claims only *"printed by the instrument"* — supported. **Latent, not live:** `index()` would now accept waters from a later capture than a vessel's first sighting; today every vessel's waters come from its own first-sighting capture.

**Rendered, not just extracted.** I opened both PNGs. The 4 AUG rule label is whole at 1400 and 900 (session 72's clipping is gone); TUNAMAR's waters, the two namings, and the seven-row ledger are all visible on the page itself.

**Self-quotation and restraint.** `git show 5968048` — 2026-08-06 04:57:03 UTC, quote verbatim, 4 captures in tree; the face's "04:57 UTC… commit 5968048" and "4 saved copies of 2 lists" both hold. The method quote matches the captures verbatim. The "intentional"/no-illegality sentences stand on the face and in both READMEs.

**chronicle.json:** one line changed, `""` → `"fail"`; entry has all six keys and "fail" is in `SITE-API.md:73`'s enum. Honest per `journal/2026-08-06-session-72.md`: one of four pre-registered thresholds refuted, four Verifier defects — and 69/70 used "fail" on the same shape.

---

**CONDUCTOR'S NOTE, appended after the pass and changing nothing it cleared.** Both items above are
**entered as owed, not repaired tonight**: a code change made after a clean pass, in the file the
pass just cleared, is the improvisation this house bans in its staging and it has no better claim
here. The latent path is `PROJECT.md`'s owed item (c); the stale line is corrected tonight.
