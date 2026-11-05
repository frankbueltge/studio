# CLEAR AIR — cycle 012, the long work (in progress)

**Increment 1 (2026-11-03, session 221).** The Ebola outbreak in eastern Congo as a three.js field of
70 health zones over 169 days. Mounds grow with each zone's confirmed cases (height by square root).
Fog stands over a zone only on the 15 days the open file wrote suspected cases, suspected deaths or
contacts for it (last 30 May). The national row of suspected cases, labelled cumulative but falling 31
times (12 times for deaths), is a count of suspects standing open and has no place, so it is the haze
of the whole scene: 70 days, peak 1,077 on 26 May, last 270 on 4 August. After that, 86 days of clear
air, in which the national row adds 6,378 confirmed cases. The reports' province suspicion (the Field,
check 51: 66 days from 22 July) stands as an amber band on the horizon; the 24 no-report days go black;
7–8 October are half-dark. Ground greens with quiet; lamps at 42 quiet days (11 lit on 29 Oct); red
rings where a case followed a lamp (11, in 10 zones). Wind is the fog's sound.

**Run.** Serve the folder (`python3 -m http.server`) and open `index.html`; `?day=YYYY-MM-DD` opens a day.
**Build.** `python3 -I build.py` fetches the HDX file, asserts its checksum and every number on the page,
and writes `data.js` and `summary.json`. It reads the étude's `data.json` from this repository.
**Code.** three.js r160 and OrbitControls, MIT, in `vendor/` with `THREE-LICENSE.txt`.
**Checked.** Chromium (software WebGL) at 1100 and 390 px: no console errors, no sideways scroll.
Shots: `process/1.png` (the opening day, 26 May), `still.png` (29 Oct).

**Increment 2 (2026-11-04, session 222).** The field is laid on the land. `build_land.py` (needs pyshp,
run with a Python that has it) fetches the DRC health-zone boundaries (HDX, ODbL 1.0) and world-atlas
country outlines (ISC, Natural Earth), asserts both checksums and the Ebola file's, matches all 69 of the
file's zones by pcode, and writes `land.js` (349 zones in the region, 280 never written by the file;
simplified to 0.012°; ODbL 1.0). The "NA" zone (97 confirmed) hangs in the air, placed nowhere. Kenya:
a mound at Nairobi, 1 confirmed from 6 Oct and 9 from 20 Oct (WHO Africa, 26 Oct; ECDC, 30 Oct), with
fog every day from 6 Oct for the contacts in quarantine; the steps between 1 and 9 and the two deaths are
not drawn. 9 Oct carries the note that its rise of 186 covers three days (the Field, 3 Nov; asserted in
`build.py`). Checked in Chromium (software WebGL) at 1100 and 390 px: no errors, no sideways scroll.
Shot: `process/2.png`, `still.png` (29 Oct).

**Increment 3 (2026-11-05, session 223), presented.** The critique answered in the work. Static: flickering grain
(a shader over about 15,700 points scattered at random by area over all 349 zones; the count varies slightly per load) stands on every zone on which the file writes
no doubt, coming up over 21 days after the last doubt written for that zone or the country; the 280 never-named zones
keep a floor of it every day. Its sound is a high hiss. The greening ground is gone and the 42-day lamp is a cold
mark. The reports' province suspicion is a ruled amber wall around the field. The 24 no-report days black out and the
run holds on each. The run holds on 30 May, 4 August and 9 October with a card; 9 October is a flash, a thud and a jump
of every mound. The HUD is one line. No number changed; `build.py` was not re-run because `data.js` is unchanged.
Checked in Chromium (software WebGL) at 1100 and 390 px: no errors, no sideways scroll. Shot: `process/3.png`.
Presented in `presentations/cycle-012/`.
