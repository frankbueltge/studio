# DRAMATURG-92 — STILL DARK, 4 August 2026

**RETURNS FOR RESTAGING.** The night this work's argument finally arrived — the count of
ships it can prove were dark on 4 August jumped from four to eleven and landed exactly on
the threshold its own printed law names — the page staged that arrival in 11.52-pixel type
for 1.6 seconds, said none of it aloud, and put the law that makes it mean anything 1,072
pixels below it on a phone; and it does all this while scrolling sideways at every browser
width between 481 and 664 pixels.

---

## THE FIRST ENCOUNTER, in the order a visitor meets it

At 390×844 the page opens well. `4 AUGUST 2026` at y=12.8, a subtitle that states the whole
subject in nineteen words, then a 57-word gloss (128.9 px) that defines *dark*, names the
instrument and admits its limit before any figure appears. At y=234 the figure: **100 %–100 %**,
the second end greyed. Under it `11 of 11`, under that `11 of 230`. Then the buttons, then
the line that says a run is coming. Everything through the state line stands above the fold
with 290 px to spare.

Then it holds still for 14.07 seconds. That stillness is the best decision on the page. A
stranger sits with a day that believes it knows itself completely, and the number that
believes it is 100 %. At 14.07 s the figure drops to 79 %, and every 1.6 s after that it
falls again while a second list of names grows under a heading that says *nobody could have
had it on the day*. At 26.87 s it reaches 26 %. **The terminal test passes.** I severed
nothing and needed no reading: from the first screen alone a stranger gets that a day's
record fills in after the day, and that three quarters of this one arrived late. The form
embodies the idea rather than illustrating it — the page's subject is delay, and the page
makes you wait.

**Presence is real.** This is not a document with a widget on it. Every stop is a button;
out-of-order presses work (I drove 9→0→7→3→9 and every state was exact); the eleven buttons
are the first eleven tab stops in order; each stop rewrites a shell command whose timestamp
matches the fetch instant in the ledger 3,600 px lower. A press during the 14 s dwell stops
the run and says so in different words from a press when nothing is playing. The ending is
right: the page finishes on *"Forty-two is what this record can place in 4 August 2026, not
what was on the sea that day"* and nothing stands after it.

**No slop.** I looked for it. There is no gradient, no icon, no emoji, no animation easing,
no colour beyond ink and one grey. Nothing on this page arrives as ornament.

And then the turn does not land. Across nine beats the share falls by degrees eight times.
Exactly one thing changes *kind*: the count of ships this record can call **certainly** dark
goes 0 → 2 → 4 → **11**. That last step is tonight's event and the largest movement this
numeral has ever made. I watched it at 26.87 s. The share went 31 → 26 in 46.4 px of bold.
The fraction went `11 of 35` → `11 of 42` in 24 px of bold. And `4 of them certainly dark`
became `11 of them certainly dark` — one extra digit, in 11.52 px, at weight 400, in the same
breath as seven new bold name-chips appearing below the fold. It is 8.0 % of the changed
pixels at 1400 and 10.4 % at 390. Then, 1.6 s later, the run says it has finished.

It slides past unseen. I drove it ten times and had to instrument the DOM to be sure I had
seen it.

---

## NUMBERED CUTS

**1. `.sd-root .sd-share-when { min-width: 46ch }` (index.html:557) and its 480 px scope
(:572–573).** The document is 665 px wide at *every viewport from 481 px to 664 px
inclusive* — 184 continuous widths — overflowing by up to **+184 px at 481 px, 38 % of the
window**. The whole page rocks sideways there: not a table inside a scroller, the page.
The comment above the rule (:562–571) announces that session 86 stopped the sideways scroll
and states the reason for scoping the repair to phones: *"the desktop line is the one the
renders and every panel to date have seen."* That sentence is the defect. The fix was
applied at the one width that was measured and left live across the entire band between the
two widths this house photographs. This is banked failure 53 verbatim, still in the file,
in the very rule whose comment declares it fixed. **Cut the media-query scope; the rule
`flex: 1 1 100%; min-width: 0` applies at all widths.** Without it the page holds its own
width at 280, 320, 360, 390, 480, 481, 540, 568, 600, 664, 665, 700, 900, 1400 and 1920 px.

**2. `.sd-root .sd-arrive-certain { font-size: 0.72rem; }` (index.html:165–170).** 11.52 px
and weight 400, on a row it shares with a 24 px/700 fraction, under a 46.4 px/700 share.
Measured at the final beat: share 12,961 px², new chips 18,704 px², fraction 2,774 px²,
**the turning numeral 2,989 px² — 8.0 % of everything that moves.** The size was chosen in
session 90 and the reason is written at :158–163: it *"must not compete with the numeral the
run is named after."* That reasoning held when the sequence was 0 → 2 → 4. Tonight the run
is named after the wrong numeral. **The count that turns takes the fraction's size and
weight — `clamp(1.1rem, 2.3vw, 1.5rem)` / 700 — and the 46.4 px share gives way to it.**
Without the cut, the one node in twenty-nine seconds that changes kind is the least emphatic
thing in its own frame.

**3. `share_fixed_of` — the string `"11 of 11"`, computed at all ten stops (index.html:787,
852, 885, 914, 939, 972, 1013, 1058, 1087, 1116) and rendered nowhere.** `showStop()`
(:2783–2830) reads eight of the stop's eighteen keys and skips this one. The consequence:
the figure prints two ends, `26 %–100 %`, and gives a denominator to only one of them. The
law at `#sd-arrive-constant` compares the certain count against precisely that missing
denominator. **Print it on the fraction's row.** At the last stop the frame then reads
`11 of 42 — 11 of 11` with `11 of them certainly dark` beside it, and the coincidence
becomes visible instead of arithmetical. No new computation: the number is already in the
frozen file, ten times.

**4. `#sd-arrive-constant` (41 words, 94 px at 390).** It stands 542 px below the numeral it
governs at 1400×900 and **1,072 px below it at 390×844, in an 844 px viewport** — it can
never share a phone screen with the number it is about. It is the only sentence on the page
that names the threshold (*"holds at 100 % until more of these ships are certainly dark on
this day than the eleven the day itself named"*). Tonight that count reached eleven exactly.
**Either it moves inside the reserved frame or it comes out.** A law that cannot be read in
the same glance as the figure it constrains is 94 px of phone screen bought for nothing.

**5. `#sd-arrive-cut-refused` (164 words, 284 px at 390) and `#sd-arrive-cut-refused-src`
(36 words, 110 px).** Two hundred words and 394 px explaining why the page does not use
multiple systems estimation — a method the visitor has never heard of and has not asked
about, argued through a quoted assumption, a scope clause, and a citation. Its conclusion,
*"That is why this page prints a band and no estimate"*, is already performed by the band
standing in the figure. **Cut both; keep the final clause if anything.** The head block
loses 394 px on a phone and the work loses nothing a stranger came for.

**6. `arrive.caption` / `#sd-arrive-cap` — "A ship reaches the list only after it comes back,
so a day that is over keeps being answered." (19 words, 56 px, at document y=1,339 on a
phone).** The gloss says it at y=98 (*"which name a ship only once it has come back"*) and
`.sd-because` says it again at y=2,998 (*"reaches the instrument's daily list only when the
ship comes back"*). Three printings of one mechanism. **Cut the caption** — it is the one of
the three that is neither the definition nor the lede's argument, and it is 1,241 px away
from the first printing, where nobody is still looking for it.

**7. `arrive.run_states` — six strings, not one of which contains a numeral.** Measured over
a full 28.5 s run: **9 figure rewrites, 3 spoken sentences, 0 spoken numbers.** A visitor who
cannot see the screen is told a run has started and that it has finished, and never told a
single figure — not 100 %, not 26 %, and not the turn. The code comment at :2503–2508 claims
*"the visitor who can see the figure move and the visitor who cannot are told the same thing
in the same words at the same moment."* That is false, and `announce.mjs` reports SPOKEN 3
and calls it green because it counts announcements and not their content — banked failure 32
one level up. **Either the claim comes out of the comment, or `run_states.done` and
`run_states.held` carry the stop's own figures.** One string each; both stops already hold
the numbers.

**8. `#sd-arrive-ladder button` — all eleven are 21 px tall** (79×21, 52×21, 59×21 ×8, 93×21)
at every width from 320 to 1920. WCAG 2.2 SC 2.5.8 sets 24×24 CSS px as the minimum. On a
phone these three wrapped rows of 21 px targets are the *only* interaction this work has.
**Three pixels of vertical padding.**

**9. `.sd-arrive-controls` and the claim at :2494 that it is "held to the bottom of the
viewport."** It is not: the mechanism is a flex `order` swap at ≤480 px (:596–600) which
reorders paint and pins nothing. `tools/fold.mjs` **exits 1 on the frozen object** — at
390×844 the ladder is off screen at scrollY 449 (top −21) and both the ladder and the state
line are gone at 674 (−246, −168). I drove it: at scrollY 700 mid-run the figure sits at
−466, the ladder at −272, the state line at −194, and the hole's list is the only thing on
screen — thirty-one names arriving with no figure, no share, no control and no announcement.
Reaching the hole is the reason to scroll; scrolling to it costs you the instrument.
**Cut the false sentence from the comment and treat the instrument's red as red.**

---

## WHAT I DROVE, AND WHERE

Chromium via Playwright, launched by me, against the frozen file.

- **Layout at nine widths** — 1400×900, 1280×800, 1024×768, 900×900, 768×1024, 430×932,
  390×844, 360×740, 320×568. Sixteen elements boxed at each. No sideways scroll at any of
  them, which is exactly why nothing found cut 1.
- **A sweep from 440 to 1100 px in 10 px steps, then single pixels at the boundaries.**
  This is where nothing else goes and it is where the work is broken: `docW` pins at 665 px
  from 481 through 664 inclusive. 480 is clean; 665 is clean; the 184 widths between them
  are not. Culprit isolated by hit-testing every unclipped element: `span.sd-share-when`,
  computed `min-width: 292.089px`, laid out at 643 px, inside the SUPERSEDED/LIVE block —
  the work's own retraction of its own published number.
- **The full run, instrumented with MutationObservers**, at 1400×900: t=0 stop 0; 245 ms
  first state line; 14,072 ms stop 1; eight beats of 1,600 ms; 26,872 ms stop 9;
  28,472 ms "finished". 49.4 % of the run is the first stop. The certain count first moves
  at 23,672 ms — 83 % of the way in — and makes tonight's jump at 26,872 ms, 94 % in.
- **Interaction**: press at t=2 s during the dwell (run dies, correct sentence, does not
  resume — right); out-of-order 9→0→7→3→9 (exact each time, bold-chip counts correct);
  replay from a held stop (returns to 100 %–100 % and re-runs with the full 14 s dwell);
  keyboard-only (all eleven buttons are the first eleven tab stops, in order).
- **Scroll during the run at 390×844** — cut 9.
- **Resize 1400→360 mid-run**: `reserve()` recomputes, the current stop is preserved
  (stop 2 held across the resize) and the run continues to stop 5. Clean.
- **`prefers-reduced-motion: reduce`** at all nine widths: rests on stop 0 with all ten
  buttons and an honest state line. This is right and I would not touch it.
- **Dark scheme at 280, 320, 360, 390, 480, 600, 1920**: tokens flip, body paints, no
  transparent ground. Clean.
- **House instruments, read-only**: `gaps.mjs` PASS/PASS (bars and axis, seven widths).
  `announce.mjs` — 1 live region, 4 writes, 3 spoken, 0 numbers. `tools/frame.mjs` HOLDS at
  both its widths. `tools/tiers.mjs` PASS. `tools/fold.mjs` **exit 1, 130 failures.**
  Two of five are red or lying, and the page shipped past both.

Not run, per the pass rules: `render.mjs`, `data.py --write`, `capture/capture.py`.

---

## WHAT THE WORK IS, WITHOUT THE NINE

Strip cuts 5 and 6 and the head loses 450 px of phone screen and three sentences it says
elsewhere. Take cuts 2, 3 and 4 and the last beat of the run becomes: **26 %–100 %** over
**11 of 42 — 11 of 11**, with **eleven certainly dark** standing at the same weight beside
the eleven it has just drawn level with, and the law within a glance. That is the piece.
Everything needed for it is already computed and already in the frozen file. What is missing
is the decision about which numeral this run is named after — and tonight the data answered
that question and the staging did not hear it.

---

**index.html, sha256 at the start of this pass:**
`a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`

**index.html, sha256 at the end of this pass:**
`a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`

Unchanged. Nothing was edited but this memo.
