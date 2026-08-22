# The OUTSTANDING relay — what it calls, what it writes, what lies to you

Reference for whoever maintains this after tonight. The instrument is
`tools/relay.py` in `frankbueltge/studio`; it is stdlib Python 3 with no dependencies
and three modes: `--atlas OUT`, `--cycle OUT`, `--measure`.

## The two channels

| what | endpoint | notes |
|---|---|---|
| what has been re-issued since an instant | `https://api.weather.gov/products?type=ZFP&start=<iso8601>` | ~6 kB for 25 minutes of the nation |
| one bulletin, full text | `https://api.weather.gov/products/<uuid>` | `productText`, the plain-language forecast verbatim |
| zones → office, timezone, stations | `https://api.weather.gov/zones?type=public` | 6.2 MB, **atlas only, never per cycle** |
| observations | `https://aviationweather.gov/api/data/metar?format=json&hours=1&bbox=…` | 31 calibrated boxes per sweep |

Both services are United States Government works in the public domain. Neither
requires a key or an account. `api.weather.gov` requires a `User-Agent` that identifies
the application and asks that clients not add cache-busting query parameters; it answers
a rate limit with **403 and a reference id, not 429**.

## The four traps, so nobody meets them twice

1. **`/products/types/ZFP` accepts no query parameters.** `start`, `limit` and `end` all
   return 400 *"not recognized"*. The filterable endpoint is `/products?type=ZFP`. The
   difference is 1.9 MB against 6 kB, every cycle, forever.
2. **The observation endpoint caps every response at 400 records silently.** One national
   bounding box returns a complete-looking quarter of the country. `--atlas` re-checks
   every box on each run and warns when one starts to cap.
3. **An `ids=` list longer than about 2,100 characters does not error — it returns two
   records.** Silent truncation. The relay uses bounded boxes instead.
4. **`reportTime` is not the observation's time.** It is rounded, and a figure was lost to
   it once already. `obsTime` is the observation's epoch and is what the relay writes.

## The two files

`claims.json` — keyed by office. Periods are deduplicated **inside one bulletin** by exact
string identity of (period name, sentence); `z` is how many zones share that exact
sentence. Nothing is averaged, ranked or summarised, and `t` is the sentence verbatim,
because the work's gate bound it: the one unit a stranger already owns has to be reachable
in the room. Windows (`s`, `e`) are resolved from the period's name against the office's
timezone using the service's own day/night convention (roughly 06:00–18:00 local and
18:00–06:00); a label that cannot be resolved unambiguously travels with a **null** window
rather than a guessed one.

`sky.json` — keyed by station. `w` is the provider's own parsed present weather, never
re-parsed here; `r` marks the ones that name falling water; `t` is `obsTime`.

Both are written through a temporary file and `os.replace`, so a failed cycle leaves the
last good data standing.

## The header the host must send

```
Cache-Control: public, max-age=60, must-revalidate
```

Without it a ten-minute write can sit behind a ten-minute edge cache and the room shows a
sky up to twenty minutes stale. GitHub Pages sends a fixed `max-age=600` and cannot be
told otherwise.
