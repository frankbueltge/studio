# Studio: publish the OUTSTANDING relay — two JSON files on the works origin, refreshed in place

This is the infrastructure the studio's sixth concept was HELD on, written by the studio so the
decision costs a review rather than a build. It also **corrects the cost figures the studio gave
in `REQUESTS.md` on 2026-08-21**, which were wrong in one direction and wrong in the other, and
it reports one finding that decides whether the thing can work at all on your hosting.

Everything below was measured first-hand against the live public channels between 04:30 and
05:20 UTC on 2026-08-22. The instrument is `tools/relay.py` in the studio repository; it runs
on stdlib Python 3 with no dependencies.

## What the relay is

A scheduled job that writes two files into the studio works origin and replaces them in place:

| file | what it carries | size | gzipped |
|---|---|---|---|
| `claims.json` | every currently open forecast period the National Weather Service is publishing, with the **claim sentence verbatim** and the stated percent where one exists | 3.0 MB | **142 kB** |
| `sky.json` | every reporting station, its position, its observation epoch, and the present weather where there is any | 77 kB | **18 kB** |

A third file, `atlas.json` (27 kB), is geography — which office is where, which stations answer
for it — and is **committed beside the work, not relayed.** It changes when a forecast zone is
redrawn, not when the weather does.

So one refresh costs a visitor's browser about **160 kB over the wire**, which is the figure that
matters for a room running unattended on a projector for eight hours.

## The three corrections to what the studio asked you for on 2026-08-21

**1. It is two hosts, not one, and the second was never named.** The claims come from
`api.weather.gov`. The sky comes from `aviationweather.gov/api/data/metar` — a different federal
service. Session 106's request said "one request returns hundreds of stations' current
observations, 400 reports, 181 kB" without saying whose. That sentence was true of a host the
request never named, which made the ask look smaller and simpler than it is.

**2. The request count was four times too low, and the byte count three times too high.**
Session 106 said *"about nine requests… call it 55 requests and ~13 MB inbound per hour."*
Measured, a steady cycle is **32 requests and 1.20 MB**; a cycle that also picks up re-issued
bulletins is about **39 requests and 1.5 MB**. At a ten-minute cadence that is **~190–235
requests and 7–9 MB per hour**, so roughly **5–6.5 GB per month** off two free public services.

The request count is higher because **the observation endpoint caps every response at 400
records and does not say so.** One national bounding box looks like a complete answer and is a
quarter of one. The relay therefore sweeps 31 calibrated boxes, each verified small enough that
the cap does not bite; `--atlas` re-checks that on every run and prints a warning if a box has
started to lie. The byte count is lower because the product index turned out to be filterable:
`/products/types/ZFP` accepts **no** query parameters at all (`start`, `limit` and `end` each
return 400 *"not recognized"*), but `/products?type=ZFP&start=<iso>` returns only what has been
re-issued since an instant — **6 kB instead of 1.9 MB**, per cycle, forever.

**3. Five of the 125 offices cannot be placed through this channel, and two of them cannot be
answered at all.** `LKN` (Elko) and `TFX` (Great Falls) name no station this sweep can locate;
`PPG` (American Samoa) and `PQE`/`PQW` (Micronesia, Marshall Islands, Palau) name **no
observation station whatsoever** in their zone metadata. The record makes promises in places
this settlement channel cannot reach. The work draws the 120 it can place and says so; it does
not draw a node it cannot answer for.

## The finding that decides whether this is possible on your hosting

**A ten-minute write is worth nothing if the file is served with a ten-minute cache.** GitHub
Pages sends a fixed `cache-control: max-age=600` on every asset and does not let you change it
(`age: 343` observed on a live Pages response), so a ten-minute publish cadence collides exactly
with a ten-minute cache and a visitor can routinely be looking at data up to twenty minutes old.
The studio's own gate refused a sixty-minute cadence in advance and would refuse this for the
same reason: it is playback with extra steps.

**What the relay needs from the host is one header on two files:**

```
Cache-Control: public, max-age=60, must-revalidate
```

Netlify (`_headers`), Cloudflare and Vercel can all set it. GitHub Pages cannot. If the works
origin is on a host that cannot set it, say so and the studio will kill the concept rather than
ship a room that lies about being live — that is the studio's decision to make and it does not
need an answer softened.

## Cadence: what can actually be promised

- **GitHub Actions `schedule:` has a documented floor of five minutes**, and GitHub documents in
  the same place that scheduled runs are **delayed during high load** and that **"some queued
  jobs may be dropped."** There is no SLA. Ten minutes is legal there; ten minutes is not
  *guaranteed* there, and the studio would rather have that written down now than discover it.
- GitHub also disables scheduled workflows in a public repository after **60 days with no
  repository activity**. A job whose only commits are its own may qualify. Worth a calendar note
  either way.
- **Cloudflare Workers Cron Triggers** take minute-granularity cron and give five triggers on the
  free plan; **Netlify Scheduled Functions** take a standard five-field cron on all plans. Either
  meets the cadence more honestly than Actions does.
- **Nothing faster than five minutes is worth doing**: `api.weather.gov` returns
  `cache-control: public, max-age=300` on observations and `max-age=120` on the product index, so
  a faster poll re-fetches identical bytes. **Ten minutes is comfortably above that floor and
  below the studio's own hard limit.** The cadence is right where it was asked for.

## Politeness, and it is not optional

The service publishes no rate cap and no terms beyond *"open data, free to use for any purpose."*
It does require a `User-Agent` identifying the application, and it asks specifically that clients
**not** use cache-busting query parameters. It answers a rate limit with **403 and a reference id,
not 429** — so error handling that only recognises 429 will read throttling as a hard failure and
either loop on it or write an empty file over a good one. `tools/relay.py` sends a contact-bearing
User-Agent, adds no cache-busting parameter, never retries a 4xx, and writes through a temporary
file and `os.replace`, so **a bad cycle cannot destroy the last good data.**

## What is in `files/`

- `files/.github/workflows/studio-outstanding-relay.yml` — the scheduled workflow, as a starting
  point. It runs `tools/relay.py --cycle` against a checkout of the studio repository and commits
  the two files to wherever the works origin serves them from. **Paths are guesses**: this session's
  environment scopes repository access to `frankbueltge/studio`, so nobody here has read the site
  source. Fix the paths, or replace the whole thing with a Worker — the workflow is the cheap part.
- `files/relay/README.md` — the endpoint list, the file shapes, and the four instrument traps met
  while writing it, so whoever maintains this does not meet them again.

The instrument itself stays in the studio repository at `tools/relay.py`, where it is version
controlled beside the work that reads it.

## What happens on your answer

- **Yes, at ten minutes or better, with the header** → the hold lifts and the work goes to its
  premiere gate. The room is already built and lit against real data; only its source moves.
- **No, or only at sixty minutes, or the header is impossible** → the studio kills the concept.
  The gate refused that waiver in advance and the studio is not asking for one.

— Ensemble, session 107, 2026-08-22
