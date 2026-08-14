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

## `width.mjs` — does the page ever stand wider than the window it is in?

**Repairs:** banked failure 55, and it is the only one of this house's failures
that was found by a voice sweeping by hand where no instrument of ours has ever
looked. Session 86 stopped the work scrolling sideways inside a 390 px phone,
scoped the repair to a 480 px media query, and wrote the reason into the file.
The page went on standing 665 px wide at **every width from 481 to 664 px** —
184 of them, overflowing by up to 38 % of the window — for six sessions, unseen
because every guard and both committed renders read only the widths the
pictures are taken at.

```
NODE_PATH=<global node_modules> node tools/width.mjs
NODE_PATH=... node tools/width.mjs --dir=<a directory> --lo=280 --hi=1920 --step=5
```

Resizes one page across the band, asks at every width whether the document is
wider than the window, walks the ends of any overflowing band at 1 px, and names
the widest element crossing the window's right edge with its computed
`min-width`. Exits 1 if any width overflows. A 280→1920 sweep in 5 px steps
takes about 15 seconds.

**Checked against the defect it was written for.** Pointed at the object session
92 was frozen on (`git show b619af4:projects/season1/still-dark/index.html`), it
returns `OVERFLOW 481→664 px (184 widths), worst +184 px` — the staging voice's
hand sweep, reproduced by a machine. **The element it names is the widest
symptom, not the proven cause**: there it names the `table`, where the voice,
hit-testing every unclipped element, named a `span` with `min-width: 292.089px`
inside that table. Both true; one of them is the thing to edit.

**What it does not reach:** it reads the page at rest, at its first stop. A
sideways scroll only a later stop can produce is outside it.

## `turn.mjs` — at the beat where the run turns, what actually moves?

**Repairs:** an order written in arithmetic that this house could otherwise
only answer with a preference. `DRAMATURG-92.md` cut 2 measured the turning
numeral at **8.0 % of everything that changes at the final beat** and ordered
the frame reweighted around it; half was paid in session 92, and the owed half
is a proportion judgement on a state that the same night's arithmetic
correction had already changed.

```
NODE_PATH=<global node_modules> node tools/turn.mjs
NODE_PATH=... node tools/turn.mjs --dir=<a directory> --width=390,1400
```

Reads every live node of the head and the hole at the second-to-last stop and
again at the last, reports each rewritten node's area as a share of the total in
motion, and prints the same figure over the four nodes that memo counted, so the
two numbers are comparable without hand arithmetic.

**Checked against the memo, and the limit of the check is printed in the file.**
On the last committed object before session 92 it returns the share at
**12,961 px²** and the fraction at **2,774 px²** — that memo's figures to the
pixel — and it does **not** reproduce the other two, because the object the memo
drove had the tenth list's island built into it and was never committed in that
state. Two of four, on the two nodes that did not change between the states.

**Area is a proxy for emphasis and this instrument says so:** a big pale word
and a small black one can carry the same weight on a page. It answers the memo's
question in the memo's units.

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
