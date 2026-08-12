# VERIFIER — STILL DARK, premiere gate, session 89

*Blocking voice. Facts and tiers only; no vote on form, staging or worth. Nothing below is taken on
the brief's word, on the record's word, or on a memo's word: every figure here was recomputed, every
sentence read off the built object, every quotation and URL fetched tonight.*

---

## The object, hashed at both ends of this pass

| | at start (18:26 UTC) | at end (18:47 UTC) |
|---|---|---|
| `projects/season1/still-dark/index.html` | `7c9d100291dcd312950b5463ec62a3715630ce700397cc90022d4a65f0838fbe` | `7c9d100291dcd312950b5463ec62a3715630ce700397cc90022d4a65f0838fbe` |
| `projects/season1/still-dark/README.md` | `fd1d52b2f53e602ab57dab629a61bd25d5676949f9dbb089f0d58f534ec26408` | `fd1d52b2f53e602ab57dab629a61bd25d5676949f9dbb089f0d58f534ec26408` |

**Neither object moved.** HEAD was not moved, nothing was committed, nothing was staged. `git show
HEAD:` was never used to obtain the object; the working tree was read directly, and HEAD is
confirmed one build behind it (`git diff` against `baaeb13` is the whole of session 89's change).

**But three files beside the object DID move under this pass, and it is banked below as N7:**
`render-1400.png`, `render-900.png`, `STATE-1.txt` and `RENDERS.json` were all rewritten at
**18:41:49–18:41:51 UTC**, in the middle of this measurement, by a run of `render.mjs` that this
voice did not make.

## What was run

```
sha256sum projects/season1/still-dark/{index.html,README.md}          (start and end)
git log --oneline -5 · git status --porcelain · git diff -U1 projects/season1/still-dark/index.html
cd projects/season1/capture
  python3 day.py 2026-08-04
  python3 day.py 2026-08-04 --as-of <each of the nine stop instants>
  python3 day.py 2026-08-04 --as-of 2026-08-12T04:36:39Z      (the eight-stop state, for comparison)
  python3 edition.py · python3 sessions.py
cd projects/season1/still-dark
  python3 data.py --check
  NODE_PATH=/opt/node22/lib/node_modules node announce.mjs · node gaps.mjs
cd /home/user/studio
  NODE_PATH=... node tools/fold.mjs   · node tools/frame.mjs · node tools/tiers.mjs   (exit codes taken
                                                                without a pipe — see N4)
  python3 tools/renders.py
```

Written by this voice and deleted again: one throwaway playwright driver, which loaded
`index.html` at 390×844, stepped `__sdArrive.show(i)` through all **nine** stops, and read back the
figure, the fraction, the standing figure, both name blocks, the hedge and the seven fixed
paragraphs from the live DOM. The prose findings below are read off the driven page and off
`STATE-1.txt`, not reasoned from the record.

Also written directly against the captures: an independent re-implementation of the two counts in
`arrive.since_note`, using `day.py`'s own `analyse()` and `bands()`, and a cross-check of all 35
vessel rows on the face — name, flag, waters, GFW id — against `captures/*.json`.

## What was fetched

| URL | result |
|---|---|
| `https://frankbueltge.de/ghost-fleet/` | **200**, 31,635 bytes, sha256 `14ddeb5c9953…` — **byte-identical to tonight's capture** |
| `https://frankbueltge.de/werke/ghost-fleet/` | 200, 27,046 bytes — all three quoted strings found verbatim |
| `https://biblio.ugent.be/publication/8647789` | 200 — Brysbaert 2019, *How many words do we read per minute?*, 238 wpm confirmed |
| 35 × `https://globalfishingwatch.org/map/vessel/…` | **35 of 35 → 200** |
| `https://paglen.studio/2020/05/22/the-other-night-sky/` | 200 |
| `https://watchthemed.net/` | 200 |

**No cited URL is dead.**

---

# VERDICT

## **FAIL — five blocking, eight noted.**

Three of the five are on the work's own face. The premiere does not go through them.

The arithmetic is not one of them. Every share, every fraction, every total, every count of copies,
lists, contents and bodies on this face is correct and reproducible tonight. What fails is a
sentence that describes a future that has already happened, a pair of numerals that arrived tonight
into a scope carrying the wrong tier word, a word — *tonight* — that has meant four different nights,
and a live record two figures and one regression behind its own object.

---

# BLOCKING

## 1. The face says a list "would be" the first to rule a name out. That list is in this record, and the same sentence already counts what it did.

**Open:** `projects/season1/still-dark/index.html:723` (data island, `arrive.since_note`) · rendered
at `#sd-arrive-since-note` · `projects/season1/still-dark/STATE-1.txt:56` · generated at
`projects/season1/still-dark/data.py:836-838`, from `data.py:443`.

The sentence, as a stranger reads it tonight:

> *"…so the return window of twenty-two of the twenty-four names added since 4 August still reaches
> back to it. **The first list that could add a name ruled out of that list would be one dated
> 12 August 2026.**"*

The list dated 12 August 2026 **arrived tonight**. It is in `projects/season1/captures/2026-08-12T182312Z.json`;
it is row 26 of this page's own ledger (`STATE-1.txt:356`); it is stop nine of this page's own run,
labelled `+8 DAYS`; and this page's own caption two blocks higher says *"Nine lists, nine answers,
one day — the last of them eight days after the day had ended."*

It did exactly what the conditional says it would do. I computed it from the captures, not from the
sentence: of the twenty-four names added since 4 August, **twenty-two** have return windows reaching
back to 4 August and **two do not** — `ISABELLA` and `LUCKY TJ`, both `resurfaced_between
2026-08-05 … 2026-08-12`, both first seen in the edition of 12 August. Those two are the names ruled
out of the list of 4 August, and they are the entire reason the first clause of that same sentence
changed tonight from *"every name"* to *"twenty-two of the twenty-four."*

So **one sentence reports the consequence and the next still calls the cause hypothetical and
future.** The generator makes this structural rather than accidental: `first_excluding` at
`data.py:443` is `DAY + window_days + 1` — a constant — and the string at `:838` has no branch on
whether a capture of that edition exists, while the clause above it at `:831-835` does branch. One
half of the sentence was built to move and the other was not.

This is **banked failure 42** in its own words: *a conditional carried by one of two sentences about
the same fact is a false sentence with a delay fuse in it.* The fuse was lit tonight. The house's own
comment at `data.py:435-438` predicted the date it would go off — *"the first edition whose additions
could be ruled out of it is one dated 12 August… a number that must come out this way until a given
date is not evidence until that date has passed"* — and the date passed at 18:23 UTC.

**Smallest repair that discharges it:** one branch, beside the one already at `:831`. When a capture
of `first_excluding` exists, the sentence must be in the past tense and must name what it did —
e.g. *"The first list that could rule a name out of that list is the one dated 12 August 2026, and
it has arrived: two of these names are ruled out of it."* Nothing else in the string needs to change.

---

## 2. Two numerals arrived on the face tonight into a paragraph whose only tier word is SOURCED, and it is not their word.

**Open:** the same string, `index.html:723` / `STATE-1.txt:56`, against the tier line four lines
above it at `STATE-1.txt:54` (`#sd-arrive-cut-tier`, island `arrive.cut.tier`).

Tonight's build replaced *"the return window of **every name** added since 4 August"* with *"the
return window of **twenty-two of the twenty-four** names added since 4 August"*
(`git diff` at `index.html:722-723`). Two figures where there were none.

The reading order the page actually delivers, taken off the built page:

```
:54   SOURCED — the three figures the list published, read off the saved copies in the words the
      parser matched in them. The count of names, and the count of lists below, are this house's own.
:56   This record cannot tell a ship … twenty-two of the twenty-four names added since 4 August …
:58   Each of the nine lists this record holds prints six to eleven names of the 189 to 257 …
:62   DERIVED — this share is worked out here, from saved copies of those lists. Nobody publishes it.
```

The only tier word standing over line 56 is **SOURCED**, and these two counts are not sourced from
anything. They are this house's own arithmetic over nine editions and twenty-six saved copies —
`later` and `not_ruled_out` at `data.py:440-442`, computed from `day.py`'s `bands()`. Upstream
publishes neither, and could not: neither figure exists until a record has accumulated nine lists.

The exception clause on line 54 does not reach them. *"The count of names, and the count of lists
below, are this house's own"* was written for **line 58** — the count of lists (*nine*) and the count
of names (*six to eleven*) are both in that sentence, and *below* is doing the pointing. Line 56 was
numeral-free when that clause was written. It is not numeral-free any more, and nothing was added to
cover it. `arrive.tier`'s **DERIVED**, two paragraphs lower at line 62, names *"this share"* — the
percentage — and not these.

This is the third appearance of the house's own cardinal sin in the same block. **Banked failure 49**
recorded it by subtraction — a cut left *eleven ships named* under a bare `SOURCED`. Tonight it is by
**addition**: new derived numerals placed into the one paragraph of that block the SOURCED exception
was not written to cover. The constitution's rule is exactly on point: *a tier word is never
inherited from a neighbouring element.*

**The counter-argument, stated fairly so the house can weigh it:** *"twenty-four names"* is arguably
"a count of names", and the exception on line 54 says the count of names is this house's own. I have
weighed it and it does not save the string. The legend on the same page defines the DERIVED count of
names narrowly — *"the count of names in each list"* (`index.html:2763`) — and twenty-two-of-twenty-four
is not a count of names in a list; it is a count of vessels across the accumulation, which is this
work's **OBSERVED** register. A reader has to choose between two readings of a forward pointer to
learn which tier two numerals carry. That is the ambiguity this gate exists to refuse, in the block
where this house has already shipped the same defect twice.

**Smallest repair that discharges it:** one clause on the end of the first sentence — *"— both counts
are this record's own, worked out here from the saved copies"* — carrying whichever of DERIVED /
OBSERVED the house rules correct. Alternatively, move `#sd-arrive-since-note` below
`#sd-arrive-tier` in the DOM. Either is one line in `data.py`.

---

## 3. "Until tonight" has now meant four different nights, and it is on the face twice.

**Open:** `index.html:730` (`arrive.cut.kept`, generated at `data.py:944-951`) rendered at
`STATE-1.txt:58`; and the ledger caption, generated at `data.py:1458-1463`, rendered at
`STATE-1.txt:327`.

> `:58`  *"This record has saved that block every night since the first, and no face of this work
> printed one of its figures **until tonight**."*
>
> `:327` *"…a figure this record has saved every night since the first and, **until tonight**,
> printed never."*

Both were true when they were written, in **session 85**. Both are false on the face a visitor loads
tonight. This face has printed those figures on every build since 85 — sessions 86, 87, 88 and 89 —
so *"no face of this work printed one of its figures until tonight"* is refuted by four earlier faces
of this work, one of which is the commit at `HEAD`.

These are not tier failures and not arithmetic failures. They are the shape this house banked as
failures 24 and 28 and caught again in `VERIFIER-87.md` §8: **a session-relative word frozen into a
string that outlives the session.** The rest of both sentences is computed and correct; only the
adverb is a hand.

I searched the memos of 86, 87 and 88 for a prior ruling that keeps these words deliberately. There
is none.

**Smallest repair that discharges it:** delete two words from each string. `data.py:951` ends
*"…and no face of this work printed one of its figures until tonight."* → *"…and no face of this work
printed one of them before this one did."* `data.py:1463` ends *"and, until tonight, printed never."*
→ *"and did not print until this face did."* Neither touches a figure.

---

## 4. The live record publishes a share the face contradicts by two points, a stop count short by one, and a fall count short by one.

**Open:** `projects/season1/PROJECT.md:31-37`.

> *"**As of session 88: 33 %–100 % — 11 of 2–33**, from **25 saved copies** holding **8 distinct
> lists** (9 contents, 15 bodies). … The figure was 100 %, 79 %, 69 %, 65 %, 55 %, 44 %, 37 % and 35 %
> before its present value … **and it has fallen six times from later lists**, on 6, 7, 8, 9, 10 and
> 11 August."*

Measured tonight, first-hand, `python3 projects/season1/capture/day.py 2026-08-04`:

```
day 2026-08-04  ·  26 capture(s) read, 9 distinct edition(s), 10 distinct content(s), 16 distinct bod(y/ies)
  SHARE knowable on the day ......... 31%–100%  (11 of 4–35)
```

Six figures in that passage are behind the object: **33 → 31**, **2–33 → 4–35**, **25 → 26 copies**,
**8 → 9 lists**, **9 → 10 contents**, **15 → 16 bodies**. The list of prior values now needs `33 %`
appended, and the fall list is **seven** falls, not six — 12 August joins 6, 7, 8, 9, 10 and 11.

I accept that `As of session 88` is an honest stamp and that this record is normally written at the
end of a session. It is nonetheless blocking **at a premiere gate**, because this file is headed
*"the live project record"* and its section *"The number, and how a stranger checks it"* is the place
the record sends a stranger for the current number. A premiere cannot ship with the record's headline
figure two points from the work's own face.

**Smallest repair that discharges it:** the six figures, the appended `33 %`, and `12 August` on the
fall list. Every one of them is printed by the command already quoted three lines above it.

---

## 5. The record says item (y)'s second span is GREEN. Tonight's build took it red, and nothing failed.

**Open:** `projects/season1/PROJECT.md:151` — *"**(y)'s SECOND SPAN IS GREEN — 786 px of 844, from
867.** … the first time in this work's measured life"* — against `projects/season1/PROJECT.md:158-160`
(`OWED AFTER 88`), which lists `(B)`, `(v)` and the 37-word heading and **does not list (y)**.

`NODE_PATH=/opt/node22/lib/node_modules node tools/frame.mjs`, run on the object under test:

```
phone 390×844 — figure-top to controls-bottom: 358 px of 844 — HOLDS
  figure-top to hole-bottom: 849 px of 844 — OVER by 5
```

786 → **849**. The two chips the ninth list added — `ISABELLA · USA` and `LUCKY TJ · USA`, both
present on the driven page and both carrying `sd-arrive-new` — added the rows that pushed it over.
The item the record calls green for the first time in the work's measured life went red on tonight's
build, and **the record carries no entry saying so**.

Nothing exited non-zero, and that is by design rather than by fault: `tools/frame.mjs:70-71` states
its exit contract explicitly — *"It does NOT change this file's exit contract: the frame test still
decides the exit code, and this span is reported red or green"* — so `frame.mjs` prints `OVER by 5`
and exits **0**, and its closing line, *"FRAME: the figure and the controls fit one screen at every
stop"*, is true of the first span only.

**I have no vote on whether five pixels should be paid, or how.** What is blocking is the record:
the live file asserts a green measurement that the instrument refutes on the current object, and
lists nothing owed against it.

**Smallest repair that discharges it:** one line in `PROJECT.md`, recording that the ninth list took
the second span from 786 to 849 of 844, and either re-opening (y) or stating in the record that the
regression is accepted. The claim of green must not stand.

---

# NOTED — not blocking

**N1. The eight-of-eight this house got right, and it is most of the object.** Every figure on the
face is computed and reproducible. `python3 data.py --check` → *"island matches the captures."* All
**nine** stops reproduce first-hand under `day.py --as-of`: 100, 79, 69, 65, 55, 44, 35, 33, **31** at
`2026-08-05T04:39:32Z`, `…05T12:54:00Z`, `…06T08:16:42Z`, `…07T18:15:53Z`, `…08T21:37:19Z`,
`…09T20:36:58Z`, `…10T22:41:12Z`, `…11T11:19:15Z`, `…12T18:23:12Z`. The nine fractions `11 of 11 · 14 ·
16 · 17 · 20 · 25 · 31 · 33 · 35` are exact against those runs. The new figures the brief named all
check: **31 %**, **4**, **35**, **26 captures**, **9 editions**. `fall.moved`'s *"fell thirty-eight
points"* is 69 − 31 ✓; its enumeration is 1+3+5+6+2+2 = **nineteen** ✓; the lede's *"Twenty-four
arrived later — nineteen of them after this page had printed its figure"* ✓; `cut.kept`'s **189 to
257** is exactly min/max of `disappearances_examined` across the nine editions ✓; the ledger caption's
**"Six lists came back in more than one set of bytes each"** is right and is computed by *content*
hash, not edition date, which is what makes the *"every field this page reads stayed identical"* half
of it true ✓; `run_states.waiting`'s *"nine states over about twenty-seven seconds"* is
`round((14118 + 8×1600)/1000)` ✓; the first dwell **14,118 ms** is 56 gloss words ÷ 238 wpm ✓, and 56
is the count under the house's own rule that a word is a token containing a letter or digit ✓.

**N2. `11 of 230` did NOT move to 257, and that is the single most important thing this build got
right.** `arrive.cut.standing` = `11 of 230`, verified against
`captures/2026-08-05T043932Z.json` — `vessels` length 11, `aggregates.disappearances_examined` 230 —
which is the only committed copy of the 4 August edition. `arrive.cut.figures` likewise stays pinned:
*"Of the 230 examined, 82 were dark inside national waters · 5,641 events in the window"*, all three
from that same file. The 12 August edition's 257 / 94 / 5,804 appear **only** in the ledger row and in
`cut.kept`'s range, where they belong. Driven through all nine stops, the standing figure reads
`11 of 230` at every one of them.

**N3. `tools/fold.mjs` — 99 failures, exit 1, and ZERO occlusions.** Confirmed against the brief and
against `KRITIKER-84.md` condition 2. The count is 11 per stop × 9 stops, against 11 × 8 = 88 last
night — the ninth stop adds a row to the grid, exactly as the record says; it is not a new defect.
Every counted failure is the controls or the run's line leaving the viewport at deep scroll on the
phone; **not one line in the whole run printed `✗COVERS`**. The guard does hit-test the material —
`fold.mjs:105-113` walks `#sd-arrive-names-since li, #sd-arrive-names-then li` and asks
`elementFromPoint` at each chip's centre whether a must-hold element is painted on it. So
**KRITIKER-84's second condition is discharged and verified tonight**: nothing occludes the names at
any of 9 stops × 9 scroll positions at 390×844, and the instrument that must fail if it did, exists
and would.

**N4. An exit code taken through a pipe is not an exit code.** My first run of `fold.mjs` reported
`EXIT=0` because `$?` after `node … | tail -30` is `tail`'s. Re-run without the pipe, `fold.mjs`
exits **1**, as its own contract says it should. I record this because a memo that certifies a red
instrument as green would be this house's failure 79 — *an instrument you built is not a check you
ran* — with an extra step.

**N5. `tools/tiers.mjs` cannot see the class of figure this build just added.** It reports every
scope carrying a tier word and exits 0, and its own closing line disclaims the rest: *"Scope is
structural, not semantic: this says a tier word is present, never that it is the right one."* Worse
for blocking item 2, its figure-matcher is digit-based: across the whole since-note string it
extracted only `4 · 12 · 2026.` — it never saw **twenty-two** or **twenty-four**, because this house
spells its counts in words. The instrument nearest to the cardinal sin is blind to any numeral
written as a word. Not a finding against tonight's build; a finding about what the instrument can
promise.

**N6. Every claim about a named third party traces to the saved capture or to a live source.** All
**35** vessel rows on the face — name, flag, waters, GFW id — were matched against `captures/*.json`
programmatically; **35 of 35 trace**, with the two `case_of_the_day` vessels (`TUNAMAR`,
`HY928-21%-81%`) carrying their waters in the capture's `prose` rather than in a `waters` key, which
is `day.py`'s documented `case_waters` path and not a gap. All three upstream quotations are verbatim
on the live method sheet, fetched tonight: *"The index counts all examined; the case and list show
named vessels"*, *"Daily. Window: disabling events that ended in the last 7 days…"*, *"The AIS picture
of the seas looks complete…"* The face's `≥ 12 h / ≥ 50 nm` definition matches upstream's *"GFW returns
only high-confidence, intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore."* **Upstream's
restraint is repeated on the face twice** — once in the head (`#sd-arrive-restraint`) and once in the
foot (`#sd-restraint`), from one string, so the two cannot drift — and it matches upstream's own *"No
claim of illegality against vessel or state"*. **No claim of illegality is made anywhere on this face
against any vessel or state.**

**N7. The sighted material moved under this pass — and the brief's premise about the em dash is
wrong.** Two separate things, both worth the house's attention:

*The movement.* `render-1400.png`, `render-900.png`, `STATE-1.txt` and `RENDERS.json` were rewritten
at **18:41:49–18:41:51 UTC**, between two of my own tool calls, by a run of `render.mjs` I did not
make. `render-1400.png` went **846,666 → 851,165 bytes**, `bbede67405ef…` → `2410c85f67ab…`, and
`RENDERS.json` was updated to match it. `STATE-1.txt` and `render-900.png` came back byte-identical.
`index.html` and `README.md` did **not** move — I hold both hashes. `python3 tools/renders.py` exits 0
and confirms `index_sha256` = `7c9d1002…`, so the new render is of the object under test and the
panel material is not stale. But this is the shape of **banked failure 39** (*this house edited an
object under the voices judging it*) and **47** (*this house moved HEAD under the two voices judging
its object*), a third time: the committed sighted material of the work changed while the gate was
measuring it. It is noted rather than blocking only because the objects I was told to hold did not
move and the render is of the same page. Two things follow. First, the 1400 px render is not
byte-reproducible — the same page rendered twice gives two hashes — so `RENDERS.json`'s guarantee for
that file is weaker than its own note claims. Second: **nothing may touch this directory while a
gate is open.**

*The em dash.* The brief asks me to confirm "the em-dash rendering of the empty flag is marked as the
work's own." **I refute that.** It is upstream's, the face says so, and the face is right. The live
page fetched tonight prints, literally:
`HY928-21%-81% <span class="font-mono text-sm text-fg-faint">(—)</span>`, and its prose reads *"A
vessel flagged — switched off its transponder for 50 days"*, against the flagged template *"A vessel
flagged ESP switched off its transponder for 37 days"* — so the em dash stands in the flag's own
position and is not sentence punctuation. `capture/capture.py:82-86` matches it and records `flag:
null`; the island keeps `null` (`index.html:971`); `flagText()` (`index.html:2449-2451`) prints `—`;
and the face's SOURCED legend says *"…printed here unrepaired: one name arrives with a machine's
percentages inside it and no flag, and '—' is what the list shows in that place."* That is true and
supported by the saved bytes. **The damaged name stands unrepaired everywhere** — in the capture, in
the island, in the chip (`HY928-21%-81% · —`, read off the driven page), in the field row, in
`fall.moved` — and the face says plainly whose damage it is. *One latent risk, for a later night, not
a finding tonight:* `flagText()` returns `—` for **any** null flag, not only this one, so the first
flagless vessel upstream renders differently would be given an em dash this record never saw. The
tier word covering that string is SOURCED. One vessel exists in that state today and it is
corroborated.

**N8. `README.md` is two sessions behind, and one of its sentences is now false in the present
tense.** `still-dark/README.md:41`: *"…all twenty later names have return windows reaching back past
4 August, so all twenty are names a longer list dated 4 August could have carried."* Tonight it is
**twenty-two of twenty-four**, and two names — `ISABELLA`, `LUCKY TJ` — are ruled out of that list.
The sentence is a report of `VERIFIER-85.md` §4 and sits inside a session-85 paragraph, which is why
this is noted and not blocking; it is nonetheless written in the present tense about a quantity that
has moved, and the fact it reports has changed materially — this is the first night any later name
could **not** have stood in the list of 4 August. `README.md:67`, `:502` and `:607` carry
session-stamped counts (`23 saved copies`, `8 lists`, `33 %–100 %`, `11 of 2–33`) which are honest as
history but mean the work's first-read document does not mention the ninth list at all. The refusal
on the face (`cut.refused`) is unaffected and remains true: it says a longer 4 August list *could*
carry names counted as late, not that all of them could.

---

## What I could not fault, and looked for

- `arrive.constant` — *"The upper end holds at 100 % until more of these ships are certainly dark on
  this day than the eleven the day itself named"* — this house's most expensive sentence, twice
  published false. It is **true tonight**: certain = 4, and 4 < 11, so the fixed end stays `–100 %`.
  Verified against `day.py`'s own upper-end arithmetic (`obs / max(n_lo, obs)` = 11/11).
- The hedge at every stop. Stops 0–6 read *"not one of these names is certainly dark"*; stop 7
  *"two…"*; stop 8 *"four of these names are certainly dark on this day and the rest are possible."*
  All three are computed and all nine are correct for their own stop. No hand typed any of them.
- `heading_since` at stop 9: *"twenty-four ships … The last two, in darker ink, arrived with the list
  of 12 AUG."* Driven: 24 chips, the last two carrying `sd-arrive-new`. ✓
- `KRITIKER-84.md` condition 1 — discharged and verified independently: the face prints *"WHAT THE
  LIST OF 4 AUG WAS THE TOP OF"*, *"Of the 230 examined, 82 were dark inside national waters · 5,641
  events in the window"*, `11 of 230`, and the heading now reads *"the eleven names it printed"*. The
  refuted *"all that the day held about itself"* is gone from the object.
- The scale under the field adapts to `dataEnd` and now carries an `11 AUG` tick with the bands
  running to 12 August; no axis was left short by the new rows. `gaps.mjs` PASS, `announce.mjs` 3
  spoken announcements and 10 figure rewrites in a 27 s run, both exit 0.
- The ninth capture is genuine and current: HTTP 200, 31,635 bytes, 10 vessels, edition 12 August, and
  the live page fetched at 18:44 UTC is **byte-identical** to it.

---

*This memo is published with the work, pass or fail. The five blocking items are cheap: two branches,
four deleted words, six figures and one line of record. Not one of them asks this work to be a
different work. Item 2 is the one that matters — this house's only stated value is that a tier word
means what it says, and tonight a build put two numbers under the wrong one by adding them where the
exception did not reach.*
