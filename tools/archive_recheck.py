#!/usr/bin/env python3
"""Ask the Internet Archive again, and keep asking, before anything is called
not found.

A first pass used one call per address to archive.org's availability endpoint.
That endpoint answers inconsistently: an address that certainly is archived came
back empty once and full a minute later. Any claim that a work is nowhere would
rest on exactly that empty answer, so this pass asks up to four times with a
pause between, and records how many times it asked and what came back each time.

The CDX index (web.archive.org) would be the better instrument and is blocked by
this environment's egress policy — recorded in METHOD.md, not worked around.

Usage: python3 tools/archive_recheck.py <variants-checked.json> <out.json>
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "StudioEnsemble-AddressCheck/1.0 (data-art atlas link survey; contact via frankbueltge.de)"
API = "https://archive.org/wayback/available?url={}"
TRIES = 4


def ask(url):
    q = API.format(urllib.parse.quote(url, safe=""))
    req = urllib.request.Request(q, headers={"User-Agent": UA})
    answers = []
    for i in range(TRIES):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.loads(r.read().decode("utf-8", "replace"))
            snap = (d.get("archived_snapshots") or {}).get("closest")
            if snap and snap.get("available"):
                return {"held": True, "timestamp": snap.get("timestamp"),
                        "wayback_url": snap.get("url"), "asked": i + 1,
                        "answers": answers + ["held"]}
            answers.append("empty")
        except Exception as e:
            answers.append(type(e).__name__)
        time.sleep(1.5 + i)
    return {"held": False, "asked": TRIES, "answers": answers,
            "caveat": "no snapshot reported after %d asks; the availability "
                      "endpoint is known to answer empty for archived pages, "
                      "and the CDX index was not reachable" % TRIES}


def main():
    src, out_path = sys.argv[1], sys.argv[2]
    works = json.load(open(src))

    todo = sorted({a["url"] for w in works for a in w["addresses"]
                   if a["check"]["state"] != "answers"})
    sys.stderr.write(f"re-asking the archive about {len(todo)} addresses\n")

    with ThreadPoolExecutor(4) as ex:
        res = dict(zip(todo, ex.map(ask, todo)))

    for w in works:
        for a in w["addresses"]:
            if a["url"] in res:
                a["check"]["archive"] = res[a["url"]]

    json.dump(works, open(out_path, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    sys.stderr.write(str(Counter(v["held"] for v in res.values())) + "\n")
    sys.stderr.write("asks needed when held: " +
                     str(Counter(v["asked"] for v in res.values() if v["held"])) + "\n")


if __name__ == "__main__":
    main()
