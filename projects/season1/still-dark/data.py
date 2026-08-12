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
_UNITS = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
          "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
          "seventeen", "eighteen", "nineteen"]
_TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
         "ninety"]
# BUILT, NOT TYPED, SINCE SESSION 84 — and the reason is that the typed version's own
# comment predicted tonight. It read: *"The list stopped at sixteen until session 78, so
# the night the total reached seventeen the band sentence started a sentence with a numeral
# while saying 'eleven' four words later — one sentence in two voices, and nothing failed.
# Extended to twenty; when the total passes twenty this will do it again."* It was extended
# to thirty instead, and tonight the total reached THIRTY-ONE — so the page printed "31
# ships could have been dark" beside "the eleven the day itself named", in one sentence, in
# two voices, and nothing failed again. A ceiling a hand has to raise is banked failure 17
# in another costume: a constant advanced by hand is a number typed by hand wearing a
# variable's name. The table now covers every count this work can reach and stops being a
# thing anyone must remember.
WORDS = {n: _UNITS[n] for n in range(20)}
for _t in range(2, 10):
    WORDS[_t * 10] = _TENS[_t]
    for _u in range(1, 10):
        WORDS[_t * 10 + _u] = f"{_TENS[_t]}-{_UNITS[_u]}"
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
        # The two ends, apart, from the same arithmetic that builds the joined string —
        # session 83, the staging voice's own one change, banked verbatim in 82 and taken
        # here: *"one figure falls 56 points while the other cannot move at all … the
        # piece's actual subject … on screen for eighteen seconds, and nothing marks it."*
        # They are split HERE and not in the browser, so no instrument of this house can
        # be shown a figure the page did not compute.
        "figure_falling": f"{round(lo * 100)} %",
        "figure_fixed": f"–{round(hi * 100)} %",
        # THE FRACTION EACH END IS, session 88, and it is the whole of tonight's build.
        # `DRAMATURG-87.md:105-110` returned its own prescription after this house built it
        # to the letter: *"Placement was never the problem; units were … the falling figure
        # must print its own fraction, not only its percentage, so that the run shows
        # `11 of 11 → 11 of 33` while `11 of 230` stands underneath."* The line range is the
        # quotation's own and not the ruling's nearest restatement: this comment cited
        # `:402` for one night, where the same voice says the same thing in different words
        # and none of the quoted text stands, and a reader sent to a line that does not hold
        # what the marks promise has been misdirected by a citation
        # (`VERIFIER-88.md` §7). The two figures in the frame shared no TERM at any of the
        # eight stops — not one of them printed `11`, and not one printed a denominator —
        # so the relation between them was carried entirely by an 11.52 px sentence. These are the
        # same two quotients `day.py` divides to get the percentages above — `obs / hi` and
        # `obs / max(lo, obs)` — written as the divisions they are, and split HERE, so no
        # face of this work can print a fraction the record did not compute.
        "fraction_falling": f"{n} of {b[1]}",
        "fraction_fixed": f"{n} of {max(b[0], n)}",
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

    # ── THE CUT — owed item (A), the largest thing this work has ever owed. ───────────
    #
    # Every capture this record holds carries an `aggregates` block. `capture/capture.py`
    # has parsed it since the first night, `capture/README.md` tiers it SOURCED, and no
    # face of this work has ever printed one number of it. The list dated 4 August prints
    # eleven names and says, in the same page, that it examined 230 disappearances out of
    # 5,641 events in its window. The heading over those eleven names called them "all
    # that the day held about itself" for nineteen sessions.
    #
    # That heading was false against bytes this house saved itself, and the art critic of
    # session 84 found it by opening the captures and asking the one question five severed
    # panels, three blocking voices and four instruments had never asked: not *does the
    # page agree with the captures*, but *what are the captures a sample of*. The answer
    # is a top-of-list display. Every list this record reads prints six to eleven names of
    # the couple of hundred it says it examined, and the share this work publishes is
    # therefore computed over a cut whose size is chosen upstream.
    #
    # WHAT IS COMPUTED HERE AND WHAT IS REFUSED. The figures are SOURCED, read off the
    # saved copies, never typed. The one thing this block does NOT do is say which way the
    # share would move if the lists were longer. `KRITIKER-84.md` §2 states that doubling
    # the list length roughly halves the figure; this house cannot check that and does not
    # adopt it. Both ends of the quotient would grow — a longer list dated 4 August could
    # carry names the numerator does not have, and longer later lists add to the total —
    # and nothing in this record measures by how much. Banked failures 31 and 33 were both
    # well-put sentences about arithmetic that nobody ran. This is the third such sentence
    # in three sessions and it is being refused rather than written.
    #
    # THE TWO EARLIER COPIES OF THE 10 AUGUST LIST HOLD TEN NAMES AND TONIGHT'S HOLDS
    # ELEVEN, and the names printed per edition below are the UNION over that edition's
    # copies for exactly that reason: the eleventh was lost to this house's own regex and
    # recovered at the gate of session 84 (banked failure 34). The captures are immutable
    # and are not rewritten; the union is how a repaired parser reaches an edition it read
    # wrong, and it is named here rather than smoothed away.
    editions = sorted({c["edition_date"] for c in caps_now})
    cut_rows = []
    for ed in editions:
        copies = [c for c in caps_now if c["edition_date"] == ed]
        names = {v["name"] for c in copies for v in c.get("vessels", [])}
        aggs = {json.dumps(c.get("aggregates"), sort_keys=True) for c in copies}
        # An assumption this house has not checked is an assumption this house has been
        # burned by. The aggregates of one edition are identical across its copies in the
        # record as it stands; if a night ever breaks that, the build stops rather than
        # picking a copy.
        if len(aggs) != 1:
            raise SystemExit(
                f"aggregates differ between saved copies of the list dated {ed}: {aggs}"
            )
        agg = copies[0]["aggregates"]
        cut_rows.append({
            "edition": ed,
            "printed": len(names),
            "examined": agg["disappearances_examined"],
            "in_window": agg["in_the_window"],
            "dark_inside_national_waters": agg["dark_inside_national_waters"],
            "vessel_days": agg["vessel_days_of_darkness_approx"],
            "copies": len(copies),
        })
    day_cut = next(r for r in cut_rows if r["edition"] == DAY)

    # THE TWENTY THAT ARRIVED LATER, AND WHAT THIS RECORD CANNOT SAY ABOUT THEM. A name
    # this house first saw in a later list is a name that COULD have stood in the list of
    # the day itself: the end of a dark interval is published only as "within the last 7
    # days", so a name added by the list of 10 August has an end band reaching back to
    # 3 August. Where that band reaches the day, the record cannot tell a ship that came
    # back later from a ship the list did not print.
    #
    # THE STRUCTURAL PART IS SAID ON THE FACE AND NOT LEFT AS A FINDING. This is 20 of 20
    # tonight partly because every list so far is dated within the window's own length of
    # the day — the first edition whose additions could be ruled out of it is one dated
    # 12 August. That sentence is printed beside the count, because a number that must
    # come out this way until a given date is not evidence until that date has passed.
    window_days = caps_now[-1]["method"]["window_days"]
    later = [e for e in now["certain"] + now["possible"]
             if seen_at[e["name"]]["first_edition_date"] != DAY]
    not_ruled_out = [e for e in later if bands(seen_at[e["name"]])[0] <= d(DAY)]
    first_excluding = d(DAY) + datetime.timedelta(days=window_days + 1)

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
        # THE STOP IS THE INSTANT THIS RECORD HAD READ THE WHOLE OF THAT LIST, AND UNTIL
        # SESSION 85 IT WAS THE INSTANT IT HAD READ ANY OF IT — a one-word difference that
        # put two different numbers for one state on this face. `min` gave the last stop an
        # as-of of 17:47 on 10 August, when this record held ten names of that list, because
        # the eleventh was still lost inside this house's own regex (banked failure 34) and
        # entered at 22:41. So the run ended on `37 %–100 %` — the share of a total of
        # thirty — under a block of thirty-one chips, while the body of the same page
        # published `35 %–100 %, 11 of 0–31`. Both numbers were honestly computed and one
        # page cannot carry both. Found by the conductor tonight, on the built object,
        # while looking at something else; it shipped in session 84 and stood at HEAD.
        #
        # `max` is the right instant and not merely the convenient one: every stop already
        # claims to be the record as it stood when that list had arrived, and a list this
        # house had read two-thirds of had not arrived here. The captures are untouched —
        # 17:47 still holds the ten names it was written with, and `--as-of 17:47` still
        # returns 37 %. What changes is which instant the run calls the arrival of a list.
        as_of = max(seen_at[r["name"]]["first_seen_utc"] for r in g["rows"])
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
            "share_falling": sh["figure_falling"],
            "share_fixed": sh["figure_fixed"],
            # The falling end, in ships, at this stop — the row that gives the run a term
            # in common with the standing figure below it. It is the only numeral in the
            # frame besides the percentage that a stop rewrites, and its numerator is the
            # same eleven at every one of them.
            "share_falling_of": sh["fraction_falling"],
            "share_fixed_of": sh["fraction_fixed"],
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
            # SPLIT IN SESSION 83, and the split is the whole point. `DRAMATURG-82.md` §3:
            # *"the head re-renders an unchanging clause 55 characters long on every beat
            # while the visitor is looking for what changed … the clause should be static
            # and only the tail should move. That is not a wording preference; it is what a
            # reader's eye needs in a 1.6 s beat."* The two pieces are joined back into
            # `when` for anything that reads one string; the browser writes only the tail.
            "when_fixed": f"of {DAY_PRINTED}’s darkness was knowable on the day itself,",
            "when_tail": (
                f"counting the lists up to {short_caps(g['edition'])}"
                + ("." if late == 0 else
                   f", {'a day' if late == 1 else word(late) + ' days'} after the day had "
                   "ended.")
            ),
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
            # OWED ITEM (w), paid in session 84, and OWED ITEM (z) with it.
            #
            # (w): until tonight this heading read "N ships DARK on that same day", which
            # asserts as fact exactly what the hedge two lines below it denies — "not one
            # of these names is certainly dark on this day" — and what the band under the
            # law denies again: "Thirty ships COULD HAVE BEEN dark on 4 August 2026 and not
            # one of them certainly". A list gives a return only to the nearest week, so
            # every one of these names is possible and none is certain. The heading now
            # says what the arithmetic says, in the band's own words. `VERIFIER-83.md` 1c
            # found it; it was left standing that night on purpose, because four severed
            # readers had been scored on it hours earlier and moving material under a
            # finished reading is this house's banked failure 29.
            #
            # (z): the names a stop adds are drawn in the page's darker ink with a darker
            # border and heavier type, and the stylesheet calls them "the only thing on
            # this page that is meant to be seen changing" — while no word anywhere on the
            # face said what the mark meant. A mark the eye can read and the ear cannot is
            # banked failure 12, and its mirror is 15; this house has now committed both.
            # The repair is words, in the block's own heading, immediately before the names
            # they describe, so eye and ear get them in the same place and in the same
            # order. They name the mark twice over — by POSITION ("the last five"), which a
            # reader who cannot see ink can check by counting, and by ink, which a reader
            # who can see it is looking at.
            # THE CAVEAT BRANCHES ON THE STOP FROM SESSION 87, AND UNTIL TONIGHT IT COULD
            # NOT. It was one string in the island, written from the record's live certain
            # count and printed unchanged under all eight stops: *"two of these names are
            # certainly dark on this day"*, standing over an empty box at stop 0 under a
            # heading that reads *nothing yet*, and over names that do not include either
            # certain ship at stops 1–6. **Both voices convened tonight found it
            # independently** (`VERIFIER-87.md` §5, `DRAMATURG-87.md` §5) and the count is
            # theirs: true at one stop of eight, and the stop a reader whose machine asks
            # for no motion never leaves is one of the seven.
            #
            # It is banked failure 42 one session after 42 was banked, and it is worse than
            # 42 in one respect that this record is going to state plainly: session 86
            # repaired that failure by giving both sentences a branch on the same value, and
            # **the value was the state of the RECORD, not the state of the RUN**. A branch
            # on the record cannot be false on the night it is written and cannot be true on
            # the screen it is printed on. The stop already computes its own band; the
            # caveat now reads off that band, like every other string a stop owns.
            "hedge": (
                "A list gives a ship's return only to the nearest week, so "
                + (
                    "not one of these names is certainly dark on this day."
                    if st[0] == 0 else
                    f"{word(st[0])} of these names are certainly dark on this day and the "
                    "rest are possible."
                )
            ),
            "heading_since": (
                "NAMED ONLY BY LATER LISTS — nothing yet. The space below is the part of "
                "this day that nobody could have had on it."
                if late == 0 else
                f"NAMED ONLY BY LATER LISTS — {word(running - arrive_stops[0]['total'])} "
                f"ship{'' if running - arrive_stops[0]['total'] == 1 else 's'} that could "
                "have been dark on that same day and that nobody could have had on it. "
                + (
                    f"The last of them, in darker ink, arrived with the list of "
                    f"{short_caps(g['edition'])}."
                    if g["count"] == 1 else
                    f"The last {word(g['count'])}, in darker ink, arrived with the list "
                    f"of {short_caps(g['edition'])}."
                )
            ),
        })
    n_stops = len(arrive_stops)
    last_late = arrive_stops[-1]["days_after"]
    # THE CLAUSE UNDER THE MOVING FRACTION WAS WRITTEN AND DELETED IN ONE SESSION, and the
    # deletion is the staging voice's order, taken. It said which end the fraction was the
    # arithmetic of and named the other end — and `DRAMATURG-88.md` §§3–4 measured what that
    # cost: the 11.52 px prose in the frame went from 166 characters to 307, it re-told the
    # sentence this session had just deleted three lines below it, it printed `11 of 11`
    # twice at stop 0 meaning two different ends, and it wedged 92 px of grey between the
    # two fractions it was written to join. *"The row is worth it. The clause is not, and
    # the clause is 86 of the 104 px."* — that ruling and its accounting stand at `:235` and
    # `:258-259`, in §4, and the character counts and the 92 px in §3; this comment cited §3
    # alone for one hour, and a section number is a citation like any other
    # (`VERIFIER-88.md` R8). The 86 px is the same voice's own prescription's
    # last clause, unbuilt until now: *"the run does the arguing, and the 11.52 px sentence
    # can go"* (`DRAMATURG-87.md:109-110`).
    # `share_fixed_of` survives in the island with no consumer on the face, and that is
    # deliberate: it is the other end's own division, computed at every stop, and the next
    # session to argue about that end should read it rather than take it by hand.
    # WHAT STOOD HERE UNTIL SESSION 83, and why it went. The last stop, and only the last,
    # appended *"Only the lower end has moved, and the next list can only lower it again."*
    # `DRAMATURG-82.md` §2 ruled that sentence a turn's content staged as boilerplate: it
    # arrived as lines four and five of a paragraph four repetitions had trained the reader
    # to stop reading, in the same 1.6 s beat as the largest chip-fill of the run. It is not
    # deleted — it is promoted out of the run entirely, into the static line below, where it
    # stands from the first frame instead of for 1.6 seconds at the end.

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
        # OWED ITEMS (q), (r) AND (u), all three paid in this one sentence in session 83,
        # because all three were the same defect wearing three names: the premise said what
        # the lists ARE without saying whose they are, what they leave out, or what word
        # they are built on.
        #
        # (u) — *"a public register"* is struck. Upstream disclaims exactly the completeness
        # that phrase asserts, in its own method sheet, fetched again tonight: *"Only
        # offshore (≥ 50 nm) and well-observed: nearshore disabling is missing — so marine
        # protected areas (mostly coastal) almost never appear; what is measured is the open
        # sea."* A caveat carried by the upstream and dropped by us is the publishing
        # condition this house accepted, broken.
        #
        # (q) — three of four severed readers in 82, both arms, made Global Fishing Watch
        # the publisher of these lists. It is not: it supplies the events. The list is
        # published at frankbueltge.de and the sentence now says so before GFW is named
        # anywhere on the face.
        #
        # (r) — the word the head's own restraint line disclaims — *"intentional"* — stood
        # nowhere in the head. Upstream, verbatim: *"GFW returns only high-confidence,
        # intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore, good satellite
        # coverage."* So the word is not decoration here: it is the filter that makes these
        # lists shorter than the sea. It is anchored at its first appearance, and the
        # caveat that follows it below now has a subject on the same screen.
        "subject_gloss": (
            "dark — the ship's AIS transponder switched off, so it stops being tracked. "
            "The lists below are the daily editions of The Ghost Fleet, published at "
            "frankbueltge.de, which name a ship only once it has come back. They carry "
            "only offshore switch-offs a machine model classed as intentional, so they are "
            "never all of a day's darkness."
        ),
        # The hedge that stood in the premise until tonight moves DOWN to the names it
        # qualifies. It was never about the figure; it is about whether a given name belongs
        # to this day, and a caveat reads at equal prominence beside its own material. It
        # also bought the room the sentence above needed: `DRAMATURG-81.md` §1 found the
        # premise four dense lines long and the run outrunning it.
        # GONE FROM THE ISLAND'S TOP LEVEL IN SESSION 87, and the deletion is the repair.
        # A string written once from the record's live band and printed under eight
        # different screens is a sentence that can only be true about one of them. It now
        # belongs to the stop, above, where it is computed from that stop's own band. The
        # top-level key is not kept as a fallback: a fallback is how a wrong sentence
        # survives a repair.
        # OWED ITEM (A), SECOND LIMB — the caveat beside its own material, which is this
        # house's own publishing condition applied to itself. The block above this line is
        # the hole: names that reached this record only after the day. Once the list is
        # known to be a cut, "arrived later" stops being a fact about the sea and becomes a
        # fact this record cannot separate from "was not printed" — and the separation is
        # not merely unmeasured, it is impossible under the published window, because the
        # end of a dark interval is given only to the nearest seven days.
        #
        # THE COUNT AND ITS EXPIRY, TOGETHER. It is all of them tonight, and it must be all
        # of them until a list dated more than the window's own length after the day
        # arrives: only an edition of 12 August or later — computed below, never typed —
        # can add a name whose end band cannot reach 4 August. Printing the count without
        # that date would publish as a finding a number that arithmetic guarantees. Both
        # are computed; the branch exists because the day the date passes, the sentence has
        # to be able to say a smaller number without a hand touching it.
        "since_note": (
            # SAID SO THAT IT IS TRUE AT EVERY STOP. This line does not move between stops
            # and the block above it does: at the first stop that space is empty and says
            # so. A fixed sentence beginning "not one of these twenty names" stood over
            # nothing for the first fourteen seconds of the run — caught in the render,
            # before any voice was convened. The names are named by the stop that brings
            # them, not by a demonstrative that has nothing to point at yet.
            # THE OPENING CLAUSE PRINTED THE RUN'S OUTCOME BEFORE THE RUN, AND IS CUT.
            # `DRAMATURG-85.md` §4, measured on three loads: the sentence stood on the first
            # screen at 1400×900 from load, nine pixels under the space it describes, while
            # the heading over that space said *"nothing yet"* — the outcome legible **22.2
            # seconds before it became true**, against a first figure change at 14.2 s and a
            # twentieth chip at 22.2 s. *"The one beat this work has bought with an honest
            # premise, it spent tonight in a subordinate clause."* Forty-six of eighty-four
            # words go, and with them the third statement of the hedge in one head.
            #
            # AND THE LAST CLAUSE SAID `that day` WHERE THE COMPUTATION SAYS `that list` —
            # `VERIFIER-85.md` §2, blocking. A name ruled out of the DAY never enters this
            # block at all; the exclusion computed here is exclusion from the LIST dated
            # 4 August. The page's own ledger caption three blocks lower draws exactly that
            # line — *"a ship leaves the list as that window moves past it. It never leaves
            # the day"* — and one sentence may not erase what another spends a caption
            # drawing. One word.
            #
            # THE BRANCH STAYS. The count is all of them tonight and must be until a list
            # dated after 11 August arrives; the day it is not, this sentence has to be able
            # to say a smaller number without a hand touching it.
            "This record cannot tell a ship that came back later from a ship the list did "
            "not print: a list gives a return only to the nearest "
            f"{word(window_days)} days, so the return window of "
            + (
                "every name added since " + day_month(DAY)
                if len(not_ruled_out) == len(later) else
                f"{word(len(not_ruled_out))} of the {word(len(later))} names added since "
                + day_month(DAY)
            )
            + " still reaches back to it. The first list that could add a name ruled out of "
            f"that list would be one dated {printed_date(first_excluding.isoformat())}."
        ),
        # The first block's heading is constant across every stop, because its count is:
        # the numerator of this work's figure cannot grow, and a heading that never moves
        # while the one under it does is the fixed point the run turns on.
        # THE OVERCLAIM, STRUCK — owed item (A), session 85. This heading said
        # *"{n} ships, all that the day held about itself"* from session 71 to session 84
        # inclusive, and it was refuted by the file this house saved on the morning of the
        # day it names: the same edition reported 230 disappearances examined and 5,641
        # events in its window. What the day held about itself is not eleven. Eleven is
        # what the list printed, and the heading now says only that. The refutation is
        # under the names, in the block this heading no longer has to carry.
        "heading_then": (
            f"IN THE LIST DATED {short_caps(DAY)} — the {word(field[0]['count'])} names "
            "it printed"
        ),
        # ── THE CUT, ON THE FACE. Owed item (A). ─────────────────────────────────────
        #
        # Four short strings under the eleven names, and they are the disclosure this work
        # has owed since its first capture. `figures` is SOURCED and carries upstream's own
        # words around each number, because those words are what the parser matched: a
        # match of `AGG_RE` proves the phrases "ships went dark inside national waters
        # lately — of", "disappearances examined (" and "in the window)." stood in those
        # bytes in that order, with these numbers in them. That is why they are printed as
        # upstream's words and not paraphrased, and why no sentence here is set in
        # quotation marks: the record holds the numbers and the parser's literal pattern,
        # not the edition's raw sentence. From tonight `capture.py` also stores the matched
        # span verbatim, so a later face can quote instead of reconstruct — the twenty-one
        # captures already committed are immutable and do not get one retrospectively.
        "cut": {
            "heading": f"WHAT THE LIST OF {short_caps(DAY)} WAS THE TOP OF",
            # THE ORDER IS THE MEANING. Upstream's own sentence makes the count of ships
            # dark inside national waters a subset of the disappearances EXAMINED, not of
            # the events in the window. Written as "… · 5,641 in the window · 82 of them
            # dark inside national waters", the "them" reaches back past the nearer number
            # and says something upstream does not. The subset stands beside the set it is
            # a subset of, and the window figure goes last.
            # CUT IN SESSION 87 ON `DRAMATURG-87.md` §3, ORDERED: the first two figures of
            # this line — the count of names and the count examined — stand in the head's
            # own frame now as the numeral `11 of 230`, and this copy was set larger and
            # blacker than the numeral it repeats, 588 px below it at 1400 px and 1,060 px
            # below it at 390. *"The page states its finding twice and gives the stronger
            # typographic voice to the copy that is 680 px away from the figure it is
            # about"* — the memo's words, and it is session 85's own standard (twenty
            # identical words, 466 px apart, cut) applied to this house a second time. What
            # survives is the content the numeral does NOT carry, and it keeps its subset
            # order: the ships dark inside national waters are a subset of the examined,
            # which is why that figure is named against `230` and the window figure goes
            # last.
            # `DRAMATURG-87.md`'s re-verdict, cut 1: *those* installed a pointer whose
            # antecedent stands 588 px above it at 1400 px and 1,060 px above it at 390. The
            # numeral itself stays, because the subset clause after it needs a set to be a
            # subset of.
            "figures": (
                f"Of the {day_cut['examined']:,} examined, "
                f"{day_cut['dark_inside_national_waters']} were dark inside national "
                f"waters · {day_cut['in_window']:,} events in the window"
            ),
            # CUT FROM 63 WORDS TO 20, AND WHAT SURVIVED IS THE SENTENCE THAT IS NOT ABOUT
            # THIS HOUSE — `DRAMATURG-85.md` §2, on the running object: of the three
            # sentences that stood here, *"the third — 'The figure above is a share of what
            # those lists print, not of what they count' — is the disclosure, and it arrives
            # 27 words in, behind two sentences that are the house talking about the
            # house."* The confession and the range are not deleted; they move below the
            # controls, where this head's other prose already lives and where nothing
            # measures a fold, and the range's one printed instance is there.
            #
            # AND THE HEADING'S CLAIM IS NOW UPSTREAM'S OWN, NOT AN INFERENCE. §2 of the
            # same memo objected that *"the top of"* asserts a selection rule the block then
            # disclaims. The objection is answered with evidence rather than by yielding:
            # the method sheet says it in words, fetched first-hand tonight (200, 27,748
            # bytes) — *"case of the day by region brisance, then duration. The index counts
            # all examined; the case and list show named vessels."* Found by
            # `VERIFIER-85.md` §5, which recorded that the strongest support for this whole
            # block was cited nowhere on the face. It is a genuine short quotation with its
            # source named on the face, which is the only kind this work prints.
            # AND THE WORD `above` WENT WITH THE MOVE. `DRAMATURG-85.md`, re-measured after
            # its own cuts were taken and pricing a cost it had not priced: this sentence —
            # *"the one line that turns the material into the finding"* — now stands 740 px
            # below the figure at 1400×900 and 1,216 px below it at 390×844, on the far side
            # of the reserved space, the buttons and the caption, and it still said *"the
            # figure above"*. A spatial word is a claim about a page, and this one had been
            # made false by the repair that moved it. It names the figure instead of
            # pointing at it.
            "said": (
                "The instrument says so itself, in its method sheet: “The index counts all "
                "examined; the case and list show named vessels.” The share this page "
                "publishes is a share of what those lists print, not of what they count."
            ),
            # MOVED OUT OF THE SPINE, NOT WITHDRAWN — `DRAMATURG-85.md` §2: *"fifty-four
            # words, in the head's dimmest type, entirely in the negative, whose whole
            # content is that a quantity has not been measured. That is a method sheet
            # inside a work."* The refusal is this house's answer to the critic's §2 and the
            # verifying pass ruled it the defensible one of the two, so it is not cut; it
            # stands below the controls with the caption.
            "refused": (
                "How the figure would move if the lists were longer is not published here: "
                "a longer list dated "
                f"{day_month(DAY)} could carry names this record counts as arriving late, "
                "and longer later lists would add to the total, so both ends of it would "
                "grow and nothing in this record measures by how much."
            ),
            # BELOW THE CONTROLS WITH THE REFUSAL: the confession, and the one printed
            # instance of the range. `DRAMATURG-85.md` §2 found the range's other instance
            # word-for-word inside the DERIVED tier line, twenty identical words 466 px
            # apart, and ordered that line back to doing the only job a tier line has.
            "kept": (
                f"Each of the {word(len(cut_rows))} lists this record holds prints "
                f"{word(min(r['printed'] for r in cut_rows))} to "
                f"{word(max(r['printed'] for r in cut_rows))} names of the "
                f"{min(r['examined'] for r in cut_rows)} to "
                f"{max(r['examined'] for r in cut_rows)} disappearances it says it examined. "
                "This record has saved that block every night since the first, and no face "
                "of this work printed one of its figures until tonight."
            ),
            # THE TIER LINE STOPPED CLAIMING WHAT IT COULD NOT COVER — `VERIFIER-85.md` §1,
            # blocking, and it is the cardinal sin in its subtlest form for the second night
            # running. The line read *"every figure in this block is read off the saved
            # copies, in the words the parser matched in them"* — a universally quantified
            # claim, false for two of the figures standing under it. `11 names printed` is
            # not published by upstream at all: it is this house's count of parsed vessel
            # entries, and the same `11` stands under a DERIVED word four blocks lower. The
            # count of lists is OBSERVED by this record's own definitions. Three figures are
            # upstream's and the line now says which three, and whose the others are.
            "tier": (
                "SOURCED — the three figures the list published, read off the saved copies "
                "in the words the parser matched in them. The count of names, and the count "
                "of lists below, are this house's own."
            ),
            # SESSION 87 — THE DISCLOSURE ENTERS THE NUMERAL. `DRAMATURG-85.md` ruled the
            # block above annotation and not staging, on one measurement — it counted the
            # block's mutations across a full run and got none — and prescribed a build
            # rather than a cut. Its words, quoted as they stand at `DRAMATURG-85.md:245`
            # and :257: *"Take the four fixed paragraphs out of the run's spine and put the
            # disclosure inside the numeral"*, and *"`230` standing still in the same frame
            # as `35 %–100 %` while it falls."* The paraphrase this comment carried until
            # `VERIFIER-87.md` §9 caught it was inside quotation marks and in neither memo;
            # an invented quotation is invented in any tier, and the marks were the whole of
            # the offence. This is that figure. It stands in the head's
            # own frame beside the share, at every stop, in the dim ink and the body weight
            # this face has meant since session 83 by *cannot move* — the same mark the
            # fixed end of the share already carries. The run then has two figures in one
            # frame and shows the difference between them by doing it: one falls sixty-seven
            # points in twenty-five seconds and the other is the same number at the last
            # stop as at the first, because it is what the list of the day printed and no
            # later list can reach it.
            "standing": f"{day_cut['printed']} of {day_cut['examined']:,}",
            # The clause the numeral needs, and its tier in the same breath: a figure whose
            # tier word travelled in a paragraph that has moved elsewhere is banked failure
            # 25, the cardinal sin by subtraction, and it is not being committed twice.
            # THE NUMERAL IS SAID IN WORDS BESIDE IT, and not because the ear needs a copy of
            # what the eye gets. `11 of 230` read as a phrase can be heard as *eleven of two
            # hundred and thirty NAMES*, which is false by an order of magnitude: the list
            # named eleven ships and says it examined two hundred and thirty disappearances.
            # A figure whose shortest reading is a wrong one does not stand on this face
            # without the sentence that closes it — and the sentence carries the tier, so
            # the eye and the ear get the same figure and the same word for where it came
            # from.
            # ONE SENTENCE SHORTER FROM SESSION 88, and only the one the run now performs.
            # *"No stop moves this figure"* was this note's telling of the thing the frame
            # could not show while the two figures spoke different languages. They speak the
            # same one from tonight: the row above is a fraction with the same numerator and
            # a denominator that moves through eight values, this row is a fraction with the
            # same numerator and one value, and a stop rewrites the first and never the
            # second. What the eye can now do for itself is not told to it again. What
            # survives is what no run can show — that these two hundred and thirty are
            # disappearances and not names, and whose count the numerator is.
            # THE ATTRIBUTION WENT OUT OF THIS STRING FOR ONE HOUR AND IS BACK — the third
            # blocking finding of `VERIFIER-88.md`, and it is banked failure 25's shape
            # again: the cardinal sin by subtraction. The shortened note printed the words
            # *eleven ships named* under a bare `SOURCED`, and this work's own legend rules
            # the count of names in a list DERIVED, in the sentence that records banked
            # failure 41 — *upstream prints names, and this house counts them*. Only the
            # 230 is the list's; the eleven is ours, and the string says so again.
            # AND THE TWO ELEVENS ARE NOT ONE FIGURE, which the defence for cutting this
            # clause assumed they were. This row's numerator is `day_cut["printed"]`, the
            # names counted across the copies of the 4 August edition; the row above it is
            # `knowable_on_the_day_OBSERVED`. They are equal in the record as it stands and
            # by nothing else — no law joins them and no check asserts one — so each row
            # carries the word for where its own numerator came from.
            "standing_note": (
                f"— {word(day_cut['printed'])} ships named, of "
                f"{day_cut['examined']:,} disappearances the list says it examined. "
                "SOURCED — the count of names is this house's own."
            ),
        },
        "stops": arrive_stops,
        # THE CONSTANT, MARKED — session 83. The staging voice's one banked change, and the
        # only one it named as the change that would most improve the head: *"one figure
        # falls 56 points while the other cannot move at all — because a register that names
        # a ship only when it comes back can never rule out a ship that never comes back.
        # That is the piece's actual subject. It is present in every frame, on screen for
        # eighteen seconds, and nothing marks it."*
        #
        # It is marked TWICE, and the second one is the point: the two ends of the figure
        # are now set apart in weight and colour AND said apart in words, standing still
        # under a figure that moves. A mark the eye can read and the ear cannot is banked
        # failure 12, and this house has now paid for that failure twice (12, 15). The
        # sentence says "upper end" and not "the right-hand number" for the same reason.
        # WHAT THIS SENTENCE SAID FOR ONE BUILD, AND WHY IT WAS FALSE — banked failure 31,
        # and it is the most serious thing this house has published in a fortnight. It read:
        # *"The upper end never moves. A list that can name a ship only when it comes back
        # can never rule out one that never comes back — so the lower end is the only end
        # this record can lower."* Both halves fail. The upper end is
        # `obs / max(certain, obs)`: it stands at 100 % only while NO ship is CERTAINLY dark
        # on this day, and `capture/day.py 2026-08-01` already returns thirteen certain — so
        # 4 August's upper end falls as soon as the bands close on its own names. And the
        # reason offered argued for an unbounded TOTAL, which lowers the LOWER end; it never
        # touched the upper one. The sentence was the staging voice's own formulation,
        # adopted here because it was well put, and it was published without being run
        # against the instrument that computes the number it described. Banked failure 23 in
        # its purest form. Caught by the verifying pass, blocking, before commit — and after
        # four severed readers had passed it at 4 of 4.
        # REPAIRED TWICE IN TWO SESSIONS, AND THE SECOND REPAIR WAS STILL FALSE — session 84.
        #
        # This sentence has now been wrong in three successive forms, each one better written
        # than the last. It said "the upper end never moves" (session 83): false, and four
        # severed readers passed it. It was repaired to "it falls the moment one of them
        # becomes certain" (session 83, in the same night's blocking pass): ALSO FALSE, and
        # this house committed it, published it in a commit message, and put it to a
        # premiere gate. `day.py:214` computes that end as `obs / max(n_lo, obs)` with
        # `obs = 11`. One ship becoming certain does nothing: the quotient is 11/11. The end
        # falls when the certain count passes the ELEVEN the day itself named — at twelve
        # certain the upper end is 11/12, 92 %. The verifying pass proved it on probe capture
        # sets and this house re-ran it before believing it.
        #
        # The lesson this house is paying for twice: a sentence about arithmetic is not
        # checked by reading it, however well it is put. It is checked by running the
        # arithmetic. Both false versions were adopted because they were clearer than what
        # they replaced.
        # Both counts below are COMPUTED, like every other number on this face. The first
        # false version of this sentence typed nothing and was wrong anyway; the repair is
        # not allowed to introduce a hand-typed number on top (banked failure 17).
        # BLOCKED AND REPAIRED THE SAME NIGHT — `VERIFIER-86.md` §4, and it is the third
        # false published sentence about this one end. The clause below read
        # *"so all {band[1]} are merely possible today"* and it was true every night this
        # figure has existed, because the certain count was zero every night. Tonight the
        # list of 11 August made two of them certain, and the sentence went on saying ALL
        # thirty-three are merely possible — while the `hedge` string, 489 px BELOW it on the
        # rendered page at 390×844, correctly said two of them are not. (That distance and
        # its direction are `VERIFIER-87.md`'s re-run, item 2: this comment said *three lines
        # above* for two sessions, wrong in magnitude and in direction both.) One page, two
        # sentences, direct contradiction. Nothing was typed to cause it: the defect was
        # structural, waiting since the string was written for the first night the certain
        # count left zero, and the hedge had been given the branch it needed and this had
        # not. **A conditional that only one of two sentences about the same fact carries is
        # a false sentence with a delay fuse in it.** Both now branch on the same value.
        # SESSION 87 — THE MIDDLE CLAUSE IS GONE, AND ITS GOING IS THE SAFER STATE. A
        # twenty-three-word clause of this sentence said what the `hedge` line says lower on
        # the same rendered page — **489 px lower at 390×844 on the object as committed**,
        # with the day's heading, eleven names, the hole's heading and twenty-two names
        # standing between them (`VERIFIER-87.md`'s re-run, items 1 and 4; the 278 px the
        # staging voice measures at 1400 is its §4). (Three lines apart in the RENDERED
        # ISLAND at the last stop, which is where that phrase came from; in this builder they
        # are 403 lines apart, and on the page they were never on one screen.) The clause: a list gives a
        # return only to the nearest week, so n of the total are merely possible and the
        # rest are certain. The whole edit removes forty-seven words and inserts three. Two sentences, one fact — and
        # that arrangement is exactly banked failure 42: last night one of the two carried a
        # branch on the certain count and the other did not, and the one without it published
        # *"all thirty-three are merely possible"* on the first night two of them were not.
        # Both were given the branch. Tonight the duplicate is removed instead: one fact, one
        # sentence, one branch, and no second copy that can be left behind by a change to the
        # first. Measured by `tools/frame.mjs`, this paragraph falls from 167 px to 83 px at
        # 390×844 and from 117 px to 67 px at 1400×900: an 84 px cut of a phone frame that
        # was 250 px over. The figure this comment carried before the pass — 57 px — was
        # reproduced by no run of that instrument, and it was written in a sentence claiming
        # it was measured by it (`VERIFIER-87.md` §6). Banked failure 26's class: a
        # hand-checkable number published without running the check, in the one comment that
        # boasted of running it.
        "constant": (
            "Neither end of this figure can rise. The upper end holds at 100 % until more of "
            "these ships are certainly dark on this day than the "
            f"{word(field[0]['count'])} the day itself named; only the lower end has moved "
            "so far, and the next list can lower it again."
        ),
        # THE RUN, SAID — session 83, owed items (s) and (t), paid by one set of strings
        # that reaches the eye and the ear from the same place.
        #
        # (t) was the largest thing this project owed: `[aria-live],[role=status],[role=alert]`
        # returned 0 on the committed page, so a visitor using a screen reader and no
        # reduced-motion preference had a document rewritten six times behind their cursor
        # with nothing announced. (s) was the cost of the beat we built in 82: a stop pressed
        # inside the first eleven seconds killed the only authored sequence the object has,
        # silently and permanently.
        #
        # The repair is one line under the buttons, in the page's own words, in a region that
        # announces its own changes. TWO announcements in an untouched run — one at the
        # start, one at the end — and not six, because six announcements in eighteen seconds
        # is the noise this house refused to ship unmeasured in 82. Every other announcement
        # is one the visitor asked for by pressing something.
        #
        # `waiting` also answers `DRAMATURG-82.md` §1, which is the other half of (s): eleven
        # seconds of stillness *"reads as an invitation"* to press a button, because nothing
        # says a performance is pending. Now something does, and it says what pressing will
        # cost.
        "run_states": {
            # `waiting` is completed below, once the derived first beat is known: the
            # duration it states is the page's own arithmetic and not a number typed beside
            # it. Banked failure 17 — *"a constant advanced by hand is a number typed by
            # hand wearing a variable's name"* — and 8, dates and figures reaching a face
            # out of a head.
            "waiting": None,
            # SESSION 83, SECOND PASS. The run's own beginning was the one event in this
            # piece with no words at all: the beat ended, the figure started falling, and
            # nothing said so to anyone who could not see it. Found by the staging voice on
            # the running object, in the same breath as the defect below.
            "started": (
                "The run has started: the figure is falling from the day's own answer to "
                "this record's live one."
            ),
            "done": (
                "The run has finished. The figure now standing is this record's live one "
                "— press any button to go back through it."
            ),
            "stopped": "You stopped the run at {stop}. Press “{replay}” to see it whole.",
            "held": "Holding {stop}. Nothing is playing; press “{replay}” to run it.",
            # What a visitor whose machine asks for no motion is told, and it is the state
            # this house's own renderer is served — so the material a panel reads says
            # plainly that nothing was running for it either.
            "rest": (
                "Your machine asks for no motion, so nothing runs: this is the day's own "
                "answer, and each button above holds a later state."
            ),
        },
        # The mechanism, said once, under the thing that has just enacted it. The word
        # order matters: the reason comes first, so a reader who arrives after the run
        # has finished still gets why the number moved.
        "caption": (
            "A ship reaches the list only after it comes back, so a day that is over "
            f"keeps being answered. {word(n_stops).capitalize()} lists, "
            f"{word(n_stops)} answers, one day — the last of them "
            f"{'a day' if last_late == 1 else word(last_late) + ' days'} after the day "
            f"had ended. The {word(field[0]['count'])} names the day itself held cannot "
            "grow; every list since has only made the day larger underneath them."
            # AND THE LAST CLAUSE WENT IN SESSION 88, ordered by `DRAMATURG-88.md`'s re-put
            # after both voices had already reported. Moving *what the ends of the figure
            # can do* below the controls landed it **5 px** under this caption — so a
            # caption ending *"and why it can only go on falling"* was read as one block
            # with a paragraph opening *"Neither end of this figure can rise"*: **one law
            # printed twice at 5 px, by a house that struck a figure printed twice at 588.**
            # CORRECTED THE SAME NIGHT, BEFORE THE CUT'S OWN PROSE HAD SHIPPED A SECOND TIME:
            # this comment said the deleted clause also carried *the figure above*, *"a spatial
            # pointer whose reach had stretched from 128 px to 869 by the same move"*. **That
            # measurement is of a different string.** 128 → 869 is the reach of *this figure*,
            # the pointer inside the CONSTANT, which was not deleted; the caption's *the figure
            # above* is 880 px and INHERITED, and the caption did not move down by this cut at
            # all — it moved up 81 px (`VERIFIER-88.md` S4, measured at 390). The cut stands on
            # the 5 px doubling, which is its own reason and needs no borrowed number.
            # The survivor states the law and the condition together, in the paragraph that
            # is only about the ends of the figure. The caption keeps the mechanism, which
            # is its job, and ends on the sentence that says what the later lists did.
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
        #
        # THE LABEL WAS TRUE AND ITS BASIS WAS NOT STATED — owed item (A), session 85, and
        # this is the sharpest form of the critic's finding. *"Worked out here, from saved
        # copies of those lists"* is exact and checkable, and it says nothing about what
        # those lists are: ten-odd names at the top of a couple of hundred. Under this
        # house's own labelling law a tier word whose declared basis is true and whose real
        # basis is unstated does not hold. The clause is added here, in the head, and not
        # only in the block below — this sentence is what a reader who scrolls no further
        # carries away about the number above it.
        #
        # AND THE CLAUSE ADDED TONIGHT IS CUT THE SAME NIGHT — `DRAMATURG-85.md` §2, the one
        # cut it named exactly, with the string: the eighteen words appended here stood
        # word-for-word in the block above, 466 px away at 1400 and 860 px at 390. *"The
        # fact keeps the one place where it is argued rather than repeated; the tier line
        # goes back to doing the only job a tier line has."* The basis the critic said was
        # unstated is stated — in the block that carries the figures, under a tier word of
        # its own, twice the size of this line and above it in reading order.
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
    # it is set for, and every one of them still has a button for every stop and no clock —
    # and, since session 83, one line that says how long the run is before it starts.
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
    # The run's whole length, computed from the two clocks that produce it and rounded to
    # the second the visitor is being promised. Nothing here is typed: change the gloss and
    # this sentence changes with it.
    run_seconds = round((arrive["first_dwell_ms"] + (n_stops - 1) * 1600) / 1000)
    arrive["run_states"]["waiting"] = (
        f"This figure runs by itself: {word(n_stops)} states over about "
        f"{word(run_seconds)} seconds, starting after a pause as long as the paragraph "
        "under the title takes to read. Any button above holds a state and stops the run."
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
            "after this page had printed its figure. All three counts are DERIVED: worked "
            "out here, from saved copies of those lists."
            # SESSION 83, on the verifying pass, blocking. These three counts stood on the
            # page's first sentence with no tier word anywhere near them, and ABOVE the
            # legend that carries the tier words in reading order — so the first numbers a
            # stranger meets were the only unmarked ones on the face. That is failure 25
            # exactly: the legend is the authority every instrument here trusts, and nothing
            # this house owns asks whether a published figure carries a tier. The mark is
            # self-contained rather than a pointer, for the same reason the head's is.
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
    # SAID OF A NAMED COLUMN AND NOT OF A POSITION — session 85. This sentence began "the
    # last column" and stopped being true the moment owed item (A) put a column after it.
    # A caption that points by position is a caption that breaks silently when the table
    # grows, which is the same defect as a tier mark lost to a cut (banked failure 25).
    ledger_caption += (
        " The “ships in that list” column counts the ships in each saved list, not the ships "
        f"this page can place in {printed_date(DAY)}: every list holds only the "
        f"{word(caps_now[-1]['method']['window_days'])} days before its own date, so a ship "
        "leaves the list as that window moves past it. It never leaves the day."
    )
    # OWED ITEM (A), THE TABLE'S LIMB — session 85. The two count columns are the finding
    # in one place: what a saved copy printed, and what the same copy said the instrument
    # had examined to print it. Both have stood in every capture since the first; until
    # tonight this table carried only the first.
    # NAMED BY THE COLUMN'S OWN NAME, not by a word the table does not print —
    # `VERIFIER-85.md` §7, which found this caption pointing at columns called SHIPS and
    # EXAMINED in a table whose headers read "ships in that list" and "disappearances
    # examined". Nothing false, and a caption that names a column should use the column's
    # name; the positional pointer this replaced broke the moment a column was added.
    ledger_caption += (
        " “Disappearances examined” is what that same copy says the instrument examined to "
        "produce those ships — a figure this record has saved every night since the first "
        "and, until tonight, printed never."
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
            # OWED ITEM (A) IN THE TABLE — session 85. The column beside it counts the
            # names a saved copy holds; this one counts what that same copy says the
            # instrument examined to produce them. Both numbers have been in every capture
            # since the first and only one of them has ever been printed. It is one column
            # and not four because the table is a record of this house's fetching, not a
            # restatement of upstream's summary: the other three aggregates stand in the
            # head, beside the eleven names they are about.
            "examined": (c.get("aggregates") or {}).get("disappearances_examined"),
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
