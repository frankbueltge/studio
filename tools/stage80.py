#!/usr/bin/env python3
"""stage80.py — build session 80's panel material from the committed page, by script.

Tonight's arm is not a variant of the page. It is the page's new head — the arrival —
photographed at each of its stops, because that head RUNS and a running thing has no
single still.

    python3 tools/stage80.py

For every stop the arrival holds, this writes `projects/season1/staging-80/step-<n>/`
with a byte-identical copy of the committed `index.html`, and renders it with

    node render.mjs ../staging-80/step-<n> --stop-after=#sd-arrive --at-step=<n>

so that the material ends where the head ends (banked failure 18: a stopping point a
reader is asked to honour is not one — it has to be a property of the material) and the
running element is driven to a NAMED stop rather than photographed wherever its clock
happened to be (`render.mjs --at-step`).

**The weakness, stated here rather than discovered later.** A strip of stills is not the
running element. A reader given five images in order is told that they are consecutive
states of one thing that runs by itself; they are not made to wait for it, and waiting is
part of what the head does. Every number this panel produces is therefore a measurement
of a PROXY for the head, and the session that publishes those numbers publishes this
paragraph beside them.

The stop count is read from the page's own data island, never typed here: a script that
hard-codes how many lists this record holds would be a hand-typed count of the record,
and this house has banked two of those.

Stdlib only.
"""

import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WORK = os.path.join(REPO, "projects", "season1", "still-dark")
SRC = os.path.join(WORK, "index.html")
STAGE = os.path.join(REPO, "projects", "season1", "staging-80")

ISLAND = re.compile(
    r'<script type="application/json" id="sd-data">\n(.*?)\n  </script>', re.S
)


def stop_count(html):
    m = ISLAND.search(html)
    if not m:
        raise SystemExit("no data island in the committed page")
    return len(json.loads(m.group(1))["arrive"]["stops"])


def main():
    with open(SRC, encoding="utf-8") as f:
        html = f.read()
    n = stop_count(html)

    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)

    for i in range(n):
        d = os.path.join(STAGE, f"step-{i}")
        os.makedirs(d)
        shutil.copyfile(SRC, os.path.join(d, "index.html"))
        r = subprocess.run(
            ["node", "render.mjs", f"../staging-80/step-{i}",
             "--stop-after=#sd-arrive", f"--at-step={i}"],
            cwd=WORK, capture_output=True, text=True,
            env=dict(os.environ, NODE_PATH=os.environ.get(
                "NODE_PATH", "/opt/node22/lib/node_modules")),
        )
        sys.stdout.write(r.stdout)
        sys.stderr.write(r.stderr)
        if r.returncode:
            return r.returncode
        print(f"staging-80/step-{i}/  rendered at stop {i} of {n - 1}")

    print("\nEach directory holds the committed page byte for byte; what differs between "
          "them is only which stop the head was driven to before the shutter fell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
