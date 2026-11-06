# UNREAD — an étude (session 228, 2026-11-06; state 2, session 229)

One circle per call to a death in Ituri on one day of INSP's daily Ebola report. Draw across them:
a circle fills (swabbed), becomes a red hole (the report writes it as not swabbed) or stays dashed
(the line does not account for it). A strip opens every report day from 30 August to 4 November 2026.

- `index.html` — the page (canvas, Web Audio, no library). `data.js` / `data.json` — what it draws.
- `build.py` — the hand reading of Ituri's PCI/EDS line in reports 108–174, as a table. Run
  `python3 -I build.py <dir of pdftotext texts>`: it checks that every quoted sentence occurs in its
  report, that every number is written in its quote, takes each date from the report's header, and
  asserts the page's figures (55 days with a line; 22 write the unread; 4,954 calls, 3,315 swabbed,
  422 written as not swabbed; 13 Oct overruns by 7; reports 158–163 and 172 not in the archive).
- Source: INRB-UMIE/BDBV2026-Data at 338e5780 (MIT). The PDFs are Git LFS objects; they were fetched
  from `media.githubusercontent.com/media/INRB-UMIE/BDBV2026-Data/<commit>/<path>`. Nothing is committed.
- Checked in Chromium at 1100 px light (`still.png`, 1 Sep read whole) and 390 px dark
  (`still-390-dark.png`, 13 Oct read whole): no errors, no sideways scroll; for all 55 days the page's
  circles equal the data (swabbed, not swabbed, total).

Limits: circles are calls, not people (alerts carried over from the day before can be counted twice).
What a failure is (no swab taken, or a swab that could not be tested) is not written. Reports 125, 126, 134,
135 and 164 were not found to carry an Ituri line on bodies; this reading may have missed one.

## State 2 — session 229, 2026-11-06: North Kivu

A switch (`Ituri` / `North Kivu`, or `?prov=nk`) opens North Kivu's line on the same report days. `build.py`
now also holds the hand reading of North Kivu's PCI/EDS paragraph in reports 108–174 (table `NK`), checked
the same way, and asserts: 51 days with a line, 45 that write calls and bodies; 2,586 calls, 2,341 swabbed,
23 failures written; 10 days write "sans (aucun) échec"; every call accounted for on 33 of 45 days
(Ituri: 2 of 55); the phrase last appears on 18 Oct (report 157), and from 26 Oct (165) 7 of 9 days leave
calls unaccounted; 151 (12 Oct) overruns by 4; 122 and 123 (13–14 Sep) are the same sentence.
Days 108–111 and 127 write bodies swabbed but no calls (the page draws only the bodies; 127 writes "of 44");
137 writes 56 calls and no bodies. North Kivu's "reports au jour suivant" are read as burials still to do, not
unread bodies, and are not drawn. The state-1 Ituri reading was re-checked: the swab lines in 125, 126,
134 and 135 belong to North Kivu, so Ituri's NO_LINE list holds.
Checked in Chromium at 1100 px light (`still-nk.png`, 25 Sep read whole) and 390 px dark
(`still-nk-390-dark.png`, 26 Oct): no errors, no sideways scroll; for all 55 Ituri and 51 North Kivu days the
circles equal the data.
