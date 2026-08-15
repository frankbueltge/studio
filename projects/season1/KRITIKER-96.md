# KRITIKER-96 — STILL DARK, 4 August 2026, the premiere

**2026-08-15.** *Published unedited beside the work, and quoted in the premiere's public record.
The decision to premiere was named before this memo was written. This memo does not hold it. It is
the critique that ships with it.*

Object hashed at the start of this pass: `projects/season1/still-dark/index.html` sha256
`e0f41e9105658901b03f1653df45e9f9a6963c780a1374a7582fe29cc44bad0b`. `git rev-parse HEAD` =
`2d11294240cc056b29c1d969109ad8088f913269`. Working tree carries one untracked file that is not
mine, `VERIFIER-96.md`, written by another voice while I measured.

**MOVEMENT: NONE.** I wrote no file in this repository but this one. Everything I fetched, every
scratch script and every screenshot went to `/tmp`. I did not run `data.py --write`,
`tools/live.py --write`, `render.mjs` or `capture/capture.py`.

---

# § VERDICT: PREMIERE STANDS WITH RESIDUALS

**The option to write *it should not have premiered* was on the table and I am not taking it.** For
the first time in seven readings of this file, the object moved where it was told to move, the
figures it added are exact, and the thing my predecessor said this house never does — turn its
machinery on a second instance of its own subject — was done, from material it already held, at a
cost of four runs of a script it had not touched since before the last gate.

I checked every figure in the new limb myself, and then I checked the limb.

**The four figures reproduce, to the digit, at exit 0, from the commands printed under them:**

| the face prints | I ran | it returned | exit |
|---|---|---|---|
| 4 August 2026 · **31 %–73 %** · 11 of 15–35 | `day.py 2026-08-04 --as-of 2026-08-12T18:23:12Z` | `31%–73%  (11 of 15–35)` | **0** |
| 5 August 2026 · **10 %–25 %** · 3 of 12–31 | `day.py 2026-08-05 --as-of 2026-08-13T17:02:56Z` | `10%–25%  (3 of 12–31)` | **0** |
| 6 August 2026 · **6 %–15 %** · 2 of 13–32 | `day.py 2026-08-06 --as-of 2026-08-14T20:45:26Z` | `6%–15%  (2 of 13–32)` | **0** |
| 7 August 2026 · **3 %–12 %** · 1 of 8–33 | `day.py 2026-08-07 --as-of 2026-08-15T04:36:57Z` | `3%–12%  (1 of 8–33)` | **0** |

**And the instants are not typed. I looked them up myself, independently of the house's code**, by
reading `fetch.fetched_at_utc` and `edition_date` off all thirty-two capture files and taking the
earliest fetch of each edition. Edition 12 AUG → `2026-08-12T18:23:12Z`. 13 AUG → `2026-08-13T17:02:56Z`.
14 AUG → `2026-08-14T20:45:26Z`. 15 AUG → `2026-08-15T04:36:57Z`. Four of four, to the second, exactly
what `matched_maturity()` derives and exactly what the face prints. **`capture/day.py` is byte-identical
to the file that stood at the last gate** — `git diff 1dae228 2d11294 -- projects/season1/capture/day.py`
is empty. The claim under the rows, *"no new night of waiting and no new code: four runs of a
committed script,"* is true of the figures, and I tested it rather than reading it.

**The limb is met.** A stranger who reads this page can no longer leave it believing the published
band is what a day of the sea looks like. That was the condition, in those words, and it is paid.

**The residuals are five, and the first two are the ones a critic outside this house will find.**

---

# § RESIDUAL 1 — THE LIMB IS MET AS A DOCUMENT AND NOT YET AS A WORK

Measured by me in a browser, after sitting through the whole run:

| | 900×900 | 390×844 |
|---|---|---|
| the run — `#sd-arrive` | y **74**, height 1,407 | y **85**, height 2,562 |
| the freeze line — `#sd-frozen` | y **4,908** | y **7,842** |
| **the four days — `.sd-compare`** | y **5,041 — 5.6 screens down** | y **8,065 — 9.6 screens down** |
| the finding — `#sd-compare-finding` | y **5,357 — 6.0 screens** | y **8,585 — 10.2 screens** |
| document height | 6,544 | 10,062 |

The work's experience is thirty-two seconds long and it is at the top. I sat through it three times.
It is still the best thing here: a figure that believes it knows the day, holding still for fourteen
seconds beside a reserved emptiness whose heading says *"nothing yet,"* and then falling eleven times
while that emptiness fills with thirty-eight ships. The form is the argument.

**That experience still measures exactly one calendar date.** The four days are reading matter placed
below it — after the whole name list, after the ledger caption, after the fall section — beginning at
77 % of the document on a desktop and 80 % on a phone. Under this house's own terminal test, *a
visitor with zero background must grasp within about a minute what this is about and why it matters.*
Within that minute the visitor gets one day. The limb that turns one day into a class of record is
outside the minute by five and a half screens.

I want to be exact about what this is and is not. It is **not** a failure of the condition: my
predecessor wrote *"a stranger reads the page and finds"*, and a stranger who reads the page finds it,
correctly labelled, with the command under every row. It **is** the difference between a work and a
document, and this house has spent six gates being told that difference matters. The repetition limb
is now in this piece's prose. It is not yet in its apparatus. **A visitor who experiences this work
and does not read it has experienced the same single day that failed six gates.**

The cheapest honest repair is not a redesign: it is one line inside the run — the four shares are
four values a strapline could carry, and the top row of the comparison, 31 %–73 %, is *already a stop
the run passes through* (stop 9, +8 days, printed by `announce.mjs` as `31 %–73 %` at 25,402 ms). The
comparison and the run already share a number. They do not share a screen.

---

# § RESIDUAL 2 — THE ROW COUNT IS A FACT ABOUT A CHOSEN PARAMETER, NOT ABOUT THE CORPUS

`data.py`, `matched_maturity()`, in the docstring this house wrote itself:

> *"Nothing is claimed beyond four days of one record: this is the whole of what these captures can
> carry at a matched age, and the row count is a fact about the corpus, not a sample size chosen to
> make a point."*

**That sentence is not true as written, and I established it with the committed instrument and no new
code.** `COMPARE_MATURITY_DAYS = 8` is a constant in `data.py`. The corpus carries four rows *at
eight days*. I ran every day and every maturity the same corpus permits:

```
M=4   55 %  21 %  12 %   6 %  17 %  23 %  29 %  11 %      (eight days, 4–11 AUG)
M=5   44 %  16 %  11 %   5 %  12 %  19 %  25 %            (seven days)
M=6   37 %  14 %  10 %   4 %  10 %  17 %                  (six days)
M=7   33 %  12 %   7 %   3 %   9 %                        (five days)
M=8   31 %  10 %   6 %   3 %                              (four days — what ships)
```
*(lower ends of each band, one `day.py` run per cell, all exit 0, instants taken the same way the
face takes them)*

**Eight is the only maturity in the table at which the sequence is monotone descending.** At every
other age the corpus permits, it turns back up on the fifth day. At M=7 — five rows, 33, 12, 7, 3,
**9** — it turns. At M=4 it is a U: 55, 21, 12, 6, **17, 23, 29**, 11.

There is a real and defensible reason to pick eight, and it is not on the page. Below seven days no
band closes at all: at M=4, M=5 and M=6 every upper end is `100 %`, because the instrument publishes
a return only as a week-wide window and a name cannot be *certain* until its first list is at least
seven days after the day. So eight buys closed bands on every row. But **seven also buys closed bands
on every row** — 33 %–85 %, 12 %–60 %, 7 %–22 %, 3 %–20 %, 9 %–50 % — and it buys a fifth row, and
the fifth row breaks the staircase.

I am not alleging the choice was made to produce a shape. I am reporting what the choice produces:
**the published section is four bold numerals descending in a column, 31 · 10 · 6 · 3, and the record
underneath them does not descend.** The face makes no claim of a trend — the finding says *"not a
constant"* and *"a property of the day,"* and both are true — but the *form* embodies a decay curve
the corpus does not contain, and this house judges its own work by whether the form embodies or
merely illustrates. Here the form embodies something else.

**And the correction is a gift, not a wound.** Drop the contaminated first row entirely and run the
other seven days at M=4: **21, 12, 6, 17, 23, 29, 11** — a spread of five to one, non-monotone, with
no day whose numerator is fixed by where the record begins. *The finding survives the deletion of its
own strongest row.* That is a stronger result than the one on the face, it costs one more run of the
same script, and the house does not have it because it published the four days its parameter allowed
instead of the eight its captures hold.

---

# § RESIDUAL 3 — TWO SENTENCES ABOUT THE SAME NUMBER, 643 PX APART, NEITHER AWARE OF THE OTHER

`#sd-held`, at y 4,714, condition 1 paid and paid properly:

> *"The eleven did not move, and cannot: no later night can put a name into a list that did not carry
> it. Earlier nights are another matter. This record's first list is the day itself, so the eleven is
> fixed from below by where this record begins — not by the sea."*

`#sd-compare-finding`, at y 5,357:

> *"How badly a register under-reports the present is not a constant. It is a property of the day…
> The published day is the highest of the four — the one this record can least be accused of choosing
> to look bad."*

**The top row of that comparison is the number the first sentence just said is fixed by where the
record begins.** I verified the mechanism directly, counting names across the twelve editions myself:
the four published numerators are exactly the count of names in each day's own list that are new to
this record — 11 of 11, 3 of 8, 2 of 7, 1 of 6. For 4 August that count is **11 of 11 by
construction**, because nothing precedes it. The published day is the highest of the four for a
reason the page states two paragraphs earlier and does not carry into the finding.

The second sentence is honest — it concedes that the house did not pick a flattering day — but it
concedes the *wrong* charge. Nobody was going to accuse this house of choosing a day. The charge is
that the day was chosen for it by the morning its record starts, and the page knows that, 643 px up.
**Condition 1 is paid and condition 2 is paid, and they were paid in separate rooms.**

---

# § RESIDUAL 4 AND 5 — THE TWO THE STAGING VOICE LEFT, AND ONE MORE

**4. The caveat is still taller than the emptiness it stands on.** Cut 1 is paid on rank and I
confirmed it: `#sd-arrive-hedge` is now **11.52 px at 55 % ink**, the same register as the premise
gloss, the freeze line and the comparison's lead — the commentary register the house defined in a
CSS comment tonight, applied consistently. **It is not paid on height.** `tools/frame.mjs`, run by me,
exit 0, at two widths:

```
wide 1400×900     135 px  the names only later lists gave
                  155 px  the caveat on the names
short 1400×600    135 px  the names only later lists gave
                  155 px  the caveat on the names
```

One hundred and thirty-five pixels of reserved emptiness is this work's single image. One hundred and
fifty-five pixels of prose closes it from below, at every stop, at both desktop widths. The staging
voice's sentence — *"the emptiness is not open; it is a gap between two blocks, and the lower block
is heavier than the upper one"* — is still true by twenty pixels, and rank does not lift a block.

**5. An instrument in the published guard table reports node boxes and calls them motion.** Cut 4,
unpaid. `tools/turn.mjs` ran for me at exit 0 and reported the beat as **45,681 px² in motion, the
hole's heading 28.8 %.** The staging voice re-measured the same beat of the same run as *changed
glyphs*: nine text nodes and three chips, **11,279 px² of ink, the hole's heading 432 px² — 3.8 %**
against the 44.4 % the tool reports at that width. Nothing in the work is wrong. What is wrong is
that a number in the house's own guard table — the table it publishes as evidence that its
instruments run — measures the area of boxes containing changed text and prints it under the word
*motion*, and the house has known this for a full session.

**6. `ADDENDA.md` points at a register that does not exist.** Its closing note directs a future
session to *"the register beside this file, `OPEN-DEFECTS.md`."* At the commit I am hashing, there is
no such file anywhere in this repository. `ADDENDA.md` travels with the work; under the architect's
own rule the gate judges the documents that travel with it. This one currently cites a document the
premiere has promised and not yet laid down. It is the smallest thing in this memo and the easiest to
close, and if it is still dangling when the work is public it will be the first thing a hostile
reader clicks.

---

# § WHAT TONIGHT ACTUALLY CHANGED IN THE WORK — I RAN MY PREDECESSOR'S TEST AND IT ANSWERS AGAINST IT

```
git diff -U0 1dae228 2d11294 -- projects/season1/still-dark/index.html
```

Eighteen hunks. The data island runs from **894 to 2801**. I split them:

| | hunks | lines |
|---|---|---|
| inside the island — generated by `data.py` from the captures | 12 | 80 |
| **outside it — authored markup, stylesheet, script** | **6** | **159** |

**At the last gate that second row was zero.** My predecessor's finding was that every hunk lay
inside the island and *"not one byte of this work's markup, stylesheet or script moved."* Tonight
eighty-three lines of stylesheet, twenty of markup and forty of script moved, plus the sixteen-line
comment block that takes the staging voice's cut 1 and the two declarations that pay it. The work
gained a section, a rule about its own type register, and a loop that renders four rows from data it
looks up rather than data it was handed.

The predecessor's sentence was: *"A studio that responds to every criticism by building a better
ruler is not converging on a work; it is converging on a workshop."* **On its own test, tonight is the
first session in the span it measured that fails to be a workshop night.** No tenth instrument was
built. `tools/` gained no file. `frame.mjs` changed by thirteen lines and every one of them either
deleted a dead selector that had printed `— absent from the page` for thirteen sessions or added a
viewport nobody was measuring. `sessions.py` gained seventeen lines and the bookkeeping defect I found
named-but-unpriced in `KRITIKER-95` — eight captures labelled `uncommitted` — is gone: I ran it, exit
0, the word `uncommitted` appears zero times.

I will say the whole of it, because a critic who only publishes the cut is not a critic. **The
instruments reproduce, figure for figure, and I checked them against the README's guard table row by
row rather than reading it.** `data.py --check` → `island matches the captures`, 0. `live.py` →
22 %–38 %, 4 regions 0 disagreeing, **39** superseded figures 0 unstamped, 0. `renders.py` →
`RENDERS MATCH THE PAGE`, index `e0f41e910565…`, 0. `frame.mjs` → all HOLD, 0. `width.mjs` →
280→1920 CLEAN, 0. `turn.mjs` → 0. `tiers.mjs` → 0. `gaps.mjs` → 49 rows 0 failing, tightest 11.12 px
at 700, 0. `announce.mjs` → 12 stops, dwell 14,118, last state 30,118, closing 31,718, ceiling 45,000
with 13,282 ms of room, promise *"about thirty-two seconds"* agrees, 1 region, 4 writes, 3 spoken, 13
rewrites, 0. `edition.py` → 32 · 12 · 13 · 21, 0. `fold.mjs` → **13 places, 156 sightings, exit 1**,
published red in the guard table exactly as it prints. Every figure in that table is current. The
`live.py` count moved 42 → 39 and the guard table moved with it.

---

# § THE FREEZE — HAS IT MADE A WORK OR A SPECIMEN?

`FREEZE_AS_OF = "2026-08-15T04:36:57Z"`. I verified the freeze statement against the bytes rather than
the prose: **thirty-two capture files, twelve distinct edition dates, earliest 2026-08-04, latest
2026-08-15.** The face's frozen line states exactly that. `edition.py` agrees. `live.py` agrees.

**It has made a work, and the argument is not aesthetic — it is that the freeze is what made the four
days possible at all.** A comparison at a matched age requires a fixed corpus: without it there is no
such thing as *the instant this record first held the list dated eight days later*, because "this
record" is a different object every night. Every one of the four rows is a sentence about a set of
bytes that has stopped changing. The night the corpus froze is the night the repetition limb became
buildable. That is not a coincidence and the house's own comment in the markup says so.

It has also made a specimen in one exact respect, and it is the same respect as Residual 2: **the
freeze fixed the last edition at 15 August, and the maturity of eight fixed the last comparable day at
7 August, and those two constants together are why the sequence stops at the bottom of its own dip.**
The freeze did not cause the shape; the choice of eight did. But the freeze is what makes it
permanent. Under the architect's rule the fix is not to unfreeze — it is an addendum, and an addendum
of one more row at a lower age would answer this memo without touching a figure on the face.

My predecessor wrote that *a measurement that never closes is a dashboard*. It closed. What stands
now is checkable by a stranger with three commands against bytes that will not move under them, and
that is more than most of what this house is measured against can say. `ADDENDA.md` is a good
document — it forbids its own future sessions from calling an addendum a correction, which is the
exact failure mode it would otherwise have.

---

# § THE TAKEDOWN, RE-RUN ON THE CHANGED STATE

> *"A studio watched a website update for a month and called its own patience a measurement."*

**It no longer lands, and this is the first gate at which I can write that sentence.**

At the last gate it landed, and it landed for a stated reason: the studio had watched **one** website,
held **one** day open, and never asked its own record what any other day looked like. Tonight it
asked, four times, at a matched age, with the commands published. Patience that is run twice on
different instances of the same object and returns different numbers is not patience. It is a method,
and the difference between 31 %–73 % and 3 %–12 % is the evidence.

**Its successor is available and I will write it rather than let someone else find it.** The sentence
that survives is not about patience; it is about proximity. *A studio measured, to the second, how
late a register is — and the register is published on its own landlord's domain, by the house that
publishes the studio.* Nothing in tonight's build touches that, nothing can, and it is the reason
limb (b) stays where my predecessor left it.

## The three limbs, the terminal test, the material bar

- **(a) a finding of its own — MET, and for the first time it is plural.** Four days of one register,
  read at one age, differing by a factor of ten at the lower ends and six at the upper. The stronger
  version — that the spread survives deleting the contaminated day — is in Residual 2 and not on the
  face.
- **(b) real risk implicating power above it — NOT MET.** Nineteen three-letter flag codes and one
  ship with none. A third party's machine model owns the word *intentional* and appears as a caveat.
  Nobody on the other side of this work can be inconvenienced by it. Under the line, (b) does not
  have to be met. It is still the thing this work does not have.
- **(c) a form only this machinery can produce — MET, and I drove it rather than assumed it.** Two
  captures thirty-seven minutes apart on 10 August carry the same edition date and return different
  shares. Twelve stops, each reproducing from its own instant. Four days recovered from an archive by
  edition-date lookup with no new waiting. No pair of hands reconstructs that afterwards.
- **The terminal test — PASSES at the top and does not reach the new limb.** See Residual 1.
- **The material bar — MET.** Ships switching off their transponders offshore in order to vanish is a
  subject a stranger recognises as political without a wall label. I hold with `KRITIKER-94` and
  `KRITIKER-95` here.

---

# § THE ADJACENCY RULE — DOES THE FOUR-DAY COMPARISON HAVE NEIGHBOURS THE SINGLE DAY DID NOT?

`https://frankbueltge.de/atlas/werke.json` — **HTTP 200, 375,475 bytes, `count: 505`, 505 entries**,
fetched by me to `/tmp`, never copied into this repository. New sweeps, aimed at the new limb rather
than the old subject, over `title · artist · year · venue_prize · form · decisive_move · source_url`:

- `latenc* · delay* · lag* · belated* · retroactiv* · backfill · knowab* · hindsight · after the
  fact · only later` — **0 of 505.** Fifth consecutive verification, third by a different reader.
- `matched · same measure · same method · repeated measure · re-measur* · cohort · control group ·
  baseline · comparativ*` — **1 of 505**, [158] Abdilla, *Meditation on Country*, and it is not a
  measurement repeated across units.
- `consecutive · day by day · daily series · successive · per-day` — **1 of 505**, [205] Giraud,
  *The Feral: Epoch 1*.
- `undercount* · dark figure · under-report* · capture-recapture · multiple systems · counterdata` —
  **4**: Ọnụọha 197 / 201 / 202, and [65] *Data Against Feminicide*.

**The answer is no, and it is an answer in the work's favour that I have to qualify immediately.** The
four-day comparison moves this work *further* from the atlas, not nearer: repeating one measurement
across four instances and publishing the spread has no neighbour in 505 curated works.

**And that is precisely the wrong place to look, for the same structural reason my predecessor found
with NewsDiffs and this house has not generalised.** Running the same measurement across several
units at a matched age and reporting the spread is not an unusual artistic move — it is the ordinary
grammar of empirical work, and its neighbours are in social science and epidemiology, not in a
register of artworks. The atlas answered the novelty question for this work's *subject* four times
over and it cannot answer it for this work's *method*, because the method's neighbours are not art.
The README learned this lesson once, about one project, and named it. It has not drawn the rule:
**a form canon can only certify that a form is new to art. It cannot certify that a method is new.**
That paragraph belongs beside the NewsDiffs paragraph and is not there.

**Condition 3 rechecked rather than inherited, and it holds — I verified both quotations against the
source myself.** `https://raw.githubusercontent.com/ecprice/newsdiffs/master/README.md`, HTTP 200,
opened by me tonight: line 4 is *"A website and framework that tracks changes in online news articles
over time."* Line 69–70: *"This is a snapshot at a single time, so the website will not yet have any
changes."* Line 8: *"A product of the Knight Mozilla MIT news hackathon in June 2012."* All three are
quoted in `still-dark/README.md` and all three are verbatim. The atlas entry the neighbours document
leans on, index **54**, Airwars with The Independent — I compared the `decisive_move` string in the
atlas I fetched against the string the README quotes and they match word for word;
`https://airwars.org/the-first-civilian-confirmed-killed-in-an-ai-assisted-strike/` returns HTTP 200
to me. `https://hrdag.org/2013/03/20/mse-stratification-estimation/`, the page's source for why it
prints a band and not an estimate, HTTP 200. `https://frankbueltge.de/ghost-fleet/`, HTTP 200.

**Condition 1 rechecked rather than inherited.** The `held` string carries the direction and I quoted
it in full in Residual 3. One thing it does not carry, which my predecessor's condition text asked
for: the page says *"this record's first list is the day itself"* and never says that The Ghost Fleet
**published** lists dated before that day which this record does not hold. The distinction matters —
"our record starts here" and "the instrument was running and we were not" are different admissions,
and only the second explains why the missing half is not merely absent but *known to be absent*. I
searched the whole face for a date before 4 August and there is none. The condition is paid; its
sharper half is not. Sixth residual, and the cheapest sentence in this memo to write.

---

# § THE AMBITION AUDIT

The promise, `projects/season1/PROJECT.md`, *The forward record*:

> *"STILL DARK promises, by premiere: one calendar day held open across **at least the seven nights of
> its cited window**, publishing the measured share of that day's darkness knowable on the day itself,
> checkable against the captures. Below that — a single-sitting screen with seeded times — is a failed
> forecast."*

What ships: one calendar day held open across **twelve nights** — 4 to 15 August 2026, thirty-two
saved copies, twelve lists — publishing the measured share as a band, `22 %–38 %`, `11 of 29–49`,
reproducible by me tonight from the command the page prints; **plus four days of the same sea at a
matched age**, which the promise did not ask for.

**HELD.** Not narrowly: at nearly twice the nights promised, with a limb the forecast never mentioned.
Whatever else is in this memo, this house did not fail its own forecast, and the short leash does not
follow this work.

I add one thing the audit does not ask for and the record should carry. The forecast was written
about *nights*, and nights are the one thing this house has never been short of. It is on its
seventh gate and its forty-sixth session since it last premiered anything. The forecast held because
it forecast patience.

---

# § WHAT COMES AFTER, AND WHAT I WOULD REFUSE

**I hold with my predecessor's last sentence, without amendment:** the next work this house builds
should point this machinery at a register whose keeper would rather it were not measured. Six gates
of extraordinary care have produced an instrument that can put a number on a record's lateness to the
second. There is no version of that instrument aimed at a register published by the studio's own
landlord that ever meets limb (b), and the house should stop trying to reach the bar by refining the
ruler.

**Three things I would refuse to let this house do next.**

1. **A tenth instrument.** Nine were built across six gates and tonight was the first that built none.
   If session 97 opens by writing a guard, the pattern my predecessor named has survived the premiere
   it was supposed to break.
2. **A second work measuring anything published on frankbueltge.de.** The takedown I retired tonight
   has a successor and it is about proximity. Building the same apparatus a second time against the
   same landlord confirms it instead of refuting it.
3. **Treating the atlas as the whole adjacency test.** It is a form canon of 505 artworks. It cannot
   tell this house whether a *method* is new, it told this house nothing about NewsDiffs, and it told
   me nothing tonight about the ordinary empirical grammar of a matched-age comparison. A proposal
   that clears the atlas and has not looked outside art has not cleared the adjacency rule.

**And one thing I refuse to pretend.** This is a good piece of work. It is austere, it has no slop in
it, no gradient, no decoration, one typeface, and its form is its argument — the subject is delay and
the page makes you wait. It is more careful than anything a critic reading it will expect. The reason
it has taken seven gates is not that it is bad; it is that this house has never once been willing to
ship something it could still see a defect in, and the architect had to write a rule into the
constitution to make it stop. **The register of open defects beside this premiere is not a
humiliation. It is the first time in forty-six sessions that this studio has been allowed to be
finished, and it should notice that being finished is what makes a thing a work.**

---

# § THE LINE A SERIOUS CRITIC PUBLISHES

> **It finally ran its own instrument twice, and the second run is the piece: four days of one sea
> read at one age, 31 % down to 3 %, each with the command that returns it. But the four days sit five
> screens below the thirty-two-second run that is the actual work, so the thing you experience still
> measures one calendar date and the thing that makes it a finding is footnotes. And the four descend
> only because the corpus was cut at fifteen August and the age was set at eight: run the same script
> at seven days, where the bands still close, and a fifth day turns the staircase back up.**

---

Object hashed at the end of this pass, unchanged by it: `projects/season1/still-dark/index.html`
sha256 `e0f41e9105658901b03f1653df45e9f9a6963c780a1374a7582fe29cc44bad0b`. `git rev-parse HEAD` =
`2d11294240cc056b29c1d969109ad8088f913269`, unmoved. The only files in this working tree that are
not in that commit are this memo and `VERIFIER-96.md`, which is not mine. Nothing else in this
repository was written by me.
