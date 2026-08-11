#!/usr/bin/env python3
"""chronicle.py — does this house's self-report satisfy the contract this house wrote?

Why this exists, and it is not a hypothetical. On 2026-08-10 session 84 appended an entry
whose `move` was `"critique"` — the word PROTOCOL.md uses for exactly that session's move
("critique (Kritiker/Verifier pass on a WIP)"). The site's enum, fixed in SITE-API.md and
enforced there by a strict schema, does not carry it: SITE-API.md says in as many words
that the site's move enum is fixed and that studio moves are MAPPED onto it. The gate went
red, no deploy happened for two nights, and the public chronicle stood at 83 entries while
this house's own file held 84. The build letters that came back
(`studio-feedback/2026-08-10.md`, `2026-08-11.md`) name the failing test and quote the
first two lines of the error, which is all the site can honestly say — whose defect it is
"cannot be derived from the log".

So: a file this house writes every session, validated against a contract this house has
committed, by a command a stranger can run.

    python3 tools/chronicle.py          # exit 0 if the file satisfies the contract
    python3 tools/chronicle.py --json   # the same, machine-readable

WHAT IT CAN AND CANNOT SAY. It can say that every entry carries the required keys, that
`move` is one of the seven words the site accepts, that `verdict` is one of the accepted
words or null, that dates parse and that session numbers do not go backwards. It CANNOT
say that the site's own schema is still the one written down here: that file lives in
another repository and this instrument does not read it. If the gate ever goes red on a
chronicle this instrument passes, the contract in SITE-API.md is the thing to re-read
first, and this file is what gets corrected.
"""

import argparse
import datetime
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
CHRONICLE = os.path.join(ROOT, "chronicle.json")

# SITE-API.md, "The chronicle self-report". Both lists are copied from the contract, and
# the contract is the authority — not this file, and not the house's own vocabulary.
MOVES = ("build", "gauntlet", "verify", "consolidation", "steer", "ship", "other")
VERDICTS = ("pass", "fail", "conditions", "graduated", "discarded", "deferred", None)
REQUIRED = ("collective_session", "date", "move", "summary", "works")


def check(entries):
    problems = []
    if not isinstance(entries, list):
        return ["chronicle.json is not a JSON array"]
    last = None
    for i, e in enumerate(entries):
        where = f"entry {i}"
        if not isinstance(e, dict):
            problems.append(f"{where}: not an object")
            continue
        n = e.get("collective_session")
        where = f"session {n}" if n is not None else where
        for k in REQUIRED:
            if k not in e:
                problems.append(f"{where}: missing key {k!r}")
        if e.get("move") not in MOVES:
            problems.append(
                f"{where}: move {e.get('move')!r} is not one of {', '.join(MOVES)} "
                "— SITE-API.md, the site's enum is fixed and studio moves map onto it"
            )
        # `verdict` is absent from two 2026-07-31 entries that the site has published, so a
        # missing key is not treated as a violation here; a PRESENT key with a word outside
        # the list is. This is a fact about the deployed record, checked against the live
        # file, not a guess about the schema.
        if "verdict" in e and e["verdict"] not in VERDICTS:
            problems.append(f"{where}: verdict {e['verdict']!r} is outside the contract")
        if not isinstance(e.get("works"), list):
            problems.append(f"{where}: works must be a list of slugs")
        try:
            datetime.date.fromisoformat(e.get("date", ""))
        except (TypeError, ValueError):
            problems.append(f"{where}: date {e.get('date')!r} is not YYYY-MM-DD")
        if isinstance(n, int) and isinstance(last, int) and n < last:
            problems.append(f"{where}: session number goes backwards after {last}")
        if isinstance(n, int):
            last = n
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--file", default=CHRONICLE)
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as fh:
        entries = json.load(fh)
    problems = check(entries)

    if args.json:
        print(json.dumps({"entries": len(entries), "problems": problems}, indent=2))
    elif problems:
        print(f"CHRONICLE: {len(problems)} problem(s) in {len(entries)} entries")
        for p in problems:
            print("  " + p)
    else:
        print(f"CHRONICLE: {len(entries)} entries, all inside the contract in SITE-API.md")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
