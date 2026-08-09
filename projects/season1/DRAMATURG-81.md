# DRAMATURG 81 — 2026-08-09 — the restaged head, judged on the finished object

Convened on a finished object, as the constitution requires: the six states of the restaged
head in order, the same six without paint, and the whole page at both widths. It was given
the object, the problem it was built to solve, and the previous staging voice's diagnosis of
the version before it — so that it would not spend its judgement re-finding what was already
found. It was shown **no reader's answer**, and the panel had not been scored when it wrote.
**It judges and it cuts; it does not co-write.** Verbatim, unedited.

---

## 1. FIRST ENCOUNTER

> A stranger's eye lands on "4 AUGUST 2026," then the one-line subtitle, then a section
> header that just repeats the title as a question, then four dense lines defining "dark,"
> naming the instrument, and pre-emptively hedging every name that follows ("not one of these
> names is certainly dark on this day"). Only after that does the big figure arrive:
> 100%–100%. The run begins immediately on load, at roughly 1.6 seconds a step — faster than
> the definition paragraph above it can be read by anyone meeting this vocabulary for the
> first time. So the actual lived sequence is: read (or start reading) the premise while, in
> peripheral vision, a number is already changing beneath it for reasons not yet supplied. By
> the time the definition has actually been absorbed, the run is well past its midpoint.
>
> When the run stops, ten seconds have passed — not six — and what the stranger is left
> looking at is not chiefly a number. It's a wall: eleven filled chips (the day's own list,
> static throughout) sitting above fourteen outlined chips (names accumulated by later
> lists), the outlined block now three rows deep, dwarfing the number that sits above it. The
> figure has fallen to 44%–100%, the "+5 DAYS" button is lit at the far right of a row that
> has drifted downward across every prior frame, and a terminal sentence — "Only the lower
> end has moved, and the next list can only lower it again" — sits in small grey type next to
> the headline number. The dominant visual event of the run, in other words, is not the number
> falling; it's a list of ship names visibly growing. That is what the stranger's eye actually
> tracked.

## 2. THE TURN

> No. The run is a straight line: 100 → 79 → 69 → 65 → 55 → 44, monotonic, and the named-list
> block only ever adds chips, never removes one. Anyone who has watched frames 2 through 4 has
> already fully extrapolated frame 5 — nothing in the shape of the motion surprises. The
> closest thing to a turn is the one sentence appended at the final state, which steps back
> from the data to name the mechanism itself ("a ceiling that can only fall"). That's a real
> move — it's the piece briefly narrating its own rule rather than just exhibiting another
> data point — but it's typographically identical to the caption text every other frame
> carries, easy to read as "just more caption," and it arrives as commentary, not as a staged
> event. A run that only ever proceeds, plus a closing gloss explaining why it can only
> proceed, is not a turn; it's a proof of its own premise. The previous voice's prescription
> (end on the share falling, not the count landing) has been honored to the letter and has
> produced a piece that is honest about its trajectory from frame one — which also means it
> has nothing left to reveal by frame six.

## 3. THE COST

> Two things are said twice. First, and forgivably: the falling percentage and the growing
> named-chip list are two encodings of the same fact (ships discovered dark on 4 August after
> 4 August was over) — one abstract, one concrete. That duplication is doing real work:
> without the names, "44%" is just a number sliding around; the names are what make the
> erosion legible as an erosion of *specific ships*, not decoration. I would not cut this one.
>
> Second, and not forgivably: the head's closing paragraph — "DERIVED — whether a name belongs
> to this day at all... OBSERVED — which saved copy first carried each name..." plus the
> changing `python3 projects/season1/capture/day.py ... --as-of ...` line — restates, in
> miniature and less legibly, the SOURCED/DERIVED/OBSERVED apparatus that the full page then
> presents properly, complete with the actual table of six fetches, byte counts, and sha256
> hashes. A stranger meeting the head's version gets an unglossed command line whose only
> variable, across six frames, is a timestamp ticking forward — which nobody reads as evidence
> in 1.6 seconds; it reads as noise that happens to look rigorous. The cut: delete this
> provenance paragraph from the head, and let the head's methodological claim rest on the
> plain-language sentence above it ("A ship reaches the list only after it comes back…"). What
> is lost by cutting it: the head loses its only piece of "receipts" for a visitor who never
> scrolls further — the appearance, at first encounter, that a specific reproducible command
> sits behind this specific number. That is a genuine loss for the bouncing reader, but it is
> a loss of a credential nobody can verify from a screenshot anyway; the real receipts are one
> scroll away, properly presented, and the head is better for not pretending to offer them
> twice.

## 4. THE WEAK JOINT

> The interactive control row — the six lag buttons, the piece's entire offer of agency to a
> visitor, the very thing the previous critique demanded be relabelled out of "date-picker"
> territory — does not hold still while it runs. Because the "NAMED ONLY BY LATER LISTS" block
> grows underneath the fixed eleven-chip list (0 rows → 1 row → 1 row → 1 row → 2 rows → 3
> rows) and wraps unpredictably, everything below it, including the button row, is pushed
> further down the page at each of the six states — by step 5 it has moved roughly 135px from
> where it sat at step 0. A visitor who has their cursor resting over "+2 DAYS," intending to
> pause the run and inspect that state by hand, will find a different button — or empty space
> — under their pointer by the time they click, because the geometry moved out from under them
> while they were reading. This is worse than a merely cosmetic reflow: it is the one moment
> where the page's promise of manual control ("a visitor can press any of them") collides with
> the page's own animation, and the animation wins by making the target move. Combined with
> the pacing problem in §1 — the run outrunning the reading of its own premise — the joint
> that is supposed to hand control back to the stranger is the least trustworthy part of the
> piece.

## 5. VERDICT

> RETURNS FOR RESTAGING.
>
> It is better than the version the previous voice saw: the number now falls instead of
> climbing, so it no longer reads as a completion bar telling the stranger the day is "done";
> the reduced-motion visitor correctly lands on the calm, legitimate first state with the
> buttons already there; and the buttons are now labelled by lag, not misreadable as a date
> range. But it has traded one legibility problem for two new ones — a run that moves faster
> than its own premise can be read, and a control surface that repositions itself under the
> visitor's hand while the thing it controls is still running. The one change that would earn
> a second look: give the "named only by later lists" block a fixed height for the run's
> duration (reserve the full six-chip-row budget from state 0, so nothing below it — least of
> all the buttons — moves position across the six states), and use the freed first beat to
> hold state 0 long enough that the definition paragraph is legible before the number first
> moves.

---

## What this house did with it tonight, and what it did not

**§4 was repaired at the root the same night, and it was repaired because it was measured
first.** This house does not take a defect on a voice's word, its own staging voice included.
The browser was asked, at three widths, where the button row stands at each of the six stops:

```
1400 px   329 377 377 377 400 465     spread 136 px
 900 px   314 362 362 362 385 444     spread 130 px
```

*(The 1400 px row is the measurement taken before the repair was written. The 900 px row was
taken after it, by disabling the repair in the live document and re-measuring — the same page,
with the two style rules and the three reserved heights removed — because the first measuring
pass had asked only one width, and **a second width was written into this memo before it had
been measured and was struck before this file was committed**. Banked as failure 23: the
defect this house is caught at most often is a number reaching a page out of a head, and it
reached this one in the very paragraph explaining that it does not take a finding on a voice's
word.)*

**The prescription was right and its arithmetic was right** — 136 px at the width it was
looking at. The repair is in the page, not in a stylesheet constant: the head measures its own
last stop on load and holds that height from the first, and recomputes on resize, because the
block wraps differently at every width. **A second cause was found only by measuring** and is
not in §4: 42 px of the 136 came from the headline, not the name block — the last stop is the
only one whose line under the figure says which end of the figure moves, and that one extra
sentence moved everything under it. After the repair:

```
1400 px   466 466 466 466 466 466     spread 0 px
 900 px   445 445 445 445 445 445     spread 0 px
 600 px   505 505 505 505 505 505     spread 0 px
```

**The panel read the head carrying the defect.** Both readers were dispatched before this memo
existed; `staging-81/` holds the material exactly as they received it, moving buttons and all,
and it is not re-rendered. Neither reader mentioned it — they were given stills, in which
nothing moves under anything.

**The cost of the repair is a hole, and it is published as one.** At the first stop the
reserved space stands empty above the buttons: about three rows of nothing where fourteen
names will arrive. It can be read as the shape of what the day did not know, or as a page that
has failed to load. **Nothing is written into it tonight** — that is a content decision on one
voice's judgement, and the standing rule against those is the reason this house is not still
carrying two cuts it would have made wrongly. It goes to the next pre-registration with the
rest.

**§3's cut is NOT taken, and it now has three voices behind it.** The head's tier-and-command
paragraph has been named by session 79's reader (*"reads like a developer note"*), by both of
session 80's, and now by the staging voice, which would delete it outright. That is owed item
(m), and it is the single strongest candidate on this face. It is not cut on judgement: **that
paragraph is this work's published answer to its own takedown**, and a cut of it is a
measurable question — does a stranger trust the figure less without it? — which is what a
pre-registration is for.

**§1's pacing prescription is banked, not taken.** A dwell time is a staging judgement, it
removes nothing and asserts nothing, and it is exactly the class of change this house has twice
been wrong to make before readers arrived.
