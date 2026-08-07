#!/usr/bin/env python3
"""STILL DARK — what makes one edition the same as another.

Written 2026-08-06 (session 70), because the record contradicted the instrument.

Until tonight this house identified an edition by the **sha256 of the raw page body**.
On that test, capture 3 (2026-08-05T19:17:55Z) was "the same edition, byte for byte" as
capture 2, and the work printed that sentence on its own face. Capture 4
(2026-08-06T04:36:19Z) broke the test: the body hash MOVED (17c07fc3… → aed92f4f…) at an
identical byte count (35,485), while every field this work reads — the printed edition
date, the aggregates, the case of the day, all eight vessels with their flags, durations
and waters — stayed identical.

So a raw-body hash is not an edition's identity. It is the identity of a *response*, and a
response carries things that are not the edition: the site's own fingerprinted asset paths
(this page links `_astro/<name>.<hash>.css` and `.js`, whose hashes move whenever the site
is rebuilt), and whatever else a deploy touches. This house does NOT claim to know which of
those moved between 19:17 and 04:36 — the raw bodies were never kept, only their hashes, so
the cause is unrecoverable and is not asserted.

What is asserted, and is checkable: two hashes, not one.

  body_sha256     — of the raw bytes. Already recorded in every capture since the first.
                    Answers: did the response change?
  content_sha256  — of the material the work actually reads, canonically serialised.
                    Answers: did the EDITION change?

The second is computed here, from a capture file alone, so it applies to captures written
before this module existed. No committed capture was rewritten to add it: the captures are
immutable, and a record that gets edited when the method improves is not a record.

    python3 edition.py            # print the table for every committed capture
"""

import glob
import hashlib
import json
import os
import re

# Exactly the fields the work publishes from. Nothing about the fetch, nothing about the
# response, nothing this house derives afterwards — those belong to other tiers and would
# make the digest answer a different question.
CONTENT_FIELDS = (
    "edition_date_printed",
    "edition_date",
    "aggregates",
    "case_of_the_day",
    "vessels",
)


def content_payload(capture):
    return {k: capture.get(k) for k in CONTENT_FIELDS}


def content_sha256(capture):
    """sha256 of the edition's own material, canonically serialised.

    Canonical means: keys sorted, no insignificant whitespace, UTF-8 as written. Two
    captures agree here exactly when the page said the same thing about the sea, whatever
    the bytes around it did.
    """
    blob = json.dumps(
        content_payload(capture),
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


# --- the case of the day's waters, added 2026-08-06 (session 73) ---------------------
#
# Upstream prints the case of the day ONCE, as a prose sentence, and never as a row of the
# list. The list rows carry a waters field; the prose carries the same information inside
# a sentence, and the parser only ever read the rows. So the vessel the instrument gives
# the most space to was the one vessel on this work's face with no waters at all
# (TUNAMAR, 4 August). The string is printed by the instrument, so recovering it is
# SOURCED, not derived — but it is recovered at READ time, from `case_of_the_day.prose`,
# which every capture has always carried. No capture is rewritten: captures are immutable,
# and — the reason that matters here — `content_sha256` digests the vessel records, so a
# parser that wrote a new field would have made two captures of one unchanged edition
# disagree about their identity. The work's own identity test would have been falsified by
# a repair. (Session 70 learned that lesson the other way round; this is the same law.)
#
# The warrant, and its exact size: MICRONESIA103 (FSM, 39 d) stands as a list row in the
# edition of 4 August with waters "Marshallese EEZ", and as the case of the day in the
# editions of 5 and 6 August with prose ending "in Marshallese EEZ". The strings agree.
# That is ONE vessel seen both ways, and it is the whole of the warrant. What the page
# does NOT state is what either field refers to — the prose names the waters at the
# RESURFACING point; the list column names no referent at all. This house therefore does
# not assert the two are the same field, only that both are strings the instrument printed
# about that vessel's waters.
CASE_WATERS_RE = re.compile(r",\s*in\s+([^,]+?)\s*\.\s*$")


def case_waters(capture):
    """The waters named in the case-of-the-day prose, or None if it names none."""
    case = capture.get("case_of_the_day") or {}
    prose = case.get("prose") or ""
    m = CASE_WATERS_RE.search(prose)
    return m.group(1).strip() if m else None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    capdir = os.path.normpath(os.path.join(here, "..", "captures"))
    rows = []
    for p in sorted(glob.glob(os.path.join(capdir, "*.json"))):
        with open(p, encoding="utf-8") as f:
            c = json.load(f)
        rows.append(
            (
                c["fetch"]["fetched_at_utc"],
                c.get("edition_date"),
                c["fetch"]["sha256"][:8],
                content_sha256(c)[:8],
                len(c.get("vessels", [])),
            )
        )
    print(f"{'fetched (UTC)':<22}{'edition':<12}{'body':<10}{'content':<10}vessels")
    for r in rows:
        print(f"{r[0]:<22}{str(r[1]):<12}{r[2]:<10}{r[3]:<10}{r[4]}")
    print(
        f"\n{len(rows)} capture(s) · "
        f"{len({r[1] for r in rows})} distinct edition date(s) · "
        f"{len({r[3] for r in rows})} distinct content(s) · "
        f"{len({r[2] for r in rows})} distinct bod(y/ies)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
