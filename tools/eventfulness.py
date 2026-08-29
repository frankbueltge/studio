#!/usr/bin/env python3
"""What the room has to show a visitor who stands in front of it — measured, not hoped.

WHY THIS EXISTS. Milestone 5 of OUTSTANDING has two limbs: *the screen never becomes a
finished tally* (evidenced 2026-08-26) and *afterglow always fading* (failed the same
night, at 34 of 200 sampled instants, longest gap 17 minutes). The house refused to
re-read the milestone to pass it and named the reason beside the null: at 04:55Z the
country held 1,237 reporting stations, 44 of them wet, and 3 with an observation under ten
minutes old. That was one instant of one night. This instrument asks the question the
whole day answers.

WHAT AN EVENT ACTUALLY IS, read out of `index.html` rather than assumed. `settle()` fires
in exactly two ways:

  1. a wet observation lands inside a forecast period the room is holding, and the room
     may call it an event only if that observation is younger than the door opening
     (`obs.t > openedAt`) — otherwise the claim is removed silently, `unwitnessed`;
  2. a period's window ends while the room has held it *from its own beginning*
     (`item.start >= openedAt`).

Every window in this record is twelve hours long (session 110, footnoted 2026-08-28 for
the two nights a year a zone changes offset). So (2) cannot fire in under twelve hours of
continuous room time — never, not rarely — and every *settlement* a visitor can possibly
see is of kind (1). **The room's visit-scale settlement rate is therefore exactly the
national arrival rate of fresh wet observations, one per office per period.** That is a
fact about the sky, and it is measurable.

WHAT THIS DELIBERATELY DOES NOT COUNT, said here because the first draft of this file
claimed it did. `rebuild()` also pushes two marks that are drawn and are not settlements:
a `sweep` when an office re-issues its bulletin (a radial line, 1.6 s) and a `heard` when
the room learns of an office for the first time (a ring, 2.2 s). They carry no verdict, no
colour and no sound, and they are excluded from `fading` in `tools/watch.mjs` because
milestone 5's limb is about the afterglow of *adjudication*. A room this instrument reports
as having nothing to settle is therefore not necessarily a still picture — re-issuance runs
at its own rate, measured separately — and no number below should be read as one.

WHAT IT MEASURES. Every observation the national network filed over the last N hours,
fetched whole; the wet ones, by the relay's own test, mapped to their office by the relay's
own atlas; the first wet observation per office per forecast period, which is the only one
that can fire because the room settles a period once. Then rooms are opened at every
five-minute offset across the span and each is asked what it would have had to show in its
first ten, twenty and sixty minutes.

THE MODEL, STATED SO IT CAN BE ATTACKED — AND IT WAS, AGAINST THE ROOM ITSELF. A room
opened at T0 flares for (office, period) iff a wet observation falls in that period after
T0, AND the sky was not already speaking for that office when the door opened: `absorbSky()`
takes the current sky at the door and `settle()` removes anything it finds there in silence.
"Already speaking" is exact where the timeline carries every report instant — the wet report
must still be that station's LATEST at T0, because `sky.json` holds only each station's
latest — and approximate on an older timeline, where any wet report inside SNAP minutes
counts and a station that has since reported clear is wrongly taken as still raining.

No room is simulated inside the first SNAP minutes of the span, because a door the data
cannot reach behind cannot be judged.

CHECKED AGAINST THE ROOM, 2026-08-29: for the room actually watched for 95 minutes from
04:40Z, the model named **eight** office-periods and the room drew **nine** — the eight
exactly, plus one (DLH) the model wrongly excluded at the door for the approximate reason
above. Before the span guard the same data predicted sixteen, seven of which were offices
whose rain had begun before the sweep's own first record.

WHAT IT DOES NOT DO. It does not judge, and it does not model sound, brightness or the
face. It counts what the sky offered and what the room's own rules would have made of it.

    python3 tools/eventfulness.py --hours 6 --out DIR [--claims FILE] [--atlas FILE]

Written 2026-08-29 (session 113). Stdlib only, like the relay it borrows from.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

METAR = "https://aviationweather.gov/api/data/metar"
UA = "(frankbueltge.de/studio, ensemble@studio.invalid)"

# The relay's own test for falling water. Imported by copy rather than by import so this
# instrument can be run against a record the relay wrote on another machine, but it is the
# same expression and a divergence between them is a defect in this file.
WET_RE = re.compile(r"(RA|SN|DZ|SG|PL|GR|GS|IC|UP|TS|SH)")

# The relay's calibrated boxes, as the starting partition. Any box that hits the service's
# silent 400-record cap over a long window is quartered until it does not — the cap is the
# second trap in tools/RELAY.md and a capped response looks exactly like a quiet corner.
TILES = [
    (24.0, -126.0, 33.0, -115.0), (33.0, -126.0, 42.0, -115.0),
    (24.0, -115.0, 33.0, -104.0), (33.0, -115.0, 42.0, -104.0),
    (24.0, -104.0, 33.0, -96.0), (33.0, -104.0, 42.0, -96.0),
    (24.0, -96.0, 30.0, -88.0), (30.0, -96.0, 36.0, -88.0),
    (36.0, -96.0, 42.0, -88.0),
    (24.0, -88.0, 30.0, -80.0), (30.0, -88.0, 33.0, -84.0),
    (30.0, -84.0, 33.0, -80.0), (33.0, -88.0, 36.0, -84.0),
    (33.0, -84.0, 36.0, -80.0), (36.0, -88.0, 42.0, -80.0),
    (24.0, -80.0, 33.0, -66.0), (33.0, -80.0, 39.0, -70.0),
    (39.0, -80.0, 42.0, -70.0), (39.0, -75.0, 45.0, -66.0),
    (42.0, -126.0, 50.0, -117.0), (42.0, -117.0, 50.0, -108.0),
    (42.0, -108.0, 50.0, -99.0), (42.0, -99.0, 50.0, -90.0),
    (42.0, -90.0, 50.0, -81.0), (42.0, -81.0, 50.0, -70.0),
    (51.0, -180.0, 62.0, -150.0), (51.0, -150.0, 72.0, -129.0),
    (62.0, -180.0, 72.0, -150.0),
    (17.0, -162.0, 23.0, -153.0), (17.0, -68.0, 19.0, -64.0),
    (12.0, 143.0, 16.0, 146.0),
]

CAP = 400          # the service's undocumented per-response record cap
MAX_DEPTH = 4      # a box quartered four times is 1/256 of its area; beyond that, report
MAX_REQUESTS = 400  # a hard stop, so a bug here cannot become a hammering of a public service


def get(url, tries=3, timeout=120):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as fh:
                return fh.read()
        except (urllib.error.URLError, OSError, TimeoutError) as err:
            last = err
            time.sleep(2 * (attempt + 1))
    raise last


def sweep(hours, log):
    """Every observation filed in the last `hours`, with no box left capped."""
    seen = {}          # (station, obsTime) -> row, so overlapping boxes cannot double-count
    stats = {"requests": 0, "bytes": 0, "boxes": 0, "split": 0, "capped_at_depth": [],
             "failed": []}
    queue = [(t, 0) for t in TILES]
    while queue:
        (lat0, lon0, lat1, lon1), depth = queue.pop()
        if stats["requests"] >= MAX_REQUESTS:
            raise RuntimeError(f"eventfulness: request ceiling {MAX_REQUESTS} reached; "
                               "no figure is worth hammering a public service for")
        url = f"{METAR}?format=json&hours={hours}&bbox={lat0},{lon0},{lat1},{lon1}"
        try:
            raw = get(url)
        except Exception as err:                       # noqa: BLE001 - reported, not swallowed
            stats["failed"].append({"bbox": [lat0, lon0, lat1, lon1],
                                    "error": err.__class__.__name__})
            continue
        stats["requests"] += 1
        stats["bytes"] += len(raw)
        try:
            rows = json.loads(raw)
        except ValueError:
            stats["failed"].append({"bbox": [lat0, lon0, lat1, lon1], "error": "not JSON"})
            continue
        stats["boxes"] += 1
        # A capped response is incomplete, not false: its 400 records are real
        # observations. The first draft threw them away and re-fetched the same sky in
        # four pieces, which is how a twelve-hour sweep walked into its own request
        # ceiling. They are kept and deduplicated by (station, observation instant).
        for row in rows:
            sid, t = row.get("icaoId"), row.get("obsTime")
            if sid and t:
                seen[(sid, int(t))] = row
        if len(rows) >= CAP and depth < MAX_DEPTH:
            # Capped: this box is telling us about a fraction of itself and saying nothing
            # about it. Quarter it. The four children overlap on no interior point.
            stats["split"] += 1
            mlat, mlon = (lat0 + lat1) / 2, (lon0 + lon1) / 2
            queue += [((lat0, lon0, mlat, mlon), depth + 1),
                      ((mlat, lon0, lat1, mlon), depth + 1),
                      ((lat0, mlon, mlat, lon1), depth + 1),
                      ((mlat, mlon, lat1, lon1), depth + 1)]
            continue
        if len(rows) >= CAP:
            stats["capped_at_depth"].append([lat0, lon0, lat1, lon1])
        log(f"  {len(rows):4d} records  depth {depth}  "
            f"[{lat0},{lon0},{lat1},{lon1}]  total {len(seen)}")
        time.sleep(0.25)   # the service asks for nothing; this house paces anyway
    return seen, stats


def load_periods(claims, back_to=None):
    """Per office: the forecast periods it is standing behind, with their windows.

    AND THE ONES IT WAS STANDING BEHIND EARLIER TONIGHT, which is not the same thing and
    was the first draft's worst error. `cycle_claims` keeps only claims whose window has
    not yet closed (`c["e"] >= now`), so tonight's record cannot describe a room opened
    twelve hours ago: every period that closed in between is simply absent from the file,
    and a simulation reading it would report those rooms as having had nothing to settle.

    The windows tile time on the office's own 06:00/18:00 local boundaries, so the closed
    ones can be reconstructed backwards from the earliest open one in twelve-hour steps —
    exact except across a zone's two offset changes a year, where a window is eleven or
    thirteen hours (tenth trap, `tools/RELAY.md`). What cannot be reconstructed is what
    those closed periods SAID: whether each named rain is not derivable from anything in
    the file, so a reconstructed period carries `w: None` and any event landing in one is
    counted but not typed.
    """
    out = {}
    for oid, rec in claims["offices"].items():
        periods = []
        for c in rec["claims"]:
            if not c.get("s") or not c.get("e"):
                continue          # a period the relay could not place in time; null window
            s = int(dt.datetime.fromisoformat(c["s"].replace("Z", "+00:00")).timestamp())
            e = int(dt.datetime.fromisoformat(c["e"].replace("Z", "+00:00")).timestamp())
            periods.append({"p": c["p"], "s": s, "e": e, "w": bool(c.get("w")),
                            "n": c.get("n"), "virtual": False})
        periods.sort(key=lambda p: p["s"])
        if periods and back_to is not None:
            s = periods[0]["s"]
            while s > back_to:
                s -= 12 * 3600
                periods.insert(0, {"p": "(closed before the record was written)", "s": s,
                                   "e": s + 12 * 3600, "w": None, "n": None,
                                   "virtual": True})
        out[oid] = periods
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--hours", type=int, default=6)
    ap.add_argument("--out", default=None, help="directory to write the timeline into")
    ap.add_argument("--claims", default="projects/outstanding/room/data/claims.json")
    ap.add_argument("--atlas", default="projects/outstanding/room/data/atlas.json")
    ap.add_argument("--snap", type=int, default=60,
                    help="minutes the opening snapshot is assumed to reach back")
    ap.add_argument("--visit", type=int, nargs="*", default=[10, 20, 60],
                    help="visit lengths in minutes")
    ap.add_argument("--step", type=int, default=5, help="minutes between simulated openings")
    ap.add_argument("--timeline", default=None,
                    help="read a previously written timeline instead of fetching")
    args = ap.parse_args()

    def log(msg):
        print(msg, file=sys.stderr, flush=True)

    atlas = json.load(open(args.atlas, encoding="utf-8"))["offices"]
    claims = json.load(open(args.claims, encoding="utf-8"))

    # station -> office, exactly as the room builds it and not as it ought to be built.
    # `index.html` does `stationOwner.set(s, id)` over `Object.entries(atlas.offices)`, a
    # single-valued map in which the LAST office naming a shared station wins. A station
    # named by two offices' zones can therefore only ever settle one office's claim. The
    # first draft of this file kept both, which invented flares the room cannot draw.
    where = {}
    for oid, rec in atlas.items():
        for sid in rec.get("stations", []):
            where[sid] = [oid]
    shared = sum(1 for rec in atlas.values() for sid in rec.get("stations", [])) - len(where)

    if args.timeline:
        doc = json.load(open(args.timeline, encoding="utf-8"))
        wet, stats, span = doc["wet"], doc["sweep"], doc["span"]
        reports = doc.get("reports") or {}
    else:
        log(f"sweeping {args.hours} h of the national network")
        seen, stats = sweep(args.hours, log)
        wet, times = [], []
        for (sid, t), row in seen.items():
            times.append(t)
            wx = row.get("wxString") or ""
            if wx and WET_RE.search(wx):
                wet.append({"s": sid, "t": t, "w": wx})
        wet.sort(key=lambda r: r["t"])
        # Every report instant per station, wet or dry. Without the dry ones the door test
        # below cannot tell a station that is raining now from one that rained an hour ago
        # and has since reported clear — and the room's opening snapshot holds only each
        # station's LATEST report, so that distinction is the door. Instants only: the rows
        # themselves are not needed and would multiply the file.
        reports = {}
        for (sid, t) in seen:
            reports.setdefault(sid, []).append(int(t))
        for v in reports.values():
            v.sort()
        span = {"from": min(times), "to": max(times), "observations": len(seen),
                "stations": len({s for s, _ in seen})}
        log(f"  {span['observations']} observations, {span['stations']} stations, "
            f"{len(wet)} wet")

    # The periods the record still holds, plus the ones it held earlier in the span and has
    # since dropped, reconstructed backwards on the twelve-hour grid.
    periods = load_periods(claims, back_to=span["from"])
    virtual = sum(1 for ps in periods.values() for p in ps if p["virtual"])

    # HOW MANY MARKS ONE DECISION MAKES. `rebuild()` gives every claim in the bulletin its
    # own item and its own key (`id|issued|k`), and `settle()` walks `node.live`, so a
    # single wet observation settles EVERY claim of that office whose window contains it —
    # one office's rain is a dozen bands going off at once, not one. The first draft
    # counted office-periods and was contradicted within the hour by the room itself,
    # which fired 58 marks in one instant on a night this model called quiet. Both numbers
    # are kept: the sky decides office-periods, the visitor sees bands.
    weight = {}
    for oid, rec in claims["offices"].items():
        per_start = {}
        for c in rec["claims"]:
            if c.get("s"):
                s = int(dt.datetime.fromisoformat(c["s"].replace("Z", "+00:00")).timestamp())
                per_start[s] = per_start.get(s, 0) + 1
        for s, n in per_start.items():
            weight[(oid, s)] = n
        if per_start:                     # for periods reconstructed backwards, the office's
            typical = sorted(per_start.values())[len(per_start) // 2]   # own median band count
            for p in periods.get(oid, []):
                if p["virtual"]:
                    weight[(oid, p["s"])] = typical

    # ---------------------------------------------------------------- the settleable set
    # One wet observation can settle at most one period per office, because the periods
    # tile time and the room settles a key once. So the events the sky offered at all are
    # the FIRST wet observation per (office, period).
    firsts = {}                     # (office, period start) -> {t, kind}
    unplaced = 0
    for obs in wet:
        offs = where.get(obs["s"])
        if not offs:
            unplaced += 1
            continue
        for oid in offs:
            for per in periods.get(oid, []):
                if per["s"] <= obs["t"] <= per["e"]:
                    key = (oid, per["s"])
                    if key not in firsts or obs["t"] < firsts[key]["t"]:
                        firsts[key] = {"t": obs["t"], "office": oid, "period": per["p"],
                                       "kind": ("unknown" if per["w"] is None else
                                                "lock" if per["w"] else "silence"),
                                       "start": per["s"], "end": per["e"]}
                    break

    # Every wet observation per office/period, so a room can be asked whether the sky had
    # already spoken for that office when its door opened.
    by_key = {}
    for obs in wet:
        for oid in where.get(obs["s"], []):
            for per in periods.get(oid, []):
                if per["s"] <= obs["t"] <= per["e"]:
                    by_key.setdefault((oid, per["s"]), []).append((obs["t"], obs["s"]))
                    break
    for v in by_key.values():
        v.sort()

    def wet_at_door(sid, t, t0):
        """Would the room's opening snapshot have carried this wet report?

        Only if it is still that station's LATEST report at the door. With the full report
        instants in hand this is exact; without them (an older timeline) it falls back to
        'any wet report inside the snapshot's reach', which over-counts door settlements
        for a station that has since reported clear — measured against the room on
        2026-08-29 as one office in nine."""
        later = reports.get(sid)
        if later:
            return not any(t < u <= t0 for u in later)
        return True

    # ---------------------------------------------------------------------- simulation
    #
    # A room cannot be simulated at a door the data does not reach behind. To know whether
    # the sky was ALREADY speaking when a room opened, the span must cover the snapshot's
    # own reach before that door; a two-hour sweep asked about a room opened twenty-three
    # minutes into it, on 2026-08-29, and predicted seven flares the room never drew —
    # every one of them an office whose rain had begun before the sweep's own first record.
    # So the first `snap` minutes of the span carry no rooms.
    first_door = span["from"] + args.snap * 60
    t0s = list(range(first_door, span["to"] - max(args.visit) * 60, args.step * 60))
    snap = args.snap * 60
    rooms = []
    for t0 in t0s:
        counts = {v: 0 for v in args.visit}
        bands = {v: 0 for v in args.visit}
        kinds = {"lock": 0, "silence": 0, "unknown": 0}
        first_at = None
        for key, ts in by_key.items():
            per_start = key[1]
            # Was the sky already speaking for this office when the door opened? Then the
            # room removes the claim silently and can never flare for it.
            if any(max(per_start, t0 - snap) <= t <= t0 and wet_at_door(sid, t, t0)
                   for t, sid in ts):
                continue
            after = [t for t, _ in ts if t > t0]
            if not after:
                continue
            t = after[0]
            ev = firsts.get(key)
            for v in args.visit:
                if t <= t0 + v * 60:
                    counts[v] += 1
                    bands[v] += weight.get(key, 1)
            if t <= t0 + max(args.visit) * 60 and ev:
                kinds[ev["kind"]] += 1
            if first_at is None or t < first_at:
                first_at = t
        rooms.append({"t0": t0, "counts": counts, "bands": bands, "kinds": kinds,
                      "wait": None if first_at is None else int((first_at - t0) / 60)})

    def pct(vals, p):
        vals = sorted(vals)
        return vals[min(len(vals) - 1, int(p * len(vals)))] if vals else None

    summary = {}
    for v in args.visit:
        b = [r["bands"][v] for r in rooms]
        summary[f"visit_{v}min_bands"] = {
            "zero_pct": round(100 * sum(1 for x in b if x == 0) / max(1, len(b)), 1),
            "min": min(b) if b else None, "median": pct(b, 0.5), "p90": pct(b, 0.9),
            "max": max(b) if b else None, "mean": round(sum(b) / max(1, len(b)), 1),
        }
        c = [r["counts"][v] for r in rooms]
        summary[f"visit_{v}min"] = {
            "rooms": len(c), "zero": sum(1 for x in c if x == 0),
            "zero_pct": round(100 * sum(1 for x in c if x == 0) / max(1, len(c)), 1),
            "min": min(c) if c else None, "median": pct(c, 0.5), "p90": pct(c, 0.9),
            "max": max(c) if c else None, "mean": round(sum(c) / max(1, len(c)), 2),
        }
    waits = [r["wait"] for r in rooms if r["wait"] is not None]
    summary["wait_for_first_flare_min"] = {
        "rooms_with_one_at_all": len(waits), "median": pct(waits, 0.5),
        "p90": pct(waits, 0.9), "max": max(waits) if waits else None,
    }
    # By hour of the day, in UTC, so the trough can be named rather than felt.
    by_hour = {}
    for r in rooms:
        h = dt.datetime.fromtimestamp(r["t0"], dt.timezone.utc).hour
        by_hour.setdefault(h, []).append(r["counts"][max(args.visit)])
    summary["by_utc_hour"] = {str(h): {"rooms": len(v), "mean": round(sum(v) / len(v), 2),
                                       "min": min(v), "max": max(v)}
                              for h, v in sorted(by_hour.items())}

    # WHEN IN THE HOUR THE SKY SPEAKS. The national observation network does not report
    # continuously: a station files near the end of the hour, and the whole country files
    # at nearly the same time. So the room's settlements do not arrive at a rate, they
    # arrive in a clump, and a visit is inside one or it is not. Ten-minute bins of the
    # minute-of-hour of every wet observation in the span, and of the settleable ones.
    def bins(times):
        b = [0] * 6
        for t in times:
            b[(dt.datetime.fromtimestamp(t, dt.timezone.utc).minute) // 10] += 1
        return b
    summary["wet_by_minute_of_hour"] = bins([o["t"] for o in wet])
    summary["settlements_by_minute_of_hour"] = bins([e["t"] for e in firsts.values()])
    # And the gaps between them, nationally: if the sky speaks once an hour, this is a
    # near-empty histogram with one tall bar and a long tail, not a spread.
    ts = sorted(e["t"] for e in firsts.values())
    gaps = [int((b - a) / 60) for a, b in zip(ts, ts[1:])]
    summary["gap_between_settlements_min"] = {
        "n": len(gaps), "median": pct(gaps, 0.5), "p90": pct(gaps, 0.9),
        "max": max(gaps) if gaps else None,
        "over_3min": sum(1 for g in gaps if g > 3),
        "over_10min": sum(1 for g in gaps if g > 10),
    }

    doc = {
        "measured": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "hours": args.hours, "span": span, "sweep": stats,
        "record": {"claims_generated": claims["generated"],
                   "offices": claims["counts"]["offices"],
                   "periods": claims["counts"]["periods"]},
        "model": {"snapshot_reach_minutes": args.snap, "step_minutes": args.step,
                  "first_door": first_door, "rooms": len(rooms),
                  "door_rule": ("exact (every report instant known)" if reports
                                else "approximate (wet reports only; over-counts the door)"),
                  "visits": args.visit,
                  "note": ("a settlement is a wet observation arriving after the door "
                           "opened, inside a period no wet observation had already been "
                           "seen in; earliest-in-window decides, as the room does from "
                           "2026-08-29. Re-issuance sweeps and first-hearings are drawn "
                           "by the room and are NOT counted here")},
        "wet_observations": len(wet), "wet_unplaced_stations": unplaced,
        "settleable_office_periods": len(firsts),
        "periods_reconstructed": virtual,
        "stations_shared_between_offices": shared,
        "kinds": {k: sum(1 for e in firsts.values() if e["kind"] == k)
                  for k in ("lock", "silence", "unknown")},
        "summary": summary,
    }
    print(json.dumps(doc, indent=2))
    if args.out:
        os.makedirs(args.out, exist_ok=True)
        with open(os.path.join(args.out, "timeline.json"), "w", encoding="utf-8") as fh:
            json.dump({"span": span, "sweep": stats, "wet": wet, "reports": reports}, fh)
        with open(os.path.join(args.out, "eventfulness.json"), "w", encoding="utf-8") as fh:
            json.dump({**doc, "rooms": rooms,
                       "events": sorted(firsts.values(), key=lambda e: e["t"])}, fh, indent=1)


if __name__ == "__main__":
    main()
