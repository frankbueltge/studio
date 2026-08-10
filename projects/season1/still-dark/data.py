#!/usr/bin/env python3
"""STILL DARK — build the work's data island from the committed captures.

Why this exists. This house has twice put a number on a face that came out of a head
instead of off a record: session 66 dropped a vessel from a shelf the conductor had
counted first-hand, and session 70 caught a sha256 written from memory before the real
one was read off the capture. Both were caught, neither should have been possible. From
tonight the figures the work prints are COMPUTED from `../captures/*.json` by this
script and pasted into `index.html` as one block; nothing in that block is typed by
hand, and re-running the script is how anyone checks that the page belongs to the
record.

    python3 data.py            # print the JSON island
    python3 data.py --check    # exit 1 if index.html's island differs from a fresh build

Tiers, unchanged and never merged:
  SOURCED  — vessel name, flag, days dark, waters, edition date: printed upstream.
  DERIVED  — the two-ended date bands, and the arithmetic of the share.
  OBSERVED — the captures: fetch time, status, bytes, hashes, and which edition first
             carried a vessel. This house's record of its own knowing.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CAPTURE_DIR = os.path.normpath(os.path.join(HERE, "..", "capture"))
CAPTURES = os.path.normpath(os.path.join(HERE, "..", "captures"))
sys.path.insert(0, CAPTURE_DIR)

from day import analyse, bands, index, load  # noqa: E402
from edition import content_sha256  # noqa: E402

# Which lede the build uses. The arms of session 78's panel differ in this string and in
# nothing else; `--lede` sets it, and the work's own committed state is whatever the last
# `--write` put in index.html. Never read from the environment: an arm that could differ
# from its control by a shell variable is not a control.
LEDE = "committed"

# Whether the build hoists the repeated OBSERVED line out of the rows: stated once per
# block instead of identically on every row. Staged as an arm in session 79 and ADOPTED
# the same night on its own frozen rule — 0 of 2 severed readers named the line or its
# replacement, against 2 of 4 naming the repetition on the uncut page the night before
# (`STAGING-79.md` Q4, `PANEL-79.md`). `--no-cuts` rebuilds the superseded shape, because
# retired is not deleted and a shape this house can no longer produce is a shape it can no
# longer be checked on. index.html renders both.
CUTS = True

DAY = "2026-08-04"
DAY_PRINTED = "4 AUGUST 2026"

# The commit that first carried the struck figure and the law printed beside it. Its
# timestamp is read from git, never typed: this house has already put one publication
# date on this face out of a head, and the dates that reach a face come off a record.
PUBLISHED_COMMIT = "91ee19b"

# There is no second constant here, and its absence is banked failure 17 (session 78).
#
# Until tonight a hand-typed `PRIOR_AS_OF` supplied the struck row's copy-and-list
# counts while `PUBLISHED_COMMIT` supplied its date, and session 75 advanced the
# constant past the commit without anything noticing that the two now named different
# moments. The face then read: *"as this page published it at 08:36 UTC on 6 August,
# from 8 saved copies of 3 lists — 69 %–100 %."* At 08:36 UTC on 6 August this record
# held FIVE saved copies. The figure was right, the date was right, and the provenance
# printed between them belonged to a third moment a day and a half later.
#
# So the struck row now has ONE anchor and it is a commit, not a typed string: the
# instant this page published the law is the instant its counts, its figure and its
# date are all read at. A constant that has to be advanced by hand each time the record
# moves is the same defect as a number typed by hand, wearing a variable's name.

# What going dark IS. Owed item (e), banked in session 74 and unpaid since: the face never
# said it. The word *transponder* appeared nowhere on a page whose whole subject is a radio
# silence — a stranger was asked to read about an absence whose mechanism was never named,
# which is the terminal test failing at the first line. The quotation is verbatim from the
# "What this is" section of the method sheet named in `method.source`; the gloss beside it
# says nothing that sheet does not say, and both of its figures are the source's own.
DEFINITION_QUOTE = (
    "The AIS picture of the seas looks complete. It is not — ships switch off their "
    "transponder on purpose to vanish."
)
# Session 77 split this in two — the working clause above the lede, the thresholds left
# below — and four severed readers refused the change at its own pre-registered mark
# (`PANEL-77.md`, Q1: arm A 1 of 2, retired to commit 8b8e777). The split is reverted with the
# sentence stands exactly as it stood, one string, not one character rewritten. The
# refuted arm is not deleted: `../staging-77/restaged/` holds the built page a stranger
# can open, beside the control it lost to.
DEFINITION = (
    "Going dark is a ship switching off its AIS transponder — the radio signal that puts it "
    "on the public picture of the sea — so that it stops being tracked. The instrument this "
    "page reads counts only disabling its own source classifies as high-confidence and "
    "intentional: at least 12 hours dark, at least 50 nautical miles offshore."
)

# Upstream's restraint, inherited and repeated wherever these numbers travel. It stood
# hand-written in the page's foot until session 80; it is a constant here now because the
# running head names twenty vessels ABOVE that foot, and a restraint that does not travel
# with the names it restrains is a restraint on the wrong page. One string, two places, no
# drift possible.
RESTRAINT = (
    "“Intentional” is a machine estimate by Global Fishing Watch — a probability, not "
    "proof; the instrument makes no claim of illegality against any vessel or state, and "
    "neither do we."
)

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_CAPS = [m.upper() for m in MONTHS]


def d(s):
    return datetime.date.fromisoformat(s)


def span(a, b):
    """'2–9 Jun' where the months agree, '27 Jun–4 Jul' where they do not."""
    if a.month == b.month:
        return f"{a.day}–{b.day} {MONTHS[a.month - 1]}"
    return f"{a.day} {MONTHS[a.month - 1]}–{b.day} {MONTHS[b.month - 1]}"


FULL_MONTHS = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
WORDS = {0: "no", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
         14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
         19: "nineteen", 20: "twenty"}
# The list stopped at sixteen until session 78, so the night the total reached seventeen
# the band sentence started a sentence with a numeral while saying "eleven" four words
# later — one sentence in two voices, and nothing failed. Extended to twenty; when the
# total passes twenty this will do it again, which is why `word()` returns digits rather
# than raising: a page that prints "20" is wrong in its manners, and a page that prints
# nothing is wrong in its facts.


def word(n):
    """A count in words where the page speaks, in digits where it counts. Never typed."""
    return WORDS.get(n, str(n))


def printed_date(s):
    x = d(s)
    return f"{x.day} {FULL_MONTHS[x.month - 1]} {x.year}"


def day_month(s):
    """'4 August' — the day named without its year, for a second naming in one sentence."""
    x = d(s)
    return f"{x.day} {FULL_MONTHS[x.month - 1]}"


def short_caps(s):
    x = d(s)
    return f"{x.day} {MONTHS_CAPS[x.month - 1]}"


def commit_time(ref):
    """The commit's own timestamp, read from git. Raises rather than guessing."""
    out = subprocess.run(
        ["git", "-C", HERE, "log", "-1", "--format=%cI", ref],
        capture_output=True, text=True, check=True,
    )
    return datetime.datetime.fromisoformat(out.stdout.strip())


def run_day(*args):
    """The verbatim output the page prints, produced by the script the page names."""
    out = subprocess.run(
        [sys.executable, os.path.join(CAPTURE_DIR, "day.py"), DAY, *args],
        capture_output=True, text=True, check=True,
    )
    return out.stdout


def share_line(a, status):
    """(figure, numerator, denominator band) for one analysis, from the script's own fields.

    `status` is the one word that makes the pair of figures readable without eyes. Until
    tonight the superseded figure was retracted by a single CSS declaration — banked failure
    12, found by 74's panel: a reader who hears this page was given two live percentages for
    one day, and a tier the eye can read and the ear cannot is a blurred tier. The word is
    part of the row's text, so it survives every extraction the strike-through does not.
    """
    lo, hi = a["share_knowable_OBSERVED"]
    n = a["knowable_on_the_day_OBSERVED"]
    b = a["vessels_dark_on_day"]["band"]
    return {
        "status": status,
        "figure": f"{round(lo * 100)} %–{round(hi * 100)} %",
        "of": f"{n} of {b[0]}–{b[1]}",
        "editions": len(a["editions_read"]),
        "captures": a["captures_read"],
    }


def band_line(a, caps):
    """The one sentence DRAMATURG-74 §A ordered under the two shares, computed throughout.

    Three severed readers of session 73, unprompted and against no threshold, named the
    notation `11 of 0–16` the hardest thing on this page — *"'11 of 0' is a nonsense
    phrase in ordinary reading"* — and its only gloss stood in the terminal block, the one
    place no hand may touch. The percentages themselves scored 3 of 3 twice. This sentence
    says why the total has two ends and what those ends do to the fraction, and it is the
    whole of tonight's edit to the face.

    Not one figure is typed. The nought in particular is a BRANCH on the computed count,
    never a literal: this house's recurring failure is a number reaching a face out of a
    head, and a nought is the easiest of all to write by hand and be wrong about.
    """
    b = a["vessels_dark_on_day"]["band"]
    n = a["knowable_on_the_day_OBSERVED"]
    lo, hi = b[0], b[1]
    # The window is the reason the count has two ends at all, and it is read off the
    # capture's own method block rather than asserted here.
    wd = caps[-1]["method"]["window_days"]
    window = "a week-wide window" if wd == 7 else f"a window {word(wd)} days wide"
    certainly = (
        "not one of them certainly" if lo == 0 else f"{word(lo)} of them certainly"
    )
    return (
        f"{word(hi).capitalize()} ships could have been dark on {printed_date(DAY)} and "
        f"{certainly}, because the instrument publishes a return only as {window} — so the "
        f"total is written {lo}–{hi}, and the share runs from {n} of {hi} to "
        f"{n} of {max(lo, n)}."
    )


def seen_all(rows):
    """The one OBSERVED date a whole block shares, or None if it shares none.

    Returns the block-level sentence only when every row in the block carries the
    identical `seen` string. One differing row is enough to refuse the hoist, and the
    refusal is the point: the rows would then be saying different things and a single
    line above them would say a third.
    """
    dates = {r["seen"] for r in rows}
    if len(dates) != 1:
        return None
    when = dates.pop().replace("first seen ", "")
    if len(rows) == 1:
        return f"this page first saw it on {when}"
    return f"this page first saw all {WORDS.get(len(rows), str(len(rows)))} on {when}"


def build():
    pub = commit_time(PUBLISHED_COMMIT).astimezone(datetime.timezone.utc)
    # the one anchor: the instant the law was published, in the format the captures
    # themselves carry, so `day.py --as-of` reproduces the struck row exactly
    published_as_of = pub.strftime("%Y-%m-%dT%H:%M:%SZ")
    caps_now = load(CAPTURES)
    caps_then = load(CAPTURES, as_of=published_as_of)
    now = analyse(DAY, caps_now)
    then = analyse(DAY, caps_then)

    # gfw ids and waters, from the capture that first carried each vessel
    gfw = {}
    for c in caps_now:
        for v in c.get("vessels", []):
            gfw.setdefault(v["name"], v.get("gfw_url"))

    rows_by_name = index(caps_now)
    seen_at = {r["name"]: r for r in rows_by_name.values()}

    groups = {}
    for e in now["certain"] + now["possible"]:
        r = seen_at[e["name"]]
        end_lo, end_hi = bands(r)
        dark_lo = end_lo - datetime.timedelta(days=e["days_dark"])
        dark_hi = end_hi - datetime.timedelta(days=e["days_dark"])
        row = {
            "name": e["name"],
            "flag": e["flag"],
            "days_dark": e["days_dark"],
            "waters": e["waters"] or "",
            "went_dark_between": [dark_lo.isoformat(), dark_hi.isoformat()],
            "resurfaced_between": [end_lo.isoformat(), end_hi.isoformat()],
            "band_text": f"dark {span(dark_lo, dark_hi)} → back {span(end_lo, end_hi)}",
            "gfw_url": gfw.get(e["name"]),
            # Short on the row, exact in the ledger. Eleven repetitions of one ISO instant
            # were eleven repetitions of this house's filing system (DRAMATURG-72 §A); the
            # instant itself is checkable four inches lower, in the OBSERVED table.
            "seen": f"first seen {short_caps(r['first_seen_utc'][:10])}",
        }
        groups.setdefault(r["first_edition_date"], []).append(row)

    target = d(DAY)
    field = []
    for ed in sorted(groups):
        late = (d(ed) - target).days
        rows = sorted(groups[ed], key=lambda r: -r["days_dark"])
        field.append({
            "edition": ed,
            "edition_printed": printed_date(ed),
            "days_after": late,
            # "edition" is the instrument's word and this house's filing word; on the face
            # it is the list the instrument published that day (DRAMATURG-72 §A). It stays
            # as a column of the OBSERVED ledger, where the filing system IS the object.
            "label": (
                f"IN THE LIST OF {short_caps(ed)} — the day itself"
                if late == 0 else
                f"ADDED BY THE LIST OF {short_caps(ed)} — "
                f"{'one day' if late == 1 else WORDS.get(late, str(late)) + ' days'} after the day"
            ),
            "count": len(rows),
            # Session 79's staged cut, owed item (l), and the first cut on this face that
            # arrives with readers behind it: `first seen 5 AUG` printed identically down
            # eleven rows of the first block, and two of four severed readers named that
            # repetition unprompted (`PANEL-78.md` Q3; `DRAMATURG-77.md` §2 ordered it a
            # night earlier on judgement alone). Under --cuts the line is stated ONCE per
            # block and the rows go quiet — but ONLY where every row in the block carries
            # the same date. Where they differ, the hoist is refused and every row keeps
            # its own line: an OBSERVED date is this house's record of its own knowing,
            # and a summary that averaged two of them would be a blurred tier bought with
            # ink. The condition is checked here, per block, every build.
            "seen_all": seen_all(rows) if CUTS else None,
            "rows": [
                dict(r, seen="") if CUTS and seen_all(rows) else r for r in rows
            ],
        })

    # ── THE ARRIVAL — owed item (k), and the first thing this page DOES. ──────────────
    #
    # Session 79 measured this face's opening sentence for the first time, with an
    # instrument rather than an instruction (`render.mjs --stop-after`), and it failed
    # 0 of 2 against a frozen mark of 2 of 2: both severed readers got the lateness and
    # NEITHER named the mechanism, and both read the page as being about ships that were
    # PRESENT on the day. Under the rule frozen before those answers existed, owed item
    # (k) stopped being a question about sentences and became one about form: *what does
    # this page do to a stranger before it tells them anything?*
    #
    # This is the answer, and it is not a fourth rewrite of the lede. The subject of this
    # work is a DELAY IN KNOWING, and a page of prose can only assert a delay. So the day
    # is run forward instead: the question stays fixed on 4 August 2026 while the list
    # answering it moves, list by list, through the five editions this record holds — and
    # the count of ships climbs while the day it describes stays finished. A reader
    # watches a past day get bigger before a word of the page has explained anything.
    #
    # Not one figure here is new and not one is typed. Every stop is a block of `field`
    # above — the same OBSERVED grouping the page has printed for weeks — with a running
    # total taken across it. The head therefore cannot disagree with the body: they are
    # one computation. Each stop is reproducible by a stranger with one command, which the
    # block prints BESIDE THE STOP rather than asking to be believed.
    #
    # THE COMMAND IS PER-STOP AND ITS ARGUMENT IS AN INSTANT, and both of those are
    # `VERIFIER-80.md` D2, which caught this line the same night it was written. The first
    # draft printed one command and invited a stranger to substitute the dates from the
    # head's own buttons. NOT ONE OF THE FIVE STOPS CHECKS OUT THAT WAY: `day.py --as-of`
    # compares against a capture's FETCH INSTANT, and every edition is captured the
    # following day, so two of the five exit non-zero and three silently return the
    # PREVIOUS stop's total. Nor is it fixable by shifting the date a day — the editions of
    # 4 and 5 August were both captured on 5 August, so no date-only argument can ever
    # isolate stop 0. A page whose published refutation of its own takedown is *the number
    # is checkable against a committed record* had put a command on its face that checked
    # nothing. The instant is the fetch time of the earliest saved copy carrying that
    # stop's list, read off the captures, never typed.
    #
    # TIERS, and this is `VERIFIER-80.md` D3. The grouping is OBSERVED — which saved copy
    # first carried a name is this house's measurement of its own record. But WHETHER A
    # NAME BELONGS TO THIS DAY AT ALL IS DERIVED, from a return published only as a
    # week-wide band. The first draft stamped the whole block OBSERVED without
    # qualification, and stood it ABOVE the page's own legend, where a stranger gets a mark
    # and no key. Both tiers are named here now, the gate first.
    # THE RESTAGING OF SESSION 81, and it is `DRAMATURG-80.md` §5 verbatim: *make the
    # no-motion reader's state step 0, not step 4, and let the run's fifth beat be the
    # share falling rather than the count landing.* That memo was written on the finished
    # object without sight of any answer, and the panel it could not see then produced the
    # same reading it had predicted from the form alone — both severed readers took a page
    # about ships that switch themselves OFF to be about ships at sea, because the head
    # animated names switching themselves ON. Its diagnosis, unedited: *"an accretion loop
    # indistinguishable from a progress bar, which finishes at twenty and thereby tells the
    # stranger that the day is now fully known"* — the precise inverse of this page's floor
    # line.
    #
    # So the number that runs is no longer the count. It is the SHARE, and it falls. The
    # numerator is fixed for ever at what the list dated 4 August held; every later list can
    # only enlarge the denominator; so the one figure that moves in this head moves DOWN,
    # and it is the same figure the body of this page publishes and strikes. Head and body
    # remain one computation: the figure is built by `share_line`, the same function that
    # builds the two rows of the law below, so the head cannot drift from the face.
    #
    # The names are split in two, and the split is TEXT and not paint (banked failures 12
    # and 15 — a correction that reached the eye and not the ear, then one with the senses
    # swapped). One block is what the day itself held; the other is headed by what it is —
    # names no one could have had on the day — so the growing block reads as the measure of
    # a hole and not as a progress bar filling. At stop 0 the second block does not exist.
    arrive_stops = []
    running = 0
    for g in field:
        running += g["count"]
        late = g["days_after"]
        as_of = min(seen_at[r["name"]]["first_seen_utc"] for r in g["rows"])
        # The state of the record AT this stop, re-run through the same analysis the page
        # uses rather than asserted — `VERIFIER-80.md` D2, second half: a stranger told to
        # check a bare `11` against `day.py` meets `0–11 (certain–possible)` and has to be
        # told which end they are looking at. Nothing here is typed; the nought in
        # particular is computed, as everywhere else on this face.
        a_st = analyse(DAY, load(CAPTURES, as_of=as_of))
        st = a_st["vessels_dark_on_day"]["band"]
        sh = share_line(a_st, "LIVE")
        arrive_stops.append({
            "as_of": as_of,
            # Kept in the data island and printed on the face nowhere since tonight (see
            # the cut of owed item (m) below): the stop's own as-of instant, in the form
            # that reproduces it, for this house's instruments and for anyone reading the
            # committed source.
            "check": f"python3 projects/season1/capture/day.py {DAY} --as-of {as_of}",
            "edition": g["edition"],
            # The stop buttons are labelled by LATENESS since tonight, and the reason is
            # `DRAMATURG-80.md` §1: they read `4 AUG … 8 AUG` under a title reading
            # `4 AUGUST 2026`, so the same string meant the day-being-held-open at the top
            # and the edition-doing-the-holding forty pixels lower — *"to a stranger the
            # row reads as a date picker: pick a day, see its ships"*, which is session
            # 79's and 80's misreading rebuilt in hardware at the exact joint where the
            # mechanism lives. A row of lags cannot be a date picker, and it says the
            # delay in the one place a reader's hand goes first. The edition itself is not
            # lost: it is named in the line under the figure, and its instant is in the
            # command beside it.
            "printed": (
                "ON THE DAY" if late == 0
                else f"+{late} DAY" if late == 1
                else f"+{late} DAYS"
            ),
            "days_after": late,
            "total": running,
            "share": sh["figure"],
            "added": [{"name": r["name"], "flag": r["flag"]} for r in g["rows"]],
            # The count is CUMULATIVE, so the line under it may not name one list as
            # having produced it. The first draft of this block read "named by the list
            # dated 8 AUG" over a total of twenty, and the list of 8 August named three:
            # a sentence that was true of the number's last increment and false of the
            # number. "Counting the lists up to" is the accumulation the total actually
            # is, and it stays true at every stop including the first.
            #
            # The last stop, and only the last, says which end of the figure moves. That
            # is `DRAMATURG-80.md` §2: *"the run has an ending only in the sense that it
            # has a last frame."* An ending is a sentence about direction, and it may not
            # be spatial — "the left-hand number" is a fact for the eye and nothing at all
            # for the ear (banked failure 12).
            "when": (
                f"of {DAY_PRINTED}’s darkness was knowable on the day itself, "
                f"counting the lists up to {short_caps(g['edition'])}"
                + ("." if late == 0 else
                   f", {'a day' if late == 1 else word(late) + ' days'} after the day had "
                   "ended.")
                # The fraction that produced the figure is NOT repeated here. Three severed
                # readers of session 73 named the notation `11 of 0–16` the hardest thing
                # on this page, and its gloss lives in the body — a head truncated above
                # that gloss may not carry the notation it explains. Both of its numbers
                # stand in the two block headings below, in words.
            ),
            # OWED ITEM (p), second limb. Until tonight this heading did not exist at the
            # first stop, so the room the page reserves for it — the repair that stopped the
            # buttons walking 136 px down the page — stood as about three rows of nothing
            # above the controls, readable as the shape of the hole OR as a page that failed
            # to load. It is now labelled from the first stop: the emptiness is the day's own
            # answer to this work's question, and a stranger is told so rather than left to
            # guess. Nothing is drawn in it; this house's rule is text and not paint.
            "heading_since": (
                "NAMED ONLY BY LATER LISTS — nothing yet. The space below is the part of "
                "this day that nobody could have had on it."
                if late == 0 else
                f"NAMED ONLY BY LATER LISTS — {word(running - arrive_stops[0]['total'])} "
                f"ship{'' if running - arrive_stops[0]['total'] == 1 else 's'} dark on "
                "that same day that nobody could have had on it"
            ),
        })
    n_stops = len(arrive_stops)
    last_late = arrive_stops[-1]["days_after"]
    arrive_stops[-1]["when"] += (
        " Only the lower end has moved, and the next list can only lower it again."
    )
    arrive = {
        # NOT "ships dark on 4 August 2026", which is what this line said in its first
        # draft and which the page's own body denies four inches lower: of these names
        # not one is CERTAINLY dark on this day, because a list gives a return only as a
        # week-wide band. A head asserting a certainty the body retracts is a blurred
        # tier — this house's cardinal sin — and it would have been the largest one on
        # this face, at the top of it. The count is a count of what the lists have put
        # into the day; that is an OBSERVED fact about the record, and it is what the
        # number under this line actually is.
        # THE QUESTION, NOT THE SHIPS. Until tonight this line began with the word SHIPS,
        # and the whole measured failure of sessions 79 and 80 is a reader carrying away
        # ships. The subject of this work is not a fleet; it is how much of one finished
        # day was knowable while it was still happening. The line is a question that does
        # not move while everything under it does — which is the one thing the running head
        # was built to stage, and it was staged with the wrong noun at the top of it.
        "subject": f"HOW MUCH OF {DAY_PRINTED} WAS KNOWABLE ON {DAY_PRINTED}",
        # The whole 0-of-2 of session 79 was a reader taking this page to be about ships
        # that were PRESENT. The word carrying the subject is glossed where it first
        # appears, in the page's own terms and no further: no claim of intent is made
        # here, because upstream makes none — "intentional" is a machine estimate, a
        # probability and not proof, and the restraint travels with the material. The
        # second sentence carries the band, and its count is a BRANCH on the computed
        # certain-end, never a literal nought.
        # OWED ITEM (n), banked by session 80 on one reader and paid here: this head named
        # "the lists" ten times and never once said whose they were — the unresolved
        # successor to "this record", which two readers had named the night before. The
        # owner is named at the first appearance of the word and nowhere else, because a
        # possessive repeated down a block is the repetition item (l) was written against.
        # OWED ITEM (o), banked by session 81 on two readers and paid here: the head named
        # its source and never said what KIND of thing it is. Both severed readers, asked
        # what they could not resolve, went straight at it — naming the owner had bought a
        # better question, not a resolved one. It now says what the thing IS, and the
        # sentence that says so carries the mechanism: a register that can name a ship only
        # once it has come back. That is the clause three panels failed to carry, and it now
        # stands in the PREMISE rather than only in the caption below the run.
        "subject_gloss": (
            "dark — the ship's AIS transponder switched off, so it stops being tracked. "
            "The lists below are the daily editions of The Ghost Fleet, a public register "
            "of such disappearances published at frankbueltge.de, which can name a ship "
            "only once it has come back."
        ),
        # The hedge that stood in the premise until tonight moves DOWN to the names it
        # qualifies. It was never about the figure; it is about whether a given name belongs
        # to this day, and a caveat reads at equal prominence beside its own material. It
        # also bought the room the sentence above needed: `DRAMATURG-81.md` §1 found the
        # premise four dense lines long and the run outrunning it.
        "hedge": (
            "A list gives a ship's return only to the nearest week, so "
            + (
                "not one of these names is certainly dark on this day."
                if now["vessels_dark_on_day"]["band"][0] == 0 else
                f"{word(now['vessels_dark_on_day']['band'][0])} of these names are "
                "certainly dark on this day and the rest are possible."
            )
        ),
        # The first block's heading is constant across every stop, because its count is:
        # the numerator of this work's figure cannot grow, and a heading that never moves
        # while the one under it does is the fixed point the run turns on.
        "heading_then": (
            f"IN THE LIST DATED {short_caps(DAY)} — {word(field[0]['count'])} ships, "
            "all that the day held about itself"
        ),
        "stops": arrive_stops,
        # The mechanism, said once, under the thing that has just enacted it. The word
        # order matters: the reason comes first, so a reader who arrives after the run
        # has finished still gets why the number moved.
        "caption": (
            "A ship reaches the list only after it comes back, so a day that is over "
            f"keeps being answered. {word(n_stops).capitalize()} lists, "
            f"{word(n_stops)} answers, one day — the last of them "
            f"{'a day' if last_late == 1 else word(last_late) + ' days'} after the day "
            f"had ended. The {word(field[0]['count'])} names the day itself held cannot "
            "grow; every list since has only made the day larger underneath them. That is "
            "why the figure above falls, and why it can only go on falling."
            # It said "Twenty is today's answer" until this line was looked at against a
            # frame of the running head at its FIRST stop, where the count reads eleven.
            # A caption that stands under a moving number may not name one of the
            # number's values, or the page contradicts itself for four seconds of every
            # visit — and the frame is how that was caught, not the reading of the string.
        ),
        # OWED ITEM (m), CUT TONIGHT after four sessions of standing. What stood here was
        # the head's own tier line and, after it, the command reproducing the stop being
        # looked at. Four voices asked for it: session 79's reader called it a developer
        # note, both of session 80's put a finger on it without being able to say why —
        # and `VERIFIER-80.md` then found they were right for a reason none of them could
        # see, the command reproducing none of the five stops it stood over —
        # and `DRAMATURG-81.md` §3 named the cut outright: *"a stranger meeting the head's
        # version gets an unglossed command line whose only variable, across six frames, is
        # a timestamp ticking forward — which nobody reads as evidence in 1.6 seconds; it
        # reads as noise that happens to look rigorous."*
        #
        # WHAT IS LOST, written here and not softened: the head loses its receipts for a
        # visitor who never scrolls. This work's published takedown — *"a studio watched a
        # website update for a month and called its own patience a measurement"* — is
        # refuted by a number a stranger can re-run, and that refutation now begins one
        # scroll below the fold. It is not deleted: the tier legend, the three commands,
        # the verbatim output of one of them and the table of every saved copy all stand in
        # the body, which is where session 79's own measurement found both readers reaching
        # when asked how they would check a number (owed item (l)). The head keeps the
        # plain-language sentence the receipts were decorating.
        #
        # `check` survives on every stop for the page's own instruments and is printed
        # nowhere on the face; the body's commands are built from the record, not from it.
        #
        # WHAT THE CUT TOOK WITH IT, AND WHAT HAD TO GO BACK THE SAME NIGHT. The deleted
        # paragraph was the only text on the face marking the SHARE as DERIVED — the page's
        # legend marks the dark-and-return spans and not the figure — so for one build this
        # work's largest number stood on its own face with no tier word anywhere near it,
        # which is this house's cardinal sin committed by subtraction. Found by the verifying
        # pass, blocking, the night the cut was made. The line below is what went back: one
        # sentence, no command, and self-contained, because a tier mark whose key is 400 px
        # further down is a mark the head's own reader cannot read. It also pays what the
        # staging voice asked for in the same breath — *"the head no longer says anywhere
        # that this page is reading saved copies … six words would fix it"* — so the mark and
        # the evidence arrive in the same clause instead of as two additions.
        "tier": (
            "DERIVED — this share is worked out here, from saved copies of those lists. "
            "Nobody publishes it."
        ),
        # The upstream restraint, and it travels with the NAMES. This block names twenty
        # vessels and their flags and stands above the foot that has always carried this
        # sentence — and in the material actually dispatched to session 80's readers,
        # truncated at this block, the foot did not exist at all (`VERIFIER-80.md` D3,
        # note b). One string, used here and in the foot, so the two cannot drift.
        "restraint": RESTRAINT,
        "replay": "run it again",
    }
    # OWED ITEM (p), first limb. `DRAMATURG-81.md` §5: *"use the freed first beat to hold
    # state 0 long enough that the definition paragraph is legible before the number first
    # moves."* The run stepped every 1.6 s from load, so the premise was still being read
    # when the figure it explains began to fall — §1's finding, and the plainest available
    # explanation of why two panels got the lateness and missed the mechanism.
    #
    # The beat is DERIVED and not chosen: the gloss's own word count divided by the mean
    # adult silent-reading rate for non-fiction English, 238 wpm, from the meta-analysis of
    # 190 studies and 18,573 participants in Marc Brysbaert, "How many words do we read per
    # minute? A review and meta-analysis of reading rate", Journal of Memory and Language
    # 109 (2019) — <https://biblio.ugent.be/publication/8647789>. SOURCED. The caveat
    # travels with the figure and is not softened: 238 is a MEAN, the same paper puts most
    # adults between 175 and 300 wpm and reports slower rates for children, older adults and
    # non-native English readers — so this beat is too short for a large share of the people
    # it is set for, and every one of them still has six buttons and no clock.
    #
    # Only the FIRST beat is derived. The rest stay at 1.6 s: they carry no new prose, and a
    # run whose every step waited out a reading rate would not be a run.
    #
    # THE COUNT IS OF WORDS AND NOT OF TOKENS, and it was not on its first run. `.split()`
    # returned 44 for this paragraph, of which one was a bare em dash — so the page published
    # "44 words" of a 43-word sentence and held its first beat 252 ms too long. Caught by the
    # verifying pass on the night it was built. It is banked failure 8 again, in its purest
    # form: a number reaching a face out of a library call nobody had put beside the thing it
    # counts. A word here is a token with a letter or a digit in it.
    gloss_words = sum(1 for t in arrive["subject_gloss"].split() if any(c.isalnum() for c in t))
    arrive["first_dwell_ms"] = round(gloss_words / 238 * 60 * 1000)
    arrive["first_dwell_note"] = (
        f"{gloss_words} words at 238 wpm (Brysbaert 2019, mean adult silent reading of "
        "non-fiction English)"
    )

    # what moved since the struck figure was true: the vessels this day gained from
    # captures later than the law's publication, named, with the list that carried them
    then_names = {e["name"] for e in then["certain"] + then["possible"]}
    gained = [e for e in now["certain"] + now["possible"] if e["name"] not in then_names]
    gained.sort(key=lambda e: -e["days_dark"])
    gained_eds = sorted({seen_at[e["name"]]["first_edition_date"] for e in gained})
    # The fall itself, in points, between the two figures — DRAMATURG-76 §2: the page had
    # the event of a number falling and staged it as two rows of bookkeeping, leaving the
    # reader to subtract 69 from 65 across two lines that both end "–100 %". The drop is
    # computed from the two analyses, never typed, and it branches on nought: a session
    # that adds a copy and no list must not print a fall that did not happen.
    drop = round(then["share_knowable_OBSERVED"][0] * 100) - round(
        now["share_knowable_OBSERVED"][0] * 100
    )
    fell = (
        f"It fell {word(drop)} point{'' if drop == 1 else 's'}. "
        if drop > 0 else
        "It has not moved since. "
    )
    # Each ship named against ITS OWN list and ITS OWN lag. Until session 78 this sentence
    # joined every gained list with "and" and then printed a single lag — the earliest —
    # for all of them, which was true only while the gained ships happened to share one
    # list. Tonight they do not: one arrived on the seventh, three on the eighth, and the
    # old sentence would have printed all four as "three days after the day". It was never
    # false on this face; it was one list away from being false, which is not a property to
    # leave in a sentence that carries the work's turn.
    by_ed = {}
    for e in gained:
        by_ed.setdefault(seen_at[e["name"]]["first_edition_date"], []).append(e["name"])

    def series(xs):
        """'A', 'A and B', 'A, B and C' — the page's own joiner, never a trailing 'and'."""
        return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]

    clauses = []
    for ed in gained_eds:
        late = (d(ed) - target).days
        clauses.append(
            f"{series(by_ed[ed])} with the list of {short_caps(ed)}, "
            f"{word(late)} day{'' if late == 1 else 's'} after the day"
        )
    # Semicolons between the clauses, because each clause already carries a comma before
    # its lag: "…7 AUG, three days after the day and TUNA PESCA…" reads as one list of
    # four things rather than two groups of ships.
    moved = (
        fell
        + "What grew was the total: "
        + (clauses[0] if len(clauses) == 1
           else "; ".join(clauses[:-1]) + "; and " + clauses[-1])
        + f" — {word(len(gained))} ship{'' if len(gained) == 1 else 's'} this record did "
        + "not hold when the law below was printed."
    )

    # The first sentence a cold reader meets, and the whole work if they read no further
    # (DRAMATURG-72 §B.1). Every number in it is counted here, none typed: the numerator
    # this record observes, what the later lists added, and how much of that arrived after
    # the figure below had already been published.
    n_obs = now["knowable_on_the_day_OBSERVED"]
    n_hi = now["vessels_dark_on_day"]["band"][1]
    # "the list published on the day itself" claimed a publication event this record never
    # observed: the earliest saved copy is from the following morning, and upstream prints a
    # date, not a publication instant (VERIFIER-72 D3). The list is DATED the day; that is
    # what the record holds, and that is now what the sentence says.
    #
    # And the day is NAMED here, twice, since session 73 (DRAMATURG-73 §A). Until tonight this
    # sentence said "that day" and "the day itself": the sentence built to carry the work was
    # anaphoric to a word it did not contain, pointing up to the headline, which is the first
    # thing an unaided recall drops. 72's Q1 was refuted at 2 of 3 on exactly that — one reader
    # carried the whole mechanism away and no date. The date is written where the anaphor stood,
    # and named a second time because a word carried once in a subordinate clause is what a
    # rebuilt sentence loses. Both namings are computed from DAY, like every other date here.
    #
    # OWED ITEM (k), and the arm this session puts to readers. The committed lede below has
    # now been measured broken twice — session 77 rebuilt the head ABOVE it and the change
    # was refuted 1 of 2, while the control it was tested against scored 0 of 2. The
    # Dramaturg's diagnosis of why (DRAMATURG-77 §1) is the one thing both panels agreed
    # with: *"The head is not broken in its order. It is broken in its referents."* Its two
    # sentences ask a cold reader to hold four things the page has not yet given them —
    # THIS RECORD, CAN PLACE IN, THE LIST DATED 4 AUGUST, ITS FIGURE — which is why hoisting
    # a good sentence over them changed nothing, and why a control reader summarised the
    # whole page as "a record of ships for August 4, 2026". That reading is faithful to the
    # sentence, not a failure of the reader.
    #
    # So this arm does not move a word of the page's order. It spends one sentence earning
    # the terms before the numbers arrive: what going dark IS, what the list IS, and why the
    # list is late. Nothing else on the face differs between the arms.
    ledes = {
        "committed": (
            f"{word(n_obs).capitalize()} of the ships this record can place in "
            f"{printed_date(DAY)} stood in the list dated {day_month(DAY)} itself. "
            f"{word(n_hi - n_obs).capitalize()} arrived later — {word(len(gained))} of them "
            "after this page had printed its figure."
        ),
        "earned": (
            "A ship that switches off its transponder disappears from the public map of the "
            "sea, and the daily list that reports it prints nothing until the ship comes "
            f"back. {word(n_obs).capitalize()} such ships were named on the list dated "
            f"{printed_date(DAY)}. {word(n_hi - n_obs).capitalize()} more, dark on that same "
            f"day, were named only by lists that came after it — {word(len(gained))} of them "
            "since this page printed the figure below."
        ),
    }
    lede = ledes[LEDE]

    # One list, more than one saved copy of it, and the copies differing in bytes: the
    # correction session 70 published on this face, in the plain words §A ordered.
    bodies_per_list = {}
    for c in caps_now:
        bodies_per_list.setdefault(content_sha256(c), set()).add(c["fetch"]["sha256"])
    split = {k: len(v) for k, v in bodies_per_list.items() if len(v) > 1}
    if split:
        n_lists, n_bodies = len(split), max(split.values())
        ledger_caption = (
            f"{word(n_lists).capitalize()} list came back in {word(n_bodies)} different sets of "
            f"bytes while every field this page reads stayed identical"
            if n_lists == 1 else
            f"{word(n_lists).capitalize()} lists came back in more than one set of bytes each "
            f"while every field this page reads stayed identical"
        ) + " — a copy's fingerprint is not the list's identity, which is why the table carries both."
    else:
        ledger_caption = (
            "Every saved copy of a list came back in identical bytes — a copy's fingerprint is "
            "not the list's identity, which is why the table carries both."
        )

    # Owed item (d), reported by two panels: the last column falls, and it stands four
    # inches under a quotation saying a night can never remove a ship. Both readings were
    # right about the page and wrong about the world — the column counts a LIST, and every
    # list holds only its own seven days. Neither the column nor the quotation moves; what
    # was missing was the sentence that lets them stand together.
    ledger_caption += (
        " The last column counts the ships in each saved list, not the ships this page can "
        f"place in {printed_date(DAY)}: every list holds only the "
        f"{word(caps_now[-1]['method']['window_days'])} days before its own date, so a ship "
        "leaves the list as that window moves past it. It never leaves the day."
    )

    ledger = []
    for c in caps_now:
        ledger.append({
            "fetched_at_utc": c["fetch"]["fetched_at_utc"],
            "http_status": c["fetch"]["http_status"],
            "bytes": c["fetch"]["bytes"],
            "sha256": c["fetch"]["sha256"][:8],
            "content_sha256": content_sha256(c)[:8],
            "edition_date_printed": c["edition_date_printed"],
            "vessels": len(c.get("vessels", [])),
        })

    return {
        "day": {"iso": DAY, "printed": DAY_PRINTED},
        "method": {
            "source": "https://frankbueltge.de/werke/ghost-fleet/",
            "edition_source": "https://frankbueltge.de/ghost-fleet/",
            "window_quote": caps_now[-1]["method"]["window_quote"],
            "definition_quote": DEFINITION_QUOTE,
            "definition": DEFINITION,
            "restraint": RESTRAINT,
        },
        "arrive": arrive,
        "lede": lede,
        "field": field,
        "fall": {
            "then": share_line(then, "SUPERSEDED"),
            "now": share_line(now, "LIVE"),
            "as_of": published_as_of,
            "band": band_line(now, caps_now),
            "held": (
                f"The {word(now['knowable_on_the_day_OBSERVED'])} did not move, and cannot. No "
                "later night can put a name into a list that did not carry it."
            ),
            "moved": moved,
            "published": (
                "A ceiling that can only fall. A further night can add a ship to a past day. It "
                "can never remove one, and it can never put a name into an edition that did not "
                "carry it."
            ),
            # Dated to the commit that first carried THIS sentence, not to an earlier,
            # differently-worded ancestor of it. The Verifier's blocking pass in session 71
            # caught the earlier claim ("and in this record since 5 August") as false by a
            # full day: the ancestor said the share can only fall, but it is not this
            # sentence, and a quotation may not borrow its ancestor's date.
            "published_when": (
                f"printed on this page {printed_date(pub.date().isoformat())} at "
                f"{pub.strftime('%H:%M')} UTC, in commit {PUBLISHED_COMMIT} — before the "
                "capture that made it fall"
            ),
            "then_published": f"at {pub.strftime('%H:%M')} UTC on {pub.day} {FULL_MONTHS[pub.month - 1]}",
        },
        "ledger": {"rows": ledger, "caption": ledger_caption},
        # The command carries its own truncation, so that what stands under "verbatim,
        # unedited" is the whole output of the command as printed. Sixteen per-ship lines
        # restated the rows above in worse type (DRAMATURG-72 §B.6); the pipe cuts them
        # where a reader would, and day.py handles the closed pipe without a traceback.
        "commands": [
            {"label": "the day", "cmd": f"python3 projects/season1/capture/day.py {DAY} | head -6"},
            {"label": "every ship, and when it arrived",
             "cmd": f"python3 projects/season1/capture/day.py {DAY}"},
            {"label": "the night before",
             "cmd": f"python3 projects/season1/capture/day.py {DAY} --as-of {published_as_of}"},
        ],
        "output": "".join(run_day().splitlines(keepends=True)[:6]),
        "floor": (
            f"No number closes this. A method that counts a disappearance only when the ship comes "
            f"back cannot see the ships that never come back. "
            f"{word(now['vessels_dark_on_day']['band'][1]).capitalize()} is what this record can "
            f"place in {printed_date(DAY)}, not what was on the sea that day."
        ),
    }


ISLAND = re.compile(
    r'(<script type="application/json" id="sd-data">\n)(.*?)(\n  </script>)', re.S
)


def main():
    global LEDE, CUTS
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--lede", choices=sorted(("committed", "earned")), default=LEDE,
                    help="which lede to build (session 78's A/B; default: the committed one)")
    ap.add_argument("--no-cuts", action="store_true",
                    help="rebuild the shape session 79's reading superseded: the OBSERVED "
                         "line printed on every row instead of once per block")
    ap.add_argument("--into", default=None,
                    help="write the island into this index.html instead of the work's own")
    a = ap.parse_args()
    LEDE = a.lede
    CUTS = not a.no_cuts
    blob = json.dumps(build(), indent=2, ensure_ascii=False)
    path = a.into or os.path.join(HERE, "index.html")
    if a.check or a.write:
        with open(path, encoding="utf-8") as f:
            html = f.read()
        m = ISLAND.search(html)
        if not m:
            print("no data island found in index.html", file=sys.stderr)
            return 2
        if a.check:
            same = json.loads(m.group(2)) == json.loads(blob)
            print("island matches the captures" if same else "ISLAND DIFFERS from the captures")
            return 0 if same else 1
        with open(path, "w", encoding="utf-8") as f:
            f.write(html[:m.start(2)] + blob + html[m.end(2):])
        print(f"island written: {len(blob)} bytes")
        return 0
    print(blob)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
