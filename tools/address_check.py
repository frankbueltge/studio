#!/usr/bin/env python3
"""Knock once at every source address in the house's Atlas of Data Art, and
record what answers.

Input : a local copy of the Atlas feed (src/data/atlas/werke.json on the site).
Output: one JSON row per distinct URL — final status, final URL, redirect
        history length, bytes read, a soft-404 signal, and (for every address
        that did not answer) whether the Internet Archive holds a snapshot.

The instrument identifies itself honestly in its User-Agent. It knocks once per
address, follows redirects, reads at most 8 KB of body, and never retries a
refusal: a door that says no is a finding, not an obstacle.

States
  answers        2xx, still at an address that names the work
  redirected     2xx, but the final URL is a different registrable domain, or
                 collapsed to a site root while a deep path was asked for
  blocked        401 / 403 / 429 / 451 — the host refuses this instrument
  gone           404 / 410 and other 4xx
  server-error   5xx
  unreachable    DNS failure, connection refused, TLS failure, timeout

Usage: python3 tools/address_check.py <werke.json> <out.jsonl> [--limit N]
"""

import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "StudioEnsemble-AddressCheck/1.0 (data-art atlas link survey; contact via frankbueltge.de)"
TIMEOUT = 25
BODY_BYTES = 8192
WORKERS = 8

# Substrings that, in the first 8 KB of a 2xx response, suggest the page is a
# placeholder rather than the work. Recorded as a signal, never as a verdict.
SOFT_404 = [
    "404 not found", "page not found", "not found", "no longer available",
    "domain is for sale", "buy this domain", "this domain may be for sale",
    "parked", "under construction", "account suspended", "site not found",
    "coming soon", "error 404",
]

PLAYER_DEAD = re.compile(r"\.(swf|dcr|dir|dxr|ra|rm|jnlp|class)(\?|$)", re.I)


def registrable(host):
    """Crude eTLD+1. Good enough to tell aiwar.cloud from yahoo.com."""
    host = (host or "").lower().lstrip("www.")
    parts = [p for p in host.split(".") if p]
    if len(parts) <= 2:
        return ".".join(parts)
    # two-label public suffixes we actually meet in this corpus
    if parts[-2] in {"co", "com", "org", "net", "ac", "gov"} and len(parts[-1]) == 2:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


class Redirects(urllib.request.HTTPRedirectHandler):
    def __init__(self):
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append((code, newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def knock(url):
    row = {
        "url": url, "state": None, "http": None, "final_url": None,
        "redirects": 0, "bytes": None, "soft_404": False, "note": None,
        "unplayable_format": bool(PLAYER_DEAD.search(url)),
        "elapsed_ms": None,
    }
    handler = Redirects()
    # No custom SSL context: the default one already carries this environment's
    # trust store, and an earlier pilot that passed its own context reported
    # every one of 24 live addresses as unreachable. Recorded in METHOD.md.
    opener = urllib.request.build_opener(handler)
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "en,de;q=0.8",
    })
    t0 = time.time()
    try:
        with opener.open(req, timeout=TIMEOUT) as resp:
            body = resp.read(BODY_BYTES)
            row["http"] = resp.status
            row["final_url"] = resp.geturl()
            row["bytes"] = len(body)
            text = body.decode("utf-8", "replace").lower()
            row["soft_404"] = any(s in text for s in SOFT_404)
    except urllib.error.HTTPError as e:
        row["http"] = e.code
        row["final_url"] = e.geturl()
        try:
            row["bytes"] = len(e.read(BODY_BYTES))
        except Exception:
            row["bytes"] = 0
    except urllib.error.URLError as e:
        row["note"] = str(e.reason)[:200]
    except Exception as e:  # socket resets, bad chunking, decoding of headers
        row["note"] = f"{type(e).__name__}: {e}"[:200]
    row["elapsed_ms"] = int((time.time() - t0) * 1000)
    row["redirects"] = len(handler.chain)

    code = row["http"]
    if code is None:
        row["state"] = "unreachable"
    elif 200 <= code < 300:
        asked = urllib.parse.urlsplit(url)
        got = urllib.parse.urlsplit(row["final_url"] or url)
        moved_host = registrable(asked.netloc) != registrable(got.netloc)
        deep = len(asked.path.strip("/")) > 0
        collapsed = deep and got.path.strip("/") == "" and not got.query
        row["state"] = "redirected" if (moved_host or collapsed) else "answers"
        if moved_host:
            row["note"] = "final host differs from the address on record"
        elif collapsed:
            row["note"] = "deep path collapsed to the site root"
    elif code in (401, 403, 429, 451):
        row["state"] = "blocked"
    elif 400 <= code < 500:
        row["state"] = "gone"
    elif code >= 500:
        row["state"] = "server-error"
    else:
        row["state"] = "unreachable"
    return row


WB = "https://archive.org/wayback/available?url={}"


def wayback(url):
    """Ask the Internet Archive whether it holds this address at all."""
    q = WB.format(urllib.parse.quote(url, safe=""))
    req = urllib.request.Request(q, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            d = json.loads(r.read().decode("utf-8", "replace"))
    except Exception as e:
        return {"held": None, "note": f"{type(e).__name__}"[:80]}
    snap = (d.get("archived_snapshots") or {}).get("closest")
    if not snap or not snap.get("available"):
        return {"held": False}
    return {"held": True, "timestamp": snap.get("timestamp"), "wayback_url": snap.get("url")}


def main():
    src, out = sys.argv[1], sys.argv[2]
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])

    works = json.load(open(src))
    urls = []
    seen = set()
    for w in works:
        u = (w.get("source_url") or "").strip()
        if u and u not in seen:
            seen.add(u)
            urls.append(u)
    if limit:
        urls = urls[:limit]
    sys.stderr.write(f"{len(works)} entries, {len(urls)} distinct addresses\n")

    with ThreadPoolExecutor(WORKERS) as ex:
        rows = list(ex.map(knock, urls))

    need = [r for r in rows if r["state"] != "answers"]
    sys.stderr.write(f"{len(need)} addresses did not answer; asking the archive\n")
    with ThreadPoolExecutor(4) as ex:
        for r, wb in zip(need, ex.map(wayback, [r["url"] for r in need])):
            r["archive"] = wb

    with open(out, "w") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    from collections import Counter
    sys.stderr.write(str(Counter(r["state"] for r in rows)) + "\n")


if __name__ == "__main__":
    main()
