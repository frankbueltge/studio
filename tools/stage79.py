#!/usr/bin/env python3
"""stage79.py — build session 79's two arms from the committed page, by script.

Session 78's arms were built by a flag in `data.py` because they differed in one
string. Tonight's do not: one arm differs in where its material ENDS, the other in
where a block of markup STANDS and in one hoisted line. A hand-cut copy of a 50 kB
page is exactly the kind of object this house has already been caught passing —
session 67 passed an object nobody had rendered — so the arms are generated from
`still-dark/index.html` here, deterministically, and a stranger can regenerate them
and diff.

    python3 tools/stage79.py

Writes:
  projects/season1/staging-79/stop/index.html   byte-identical to the committed page.
      The arm is not the FILE; it is what `render.mjs --stop-after=#sd-lede` renders
      from it — a page whose material ends at the lede, so nothing has to be asked of
      the reader (banked failure 18).
  projects/season1/staging-79/cut/index.html    the committed page with the OBSERVED
      ledger and its caption moved ABOVE the terminal block, so the last thing before
      the ending is the work's own verbatim output and not fourteen rows of truncated
      sha256 (DRAMATURG-77 §4, corroborated by three of four severed readers in
      PANEL-78.md Q3). Its data island is then written by `data.py --cuts`, which
      hoists the repeated OBSERVED line out of the rows.

What this script may NOT do, and does not: delete the ledger. Three readers named it
as machine exhaust and the exhaust is real, but the table is the only OBSERVED
evidence standing on this face, and trading a work's evidence chain for tidiness on a
taste report is not a cut this house makes on judgement. If the move does not stop
readers naming it, deletion goes to a later reading as its own question, with its own
refuting number.

Stdlib only.
"""

import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
WORK = os.path.join(REPO, "projects", "season1", "still-dark")
STAGE = os.path.join(REPO, "projects", "season1", "staging-79")
SRC = os.path.join(WORK, "index.html")

# The two halves of the evidence section, matched on their own markup so a change to
# either one breaks this script loudly instead of producing a silently wrong arm.
TERMINAL = re.compile(
    r'(\n  <section class="sd-evidence">\n)'
    r'(.*?<p class="sd-raw-cap">verbatim, unedited</p>\n    </div>\n)'
    r'(.*?)'
    r'(    <p class="sd-ledger-cap" id="sd-ledger-cap"></p>\n'
    r'    <div class="sd-ledger" id="sd-ledger"></div>\n)',
    re.S,
)


def reorder(html):
    m = TERMINAL.search(html)
    if not m:
        print("the evidence section does not have the shape this script expects; "
              "the arm was NOT written", file=sys.stderr)
        raise SystemExit(2)
    open_tag, terminal, comment, ledger = m.groups()
    swapped = open_tag + ledger + comment + terminal
    return html[:m.start()] + swapped + html[m.end():]


def main():
    for arm in ("stop", "cut"):
        os.makedirs(os.path.join(STAGE, arm), exist_ok=True)

    shutil.copyfile(SRC, os.path.join(STAGE, "stop", "index.html"))

    with open(SRC, encoding="utf-8") as f:
        html = f.read()
    cut_path = os.path.join(STAGE, "cut", "index.html")
    with open(cut_path, "w", encoding="utf-8") as f:
        f.write(reorder(html))

    r = subprocess.run(
        [sys.executable, os.path.join(WORK, "data.py"), "--cuts", "--write",
         "--into", cut_path],
        capture_output=True, text=True,
    )
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    if r.returncode:
        return r.returncode

    print("staging-79/stop/index.html   (identical to the committed page)")
    print("staging-79/cut/index.html    (ledger lifted above the terminal block, "
          "island built with --cuts)")
    print("\nnow, from projects/season1/still-dark/:")
    print("  node render.mjs ../staging-79/stop --stop-after=#sd-lede")
    print("  node render.mjs ../staging-79/cut")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
