#!/usr/bin/env python3
"""STILL DARK — build the work's data island from the committed captures.

Why this exists. This house has twice put a number on a face that came out of a head
instead of off a record: session 66 dropped a vessel from a shelf the conductor had
counted first-hand, and session 70 caught a sha256 written from memory before the real
one was read off the capture. Both were caught, neither should have been possible. From
tonight the figures the work prints are COMPUTED from `../captures/*.json` by this
script and pasted into `index.html` as one block; nothing in that block is typed by
hand, and re-running the script is how anyone checks that the page belongs to the
record.

    python3 data.py            # print the JSON island
    python3 data.py --check    # exit 1 if index.html's island differs from a fresh build

Tiers, unchanged and never merged:
  SOURCED  — vessel name, flag, days dark, waters, edition date: printed upstream.
  DERIVED  — the two-ended date bands, and the arithmetic of the share.
  OBSERVED — the captures: fetch time, status, bytes, hashes, and which edition first
             carried a vessel. This house's record of its own knowing.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAPTURE_DIR = os.path.normpath(os.path.join(HERE, "..", "capture"))
CAPTURES = os.path.normpath(os.path.join(HERE, "..", "captures"))
sys.path.insert(0, CAPTURE_DIR)

from day import analyse, bands, index, load  # noqa: E402
from edition import content_sha256  # noqa: E402

DAY = "2026-08-04"
DAY_PRINTED = "4 AUGUST 2026"

# The night whose figure the page strikes through: the last capture before tonight's.
# Named, not guessed — the page prints it, and `day.py --as-of` reproduces it.
PRIOR_AS_OF = "2026-08-06T04:36:19Z"

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_CAPS = [m.upper() for m in MONTHS]


def d(s):
    return datetime.date.fromisoformat(s)


def span(a, b):
    """'2–9 Jun' where the months agree, '27 Jun–4 Jul' where they do not."""
    if a.month == b.month:
        return f"{a.day}–{b.day} {MONTHS[a.month - 1]}"
    return f"{a.day} {MONTHS[a.month - 1]}–{b.day} {MONTHS[b.month - 1]}"


FULL_MONTHS = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven"}


def printed_date(s):
    x = d(s)
    return f"{x.day} {FULL_MONTHS[x.month - 1]} {x.year}"


def short_caps(s):
    x = d(s)
    return f"{x.day} {MONTHS_CAPS[x.month - 1]}"


def run_day(*args):
    """The verbatim output the page prints, produced by the script the page names."""
    out = subprocess.run(
        [sys.executable, os.path.join(CAPTURE_DIR, "day.py"), DAY, *args],
        capture_output=True, text=True, check=True,
    )
    return out.stdout


def share_line(a):
    """(figure, numerator, denominator band) for one analysis, from the script's own fields."""
    lo, hi = a["share_knowable_OBSERVED"]
    n = a["knowable_on_the_day_OBSERVED"]
    b = a["vessels_dark_on_day"]["band"]
    return {
        "figure": f"{round(lo * 100)} %–{round(hi * 100)} %",
        "of": f"{n} of {b[0]}–{b[1]}",
        "editions": len(a["editions_read"]),
        "captures": a["captures_read"],
    }


def build():
    caps_now = load(CAPTURES)
    caps_then = load(CAPTURES, as_of=PRIOR_AS_OF)
    now = analyse(DAY, caps_now)
    then = analyse(DAY, caps_then)

    # gfw ids and waters, from the capture that first carried each vessel
    gfw = {}
    for c in caps_now:
        for v in c.get("vessels", []):
            gfw.setdefault(v["name"], v.get("gfw_url"))

    rows_by_name = index(caps_now)
    seen_at = {r["name"]: r for r in rows_by_name.values()}

    groups = {}
    for e in now["certain"] + now["possible"]:
        r = seen_at[e["name"]]
        end_lo, end_hi = bands(r)
        dark_lo = end_lo - datetime.timedelta(days=e["days_dark"])
        dark_hi = end_hi - datetime.timedelta(days=e["days_dark"])
        row = {
            "name": e["name"],
            "flag": e["flag"],
            "days_dark": e["days_dark"],
            "waters": e["waters"] or "",
            "went_dark_between": [dark_lo.isoformat(), dark_hi.isoformat()],
            "resurfaced_between": [end_lo.isoformat(), end_hi.isoformat()],
            "band_text": f"dark {span(dark_lo, dark_hi)} → back {span(end_lo, end_hi)}",
            "gfw_url": gfw.get(e["name"]),
            "seen": f"first seen {r['first_seen_utc']}",
        }
        groups.setdefault(r["first_edition_date"], []).append(row)

    target = d(DAY)
    field = []
    for ed in sorted(groups):
        late = (d(ed) - target).days
        rows = sorted(groups[ed], key=lambda r: -r["days_dark"])
        field.append({
            "edition": ed,
            "edition_printed": printed_date(ed),
            "days_after": late,
            "label": (
                f"IN THE EDITION OF {short_caps(ed)} — the day itself"
                if late == 0 else
                f"ADDED BY THE EDITION OF {short_caps(ed)} — "
                f"{'one day' if late == 1 else WORDS.get(late, str(late)) + ' days'} after the day"
            ),
            "count": len(rows),
            "rows": rows,
        })

    # what moved since the struck figure was true: the vessels this day gained from
    # captures later than PRIOR_AS_OF, named, with the edition that carried them
    then_names = {e["name"] for e in then["certain"] + then["possible"]}
    gained = [e for e in now["certain"] + now["possible"] if e["name"] not in then_names]
    gained.sort(key=lambda e: -e["days_dark"])
    gained_eds = sorted({seen_at[e["name"]]["first_edition_date"] for e in gained})
    moved = (
        "The denominator moved, by "
        + " and ".join(e["name"] for e in gained)
        + f" — {WORDS.get(len(gained), str(len(gained)))} ships that entered the record with the "
        + " and ".join(f"edition of {short_caps(x)}" for x in gained_eds)
        + f", {WORDS.get((d(gained_eds[0]) - target).days, '')} days after the day."
    )

    ledger = []
    for c in caps_now:
        ledger.append({
            "fetched_at_utc": c["fetch"]["fetched_at_utc"],
            "http_status": c["fetch"]["http_status"],
            "bytes": c["fetch"]["bytes"],
            "sha256": c["fetch"]["sha256"][:8],
            "content_sha256": content_sha256(c)[:8],
            "edition_date_printed": c["edition_date_printed"],
            "vessels": len(c.get("vessels", [])),
        })

    return {
        "day": {"iso": DAY, "printed": DAY_PRINTED},
        "method": {
            "source": "https://frankbueltge.de/werke/ghost-fleet/",
            "edition_source": "https://frankbueltge.de/ghost-fleet/",
            "window_quote": caps_now[-1]["method"]["window_quote"],
        },
        "field": field,
        "fall": {
            "then": share_line(then),
            "now": share_line(now),
            "as_of": PRIOR_AS_OF,
            "held": (
                f"{now['knowable_on_the_day_OBSERVED']} did not move. No later night can put a "
                "name into an edition that did not carry it."
            ),
            "moved": moved,
            "published": (
                "A ceiling that can only fall. A further night can add a ship to a past day. It "
                "can never remove one, and it can never put a name into an edition that did not "
                "carry it."
            ),
            # Dated to the commit that first carried THIS sentence, not to an earlier,
            # differently-worded ancestor of it. The Verifier's blocking pass in session 71
            # caught the earlier claim ("and in this record since 5 August") as false by a
            # full day: the ancestor said the share can only fall, but it is not this
            # sentence, and a quotation may not borrow its ancestor's date.
            "published_when": (
                "printed on this page 6 August 2026 at 04:57 UTC, in commit 5968048 — "
                "before the capture that made it fall"
            ),
        },
        "ledger": {
            "rows": ledger,
            "caption": (
                f"{len(ledger)} captures · {len({r['edition_date_printed'] for r in ledger})} editions · "
                f"{len({r['content_sha256'] for r in ledger})} contents · "
                f"{len({r['sha256'] for r in ledger})} bodies — a raw body hash is not an edition's "
                "identity; the content column is."
            ),
        },
        "commands": [
            {"label": "the day", "cmd": f"python3 projects/season1/capture/day.py {DAY}"},
            {"label": "the night before",
             "cmd": f"python3 projects/season1/capture/day.py {DAY} --as-of {PRIOR_AS_OF}"},
        ],
        "output": run_day(),
        "floor": (
            f"No number closes this. A method that counts a disappearance only when the ship comes "
            f"back cannot see the ships that never come back. {now['vessels_dark_on_day']['band'][1]} "
            f"is what this record can place in {printed_date(DAY)}, not what was on the sea that day."
        ),
    }


ISLAND = re.compile(
    r'(<script type="application/json" id="sd-data">\n)(.*?)(\n  </script>)', re.S
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    blob = json.dumps(build(), indent=2, ensure_ascii=False)
    path = os.path.join(HERE, "index.html")
    if a.check or a.write:
        with open(path, encoding="utf-8") as f:
            html = f.read()
        m = ISLAND.search(html)
        if not m:
            print("no data island found in index.html", file=sys.stderr)
            return 2
        if a.check:
            same = json.loads(m.group(2)) == json.loads(blob)
            print("island matches the captures" if same else "ISLAND DIFFERS from the captures")
            return 0 if same else 1
        with open(path, "w", encoding="utf-8") as f:
            f.write(html[:m.start(2)] + blob + html[m.end(2):])
        print(f"island written: {len(blob)} bytes")
        return 0
    print(blob)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
