"""FIRST MET — build data.json from the Field's data54.js (check 54), pinned by commit and checksum.

The Field's file is fetched at a fixed commit, checked, and reduced to what the page draws:
per readable report day, new confirmed cases and how many of them were community deaths.
Nothing here is re-measured; the counts are the Field's, re-summed and asserted.
"""
import hashlib, json, urllib.request, pathlib

COMMIT = "5589ea174de1bcae98927ddc5f5649d4015a7b4d"
URL = ("https://raw.githubusercontent.com/frankbueltge/field-research/"
       f"{COMMIT}/artifacts/cycle-012/the-quiet-curve/data54.js")
SHA = "2a5d215777c3a5c1673435b1f3d97334a81980540665b2725d0758a60fc8692c"

raw = urllib.request.urlopen(URL, timeout=60).read()
assert hashlib.sha256(raw).hexdigest() == SHA, "the Field's file changed; re-read before building"
t = raw.decode()
d = json.loads(t[t.index("{"): t.rindex("}") + 1])

s = d["series"]
assert len(s) == 80 == d["summary"]["usable"]
assert sum(x["new"] for x in s) == 5966 == d["summary"]["newConfirmed"]
assert sum(x["comm"] for x in s) == 1921 == d["summary"]["communityDeaths"]
assert all(0 <= x["comm"] <= x["new"] for x in s)
assert s[0]["date"] == "2026-07-13" and s[-1]["date"] == "2026-11-01"
assert max(x["new"] for x in s) == 172 and min(x["new"] for x in s) == 40
assert [x["date"] for x in s].count("2026-10-01") == 2  # two reports carry that date

# calendar days in the window with no readable report
from datetime import date, timedelta
d0, d1 = date(2026, 7, 13), date(2026, 11, 1)
have = {x["date"] for x in s}
gaps = []
k = d0
while k <= d1:
    if k.isoformat() not in have:
        gaps.append(k.isoformat())
    k += timedelta(days=1)
assert len(gaps) == 112 - 79 == 33, len(gaps)  # 112 calendar days, 79 distinct dates

shares = [x["comm"] / x["new"] for x in s]
out = {
    "source": URL,
    "sha256": SHA,
    "days": [{"date": x["date"], "new": x["new"], "comm": x["comm"]} for x in s],
    "gaps": gaps,
    "totals": {"new": 5966, "comm": 1921, "alive": 5966 - 1921},
    "share_range": [round(min(shares), 3), round(max(shares), 3)],
}
pathlib.Path(__file__).with_name("data.json").write_text(json.dumps(out, separators=(",", ":")))
print("ok", out["totals"], "gaps", len(gaps), "share range", out["share_range"])
