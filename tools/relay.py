#!/usr/bin/env python3
"""Relay: mirror two live public-forecast facts onto the work's own origin.

The work runs under `connect-src 'self'` and cannot call the public weather API from
the browser. This instrument runs outside the browser, on a schedule, and writes two
small JSON files that the work's own origin then serves as static files:
`forecasts.json` (every open period of every currently-issued Zone Forecast Product) and
`stations.json` (a national sample of live station observations).

Both files it reads are plain HTTPS GET against `https://api.weather.gov`:

  index      /products/types/ZFP                          latest ~5000 product headers
  product    /products/{id}                                one bulletin's full text
  stations   /stations?id=A,B,C                            station metadata incl. lat/lon
  obs        /stations/{id}/observations/latest             one station's latest reading
  zone geom  /zones/forecast/{UGC}                          one zone's polygon (optional, costly)

Five things found running against the live service tonight, each the hard way:

1. OFFICE COUNT IS 123, NOT 126. `/products/types/ZFP/locations` lists 126 codes, but
   several are forecast-AREA subdivisions that share one physical issuing office (AER
   and ALU both issue as PAFC; NSB and WCZ both issue as PAFG; PR issues as TJSJ; PPG
   issues as NSTU) — 126 collapses to 123 once you count by the `issuingOffice` that
   actually appears on issued bulletins. This instrument never reads that 126-entry
   registry at all: it discovers offices ONLY from `issuingOffice` values that appear on
   real, currently-issued products in the national index, which sidesteps the trap
   entirely and was cross-checked stable (123, both a 5-day window and the trailing 24h).
   A companion trap that this therefore never hits: calling
   `/products/types/ZFP/locations/{CODE}` with a plausible-but-wrong 3-letter code
   (`PHX` instead of `PSR`, `SEA` instead of `SEW`) returns HTTP 200 with an EMPTY
   `@graph` — indistinguishable from "this office stopped publishing" unless you already
   know the right code. Sidestepped by never using that per-code endpoint.
2. NO BULK "ALL LATEST OBSERVATIONS" ENDPOINT EXISTS on this API — only one station at a
   time (`/stations/{id}/observations/latest`). Dead end worth naming: the Iowa
   Environmental Mesonet's `currents.json?networkclass=ASOS` DOES return a real bulk
   feed — every ASOS station worldwide in one response — but it is 54 MB, not scoped to
   the US, and not this work's declared source; it was measured with the body sent to
   `/dev/null` (Content-Length only) and never written to disk. Its narrower
   `currents.json?network=IA_ASOS` does work as real bulk (60 stations, ~77 kB) but
   there is no single `network=US` — you would need one request per state network, and
   the field names (`p01i`, inches) do not match this work's committed schema
   (`precipitationLastHour`, mm) anyway. So stations.json is built from a fixed, small,
   named list of major-airport station IDs, fetched from `api.weather.gov` only, each
   ID CONFIRMED LIVE against `/stations?id=...` before use — any that does not resolve
   is dropped, never guessed at.
3. ZONE GEOMETRY IS THE EXPENSIVE PART, SO THIS RELAY NEVER FETCHES IT LIVE. The bulk
   zone listing (`/zones?type=public&limit=5000`) returns every zone's metadata in ONE
   request, but its `geometry` field is always `null`. Real polygon coordinates live
   only on the per-zone endpoint (`/zones/forecast/{UGC}`), and that ranges roughly
   0.3-290 kB per zone depending on coastline complexity — tens to hundreds of megabytes
   for a value the room only needs as a rough point, unaffordable every relay cycle.
   But zone polygons do not move, so the cost is payable exactly ONCE: run
   `tools/zone_gazetteer.py` offline (see that file) to build a static
   `projects/outstanding/zone-centroids.json` (UGC -> [lat, lon], ~4,080 zones, ~115 kB).
   THIS FILE, EVERY CYCLE, ONLY READS THAT LOOKUP (see `load_gazetteer`/
   `apply_gazetteer` below) — it makes no `/zones/forecast/{UGC}` request of its own
   by default. A zone missing from the lookup ships `lat`/`lon`: null, same as before.
   The old `--with-zone-geometry`/`--geometry-sample` flags still exist below as a
   bounded, explicitly opt-in escape hatch for cost measurement or filling a genuinely
   new zone the offline pass hasn't seen yet — never used by a normal cycle.
   STATION geometry has no such cost: the bulk `/stations?id=...` listing carries a
   Point per station for free.
4. THE NATIONAL INDEX IS A ROLLING WINDOW (~5000 most recent products, several days
   deep), not a live "current state" list — but every office reissues at least twice a
   day, so the latest-per-office derived from it has been confirmed complete (123/123)
   against a same-instant per-office cross-check.
5. `tools/zfp_harvest.py` already has the parser for this bulletin format
   (`zone_blocks()`, `PERIOD`/`PCT`/`UGC` regexes, `QUALIFIERS`/`PRECIP_WORDS`); this
   file imports and reuses it rather than re-deriving it. Its docstring's traps (the
   half-open archive date window, `limit=9999`, zone codes renumbered across decades)
   are about the ARCHIVE endpoint and do not apply to this live-API relay, but the
   parsing regexes and word lists are the same bulletin format and are reused verbatim.

Output shape is fixed by the conductor (see projects/outstanding/CONCEPT.md and the
session brief) and is not changed here. `percent` is the FIRST stated percent in a
period's text if any (periods essentially always carry at most one live probability;
this is documented, not silently assumed). `words` is qualifiers-then-precip-words
actually found in the text (via zfp_harvest.describe()). `silent` is true only when a
period names neither a number nor a precipitation word at all.

Usage:
  python3 tools/relay.py --out DIR
      Cold run: discovers every currently-issued ZFP office, fetches and parses each
      bulletin, samples station observations, writes forecasts.json + stations.json +
      relay-state.json (small: office -> product id + issuanceTime, for --incremental).

  python3 tools/relay.py --out DIR --incremental
      Re-fetches only bulletins whose issuanceTime differs from relay-state.json.
      Offices that have not reissued reuse their previously-parsed zones from the
      forecasts.json already in DIR (never a re-parse of cached raw text — no whole-
      bulletin corpus is kept on disk between runs, only the small parsed JSON output).
      Falls back to a full cold fetch for any office with no prior state.

  python3 tools/relay.py --out DIR --with-zone-geometry --geometry-sample 40
      Also computes a lat/lon centroid per zone from LIVE polygon geometry, bounded to
      the first N zones encountered (cost measurement / bounded escape-hatch use only —
      see point 3 above; a normal cycle relies on --gazetteer instead of this).

  python3 tools/relay.py --out DIR --gazetteer path/to/zone-centroids.json
      Every zone's lat/lon is filled from this static offline lookup (built once by
      tools/zone_gazetteer.py) instead of being fetched. Default path is
      projects/outstanding/zone-centroids.json next to this repo's tools/ directory;
      a missing file simply leaves lat/lon: null, same as always. This is the normal,
      cheap path — no geometry request happens in a regular relay cycle.

Always sends the required User-Agent. Concurrency capped at --workers (default 8,
maximum 8). Every HTTP call retries up to 3 times with 2/4/8 s backoff.
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zfp_harvest import zone_blocks, describe  # noqa: E402  (reused, not re-derived)

API = "https://api.weather.gov"
UA = "(frankbueltge.de studio relay, f.bueltge@gmail.com)"

# A fixed, small, national sample of major-airport station identifiers. Public
# reference identifiers (not weather data) — every one is confirmed live against
# /stations?id=... before use in run(); anything that does not resolve is dropped.
STATION_CANDIDATES = sorted(set("""
KABQ KALB KATL KBDL KBIL KBIS KBNA KBOI KBOS KBWI KCAE KCLE KCRW KCYS KDCA KDEN KDFW
KDSM KDTW KEWR KFSD KHNL KICT KILG KIND KJFK KLAS KLAX KLIT KMHT KMIA KMKE KMSP KMSY
KOKC KOMA KORD KPDX KPHL KPHX KPVD KPWM KRDU KRIC KSAN KSDF KSEA KSFO KSLC KSTL KTPA
PANC PABE PAFA PAJN PHNL PHTO PGUM TJSJ
""".split()))


def http_get(url, timeout=60, tries=3):
    """GET with the required User-Agent, retried with backoff. Returns bytes or raises."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/geo+json"})
    last = None
    for attempt in range(tries):
        try:
            t0 = time.time()
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read()
            return body, time.time() - t0
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1) ** 2)
    raise RuntimeError(f"GET failed after {tries} tries: {url}: {last}")


def get_json(url, timeout=60, tries=3):
    body, elapsed = http_get(url, timeout=timeout, tries=tries)
    return json.loads(body), len(body), elapsed


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------
# Forecasts
# ---------------------------------------------------------------------------

def discover_offices(meter):
    """Latest product id + issuanceTime per office, from the national ZFP index alone."""
    data, nbytes, elapsed = get_json(f"{API}/products/types/ZFP")
    meter["requests"] += 1
    meter["bytes"] += nbytes
    meter["index_seconds"] = elapsed
    latest = {}
    for entry in data["@graph"]:
        office = entry["issuingOffice"][1:]  # drop the WMO/ICAO region prefix letter
        t = entry["issuanceTime"]
        if office not in latest or t > latest[office]["issuanceTime"]:
            latest[office] = {"product_id": entry["id"], "issuanceTime": t}
    return latest, len(data["@graph"])


def fetch_product_text(product_id):
    data, nbytes, elapsed = get_json(f"{API}/products/{product_id}")
    return data["productText"], nbytes, elapsed


def parse_office(office, product_id, issued_at, text):
    zones = []
    for blk in zone_blocks(text):
        place = ""
        for h in blk["header"]:
            h = h.strip()
            if h:
                place = h.rstrip("-").strip().upper()
                break
        periods = []
        for label, ptext in blk["periods"]:
            pcts, quals, precip = describe(ptext)
            periods.append({
                "label": label,
                "text": ptext,
                "percent": pcts[0] if pcts else None,
                "words": quals + precip,
                "silent": (not pcts) and (not precip),
            })
        zones.append({"ugc": blk["ugc"], "place": place, "lat": None, "lon": None, "periods": periods})
    return {"office": office, "product_id": product_id, "issued_at": issued_at, "zones": zones}


def build_forecasts(out_dir, incremental, workers, meter):
    latest, index_entries = discover_offices(meter)
    meter["offices_in_index"] = len(latest)
    meter["index_entries"] = index_entries

    prior_state = {}
    prior_offices = {}
    state_path = os.path.join(out_dir, "relay-state.json")
    fc_path = os.path.join(out_dir, "forecasts.json")
    if incremental and os.path.exists(state_path) and os.path.exists(fc_path):
        with open(state_path, encoding="utf-8") as f:
            prior_state = json.load(f)
        with open(fc_path, encoding="utf-8") as f:
            prior_offices = {o["office"]: o for o in json.load(f)["offices"]}

    to_fetch, reused = [], []
    for office, info in latest.items():
        prev = prior_state.get(office)
        if incremental and prev and prev.get("issuanceTime") == info["issuanceTime"] and office in prior_offices:
            reused.append(office)
        else:
            to_fetch.append(office)
    meter["offices_reused"] = len(reused)
    meter["offices_fetched"] = len(to_fetch)

    offices_out = [prior_offices[o] for o in reused]
    fetch_seconds = 0.0

    def job(office):
        info = latest[office]
        text, nbytes, elapsed = fetch_product_text(info["product_id"])
        return office, info, text, nbytes, elapsed

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for office, info, text, nbytes, elapsed in ex.map(job, to_fetch):
            meter["requests"] += 1
            meter["bytes"] += nbytes
            fetch_seconds = max(fetch_seconds, elapsed)
            offices_out.append(parse_office(office, info["product_id"], info["issuanceTime"], text))
    meter["fetch_wall_seconds"] = fetch_seconds

    offices_out.sort(key=lambda o: o["office"])
    forecasts = {"generated_at": now_iso(), "source": API, "offices": offices_out}
    new_state = {o: latest[o] for o in latest}
    return forecasts, new_state


# ---------------------------------------------------------------------------
# Zone gazetteer (default path) — a static, offline-built UGC -> [lat, lon]
# lookup (see tools/zone_gazetteer.py). Reading it costs one small local
# file read, never a network request; this is the ONLY way lat/lon get
# filled in a normal relay cycle (point 3 above).
# ---------------------------------------------------------------------------

def default_gazetteer_path():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "..", "projects", "outstanding", "zone-centroids.json")


def load_gazetteer(path):
    """Load the offline UGC -> [lat, lon] lookup. Returns {} (never raises) if the
    file is absent or unreadable — a relay cycle must still produce valid output,
    with every zone's lat/lon simply staying null, if the gazetteer hasn't been
    built yet or its path is wrong."""
    if not path or not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    data.pop("_meta", None)
    return data


def apply_gazetteer(forecasts, gazetteer, meter):
    """Fill lat/lon on every zone from the static lookup, in place. No network
    call happens here — this is a pure in-memory dict lookup per zone."""
    total = 0
    filled = 0
    for off in forecasts["offices"]:
        for z in off["zones"]:
            total += 1
            pt = gazetteer.get(z["ugc"])
            if pt and len(pt) == 2:
                z["lat"], z["lon"] = pt[0], pt[1]
                filled += 1
    meter["zones_total"] = total
    meter["zones_geocoded"] = filled
    meter["zones_geocoded_from_gazetteer"] = filled


# ---------------------------------------------------------------------------
# Zone geometry (optional, measured cost)
# ---------------------------------------------------------------------------

def polygon_centroid(rings):
    """Planar centroid of the largest ring by |area| (shoelace). Good enough for a
    point light on a dark field; not a proper geodesic centroid, and no ring holes
    (interior rings) are subtracted, so a doughnut-shaped zone would be slightly off."""
    best_ring, best_area = None, 0.0
    for ring in rings:
        a = 0.0
        for i in range(len(ring) - 1):
            x1, y1 = ring[i]
            x2, y2 = ring[i + 1]
            a += x1 * y2 - x2 * y1
        if abs(a) > best_area:
            best_area, best_ring = abs(a), ring
    if not best_ring or best_area == 0:
        return None
    signed = sum(best_ring[i][0] * best_ring[i + 1][1] - best_ring[i + 1][0] * best_ring[i][1]
                 for i in range(len(best_ring) - 1)) / 2
    if signed == 0:
        return None
    cx = sum((best_ring[i][0] + best_ring[i + 1][0]) *
              (best_ring[i][0] * best_ring[i + 1][1] - best_ring[i + 1][0] * best_ring[i][1])
              for i in range(len(best_ring) - 1)) / (6 * signed)
    cy = sum((best_ring[i][1] + best_ring[i + 1][1]) *
              (best_ring[i][0] * best_ring[i + 1][1] - best_ring[i + 1][0] * best_ring[i][1])
              for i in range(len(best_ring) - 1)) / (6 * signed)
    return cy, cx  # lat, lon


def fetch_zone_geometry(ugc, meter):
    data, nbytes, elapsed = get_json(f"{API}/zones/forecast/{ugc}")
    meter["requests"] += 1
    meter["bytes"] += nbytes
    geom = data.get("geometry")
    if not geom:
        return None
    if geom["type"] == "Polygon":
        rings = geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        rings = [r for poly in geom["coordinates"] for r in poly]
    else:
        return None
    return polygon_centroid(rings)


def apply_zone_geometry(forecasts, sample_n, workers, meter):
    ugcs = []
    for off in forecasts["offices"]:
        for z in off["zones"]:
            ugcs.append((off, z))
    subset = ugcs[:sample_n] if sample_n else ugcs
    meter["zone_geometry_attempted"] = len(subset)

    def job(pair):
        off, z = pair
        try:
            c = fetch_zone_geometry(z["ugc"], meter)
        except Exception:
            c = None
        return z, c

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for z, c in ex.map(job, subset):
            if c:
                z["lat"], z["lon"] = round(c[0], 4), round(c[1], 4)


# ---------------------------------------------------------------------------
# Stations
# ---------------------------------------------------------------------------

def build_stations(workers, meter):
    ids = ",".join(STATION_CANDIDATES)
    meta, nbytes, elapsed = get_json(f"{API}/stations?id={ids}")
    meter["requests"] += 1
    meter["bytes"] += nbytes
    resolved = {}
    for feat in meta["features"]:
        p = feat["properties"]
        lon, lat = feat["geometry"]["coordinates"]
        resolved[p["stationIdentifier"]] = {"name": p.get("name", ""), "lat": lat, "lon": lon}
    meter["stations_requested"] = len(STATION_CANDIDATES)
    meter["stations_resolved"] = len(resolved)

    def job(sid):
        try:
            data, nbytes, elapsed = get_json(f"{API}/stations/{sid}/observations/latest")
            return sid, data, nbytes, elapsed, None
        except Exception as exc:  # noqa: BLE001 - live station feed, one of many
            return sid, None, 0, 0.0, str(exc)

    stations_out = []
    ages = []
    fetched_at = datetime.datetime.now(datetime.timezone.utc)
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        for sid, data, nbytes, elapsed, err in ex.map(job, sorted(resolved)):
            meter["requests"] += 1
            meter["bytes"] += nbytes
            if err:
                errors.append((sid, err))
                continue
            props = data["properties"]
            precip = props.get("precipitationLastHour") or {}
            ts = props.get("timestamp")
            if ts:
                try:
                    obs_dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    ages.append((fetched_at - obs_dt).total_seconds() / 60.0)
                except ValueError:
                    pass
            stations_out.append({
                "id": sid,
                "name": resolved[sid]["name"],
                "lat": resolved[sid]["lat"],
                "lon": resolved[sid]["lon"],
                "observed_at": ts,
                "precip_last_hour_mm": precip.get("value"),
                "present_weather": ",".join(w.get("weather", "") for w in props.get("presentWeather", []) or []),
                "text": props.get("textDescription", ""),
            })
    meter["station_errors"] = errors
    meter["obs_age_minutes"] = ages
    stations_out.sort(key=lambda s: s["id"])
    return {"generated_at": now_iso(), "source": API, "stations": stations_out}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--incremental", action="store_true")
    ap.add_argument("--with-zone-geometry", action="store_true")
    ap.add_argument("--geometry-sample", type=int, default=0,
                     help="limit zone-geometry fetches to the first N zones (0 = all)")
    ap.add_argument("--gazetteer", default=None,
                     help="path to the offline UGC->[lat,lon] lookup built by "
                          "tools/zone_gazetteer.py (default: projects/outstanding/"
                          "zone-centroids.json next to this repo's tools/ dir)")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    workers = max(1, min(8, a.workers))
    os.makedirs(a.out, exist_ok=True)

    meter = {"requests": 0, "bytes": 0}
    t0 = time.time()

    forecasts, state = build_forecasts(a.out, a.incremental, workers, meter)

    gazetteer_path = a.gazetteer or default_gazetteer_path()
    gazetteer = load_gazetteer(gazetteer_path)
    meter["gazetteer_path"] = gazetteer_path
    meter["gazetteer_entries"] = len(gazetteer)
    apply_gazetteer(forecasts, gazetteer, meter)

    if a.with_zone_geometry:
        apply_zone_geometry(forecasts, a.geometry_sample, workers, meter)
    stations = build_stations(workers, meter)

    meter["wall_seconds"] = time.time() - t0

    with open(os.path.join(a.out, "forecasts.json"), "w", encoding="utf-8") as f:
        json.dump(forecasts, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(a.out, "stations.json"), "w", encoding="utf-8") as f:
        json.dump(stations, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(a.out, "relay-state.json"), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    with open(os.path.join(a.out, "relay-meter.json"), "w", encoding="utf-8") as f:
        json.dump(meter, f, indent=2, default=str)

    n_periods = sum(len(z["periods"]) for o in forecasts["offices"] for z in o["zones"])
    n_pct = sum(1 for o in forecasts["offices"] for z in o["zones"] for p in z["periods"] if p["percent"] is not None)
    n_silent = sum(1 for o in forecasts["offices"] for z in o["zones"] for p in z["periods"] if p["silent"])
    print(f"offices={len(forecasts['offices'])} zones={sum(len(o['zones']) for o in forecasts['offices'])} "
          f"periods={n_periods} numeric={n_pct} silent={n_silent}")
    print(f"zones geocoded from gazetteer: {meter['zones_geocoded']}/{meter['zones_total']} "
          f"({gazetteer_path}, {meter['gazetteer_entries']} entries loaded)")
    print(f"stations={len(stations['stations'])}/{meter['stations_requested']} requested "
          f"({len(meter['station_errors'])} errors)")
    print(f"requests={meter['requests']} bytes={meter['bytes']:,} wall={meter['wall_seconds']:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
