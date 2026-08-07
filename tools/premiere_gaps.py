#!/usr/bin/env python3
"""The premiere sequence of this house, and the gaps between its premieres.

Why this exists. On 2026-08-07 the site's build gate was red all day on an assertion in
the site's own test suite — `RECOVERY overlaps ONE TAP` — about two work names being
lettered over each other on a diagram built from this house's committed record. This
house cannot read the site repository and cannot run that test. What it can do is print,
from its own record, exactly what that diagram is drawn from: which works premiered, on
what dates, and how far apart. The smallest gap is where a label collision will happen
first, and it is a fact of the record rather than a guess about someone else's code.

    python3 tools/premiere_gaps.py
    python3 tools/premiere_gaps.py --json

Reads `chronicle.json` at the repository root: every entry whose move is "ship" and which
names a work. Nothing here is typed by hand.
"""

import argparse
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHRONICLE = os.path.join(ROOT, "chronicle.json")


def premieres():
    with open(CHRONICLE, encoding="utf-8") as f:
        entries = json.load(f)
    out = []
    for e in entries:
        if e.get("move") != "ship":
            continue
        for slug in e.get("works") or []:
            out.append({"date": e["date"], "work": slug})
    out.sort(key=lambda r: (r["date"], r["work"]))
    return out, entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    rows, entries = premieres()
    if not rows:
        print("no premieres in the record", file=sys.stderr)
        return 2

    d = datetime.date.fromisoformat
    for i, r in enumerate(rows):
        r["gap_days"] = None if i == 0 else (d(r["date"]) - d(rows[i - 1]["date"])).days

    dates = sorted({e["date"] for e in entries})
    span = (d(dates[-1]) - d(dates[0])).days

    if a.json:
        print(json.dumps({
            "premieres": rows,
            "record_span_days": span,
            "record_first_date": dates[0],
            "record_last_date": dates[-1],
            "entries": len(entries),
        }, indent=2))
        return 0

    print("premieres in the committed record\n")
    print(f"{'date':<12} {'gap':>6}   work")
    for r in rows:
        gap = "" if r["gap_days"] is None else f"{r['gap_days']} d"
        print(f"{r['date']:<12} {gap:>6}   {r['work']}")

    gaps = [r for r in rows if r["gap_days"] is not None]
    tight = min(gaps, key=lambda r: r["gap_days"])
    i = rows.index(tight)
    print(f"\nsmallest gap: {tight['gap_days']} d, "
          f"{rows[i - 1]['work']} → {tight['work']}")
    print(f"record: {len(entries)} entries over {span} days "
          f"({dates[0]} → {dates[-1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
