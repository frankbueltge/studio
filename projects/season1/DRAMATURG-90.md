# DRAMATURG — STILL DARK, premiere gate, session 90

**Convened on the working tree, not on `HEAD`.** Hash taken by me before I drove anything:

```
e98d1507f71bb0dc9ecfca3db587a366db3eb764f8e1116bbb58960cd834f4fb  projects/season1/still-dark/index.html
```

**I moved nothing.** Every script and every screenshot of this pass is in the session scratchpad
(`$S = …/scratchpad/dram90/`), outside the repository. I ran no writing instrument: not
`render.mjs`, not `data.py --write`. The only file I created in this repository is this memo. The
hash is re-taken at the foot and it did not move.

---

## WHAT I DROVE, AND HOW

Chromium, `file://…/still-dark/index.html`, at **390×844** and **1400×900**, light scheme, motion
reduced and motion on.

| driven | script | what it did |
|---|---|---|
| the nine stops | `$S/drive90.mjs` | all nine pressed at both widths; every geometry, size, weight, ink, letter-spacing and string of 25 nodes |
| the frames a reader occupies | `$S/frame90.mjs` | scroll 0, figure-at-top, figure-centred, at stops 0 · 7 · 8, both widths; hole px and whole chips in each |
| the self-running head | `$S/beat90.mjs` | load → 31 s, motion ON, a `MutationObserver` on thirteen nodes, every fire timestamped |
| the live turn on a phone | `$S/live90.mjs` | the auto-run watched at scroll 0 and screenshotted at 13.5 · 22.3 · 23.95 · 25.55 · 27.5 s |
| **what each step changes in pixels** | `$S/ink90.mjs` | the head screenshotted at all nine stops, decoded in node by an own PNG inflater, consecutive stops differenced row by row and column by column |
| what tonight cost | `$S/cmp90.mjs`, `$S/range90.mjs` | `HEAD`'s `index.html` written into the scratchpad and driven beside the tree's, same script, same run |
| occlusion | `$S/occ90.mjs`, `$S/occ3.mjs` | every chip hit-tested at its own centre at nine stops and every 40 px of the whole scroll range, both widths, plus the new span |
| the proof, run | terminal | three of the nine printed commands executed and their output compared to the face |
| the island | `$S/island90.mjs` | `as_of` and `check` compared string by string at all nine stops |

**House instruments, all read-only, run by me and not trusted blindly:** `tools/fold.mjs` (exit 1,
108), `tools/frame.mjs` (exit 0), `tools/tiers.mjs` (exit 0), `gaps.mjs` (exit 0, PASS),
`announce.mjs` (exit 0, 3 spoken / 10 figure rewrites), `python3 data.py --check` (exit 0, *island
matches the captures*). `git status` is byte-identical before and after my pass.

### The nine states, read off the live DOM, identical at both widths

```
stop 0  100 %–100 %  11 of 11  0 of them certainly dark   0 chips
stop 1   79 %–100 %  11 of 14  0 of them certainly dark   3
stop 2   69 %–100 %  11 of 16  0 of them certainly dark   5
stop 3   65 %–100 %  11 of 17  0 of them certainly dark   6
stop 4   55 %–100 %  11 of 20  0 of them certainly dark   9
stop 5   44 %–100 %  11 of 25  0 of them certainly dark  14
stop 6   35 %–100 %  11 of 31  0 of them certainly dark  20
stop 7   33 %–100 %  11 of 33  2 of them certainly dark  22
stop 8   31 %–100 %  11 of 35  4 of them certainly dark  24
```

---

## 1 · THE TURN IS STAGED. The return of session 89 is discharged, and here is the arithmetic

My return was one sentence: *"the head's frame prints how much of the day was knowable and never
prints how much of it is known, and knowing is the only thing in this run that turns."* I tested it
back, clause by clause.

### (a) Where the count stands, and where the caveat stood

Document positions, phone, at every one of the nine stops:

| | 390×844 | 1400×900 |
|---|---|---|
| figure top | 234.4 | 146.9 |
| **`#sd-arrive-certain` top–bottom** | **327.9 – 344.6** | **246.2 – 262.9** |
| Δ below the figure's own top | **93.6 px** | **99.3 px** |
| `#sd-arrive-hedge` (where the turn stood in 89) | 1065.8 | 520.6 |
| Δ below the figure | 831.4 px | 373.7 px |

And the finding that settles it. **A 390×844 phone holds the whole figure in frame at every scroll
position from 0 to 234.** It holds the whole count at every position from 0 to 328. The first
interval is inside the second, so:

> **At every scroll position at which a phone holds the whole figure, it also holds the whole
> count. There are 235 of them, and one of them is scrollY 0.**

The same computation on last night's committed object, driven by me tonight in the same script: the
figure is whole at scrollY 0–234; the caveat that carried the turn is whole only from scrollY 296.
**The intersection is empty. There was no scroll position on a phone at which a visitor could hold
the figure and the run's one categorical event in one frame. Tonight there are 235.**

### (b) The turn during the live run, on a phone, at scroll 0 — driven, not reasoned

`$S/live90.mjs`, motion ON, no scrolling, viewport 390×844:

```
t≈13,500 ms  scrollY 0   100 %–100 %   11 of 11   0 of them certainly dark   WHOLE in first screen
t≈22,300 ms  scrollY 0    35 %–100 %   11 of 31   0 of them certainly dark   WHOLE
t≈23,950 ms  scrollY 0    33 %–100 %   11 of 33   2 of them certainly dark   WHOLE
t≈25,550 ms  scrollY 0    31 %–100 %   11 of 35   4 of them certainly dark   WHOLE
t≈27,500 ms  scrollY 0    31 %–100 %   11 of 35   4 of them certainly dark   WHOLE
```

A phone visitor who loads the page and touches nothing meets `0 → 2 → 4` without moving a finger.

### (c) The beat: it is written on the run's own spine, not beside it

`$S/beat90.mjs`, motion ON, 390×844, load to 31 s, thirteen nodes observed:

```
#sd-arrive-count           8   14238 · 15839 · 17439 · 19039 · 20639 · 22239 · 23841 · 25450
#sd-arrive-frac            8   the same eight milliseconds
#sd-arrive-certain         8   the same eight milliseconds
#sd-arrive-when            8   the same eight
#sd-arrive-head-since      8   the same eight
#sd-arrive-names-since     8   the same eight
#sd-arrive-hedge           8   the same eight
#sd-arrive-proof-as-of     8   the same eight
#sd-arrive-proof-cmd       8   the same eight
#sd-arrive-standing-fig    0
#sd-arrive-standing-note   0
#sd-arrive-state           3   461 · 14238 · 27039
```

**The prescription of 87 holds under the restaging: the three live numerals are rewritten at the
identical millisecond, eight times, against a standing figure that never moves.** The count that
turns is on the spine, not hung off it. `announce.mjs` reports the same run independently
(14,198 → 25,399, done 26,998). Two roads, one number.

### (d) The type: it is a third live thing, not a second headline

Measured on the running object at the last stop:

| node | size | weight | ink | rewritten |
|---|---|---|---|---|
| `#sd-arrive-count-falling` | 30.4 / 46.4 px | 700 | `rgb(17,17,17)` | 8× |
| `#sd-arrive-count-fixed` | 30.4 / 46.4 px | 400 | `rgba(0,0,0,0.55)` | 8× |
| `#sd-arrive-frac` | 17.6 / 24 px | 700 | `rgb(17,17,17)` | 8× |
| **`#sd-arrive-certain`** | **11.52 px** | **400** | **`rgb(17,17,17)`** | **8×** |
| `#sd-arrive-standing-fig` | 17.6 / 24 px | 400 | `rgba(0,0,0,0.55)` | 0 |
| `#sd-arrive-standing-note` | 11.52 px | 400 | `rgba(0,0,0,0.55)` | 0 |

**The frame reads as one column and the system is consistent.** Two rows, each a figure with a note
at its shoulder, at the same two sizes; the live row in live ink, the standing row in dim. The count
takes the note's *size* and the run's *ink*, which is exactly what it is. It carries
`font-variant-numeric: tabular-nums`, so the digit that steps `0 → 2 → 4` does not move sideways.

**`0 of them certainly dark` beside `11 of 11` is a state and not a stutter, and the reason is
grammatical, not typographic:** the word *them* takes its antecedent from the numeral 12.8 px to its
left, on the same baseline, and the antecedent is correct at every stop — 0 of the 11 at stop 0, 4 of
the 35 at stop 8. There is no third reading available.

---

## 2 · THE CATEGORICAL EVENT, TOLD FROM THE EIGHT OF DEGREE — in pixels, on the screen

This is the measurement the return asked for and it is the one I would not take on argument. I
screenshotted the head band at all nine stops, decoded the PNGs in node with an inflater of this
memo's own scripts, and differenced consecutive stops row by row and column by column.

**390×844, head band 186 px tall, pixels changed per step:**

```
step   total   figure-band   when-band   frac column   CERTAIN column
0→1     3663          2321        1224           118              0
1→2     2203           305        1782           116              0
2→3     2200           231        1850           119              0
3→4     2413           227        1970           216              0
4→5      921           582         227           112              0
5→6     2692           575        1920           197              0
6→7     2206           201        1845            99             61
7→8      732           234         349            90             59
```

**1400×900, head band 163 px tall:**

```
step   total   figure-band   when-band   frac column   CERTAIN column
0→1    13949          8414       11318           201              0
1→2     3378           644        2885           191              0
2→3     3332           448        2849           207              0
3→4     3554           416        3020           353              0
4→5     1718          1198         955           178              0
5→6     4271          1209        3352           330              0
6→7     3272           384        2786           168             64
7→8     1170           459         738           138             61
```

**Every other column in the head changes at every one of the eight steps. This one changes at two.**
Six consecutive steps in which the count's column is inert to the pixel — not nearly still, *zero* —
and then 61 and 59 px at 390, 64 and 61 at 1400. **On stage, in ink, there is now exactly one place
in this head that behaves categorically while everything around it slides.** That is the answer to
*"is the run's one categorical event distinguishable from the eight movements of degree — on stage,
not in the data"*: yes, and it is the only column of which it is true.

**I record the honest counterweight.** At the step that turns, those 61 px are **2.8 %** of the
2,206 px changing in the head at that millisecond; the clause above changes 1,845 px in the same
frame. The turn is the smallest live thing in the frame and it happens in the last 1.6 s of a 26.9 s
run. **It is legible and it is not loud.** I judged both readings against the screenshots and I take
the staging: the event is a stillness that breaks, and a stillness that breaks does not need to be
large — it needs to be in frame at the moment it breaks, and it is, at scroll 0, on a phone, at both
milliseconds. What would make it louder is weight or ink, and this house has withdrawn a repair for
arriving as a new register before. I do not order one.

---

## 3 · IT BOUGHT NO HEIGHT. Cut 1 of session 89 is discharged and the object is above its floor

`HEAD`'s `index.html` driven in the scratchpad beside the tree's, one script, one run
(`$S/cmp90.mjs`), stop 8:

| | 89 (`HEAD`) | 90 (tree) | cost |
|---|---|---|---|
| **390** figure top | 234.4 | 234.4 | 0 |
| **390** figure-top → controls-bottom | 327 px of 844 | **328 px** | **+1 px** |
| **390** hole sharing a frame with the whole figure | 273 px, 24/24 chips | **273 px, 24/24 chips** | **0** |
| **1400** figure-top → controls-bottom | 479 px of 900 | 598 px | +119 px |
| **1400** hole sharing a frame with the whole figure | 89 px, 24/24 chips | 89 px, 24/24 chips | 0 |

**The restaging cost one pixel at 390.** The claim that it rides an existing row and buys no height
is true, and I checked it against the thing it was protecting: `tools/frame.mjs` now prints Cut 1's
own item —

```
phone 390×844 — figure-top to controls-bottom: 328 px of 844 — HOLDS
  the hole sharing a frame with the whole figure: 273 px, 24 of 24 chips at the last stop
      — floor 268 px / 22 chips — HOLDS
```

— and the object stands **5 px and 2 chips above the floor I set**, not on it. The instrument was
restated as ordered, the header carries the reason, and the span it replaced is gone. **Cut 1 of 89
is discharged.**

**The 119 px at 1400 is the proof block, and it stands above the controls at that width.** I priced
it rather than assuming: at 1400 the controls run 683.6–744.4 and the viewport is 900, so **the
controls and the run's line are still whole in the first screen, with 155.6 px to spare**, at every
stop. Nothing the performance invites you to press left the screen. At 390 the controls stand at
428 — above the material — so the proof at 1,148.8 costs them nothing at all. The placement below
the reserved space is honoured and the ordering claim in the build's comment is true as measured.

**Reflow across the nine stops.** Every node of the head is byte-stable at all nine stops at both
widths: figure `234.36/264.77`, when `267.97/321.13`, frac `325.94/343.53`, certain
`327.94/344.63`, standing `349.47/367.06`, controls `428.36/562.06`, state `506.06/554.06` at 390 —
identical at every stop; the same at 1400. Below the controls at 390 three blocks sit **0.12 px**
lower at stops 1–8 than at stop 0, from a line-height rounding in the hole's heading. **One eighth
of a pixel is not a reflow a reader can experience and I do not dress it as one.** The row members
are geometrically frozen too: `#sd-arrive-certain` occupies `119.94 … 291.86` at every stop, 53 px
clear of the content edge, so it cannot wrap and it does not.

**Occlusion, re-checked because the wide layout moved 119 px.** Every chip hit-tested at its own
centre, nine stops, every 40 px of the whole scroll range, both widths: **3,385 chips in view, 0
covered**; the new span in view 144 times, 0 covered. (Two hits at 390 landed on a centre lying
exactly on the viewport's last row and returned nothing; re-driven with the centre required strictly
inside, they vanish. I report the probe's own artefact rather than a finding it did not make.) §3
of 89 is undisturbed.

---

## 4 · THE PROOF BLOCK — it is not a shell command pasted on a work, because I ran it

The test of whether an evidence block is inert is whether it does anything. I copied three of the
nine lines the face prints and ran them, unedited:

```
--as-of 2026-08-05T04:39:32Z   →  1 capture(s) read · SHARE 100%–100%  (11 of 0–11)
--as-of 2026-08-11T11:19:15Z   → 23 capture(s) read · SHARE  33%–100%  (11 of 2–33)
--as-of 2026-08-12T18:23:12Z   → 26 capture(s) read · SHARE  31%–100%  (11 of 4–35)
```

The face at those three stops prints `100 %–100 % · 11 of 11 · 0 of them certainly dark`,
`33 %–100 % · 11 of 33 · 2 of them certainly dark`, `31 %–100 % · 11 of 35 · 4 of them certainly
dark`.

**The command reproduces the share AND the count that turns.** `0–11`, `2–33`, `4–35`: the lower end
of the band the terminal prints is the numeral tonight's restaging put in the frame. **The evening's
two builds verify each other** — the thing the head now stages is the thing the printed line
returns, and a stranger can close that loop in one paste. That is the opposite of decorative, and it
is the first time in this gate's life that a claim on this work's face has been checkable by a
visitor rather than by a critic. `git status` was byte-identical after I ran all three.

**It is height-stable, as claimed.** At every one of the nine stops the block is exactly 119 px at
390 and 89.25 px at 1400; the instant is 20 characters and the command 79 at all nine. It cannot
walk anything under a reader.

**It handles its own hardest moment.** At stop 0 the button says `ON THE DAY` and the printed
instant is `2026-08-05T04:39:32Z` — the day *after*. That looks wrong for one second and it is not:
the lead says the instant is *when this record first held every name the stop adds*, and the command
returns `1 capture(s) read · 100%–100%`. The sentence that absorbs that friction earns its place and
I keep it.

### But the block prints one thing twice, and tonight's build created that

```
y 1223   2026-08-12T18:23:12Z
y 1238   python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-12T18:23:12Z
```

I compared the strings in the data island at all nine stops: **`as_of` is a byte-exact substring of
`check` at every one of them.** The face prints the same twenty characters twice, on consecutive
lines, 15 px apart, at the same size, the same weight, the same family and the same ink. At 390 the
command wraps and the repeat lands at the *start* of its own line, directly under the first
printing. The block's payload is 44.6 px of its 119; **14.9 px of that payload — a third of it — is
a string the next line reprints in full.**

### And its lead is longer than the thing it introduces

266 characters, **70.5 px at 390 — five lines to introduce two.** Sentence by sentence:

> *"Every stop of this run is an instant of this record, and every instant is re-derivable from the
> saved copies in this repository."* — **the block described to a person looking at it.** Nine stops
> rewrite both strings at the same eight milliseconds as the figure; I ran three of the nine and got
> the three printed shares. The run performs this sentence, and the terminal performs it again.
>
> *"OBSERVED — the instant below is when this record first held every name the stop adds, read off
> the captures and not chosen."* — the tier word and the provenance. **No run performs it, it is the
> sentence that answers stop 0, and it stays.**
>
> *"This stop is:"* — thirteen characters of hinge. Stays.

---

## 5 · ECONOMY — what else tonight's build put twice on the face

Positions taken at 390, stop 8, in document order.

**(i) The caveat is now a node the run rewrites eight times without ever changing a character.**
I read `#sd-arrive-hedge` at all nine stops: **one string, nine times.** Yet it is set at 12.48 px in
`rgb(17,17,17)` — **the live ink, and 0.96 px larger than the numeral that took its job.** After
tonight the ink hierarchy of this head points the wrong way by a hair: the only sentence in the run
that cannot change is heavier than the only figure in the run that turns.

I do **not** order it changed, and I want the reason on the record, because it is the reason the
caveat survives at all: **that sentence is the key to the numeral.** *"A name counts as certain here
only when every day of that week leaves it dark on this one"* is what the word *certainly* means in
`4 of them certainly dark`, and a numeral whose unit is a published window needs its unit said once.
A visual code needs its key — the same ground on which I kept the ink key in 89. The key stands
738 px below the numeral at 390 and 275 px at 1400, which I note and do not order, exactly as I
noted the constant's 1,080 px in 89.

**(ii) The mechanism is on this face three times.** `#sd-arrive-hedge` at 1,066 (*"a list gives a
ship's return only to the nearest week"*), `#sd-arrive-since-note` at 1,686 (*"a list gives a return
only to the nearest seven days"*), `cut.refused` at 2,033 (*"its return falls in that edition's
seven-day window"*). The second carries a figure the first does not (22 of the 24) and the third is
the hinge of a different argument. **The first is now the only printing that carries nothing else** —
tonight's rewrite took its count away and moved it into the frame. It is not a clean cut: the clause
is the premise of the key in (i) and deleting it breaks the sentence that defines *certain*. Noted,
not ordered, and named here so the next session does not discover it as new.

**(iii) `arrive.tier` at 2,402** now reads *"this share, and the count of names certainly dark
**beside it**, are worked out here"*. The deixis reaches 2,074 px up the page to a row it calls
*beside*. One word, below every fold, in the tier band. Noted, not ordered.

**What tonight's build did NOT double.** The count in the frame does not restate the caveat (the
caveat no longer counts), does not restate the band in the evidence (2,000 px away, different
notation), and does not restate the heading of the hole (which counts ships, not certainties). The
one clean doubling this build created is the instant, and it is Cut 1 below.

---

## 6 · `tools/fold.mjs` 99 → 108 IS THE SAME MOVED RULER FOR THE THIRD SESSION, and tonight I can prove it

The instrument's probe grid is `range · k / 8`, where `range` is the bottom of `#sd-arrive` minus the
viewport height (`fold.mjs:72-79`). It is therefore a direct function of how tall the section is.
I drove both objects with one script (`$S/range90.mjs`):

```
89 (HEAD)   #sd-arrive bottom 2115   range 1271   step 159
            probes  0 · 159 · 318 · 477 · 636 · 794 · 953 · 1112 · 1271
            controls lost at 6/9 · run's line lost at 5/9  →  11 per stop  →  99

90 (tree)   #sd-arrive bottom 2547   range 1703   step 213
            probes  0 · 213 · 426 · 639 · 852 · 1064 · 1277 · 1490 · 1703
            controls lost at 6/9 · run's line lost at 6/9  →  12 per stop  →  108
```

**The run's line moved one pixel between the two objects** (506–554 against 505–553). **Its third
probe moved 162 px**, from 477 to 639, because the section got 432 px taller — and at 477 the line
was on screen, at 639 it is not. **That is the entire nine-failure difference.** Occlusions in
tonight's run: **zero** (`✗COVERS` appears not once in 306 marks). Chips covered: **zero**.

A gate cannot let this be entered a third time as a regression. Cut 3 below.

---

## 7 · FIRST ENCOUNTER, and the ENDING — checked because the build touched both, and both stand

**390, scroll 0, after the run.** The whole head is now on the first screen: the date, the subtitle,
the gloss, `31 %–100 %`, the clause, `11 of 35  4 of them certainly dark`, `11 of 230` and its note,
the nine buttons, the replay, the run's line, the eleven names the day printed, the hole's heading,
and **63 px and four chips of the reserved space itself**. In 89 a phone at scroll 0 met the heading
naming the space and not one pixel of the space. Tonight it meets four names of it. The cuts of 89
paid that, and the restaging did not spend it back.

**1400, scroll 0.** The whole argument is still on one screen and it is still the best thing in this
work — and the proof block is now inside that screen, 89 px of dim apparatus with two lines of live
ink, standing between the caveat and the controls. I looked hard at whether a shell command in the
best first encounter this work has damages it. **It does not:** it is set at 9.92 px in
`rgba(0,0,0,0.55)`, under a hole and a caveat, and the eye reaches the controls past it without
stopping. What separates the two copyable lines from the lead is ink alone — same size, same family,
same weight — and on the screen that is enough to read them as a different kind of object.

**The ending** — *"The run has finished. The figure now standing is this record's live one — press
any button to go back through it."* — is unchanged, still reachable, and now leaves a phone visitor
holding one more thing than it did: the count at its true value, in frame, 93.6 px under the figure.
Passed in 89, better tonight, not re-opened.

**What I checked and will not re-open:** the beat (§1c, level with 88 and 89), the reader who leaves
(paid in 89), the occlusion history (§3, re-driven and clean), the `100 %–100 %` reading (§4 of 89),
the run's own line (Cut 3 of 89 landed; measured 26.9 s load to done, and the sentence is now true).
Cuts 3–6 of session 89 are all in the object; I verified each by string search.

---

## VERDICT

# PASSES AS STAGED

**The restaging discharges the return.** I wrote one testable sentence in 89 and tonight it is false
of this object in every clause. The head's frame prints how much of the day is *known*: a live
numeral, on the fraction's own row, 93.6 px below the figure at 390 and 99.3 at 1400, rewritten at
the same eight milliseconds as the run's spine against a standing figure that never moves. In 89
**no** scroll position on a phone held the whole figure and the run's one categorical event in one
frame; tonight **235 of them do, and one is scrollY 0** — so a visitor who loads the page and touches
nothing meets `0 → 2 → 4` where they are already looking. And the event is told from the eight
movements of degree **on stage, in pixels**: the count's column is inert to the pixel across six
consecutive steps and then moves 61 and 59 px — the only column in this head of which that is true.

It was paid for out of nothing. **One pixel at 390.** The span my Cut 1 restated stands at 273 px and
24 of 24 chips against a floor of 268 and 22 — above it, not on it. Nothing reflows at nine stops at
either width beyond an eighth of a pixel. No chip is covered in 3,385 hit-tests. And the proof block
is not a shell command pasted onto a work: I ran three of the nine lines it prints and each returned
the share the face shows **and the certain count beside it** — the two builds of this evening verify
one another, and a stranger can close that loop in one paste without a critic's help.

**What is left is economy, and it is three cuts, none of them structural.**

### The cuts, each checkable by a stranger in a named file

1. **`index.html:2272` (the element) and `index.html:2589` (the write) — strike
   `#sd-arrive-proof-as-of`.** The line below it prints the same twenty characters: I compared
   `as_of` against `check` in the data island at all nine stops and it is a byte-exact substring of
   the command at every one. On a phone the command wraps and the repeat lands directly under the
   original, 15 px away, in the same size, weight, family and ink. **A third of the block's payload
   is a reprint.** The tier word and the provenance in the lead keep pointing at the instant, which
   remains on the face inside the command; a stranger checks the cut by reading two consecutive
   lines and finding one string.
2. **`index.html:1108` — strike the first sentence of `arrive.proof`**, *"Every stop of this run is
   an instant of this record, and every instant is re-derivable from the saved copies in this
   repository."* The block performs it: both strings are rewritten at every one of the eight beats,
   and I ran three of the printed commands and got the three printed shares. The lead is 266
   characters and 70.5 px at 390 — **five lines to introduce two.** The survivor, *"OBSERVED — the
   instant below is when this record first held every name the stop adds, read off the captures and
   not chosen. This stop is:"*, is the tier claim, the provenance, and the sentence that answers why
   `ON THE DAY` prints an instant dated the next day. Pure deletion; the survivor stands.
3. **The record — do not enter `fold.mjs` 99 → 108 as a regression.** The instrument's probe grid is
   `range · k / 8` (`fold.mjs:72-79`), and I drove both objects tonight with one script: the section
   grew 432 px, so the step grew from 159 to 213, so the run's line's third probe moved from 477 to
   639 and now falls after the line has left the viewport. **The element itself moved one pixel.**
   Zero occlusions, zero chips covered, in 306 marks. The honest entry is **12 must-hold losses per
   stop against 11, on a probe grid that stretched by 34 %** — and the standing entry, third session
   running, is that this instrument reports the height of the page.

**Cuts 1 and 2 are ordered for economy and cut 3 for truth. None is to be booked against any frame
measurement**; if a session prices their height as a gain, that is banked failure 48 recurring and I
have named it in advance, as I did in 89.

---

**Hash re-taken at the foot, after all measurement, by me:**

```
e98d1507f71bb0dc9ecfca3db587a366db3eb764f8e1116bbb58960cd834f4fb  projects/season1/still-dark/index.html
```

**Unchanged from the head of this memo. `git status` is byte-identical to what I found. The object
did not move under me and I did not move it.**

*Every position, size, weight, ink, letter-spacing, mutation timestamp, pixel-difference count,
probe grid, hit-test and instrument exit in this memo was taken by me tonight on the running object
at 390×844 and 1400×900. The pixel differences are decoded from element screenshots by a PNG
inflater written in this pass's own scripts. The comparison against last night is `HEAD`'s own file
written into the scratchpad and driven by the same script in the same run. The three terminal
outputs are the work's own printed commands, executed unedited. Published verbatim beside the work.*

---

**THE SENTENCE A SESSION SHOULD PRINT ABOUT THIS GATE:**

> The turn is on stage: the count of ships this day can be certain of now stands as live ink on the
> fraction's own row, 93.6 px under the figure, and where last night there was **no** position on a
> phone at which a visitor could hold the figure and the run's one categorical event in a single
> frame, tonight there are 235 of them and one is the top of the page — so a visitor who loads and
> touches nothing watches `0 → 2 → 4` arrive where they are already looking, in the only column of
> this head that is inert to the pixel for six steps and then moves; it cost one pixel at 390, the
> reserved space still shares 273 px and all twenty-four of its names with the whole figure, nothing
> reflows and nothing is covered; the proof beneath it is live, not decorative — three of its nine
> printed commands, run unedited, returned the share **and** the certain count the face shows — and
> what is left to cut is a twenty-character instant the next line reprints in full, a lead of five
> lines introducing two, and an instrument that went from 99 to 108 because the page got taller.
