#!/usr/bin/env python3
"""stage_pressure.py — why the site's stage figure collides, and when it will collide again.

Session 106 judged the build gate's failure rather than finding it, and said so on its own
face: *"offered as a judgement, not a finding, because this session could not read the site
source."* That was true of the site repository. It was not true of this one. Session 99
proposed a repair through `site-prs/` and, in doing so, committed a copy of the two files
under discussion into this repository:

    site-prs/studio-returns-after-the-privacy-rule/files/src/lib/studio/season.ts
    site-prs/studio-returns-after-the-privacy-rule/files/src/lib/studio/season.test.ts

The failing assertion the build letter quotes is `season.test.ts:187`, and line 187 of our
mirror is that assertion, character for character. So the diagnosis below is first-hand
against a mirror, and the mirror's currency is itself evidence: a stale copy would not have
the failing line at the failing line number.

WHAT THIS MEASURES. The stage figure places one "pool" per premiered work on a time axis.
A pool is as wide as the title it lights (`poolRx`), and the axis is the whole chronicle's
date span mapped onto a fixed 1034 px. Every session that lands extends `lastDate` by a day,
so the axis buys one more day with the same pixels and every existing pool slides left into
a tighter cluster — while the pools themselves never get narrower, because a title's length
does not change. The figure then asks a relaxation to push them apart again.

This script reports the pressure that relaxation is under: how much horizontal room the
pools need, how much the axis actually gives them where they sit, and how that gap has moved
and will move. It does NOT reproduce the layout. `relaxOverlaps` lives in
`src/lib/dataviz/geometry.ts`, which is not mirrored here, so whether 24 iterations converge
is not knowable from this repository. What IS knowable is the pressure, and the pressure is
the thing that grows every night.

ASSUMPTION, NAMED. `bandScale` is read as a linear map from the date domain onto
[AXIS.x0, AXIS.x1]. Its source is not in our mirror either. If it pads its domain, the
absolute figures below shift; the direction and the per-day rate do not, because both follow
from the domain widening by one day per landed session against a fixed pixel range.

Usage:  python3 tools/stage_pressure.py
        python3 tools/stage_pressure.py --forecast 30
"""

import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
MIRROR = os.path.join(
    REPO, "site-prs", "studio-returns-after-the-privacy-rule", "files",
    "src", "lib", "studio", "season.ts",
)

# Constants read out of the mirror rather than typed here, so this script fails loudly if the
# figure's geometry changes under it instead of quietly measuring a stage that no longer exists.
WANTED = {
    "AXIS_X0": r"const AXIS = \{ x0: (\d+)",
    "AXIS_X1": r"const AXIS = \{ x0: \d+, x1: (\d+)",
    "FLOOR_X0": r"const FLOOR = \{ x0: (\d+)",
    "FLOOR_X1": r"x1: (\d+), y1:",
    "POOL_RY": r"const POOL_RY = (\d+)",
    "LIT_JITTER": r"const LIT_JITTER = (\d+)",
    "POOL_RX_MIN": r"Math\.max\((\d+), 26 \+ label\.length",
    "POOL_RX_BASE": r"Math\.max\(\d+, (\d+) \+ label\.length",
    "POOL_RX_PER": r"label\.length \* ([\d.]+)\)",
}
# The lit band's relaxation call: settle(lit, ..., 0, 18) — the 18 is the gap.
GAP_RE = r"\.\.\.settle\(lit, LIT_Y - LIT_JITTER, LIT_Y \+ LIT_JITTER, 0, (\d+)\)"


def constants():
    src = open(MIRROR, encoding="utf-8").read()
    out = {}
    for name, pat in WANTED.items():
        m = re.search(pat, src)
        if not m:
            raise SystemExit(f"stage_pressure.py: {name} not found in the mirror — the figure has "
                             f"changed shape and this instrument is measuring a stage that is gone")
        out[name] = float(m.group(1))
    m = re.search(GAP_RE, src)
    if not m:
        raise SystemExit("stage_pressure.py: the lit band's relaxation gap not found in the mirror")
    out["GAP"] = float(m.group(1))
    return out


def pool_rx(label, c):
    return max(c["POOL_RX_MIN"], c["POOL_RX_BASE"] + len(label) * c["POOL_RX_PER"])


def works(chronicle):
    """One (date, TITLE) per premiere, read the way the figure reads it: move == 'ship'."""
    out = []
    for e in chronicle:
        if e.get("move") != "ship":
            continue
        slug = (e.get("works") or [None])[0]
        if not slug:
            continue
        meta_path = os.path.join(REPO, "works", slug, "meta.json")
        if not os.path.exists(meta_path):
            continue
        title = json.load(open(meta_path, encoding="utf-8"))["title"].upper()
        out.append((e["date"], title))
    return out


def report(chronicle, c, last_date=None):
    days = lambda d: (datetime.date.fromisoformat(d) - first).days  # noqa: E731
    dates = [e["date"] for e in chronicle]
    first = datetime.date.fromisoformat(min(dates))
    last = datetime.date.fromisoformat(last_date or max(dates))
    span = (last - first).days
    px_per_day = (c["AXIS_X1"] - c["AXIS_X0"]) / span

    marks = []
    for date, title in works(chronicle):
        marks.append({
            "title": title,
            "date": date,
            "x": c["AXIS_X0"] + days(date) * px_per_day,
            "rx": pool_rx(title, c),
        })
    marks.sort(key=lambda m: m["x"])

    # Room the whole band needs if every pool stayed on one row, against the room the
    # relaxation is allowed to use (settle's own bounds: FLOOR.x0 + 40 .. FLOOR.x1 - 40).
    need_total = 2 * sum(m["rx"] for m in marks) + c["GAP"] * (len(marks) - 1)
    have_total = (c["FLOOR_X1"] - 40) - (c["FLOOR_X0"] + 40)

    print(f"axis: {span} days over {c['AXIS_X1'] - c['AXIS_X0']:.0f} px = "
          f"{px_per_day:.2f} px/day   (first {first}, last {last})")
    print(f"band: needs {need_total:.0f} px on one row, relaxation may use {have_total:.0f} px "
          f"-> slack {have_total - need_total:+.0f} px")
    print()
    worst = None
    for a, b in zip(marks, marks[1:]):
        gap = b["x"] - a["x"]
        need = a["rx"] + b["rx"] + c["GAP"]
        deficit = need - gap
        flag = "COLLIDES" if gap < a["rx"] + b["rx"] else "clear   "
        print(f"  {flag}  {a['title']:<18} -> {b['title']:<18} "
              f"axis gives {gap:6.1f} px, pools want {need:6.1f} px, deficit {deficit:+7.1f}")
        if worst is None or deficit > worst[0]:
            worst = (deficit, a["title"], b["title"])
    print()
    print(f"  worst pair: {worst[1]} / {worst[2]}, {worst[0]:.1f} px of separation to be found")
    print(f"  vertical escape: two pools clear each other at |dy| >= {2 * c['POOL_RY']:.0f} px; "
          f"the lit band is {2 * c['LIT_JITTER']:.0f} px tall, so a two-row split is "
          f"{'possible' if 2 * c['LIT_JITTER'] >= 2 * c['POOL_RY'] else 'IMPOSSIBLE'}")
    return worst[0], px_per_day


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forecast", type=int, default=0,
                    help="also report the pressure N days from the chronicle's last date")
    a = ap.parse_args()
    c = constants()
    chronicle = json.load(open(os.path.join(REPO, "chronicle.json"), encoding="utf-8"))
    print("=== tonight ===")
    today_deficit, _ = report(chronicle, c)
    if a.forecast:
        last = max(e["date"] for e in chronicle)
        future = (datetime.date.fromisoformat(last)
                  + datetime.timedelta(days=a.forecast)).isoformat()
        print(f"\n=== the same figure {a.forecast} days later, nothing else changed ===")
        later_deficit, _ = report(chronicle, c, last_date=future)
        rate = (later_deficit - today_deficit) / a.forecast
        print(f"\n  the worst pair loses {rate:.2f} px of separation per day the record "
              f"keeps being published")
    return 0


if __name__ == "__main__":
    sys.exit(main())
