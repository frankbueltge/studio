#!/usr/bin/env python3
"""Zone gazetteer: a one-time, offline pass building a static UGC -> [lat, lon]
lookup for every public forecast zone, so `tools/relay.py` never has to fetch
zone geometry during a relay cycle.

Why this exists (see projects/outstanding/RELAY-MEASUREMENT.md §3): the bulk
zone listing (`/zones?type=public&limit=5000`) returns every zone's metadata
in one request but its `geometry` field is always `null`. Real polygon
coordinates live only on the per-zone endpoint
(`https://api.weather.gov/zones/forecast/{UGC}`), averaging ~78.5 kB/zone —
about 296 MB across the ~3,771 zones a live relay cycle actually holds, and
more again across the full ~4,080-zone public-zone registry. That cost is
unaffordable *every ten minutes*, but the polygons themselves do not move, so
it is affordable exactly ONCE. This script is that once: it runs standalone,
off-cycle, and writes a small static file relay.py reads back forever after.

THE DISK RULE THIS FILE OBEYS, ABSOLUTELY: it never writes a polygon to disk,
not even transiently. Each zone's response body is held in memory only long
enough to parse its `geometry` and reduce it to one [lat, lon] pair; the body
and parsed coordinate arrays are then dropped (falls out of scope; nothing is
retained beyond the two floats). The only things this script ever writes to
disk are: (a) the small partial-progress file (UGC -> [lat, lon] computed so
far, a few hundred KB at most even at full size), and (b) the final compact
output. A previous pass on this material was killed for violating exactly
this rule; this rewrite does not carry raw geometry across a write() call
anywhere.

CENTROID METHOD -- read before changing anything here. For each ring of each
polygon (exterior and interior alike, and every polygon part of a
MultiPolygon), this computes the standard closed-polygon centroid via the
shoelace formula:

    A     = (1/2) * sum_i (x_i * y_{i+1} - x_{i+1} * y_i)
    C_x   = (1/(6A)) * sum_i (x_i + x_{i+1}) * (x_i * y_{i+1} - x_{i+1} * y_i)
    C_y   = (1/(6A)) * sum_i (y_i + y_{i+1}) * (x_i * y_{i+1} - x_{i+1} * y_i)

then combines all ring centroids into ONE point by weighting each ring's
centroid by that ring's |A| and averaging. A handful of coastal zones
(counties whose boundary follows a shoreline) return their polygon wrapped in
a `GeometryCollection` rather than a bare `Polygon`/`MultiPolygon`; every
Polygon/MultiPolygon member found anywhere inside such a collection
(recursively) is included in the same weighted average, and any non-area
member (Point/LineString) is skipped. This is deliberately NOT a mean of
vertices (which would drag the point toward wherever the coastline happens to
be most densely sampled) and NOT "largest ring only" (which silently drops
real area on a genuine multipart zone). It is also not a true area-minus-
holes centroid: an interior ring (a hole -- e.g. a lake excluded from a zone)
contributes its own small centroid weighted by its own small |A| rather than
subtracting from the exterior ring's contribution, which is a small, accepted
simplification for zones this size (islands as separate features, coastline
holes rarely more than a few percent of a zone's area).

ON A MULTIPOLYGON specifically (a zone with genuinely separate landmasses,
e.g. an island chain), this produces the AREA-WEIGHTED average of every
part's centroid -- a point pulled toward whichever part is largest, which can
legitimately fall in open water between two comparably-sized parts. That is
the documented, accepted behaviour: a single representative point for a
field of lights, not a claim that the point is "on" the zone.

Politeness / robustness:
  - User-Agent: (frankbueltge.de studio gazetteer, f.bueltge@gmail.com), always sent.
  - At most 8 concurrent workers (--workers, capped at 8).
  - Every GET retries up to 4 times with 2/4/8/16 s backoff before counting
    as a permanent failure for that zone.
  - RESUMABLE: progress is flushed to a small partial-results file
    (`<out>.partial.json`, holding ONLY completed [lat, lon] results and the
    UGCs already known to have failed -- never a response body) every few
    completions. A second run loads that file first and only fetches UGCs
    missing from it, so an interrupted pass does not start from zero. Pass
    --retry-failed to re-attempt UGCs the partial file recorded as failed.
  - Python 3 standard library only. No third-party dependencies.

Usage:
  python3 tools/zone_gazetteer.py --out projects/outstanding/zone-centroids.json
  python3 tools/zone_gazetteer.py --out projects/outstanding/zone-centroids.json --retry-failed
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

API = "https://api.weather.gov"
UA = "(frankbueltge.de studio gazetteer, f.bueltge@gmail.com)"
SOURCE_PATTERN = f"{API}/zones/forecast/{{UGC}}"


def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def http_get(url, timeout=60, tries=4):
    """GET with the required User-Agent, retried with backoff. Returns bytes or raises.
    The caller is responsible for dropping the returned bytes promptly -- this
    function never writes them anywhere itself."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/geo+json"})
    last = None
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            if attempt < tries - 1:
                time.sleep(2 * (attempt + 1) ** 2)
    raise RuntimeError(f"GET failed after {tries} tries: {url}: {last}")


def list_zone_ids(meter):
    """The one bulk, cheap call: every public zone's UGC, metadata only
    (`geometry` is always null on this endpoint -- see module docstring).
    The 6+ MB body is parsed for `properties.id` alone and then dropped."""
    body = http_get(f"{API}/zones?type=public&limit=5000")
    meter["requests"] += 1
    meter["bytes_in"] += len(body)
    data = json.loads(body)
    ids = sorted({f["properties"]["id"] for f in data["features"]})
    del body, data  # never held onto; nothing here is a polygon anyway
    return ids


# ---------------------------------------------------------------------------
# Geometry -> point, area-weighted centroid over every ring. See module
# docstring "CENTROID METHOD" for the formula and what it does on a
# MultiPolygon. Input rings are GeoJSON [lon, lat] order; output is (lat, lon).
# ---------------------------------------------------------------------------

def ring_area_and_centroid(ring):
    """Shoelace area (signed) and centroid of one closed ring of [lon, lat]
    pairs. Returns (abs_area, (cx, cy)) in (lon, lat) order, or (0.0, None)
    for a degenerate ring (fewer than 4 points, or zero signed area)."""
    if len(ring) < 4:
        return 0.0, None
    a = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(len(ring) - 1):
        x1, y1 = ring[i]
        x2, y2 = ring[i + 1]
        cross = x1 * y2 - x2 * y1
        a += cross
        cx += (x1 + x2) * cross
        cy += (y1 + y2) * cross
    a *= 0.5
    if a == 0:
        return 0.0, None
    cx /= (6 * a)
    cy /= (6 * a)
    return abs(a), (cx, cy)


def iter_polygons(geometry):
    """Yield every polygon (a list of rings) found in a geometry -- straight
    from a Polygon, every part of a MultiPolygon, or (a handful of coastal
    zones return this) every Polygon/MultiPolygon member of a
    GeometryCollection, recursively. Point/LineString members contribute no
    area and are silently skipped."""
    gtype = geometry.get("type")
    if gtype == "Polygon":
        yield geometry.get("coordinates") or []
    elif gtype == "MultiPolygon":
        for poly in geometry.get("coordinates") or []:
            yield poly
    elif gtype == "GeometryCollection":
        for sub in geometry.get("geometries") or []:
            yield from iter_polygons(sub)
    # Point / LineString / MultiLineString / MultiPoint: no area, skipped.


def polygon_centroid(geometry):
    """Area-weighted centroid across every ring of every polygon part found
    anywhere in the geometry (see iter_polygons for what "found" covers,
    including inside a GeometryCollection). Returns (lat, lon) or None for an
    empty/unsupported geometry (no polygon part anywhere in it)."""
    polys = list(iter_polygons(geometry))
    total_w = 0.0
    sx = 0.0
    sy = 0.0
    for poly in polys:
        for ring in poly:
            w, c = ring_area_and_centroid(ring)
            if c is None or w == 0.0:
                continue
            sx += c[0] * w
            sy += c[1] * w
            total_w += w
    if total_w == 0.0:
        return None
    lon = sx / total_w
    lat = sy / total_w
    return lat, lon


def fetch_centroid(ugc, meter):
    """Fetch one zone's geometry, reduce it to a centroid, discard the body.
    The response bytes and parsed coordinate lists exist only for the
    duration of this call -- nothing here is written to disk."""
    body = http_get(f"{API}/zones/forecast/{ugc}")
    meter["requests"] += 1
    meter["bytes_in"] += len(body)
    try:
        data = json.loads(body)
    finally:
        del body
    geom = data.get("geometry")
    if not geom:
        return None
    c = polygon_centroid(geom)
    del data, geom
    return c


# ---------------------------------------------------------------------------
# Resumable partial-results file: {ugc: [lat, lon]} for successes plus a
# "_failed" list -- results only, never a response body.
# ---------------------------------------------------------------------------

def load_partial(path):
    if not os.path.exists(path):
        return {}, set()
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return {}, set()
    failed = set(data.pop("_failed", []))
    return data, failed


def save_partial(path, done, failed):
    tmp = path + ".tmp"
    out = dict(done)
    out["_failed"] = sorted(failed)
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="final output path, e.g. projects/outstanding/zone-centroids.json")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--retry-failed", action="store_true", help="re-attempt UGCs the partial file recorded as failed")
    ap.add_argument("--flush-every", type=int, default=20, help="write the partial file every N completions")
    a = ap.parse_args()
    workers = max(1, min(8, a.workers))
    partial_path = a.out + ".partial.json"

    meter = {"requests": 0, "bytes_in": 0}
    t0 = time.time()

    all_ids = list_zone_ids(meter)
    done, failed = load_partial(partial_path)
    if a.retry_failed:
        failed = set()
    todo = [u for u in all_ids if u not in done and u not in failed]

    print(f"zones total={len(all_ids)} already_done={len(done)} already_failed={len(failed)} "
          f"to_fetch={len(todo)}", file=sys.stderr)

    completed = 0

    def job(ugc):
        try:
            c = fetch_centroid(ugc, meter)
        except Exception as exc:  # noqa: BLE001 - live network call, one of thousands
            return ugc, None, str(exc)
        return ugc, c, None

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
            for ugc, c, err in ex.map(job, todo):
                completed += 1
                if c is not None:
                    done[ugc] = [round(c[0], 4), round(c[1], 4)]
                    failed.discard(ugc)
                else:
                    failed.add(ugc)
                    if err and completed % 50 == 0:
                        print(f"  ...still failing example: {ugc}: {err}", file=sys.stderr)
                if completed % a.flush_every == 0:
                    save_partial(partial_path, done, failed)
                    print(f"  {completed}/{len(todo)} fetched this run "
                          f"({len(done)} total ok, {len(failed)} total failed)", file=sys.stderr)
    finally:
        # Always flush on the way out, including on Ctrl-C / a killed run --
        # this is the whole point of resumability.
        save_partial(partial_path, done, failed)

    wall = time.time() - t0
    header = {
        "generated_at": now_iso(),
        "source": SOURCE_PATTERN,
        "zone_count": len(all_ids),
        "zones_ok": len(done),
        "zones_failed": len(failed),
        "failed_ugcs": sorted(failed),
    }
    out = {"_meta": header}
    out.update(done)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    tmp = a.out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"), sort_keys=True)
    os.replace(tmp, a.out)

    size = os.path.getsize(a.out)
    print(f"zones={len(all_ids)} ok={len(done)} failed={len(failed)} "
          f"requests={meter['requests']} bytes_in={meter['bytes_in']:,} wall={wall:.1f}s "
          f"out={a.out} ({size:,} B)")
    if failed:
        print(f"failed_ugcs={sorted(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
