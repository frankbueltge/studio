# NO PUBLIC LAND

The Studio's work for cycle 013, step 1 of the programme *Can increasingly capable AI be kept under human and
democratic control, and by whom?* Presented 2026-11-09 (session 237). Score: `SCORE.md`. Process: `PROCESS.json`, `process/`.

**Build.** `python3 -I build.py <the Field's ai_chip_owners_cumulative_by_designer.csv> <results65.json> <gpu_clusters_direct67.csv> <results67.json>` — the first two
from field-research@bb56805, `artifacts/cycle-013/who-holds-the-compute/`, checked by sha256. It aggregates all
215 rows by owner and quarter (median, 5th and 95th percentile, power in MW), asserts every quarter's total, every
owner's sum and the five's share against the Field's file and the figures the page states, and writes `data.js`.
A row with no range is counted at its median at both ends and flagged.

**Check.** `node verify.mjs <n>` opens the page at 1100 px light and 390 px dark, fails on any error or sideways
scroll, fits all 17 quarters and fails if any parcel's area is off its share by more than 0.5 points (worst seen:
0.05), and writes `process/<n>.png`.

**Form.** Each parcel is a cell of a power diagram on the unit land (a fixed, noisy coast normalised to the area of
the unit disk); weights and sites are fitted iteratively until every cell's area matches its owner's share. At true
scale the land's radius goes with the square root of the counted stock outside the smuggled row; the smuggled row
lies offshore at the same scale. The hum: one sine per owner at a harmonic of 60 Hz, gain by share, panned by
parcel; master level by the log of the stock's power draw.

**Stakes (since session 236).** Every cluster of the Field's copy of Epoch AI's GPU-cluster list with an H100e estimate
(459) is a square of its true area at the land's scale, standing from the first survey on or after its first
operational date (undated: from the end of 2025). It stands in its owner's parcel where the owner table has a row
(by the first owner the list names; Meta AI as Meta; clusters in China in the record's "China"); public and
public/private clusters stand in the column off the coast; the rest in "everyone else". A later "Phase n" of a site
replaces the earlier from its survey on (read from the names, an estimate). `build.py` asserts the count, the H100e
sum and the public and mixed shares against the Field's `results65.json`, and every stake figure the page states.

**Stakes (since session 237).** Rebuilt from the Field's direct fetch of the cluster list (study 67,
field-research@759d15f, `data/gpu_clusters_direct67.csv` and `results67.json`, sha256-pinned). A cluster stands from the first
survey on or after its first operational date until the survey in which the cluster the list names under "Superseded by"
stands (29 such pairs; NVIDIA SATURN V Phase 2 names a successor the list does not hold, so it stands, as in the Field's
count). The six undated clusters are not staked. `build.py` asserts 460 clusters and 1,573,244 H100e in the list, and
425 standing at the end of 2025 with 1,234,247 H100e, public 12.7 % and mixed 4.4 %, all equal to the Field's
`results67.json`; it writes the stakes' coverage of the land for every finished quarter (73.6 % in March 2022, 6.1 % at the
end of 2025), which the page states. The section above describes the second state and is kept as written.

**Third state (session 237).** The cluster list is off by default and the public column reads "— (not 0)"; public stakes are
crossed outlines, never filled. An inset at the top right draws the same power diagram at a fixed radius, from the same fit.
