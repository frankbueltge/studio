#!/usr/bin/env python3
"""prereg.py — freeze a pre-registration at dispatch, and prove afterwards whether it moved.

Repairs the defect of "the pre-registration moved twice while the readers
were answering it": this house writes its questions and pass marks into a
staging memo before dispatching severed readers, and until now nothing ever
froze, hashed or checked that memo — so an edit mid-panel was only caught by
accident. This tool hashes the file at freeze time and refuses to let a
second freeze silently replace the record; every later change to a sealed
file must break the seal explicitly, and breaking the seal always leaves a
trace instead of erasing the old one.

Commands:
    prereg.py freeze <file> [--break-seal]
    prereg.py verify <file>
    prereg.py status [dir]

Stdlib only.
"""

import argparse
import datetime
import hashlib
import os
import sys

SIDECAR_SUFFIX = ".frozen"

STANZA_SEP = "-" * 40


def utc_now_iso():
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def sha256_of_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        data = f.read()
    h.update(data)
    return h.hexdigest(), len(data)


def sidecar_path(path):
    return path + SIDECAR_SUFFIX


def write_first_stanza(sidecar, path, digest, length, timestamp):
    with open(sidecar, "w", encoding="utf-8") as f:
        f.write("PRE-REGISTRATION SEAL\n")
        f.write("path: {}\n".format(path))
        f.write("sha256: {}\n".format(digest))
        f.write("bytes: {}\n".format(length))
        f.write("frozen_utc: {}\n".format(timestamp))


def append_broken_seal_stanza(sidecar, digest, length, timestamp):
    with open(sidecar, "a", encoding="utf-8") as f:
        f.write("\n{}\n".format(STANZA_SEP))
        f.write("SEAL BROKEN\n")
        f.write("new_sha256: {}\n".format(digest))
        f.write("new_bytes: {}\n".format(length))
        f.write("broken_utc: {}\n".format(timestamp))


def parse_sidecar(sidecar):
    """Parse a .frozen sidecar into (first_stanza_dict, list_of_broken_stanza_dicts)."""
    with open(sidecar, "r", encoding="utf-8") as f:
        content = f.read()

    stanza_texts = content.split("\n" + STANZA_SEP + "\n")
    first_raw = stanza_texts[0]
    broken_raws = stanza_texts[1:]

    def parse_kv(raw):
        d = {}
        for line in raw.splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                d[k.strip()] = v.strip()
        return d

    first = parse_kv(first_raw)
    broken = [parse_kv(r) for r in broken_raws]
    return first, broken


def cmd_freeze(args):
    path = args.file
    if not os.path.isfile(path):
        print("ERROR: no such file: {}".format(path), file=sys.stderr)
        return 2

    sidecar = sidecar_path(path)
    digest, length = sha256_of_file(path)
    timestamp = utc_now_iso()

    if os.path.exists(sidecar):
        if not args.break_seal:
            print(
                "REFUSED: {} already exists. This pre-registration is already frozen.".format(
                    sidecar
                ),
                file=sys.stderr,
            )
            print(
                "Use --break-seal if the memo genuinely must change after dispatch; "
                "this will append a traceable record, not erase the original seal.",
                file=sys.stderr,
            )
            return 3
        append_broken_seal_stanza(sidecar, digest, length, timestamp)
        print("SEAL BROKEN: appended new stanza to {}".format(sidecar))
        print("new sha256: {}".format(digest))
        print("new bytes:  {}".format(length))
        print("broken at:  {}".format(timestamp))
        print(
            "The original freeze stanza was NOT removed — the sidecar now proves this file moved."
        )
        return 0

    write_first_stanza(sidecar, path, digest, length, timestamp)
    print("FROZEN: {}".format(sidecar))
    print("sha256:     {}".format(digest))
    print("bytes:      {}".format(length))
    print("frozen at:  {}".format(timestamp))
    return 0


def cmd_verify(args):
    path = args.file
    sidecar = sidecar_path(path)

    if not os.path.isfile(sidecar):
        print(
            "NO SEAL: {} has no {} sidecar. An unfrozen pre-registration is a failure, "
            "not a pass.".format(path, sidecar),
            file=sys.stderr,
        )
        return 2

    if not os.path.isfile(path):
        print("ERROR: no such file: {}".format(path), file=sys.stderr)
        return 2

    first, broken = parse_sidecar(sidecar)
    current_digest, _current_len = sha256_of_file(path)
    frozen_digest = first.get("sha256", "")
    frozen_time = first.get("frozen_utc", "unknown")

    if current_digest == frozen_digest:
        print("UNMOVED")
        print("sha256:    {}".format(frozen_digest))
        print("frozen at: {}".format(frozen_time))
        if broken:
            print(
                "NOTE: {} broken-seal stanza(s) recorded in {} even though current bytes "
                "match the first seal.".format(len(broken), sidecar)
            )
        return 0
    else:
        print("MOVED")
        print("frozen sha256:  {}".format(frozen_digest))
        print("current sha256: {}".format(current_digest))
        print("frozen at:      {}".format(frozen_time))
        print("broken seals:   {}".format(len(broken)))
        return 1


def cmd_status(args):
    directory = args.dir or "."
    if not os.path.isdir(directory):
        print("ERROR: no such directory: {}".format(directory), file=sys.stderr)
        return 2

    found_any = False
    exit_code = 0
    for root, _dirs, files in sorted(os.walk(directory)):
        for name in sorted(files):
            if not name.endswith(SIDECAR_SUFFIX):
                continue
            found_any = True
            sidecar = os.path.join(root, name)
            original = sidecar[: -len(SIDECAR_SUFFIX)]

            try:
                first, broken = parse_sidecar(sidecar)
            except OSError as e:
                print("{}: ERROR reading sidecar ({})".format(sidecar, e))
                exit_code = 2
                continue

            frozen_digest = first.get("sha256", "")
            seals_note = (
                "{} seal(s) broken".format(len(broken)) if broken else "no seals broken"
            )

            if not os.path.isfile(original):
                print("{}: NO SOURCE FILE ({})".format(original, seals_note))
                exit_code = max(exit_code, 2)
                continue

            current_digest, _len = sha256_of_file(original)
            if current_digest == frozen_digest:
                print("{}: UNMOVED ({})".format(original, seals_note))
            else:
                print("{}: MOVED ({})".format(original, seals_note))
                exit_code = max(exit_code, 1)

    if not found_any:
        print("no *.frozen sidecars found under {}".format(directory))
    return exit_code


def main():
    parser = argparse.ArgumentParser(
        description="Freeze a pre-registration at dispatch and prove afterwards whether it moved."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_freeze = sub.add_parser("freeze", help="hash and seal a file")
    p_freeze.add_argument("file", help="path to the pre-registration file")
    p_freeze.add_argument(
        "--break-seal",
        action="store_true",
        help="append a new stanza recording a deliberate, traceable change to an already-sealed file",
    )
    p_freeze.set_defaults(func=cmd_freeze)

    p_verify = sub.add_parser("verify", help="check a file against its seal")
    p_verify.add_argument("file", help="path to the pre-registration file")
    p_verify.set_defaults(func=cmd_verify)

    p_status = sub.add_parser("status", help="report on all sealed files under a directory")
    p_status.add_argument("dir", nargs="?", default=".", help="directory to scan (default: .)")
    p_status.set_defaults(func=cmd_status)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
