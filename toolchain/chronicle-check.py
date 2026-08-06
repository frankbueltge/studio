#!/usr/bin/env python3
"""Validate chronicle.json against the published contract, before landing.

    python3 toolchain/chronicle-check.py        # exit 1 and name every offending entry

Why this exists. The site validates this file strictly (Zod) and a malformed entry fails
the whole integration: nothing deploys, the last good state stays live, and a letter lands
in `studio-feedback/` the next day. Twice in two days this house wrote a verdict that reads
perfectly in English and is not in the enum:

  session 67, 2026-08-05  "conditions-discharged"   → red build, letter of 2026-08-05
  session 72, 2026-08-06  ""                        → red build, letter of 2026-08-06

Both times the field was filled with a description of the night instead of one of the seven
words the contract offers. The contract is `SITE-API.md`; the enums below are copied from
it and from the site's own schema (`src/lib/studio/chronicle.ts`), which is public. The
check is deliberately dumb and offline: it reads the file this house commits and says which
line the gate will reject, tonight, rather than tomorrow.

An omitted `verdict` is legal — the site defaults it to null. An empty string is not: the
gate reads it as a claim, and it is not one of the claims available.
"""

import json
import os
import re
import sys

MOVES = ["build", "gauntlet", "verify", "consolidation", "steer", "ship", "other"]
VERDICTS = ["pass", "fail", "conditions", "graduated", "discarded", "deferred"]
SLUG = re.compile(r"^[a-z0-9-]+$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check(entries):
    problems = []
    seen = {}
    for i, e in enumerate(entries):
        where = f"entry {i} (session {e.get('collective_session', '?')}, {e.get('date', '?')})"

        n = e.get("collective_session")
        if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
            problems.append(f"{where}: collective_session must be a positive integer, got {n!r}")
        elif n in seen:
            problems.append(f"{where}: collective_session {n} already used by entry {seen[n]}")
        else:
            seen[n] = i

        if not DATE.match(str(e.get("date", ""))):
            problems.append(f"{where}: date must be YYYY-MM-DD, got {e.get('date')!r}")

        if e.get("move") not in MOVES:
            problems.append(
                f"{where}: move {e.get('move')!r} is not in the enum — one of {MOVES}"
            )

        s = e.get("summary")
        if not isinstance(s, str) or len(s) < 20:
            problems.append(f"{where}: summary must be a string of at least 20 characters")

        w = e.get("works")
        if not isinstance(w, list):
            problems.append(f"{where}: works must be a list (use [] when none)")
        else:
            for slug in w:
                if not isinstance(slug, str) or not SLUG.match(slug):
                    problems.append(f"{where}: work slug {slug!r} is not [a-z0-9-]+")

        if "verdict" in e:
            v = e["verdict"]
            if v is not None and v not in VERDICTS:
                extra = " — an empty string is not 'no verdict'; omit the key or use null" if v == "" else ""
                problems.append(
                    f"{where}: verdict {v!r} is not in the enum — one of {VERDICTS}, "
                    f"or null{extra}"
                )

        for key in e:
            if key not in ("collective_session", "date", "move", "summary", "works", "verdict"):
                problems.append(f"{where}: unknown key {key!r} — the contract has six")

    return problems


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "chronicle.json")
    try:
        entries = json.load(open(path))
    except json.JSONDecodeError as exc:
        print(f"chronicle-check: {path} is not valid JSON — {exc}")
        return 1
    if not isinstance(entries, list):
        print(f"chronicle-check: {path} must be a list of entries")
        return 1

    problems = check(entries)
    if problems:
        print(f"chronicle-check: {len(problems)} problem(s) in {len(entries)} entries — "
              f"the site's gate will reject this file and nothing will deploy.\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"chronicle-check: {len(entries)} entries, all valid against the published contract.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
