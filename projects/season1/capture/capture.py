#!/usr/bin/env python3
"""STILL DARK — the nightly capture.

Fetches the live Ghost Fleet edition (https://frankbueltge.de/ghost-fleet/), extracts
the named vessels and the aggregates, and writes one immutable JSON capture per run to
projects/season1/captures/<UTC timestamp>.json.

Why this exists. The instrument publishes, by its own method sheet, only "disabling
events that ended in the last 7 days (complete vanish-and-return stories)". A ship that
is still dark is in no edition. So a calendar day of the sea is almost empty on the day
itself and keeps filling for weeks afterwards. Nobody — including the instrument —
keeps a day-addressed record of that filling. These captures are that record: the
FIRST capture in which a vessel appears is the day this house could first know of it,
observed, not derived.

Tiers, and the line the work may not cross:
  SOURCED  — what the page prints: vessel name, flag, duration in days, waters, the
             edition date, the aggregates, the Global Fishing Watch vessel id.
  DERIVED  — anything computed from those, with its uncertainty carried (the end date
             of a dark interval is published only as "within the last 7 days", so every
             derived interval is a band, never a point).
  OBSERVED — first_seen_utc: the timestamp of the earliest capture holding this vessel.
             This is our own measurement of our own record.
There is no IMAGINED tier in this file, and no invented time is ever attached to a
vessel name (gate condition C1, projects/season1/KRITIKER-GATE-66.md).

Usage:  python3 capture.py [--out DIR] [--url URL]
Deterministic apart from the fetch itself: same page bytes in, same JSON out, except
for fetched_at. The raw body's sha256 is recorded so a stranger can check that the
parse belongs to the bytes.
"""

import argparse
import datetime
import hashlib
import html
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import content_sha256  # noqa: E402

URL = "https://frankbueltge.de/ghost-fleet/"
METHOD_URL = "https://frankbueltge.de/werke/ghost-fleet/"

# The method sentence the whole work rests on, quoted verbatim from METHOD_URL.
WINDOW_QUOTE = (
    "Daily. Window: disabling events that ended in the last 7 days "
    "(complete vanish-and-return stories)."
)
WINDOW_DAYS = 7

VESSEL_RE = re.compile(
    r'<li class="flex flex-wrap[^"]*">\s*'
    r'<span class="text-fg-muted">([^<]+?)\s*'
    r'<span class="font-mono text-xs text-fg-faint">\(([A-Z]{3})\)</span></span>\s*'
    r'<span class="font-mono text-xs text-fg-faint">(\d+)\s*days\s*·\s*([^<]+?)</span>\s*'
    r'<a class="[^"]*" href="([^"]+)"',
    re.S,
)
CASE_RE = re.compile(
    r'The case of the day\s*</p>\s*<p class="[^"]*">([^<]+?)\s*'
    r'<span class="font-mono text-sm text-fg-faint">\(([A-Z]{3})\)</span></p>\s*'
    r'<p class="[^"]*">\s*(.*?)\s*</p>.*?href="(https://globalfishingwatch\.org[^"]+)"',
    re.S,
)
DATE_RE = re.compile(r'<p class="mt-1 font-mono text-xs text-fg-faint">([^<]+)</p>')
AGG_RE = re.compile(
    r'tabular-nums">(\d[\d,]*)</p>.*?'
    r'ships went dark inside national waters lately\s*—\s*of\s*(\d[\d,]*)\s*'
    r'disappearances examined\s*\((\d[\d,]*)\s*in the window\)\.',
    re.S,
)
VESSEL_DAYS_RE = re.compile(r'Together about\s*([\d,]+)\s*vessel-days of darkness')
# The site's own fingerprinted asset paths. Not part of the edition and never read by the
# work — recorded from session 70 so that a body hash which moves while the edition stands
# still can be attributed instead of guessed at. (The 2026-08-06 capture moved its body
# hash at an identical byte count with every read field unchanged; the earlier bodies were
# not kept, so that one stays unattributable and is left so.)
ASSET_RE = re.compile(r'(?:href|src)="([^"]*_astro/[^"]+)"')
DURATION_RE = re.compile(r'switched off its transponder for\s*(\d+)\s*days')
# the trailing "…, in <waters>." of the case-of-the-day sentence; see the note where it is used
PROSE_WATERS_RE = re.compile(r",\s*in\s+([^,]+?)\.\s*$")


def num(s):
    return int(s.replace(",", "").replace(" ", ""))


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def fetch(url):
    """Fetch with curl; return (body_bytes, http_status). No third-party library."""
    proc = subprocess.run(
        ["curl", "-sS", "-w", "\n%{http_code}", url],
        capture_output=True,
    )
    if proc.returncode != 0:
        raise SystemExit(f"fetch failed: {proc.stderr.decode('utf-8', 'replace')}")
    raw = proc.stdout
    body, _, status = raw.rpartition(b"\n")
    return body, int(status)


def parse(body):
    s = body.decode("utf-8", "replace")
    out = {}

    m = DATE_RE.search(s)
    out["edition_date_printed"] = clean(m.group(1)) if m else None

    m = CASE_RE.search(s)
    if m:
        prose = clean(m.group(3))
        d = DURATION_RE.search(prose)
        out["case_of_the_day"] = {
            "name": clean(m.group(1)),
            "flag": m.group(2),
            "days_dark": int(d.group(1)) if d else None,
            "prose": prose,
            "gfw_url": m.group(4),
        }

    m = AGG_RE.search(s)
    if m:
        out["aggregates"] = {
            "dark_inside_national_waters": num(m.group(1)),
            "disappearances_examined": num(m.group(2)),
            "in_the_window": num(m.group(3)),
        }
    m = VESSEL_DAYS_RE.search(s)
    if m and "aggregates" in out:
        out["aggregates"]["vessel_days_of_darkness_approx"] = num(m.group(1))

    others = []
    for m in VESSEL_RE.finditer(s):
        others.append(
            {
                "name": clean(m.group(1)),
                "flag": m.group(2),
                "days_dark": int(m.group(3)),
                "waters": clean(m.group(4)),
                "gfw_url": m.group(5),
            }
        )
    out["others_gone_dark"] = others

    vessels = []
    if out.get("case_of_the_day"):
        c = dict(out["case_of_the_day"])
        c["role"] = "case_of_the_day"
        # Upstream prints this one vessel's waters inside its prose sentence rather than as
        # a field. Until 2026-08-06 this parser wrote null here, and the work's face carried
        # an empty column for a fact the record held — TUNAMAR, for five nights. The words
        # taken are upstream's, verbatim; only the cut is ours, so the value stays SOURCED,
        # and where the sentence carries no waters it stays null rather than guessing.
        m2 = PROSE_WATERS_RE.search(c.get("prose") or "")
        c["waters"] = clean(m2.group(1)) if m2 else None
        vessels.append(c)
    for o in others:
        o = dict(o)
        o["role"] = "other"
        vessels.append(o)
    out["vessels"] = vessels
    out["page_assets"] = sorted(set(ASSET_RE.findall(s)))
    return out


def edition_iso(printed):
    """'4 August 2026' -> '2026-08-04'. Returns None if the format ever changes."""
    if not printed:
        return None
    for fmt in ("%d %B %Y", "%d. %B %Y"):
        try:
            return datetime.datetime.strptime(printed.strip(), fmt).date().isoformat()
        except ValueError:
            continue
    return None


def derive(vessels, edition):
    """Per vessel, the dark interval as a BAND, never a point.

    The edition holds events that ended within the 7 days before its own date, so
    end ∈ [edition − 7, edition] and start = end − days_dark. Both ends of both bands
    are printed. This is the whole of what may be said about a vessel's timing from
    published material; anything narrower would be invention.
    """
    if not edition:
        return []
    ed = datetime.date.fromisoformat(edition)
    rows = []
    for v in vessels:
        d = v.get("days_dark")
        if d is None:
            continue
        end_lo, end_hi = ed - datetime.timedelta(days=WINDOW_DAYS), ed
        rows.append(
            {
                "name": v["name"],
                "flag": v["flag"],
                "days_dark": d,
                "went_dark_between": [
                    (end_lo - datetime.timedelta(days=d)).isoformat(),
                    (end_hi - datetime.timedelta(days=d)).isoformat(),
                ],
                "resurfaced_between": [end_lo.isoformat(), end_hi.isoformat()],
                "tier": "DERIVED",
                "basis": "published days_dark + published window; both bands printed",
            }
        )
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=URL)
    ap.add_argument(
        "--out",
        default=os.path.normpath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "captures")
        ),
    )
    args = ap.parse_args()

    body, status = fetch(args.url)
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    parsed = parse(body) if status == 200 else {}
    edition = edition_iso(parsed.get("edition_date_printed"))

    capture = {
        "capture_version": 1,
        "fetch": {
            "url": args.url,
            "fetched_at_utc": now.isoformat().replace("+00:00", "Z"),
            "http_status": status,
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        },
        "method": {"source": METHOD_URL, "window_quote": WINDOW_QUOTE, "window_days": WINDOW_DAYS},
        "edition_date_printed": parsed.get("edition_date_printed"),
        "edition_date": edition,
        "case_of_the_day": parsed.get("case_of_the_day"),
        "aggregates": parsed.get("aggregates"),
        "vessels": parsed.get("vessels", []),
        "derived_intervals": derive(parsed.get("vessels", []), edition),
        # Outside the edition and outside every tier the work publishes from: the response's
        # own furniture, kept only so a moved body hash can be explained rather than guessed.
        "page_assets": parsed.get("page_assets", []),
        "tiers": {
            "SOURCED": "vessels, aggregates, edition date, gfw ids — printed on the page",
            "DERIVED": "derived_intervals — arithmetic on published durations, bands printed",
            "OBSERVED": "fetched_at_utc — this house's own record of when it could first know",
        },
    }

    # Two hashes, since session 70: the body's, and the edition's own. A body hash answers
    # "did the response change"; this answers "did the edition change", and it is computed
    # from the capture's own fields so it applies to captures written before it existed.
    capture["content_sha256"] = content_sha256(capture)

    os.makedirs(args.out, exist_ok=True)
    stamp = now.strftime("%Y-%m-%dT%H%M%SZ")
    path = os.path.join(args.out, f"{stamp}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(capture, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(path)
    print(
        f"  status {status} · {len(body)} bytes · edition {capture['edition_date']} · "
        f"{len(capture['vessels'])} vessels"
    )
    if status != 200 or not capture["vessels"]:
        print("  WARNING: nothing parsed — the page's markup may have changed.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
