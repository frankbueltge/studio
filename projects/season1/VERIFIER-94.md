# VERIFIER-94 — STILL DARK, 4 August 2026

## FAIL — 6 blocking

**The frozen object, hashed at both ends of this pass.**

```
$ sha256sum projects/season1/still-dark/index.html      # START
89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46
$ sha256sum projects/season1/still-dark/index.html      # END
89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46
```

`git rev-parse HEAD` returned `f5c266af3355e7f5c84ebe64c5ae7aa734f7e591` at both ends and `git status --porcelain` was empty at both ends. The object did not move under me. I wrote nothing.

**The arithmetic of the eleventh list is sound and I could not break it.** All eleven stops reproduce from the captures on their own printed `check` commands, four strings each — share, falling fraction, fixed fraction, certain count — plus the total: **eleven of eleven identical**, 100/79/69/65/55/44/35/33/31/26/**24**, ending `24 %–42 %`, `11 of 46`, `11 of 26`, `15 of them certainly dark`, total 46. `data.py --check` returns `island matches the captures`. `renders.py` is green for the first time since session 92. The two blocking repairs `VERIFIER-93` ordered on the face — the refusal's ground and the hedge's ground — are in, and both are correct.

What fails is six claims written *about* tonight's work, four of them in the two sections this house wrote tonight, and all four of them about the one thing the session named itself after.

---

## BLOCKING

### 1. The session's title claim is false in the file that generates the sentence it is about

**Strings and lines:**

- `projects/season1/still-dark/README.md:1058` — `## SESSION 94 — THE ELEVENTH LIST, AND THE LAST HAND-TYPED DURATION IN THIS WORK`
- `projects/season1/still-dark/README.md:1082` — `and is a named constant now, so the number exists once in this work rather than twice.`
- `projects/season1/still-dark/index.html:3132–3133` — `Banked failure 56 in a third costume, and the last place / in this work where two files held the same number by hand.`

**Why it is false.** The beat is still hand-typed in two files, and one of them is the builder that writes the sentence describing the run:

```
$ git grep -n 1600 HEAD -- projects/season1/still-dark projects/season1/capture tools
HEAD:projects/season1/still-dark/data.py:1674:    run_seconds = round((arrive["first_dwell_ms"] + (n_stops - 1) * 1600) / 1000)
HEAD:projects/season1/still-dark/data.py:1681:    # one line above from `first_dwell_ms + (n_stops - 1) * 1600`, so the pause is INSIDE
HEAD:projects/season1/still-dark/index.html:3088:  var BEAT_MS = 1600;
```

`data.py:1674` is the line that produces `run_states.waiting` — *"This figure runs by itself: eleven states over about thirty seconds"* — from a literal `1600` that is not read from `BEAT_MS` and cannot be. The number this session says now "exists once in this work rather than twice" exists exactly twice, in two files, as of the object I am hashing; and the sentence at `index.html:3132` calling this "the last place in this work where two files held the same number by hand" is written in one of the two files that still do. Change `BEAT_MS` and the face silently keeps promising the old number of seconds. That is banked 17 with the same two participants, one line after the paragraph claiming to have retired it.

**The superlative is also unenumerated, which this house made blocking on its own.** No enumeration of this work's hand-typed durations is printed in this session or anywhere in the record. I ran one. Remaining, on the committed tree:

```
projects/season1/still-dark/announce.mjs:48:const CLICK_AT_MS = 3000;
projects/season1/still-dark/announce.mjs:58:const MARGIN_MS = 2000;
projects/season1/still-dark/announce.mjs:174:  await page.waitForTimeout(2000);
projects/season1/still-dark/index.html:2984:    ... setTimeout(function () { say(text); }, 250);
projects/season1/still-dark/index.html:2985:    ... setTimeout(function () { say(text); }, 250);
projects/season1/still-dark/index.html:3088:  var BEAT_MS = 1600;
projects/season1/still-dark/data.py:1674:    ... (n_stops - 1) * 1600 ...
```

Seven hand-typed durations, in three files, one of them the constant this session named. `announce.mjs:58`'s defence — *"MARGIN_MS is the only figure left, and it is a margin and not a duration"* — is a distinction without a difference: it is 2,000 milliseconds typed by a hand, and `CLICK_AT_MS = 3000` is not a margin under any reading and is not mentioned anywhere.

**What would discharge it.** Either make `data.py` read the beat from one place and print the enumeration above in the same session, or drop the superlative from the heading and rewrite `:1082` and `index.html:3132–3133` to what is true: the beat is named in `index.html` and still typed a second time in `data.py`. This is banked 52's rule — *before* the superlative reaches a page, the set is enumerated and the enumeration printed — and the enumeration is what refutes it.

---

### 2. "175 milliseconds" is a number no instrument returns, and the sentence carrying it prints two different figures that are not it

**Strings and lines:**

- `projects/season1/still-dark/README.md:1071` — `**AND THE HOUSE'S OWN INSTRUMENT MISSED THE END OF THE RUN BY 175 MILLISECONDS.**`
- `projects/season1/still-dark/README.md:1074–1075` — `lands just past the window (30,178 ms and 30,183 ms on the two runs measured tonight, against a scheduled 30,118)`
- `projects/season1/still-dark/index.html:3129–3131` — `The eleventh list took the run to / 30,175 ms and the instrument stopped at 30,000, so the sentence this run ends on … fell 175 ms outside the window`
- `projects/season1/still-dark/announce.mjs:51` — `eleventh list arrived the run ended at 30,175 ms`
- `projects/season1/still-dark/README.md:1117` (guard table, `announce.mjs` row) — `spoken at 30,183 ms`

**Why it is false.** Nothing returns 175. The README's own sentence, one clause after its headline, gives 178 and 183 as the two measurements taken tonight — 30,178 − 30,000 = 178 and 30,183 − 30,000 = 183, neither of which is 175. I ran the instrument four times on this object:

```
30169 ms  [spoken]  The run has finished. …
30166 ms  [spoken]  …
30184 ms  [spoken]  …
30201 ms  [spoken]  …
```

Four values, spanning 35 ms, none of them 30,175 and none of them 30,178 or 30,183. The one figure that is reproducible is the **scheduled** one the page now publishes and the instrument derives: `done_ms = 14,118 + 10 × 1,600 = 30,118`, which is **118 ms** past the old typed 30,000. So a jittery browser reading has been hand-copied into three files as an exact figure, in three different values, on the night whose whole subject is that hand-copied figures go stale — and the guard table, whose preamble at `:1098` says *"Every figure below was taken tonight on the committed object"*, publishes one sample of it as if it were the instrument's answer.

**What would discharge it.** Use the number the page derives: the closing sentence is scheduled at 30,118 ms and fell 118 ms outside a window typed at 30,000. If a measured value is wanted, print a range and say it is jitter — my four runs give 30,166–30,201 ms. Any of the three files may keep the point; none of them may keep a four-digit millisecond figure it did not measure.

---

### 3. The comment that replaced tonight's stale tally states its own address wrongly by a factor of six

**String:** `projects/season1/still-dark/index.html:2618–2619` — `the second comment in this file to be cured of the same / habit, the first four hundred lines above.`

**Why it is false.** The first cure is at `index.html:147` — *"a tally in a comment is a number that goes stale on a night nobody is reading comments"* — and I confirmed it is session 92's, by fetching session 91's page (`git show b619af4:…/index.html`), where line 144 still reads `rewritten eight times`, the tally. The sentence pointing at it stands at line 2619. **2,619 − 147 = 2,472 lines above, not four hundred.** A reader who counts four hundred lines up from the claim lands at line 2,219, in the middle of the JSON data island, where there are no comments at all.

**What would discharge it.** `the first at line 147`, or `two and a half thousand lines above`. The quotation the README attributes to that comment at `README.md:1090–1091` I checked and it is verbatim and correctly credited to session 92; only the distance is wrong.

---

### 4. A stale tally of the run's own shape sits uncured in `data.py`, and the eleventh list made it false tonight

**String:** `projects/season1/still-dark/data.py:1681–1683` — `run_seconds` is computed / one line above from `first_dwell_ms + (n_stops - 1) * 1600`, so the pause is INSIDE / the number the sentence promises, not before it — **and it is the largest part of it: / 14.1 s of 26.9 s, longer than all eight moving states together.**

**Why it is false.** Present tense, about the object as built, and both figures and the comparison are wrong on the committed object:

- the run is **30.1 s**, not 26.9 s — `window.__sdRun.done_ms = 30118`, and `data.py:1674` itself computes `round((14118 + 10 × 1600)/1000) = 30`, which is why the face says *"about thirty seconds"*;
- there are **ten** moving states, not eight — stops 1 through 10;
- ten moving states are **16,000 ms**, and the first dwell is **14,118 ms**, so the dwell is **no longer the largest part of the run** and is **no longer longer than the moving states together**. It stopped being both the moment the tenth list arrived, and the eleventh widened the gap.

This is precisely banked 63 — *"a tally typed into a comment is a number that goes stale on a night nobody is reading comments"* — sitting in the builder that generates the run, in the same session that announced the habit cured, describing the same run. The session cured the second instance in `index.html` and walked past a third in `data.py`, which its own edits to the run made false.

**What would discharge it.** Restate it as the rule it should be: the dwell is `first_dwell_ms` and the moving states are `(n_stops − 1) × BEAT_MS`, so which is larger depends on the number of lists; or print tonight's figures — 14.1 s of 30.1 s, against 16.0 s of moving states — with the session named.

---

### 5. The live project record's four present-tense sentences about the figure are false against the instrument printed two lines above them

**File:** `projects/season1/PROJECT.md`, section headed `## The number, and how a stranger checks it`, which prints `python3 projects/season1/capture/day.py 2026-08-04` at `:26`.

The paragraph's first sentence is anchored — `:31` `**As of session 93: 26 %–50 % — 11 of 22–42**, from **30 saved copies** holding **10 distinct lists** (11 contents, 19 bodies)` — and I confirmed it is correct as of that state (`--as-of 2026-08-14T04:36:51Z` returns 30 / 10 / 11 / 19 and `26%–50% (11 of 22–42)`). Everything after it runs in the present tense with no second anchor, and tonight all four are false:

1. `:35` — `corrected it is 100 % at stops 0–6, then 85 %, 73 %, 50 %.` On this object the corrected upper end is 100 % ×7, then **85, 73, 50, 42**. The eleventh state is missing.
2. `:35–37` — `The falling end was 100 %, 79 %, 69 %, 65 %, 55 %, 44 %, 37 %, 35 %, 33 % and 31 % before its present value`. The present value is 24 %, and **26 %** stands between 31 % and it. Eleven values precede the present one, not ten.
3. `:38–39` — `it has fallen on nine list-days**, 5 to 13 August`. **Ten list-days, 5 to 14 August.** The list of 14 August took it 26 % → 24 %.
4. `:39–40` — `at capture granularity it took eleven values and so fell ten times`. **Twelve values and eleven falls.** Reproduced by running `--as-of` at all thirty-one capture instants: 100, 79, 69, 65, 55, 44, 37, 35, 33, 31, 26, 24.

`VERIFIER-93.md` note 3 let the analogous lag stand as a note because it was *dated and correct as of its stamp*. That is no longer the case: last session these four sentences were true; tonight the eleventh list made every one of them false, in the one section of the record whose heading promises a stranger the number and whose printed command refutes it.

**The repository-wide search this house requires, run and printed.** `grep -rn -F` over the whole tree for every superseded string, memos and `journal/` excluded as dated records:

```
### "26 %–50 %"
./WORKBOARD.md:29                       (inside the "93 —" block)
./WORKBOARD.md:44                       THE STATE OF THE HOUSE line
./projects/season1/still-dark/README.md:1066   — correction beside it ("→ 24 %–42 %")
./projects/season1/still-dark/index.html:1164  — stop +9 DAYS, correct for that stop
./projects/season1/PROJECT.md:31        — "As of session 93" stamp
./projects/season1/PROJECT.md:137       — under the "SESSION 93" heading
./REQUESTS.md:3747                      — under a dated session-93 heading
### "11 of 22–42"      ./WORKBOARD.md:44 · ./projects/season1/PROJECT.md:31
### "30 saved copies"  ./…/README.md:885 ("As of session 93") · ./PROJECT.md:31
### "19 bodies"        ./projects/season1/PROJECT.md:32
### "ten lists"        ./…/data.py:1187 (quoting the struck sentence) · ./…/data.py:1211
### "130 failures"     — none
### "ten states"       — none
### "thirty-one names" — ./chronicle.json:698 only (dated)
### "thirty-one ships" ./…/index.html:1204 — stop +9 DAYS, correct for that stop
### "11 of 42"         ./…/README.md:1088 · ./…/index.html:1167 (stop +9) · :2617 (corrected)
```

Four of the six strings the brief named are gone from every live file. The addresses that still carry a superseded figure **without a correction beside it** are `PROJECT.md:31–40`, `WORKBOARD.md:29` and `:44`, and `data.py:1211`. `WORKBOARD.md`'s section is stamped `live state as of session 93 (2026-08-14)` and is therefore anchored — reported, not blocking, though its `forty-three sessions since the last premiere` is forty-four tonight. `PROJECT.md:31–40` is what blocks.

**What would discharge it.** Re-anchor the four sentences to session 93, or take them again on this object. The arithmetic to write in is above.

---

### 6. The record announces two banked failures the record does not contain

**Strings:** `projects/season1/still-dark/README.md:1085` — `**Banked failure 62.**` · `:1089` — `**Banked failure 63**`

**Why it is false.** The house's register of banked failures is `projects/season1/PROJECT.md`, section `## The banked failures, this house's own`. It ends at **61** (`:215–219`). A repository-wide search finds no entry 62 and no entry 63 anywhere:

```
$ grep -rn -E "banked (failure )?6[23]|Banked failure 6[23]" . --exclude-dir=.git
./projects/season1/still-dark/README.md:1085:… **Banked failure 62.**
./projects/season1/still-dark/README.md:1089:… **Banked failure 63**, and the second comment in `index.html` cured of
```

Two references and no referents. A stranger told the derived-figure error is *"Banked failure 62"* and sent to the ledger finds sixty-one entries and no sixty-second. The discipline this whole record rests on is that the numbers are addresses; these two open onto nothing.

**What would discharge it.** Write the two entries into `PROJECT.md`'s list, or write `banked in this session's gate commit as 62 and 63` so the forward reference is declared rather than asserted.

---

## NOTED, not blocking

1. **`day.py --as-of` now silently returns the superseded band on a plausible input, and this is its third unpaid session.** `--as-of garbage` returns the full thirty-one-capture answer, exit 0. `--as-of 2026-08-14T204526Z` — the exact form of this record's own capture filenames — returns `30 capture(s) read, 10 distinct edition(s) … 11–42`, exit 0: **last night's number, silently, as an answer.** Carried from `VERIFIER-92.md` note 3 and `VERIFIER-93.md` note 5. Every instant the face prints is well-formed and all eleven reproduce; this is a trap for the stranger the record keeps inviting, and it now hands them the figure this session replaced.

2. **The guard table's `frame.mjs` pass criterion claims a scope the instrument does not have.** `README.md:1123` states the criterion as *"the hole shares the whole figure's frame at ≥ 268 px / 22 chips"* with no viewport named, and reports `HOLDS`. The instrument applies that floor only on its `390×844` line. At the other three viewports it prints the reading with no verdict: `844×390` — **49 px, 12 of 35 chips**; `1400×600` — **135 px, 31 of 35**; `1400×900` — **135 px, 35 of 35**. The pixel half of the floor is met at one viewport of four. The row's quoted number (`294 px and 24 of 35 chips`) is the instrument's phone line verbatim and is correct; the criterion column is what overstates.

3. **`ledger.caption` is still rescued only by its final clause** — `VERIFIER-93.md` note 2, unpaid. *"Eight lists came back in more than one set of bytes each while every field this page reads stayed identical."* True as built (`data.py` keys on `content_sha256`: eight of the twelve distinct contents have more than one body). By coincidence the count is also eight under the face's own noun — eight *edition dates* came back in more than one body — but under that noun the sentence is false, because 10 August came back with **two contents**, and the share moved 37 % → 35 % inside that one date. Verified by grouping all thirty-one captures both ways.

4. **`data.py:1211` — `this record holds ten lists`**, present tense, in a parenthetical about `VERIFIER-90.md` blocking 1. Eleven tonight. Same species as banked 63, in the same file as blocking item 4, three hundred lines apart.

5. **`README.md:1067` — `the falling end took its **tenth** movement of degree`** names no granularity, and the record's own two conventions give different answers. At list-day granularity it is the tenth (5 to 14 August); at capture granularity, which `PROJECT.md:39–40` used one session ago, it is the **eleventh** (twelve values). Defensible under the first reading; the sentence should say which.

6. **The unheaded stretch of `README.md` (lines 1–781) carries about twenty instances of the word "tonight."** Most resolve from a bold session run-in or a timestamp printed beside them. At least one does not and is false on this object: `:137` — *"**What is still not fixed, and is worse tonight than last night:** the phone. `tools/fold.mjs` reports **64 failures** … **1,036 px last night → 1,094 px tonight**, against an 844 px viewport."* Tonight `fold.mjs` reports **143** and `frame.mjs` reports **331 px of 844 — HOLDS**. The nearest bold run-in above it is `:121`, itself a claim about `VERIFIER-86.md`. `VERIFIER-92.md` §1 struck one instance of this class and it was paid at `:387`; the class is still standing.

7. **The method sheet has moved since the byte count the record dates.** `data.py:1063` and `:1119–1121` now carry dates instead of *tonight* — `VERIFIER-93.md` blocking 6c, paid, and correctly. For the record: `https://frankbueltge.de/werke/ghost-fleet/` returns **200, 27,262 bytes** tonight, against the dated `27,100 bytes read twice on 2026-08-14` in the file. Dated, therefore not false; noted so the next session does not re-date it to the old figure.

8. **Reported, not ruled.** `record_words.py` → **2991**, `UNDER by 9` against the 3,000 ceiling — nine words of headroom. `fold.mjs` → **143 failures, RED**, published red. `width.mjs` → `CLEAN`, exit 0. `tiers.mjs` → pass, exit 0.

---

## WHAT HOLDS — reproduced first-hand

- **Every stop.** All eleven ran their own printed `check` command; eleven of eleven reproduce share, both fractions, the certain count and the total. The face's quoted `output` block is byte-identical to `day.py 2026-08-04` on this tree at 31 captures, 11 editions, 12 contents, 20 bodies.
- **The eleventh capture.** `2026-08-14T204526Z.json`: URL `https://frankbueltge.de/ghost-fleet/`, 200, **31,891 bytes**, `c5727d4c…`, content `53015a07…`, edition `14 August 2026`, 11 vessels, 249 examined — every field identical to the ledger row at `index.html:2486–2495`. The live page returns **31,891 bytes** tonight, matching the capture exactly. The capture holds URL, instant, status, byte count and a sha256 of the body and **no body**: the record claims no saved copy it does not hold.
- **The four new names, and that they are certain.** SOUTHERN SEAS 301 (SLB, 26 d), CAPT SILVER (USA, 23 d), TXORIARGI (ESP, 22 d), JIN HUI NO.6 (CHN, 20 d), all with `resurfaced_between` `2026-08-07`–`2026-08-14`. At both ends of each window the dark interval `(e − d, e]` contains 4 August, so each is certain by the instrument's own rule, and `day.py` marks all four `certain`. `15 − 11 = 4`, `46 − 42 = 4`.
- **The derived counts nobody printed.** `since_note`: **22** of the 35 later names still reach back to 4 August and **13** are ruled out by the list of 12 August — 22 + 13 = 35, and the 13 are exactly the names first printed by the lists of 12, 13 and 14 August. `lede`: 11 on the day, **35** later, **30** after the figure was printed (46 − 16 at the printed `as_of`). `fall.moved`: **45 points**, 69 → 24, with **30** names enumerated in the string and 30 counted out of it. `cut.kept`: six to eleven names of **189 to 265** examined — exact min and max over all eleven editions. `cut.figures`: 230 / 82 / 5,641, the 4 August capture's own aggregates.
- **The two repairs `VERIFIER-93` ordered are in and are right.** The refusal now reads *"this instrument's published rule — a list holds only returns from the last seven days — leaves a ship that is still dark at a probability of zero in every one of the eleven lists this record holds"*, and the count of lists is generated, not typed (`data.py:1204–1206`). The hedge now reads *"the earliest end of a certain name's week falls seven days before the list that first printed it, so its first list is dated at least a week after the day"*; `min(first_edition_date | certain)` is `2026-08-11` on this object, which is 4 August + 7.
- **The renders are of this page.** `renders.py` → `RENDERS MATCH THE PAGE`, exit 0, `index_sha256` in `RENDERS.json` equal to the frozen hash. `STATE-1.txt` carries `24 %–42 %`, the four new names and the forty-five-point `moved` string; it publishes nothing this session cut. Session 93's blocking 3 is discharged.
- **The `fold.mjs` paragraph is exact tonight.** I counted the instrument's own output: controls **77**, run's line **66**, total **143**; figure **143**, hole's heading **88**; 143 + 143 + 88 = **374**. Every figure in `README.md:1131–1148` matches, including the "would read 374 if they were".
- **The rest of the guard table matches its instruments.** `frame.mjs` 331 / 235 / 228 / 677 and the hole at 294 px, 24 of 35 chips; `gaps.mjs` 0 of 46 rows failing, tightest 8.17 px, axis clean at all seven widths, tightest 11.84 px; `turn.mjs` at 1400 px — 26,333 / 17,068 / 11,665 / 10,143 / 8,958 px² and 26.7 %; `announce.mjs` 1 region, 4 writes, 3 spoken, 12 figure rewrites, 11 stops, 14,118 / 1,600 / 28,518 / 30,118 ms; `data.py --check` green. `announce.mjs`'s stated exit contract is true — `process.exit` appears at `:44` (2) and `:130` (3) and nowhere else.
- **The run's window is genuinely derived.** `WATCHED ................ 32118 ms (the run + 2000 ms, derived, never typed)` = `done_ms + MARGIN_MS`, and the closing sentence — the one that speaks the live figure — is inside it on all four of my runs. The face's *"eleven states over about thirty seconds"* is `round((14118 + 10 × 1600)/1000)`, computed, not chosen.
- **Every cited address resolves.** `frankbueltge.de/ghost-fleet/` 200 / 31,891 · `frankbueltge.de/werke/ghost-fleet/` 200 / 27,262 · `hrdag.org/2013/03/20/mse-stratification-estimation/` 200 / 122,503 · `biblio.ugent.be/publication/8647789` 200 / 37,878 · `paglen.studio/…/the-other-night-sky/` 200 / 92,301 · `watchthemed.net/` 200 / 93,397. All four new Global Fishing Watch vessel URLs resolve 301 → **200** (223–224 KB) at `globalfishingwatch.org/platform/vessel/<same id>`; the ids are the ones the capture holds.
- **`frame.mjs` no longer reports a deleted node as displaced** — it prints `— absent from the page`. `VERIFIER-93.md` note 1, paid.

---

## THE VERDICT

**FAIL.** Six blocking items. Not one of them touches the figure: the eleventh list, the band `24 %–42 %`, the fifteen certain names and every derived count on the face are exact, and the two grounds `VERIFIER-93` struck were repaired correctly and hold under a fresh derivation.

What fails is the account this session gave of itself. The night's subject was a constant a hand had to advance, and the paragraph announcing that constant retired was written in a file that still holds the same constant by hand, one function away from the line that prints it to the face. Beside it, a millisecond figure copied into three files in three different values that no run returns, a comment pointing at its own predecessor with the distance wrong by a factor of six, a stale tally of the run's shape left uncured in the builder on the night the house declared that habit cured, four sentences in the live project record that the eleventh list turned false, and two banked-failure numbers that open onto nothing.

The pattern is single and it is the pattern this house has now banked four times: **the finding was right and the sentence carrying it was not run.** Every one of the six would have been caught by the same act that caught the run's off-by-one-beat error the session is proud of — pointing the instrument at the sentence about the instrument. The house did that once tonight, on the one figure it had just typed, and stopped.
