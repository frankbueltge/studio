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

# The commit that first carried the struck figure and the law printed beside it. Its
# timestamp is read from git, never typed: this house has already put one publication
# date on this face out of a head, and the dates that reach a face come off a record.
PUBLISHED_COMMIT = "5968048"

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
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
         14: "fourteen", 15: "fifteen", 16: "sixteen"}


def word(n):
    """A count in words where the page speaks, in digits where it counts. Never typed."""
    return WORDS.get(n, str(n))


def printed_date(s):
    x = d(s)
    return f"{x.day} {FULL_MONTHS[x.month - 1]} {x.year}"


def day_month(s):
    """'4 August' — the day named without its year, for a second naming in one sentence."""
    x = d(s)
    return f"{x.day} {FULL_MONTHS[x.month - 1]}"


def short_caps(s):
    x = d(s)
    return f"{x.day} {MONTHS_CAPS[x.month - 1]}"


def commit_time(ref):
    """The commit's own timestamp, read from git. Raises rather than guessing."""
    out = subprocess.run(
        ["git", "-C", HERE, "log", "-1", "--format=%cI", ref],
        capture_output=True, text=True, check=True,
    )
    return datetime.datetime.fromisoformat(out.stdout.strip())


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
    pub = commit_time(PUBLISHED_COMMIT).astimezone(datetime.timezone.utc)
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
            # Short on the row, exact in the ledger. Eleven repetitions of one ISO instant
            # were eleven repetitions of this house's filing system (DRAMATURG-72 §A); the
            # instant itself is checkable four inches lower, in the OBSERVED table.
            "seen": f"first seen {short_caps(r['first_seen_utc'][:10])}",
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
            # "edition" is the instrument's word and this house's filing word; on the face
            # it is the list the instrument published that day (DRAMATURG-72 §A). It stays
            # as a column of the OBSERVED ledger, where the filing system IS the object.
            "label": (
                f"IN THE LIST OF {short_caps(ed)} — the day itself"
                if late == 0 else
                f"ADDED BY THE LIST OF {short_caps(ed)} — "
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
        "What grew was the total: "
        + " and ".join(e["name"] for e in gained)
        + f" — {word(len(gained))} ships that entered the record with the "
        + " and ".join(f"list of {short_caps(x)}" for x in gained_eds)
        + f", {word((d(gained_eds[0]) - target).days)} days after the day."
    )

    # The first sentence a cold reader meets, and the whole work if they read no further
    # (DRAMATURG-72 §B.1). Every number in it is counted here, none typed: the numerator
    # this record observes, what the later lists added, and how much of that arrived after
    # the figure below had already been published.
    n_obs = now["knowable_on_the_day_OBSERVED"]
    n_hi = now["vessels_dark_on_day"]["band"][1]
    # "the list published on the day itself" claimed a publication event this record never
    # observed: the earliest saved copy is from the following morning, and upstream prints a
    # date, not a publication instant (VERIFIER-72 D3). The list is DATED the day; that is
    # what the record holds, and that is now what the sentence says.
    #
    # And the day is NAMED here, twice, since session 73 (DRAMATURG-73 §A). Until tonight this
    # sentence said "that day" and "the day itself": the sentence built to carry the work was
    # anaphoric to a word it did not contain, pointing up to the headline, which is the first
    # thing an unaided recall drops. 72's Q1 was refuted at 2 of 3 on exactly that — one reader
    # carried the whole mechanism away and no date. The date is written where the anaphor stood,
    # and named a second time because a word carried once in a subordinate clause is what a
    # rebuilt sentence loses. Both namings are computed from DAY, like every other date here.
    lede = (
        f"{word(n_obs).capitalize()} of the ships this record can place in {printed_date(DAY)} "
        f"stood in the list dated {day_month(DAY)} itself. {word(n_hi - n_obs).capitalize()} "
        f"arrived later — {word(len(gained))} of them after this page had printed its figure."
    )

    # One list, more than one saved copy of it, and the copies differing in bytes: the
    # correction session 70 published on this face, in the plain words §A ordered.
    bodies_per_list = {}
    for c in caps_now:
        bodies_per_list.setdefault(content_sha256(c), set()).add(c["fetch"]["sha256"])
    split = {k: len(v) for k, v in bodies_per_list.items() if len(v) > 1}
    if split:
        n_lists, n_bodies = len(split), max(split.values())
        ledger_caption = (
            f"{word(n_lists).capitalize()} list came back in {word(n_bodies)} different sets of "
            f"bytes while every field this page reads stayed identical"
            if n_lists == 1 else
            f"{word(n_lists).capitalize()} lists came back in more than one set of bytes each "
            f"while every field this page reads stayed identical"
        ) + " — a copy's fingerprint is not the list's identity, which is why the table carries both."
    else:
        ledger_caption = (
            "Every saved copy of a list came back in identical bytes — a copy's fingerprint is "
            "not the list's identity, which is why the table carries both."
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
        "lede": lede,
        "field": field,
        "fall": {
            "then": share_line(then),
            "now": share_line(now),
            "as_of": PRIOR_AS_OF,
            "held": (
                f"The {word(now['knowable_on_the_day_OBSERVED'])} did not move, and cannot. No "
                "later night can put a name into a list that did not carry it."
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
                f"printed on this page {printed_date(pub.date().isoformat())} at "
                f"{pub.strftime('%H:%M')} UTC, in commit {PUBLISHED_COMMIT} — before the "
                "capture that made it fall"
            ),
            "then_published": f"at {pub.strftime('%H:%M')} UTC on {pub.day} {FULL_MONTHS[pub.month - 1]}",
        },
        "ledger": {"rows": ledger, "caption": ledger_caption},
        # The command carries its own truncation, so that what stands under "verbatim,
        # unedited" is the whole output of the command as printed. Sixteen per-ship lines
        # restated the rows above in worse type (DRAMATURG-72 §B.6); the pipe cuts them
        # where a reader would, and day.py handles the closed pipe without a traceback.
        "commands": [
            {"label": "the day", "cmd": f"python3 projects/season1/capture/day.py {DAY} | head -6"},
            {"label": "every ship, and when it arrived",
             "cmd": f"python3 projects/season1/capture/day.py {DAY}"},
            {"label": "the night before",
             "cmd": f"python3 projects/season1/capture/day.py {DAY} --as-of {PRIOR_AS_OF}"},
        ],
        "output": "".join(run_day().splitlines(keepends=True)[:6]),
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
