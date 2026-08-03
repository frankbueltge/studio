#!/usr/bin/env python3
"""
VERIFIER-62 — extraction helper only.

This script does NOT decide MARK-ON-OBJECT for any record. It exists so a
stranger can print the same 55 Description fields the Verifier read by hand
and see the same text, in the same order, that produced the per-record table
in VERIFIER-62-BRANDMARK.md.

Usage:
    python3 verifier-62-extract.py recalls-2026-07-01_2026-08-02.json

Prints, for each record in file order: RecallNumber, a one-line object name
(Title, truncated to the leading noun phrase before the first " Recalled"),
and the full verbatim Description field.

No coding, no regex classification, no tally happens in this file. Coding
was done by a human reading each block below, one at a time, against the
written coding quoted in VERIFIER-62-BRANDMARK.md section 1.
"""
import json
import sys


def one_line_name(title, products):
    if products:
        name = products[0].get("Name", "").strip()
        if name:
            return name
    if " Recalled" in title:
        return title.split(" Recalled")[0].strip()
    return title.strip()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "recalls-2026-07-01_2026-08-02.json"
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    print(f"N = {len(data)}")
    for i, rec in enumerate(data, 1):
        num = rec.get("RecallNumber", "")
        name = one_line_name(rec.get("Title", ""), rec.get("Products", []))
        desc = rec.get("Description", "")
        print("=" * 100)
        print(f"[{i:02d}] RecallNumber {num} — {name}")
        print("-" * 100)
        print(desc)
    print("=" * 100)


if __name__ == "__main__":
    main()
