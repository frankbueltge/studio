#!/usr/bin/env python3
"""The index must see everywhere this practice writes.

The tool arrived here on 2026-08-12, ported from the atelier after the same failure was found
in three houses on one night. This house's version of it was the plainest: there was no recall
at all. The constitution says memory is "`memory/`, `projects/` and this repository's git
history" — and that was 585,000 words across 232 files, `projects/` alone 277,000, the curated
`memory/` itself 86,000. A session was told to hold, by reading, what no session can read.

The tool is only half of the fix. The other half is this test, because the failure in the
sibling houses was never a broken tool: `recall` kept working perfectly on a corpus that no
longer held the work, and nothing said so. In the atelier a whole unit of work moved into a
directory the index did not cover and stayed invisible for six weeks; in the field the four
files the constitution names FIRST at orientation were the ones recall could not return.

So the check is not "does the tool work". It is: **does the index still point at the places
this repository actually keeps its records.**
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cli import SOURCE_GLOBS, _collect_source_files

REPO_ROOT = Path(__file__).resolve().parents[2]

# Directories holding this practice's records. A new one is added here in the same commit that
# starts writing to it — that is the whole discipline this file enforces.
RECORD_DIRS = ["journal", "works", "projects", "etudes", "delivery", "studio-feedback"]

# Files the constitution's Memory section names. These must be reachable by recall, or the
# instruction sends a session to files it then has to open by hand.
CURATED_MEMORY = [
    "memory/decisions.md",
    "memory/open-questions.md",
    "memory/discarded.md",
]

# Everything else at the root, with the reason it is not indexed. Listing exclusions explicitly
# means a new top-level directory cannot be silently forgotten.
NOT_RECORDS = {
    "archive": "superseded texts, kept unchanged; recall should return the live text",
    "site-prs": "pull-request bodies for the site, not this practice's record",
    "toolchain": "code and configuration",
    "tools": "code",
    "memory": "indexed: curated files, dossiers, method-notes, season-two",
}


def _covered(rel_dir: str) -> bool:
    return any(glob.startswith(f"{rel_dir}/") for glob in SOURCE_GLOBS)


def test_every_record_directory_is_indexed() -> None:
    missing = [d for d in RECORD_DIRS if (REPO_ROOT / d).is_dir() and not _covered(d)]
    assert not missing, (
        f"these directories hold records but no SOURCE_GLOBS entry reaches them: {missing}. "
        "A session cannot recall what is not indexed, so it reads the whole record instead. "
        "Add the glob in the commit that starts writing there."
    )


def test_the_curated_memory_is_reachable() -> None:
    indexed = {p.resolve() for p in _collect_source_files(REPO_ROOT)}
    unreachable = [
        rel for rel in CURATED_MEMORY
        if (REPO_ROOT / rel).is_file() and (REPO_ROOT / rel).resolve() not in indexed
    ]
    assert not unreachable, (
        f"the curated memory is not reachable by recall: {unreachable}. The constitution's "
        "Memory section names these; if recall cannot return them, the instruction is decorative."
    )


def test_no_record_directory_is_silently_unindexed() -> None:
    unaccounted = []
    for entry in sorted(REPO_ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        if entry.name in RECORD_DIRS or entry.name in NOT_RECORDS:
            continue
        if not any(entry.rglob("*.md")):
            continue
        unaccounted.append(entry.name)
    assert not unaccounted, (
        f"top-level directories holding markdown are neither indexed nor declared non-records: "
        f"{unaccounted}. Add each to RECORD_DIRS (and SOURCE_GLOBS) or to NOT_RECORDS with the "
        "reason it is not a record."
    )


def test_the_largest_record_directory_is_actually_reachable() -> None:
    """The regression in the first person: `projects/` is the biggest thing here."""
    projects = REPO_ROOT / "projects"
    if not projects.is_dir():
        return
    on_disk = {p.resolve() for p in projects.rglob("*.md")}
    if not on_disk:
        return
    indexed = {p.resolve() for p in _collect_source_files(REPO_ROOT)}
    assert on_disk & indexed, (
        "no file under projects/ is indexed — 277,000 words the constitution calls memory, "
        "which recall cannot reach."
    )
