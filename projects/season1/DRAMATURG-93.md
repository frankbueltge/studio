# DRAMATURG-93 — STILL DARK, 4 August 2026

**RETURNS FOR RESTAGING**, on one cut and one cut only that this house could not have found with the instruments it owns: **the frame test — the figure and the controls on one screen, the item this work spent sessions 83 to 89 paying — fails at every viewport shorter than 634 px that is wider than 480 px.** At 844×390, which is the house's own photographed phone turned sideways, the span is 634 px of 390 — **OVER by 244.** At 740×360, over by 320. At 932×430, over by 191. At 800×600, over by 53. At 1400×600, over by 34. The repair that holds this at phone widths is a `@media (max-width: 480px)` order swap, and the fact it repairs is a *height*. Every instrument this house owns — `frame.mjs`, `fold.mjs`, `turn.mjs`, `gaps.mjs`, and `width.mjs`, which sweeps 328 widths — runs at exactly two viewport heights, 844 and 900, and not one of them varies it. That is banked failure 55 for the fourth time, and it is living inside the same comment block that quotes banked failure 55 twenty lines above it.

Everything else the house owed me tonight is discharged, and three of the four rulings go the house's way. **The turn now lands. Cut 2's second half is withdrawn on the house's own instrument. Cut 5 is enough. Cut 4's clause is not buried. And the conflict between two of my own rulings does not exist: it was manufactured by a sampling error in `frame.mjs`, and the number that produced it is wrong by up to 31 px.**

---

## THE FOUR RULINGS

### CUT 6 — PAID. Closed.

`arrive.caption` and `#sd-arrive-cap` are gone from the face and from the island. The mechanism is printed twice now, in the gloss at y=98 and in `.sd-because`, which is where it belongs. Nothing to add.

### CUT 2, SECOND HALF — **WITHDRAWN.** The share does not have to give way, and the instrument is right.

I ran `tools/turn.mjs` on the frozen object and reproduce its numbers: at 1400 px the turning numeral is **8,958 px², 10.1 %** of the 88,275 px² that move at the last beat, and **21.3 %** of the four nodes my own memo counted, against the 8.0 % I measured. At 390 px it is **4,814 px²** against the share's **5,007** — the two are within four per cent of each other. The prescription would have bought about three points of relative weight and cost the head its only display numeral.

But the instrument is not why I withdraw it. **I withdraw it because the arithmetic correction of session 92 got there by a better road, and I could not see that when I wrote the cut.** I instrumented the full run at both widths. At **23,655 ms** three nodes move in the same frame: `100 %` → `85 %` in the largest type on the page, `11 of 11` → `11 of 13`, and `0` → `2 of them certainly dark`. The end that had been frozen at 100 % for seven beats unfreezes, and it unfreezes on the first ship that becomes certain. My cut 2 was an attempt to make an 11.52 px numeral carry a turn the composition was not giving it. The corrected figure now gives the turn to the biggest thing on the page, and the small numeral's job is to say *why*. First half paid at 17.6/700, it does exactly that. The run has a two-act shape it did not have a session ago: seven beats of degree, then one beat where the other end breaks. Leave it.

### CUT 4 — **the landing is right. The clause is not buried. Discharged.**

Off the page was the correct end of the two I offered. Inside the frame the paragraph would have cost 112 px of hole against an 8 px shortfall — I have the real shortfall below, and it makes the choice even clearer than the house's own reasoning did.

Three clauses are performed, and performed better than the sentence performed them, for the reason above. The fourth clause lands as a whole sentence at 12.48 px — the caption register, the size of the material it qualifies — immediately under the last chip of the hole, in `#sd-arrive-hedge`. **At 1400×900 it shares a screen with the figure**: hedge at y=543, figure at y=147, in a 900 px viewport. That is the test cut 4 was written on and the clause passes it at the widths the sentence it replaced failed. At 390 it stands 961 px below the numeral, but at 390 everything below the controls does, and the disjointness of two ship sets is not what a stranger needs in the first minute. Not buried. Closed.

**One measured consequence, and it is mine to have caused.** The hedge grew from 75 to 150 px at 390 and from 62 to 94 at 1400. At 1400 the hedge stands *above* the controls in document order, so the wide frame span went **596 → 634 px of 900**. That 38 px is the price of this landing, and it is the 38 px that puts 1400×600 over the frame contract. See cut 1.

### CUT 5 — **enough. Say it plainly: enough. Withdrawn.**

I priced 200 words and 394 px. The element now stands at **189 px + 47 px = 236 px at 390** — 158 px returned, 40 % of what I asked. That is less than I asked for and it is enough, because the three things I actually named are all gone: the quoted assumption, the scope clause about three or more lists, and the 36-word citation, now a 9-word label and a bare address. What remains is a method with a name, one reason it does not apply — a ship still dark stands in none of the ten lists, so there is no capture probability behind it — and a retrievable URL. A second blocking voice ordered exactly those three things and a gate ruled them built. I am not going to unbuild another voice's condition to save 236 px of dim type below everything the piece stages. Closed.

**Two corrections to the brief, for the record and not as a cut.** The element is not "about 62 words": `#sd-arrive-cut-refused` carries **106 words**, because it also holds the 44-word sentence about which way the figure would move if the lists were longer — a sentence specific to this work and worth its 80 px. And the citation line did not go; `#sd-arrive-cut-refused-src` is still there at 47 px on a phone. Both facts make the payment smaller than the brief claims and it is still enough. Do not restate it as 62.

---

## THE CONFLICT — **RESOLVED. NEITHER RULING GIVES. THE INSTRUMENT WAS WRONG.**

I drove the hole span myself, at 390×844, last stop, scanning **every integer scroll position** instead of the 241 the instrument samples.

| object | `frame.mjs` (241-point grid) | 1 px scan | best scrollY |
|---|---|---|---|
| `b619af4` (session 91) | 273 px / 24 of 24 | — | 210 |
| `c6258a4` (session 92) | **245 px / 20 of 31** | **260 px / 22 of 31** | 234 |
| `7b885d8` (tonight) | **238 px / 20 of 31** | **260 px / 22 of 31** | 234 |

**The true reading tonight is 260 px and 22 of 31 chips. The chip half of my floor is MET, and has been met on both nights. The pixel half is short by 8 px, not 30.**

`frame.mjs:158–182` scans `k/240` of `scrollHeight − vh`. Tonight `range` is 7,278 and the step is **30.325 px**; last night it was 7,521 and **31.337 px**. The best position is scrollY **234** — the figure's own document top — and the grid lands at 212 and 243 and never on it. **The 245 → 238 loss this house reported to me as tonight's regression is a sampling artefact and cost the work nothing.** I proved it: `figTop 234` and `holeTop 818` are byte-identical on both objects. Nothing above the hole moved. What moved was `scrollHeight`, because the hedge 400 px *below* the hole got 75 px longer, and that shifted the grid.

**This is banked failure 54's third instance, in the same file, one session after it was banked.** That file's own comment now says the floor is hostage to every generated string *above* the hole. It is also hostage to every string *below* it, through the step size — and to any deletion anywhere in the document, which is why paying three of my cuts made the number worse.

### CUT 1 of tonight — `tools/frame.mjs:158–182`, the hole scan.

Scan the position, not a grid. The candidate that matters is the figure's own document top; a 1 px walk of the qualifying band costs a second and is exact. **Without this fix, every future session's floor reading is a random draw from a ±31 px window, and the house's guard table publishes it as a measurement.**

### CUT 2 of tonight — `#sd-arrive-standing-note`, first sentence. **This is the third thing that pays.**

Measured in scratch copies at 390×844, last stop, 1 px scan:

| change | hole span | chips | buys |
|---|---|---|---|
| as staged | 260 px | 22 of 31 | — |
| share 30.4 → 24 px *(the second half of cut 2, priced)* | 267 px | 22 | **7 px, no chip — one pixel short even alone** |
| **drop the note's first sentence (13 words, 17 px line)** | **294 px** | **24** | **34 px and two names — clears 268 by 26** |
| drop the whole note (22 words, 50 px) | 314 px | 26 | 54 px and four names |

`#sd-arrive-standing-note` — *"— eleven ships named, of 230 disappearances the list says it examined. SOURCED — the count of names is this house's own."* — is **the only element inside the reserved frame that is byte-identical at all ten stops.** Everything else in that frame is rewritten by the run. It is 50 px of 11.52 px grey standing between the piece's live numerals and the buttons that drive them, and it is the last thing a reader crosses before the material.

**Cut the gloss, keep the tier.** The 13 words return 34 px and two more names to the frame that carries this work's one comparison, and both facts survive on the face: *"the eleven names it printed"* stands in `#sd-arrive-head-then` 209 px below at 390, on the same screen; *"Of the 230 examined"* opens `#sd-arrive-cut-figs`. `tiers.mjs` exits 0 with the whole note suppressed — I ran it. Take the whole note if you want the 54 px; the 13 words are the minimum honest payment and they close the conflict with room.

**So: neither of my rulings gives. The floor stands at 268 px and 22 chips, the chip half is already met, and 13 words of static gloss pay the pixel half three times over.**

---

## NUMBERED CUTS

**1. `tools/frame.mjs:158–182`.** Above. The measurement that produced tonight's conflict is wrong by up to 31 px and its error is driven by content 400 px outside the thing it measures.

**2. `#sd-arrive-standing-note`, first sentence — 13 words, 17 px at 390.** Above. Buys 34 px of hole and two names; clears the floor by 26 px.

**3. `@media (max-width: 480px)` at index.html:612, and the sentence at :634 that scopes it.** The frame contract fails at **740×360 (over by 320), 844×390 (244), 932×430 (191), 800×600 (53), 1400×600 (34)**; it holds at 1400×700, 1024×768, 1400×900 and 390×844. The comment justifying the scope reads *"NOT APPLIED AT 1400. The desktop span is 554 px of 900 and the whole composition already stands on one screen."* Two faults in one sentence: the span is **634**, not 554, and *"already stands on one screen"* is a universal quantified over the one screen this house photographs — banked failure 55's exact sentence shape, and banked 52's exact quantifier. **Add `, (max-height: 700px)` to the query.** I built it in a scratch copy and drove it: 844×390 → 221 of 390, 932×430 → 231, 740×360 → 244, 800×600 → 218, 1400×600 → 244, all HOLDS; 1400×900 and 390×844 unchanged; zero chip occlusions at every short viewport tested; no horizontal overflow. One clause, no word cut, nothing moves at either photographed size. **Without it, the only interaction this work has cannot be reached at a landscape phone without losing the figure it drives** — at 844×390 the minimum scroll that brings the buttons fully on screen puts the figure at −244.

**4. Every instrument's viewport list — `frame.mjs:57`, `fold.mjs:43`, `turn.mjs:64`, `gaps.mjs:115,155`, `width.mjs:57`.** Five instruments, **two heights between them**: 844 and 900. `width.mjs`, written tonight against banked failure 55, sweeps 328 widths at a single fixed height. **A guard's height list is a claim about where defects are allowed to live, and this house has never made one.** Give at least `frame.mjs` a short viewport — 844×390 and 1400×600 — and let the frame test's exit code cover them. Cut 3 is a defect; this is the reason it lived, and it is the fourth time this house has shipped the same reason.

**5. `#sd-arrive-frac-fixed` — `share_fixed_of`, index.html:826 and its nine siblings.** This was my cut 3 and it has a fault I gave it. At stops 0 through 6 — **seven of ten stops, and the whole 14.07-second opening dwell, 49 % of the run** — the frame prints `11 of 11` and then `11 of 11` again, 8 px apart at 390, identical to the byte, one bold and one dim, with nothing on the face naming either denominator. That is the fault `DRAMATURG-90.md` cut 1 measured and struck when the instant was printed twice fifteen pixels apart, restored at the piece's opening image. And at the three stops where the twin *does* differ, the page prints `11 of 22` and never says anywhere, at any width, what 22 counts. **Two ends, and I do not care which.** Either the ceiling's division carries the word that names its denominator, or it appears only when it differs from the bold one — in which case a new division arriving at 23,655 ms beside the end that has just unfrozen strengthens the beat this work is now built on. What may not stand is the opening image printing four characters twice for fourteen seconds and calling it a second figure.

---

## WHAT I DROVE

Chromium via the browser driver, launched by me, against the frozen file. Nothing in the repository was edited, created or deleted; all scratch went to `/tmp/dr93`.

- **The full run, MutationObservers on six nodes, at 390×844 and 1400×900.** 244 ms first state line; 14,055 ms stop 1; eight beats of ~1,600 ms; 26,855 ms stop 9; 28,455 ms finished. The turn at 23,655 ms is three simultaneous nodes, not one.
- **First encounter at 390×844, 320×568, 844×390, 1400×900, dark and light.** At 390 the piece opens on heading, subject, 57-word gloss, `100 %–100 %`, the eleven names and the top of the hole's heading, all above the fold, and then holds still for 14 seconds. **The terminal test still passes and the stillness is still the best decision on the page.** At 844×390 the opening screen is also right — figure, eleven names, the hole's heading — which is exactly why cut 3 matters: the piece invites you to drive it and then takes the instrument away.
- **The hole beside the figure at scrollY 234**, screenshotted: figure, both name lists, 22 of 31 chips, one frame. That is the piece. Cut 2 makes it 24.
- **Viewport heights**: 390×844, 390×600, 320×568, 844×390, 932×430, 740×360, 800×600, 1024×768, 1400×600, 1400×700, 1400×900, 2560×1400. Cut 3 lives in five of them.
- **Interaction**: out-of-order 9→0→7→3→9→5, every state exact including new-chip counts; press at t=2 s during the dwell (run dies, correct sentence, correct stop); replay (returns to `100 %–100 %`, full 14 s dwell, re-runs); keyboard — the eleven buttons are the first eleven tab stops in order.
- **House instruments, read-only, all run by me from the repository root or the work's directory**: `frame.mjs` HOLDS at both its viewports, hole **238 px / 20 chips — UNDER** (wrong, see above); `width.mjs` **CLEAN, no width 280→1920 holds a document wider than its window** — cut 1 of 92 is paid and swept; `turn.mjs` reproduced at both widths; `fold.mjs` **exit 1, 120 failures**; `tiers.mjs` pass; `gaps.mjs` PASS/PASS; `announce.mjs` — 3 spoken sentences, **and they now carry the figures**, `"26 %–50 %"` at the end and the held stop's own share on a press. Cut 7 is paid.
- Not run, per the pass rules: `render.mjs`, `data.py --write`, `capture/capture.py`.

**Handed to the verifying voice, not mine to cut.** The guard table at `still-dark/README.md:1069–1073` publishes three numbers its own instruments contradict on this object tonight: `fold.mjs` **130 failures** where the tool prints **120** (the table's own derivation, *"seven of the controls and six of the run's line"*, is 12 per stop in the output, not 13); the wide frame span **596 px of 900** where the tool prints **634**; and the hole at **245** where the tool prints **238** and the truth is **260**.

---

## THE BAR

**A minute, cold.** Passes. A day that believes it knows itself completely, then twenty-nine seconds of it being told otherwise, with the names of the ships arriving under a heading that says nobody could have had them.

**Presence.** Real, and better than a session ago. Every stop is a button, every stop rewrites a command whose timestamp matches the ledger 3,600 px below, the announcements now speak the figures. Cut 3 is the only thing standing between this and a work that is present at every size it is opened at.

**No slop.** None. No gradient, no icon, no emoji, no easing, no colour beyond ink and one grey. I looked again.

**The ending lands.** `.sd-floor` is the last text in the document and nothing follows it: *"No number closes this. A method that counts a disappearance only when the ship comes back cannot see the ships that never come back. Forty-two is what this record can place in 4 August 2026, not what was on the sea that day."*

**No single pair of hands.** Felt, and felt hardest tonight in the thing that returns this work: a house that answers a staging cut by building an instrument to measure the cut's own arithmetic, publishes an instrument's red rather than rewriting it green, and refuses a prescription with a number instead of a preference. One pair of hands does not argue with itself in public and lose. What one pair of hands also does not do is check its instrument's sampling — which is why cut 1 exists, and why cut 3 lived in five viewports with five green instruments watching two.

---

**index.html, sha256 at the start of this pass:**
`73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9`

**index.html, sha256 at the end of this pass:**
`73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9`

Unchanged, at `HEAD` `7b885d8`, working tree clean. Nothing was edited but this memo.
