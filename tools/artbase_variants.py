#!/usr/bin/env python3
"""Recover, for every Atlas entry that cites Rhizome's ArtBase, the addresses
the ArtBase itself records for that work.

The Atlas of Data Art cites `artbase.rhizome.org/wiki/Item:Q<n>` for a large
part of its net-art holdings. That record is a Wikibase item, and it links
variant items, each carrying an access URL (property P46) and a variant type
(P118) — Rhizome distinguishes its own preserved copy from the outside link,
the address the work lived at in the world.

This script reads those two addresses per work, using only the public Wikibase
API, in batches of 40 items per request. Nothing is scraped from rendered HTML.

Usage: python3 tools/artbase_variants.py <werke.json> <out.json>
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://artbase.rhizome.org/w/api.php"
UA = "StudioEnsemble-AddressCheck/1.0 (data-art atlas link survey; contact via frankbueltge.de)"
ITEM = re.compile(r"artbase\.rhizome\.org/wiki/Item:(Q\d+)", re.I)
BATCH = 40


def api(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def entities(ids):
    out = {}
    for i in range(0, len(ids), BATCH):
        chunk = ids[i:i + BATCH]
        d = api({"action": "wbgetentities", "ids": "|".join(chunk)})
        out.update(d.get("entities", {}))
        sys.stderr.write(f"  fetched {len(out)}/{len(ids)}\n")
    return out


def claim_values(entity, pid):
    vals = []
    for c in entity.get("claims", {}).get(pid, []):
        dv = c["mainsnak"].get("datavalue")
        if dv:
            vals.append(dv["value"])
    return vals


def label(entity):
    return (entity.get("labels", {}).get("en") or {}).get("value")


def main():
    src, out_path = sys.argv[1], sys.argv[2]
    works = json.load(open(src))

    wanted = []          # (qid, atlas entry)
    for w in works:
        m = ITEM.search(w.get("source_url") or "")
        if m:
            wanted.append((m.group(1), w))
    qids = sorted({q for q, _ in wanted}, key=lambda s: int(s[1:]))
    sys.stderr.write(f"{len(wanted)} Atlas entries cite the ArtBase; {len(qids)} distinct records\n")

    sys.stderr.write("work items:\n")
    items = entities(qids)

    # P45 links a work to its variant items.
    variant_ids = []
    for qid, e in items.items():
        for v in claim_values(e, "P45"):
            if isinstance(v, dict) and v.get("id"):
                variant_ids.append(v["id"])
    variant_ids = sorted(set(variant_ids), key=lambda s: int(s[1:]))
    sys.stderr.write(f"variant items: {len(variant_ids)}\n")
    variants = entities(variant_ids)

    # P118 names the variant's kind; resolve those labels too.
    kind_ids = sorted({v["id"] for e in variants.values()
                       for v in claim_values(e, "P118") if isinstance(v, dict)},
                      key=lambda s: int(s[1:]))
    kinds = entities(kind_ids) if kind_ids else {}
    kind_label = {k: label(e) for k, e in kinds.items()}
    sys.stderr.write(f"variant kinds: {kind_label}\n")

    rows = []
    for qid, w in wanted:
        e = items.get(qid)
        if not e:
            rows.append({"qid": qid, "title": w["title"], "artist": w["artist"],
                         "year": w["year"], "clusters": w["clusters"],
                         "error": "record not returned by the ArtBase API",
                         "addresses": []})
            continue
        addrs = []
        for v in claim_values(e, "P45"):
            if not (isinstance(v, dict) and v.get("id")):
                continue
            ve = variants.get(v["id"])
            if not ve:
                continue
            urls = [u for u in claim_values(ve, "P46") if isinstance(u, str)]
            kind = None
            for kv in claim_values(ve, "P118"):
                if isinstance(kv, dict):
                    kind = kind_label.get(kv["id"]) or kv["id"]
            for u in urls:
                addrs.append({"variant": v["id"], "kind": kind,
                              "label": label(ve), "url": u})
        rows.append({
            "qid": qid, "title": w["title"], "artist": w["artist"],
            "year": w["year"], "clusters": w["clusters"], "form": w["form"],
            "atlas_url": w["source_url"], "addresses": addrs,
        })

    json.dump(rows, open(out_path, "w"), ensure_ascii=False, indent=1)
    from collections import Counter
    sys.stderr.write("addresses per work: " +
                     str(Counter(len(r["addresses"]) for r in rows)) + "\n")
    sys.stderr.write("by kind: " +
                     str(Counter(a["kind"] for r in rows for a in r["addresses"])) + "\n")


if __name__ == "__main__":
    main()
