#!/usr/bin/env python3
"""renders.py — do the committed renders belong to the committed page?

Banked failure (i), STILL DARK: the renders are the only sighted material a severed
panel ever receives, and until tonight nothing in this house checked that they had been
made from the page committed beside them. Session 74 found, in one night of sighted
reading, a misalignment that eight text-only panels had passed — which is exactly how
much weight those images carry. Session 75 moved the face and remade them by hand; a
forgotten hand would have shown the next panel a superseded figure, and no instrument
here could have said so.

render.mjs writes RENDERS.json at render time: the sha256 of the index.html it rendered,
and the sha256 of each file it wrote. This script recomputes all of them from the files
on disk and reports.

    python3 tools/renders.py                 # the project's work directory (default)
    python3 tools/renders.py <dir> [<dir>…]  # any directory holding a RENDERS.json

Exit codes:  0 every hash matches · 1 something is stale · 2 no RENDERS.json at all.

A stale render is not an error to be silenced. It means the images a panel would be shown
are not the page — remake them with `node render.mjs` and commit both.
"""

import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
DEFAULT = os.path.join(REPO, "projects", "season1", "still-dark")
MANIFEST = "RENDERS.json"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def check(directory):
    """Return (ok, lines). ok is False if anything is stale or missing."""
    lines = []
    path = os.path.join(directory, MANIFEST)
    rel = os.path.relpath(directory, REPO)
    if not os.path.exists(path):
        return None, [f"{rel}: no {MANIFEST} — nothing claims these renders belong to anything"]

    with open(path, encoding="utf-8") as f:
        m = json.load(f)

    ok = True
    src = os.path.join(directory, m["rendered_from"])
    if not os.path.exists(src):
        return False, [f"{rel}: {m['rendered_from']} is missing"]

    actual = sha256(src)
    if actual == m["index_sha256"]:
        lines.append(f"  {m['rendered_from']:<18} {actual[:12]}…  the page the renders were made from")
    else:
        ok = False
        lines.append(
            f"  {m['rendered_from']:<18} {actual[:12]}…  STALE — rendered from "
            f"{m['index_sha256'][:12]}…, the page has moved since"
        )

    for name, expected in m["outputs"].items():
        f_path = os.path.join(directory, name)
        if not os.path.exists(f_path):
            ok = False
            lines.append(f"  {name:<18} MISSING")
            continue
        got = sha256(f_path)
        if got == expected:
            lines.append(f"  {name:<18} {got[:12]}…  as written")
        else:
            ok = False
            lines.append(f"  {name:<18} {got[:12]}…  CHANGED since it was rendered")

    return ok, lines


def main():
    dirs = sys.argv[1:] or [DEFAULT]
    worst = 0
    for directory in dirs:
        rel = os.path.relpath(os.path.abspath(directory), REPO)
        ok, lines = check(os.path.abspath(directory))
        if ok is None:
            print("\n".join(lines))
            worst = max(worst, 2)
            continue
        print(f"{rel}")
        print("\n".join(lines))
        print("  RENDERS MATCH THE PAGE" if ok else "  RENDERS ARE STALE — run `node render.mjs`")
        if not ok:
            worst = max(worst, 1)
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
