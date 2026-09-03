#!/usr/bin/env python3
"""Join the two knocks into one portrait: where each ArtBase-cited work of the
Atlas can still be found, and by whom it is kept.

Inputs
  survey.jsonl          stage one — the address the Atlas itself cites (503)
  variants-checked.json stage two — the addresses the ArtBase record names

Output
  data.json             everything the work's page draws, and nothing else

Per-work states, in the order they are tested:
  own          an outside link still answers with the work at it
  moved        the outside link redirects to another host that keeps the path —
               the work went with its maker
  keeping      no live outside link, but Rhizome (or an archive variant) serves it
  archive      nothing live, but the Internet Archive holds one of its addresses
  lost         nothing answered and no archive copy was reported

Usage: python3 tools/two_addresses.py <survey.jsonl> <variants-checked.json> <out.json>
"""

import json
import re
import sys
from collections import Counter
from urllib.parse import urlsplit

# Hand-adjudicated: pages that returned 200 while the automatic placeholder
# signal fired. Each was fetched and read by hand on 2026-09-03. The quote is
# the evidence; `gone` says how it was ruled.
ADJUDICATED = {
    "http://www.findelmundo.com.ar/ip-poetry/index-en.html": {
        "gone": True,
        "quote": "HTTP 404 - File not found",
        "note": "the host serves its own not-found page under a 200 status",
    },
    "http://www.erinohara.net/dessertrhizome.html": {
        "gone": True,
        "quote": "Welcome erinohara.net - BlueHost.com",
        "note": "the hosting company's placeholder stands where the work was",
    },
    "http://www.babel.ca/patinage": {
        "gone": True,
        "quote": "Coming soon",
        "note": "the domain lives and the work is not on it",
    },
    "http://www.pipedreams.net.nz/jacquard/": {
        "gone": False,
        "quote": "Luke Duncalfe - (Jacquard Loom Panels 1, 2, 4, 5 & 7, 2002)",
        "note": "false positive of the automatic signal — the work is at its address",
    },
}

SALE = re.compile(r"hugedomains|afternic|sedo|dan\.com|domain(name)?s?[-.]?(for)?sale|godaddy", re.I)


def segs(u):
    p = urlsplit(u).path.strip("/")
    return [s for s in p.split("/") if s and s not in {"index.html", "index.htm", "index.php"}]


def kept_path(src, dst):
    """Did the redirect keep something that names the work?"""
    a, b = segs(src), segs(dst)
    if not a or not b:
        return False
    tail = a[-1].lower()
    tail = re.sub(r"\.(html?|php|shtml|asp)$", "", tail)
    if not tail:
        return False
    return any(tail == re.sub(r"\.(html?|php|shtml|asp)$", "", s.lower()) for s in b)


def outside_state(addr):
    """Refine an outside link's automatic state with what was read by hand."""
    c = addr["check"]
    st, url = c["state"], c["url"]
    adj = ADJUDICATED.get(url)
    if st == "answers":
        if adj and adj["gone"]:
            return "placeholder", adj
        return "answers", adj
    if st == "redirected":
        final = c.get("final_url") or ""
        if SALE.search(final):
            return "for-sale", None
        return ("moved" if kept_path(url, final) else "swallowed"), None
    return st, None


def main():
    survey_path, variants_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

    survey = [json.loads(l) for l in open(survey_path)]
    works = json.load(open(variants_path))

    frame = Counter(r["state"] for r in survey)

    rows = []
    for w in works:
        outside, keepers = [], []
        for a in w["addresses"]:
            if a["kind_norm"] == "outside":
                st, adj = outside_state(a)
                outside.append({"url": a["url"], "state": st,
                                "final_url": a["check"].get("final_url"),
                                "http": a["check"].get("http"),
                                "archive": a["check"].get("archive"),
                                "adjudication": adj})
            else:
                keepers.append({"url": a["url"], "kind": a["kind_norm"],
                                "state": a["check"]["state"],
                                "http": a["check"].get("http"),
                                "archive": a["check"].get("archive")})

        held = any(k["state"] == "answers" for k in keepers)
        archived = any((o.get("archive") or {}).get("held") for o in outside) or \
                   any((k.get("archive") or {}).get("held") for k in keepers)

        if any(o["state"] == "answers" for o in outside):
            state = "own"
        elif any(o["state"] == "moved" for o in outside):
            state = "moved"
        elif held:
            state = "keeping"
        elif archived:
            state = "archive"
        else:
            state = "lost"

        year = w["year"]
        m = re.search(r"(19|20)\d{2}", str(year))
        rows.append({
            "qid": w["qid"], "title": w["title"], "artist": w["artist"],
            "year": year, "year_num": int(m.group(0)) if m else None,
            "clusters": w["clusters"], "form": w.get("form"),
            "atlas_url": w["atlas_url"],
            "state": state, "outside": outside, "keepers": keepers,
            "has_outside": bool(outside), "has_keeper": bool(keepers),
        })

    out = {
        "generated": "2026-09-03",
        "source": {
            "atlas": "https://raw.githubusercontent.com/frankbueltge/frankbueltge.de/main/src/data/atlas/werke.json",
            "artbase": "https://artbase.rhizome.org/w/api.php (Wikibase, public)",
            "archive": "https://archive.org/wayback/available",
            "note": "see METHOD.md for the exact feeds and the run log",
        },
        "frame": {
            "atlas_entries": 521,
            "distinct_addresses": len(survey),
            "states": dict(frame),
        },
        "works": rows,
        "totals": {
            "works": len(rows),
            "states": dict(Counter(r["state"] for r in rows)),
            "outside_states": dict(Counter(o["state"] for r in rows for o in r["outside"])),
            "keeper_states": dict(Counter(k["state"] for r in rows for k in r["keepers"])),
            "with_keeper": sum(1 for r in rows if r["has_keeper"]),
            "without_keeper": sum(1 for r in rows if not r["has_keeper"]),
        },
    }
    json.dump(out, open(out_path, "w"), ensure_ascii=False, indent=1)

    print("frame (addresses the Atlas cites):", dict(frame))
    print("works:", len(rows))
    print("states:", out["totals"]["states"])
    print("outside link states:", out["totals"]["outside_states"])
    print("keeper states:", out["totals"]["keeper_states"])
    print("works with a keeper:", out["totals"]["with_keeper"],
          "without:", out["totals"]["without_keeper"])
    by_decade = Counter()
    for r in rows:
        if r["year_num"]:
            by_decade[(r["year_num"] // 5 * 5, r["state"])] += 1
    for k in sorted(by_decade):
        print("  ", k, by_decade[k])


if __name__ == "__main__":
    main()
