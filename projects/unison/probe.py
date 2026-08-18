#!/usr/bin/env python3
"""Probe for the UNISON concept: does BIPM Circular T actually show a spread of
local UTC realizations, and which way does it move over thirty years?

Fetches a sample of Circular T issues, parses section 1 ([UTC-UTC(k)]/ns), and
reports, per issue: labs present, and the distribution of |UTC-UTC(k)|.
Reports parse failures rather than dropping them.
"""
import re, sys, os, json, urllib.request, statistics as st

BASE = "https://webtai.bipm.org/ftp/pub/tai/Circular-T/cirt/cirt.%d"
CACHE = sys.argv[1] if len(sys.argv) > 1 else "cirt"
os.makedirs(CACHE, exist_ok=True)

def get(n):
    p = os.path.join(CACHE, "cirt.%d" % n)
    if not os.path.exists(p):
        try:
            with urllib.request.urlopen(BASE % n, timeout=60) as r:
                open(p, "wb").write(r.read())
        except Exception as e:
            return None, str(e)
    return open(p, encoding="latin-1").read(), None

NUM = re.compile(r"^-?\d+(?:\.\d+)?$")

def parse(txt):
    """Return (list_of_(lab, [offsets]), n_dates, n_unparsed_lines)."""
    lines = txt.splitlines()
    # locate the MJD header of section 1
    mjd_i = None
    for i, l in enumerate(lines[:60]):
        if re.search(r"\bMJD\b", l):
            mjd_i = i
            break
    if mjd_i is None:
        return None, None, None
    mjds = [t for t in lines[mjd_i].split() if re.fullmatch(r"\d{5}", t)]
    n = len(mjds)
    if n == 0:
        return None, None, None
    rows, bad = [], 0
    for l in lines[mjd_i + 1:]:
        if not l.strip():
            continue
        if re.match(r"\s*\d+\s*-\s", l):      # next numbered section
            break
        m = re.match(r"\s*([A-Z][A-Z0-9]{1,4})\s+\(", l)
        if not m:
            continue
        lab = m.group(1)
        rest = re.sub(r"\([^)]*\)", " ", l[m.end() - 1:])   # drop (City) and note refs
        toks = rest.split()
        vals = []
        for t in toks:
            if len(vals) == n:
                break
            if t == "-":
                vals.append(None)
            elif NUM.match(t):
                vals.append(float(t))
            else:
                bad += 1
                break
        if len(vals) == n:
            rows.append((lab, vals))
        else:
            bad += 1
    return rows, n, bad

def frac(v, lim):
    return sum(1 for x in v if abs(x) <= lim) / len(v)

issues = list(range(100, 464, 12)) + [463]
print("issue  date-guess  labs  vals  median|d|   p90|d|      max|d|   <=10ns  <=100ns  unparsed")
series = []
for k in issues:
    txt, err = get(k)
    if txt is None:
        print("%5d  FETCH FAILED: %s" % (k, err)); continue
    rows, n, bad = parse(txt)
    if not rows:
        print("%5d  PARSE FAILED (no rows)" % k); continue
    d = re.search(r"(19|20)\d\d[^\n]{0,20}", txt[:400])
    vals = [v for _, vs in rows for v in vs if v is not None]
    med, p90 = st.median(map(abs, vals)), sorted(map(abs, vals))[int(.9 * len(vals))]
    print("%5d  %-10s %5d %6d %10.1f %10.1f %11.1f %7.2f %8.2f %9d"
          % (k, (d.group(0)[:10] if d else "?"), len(rows), len(vals),
             med, p90, max(map(abs, vals)), frac(vals, 10), frac(vals, 100), bad))
    series.append(dict(issue=k, labs=len(rows), median=med, p90=p90,
                       within10=frac(vals, 10), within100=frac(vals, 100)))
json.dump(series, open(os.path.join(CACHE, "..", "probe-result.json"), "w"), indent=1)
