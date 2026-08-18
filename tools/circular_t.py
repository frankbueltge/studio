#!/usr/bin/env python3
"""circular_t.py — harvest and parse BIPM Circular T, section 1: [UTC-UTC(k)]/ns.

Banked as house material on 2026-08-18 (session 102) at the Kritiker's instruction, after the
UNISON concept died at the gate. The concept is dead and does not return; the parser is not,
because the neighbour search that ran the same evening established two things worth keeping:
no artist has used Circular T as material, and a repository search for Circular T parsers
returned nothing. So this is the only one this house knows of, and it works.

What it reads. Circular T is the BIPM's monthly bulletin, published since 1996, whose first
section gives [UTC-UTC(k)]/ns on a five-day grid: how far each national laboratory's own
realization of UTC — the legal time in that country — sat from true UTC, in nanoseconds.
364 issues exist as of 2026-08-18 (cirt.100 .. cirt.463; cirt.464 is 404). CC BY 4.0,
https://www.bipm.org/en/copyright. Issues are ~24-37 KB of plain text.

Two layouts, both handled: the 1996-2002 form (four date columns, integer nanoseconds, no
uncertainty columns) and the 2003- form (seven date columns, one decimal, followed by uA/uB/u
which must NOT be mistaken for offsets). The number of offset columns is taken from the count
of five-digit MJDs in the header, never assumed.

What it refuses to do. Missing values are the literal "-" in the bulletin and are returned as
None, never as zero. A line that does not yield exactly the header's number of values is
counted as unparsed and reported; nothing is silently dropped. Across 32 issues sampled every
twelfth from 1996 to 2026, unparsed lines: 0.

Usage:
    python3 tools/circular_t.py <cache-dir> [first] [last] [step]
Prints one row per issue: labs, values, median |offset|, p90, max, share within 10 ns / 100 ns,
and unparsed lines. Import `get` and `parse` to use it as a library.
"""
import re
import os
import sys
import urllib.request
import statistics as st

BASE = "https://webtai.bipm.org/ftp/pub/tai/Circular-T/cirt/cirt.%d"
FIRST, LAST = 100, 463          # as of 2026-08-18; cirt.464 returns 404
NUM = re.compile(r"^-?\d+(?:\.\d+)?$")


def get(n, cache):
    """Fetch issue n, caching to disk. Returns (text, error)."""
    os.makedirs(cache, exist_ok=True)
    p = os.path.join(cache, "cirt.%d" % n)
    if not os.path.exists(p):
        try:
            with urllib.request.urlopen(BASE % n, timeout=60) as r:
                open(p, "wb").write(r.read())
        except Exception as e:                      # noqa: BLE001 — reported, not swallowed
            return None, str(e)
    return open(p, encoding="latin-1").read(), None


def parse(txt):
    """Parse section 1. Returns (rows, n_dates, n_unparsed) where rows is
    [(lab_code, [offset_ns or None, ...]), ...]."""
    lines = txt.splitlines()
    mjd_i = next((i for i, l in enumerate(lines[:60]) if re.search(r"\bMJD\b", l)), None)
    if mjd_i is None:
        return None, None, None
    n = len([t for t in lines[mjd_i].split() if re.fullmatch(r"\d{5}", t)])
    if n == 0:
        return None, None, None
    rows, bad = [], 0
    for l in lines[mjd_i + 1:]:
        if not l.strip():
            continue
        if re.match(r"\s*\d+\s*-\s", l):            # next numbered section of the bulletin
            break
        m = re.match(r"\s*([A-Z][A-Z0-9]{1,4})\s+\(", l)
        if not m:
            continue
        rest = re.sub(r"\([^)]*\)", " ", l[m.end() - 1:])   # drop (City) and note markers
        vals = []
        for t in rest.split():
            if len(vals) == n:
                break                               # stop before uA/uB/u
            if t == "-":
                vals.append(None)
            elif NUM.match(t):
                vals.append(float(t))
            else:
                bad += 1
                break
        if len(vals) == n:
            rows.append((m.group(1), vals))
        else:
            bad += 1
    return rows, n, bad


def _main():
    cache = sys.argv[1] if len(sys.argv) > 1 else "cirt"
    first = int(sys.argv[2]) if len(sys.argv) > 2 else FIRST
    last = int(sys.argv[3]) if len(sys.argv) > 3 else LAST
    step = int(sys.argv[4]) if len(sys.argv) > 4 else 12
    print("issue  labs  vals  median|d|      p90|d|      max|d|  <=10ns  <=100ns  unparsed")
    for k in list(range(first, last + 1, step)) + ([last] if (last - first) % step else []):
        txt, err = get(k, cache)
        if txt is None:
            print("%5d  FETCH FAILED: %s" % (k, err))
            continue
        rows, _, bad = parse(txt)
        if not rows:
            print("%5d  PARSE FAILED (no rows)" % k)
            continue
        v = [abs(x) for _, vs in rows for x in vs if x is not None]
        print("%5d %5d %6d %10.1f %11.1f %11.1f %7.2f %8.2f %9d"
              % (k, len(rows), len(v), st.median(v), sorted(v)[int(.9 * len(v))], max(v),
                 sum(1 for x in v if x <= 10) / len(v),
                 sum(1 for x in v if x <= 100) / len(v), bad))


if __name__ == "__main__":
    _main()
