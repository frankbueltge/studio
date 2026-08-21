#!/usr/bin/env python3
"""Harvest the public forecast: the words and the numbers, and what the sky did after.

Two public archives, both plain HTTP GET, both from the Iowa Environmental Mesonet:

  ZFP text   https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py
             ?pil=ZFP<OFFICE>&sdate=YYYY-MM-DD&edate=YYYY-MM-DD&fmt=text&limit=9999
  ASOS obs   https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py
             ?station=<ID>&data=p01i&...&tz=<TZ>&format=onlycomma&missing=M&trace=0.0001

The Zone Forecast Product is the plain-language forecast a member of the public reads.
p01i is one-hour precipitation in inches; the service defines measurable precipitation as
>= 0.01 inch, which is the threshold its own probability of precipitation is stated
against.

Three traps, found the hard way and documented so the next reader does not re-find them:

1. The archive's date window is HALF-OPEN. `sdate=X&edate=X` returns the string
   "ERROR: Could not Find", not an empty result — a 200 response carrying a failure. The
   end date must be the day after the start date.
2. Without `limit=9999` the archive returns ONE product for the whole window. A first
   run of this instrument fetched a month at a time and silently kept the last bulletin
   of each month.
3. UGC zone codes are renumbered across the decades. Zones are therefore matched on the
   CITY NAME in the zone header, which is stable, and never on the code.

Usage:  python3 tools/zfp_harvest.py [--cache DIR] [--days 1,11,21] [--from 2006] [--to 2026]
Writes  <cache>/periods.csv  (one row per forecast period)
        <cache>/days.csv     (one row per office-day, including the ones that failed)
        <cache>/obs.csv      (hourly precipitation, local time)
"""
import argparse
import csv
import datetime
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

# office -> (regex matching the city named in the zone header, station, timezone)
TARGETS = {
    "DMX": (r"DES MOINES", "DSM", "America/Chicago"),
    "SEW": (r"SEATTLE", "SEA", "America/Los_Angeles"),
    "PSR": (r"PHOENIX", "PHX", "America/Phoenix"),
    "MFL": (r"MIAMI", "MIA", "America/New_York"),
    "OKX": (r"NEW YORK|MANHATTAN", "NYC", "America/New_York"),
    "BOU": (r"DENVER", "DEN", "America/Denver"),
}

PRODUCT_SEP = "\x01"
UGC = re.compile(r"^([A-Z]{2}Z\d{3}(?:[->][0-9A-Z]+)*)-\d{6}-$")
PERIOD = re.compile(r"^\.([A-Z][A-Za-z0-9 .'/]{1,45}?)\.\.\.")
PCT = re.compile(r"(\d{1,3})\s*percent", re.I)
ISSUED = re.compile(r"^\d{1,4}\s+(AM|PM)\s+[A-Z]{3,4}\s+\w{3}\s+\w{3}\s+\d{1,2}\s+\d{4}$", re.I)

QUALIFIERS = ["slight chance", "likely", "isolated", "widely scattered", "scattered",
              "numerous", "widespread", "occasional", "periods of", "intermittent", "patchy"]
PRECIP_WORDS = ["rain", "showers", "thunderstorm", "snow", "drizzle", "sleet",
                "freezing rain", "flurries", "precipitation", "storms", "sprinkles", "hail"]


def get(url, timeout=240, tries=3):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as r:
                body = r.read().decode("utf-8", "replace")
            if body.startswith("ERROR:"):
                return "__ERROR__" + body.strip()[:60]
            return body
        except Exception as exc:  # noqa: BLE001 - remote archive, retried
            if attempt == tries - 1:
                return f"__ERROR__{type(exc).__name__}:{exc}"
            time.sleep(3 * (attempt + 1))
    return "__ERROR__unreachable"


def fetch_zfp(office, day):
    end = (day + datetime.timedelta(days=1)).isoformat()
    return get("https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py"
               f"?pil=ZFP{office}&sdate={day.isoformat()}&edate={end}&fmt=text&limit=9999")


def fetch_obs(station, tz, year):
    return get("https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
               f"?station={station}&data=p01i&year1={year}&month1=1&day1=1"
               f"&year2={year + 1}&month2=1&day2=1&tz={tz}"
               "&format=onlycomma&missing=M&trace=0.0001&report_type=3&direct=no",
               timeout=300)


def wmo_stamp(text):
    for line in text.split("\n")[:6]:
        parts = line.split()
        if len(parts) == 3 and re.match(r"^FPUS\d\d$", parts[0]):
            return parts[2]
    return ""


def issued_line(text):
    for line in text.split("\n")[:14]:
        s = " ".join(line.split())
        if ISSUED.match(s):
            return s
    return ""


def zone_blocks(text):
    """Split one product into zone blocks, each with its header and its periods."""
    lines = text.split("\n")
    blocks, cur, i = [], None, 0
    while i < len(lines):
        raw = lines[i].rstrip()
        mu = UGC.match(raw.strip())
        if mu:
            if cur:
                blocks.append(cur)
            cur = {"ugc": mu.group(1), "header": [], "periods": []}
            i += 1
            while i < len(lines) and not PERIOD.match(lines[i]) and not UGC.match(lines[i].strip()):
                cur["header"].append(lines[i].strip())
                i += 1
            continue
        mp = PERIOD.match(raw)
        if mp and cur is not None:
            label = mp.group(1).strip().upper()
            body, j = [raw[mp.end():]], i + 1
            while j < len(lines):
                nxt = lines[j]
                if PERIOD.match(nxt) or UGC.match(nxt.strip()) or nxt.strip() == "$$":
                    break
                body.append(nxt)
                j += 1
            cur["periods"].append((label, " ".join(" ".join(body).split())))
            i = j
            continue
        i += 1
    if cur:
        blocks.append(cur)
    return blocks


def describe(text):
    low = text.lower()
    pcts = [int(x) for x in PCT.findall(low)]
    quals = []
    for q in QUALIFIERS:
        if q not in low:
            continue
        if q == "scattered" and "widely scattered" in low:
            continue
        quals.append(q)
    precip = [w for w in PRECIP_WORDS if w in low]
    return pcts, quals, precip


def run_day(job):
    office, day = job
    city_re = TARGETS[office][0]
    raw = fetch_zfp(office, day)
    if raw.startswith("__ERROR__"):
        return [], [office, day.isoformat(), 0, 0, 0, raw[9:]]
    products = [p for p in raw.split(PRODUCT_SEP) if p.strip()]
    rows, matched = [], 0
    for p in products:
        stamp, issued = wmo_stamp(p), issued_line(p)
        for blk in zone_blocks(p):
            if not re.search(city_re, " ".join(blk["header"]).upper()):
                continue
            matched += 1
            for idx, (label, ptext) in enumerate(blk["periods"]):
                pcts, quals, precip = describe(ptext)
                rows.append([office, day.isoformat(), stamp, issued, blk["ugc"], idx, label,
                             "|".join(str(x) for x in pcts), "|".join(quals),
                             "|".join(precip), ptext[:240]])
    return rows, [office, day.isoformat(), len(products), matched, len(rows), ""]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="zfp-cache")
    ap.add_argument("--days", default="1,11,21")
    ap.add_argument("--from", dest="y0", type=int, default=2006)
    ap.add_argument("--to", dest="y1", type=int, default=2026)
    ap.add_argument("--skip-obs", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    days = [int(x) for x in a.days.split(",")]

    jobs = []
    for office in TARGETS:
        for y in range(a.y0, a.y1 + 1):
            for m in range(1, 13):
                for d in days:
                    try:
                        jobs.append((office, datetime.date(y, m, d)))
                    except ValueError:
                        pass

    with open(f"{a.cache}/periods.csv", "w", newline="", encoding="utf-8") as pf, \
         open(f"{a.cache}/days.csv", "w", newline="", encoding="utf-8") as df:
        pw, dw = csv.writer(pf), csv.writer(df)
        pw.writerow(["office", "date", "wmo_ddhhmm", "issued", "ugc", "period_index",
                     "period_label", "pcts", "qualifiers", "precip_words", "text"])
        dw.writerow(["office", "date", "products", "matched_zone_blocks", "periods", "error"])
        done = 0
        with ThreadPoolExecutor(max_workers=4) as ex:
            for rows, tally in ex.map(run_day, jobs):
                pw.writerows(rows)
                dw.writerow(tally)
                done += 1
                if done % 200 == 0:
                    pf.flush()
                    df.flush()
                    print(f"  forecasts: {done}/{len(jobs)} office-days", flush=True)

    if a.skip_obs:
        print("HARVEST COMPLETE (observations skipped)")
        return 0

    with open(f"{a.cache}/obs.csv", "w", encoding="utf-8") as f:
        f.write("station,valid_local,p01i\n")
        for office, (_re, station, tz) in TARGETS.items():
            for y in range(a.y0, a.y1 + 1):
                body = fetch_obs(station, tz, y)
                if body.startswith("__ERROR__"):
                    print(f"  observations FAILED {station} {y}: {body[9:70]}", flush=True)
                    continue
                lines = body.strip().split("\n")[1:]
                for line in lines:
                    if line.strip():
                        f.write(line.strip() + "\n")
            print(f"  observations: {station} done", flush=True)
    print("HARVEST COMPLETE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
