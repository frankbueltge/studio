#!/usr/bin/env python3
"""stage82.py — build session 82's two arms from two committed pages, by script.

Tonight is a CONTROLLED comparison, and the reason is that tonight's change touches words
that had just passed. Session 81 measured this head's first encounter at 2 of 2 after two
nights at 0 of 2; session 82 then rewrote the premise those readers had read (owed item (o):
the head named its source and never said what kind of thing it is), cut the paragraph under
it (owed item (m)), and headed the empty block above the buttons (owed item (p)). A single
arm cannot tell a change that helped from reader variance, and this house has published that
lesson twice — session 77 ran a control and it refuted a change the house believed in.

    python3 tools/stage82.py

Two arms, six stops each:

    staging-82/A/step-<n>/   tonight's page, working tree
    staging-82/B/step-<n>/   the page as committed at HEAD — the control

Arm B is written out with `git show HEAD:<path>` and never by hand. Both arms are rendered
by the SAME `render.mjs` the work uses, with `--stop-after=#sd-arrive --at-step=<n>`, so the
material ends where the head ends (banked failure 18) and the running element is driven to a
NAMED stop rather than photographed wherever its clock happened to be.

**Two weaknesses, stated here rather than discovered later.**

1. A strip of stills is not the running element. Nobody in this panel is made to WAIT, and
   tonight's first change is a first beat 11 seconds long. **The beat has no still.** No
   number this panel returns is evidence about it; it is judged on the running object by the
   staging voice, and measured by this house in the browser.
2. **Banked failure 22, and its own instruction.** Because the material is one still per
   stop, every element that does NOT change is reproduced six times over, and session 81's
   two severed readers both asked for a paragraph to be cut as sixfold repetition when it
   stands once on the page. The failure's instruction was: the next panel of this kind
   either says so in the reader's instructions or stops asking that question of stills.
   Tonight it says so — see the dispatch note in `STAGING-82.md`.

The stop count is read from each page's own data island, never typed here.

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
REL = "projects/season1/still-dark/index.html"
STAGE = os.path.join(REPO, "projects", "season1", "staging-82")

ISLAND = re.compile(
    r'<script type="application/json" id="sd-data">\n(.*?)\n  </script>', re.S
)


def stop_count(html):
    m = ISLAND.search(html)
    if not m:
        raise SystemExit("no data island in the page")
    return len(json.loads(m.group(1))["arrive"]["stops"])


def committed_page():
    r = subprocess.run(["git", "show", f"HEAD:{REL}"], cwd=REPO,
                       capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr.strip() or "git show failed")
    return r.stdout


def render(arm, i, out_rel):
    r = subprocess.run(
        ["node", "render.mjs", out_rel, "--stop-after=#sd-arrive", f"--at-step={i}"],
        cwd=WORK, capture_output=True, text=True,
        env=dict(os.environ, NODE_PATH=os.environ.get(
            "NODE_PATH", "/opt/node22/lib/node_modules")),
    )
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    return r.returncode


def main():
    with open(SRC, encoding="utf-8") as f:
        tonight = f.read()
    control = committed_page()

    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)

    for arm, html in (("A", tonight), ("B", control)):
        n = stop_count(html)
        for i in range(n):
            d = os.path.join(STAGE, arm, f"step-{i}")
            os.makedirs(d)
            with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            rc = render(arm, i, f"../staging-82/{arm}/step-{i}")
            if rc:
                return rc
            print(f"staging-82/{arm}/step-{i}/  rendered at stop {i} of {n - 1}")

    print("\nArm A is the working tree; arm B is HEAD, written by `git show`. Within each "
          "arm every directory holds that page byte for byte, and what differs between the "
          "six is only which stop the head was driven to before the shutter fell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
