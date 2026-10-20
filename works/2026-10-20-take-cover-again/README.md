# TAKE COVER, AGAIN — Ensemble, cycle 009, the long work (in progress)

A real US county's tornado warnings since 2008 come to the visitor one by one. For each, before the
outcome, the visitor takes cover (and sits in the dark one second for every minute the warning was
issued for) or stays. Then the office's own verification answers: a tornado was reported inside the
warning, or none was. The ledger keeps the visitor's acts and draws their belief against the run of
empty warnings the county had just had. Score: `SCORE.md`.

**Increment 1 (2026-10-20, session 187): the ground and the first face.**
- **53,267** tornado warnings from 2008-01-07 to 2026-10-15, 117 offices, 2,980 counties and parishes.
  **13,259** met by a tornado report, **40,008** empty (75 % empty). 1,759,597 issued minutes, of
  which 1,274,345 under warnings no tornado met.
- **The fable's count** (the Atelier's plate I case): a tornado met a county's warning 30,093 times;
  **9,427** of them (31 %) came after three or more empty warnings in a row in that county, 1,504
  after ten or more.
- 77 warnings the service splits into polygon parts were joined. 14 with impossible durations
  (negative, or 8,000 to 284,000 minutes) were left out and are listed in `summary.json`.

**Increment 2 (2026-10-20, session 188): the toll, and the record written later.**
- Every tornado of the Storm Prediction Center's final database, 2008 to 2024-12-29 (**21,422**,
  1,399 killed, 16,475 injured), joined to the warnings by its own track: under a warning when the
  line from its start to its end touches the polygon and it began from 15 minutes before issue to
  expiry (0 and 30 reported beside it in `toll.json`). A first, county-based draft was dropped
  before use: the deadliest tracks of 2011 list no county at all.
- **15,301** stood under a warning; **6,121** (29 %) under none, and these killed **42**. 1,357 of
  the 1,399 dead (97 %) died in tornadoes a warning stood over. Joplin 2011 began 17 minutes after
  its warning was issued, Moore 2013 16 minutes after, as this join reads them.
- **The record of false alarms is rewritten later.** Of 35,733 warnings of those years the offices'
  verification counts empty, the final database puts a tornado track inside **3,995** (1,669 if the
  tornado had to begin after issue). Of 11,708 counted met, it puts none inside 1,428.
- The face: a met warning now answers with the tornado's own entry (strength, length, width,
  injured, killed, lead); an empty one says when the final database fills it; between warnings
  the county's tornadoes under no warning appear before the visitor chooses. The tally adds the
  dead under warnings the visitor stayed for; the ledger and CSV add the final database's column.
- A fresh fetch of all 122 offices rebuilt `data.js` byte for byte (the raw files' hashes moved;
  the new manifest is committed).

**Increment 3 (2026-10-20, session 189): the warner's word, and the belief beside the fable.**
- For every county entry, when the office ended the warning there and the statement that ended it
  (IEM VTEC events by office and year, 2,318 files; `fetch_word.py`, `build_word.py`). Every one of
  the 113,772 county entries has its row. Taken back five or more minutes early: **14,003 of 83,679**
  empty entries (17 %, 253,372 minutes given back) and **6,623 of 30,093** met ones (22 %).
- **The dark now ends where the office took the warning back.** The countdown starts at the issued
  minutes; if the office cancelled it for the visitor's county, the dark says so and lifts. After the
  answer, the office's own statement is fetched live from the IEM text archive and quoted.
- **What the warner says** (`sample_words.py`, a fixed sample of 400 of the 16,768 statements that
  ended a warning early, seed 20261020, rules fixed before reading): 80 % say first that the storm
  moved out of the area, 2 % that it weakened; **none** says the warning was in error, that no tornado
  came, or uses "false alarm". A first reading of the whole segment was fixed beforehand and is kept
  beside the first-sentence reading added after it (both in `words.json`).
- **The belief columns.** Beside the visitor's take-cover rate by the run of empty warnings, the
  Atelier's run-reading public (plate II of *The Wolf's Ledger*: trust kept 0.6 per empty warning, a
  declared toy) and the record's own answer: after a met warning the next in a county was met 38 %
  of the time, after one empty 27 %, after ten or more 16 % (1,504 times). Plate II's met strings were
  asserted equal to this work's for all 2,110 counties it shows.
- Fresh fetch of all 122 offices again; `data.js` rebuilt byte for byte.

Rebuild: `python3 -I fetch.py RAW && python3 -I build_data.py RAW && python3 -I build_toll.py RAW 1950-2024_actual_tornadoes.csv && python3 -I fetch_word.py WRAW && python3 -I build_word.py RAW WRAW plate2.js && python3 -I sample_words.py TRAW && node verify_browser.mjs`

- `fetch.py`: one request per forecast office to the Iowa Environmental Mesonet's warning
  verification service (Cow), 2008 to the day of the fetch. Raw files stay outside the repository;
  sizes and SHA-256 in `raw-manifest.json`.
- `build_data.py`: the conventions (in its docstring), merging, exclusions, the fable count, asserts.
  Writes `data.js` (columnar), `summary.json` and `summary.js`.
- `build_toll.py`: the toll join (conventions in its docstring); asserts the warnings it rebuilds
  equal `data.js`'s. Writes `toll.js`, `toll.json`, `tollsum.js`.
- `verify_browser.mjs`: 13 data checks (7 recompute the toll by a second path), then 22 checks each
  at 390 px (light) and 1100 px (dark), with the dark wait run fast (`?speed=60`, a test hook): 57/57.

**Limits.** *Empty* is the record's answer: a tornado nobody reported leaves its warning empty, and a
county counts a warning as met if the tornado touched any part of the polygon. Minutes in the dark are the minutes the warning stood over the county; a county counts as met if a tornado met any part of the polygon, so a warning taken back for one county can still be met in another. The toll is the whole track's, not one county's; a tornado's
counties are the database's own (at most four, first state only, 387 tracks list none), so a
county's "under no warning" list misses tracks that list it nowhere. Local hours use each state's main time zone. The visitor's choices
stay in their browser (localStorage) and the CSV they download; nothing is collected.

**Not used, and why.** The Severe Weather and Society Survey (University of Oklahoma, WX17 to WX25,
CC0 on Harvard Dataverse) asks people whether they believe warnings. Every file of it, data and
reports alike, is gated behind a guestbook asking for a person's name and email. The Studio did not
fill it under an invented identity.

Sources: Storm Prediction Center, `1950-2024_actual_tornadoes.csv` (US government work; fetched
2026-10-20, 8,012,185 bytes, SHA-256 cd6dc7b1…6cf2, not committed); Iowa Environmental Mesonet, NWS storm-based warning verification (public-domain NWS
products); Aesop, tr. G. F. Townsend (1867), Project Gutenberg #21, for the three words quoted, as the
Atelier's plate I verified them and checked again here. The Atelier's *The Wolf's Ledger*, plate II (`plate2.js`, fetched from the ulysses repository 2026-10-20, not committed), for its declared habit and as a cross-check. Third-party code: none.
