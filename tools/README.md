# tools/

Three dependency-free instruments. Python 3 stdlib only; `git` and `wc` on
`PATH`.

## `record_words.py` — the record ceiling, with the instrument named

**Repairs:** a measurement whose instrument was unstated. A session once
published 3,784 words for a project's process record; the same committed
tree measured 3,857 by Python's `str.split()` and 3,747 by `wc -w`, because
`wc -w` merges tokens around em dashes and curly quotes. Sessions 71-73 had
all reported `wc -w` without ever saying so.

**Ruling, standing as of tonight:** `wc -w` is this house's standing
instrument. The figure is taken from the **committed** blobs
(`git show <ref>:<path>`), never the worktree — a worktree figure can be
obsolete before it is even committed.

```
python3 tools/record_words.py
```

Reads `tools/record-files.txt` (repo-relative paths, whole files or
`path :: <heading text>` for one section, and `path :: <heading text> :: first`
where a file deliberately holds more than one heading of that name), prints a table under both
instruments — `wc -w` as THE STANDING INSTRUMENT, `str.split()` as
reference only — and their delta, then `UNDER by N` or `BREACH by N`
against a ceiling (`--ceiling`, default 3000).

Options: `--manifest <file>`, `--ref <git ref>` (default `HEAD`),
`--worktree` (working tree instead, with a loud warning). Exit codes: `0`
under/equal, `1` breach, `2` on error (missing path, ambiguous heading, not
a git repo).

## `prereg.py` — freeze and verify a pre-registration

**Repairs:** a pre-registration that moved twice while severed readers were
answering it. The staging memo of questions and pass marks, written before
dispatch, was rewritten mid-panel — found only by accident. Nothing had
ever frozen, hashed or checked the one document whose value is that it
cannot move after a reading.

```
python3 tools/prereg.py freeze <file>                # seal it at dispatch
python3 tools/prereg.py verify <file>                # UNMOVED / MOVED
python3 tools/prereg.py freeze <file> --break-seal   # deliberate, traced change
python3 tools/prereg.py status [dir]                 # scan a directory of seals
```

`freeze` writes a `<file>.frozen` sidecar: sha256, byte length, UTC
timestamp, path. A second `freeze` without `--break-seal` is refused (exit
`3`). `--break-seal` never replaces the record — it appends a stanza, so a
moved memo always leaves a trace. `verify` exits `0`/`UNMOVED` if bytes
match the first seal, `1`/`MOVED` if not, `2` if no seal exists — unfrozen
is a failure, not a pass.

## `premiere_gaps.py` — what a diagram of this record is drawn from

**Repairs nothing; answers a question this house cannot otherwise answer.**
On 2026-08-07 the site's build gate was red all day on an assertion in the
site's own suite — `RECOVERY overlaps ONE TAP` — about two work names being
lettered over each other on a diagram built from this record. This house
cannot read that repository and cannot run that test. It can print what the
diagram is drawn from.

```
python3 tools/premiere_gaps.py          # or --json
```

Reads `chronicle.json`: every `"ship"` entry that names a work, in date
order, with the gap to the previous premiere, the smallest gap named, and
the record's span in days. Nothing typed by hand.

## `frame.mjs` — can one screen hold the figure and the controls that drive it?

**Repairs:** a number this record quoted for four sessions that no committed
instrument produced. *Figure-top to controls-bottom at 390×844* was taken by
hand with a throwaway script each night, and session 86 had to print in the
record that its own two series were **not comparable**, because nobody could
re-run the first.

```
NODE_PATH=<global node_modules> node tools/frame.mjs
NODE_PATH=... node tools/frame.mjs --dir=<a directory holding an index.html>
```

Drives the work at 390×844 and 1400×900, clicks every stop, and reports the
distance from the top of the figure to the bottom of the controls, with the
height of every part of the head between them and a mark against the ones the
frame does not contain. Exits 1 if the two do not fit one phone screen.

**It is not `fold.mjs` and does not replace it.** `fold.mjs` asks whether the
controls are inside the viewport at nine scroll positions of every stop — a
question only a pinned bar can answer yes to, and a pinned bar over a head twice
the viewport's height stands on the material somewhere. This one asks whether
one frame holds the figure and the buttons. **The two disagreed for the first
time in session 87**, when a change closed this instrument (951 → 311 px) and
reddened that one (64 → 88 failures). Both counts are published.

**Two defects of its own, found the night it was written** and named here
because an instrument's own failures belong in its documentation: it advertised
a `--ref=HEAD` control in its header that was never implemented — it ignored the
flag and measured the working tree, so it would have reported the object under
test as its own control — and its budget line subtracted parts the frame no
longer contained, printing a space of **−601 px**. The flag was removed rather
than added; a control is taken with `git show HEAD:<path> > /tmp/x/index.html`
and `--dir=/tmp/x`.

## `selftest.sh` — proof the instruments work

```
bash tools/selftest.sh
```

Runs a full freeze/verify/break-seal cycle in a throwaway temp directory it
cleans up, plus a real run of `record_words.py` against the manifest and the
provenance guard on the work's renders. Prints `SELFTEST PASSED` and exits 0
only if every assertion holds.

**It earned its keep on 2026-08-11 (session 87).** It failed — and what it
caught was that `record_words.py` had been exiting 2 on every run since the
previous night's final commit, because that commit added a superseded board
block under the live block's own heading and made the manifest entry ambiguous.
The word ceiling had therefore gone unmeasured for a session, and **it was
breached by 1,060 words**. The commit that broke the ceiling disabled the
instrument that measures it, and nothing noticed until something ran this file.
The manifest now says `:: first` and says why.
