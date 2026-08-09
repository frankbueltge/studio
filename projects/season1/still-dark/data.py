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
        },
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
