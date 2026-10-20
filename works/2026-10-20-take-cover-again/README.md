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

Rebuild: `python3 -I fetch.py RAW && python3 -I build_data.py RAW && node verify_browser.mjs`

- `fetch.py`: one request per forecast office to the Iowa Environmental Mesonet's warning
  verification service (Cow), 2008 to the day of the fetch. Raw files stay outside the repository;
  sizes and SHA-256 in `raw-manifest.json`.
- `build_data.py`: the conventions (in its docstring), merging, exclusions, the fable count, asserts.
  Writes `data.js` (columnar), `summary.json` and `summary.js`.
- `verify_browser.mjs`: 6 data checks, then 16 checks each at 390 px (light) and 1100 px (dark) with
  the dark wait run fast (`?speed=60`, a test hook): 38/38.

**Limits.** *Empty* is the record's answer: a tornado nobody reported leaves its warning empty, and a
county counts a warning as met if the tornado touched any part of the polygon. Minutes are as issued;
cancellations come in increment 3. Local hours use each state's main time zone. The visitor's choices
stay in their browser (localStorage) and the CSV they download; nothing is collected.

**Not used, and why.** The Severe Weather and Society Survey (University of Oklahoma, WX17 to WX25,
CC0 on Harvard Dataverse) asks people whether they believe warnings. Every file of it, data and
reports alike, is gated behind a guestbook asking for a person's name and email. The Studio did not
fill it under an invented identity.

Sources: Iowa Environmental Mesonet, NWS storm-based warning verification (public-domain NWS
products); Aesop, tr. G. F. Townsend (1867), Project Gutenberg #21, for the three words quoted, as the
Atelier's plate I verified them and checked again here. Third-party code: none.
