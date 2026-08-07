#!/usr/bin/env python3
"""record_words.py — measure a project's live process record against its ceiling.

Repairs the defect of "a measurement whose instrument is unstated": this
house now declares, out loud, every time it counts, which tool did the
counting. `wc -w` is the standing instrument. Python's `str.split()` is
printed alongside it, labelled reference only, so the delta between the two
is visible rather than silently swallowed.

By default the count is taken from the COMMITTED tree (`git show <ref>:<path>`),
never the worktree, because a worktree figure can be obsolete before it is
even committed. Pass --worktree to read the working tree instead; doing so
prints a loud warning.

Reads a manifest of repo-relative paths, each either counted whole or
narrowed to one markdown section via `path :: <heading text>`. Stdlib and
`git`/`wc` only — no third-party packages.
"""

import argparse
import os
import re
import subprocess
import sys

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S.*)$")

# `wc -w` tokenizes differently under different locales (that is the whole
# reason the instrument had to be named). Pin the classic byte-oriented C
# locale explicitly so the standing figure does not silently change with
# whoever's shell happens to launch this script — Python itself coerces a
# bare C/POSIX locale to a UTF-8 one for its own subprocesses, which would
# otherwise make the count depend on an unstated detail all over again.
_WC_ENV = dict(os.environ)
_WC_ENV["LC_ALL"] = "C"


class RecordError(Exception):
    """Raised for any condition that should abort with exit code 2."""


def run(cmd, cwd=None, input_bytes=None, env=None):
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    return proc.returncode, proc.stdout, proc.stderr


def get_repo_root():
    code, out, err = run(["git", "rev-parse", "--show-toplevel"])
    if code != 0:
        raise RecordError(
            "not a git repository (git rev-parse --show-toplevel failed): "
            + err.decode("utf-8", "replace").strip()
        )
    return out.decode("utf-8").strip()


def read_committed(repo_root, ref, path):
    code, out, err = run(["git", "show", "{}:{}".format(ref, path)], cwd=repo_root)
    if code != 0:
        raise RecordError(
            "could not read {}:{} from committed tree: {}".format(
                ref, path, err.decode("utf-8", "replace").strip()
            )
        )
    return out.decode("utf-8", "replace")


def read_worktree(repo_root, path):
    import os

    full = os.path.join(repo_root, path)
    try:
        with open(full, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError as e:
        raise RecordError("could not read worktree file {}: {}".format(full, e))


def find_headings(text):
    """Return list of (line_index, level, heading_text) for markdown headings."""
    headings = []
    for i, line in enumerate(text.splitlines()):
        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            heading_text = m.group(2).strip()
            headings.append((i, level, heading_text))
    return headings


def extract_section(text, needle, path_label):
    lines = text.splitlines()
    headings = find_headings(text)
    matches = [h for h in headings if needle in h[2]]
    if len(matches) == 0:
        raise RecordError(
            "no heading matching '{}' found in {}".format(needle, path_label)
        )
    if len(matches) > 1:
        detail = "; ".join(
            "line {}: '{}'".format(idx + 1, txt) for idx, _lvl, txt in matches
        )
        raise RecordError(
            "ambiguous heading '{}' in {}: matches {} headings ({})".format(
                needle, path_label, len(matches), detail
            )
        )
    start_idx, start_level, _ = matches[0]
    end_idx = len(lines)
    for idx, level, _txt in headings:
        if idx > start_idx and level <= start_level:
            end_idx = idx
            break
    return "\n".join(lines[start_idx:end_idx])


def parse_manifest(manifest_path):
    entries = []
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()
    except OSError as e:
        raise RecordError("could not read manifest {}: {}".format(manifest_path, e))
    for lineno, raw in enumerate(raw_lines, start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "::" in line:
            path_part, heading_part = line.split("::", 1)
            path = path_part.strip()
            heading = heading_part.strip()
            if not path or not heading:
                raise RecordError(
                    "manifest {} line {}: malformed entry '{}'".format(
                        manifest_path, lineno, line
                    )
                )
            entries.append((path, heading))
        else:
            entries.append((line, None))
    if not entries:
        raise RecordError("manifest {} has no entries".format(manifest_path))
    return entries


def wc_w_count(text):
    code, out, err = run(
        ["wc", "-w"], input_bytes=text.encode("utf-8"), env=_WC_ENV
    )
    if code != 0:
        raise RecordError("wc -w failed: " + err.decode("utf-8", "replace").strip())
    first_field = out.decode("utf-8").strip().split()[0]
    return int(first_field)


def python_split_count(text):
    return len(text.split())


def resolve_manifest_path(manifest_arg, repo_root):
    import os

    if os.path.isfile(manifest_arg):
        return manifest_arg
    candidate = os.path.join(repo_root, manifest_arg)
    if os.path.isfile(candidate):
        return candidate
    raise RecordError(
        "manifest not found at '{}' or '{}'".format(manifest_arg, candidate)
    )


def main():
    parser = argparse.ArgumentParser(
        description="Measure a project's live process record against its word ceiling, "
        "with the counting instrument named."
    )
    parser.add_argument(
        "--manifest",
        default="tools/record-files.txt",
        help="manifest file listing entries to count (default: tools/record-files.txt)",
    )
    parser.add_argument(
        "--ref",
        default="HEAD",
        help="git ref to read committed blobs from (default: HEAD)",
    )
    parser.add_argument(
        "--worktree",
        action="store_true",
        help="read the working tree instead of the committed tree (obsolete-before-commit risk)",
    )
    parser.add_argument(
        "--ceiling",
        type=int,
        default=3000,
        help="word ceiling to compare the standing instrument's total against (default: 3000)",
    )
    args = parser.parse_args()

    try:
        repo_root = get_repo_root()
        manifest_path = resolve_manifest_path(args.manifest, repo_root)
        entries = parse_manifest(manifest_path)

        if args.worktree:
            print(
                "WARNING: --worktree reads the working tree, not the committed tree. "
                "A worktree figure can be obsolete before it is even committed. "
                "The house's standing figure is taken from committed blobs (git show).",
                file=sys.stderr,
            )

        rows = []  # (label, wc_count, split_count)
        for path, heading in entries:
            if args.worktree:
                text = read_worktree(repo_root, path)
            else:
                text = read_committed(repo_root, args.ref, path)

            if heading is not None:
                section_text = extract_section(text, heading, path)
                label = "{} :: {}".format(path, heading)
            else:
                section_text = text
                label = path

            wc_count = wc_w_count(section_text)
            split_count = python_split_count(section_text)
            rows.append((label, wc_count, split_count))

    except RecordError as e:
        print("ERROR: {}".format(e), file=sys.stderr)
        return 2
    except Exception as e:  # unexpected failure — still an error, not a silent pass
        print("ERROR: unexpected failure: {}".format(e), file=sys.stderr)
        return 2

    source_desc = "WORKING TREE" if args.worktree else "committed tree ({})".format(args.ref)
    print("Source: {}".format(source_desc))
    print()

    label_width = max(len(r[0]) for r in rows)
    label_width = max(label_width, len("ENTRY"))
    header = "{:<{lw}}  {:>12}  {:>12}  {:>8}".format(
        "ENTRY", "wc -w", "split()", "delta", lw=label_width
    )
    print(header)
    print("-" * len(header))
    total_wc = 0
    total_split = 0
    for label, wc_count, split_count in rows:
        delta = split_count - wc_count
        print(
            "{:<{lw}}  {:>12}  {:>12}  {:>8}".format(
                label, wc_count, split_count, delta, lw=label_width
            )
        )
        total_wc += wc_count
        total_split += split_count
    print("-" * len(header))
    total_delta = total_split - total_wc
    print(
        "{:<{lw}}  {:>12}  {:>12}  {:>8}".format(
            "TOTAL", total_wc, total_split, total_delta, lw=label_width
        )
    )
    print()
    print("wc -w                          : {}  <-- THE STANDING INSTRUMENT".format(total_wc))
    print("python str.split() (reference only): {}".format(total_split))
    print("delta (split - wc -w)          : {}".format(total_delta))
    print()

    ceiling = args.ceiling
    if total_wc <= ceiling:
        print("UNDER by {} (standing figure {} vs ceiling {})".format(
            ceiling - total_wc, total_wc, ceiling
        ))
        return 0
    else:
        print("BREACH by {} (standing figure {} vs ceiling {})".format(
            total_wc - ceiling, total_wc, ceiling
        ))
        return 1


if __name__ == "__main__":
    sys.exit(main())
