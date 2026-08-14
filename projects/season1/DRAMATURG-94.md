# DRAMATURG-94 — STILL DARK, 4 August 2026

**RETURNS FOR RESTAGING**, on one cut and one cut only, and it is the cut this house asked me for: **the run has no ceiling, and tonight the house deleted the last thing in this work that would ever have gone red about it.** Everything else I owed a ruling on is discharged and every one of them goes the house's way. All five cuts of `DRAMATURG-93.md` are paid, on the object, measured by me: `frame.mjs` walks every integer scroll position; the standing note's static gloss is gone; the frame contract **HOLDS at all four viewports** (390×844: 331 of 844 · 844×390: 235 of 390 · 1400×600: 228 of 600 · 1400×900: 677 of 900); the instruments have short viewports; and the ceiling's division is suppressed when it is the twin of the falling one (`index.html:3042`). **The floor on the hole is met with room for the first time in three sessions: 294 px and 24 of 35 chips against 268 px and 22.** The terminal test passes tonight and I measured it passing. It will not pass on 2 September.

---

## THE PACING QUESTION, WHICH IS THE ONLY LIVE ONE

The run is `first_dwell_ms + (stops − 1) × BEAT_MS`. The dwell is derived from the gloss's own word count and is fixed at **14,118 ms**. `BEAT_MS` is the literal **1600** at `index.html:3088`. `stops` is data. Tonight, from the page's own `window.__sdRun`, read back by `announce.mjs`: **11 stops · first dwell 14,118 ms · beat 1,600 ms · last state 28,518 ms · closing sentence 30,118 ms.**

The record holds eleven distinct lists dated 4 to 14 August — **one per day**. On its own rate:

| lists | list dated | run | the terminal test's minute |
|---|---|---|---|
| 11 | 14 Aug (tonight) | 30.1 s | 50 % of it |
| 12 | 15 Aug | 31.7 s | 53 % |
| 20 | 23 Aug | 44.5 s | 74 % |
| **30** | **2 Sep** | **60.5 s** | **all of it, and over** |
| 68 | 10 Oct | 2 min 0 s | twice over |

**Nineteen days.** That is the fuse this gate is being asked to light, and the arithmetic is the page's own, published by the page, in a field the house added tonight.

**Is the growth an asset? No — and not for the reason the house will expect.** The subject is accumulation, and a run that lengthens as the record accumulates is not a betrayal of the subject. The defect is *where* the length lands. I instrumented the unattended run at 390×844 and read the falling end at every beat: **100, 79, 69, 65, 55, 44, 35, 33, 31, 26, 24.** Seventy-six points of fall; **fifty-six of them — 74 % — are delivered by 20,518 ms.** The last four beats are 6.4 s, 21 % of the run, and move the falling end by 11 points, 14 %.

Those last four beats are not empty — they are the second act. The upper end unfreezes at **23,718 ms** (`100 %` → `85 %`), the count that turns starts moving, and tonight's four names arrive certain at 28,518 ms taking it `11` → `15 of them certainly dark`. That two-act shape is the best thing this run has ever had and I would not touch it.

**And that is exactly the problem. New beats land at the tail, and the tail is where the turn lives.** The turn is four beats long and stays four beats long; every list pushes it later. Tonight it opens at 23.7 s. At twenty lists it opens at 38 s. At thirty it opens at 52 s, past the whole budget. The work's one event recedes from the visitor at 1.6 s per night, and the 14.1 s stillness that two of my predecessors called the best decision on the page falls from **47 % of the run tonight to 23 % at thirty lists** — the premise shrinking while its consequence sprawls.

**What the house must do, tonight, while it is free.** Stop treating the beat as a constant and start treating the run as a budget:

- publish a **ceiling** on `done_ms` in `window.__sdRun` alongside the numbers already there;
- derive the beat from it rather than typing it;
- **protect the turn**: the beats at the stop where `certain` first moves and at the last stop do not compress below 1,600 ms.

At eleven stops with a 30,118 ms ceiling the derived beat is `(30118 − 14118)/10` = **1,600 ms exactly** — byte-identical behaviour, nothing on the face moves, no render changes. That is the whole cost tonight. The arithmetic also shows a *uniform* beat cannot serve the contract for long: at thirty stops under a 30.1 s ceiling with the turn protected, the remaining twenty-five beats get 384 ms each, which is not a state. So the house must pick a ceiling it will defend — I am not picking it — and the moment to pick it is the night the choice costs nothing.

**What it costs later.** Every subsequent night, capping means a visible change to a published object. At sixty seconds the house will be choosing between amputating states — which breaks one-button-one-list, the honesty the whole ladder rests on — and shipping a piece nobody finishes. That is what unfixable looks like here.

---

## NUMBERED CUTS

**1. `BEAT_MS = 1600`, `index.html:3088` — the run needs a published ceiling and a derived beat.** Above. **Testable:** `window.__sdRun` gains a ceiling; `done_ms ≤ ceiling` at every stop count; the beat carrying the turn is ≥ 1,600 ms. Tonight the derived beat is 1,600 ms and nothing moves.

**2. `announce.mjs` — the assertion that was deleted tonight and called a repair.** The README, `still-dark/README.md:1071–1082`: *"A guard that goes quietly wrong on the night the work succeeds is the same failure as the `head -6`… Paid, and not by advancing the constant: the page publishes its own run… and the instrument derives its window."* The diagnosis is right and the repair is half a repair. **That stale `30000` was, by accident, the only assertion anywhere in this house that the run must fit inside thirty seconds.** It has been replaced by a follower: `WATCH_MS = __sdRun.done_ms + MARGIN_MS`. I ran it — **`WATCHED 32,118 ms (the run + 2,000 ms, derived, never typed)`, exit 0.** In 2027 it will patiently watch for four minutes and exit 0. From tonight, **no instrument in this work can ever go red for the run's length.** That is the textbook shape of an alibi: the alarm converted into a gauge, and the conversion published as the night's headline repair. **Testable:** `announce.mjs` already exits 3 when the page does not publish its run; give it an exit for *the run is longer than the work says it may be*. It is one comparison, and it is the guard cut 1 needs.

**3. `1600` exists twice, and the README says it exists once.** `README.md:1082`: *"The beat itself was a literal `1600` inside the run and is a named constant now, **so the number exists once in this work rather than twice.**"* Refuted by grep on the frozen tree: `index.html:3088` (`var BEAT_MS = 1600;`) and **`data.py:1674`** (`run_seconds = round((arrive["first_dwell_ms"] + (n_stops - 1) * 1600) / 1000)`). The second copy computes the only sentence that sets a visitor's expectation of the run — *"This figure runs by itself: eleven states over about thirty seconds. Any button above holds a state and stops the run."* Naming the literal did not remove the duplicate; it **moved** it, from `index.html` ↔ `announce.mjs` to `index.html` ↔ `data.py`. Banked failure 56 in a fourth costume, in the paragraph banking the third. Move the beat and the page runs one length while speaking another, silently, and every guard exits 0 — because `announce.mjs` reads `__sdRun` and no instrument in this work reads `run_states.waiting`. **Testable:** parse the seconds word out of `arrive.run_states.waiting` and assert it equals `round(__sdRun.done_ms / 1000)`. It holds tonight. Change either literal and it does not.

**4. `#sd-arrive-head-since`, second sentence — *"The last four, in darker ink, arrived with the list of 14 AUG."*** First, the correction that makes the cut: **in the unattended run the run's line does not move at any beat.** I put a MutationObserver on it across a 33-second run at 390×844 — **three writes, at 349 ms, 14,174 ms and 30,173 ms**, and nothing at the ten beats. `tools/turn.mjs` drives by clicking buttons, so it books `the run's line` at 16,571 px² / **27.7 %** at 390 and 17,068 px² / **21.4 %** at 1400 — motion that exists only under a finger, and the guard table publishes it. Take it out of turn.mjs's own totals and the performance every unattended visitor actually sees reads:

| at the turn, 390 px | px² | share |
|---|---|---|
| **the hole's heading** | **20,411** | **47.1 %** |
| the 4 names the beat adds | 10,119 | 23.4 % |
| the share, both ends | 5,007 | 11.6 % |
| the count that turns | 4,814 | 11.1 % |
| the two divisions | 2,982 | 6.9 % |

At 1400 px the heading is 26,333 of 62,647 — **42.0 %**. **The largest moving object in this work's climax is a two-sentence grey caption at 10.56 px, four times the share and four times the count that turns, at both widths.** Its second sentence is **5,267 px² at 390, two of the element's five line-boxes**, and it says in words what three things on the same screen already perform: the four chips *are* in darker ink, the button the run stands on reads `+10 DAYS`, and a held stop's line reads `Holding +10 DAYS`. Fourth printing of one fact. **What it does not buy, and I measured it so nobody has to guess: nothing.** I stripped it in the live DOM at all four viewports — the hole span and chip count are unchanged (390×844: 294 px / 24 of 35 before and after), because the heading's height is reserved by `reserve()` at `index.html:3199`. **This cut buys motion, not pixels.** **Testable:** rerun `turn.mjs` with the run played rather than clicked; the hole's heading must fall below the share at 1400.

**5. `tools/turn.mjs` measures a beat that only exists under a finger.** Above. It clicks the ladder, so it reports a node that never changes in the automatic run and omits nothing that does. This is the instrument built last session to refuse a staging prescription, and it is measuring the wrong performance — the one 0 % of unattended visitors see. **Testable:** let the run play; `#sd-arrive-state` must not appear in the report.

**6. `tools/frame.mjs:205` — `if (px > best.px)`, against its own comment eight lines above: *"among those, take the one showing most of the hole. Chips count only when a chip is wholly inside the viewport — a name cut in half is not a name a visitor read."*** The code maximises pixels and keeps the **first** tie; the comment promises the chip-maximising position. I walked every qualifying scroll position at all four viewports:

| viewport | tie band | frame.mjs's rule | its own comment | cost |
|---|---|---|---|---|
| 390×844 | 1 position | 294 px / **24** of 35 | 294 px / **24** | 0 |
| 844×390 | 1 position | 49 px / 12 | 49 px / 12 | 0 |
| **1400×600** | **132 positions (scrollY 15–146)** | **135 px / 31 of 35** | **135 px / 35 of 35** | **4 chips** |
| 1400×900 | 147 positions | 135 px / 35 | 135 px / 35 | 0 |

**The chip half of the floor — the half `DRAMATURG-93.md` proved had been met all along — is decided by a rule that does not maximise chips, and it is right at 390×844 tonight only because the tie band there happens to be one pixel wide.** Widen the band by a pixel of layout and the floor's enforced number becomes a first-tie draw. Banked failure 54 again, in the function written last session to end banked failure 54. **Testable:** prefer chips on a tie; 1400×600 must read 35 of 35.

**7. `tools/fold.mjs` published red — my ruling: honest about the fact, alibi about the ruler, and the ruler is now the sampling defect this house fixed one file away.** The fact is honest and I reproduce it: **143 failures, exit 1**, and it is one finding repeated — the controls off at seven of nine scroll positions and the run's line at six, at 390×844, on all eleven stops, `7 × 11 = 77` and `6 × 11 = 66`. **Zero occlusions at every stop and every position.** The README's derivation is correct tonight and was not last session; good. But the number is `13 × stops`: **120 at ten stops, 143 at eleven, 156 tomorrow, without one line of layout moving.** The house says so itself — *"this number rises by thirteen every time this work succeeds at what it does, and that is a fact about the instrument's ruler and not about the page's staging"* — and then prints it in the guard table's *"tonight, on this page"* cell as the reading. **An instrument whose author has written down that its ruler is wrong, and who publishes the reading anyway, has stopped being a guard.** Worse: `fold.mjs:78–80` still samples `round(range × k / 8)` — **nine positions over a range that grows with every list**, so the positions drift apart each night. That is precisely the grid whose step was set by document height, struck in `frame.mjs` last session as banked failure 54's third instance, alive in the sibling file. **Two ends, and I do not care which.** Floor what the house actually decided — the controls must be reachable from the position where the whole figure and the hole share a frame, which `frame.mjs` already finds by a 1 px walk — so the instrument can go green and can go red again; or drop the per-stop multiplication and report the two elements and the scroll band once, because that is the whole finding. **Testable either way: the reading must not change when a list arrives and no layout moves.**

---

## WHAT I LOOKED FOR AND DID NOT FIND

- **A broken first encounter.** At 390×844 the page opens on `4 AUGUST 2026`, *"one day of the sea, and how much of it was knowable on the day itself"*, the 56-word gloss, `100 %–100 %` at y=234, `11 of 11`, `0 of them certainly dark`, `11 of 230`, the controls at y=415–502, the run's line at 510–558, `IN THE LIST DATED 4 AUG — the eleven names it printed`, all eleven names, and the top of the hole's heading — **every one of them above an 844 px fold**, and then fourteen seconds of nothing. The stillness is still the best decision on the page. At 844×390 the frame holds at 235 of 390 and at scrollY 141 the figure, the eleven names, the hole's heading and the top of the hole stand in one 390 px frame. The terminal test passes on the first screen alone.
- **A landscape-phone defect.** I chased one. `frame.mjs` reports `49 px, 12 of 35 chips` at 844×390 and I read **0 chips at stops 1–5** — and it is an artefact of its own proxy, not of the staging: at that viewport the reserved height makes each `li` 158 px tall at three names and 20 px at thirty-five, so *"wholly inside"* stops standing for *"read"*. The names are legible. No cut. But two numbers computed by one rule that mean different things at different viewports should not sit in one guard cell — fold it into cut 6.
- **A defect in the twin division.** `11 of 11` is born at 14,118 ms — the loudest instant in the run — and then does not move for six beats while everything around it does. I went looking for a fault and it is the opposite: that is the ceiling *performing* its freeze, and it unfreezes on the first ship that becomes certain. The house built exactly what it was asked for. Leave it.
- **Slop.** None. No gradient, no icon, no emoji, no easing, no colour beyond ink and one grey, dark scheme clean at 320/390/480/844/1400/1920 with `rgb(13,13,13)` painted on `body` and **no sideways scroll at any width** (`width.mjs` CLEAN, 280→1920).
- **Presence.** Real and exact. Out-of-order 9→0→7→3→10→5, every state right including chip counts and the certain count. A press at t=2 s during the dwell: run dies, *"You stopped the run at +3 DAYS, 65 %–100 %. Press "run it again" to see it whole."* The eleven stops plus `run it again` are the first twelve tab stops, in order. `gaps.mjs` PASS/PASS. `announce.mjs` speaks three sentences and they carry the figures.
- **A weak ending.** `.sd-floor` is the last text in the document and nothing follows it: *"No number closes this. A method that counts a disappearance only when the ship comes back cannot see the ships that never come back. **Forty-six** is what this record can place in 4 August 2026, not what was on the sea that day."* Updated with the eleventh list. It is right.

**A measurement I could not take:** whether a capped, non-uniform beat still reads. No committed instrument varies the beat, and I will not fabricate a number for a run this object does not have. The house builds it or the house reasons it, and either way it does so before the ceiling is chosen — not after.

---

## WHAT I DROVE

A browser library's Chromium, launched by me, against the frozen file; inline read-only measurement only; one scratch capture of an instrument's stdout, outside the repository. Committed instruments, all run by me: `tools/frame.mjs` **exit 0, HOLDS at four viewports, hole 294 px / 24 of 35 — HOLDS**; `tools/width.mjs` **CLEAN**; `tools/turn.mjs` reproduced at both widths; `tools/fold.mjs` **exit 1, 143 failures, zero occlusions**; `gaps.mjs` **PASS/PASS**; `announce.mjs` **exit 0, 4 writes, 3 spoken, 12 figure rewrites, window 32,118 ms derived**. Read directly: `render-900.png`, `RENDERS.json` (`index_sha256` matches the committed file), `STATE-1.txt`, `README.md`, `data.py`, `PROJECT.md`, `DRAMATURG-88..93`. Not run, per the pass rules: `render.mjs`, `data.py --write`, `capture/capture.py`.

My own measurements tonight: the unattended run under MutationObservers on eleven nodes at 390×844 (83 mutations in 33 s, tabulated per beat); per-beat changed area at 390 and 1400 across all ten beats; the hole's heading split by text range at both widths; the shared-frame scan reproduced at four viewports with the tie band enumerated; the second sentence stripped in the live DOM and re-measured; the landscape-phone frame at every stop.

---

**index.html, sha256 at the START of this pass:**
`89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46`

**index.html, sha256 at the END of this pass:**
`89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46`

**The object did not move under me.** `HEAD` `f5c266a` at the start and at the end, working tree clean at both. Nothing in the repository was created, edited or deleted. I wrote nothing but this memo.
