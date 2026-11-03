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
