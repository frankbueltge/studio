# DRAMATURG — STILL DARK, session 88

**Convened on the frozen object.** Hashes taken by me before I drove anything:

```
0e212c993ebc6e04a51a36462f490e4588b214b17bdf80c6208fee894261a5f7  projects/season1/still-dark/index.html
693855d08d1cc6723b48d48d81b4ee0b11a72945a0dd2455dac7fcbeb70328ec  projects/season1/still-dark/data.py
```

**I edited nothing but this file.** Where I needed to know what a part costs I removed it from the
live DOM of a headless page, re-fired the page's own `resize` so its own `reserve()` re-ran
(`index.html:2532`), and re-measured; the files on disk were never touched and the hashes are
re-verified at the foot.

I am here to test my own prescription for the second night running. Last night I built it, returned
it, and rewrote it. Tonight it was built to the new letter. **Where the answer is for the build I
say so first, and where it is against me I say that too.**

The control throughout is the page as committed **before tonight**, taken at the top of this pass:

```
mkdir -p $S/ctl && git show HEAD:projects/season1/still-dark/index.html > $S/ctl/index.html
sha256  78da6a5d08f0141be3a0d24fec212b4ca4a3a991c461fa2494d5c001571b12b5
```

**`HEAD` moved under me at 04:57 while I was measuring** — the build was committed as `1003f95`, and
`git show HEAD:` now returns the object under test. My control was extracted before that and its
hash matches `git show 658a6fd:projects/season1/still-dark/index.html` exactly, which I re-verified
after the fact. **Anyone re-running the control numbers in this memo must write `658a6fd`, not
`HEAD`** — quoting `HEAD` as a control after the commit lands is the defect I convicted `frame.mjs`
of last night (`DRAMATURG-87.md` §2), and it would have swallowed this whole memo silently.

`$S` is this session's scratchpad. Every script named below is in it.

---

## 1 · THE QUESTION, ANSWERED: YES — the run now does the arguing

**Driven.** `$S/frame88.mjs` — chromium 390×844 and 1400×900, light, `reducedMotion: reduce`, all
eight stops pressed through `#sd-arrive-ladder`, `getBoundingClientRect` and `getComputedStyle` on
every node of `.sd-arrive-headline`; `$S/mut88.mjs` — a 40 s free run with motion ON at 1400×900 and
a `MutationObserver` on six named nodes; `$S/shot88.mjs` — element screenshots of the frame at
stop 0 and stop 7 at both widths, `deviceScaleFactor: 2`, looked at.

**The eight states, read off the live DOM** (`node $S/frame88.mjs projects/season1/still-dark`):

```
stop 0  100 %–100 %  | 11 of 11 | 11 of 230       stop 4   55 %–100 %  | 11 of 20 | 11 of 230
stop 1   79 %–100 %  | 11 of 14 | 11 of 230       stop 5   44 %–100 %  | 11 of 25 | 11 of 230
stop 2   69 %–100 %  | 11 of 16 | 11 of 230       stop 6   35 %–100 %  | 11 of 31 | 11 of 230
stop 3   65 %–100 %  | 11 of 17 | 11 of 230       stop 7   33 %–100 %  | 11 of 33 | 11 of 230
```

Last night's whole charge was one sentence: *"Eight states, and not one of them prints `11`"*
(`DRAMATURG-87.md:96`). **Eight states, and every one of them prints `11` now.** The numerator
repeats down the column, the denominators go 11 · 14 · 16 · 17 · 20 · 25 · 31 · 33 against a 230
that never moves. That is the thing I asked for, in the words I asked for it in.

**Judged at stop 0, as ordered.** The frame reads `100 %–100 %` over `11 of 11` over `11 of 230`.
This is the moment the disclosure is largest and last night it was the moment it was most invisible,
because *"`100 %` and `11 of 230` have no digit in common"* (`DRAMATURG-87.md:101`). They have three
digits in common tonight. A stranger sees a list that thought it had all of it — `11 of 11`, the
same eleven — and, one line under, the same eleven against the 230 the list itself says it looked
through. Nothing tells them that. The two lines say it.

**Judged at stop 7.** `33 %–100 %` over `11 of 33` over `11 of 230`. The run has moved one
denominator by 22 and left the other alone, in one column, in the same face and the same tabular
figures. Last night at this stop the two figures were *"as unrelated to the eye as they were at
second zero"*; tonight the relation is the only thing in the column that changed.

**The run's own arithmetic, timed** (`node $S/mut88.mjs`, 40 s, motion on, 1400×900):

```
#sd-arrive-count-falling      7 mutations   first 14053 ms   last 23653 ms   → «33 %»
#sd-arrive-frac               7 mutations   first 14053 ms   last 23653 ms   → «11 of 33»
#sd-arrive-frac-note          0 mutations
#sd-arrive-standing-fig       0 mutations
#sd-arrive-standing-note      0 mutations
```

The two numerals are rewritten **at the same millisecond, seven times** — 14053 · 15654 · 17253 ·
18853 · 20453 · 22053 · 23653 — and nothing else in the frame moves at all. The clause under the new
figure is written once, on load (`index.html:2284`), and it holds through a whole run. That is
staging, and it is the second half of my prescription executed as exactly as the first half was
executed last night.

**No reflow.** `.sd-arrive-headline` stands at 268–523 at every one of the eight stops at 390, and
163–376 at every one at 1400 (`$S/frame88.mjs`, eight-state block). The reservation absorbs the new
row.

**The added row is staging, not a second annotation.** It moves with the run, in the run's ink, in
the run's column, at the standing figure's size. **The clause under it is a second annotation, and
§3 is about nothing else.**

---

## 2 · THE `cannot move` MARK — it kept one meaning, and the size axis now carries the sign it lacked

Last night I convicted the mark of carrying two meanings without a second sign:
*"dim ink now means two different things in one block … A stranger has no key to that"*
(`DRAMATURG-87.md:79`). Measured tonight at 390×844 and 1400×900 (`$S/frame88.mjs`):

| node | 390 px | 1400 px | ink | mutations in a 40 s run |
|---|---|---|---|---|
| `#sd-arrive-count-falling` | 30.4 px / **700** | 46.4 px / **700** | `rgb(17,17,17)` | **7** |
| `#sd-arrive-count-fixed` | 30.4 px / 400 | 46.4 px / 400 | `rgba(0,0,0,0.55)` | 0 |
| `#sd-arrive-frac` | 17.6 px / **700** | 24 px / **700** | `rgb(17,17,17)` | **7** |
| `#sd-arrive-standing-fig` | 17.6 px / 400 | 24 px / 400 | `rgba(0,0,0,0.55)` | 0 |

Both new numerals are `font-variant-numeric: tabular-nums`, both new rows share a left edge at x 22.
**The rule is now exact and it is exceptionless on the face: live ink at display weight is rewritten
by a stop; dim ink at body weight is written once.** The size axis says which language — percent
above, ships below. The CSS claims precisely this at `index.html:150-152`: *"The mark this face has
meant by CANNOT MOVE since session 83 keeps its one meaning: it is on the row that does not move and
off the row that does."* **Measured, that claim is true.**

It is true at the clause layer as well, which I did not expect and checked because I did not:
`#sd-arrive-when`, the clause under the falling percentage, is live ink (`rgb(17,17,17)`, 13.12 px at
390) and it **is** rewritten by a stop — 91 characters at stop 0, 128 at stop 7. Both dim clauses
mutate zero times. **Four numerals and three clauses, one rule, no exception.** My §1 charge of last
night is discharged and I strike it.

---

## 3 · THE CLAUSE — the 11.52 px sentence did not go; it doubled, and it re-tells the sentence deleted three lines below it

My prescription ended: *"the run does the arguing, and the 11.52 px sentence can go"*
(`DRAMATURG-87.md:109-110`). Measured, the small print in the frame at 390×844
(`$S/frame88.mjs`, both builds):

| | 11.52 px prose in the frame | height at 390 |
|---|---|---|
| committed page | `standing_note`, 166 ch | 67 px |
| tonight | `fraction_note` 228 ch + `standing_note` 79 ch = **307 ch** | 83 + 33 = **116 px** |

**+141 characters, +49 px. The sentence I retired grew by 85 % in text and 73 % in height.**

And the character it wrote is the character it deleted. The control's note read
*"— the list of 4 AUG named eleven ships out of the 230 disappearances it says it examined. **No stop
moves this figure.** SOURCED — the count of names is this house's own."* (read off the control DOM).
That sentence is gone from `index.html:734`, correctly, because the run performs it. Three lines
higher, `index.html:736` now reads:

```
"fraction_note": "— the falling end as a division: the names the day's list had already given, of
the ships that could have been dark on it. The other end is 11 of 11 at every stop. OBSERVED over
DERIVED — the count of names is this record's own.",
```

***"The other end is 11 of 11 at every stop"* is *"No stop moves this figure"* with a different
subject.** The session struck a told-not-shown sentence out of one row and wrote a longer
told-not-shown sentence into the row above it, in the same block, on the same night. That is the
defect migrating upward, not being paid.

**And the figure it tells is one the page holds and declines to print.** `index.html:749` and its
seven siblings carry `"share_fixed_of": "11 of 11"` at every stop, and the record's own block carries
`"fraction_fixed": "11 of 11"` at `index.html:1698` and `:1709`. `grep -n "share_fixed_of"` finds
eight data entries and **no line of script that renders any of them** — the only consumer in the file
is `fracEl.textContent = s.share_falling_of` at `index.html:2380`. So the frame prints one end of the
band in ships, keeps the other end in the file, and puts it in 11.52 px prose instead. **That is the
exact fault I convicted last night, one row down and one night later.**

**It collides with itself at stop 0.** At stop 0 the numeral reads `11 of 11` and three lines under
it the clause reads *"The other end is 11 of 11 at every stop."* The same eight characters, twice on
one phone screen, naming two different ends of the band. I looked at it magnified
(`$S/shots/new-390-frame-stop0.png`). It is not a subtlety; it is the largest and the smallest ink in
the block saying the same string about different things.

**It stands between the two figures it exists to join.** Measured (`$S/w88.mjs`), the gap from the
bottom of `#sd-arrive-frac` to the top of `#sd-arrive-standing-fig`:

```
 390 as shipped   92 px      1400 as shipped   56 px
 390 frac-note CUT  5 px     1400 frac-note CUT  5 px
```

At 390 the clause wraps under its numeral and wedges **92 px — five lines of the dimmest ink on the
page — between the two fractions whose comparison is the entire finding.** That is 5.1 times the
height of either numeral (18 px each). At 1400 the clause sets to the right at x 151 and the left
column reads clean: `33 %–100 %` / `11 of 33` / `11 of 230`, three figures, nothing between them.
**The staging is unambiguous at 1400 and is being read across a grey wall at 390** — and 390 is the
width every frame fight in this work's last four sessions has been about.

**The frame's own balance, in characters** (`$S/frame88.mjs`, stop 0, 390):

| | prose | figures | ratio |
|---|---|---|---|
| committed page | 257 ch | 20 ch | 12.9 : 1 |
| tonight | 398 ch | 28 ch | 14.2 : 1 |
| tonight, `#sd-arrive-frac-note` cut | 170 ch | 28 ch | **6.1 : 1** |

The build added a figure and made the frame wordier per figure than it was. The cut makes it the
least wordy frame this head has had.

---

## 4 · THE PRICE — the staging cost 18 px and was bought at 104

**Driven.** `node tools/frame.mjs --dir=projects/season1/still-dark` and the same against `$S/ctl`;
then `$S/cut88b.mjs`, which removes an element, fires `resize` so the page's own `reserve()` re-runs,
and takes the maximum over all eight stops. **Its no-cut baseline reproduces `frame.mjs` exactly —
943 / 387 / 255 — so the method is checked before any delta is quoted from it.**

```
tools/frame.mjs, phone 390×844        figure→controls     figure→hole-bottom     frame block
  committed (git show HEAD → $S/ctl)      311 px HOLDS       867 px  OVER 23        179 px
  tonight                                 387 px HOLDS       943 px  OVER 99        255 px
tools/frame.mjs, wide 1400×900
  committed                               554 px HOLDS       423 px  HOLDS          149 px
  tonight                                 617 px HOLDS       486 px  HOLDS          212 px
```

The house's three numbers are confirmed: 311 → 387, 867 → 943, over by 23 → **over by 99**.

**What each part of tonight's build actually cost** (`node $S/cut88b.mjs`, 390×844, max over 8 stops,
page's own reservation re-run):

```
  hole  943 px OVER 99  · frame 255 px   nothing cut — reproduces frame.mjs
  hole  857 px OVER 13  · frame 168 px   #sd-arrive-frac-note cut          (−86 px)
  hole  907 px OVER 63  · frame 218 px   #sd-arrive-standing-note cut      (−36 px)
  hole  820 px HOLDS    · frame 132 px   both small-print clauses cut      (−123 px)
  hole  839 px HOLDS    · frame 151 px   the whole new row reverted        (−104 px)
  hole  856 px OVER 12  · frame 255 px   #sd-arrive-constant cut           (−87 px)
  hole  872 px OVER 28  · frame 255 px   #sd-arrive-state cut              (−71 px)
  hole  909 px OVER 65  · frame 255 px   #sd-arrive-head-then cut          (−34 px)
  hole  769 px HOLDS    · frame 168 px   frac-note + constant             (−174 px)
  hole  822 px HOLDS    · frame 168 px   frac-note + day's heading        (−121 px)
```

Read those three ways, and each is a finding:

1. **The numeral costs 18 px.** Revert the whole row: 839. Keep the numeral, cut its clause: 857.
   **The difference between the staging and no staging is 18 px. The difference between the staging
   and the annotation under it is 86 px.** The house paid 104 px, of which 17 % is the thing I
   ordered built.
2. **The prose cut alone would have paid last night's debt with 5 px to spare.** Reverting tonight's
   row leaves 839 of 844 — because the same session that added 109 px of new row also trimmed
   `standing_note` from 166 characters to 79, worth 28 px against the committed 867. **Cut 3 of last
   night's re-verdict — *"Pay the 23 px"* (`DRAMATURG-87.md:818`) — was in the session's hand,
   already earned, and was spent on a clause.**
3. **The cut lands the item green for the first time in this work's measured life.** Cut the clause
   and the day's heading: 822 of 844. Cut the clause and the constant: 769 of 844, 75 px of slack.

**And the frame ends up smaller than the published one while carrying a figure more:** 168 px at 390
against the committed 179, 161 px at 1400 against the committed 149 (`$S/w88.mjs`). The prescription,
executed with the cut, is **−11 px on a phone and +1 figure.**

**What the taller head costs a stranger, in the piece's own terms.** At 390, stop 7, the top of
`#sd-arrive-names-since` — the space the work exists to show filling — stands at y 961 on the
committed page's 885 (`$S/frame88.mjs`). Both are below an 844 px fold; **the deficit went from 41 px
to 117 px.** I looked at the phone screen (`$S/shots/new-390-stop7.png`): a stranger holding a phone
at the last stop sees the title, the definition, `33 %–100 %`, `11 of 33`, five lines of grey,
`11 of 230`, two lines of grey, the buttons, the run's line, the constant, the day's heading, and the
day's own eleven names. **They do not see one chip of the twenty-two that later lists gave.** The
piece has two arguments — a number falling, a space filling — and tonight it traded the second for
the first. **Answered plainly: the row is worth it. The clause is not, and the clause is 86 of the
104 px.**

---

## 5 · THE INSTRUMENTS — one is verified, and the other's 8-point improvement is a moved ruler

**`tools/frame.mjs`'s second span is sound, and it retro-validates a number nobody could re-run.**
Its own comment says both sessions *"quoted it from a number nobody could re-run"* (`frame.mjs:66-69`).
Run against the committed page it returns **867 px of 844, over by 23** — the exact figure I took by
hand last night and printed at `DRAMATURG-87.md:818`. An instrument that reproduces the hand
measurement it was built to replace has been checked. My own independent method (`$S/cut88b.mjs`)
reproduces tonight's 943 to the pixel. **Three roads, one number.**

**Its exit contract is as advertised.** `node tools/frame.mjs --dir=projects/season1/still-dark;
echo $?` → **0**, while printing `OVER by 99`. The file states this at `frame.mjs:70-72`:
*"this span is reported red or green and left to the session to argue. An instrument that failed the
build on a measurement no gate has ruled on would be legislating."* I have now ruled on it (§4). The
next session may make it a gate; I do not order it tonight, and the summary line above the exit —
`FRAME: the figure and the controls fit one screen at every stop` — names its subject precisely and
is not made false by the red span printed three lines above it. Checked, not a fault.

**`fold.mjs` 88 → 80 is not an improvement and must not be banked as one.**
`node tools/fold.mjs --dir=…; echo $?` → **1** on both builds.

```
                              committed   tonight
  ✗OFF marks printed, total       104        104
  phone: the figure OFF            56         56
  phone: the controls OFF          48    →    40
  phone: the run's line OFF        40         40
  chips covered                     0          0
  FOLD failures                    88    →    80
```

The whole delta is the controls, at exactly one scroll probe per stop (8 × 1 = 8). `fold.mjs:76-79`
walks `range * k / 8` for `k = 0…8`, and the head got taller, so the probe grid stretched: the
committed page is probed at `0 · 162 · 323 · 485 · 646 · 808 · 969 · 1131 · 1292`, tonight's at
`0 · 171 · 342 · 513 · 684 · 855 · 1026 · 1197 · 1368`. At the committed probe 3 (y=485) the controls
stand at −30–15 and fail; at tonight's probe 3 (y=513) they stand at 18–63 and pass. **Nothing was
repaired. The ruler's tick marks moved because the page grew, and eight failures fell through the
gap between them.** The instrument is not at fault — it samples, and it says so — but a session that
prints *"fold went 88 to 80"* beside *"the head is 76 px taller"* is printing a coincidence as a
credit. It is failure-shaped, and I name it before the record does.

---

## 6 · WHAT I CHECKED BECAUSE I CONVICTED IT BEFORE, AND FOUND CLEAN

1. **No doubled figure.** `$S/dup88.mjs` walks every leaf node and prints every occurrence of
   `11 of` or `230` on the rendered page. The record's own band `11 of 2–33` (`.sd-share-of`) stands
   **5,360 px below** the frame at 390 and **3,388 px below** at 1400, in a different notation (both
   ends, 11.52 px). It is not the 588 px doubling I struck last night. `230` appears in the frame,
   once in `#sd-arrive-cut-figs` at y 1499 with the pointer I ordered repaired, and once in a table
   cell at y 6296. No figure is published twice in one glance.
2. **The reservation holds under the new row.** Frame box byte-identical across all eight stops at
   both widths (§1). Nothing steps.
3. **The tier vocabulary survives the cut I am about to order.** `#sd-arrive-tier` at
   `index.html:2128` publishes *"DERIVED — this share is worked out here, from saved copies of those
   lists. Nobody publishes it."*, and `standing_note` keeps `SOURCED`. Deleting `fraction_note`
   removes no tier mark that the page does not already carry.
4. **The clause under the standing figure is doing work and stays.** 79 characters, 33 px at 390. It
   is the only place the face says what the 230 *are* — disappearances the list says it examined,
   not names. No run can show that. It is the one piece of prose in this frame I will defend.

---

## 7 · WHAT I DID NOT MEASURE

1. **`announce.mjs` and `gaps.mjs`.** Not run. The new numeral is inside no live region — the page's
   only one is `#sd-arrive-state` at `index.html:2105` — so a screen-reader visitor hears the run's
   five sentences and neither figure. That was true last night for the percentage and is now true for
   two numerals. Unchanged, unmeasured, still first in the queue.
2. **The dark scheme, and any width between 390 and 480.** Both builds driven at 390 and 1400 only.
3. **`data.py`**, beyond `grep` for the four keys quoted here.
4. **The ending after the last stop, and everything below `#sd-arrive-tier`.**
5. **Whether cutting `#sd-arrive-constant` costs a meaning the run does not perform.** I priced it
   (−87 px) and read it; three of its four clauses are now performed by the three rows, the fourth is
   a conditional about lists not yet published, which no run can show. **I have not decided that, and
   I do not order it.**

---

## VERDICT

**PASSES AS STAGED — and the cut in §4 is a condition of shipping, not a suggestion.**

**The restaging verdict lifts.** It lifts on the measurement it was given on: the two figures share a
term, the run rewrites one denominator seven times and leaves the other alone, both numerals move at
the same millisecond, both clauses hold still, and the `cannot move` mark governs four numerals and
three clauses without an exception. At stop 0 a stranger sees `11 of 11` over `11 of 230`; at stop 7
`11 of 33` over `11 of 230`. **Nothing tells them the relation. The column shows it.** That is what I
asked for two nights running, and it is built.

**I am passing this and not returning it for a reason I will state as a rule, so it can be used
against me later: restaging is owed when no cut can fix it; a cut is owed when a cut can.** Last
night's fault needed a build and I returned it. Every fault I found tonight is payable by deletion.

**But this page must not ship as it stands, and that is new.** I shipped in 85 and 87 on the ground
that *"nothing on this face is worse than what is published"* (`DRAMATURG-87.md:838`). **That ground
is gone tonight**: figure-top to hole-bottom is 943 against the published 867, and the one frame in
which a phone reader can watch the number fall and the space fill is 99 px away instead of 23. Ship
with the cut taken. It is one element and one string, it takes the item to 857 — **smaller than the
debt I ordered paid last night** — and it makes the frame 168 px, eleven pixels under the published
one, carrying a figure more.

**The cuts I order, and nothing else:**

1. **Delete `#sd-arrive-frac-note` entirely** — the element at `index.html:2065`, its write at
   `index.html:2284`, and the `fraction_note` string at `index.html:736`. **86 px at 390×844**
   (943 → 857); frame 255 → 168 px at 390 and 212 → 161 px at 1400; the gap between the two
   fractions **92 px → 5 px** at 390 and 56 → 5 at 1400. It re-tells the sentence deleted three lines
   under it, it prints in prose a figure the file already holds unrendered at `index.html:749`, it
   collides with its own numeral at stop 0, and it stands in the road between the two figures it was
   written to join. **This is my own prescription's last clause, unbuilt: the 11.52 px sentence can
   go.**
2. **Pay the remaining 13 px, and not out of whitespace.** Measured (`$S/ws88.mjs`): the frame's
   `margin-bottom` (8 px) plus its `gap` at half (5 px) lands at **exactly 844 of 844** — a hold with
   zero slack, which I refuse as a hold. Take it from an element: **`#sd-arrive-constant`, −87 px →
   769 of 844 with 75 px of slack**, or `#sd-arrive-head-then`, −34 px → 822 with 22 px. My order is
   the constant, subject to §7.5; the day's heading is the safe one and I will not argue with it.
3. **Do not touch the new row, and do not cut `#sd-arrive-standing-note`.** Reverting the row buys
   104 px and deletes the finding. Cutting the standing note buys 36 px and deletes the only line
   that says what 230 counts.
4. **Do not bank `fold.mjs` 88 → 80 as a repair.** §5. It is a moved ruler, and the honest entry is
   that the instrument is red at 80 for the same reason it was red at 88.

---

**Hashes re-verified at the foot, after all measurement, by me:**

```
0e212c993ebc6e04a51a36462f490e4588b214b17bdf80c6208fee894261a5f7  projects/season1/still-dark/index.html
693855d08d1cc6723b48d48d81b4ee0b11a72945a0dd2455dac7fcbeb70328ec  projects/season1/still-dark/data.py
```

Unchanged from the head of this memo. The object did not move under me and I did not move it.

*Every position, type size, weight, colour, character count, mutation timing, span and instrument
exit in this memo was taken by me tonight on the running object; the control is `658a6fd` rendered
out of a second directory, extracted before that commit landed; the cut prices are taken with the page's own
`reserve()` re-run and are checked against `tools/frame.mjs` at the baseline. Scripts are in this
session's scratchpad. Published verbatim beside the work.*

---

**THE SENTENCE A SESSION SHOULD PRINT ABOUT THIS FINDING:**

> The falling figure speaks in ships at last and the run does the arguing — `11 of 11` to `11 of 33`
> over an unmoving `11 of 230`, the two numerals rewritten at the same millisecond seven times and
> the standing one never, so the disclosure is performed instead of asserted and the staging verdict
> lifts; but the 228-character clause written under it is not the 11.52 px sentence going, it is that
> sentence doubling — the frame's small print grew from 166 characters to 307, it re-tells in the
> row above the very sentence it deleted in the row below, it prints in the page's dimmest ink a
> figure the file already holds unrendered, it wedges 92 px of grey between the two fractions it
> exists to join on a phone, and it costs 86 of the 104 px that took figure-top-to-hole-bottom from
> 23 px over one phone screen to 99 — cut that one element and the same frame is 168 px, eleven
> pixels smaller than the published one while carrying a figure more.

---
---

# RE-PUT ON THE CHANGED STATE — session 88, after the cuts

**Re-convened on the object as it now stands. Hashes taken by me before I drove anything:**

```
5325c15a7a3004be4194a674300cd9e6f32ae7d12fa4b93ce57484338a13a5b8  projects/season1/still-dark/index.html
ed083eab4edf63434b4fb1b1c2ea486d841570296cdcba0e7f53dd791668636b  projects/season1/still-dark/data.py
```

Both differ from the hashes at the head of the memo above; the object moved and this section is
taken on the moved one. **The memo above is untouched.** I edited nothing but this file. Control is
still `658a6fd`, extracted before the build landed, `sha256 78da6a5d…`.

---

## R1 · THE FRAME — it stages better without the clause than with it

`node $S/frame88.mjs projects/season1/still-dark` (390×844 and 1400×900, all eight stops):

| | `658a6fd` | my pass | now |
|---|---|---|---|
| gap, fraction-bottom → standing-top, 390 | — | 92 px | **5 px** |
| gap, same, 1400 | — | 56 px | **5 px** |
| frame block, 390 | 179 px | 255 px | **185 px** |
| frame block, 1400 | 149 px | 212 px | **161 px** |
| `standing_note` | 166 ch / 67 px | 79 ch / 33 px | **120 ch / 50 px** |
| prose : figure, in characters, 390 | 12.9 : 1 | 14.2 : 1 | **7.5 : 1** |

**The numeral standing clauseless is the better object.** The two fractions are now 5 px apart at
both widths — the number I priced — and the column reads `33 %–100 %` / `11 of 33` / `11 of 230`
with nothing between them. I looked at it magnified (`$S/shots/after-390-frame-stop7.png`). At 390 it
is now what it already was at 1400: three figures in one column, one of them rewritten by the run.

**The mutation rule holds, and it is cleaner than the one I verified.** `node $S/mut88.mjs`, 40 s
free run, motion on: `#sd-arrive-count-falling` **7**, `#sd-arrive-frac` **7** — same milliseconds,
14047 · 15647 · 17247 · 18847 · 20447 · 22047 · 23647 — `#sd-arrive-standing-fig` **0**,
`#sd-arrive-standing-note` **0**; `#sd-arrive-when` still rewritten per stop in live ink (91 ch at
stop 0, 128 at stop 7). *(My script also printed one phantom mutation for the deleted
`#sd-arrive-frac-note`: that is its own missing-node marker, not an event. Disclosed rather than
quoted.)* The rule is now **four numerals and two clauses**, and the one dim clause left in the frame
belongs to the one figure that cannot move — where before a dim clause hung under a live numeral.
The frame is 6 px taller than `658a6fd` at 390 and 12 px taller at 1400, carrying a figure more and
26 characters less prose than the published page. **That is the trade I asked for.**

**The attribution clause coming back (`VERIFIER-88.md` §3) is right and I do not contest a pixel of
it.** `standing_note` at `index.html:734` is 41 characters longer than what I measured and costs
17 px at 390. A bare `SOURCED` over a count this house derived is a false tier mark, and a false tier
mark is worth more than 17 px. My §6.4 defended this clause and was measuring a version of it that
had already been cut; the verifying voice caught what I did not.

---

## R2 · THE CONSTANT'S MOVE — it is the cut, and its landing was not measured

**Ruling on the question put to me: moving it is the cut, not an evasion.** The span I ruled on asks
what stands **between** the figure and the space that fills under it. 88 px genuinely stopped
standing there — `frame.mjs` now reports *"what the ends of the figure can do — outside the frame at
this width"* at **both** widths, where at 1400 it was inside the span before. The string is on the
page verbatim, all 235 characters (`index.html:1029`), so nothing the run cannot perform was lost;
and the ceiling law it opens with is indeed published elsewhere in the body, at `index.html:1716`
— *"A ceiling that can only fall…"* — and again in the record's own output at `:1989`. The house's
account of its own change checks out.

**And it landed on top of a paragraph that already says its first sentence.** Measured
(`$S/after88.mjs`, 390×844):

```
  #sd-arrive-cap        1148–1317  h168  12.48px  rgb(17,17,17)
  #sd-arrive-constant   1322–1434  h112  12.48px  rgb(17,17,17)      gap: 5 px
```

`index.html:1038` ends: *"That is why the figure above falls, **and why it can only go on
falling**."* `index.html:1029` begins, 5 px lower, in the identical size and the identical ink:
*"**Neither end of this figure can rise.**"* **Those are one sentence twice.** Last night I struck a
figure published twice 588 px apart. This is a law published twice **5 px** apart, in matching type,
read as one block of four sentences. I looked at it (`$S/shots/after-390-cap-constant.png`); it is
not a subtlety.

**Two further costs of the landing, measured, neither of them fatal:**

1. **The paragraph got louder on its way out.** `11.52 px` dim `rgba(0,0,0,0.55)` → `12.48 px` live
   `rgb(17,17,17)`, and 83 px → 112 px at 390. The retired explanation of the mark is now larger and
   blacker than it was in the spine. Inside the frame this would break the rule of §2; it is outside
   the frame and matches its new neighbours, so it is a loudness question, not a mark question.
2. **The pointer stretched.** *"this figure"* stood 128 px under the frame at 390 and 4 px at 1400;
   it now stands **869 px** under it at 390 and **440 px** at 1400 — 1,054 px from the top of the
   figure it names. It has an antecedent 5 px above (*"the figure above"*, itself 880 px from the
   figure, inherited), which is how a reader will resolve it, and that antecedent is the doubled
   sentence.

---

## R3 · IS 786 REAL — yes, and here is its arithmetic

`node tools/frame.mjs --dir=projects/season1/still-dark; echo $?` → **0**

```
phone 390×844 — figure-top to controls-bottom: 317 px of 844 — HOLDS
  figure-top to hole-bottom: 786 px of 844 — HOLDS
wide 1400×900 — 495 px HOLDS · 364 px HOLDS
```

All four house numbers confirmed. **786 = 943 − 86 (`fraction_note`) − 88 (the constant) + 17
(the attribution clause restored).** It reconciles to the pixel against my own cut prices, taken two
hours earlier by a different method. **Green, and the first green this item has measured** — my §4
target was 857 and the object came in 71 px under it.

**But 88 of the 157 px moved rather than went, and the page is longer, not shorter.** At 390 the
document is **7,243 px against `658a6fd`'s 7,190** and `#sd-arrive`'s scroll range **1,328 against
1,292**. The frame is green because prose left the corridor between the figure and the hole, which
is the right thing to have happened; it is not green because the page got shorter. Both facts belong
in the record.

`node tools/fold.mjs …; echo $?` → **1**, **88 failures** — level with `658a6fd`, as §5 said it
would be. Third data point on the same claim: scroll range 1,292 → **88**, 1,368 → **80**,
1,328 → **88**. **The count tracks the head's length, not its repair.** `tools/tiers.mjs` exits **0**.

---

## R4 · IS ANYTHING WORSE THAN `658a6fd` — one thing, and I name it plainly

**Everything I priced is better or level:** the span 867 → 786 (green), the frame's prose per figure
12.9 : 1 → 7.5 : 1, the two figures joined at 5 px instead of never, `fold.mjs` level, `tiers.mjs`
green, no reflow across eight stops at either width (`frame@268–453` at all eight, 390;
`163–325` at all eight, 1400), no figure published twice within one screen.

**One thing is worse: the junction at `index.html:1038` / `:1029`.** On the published page those two
paragraphs stood 655 px apart at 390 in different sizes and different inks. They now stand 5 px apart
in the same size and the same ink, saying the same law twice. Nothing else on this face is worse than
what is published.

---

## RE-VERDICT

**PASSES AS STAGED — the verdict of the memo above stands, its condition is discharged, and one cut
is owed at the landing site.**

The cut I made a condition of shipping was taken whole, and taken better than I priced it: the frame
holds the two fractions 5 px apart, the item is green at 786 of 844 for the first time in this work's
life, and the run still does the arguing at seven mutations to zero. **Ship it.**

**The one cut owed, and nothing else:**

1. **Strike the first sentence of the constant — *"Neither end of this figure can rise."*
   (`index.html:1029`)** — or the last clause of the caption, *"and why it can only go on falling"*
   (`index.html:1038`). One of the two, not both: they are one statement, 5 px apart, in matching
   type. Whichever goes, the survivor should carry the pointer, because *"this figure"* is now
   1,054 px from the figure at 390 and its only nearby antecedent is the sentence being struck.
   It costs one line — about 19 px at 390 — and it is not a px cut; it is the doubling rule this
   house applied at 588 px applied at 5.

**Ship tonight with this one item open.** It is a sentence, it is below the fold, it is not on the
staging, and holding a green frame for it would be holding the best measured state of this head over
a repair that fits in one line.

**Hashes re-verified at the foot of this re-put, after all measurement, by me:**

```
5325c15a7a3004be4194a674300cd9e6f32ae7d12fa4b93ce57484338a13a5b8  projects/season1/still-dark/index.html
ed083eab4edf63434b4fb1b1c2ea486d841570296cdcba0e7f53dd791668636b  projects/season1/still-dark/data.py
```

Unchanged from the head of this section.

---

**THE SENTENCE A SESSION SHOULD PRINT ABOUT THE RE-PUT:**

> The cut was taken and the frame is the best this head has measured — the two fractions 5 px apart
> at both widths where they stood 92 apart, seven mutations to zero, 7.5 characters of prose per
> character of figure against the published 12.9, and figure-top to hole-bottom green at 786 of 844
> for the first time in this work's life, reconciling to the pixel as 943 − 86 − 88 + 17; the
> constant's move out of that corridor is the cut and not an evasion of it, since the string travels
> whole and the law it opens with is published in the body at `index.html:1716` — but 88 of the
> 157 px moved rather than went, the page is 53 px longer than the one published, and the paragraph
> landed 5 px under a caption that already ends *"and why it can only go on falling"* to open
> *"Neither end of this figure can rise"*, in the same size and the same ink: one law printed twice
> at 5 px by a house that struck a figure printed twice at 588.
