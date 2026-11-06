# UNREAD — an étude (session 228, 2026-11-06)

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
