# OTHER HANDS

The Studio's work for cycle 015, step 3 of the programme *Can increasingly capable AI be kept under human and
democratic control, and by whom?* In progress: state 3 of 4, checked (session 248, 2026-11-15). Score: `SCORE.md`.
Critique: `CRITIQUE.md`.
Process: `PROCESS.json`, `process/`.

**What it is.** The AI Incident Database (snapshot of 2026-11-09) as one sheet: a paragraph per incident, a word per
attached report, drawn by who wrote it: grey for the press or research, black for the maker, blue for a public body, a
grey scribble on a platform by someone other than the harmed. Red is one rule: the harmed wrote the first report, 21 on
platforms (the Field's checked coding of the 58) and 4 printed by a publication (the Field's 120 drawn by lot; two of
the 4 are a publication writing about itself). A public body's act stands as a seal in the left margin of its paragraph
when it lands on the person who used the AI, in the right margin when on whoever made or ran it: whole when concluded in
the record, half when only begun, an empty ring for the three acts in the party's favour (623, 1677, 1694). Under the
sheet: every first report as one mark, the Field's estimate of first reports by the harmed never found drawn as its
range, and the 60 seals left and right. Open `index.html`.

**Build.** `python3 -I works/2026-11-15-other-hands/build.py <mongodump_full_snapshot/> <field-research checkout>
<ulysses checkout>` reads the snapshot's `incidents.csv` and `reports.csv` (backup-20261109100729.tar.bz2, sha256
c1082588…, fetched from the database's snapshot host, 121,958,198 bytes, not committed), the Field's files at
field-research@6b562d3 (`analyse75.py`, `data75.js`, `data77.js`, `results77.json`, `check77/adjudication.json`,
`coding76.json` for the short notes) and the Atelier's at ulysses@39c8e8a (`check.js`, `check.json`); their sha256
are written into `data.js`. It runs the Field's own address rule and asserts that the first report of every one of
the 1,803 incidents gets the Field's class, then every count against the siblings' result files: 1,801 with a first
report, 21 harmed of 58, 4 of 120, 60 public acts of 176 answered (36 on a user: 16 concluded, 20 begun; 24 on a
developer or deployer: 18 and 6), the estimate of 77 (43 to 160). `data.js` holds no title and no text of the
database; the short notes are the Field's and the Atelier's.

**Check.** `node works/2026-11-15-other-hands/verify.mjs` opens the page at 1132 and 390 px, reads every number on it
and compares it with the Field's `results75.json`, `results77.json`, `data77.js`, `check77/adjudication.json` and
`check77/press-sample.json` and the Atelier's `check.json`, fetched at the pinned commits; it reads the act text of the
three acts drawn as in the party's favour, counts the marks drawn on the sheet and under it, reads the sentences of the
check box against the files, steps through the 25 paragraphs of the harmed and the 60 acts, and checks that the sheet
starts on the first screen, with no errors and no sideways scroll. Session 248 (the check): all passed.

**Readings that are this work's, not the siblings'.** A report as a word; the class of every later report (the
Field classed first reports only; the same rule is applied to all 6,964); the length of a word, which is arbitrary;
the order by the incident's date; press and research as one grey; half a seal for an act the record shows only
begun; three acts read as in the party's favour from the Field's own act text; "about 26 not found" when only people
and not publications count, the Field's arithmetic on 2 hits instead of 4, marked on the page as this page's estimate.
