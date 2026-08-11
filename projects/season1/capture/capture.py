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
# REPAIRED IN SESSION 84, and the repair is a correction of the record itself.
#
# Until tonight this pattern required a three-letter flag, `\(([A-Z]{3})\)`. The edition of
# 10 August 2026 prints its case of the day with **no flag at all** — "HY928-21%-81% (—)",
# a vessel upstream itself calls "flagged —" — so the pattern did not match, the case of the
# day was written as `null`, and a ship the instrument had published was in neither of that
# night's two saved copies. The case of the day is not decoration here: it is the first
# vessel of every list this house has saved (TUNAMAR on 4 August, TUNA PESCA on 9 August),
# and dropping it dropped a disappearance out of the day's total. **Membership of this
# record must not depend on whether upstream printed a flag.** The flag is now optional and
# is recorded as `null` when it is absent, which is what upstream itself publishes.
#
# What this does NOT do: rewrite the two captures of 10 August. Captures are immutable, and
# a record that gets edited when its parser improves is not a record. The vessel enters from
# the next capture forward, and the gap it left is published rather than closed — see
# `../still-dark/README.md` and `../PROJECT.md`. A work about the delay between a thing
# happening and a thing being knowable lost a ship inside its own instrument for six hours,
# and the honest place for that is the face of the work, not a silent re-parse.
CASE_RE = re.compile(
    r'The case of the day\s*</p>\s*<p class="[^"]*">([^<]+?)\s*'
    r'<span class="font-mono text-sm text-fg-faint">\((?:([A-Z]{3})|—|-|&mdash;)\)</span></p>\s*'
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
        # THE SPAN ITSELF, FROM SESSION 85 — and it is written OUTSIDE the aggregates, for
        # a reason worth the four lines. Until tonight this parser kept the numbers and
        # threw the sentence they stood in away, so a face that wanted to quote the edition
        # could only refill the regex's own literal pattern — true, because a match proves
        # those words stood in those bytes, and still not a quotation. From this capture on
        # the matched text is kept verbatim and a later face can quote instead of
        # reconstruct. The twenty-one captures already committed do not get one
        # retrospectively: captures are immutable, and a record that gets edited when the
        # method improves is not a record.
        #
        # WHY NOT INSIDE `aggregates`: that key is one of `edition.CONTENT_FIELDS`, so a
        # new sub-key would move `content_sha256` for every capture written from tonight —
        # and this work publishes the count of distinct CONTENTS on its own face. An
        # unchanged edition would have been reported as a changed one, by us, on the night
        # we improved our own parser. It sits beside `page_assets` instead: recorded,
        # outside every tier's arithmetic, and outside the digest that answers whether the
        # edition changed. The cost is stated and accepted — a rewording upstream that left
        # all four numbers standing would not move the content hash.
        #
        # The span starts at the first NUMBER and not at the match, because the pattern
        # has to bite into an attribute (`tabular-nums">`) to find it, and an attribute
        # fragment carried into a quotation is exactly the kind of thing that later gets
        # printed as the page's own words. `clean` takes the tags between the count and the
        # sentence out; what is kept is what a reader of that page reads.
        out["aggregates_text"] = clean(s[m.start(1):m.end()])
    m = VESSEL_DAYS_RE.search(s)
    if m and "aggregates" in out:
        out["aggregates"]["vessel_days_of_darkness_approx"] = num(m.group(1))
        out["vessel_days_text"] = clean(m.group(0))

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
        c["waters"] = None
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
        # The two sentences the aggregates were read out of, verbatim, from session 85.
        # SOURCED like the numbers in them, and deliberately outside `aggregates` so the
        # edition's content digest does not move on the night this parser got better.
        "aggregates_text": parsed.get("aggregates_text"),
        "vessel_days_text": parsed.get("vessel_days_text"),
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
