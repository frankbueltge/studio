#!/usr/bin/env python3
"""Second stage: knock at the addresses recovered from the ArtBase records.

Stage one knocked at the address the Atlas cites — for these works, a catalogue
record. This stage knocks at the addresses that record names for the work
itself: the artist's own ("outside link"), Rhizome's preserved copy ("ArtBase
variant"), and a handful of archive or emulation variants.

Usage: python3 tools/address_check_variants.py <variants.json> <out.json>
"""

import json
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from address_check import knock, wayback  # noqa: E402


def kind_of(address):
    """Normalise the variant label into three keepers of an address."""
    lab = (address.get("label") or "").lower()
    url = (address.get("url") or "").lower()
    if "artbase variant" in lab or "artbase.rhizome.org" in url or "archive.rhizome.org" in url:
        return "rhizome"
    if "web archive" in lab or "archived" in lab or "web.archive.org" in url:
        return "web-archive"
    if "outside link" in lab:
        return "outside"
    return "other"


def main():
    src, out_path = sys.argv[1], sys.argv[2]
    works = json.load(open(src))

    urls = {}
    for w in works:
        for a in w["addresses"]:
            a["kind_norm"] = kind_of(a)
            urls.setdefault(a["url"], None)
    order = list(urls)
    sys.stderr.write(f"{len(works)} works, {len(order)} distinct addresses\n")

    with ThreadPoolExecutor(8) as ex:
        for u, r in zip(order, ex.map(knock, order)):
            urls[u] = r

    need = [r for r in urls.values() if r["state"] != "answers"]
    sys.stderr.write(f"{len(need)} did not answer; asking the archive\n")
    with ThreadPoolExecutor(4) as ex:
        for r, wb in zip(need, ex.map(wayback, [r["url"] for r in need])):
            r["archive"] = wb

    for w in works:
        for a in w["addresses"]:
            a["check"] = urls[a["url"]]

    json.dump(works, open(out_path, "w"), ensure_ascii=False, indent=1)

    from collections import Counter
    c = Counter((a["kind_norm"], a["check"]["state"])
                for w in works for a in w["addresses"])
    for k in sorted(c):
        sys.stderr.write(f"  {k[0]:12} {k[1]:14} {c[k]}\n")


if __name__ == "__main__":
    main()
