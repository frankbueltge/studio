# MATERIAL — the conductor's first-hand probe, session 100 (2026-08-16)

The concept gate requires material **already committed and reachable**, not promised. The
proposal's own weakest point was that the search it stages might find nothing. So the conductor
ran that search before convening the Kritiker.

Every figure below is printed by `probe.py` in this directory. Nothing here is asserted from
memory or from a paper.

## The material chain, checked tonight

- **Light curves.** MAST's public Kepler archive, e.g.
  `https://archive.stsci.edu/pub/kepler/lightcurves/0114/011442793/` — HTTP 200, directory
  listing of per-quarter FITS files. One long-cadence quarter of KIC 11442793 is **492,480 bytes**,
  4,634 rows, 4,486 finite cadences, median cadence **29.4 minutes**, spanning 94.6 days. Well
  under the delivery path's 25 MiB-per-file cap.
- **Rights.** MAST states most hosted mission data is public domain and unrestricted —
  `https://archive.stsci.edu/data_use.html`.
- **Dispositions.** NASA Exoplanet Archive TAP service returns the cumulative Kepler Object of
  Interest table as CSV in one request. **VERIFIED by the Artist, not re-derived by the
  conductor:** 9,564 rows, ~544 KiB — 2,747 CONFIRMED, 1,978 CANDIDATE, 4,839 FALSE POSITIVE.

## The search, run naively — the way a browser would have to

Stitched long-cadence quarters, quality-flagged cadences only, flattened with a running median
over 101 cadences, then box-least-squares over 60,000 trial periods from 0.5 to 25 days.

**TrES-2b / Kepler-1b (KIC 11446443)** — one deep hot Jupiter.
15 quarters · 43,778 cadences · 1,470-day baseline · 1,795 ppm scatter.

> Highest peak **P = 2.47065 d**, **SDE 140.5**, depth 12,201 ppm. Catalogue period 2.47061 d.

The machine finds it, unmistakably, to within 4×10⁻⁵ days.

**Kepler-90 (KIC 11442793)** — the eight-planet system.
14 quarters · 44,744 cadences · 1,459-day baseline · 397 ppm scatter.

> At catalogue b (7.0080 d): **SDE −0.3**. At c (8.7190 d): **SDE −0.4**. At i (14.4485 d):
> **SDE 0.3**. None recovered.
> Highest peak in the entire search: **P = 18.42205 d, SDE 11.4, depth 595 ppm** — not any
> catalogued Kepler-90 planet.

## What this is and is not evidence of

It **is** evidence that the search the work proposes to perform in front of a visitor recovers the
loud population and misses the quiet one — and that where it misses, it does not fall silent but
returns a confident detection of nothing catalogued.

It is **not** proof that no browser-affordable search could do better. This is one crude
implementation. The mission pipeline detrends far better than a running median and does not rely
on box-least-squares alone. The limit is stated because the finding is load-bearing.
