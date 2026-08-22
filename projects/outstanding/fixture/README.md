# Development fixture — NOT the work's data source

`forecasts.sample.json` and `stations.sample.json` in this directory are a **frozen
snapshot**, captured once, from a real run of `tools/relay.py` against the live public
weather API:

- Captured at: **2026-08-22T01:10:18Z** (`generated_at` inside `forecasts.sample.json`;
  `stations.sample.json` reads `2026-08-22T01:10:21Z`)
- Source: `https://api.weather.gov`
- Command: `python3 tools/relay.py --out <dir>` (with `zone-centroids.json` present, so
  zone `lat`/`lon` are real, not null — see below), then trimmed to 4 offices
  (`OKX` New York, `SEW` Seattle, `GUM` Guam, `KEY` Key West — chosen for spread: two
  large multi-zone offices, one small territory office, one single-zone office) and 12
  stations, to stay under the room's fixture-size budget.
- `forecasts.sample.json`: 4 offices, 71 zones, 977 periods, 187,429 bytes.
- `stations.sample.json`: 12 stations, 2,548 bytes.
- **68 of the 71 zones carry real `lat`/`lon`** from `projects/outstanding/zone-
  centroids.json` (see `tools/zone_gazetteer.py`); the other 3 (`GUZ001-MPZ001`,
  `MPZ002-003`, `FLZ076>078`) are compound multi-zone UGC headers the bulletin parser
  emits as one string — not a single code the gazetteer can look up — so they keep
  `lat`/`lon`: null on purpose, same as any zone the lookup doesn't cover.

**This is a fixture for building the room's screen against real-shaped data. It is not
live, it does not update, and it must never be pointed to by the shipped work.** The
work's actual data comes from `tools/relay.py` run on a schedule against
`https://api.weather.gov`, writing `forecasts.json` and `stations.json` fresh in place.
Every claim text in this fixture is verbatim from the public forecast at the instant
above — it will be stale by the time anyone reads this file, which is the point: it
exists to unblock building the screen, not to describe current weather.

See `projects/outstanding/RELAY-MEASUREMENT.md` for the full measurement of the live
relay, including size, request cost, and coverage figures this snapshot was drawn from.
