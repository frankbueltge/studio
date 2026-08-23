# The OUTSTANDING relay — what it calls, what it writes, what lies to you

The operator's page for `tools/relay.py`. The implementer's page is the file's own
docstring. Written 2026-08-22 as a proposal to the site side, moved here 2026-08-23 when
the proposal channel turned out to be unable to carry it, and corrected the same night by
measuring the things it had reasoned about.

The instrument is stdlib Python 3, no dependencies, three modes:
`--atlas OUT`, `--cycle OUT`, `--measure`.

## The two channels

| what | endpoint | notes |
|---|---|---|
| what has been re-issued since an instant | `https://api.weather.gov/products?type=ZFP&start=<iso8601>` | ~6 kB for 25 minutes of the nation |
| one bulletin, full text | `https://api.weather.gov/products/<uuid>` | `productText`, the plain-language forecast verbatim |
| zones → office, timezone, stations | `https://api.weather.gov/zones?type=public` | 6.2 MB, **atlas only, never per cycle** |
| observations | `https://aviationweather.gov/api/data/metar?format=json&hours=1&bbox=…` | 31 calibrated boxes per sweep |

Both services are United States Government works in the public domain. Neither requires a
key or an account. `api.weather.gov` requires a `User-Agent` that identifies the
application and asks that clients not add cache-busting query parameters; it answers a
rate limit with **403 and a reference id, not 429**.

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

## The fifth trap, found 2026-08-23, and it is about what the room shows

**`claims.json` is an accumulation, not a snapshot.** Each cycle merges the bulletins
re-issued since an instant into what the file already held and drops periods whose window
has closed. A relay started with no `claims.json` beside it therefore holds only the
offices that happened to re-draft in the last few minutes — **twelve of 125** on the first
cycle run from nothing on 2026-08-23 — and fills toward the whole record over roughly half
a day, as each office re-issues on its own clock.

Left alone, that is a room drawing a country it has not been told about. Two answers, and
both are now in place: the relay backfills twelve hours on a cold start automatically
(the absence of the file is the signal; `--prime N` overrides the width; the printed report
names which of the two the run was), and the room draws an office it has not heard from as
bare and unlit, never as an office that promised nothing.

## The sixth trap, found the same night: an office arrives under two names

The claims channel names an office by its **ICAO station id**; the atlas keys offices by
the id their **zone metadata** uses. For 121 of 123 the two coincide by accident of the
prefix — `KOAX` → `OAX`, and the zones say `OAX`; `PAFC` → `AFC`, and the zones say `AFC`.
For two they simply differ, and those offices' promises were being filed under a key no
atlas entry answers to and dropped without a trace:

| arrives as | belongs to | what was being lost |
|---|---|---|
| `TJSJ` | `SJU` | San Juan — 15 zones, 176 open claims, **Puerto Rico and the Virgin Islands entire** |
| `NSTU` | `PPG` | Pago Pago — 1 zone, 8 open claims. American Samoa's forecasts *do* arrive; what it has no station for is answering them |

`OFFICE_ALIAS` in `relay.py` is keyed by the full id, not the three-letter tail, so a
future office whose tail collides cannot inherit an alias by accident. Verified against
the live index the same night: the only ids that are not four characters beginning with K
are `NSTU`, `PAFC`, `PAFG`, `PAJK`, `PGUM`, `PHFO`, `TJSJ`, and of those only the two above
disagree with the atlas.

**What the fix is worth, measured before and after on the same night's record:** 119 of 120
placeable offices drawable → **120 of 120**, and 98.4 % → **98.88 %** of all standing
periods reaching the room. The 1.12 % that remains is the five offices this channel cannot
place (`LKN`, `TFX`) or cannot answer at all (`PPG`, `PQE`, `PQW`).

## What a cycle costs, measured rather than estimated

All figures first-hand, 2026-08-23, against the live services.

| | requests | inbound | seconds |
|---|---|---|---|
| cold start (`--prime 720`, once) | 155 | 7.9 MB | 91 |
| warm cycle, 3 offices re-issued | 35 | 1.74 MB | 16 |
| warm cycle, 12 offices re-issued | 44 | 2.03 MB | 44 |

A cycle's cost is a **range driven by re-issuance**, not a constant. At a ten-minute
cadence that is roughly 190–260 requests and 7–12 MB an hour off two free public services.

**How it splits between the two hosts, which matters because only one of them publishes a
number.** Every cycle is `1 + N + 31`: one product index and one fetch per re-issued
bulletin to `api.weather.gov`, and **exactly 31 observation boxes to `aviationweather.gov`,
always, warm or cold.** So the aviation service sees 31 requests per cycle — 186 an hour at
a ten-minute cadence — against its **published ceiling of 100 requests per minute**
(<https://aviationweather.gov/data/api/>), with the whole sweep fitting inside one minute
with room to spare, and the cold start does not change that number at all. The National
Weather Service takes the other 1–124 and **publishes no numeric ceiling**: its
documentation says only that the limit "is not public information, but allows a generous
amount for typical use", that a User-Agent identifying the application is required
(<https://www.weather.gov/documentation/services-web-api>), and, in its FAQ, "Please don't
use cache busting techniques like random numbers in the query string"
(<https://weather-gov.github.io/api/general-faqs>). That there is no published number is
itself the finding; nobody here should estimate one.

## What the files hold, once the relay is warm

Measured whole on 2026-08-23: **123 offices, 25,738 distinct claim sentences, 46,739
forecast periods standing open, 19,015 of them carrying a stated percent and 26,399 saying
nothing about precipitation at all.**

| file | raw | gzipped |
|---|---|---|
| `claims.json` | 5.5 MB | 275 kB |
| `sky.json` | 89 kB | 22 kB |

So one refresh costs a visitor's browser about **297 kB over the wire**. The figure of
~160 kB given to the site side on 2026-08-22 was measured against a file that had not yet
filled; it is corrected here.

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

## The header, and the retraction of the finding that was supposed to decide everything

On 2026-08-22 this page said the host must be made to send
`Cache-Control: public, max-age=60, must-revalidate`, because a ten-minute write behind a
ten-minute cache shows a stranger a sky twenty minutes old — and it named the fixed
`max-age=600` of one particular static-hosting product as the thing that made this the
finding on which the whole work turned.

**That was reasoned from a host this site does not use.** Measured on 2026-08-23, the works
origin answers `server: cloudflare` and sends, on the work path itself and on the JSON
already served next door:

```
cache-control: public, max-age=0, must-revalidate
```

which is stricter than what was asked for.

**And the retraction goes further than that, because the ask was aimed at the wrong
mechanism entirely.** Every one of those paths also answers `cf-cache-status: DYNAMIC`,
which this infrastructure defines as having decided at request time that the asset is not
eligible for cache, so the request reached the origin **without a cache lookup at all**
(<https://developers.cloudflare.com/cache/concepts/cache-responses/>) — and its default
behaviour does not cache HTML or JSON
(<https://developers.cloudflare.com/cache/concepts/default-cache-behavior/>). The tell is
`chronicle.json`, which sends `max-age=3600` to the browser and is nonetheless `DYNAMIC` at
the edge: **what the origin tells a browser and what the edge decides to hold are two
separate systems here.** Shortening `max-age` would not have changed what a visitor sees,
because nothing was consulting it to decide whether to cache.

**What replaces the ask is narrower and is not a header at all.** The one caching mechanism
proven to exist on this zone and invisible from outside is a Cache Rule setting an Edge
Cache TTL: the vendor documents that under Origin Cache Control the original
`Cache-Control` "passes downstream from our edge **even if Edge Cache TTL overrides are
present**" (<https://developers.cloudflare.com/cache/concepts/cache-control/>). An edge rule
could therefore hand back a copy from before the last write while still telling the browser
not to cache it, and no amount of measuring from outside would show it. `robots.txt`
answered `REVALIDATED` — served from the edge after a conditional check — which is proof
that at least one path on this zone genuinely is edge-cached, and nothing about content type
predicted which. So: **once the two output paths are chosen, someone with the dashboard has
to confirm no Cache Rule matches them.** That is a check, not a header, and it can only
happen after the paths exist.

What is still missing beyond that is something that **runs** the relay every ten minutes and
writes its two files onto this origin. Three routes, priced 2026-08-23:

- **A scheduled job in the code-hosting platform's CI**, committing the files into the site
  repository. Documented floor five minutes, so ten is legal; the same page documents that
  scheduled runs "can be delayed during periods of high loads" and that "some queued jobs
  may be dropped"
  (<https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows>). It
  also rests on an assumption nobody here has verified: that this site redeploys from a git
  commit at all. A sketch is kept at `tools/relay-schedule.yml.example`, paths and all,
  still guesses.
- **A scheduled function on the vendor already fronting this zone**, writing to its own
  storage and served same-origin. Minute granularity, so ten minutes is trivial, and no
  "may be dropped" language is published
  (<https://developers.cloudflare.com/workers/configuration/cron-triggers/>). The free tier
  allows 50 outbound requests per invocation against this relay's 32–46, which fits with
  little headroom (<https://developers.cloudflare.com/workers/platform/limits/>). It needs
  the zone owner's account; it is not something this house can install.
- **A same-origin handler that calls the two services at request time**, with no file written
  at all. `connect-src 'self'` constrains what the *browser* may fetch and says nothing about
  what a same-origin server-side route does internally, so this is permitted. It is a real
  option and it changes what the work is: data would refresh only when someone is looking, so
  a room left open with nobody in it stops being told anything. That is a decision about the
  work, not about hosting, and it is not made here.

## The fixtures beside the room

`projects/outstanding/room/data/` carries four, and each says on its own face whether it is
whole or cut:

- `fixture-claims.json` / `fixture-sky.json` — a five-office, 69-station excerpt of a
  national capture of 2026-08-22, so the room runs with no relay at all. Until 2026-08-23
  their `counts` blocks still reported the parent capture's figures — 66 offices and 27,207
  periods against the five offices and 2,445 periods actually in the file, 1,514 stations
  against 69. Recomputed to describe the files they are in. A count that describes a file
  the reader does not have is a false claim in a committed file, which is the failure this
  house exists to refuse.
- `fixture-cold-claims.json` / `fixture-cold-sky.json` — whole and unedited: one cycle run
  from nothing on 2026-08-23, twelve offices and 1,725 stations. The state a young relay is
  actually in, kept so it stays testable (`?cold`).
