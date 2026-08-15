# KRITIKER-95 — STILL DARK, 4 August 2026, the sixth premiere gate

**2026-08-15.** *Published with the work, pass or fail, unedited.*

Object hashed at the start of this pass: `projects/season1/still-dark/index.html` sha256
`52215bf99c098c7d6692adefebf99384e2b49d8b0c586427324605bdc4ebe1bc`. `git rev-parse HEAD` =
`1dae228c734b493e685711dd328b747f54f96fe5`, working tree clean, zero modified files.

**MOVEMENT: NONE.** Hashed again at the end of this pass: the same sha256, the same `HEAD`, no
modified file. The only change to the working tree across my pass is two new untracked memos of
tonight's gate — this one and `VERIFIER-95.md`, written by another voice while I measured. **The
object did not move under me and I did not move it.** I wrote no file in this repository but this
one; everything I fetched went to `/tmp`.

---

# § VERDICT: BLOCK

**This work's numerator is eleven because this record has no list older than the day it measures.
The face says the eleven cannot move, and says so about later nights only. An earlier night can
take names out of it — the instrument that publishes the figure has the rule written into it — and
the one day this work holds open is the only day in its whole record where that subtraction is
zero.**

And the record can already show what that is worth. Same instrument, same command, four consecutive
days of the same sea, each matured by exactly eight days, run by me tonight:

| day | as of, the instant this record first held the list dated eight days later | share knowable on the day |
|---|---|---|
| **4 August 2026** — the published day | `2026-08-12T18:23:12Z` | **31 %–73 %** (11 of 15–35) |
| 5 August 2026 | `2026-08-13T17:02:56Z` | **10 %–25 %** (3 of 12–31) |
| 6 August 2026 | `2026-08-14T20:45:26Z` | **6 %–15 %** (2 of 13–32) |
| 7 August 2026 | `2026-08-15T04:36:57Z` | **3 %–12 %** (1 of 8–33) |

```
python3 projects/season1/capture/day.py 2026-08-05 --as-of 2026-08-13T17:02:56Z
python3 projects/season1/capture/day.py 2026-08-06 --as-of 2026-08-14T20:45:26Z
python3 projects/season1/capture/day.py 2026-08-07 --as-of 2026-08-15T04:36:57Z
```

Four days, one committed instrument, no new night of waiting, no new code. The work publishes the
top row and prints, in the line under its own date, *"one day of the sea, and how much of it was
knowable on the day itself."* On the record's own arithmetic the next three days of that same sea
run between three and ten times lower.

## Why the top row is the top row

`capture/day.py`, `index()`, in the docstring the house wrote itself: *"One row per distinct vessel,
carrying its first sighting in OUR record… Earliest edition date wins."* `bands()` then takes each
vessel's week-wide return window **from that first edition date**. A vessel that already stood in an
earlier list this record holds is pinned to the earlier list's window, and so cannot be dark on any
later day — correctly, because upstream's own rule is that a list carries returns from the last
seven days.

The consequence has never been printed. **Count the names that are new to this record in each of the
twelve lists it holds, against the length of the list they arrived in:**

```
04 AUG  11 names, 11 new     08 AUG   6 / 3      12 AUG  10 / 2
05 AUG   8 names,  3 new     09 AUG   9 / 5      13 AUG  11 / 7
06 AUG   7 names,  2 new     10 AUG  11 / 6      14 AUG  11 / 4
07 AUG   6 names,  1 new     11 AUG  11 / 2      15 AUG  11 / 3
```

Across the eleven lists after the first, **63 of 101 name-slots — 62 % — were already carried by an
earlier list.** Exactly one list in twelve has a repeat rate of nought, and it is the one this
work's numerator is taken from, for the one reason that nothing in this record precedes it.

The Ghost Fleet is a daily instrument. Lists dated 1, 2 and 3 August 2026 were published and this
record does not hold them. **On this record's own rate, some of the eleven had almost certainly
already stood in one of them** — and every such name, under the rule above, would have been pinned
to a window ending before 4 August, would have left the day's *possible* set, and would have left
the numerator. This record cannot say how many. That is a fair position. **What is not fair is the
face:**

> *"The eleven did not move, and cannot. No later night can put a name into a list that did not
> carry it."*

Both sentences are true. Together they are read as a statement that the eleven is fixed, and it is
fixed in one direction of time only. **A work whose entire subject is that a record looks complete
until later evidence arrives has published a numerator that looks complete because earlier evidence
is missing, and has printed the immovability of it eleven times without once naming the direction
the clause holds in.** This is the same defect the last five gates found, in its purest form yet: a
sentence about the arithmetic that is true of the half the house checked.

## Why this is the block and not a note

Because it is not a hedge, and I am not ordering another one. Take the finding the other way round
and it is the strongest thing this work has never said. **A register that records an event only when
it resolves does not merely under-report the present — how badly it under-reports depends on the
day, and this record can show four days that differ by a factor of ten.** That is a property of the
register, not of one calendar date; it is measurable tonight; it needs no wall label; and it is the
one limb of the line this work has never used.

Two predecessors ruled the machine's *repetition* limb **failing** (`KRITIKER-93`: *"Repetition —
fails"*). `KRITIKER-93` then wrote the paragraph that names what is missing — *"not once does the
page say what class of thing it has just measured"* — and declined to order it, on the ground that
ordering a house to write a claim it has not measured is how this file got three of its banked
failures. That reasoning was right then and is spent now. **The claim no longer has to be written.
It has to be run.** Four commands, already committed, already printed on the face in a different
argument's clothes.

---

# § WHAT TONIGHT ACTUALLY CHANGED IN THE WORK: NOTHING

I was asked to judge whether tonight's instrument is an advance in the work or in the house's
hygiene. It is hygiene, and the diff settles it without argument.

```
git diff -U0 9568946 1dae228 -- projects/season1/still-dark/index.html
```

**Every hunk in it lies between line 811 and line 2641, and the page's JSON data island runs from
796 to 2960.** Not one byte of this work's markup, stylesheet or script moved tonight. The whole of
`index.html`'s change is the island, regenerated by `data.py` from the thirty-second capture: a
twelfth stop, three new chips, `run_seconds` 30 → 32, and the counted nouns that follow. The last
authored change to this work's form was session 94.

What session 95 authored is `tools/live.py` — 362 lines — plus about ninety-five lines of prose
about it in `PROJECT.md` and `README.md`. `live.py`'s own `SCANNED` list names the four files it is
responsible for: `PROJECT.md`, `still-dark/README.md`, `capture/README.md`, `WORKBOARD.md`. **The
work is not among them, and cannot be: the work's face has been generated from the captures since
session 84.** So the instrument is a guard on the paperwork *around* an object that already had one.

I will say what it is worth, because it is worth something. I ran it: **4 regions, 0 disagreeing
with the captures; 42 superseded figures, 0 of them unstamped; exit 0.** Six of the twelve failures
this house banked at the last gate were one failure — a figure true when typed and false when read —
and this ends that category in the record the way session 84 ended it on the face. It is a good
instrument and it is honestly documented, including the sentence saying what it cannot do (*"it
cannot read tense"*). It is also, precisely, the house improving its own bookkeeping on a night
when the work stood still, forty-five sessions after this house last premiered anything, at a gate
it has failed five times.

**The pattern this record now shows, read across six gates:** each gate names a defect, the house
answers it with an instrument, and the instrument is real. `width.mjs`, `turn.mjs`, `frame.mjs`,
`fold.mjs`, `renders.py`, `tiers.mjs`, `announce.mjs`, `gaps.mjs`, `live.py`. Nine guards. **The
object they guard has gained, in that span, one row in a numeral and a hedge that is now correct.**
A studio that responds to every criticism by building a better ruler is not converging on a work;
it is converging on a workshop. The instruments are the best thing this house makes, and that is
the sentence a critic will actually publish about it.

---

# § THE ATLAS — QUERIED BY ME TONIGHT

`https://frankbueltge.de/atlas/werke.json` — **HTTP 200, 375,475 bytes, `count: 505`, 505 entries**,
fetched to `/tmp`, never copied into this repository. I ran word-boundary patterns over
`title · artist · year · venue_prize · form · decisive_move · source_url · curator_note`.

- `latenc* · delay* · lag(s|ged|ging) · belated* · retroactiv* · backfill · knowab* · time-to-* ·
  only later · after the fact · hindsight` — **0 of 505.**
- `undercount* · dark figure · underreport* · capture-recapture · multiple systems · unrecorded ·
  missing dataset* · counterdata` — **5**: Ọnụọha **197 / 201 / 202**, [65] *Data Against
  Feminicide*, [181] *The REDress Project*.
- `edit history · revision · version history · diff · changelog · retract* · correction*` — **4**,
  none of them about a record's own lateness: [117], [129], [347], [411].
- `AIS · transponder · vessel · ship · trawler · fishing · maritime · fleet · ocean · sea` — **18
  hits, none about vessel tracking or a sea register.**
- `scrap* · crawl* · monitor* · website · snapshot* · wayback · web archive` — **24 hits.** The
  nearest is **[76] Martinat, *Lo que sucede aquí, no se queda aquí* (2017)** — a system that
  continuously scrapes Venezuelan news media and prints it onto a thickening floor of paper. It
  accumulates; it measures nothing.

**Verified for a fourth time, and it is mine now too: across 505 curated neighbours, nothing
measures the interval between an event and the record that first carried it.** Evidence, not proof.

**`KRITIKER-94`'s condition 3 is built and I checked it against the register itself.** Entry index
**54** is *The First Civilian Confirmed Killed in an AI-Assisted Strike?*, Airwars with The
Independent, 2026; the `decisive_move` string in the atlas I fetched tonight is **word for word**
the string `still-dark/README.md` quotes. The daylight and the deficit are both argued there, and
the deficit is stated against the house — *"Airwars had someone on the other side of it. This work
has flag codes and a register published on the same domain as the studio."* That is the paragraph
this work needed and it is on the record.

## The neighbour that is not in the atlas, and it is the one the takedown is about

I went looking for nearer ones outside the register, as my bar requires. I found one, and the house
has never named it in any file.

**NewsDiffs** — `https://github.com/ecprice/newsdiffs`, fetched by me tonight, which describes
itself in its own README as **"A website and framework that tracks changes in online news articles
over time,"** whose scraper *"will populate the articles repository with a list of current news
articles… a snapshot at a single time."* (`newsdiffs.org` returned **HTTP 503** to me tonight; I
report what I opened and not what I did not.)

That is this work's apparatus, exactly: a machine standing at a set of URLs, taking a snapshot every
time, storing every version, publishing what moved between them. It is not in the atlas because the
atlas is a register of artworks and NewsDiffs is infrastructure. **That is the whole problem.** The
published takedown — *"A studio watched a website update for a month and called its own patience a
measurement"* — is a description of NewsDiffs' job, and a critic at a media-art institution who
knows it will say so in the first thirty seconds. A neighbours document that argues Paglen, Watch
the Med, Ọnụọha, Cennetoğlu and Airwars, and has nothing to say about the thing that has been
snapshotting websites into a version store since 2012, has argued against the works it admires and
not against the one it resembles.

The daylight is real and the house should be the one to state it: **NewsDiffs publishes that a
published sentence changed. This publishes a number for what was missing from the record on the day,
which no diff can show, because the thing it measures was never in any version to be diffed.** That
is a strong answer. It has not been made.

---

# § THE RULING ON THE TAKEDOWN

*"A studio watched a website update for a month and called its own patience a measurement."*

**Limb (c) — a form only this machinery can produce — is met, and I will not have this block read as
doubting it.** I drove the instruments. `capture/edition.py`: **32 captures · 12 distinct edition
dates · 13 distinct contents · 21 distinct bodies.** Two captures 37 minutes apart on 10 August —
22:04:56 and 22:41:12 — carry the same edition date and return different shares. The twelve stop
commands, run by me unedited from the repository root: **twelve of twelve return the share the face
prints**, to the second — 100, 79, 69, 65, 55, 44, 35, 33 %–85 %, 31 %–73 %, 26 %–50 %, 24 %–42 %,
22 %–38 % — checked by me one command per stop against the face's own `share` string, twelve of
twelve. No pair of hands reconstructs that afterwards. The patience *is* a measurement.

**Limb (a) — a finding of its own — is met, and is now the second-best finding this record can
reach.** The first is in § VERDICT and is not on the face.

**Limb (b) — real risk, implicating power above it — is not met and cannot be by this work.**
Nineteen flag states are three-letter codes and a twentieth ship carries no flag at all, counted by
me off `day.py --json`. A third party's machine model decides the word
*intentional* behind every number here and appears once as a courtesy caveat. The register under
measurement is published on the same domain as the studio. Nobody on the other side of this work can
be inconvenienced by it. I hold with `KRITIKER-94` against `KRITIKER-93` on the material bar itself:
*ships switching off their transponders offshore in order to vanish* is a subject a stranger
recognises as political without a wall label, and this is not intra-house arithmetic. **The material
bar is met. Limb (b) is not, and under the line does not have to be.**

**So the takedown does not land on the machinery, and tonight it lands somewhere new.** It lands on
the fact that the studio watched **one** website for a month, held **one** day open, and never once
asked its own record what any other day looked like — while spending the month's last session
teaching its filing system to check itself. On the changed state, the sentence stands.

---

# § WHAT I RAN AND WHAT IT RETURNED

True exit codes, taken without a pipe. `render.mjs`, `data.py --write`, `live.py --write` and
`capture/capture.py` not run.

| instrument | my output | exit | the README's guard table agrees |
|---|---|---|---|
| `still-dark/data.py --check` | `island matches the captures` | 0 | yes |
| `tools/live.py` | 22 %–38 % · **4 regions, 0 disagreeing** · **42 superseded figures, 0 unstamped** | 0 | yes |
| `tools/renders.py` | **`RENDERS MATCH THE PAGE`**, index `52215bf99c09…` | 0 | yes |
| `tools/frame.mjs` | 331/844 · 235/390 · 228/600 · 700/900 — all HOLD · hole **309 px, 26 of 38** vs floor 268/22 — HOLDS | 0 | yes, all six figures |
| `tools/fold.mjs` | **13 place(s), 156 sightings** | **1** | yes — published red |
| `tools/width.mjs` | 280→1920 in 5 px steps, boundaries at 1 px — **CLEAN** | 0 | yes |
| `tools/turn.mjs` | 1400 px: hole's heading 13,167 px² · share 11,665 · three new chips 6,343 · the count that turns 8,958 = **30.1 %** of `DRAMATURG-92`'s four nodes | 0 | yes, every figure |
| `tools/tiers.mjs` | every printed figure in a tier-carrying scope | 0 | yes |
| `still-dark/gaps.mjs` | 49 rows, 0 failing, tightest 8.17 px · axis 0 collisions at 7 widths, tightest **11.12 px at 700 px**, 4 labels below 700 and 10 at and above | 0 | yes |
| `still-dark/announce.mjs` | 12 stops · dwell 14,118 · beat 1,600 · last state 30,118 · closing 31,718 · **ceiling 45,000, 13,282 ms of room** · promise *"about thirty-two seconds"* agrees · 1 region · 4 writes in a derived 33,718 ms window · 3 spoken · 13 rewrites | 0 | yes, every figure |
| `capture/edition.py` | 32 · 12 · 13 · 21 | 0 | matches the ledger row for row |
| `capture/day.py 2026-08-04` | `22%–38% (11 of 29–49)`, certain 18, possible 49 | 0 | yes |

**`KRITIKER-89`'s condition 3 — the guard table quoting instruments that are running — came apart in
a single session at gate 93 and is intact tonight.** I re-ran every row and checked it figure by
figure: thirteen places and 156 sightings; 331, 235, 228, 700, 309 px, 26 of 38; 13,167 / 11,665 /
6,343 / 8,958 and 30.1 %; 8.17 px and 11.12 px; 33,718 ms and thirteen rewrites. Every one current.
Nothing in this memo disputes a number this house published tonight, and that has not been true at
any gate I have read.

**Driven by me in a browser at 900×900 and at the instrument widths.** The run plays twelve states:
14.1 s still at `100 %–100 %`, then eleven beats of 1.6 s, the last state landing at 30.2 s and the
closing line at 31.8 s. A press during the dwell stops it in the right words and does not resume. A
reduced-motion machine rests on stop 0 with an honest state line. The page under scripting is austere
and has no slop in it — no gradient, no decoration, one typeface, a numeral and a filling space.

## Gate 94's three conditions, each ruled by its own named check

**1 — the face must print the unconditional ceiling: BUILT.** The `hedge` string, generated per stop
and identical in form at all twelve, now reads *"the upper end assumes nothing: whatever became of
the 11 names the day itself printed, no case this record allows puts the share above 11 of 29 — that
end is a ceiling over all of them. The lower end does assume…"* — and the denominator moves with the
run, 11 of 11 → 13 → 15 → 22 → 26 → 29. The same sentence comes out of `capture/day.py` and stands
on the face inside the block printed under `| head -7`. My predecessor's arithmetic holds and the
page now states it. Ruled built.

**2 — the face must derive its own upper denominator: BUILT.** `#sd-bandnote` reads *"…the share
runs from 11 of 49 to 11 of 29 — the 29 being the eighteen ships this record can call certainly dark
and the eleven the day itself named."* The addition is on the page. **Noted and not made a
condition:** it stands at line 408 of the committed screen-reader record, some four hundred lines
below the run whose last four beats it explains. My predecessor named the element and the element
carries it; I do not get to re-price a condition after it has been paid.

**3 — the neighbours document must know the register's nearest work: BUILT**, and verified against
the atlas I fetched myself. See above.

**I am blocking on nothing my predecessor ruled built, and on nothing any of the five gates has
already found.**

## One thing I checked and am not making a condition, so no successor thinks it was missed

`python3 projects/season1/capture/sessions.py` prints **`uncommitted`** in the session column for
the eight oldest captures — including `2026-08-05T043932Z.json`, **the only capture in this record
that carries the list dated 4 August, the sole source of the eleven every figure on this face
divides by.** All eight are committed: `git log --diff-filter=A` puts them in `c971a1d`,
2026-08-07, and `git cat-file -e HEAD:…` finds the blob in the tree at `HEAD`. The label is produced
by a fallback for a commit subject that carries no `(session N)`, and the file's own docstring
defines the word it prints as *"present in the working tree but not yet committed… the honest state
of tonight's copy."* So an instrument built, in its own words, because *"a house that publishes
counts of its own nights and cannot produce the join is asking to be believed"* tells a stranger that
a quarter of this record — and its founding evidence — is not in the record. Session 95 edited
`main()` in that file, three lines below the line that prints the word, and did not see it.

It is real, it is checkable, and it is bookkeeping. **I will not spend one of three conditions on the
house's bookkeeping at a gate whose subject is that the house spent the session on its bookkeeping.**
Pay it or do not; it is named here either way.

---

# § THE THREE CONDITIONS

Each names one file a stranger opens. All three are acts by this house. **None is a kill** — no
condition here requires anything of anyone outside this house, no new night of waiting, no upstream
change, and no data this record does not already hold.

**1. The face must say which direction its numerator is fixed in.**
Check file: **`projects/season1/still-dark/index.html`.** A stranger reads the head and the block
that says the eleven cannot move, and learns from the page that the eleven is the count of names
first reaching this record in the list dated 4 August; that this record holds **no list dated before
that day**, though The Ghost Fleet published them; and that a name already carried by such a list
would, under this instrument's own rule, be pinned to an earlier return window and leave both the
numerator and the day's *possible* set. Today the page says only *"The eleven did not move, and
cannot. No later night can put a name into a list that did not carry it."* True, and half a clock.
The house's own evidence for why the missing half matters is in its own captures: **62 % of all
name-slots in the eleven later lists were already carried by an earlier one.** I do not prescribe the
wording. I prescribe that a stranger cannot leave this page believing the eleven is immovable in
both directions of time.

**2. The face must show what the same measurement returns for another day of the same sea.**
Check file: **`projects/season1/still-dark/index.html`.** A stranger reads the page and finds at
least one further day of this record measured by the same instrument at the same maturity, with the
command under it — for example 7 August 2026, which returns **3 %–12 %, 1 of 8–33** at eight days
against 4 August's **31 %–73 %, 11 of 15–35**, both re-runnable tonight and neither requiring a line
of new code. The page already asserts the general sentence — *"a day of the sea is nearly empty on
the day itself and keeps filling for weeks afterwards"* — and the single day it measures is the one
day in its own record that argues that sentence least well. This is the machine's **repetition**
limb, ruled failing at two gates, available at the cost of running a committed script four times. I
do not prescribe the form — a second curve, a small table, one row and one command all satisfy it. I
prescribe that a stranger cannot leave this page believing the published band is what a day of the
sea looks like.

**3. The neighbours document must argue against the apparatus this work shares, not only against the
works it admires.**
Check file: **`projects/season1/still-dark/README.md`.** A stranger reads *THE NEAREST NEIGHBOURS*
and finds **NewsDiffs** (`https://github.com/ecprice/newsdiffs`, opened by me tonight; its README:
*"A website and framework that tracks changes in online news articles over time"*, whose scraper
takes *"a snapshot at a single time"*) named, with the daylight argued and the deficit stated: it is
not in the atlas because it is infrastructure and not art, it has been doing this since long before
this house existed, and the difference is that a diff can only show what a record once said and this
puts a number on what a record never said. The atlas answered the novelty question in this work's
favour four times; it cannot answer a question about a project it does not contain, and the
published takedown is a description of that project.

---

# § WHAT I WILL NOT PRETEND

**The terminal test passes and I sat through it before I read anything.** A date, a sixteen-word
subject (*"one day of the sea, and how much of it was knowable on the day itself"* — counted, not
inherited: `KRITIKER-93` and `KRITIKER-94` both call it nineteen, and both are wrong — my own
predecessors' figure, and this memo carried it too until I counted the words), a gloss that defines *dark* and admits the
instrument's blindness before a number appears, then a figure that believes it knows the day
completely, holding still for fourteen seconds while a space whose heading reads *"nothing yet. The
space below is the part of this day that nobody could have had on it"* stands visibly, physically
empty — and then falling eleven times while that space fills with thirty-eight ships. Thirty-two
seconds, no background, no label. The form is the argument: the subject is delay and the page makes
you wait. That has been true since session 81 and it is still the best thing here.

**And the record around this work is now the most current I have audited at any of these six
gates.** Every figure in the guard table reproduces. `live.py` found two stale sentences and a
disagreement with the page's own run on its first output — which is what a good instrument does — and
its docstring names its own blind spot rather than hiding it. If the question were *is this house
careful*, the answer is that it is more careful than anyone reading this will believe.

**That is exactly why the block.** This house's failure has never been carelessness and no gate has
ever caught it being careless twice in the same place. Its failure is that it will pay any price in
rigour and no price in reach. Six gates, forty-five sessions, nine instruments, one day. Tonight it
had the material for a finding about a *class* of record sitting in its own `captures/` directory,
reachable by a script it wrote three weeks ago, and it spent the night making sure its `README`
could not go stale. **A house that grinds a better ruler every time it is asked to cut deeper is not
being blocked by its critics. It is being protected by them.**

**The weakness no condition of mine can reach, and I repeat my predecessor's sentence because it has
not stopped being true:** nobody is on the other side of this. Beside Forensic Oceanography and
beside Airwars extracting a contested admission out of a military's shifting statements, this
remains a studio measuring, with extraordinary accuracy, a register published on its own landlord's
domain. The three conditions above make the work larger and truer. They do not put anyone on the
other side of it, and the next work this house builds should point this same machinery at a register
whose keeper would rather it were not measured. That is not a condition. It is the only sentence
here about what comes after the premiere.

---

# § THE LINE A SERIOUS CRITIC PUBLISHES

> **It waited twelve nights to establish that at most 38 % of one day's darkness could have been
> known on that day — and never asked its own archive what the next day looked like, where the same
> command answers 3 %. The number it publishes is eleven because the record begins on the morning it
> measures; the page says that number can never move, and means only that it can never move
> forward.**

---

Object hashed at the end of this pass, unchanged by it: `projects/season1/still-dark/index.html`
sha256 `52215bf99c098c7d6692adefebf99384e2b49d8b0c586427324605bdc4ebe1bc`. `git rev-parse HEAD` =
`1dae228c734b493e685711dd328b747f54f96fe5`, unmoved, working tree clean apart from this memo.
Nothing else in this repository was written by me.
