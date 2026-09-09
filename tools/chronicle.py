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

And a third time on 2026-09-09, in a shape this instrument could not see. Session 132
wrote `journal/2026-09-09-session-132.md` and never appended its entry, so the file was
131 entries against 132 sessions in the journal. Every entry present was inside the
contract, so this instrument said so and exited 0. The site's gate counts the two against
each other (`src/lib/studio/chronicle.test.ts`, "every served anchor resolves against the
real synced journals") and refused the night: `expected 131 to be 132`. Studio integrate
was red three times that day and session 132 did not reach the site. A malformed entry and
a missing one darken the site alike, so the completeness check below is part of the
contract this instrument enforces, not a separate courtesy.

So: a file this house writes every session, validated against a contract this house has
committed, by a command a stranger can run.

    python3 tools/chronicle.py          # exit 0 if the file satisfies the contract
    python3 tools/chronicle.py --json   # the same, machine-readable

WHAT IT CAN AND CANNOT SAY. It can say that every entry carries the required keys, that
`move` is one of the seven words the site accepts, that `verdict` is one of the accepted
words or null, that dates parse and that session numbers do not go backwards. It can say
that the number of entries matches the number of sessions the journal holds, and name the
days where the two disagree. It CANNOT say that the site's own schema is still the one
written down here: that file lives in another repository and this instrument does not read
it. It also cannot say whether a missing entry is the night's or an older one — it reports
the day, and the house reads the journal. If the gate ever goes red on a chronicle this
instrument passes, the contract in SITE-API.md is the thing to re-read first, and this
file is what gets corrected.
"""

import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
CHRONICLE = os.path.join(ROOT, "chronicle.json")
JOURNAL = os.path.join(ROOT, "journal")

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


DAY = re.compile(r"^(\d{4}-\d{2}-\d{2})")
FENCE = re.compile(r"^(```|~~~)")
H1 = re.compile(r"^# ")


def count_sessions(body):
    """Sessions in one journal day, counted the way the site splits them.

    Mirrors `splitSessions` in the site's src/lib/engines/journal.ts: a session starts at
    every top-level H1, a `# ` line inside a code fence is not a heading (these journals
    quote shell and yaml), text before the first H1 is its own chunk, and a file with no
    H1 at all is one session. The site derives one anchor per session and requires one
    chronicle entry per anchor, so this count is the number the site will expect.
    """
    chunks, current, in_fence = [], [], False
    for line in body.split("\n"):
        if FENCE.match(line):
            in_fence = not in_fence
        elif not in_fence and H1.match(line) and any(l.strip() for l in current):
            chunks.append(current)
            current = []
        current.append(line)
    if current:
        chunks.append(current)
    return len([c for c in ("\n".join(c) for c in chunks) if c.strip()]) or 1


def journal_sessions(journal_dir):
    """{day: session count} for every `YYYY-MM-DD*.md` in the journal directory."""
    days = {}
    for name in sorted(os.listdir(journal_dir)):
        if not name.endswith(".md"):
            continue
        m = DAY.match(name)
        if not m:
            continue
        with open(os.path.join(journal_dir, name), encoding="utf-8") as fh:
            days[m.group(1)] = days.get(m.group(1), 0) + count_sessions(fh.read())
    return days


def check_completeness(entries, journal_dir):
    """Does the self-report cover every session the journal holds, day by day?

    Checked per day rather than only in total, because two errors that cancel in the total
    (a missing entry on one night, a duplicate on another) leave the site's anchor set and
    the chronicle the same length and still mismatched. Across the 131 entries and 122
    journal days standing on 2026-09-09, the day is the key the two agree on everywhere.
    """
    problems = []
    if not os.path.isdir(journal_dir):
        return problems
    in_journal = journal_sessions(journal_dir)
    in_chronicle = {}
    for e in entries:
        if isinstance(e, dict) and isinstance(e.get("date"), str):
            in_chronicle[e["date"]] = in_chronicle.get(e["date"], 0) + 1
    for day in sorted(set(in_journal) | set(in_chronicle)):
        j, c = in_journal.get(day, 0), in_chronicle.get(day, 0)
        if j == c:
            continue
        if j > c:
            problems.append(
                f"{day}: {j} session(s) in the journal, {c} entry/entries in chronicle.json "
                "— the site renders a session the self-report does not cover, and refuses "
                "the night for it"
            )
        else:
            problems.append(
                f"{day}: {c} entry/entries in chronicle.json, {j} session(s) in the journal "
                "— the self-report claims a session the journal does not hold"
            )
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--file", default=CHRONICLE)
    ap.add_argument(
        "--journal",
        default=JOURNAL,
        help="journal directory to check the entries against; skipped if absent",
    )
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as fh:
        entries = json.load(fh)
    problems = check(entries) + check_completeness(entries, args.journal)

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
