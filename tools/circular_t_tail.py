#!/usr/bin/env python3
"""circular_t_tail.py — the tail of UTC, and who is in it.

Banked as house material on 2026-08-19 (session 103). Companion to `circular_t.py`, which
harvests and parses BIPM Circular T; this one asks the only question the parser left open:
the median converges, so **who does not**, and are they the same institutes for thirty years?

It answers with the institution's own threshold, never one of ours, and the provenance of that
threshold needs stating carefully because the obvious citation is a withdrawn document.

- The wording this house quotes is from Recommendation **ITU-R TF.536-2 (2003)**, which
  defines UTC(k) as 'Time-scale realized by institute "k" and kept in close agreement with
  UTC, with the goal to be within +/- 100 ns, according to Recommendation S5 (1993) of the
  Consultative Committee for the Definition of the Second'.
  https://www.itu.int/dms_pubrec/itu-r/rec/tf/R-REC-TF.536-2-200305-W!!PDF-E.pdf
  **That recommendation was suppressed on 18/02/11 (CACE/529) and is marked Withdrawn**
  (https://www.itu.int/rec/R-REC-TF.536/en). It is cited here as a record of the WORDING and
  never as an instrument in force.
- The keeper still publishes the recommendation itself. Its current rules page
  (https://webtai.bipm.org/database/guidelines.html) links, under "Technical recommendation
  for UTC(k)", to https://webtai.bipm.org/database/documents/ccds-rec1993_offset_100ns.pdf —
  which is an **image-only scan** (three CCITTFax images, no font, no text layer). This house
  has NOT read its contents and does not quote it; what can be said is that the BIPM publishes
  it today as the technical recommendation for UTC(k).

It is a GOAL, not a compliance limit, requirement or tolerance, and this file says so wherever
it prints the number. It is dated 1993 — three years before the first bulletin in the corpus —
so the record does the discriminating and nothing here chooses where the line falls.

IDENTITY COMES FROM THE KEEPER TOO. A laboratory that is renamed enters the bulletin under a
new acronym and its old record does not follow it: Budapest is OMH, then MKEH, then BFKH, and
none of the three alone spans the corpus, so the register shows three laboratories where there
is one institute. This file does NOT guess at that. The BIPM publishes its own roster with a
`lab_formerly` column, and `successions()` reads it. An earlier version of this file inferred
succession from "same city, zero-day handover"; that heuristic was written and retired inside
one session (2026-08-19) after this house's verifying pass showed it abutting across cities,
treating a merger as a rename, and rejecting Pretoria CSIR -> ZA, which the roster states is
one institute. It also could never have found La Plata's TCC -> AGGO, whose two acronyms sit
under different cities in the bulletin.

The succession is not an indictment device and must not be used as one: it reveals recovery
far more often than persistence. Singapore's PSB was outside the goal on 75.2 % of its
observations and SG, the same institute, on 3.3 %; Warszawa 78.7 % -> 5.1 %; Tsukuba
77.0 % -> 8.4 %.

WHAT THIS FILE WILL NOT SAY. Not every contributor to Circular T is a national metrology
institute, and the bulletin does not claim they are. The roster's `lab_mra` column is BLANK
for 19 of the 87 active contributors, six of which are outside the goal on the corpus's last
date. A laboratory with no CIPM MRA signatory must never be described as a country's official
timekeeper or its legal time: IFAG (Wettzell) is a geodesy agency and Germany's national
metrology institute is PTB, which is in this same corpus under its own code.

Usage:
    python3 tools/circular_t_tail.py <cache-dir>
Prints: corpus integrity, the yearly series (median, share outside the goal, absolute tail
size against ensemble size), tail membership and its overlap a decade apart, the laboratories
never once outside, and the keeper's own succession chains over the whole corpus.
"""
import os
import re
import sys
import datetime
import statistics as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circular_t import get, parse, FIRST, LAST          # noqa: E402

GOAL_NS = 100.0          # CCDS Recommendation S5 (1993). A goal, not a limit. See docstring.
MJD0 = datetime.date(1858, 11, 17)


def iso(mjd):
    return (MJD0 + datetime.timedelta(days=int(mjd))).isoformat()


def load(cache, first=FIRST, last=LAST):
    """Returns (values, cities, unparsed) where values is {(lab, mjd): offset_ns}.

    Issues overlap at their edges, so a (lab, mjd) pair can be published twice; the later
    issue wins, which is also the BIPM's own order of revision.
    """
    values, cities, unparsed = {}, {}, []
    for n in range(first, last + 1):
        txt, err = get(n, cache)
        if txt is None:
            print("FETCH FAILED cirt.%d: %s" % (n, err), file=sys.stderr)
            continue
        issue, mjds, bad = parse(txt)
        if issue is None:
            print("PARSE FAILED cirt.%d" % n, file=sys.stderr)
            continue
        if bad:
            unparsed.append((n, bad))
        for m in re.finditer(r"^\s*([A-Z][A-Z0-9]{1,4})\s+\(([^)]*)\)", txt, re.M):
            cities[m.group(1)] = m.group(2).strip()
        values.update(issue)
    return values, cities, unparsed


def series(values):
    """Per-lab observation lists, sorted by date."""
    obs = {}
    for (lab, mjd), v in values.items():
        obs.setdefault(lab, []).append((mjd, v))
    for lab in obs:
        obs[lab].sort()
    return obs


ROSTER_URL = "https://webtai.bipm.org/webdb/temp/showlab.csv"


def roster(cache):
    """The BIPM's own roster of contributing laboratories, cached beside the bulletins.

    Columns that matter: `lab_ref` (the acronym used in the bulletin), `lab_formerly` (the
    acronyms this institute used before — the keeper's OWN succession record), `lab_mra` (the
    CIPM MRA signatory it belongs to; BLANK means none), `lab_stop` (blank = still active).
    Linked from https://webtai.bipm.org/database/showlab.html, which renders it as a table.
    """
    import csv
    import urllib.request
    p = os.path.join(cache, "showlab.csv")
    if not os.path.exists(p):
        os.makedirs(cache, exist_ok=True)
        with urllib.request.urlopen(ROSTER_URL, timeout=60) as r:
            open(p, "wb").write(r.read())
    return {r["lab_ref"]: r for r in csv.DictReader(open(p, encoding="latin-1"))}


def successions(reg, obs):
    """Chains of acronyms that are ONE institute, taken from the keeper's own record.

    This replaces a heuristic — same city, zero-day handover — that this house wrote and then
    retired within the same session on 2026-08-19. Its own verifying pass showed the rule
    abutting ACROSS cities at year boundaries (four codes turn over on 2006-12-30 at once),
    treating a merger as a rename, and rejecting Pretoria CSIR -> ZA, which the roster below
    states outright is one institute. Guessing identity was never necessary: the institution
    publishes it, and this house's standing principle is that the record does the
    discriminating.

    `lab_formerly` lists predecessors, separated by "|" or ",". Only codes that actually
    appear in the bulletins are kept, and the chain is ordered by first observation.
    """
    chains = []
    for code, r in reg.items():
        prev = [p.strip() for p in re.split(r"[|,]", r.get("lab_formerly", "") or "") if p.strip()]
        chain = [c for c in prev + [code] if c in obs]
        if len(chain) > 1:
            chain.sort(key=lambda c: obs[c][0][0])
            chains.append((r.get("city_ref", "").strip(), r.get("country_ref", "").strip(),
                           (r.get("lab_mra", "") or "").strip(), chain))
    return sorted(chains)


def chain_series(chain, obs):
    """One institute's observations across its successive codes, one value per grid date.

    On a handover date the bulletin lists both codes; the successor's value wins, so a joined
    record is a count of dates and never double-counts the handover.
    """
    seq = {}
    for code in chain:
        for mjd, v in obs[code]:
            seq[mjd] = v
    return sorted(seq.items())


def _outside(vs):
    return sum(1 for v in vs if abs(v) > GOAL_NS)


def _main():
    cache = sys.argv[1] if len(sys.argv) > 1 else "cirt"
    values, cities, unparsed = load(cache)
    obs = series(values)
    dates = sorted({m for _, m in values})
    print("corpus: %d laboratories, %d values, %d grid dates, %s .. %s"
          % (len(obs), len(values), len(dates), iso(dates[0]), iso(dates[-1])))
    print("unparsed lines: %d %s" % (sum(b for _, b in unparsed),
                                     ["cirt.%d:%d" % t for t in unparsed] or "(none)"))

    print("\nyear      n   median   p90    outside the +/-100 ns goal   labs/date  outside/date")
    by_year = {}
    for (lab, mjd), v in values.items():
        by_year.setdefault(iso(mjd)[:4], []).append(abs(v))
    date_labs = {}
    for (lab, mjd), v in values.items():
        date_labs.setdefault(mjd, []).append(v)
    for y in sorted(by_year):
        a = by_year[y]
        ds = [d for d in dates if iso(d)[:4] == y]
        n_labs = sum(len(date_labs[d]) for d in ds) / len(ds)
        n_out = sum(_outside(date_labs[d]) for d in ds) / len(ds)
        print("%s %6d %8.1f %7.1f %10d (%5.1f %%) %14.1f %11.1f"
              % (y, len(a), st.median(a), sorted(a)[int(.9 * len(a))],
                 _outside(a), 100 * _outside(a) / len(a), n_labs, n_out))

    def tail(y):
        return {l for (l, m), v in values.items() if iso(m)[:4] == y and abs(v) > GOAL_NS}
    print("\ntail membership a decade apart")
    for a, b in (("1996", "2006"), ("2006", "2016"), ("2016", "2026")):
        A, B = tail(a), tail(b)
        print("  %s: %3d   %s: %3d   in both: %3d  (%.0f %% of %s already in %s)"
              % (a, len(A), b, len(B), len(A & B), 100 * len(A & B) / len(B), b, a))

    last = dates[-1]
    now_out = sorted(((l, values[(l, last)]) for l in obs if (l, last) in values
                      and abs(values[(l, last)]) > GOAL_NS), key=lambda t: -abs(t[1]))
    print("\noutside the goal on %s: %d of %d laboratories" %
          (iso(last), len(now_out), sum(1 for l in obs if (l, last) in values)))
    for l, v in now_out:
        run = 0
        for m, x in reversed(obs[l]):
            if abs(x) > GOAL_NS:
                run += 1
            else:
                break
        print("   %-5s %-26s %10.1f ns   %4d consecutive, since %s"
              % (l, cities.get(l, "")[:26], v, run, iso(obs[l][len(obs[l]) - run][0])))

    reg = roster(cache)
    nonsig = {c for c, r in reg.items() if not (r.get("lab_mra") or "").strip()}
    print("\n   of those %d, the CIPM MRA signatory column of the keeper's own roster is BLANK"
          " for %d:" % (len(now_out), sum(1 for l, _ in now_out if l in nonsig)))
    print("   %s" % ", ".join(sorted(l for l, _ in now_out if l in nonsig)))
    print("   (a blank means the laboratory is not covered by the CIPM MRA. It is NOT a"
          " national metrology\n    institute's UTC(k) and must never be named as a country's"
          " legal time.)")

    print("\nnever once outside the goal")
    for l in sorted(obs):
        vs = [v for _, v in obs[l]]
        if not _outside(vs):
            print("   %-5s %-26s %4d obs" % (l, cities.get(l, "")[:26], len(vs)))

    print("\nsuccession, from the keeper's own roster (`lab_formerly`)")
    for city, country, mra, chain in successions(reg, obs):
        seq = chain_series(chain, obs)
        vs = [v for _, v in seq]
        print("   %-20s %-14s %-26s %4d obs %s .. %s  outside %d (%.1f %%)  MRA=%s"
              % (city[:20], country[:14], "->".join(chain), len(vs), iso(seq[0][0]),
                 iso(seq[-1][0]), _outside(vs), 100 * _outside(vs) / len(vs), mra or "-"))
        for c in chain:
            v2 = [v for _, v in obs[c]]
            print("        %-6s %4d obs %s .. %s  outside %d (%.1f %%)"
                  % (c, len(v2), iso(obs[c][0][0]), iso(obs[c][-1][0]),
                     _outside(v2), 100 * _outside(v2) / len(v2)))


if __name__ == "__main__":
    _main()
