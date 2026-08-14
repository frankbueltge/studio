#!/usr/bin/env python3
"""STILL DARK — the day instrument.

Holds ONE calendar day open and asks the work's question about it:

    of the vessel-days of darkness that belong to that day, what share was
    knowable on the day itself?

Nobody publishes that number, upstream least of all: the Ghost Fleet's window is
"disabling events that ended in the last 7 days (complete vanish-and-return stories)",
so an edition is a list of endings, never a picture of a day. This script reads the
committed captures in projects/season1/captures/ and computes the share two ways, kept
strictly apart:

  DERIVED  — available from a single capture. A vessel's event ended somewhere in the
             7 days before its edition date, so its dark interval is a band. A vessel
             is CERTAIN for day T if T lies in the interval under every end in the band,
             POSSIBLE if under some. It was knowable on T only if it had ended by T.
             The answer is a range, never a point, because the input is a range.
  OBSERVED — available only once nights accumulate. A vessel was knowable on T if it
             stands in a capture whose edition date is on or before T. This is our own
             record measuring itself, and it is the number the work will publish.

Both are printed. Where OBSERVED cannot yet be computed (no capture from on or before
the target day), the script says so instead of falling back to DERIVED — the fallback
is exactly the blur the work exists to refuse.

Usage:  python3 day.py 2026-07-10 [--captures DIR] [--as-of UTC] [--json]

--as-of reads only the captures fetched at or before a UTC instant, so the record as it
stood at any past moment can be re-run by anyone. The work's first screen is exactly such
a moment; without this flag that screen would be a state only this house could reproduce.
"""

import argparse
import datetime
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edition import case_waters, content_sha256  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CAPTURES = os.path.normpath(os.path.join(HERE, "..", "captures"))


def load(capdir, as_of=None):
    caps = []
    for p in sorted(glob.glob(os.path.join(capdir, "*.json"))):
        with open(p, encoding="utf-8") as f:
            c = json.load(f)
        if as_of and c["fetch"]["fetched_at_utc"] > as_of:
            continue
        c["_path"] = os.path.basename(p)
        caps.append(c)
    return caps


def vessel_key(v):
    """Identity across captures: the Global Fishing Watch id where present, else name+flag."""
    u = v.get("gfw_url") or ""
    return u.rsplit("/", 1)[-1] if u else f"{v.get('name')}|{v.get('flag')}"


def index(caps):
    """One row per distinct vessel, carrying its first sighting in OUR record.

    EVERY published field of a vessel comes from ONE capture — the first sighting — and
    that is why this runs in two passes rather than one. First sighting is the
    measurement, and it may not be revised.

    Rewritten session 74 (2026-08-07), discharging the latent defect
    `VERIFIER-73.md` recorded and `PROJECT.md` carried as owed item (c). The single-pass
    version filled a missing waters string from *whichever* capture happened to carry
    one, so a vessel first seen without waters could later stand on the face with waters
    read out of a different night's edition — a field silently taken from a capture that
    is not the vessel's own first sighting. It was never live (today every vessel's
    waters come from its first-sighting capture), and a defect is repaired before it
    goes live or the repair is a story about luck.

    The case of the day still needs its exception, and it is now exactly one capture
    wide: upstream prints that one vessel's waters as prose and never as a list row, so
    `case_waters` recovers the printed string — from the FIRST-SIGHTING capture only.
    See `edition.py` for the warrant and its size.
    """
    # Pass 1 — for each vessel, which capture is its first sighting? Earliest edition
    # date wins; captures arrive in fetch order, so an equal edition date keeps the
    # earlier fetch. Nothing is read off a vessel here except its identity.
    first = {}
    for c in caps:
        ed = c.get("edition_date")
        for v in c.get("vessels", []):
            k = vessel_key(v)
            prev = first.get(k)
            if prev is None or (ed and prev[0] and ed < prev[0]):
                first[k] = (ed, c, v)

    # Pass 2 — build each row from its own first-sighting capture, and only there.
    rows = {}
    for k, (ed, c, v) in first.items():
        rows[k] = {
            "name": v["name"],
            "flag": v["flag"],
            "days_dark": v.get("days_dark"),
            "waters": v.get("waters")
            or (case_waters(c) if v.get("role") == "case_of_the_day" else None),
            "first_edition_date": ed,
            "first_capture": c["_path"],
            "first_seen_utc": c["fetch"]["fetched_at_utc"],
            "editions": [],
        }

    # The edition list is the one field that is legitimately cumulative: it records every
    # edition in which this record has seen the vessel, which is a fact about the record.
    for c in caps:
        ed = c.get("edition_date")
        if not ed:
            continue
        for v in c.get("vessels", []):
            r = rows.get(vessel_key(v))
            if r is not None and ed not in r["editions"]:
                r["editions"].append(ed)
    return rows


def bands(row, window_days=7):
    """(earliest end, latest end) for a vessel's darkness, from its first edition."""
    ed = datetime.date.fromisoformat(row["first_edition_date"])
    return ed - datetime.timedelta(days=window_days), ed


def analyse(target, caps):
    t = datetime.date.fromisoformat(target)
    rows = index(caps)
    certain, possible, knowable_derived, knowable_observed = [], [], [], []

    for r in rows.values():
        d = r.get("days_dark")
        if not d or not r.get("first_edition_date"):
            continue
        end_lo, end_hi = bands(r)
        # The dark interval under an end e is (e - d, e]; T belongs to it iff e - d < T <= e.
        # CERTAIN means that holds for every end in the band, POSSIBLE for some of them.
        ends = [end_lo + datetime.timedelta(days=i) for i in range((end_hi - end_lo).days + 1)]
        feasible = [e for e in ends if (e - datetime.timedelta(days=d)) < t <= e]
        if not feasible:
            continue
        in_all = len(feasible) == len(ends)
        f_lo, f_hi = min(feasible), max(feasible)
        entry = {
            "name": r["name"],
            "flag": r["flag"],
            "days_dark": d,
            "waters": r["waters"],
            # narrowed to the ends under which this vessel was in fact dark on the target day
            "resurfaced_between": [f_lo.isoformat(), f_hi.isoformat()],
            "first_edition_date": r["first_edition_date"],
            "first_seen_utc": r["first_seen_utc"],
            "days_late_derived": [(f_lo - t).days, (f_hi - t).days],
        }
        (certain if in_all else possible).append(entry)
        if f_hi <= t:  # could have been in an edition on or before T under every feasible end
            knowable_derived.append(entry)
        if r["first_edition_date"] <= target:
            knowable_observed.append(entry)

    have_capture_on_or_before = any(
        c.get("edition_date") and c["edition_date"] <= target for c in caps
    )
    n_lo, n_hi = len(certain), len(certain) + len(possible)
    return {
        "target_day": target,
        "captures_read": len(caps),
        # Captures and editions are not the same count, and the difference is the work's
        # own subject: on 5 August 2026 three captures held two editions, because the
        # 12:54 and 19:17 fetches returned the same edition byte for byte. A ceiling is
        # only as strong as the number of DISTINCT editions behind it, so that is what
        # gets printed beside it.
        "editions_read": sorted({c["edition_date"] for c in caps if c.get("edition_date")}),
        # Three counts, not two, since session 70. A capture on 2026-08-06 returned the
        # 5 August edition with a DIFFERENT body hash at an identical byte count, while
        # every field this work reads was unchanged: the response moved, the edition did
        # not. So "distinct bodies" is a fact about the site and "distinct contents" is
        # the fact about the sea. See capture/edition.py.
        "distinct_bodies": len({c["fetch"]["sha256"] for c in caps}),
        "distinct_contents": len({content_sha256(c) for c in caps}),
        "capture_range": [
            min((c["fetch"]["fetched_at_utc"] for c in caps), default=None),
            max((c["fetch"]["fetched_at_utc"] for c in caps), default=None),
        ],
        "vessels_dark_on_day": {"certain": n_lo, "possible_extra": len(possible), "band": [n_lo, n_hi]},
        "knowable_on_the_day_DERIVED": len(knowable_derived),
        "share_knowable_DERIVED": (
            None if n_hi == 0 else [round(len(knowable_derived) / n_hi, 4), round(len(knowable_derived) / n_lo, 4) if n_lo else None]
        ),
        "knowable_on_the_day_OBSERVED": (
            len(knowable_observed) if have_capture_on_or_before else None
        ),
        # The number the work publishes, and it is a band because its denominator is one.
        # Numerator: vessels standing in an edition on or before the target day — our own
        # captures, nothing derived. Denominator: the vessels our record places in the day,
        # itself a band [certain, certain+possible].
        #
        # THE PREMISE THIS COMMENT CARRIED FOR NINE SESSIONS WAS FALSE, and it is the worst
        # thing this house has published. It read: *"A vessel knowable on the day was dark on
        # it, so the denominator can never fall below the numerator: the low end of the band
        # is obs / possible, the high end obs / max(certain, obs)."* A vessel knowable on the
        # day was only POSSIBLY dark on it, and the two sets the quotient divides are
        # DISJOINT BY CONSTRUCTION — which this file proves twelve lines above without ever
        # having been asked to. A vessel is `certain` only when EVERY end of its published
        # return window leaves it dark on the day, and a window that ends on or before the
        # day is what puts a vessel in an edition dated on or before the day. So a knowable
        # vessel is never a certain one; run it and see:
        #     certain ∩ (the names in the edition dated <= the day)  ==  empty, at every stop.
        # `max(certain, obs)` therefore asserted a world in which the day's whole darkness is
        # the eleven names the day itself printed — a world in which the eleven vessels that
        # are CERTAINLY dark on that day are not dark on it. In the world where the
        # denominator really is obs, the numerator is 0 and the share is 0 %, not 100 %.
        # Found at the premiere gate of session 92 by the critic, proved on this file's own
        # --json output, and this record does not patch it quietly: `KRITIKER-92.md`.
        #
        # WHAT IS TRUE. Write C for certain, K for the knowable, k for however many of the K
        # were in fact dark on the day, and m for the rest of the possible ones that were.
        # The share is k / (C + k + m). It is largest at k = K, m = 0 — the CEILING is
        # obs / (certain + obs) — and smallest at k = 0, where it is 0, because every
        # knowable vessel is possible and not one is certain. So the pair below is a band
        # ONLY under the stated condition that every vessel the day itself named was in fact
        # dark on it; unconditionally the floor is 0, and `share_floor_unconditional` says
        # so rather than leaving a reader to find it out the way this house did.
        # It is still a CEILING that can only fall: every further capture can add vessels to
        # the day, never remove one, and can never make a past edition contain a name it did
        # not — and now the ceiling falls on the FIRST vessel that becomes certain, not on
        # the twelfth, which is what the three superseded sentences about this end were all
        # groping at and none of them reached.
        "share_knowable_OBSERVED": (
            None
            if (not have_capture_on_or_before or n_hi == 0)
            else [
                round(len(knowable_observed) / n_hi, 4),
                round(
                    len(knowable_observed) / (n_lo + len(knowable_observed)), 4
                )
                if (n_lo + len(knowable_observed))
                else None,
            ]
        ),
        # Printed beside the band so the condition the band stands on cannot be dropped in
        # transit. WHICH END THE CONDITION BINDS, corrected in session 94 by KRITIKER-94
        # and re-derived here before it was typed: the comment above says the share is
        # largest at k = K, m = 0, so obs / (certain + obs) is the maximum over EVERY value
        # of k this record allows — a ceiling that holds unconditionally, not a figure that
        # assumes anything. Only the lower end needs the assumption. For one session this
        # string said "both ends assume", the face printed it eleven times in its largest
        # paragraph, and it hedged away the one unconditional result this work has.
        "share_band_condition": (
            None
            if not have_capture_on_or_before
            else (
                f"the upper end assumes nothing: whatever became of the "
                f"{len(knowable_observed)} names the day itself printed, no case this "
                f"record allows puts the share above {len(knowable_observed)} of "
                f"{n_lo + len(knowable_observed)} — that end is a ceiling over all of "
                f"them. The lower end does assume every one of those "
                f"{len(knowable_observed)} was in fact dark on the day; not one of them "
                f"is certain, so unconditionally the share's floor is 0"
            )
        ),
        "share_floor_unconditional": 0.0 if have_capture_on_or_before else None,
        "share_is_a_falling_ceiling": have_capture_on_or_before and n_hi > 0,
        "observed_note": (
            None
            if have_capture_on_or_before
            else "no capture from on or before the target day — the OBSERVED share is not "
            "yet measurable and is deliberately not substituted with the DERIVED one"
        ),
        "certain": sorted(certain, key=lambda e: -e["days_dark"]),
        "possible": sorted(possible, key=lambda e: -e["days_dark"]),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("day", help="target calendar day, YYYY-MM-DD")
    ap.add_argument("--captures", default=DEFAULT_CAPTURES)
    ap.add_argument(
        "--as-of",
        dest="as_of",
        default=None,
        help="read only captures fetched at or before this UTC instant, e.g. 2026-08-05T12:00:00Z",
    )
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    # THE INSTANT IS CHECKED BEFORE IT IS USED — session 94, paying a note three verifying
    # passes old (`VERIFIER-92` note 3, `VERIFIER-93` note 5, `VERIFIER-94` note 1). The
    # comparison below is a STRING comparison against `fetched_at_utc`, so an instant this
    # instrument cannot read did not fail: it sorted, and the answer came back with a
    # straight face. `--as-of 2026-08-14T204526Z` — the exact shape of this record's own
    # capture FILENAMES, which is the form a stranger is likeliest to paste — silently
    # dropped the newest capture and returned the previous night's band as tonight's answer.
    # A record that invites a stranger to check it does not get to answer a question it did
    # not understand.
    if a.as_of is not None:
        probe = a.as_of[:-1] + "+00:00" if a.as_of.endswith("Z") else a.as_of
        try:
            when = datetime.datetime.fromisoformat(probe)
            # AND IT IS NORMALISED, WHICH IS THE HALF THAT ACTUALLY PAYS THE NOTE. Validating
            # alone was not enough and this house checked: `2026-08-14T204526Z` PARSES — the
            # basic ISO form is legal — and then loses to `2026-08-14T20:45:26Z` in the string
            # comparison, dropping the newest capture and answering with last night's band.
            # Every instant this instrument accepts is rewritten into the one shape the
            # captures are stamped in before anything is compared.
            if when.tzinfo is not None:
                when = when.astimezone(datetime.timezone.utc).replace(tzinfo=None)
            a.as_of = when.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            raise SystemExit(
                f"--as-of {a.as_of!r} is not a UTC instant this instrument can read. "
                "Write it as 2026-08-14T20:45:26Z — the form printed beside every stop on "
                "the work's own face. (Capture filenames drop the colons; that form is not "
                "an instant and is refused here rather than silently answered.)"
            )

    caps = load(a.captures, a.as_of)
    if not caps:
        raise SystemExit(
            f"no captures in {a.captures}"
            + (f" at or before {a.as_of}" if a.as_of else "")
        )
    res = analyse(a.day, caps)
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return 0

    b = res["vessels_dark_on_day"]["band"]
    n_ed = len(res["editions_read"])
    print(
        f"day {res['target_day']}  ·  {res['captures_read']} capture(s) read, "
        f"{n_ed} distinct edition(s), {res['distinct_contents']} distinct content(s), "
        f"{res['distinct_bodies']} distinct bod(y/ies)"
    )
    print(f"  vessels dark on that day .......... {b[0]}–{b[1]} (certain–possible)")
    print(f"  knowable on the day, DERIVED ...... {res['knowable_on_the_day_DERIVED']}")
    obs = res["knowable_on_the_day_OBSERVED"]
    print(f"  knowable on the day, OBSERVED ..... {obs if obs is not None else 'not yet measurable'}")
    sh = res["share_knowable_OBSERVED"]
    if sh:
        # The denominators are printed as the two divisions they actually are. Until session
        # 92 this line printed `({obs} of {b[0]}–{b[1]})` — the certain count as the ceiling's
        # denominator — which is the same false premise the band itself carried: the ceiling
        # divides by certain PLUS the knowable, because no knowable vessel is a certain one.
        print(
            f"  SHARE knowable on the day ......... {sh[0]*100:.0f}%–{sh[1]*100:.0f}%  "
            f"({obs} of {b[0] + obs}–{b[1]})"
        )
        print(
            f"    (a ceiling from {n_ed} edition(s), {res['captures_read']} capture(s): further "
            f"nights can only add vessels to this day, so this share can only fall)"
        )
        print(f"    ({res['share_band_condition']}.)")
    if res["observed_note"]:
        print(f"    ({res['observed_note']})")
    for e in res["certain"] + res["possible"]:
        lo, hi = e["days_late_derived"]
        tag = "certain " if e in res["certain"] else "possible"
        print(
            f"  {tag} {e['name']:<20} {e['flag']}  {e['days_dark']:>3} d dark  "
            f"arrived {lo}–{hi} days after the day"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        # `day.py <date> | head` is how a stranger will read this. A closed pipe is not
        # an error in the instrument and must not print a traceback that looks like one.
        os.dup2(os.open(os.devnull, os.O_WRONLY), 1)
        raise SystemExit(0)
