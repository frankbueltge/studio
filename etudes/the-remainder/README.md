# THE REMAINDER — étude (2026-10-26, session 205)

A form study made between cycle 010's presentation and the convening. It is not a work of a cycle.
It covers sixteen humanitarian appeals for Sudan, 2011–2026, from OCHA's Financial Tracking Service.
Each row is the sum asked for. Every grant that came is a lit grain, in date order and as wide
as its dollars. The rest of the row is what was asked for and never came, and FTS holds no
record of it. Playback sounds one tone per grant as the line passes it: bigger grants sound lower,
and commitments not yet paid have a second timbre. The remainder plays as silence at the same scale,
one second per US$100 m by default.

**Numbers (from `data.json`, recomputable).** Asked US$ 26,922.8 m. Came US$ 14,260.0 m.
Remainder US$ 12,662.8 m (47.0 %). 2025: asked 4,162.5 m, came 1,664.7 m (40.0 %), so at the
default pace about 25 s of the year's 42 s is silence. 2026 is an open appeal.

**Method.** `build_data.py` reads the API downloads (the plan list for SDN, and every flow of each of
the 16 Sudan plans). It keeps flows with boundary `incoming` and status not `pledge`. For
every plan their sum equals FTS's own incoming `fundingTotal`, and the script asserts it. Nine
flows with zero or negative amounts (corrections) are skipped and counted per year.
Requirements are FTS's revised requirements. Regional refugee plans and the 2020 COVID plans
are excluded. The downloads (about 20 MB) are not committed; the script names the endpoints.

**Licence of the data.** CC BY-IGO, OCHA FTS (as listed on HDX, `sdn-requirements-and-funding-data`).
No third-party code: the page is plain HTML, canvas and Web Audio.

**Why this form.** The briefing's fallback question asks what the cuts removed. Its answer is a sum
with no record behind it. Duration gives that sum a body the visitor has to sit through, measured
against the sound of what came.

**Atlas neighbours.** *Of All the People in All the World: Stats with Rice* (Stan's Cafe),
*The Library of Missing Datasets* (Mimi Ọnụọha), *The REDress Project* (Jaime Black). Daylight:
the absence here is a sum that was counted, asked for and not met. It is given a duration on the
same scale as the sound of what was given. The grains are grants, not people.

**Builds on.** The Field's probe of the briefing's open-data doors
(field-research `notes/convening-after-010/probe.json`, 2026-10-26), which found the FTS API
open. It sits beside the Atelier's *The Unclassified* (ulysses
`artifacts/convening-after-010/the-unclassified/`).

Files: `index.html` (loads `data.json`), `data.json`, `build_data.py`, `still.png` (1100 px).
