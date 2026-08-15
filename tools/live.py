#!/usr/bin/env python3
"""The live figures of STILL DARK are generated into the record, and every superseded
figure in it must carry the instant it was true of.

Why this exists. Of the twelve failures this house banked at the fifth premiere gate,
six were the same failure: a figure that was true when a hand typed it and false by the
time anyone read it (banked 63, 64, 65, 66, 67, 71). The work's own face stopped having
that problem in session 84, when `data.py` began generating the page's data island from
the captures and `data.py --check` began failing the build if the two disagreed. The
record around the work — `PROJECT.md`, `WORKBOARD.md`, the work's `README.md` — never got
that treatment, and went on being typed by hand every night against a number that moves
every night.

This is that treatment. Two instruments in one file:

    python3 tools/live.py                # both checks; exit 1 if either fails
    python3 tools/live.py --write        # fill the generated regions from the captures
    python3 tools/live.py --regions      # regions only
    python3 tools/live.py --superseded   # the superseded-figure scan only

REGIONS. A file marks a generated region with a pair of HTML comments:

    <!-- live:share -->
    ...generated text...
    <!-- /live:share -->

`--check` regenerates every region from `capture/day.py` and `capture/edition.py` and
fails, naming the file and line, if what stands there is not what the captures say. The
prose of a region lives in SNIPPETS below, in one place, and nowhere in the record.

SUPERSEDED FIGURES. The rest of the record may — and should — carry earlier values of
these figures: that history is the work. What it may not do is carry them unstamped. So
the scan finds every share band, every `11 of X–Y`, every count of saved copies and every
count of distinct lists/contents/bodies/edition dates in the scanned files, and for each
one whose value is not tonight's it requires the paragraph it stands in to name WHEN it
was true — a UTC instant, a session number, a `→` transition, or a git hash a stranger
can open. A figure without its instant is a claim without its knowability, which is the
one thing this particular work is about.

What this instrument does NOT do, and will not pretend to: it cannot read tense. A
paragraph that says "the record holds N copies" in the present tense about a superseded
N passes this scan if it carries an instant. Judging that sentence is a reader's work,
and it stays a reader's work.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
CAPTURE = os.path.join(REPO, "projects", "season1", "capture")
CAPTURES = os.path.join(REPO, "projects", "season1", "captures")
DAY = "2026-08-04"

# The record files this instrument is responsible for. A file that starts carrying live
# figures and is not listed here is outside every check in this file.
SCANNED = [
    "projects/season1/PROJECT.md",
    "projects/season1/still-dark/README.md",
    "projects/season1/capture/README.md",
    "WORKBOARD.md",
]

BEGIN = re.compile(r"<!--\s*live:([a-z0-9-]+)\s*-->")
END = re.compile(r"<!--\s*/live:([a-z0-9-]+)\s*-->")


# ---------------------------------------------------------------- the source of truth

def figures():
    """Every live figure, read from the instruments and never from a file of prose."""
    out = subprocess.run(
        [sys.executable, os.path.join(CAPTURE, "day.py"), DAY, "--json"],
        capture_output=True, text=True, check=True,
    )
    d = json.loads(out.stdout)

    editions = set()
    contents = set()
    bodies = set()
    latest = None
    sys.path.insert(0, CAPTURE)
    from edition import content_sha256  # noqa: E402

    for name in sorted(os.listdir(CAPTURES)):
        if not name.endswith(".json"):
            continue
        cap = json.load(open(os.path.join(CAPTURES, name)))
        editions.add(cap["edition_date"])
        contents.add(content_sha256(cap))
        bodies.add(cap["fetch"]["sha256"])
        latest = cap

    lo, hi = d["share_knowable_OBSERVED"]
    band = d["vessels_dark_on_day"]["band"]
    obs = d["knowable_on_the_day_OBSERVED"]
    return {
        "share": f"{round(lo * 100)} %–{round(hi * 100)} %",
        "obs": obs,
        "denom_lo": band[0] + obs,   # certain + observed — the end that can only fall
        "denom_hi": band[1],
        "captures": d["captures_read"],
        "lists": len(editions),      # a LIST is an edition date: one list per day
        "contents": len(contents),
        "bodies": len(bodies),
        "certain": band[0],
        "latest_instant": latest["fetch"]["fetched_at_utc"],
        "latest_edition": latest["edition_date"],
    }


# ------------------------------------------------------------------------- the regions

def snip_share(f):
    return (
        f"**Live, at the capture of {f['latest_instant']}: `{f['share']}` — "
        f"{f['obs']} of {f['denom_lo']}–{f['denom_hi']}**, from **{f['captures']} saved copies** "
        f"holding **{f['lists']} distinct lists** ({f['contents']} contents, {f['bodies']} bodies). "
        f"*Generated by `python3 tools/live.py --write`; `python3 tools/live.py` fails if it "
        f"disagrees with the captures.*"
    )


def _history():
    """The falling end at every capture, re-derived — never typed, never carried forward."""
    sys.path.insert(0, CAPTURE)
    from edition import content_sha256  # noqa: E402
    rows = []
    for name in sorted(os.listdir(CAPTURES)):
        if not name.endswith(".json"):
            continue
        cap = json.load(open(os.path.join(CAPTURES, name)))
        at = cap["fetch"]["fetched_at_utc"]
        out = subprocess.run(
            [sys.executable, os.path.join(CAPTURE, "day.py"), DAY, "--as-of", at, "--json"],
            capture_output=True, text=True, check=True,
        )
        d = json.loads(out.stdout)
        lo, hi = d["share_knowable_OBSERVED"]
        rows.append((at, cap["edition_date"], round(lo * 100), round(hi * 100)))
    return rows


def snip_falls(f):
    rows = _history()
    by_capture = []
    for _at, _ed, lo, _hi in rows:
        if not by_capture or by_capture[-1] != lo:
            by_capture.append(lo)
    # A LIST is an edition date, and its value is the one that date ended on — the same
    # choice the face's run makes. Taking the FIRST capture of a date instead puts 37 %
    # into this sequence where the page's own run shows 35 %, because 10 August produced
    # two lists under one date. Found by this instrument disagreeing with the face,
    # session 95.
    last_of_date = {}
    order = []
    for _at, ed, lo, _hi in rows:
        if ed not in last_of_date:
            order.append(ed)
        last_of_date[ed] = lo
    by_list = []
    for ed in order:
        if not by_list or by_list[-1] != last_of_date[ed]:
            by_list.append(last_of_date[ed])
    seq = ", ".join(f"{v} %" for v in by_list)
    return (
        f"**The falling end has taken {len(by_list)} values at list granularity** — {seq} — "
        f"and so has fallen {len(by_list) - 1} times; at capture granularity it took "
        f"{len(by_capture)} values and fell {len(by_capture) - 1} times, the two granularities "
        f"differing because one edition date has produced more than one list. Every value is "
        f"reproduced by `python3 projects/season1/capture/day.py 2026-08-04 --as-of <instant>`, "
        f"and this paragraph is generated from those runs rather than carried forward."
    )


def snip_share_short(f):
    return (
        f"the share is **{f['share']}, {f['obs']} of {f['denom_lo']}–{f['denom_hi']}**, from "
        f"{f['captures']} saved copies holding {f['lists']} lists "
        f"(generated — `python3 tools/live.py`)"
    )


SNIPPETS = {
    "share": snip_share,
    "share-short": snip_share_short,
    "falls": snip_falls,
}


def regions_in(text):
    """Yield (name, line_of_begin, start_index, end_index) for each marked region."""
    lines = text.split("\n")
    open_name = None
    open_line = None
    start = None
    pos = 0
    for i, line in enumerate(lines, start=1):
        b = BEGIN.search(line)
        e = END.search(line)
        if b and not line.strip().startswith("<!-- /"):
            if open_name is not None:
                raise SystemExit(f"live.py: region live:{open_name} opened at line {open_line} is not closed")
            open_name, open_line = b.group(1), i
            start = pos + len(line) + 1
        elif e:
            if open_name is None:
                raise SystemExit(f"live.py: stray closing marker at line {i}")
            if e.group(1) != open_name:
                raise SystemExit(f"live.py: region live:{open_name} closed as live:{e.group(1)} at line {i}")
            yield open_name, open_line, start, pos
            open_name = None
        pos += len(line) + 1
    if open_name is not None:
        raise SystemExit(f"live.py: region live:{open_name} opened at line {open_line} is not closed")


def check_regions(f, write=False):
    bad = 0
    seen = 0
    for rel in SCANNED:
        path = os.path.join(REPO, rel)
        text = open(path, encoding="utf-8").read()
        edits = []
        for name, line, start, end in regions_in(text):
            seen += 1
            if name not in SNIPPETS:
                print(f"  {rel}:{line}  live:{name} — no snippet of that name exists")
                bad += 1
                continue
            want = SNIPPETS[name](f) + "\n"
            have = text[start:end]
            if have == want:
                continue
            if write:
                edits.append((start, end, want))
            else:
                bad += 1
                print(f"  {rel}:{line}  live:{name} DIFFERS")
                print(f"      captures say : {want.strip()}")
                print(f"      record says  : {have.strip()}")
        if write and edits:
            for start, end, want in reversed(edits):
                text = text[:start] + want + text[end:]
            open(path, "w", encoding="utf-8").write(text)
            print(f"  {rel}: {len(edits)} region(s) written")
    if not write:
        print(f"REGIONS: {seen} marked, {bad} disagreeing with the captures")
    return bad


# --------------------------------------------------------- the superseded-figure scan

FIGURE_PATTERNS = [
    ("share band", re.compile(r"\d{1,3}\s?%\s?–\s?\d{1,3}\s?%")),
    ("share as a division", re.compile(r"\b\d{1,3} of \d{1,3}[–-]\d{1,3}\b")),
    ("saved copies", re.compile(r"\b\d{1,3} saved copies\b")),
    ("a count of the record", re.compile(r"\b\d{1,3} (?:distinct )?(?:lists|contents|bodies|edition dates)\b")),
]

# A paragraph carrying a superseded figure must say when it was true, one of these ways.
STAMPS = [
    re.compile(r"--as-of"),
    re.compile(r"\b20\d\d-\d\d-\d\dT\d\d:?\d\d:?\d\dZ?"),
    re.compile(r"\bsessions? \d\d\b", re.I),
    re.compile(r"\b\d\d['’]s\b"),
    re.compile(r"→"),
    re.compile(r"git show"),
    re.compile(r"`[0-9a-f]{7,}"),
]


def live_strings(f):
    """Every rendering of tonight's figures that the scan must accept as current."""
    ok = set()
    lo, hi = f["share"].split("–")
    ok.add(f["share"])
    ok.add(f["share"].replace(" %", "%"))
    ok.add(f"{f['obs']} of {f['denom_lo']}–{f['denom_hi']}")
    ok.add(f"{f['obs']} of {f['denom_lo']}-{f['denom_hi']}")
    ok.add(f"{f['captures']} saved copies")
    for word, n in (("lists", f["lists"]), ("contents", f["contents"]),
                    ("bodies", f["bodies"]), ("edition dates", f["lists"])):
        ok.add(f"{n} {word}")
        ok.add(f"{n} distinct {word}")
    return ok


def paragraphs(text):
    """(start_line, text) for each blank-line-separated block."""
    out = []
    line_no = 1
    for block in text.split("\n\n"):
        out.append((line_no, block))
        line_no += block.count("\n") + 2
    return out


def scan_superseded(f):
    ok = live_strings(f)
    unstamped = 0
    stamped = 0
    for rel in SCANNED:
        path = os.path.join(REPO, rel)
        text = open(path, encoding="utf-8").read()
        # regions are generated; they are current by construction
        cut = []
        last = 0
        for _n, _l, start, end in regions_in(text):
            cut.append(text[last:start])
            cut.append(re.sub(r"[^\n]", " ", text[start:end]))
            last = end
        cut.append(text[last:])
        text = "".join(cut)

        for line_no, block in paragraphs(text):
            hits = []
            for label, pat in FIGURE_PATTERNS:
                for m in pat.finditer(block):
                    if m.group(0).strip() in ok:
                        continue
                    hits.append((label, m.group(0).strip()))
            if not hits:
                continue
            if any(s.search(block) for s in STAMPS):
                stamped += len(hits)
                continue
            unstamped += len(hits)
            print(f"  {rel}:{line_no}  UNSTAMPED — {', '.join(f'{v} ({l})' for l, v in hits)}")
            print(f"      {' '.join(block.split())[:150]}")
    print(f"SUPERSEDED: {stamped} superseded figure(s) carry their instant, {unstamped} do not")
    return unstamped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--regions", action="store_true")
    ap.add_argument("--superseded", action="store_true")
    a = ap.parse_args()

    f = figures()
    print(f"LIVE, from {f['captures']} captures: {f['share']} — {f['obs']} of "
          f"{f['denom_lo']}–{f['denom_hi']} · {f['lists']} lists · {f['contents']} contents · "
          f"{f['bodies']} bodies · latest {f['latest_instant']}")

    only_r = a.regions and not a.superseded
    only_s = a.superseded and not a.regions
    bad = 0
    if not only_s:
        bad += check_regions(f, write=a.write)
    if not only_r and not a.write:
        bad += scan_superseded(f)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
