# DRAMATURG — STILL DARK, premiere gate, session 91

**2026-08-13.** Convened on the frozen working tree, re-run because the object changed after the
pass of session 90.

**Object hash, taken by me before I looked at anything:**

```
05ea10f04d6455e36ca64df8e330bfd35b5c463e5bd886dcf419c65aaad3853f  projects/season1/still-dark/index.html
babd179e884bb9d590309c18a8b65bf785f54d75  (HEAD)
```

**I ran no writing instrument.** Not `render.mjs`, not `data.py --write`, not `capture.py` — banked
failure 50 is the reason and I treated it as law, not advice. I read the conductor's frozen renders
(`STATE-1.txt`, `render-900.png`, `render-1400.png`) and I drove the page myself in headless Chromium
from scripts held **outside this repository**, in the session scratchpad. The only file I have
written here is this memo. `git status` and the hash are re-taken at the foot and neither moved.

I did not read `KRITIKER-91.md`, which appeared in the tree while I was working.

---

## § WHAT A STRANGER MEETS

**A phone, 390 × 844, scroll 0, nothing touched.** The first screen holds 290 words — one tenth of
the 2,908 on the whole face — and in reading order: the date, one line of subtitle, a 55-word gloss,
then **100 %–100 %** at 30.4 px with the falling half in black and the fixed half in grey, the clause
*of 4 AUGUST 2026's darkness was knowable on the day itself, counting the lists up to 4 AUG*, then
**11 of 11 · 0 of them certainly dark**, then **11 of 230**, then a rail of nine buttons with a black
filled chip on `ON THE DAY`, then the run's own line, then the eleven names the day printed and the
first six of the names it did not.

Then nothing happens for fourteen seconds.

That is the first thing I got wrong, and I want it on the record because it is the thing I would have
cut if I had trusted my first pass. The state line promises *nine states over about twenty-seven
seconds*; a reader does that arithmetic and expects a step every three seconds. The constant in the
file is `first_dwell_ms: 14118`, and every subsequent step is `1600`. So state 1 is held **8.8 times
longer** than the eight that follow. At second three, at second eight, the page is a still photograph
that has just told you it is a film. My first note said *dead air, 53 % of the advertised run*.

It is not dead air. `arrive.first_dwell_note` — in the data island, invisible on the face — reads
*"56 words at 238 wpm (Brysbaert 2019, mean adult silent reading of non-fiction English)"*. The dwell
is the time it takes to read the frame at a cited rate. And the dwell is doing the work of the whole
piece: **you have to be allowed to believe 100 %–100 % before it is taken from you.** Fourteen
seconds of total, unqualified completeness is the trap, and it is set with a stopwatch. I withdraw
the note and I credit the craft.

**Then the second thing I missed, which is the reason this staging holds at all.** At 14.2 s the
number moves — and so does the rail. The black chip walks `ON THE DAY → +1 DAY → … → +8 DAYS`, one
button every 1.6 s, and at 390 that rail sits at y 433–470, inside the same screen as the figure.
I hit-tested every button at seven instants: exactly one is filled `rgb(17,17,17)` on white at every
moment of the run. So a visitor watching a percentage fall from 100 to 31 is simultaneously watching
a marker walk forward through eight days. **Time is made spatial in the same frame as the number it
explains.** That is why the 14-word clause under the figure, which is rewritten every 1.6 s and would
take 3.5 s to read at the page's own 238 wpm, does not need to be read: the rail already says where
you are. The clause is redundant during the run, not too fast for it.

**The turn.** `0 of them certainly dark` → `2` at 23.8 s → `4` at 25.4 s, in the last 1.6 s of the
run. On my measurement it stands at y 327.9–344.6 of an 844-px screen — in frame at scroll 0, as
session 90 built it to be. It is set at 11.52 px, weight 400: the **smallest live type in the head**,
beside a fraction at 17.6 px bold and a percentage at 30.4 px bold. My predecessor priced this
honestly (61 px of 2,206 changing at that instant) and declined to order weight or ink. I looked at
the same moment at 3× and I reach the same place by a different road: the turn is not loud, but the
digit is the only glyph in the head that has been *still* for six consecutive steps, and stillness
that breaks reads without being large. I do not order it changed either, and I note that two
dramaturgs arriving independently at *legible but quiet* is now the standing reading of this element.

**What a stranger holds after 27 seconds:** a number that fell by 69 points, a clock that walked eight
days, and one digit that went from nothing to four. That is the piece, and it happens above the fold
in under half a minute. **The terminal test passes, and it passes on the phone.**

**Where the first encounter breaks.** Below the fold, at y 3341 on the phone, is the best thing on
this page and the thing neither of my predecessors examined: the timeline. Every ship's dark span
drawn as a solid black bar with **hatched ends**, against a vertical rule at 4 AUG that every bar
crosses. The hatching *is* the seven-day return window — the single hardest idea in this work, the
one the prose explains four separate times, drawn so that it needs no explaining at all. Solid means
certain, hatched means the week nobody can resolve. That is the form embodying instead of
illustrating, and it is better than any sentence on the page.

It stands on a broken ruler. At 390 px, **eight of the nine gaps between the timeline's ten date
labels are negative** — `2 JUN` and `9 JUN` overprint by 14.9 px, and the axis renders as
`2 J9NJUN16 JUN23 JU30 JUN7 JUL14 JU21 JU28 JUL`. At 360 px it is eight collisions again, worst
17.6 px. At 414 px, eight. It clears to one at 480 and to zero at 700 and above — which is why the
committed renders at 900 and 1400 look clean and why no gate has caught it. `gaps.mjs` measures a
vessel's label against its own bar and passes; `frame.mjs` measures the head's height; `fold.mjs`
measures what leaves the viewport. **Nothing in this house looks at the axis, and the axis is the
only thing telling a phone reader what the hatching is measuring.**

**Reduced motion.** `announce.mjs` confirms the resting page opens at the day's own answer and says
so: *"Your machine asks for no motion, so nothing runs: this is the day's own answer, and each button
above holds a later state."* A reduced-motion visitor who presses nothing leaves holding
`100 %–100 %` — the exact impression the work exists to break. It is honestly labelled, the rail is
in the same screen, and the alternative (opening at 31 %) would destroy the arc. I name the risk and
order nothing.

**The arc and the ending.** Nine stops build rather than enumerate, because the falling half is black
and the held half is grey: the figure's own typography states, at every stop, that only one end can
move. The ending is `#sd-floor` — *"No number closes this. A method that counts a disappearance only
when the ship comes back cannot see the ships that never come back. Thirty-five is what this record
can place in 4 August 2026, not what was on the sea that day."* That is the right last thing and it
is one of the best sentences this house has printed.

**It is not the last thing.** Below it stand a source line and then, as the final element of the
page, a 179-character legal disclaimer that is **byte-identical** to one printed 5,313 px earlier.
A reader who walks the whole 7,855 px to earn that floor sentence is handed a duplicate of a
disclaimer instead.

**Tonight's change.** I drove `HEAD`'s file beside the tree's in one script: the 28th capture cost
**+17 px of page height and +10 words at both widths**, and `#sd-arrive` — the whole head — is
`84.5 – 2549.0` in both, identical to the tenth of a pixel. A work that can absorb a night's evidence
without moving a single element of its staging has been built correctly. That is the strongest thing
I can say about this object and it is not a thing I can say about most of what passes gates here.

---

## § CUTS

**1 · The timeline's tick labels below 700 px — six of the ten go.** `.sd-scale`, `index.html:1937`
region. Measured by me at seven widths: **8 collisions of 9 gaps at 360, 390 and 414 px; 1 at 480;
0 at 700 and 1400.** Ten labels need roughly 377 px of inked width and the scale is 337 px at 390 and
307 px at 360. The chart survives the cut — the bars, the hatching and the 4 AUG rule are untouched —
and four labels clear the floor with room. **The test a stranger re-takes: no negative gap between
adjacent tick labels at 360 px.** This is the sharpest cut of the three sessions I can see because it
is the only one that repairs the place where this work *shows* instead of *tells*.

**2 · `#sd-restraint` (`index.html:2404`), its write (`index.html:2516`), and `data.method.restraint`
(`index.html:744`) — strike all three.** The sentence *"'Intentional' is a machine estimate by Global
Fishing Watch — a probability, not proof; the instrument makes no claim of illegality against any
vessel or state, and neither do we"* is already printed in full by `#sd-arrive-restraint`
(`index.html:2338`, from `arrive.restraint`, `index.html:1106`) at y 2470 on the phone and y 1422 at
1400 — **179 characters, byte-identical, zero additional payload, the only pure duplicate on this
face.** It stands inside the section that uses the word *intentional*, which is where a restraint
belongs. The second printing stands 5,313 px later where nothing has claimed anything.

The comment at `index.html:2401` says *"one string now feeds the head and the foot, so the two cannot
drift apart."* That is not what the file does — there are two keys, at lines 744 and 1106, and the
code writes one to each element. The house solved the drift and kept the double printing; I am
cutting the printing.

**3 · Nothing may stand between `#sd-floor` (`index.html:2396`) and the bottom of the page.** With
cut 2 taken, the source line at `index.html:2399` still stands after the ending. A work whose last
sentence is *"not what was on the sea that day"* does not end on a URL. The source line is owed and
keeps its place on the face — above the floor, not after it. This is a cut of position, and it is the
whole repair of the ending.

**4 · The first sentence of `data.method.definition` (`index.html`, `method.definition`) — strike
it.** *"Going dark is a ship switching off its AIS transponder — the radio signal that puts it on the
public picture of the sea — so that it stops being tracked."* renders at y 2748 on the phone. The
first screen, at y 98, already said *"dark — the ship's AIS transponder switched off, so it stops
being tracked"* — the same clause, nearly the same words, 2,650 px earlier and in the frame every
visitor sees. 154 characters go; the survivor, *"The instrument this page reads counts only disabling
its own source classifies as high-confidence and intentional: at least 12 hours dark, at least 50
nautical miles offshore"*, is the only part that carries anything the face has not said, and it
stands alone.

### What I examined and did not cut, with the reason

- **`arrive.hedge` at y 1066.** Session 90 named the seven-day window as printed three times and
  refused the cut because the hedge is the key to the word *certainly* in the turn. I found a fourth
  printing (`fall.band`, y 6285) and it does not change the argument: the key must stand near the
  thing it unlocks. I do not re-litigate a predecessor's reasoned refusal without new evidence and I
  have none.
- **The proof lead.** Cut 2 of session 90 was paid — the sentence *"Every stop of this run is an
  instant of this record…"* is gone and the block is 266 → 183 characters — but the ordered survivor
  `"This stop is:"` (13 chars) was replaced by `"Run the line and this stop's share comes back:"`
  (45). The object re-inflated a cut it had been given. I let it stand, because the substitute tells
  a reader what the line *does* and the old hinge told them nothing, and because the block is now
  55.6 px of lead over 29.8 px of command rather than 70.5 over 30. Named so the next session does
  not find it as new.
- **Cut 1 of session 90** (`#sd-arrive-proof-as-of`) is discharged: the duplicated instant is gone
  from the face; the command still carries it.

---

## § WHAT THE STAGING EARNS

**The head is the best object this house has staged under v2, and the reason is one typographic
decision.** `100 %–100 %` sets the falling end at weight 700 in `rgb(17,17,17)` and the fixed end at
weight 400 in `rgba(0,0,0,0.55)`. The sentence *"neither end of this figure can rise"* is printed
1,000 px away and does not need to be: the type has already said which end is alive. The grey half
never moves through nine stops. That is the form doing the argument.

**The run is legible as a machine and not as an animation.** Nine states, a marker walking a rail,
a figure falling, a clause naming the day, and one digit that stays still through six steps and then
moves — all rewritten at the same millisecond, all inside one phone screen, all replayable by a
button that is also in that screen. Nothing decorates. There is no easing, no counter roll-up, no
transition; the numbers simply *are different*, which is what a re-derived state looks like.

**The machine's advantage is felt, then checked — in that order.** I took the page's own printed
command and ran it unedited from the repository root:

```
python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-10T22:41:12Z
   → 20 capture(s), SHARE 35%–100%  (11 of 0–31)          face at stop 6: 35 %–100 % · 11 of 31 · 0 certainly dark
python3 projects/season1/capture/day.py 2026-08-04
   → 28 capture(s), SHARE 31%–100%  (11 of 4–35)          face at stop 8: 31 %–100 % · 11 of 35 · 4 certainly dark
```

Both returned the face's figures **and the certain count that turns** — including tonight's 28th
capture, folded in hours ago. A stranger closes that loop in one paste. The claim on the face is not
asserted-then-demonstrated-in-a-shell-command; the shell command is the *second* encounter, offered
after the run has already made the point without it. That ordering is what keeps the proof block from
being an apparatus fetish, and it is correct.

**And the hatching.** Solid for what is certain, hatched for the week the instrument refuses to
resolve, drawn across a rule at 4 AUG that every bar crosses. It is the one place where the work's
hardest idea arrives through the eye. Cut 1 exists to protect it.

---

## § THE MEASUREMENT

Three numbers of my own, each re-takeable by a stranger with the frozen file and a headless browser.

**(a) The axis collision.** Load `index.html` at each viewport width, take the ten children of
`.sd-scale`, measure each label's inked extent with a `Range` over its text node, and count adjacent
pairs whose gap is negative:

| viewport | scale width | negative gaps (of 9) | worst overlap |
|---|---|---|---|
| 360 px | 307 px | **8** | 17.6 px |
| **390 px** | 337 px | **8** | **14.9 px** |
| 414 px | 361 px | **8** | 12.7 px |
| 480 px | 427 px | 1 | 6.7 px |
| 700 px | 647 px | 0 | — |
| 900 px | 847 px | 0 | — |
| 1400 px | 1347 px | 0 | — |

**Every phone width tested overprints eight of nine label pairs; every committed render is taken at a
width where the defect is invisible.**

**(b) The run's two speeds.** `arrive.first_dwell_ms = 14118` (`index.html:1109`); the interval is
`1600` (`index.html:2672`). Confirmed independently against `announce.mjs`, whose figure rewrites
land at 14195 · 15796 · 17396 · 18996 · 20596 · 22196 · 23796 · 25396 ms — seven intervals of
1600 ± 1 ms after one of 14,104 ms. **The first state is held 8.8× longer than each of the eight that
follow, and 52.4 % of a 26.9-second run is spent on it.** The state line's own words, *"nine states
over about twenty-seven seconds"*, invite 3.0 s per state. The distribution is deliberate and cited
(56 words at 238 wpm) and I judged it earned; the number is here so the next session that shortens it
knows what it is spending.

**(c) What the night cost.** `HEAD`'s `index.html` extracted to the scratchpad and driven beside the
tree's by one script in one run: **page height 7,838 → 7,855 px at 390 and 5,155 → 5,172 at 1400
(+17 px both), body text 2,898 → 2,908 words (+10), and `#sd-arrive` identical at `84.5 – 2549.0` at
390 and `77.6 – 1470.1` at 1400.** The 28th capture moved one table row and one word of a caption and
did not touch a single element of the staging.

Instruments run read-only and not trusted blindly: `tools/frame.mjs` (HOLDS both widths; hole 273 px
/ 24 of 24 chips against a floor of 268 / 22), `tools/fold.mjs` (108, published red — the standing
entry from session 90 that this instrument reports the height of the page still applies),
`gaps.mjs` (PASS), `announce.mjs` (1 live region, 3 spoken, 10 figure rewrites, reduced-motion rest
state correct). `git status` and the object hash are byte-identical before and after my pass.

---

# VERDICT: PASSES AS STAGED

**The weakness, in one sentence:** on the phone — the device this work is met on — the one place where
STILL DARK stops explaining and simply *shows*, the hatched return-window drawn against the 4 AUG
rule, stands on a time axis whose ten date labels overprint each other in eight of nine gaps, because
every committed render and every committed instrument in this house looks at the head, the fold or the
chips, and none of them has ever looked at the ruler.

It passes because the staging is not weak — it is strong and it is over-decorated by four sentences
and one broken ruler, and that is what a cut list is for. The head earns the premiere: a stranger on
a phone who touches nothing watches 100 % become 31 % while a marker walks eight days beneath it and
one still digit goes to four, all in the first screen, in under half a minute, and can then paste one
printed line into a terminal and get the same numbers back. I would not return that for restaging
over a ruler and a disclaimer printed twice. **Four cuts, ordered. None is structural, none touches
the head, and none may be booked against any frame measurement as a height gain — that is banked
failure 48 and I name it in advance as both my predecessors did.**

---

**Hash re-taken at the foot, after all measurement, by me:**

```
05ea10f04d6455e36ca64df8e330bfd35b5c463e5bd886dcf419c65aaad3853f  projects/season1/still-dark/index.html
babd179e884bb9d590309c18a8b65bf785f54d75  (HEAD)
```

**Unchanged from the head of this memo. `git status` is what I found it, plus this file. The object
did not move under me and I did not move it. No writing instrument was run.**

*Every position, width, ink, weight, timestamp, collision and page height in this memo was taken by
me tonight on the frozen object at 360 · 390 · 414 · 480 · 700 · 900 · 1400 px, in headless Chromium
driven from scripts held outside this repository. The comparison against last night is `HEAD`'s own
file extracted to the scratchpad and driven by the same script in the same run. The two terminal
outputs are the work's own printed commands, executed unedited from the repository root. Published
verbatim beside the work.*

---

**THE SENTENCE A SESSION SHOULD PRINT ABOUT THIS GATE:**

> The best thing on this page is the one thing no gate had looked at — a ship's dark span drawn solid
> where it is certain and hatched where the instrument refuses to resolve the week, every bar crossing
> a rule at 4 AUG — and on every phone width tested its date axis overprints itself in eight of nine
> gaps, invisible in both committed renders because both are taken at widths where it comes out clean.
