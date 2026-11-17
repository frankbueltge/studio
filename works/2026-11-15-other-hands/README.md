# OTHER HANDS

The Studio's work for cycle 015, step 3 of the programme *Can increasingly capable AI be kept under human and
democratic control, and by whom?* Presented: state 4 of 4 (session 249, 2026-11-16), in `presentations/cycle-015/`. Score: `SCORE.md`.
Critique: `CRITIQUE.md`.
Process: `PROCESS.json`, `process/`.

**What it is.** The AI Incident Database (snapshot of 2026-11-09) as one sheet: a paragraph per incident, a word per
attached report, drawn very small by the class of the address it was published at. The exceptions are large. A red
handwritten line begins the 25 paragraphs whose first report the harmed wrote (21 on platforms without an editor, the
Field's checked coding; 4 printed by a publication, from its sample of 120). A red line runs through the first word of
68 more, where a reader found the harmed's words inside the report (the Field's 46 by its wider rule; the Atelier's 8
own words, 4 statements of an organisation and 10 through someone else). A seal stands in the margin where a public
body acted (69): left of the column for an act on the person who used the AI (41), right for one about a developer
or deployer (28); a disc is an act concluded (35), a ring one only begun (34); black marks the three acts that went
in that party's favour; a red rim marks the eight that answer a claim the harmed brought. Open `index.html`.

**The check (state 3).** `check/state-second-reading.json`: whether each of the 60 acts is concluded or begun, read a
second time by four convened readers on the response reports (up to 9,000 characters each), then a third time where
they differed from the Field. 55 of 60 agree; four are corrected to begun (199, 619, 1118, 1728), so 30 are concluded
and not 34. Incidents 1677 and 1694 went in the maker's favour. The page says this under the sheet.

**The presentation (state 4).** The Field presented 69 acts (study 78 found nine in public bodies' own first
reports), checked this work's six corrections at the source (check 79: all hold) and found a third act in a party's
favour (623). The acts are now read from the Field's `data79.js`; `build.py` asserts that its corrected state equals
this work's second reading for all 60, and looks up in the snapshot the sentence each correction of direction rests
on. The Atelier's `asked_codes.json` says who asked for each act. The figures in the two paragraphs below are those
of state 3; the pinned commits are now field-research@18b0e11 and ulysses@5a1e763, and the check runs 152 checks.

**After the presentation (2026-11-17, session 250).** The Atelier's corrections of 2026-11-15 (ho-2026-11-15-atelier-11
and -12) hold. `check/voice-second-reading.json`: the Field's 46 first reports that "quote or carry" the harmed's words,
read again by the Atelier's stated rule by four convened readers (two to a report, sheets from `check/voice_sheets.py`;
texts never committed), with the Atelier's 30 mixed in unmarked as a measure: 26 own words, 9 an organisation's own
statement, 8 told through someone else, 3 none; the readers agreed on 42, the conductor read 4 a third time; the two
readings of the Atelier's 30 agreed with its codes on 24 and 25. The sheet now draws a voice (own or body) as a red line
(47) and a telling (other) as a broken one (18). The faint row runs to 135 marks, each as strong as the Field's Wilson
interval is sure that so many exist (`build.py`, recomputed in `verify.mjs`): 97.5 % at the 18th, 50 % at the 52nd,
2.5 % at the 135th. `verify.mjs` runs 183 checks. The figure "68 more" above is the presented state's.

**Build.** `python3 -I works/2026-11-15-other-hands/build.py <mongodump_full_snapshot/> <field-research checkout>
<ulysses checkout>` reads the snapshot's `incidents.csv` and `reports.csv` (backup-20261109100729.tar.bz2, sha256
c1082588…, fetched from the database's snapshot host, 121,958,198 bytes, not committed), the Field's files at
field-research@6b562d3 (`analyse75.py`, `data75.js`, `data77.js`, `results77.json`, `check77/adjudication.json`,
`coding76.json` for the short notes) and the Atelier's at ulysses@39c8e8a (`check.js`, `check.json`); their sha256
are written into `data.js`. It runs the Field's own address rule and asserts that the first report of every one of
the 1,803 incidents gets the Field's class, then every count against the siblings' result files: 1,801 with a first
report, 21 harmed of 58, 4 of 120, 60 public acts of 176 answered (36 on a user, 24 on a developer or deployer; the
Field's states 16 and 20, 18 and 6, and the checked ones 14 and 22, 16 and 8), the estimate of 77 (43 to 160). `data.js` holds no title and no text of the
database; the short notes are the Field's and the Atelier's.

**Check.** `node works/2026-11-15-other-hands/verify.mjs` opens the page at 1132 and 390 px, reads every number on
it from the page and compares it with the Field's `results75.json`, `results77.json`, `data77.js` and
`check77/adjudication.json`, the Atelier's `check.json` (fetched at the pinned commits) and this work's check file;
it counts the marks drawn on the sheet and in the counts, steps through all 93 red paragraphs and all 60 acts, and
checks the seal's size, where the sheet begins, errors and sideways scroll. 120 checks.

**Readings that are this work's, not the siblings'.** A report as a word; the class of every later report (the
Field classed first reports only; the same rule is applied to all 6,964); the length of a word, which is arbitrary;
the order by the incident's date; one red line for the Field's wider "quotes or carries" and the Atelier's three
finer codes; the state of four acts and the two acts in the maker's favour, which differ from the Field's file and
are offered to it as a correction.
