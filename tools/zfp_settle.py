#!/usr/bin/env python3
"""Measure the vocabulary of the public forecast and settle it against the sky.

Reads the cache written by tools/zfp_harvest.py and prints, with its bookkeeping:

  A  what the record offers, per office — how often it gives a number, a word, or nothing
  B  the histogram of the numbers it states, and the ones it never states
  C  what the words are worth where the record itself pairs one word with one number
  D  what the sky did after each number, and after each word standing alone
  E  what the sky did after the periods that named no precipitation at all

Three things this instrument refuses to do, each because a first pass did it and was wrong:

* It does not treat the boilerplate "chance of precipitation 40 percent" as a use of the
  categorical word "chance". Every numeric period carries that phrase, so counting it
  reports the word in 100 % of numeric periods and the pairing it produces is noise.
* It does not count a likelihood word as a claim about rain unless a precipitation noun
  attaches to it. "Patchy" attaches to precipitation in 12 % of its appearances and
  "widespread" in 32 %; the rest are fog and frost.
* It does not silently drop what it cannot resolve. Periods whose label does not map onto
  one of the service's own twelve-hour blocks, and blocks the station did not observe,
  are counted and printed.

Usage:  python3 tools/zfp_settle.py [--cache DIR]
"""
import argparse
import collections
import csv
import datetime
import math
import os
import re
import sys

OFFICE_STATION = {"DMX": "DSM", "SEW": "SEA", "PSR": "PHX",
                  "MFL": "MIA", "OKX": "NYC", "BOU": "DEN"}
WEEKDAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
MONTHS = {m: i + 1 for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])}
ISSUED_RE = re.compile(
    r"^(\d{1,2})(\d{2})\s+(AM|PM)\s+([A-Z]{3,4})\s+(\w{3})\s+(\w{3})\s+(\d{1,2})\s+(\d{4})$", re.I)

PRECIP_NOUN = (r"(rain|showers?|thunderstorms?|tstms?|snow|drizzle|sleet|flurries|"
               r"precipitation|storms?|hail|wintry|ice|freezing|sprinkles|graupel|squalls?)")
WORDS = ["slight chance", "likely", "isolated", "scattered", "numerous",
         "periods of", "occasional"]
ATTACH = {w: re.compile(rf"\b{re.escape(w)}\b[^.]{{0,40}}?{PRECIP_NOUN}", re.I) for w in WORDS}
ATTACH["likely"] = re.compile(rf"{PRECIP_NOUN}[^.]{{0,30}}?\blikely\b", re.I)
ANY_PCT = re.compile(r"(\d{1,3})\s*percent", re.I)
ATTACHED = re.compile(r"\b(\d{1,3})\s*percent\s+chance\s+of\s+([a-z ]{3,30})", re.I)
TRAILING = re.compile(
    r"\bchance\s+of\s+(?:measurable\s+)?([a-z ]{3,30}?)\s*(?:is|near|around)?\s*(\d{1,3})\s*percent",
    re.I)

# The service's own published mapping, https://www.weather.gov/hun/zfp_terminology
POLICY = {"slight chance": (20, 20), "likely": (60, 70), "isolated": (10, 20),
          "scattered": (30, 50), "numerous": (60, 70),
          "periods of": (80, 100), "occasional": (80, 100)}


def wilson(k, n):
    if n == 0:
        return (0.0, 0.0)
    p, z = k / n, 1.96
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def parse_issued(s):
    m = ISSUED_RE.match(" ".join(s.split()))
    if not m:
        return None
    hh, _mm, ampm, _tz, _dow, mon, day, yr = m.groups()
    mon = MONTHS.get(mon.upper()[:3])
    if not mon:
        return None
    hour = int(hh) % 12 + (12 if ampm.upper() == "PM" else 0)
    try:
        return datetime.date(int(yr), mon, int(day)), hour
    except ValueError:
        return None


def resolve(label, issued_date):
    """Map a period label onto (block date, 'day'|'night'), or None if not unambiguous."""
    lab = label.strip().upper()
    if lab in ("TODAY", "THIS AFTERNOON"):
        return issued_date, "day"
    if lab == "TONIGHT":
        return issued_date, "night"
    for i, wd in enumerate(WEEKDAYS):
        delta = (i - issued_date.weekday()) % 7
        if lab == wd:
            return issued_date + datetime.timedelta(days=delta or 7), "day"
        if lab == f"{wd} NIGHT":
            return issued_date + datetime.timedelta(days=delta or 7), "night"
    return None


def load_obs(path):
    obs = collections.defaultdict(dict)
    with open(path, encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            if len(row) < 3:
                continue
            try:
                dt = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M")
            except ValueError:
                continue
            val = None if row[2] in ("M", "", "None") else float(row[2])
            key = (dt.date(), dt.hour)
            if val is None:
                obs[row[0]].setdefault(key, None)
            else:
                prev = obs[row[0]].get(key)
                obs[row[0]][key] = val if prev is None else max(prev, val)
    return obs


def score_block(obs_st, block_date, kind):
    if kind == "day":
        hours = [(block_date, h) for h in range(6, 18)]
    else:
        nxt = block_date + datetime.timedelta(days=1)
        hours = [(block_date, h) for h in range(18, 24)] + [(nxt, h) for h in range(0, 6)]
    present, wet = 0, False
    for key in hours:
        v = obs_st.get(key)
        if v is None:
            continue
        present += 1
        if v >= 0.01:
            wet = True
    if wet:
        return True
    return None if present < 9 else False


def words_alone(text):
    """Likelihood words in a period, counted only where a precipitation noun attaches."""
    found = [w for w in WORDS if ATTACH[w].search(text)]
    if "scattered" in found and "widely scattered" in text.lower():
        found.remove("scattered")
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="zfp-cache")
    a = ap.parse_args()

    rows = list(csv.DictReader(open(f"{a.cache}/periods.csv", encoding="utf-8")))
    days = list(csv.DictReader(open(f"{a.cache}/days.csv", encoding="utf-8")))
    obs_path = f"{a.cache}/obs.csv"
    if not os.path.exists(obs_path):
        print(f"NO OBSERVATIONS at {obs_path} — the vocabulary sections run, the settlement "
              f"cannot. Run tools/zfp_harvest.py without --skip-obs, or wait for it to finish.")
        obs = None
    else:
        obs = load_obs(obs_path)

    failed = [d for d in days if d["error"]]
    print(f"PERIODS REACHED: {len(rows):,}   office-days requested: {len(days):,}   "
          f"office-days the archive did not answer: {len(failed):,} "
          f"({len(failed)/len(days):.1%})")

    print("\nA. WHAT THE RECORD OFFERS")
    print(f"{'office':7} {'periods':>9} {'names precip':>14} {'gives a number':>16} {'word only':>12}")
    for off in sorted({r["office"] for r in rows}):
        sub = [r for r in rows if r["office"] == off]
        prec = [r for r in sub if r["precip_words"]]
        num = [r for r in sub if r["pcts"]]
        wo = [r for r in prec if not r["pcts"]]
        print(f"{off:7} {len(sub):>9,} {len(prec):>9,} {len(prec)/len(sub):>4.0%} "
              f"{len(num):>11,} {len(num)/len(sub):>4.0%} {len(wo):>7,} {len(wo)/len(sub):>4.0%}")

    print("\nB. THE NUMBERS IT STATES")
    vals = collections.Counter(int(v) for r in rows for v in r["pcts"].split("|") if v)
    total = sum(vals.values())
    print(f"   {total:,} numeric claims")
    for v in range(0, 101, 10):
        c = vals.get(v, 0)
        print(f"   {v:>3} % {c:>8,} {c/total:>7.2%}  {'#' * int(60 * c / max(vals.values()))}")
    offgrid = {v: c for v, c in vals.items() if v % 10}
    print(f"   off the ten-point grid: {sum(offgrid.values()):,} {sorted(offgrid.items())[:8]}")

    print("\nC. ONE WORD AND ONE NUMBER IN THE SAME PERIOD, against the published mapping")
    pairs = collections.defaultdict(collections.Counter)
    for r in rows:
        allp = ANY_PCT.findall(r["text"])
        if len(allp) != 1:
            continue
        rest = TRAILING.sub(" ", ATTACHED.sub(" ", r["text"]))
        ws = words_alone(rest)
        if len(ws) == 1:
            pairs[ws[0]][int(allp[0])] += 1
    print(f"   {'word':16} {'n':>8} {'policy':>9} {'inside':>7} {'median':>7}  distribution")
    for w in WORDS:
        c = pairs.get(w)
        if not c or sum(c.values()) < 50:
            continue
        tot = sum(c.values())
        lo, hi = POLICY[w]
        inside = sum(v for k, v in c.items() if lo <= k <= hi)
        flat = sorted(k for k, v in c.items() for _ in range(v))
        dist = ", ".join(f"{k}:{v/tot:.0%}" for k, v in sorted(c.items()) if v / tot >= 0.03)
        print(f"   {w:16} {tot:>8,} {f'{lo}-{hi}':>9} {inside/tot:>6.0%} "
              f"{flat[len(flat)//2]:>7}  {dist}")

    if obs is None:
        print("\nD/E. THE SKY: not settled, no observations in the cache.")
        return 0

    print("\nD. WHAT THE SKY DID")
    book = collections.Counter()
    bynum = collections.defaultdict(lambda: [0, 0])
    byword = collections.defaultdict(lambda: [0, 0])
    silent = [0, 0]
    for r in rows:
        book["periods"] += 1
        iss = parse_issued(r["issued"])
        if not iss:
            book["issuance unreadable"] += 1
            continue
        res = resolve(r["period_label"], iss[0])
        if not res:
            book["label not one of the service's blocks"] += 1
            continue
        block_date, kind = res
        wet = score_block(obs[OFFICE_STATION[r["office"]]], block_date, kind)
        if wet is None:
            book["block not observed"] += 1
            continue
        book["scored"] += 1
        pcts = [int(v) for v in r["pcts"].split("|") if v]
        if len(pcts) == 1:
            b = bynum[pcts[0]]
            b[0] += wet
            b[1] += 1
        elif not pcts:
            ws = words_alone(r["text"])
            if len(ws) == 1:
                b = byword[ws[0]]
                b[0] += wet
                b[1] += 1
            elif not r["precip_words"]:
                silent[0] += wet
                silent[1] += 1
    for k in ["periods", "issuance unreadable", "label not one of the service's blocks",
              "block not observed", "scored"]:
        print(f"   {k:42} {book[k]:>9,}")

    print(f"\n   {'stated':>7} {'claims':>9} {'it rained':>11} {'95 % interval':>18} {'gap':>7}")
    for v in sorted(bynum):
        k, n = bynum[v]
        lo, hi = wilson(k, n)
        print(f"   {v:>6} % {n:>9,} {k/n:>10.1%} {f'{lo:.1%} - {hi:.1%}':>18} {k/n*100-v:>+6.1f}")

    print(f"\n   {'word alone':16} {'claims':>8} {'it rained':>11} {'95 % interval':>18} {'policy':>9}")
    for w, (k, n) in sorted(byword.items(), key=lambda kv: -kv[1][1]):
        if n < 100:
            continue
        lo, hi = wilson(k, n)
        p = POLICY[w]
        print(f"   {w:16} {n:>8,} {k/n:>10.1%} {f'{lo:.1%} - {hi:.1%}':>18} {f'{p[0]}-{p[1]}':>9}")

    k, n = silent
    lo, hi = wilson(k, n)
    print(f"\nE. THE PERIODS THAT NAMED NOTHING: {n:,} scored; it rained anyway "
          f"{k/n:.1%} of the time ({lo:.1%} - {hi:.1%})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
