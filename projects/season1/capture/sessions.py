#!/usr/bin/env python3
"""STILL DARK — which session bought which saved copy, read off git and never typed.

Why this exists. Owed item (h), banked in session 74 and unpaid until 77: this work's
record says things like *"three nights bought a copy and no list"* and *"the fifth night
in five that added a copy and no list"*, and **no file in this repository let a stranger
check them.** The capture filenames carry a fetch time; the sessions carry numbers; and
nothing joined the two. A house that publishes counts of its own nights and cannot
produce the join is asking to be believed, which is the one thing this work refuses to
ask of anybody.

The join is not written by hand here — it is derived, the way every other figure on this
work's face is derived. `git log --diff-filter=A` names the commit that FIRST added each
capture file; the session number is read out of that commit's own subject line, which
this house's landing law fixes as `Ensemble session <DATE> (session N): …`. So the map
is a fact about the repository, re-derivable by anyone with a clone, and it goes stale
the moment the record does — it cannot drift, because it is never stored.

    python3 sessions.py            # the map: session → capture(s) → list bought or not
    python3 sessions.py --json     # the same, machine-readable

A capture present in the working tree but not yet committed is printed as `uncommitted`
with no session number. That is the honest state of tonight's copy at the moment it is
taken, and the map says so rather than guessing at the session it is about to belong to.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAPTURES = os.path.normpath(os.path.join(HERE, "..", "captures"))
REPO = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
REL = os.path.relpath(CAPTURES, REPO)

sys.path.insert(0, HERE)
from edition import content_sha256  # noqa: E402

SESSION_RE = re.compile(r"\(session (\d+)\)")


def git(*args):
    out = subprocess.run(["git", "-C", REPO] + list(args),
                         capture_output=True, text=True, check=True)
    return out.stdout


def first_adds():
    """{capture filename: (session or None, commit, date)} from the adding commit."""
    log = git("log", "--diff-filter=A", "--reverse",
              "--format=%x00%h%x1f%ad%x1f%s", "--date=short", "--name-only", "--", REL)
    found = {}
    for block in log.split("\x00")[1:]:
        head, _, files = block.partition("\n")
        h, date, subject = head.split("\x1f", 2)
        m = SESSION_RE.search(subject)
        session = int(m.group(1)) if m else None
        for path in files.strip().splitlines():
            path = path.strip()
            if path:
                found[os.path.basename(path)] = (session, h, date)
    return found


def build():
    adds = first_adds()
    rows = []
    seen_content = {}
    for name in sorted(os.listdir(CAPTURES)):
        if not name.endswith(".json"):
            continue
        with open(os.path.join(CAPTURES, name)) as f:
            cap = json.load(f)
        content = content_sha256(cap)[:8]
        session, commit, date = adds.get(name, (None, None, None))
        # A capture bought a LIST if its edition's material is one no earlier capture
        # held. Nights that bought only a copy are the work's own subject, so the map
        # marks them rather than leaving them to be counted by eye.
        new_list = content not in seen_content
        if new_list:
            seen_content[content] = name
        rows.append({
            "capture": name,
            "session": session,
            "commit": commit,
            "commit_date": date,
            "edition_date_printed": cap["edition_date_printed"],
            "content_sha256": content,
            "vessels": len(cap.get("vessels", [])),
            "bought_a_list": new_list,
            "same_list_as": None if new_list else seen_content[content],
        })
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = build()
    if a.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0

    print(f"{'session':>8}  {'capture':<24} {'list':<12} {'content':<9} ships  bought")
    for r in rows:
        s = str(r["session"]) if r["session"] is not None else "uncommitted"
        bought = "A LIST" if r["bought_a_list"] else f"copy only (= {r['same_list_as'][:17]})"
        print(f"{s:>8}  {r['capture']:<24} {r['edition_date_printed']:<12} "
              f"{r['content_sha256']:<9} {r['vessels']:>4}   {bought}")

    lists = sum(1 for r in rows if r["bought_a_list"])
    sessions = sorted({r["session"] for r in rows if r["session"] is not None})
    print()
    print(f"{len(rows)} capture(s) over {len(sessions)} committed session(s) "
          f"({sessions[0]}–{sessions[-1]}) · {lists} distinct list(s)")
    # Counted per SESSION, not per capture. Until session 79 every session had bought
    # exactly one copy, so the distinction had never mattered and the line simply walked
    # the captures — which printed "79, 79" the first night a session bought two (it
    # straddled 00:00 UTC). A session that bought two copies and no list is one such
    # session, not two, and a line that says otherwise is a count of this house's own
    # nights that is wrong; this record has already banked two of those (failures 16, 17).
    # A session counts here only if NONE of its captures brought a list.
    with_list = {r["session"] for r in rows if r["bought_a_list"]}
    copies_only = []
    for r in rows:
        s = r["session"]
        if s is None or s in with_list or s in copies_only:
            continue
        copies_only.append(s)
    if copies_only:
        run = ", ".join(str(s) for s in copies_only)
        print(f"sessions that bought a copy and no list: {run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
