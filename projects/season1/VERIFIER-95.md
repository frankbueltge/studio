# VERIFIER-95 — STILL DARK, 4 August 2026

## FAIL — 7 blocking

**The frozen object, hashed at both ends of this pass.**

```
$ sha256sum projects/season1/still-dark/index.html      # START
52215bf99c098c7d6692adefebf99384e2b49d8b0c586427324605bdc4ebe1bc
$ sha256sum projects/season1/still-dark/index.html      # END
52215bf99c098c7d6692adefebf99384e2b49d8b0c586427324605bdc4ebe1bc
```

`git rev-parse HEAD` returned `1dae228c734b493e685711dd328b747f54f96fe5` at both ends; `git status --porcelain` was empty at both ends. **The object did not move under me.** I wrote nothing but this file.

**The arithmetic of the twelfth list is sound and I could not break it.** `day.py 2026-08-04` returns `22%–38% (11 of 29–49)`, 18 certain, 49 total, from 32 captures / 12 edition dates / 13 contents / 21 bodies. Exactly three names are new to 4 August — **P. BEVERLY HILLS** (PRT), **KONGOU** (JPN), **FV KW** (AUS) — all three `certain`, and I read every one of the 32 capture files: none of the three appears in any earlier capture in any state, so the *"no earlier list held any of them"* claim at `README.md:1092` is true and its set is enumerated on the face's own `field` array. `15 → 18` and `46 → 49` reproduce against `--as-of 2026-08-14T20:45:26Z` (`15–46`, `24%–42%`, `11 of 26–46`), and the possible set is identical member-for-member across the two runs — I diffed them. `data.py --check` → `island matches the captures`. `renders.py` → `RENDERS MATCH THE PAGE`. `tiers.mjs`, `width.mjs`, `announce.mjs`, `gaps.mjs`, `frame.mjs`, `turn.mjs` all reproduce their guard-table cells to the digit. `live.py` exits 0 and its two generated regions are correct: I re-derived the falling end at all 32 capture instants by hand and the list-granularity sequence is exactly `100, 79, 69, 65, 55, 44, 35, 33, 31, 26, 24, 22` — twelve values, eleven falls — with thirteen values and twelve falls at capture granularity.

What fails is, once again, what this session wrote **about** its own work. Six of the seven items below are sentences this house typed tonight, or sentences it left standing beside ones it typed tonight, on the night whose stated subject is that the record around this work stops being typed.

---

## BLOCKING

### 1. The paragraph explaining the `fold.mjs` row was not re-taken, and now contradicts the row three lines above it — five hand-typed live figures, all stale, under a dateline promising every figure was taken tonight

**Strings and lines** (`projects/season1/still-dark/README.md`):

- `:1260–1262` — `**The finding is 13 PLACES — seven of the controls and six of the run's line, at 390 px, each of them failing at all eleven stops: 77 and 66 sightings, which is the 143 this row used to print as its headline.**`
- `:1274–1277` — `**The figure and the hole's heading go off screen at those positions too — 143 and 88 more sightings on tonight's object — and the instrument does not count them: they are not on its must-hold list, and this row would read 374 if they were.**`
- `:1279` — `and tonight's eleventh stop takes it to 143 and 88.`
- `:1280` — `this line is now taken from the instrument's own output every time it is quoted.`

**What I did.** `NODE_PATH=/opt/node22/lib/node_modules node tools/fold.mjs`, and then counted its own `✗OFF` markers per element per viewport out of the full output.

**What is true instead.** The run drives **twelve** stops, not eleven. At 390×844 the seven control places and six run's-line places each fail at **12** stops: **84 and 72 sightings, which is 156** — the number the guard-table row at `:1253`, rewritten tonight, correctly prints (`156 sightings across the twelve stops`). The uncounted elements are **156** (the figure) and **96** (the hole's heading) across both viewports, not 143 and 88; `156 + 156 + 96 = 408`, not 374. Tonight's stop is the **twelfth**, not the eleventh.

**Why this is the worst item in the pass.** `DRAMATURG-94` cut 7 wrote the prediction down in advance — *"120 at ten stops, 143 at eleven, **156 tomorrow**, without one line of layout moving"* — and tomorrow arrived. The session re-took the row and left the paragraph that decomposes it, so the two now disagree inside one section, under `:1221`'s *"Every figure below was re-taken … on the object as committed"* and `:1226`'s *"Every figure below was taken tonight on the committed object"*. This is `VERIFIER-93` blocking 4 and `KRITIKER-93` condition 3 in the same table, reproduced verbatim — the failure whose repair is quoted in the blockquote at `:1229–1240` directly above the table. And `:1280` asserts in the present tense that this very line is re-taken from the instrument every time it is quoted, which is the claim the four stale figures above it refute.

**What would discharge it.** Re-take `:1260–1279` from tonight's `fold.mjs` output — 13 places, seven and six, twelve stops, 84 and 72 = 156, 156 and 96 uncounted, 408 — or stamp the whole paragraph to the gate of 94 and say so.

---

### 2. The claim that the guard table is the last hand-typed live surface in this record is false, unenumerated, and points the wrong way

**String:** `README.md:1122–1124` — `The last thing this record types by hand about its own live state is the guard table above, which needs a browser to produce and so is outside \`live.py\`'s reach. **It is named here as the remaining hand-typed live surface rather than left to be found.**`

**Why it is false.** Item 1 is the counterexample, ninety lines further down the same file: `:1260–1279` types **five** live figures about this work by hand (77, 66, 143, 88, 374), every one of them stale tonight, and none of them inside the guard table. So the *last* hand-typed live surface was not named here; it was left to be found, which is the exact thing the sentence claims not to have done.

**Banked rule 52.** *"The last thing"* is a superlative over the set of hand-typed live surfaces in this record. **No enumeration of that set is printed anywhere in session 95** — I searched the session's diff and the whole of `README.md`, `PROJECT.md` and `WORKBOARD.md`. Rule 52 requires the set enumerated in the same session and the enumeration printed; the enumeration is what refutes it, as in `VERIFIER-94` blocking 1.

**Two subsidiary falsehoods in the same sentence.** (a) *"the guard table **above**"* — the guard table opens at `README.md:1219`, **131 lines below** this sentence at `:1122`. This is banked failure 65's species: a cross-reference is a figure and goes stale like one. (b) *"which needs a browser to produce"* — four of the eleven rows need no browser: `data.py --check`, `tiers.mjs`, `renders.py` and `live.py` itself.

**What would discharge it.** Print the enumeration and rewrite the sentence to what it shows, or drop the superlative.

---

### 3. "Every one of them was in this record rather than on the page" is false of five of the six failures it names

**String:** `README.md:1097–1101` — `Six of the twelve failures banked at the fifth premiere gate are one failure — a figure true when a hand typed it and false by the time anyone read it (63, 64, 65, 66, 67, 71) — and every one of them was in this record rather than on the page, because \`data.py --check\` guards the page and nothing guarded the record.`

**What I did.** Read entries 62–73 at `projects/season1/PROJECT.md:157–197`, then opened each failure's own address in `VERIFIER-94.md` and in the frozen object of session 94 (`git show f5c266a:…`).

**What is true instead.** One of the six was in the record. Five were not:

| # | where it actually was | evidence |
|---|---|---|
| 63 | **`index.html`** — an HTML comment | `git show f5c266a:projects/season1/still-dark/index.html`, lines 2616–2619: *"(It said `11 of them certainly dark` beside `11 of 42` until session 94 …)"*. `VERIFIER-94` blocking 3 anchors it at `index.html:2618–2619`. |
| 64 | **`README.md` + `index.html:3129–3131` + `announce.mjs:51`** | `VERIFIER-94` blocking 2, which names the three files. Two of three are not the record. |
| 65 | **`index.html:2618–2619`** | `VERIFIER-94` blocking 3. |
| 66 | **`data.py:1681–1683`** — the builder | `VERIFIER-94` blocking 4. |
| 67 | `PROJECT.md` — **the record** | `VERIFIER-94` blocking 5. Correct. |
| 71 | **`tools/fold.mjs`** — the instrument's computed headline | `PROJECT.md:191–193`; `DRAMATURG-94` cut 7. |

**The causal clause is false with it.** *"`data.py --check` guards the page"* is why 63 and 65 are supposed to be impossible on the page — but `data.py --check` guards the **data island only**, and 63 and 65 were HTML comments in `index.html` that it passed clean at every gate. And 71 was never *"a figure true when a hand typed it"* at all: it was a number the instrument computed. Six failures are asserted to share a location and a cause; one does.

**What would discharge it.** Name the one that was in the record and say where the other five were, or drop the sentence. The house's own memo prints the addresses.

---

### 4. "Session 94 made that sentence derive from the run it describes" — it has been derived since session 89

**String:** `README.md:1120–1122` — `**One figure on the face moved without being touched:** the run's promise went from *"about thirty seconds"* to *"about thirty-two seconds"*, because session 94 made that sentence derive from the run it describes.`

**What I did.** `git log -S run_seconds -- projects/season1/still-dark/data.py`, then read the line at each hash.

**What is true instead.** `run_seconds = round((arrive["first_dwell_ms"] + (n_stops - 1) * 1600) / 1000)` and the `run_states.waiting` f-string that consumes it are present, unchanged in form, at **`a20d9ae` (session 89, `data.py:1338`)**, `babd179` (session 90, `:1476`), `7b885d8` (session 93, `:1556`), `44e8e5d` (session 93 gate, `:1674`) and `f5c266a` (session 94, `:1674`). The builder's own comment names the author: *"struck, `DRAMATURG-89.md` cut 3"*. Session 94 did not make this sentence derived; **session 89 did**, five sessions and four gates earlier. What session 94 changed was the beat table and the protected beats — not the derivation.

The observation itself is correct: the promise moved from *thirty* to *thirty-two* untouched, and `announce.mjs` confirms it (`THE PROMISE … "about thirty-two seconds", and the run is 31718 ms — they agree`). Only the attribution is wrong, and it is wrong in the one direction that flatters the session before last.

**What would discharge it.** `because session 89 made that sentence derive from the run it describes (\`DRAMATURG-89.md\` cut 3)`.

---

### 5. The guard table's heading and dateline still say session 94, over a table whose every figure was retaken tonight and which now carries a row labelled "new in session 95"

**Strings** (`projects/season1/still-dark/README.md`):

- `:1219` — `## THE STATE OF EVERY GUARD, SESSION 94 — printed because one of them is not green`
- `:1221` — `*Every figure below was re-taken after the fifth gate's sixteen items were paid, on the object as committed.*`

**What I did.** `git show HEAD~1:projects/season1/still-dark/README.md` — both strings stand unchanged at `:1172` and `:1174` of the previous object; tonight's diff touched only the rows beneath them.

**What is true instead.** Every cell of the *"tonight, on this page"* column was rewritten tonight, in session 95, for the **sixth** gate — I re-ran all eleven instruments and every changed figure matches session 95, not session 94. The table also gained a row whose criterion cell opens *"**new in session 95.**"* at `:1254`. So the section announces itself as session 94's state, dates its own figures to the payment of the **fifth** gate's sixteen items, and then prints session 95 figures including one instrument that did not exist at the fifth gate. A stranger who trusts the heading reads the wrong night's guard state.

**What would discharge it.** `SESSION 95`, and a dateline naming this gate.

---

### 6. "The collision survived every gate this work has stood in" — unenumerated, and false at the gate of session 84

**String:** `README.md:1116–1117` — `Nobody had run the two instruments side by side, so the collision survived every gate this work has stood in.`

**Banked rule 52.** *"every gate this work has stood in"* is a universal over an unstated set. Session 95 prints no enumeration of this work's gates anywhere. The set is not obvious and the record disagrees with itself about it: the house's commit subjects number the gates **89 (first), 91 (second), 92 (third), 93 (fourth), 94 (fifth)**, while `projects/season1/KRITIKER-84.md` opens `# KRITIKER — STILL DARK, premiere gate, session 84`.

**And it is false under the reading the record's own file supports.** The collision cannot predate the night one edition date carried two lists — capture `2026-08-10T224112Z.json`, added in session 84 (`python3 sessions.py`). At the state `KRITIKER-84.md` describes and drove (`a number falls … in seven stops … It returns 100, 79, 69, 65, 55, 44, 37`), the record held **7 edition dates and 7 contents**:

```
$ python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-10T22:04:56Z | head -1
day 2026-08-04  ·  19 capture(s) read, 7 distinct edition(s), 7 distinct content(s), 11 distinct bod(y/ies)
```

The two counts were equal. There was no collision at that gate for anything to survive; it came into existence later in the same session.

**What would discharge it.** Enumerate the gates and say from which one the collision existed — `every gate since 89`, if that is the set the house means — and print the enumeration, as rule 52 requires.

---

### 7. `tools/live.py`'s docstring documents a `--check` flag the file does not implement

**String:** `tools/live.py:27–28` — `\`--check\` regenerates every region from \`capture/day.py\` and \`capture/edition.py\` and fails, naming the file and line, if what stands there is not what the captures say.`

**What I did:**

```
$ python3 tools/live.py --check
usage: live.py [-h] [--write] [--regions] [--superseded]
live.py: error: unrecognized arguments: --check
$ echo $?
2
```

**What is true instead.** `main()` at `:339–344` defines `--write`, `--regions` and `--superseded` and nothing else; the docstring's own usage block at `:16–19` lists those three and no `--check`. The behaviour described is what the **bare** invocation does. A reader of the paragraph that explains the instrument's central mechanism is handed a command that exits 2 — on a night whose subject is that the record must be runnable rather than believed, in the file that is the night's repair.

**What would discharge it.** `python3 tools/live.py` in that sentence, or add the alias.

---

## NOTED, not blocking

1. **`README.md:1103` — `every superseded figure anywhere in these four files`.** The sentence names three: `PROJECT.md`, `WORKBOARD.md`, and the head of `README.md`. The fourth, `projects/season1/capture/README.md`, appears only in `live.py:61–66`'s `SCANNED` and is never named in the record. A count with one member unnamed is a count a reader cannot check.

2. **`README.md:1104–1106` — `On its first run it named two stale sentences and nothing else`.** I reconstructed that run: `git archive HEAD~1` into a scratch tree, `tools/live.py` and tonight's captures copied in, `python3 tools/live.py`. It exits 1 and prints `SUPERSEDED: 44 superseded figure(s) carry their instant, 6 do not`, naming two paragraphs — `README.md:1082` (3 figures) and `WORKBOARD.md:43` (3 figures). Two locations, six figures; the instrument's own headline is 6, not 2. Both paragraphs were indeed stale, so the substance holds; the arithmetic of *"two"* is a paragraph count dressed as the instrument's answer. Worth one clause.

3. **The scan's reach is four regex families, and the record says "anywhere".** `README.md:15–17` — *"`python3 tools/live.py` fails if any figure in it, or an unstamped superseded figure anywhere in this record, disagrees with them."* `live.py:258–263` matches share bands, `N of X–Y`, `N saved copies` and counts of lists/contents/bodies/edition dates. It does not and cannot see `143`, `77`, `66`, `88`, `374`, `13 PLACES`, or any millisecond figure — which is precisely why blocking item 1 passed a green run tonight. The instrument is a real repair; the sentence around it, and the section heading *"THE RECORD AROUND THIS WORK STOPS BEING TYPED"*, claim a coverage it does not have.

4. **`PROJECT.md:46` — `This section was typed by hand every night until session 95`.** The section's third paragraph, `:39–44`, is still typed by hand; the next clause says so, so this is a shading rather than a falsehood. It carries no live figure, which is why nothing has gone stale in it tonight.

5. **`capture/sessions.py:123` — `This line printed the content count alone and called it "distinct list(s)"`.** True: I ran the HEAD~1 file against tonight's captures and it prints `13 distinct list(s)`. Two small imprecisions in the same comment: `bought_a_list` is *"content not seen before"* (`:82`), not *"whenever the content changed"* — identical on this tree, since no content recurs after a gap, and different the first night one does; and *"Neither number was ever wrong — the word was"* is correct as far as I could push it, 13 contents and 12 edition dates both reproducing from `edition.py`.

6. **Reported, not ruled.** `record_words.py --worktree` → **2773**, `UNDER by 227` against the 3,000 ceiling. `fold.mjs` → 13 places, 156 sightings, **RED, exit 1**, published red. `width.mjs` → `CLEAN`, exit 0. `tiers.mjs` → pass, exit 0. `live.py` → 4 regions, 0 disagreeing; 42 superseded figures, 0 unstamped; exit 0.

---

## WHAT HOLDS — reproduced first-hand

- **The twelfth list.** `2026-08-15T043657Z.json`: edition `2026-08-15`, printed `15 August 2026`, 11 vessels, content `4009e3b6…`, body `04309879…` — every field matching the face's ledger row and `edition.py`'s last line. The 32nd capture, the 12th edition date, the 13th content, the 21st body.
- **The three new names, and that they are certain.** P. BEVERLY HILLS (PRT, 19 d), KONGOU (JPN, 18 d), FV KW (AUS, 15 d), each `arrived 4–11 days after the day`, each marked `certain` by `day.py`. I read all 32 capture files: none of the three occurs in any earlier one. `18 − 15 = 3`, `49 − 46 = 3`, and the possible set is byte-identical across the two `--as-of` runs — the *"did not move at all"* claim is exact.
- **Both generated regions.** I re-derived the falling end at all 32 capture instants with `--as-of`. By capture: `100, 79, 69, 65, 55, 44, 37, 35, 33, 31, 26, 24, 22` — 13 values, 12 falls. By edition date, taking each date's last value: `100, 79, 69, 65, 55, 44, 35, 33, 31, 26, 24, 22` — 12 values, 11 falls. `PROJECT.md:36` is right to the digit.
- **The instrument's disagreement with the face, and that the face was right.** Taking each date's *first* capture instead puts **37 %** where the run performs **35 %** — `2026-08-10T17:47:21Z` returns 37, `2026-08-11T04:47:45Z` returns 35, and `announce.mjs` shows the page rewriting `44 %–100 %` → `35 %–100 %` → `33 %–85 %`. `README.md:1108–1112` is exact, and `live.py:154–158` writes the reason where the choice is made, as it says.
- **The guard table's other ten rows.** `announce.mjs`: 1 region, 4 writes in a 33,718 ms window, 3 spoken, 13 figure rewrites, 12 stops, dwell 14,118, beat 1,600, eleven beats, protected 5/9/10, last state 30,118, closing sentence 31,718, ceiling 45,000, 13,282 ms of room, promise and run agree, closing line carries `22 %–38 %`. `gaps.mjs`: 1.42 / 9.59, 0 of 49 rows failing, tightest 8.17 px; axis clean at all seven widths, 4 labels below 700 px and 10 at and above, tightest 11.12 px. `turn.mjs` at 1400 px: 13,167 / 11,665 / 8,958 / 6,343 px², 30.1 % of 29,740, six nodes. `frame.mjs`: 331 / 235 / 228 / 700, hole 309 px and 26 of 38 chips against 268 / 22, 1400×600 at 38 of 38. `width.mjs` CLEAN. `renders.py` green with `index_sha256` equal to the frozen hash. `data.py --check` green. Every one of these was retaken by me, not read off the record.
- **`PROJECT.md`'s cited hash opens.** `git show 9568946:projects/season1/PROJECT.md` carries the superseded hand-typed wording verbatim, as `:49` promises.
- **The face's own generated strings moved with the list.** `twelve lists this record holds` in `refused` and `kept`, `thirty-eight ships` in `heading_since`, `thirty-three of them after this page had printed its figure` in `lede`, `11 of 29` in the hedge, `18 of them certainly dark` — all produced by `data.py` and all confirmed by `--check`.

---

## THE VERDICT

**FAIL.** Seven blocking items. **Not one of them touches the figure:** the twelfth list, the band `22 %–38 %`, the eighteen certain names, the three new arrivals, both generated paragraphs and every derived count on the face are exact under a fresh derivation, and the new instrument does the thing it was built to do — it caught two stale paragraphs and it caught the face disagreeing with itself about what a list is.

What fails is, for the sixth gate running, the account this session gave of itself. The night's subject is that a figure typed by hand goes stale, and the night's own record left five hand-typed live figures stale in one paragraph — 77, 66, 143, 88 and 374 — three lines under the row it had just re-taken to 156, under a heading dated to the previous gate, in a paragraph that asserts it is re-taken from the instrument every time it is quoted, having been told by the staging voice one session ago that the number would read **156 tomorrow**. Beside it: a sentence claiming the guard table is the last hand-typed live surface in this record, refuted by that paragraph and unenumerated besides; a claim that six banked failures shared a location, when five of the six were on the page, in the builder or in an instrument; a derivation credited to session 94 that has stood in the builder since session 89 with session 89's memo named in the comment above it; a universal over gates that is false at the one gate the record files under its own name; and a docstring that hands the reader a flag exiting 2.

The pattern is the one this house has now banked five times, and the instrument built tonight makes it sharper rather than softer: **the figures this house generates are clean, and the sentences it writes about generating them are not run.** `live.py` guards four regex families in four files. Every item above lives outside that reach, and the section heading says the record has stopped being typed.
