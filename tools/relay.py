#!/usr/bin/env python3
"""relay.py — the instrument OUTSTANDING was HELD on, written on this side of the wall.

The work's origin serves `connect-src 'self'`. A room that settles live public
promises therefore cannot reach the two federal channels it settles them from; it
needs those channels relayed onto its own origin as flat JSON, refreshed in place.
Session 106 asked the team for that relay and named its cost. This file is that
relay, so the ask costs a review rather than a build — and so the cost figures in
the ask can be corrected by measurement instead of estimated again.

Two channels, two hosts, and the second one was not named in the request:

  CLAIMS  api.weather.gov          — the Zone Forecast Product, the plain-language
          forecast a person actually reads. `/products?type=ZFP&start=<iso>` returns
          only what has been re-issued since an instant (6 kB for 25 minutes of the
          nation), and `/products/<id>` returns one bulletin's full text.
  SKY     aviationweather.gov      — hourly station observations (METAR), the record
          that answers the promise. Present weather arrives already parsed by the
          provider as `wxString`; this file never parses a raw observation itself.

Three modes:

    python3 tools/relay.py --atlas   OUT_DIR   # once: offices, their places, their stations
    python3 tools/relay.py --cycle   OUT_DIR   # one relay cycle: claims.json + sky.json
    python3 tools/relay.py --measure           # print the true per-cycle cost, fetch nothing else

THE COLD START, which nobody wrote down until 2026-08-23 and which changes what the
room is looking at. `claims.json` is NOT a snapshot of the country; it is an
accumulation. Each cycle merges the bulletins re-issued since an instant into what the
file already held, and drops periods whose window has closed. A relay switched on with
no `claims.json` beside it therefore knows only the handful of offices that happened to
re-draft in the last few minutes — twelve of 125 on the first cycle of 2026-08-23 — and
fills toward the whole record over roughly half a day, as every office re-issues on its
own clock. Left to itself that is a room drawing a country it has not been told about.

So a cold start asks for twelve hours instead of twenty-five minutes: 155 requests and
7.9 MB, once, measured 2026-08-23, and the file lands whole — 123 offices, 25,738 claim
sentences, 46,739 forecast periods standing open, 5.5 MB raw and 275 kB gzipped. That is
automatic: the absence of `claims.json` is the signal, `--prime N` overrides the width,
and the printed report says which of the two happened. What a relay costs its services
on the first minute is not what it costs them on the second.

WHAT THIS FILE WILL NOT DO. It will not condense a claim. Periods are deduplicated
inside a bulletin by exact string identity of (period name, sentence) and carry the
count of zones that share them; nothing is averaged, ranked or summarised, and the
sentence travels verbatim because the gate bound it: "the one unit the stranger owns
must be reachable in the room."

TRAPS MET WHILE WRITING IT, each one recorded rather than quietly routed around:

  * `/products/types/ZFP` accepts NO query parameters — `start`, `limit` and `end`
    all return 400 "not recognized". The filterable endpoint is `/products?type=ZFP`.
    The difference is 1.9 MB per cycle against 6 kB.
  * The METAR endpoint caps every response at 400 records and says nothing about it.
    A single national bbox looks like a complete answer and is a quarter of one.
  * An `ids=` list longer than roughly 2,100 characters does not error: it returns
    two records. Silent truncation, so this file uses bounded bboxes instead.
  * `reportTime` is not the observation's time (session 106 lost a figure to it).
    `obsTime` is the epoch of the observation; that is what this file writes.
"""

import argparse
import datetime
import json
import math
import os
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "(frankbueltge.de/studio, ensemble@studio.invalid)"

PRODUCTS = "https://api.weather.gov/products"
ZONES = "https://api.weather.gov/zones?type=public"
METAR = "https://aviationweather.gov/api/data/metar"

# An office arrives on the claims channel as an ICAO station id and is looked up in the
# atlas under the id its own zone metadata uses. For the continental offices the two
# coincide by accident of the K prefix — KOAX, last three OAX, and the zones say OAX —
# and for Alaska and Hawaii the P prefix does the same. For two offices it is not an
# accident and the two names simply differ, so their promises were being filed under a
# key no atlas entry answers to and dropped without a trace. Found 2026-08-23 by running
# the relay whole for the first time and asking which offices the room could not draw.
#
#   TJSJ -> SJU   San Juan. 15 zones, 176 open claims, Puerto Rico and the Virgin
#                 Islands entire, absent from the room since the room existed.
#   NSTU -> PPG   Pago Pago. 1 zone, 8 open claims. American Samoa's forecasts do
#                 arrive on this channel — session 107 recorded only that no station
#                 there answers them, which is true and is a different sentence.
#
# Keyed by the full id rather than the three-letter tail, so a future office whose tail
# happens to collide with one of these cannot inherit the alias by accident.
OFFICE_ALIAS = {"TJSJ": "SJU", "NSTU": "PPG"}

# Bounded boxes that between them cover the issuing area of every office that
# publishes this product. Every box is small enough that the endpoint's silent
# 400-record cap does not bite; `--measure` re-checks that on every run, because a
# box that starts returning 400 has started lying.
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

UGC = re.compile(r"^([A-Z]{2}Z\d{3}(?:[->][0-9A-Z]+)*)-\d{6}-$")
PERIOD = re.compile(r"^\.([A-Z][A-Za-z0-9 .'/]{1,45}?)\.\.\.")
PCT = re.compile(r"(\d{1,3})\s*percent", re.I)
WEEKDAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# The service's own precipitation vocabulary. Presence of any of these is what makes
# a period a claim about rain rather than a silence. No weighting is attached to any
# of them here: the gate forbids an archive-derived figure reaching the rendering,
# and a table of word-to-probability is exactly that.
PRECIP_WORDS = (
    "rain", "shower", "showers", "thunderstorm", "thunderstorms", "tstms", "snow",
    "drizzle", "sleet", "flurries", "precipitation", "storms", "hail", "wintry",
    "freezing", "sprinkles", "graupel", "squall", "squalls", "ice pellets",
)
PRECIP_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in PRECIP_WORDS) + r")\b", re.I)

# METAR present-weather tokens that mean water is arriving at the station now. The
# provider hands us `wxString` already parsed; this set only decides whether what it
# handed us settles a promise about rain.
WET_RE = re.compile(r"(RA|SN|DZ|SG|PL|GR|GS|IC|UP|TS|SH)")

_STATS = {"requests": 0, "bytes": 0}


def get(url, timeout=90, tries=3, accept="application/json"):
    """One GET, counted. Retries only on transport failure, never on a 4xx."""
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as fh:
                raw = fh.read()
            _STATS["requests"] += 1
            _STATS["bytes"] += len(raw)
            return raw
        except urllib.error.HTTPError as exc:
            # The service answers a rate limit with 403 and a reference id, not 429.
            # Retrying a 403 quickly is how a polite client becomes an impolite one.
            raise RuntimeError(f"HTTP {exc.code} on {url}: {exc.read()[:200]!r}") from exc
        except Exception as exc:  # transport only
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"unreachable after {tries} tries: {url}: {last}")


def get_json(url, **kw):
    return json.loads(get(url, **kw))


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# --------------------------------------------------------------------- the atlas

def build_atlas(out_dir):
    """Where the offices are, and which stations can answer for them.

    Geography, not a claim: it changes when a zone is redrawn, not when the weather
    does, so it is built once and committed beside the work rather than relayed.
    An office's place is the mean position of the stations its own zones name.
    """
    zones = get_json(ZONES, timeout=180)["features"]
    stations = {}
    tiles_used = []
    for tile in TILES:
        url = f"{METAR}?format=json&hours=3&bbox={tile[0]},{tile[1]},{tile[2]},{tile[3]}"
        rows = json.loads(get(url))
        tiles_used.append((tile, len(rows)))
        for row in rows:
            sid, lat, lon = row.get("icaoId"), row.get("lat"), row.get("lon")
            if sid and lat is not None and lon is not None:
                stations[sid] = (round(float(lat), 4), round(float(lon), 4))

    offices = {}
    for feat in zones:
        props = feat["properties"]
        cwa = (props.get("cwa") or [None])[0]
        if not cwa:
            continue
        rec = offices.setdefault(cwa, {"zones": 0, "stations": set(), "tz": {}})
        rec["zones"] += 1
        for tz in props.get("timeZone") or []:
            rec["tz"][tz] = rec["tz"].get(tz, 0) + 1
        for url in props.get("observationStations") or []:
            sid = url.rsplit("/", 1)[-1]
            if sid in stations:
                rec["stations"].add(sid)

    atlas = {"built": iso(utcnow()),
             "source": {"zones": ZONES, "stations": METAR},
             "note": "office position is the mean of the stations its own zones name",
             "offices": {}}
    for cwa, rec in sorted(offices.items()):
        sids = sorted(rec["stations"])
        if sids:
            lat = sum(stations[s][0] for s in sids) / len(sids)
            # Longitude must be averaged on the circle, not the number line. An
            # office whose stations straddle the antimeridian — Guam's three
            # Marianas fields sit near +145, and its zones also name a Honolulu
            # station near -158 — averages arithmetically to a meaningless value
            # (Guam came out at lon 69.4, an ocean south of India, and was drawn
            # in Puerto Rico's corner). The circular mean puts it back in the
            # Pacific. For any office whose stations do not cross ±180 the
            # circular mean equals the arithmetic one, so no CONUS office moves.
            sx = sum(math.cos(math.radians(stations[s][1])) for s in sids)
            sy = sum(math.sin(math.radians(stations[s][1])) for s in sids)
            lon = math.degrees(math.atan2(sy, sx)) if (sx or sy) else None
        else:
            lat = lon = None
        tz = max(rec["tz"], key=rec["tz"].get) if rec["tz"] else "UTC"
        atlas["offices"][cwa] = {
            "lat": None if lat is None else round(lat, 3),
            "lon": None if lon is None else round(lon, 3),
            "tz": tz, "zones": rec["zones"], "stations": sids,
        }
    placed = sum(1 for o in atlas["offices"].values() if o["lat"] is not None)
    atlas["counts"] = {"offices": len(atlas["offices"]), "placed": placed,
                       "zones": len(zones), "stations": len(stations)}
    write_atomic(os.path.join(out_dir, "atlas.json"), atlas)
    print(f"atlas: {len(atlas['offices'])} offices ({placed} placed), "
          f"{len(zones)} zones, {len(stations)} stations, "
          f"{_STATS['requests']} requests, {_STATS['bytes']} bytes")
    capped = [t for t, n in tiles_used if n >= 400]
    if capped:
        print(f"WARNING: {len(capped)} tile(s) hit the silent 400-record cap: {capped}")
    return atlas


# ------------------------------------------------------------------- the claims

def zone_blocks(text):
    """Split one bulletin into zone blocks, each with its periods. Structure only."""
    lines = text.split("\n")
    blocks, cur, i = [], None, 0
    while i < len(lines):
        raw = lines[i].rstrip()
        m_ugc = UGC.match(raw.strip())
        if m_ugc:
            if cur:
                blocks.append(cur)
            cur = {"ugc": m_ugc.group(1), "periods": []}
            i += 1
            continue
        m_per = PERIOD.match(raw)
        if m_per and cur is not None:
            label = m_per.group(1).strip().upper()
            body, j = [raw[m_per.end():]], i + 1
            while j < len(lines):
                nxt = lines[j]
                if PERIOD.match(nxt) or UGC.match(nxt.strip()) or nxt.strip() == "$$":
                    break
                body.append(nxt)
                j += 1
            cur["periods"].append((label, " ".join(" ".join(body).split())))
            i = j
            continue
        i += 1
    if cur:
        blocks.append(cur)
    return blocks


def window(label, issued, tz_offset_hours):
    """Resolve a period label onto a UTC window.

    The product names its periods in words, not timestamps. The service's own day
    period runs roughly 06:00–18:00 local and its night period 18:00–06:00; that
    convention is what is applied here, and it is an approximation of a boundary the
    product does not state. A label this cannot resolve returns None and the period
    travels with a null window rather than a guessed one.
    """
    lab = label.strip().upper()
    local = issued + datetime.timedelta(hours=tz_offset_hours)
    day = local.date()
    kind = None
    if lab in ("TODAY", "THIS AFTERNOON", "REST OF TODAY", "THIS MORNING"):
        kind = "day"
    elif lab in ("TONIGHT", "REST OF TONIGHT", "OVERNIGHT"):
        kind = "night"
    else:
        for idx, name in enumerate(WEEKDAYS):
            delta = (idx - day.weekday()) % 7
            if lab == name:
                day, kind = day + datetime.timedelta(days=delta or 7), "day"
                break
            if lab == f"{name} NIGHT":
                day, kind = day + datetime.timedelta(days=delta or 7), "night"
                break
    if kind is None:
        return None, None
    if kind == "day":
        start_local = datetime.datetime.combine(day, datetime.time(6, 0))
        end_local = datetime.datetime.combine(day, datetime.time(18, 0))
    else:
        start_local = datetime.datetime.combine(day, datetime.time(18, 0))
        end_local = start_local + datetime.timedelta(hours=12)
    off = datetime.timedelta(hours=tz_offset_hours)
    return (start_local - off).replace(tzinfo=datetime.timezone.utc), \
           (end_local - off).replace(tzinfo=datetime.timezone.utc)


TZ_OFFSET = {  # standard-time offsets; the product's own periods are coarser than DST
    "America/New_York": -4, "America/Detroit": -4, "America/Kentucky/Louisville": -4,
    "America/Indiana/Indianapolis": -4, "America/Toronto": -4,
    "America/Chicago": -5, "America/Menominee": -5, "America/North_Dakota/Center": -5,
    "America/Indiana/Knox": -5, "America/Winnipeg": -5,
    "America/Denver": -6, "America/Boise": -6, "America/Phoenix": -7,
    "America/Los_Angeles": -7, "America/Anchorage": -8, "America/Juneau": -8,
    "America/Nome": -8, "America/Adak": -9, "Pacific/Honolulu": -10,
    "America/Puerto_Rico": -4, "Pacific/Guam": 10, "Pacific/Pago_Pago": -11,
}


def parse_bulletin(text, tz):
    """One bulletin -> its distinct claims, deduplicated by exact string identity."""
    off = TZ_OFFSET.get(tz, 0)
    seen = {}
    order = []
    zones = 0
    for block in zone_blocks(text):
        zones += 1
        for label, sentence in block["periods"]:
            if not sentence:
                continue
            key = (label, sentence)
            if key not in seen:
                pcts = [int(x) for x in PCT.findall(sentence)]
                seen[key] = {"p": label, "t": sentence,
                             "n": max(pcts) if pcts else None,
                             "w": bool(PRECIP_RE.search(sentence)),
                             "z": 0}
                order.append(key)
            seen[key]["z"] += 1
    return [seen[k] for k in order], zones


def cycle_claims(out_dir, since_minutes, atlas):
    """One claims cycle: what has been re-issued since, in full, verbatim."""
    since = utcnow() - datetime.timedelta(minutes=since_minutes)
    index = get_json(f"{PRODUCTS}?type=ZFP&start={urllib.parse.quote(iso(since))}")
    graph = index.get("@graph") or []

    prev_path = os.path.join(out_dir, "claims.json")
    prev = {}
    if os.path.exists(prev_path):
        try:
            prev = json.load(open(prev_path, encoding="utf-8")).get("offices", {})
        except (ValueError, OSError):
            prev = {}

    newest = {}
    for prod in graph:
        office = OFFICE_ALIAS.get(prod.get("issuingOffice") or "",
                                  (prod.get("issuingOffice") or "")[-3:])
        if not office:
            continue
        cur = newest.get(office)
        if cur is None or prod["issuanceTime"] > cur["issuanceTime"]:
            newest[office] = prod

    offices = dict(prev)
    fetched = 0
    tz_unknown = []
    for office, prod in sorted(newest.items()):
        if prev.get(office, {}).get("issued") == prod["issuanceTime"]:
            continue
        text = get_json(f"{PRODUCTS}/{prod['id']}").get("productText") or ""
        fetched += 1
        entry = atlas.get("offices", {}).get(office) or {}
        tz = entry.get("tz") or "UTC"
        if not entry.get("tz"):
            # An office the atlas cannot place in its own hours. TODAY and TONIGHT are
            # local words; read against UTC they name the wrong twelve hours. The claim
            # still travels verbatim and the window is still written, because a room that
            # is told nothing about an office draws it bare — but the office is named in
            # the file and in the report, so a wrong window is never a silent one.
            tz_unknown.append(office)
        claims, zones = parse_bulletin(text, tz)
        issued = datetime.datetime.fromisoformat(prod["issuanceTime"])
        for claim in claims:
            start, end = window(claim["p"], issued.astimezone(datetime.timezone.utc),
                                TZ_OFFSET.get(tz, 0))
            claim["s"] = iso(start) if start else None
            claim["e"] = iso(end) if end else None
        offices[office] = {"issued": prod["issuanceTime"], "zones": zones,
                           "claims": claims}

    now = utcnow()
    live = {}
    for office, rec in offices.items():
        kept = [c for c in rec["claims"] if not c.get("e") or c["e"] >= iso(now)]
        if kept:
            live[office] = {"issued": rec["issued"], "zones": rec["zones"], "claims": kept}

    doc = {
        "generated": iso(now),
        "source": PRODUCTS + "?type=ZFP",
        "licence": "United States Government work, public domain",
        "note": ("periods deduplicated inside a bulletin by exact identity of "
                 "(period name, sentence); z is the number of zones sharing it; "
                 "the sentence is verbatim and is never summarised"),
        "fields": {"p": "period name", "t": "claim sentence, verbatim",
                   "n": "stated percent, null where none", "w": "names precipitation",
                   "z": "zones sharing this exact sentence",
                   "s": "window start, UTC", "e": "window end, UTC"},
        "counts": {"offices": len(live),
                   "claims": sum(len(o["claims"]) for o in live.values()),
                   "periods": sum(c["z"] for o in live.values() for c in o["claims"]),
                   "numeric": sum(c["z"] for o in live.values()
                                  for c in o["claims"] if c["n"] is not None),
                   "silent": sum(c["z"] for o in live.values()
                                 for c in o["claims"] if not c["w"]),
                   "reissued": fetched,
                   "tz_unknown": len(tz_unknown)},
        "tz_unknown": sorted(tz_unknown),
        "offices": live,
    }
    write_atomic(os.path.join(out_dir, "claims.json"), doc)
    return doc


# ---------------------------------------------------------------------- the sky

def cycle_sky(out_dir):
    """One sky cycle: every reporting station, and what it says is falling."""
    latest = {}
    capped = []
    failed = []
    for tile in TILES:
        url = f"{METAR}?format=json&hours=1&bbox={tile[0]},{tile[1]},{tile[2]},{tile[3]}"
        try:
            rows = json.loads(get(url))
        except (ValueError, OSError) as err:
            # This service answers a bad minute with something that is not JSON, and one
            # such minute used to end the whole cycle in a traceback — in a relay meant to
            # run unattended for months, a scheduled run that dies leaves the room reading
            # a file nobody is updating. One box is one corner of the sky: it is dropped,
            # named, and the rest of the country is still written.
            failed.append({"bbox": list(tile), "error": err.__class__.__name__})
            continue
        if len(rows) >= 400:
            capped.append(tile)
        for row in rows:
            sid = row.get("icaoId")
            if not sid or row.get("lat") is None:
                continue
            cur = latest.get(sid)
            if cur is None or (row.get("obsTime") or 0) > cur.get("obsTime", 0):
                latest[sid] = row

    stations, wet = {}, 0
    for sid, row in sorted(latest.items()):
        wx = row.get("wxString") or ""
        rec = {"la": round(float(row["lat"]), 3), "lo": round(float(row["lon"]), 3),
               "t": int(row.get("obsTime") or 0)}
        if wx:
            rec["w"] = wx
            if WET_RE.search(wx):
                rec["r"] = 1
                wet += 1
        if row.get("precip") is not None:
            rec["p"] = row["precip"]
        stations[sid] = rec

    doc = {
        "generated": iso(utcnow()),
        "source": METAR,
        "licence": "United States Government work, public domain",
        "note": ("present weather is the provider's own parsed wxString, never "
                 "re-parsed here; t is obsTime, the observation's epoch, and not "
                 "reportTime, which is not the observation's time"),
        "fields": {"la": "latitude", "lo": "longitude", "t": "observation epoch",
                   "w": "present weather, verbatim", "r": "1 where that names falling water",
                   "p": "precipitation reported by the provider, where present"},
        "counts": {"stations": len(stations), "reporting_weather":
                   sum(1 for s in stations.values() if "w" in s), "wet": wet,
                   "boxes": len(TILES), "boxes_failed": len(failed)},
        "stations": stations,
    }
    if capped:
        doc["warning"] = f"{len(capped)} tiles hit the 400-record cap: {capped}"
    if failed:
        doc["unanswered"] = failed
    if len(failed) == len(TILES):
        # Not one corner of the sky answered. A file of no observations is not a sky
        # with nothing falling in it, and the last good file is better than that lie.
        raise RuntimeError("relay: every observation box failed; sky.json left untouched")
    write_atomic(os.path.join(out_dir, "sky.json"), doc)
    return doc


# --------------------------------------------------------------------- plumbing

def write_atomic(path, doc):
    """A bad cycle must never destroy the last good file. Write, then rename."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, separators=(",", ":"), sort_keys=False)
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--atlas", metavar="OUT_DIR")
    ap.add_argument("--cycle", metavar="OUT_DIR")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--since", type=int, default=25,
                    help="minutes of re-issuance to ask for on a warm run (default 25)")
    ap.add_argument("--prime", type=int, default=720,
                    help="minutes to ask for on a COLD start — no claims.json beside the "
                         "output yet (default 720, twelve hours, one full re-issuance "
                         "round). Pass --prime 25 to refuse the backfill and let the "
                         "room fill in front of whoever is watching.")
    ap.add_argument("--atlas-file", default=None)
    args = ap.parse_args()

    started = time.time()
    if args.atlas:
        os.makedirs(args.atlas, exist_ok=True)
        build_atlas(args.atlas)
    elif args.cycle or args.measure:
        out = args.cycle or os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                         "..", "projects", "outstanding", "room", "data")
        out = os.path.normpath(out)
        os.makedirs(out, exist_ok=True)
        atlas_path = args.atlas_file or os.path.join(out, "atlas.json")
        # The eighth trap, met on 2026-08-25 and it cost a whole night's record. A cycle
        # run beside no atlas used to fall back to an empty one, and an empty atlas means
        # every office is read in UTC: TODAY and TONIGHT are local words, so every window
        # in the file lands on 06:00Z/18:00Z and is wrong by up to ten hours — for all 123
        # offices at once, in a file that looks complete and warns about nothing. A relay
        # that cannot place its offices in their own hours does not write; it says so.
        if not os.path.exists(atlas_path):
            raise SystemExit(
                f"relay: no atlas at {atlas_path}. Without it every forecast window would "
                f"be written in UTC and be wrong for every office. Run --atlas first, or "
                f"pass --atlas-file.")
        atlas = json.load(open(atlas_path, encoding="utf-8"))
        # A cold start is not a cycle. With no claims.json beside the output there is
        # nothing to merge into, and twenty-five minutes of re-issuance would hand the
        # room a dozen offices and call it the country. The absence of the file is the
        # signal; the report below says which of the two this run was.
        cold = not os.path.exists(os.path.join(out, "claims.json"))
        since = args.prime if cold else args.since
        claims = cycle_claims(out, since, atlas)
        sky = cycle_sky(out)
        elapsed = time.time() - started
        print(json.dumps({
            "claims": claims["counts"], "sky": sky["counts"],
            "cost": {"cold_start": cold, "since_minutes": since,
                     "requests": _STATS["requests"], "bytes_in": _STATS["bytes"],
                     "seconds": round(elapsed, 1),
                     "claims_bytes_out": os.path.getsize(os.path.join(out, "claims.json")),
                     "sky_bytes_out": os.path.getsize(os.path.join(out, "sky.json"))},
        }, indent=2))
    else:
        ap.error("one of --atlas, --cycle or --measure is required")
    return 0


if __name__ == "__main__":
    sys.exit(main())
