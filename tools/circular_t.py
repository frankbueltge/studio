#!/usr/bin/env python3
"""circular_t.py — harvest and parse BIPM Circular T, section 1: [UTC-UTC(k)]/ns.

Banked as house material on 2026-08-18 (session 102) at the Kritiker's instruction, after the
UNISON concept died at the gate. The concept is dead and does not return; the parser is not,
because the neighbour search that ran the same evening established two things worth keeping:
no artist has used Circular T as material, and a repository search for Circular T parsers
returned nothing. So this is the only one this house knows of.

**CORRECTED 2026-08-19 (session 103), and the correction is large.** The version banked on
2026-08-18 read only the FIRST page of section 1. In the 1996-2002 layout that section runs
across two pages: the first carries four date columns, then a page break, then the banner
`1 - Coordinated Universal Time UTC. (Cont.)` and a SECOND MJD header with the remaining
three. The old code took one header from the first 60 lines and stopped at the first line
matching a section banner — which is the continuation banner — so **it silently discarded
three of every seven dates in every issue from 1996 to 2002.** Every figure session 102
published from this file is wrong by that much; the corrections are recorded in
`memory/dossiers/circular-t-tail.md` and in the journal of session 103. Found by this house's
own verifying pass, which wrote its own parser rather than trusting this one.

The trap the fix must not fall into: section 2 is `2 - International Atomic Time TAI and
local atomic time scales TA(k)`, and its rows have exactly the same shape as section 1's
while carrying a DIFFERENT QUANTITY, TAI-TA(k). Parsing "every MJD header in the file" would
silently mix the two. Section 1 therefore ends at the first banner whose section number is
not 1, and that is the whole rule.

What it reads. Circular T is the BIPM's monthly bulletin, published since 1996, whose first
section gives [UTC-UTC(k)]/ns on a five-day grid: how far laboratory k's own realization of
UTC sat from UTC, in nanoseconds. 364 issues exist as of 2026-08-19 (cirt.100 .. cirt.463;
cirt.464 is 404). CC BY 4.0, https://www.bipm.org/en/copyright. Issues are ~24-37 KB of text.

**Not every contributor is a national metrology institute**, and this file must not be read as
saying so. The version banked on 2026-08-18 described section 1 as "each national laboratory's
own realization of UTC — the legal time in that country". That sentence was false and is
withdrawn: IFAG (Wettzell) is a geodesy agency, CAO (Cagliari) an astronomical observatory,
and 19 of the 87 currently listed contributors carry no CIPM MRA signatory status at all. The
BIPM publishes the roster with that column at https://webtai.bipm.org/database/showlab.html.

Two layouts, both handled: the 1996-2002 form (four + three date columns across two pages,
integer nanoseconds, no uncertainty columns) and the 2003- form (seven date columns on one
page, one decimal, followed by uA/uB/u which must NOT be mistaken for offsets). The number of
offset columns is taken from the count of five-digit MJDs in each header, never assumed.

What it refuses to do. Missing values are the literal "-" in the bulletin and are absences,
never zero. A line that does not yield exactly its header's number of values is counted as
unparsed and reported; nothing is silently dropped. Across all 364 issues, unparsed lines: 1
(cirt.190, `CNMP (Panama)`, six values printed under a seven-date header — the row is refused
rather than guessed at).

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
FIRST, LAST = 100, 463          # as of 2026-08-19; cirt.464 returns 404
NUM = re.compile(r"^-?\d+(?:\.\d+)?$")
BANNER = re.compile(r"^\s*(\d+)\s*-\s")            # "1 - ... (Cont.)" / "2 - ..."
MJD_HDR = re.compile(r"\bMJD\b")
LABROW = re.compile(r"\s*([A-Z][A-Z0-9]{1,4})\s+\(")


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
    """Parse section 1 across all its pages.

    Returns (values, mjds, n_unparsed) where `values` is {(lab_code, mjd): offset_ns} and
    `mjds` is the sorted list of grid dates this issue publishes. Absent values simply do not
    appear in the mapping — there is no None to mistake for a number.
    """
    lines = txt.splitlines()
    start = next((i for i, l in enumerate(lines) if BANNER.match(l)
                  and BANNER.match(l).group(1) == "1"), None)
    if start is None:
        return None, None, None

    values, mjds, cur, bad = {}, set(), None, 0
    for l in lines[start + 1:]:
        m = BANNER.match(l)
        if m:
            if m.group(1) != "1":
                break                               # section 2 onward: a different quantity
            cur = None                              # continuation page: await its own header
            continue
        if MJD_HDR.search(l):
            cur = [int(t) for t in l.split() if re.fullmatch(r"\d{5}", t)]
            if not cur:
                cur = None
            else:
                mjds.update(cur)
            continue
        if cur is None or not l.strip():
            continue
        lm = LABROW.match(l)
        if not lm:
            continue
        rest = re.sub(r"\([^)]*\)", " ", l[lm.end() - 1:])   # drop (City) and note markers
        vals = []
        for t in rest.split():
            if len(vals) == len(cur):
                break                               # stop before uA/uB/u
            if t == "-":
                vals.append(None)
            elif NUM.match(t):
                vals.append(float(t))
            else:
                bad += 1
                break
        if len(vals) == len(cur):
            for mjd, v in zip(cur, vals):
                if v is not None:
                    values[(lm.group(1), mjd)] = v
        else:
            bad += 1
    return values, sorted(mjds), bad


def _main():
    cache = sys.argv[1] if len(sys.argv) > 1 else "cirt"
    first = int(sys.argv[2]) if len(sys.argv) > 2 else FIRST
    last = int(sys.argv[3]) if len(sys.argv) > 3 else LAST
    step = int(sys.argv[4]) if len(sys.argv) > 4 else 12
    print("issue  labs  dates  vals  median|d|      p90|d|      max|d|  <=10ns  <=100ns  unparsed")
    for k in list(range(first, last + 1, step)) + ([last] if (last - first) % step else []):
        txt, err = get(k, cache)
        if txt is None:
            print("%5d  FETCH FAILED: %s" % (k, err))
            continue
        values, mjds, bad = parse(txt)
        if not values:
            print("%5d  PARSE FAILED (no values)" % k)
            continue
        v = [abs(x) for x in values.values()]
        print("%5d %5d %6d %5d %10.1f %11.1f %11.1f %7.2f %8.2f %9d"
              % (k, len({lab for lab, _ in values}), len(mjds), len(v), st.median(v),
                 sorted(v)[int(.9 * len(v))], max(v),
                 sum(1 for x in v if x <= 10) / len(v),
                 sum(1 for x in v if x <= 100) / len(v), bad))


if __name__ == "__main__":
    _main()
