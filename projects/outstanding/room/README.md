# OUTSTANDING — the room (build note)

Milestone 1 — *every office's nodes drawn, all rings open, nothing settled
this session* — built and verified true. Machinery for milestones 2–5
(flare, rupture, re-issuance sweep, afterglow) is built and verified against
real bulletins/station data, driven by actual file changes, never a timer
over a fixed file.

## Data contract

Polls `forecasts.json` (`offices[].zones[].periods[]`: `label`, `text`,
`percent`|null, `words[]`, `silent`) + `stations.json`
(`stations[].{lat,lon,observed_at,precip_last_hour_mm,present_weather,text}`)
every 15s from `RELAY_BASE`, a const atop `room.js` — default
`/studio/relay/outstanding`, overridable via `?relay=`.

## Built

`index.html` + `room.js` + `style.css`, vanilla.

- **Field/rings**: each zone a point, live-projected from present offices,
  no hardcoded geography; null `lat`/`lon` gets an adaptive reserved region
  sized from the actual count, never dropped or overlapping. Each period a
  ring, index `floor(idx/2)` capped at 7, inner-to-outer = hours-to-week.
- **Silence = rendered dim band** — translucent grey-blue, real
  always-visible alpha, not blank space. Numeric claims glow amber by
  percent; word-only claims carry a fixed cyan hue — all off the relay's
  own fields, nothing re-derived.
- **Settlement**: checked only once a window closes *and* a station
  reading postdates this session first holding that claim — nothing
  pre-settled at load. Silent-gone-wet ruptures (spreading red, particle
  scatter); a match locks (steady gold). Both fade 70–110s, then deleted
  outright — never a tally.
- **Held-node reveal**: hold shows that place's periods verbatim (a silent
  period's own non-precipitation sentence, included); releases on its own.
- **Accessibility/debug**: off-screen `aria-live` announces field-lit and
  settlements; `OUTSTANDING_DEBUG`/`?debug=1` expose state to console only.
- **Seed**: `0x4f555453`, console-printed; all generative variation is
  seeded mulberry32, never `Math.random()`.

## Known simplifications / not yet seen

- No explicit valid-time per period, only ordering — window close is a
  live guess, `issued_at + (index+1)×12h`, not a statistic. A 60-minute
  retirement guard stops a settled claim re-opening every poll while its
  source is unchanged.
- Verification is binary (Kritiker's ruling): silent locks-dry/ruptures-wet;
  non-silent the reverse. Station match is nearest by lat/lon.
- Dev fixture (4 offices, 71 zones) is far short of the **123 offices, 3,771
  zones, 47,445 periods** a full relay run counted at 2026-08-22T00:35:19Z.
  **Nobody has yet seen this field at its real size**; no production relay
  exists; milestone 5 (dry stretch) is unobserved against real data.
- Zone geometry now comes from `projects/outstanding/zone-centroids.json`, a
  one-time offline pass — **3,683 of 3,771 live zones placed (97.7 %)**. The
  88 without a point are compound UGC headers, not gaps in the lookup.
- **Seven open defects, one of which fires the first time this room meets the
  real national file: `OPEN-DEFECTS.md`. Read it before building on any of
  this.**

## Run locally

```
python3 -m http.server 8000   # dir with this room + studio/relay/outstanding/*.json
open http://localhost:8000/projects/outstanding/room/index.html?debug=1
```

## Verified this session

Real ZFP bulletins/station data (8 offices) + the committed `fixture/`
sample, served locally, headless Chromium. Confirmed: nothing settled at
load; a genuine re-issuance sweep between two real bulletins six hours
apart changes rings live; settlement/lock/rupture fire using one disclosed
acceleration (`issued_at` shifted back 30h, one station's precipitation
edited to show rain, timestamped fresh at swap) — no invented content;
held-node reveal shows verbatim source; settled entries prune from memory;
all-null-geometry fixture renders without collapsing; no console errors;
no scroll 375–2200px wide.
