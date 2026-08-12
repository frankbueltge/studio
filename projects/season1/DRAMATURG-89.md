# DRAMATURG — STILL DARK, premiere gate, session 89

**Convened on the working tree, not on `HEAD`.** Hash taken by me before I drove anything:

```
7c9d100291dcd312950b5463ec62a3715630ce700397cc90022d4a65f0838fbe  projects/season1/still-dark/index.html
```

**I edited nothing but this file.** Every script named below is in this session's scratchpad
(`$S`), outside the repository. I ran the house's own `render.mjs` once, as offered; it rewrote
`STATE-1.txt`, `RENDERS.json`, `render-1400.png` and `render-900.png`, all four of which were
already modified in the working tree before my pass. **`index.html` was never touched** — the hash
above is re-verified at the foot and it did not move.

---

## WHAT I DROVE, AND WHAT IT SAID

Chromium, `file://…/still-dark/index.html`, at **390×844** and **1400×900**, light scheme, with
motion on and with motion reduced.

| driven | script | what it did |
|---|---|---|
| first encounter | `$S/drive89.mjs` | every painted text run inside the first viewport at scrollY 0, with its y, size, weight and ink |
| the nine stops | `$S/drive89.mjs` | all nine pressed at both widths; figure, fraction, standing figure, clause, heading, caveat, chip counts, boxes |
| the self-running head | `$S/beat89.mjs` | load to rest with motion ON, a `MutationObserver` on ten nodes, sampled at 0.5 · 3 · 8 · 13.5 · 29.5 · 33.5 s |
| the reader who leaves | `$S/beat89.mjs` | reload, scroll two screens away at second 3, return at 29 s |
| occlusion | `$S/drive89.mjs` | every chip of `#sd-arrive-names-since` hit-tested at its own centre, at every stop, at every 40 px of the whole scroll range, both widths |
| the frame | `$S/frame89.mjs` | the span, the scroll position that holds it, the chips and pixels lost at either end, and the hole's growth curve |
| what a 5 px clip costs | `$S/ink89b.mjs`, `$S/lastchip89.mjs` | element screenshots decoded in node (own PNG inflater, no browser canvas), ink counted row by row |
| the turn | `$S/turn89.mjs` | which node changes KIND across the run, where it stands, and the best frame a phone can occupy |
| prose | `$S/prose89.mjs` | every string of the head with its y, height, size, ink, character count, and distance from the figure |

**House instruments, run and not trusted blindly:** `tools/frame.mjs` (exit 0), `tools/fold.mjs`
(exit 1, 99), `announce.mjs` (exit 0), `gaps.mjs` (exit 0, PASS), `render.mjs` (exit 0).

### The nine states, read off the live DOM at both widths

```
stop 0  100 %–100 %  11 of 11  11 of 230   then 11  since  0      stop 5   44 %–100 %  11 of 25  since 14
stop 1   79 %–100 %  11 of 14  11 of 230   then 11  since  3      stop 6   35 %–100 %  11 of 31  since 20
stop 2   69 %–100 %  11 of 16  11 of 230   then 11  since  5      stop 7   33 %–100 %  11 of 33  since 22
stop 3   65 %–100 %  11 of 17  11 of 230   then 11  since  6      stop 8   31 %–100 %  11 of 35  since 24
stop 4   55 %–100 %  11 of 20  11 of 230   then 11  since  9
```

**The ninth stop is on the object.** 31 %–100 %, `11 of 35`, 24 chips, the caveat at four certain.
The head's frame is byte-stable across all nine stops at both widths — `268–453` at 390 and
`163–325` at 1400, at every one. The reservation absorbs the ninth list. Nothing steps.

### The run's own arithmetic, motion ON, 390×844 (`$S/beat89.mjs`)

```
#sd-arrive-state          3   407 · 14212 · 27012
#sd-arrive-count          8   14212 · 15812 · 17412 · 19012 · 20612 · 22212 · 23812 · 25413
#sd-arrive-frac           8   the same eight milliseconds
#sd-arrive-when           8   the same eight
#sd-arrive-head-since     8   the same eight
#sd-arrive-names-since    8   the same eight
#sd-arrive-hedge          8   the same eight
#sd-arrive-standing-fig   0
#sd-arrive-standing-note  0
```

The prescription of 87, built in 88, holds under a ninth stop: **eight rewrites of the falling
numeral and its fraction at the identical millisecond, zero of the standing figure.** The house's
own `announce.mjs` reports the same run independently (14,202 → 25,402, done 27,002). Two roads,
one number. §1 of the memo before mine is not disturbed and I do not reopen it.

---

## 1 · THE FRAME QUESTION — I rule against the ITEM, not against the object

`tools/frame.mjs` tonight, confirmed by me:

```
phone 390×844 — figure-top to controls-bottom: 358 px of 844 — HOLDS
  figure-top to hole-bottom: 849 px of 844 — OVER by 5
wide 1400×900 — 495 px HOLDS · 364 px HOLDS
```

### (a) The 5 px is not a defect a visitor experiences. Measured three ways.

There are exactly two frames a visitor can stand in, and I priced both.

**Stand the whole figure at the top of the screen (scrollY 268).** Figure `0…30`, hole `576…849`
— 268 px of the filling space in frame, **22 of 24 chips wholly inside**. What falls off is the last
row: `ISABELLA · USA` and `LUCKY TJ · USA`, the two names the ninth list brought. I screenshotted
those two chips and counted their ink row by row (`$S/lastchip89.mjs`):

```
"ISABELLA · USA"  box h20: 102,2,2,2,2,2,41,43,32,45,43,38,57,55,2,2,2,2,2,102
                           └ rule            └── the letters, rows 6–13 ──┘        rule ┘
```

The 5 px cut takes rows 15–19: **the chip's bottom rule and nothing else. Not one pixel of either
name.**

**Or put the hole's last pixel on the fold (scrollY 273).** The figure box then runs `−5…25`. I
screenshotted the figure and counted its ink: **the ink begins 4 px inside its own box**, so the
clip removes **1 px of glyph** — and off the *dim, unmoving* `–100 %`; the falling `31 %` has 7 px
of clearance and loses **nothing**.

**Ruled: a 5 px overflow on this head costs a hairline rule or one pixel of one numeral, at one
scroll position of a 7,484 px document. No sentence and no word of prose may be spent on it.** This
house has banked failure 48 for spending prose on pixels. I will not open a second account.

### (b) But the item cannot ever be held, and that is the finding.

The hole is a reserved block. Its height is its own content, and its content is the work's subject.
I rebuilt it at n chips with the reservation released and measured (`$S/frame89.mjs`):

```
  20 chips → hole 227 px   span 803    (41 px of slack)
  22 chips → hole 250 px   span 826    (18 px of slack)     ← session 88, green at 786*
  24 chips → hole 273 px   span 849    OVER  5              ← tonight
  26 chips → hole 296 px   span 872    OVER 28
  28 chips → hole 319 px   span 895    OVER 51
  32 chips → hole 365 px   span 941    OVER 97
```

**23 px per row, one row per two names.** This record's own lists have added 3 · 2 · 1 · 3 · 5 · 6 ·
2 · 2. The tenth list at the median takes the span to **872, over by 28**; the eleventh to 895; and
at 32 chips the overflow is 97 px — **more than three times the figure's own height**, at which
point what is lost is names, not rules.

So a 5 px trim tonight buys **zero nights**. It is under water on the very next list.

**And this is not bad luck; it is the item's arithmetic.** The item measures figure-top to
hole-**bottom**. The hole's bottom is the count of ships later lists gave. **The item therefore goes
red on exactly the nights the work succeeds at its subject, and could only be green permanently if
the day stopped filling.** Session 88 paid it once — 157 px, of which 88 moved rather than went —
and the payment lasted one night. That is the shape of the trap, and the house is one list from
walking into it again.

### (c) The item is the mistake. The staging fact it was a proxy for is bounded, and is met.

The hole grows **downward from a top that does not move.** Measured: `#sd-arrive-names-since` stands
at document y **844 at all nine stops** at 390 and **439 at all nine** at 1400. The eleven names
above it cannot grow — that is the work's own published law. So *figure-top to hole-top* is
**576 px at 390** and stable against every future list.

Tonight's honest staging number is therefore this, and it is the one the record should carry:

> **At 390×844, with the whole figure at the top of the screen, a visitor holds 268 px of the
> filling space and 22 of its 24 names in the same frame** (1400×900: the whole figure, the whole
> hole, all 24). That number does not fall when the tenth list lands.

**CUT 1 (in `tools/frame.mjs`, checkable by a stranger).** The second span, `HOLE_BOTTOM` at
`frame.mjs:74` and its report at `:140-147`, is **struck and replaced by the measurement above**:
with `#sd-arrive-count` placed at the top of the viewport, how many pixels and how many whole chips
of `#sd-arrive-names-since` share that frame, floored at tonight's **268 px / 22 chips**. The header
note at `frame.mjs:66-73` must say why: *a span whose far end is the work's own accumulation is an
item that fails on success.* **No pixel of prose is to be spent against the old item, and its
`OVER by 5` is not to be reported as a regression.**

---

## 2 · `tools/fold.mjs` 88 → 99 IS THE SAME MOVED RULER, POINTING THE OTHER WAY

The predecessor caught this instrument reporting an improvement that was a stretched probe grid.
Tonight it will offer this house a *regression*, and it is the identical artefact. Counted per stop
from the raw output at 390 (`$S/fold89.txt`):

```
stop  0 1 2 3 4 5 6 7 8
ctl   6 6 6 6 6 6 6 6 6
line  5 5 5 5 5 5 5 5 5
                              88 / 8 stops = 11.0     99 / 9 stops = 11.0
```

**Eleven per stop last night on eight stops; eleven per stop tonight on nine.** Nothing got worse.
The count tracks the number of stops and the scroll range (1,328 → 1,354), not the head's health, for
the third session running. Chips covered: **0**. `fold.mjs` exits 1 at 99 for precisely the reason it
exited 1 at 88.

**CUT 2.** The record must not print *fold went 88 to 99* as a finding. If a number is printed at all
it is **11 failures per stop, level with session 88** — and the honest entry is that this instrument
reports the length of the run.

---

## 3 · THE MOBILE OCCLUSION HISTORY IS PAID, AND I CHECKED IT HARDER THAN THE HOUSE DOES

A pinned control bar once painted out ten of nineteen chips at 390. I hit-tested **every chip of
`#sd-arrive-names-since` at its own centre, at every one of the nine stops, at every 40 px of the
entire scroll range, at both widths**:

```
390×844   2,269 chips in view   0 covered
1400×900  1,337 chips in view   0 covered
```

The reason is structural and I verified it: at phone widths the controls are painted **above** the
material (`#sd-arrive-controls` at document 461–625, `#sd-arrive-names-since` at 844–1117), static,
not pinned, so there is no scroll position at which a control can stand on a name. The block is
`overflow: visible`, `scrollHeight` equal to its height — nothing clipped, nothing merely in the DOM.
**Clean. I strike this from the standing worries.**

---

## 4 · FIRST ENCOUNTER — and `100 %–100 %` is a STATEMENT, not a stutter

**At 1400×900 the whole argument is on the first screen and it is the best thing in this work.** A
stranger meets, in order: the date; `100 %–100 %` at 46.4 px; the clause that gives it its unit; `11
of 11`; `11 of 230`; the eleven names the day printed; the heading *NAMED ONLY BY LATER LISTS —
nothing yet*; **89 px of reserved emptiness**; the caveat; the buttons; the run's line. The empty box
is the piece. It is on stage at second zero and it fills while you watch. Nothing has to be said.

**At 390×844 that emptiness is one pixel below the fold.** `#sd-arrive-names-since` stands at
document y 844 in an 844 px viewport, so at scroll 0 a phone visitor sees the heading naming the
space and **not one pixel of the space itself**. This, not the 5 px, is the phone's real deficit, and
it is unchanged from before tonight.

**On the range whose ends are identical.** The previous critique called it a stutter. Measured, it is
not, and the reason is on the face: the two ends are set differently and the difference is this
head's own published law.

```
#sd-arrive-count-falling  30.4 px  weight 700  rgb(17,17,17)      rewritten 8× in a run
#sd-arrive-count-fixed    30.4 px  weight 400  rgba(0,0,0,0.55)   rewritten 0×
```

The eye does not read `100 100`. It reads a live figure and a mark beside it, and one line under, the
same thing in ships: `11 of 11` — a list that thought it had all of it — over `11 of 230`. When the
run starts, the live end walks away from the mark and the range opens. **A zero-width range at second
zero, opening to 31 %–100 % by second 25, is the whole finding in one gesture.** I pass it.

**But the key to the notation is 1,080 px away on a phone.** What the two ends *are* is said only in
`#sd-arrive-constant`, at Δfigure **1,080 px** at 390 (Δ583 at 1400). Noted; not ordered, because the
run itself teaches the notation within fifteen seconds to anyone who stays.

---

## 5 · THE READER WHO LEAVES DURING THE BEAT — owed item (v), and I rule it PAID, on a re-description

I drove it: load, wait to second 3, scroll two screens down, come back at 29 s.

```
returned at 29 s:  31 %–100 %  ·  24 chips standing  ·  "The run has finished. The figure now
standing is this record's live one — press any button to go back through it."
```

**Nothing is lost, because the end state carries the whole argument standing still:** `31 %–100 %`
over `11 of 35` over `11 of 230`, eleven names the day printed against twenty-four it did not, and
one press to see it move. The run is spent, not wasted. (v) is paid and I close it.

**But the head misdescribes its own rhythm, and the misdescription is why (v) has looked unpaid for
three sessions.** Measured on the running object, three ways in agreement (my observer, the house's
`announce.mjs`, and `first_dwell_ms` at `index.html:1070`):

```
load → first movement of the figure   14,212 ms
first → last movement                 11,200 ms   (eight steps of 1,600)
run declared done                     27,000 ms
```

The face says: *"nine states over about twenty-seven seconds, **starting after a pause** as long as
the paragraph under the title takes to read."* Grammatically the twenty-seven seconds begins **after**
the pause. **It does not. The pause IS state zero.** The object has nine states spanning 26.9 s of
which the first lasts 14.1 s and the other eight 1.6 s each — a first state **nine times longer** than
any other, and longer than all eight of them together. A visitor who reads that sentence and starts a
stopwatch waits 41 seconds for a thing that ended at 27.

**This is the one sentence a visitor who cannot see the figure ever hears about the performance**
(`#sd-arrive-state` is the page's only live region; `announce.mjs`: three spoken, ten figure
rewrites). It is wrong about the shape of the performance, and its second clause is this house
explaining its own reading-speed arithmetic on the work's face.

**CUT 3 — `index.html:1059`.** Strike the clause **`, starting after a pause as long as the paragraph
under the title takes to read`**. The survivor — *"This figure runs by itself: nine states over about
twenty-seven seconds. Any button above holds a state and stops the run."* — is **true as measured**,
26.9 s load to done. Pure deletion; a stranger checks it with a stopwatch.

---

## 6 · THE PAGE OVER-EXPLAINS. Here is every sentence the object already performs.

Measured positions at 390, last stop (`$S/prose89.mjs`), Δ from the top of the figure.

**(i) `index.html:1066`, the caption, Δfig +944, 295 ch, 131 px.**

> *"A ship reaches the list only after it comes back, so a day that is over keeps being answered.*
> **~~Nine lists, nine answers, one day — the last of them eight days after the day had ended. The
> eleven names the day itself held cannot grow; every list since has only made the day larger
> underneath them.~~**"

Sentence 1 is the premise; no run performs it; **it stays.** Sentences 2 and 3 are the object
described to a person watching it:

- *Nine lists, nine answers* — **nine buttons stand 483 px above this sentence**, labelled `ON THE
  DAY … +8 DAYS`.
- *the last of them eight days after the day had ended* — `#sd-arrive-when` prints
  **"eight days after the day had ended"** *verbatim*, at Δfig **+33**, in live ink, rewritten at
  every stop. **The same clause twice on one page, 911 px apart, one of them performed.**
- *The eleven names the day itself held cannot grow; every list since has only made the day larger
  underneath them* — this is `11 of 11 → 11 of 35`. It is the sentence the frame was rebuilt in
  session 88 to retire, on the prescription *"the run does the arguing."*

**CUT 4 — strike sentences 2 and 3 of `index.html:1066`.** Pure deletion; the survivor stands.

**(ii) `index.html:1057`, the constant, Δfig +1,080.**

> *"Neither end of this figure can rise. The upper end holds at 100 % until more of these ships are
> certainly dark on this day than the eleven the day itself named;* **~~only the lower end has moved
> so far~~**, *and the next list can lower it again."*

Sentences 1, 2 and the last clause are conditions on the future; no run can show them; **they stay,
and I defend them.** *"only the lower end has moved so far"* is the run, at eight mutations to zero,
under the head's own published `cannot move` mark. It is the clause the mark exists to make
unnecessary.

**CUT 5 — strike `only the lower end has moved so far` from `index.html:1057`.** Its survivor must
name the end it lowers rather than inheriting `it` from the struck clause. **One clause, deleted, and
the pointer repaired** — the same order the memo before mine made at its own landing site.

**(iii) `index.html:721` + `index.html:2100` — the subject line, Δfig −171, 55 ch, 33 px at 390.**

Three printings of one thesis inside the first 353 px of a phone screen:

```
y  43  .sd-sub               one day of the sea, and how much of it was knowable on the day itself
y  97  #sd-arrive-subject    HOW MUCH OF 4 AUGUST 2026 WAS KNOWABLE ON 4 AUGUST 2026
y 301  #sd-arrive-when       …was knowable on the day itself, counting the lists up to 12 AUG…
```

The subtitle is the page's; the `when` clause is the figure's own unit and the run rewrites it. **The
middle one is the same sentence in capitals, and it is the only one nothing needs.**

**CUT 6 — delete `"subject"` (`index.html:721`) and `#sd-arrive-subject` (`index.html:2100`).** It
stands **above** the figure, so it pays nothing against any frame item and I claim nothing for it: it
brings the figure 37 px nearer the top of a phone.

**What I checked and will not cut.** `subject_gloss` (the definition of *dark* — no run performs it);
`standing_note` (the only line saying what 230 counts — its tier word was blocking in 88 and stays);
`head_since`'s ink key (*"in darker ink"* — a visual code needs its key); `hedge` (§7); the premise in
`.sd-because`, which restates the caption's first sentence 1,418 px lower in different words — noted,
too far apart to be a doubling, not ordered.

---

## 7 · THE ARC, THE TURN, AND WHY THIS RETURNS — the run's only turn is staged where nobody stands

The figure across nine stops: **100 · 79 · 69 · 65 · 55 · 44 · 35 · 33 · 31.** Deltas: −21 −10 −4 −10
−11 −9 −2 **−2**. **The ninth stop's movement is the smallest in the run, tied with the eighth.** On
the frame alone, the ninth stop is the run getting longer.

**But the ninth stop is not a slide, and here is what it actually did.** I read every node across all
nine stops and exactly one changes **kind** rather than degree:

```
stops 0–6   "…so not one of these names is certainly dark on this day."
stop  7     "…so two of these names are certainly dark on this day and the rest are possible."
stop  8     "…so four of these names are certainly dark on this day and the rest are possible."
```

**That is the turn.** It is the moment this record stops saying *possible* and starts saying
*certain* — a day's darkness becoming **known**, which is the subject of the work. Everything else in
the run is monotone. The ninth stop earns its place twice over: it doubled the certain count.

**And the object refuses to stage it.** Measured:

| | 390×844 | 1400×900 |
|---|---|---|
| `#sd-arrive-hedge`, distance below the figure | **861 px** | 373 px |
| at scroll 0 | **285 px below the fold** | in frame |
| at the best frame a visitor can occupy (scrollY 268) | **17 px below the fold** | in frame |
| its size / ink / mark | 12.48 px, `rgb(17,17,17)`, body prose | same |
| anything distinguishing the stop it turns on | **none** | none |

So on a phone the run's one categorical event has **never once been inside the frame**, at any stop,
at any scroll position that also holds the figure. And at both widths it is undifferentiated body
prose that mutates at the same millisecond as six other nodes.

**Worse: the frame prints one end of the record's band and hides the end that moved.** The published
share is **`11 of 4–35`**. The head's frame prints **`11 of 35`**. The `4` — the certain count, the
only quantity the eighth and ninth lists have moved — appears on the whole face **only as an English
word inside that paragraph**. I checked the data: each stop carries `total`, `share_falling_of`,
`share_fixed_of` and a prose `hedge`, and **no per-stop certain count exists as a figure anywhere in
the file** (`index.html:1032-1055` and its eight siblings).

**This is the conviction of `DRAMATURG-88.md` §3, one row over and one night later.** That memo
struck a clause for *printing in the page's dimmest ink a figure the file already holds unrendered*.
Tonight the frame prints one end of the total in ships and puts the other end in a sentence — and
that sentence is below the fold on a phone, and it is the only place the run turns.

**No cut makes a turn visible.** I could buy the 17 px that would drag the caveat into the best
frame — and I refuse, on my own §1: it would be prose spent on pixels, and the hedge sits *below* the
growing hole, so it recedes 23 px with every row the tenth list adds. **A 17 px purchase dies exactly
as a 5 px purchase dies.** The turn has to be attached to the figure, not trail the hole. That is a
build, and a build is a restaging.

---

## 8 · THE ENDING — reachable, and thin at 390

The second after the run ends, at 390, scroll 0, everything a visitor needs is on screen:

```
figure  268–298 IN VIEW · fraction 359–377 IN VIEW · controls 461–625 IN VIEW
"run it again" 509–530 IN VIEW · the run's line 538–617 IN VIEW
the hole 844–1117  NOT ONE PIXEL IN VIEW
```

*"The run has finished. The figure now standing is this record's live one — press any button to go
back through it."* — an ending that names itself, offers the replay in reach, and leaves the figure
standing at its true value. **That is a real ending and I pass it.** But at 390 the second half of the
argument — the space the number is about — is entirely below the fold at the moment the run stops, so
what a phone visitor is left holding is a number and a row of buttons. Not ordered; it is the same
576 px that §1(c) measures, and the honest floor is there.

---

## VERDICT

# RETURNS FOR RESTAGING

**Not for anything that got worse tonight.** The ninth stop landed clean: no reflow at either width,
no chip covered in 3,606 hit-tests, the two numerals still rewritten at the identical millisecond
eight times against a standing figure that never moves, the ending reachable, and the reader who
leaves at second three losing nothing. Measured against last night, this object is level or better
everywhere except a five-pixel rule I have ruled worthless.

**It returns because the ninth list made the standing weakness undeniable.** The run's only turn —
*not one of these names is certainly dark* → *two* → **four** — is the event the eighth and ninth
lists exist to have caused, and the head stages it as body prose 861 px under the figure, off the
phone screen at every stop and every scroll position, in a sentence that carries the record's own
published `4` in a word while the frame beside the figure prints only `35`. **The frame has three
rows and the ninth list touched none of them in a way an eye can tell from the eighth.** On stage, a
run that turned reads as a run that is merely longer. That is a staging fault, it is not payable by
deletion, and it is the same fault this house returned in 87 and built out in 88, one row up.

**The weakness, in one sentence, so a restaging can be tested against it:** *the head's frame prints
how much of the day was knowable and never prints how much of it is known, and knowing is the only
thing in this run that turns.*

**And the frame question is answered so that no night is spent on it:** the 5 px is a hairline rule
or one pixel of a dim numeral, at one scroll position of a 7,484 px document; **the item is the
mistake, not the object**, because its far end is the work's own accumulation and it therefore fails
on success. Restate the instrument (Cut 1) and do not pay it in prose.

### The cuts, each checkable by a stranger in a named file

1. **`tools/frame.mjs:66-74, 140-147`** — strike the figure-top→hole-**bottom** span; measure instead
   how much of the hole shares a frame with the whole figure, floored at tonight's **268 px / 22 of
   24 chips** at 390. Say in the header why: an item whose far end is the work's subject goes red on
   success.
2. **The record** — do not print `fold.mjs` 88 → 99 as a regression. It is **11 failures per stop at
   both counts**; the number tracks the number of stops.
3. **`index.html:1059`** — strike `, starting after a pause as long as the paragraph under the title
   takes to read`. The clause is false as read: measured, the nine states span 26.9 s **including**
   the pause, and the pause is state zero at 14.1 s.
4. **`index.html:1066`** — strike sentences 2 and 3 of the caption. *"eight days after the day had
   ended"* is printed verbatim 911 px higher, in live ink, rewritten at every stop; *"the eleven names
   … cannot grow"* is `11 of 11 → 11 of 35`.
5. **`index.html:1057`** — strike `only the lower end has moved so far`; the survivor must name the
   end it lowers. The run performs that clause at eight mutations to zero.
6. **`index.html:721` and `index.html:2100`** — delete the subject line. Third printing of one thesis
   in the first 353 px of a phone screen. It stands above the figure and pays nothing against any
   frame item; I claim nothing for it.

**Cuts 3–6 are ordered for truth and economy, never as pixels.** If the house books their height
against any frame measurement, that is banked failure 48 recurring and I have named it in advance.

---

**Hash re-verified at the foot, after all measurement, by me:**

```
7c9d100291dcd312950b5463ec62a3715630ce700397cc90022d4a65f0838fbe  projects/season1/still-dark/index.html
```

**Unchanged from the head of this memo. The object did not move under me and I did not move it.**

*Every position, size, weight, ink, character count, mutation timing, span, ink row and instrument
exit in this memo was taken by me tonight on the running object at 390×844 and 1400×900. The growth
curve is taken by rebuilding the hole with the reservation released and re-measuring. The ink counts
are decoded from element screenshots by an inflater written in this memo's own scripts. Published
verbatim beside the work.*

---

**THE SENTENCE A SESSION SHOULD PRINT ABOUT THIS GATE:**

> The ninth list landed clean — no reflow at nine stops, zero chips covered in 3,606 hit-tests, the
> two numerals still rewritten at the same millisecond eight times against a figure that never moves
> — and the five pixels the frame instrument went red by are a chip's bottom rule at one scroll
> position and one pixel of a dim numeral at the other, measured off the screen itself; the item is
> the mistake and not the object, because its far end is the work's own accumulation, so it fails on
> exactly the nights the work succeeds and the next list takes it to 28 px over whatever is trimmed
> tonight; but the run returns for restaging all the same, because the one thing in it that turns —
> *not one of these names is certainly dark* to *two* to **four** — is staged as body prose 861 px
> under the figure, off the phone screen at every stop and every scroll position, while the frame
> beside the figure prints `11 of 35` and never the `4`, so the ninth stop, which doubled the count
> of ships this day can be certain of, reads on stage as a two-point slide and a run that is merely
> longer.
