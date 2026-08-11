# DRAMATURG — STILL DARK, session 87

**Convened on the frozen object.** Hashes verified by me, before I drove anything:

```
f43a481b59933f43806931c87c26cd8fbdf30f3ea87d735fae3da202a79b8eaa  projects/season1/still-dark/index.html
3a459aaa4a2f3f55d797bb18e4090cb468e4fcd665f60a9ed7ee63dd5359488f  projects/season1/still-dark/data.py
```

Both match the dispatch. **I edited nothing.** Where I needed to know what a part costs, I removed it
from the live DOM of a headless page and re-measured; the file on disk was never touched, and the
hashes are re-verified at the foot of this memo.

I am here to test my own prescription. Session 85 asked for *"the disclosure inside the numeral, a
second figure standing still in the same frame while the first falls."* It was built tonight. I
answer for it below, and where the answer is against me I say so.

**Everything numbered here was measured tonight on the running object.** Two readings I drafted from
the screenshots before taking them turned out wrong when I drove the run properly (stops 2–5 of the
falling figure); the measured values stand and the drafted ones are gone. Banked failure 23 is a
measurement written into a memo before it was taken, and I will not add to it.

---

## 1 · THE SECOND FIGURE — built to the letter, and it is annotation with a better address

**Driven.** Chromium at 390×844 and 1400×900, light scheme, `reducedMotion: reduce`; all eight stops
pressed through `#sd-arrive-ladder`; `getBoundingClientRect` and `getComputedStyle` on every node in
`.sd-arrive-headline`; a `MutationObserver` on eight named elements across a full 40 s free run with
motion on; viewport and full-page screenshots at stop 0 and stop 7, magnified and looked at.

**The frame, measured at 1400×900:**

| | node | box | type | ink |
|---|---|---|---|---|
| row 1 | `#sd-arrive-count-falling` `33 %` | 163–210 | 46.4 px / **700** | `rgb(17,17,17)` |
| row 1 | `#sd-arrive-count-fixed` `–100 %` | 163–210 | 46.4 px / 400 | `rgba(0,0,0,0.55)` |
| row 1 | the clause | 191–250 | 15.2 px / 400 | `rgb(17,17,17)` |
| row 2 | `#sd-arrive-standing-fig` `11 of 230` | 255–279 | **24 px / 400** | `rgba(0,0,0,0.55)` |
| row 2 | `#sd-arrive-standing-note` | 263–313 | 11.52 px / 400 | `rgba(0,0,0,0.55)` |

At 390×844 the same block is two rows of 87 px and 88 px inside a 179 px frame — **the two rows are
the same height to within a pixel.**

**What the build got right, and I will not have it lost in the ruling.** The row is where I asked for
it: same column, same left edge, one row under the other, no rule between, inside one grid whose own
CSS comment says the grid exists *"so the second row cannot be read as a caption of the first."* It
wears the `cannot move` face this head has meant by dim ink at body weight since session 83. It is
written once on load. I confirmed that no stop touches it: `MutationObserver` on
`#sd-arrive-standing-fig` and `#sd-arrive-standing-note`, full free run, **0 mutations** on each,
while `#sd-arrive-count-falling` mutated 7 times in the same window (first at **14,073 ms**, last at
**23,673 ms**). Stop 0 and stop 7 hold the row at byte-identical text and identical boxes
(359–447 at 390, 255–313 at 1400). The prescription was executed faithfully. The fault below is not
a fault of execution.

**AND IT DOES NOT STAGE THE DISCLOSURE, for one reason I can put in a single measurement: THE TWO
FIGURES SHARE NO VISIBLE TERM.**

The finding — my finding, the one I asked to be staged — is that the numerator does not move. It is
**11** in both figures; the denominator under the percentage is 33, and the list's own denominator is
230. So the whole disclosure lives in the numerator being the same. I read the falling figure off the
live DOM at all eight stops:

```
stop 0  100 %–100 %     stop 4   55 %–100 %
stop 1   79 %–100 %     stop 5   44 %–100 %
stop 2   69 %–100 %     stop 6   35 %–100 %
stop 3   65 %–100 %     stop 7   33 %–100 %
```

**Eight states, and not one of them prints `11`. Not one prints a denominator either.** The falling
figure speaks in percent; the standing figure speaks in ships. There is nothing on the face by which
an eye can join them — nothing except a sentence that *tells* the reader they are joined:
`— the list of 4 AUG named eleven ships out of the 230 disappearances it says it examined. No stop
moves this figure.` That sentence is set at **11.52 px in the head's dimmest ink**, and it is the
same species of sentence, doing the same job, as the block §3 of my session-85 memo convicted. The
block was 257 px tall and stood 434–691; the note is 50 px tall and stands 263–313. **It has been
made smaller, moved into the frame, and left inert.** Prose beside a run is annotation; prose *inside
the frame* beside a run is annotation with a better address.

**The dispatch's question, answered plainly: does a stranger who watches the run see the relation
between the two figures without being told it? No.** What a stranger sees at 14.1 s is a bold black
number falling from `100 %` to `79 %`, and four lines below it a grey `11 of 230` that does not
change. The only reading available without the note is *"one number moves, another doesn't"* — which
is true, and is not the finding. Which number is the honest denominator is carried entirely by words.

**Judged at stop 0 and at stop 7, as ordered.** At stop 0 the frame reads `100 %–100 %` over
`11 of 230`. That is the moment the disclosure is largest — 11 of 11 against 11 of 230 — and the
moment it is most completely invisible, because `100 %` and `11 of 230` have no digit in common. At
stop 7 it reads `33 %–100 %` over `11 of 230`, and the two are as unrelated to the eye as they were
at second zero. **The part of the frame that carries the disclosure is the part the run cannot
reach.** Two things in one frame, one alive and one dead, is not a relation.

**One cost the build accepted without measuring it, and it is mine to name.** The frame now holds
**three numerals, two of which cannot move**: the fixed end `–100 %` (dim, at the *full* display size
of 46.4 px) and the standing figure `11 of 230` (dim, at 24 px — 52 % of it). The CSS argues the
half-size deliberately, *"because the one thing it must never do is compete with the number the run
is about."* The reasoning is sound and the consequence is not: dim ink now means two different
things in one block — at full size, *the other end of this same band*; at half size, *a different
fraction with a different denominator*. A stranger has no key to that. The `cannot move` mark, which
was this head's cleanest invention, has been asked to carry a second meaning and has not been given
a second sign.

**RULING ON CHANGE 1.** The prescription was built exactly as written and the prescription was
insufficient — that is my error, and it is stated as mine. Placement was never the problem; **units
were.** The second figure does not need to move again. The disclosure stages itself the moment the
two figures speak the same language: the falling figure must print its own fraction, not only its
percentage, so that the run shows `11 of 11 → 11 of 33` while `11 of 230` stands underneath. Then
the numerator repeats down the column, the denominators diverge, the run does the arguing, and the
11.52 px sentence can go. **Until it speaks in ships, the second figure is a caption in a good seat.**

---

## 2 · THE FORCED CHOICE — and the finding is that not one of the three doors closes it

**Driven.** `tools/frame.mjs` on the frozen object; then the same span re-taken by my own script with
each candidate part **removed from the DOM, the JS height reservation cleared, and the maximum taken
over all eight stops** — because `.sd-arrive-headline` has its `min-height` set at load from the
tallest stop, and a naive `display:none` leaves that reservation standing. *My first pass did exactly
that and reported that cutting the standing figure recovers 0 px. It was wrong, I caught it against
the source, and every number below is from the corrected pass.*

`tools/frame.mjs` on the frozen object:

```
phone 390×844 — figure-top to controls-bottom: 951 px of 844 — OVER by 107
    179 px  the frame: both figures and their clauses
     83 px  what the ends of the figure can do
     30 px  the day's own heading
    112 px  the names the day itself printed
     59 px  the hole's heading
    250 px  the names only later lists gave
     75 px  the caveat on the names
    116 px  the controls and the run's line
     47 px  the space between them
wide 1400×900 — 554 px of 900 — HOLDS
```

**The committed page, as a control — and an instrument fault found in taking it.** `frame.mjs`
documents `--ref=HEAD` in its own header comment (line 13) as *"the committed page, via a temp
copy."* **The flag is not implemented.** The string `ref` occurs nowhere in the file except that
comment line; `--ref=HEAD` is silently ignored and the tool measures the working tree. I ran it and
it returned **951 px — the object under test, reported as the control.** I took the control properly
instead, with `git show HEAD:… > tmp/index.html` (sha `85eead78…`) and `--dir`:

| part, 390×844 | committed | tonight | Δ |
|---|---|---|---|
| the frame: both figures and their clauses | 87 | **179** | **+92** |
| what the ends of the figure can do (`constant`) | 167 | **83** | **−84** |
| the day's own heading | 30 | 30 | 0 |
| the eleven names | 112 | 112 | 0 |
| the hole's heading | 59 | 59 | 0 |
| the names only later lists gave | 250 | 250 | 0 |
| the caveat | 75 | 75 | 0 |
| the controls and the run's line | 116 | 116 | 0 |
| **the space between them** | 198 | **47** | **−151** |
| **span** | **1,094** | **951** | **−143** |

**Read that table before ruling on anything.** The standing figure cost **+92 px**; the constant's
thirty-two words paid **−84 px** back. **The two head changes of tonight net +8 px.** The entire
143 px the phone frame gained is the three paragraphs leaving the spine — the −151 px in *the space
between them*. Whatever else is argued tonight, the frame did not move because of the figures.

**THE HONEST MENU.** Each candidate removed, reservation cleared, max over eight stops:

| cut | span | result |
|---|---|---|
| **(a) the standing figure row** — the thing built tonight | **859** | **OVER by 15** |
| (a′) its note only, numeral kept | 881 | OVER by 37 |
| **(b) the `constant` line** | **864** | **OVER by 20** |
| **(c) the caveat on the names** | **868** | **OVER by 24** |
| (a)+(b) | 771 | fits, 73 spare |
| (b)+(c) | 781 | fits, 63 spare |
| (a′)+(b) | 794 | fits, 50 spare |
| cut the eleven names the day itself printed | 796 | fits, 48 spare |
| **(d) controls moved up under the frame** | **303** | **fits, 541 spare** |

**The forced choice as posed cannot be won, and that is the ruling.** It offers three doors —
(a) the standing figure, (b) the constant, (c) some of the material — and **all three are short:
by 15 px, 20 px and 24 px.** Taking any one of them alone destroys a load-bearing element and still
leaves `frame.mjs` red. Had the house taken door (a) on the strength of the dispatch, it would have
deleted my own prescription, the only thing built tonight, and bought a page still 15 px over. **The
premise that one of these three closes the phone frame is false, and it is false by measurement, not
by taste.**

The pairs that do close it close it by 48–73 px. That is the whole margin, and this head has grown in
four of the last five sessions; 63 px is one added clause. **A repair with 63 px of headroom is a
repair that will be owed again inside two sessions.** And the cheapest pair, (a)+(b) at 771, pays for
73 px with the second figure *and* the line that marks what the figure's ends can do — the two most
argued elements on the face. That price is absurd and I will not order it.

**I RULE FOR (d), THE FOURTH THING, AT PHONE WIDTHS ONLY.** The controls move directly under the
frame, the instrument becomes one block, and the material fills below it. Measured, at 390×844,
with the controls reparented under `.sd-arrive-headline`:

```
figure          268–298      controls        455–571     (span 303, 541 px spare)
constant        575–658      the eleven      701–812
hole's heading  821–880      the hole        885–1135    caveat 1144–1219
```

**What it costs, stated exactly, because the dispatch requires it.**

1. **The hole leaves the first screen entirely.** Today the reserved space stands 761–1011, so 83 px
   of it is visible above the 844 fold at scroll 0. Under (d) it stands 885–1135 and **none of it
   is.** The reader must scroll 291 px to see the thing the run fills. That is the real price, it is
   paid in the work's one comparison, and I do not pretend it is small.
2. **The buttons interrupt the sentence.** Today the eye runs figure → standing figure → constant →
   the eleven names → the hole. Under (d) it runs figure → *buttons* → constant → the eleven names →
   the hole. The instrument is spliced into the middle of the argument.
3. **It buys nothing at 1400 and must not be applied there.** The desktop span is 554 of 900 and the
   whole composition — figure, both figures' clauses, constant, eleven names, hole, caveat, buttons,
   live line, caption — already stands on one screen. Moving the controls up at desktop widths would
   break a whole composition to solve a problem that does not exist there. **(d) is a breakpoint, not
   a redesign.** If the house will not accept a width-conditional order, then it must take (b)+(c),
   and it cannot take (c) as it stands — see §5.

Against those three costs: 541 px of headroom instead of 63, no sentence deleted, and the longest
walk on the page falls from 375 px (fold to controls-bottom, today) to 291 px (fold to hole-bottom).
**(d) is the only option on the menu that survives the next paragraph this head writes.**

---

## 3 · THE THREE PARAGRAPHS BELOW THE CONTROLS — findable, and duplicated

**Driven.** Full-page geometry and computed type at 1400×900 and 390×844, stop 7; text of every
paragraph read off the live DOM.

**Is the finding still findable? Yes, and it is correctly placed as prose.** Below the controls the
reader meets, in order: the caption (725–819), the heading `WHAT THE LIST OF 4 AUG WAS THE TOP OF`
(824–839), the four aggregates (843–892), and then the disclosure itself at 898–954 —
*"The instrument says so itself, in its method sheet: 'The index counts all examined; the case and
list show named vessels.' The share this page publishes is a share of what those lists print, not of
what they count."* A reader who scrolls past the instrument cannot miss it: it is directly under a
heading that announces it. **And the dangling pointer is repaired** — session 85 caught this sentence
saying *"the figure above"* from 740 px below; it now says *"The share this page publishes"*, which
is true from anywhere on the page. That string was the one change neither voice had seen. It holds.

**But the distance was named as a cost in session 85 and it has not been paid.** The disclosure
sentence stands **735 px below the figure at 1400×900** (163 → 898) and **~1,220 px below it at
390×844**. Session 85 measured 740 px and called it the cost of my own prescription. It is 735 px.
**The cost was named, priced and carried.** That is not a new charge; it is the same charge, and §1
is why it will not go away by moving prose again.

**IS ANYTHING DUPLICATED ACROSS THE TWO PLACES? YES — and I apply session 85's own standard, which
cut twenty identical words 466 px apart.**

| where | node | type | text |
|---|---|---|---|
| above, y 255 | `#sd-arrive-standing-fig` | 24 px, **dim** | `11 of 230` |
| above, y 263 | `#sd-arrive-standing-note` | 11.52 px, **dim** | *"…named eleven ships out of the 230 **disappearances it says it examined**."* |
| below, y 843 | `#sd-arrive-cut-figs` | **16.8 px, full black** | *"**11** names printed · **230 disappearances examined**, 82 of them dark inside national waters · 5,641 events in the window"* |
| below, y 1073 | `#sd-arrive-cut-kept` | 12.48 px, black | *"…prints six to eleven names of the 189 to 250 **disappearances it says it examined**."* |

- **Both figures stand twice**: `11` and `230`, at y 255 and y 843 — **588 px apart at 1400, 1,060 px
  apart at 390.**
- **Five identical words stand twice**: *"disappearances it says it examined"*, at y 263 and y 1073 —
  **810 px apart at 1400.**

And the duplication runs the wrong way. **The lower copy is set larger and darker than the upper
one**: 16.8 px in full black against a 24 px dim numeral over an 11.52 px dim note. The page states
its finding twice and gives the *stronger* typographic voice to the copy that is 680 px away from the
figure it is about. That is the exact defect session 85 cut a string for, reproduced across the
controls instead of across a paragraph.

**THE CUT I ORDER.** From `#sd-arrive-cut-figs`, delete

```
11 names printed · 230 disappearances examined,
```

and repoint the survivor at the numeral above it, which now carries those two figures on the face.
What remains — *82 of them dark inside national waters · 5,641 events in the window* — is the only
content in that line the standing figure does not already print, and it is the content that earns the
heading above it. Nothing is lost from the record; two figures stop being published twice at two
different weights; and the numeral above becomes the page's single statement of `11 of 230`, which
is what change 1 was built to make it.

*Optional second cut, not ordered:* `#sd-arrive-cut-kept`'s clause *"of the 189 to 250 disappearances
it says it examined"* is the third statement of the same relation. It is defensible, because it is
the only one that gives the range across all eight lists rather than one list's figure. I leave it.

---

## 4 · THE CONSTANT'S THIRTY-TWO WORDS — better, not thinner

**Driven.** Text of `#sd-arrive-constant` read at all eight stops on the frozen object, and against
`git show HEAD:` for the committed wording.

Committed (167 px at 390): *"…it holds at 100 % while no more of these ships are CERTAINLY dark on
this day than the eleven the day itself named — **a list gives a return only to the nearest week, so
thirty-one of the thirty-three are merely possible today and two are certain** — and it falls as soon
as one more than those eleven is certain. Only the lower end has moved so far…"*

Tonight (83 px): *"Neither end of this figure can rise. The upper end holds at 100 % until more of
these ships are certainly dark on this day than the eleven the day itself named; only the lower end
has moved so far, and the next list can lower it again."*

**RULING: the head reads better, and the cut was more than economy — it removed a fuse.** The words
deleted are the *"nearest week / certain / merely possible"* clause, and the `hedge` line says the
same thing 278 px below (317 → 595 at 1400). **Banked failure 42 was created by exactly this pair**:
one fact carried by two sentences, one of which branched and one of which did not, so a sentence
correct for months published *"all thirty-three are merely possible"* on the first night two were
not. Deleting the duplicate deletes the second place that fact can go stale. That is the right
reason for the cut, it is a better reason than the word count, and the house should record it as the
reason.

**One residue, and it is small.** *"certainly dark"* is now a term of art used at y 317 and defined
at y 595 — 278 px before its definition — and the defining sentence is set blacker and larger
(12.48 px, `rgb(17,17,17)`) than the sentence that needs it (11.52 px, dim). The line that depends
looks less important than the line depended on. Not a cut; a note for whoever next touches that
pair.

---

## 5 · A SENTENCE THAT IS FALSE AGAINST ITS OWN SCREEN AT SEVEN OF EIGHT STOPS

This is the largest thing I found tonight and it is not one of the three changes I was sent to judge.

**Driven.** `#sd-arrive-hedge` read at all eight stops; the contents of `#sd-arrive-names-since` read
at stops 0, 1, 6 and 7; `MutationObserver` on the hedge across a full free run; a screenshot at
1400×900, scroll 0, stop 0, looked at.

`#sd-arrive-hedge` is **byte-identical at all eight stops** and mutates **0 times** across a full
run:

> *"A list gives a ship's return only to the nearest week, so **two of these names are certainly dark
> on this day** and the rest are possible."*

The chips in the space it points at, counted at every stop: **0 · 3 · 5 · 6 · 9 · 14 · 20 · 22.** The
two certain names are `PANOFI FORE RUNNER · GHA` and `HEATHER LYNN · USA`, and I read them off the
live DOM: they are **absent at stop 6 (20 chips) and present only at stop 7.**

**So at seven of the eight stops the sentence asserts a fact about two names that are not on the
screen — and at stop 0 it asserts it over an empty box.** At stop 0 the heading 106 px above it reads
*"NAMED ONLY BY LATER LISTS — **nothing yet.** The space below is the part of this day that nobody
could have had on it."* Directly under the empty space, in black body type, on the **first screen at
1400×900 at scroll 0**, at `y 595–633`, stands *"two of these names are certainly dark on this day."*
I have the screenshot. **Nothing yet, and two of them are certainly dark, three lines apart, on
load.**

**This is banked failure 42's class exactly, one session after it was banked, in the line that pass
repaired.** 42 reads: *"a right sentence with no branch under it… not a wrong figure, but a right
sentence with no branch under it."* Session 86 put both `constant` and `hedge` on the same value —
and that value is the **record's** live certain-count, not the **displayed stop's**. `hedge` is a
single string in the data, not a per-stop state; it can never branch on the run. **A branch on the
state of the record is not a branch on the state of the run**, and the run is what a stranger
watches.

**It is inherited, not tonight's.** I checked: the string is identical in `git show HEAD:` at
line 651 and in the working tree at line 681. It stands on the committed, live page. Tonight's
increment did not cause it and does not repair it.

**Two consequences, and I am ruling only on the first.** As staging: the caveat contradicts its own
heading at stop 0 and points at absent names at stops 1–6, so at seven of eight stops the run's
last line disagrees with the run. That is mine, and it is a defect of the run, not of a sentence.
**The tier and fact question — whether a page may publish, on load, a certainty about names it is
not showing — is not mine. It goes to the verifying voice, named here so that it cannot be lost the
way `HY928-21%-81% · null` was lost for four sessions.** And this is *also* why option (c) of the
forced choice cannot simply be taken: the caveat cannot be deleted for 24 px while it is the only
line carrying the *nearest-week* limit, which this record calls its weakest joint — it has to be
made to branch first.

---

## 6 · STILL OPEN, MEASURED TONIGHT AND NOT CLAIMED FIXED BY ANYONE

1. **(v), the reader who leaves during the first beat — unchanged and unrepaired.** First mutation of
   `#sd-arrive-count-falling` at **14,073 ms**, confirmed independently by `announce.mjs` over two
   runs: first figure rewrite at **14,184 / 14,171 ms**, last at **23,784 / 23,772 ms**. That log
   also reproduces the eight states of §1 exactly — `100 · 79 · 69 · 65 · 55 · 44 · 35 · 33` — by a
   second instrument. For fourteen seconds after load nothing on
   the page moves. At 390×844 scroll 0 during those fourteen seconds the reader has the figure
   (268–447), the constant (451–534), the eleven names (576–688), the hole's heading (697–756) and
   83 px of an empty box. The spoken line still calls the pause *"as long as the paragraph under the
   title takes to read"* — a referent this head has changed three times since it was written.
2. **The 37-word heading — still 37 words, and now measured per stop.** `#sd-arrive-head-since` runs
   **23 · 37 · 37 · 38 · 37 · 37 · 37 · 37** words across the eight stops. It is 37 or more at seven
   of eight. Unrepaired.
3. **`tools/fold.mjs`: 64 failures**, exactly session 86's count. Every one of the 64 is the same
   shape — `the figure … ✗OFF` at scroll ≥ 176 px at 390, at every stop. **Not one failure is a
   control or a live line off the viewport.** The instrument is red for one reason and `frame.mjs`
   states that reason in a single number.
4. **`tools/frame.mjs` advertises a control it cannot take** (§2): `--ref=HEAD` is documented in the
   file's own header and unimplemented, and returns the working tree silently. An instrument built
   to end the defect *"a measurement whose instrument is unstated"* ships with a flag that reports
   the object under test as its own control. It is a two-line fix and it should be made before the
   next session quotes a `--ref` number.
5. **`gaps.mjs` PASS. `announce.mjs` runs clean**, three announcements, correct interrupt behaviour
   on a mid-run press, correct resting text under reduced motion.
6. `HY928-21%-81% · —` is still the fifteenth chip in the space; the `null` is gone, the name is
   upstream's, and session 86 handled it correctly. Named here only to confirm I saw it on the face.

---

## VERDICT

**RETURNS FOR RESTAGING — and SHIP TONIGHT WITH THE VERDICT STANDING OPEN.**

**The restaging verdict does not lift, and the weakness is named precisely: the two figures in the
frame do not share a term, so the second one is a caption in a good seat.** My prescription was built
to the letter and the letter was not enough. Placement was never the fault; units are. Until the
falling figure prints `11 of 11 → 11 of 33` beside the standing `11 of 230`, the run does not argue
the disclosure and the 11.52 px sentence is still doing the work. That is the whole of what is owed
on (A)'s staging, it is smaller than what was built tonight, and it is checkable in one look.

**And it ships, for the same reason it shipped in 85 and for one more.** Every number moved the right
way: the phone span 1,094 → 951, the desktop span 650 → 554, `fold.mjs` level at 64, no sentence
deleted from the record, the disclosure's dangling pointer repaired, and the constant's cut removed a
banked-failure fuse rather than merely words. Nothing regressed. Against that, the one sentence on
this face I would block for — the caveat of §5 — is **inherited and already live**, and holding
tonight's increment would not take it off the public page for a single night. **A restaging verdict
is a claim about the staging; it is not a reason to hold a page that is better than the one
published.** Ship it, carry the verdict, and build the fraction.

**The three cuts I order, and nothing else:**

1. **Delete `11 names printed · 230 disappearances examined,` from `#sd-arrive-cut-figs`** and
   repoint the survivor. Two figures published twice, 588 px apart at 1400, the lower copy in the
   heavier face. Session 85's standard, applied to this house.
2. **Move the controls under the frame at phone widths only.** The only door that closes the phone
   frame without deleting a load-bearing line, and the only one with more than 73 px of margin.
   Costs named in §2: the hole leaves the first screen, the buttons split the argument, and it must
   not be applied at 1400.
3. **Do not take door (a).** Cutting the standing figure recovers 92 px, leaves the span at 859
   against 844, and deletes the one thing built tonight. It is a cut that pays a price and does not
   buy the goods.

---

## WHAT I DID NOT MEASURE

Named plainly, so the next session knows the edges of this memo rather than trusting it whole.

1. **Screenshot-difference of the run.** Sessions 84 and 85 counted changed pixels per frame to show
   where the run's motion actually lands (the 62 % / 0 % desktop-versus-phone split). **I did not run
   it tonight.** §1's charge rests on `MutationObserver` counts and on reading the eight states, not
   on a pixel diff. The diff would strengthen §1 and could not overturn it — 0 mutations is 0 pixels
   — but it is not in this memo and must not be cited from it.
2. **The severed-reader question.** I have not put the two figures in front of anyone. My claim that
   a stranger cannot join `33 %` to `11 of 230` is a measurement of the object (no shared term), not
   a reading of a reader. A panel could refute it and should be given the chance before the numeral
   is rebuilt.
3. **Option (d) at 1400×900.** I measured (d) only at 390. My ruling that it must not be applied at
   desktop widths is argued from the current desktop span (554 of 900, whole composition) and not
   from a built (d) at 1400.
4. **Dark scheme and `prefers-reduced-motion` interaction with the new frame.** Everything above was
   driven in `colorScheme: light`. The dim ink of the standing figure is `rgba(0,0,0,0.55)`; I did
   not check what the `cannot move` mark looks like against a dark ground, and §1's charge about two
   grades of dim would change if the dark palette flattens them.
5. **Sideways scroll.** `documentElement.scrollWidth` reads **390** at a 390 px viewport on the frozen
   object, so session 86's repair holds and I confirm it — but I did not re-walk the wide OBSERVED
   table for a horizontal-drag measurement the way session 85 did.
6. **The ending after the last stop.** I judged stop 0 and stop 7 as ordered and the arc between
   them, but I did not sit with what the page does *after* the run finishes — the resting state, the
   replay affordance, whether the ending lands or merely stops. That was §4 of my 85 memo and it is
   not re-measured here.
7. **Everything below `#sd-arrive-tier`.** The OBSERVED table, the legend, the restraint line and the
   README were outside the three changes I was sent to judge and I did not drive them.

---

**Hashes re-verified at the foot of this memo, after all measurement, by me:**

```
f43a481b59933f43806931c87c26cd8fbdf30f3ea87d735fae3da202a79b8eaa  projects/season1/still-dark/index.html
3a459aaa4a2f3f55d797bb18e4090cb468e4fcd665f60a9ed7ee63dd5359488f  projects/season1/still-dark/data.py
```

Unchanged from the head. The object did not move under me and I did not move it.

*Every position, type size, colour, word count, timing, mutation count and instrument exit in this
memo was taken by me on the running object during this session; the committed-page control was taken
from `git show HEAD:` rendered out of a second directory by the same script. Where a first pass was
wrong, the wrong number is gone and the corrected pass is named as such. Scripts are in this
session's scratchpad. Published verbatim beside the work.*

---

## RE-VERDICT ON THE CHANGED STATE

**Convened a second time, on the object as the cuts left it.** Hashes verified by me before I drove
anything:

```
a0fd3755219bbf96b236029d046f78bd3967634bb409ef6690c0662f9529b357  projects/season1/still-dark/index.html
a982bda19563acca5390e12b45b1a0fcde5cf9049b3da429afd87e78efb9cb13  projects/season1/still-dark/data.py
```

Both match the dispatch. **Nothing above this line has been touched** — the memo ships as written,
including the two places below where I find it wrong. I edited nothing in the work. Where I needed
last night's paint as a control I injected a stylesheet into a headless page and re-measured; the
files on disk were never opened for writing, and the hashes are re-verified at the foot.

All three cuts were taken. Two of the three costs I priced came in as priced; one did not; and there
is a third cost I never measured, which I name below as mine.

---

### R1 · CUT 1 — taken in the half that mattered, and my order was wrong about the other half

**Driven.** `#sd-arrive-cut-figs` and every text node in `.sd-arrive` read off the live DOM at
1400×900, stop 7, with position, computed size and computed colour on each; the same at 390×844.

The survivor, measured:

| | node | y at 1400 | type | ink |
|---|---|---|---|---|
| above | `#sd-arrive-standing-fig` | 255–279 | 24 px / 400 | `rgba(0,0,0,0.55)` |
| below | `#sd-arrive-cut-head` | 824–839 | 10.56 px / **700** | `rgba(0,0,0,0.55)` |
| below | `#sd-arrive-cut-figs` | **843–892** | 16.8 px / 400 | `rgb(17,17,17)` |

> *"Of those 230 examined, 82 were dark inside national waters · 5,641 events in the window"*

**Is the duplication I measured gone? Half of it, and the half that mattered.** My §3 charged that
*"both figures stand twice: `11` and `230`."* Walked again tonight, every occurrence in the head:

- **`11` no longer stands twice.** It is gone from `#sd-arrive-cut-figs` entirely. The numeral at
  y 255 is now the page's single statement of the numerator, which is what change 1 was built to
  make it. **Charge discharged.**
- **`230` still stands twice** — y 255 at 24 px in `rgba(0,0,0,0.55)`, y 843 at 16.8 px in
  `rgb(17,17,17)`. 588 px apart at 1400, 1,060 px at 390, and the lower copy is still the darker one.

**And on that second half my order was wrong, the build was right to refuse it, and the source says
why.** `data.py:830–835` argues that upstream's own sentence makes the 82 a subset of the *examined*
and not of the *window*, so that written without `230` in the line, *"82 of them"* reaches back past
the nearer number and asserts something upstream does not. That is correct. **`230` is the
denominator of `82`, it is load-bearing where it stands, and a cut that removed it would have bought
a tidier page with a wrong figure.** I ordered both figures out; the build kept the one that could
not go and deleted the one that could. It read the reason and printed it in the source. **The refusal
is upheld and the order is withdrawn.**

**Does the survivor still earn its heading? Yes — and better than what it replaced.** The heading
claims *"WHAT THE LIST OF 4 AUG WAS THE TOP OF"*, and the line under it now carries `230`, `82` and
`5,641`: three figures upstream published, of which two stand nowhere else on this face. Before the
cut the same line opened on `11 names printed`, which the block's own tier line
(`#sd-arrive-cut-tier`) has to disclaim as *"this house's own"* — a house count leading a line under
a heading about what the list published. Tonight the line is three SOURCED figures and the tier
line's disclaimer no longer has to cover its first clause. That is a gain I did not order and it
should be recorded as the build's.

**ONE NEW DEFECT, AND IT IS MINE.** The survivor opens *"Of those 230 examined…"*. **`those` is a
pointer with no antecedent in its own block.** The nearest `230` stands 588 px above at 1400 and
1,060 px above at 390, on the far side of the controls, the caption and a heading. This is the exact
class of fault session 85 struck as *"the figure above"* and that this same session repaired in
`#sd-arrive-cut-said` by replacing a pointer with a name — and my cut has installed a fresh pointer
in the line immediately above the repaired one. The build inherited the word from the shape of my
order; the order is mine and so is the word.

**Cut ordered: `Of those 230 examined` → `Of the 230 examined`.** One word. It keeps the subset
order the source argues for, keeps `82`'s denominator on the face, and stops the line pointing at
something a phone reader would have to scroll 1,060 px to find.

---

### R2 · CUT 2 — the phone staging, now that it exists

**Driven.** `tools/frame.mjs` on the object; then Chromium at 390×844, light, `reducedMotion:
reduce`, all eight stops through `#sd-arrive-ladder`, full-page geometry at every stop, viewport
screenshots at stop 0 scroll 0, stop 7 scroll 0 and stop 7 scroll 162, magnified and looked at; and
the same nine-position walk `fold.mjs` uses, run twice — once on the object, once with the `order`
rule injected out to recover last night's paint as a control.

`frame.mjs` confirmed by me: **311 px of 844 — HOLDS, at every stop. Desktop untouched at 554 of
900.** The rule is scoped at `max-width: 480px`, it is `order` on a flex column, and the DOM is
unmoved: `.sd-arrive-headline` `order: 0`, `.sd-arrive-controls` `order: 1`, everything else
`order: 2`. **Paint and not order, as ordered, and a screen reader still meets the caveat before the
controls.**

**My estimate against the built object, 390×844, stop 0:**

| | §2 estimate | built | Δ |
|---|---|---|---|
| the figure | 268–298 | 268–298 | 0 |
| the controls | 455–571 | 455–571 (ladder 455–500, run's line 508–571) | 0 |
| the constant | 575–658 | 575–658 | 0 |
| the eleven names | 701–812 | 701–812 | 0 |
| the hole's heading | 821–880 | 821–880 | 0 |
| **the hole** | **885–1135** | **885–1135** | **0** |
| the caveat | 1144–1219 | 1147–1222 | +3 |

**The estimate was right to within 3 px at every line**, so nothing below is a surprise of
arithmetic. What follows is what the arithmetic looks like when a person meets it.

**THE FIRST ENCOUNTER, 390×844, stop 0, scroll 0, looked at.** The eye runs: the title → the gloss →
the section's heading and its paragraph → **`100 %–100 %`** → the clause → `11 of 230` → the note →
**the eight buttons and `run it again`** → the run's line → the constant → the day's heading → all
eleven names the day printed → two of the three lines of the hole's heading, cut off at the fold.

**Cost 1 — the hole leaves the first screen. Confirmed exactly, and it reads WORSE in the object
than in my estimate**, for a reason the estimate could not see. The first screen does not merely lose
the reserved space; **it ends mid-sentence in the heading that announces it.** The last words a phone
reader sees on load are *"The space below is the part of this day that nobody"* — and there is no
space below. Before the cut, the same reader's screen ended on that heading whole plus 83 px of the
emptiness itself, so the shape of the hole was the last thing on the screen. That image is the one
thing this head exists to give, and the cut spends it. I wrote *"I do not pretend it is small"*; it
is larger than I wrote.

**Cost 2 — the buttons split the argument. Reads BETTER in the object than in my estimate, and I
withdraw the charge.** I wrote that the eye would run figure → *buttons* → constant, and called the
instrument *"spliced into the middle of the argument."* On the built page it is not a splice, because
the buttons do not arrive alone: the ladder (45 px) and the run's line (63 px) are one 116 px block
with its own voice, and the constant that follows — *"Neither end of this figure can rise… the next
list can lower it again"* — now reads as a statement about what the buttons just offered rather than
a claim floating in front of any means of testing it. Figure → instrument → what the instrument
cannot do → the material is a sound order. **I predicted a wound and the object has a joint.**

**AND A GAIN I DID NOT PRICE AT ALL, which is the largest thing on this side of the ledger.** At
`reducedMotion: reduce` — the state a machine reports, and the state my own §6 says a reader may
never leave — **nothing on this page moves.** The run's line says so in words:

> *"Your machine asks for no motion, so nothing runs: this is the day's own answer, and each button
> below holds a later state."*

On the committed page that sentence stands at **y 1298** and the buttons at **y 1245** — measured by
me, `git show HEAD:` rendered out of a second directory. **Both are below the phone's first screen and
below its second.** A reduced-motion phone reader met a static number, three blocks of prose, and no
evidence that this page was an instrument at all. Tonight the buttons and the sentence naming them
both stand at 455–571, above the fold, in the first encounter. **The cut did not only buy 640 px of
frame; it is the difference between a reader learning that this page runs and never learning it.**
That is worth more than 83 px of empty box, and it is why the cut was right.

**AND A THIRD COST I NEVER MEASURED. It is mine, and it is 23 px.** Three pairs matter on a phone,
and an 844 px screen holds two of them:

| the pair | last night | tonight |
|---|---|---|
| the figure and the buttons that drive it | 951 of 844 — **✗** | **311 — ✓** |
| the buttons and the space they fill | 387 — ✓ | 680 — ✓ |
| **the figure and the space it is about** | **743 — ✓** | **867 — ✗, over by 23** |

Figure-top is 268 in both. The hole's bottom was 1011 and is now 1135, because the 116 px instrument
and its gap moved above it. **Last night there was a 101 px band of scroll — 167 to 268 — at which a
phone reader could see the falling numeral whole and the whole reserved space at once. Tonight that
band is empty.** At scroll 268, where the numeral's top is exactly at the top of the screen, the space
shows 227 of its 250 px: it is short by the same 23. At scroll 291, where the space is whole, the
numeral row stands at −23 to 7 and is gone.

**That is the work's argument — a number falls while a space fills — and on a phone the two ends of
it can no longer be held in one frame.** `frame.mjs` cannot see this: it measures figure-top to
controls-bottom, which asks whether a reader can *reach* the instrument, not whether they can *watch*
it. I ordered a repair against the instrument's question and did not ask my own. **The cut closed the
frame the instrument is in and opened the frame the argument is in.**

**It is not fatal and the cut stands.** A reader who cannot press sees no fall at all, and the space
fills whether or not the numeral is on the screen: at stop 7, scroll 162 — screenshotted and looked
at — the numeral `33 %–100 %`, the standing figure, the eight buttons, the run's line, the constant,
the eleven names and 121 px of filled chips are all on one screen, which is enough to see that a
press does two things. And 23 px is a debt one line-height pays. **Cut ordered below.**

---

### R3 · THE FOLD TRADE — RULED

**Driven.** `tools/fold.mjs` on the object, full log kept. Then my own script on the same nine
positions the tool walks (`#sd-arrive`'s scroll range in eighths: 0, 162, 323, 485, 646, 808, 969,
1131, 1292), run twice at 390×844 — once as built, once with the `order` rule injected out.

| | controls off viewport | run's line off | total |
|---|---|---|---|
| last night's paint (order removed) | 32 | 32 | **64** |
| tonight, as built | **48** | **40** | **88** |

**The house's breakdown reproduces exactly on a second instrument.** 0 chips covered in both.

**And my §2 and §6 are wrong about what those failures are, and the error is mine, not the
instrument's.** `fold.mjs:50` declares the figure `must: false`, and line 124 increments `failures`
only when `s.must && !s.inside`. The figure is marked `✗OFF` **96 times** in tonight's log and counts
**zero** times. I read the marks in the log and reported them as the failures. The count was right;
the account was not. §6.3's *"Not one failure is a control or a live line off the viewport"* is the
precise inversion of the truth: **every failure is a control or a live line off the viewport, and
always was.** The correction stands in the work's README and not in the memo above, which ships as
written.

**The trade, stated as a trade.** The cut turns `frame.mjs` from 951-of-844 red to 311-of-844 green
at every stop, and adds 24 failures to `fold.mjs`. All 24 are one shape: the controls now leave the
top of an 844 px viewport at scroll 500 instead of scroll 1148, so a reader who scrolls to the prose
loses them 648 px earlier. At stop 0 the controls are inside the viewport at **three of nine probes
tonight** (0, 162, 323) against **seven of nine last night** (322 through 1128).

**RULING: THE TRADE IS RIGHT, AND I TAKE IT.** Three reasons, in order of weight.

1. **The two instruments are not weighing the same reader.** `frame.mjs` asks whether the instrument
   can be found. `fold.mjs` asks whether it can be found *again, from anywhere*. A reader who never
   learns the page runs never asks the second question — and on a reduced-motion phone, last night's
   paint gave them no way to learn it, because the buttons and the only sentence that names them both
   stood below two screens of scroll. **A control you cannot reach from the bottom of the page is a
   lesser fault than a control you never meet at all.**
2. **The 24 new failures are all deep in the prose, and the prose is not the run.** Every one of them
   falls at scroll ≥ 485, positions at which the reserved space is itself leaving the top of the
   screen. The reader they describe is not watching the run; they are reading the paragraphs below
   it, having finished with the instrument. And the first button in the ladder they scroll back to is
   `run it again`.
3. **`fold.mjs`'s own header says it can be passed only by a pinned bar, and this house has already
   withdrawn a pinned bar** for painting over ten of nineteen name chips (session 84; the tool's
   comment at lines 26–33 records it). An instrument whose only clean pass is a repair this house has
   banked as a failure produces a report, not a gate. It stays red, it stays printed — *"an instrument
   is not retired for being hard to pass"* is right and I am not asking for it to be — **and it does
   not veto a staging repair.**

**What the trade does not license.** It is not a finding that 88 is fine. Two cheap joinery repairs
would lower it without unpicking the cut — `run it again` made the target of a skip-link from the
prose, or a second text-only anchor to the ladder under the caption. Neither is staging. Neither is
ordered tonight, and neither should be traded for the frame.

---

### R4 · THE CAVEAT — a per-stop string, and it is the best-staged thing on this face

**Driven.** `#sd-arrive-hedge` read at all eight stops at 1400×900 and at 390×844, with height and
absolute position at each; and a `MutationObserver` on it across a full 40 s free run with motion on.

**Text, measured, eight stops:** *"A list gives a ship's return only to the nearest week, so **not one
of these names is certainly dark on this day**"* at stops 0–6, and *"…so **two of these names are
certainly dark on this day and the rest are possible**"* at stop 7. **The sentence I found false at
seven of eight stops is true at eight of eight.**

**Height and position, measured:**

- 1400×900: **37 px at every one of the eight stops.**
- 390×844: **75 px at every one of the eight stops, top edge at y 1147, unmoved.**
- Across a 40 s free run with motion on: **7 mutations**, first at **13,376 ms**, last at
  **22,976 ms**, and `min height 37 · max height 37` — **not one pixel of reflow.** Nothing under it
  moves when it changes.

**RULING: IT READS AS PART OF THE RUN.** A wobble is a block that changes size, changes position, or
changes out of time with everything else. This one does none of the three. It changes on the same
press as the chips it is about; it changes at the same seven moments and inside the same window as
the numeral (13.4 s to 23.0 s, against the figure's 14.1 s to 23.7 s); and it occupies the same
reserved 75 px before and after. **A sentence that is answerable to the screen and costs the page no
movement to be answerable is not a wobble under the run. It is the run, speaking.**

**And it does the thing §1 said the frame does not do.** The two numerals in the head share no
visible term; **the caveat and the space above it now do.** At stop 6 the space holds 20 names and
the line says *not one* is certain. At stop 7 it holds 22 and the line says *two* are. A reader who
watches that press sees a count in a sentence move with a count on the screen — which is exactly the
mechanism §1 charged the frame with lacking, built three blocks lower, in words instead of numerals,
as a by-product of repairing something else. **I record it as a credit to the repair and as evidence
for §1's prescription rather than against it: the mechanism works, so build it in the numeral too.**

**One reservation, small, not a cut.** At stops 0–6 the line reads *"not one of **these names** is
certainly dark on this day"* over a space that at stop 0 holds no names at all. It is no longer
false, but at stop 0 it has no referent. `heading_since` already branches on the empty case in words
(*"nothing yet"*); the caveat could too. Noted for whoever next touches that pair.

---

### R5 · THE EIGHT STATES — my §1 is right, and the dispatch's account of my §1 is not

The dispatch reports that §1 prints the middle four states as 44, 38, 36, 35. **It does not.**
`DRAMATURG-87.md:64–69` prints them in two columns of four: `100 · 79 · 69 · 65` and
`55 · 44 · 35 · 33`. Read again tonight off `#sd-arrive-count-falling` at all eight stops at
1400×900, one button at a time: **100, 79, 69, 65, 55, 44, 35, 33.** The same series, now confirmed
by a third instrument after `announce.mjs` in §6. **There is no discrepancy to resolve; `38` and `36`
appear nowhere in this memo.** Nothing turned on it either way — the charge is that no state prints
`11` and none prints a denominator, and none of these eight does.

While counting them I found a ninth button in `#sd-arrive-ladder`. It is not a ninth state: it is
`run it again`, class `sd-arrive-replay`, which `fold.mjs` correctly excludes from its stop walk and
which returns the face to stop 0. Named here only so a later session does not read nine states off a
button count.

---

### R6 · A SPATIAL WORD THAT POINTS THE WRONG WAY — inherited, and promoted by my own cut

Found tonight, recorded by neither pass. `#sd-arrive-state` reads *"…and each button **below** holds
a later state"* under reduced motion, and *"Any button **below** holds a state and stops the run"*
under motion. **The buttons are above it. At every width, on the committed page and on tonight's:**

| | ladder | the run's line |
|---|---|---|
| committed, 390×844 | 1245–1290 | 1298–1361 |
| committed, 1400×900 | 737–758 | 766–814 |
| tonight, 390×844 | **455–500** | **508–571** |
| tonight, 1400×900 | 641–661 | 669–717 |

It is the same class as *"the figure above"*, which session 85 struck and this session repaired in
`#sd-arrive-cut-said`. **It is inherited, it is not caused by cut 2, and I did not find it last
night.** What cut 2 did is **move it from y 1298 to y 508 — onto the phone's first screen**, so a
stranger's first encounter with this work now contains a sentence pointing the wrong way at the only
controls on the page. The fault is the house's; the promotion is mine.

---

## RE-VERDICT

**RETURNS FOR RESTAGING — and SHIP TONIGHT WITH THE VERDICT STANDING OPEN.**

**The verdict does not lift, and it does not lift for the reason it was given.** All three cuts were
taken and not one of them was aimed at §1's charge, because §1's charge was not a cut — it was a
build. The falling figure still prints `100 · 79 · 69 · 65 · 55 · 44 · 35 · 33` and the standing
figure still prints `11 of 230`, and **the two figures in the frame still share no visible term.**
Until the run shows `11 of 11 → 11 of 33` beside a standing `11 of 230`, the disclosure is carried by
an 11.52 px sentence and the second figure is a caption in a good seat. That is the whole of what is
still owed, and R4 is now evidence that it will work: the caveat proves that a string which moves
with the material reads as part of the run.

**And it ships again, for the same reason and one more.** The phone frame closed, 951 → 311 of 844,
green at every stop, on the fourth attempt at owed item (y). The desktop did not move. The sentence
I found false at seven of eight stops is true at eight of eight, with no reflow. One of two doubled
figures stopped being published twice, and the other was correctly refused because it is a
denominator. Nothing was deleted from the record. And a reduced-motion phone reader now meets the
instrument on the first screen instead of never. Against that: 24 more `fold.mjs` probes deep in the
prose, which I have ruled the right trade; 23 px on a frame nobody had measured before tonight; and
two one-word pointers. **Nothing on this face is worse than what is published, and several things are
better. Ship it, carry the verdict, and build the fraction.**

**Further cuts, and nothing else:**

1. **`Of those 230 examined` → `Of the 230 examined`** in `#sd-arrive-cut-figs`. My cut installed a
   pointer whose antecedent is 588 px above at 1400 and 1,060 px above at 390. The `230` itself stays
   — `82 of them` needs it, the build was right to keep it against my order, and that half of cut 1
   is withdrawn.
2. **`each button below` / `Any button below` → the buttons are above it**, at every width and on the
   committed page. Inherited fault; cut 2 promoted it to the phone's first screen. One word, or strike
   the pointer the way `said`'s was struck.
3. **Pay the 23 px.** Figure-top to hole-bottom is 867 of 844 at 390×844. Any 23 px between them —
   the run's line's 63, the 8 px gap under the frame, the day's heading's 30 — restores the only
   frame in which a phone reader can watch the number fall and the space fill at the same time. It is
   the work's argument and it is currently 23 px wider than a phone.

**Not ordered, and named so it is not read as an omission:** nothing about `fold.mjs`'s 88. It stays
red and it stays printed.

---

## WHAT I DID NOT RE-MEASURE

1. **Everything in `WHAT I DID NOT MEASURE` above, except where R1–R6 says otherwise.** The
   screenshot-difference of the run, the severed-reader question, option (d) at 1400×900 as a built
   thing, the dark scheme, the wide OBSERVED table's horizontal drag, the ending after the last stop,
   and everything below `#sd-arrive-tier` are all still unmeasured, by this pass as by the last.
2. **The desktop face, beyond confirming `frame.mjs` at 554 of 900 and reading the eight states,
   the caveat and the cut line off it.** I did not re-walk the 1400×900 composition after cut 1
   shortened `#sd-arrive-cut-figs` by 8 px; the blocks below it all move up by that much and I did
   not look at what that does to the caption's spacing.
3. **`announce.mjs` and `gaps.mjs`.** Not re-run tonight. §6.5's PASS is last night's, and the
   caveat's new per-stop branch is a string a screen reader will now hear change — whether
   `announce.mjs` announces it, or announces it twice, or interrupts the figure to do so, is
   unmeasured and is the first thing the next pass should drive.
4. **The 23 px of R2, as a built repair.** I measured the deficit, not any of the three ways of
   paying it. Which 23 px to take is a staging decision I have not made.
5. **`data.py` beyond the four strings this memo quotes.** I read `cut`, `hedge`, `heading_since` and
   `heading_then` and their comments. The rest of the 1,504 lines I did not open.
6. **The phone at any width between 390 and 480.** The `order` rule fires at `max-width: 480px` and I
   drove it only at 390. The frame at 480 is not measured, and a 480 px screen is 90 px wider than
   the one every number in R2 was taken on.
7. **Motion on, at 390.** R2's staging was judged under `reducedMotion: reduce`; the 40 s free run of
   R4 was driven at 1400. What the reordered phone head looks like while the run is actually running
   — whether the buttons above the material draw the eye off the chips filling below — I did not
   watch.

---

**Hashes re-verified at the foot of this re-verdict, after all measurement, by me:**

```
a0fd3755219bbf96b236029d046f78bd3967634bb409ef6690c0662f9529b357  projects/season1/still-dark/index.html
a982bda19563acca5390e12b45b1a0fcde5cf9049b3da429afd87e78efb9cb13  projects/season1/still-dark/data.py
```

Unchanged from the head of this section. The object did not move under me and I did not move it.

*Every position, type size, colour, height, mutation count, timing and instrument exit in this
re-verdict was taken by me on the running object during this pass; last night's paint was recovered
as a control by injecting a stylesheet into a headless page, and the committed page by
`git show HEAD:` rendered out of a second directory. Where this pass finds the memo above wrong —
§3's second figure, and §2 and §6.3's account of the 64 — the memo is left standing and the
correction is here. Scripts are in this session's scratchpad. Published verbatim beside the work.*
