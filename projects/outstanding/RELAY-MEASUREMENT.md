# RELAY-MEASUREMENT — `tools/relay.py` against the live public weather API, 2026-08-22

All figures below are from real runs tonight (UTC); `$OUT` is scratch output.

## 1. Cold run, coverage

`python3 tools/relay.py --out $OUT` — started 00:35:19Z, wall 14.0 s, 183 requests,
8,690,140 B in.

**Offices: 123**, not the 126 in `/products/types/ZFP/locations` — several registry codes
share one physical office (`AER`+`ALU`→`PAFC`, `NSB`+`WCZ`→`PAFG`, `PR`→`TJSJ`,
`PPG`→`NSTU`). `relay.py` derives offices only from `issuingOffice` on issued bulletins,
sidestepping the per-code lookup's own trap: `/products/types/ZFP/locations/{CODE}`
returns HTTP 200 with an empty `@graph` for a wrong-but-plausible code (confirmed
`PHX`/`SEA` vs. real `PSR`/`SEW`).

**3,771 zones, 47,445 periods.** Numeric 20,217 (42.6 %), silent 25,766 (54.3 %, naming
neither a number nor a precipitation word), word-only 1,462 (3.1 %). Silence is this
record's commonest promise, as CONCEPT.md claims. Edge case, reported not fixed: 922
periods (1.9 %) are `silent: true` yet carry a qualifier attached to fog, not rain
(`AJK AKZ317` MONDAY NIGHT: "Patchy fog." → `words: ["patchy"]`) — matching
`zfp_settle.py`'s own finding. Correct by the spec's wording, but a `words`-driven UI
could misread it as non-silent.

These counts are **exact, from a full run** — against the house's own 8-office
extrapolation (42,900) and VERIFIER-107.md's 12-office one (95 % CI ≈14,800–34,700).
47,445 sits above both.

## 2. Size

```
forecasts.json   9,585,621 B raw   370,588 B gzip  (25.9x)
stations.json       11,848 B raw     2,264 B gzip  (5.2x)
```
371 kB gzipped reloads easily every 10 minutes; the 9.6 MB raw figure is a parse cost,
not — with gzip serving — a network one.

**De-duplication, measured, not implemented:** of 47,445 periods, **24,161 (50.9 %) are
byte-identical to another period's text within the same office**. A per-office texts
table cuts raw period-text bytes 41.7 % (4,884,536 → 2,846,372); global de-dup, 48.1 %
(19,445 unique strings). The output shape is fixed and verbatim text stays inline, so
this is handed back rather than applied.

## 3. Zone geometry (lat/lon), measured cost

Bulk zone listing (`/zones?type=public&limit=5000`, 1 request, 6.2 MB) returns
`geometry: null` always; coordinates require the per-zone endpoint
(`/zones/forecast/{UGC}`), sampled at 40 zones: **+40 requests, +3,138,343 B, avg
78.5 kB/zone** (264 B to 71,548 B — coastline complexity dominates). Extrapolated to all
3,771 zones: **≈3,771 requests, ≈296 MB** — never run in full inside a cycle. `lat`/`lon`
ship `null` from the live cycle; the one-time pass that fills them is §8.

Station lat/lon is free: the bulk `/stations?id=A,B,C...` listing carries a `Point` per
station in the same request used for metadata (55–58 of 59 requested IDs resolve; `KHNL`
does not — `PHNL`, its real ID, does; dropped, not guessed).

## 4. Cost per cycle: cold vs. incremental

| run | requests | bytes in | wall | offices fetched | reused |
|---|---|---|---|---|---|
| cold (00:35:19Z) | 183 | 8,690,140 | 14.0 s | 123 | 0 |
| incremental (00:47:04Z) | 67 | 2,788,891 | 5.4 s | 7 | 116 |

Incremental is **36.6 % of cold's requests, 32.1 % of its bytes**, 11.75 min after cold
start, and its 7 offices are exactly the 7 whose `issuanceTime` changed (§5's independent
raw-index diff names the same 7). 67 = 1 index + 7 bodies + 1 station list + 58
observations, which are always re-fetched by design.

## 5. Is the 10-minute cadence real?

Two raw index fetches, independent of `relay.py`, 631 s apart: `00:36:28Z` →
`00:46:59Z` (10 min 31 s, reported exactly, not rounded to "10").

**7 of 123 offices (5.7%) reissued in that window:** `APX, CAE, FGZ, FWD, PAH, PSR, RIW` —
none appeared or dropped between fetches.

**Periods touched: 2,871 of 47,445 (6.05%)** — those 7 offices' period totals, summed
from the post-incremental `forecasts.json` (`APX` 420, `CAE` 364, `FGZ` 216, `FWD` 644,
`PAH` 527, `PSR` 294, `RIW` 406). Answers the gate's real question: **yes — a visitor
standing for twenty minutes sees change arrive.** 6% of all open periods on screen got a
fresh, verdict-eligible bulletin in this one window.

**Labelled as inference, not measurement:** this is one 10.5-minute sample.
VERIFIER-107.md measured 10-minute reissue counts across a full day, bursty (1–59
offices/bucket, mean 9.2, stdev 9.1); my 7-office figure sits inside that range, below
the mean — real, not a guaranteed rate for every hour. Not in doubt: change arrived
inside the interval this session actually watched.

## 6. Observation freshness

58 resolved stations, fetched 00:35Z. Newest-reading age at fetch, minutes: **min 10.5,
p25 15.5, p50 20.5, p75 25.5, p90 39.5, max 42.5, mean 22.1.** Contradicts CONCEPT.md's
"about an hour"; matches VERIFIER-107.md's 40-station figure (median 20.9, p90 26.9) —
well under an hour, both times.

## 7. Verdict

A 10-minute relay is feasible **at this size** if **the site serves `forecasts.json`
gzipped** (370 kB, not 9.6 MB, per fetch). If not, the 41–48 %-lossless texts-table
reduction above is measured and ready; the fixed output shape was not changed
unilaterally. Zone `lat`/`lon` ships `null` from the live cycle and is filled by the
one-time pass in §8: live it would add ~3,771 requests and ~296 MB to a cycle otherwise
costing 67–183 requests and 2.8–8.7 MB. Station lag runs 10–42 min here — the room
watches a sky about 20 minutes old, refreshed on its own clock, not an hour-old one.

## 8. Zone geometry, resolved

`tools/zone_gazetteer.py`, one-time offline pass, `generated_at` **2026-08-22T01:09:15Z**.
4,080 public zones. First pass: 4,081 requests, 325,589,567 B in, 496.6 s wall, 77
failed (`GeometryCollection`-shaped geometry, unhandled). Fixed; a resumable
`--retry-failed` pass fetched only those 77: 78 requests, 48,578,130 B in, 5.1 s wall, 0
failed. **Combined: 4,159 requests, 374,167,697 B in (streamed, centroid computed,
discarded — never written to disk), 501.7 s wall, 0 zones failed.** Output
`projects/outstanding/zone-centroids.json`: **114,700 B**.

`tools/relay.py` cold run against this lookup: **3,683 of 3,771 live zones (97.7%)**
geocoded, 0 extra requests. The 88 ungeocoded are compound multi-zone UGC headers
(e.g. `GUZ001-MPZ001`) `zfp_harvest.zone_blocks()` returns as one joined string, not a
single code the lookup can match — pre-existing, unrelated to this pass, reported not
fixed.

Fixture regenerated (`forecasts.sample.json`, 71 zones, 187,429 B). Headless load
(Playwright/Chromium, 1600x900): field lays out — 71 places, 977 open periods, no
console errors. OKX/SEW render as two distinct, correctly west/east-ordered clusters,
not stacked. GUM/KEY's own zones are exactly the compound-header ones above, so they
render in the unplaced strip in this capture. Separately verified, with GUM's real
centroid (13.4435, 144.7774) injected into a scratch copy through the real `room.js`:
dynamic bounds **does** crush the continental offices — OKX-SEW separation drops from
1,271 px (86% of width) with Guam excluded to 239 px (16%) with it included, Guam
landing at the far edge. Reported to the conductor as a `room.js` finding, not fixed.
