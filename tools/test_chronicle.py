"""Proof that chronicle.py sees a missing self-report and a hollow premiere, not only a
malformed entry.

Run: python3 -m pytest tools/test_chronicle.py

The shape checks were already covered by the fact that they had fired twice in anger
(session 84's move, session 100's verdict). The completeness check had not: on 2026-09-09
session 132 wrote a journal day and no entry, this instrument exited 0, and the site's gate
refused the night with `expected 131 to be 132`. These tests pin both halves, and the last
one reads the real repository so a drift between this counter and the journal on disk shows
up here rather than in a build letter the next morning.

The third half was added on 2026-10-03, after session 150 shipped
`works/2026-10-03-who-writes-the-row/` without a `meta.json` and the site's dossier test
refused the night. The shape checks passed and the counts agreed; nothing in this
repository asked for the one file the mirror reads first.
"""

import json
import os

import pytest

from chronicle import (
    check,
    check_completeness,
    check_shipped_works,
    count_sessions,
    journal_sessions,
)

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def entry(session, date, **over):
    e = {
        "collective_session": session,
        "date": date,
        "move": "ship",
        "summary": "A self-report with a summary long enough for the site's schema.",
        "works": [],
        "verdict": None,
    }
    e.update(over)
    return e


def write_journal(tmp_path, days):
    d = tmp_path / "journal"
    d.mkdir()
    for name, body in days.items():
        (d / name).write_text(body, encoding="utf-8")
    return str(d)


# --- counting sessions the way the site splits them -------------------------------------


def test_one_h1_is_one_session():
    assert count_sessions("# Session 132 — 2026-09-09\n\nbody\n") == 1


def test_several_h1s_are_several_sessions():
    body = "# Session 1\n\na\n\n# Session 2\n\nb\n\n# Session 3\n\nc\n"
    assert count_sessions(body) == 3


def test_a_hash_inside_a_code_fence_is_not_a_heading():
    # The journals quote shell constantly; `# comment` inside a fence must not open a
    # session. This is the case that would silently inflate the expected count.
    body = "# Session 1\n\n```bash\n# not a heading\ngit push\n```\n\nstill session 1\n"
    assert count_sessions(body) == 1


def test_text_before_the_first_h1_is_its_own_chunk():
    assert count_sessions("preamble\n\n# Session 1\n\nbody\n") == 2


def test_a_file_with_no_h1_is_one_session():
    assert count_sessions("just prose, no headings\n") == 1


def test_journal_sessions_sums_per_day_and_ignores_non_markdown(tmp_path):
    d = write_journal(
        tmp_path,
        {
            "2026-09-08-session-131.md": "# Session 131\n\nbody\n",
            "2026-09-09-session-132.md": "# Session 132\n\nbody\n",
            "2026-09-09-session-133.md": "# Session 133\n\nbody\n",
            "README.txt": "not a journal day",
            "notes.md": "no date prefix, not a journal day",
        },
    )
    assert journal_sessions(d) == {"2026-09-08": 1, "2026-09-09": 2}


# --- the completeness check ------------------------------------------------------------


def test_a_covered_journal_is_silent(tmp_path):
    d = write_journal(tmp_path, {"2026-09-08-session-131.md": "# Session 131\n\nbody\n"})
    assert check_completeness([entry(131, "2026-09-08")], d) == []


def test_the_night_of_2026_09_09_is_caught(tmp_path):
    # The real shape: the journal day landed, the entry did not.
    d = write_journal(
        tmp_path,
        {
            "2026-09-08-session-131.md": "# Session 131\n\nbody\n",
            "2026-09-09-session-132.md": "# Session 132\n\nbody\n",
        },
    )
    problems = check_completeness([entry(131, "2026-09-08")], d)
    assert len(problems) == 1
    assert "2026-09-09" in problems[0]
    assert "1 session(s) in the journal, 0 entry" in problems[0]


def test_an_entry_with_no_journal_day_is_caught(tmp_path):
    d = write_journal(tmp_path, {"2026-09-08-session-131.md": "# Session 131\n\nbody\n"})
    problems = check_completeness([entry(131, "2026-09-08"), entry(132, "2026-09-09")], d)
    assert len(problems) == 1
    assert "the self-report claims a session the journal does not hold" in problems[0]


def test_two_errors_that_cancel_in_the_total_are_both_reported(tmp_path):
    # The reason the check is per day: one missing and one duplicated entry leave the two
    # totals equal and the site's anchor set still mismatched.
    d = write_journal(
        tmp_path,
        {
            "2026-09-08-session-131.md": "# Session 131\n\nbody\n",
            "2026-09-09-session-132.md": "# Session 132\n\nbody\n",
        },
    )
    problems = check_completeness(
        [entry(131, "2026-09-08"), entry(131, "2026-09-08")], d
    )
    assert len(problems) == 2
    assert any("2026-09-08" in p for p in problems)
    assert any("2026-09-09" in p for p in problems)


def test_an_absent_journal_directory_is_not_a_violation(tmp_path):
    # Absent tool = no guard, never a block (auto-land.yml holds the same line).
    assert check_completeness([entry(1, "2026-07-12")], str(tmp_path / "nope")) == []


def test_completeness_is_independent_of_the_shape_checks(tmp_path):
    # A malformed entry must not also be reported as missing, and vice versa: the two
    # checks answer different questions and the operator needs to know which failed.
    d = write_journal(tmp_path, {"2026-09-08-session-131.md": "# Session 131\n\nbody\n"})
    bad = entry(131, "2026-09-08", move="critique")
    assert check_completeness([bad], d) == []
    assert any("critique" in p for p in check([bad]))


# --- the real repository ---------------------------------------------------------------


def test_the_committed_chronicle_covers_the_committed_journal():
    # Reads what is on disk. If this fails, a session landed a journal day without its
    # self-report and the site's integrate gate will refuse the night.
    path = os.path.join(ROOT, "chronicle.json")
    journal = os.path.join(ROOT, "journal")
    if not (os.path.exists(path) and os.path.isdir(journal)):
        pytest.skip("not running inside the studio repository")
    with open(path, encoding="utf-8") as fh:
        entries = json.load(fh)
    assert check_completeness(entries, journal) == []


# --- a shipped work carries the file the mirror reads first ------------------------------


def works_dir(tmp_path, works):
    """works: {slug: [filenames]} — a slug with no meta.json is the failure under test."""
    d = tmp_path / "works"
    d.mkdir()
    for slug, names in works.items():
        (d / slug).mkdir()
        for name in names:
            (d / slug / name).write_text("{}", encoding="utf-8")
    return str(d)


def test_a_shipped_work_with_its_meta_is_silent(tmp_path):
    w = works_dir(tmp_path, {"2026-10-03-a-work": ["meta.json", "index.html"]})
    entries = [entry(150, "2026-10-03", works=["2026-10-03-a-work"])]
    assert check_shipped_works(entries, w) == []


def test_the_hollow_premiere_of_2026_10_03_is_caught(tmp_path):
    w = works_dir(tmp_path, {"2026-10-03-a-work": ["index.html", "results.json"]})
    entries = [entry(150, "2026-10-03", works=["2026-10-03-a-work"])]
    problems = check_shipped_works(entries, w)
    assert len(problems) == 1
    assert "2026-10-03" in problems[0]
    assert "works/2026-10-03-a-work/meta.json is missing" in problems[0]


def test_a_named_work_with_no_directory_is_caught_the_same_way(tmp_path):
    w = works_dir(tmp_path, {})
    entries = [entry(150, "2026-10-03", works=["2026-10-03-never-written"])]
    problems = check_shipped_works(entries, w)
    assert len(problems) == 1
    assert "2026-10-03-never-written" in problems[0]


def test_a_move_that_is_not_a_ship_puts_nothing_on_the_site(tmp_path):
    w = works_dir(tmp_path, {"2026-10-03-a-work": ["index.html"]})
    for move in ("build", "gauntlet", "verify", "consolidation", "steer", "other"):
        entries = [entry(150, "2026-10-03", move=move, works=["2026-10-03-a-work"])]
        assert check_shipped_works(entries, w) == [], move


def test_every_hollow_work_in_one_entry_is_named(tmp_path):
    w = works_dir(tmp_path, {"a": ["meta.json"], "b": [], "c": []})
    entries = [entry(150, "2026-10-03", works=["a", "b", "c"])]
    problems = check_shipped_works(entries, w)
    assert len(problems) == 2
    assert all("works/a/" not in p for p in problems)


def test_an_absent_works_directory_is_not_a_violation(tmp_path):
    entries = [entry(150, "2026-10-03", works=["2026-10-03-a-work"])]
    assert check_shipped_works(entries, str(tmp_path / "nope")) == []


def test_the_new_check_is_independent_of_the_other_two(tmp_path):
    """A hollow premiere is invisible to the shape and completeness checks — that is why
    the site saw it and this instrument did not."""
    w = works_dir(tmp_path, {"2026-10-03-a-work": ["index.html"]})
    j = write_journal(tmp_path, {"2026-10-03-session-150.md": "# Session 150\n\nbody\n"})
    e = entry(150, "2026-10-03", works=["2026-10-03-a-work"])
    assert check([e]) == []
    assert check_completeness([e], j) == []
    assert len(check_shipped_works([e], w)) == 1
