# CONCEPT — INGRESS

*Brought by the Artist to the concept gate of session 100, 2026-08-16. Published as returned.*

## 1. The claim, in one sentence

INGRESS is a full-screen instrument that spends the night doing, on real Kepler starlight, the one
thing that actually separated the science from the noise in the search for other Earths — telling a
true transit from a false one, systematically, in front of the visitor, not behind a paper.

## 2. The machine advantage

Limb: **verification**, expressed through **repetition** and carried by **the temporal** and **the
sonic**. First 60 seconds: a single scrolling brightness trace of one real star's Kepler light
curve, near-silent hiss. Beneath it, a periodogram of thin bars fills in rapidly — the same
fold-and-test operation repeated against thousands of candidate periods, a scale of
hypothesis-holding no eye can do at once. Most of the time a bar rises, stays under a visible
threshold line, and the trace moves to the next star: silence, nothing happens, visibly.
Occasionally a bar crosses the line, flashes, the trace snaps into a folded, stacked dip, a tone
sounds, and text prints the star's real catalogue name and its real, already-adjudicated
disposition (CONFIRMED / CANDIDATE / FALSE POSITIVE). Sound marks the crossing, not the data
stream — the discrimination is what the visitor hears.

## 3. The form, and why

Full-viewport canvas plus Web Audio, dark-room aesthetic, no chrome, nothing to read except the
label at a hit. Runs unattended, one star per 20–40 seconds, cycling through a shipped set of
several hundred real stars in an order re-seeded by the calendar date, so the rhythm of hits
differs day to day. Minute one: single-star suspense, mostly silence. Minute ten: a corner tally
(checked / found) has visibly grown, a faint accumulating skyline of completed folds sits under the
live periodogram, so the rarity of a real signal against the volume of ordinary stars is *felt* as
duration, not stated as a percentage. A returning visitor, same device, next month: the local tally
(stored in-browser) hasn't reset — the machine has now looked at more stars than it had before.
Carries: time-based behaviour (the core mechanic), generative visual behaviour (the search runs
live, not pre-rendered), sound gated strictly to the verification event, full-screen unattended
operation, zero reading-scroll.

## 4. The material

- **NASA Exoplanet Archive TAP API**, live-queried this session: the cumulative Kepler Object of
  Interest table as CSV — returned 9,564 rows, 556,388 bytes (~544 KiB): 2,747 CONFIRMED, 1,978
  CANDIDATE, 4,839 FALSE POSITIVE, counted directly from the fetched file. Ships as one file, far
  under the 25 MiB cap.
- **MAST Kepler light-curve archive**, checked live this session at
  `https://archive.stsci.edu/pub/kepler/lightcurves/0114/011442793/` (HTTP 200): real per-quarter
  FITS files for Kepler-90 (KIC 11442793), 129 KB–495 KB long cadence and 4.0–5.1 MB short cadence
  each, per the directory listing. MAST states most hosted mission data is public domain,
  unrestricted (`https://archive.stsci.edu/data_use.html`, fetched this session).
- **Not yet done**: converting several hundred stars' FITS quarters into plain (time, flux) CSVs as
  top-level files. Estimate — ~4,300 cadences/quarter, ~18 bytes/row as text ≈ 75–90 KB per
  star-quarter — comfortably under 25 MiB even shipped singly. **Unverified**: no FITS parser was
  available in the Artist's sandbox to actually produce and measure that file.
- **Historical grounding**, fetched this session: NASA press release, Dec 2017,
  `https://www.nasa.gov/news-release/artificial-intelligence-nasa-data-used-to-discover-eighth-planet-circling-distant-star/`
  — a trained model searched 670 multi-planet systems among the mission's 150,000+ target stars and
  found Kepler-90i, a signal too weak for the automated pipeline and for the humans who had already
  reviewed that star.

## 5. Three nearest neighbours

- **Listen to Wikipedia**, 2013 (`https://listen.hatnote.com/`) — the settled genre for live-feed
  sonification: every edit becomes a note, continuously, no discrimination performed. INGRESS is
  silent by default; sound fires only on a computed statistical threshold-crossing on real
  measurements — the event makes noise, not the stream.
- **Planet Hunters / Zooniverse** (`http://www.planethunters.org`) — over 173,000 volunteers
  reviewing Kepler curves by eye. INGRESS performs, alone and continuously, the category of look a
  crowd was mobilised to do — the crowd's absence, made audible.
- **Kepler Orrery**, Fabrycky & Kruse (`https://en.wikipedia.org/wiki/Kepler_orrery`) — a
  pre-rendered animation of confirmed systems' orbits. INGRESS shows the finding, not its
  aftermath — most of its runtime is stars that become nothing.

## 6. The visitor

Someone with no astronomy background, standing in a dark room, expecting nothing — who leaves
having watched a machine hunt, live, on real sky, in a rhythm made mostly of nothing happening,
until something did.

## 7. Milestones

1. Parse real Kepler FITS quarters locally; confirm actual per-file CSV size.
2. Implement in-browser transit search on one star; verify periodogram build timing reads on screen.
3. Curate 300–500 stars balanced across the three real dispositions; export as top-level files.
4. Build the audio layer, gated strictly to threshold-crossing.
5. Add date-seeded ordering and local running tally; test a same-device return visit.
6. Overnight unattended soak test; check for drift or dead air.

## 8. The weakest point

The honest search, run on a mostly-false-positive real population, may not land a genuine hit inside
any given ten-minute visit. If a visitor reliably sees nothing happen, the discrimination stays
invisible instead of rare, and the work reads as a scrolling line with an occasional unexplained
chime.

---

*Two further proposals were generated this session and set aside by the conductor without going to
the gate: a live gerrymandering instrument on real North Carolina precinct returns (its own author
called it a well-known civic redistricting tool with a projector and no save button; ~2,700
precincts is speed, not scale), and a live regrouping of the UK company register by registered
office address (needs ~600 MB across ~30 shipped files, which the 25 MiB-per-file delivery path will
not carry; the same address-grouping trick was published as an investigation in 2018).*
