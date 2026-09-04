#!/usr/bin/env python3
"""Derive WHERE SOMEONE LOOKED from the house's Atlas of Data Art.

    python3 tools/atlas_windows.py

Reads the Atlas feed live (never mirrored into this repository), pins it by
sha256, and writes the derived record the work is built from:

    works/2026-09-04-where-someone-looked/data.json

Nothing of the Atlas's own prose is carried across. Per entry the record keeps
the facts the page shows a reader - title, maker, the year the file states, the
address it cites - and, of the `decisive_move` field, only measurements: its
length in words and whether it matches the scraped-catalogue-furniture rule
this practice published on 2026-09-03. The sentences themselves stay in the
feed, where they belong.

Two fields of the file are read as they stand and not interpreted:

  verify_status   `verified` or `toVerify`. The page reads `verified` as "an
                  entry someone has checked" and says so; the field's exact
                  meaning is the house's, not this practice's.
  year            often a range ("2016-2021", "2019-ongoing"). The first
                  four-digit year is taken and the raw string kept beside it.
"""

import collections
import datetime
import hashlib
import json
import os
import re
import sys
import urllib.request
from urllib.parse import urlparse

FEED = ("https://raw.githubusercontent.com/frankbueltge/frankbueltge.de/"
        "main/src/data/atlas/werke.json")
MIRROR = "https://frankbueltge.de/atlas/werke.json"
UA = "StudioEnsemble-AtlasWindows/1.0 (+https://frankbueltge.de/studio)"

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "works", "2026-09-04-where-someone-looked", "data.json")

# The rule published by this practice on 2026-09-03 for a `decisive_move` that
# is scraped catalogue page furniture rather than a curator's sentence.
FURNITURE = re.compile(r"inception:|access URL:|attributed to:|description edit|PreviousNext")

# An address carrying at least this many entries is called a list. The
# partition is unchanged for any threshold between 10 and 39 - see the record's
# `rule.stable_between`, which this script derives rather than asserts.
LIST_THRESHOLD = 10


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def host_of(url):
    return urlparse(url).netloc.lower().removeprefix("www.")


def first_year(raw):
    m = re.findall(r"(?:19|20)\d{2}", str(raw))
    return int(m[0]) if m else None


def main():
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    raw = get(FEED)
    sha = hashlib.sha256(raw).hexdigest()
    works = json.loads(raw.decode("utf-8"))
    if not isinstance(works, list):
        sys.exit("feed is not a list of entries")

    # Cross-check: the same file is served from the site under its own address.
    # A disagreement between the two would be a finding; it is recorded either
    # way and never guessed at.
    mirror = {"url": MIRROR, "entries": None, "note": None}
    try:
        m = json.loads(get(MIRROR, timeout=45).decode("utf-8"))
        if isinstance(m, dict):
            mirror["entries"] = m.get("count") or len(m.get("werke") or m.get("works") or [])
            mirror["note"] = "served wrapped; compared by count only"
        else:
            mirror["entries"] = len(m)
            mirror["note"] = "served as a bare list; compared by count only"
    except Exception as exc:                                   # noqa: BLE001
        mirror["note"] = f"unreachable from this session: {type(exc).__name__}"

    hosts = collections.Counter(host_of(e["source_url"]) for e in works)

    # Derive the range of thresholds that give exactly this partition, so the
    # choice of 10 is shown to be free rather than asserted to be.
    sizes = sorted(set(hosts.values()))
    listed = {h for h, n in hosts.items() if n >= LIST_THRESHOLD}
    lo = max([s for s in sizes if s not in (n for h, n in hosts.items() if h in listed)] + [0]) + 1
    hi = min(hosts[h] for h in listed)

    rows = []
    for i, e in enumerate(works):
        h = host_of(e["source_url"])
        dm = e.get("decisive_move") or ""
        rows.append({
            "i": i,
            "title": e["title"],
            "artist": e["artist"],
            "year": first_year(e["year"]),
            "year_raw": e["year"],
            "host": h,
            "url": e["source_url"],
            "list": h in listed,
            "read": e.get("verify_status") == "verified",
            "furniture": bool(FURNITURE.search(dm)),
            "dm_words": len(dm.split()),
            "clusters": e.get("clusters") or [],
            "axis": e.get("axis_pole"),
            "form": e.get("form"),
            "lab": bool(e.get("lab_renderable")),
        })

    years = []
    by_year = collections.defaultdict(list)
    for r in rows:
        by_year[r["year"]].append(r)
    span = range(min(by_year), max(by_year) + 1)
    for y in span:
        rs = by_year.get(y, [])
        years.append({
            "year": y,
            "n": len(rs),
            "read": sum(1 for r in rs if r["read"]),
            "hand": sum(1 for r in rs if not r["list"]),
            "addresses": len({r["host"] for r in rs}),
        })

    host_rows = []
    for h, n in hosts.most_common():
        ys = [r["year"] for r in rows if r["host"] == h]
        host_rows.append({
            "host": h, "n": n, "first_year": min(ys), "last_year": max(ys),
            "list": h in listed,
            "read": sum(1 for r in rows if r["host"] == h and r["read"]),
            "furniture": sum(1 for r in rows if r["host"] == h and r["furniture"]),
        })

    read = {r["i"] for r in rows if r["read"]}
    hand = {r["i"] for r in rows if not r["list"]}

    record = {
        "work": "WHERE SOMEONE LOOKED",
        "practice": "Ensemble - The Studio",
        "generated_utc": now,
        "source": {
            "url": FEED, "sha256": sha, "bytes": len(raw), "entries": len(works),
            "fetched_utc": now, "mirror_check": mirror,
        },
        "rule": {
            "list_threshold": LIST_THRESHOLD,
            "stable_between": [lo, hi],
            "furniture_pattern": FURNITURE.pattern,
        },
        "counts": {
            "works": len(rows),
            "addresses": len(hosts),
            "lists": len(listed),
            "from_lists": sum(1 for r in rows if r["list"]),
            "by_hand": len(hand),
            "read": len(read),
            "unread": len(rows) - len(read),
            "read_and_hand": len(read & hand),
            "read_not_hand": len(read - hand),
            "hand_not_read": len(hand - read),
            "either": len(read | hand),
        },
        "hosts": host_rows,
        "years": years,
        "works_list": rows,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=1)
        f.write("\n")
    c = record["counts"]
    print(f"{OUT}\n  {c['works']} works, {c['addresses']} addresses, "
          f"{c['lists']} lists carrying {c['from_lists']}\n"
          f"  read {c['read']} - by hand {c['by_hand']} - both {c['read_and_hand']} "
          f"- differing {c['read_not_hand'] + c['hand_not_read']}\n"
          f"  feed sha256 {sha}")


if __name__ == "__main__":
    main()
