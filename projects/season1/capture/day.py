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
    """One row per distinct vessel, carrying its first sighting in OUR record."""
    rows = {}
    for c in caps:
        ed = c.get("edition_date")
        for v in c.get("vessels", []):
            k = vessel_key(v)
            r = rows.setdefault(
                k,
                {
                    "name": v["name"],
                    "flag": v["flag"],
                    "days_dark": v.get("days_dark"),
                    "waters": v.get("waters"),
                    "first_edition_date": ed,
                    "first_capture": c["_path"],
                    "first_seen_utc": c["fetch"]["fetched_at_utc"],
                    "editions": [],
                },
            )
            if ed and ed not in r["editions"]:
                r["editions"].append(ed)
            if ed and r["first_edition_date"] and ed < r["first_edition_date"]:
                r.update(
                    first_edition_date=ed,
                    first_capture=c["_path"],
                    first_seen_utc=c["fetch"]["fetched_at_utc"],
                )
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
        # itself a band [certain, certain+possible]. A vessel knowable on the day was dark
        # on it, so the denominator can never fall below the numerator: the low end of the
        # band is obs / possible, the high end obs / max(certain, obs).
        # It is a CEILING that can only fall: every further capture can add vessels to the
        # day, never remove one, and can never make a past edition contain a name it did not.
        "share_knowable_OBSERVED": (
            None
            if (not have_capture_on_or_before or n_hi == 0)
            else [
                round(len(knowable_observed) / n_hi, 4),
                round(len(knowable_observed) / max(n_lo, len(knowable_observed)), 4)
                if max(n_lo, len(knowable_observed))
                else None,
            ]
        ),
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
        f"{n_ed} distinct edition(s)"
    )
    print(f"  vessels dark on that day .......... {b[0]}–{b[1]} (certain–possible)")
    print(f"  knowable on the day, DERIVED ...... {res['knowable_on_the_day_DERIVED']}")
    obs = res["knowable_on_the_day_OBSERVED"]
    print(f"  knowable on the day, OBSERVED ..... {obs if obs is not None else 'not yet measurable'}")
    sh = res["share_knowable_OBSERVED"]
    if sh:
        print(
            f"  SHARE knowable on the day ......... {sh[0]*100:.0f}%–{sh[1]*100:.0f}%  "
            f"({obs} of {b[0]}–{b[1]})"
        )
        print(
            f"    (a ceiling from {n_ed} edition(s), {res['captures_read']} capture(s): further "
            f"nights can only add vessels to this day, so this share can only fall)"
        )
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
