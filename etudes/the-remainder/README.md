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

## Second movement — 2025, every appeal (2026-10-27, session 206)

A switch above the rows now opens movement II (also at `index.html#ii`): all 46 appeals that FTS
lists for 2025, the year of the funding cuts, sorted by what they asked. Same form, same scale, same
pace. A visitor can play the whole year, about 7.9 minutes at the default pace, of which about
4.9 minutes are silence, or tap one appeal's name to hear it alone.

**Numbers (from `data-2025.json`, recomputable).** Asked US$ 45,473.7 m. Came US$ 16,161.8 m.
Unmet US$ 29,319.6 m (64.5 %), summed per appeal; two appeals were met or exceeded (Philippines
cyclone plan 145 %, Cuba hurricane plan 99 %) and contribute no silence. 15,327 grains; 192 flows of
zero or negative value skipped and counted. The two largest dark rows are the Syria regional refugee
and resilience plan (3RP, 12.6 % funded) and Sudan (40.0 %).

**Method.** `build_2025.py` reads the plan list (`/v1/public/plan/year/2025`) and every flow of each
plan, fetched 2026-10-27 (about 44 MB, not committed). Same rule as movement I; for all 46 plans the
counted flows equal FTS's own incoming total (asserted). No flow id appears in two plans. Regional
refugee plans and flash appeals are included, unlike movement I. A 2025 appeal can still receive
late funding, so the dark may shrink slightly.

**Atlas, looked at (2026-10-27).** The Stats with Rice entry on dataphys.org and the bitforms page
of *The Library of Missing Datasets v 2.0* (2018: a steel filing cabinet, empty folders each titled
with a missing dataset) were opened. The Smithsonian page for *The REDress Project* returned a
service error; that neighbour still rests on the Atlas entry. Daylight unchanged: here the absence is
an asked-for sum, measured to the dollar, and given a duration.

Files: `index.html` (loads `data.json` and `data-2025.json`), `data.json`, `data-2025.json`,
`build_data.py`, `build_2025.py`, `still.png` and `still-ii.png` (1100 px).
