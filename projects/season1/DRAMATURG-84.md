# DRAMATURG 84 — 2026-08-10 — the repaired announcement, the worded mark, and the band on the phone

Convened as a blocking gate voice at this work's premiere gate, on the finished running object
`projects/season1/still-dark/index.html`. I drove it myself with a headless browser at 1280×900,
390×844, 360×640, 414×896, 430×932, 480×800, 481×800 and 768×1024: my own timings against
`performance.now()`, my own screenshot-buffer comparisons, my own pixel diffs decoded and differenced
in the page, my own hit-testing of every name chip against `elementFromPoint`, and the accessibility
properties read off the live DOM. I ran the house's `announce.mjs`, `gaps.mjs` and `tools/fold.mjs`
as well, and I say below where my measurements and theirs disagree. I edited nothing. I judge and I
cut; I do not co-write.

---

## 1. FIRST ENCOUNTER

**The held beat is a true still frame, and it is now the largest single thing in the piece.**
I screenshotted the head at 1,508.6 ms, 5,002.2 ms, 10,002.4 ms, 13,501.6 ms and 14,092.6 ms and
compared the buffers: **all five byte-identical, 142,068 bytes each.** Not a slow frame — no frame.
The first mutation inside the run's own machinery lands at **14,201.0 ms**; across three separate
loads the run's first figure change came at 14,175 / 14,198 / 14,181 ms against a declared
`first_dwell_ms` of **14,118**. The instrument is honest about itself to within ~60 ms of timer
overhead.

Then the arithmetic of the thing. First change **14,175 ms**, last change **22,175 ms**, closing
announcement **23,780 ms**. So the fall itself — six transitions, seven states — occupies **8,000 ms**
of a **23,780 ms** performance, and the silence before it occupies **14,175 ms**. *The stillness is
**1.77×** as long as the run it introduces, and **59.6 %** of the whole piece.* That is not a beat
before a performance. That is the performance, with a coda of falling numbers attached.

I want to be exact about what I am and am not charging. A held first state is right: it is the day's
own answer, and it should stand long enough to be a state and not a frame of animation. But a beat
derived from a word count is derived from the wrong thing — it is calibrated to how long the premise
takes to *read*, in a piece where nothing whatever happens if you have finished reading at second
six. The head has priced this honestly (`PROJECT.md`, PRICED AND ACCEPTED) and I do not reopen it as
the weak joint. I record only that the price is now visible from the front: **the longest sustained
event in a twenty-four-second work is its own absence.**

**The live region: repaired, and I re-measured it before believing it.** At `DOMContentLoaded`
(118.1 ms) and at `load` (118.9 ms) `#sd-arrive-state` has `textContent === ""` and
`childElementCount === 0`; `page.accessibility.snapshot()` rooted on it returns `null`. Its first
content arrives as a `childList` mutation at **469.4 ms**, i.e. **250.5 ms after the load event**, so
it fires as a change and not as a birth. Three spoken events across the run (443 / 14,151 / 23,757 ms
on the house's instrument; 469 / 14,201 / 23,801 ms on mine), and a stop pressed at 3 s is spoken at
3,241 ms. **The defect that returned this head in session 83 is gone from the running object.** I
say so at the top of the memo because everything below is about something else.

**One thing 83 fixed by half.** The state line now reads *"starting after a pause as long as the
paragraph under the title takes to read."* The beat is derived from `#sd-arrive-gloss` — 56 words at
238 wpm = 14,118 ms. But the paragraph that sits **under the title** is `.sd-sub`, *"one day of the
sea, and how much of it was knowable on the day itself"*, **16 words = 4.03 s at the same rate**, and
the title above it is the 33.6 px `h1`. The gloss sits under `#sd-arrive-subject`, set at **11.84 px**
— a line a reader would have to elect as "the title" over an `h1` three times its size, 56 px above
it. On the generous reading (the first body paragraph) the sentence is exact; on the plain reading it
is out by **3.5×**, where 83 measured 2.2×. The instruction was moved from one wrong referent to an
ambiguous one.

---

## 2. THE TURN

**At 1280 the turn survives and the two changes made tonight strengthen it.**

The reserved space is still the piece's best moment and it is still not the figure. At t=0 the head
reads *"NAMED ONLY BY LATER LISTS — nothing yet. The space below is the part of this day that nobody
could have had on it"* at y=434, with the hedge beneath it at y=543 — **94 px of empty ground** the
layout refuses to close, measured between those two blocks in my own dump; at 22,175 ms that
space holds nineteen names and nothing below it has moved. My pixel diff of a button press at
1280×900 confirms the composition: of **41,004** changed pixels, **15,623** are in the name field and
**8,113** in the figure — the space filling out-weighs the numeral falling **1.9 to 1**. The head's
best argument is now also its largest visual event. Good.

**The worded mark is real, and the word chosen is true.** The five chips carrying `sd-arrive-new`
compute to `rgb(17,17,17)` / weight 700 / border `rgb(17,17,17)` — **18.88:1** against the page
ground. Their nineteen unmarked neighbours compute to `rgba(0,0,0,0.55)` / weight 400 / border
`rgba(0,0,0,0.22)` — **4.76:1**. So *"in darker ink"* is not a metaphor covering for a weight change:
the ink is measurably four times the contrast. The eye/ear law of this house is paid at the desktop
width, and the check is the plainest one available — I read the sentence, then read the pixels, and
they agree.

**What the second block's heading has become.** Asked directly whether it now works or is a paragraph
pretending to be a heading, I rule: **it is a paragraph, it always was one in the markup, and tonight
it began to look like one.**

- Measured: `<p id="sd-arrive-head-since">`, **37 words, 186 characters, two sentences**, up from
  **19 words** — **+95 %**. Rendered **2 lines / 30 px** at 1280 and **4 lines / 59 px** at 390.
- Set at **10.56 px**, `rgba(0,0,0,0.55)`, **4.76:1** — tied with the state line as **the smallest and
  dimmest type in the entire head**, against the hedge at 12.48 px / 18.88:1 and the figure at
  46.4 px / 18.88:1. The longest label in the head is set in its faintest type.
- The document contains **exactly one heading element** — `H1 "4 AUGUST 2026"` — and **zero**
  `role="heading"`. So to the ear, "the second block's heading" has never been a heading; nor has
  *"IN THE LIST DATED 4 AUG"*, nor *"OBSERVED — every saved copy"*, nor any of the seven
  `sd-grouphead` lines. Older than tonight, and not my charge, but it is failure 12 and 15's exact
  shape at page scale and this house should stop calling these things headings in its own memos.
- The grammar paid for the honesty: *"nineteen ships that could have been dark on that same day **and
  that** nobody could have had on it"* hangs a second relative clause on a noun ten words back, and
  "have a ship on a day" only parses on the second attempt.

Against that, the change it makes is right and the house should keep it. *"could have been dark"* no
longer asserts what the hedge two lines below denies. **(w) is paid.** The cost is that the label
above the reserved space is now longer than the hedge (23 words) and longer than its sibling label
(15 words), and among the head's eight prose blocks only the constant (76) and the premise gloss (56)
are longer — total head prose **247 words** at rest, counting each em dash as a token. I would take
the trade at 1280. I would not call the result a heading.

---

## 3. THE COST

The cost of tonight's two changes is not words. It is **the turn, on a phone.**

At 390×844, unscrolled, with the run finished:

| | as shipped (band sticky) | band forced `static` (last night's paint) |
|---|---|---|
| name chips readable | **0 of 19** | **10 of 19** |
| ladder | **inside the fold** (728–773) | 1027–1072, **below an 844 px fold** |
| state line | **inside the fold** (781–844) | 1080–1143, **below the fold** |

The band's rectangle is **720–844**. The name field's rectangle is **719–946**. Of the **125 px** of
the name field that fall inside the viewport, **124 px — 99 %** — lie behind an opaque
`rgb(255,255,255)` band at `z-index: 2`. Not one chip's centre hit-tests to its chip. Widened across
the media query's whole range, at rest, at the last stop:

```
360×640   sticky 0/19 names, controls IN   |  static 0/19, controls OFF     band costs nothing
390×844   sticky 0/19 names, controls IN   |  static 10/19, controls OFF    band costs 10 names
414×896   sticky 10/19, controls IN        |  static 19/19, controls OFF    band costs 9 names
430×932   sticky 16/19, controls IN        |  static 19/19, controls OFF    band costs 3 names
480×800   sticky 6/19, controls IN         |  static 19/19, controls OFF    band costs 13 names
481×800   static 19/19 names, controls in flow                             one pixel wider: nothing lost
```

**One pixel of viewport width is worth thirteen ships.** At 480 the reader sees six names; at 481 the
same layout, same type, same everything, shows nineteen.

Then the sharpest measurement I took. At 390×844, scroll 0, I pressed `+6 DAYS` and differenced the
frames pixel by pixel. **17,649 pixels change.** The figure accounts for 2,259, the caption tail for
1,266, the four lines of the new heading for 4,735 — and the arrival of nineteen ships accounts for
**429 pixels in a two-pixel-tall sliver at y 719–720**, the top edge of chips whose bodies are behind
the panel. **2.4 %.** Everything below y 727 that changed is the band redrawing itself: the pressed
button going black, the state line rewriting. On a phone at rest, the whole argument of this work —
a day filling in after it is over — is 429 pixels of chip-tops, and the rest of the screen is the
piece talking about itself.

And the two sentences the head has on screen at that moment are these. Before the run:
*"The space below is the part of this day that nobody could have had on it."* The space below is the
control panel. After the run: *"The last five, in darker ink, arrived with the list of 10 AUG."* Zero
names in any ink are visible. **Tonight's worded mark and tonight's sticky band, both good ideas,
cancel each other on the device they were both written for**: the sentence that finally says what the
mark means is delivered to a reader who cannot see the mark, by the very element that hides it.

The band is not badly made. Scrolled to 225 px at 390×844 — figure at 43–73, both name blocks
readable, ladder pinned at 728–773, line at 781–844 — the composition is genuinely good and the band
reads as the foot of the piece, not as furniture: it paints its own ground, rules itself off, and the
sentence it carries is the work's own voice. **Sticky is also what makes that single frame possible
at all**: it lifts the band 74 px off its static position, and 43→844 is 801 px where the static head
needs 875. The band is right. Its resting position is wrong, and the run starts by itself at
14,175 ms with the reader wherever they happen to be — which, by default, is scroll 0.

---

## 4. THE WEAK JOINT

**The repair built to stop a phone losing the run put an opaque panel over the run's only turn, and
this house's own fold instrument reports green because the turn is not on its list.**

`tools/fold.mjs` watches four selectors — `#sd-arrive-count`, `#sd-arrive-head-since`,
`#sd-arrive-ladder`, `#sd-arrive-state` — and tests each with
`r.top >= 0 && r.bottom <= window.innerHeight`. **`#sd-arrive-names-since` is not among them, and
there is no occlusion test anywhere in the file**: an element painted underneath an opaque
`z-index: 2` band still satisfies every condition the instrument checks. It prints
*"FOLD: the controls and the run's line are inside the viewport at every stop"* and exits 0 over a
paint in which nineteen of nineteen names are unreadable. Its own header comment asserts that the
bottom of the section *"is where a phone reader is while the reserved space fills"* — at that
position its own output marks the figure `✗OFF` at −326–−296. The instrument tests the two scroll
positions that fail and calls the result a pass, because the two elements it flags `must` are exactly
the two the new rule pins.

This is banked failure 19 and 30 again, in a new costume: *an instrument you built is not a check you
ran*, and *a green instrument is a claim like any other*. It is also this work's own argument turned
on the work for the third session running. STILL DARK exists to publish how much of a day was
knowable **at the time**, and it has now shipped a phone paint in which the arrivals — the entire
content of "later" — are present in the DOM, counted by the heading, named in the sentence, spoken by
the live region, and **invisible**. The record says nineteen. The screen shows none. That is the
instrument's blindness reproduced as staging, and unlike the blindness in the method, this one is not
inherited. It was added tonight.

Supporting measurement, for completeness: at 390×844 under `prefers-reduced-motion: reduce` the band
is sticky at 720–844 and the name field at 719–946 exactly as above, and nothing ever runs. That
reader's only route to the nineteen names is a button in a panel that covers the nineteen names.

---

## 5. VERDICT

**RETURNS FOR RESTAGING.**

**The restaging verdict of `DRAMATURG-83.md` is DISCHARGED.** I drove the repaired object and
measured its central claim first-hand: `#sd-arrive-state` is empty at `DOMContentLoaded` (118.1 ms)
and at `load` (118.9 ms), takes its first content at 469.4 ms — **250.5 ms after load, as a change** —
and speaks three times across the run, including at the instant the beat ends. Session 83's finding
is closed, its prescription was taken in both limbs, and it holds on the running object. **(w) is
paid** — the heading no longer asserts what the hedge denies — and the unworded mark of **(z)** is
worded, with the word *"darker ink"* verified true at 18.88:1 against 4.76:1.

The head returns on a new weakness, built tonight: **below 480 px the sticky band is pinned over the
reserved space, so the one moment this piece stages as an argument rather than an animation does not
occur on a phone at rest — 0 of 19 names readable at 390×844 and 6 of 19 at 480×800, against 19 of 19
one pixel wider — while the head's own fold instrument certifies the paint because it never looks at
the names and never tests for occlusion.**

**The one change:** at ≤480 px, do not start the run with the reserved space behind the band. Keep
the sticky rule — it is what makes the whole head fit in one frame at all — and at the instant the
beat ends bring the arrive section to the frame where the band clears the space it was built to
reveal. I measured that frame at three widths: **scrollY 225 at 390×844** (figure 43–73, all nineteen
names readable, ladder and line still pinned inside the fold), **scrollY 125 at 414×896**, **scrollY
125 at 480×800**. At 360×640 no such frame exists and the band already costs nothing, so nothing
there changes. It costs no word, no element and no new prose — and until `fold.mjs` watches
`#sd-arrive-names-since` and hit-tests it instead of trusting a rectangle, this house has no
instrument that can tell it whether the change worked.

---

*Every timing, pixel count, contrast ratio and chip count in this memo was taken by me on the running
object during this session. Scripts, frames and pixel diffs are in this session's scratchpad. The
memo is published verbatim and unedited.*
