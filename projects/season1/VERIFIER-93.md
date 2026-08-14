# VERIFIER-93 — STILL DARK, 4 August 2026

## FAIL — 6 blocking

**The frozen object, hashed at both ends of this pass.**

```
$ sha256sum projects/season1/still-dark/index.html      # START
73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9
$ sha256sum projects/season1/still-dark/index.html      # END
73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9
```

`HEAD` `7b885d8a2b06ba0a8fe379ab0160ed3864a4abb1`, `git status --porcelain` empty at both ends. The object did not move under me and I wrote nothing.

**The arithmetic is sound and I could not break it.** All ten stops reproduce from the captures on their own printed `--as-of` commands; `data.py --check` returns `island matches the captures`; the face's quoted `day.py` output is byte-identical to a fresh run; all four distinct cited hosts answer 200 and every quotation I could extract from a source page is verbatim. The disjointness the house asked me to rule on **is true, and true in general, not only tonight** — I proved it at all thirty stops and from the instrument's own construction.

What fails is six sentences written *about* those numbers, four of them written tonight, and one guard that is red on the committed object and was reported green.

---

## BLOCKING

### 1. The refusal's remaining reason is not supported by the page it cites, and that page contradicts it

**String:** `It needs a capture probability behind each ship, and a ship that is still dark stands in none of the ten lists this record holds. That is why this page prints a band and no estimate.`
**File/line:** `projects/season1/still-dark/index.html:804` (`arrive.cut.refused`), generated at `projects/season1/still-dark/data.py:1094–1105`. Marked SOURCED against `https://hrdag.org/2013/03/20/mse-stratification-estimation/` by `index.html:805–808`.

**Why it is false.** I fetched that page first-hand tonight (200, 122,503 bytes) and read it whole. Standing in none of the lists is not what stops MSE — **it is MSE's estimand.** The page's own Q14 sets out the model this house is refusing:

> "The (log of the) expected cell count m000 is a function of the other observed cell counts… The total number of cases is the sum of the observed cases (that is, the seven values of m) plus e^a."

`m000` is by definition the cases in *no* list. The sentence one line above it on the face already says as much — *"which reads the overlaps between several incomplete lists to say how many none of them caught"* — so the face now gives, as the reason the method cannot be used, the exact thing the previous sentence says the method is for. And on "needs a capture probability behind each ship", the cited page says the opposite of a requirement:

> "the two final assumptions—equal catchability and list independence—are unnecessary for MSE analyses with >=3 datasets, because both individual differences in catchability and dependence between lists can be parameterized and modeled."

Its only qualification is one of practice, not of possibility: *"it is not always practically feasible to model both capture probability and list dependences."* A stranger who follows the address printed beside the claim is handed the claim's refutation. **This is `VERIFIER-90.md` blocking 1 recurring in a new costume** — that pass struck the same block for resting on a two-list assumption the same page scopes away, and tonight's compression re-broke it by deleting the clause that was doing the work.

**What the true statement is, and this house already owns it.** The superseded 164-word string said it: *"a ship enters an edition only once its return has fallen inside that edition's seven-day window, so a ship that is still dark stands in no list, **at no probability**, in all ten of them."* `still-dark/README.md:1003–1005` still says it. The point is not absence from the lists; it is that entry is governed by a **published deterministic rule** — *"Daily. Window: disabling events that ended in the last 7 days (complete vanish-and-return stories)"*, which I re-fetched verbatim from the method sheet tonight (200, 27,100 bytes) — so a still-dark ship's capture probability is exactly **zero in every list, by rule and not by sampling**, and a class with a structural zero in every system is not estimable. That claim the cited page does not contradict. Four words were cut and the argument went with them.

**Smallest repair,** inside the cut's word budget: `It needs a capture probability behind each ship, and this instrument's published rule — a list holds only returns from the last seven days — gives a ship that is still dark a probability of zero in every one of the ten lists this record holds.` **I checked my own repair:** the window rule is quoted verbatim from the sheet I fetched tonight and already stands in the island under `method.window_quote`; and zero-in-every-system is the one condition under which `m000` is not identifiable, which is the only ground the cited page leaves standing.

---

### 2. The new clause in `hedge` states a true conclusion on a false ground, and the record refutes the ground in the same run

**String:** `And no ship this record could name on the day itself is ever among the certain: to stand in a list dated that day it had to be back, and to be certain it had to be dark.`
**File/line:** `projects/season1/still-dark/index.html:877, 910, 939, 964, 997, 1038, 1083, 1112, 1141, 1190` (all ten stops), generated at `projects/season1/still-dark/data.py:735–742`.

**The head clause is true, and true in general.** I re-derived it two ways and it is not a fact about tonight:

- **Empirically, at every stop.** I ran `day.py 2026-08-04 --as-of <t> --json` at all thirty capture instants and intersected `certain` with `{first_edition_date ≤ 2026-08-04}`. Empty at all thirty. Where `certain` is non-empty (captures 23–30), `min(first_edition_date | certain) = 2026-08-11` at every one.
- **By construction, for any day and any capture set.** `day.py:analyse` marks a vessel `certain` only when *every* end in its band `[ed−7, ed]` leaves it dark on T, which forces `ed−7 ≥ T`, i.e. `ed ≥ T+7`. `knowable_observed` requires `first_edition_date ≤ T`. `T+7 ≤ ed ≤ T` is unsatisfiable. The disjointness is unconditional, for any window length > 0, at every past and future stop.

**Why the printed ground is false.** The colon clause asserts that being *back* and being *dark* are incompatible. Under this record's own instrument they are not. `day.py:analyse` takes the dark interval under an end `e` to be `(e−d, e]` — **inclusive of `e`** — so a ship whose event ended on 4 August is both back on 4 August and dark on 4 August. The record prints exactly such ships: `day.py 2026-08-04 --as-of 2026-08-06T08:36:39Z` returns

```
possible TUNAMAR              PAN   56 d dark  arrived 0–0 days after the day
possible MICRONESIA103        FSM   39 d dark  arrived 0–0 days after the day
```

TUNAMAR's *only* feasible end is 4 August: its single route to being dark on the day is having come back on the day. It stands in the list dated 4 August and it is counted among the 42. Read the other way — *dark* meaning *still dark, not back* — the clause is false again, and more simply: all eleven certain ships **are** back, since coming back is the only way any ship reaches any list. Under both readings the ground fails while the conclusion holds.

**The real ground, which is stronger and shorter than the one printed:** a name is certain only if every end of its week-wide window leaves it dark on the day, and the earliest of those ends is *seven days before* the list that first printed it — so a certain name's first list is dated at least a week after the day, and can never be a list dated on or before it.

**Smallest repair:** `…: a name is certain only when every end of its week-wide window leaves it dark on this day, and the earliest of those ends falls seven days before the list that first printed it — so its first list is dated at least a week after the day.` **I checked my own repair** against the thirty-stop run above: `min(first_edition_date | certain) = 2026-08-11 = 4 August + 7` at every stop, with no exception.

**A note on the house's own proof, because it is why the false ground was written.** The verification relayed with this brief reads *"every certain vessel's earliest possible return end is 2026-08-11."* **That is not true.** From tonight's `--json`: `PANOFI FORE RUNNER` and `HEATHER LYNN` carry `resurfaced_between: ["2026-08-04", "2026-08-11"]` — their earliest possible return end is **4 August itself**, the day. What is 2026-08-11 is the earliest **first_edition_date**. The invariant lives on the date of the list, not on the date of the return, and a house that believes it lives on the return will write precisely the sentence at `index.html:877`. Banked failure 51's rule, again: the finding was right and the wording taken with it was not checked.

---

### 3. The committed renders and the screen-reader record were made from a different page — and this exact failure is already banked in the work's own README

**File:** `projects/season1/still-dark/RENDERS.json`, `STATE-1.txt`, `render-1400.png`, `render-900.png`.

```
$ python3 tools/renders.py ; echo EXIT=$?
projects/season1/still-dark
  index.html         73190c512c42…  STALE — rendered from 732a57810d27…, the page has moved since
  RENDERS ARE STALE — run `node render.mjs`
EXIT=1
```

`732a57810d27…` is the index.html of `c6258a4` — **session 92's page.** Session 93 changed the face and did not re-render, so the guard whose whole purpose is this provenance is red on the frozen object. `VERIFIER-92.md` listed `renders.py → RENDERS MATCH THE PAGE` under WHAT HOLDS; it no longer holds.

**What that costs is not bookkeeping.** `STATE-1.txt` is described at `still-dark/README.md:713` as *"what a screen reader receives, used unedited as panel material."* The committed one still publishes both paragraphs cut tonight and the quotation cut tonight:

- `STATE-1.txt:48` — `A ship reaches the list only after it comes back, so a day that is over keeps being answered.` (`#sd-arrive-cap`, cut 6)
- `STATE-1.txt:50` — `Neither end of this figure can rise. Both fall: … and no ship this record can name on the day itself is ever among the certain.` (`#sd-arrive-constant`, cut 4)
- `STATE-1.txt:64` — the 164-word refusal, quotation and scope clause intact.

**This house has already failed on this and written it down.** `still-dark/README.md:246–247`, among session 87's paid blocking items: *"a committed `STATE-1.txt` rendered from a page that had already moved, **publishing to the screen-reader record the one sentence tonight's repair exists to replace**."* Tonight it publishes three of them.

**How I checked:** `tools/renders.py` (exit 1), then `for h in $(git log --format=%h -25); do git show $h:…/index.html | sha256sum; done` to attribute `732a5781` to `c6258a4`, then grep of the committed `STATE-1.txt`. **Smallest repair:** run `node render.mjs` and commit the three outputs with `RENDERS.json`, or, if the renders are deliberately held at session 92, say so in `RENDERS.json`'s `note` and stop the guard reporting provenance it does not have.

---

### 4. The guard table describes "the page as committed" with two figures that are not the committed page's

**Strings and lines,** `projects/season1/still-dark/README.md`:

- `:1069` — `365 px of 844 · **596 px of 900** — HOLDS · **245 px and 20 of 31 chips against the floor of 268 and 22 — UNDER**`
- `:1070` — `It reads **245** now`
- `:1071` — `**130 failures — RED**`

**Why it is false.** The section's own preamble (`:1056–1059`) is in the present tense about the present object: *"**One of them is red on the page as committed, and this is where a stranger is told so before they run it.** Every figure below was taken tonight on the committed object; each line names the command and what makes it pass."* On the object at `HEAD` the named commands return:

```
$ NODE_PATH=… node tools/frame.mjs
phone 390×844 — figure-top to controls-bottom: 365 px of 844 — HOLDS
  the hole sharing a frame with the whole figure: 238 px, 20 of 31 chips — floor 268 px / 22 chips — UNDER
wide 1400×900 — figure-top to controls-bottom: 634 px of 900 — HOLDS

$ NODE_PATH=… node tools/fold.mjs
FOLD: 120 failure(s) …
```

**596 is 634; 245 is 238; 130 is 120.** The 1400 px span moved because two paragraphs left the head; the hole's share moved with it; `fold.mjs` dropped ten because the same two paragraphs took a sampling position with them. `README.md:761` also types `130` a second time, in the file's unheaded stretch — `VERIFIER-92.md` noted that hand-typed count as banked 17's species and said it *"will be false on the next list."* It was false on the next night instead. This is `KRITIKER-89.md` condition 3 — guards green, or their current output printed truthfully — and it is not discharged on this object.

**Smallest repair:** re-run the three commands and write in their outputs, or stamp the whole table `SESSION 92, on `c6258a4`` and drop *"as committed"*. **I checked my own repair:** the three commands above are the ones the table names, run from the directories it names, on the tree at `HEAD` with nothing dirty.

---

### 5. "200 words to 62" — the compression this claims is not the compression that happened

**String:** `the quotation, its scope clause and the second element's 36-word citation line go — **200 words to 62**, 394 px to what the guard now measures`
**File/line:** `projects/season1/still-dark/data.py:1087`.

**Why it is false.** The two elements the number governs are `arrive.cut.refused` and `arrive.cut.refused_source.text`. Measured with **`wc -w`, this house's own standing instrument** (`tools/README.md`), on the strings extracted from the two committed islands:

| | refused | source | total |
|---|---|---|---|
| `c6258a4` (session 92) | 163 | 34 | **197** |
| `7b885d8` (tonight) | 106 | 7 | **113** |

By `str.split()`, printed as reference only: 164 + 35 = 199 → 107 + 8 = 115. The "200" is right — it is `DRAMATURG-92.md:99–100`'s own count (`164 words` + `36 words`). **The 62 is not a measurement of anything on the page**: the true figure is 113, and 62 is closest to the block's final three sentences taken alone (63 by `split()`), which is not what "200 words" counted. The claim as printed says the block shrank by 69 %; it shrank by 43 %.

This is the banked species the house named for itself — a sentence repaired without once running the arithmetic it describes — sitting in the comment that documents tonight's payment of a cut priced in words.

**How I checked:** parsed the `sd-data` island out of both committed `index.html` blobs, wrote the four strings to files, `wc -w`. **Smallest repair:** `200 words to 113`.

---

### 6. Three comments in the frozen object and its builder describe a quotation this session deleted

**a. `projects/season1/still-dark/index.html:2613`** — the object under test, at the site of tonight's own cut:

> `<!-- The address of the requirement quoted one line up. A SOURCED sentence about a named third party's method carries its retrievable URL on the face that prints it… -->`

Nothing is quoted one line up. `#sd-arrive-cut-refused` carries no quotation marks and no quoted requirement; the requirement was cut tonight. `data.py:1110–1112`, describing the *same element*, states the opposite and states it correctly: *"Nothing on the face quotes that page any more; what stands is this house's own one-line characterisation."* Two committed comments about one `<p>`, contradicting each other, both written or left standing tonight.
**Smallest repair:** `The address of the method characterised one line up.`

**b. `projects/season1/still-dark/data.py:1038`** — `BOTH QUOTATIONS ARE FETCHED, NOT REMEMBERED. The capture rule is quoted from Amelia Hoover Green…`. There is now one quotation in this block, not two; the capture rule is quoted nowhere on the face.

**c. `projects/season1/still-dark/data.py:1000` and `:1043`** — the same URL, the same word:

- `:1000` — `the method sheet says it in words, fetched first-hand tonight (200, 27,748 bytes)`
- `:1043` — `(https://frankbueltge.de/werke/ghost-fleet/, 200, 27,046 bytes tonight)`

Two byte counts 702 apart for one page, both labelled *tonight*, in one file. I fetched it twice tonight: **200, 27,100 bytes**, stable. Neither figure is tonight's. Both are inherited unchanged from `babd179` (session 90) — `git show babd179:…/data.py | grep -n "27,748\|27,046"` returns both at their old line numbers — so the word *tonight* has now survived four sessions in a file that was edited tonight. Banked failures 24 and 28, the session-relative adverb frozen into a string that outlives the session, which `VERIFIER-89.md §3` struck once already.
**Smallest repair:** one byte count, taken tonight, with the date of the fetch instead of *tonight*.

---

## NOTED, not blocking

1. **`tools/frame.mjs` reports a deleted node as merely mis-placed.** With `#sd-arrive-constant` off the page, `frame.mjs:236` returns `{h: null, inside: false}` and `:254` prints, at both widths:
   `— px  what the ends of the figure can do   — outside the frame at this width`
   The paragraph is not outside the frame at this width; it is not on the page at any width. An instrument that reports absence as displacement tells the next session the thing still exists. That is banked 54's shape — a guard whose account of itself misleads — and no number is wrong, which is why it is here and not above. A missing selector should print `— absent from the page` and say so once, or leave the list.
2. **`ledger.caption` — "Eight lists came back in more than one set of bytes each while every field this page reads stayed identical."** True as built: `data.py:1682–1687` keys on `content_sha256`, and eight of the eleven distinct contents have more than one body hash. But the face uses *list* to mean an edition date everywhere else — *"the ten lists this record holds"*, *"Each of the ten lists…"* — and under **that** noun the sentence is false: eight edition dates came back in more than one set of bytes, but one of them, 10 August, came back with **different fields too** (two contents, and the share fell 37 % → 35 % inside that one date). The clause that follows — *"a copy's fingerprint is not the list's identity"* — is what rescues it, and it is doing more work than a reader will notice. Verified by grouping the thirty captures both ways.
3. **`PROJECT.md` carries no session-93 entry**; its number line is stamped *"As of session 92: … from 29 saved copies … (11 contents, 18 bodies)"* and I confirmed it correct **as of** that state: `--as-of 2026-08-13T17:02:56Z` returns 29 captures, 18 bodies, 11 contents. Tonight's record is 30 / 19 / 11. Dated, so not false — but the live project record now describes a state one night behind the object at `HEAD`, and every figure in it was checked against a page that has since moved (see blocking 4).
4. **`PROJECT.md`: "it has fallen nine times from later lists, on 5, 6, 7, 8, 9, 10, 11, 12 and 13 August."** Nine list-days, all nine correct. At capture granularity the falling end took **eleven** values and therefore fell **ten** times: 100, 79, 69, 65, 55, 44, **37, 35**, 33, 31, 26 — the 10 August list produced two of them, and 37 % is reachable only by `--as-of`, never by a stop on the face. Reproduced by running `--as-of` at all thirty capture instants.
5. **`day.py --as-of` still swallows malformed instants** — `--as-of garbage` returns the full thirty-capture answer, `--as-of 2026-08-13T170256Z` (the form of the capture filenames) returns `28 capture(s) … 4–35`, both exit 0. Carried unpaid from `VERIFIER-92.md` note 3. Every instant the face prints is well-formed and all ten check out.
6. **Every instrument claim in `tools/width.mjs`, `tools/turn.mjs` and the new `tools/README.md` sections reproduces.** I ran both against the control (`git show b619af4:…/index.html` → `/tmp/x92`) and against the object:
   - `width.mjs --dir=/tmp/x92` → `OVERFLOW 481→664 px (184 widths), worst +184 px — widest offender table`, exit 1. The header's *"reproduces that voice's hand sweep exactly"* is exact, to the width and the pixel, against `DRAMATURG-92.md:152–156`; the `span.sd-share-when`/`min-width: 292.089px` attribution is that memo's, verbatim, and correctly credited to it and not to the tool.
   - A full 280→1920 sweep at 5 px took **14.25 s** against the documented *"about 15 seconds"*. On the object at `HEAD`: `no width holds a document wider than its window. CLEAN`, exit 0.
   - `turn.mjs --dir=/tmp/x92` at 1400 px → the share **12,961 px²** and the fraction **2,774 px²** — `DRAMATURG-92.md:73`'s figures to the pixel — and it does **not** return 18,704 or 2,989, exactly as its header says, because the committed beat adds two chips (3,980 px²) and not seven. The disclaimed two-of-four is honest and the reason given is the right one.
7. **Reported, not ruled.** `python3 tools/record_words.py` → `2938`, **UNDER by 62** on the committed tree. `fold.mjs` → **120 failures, RED**, published red. `frame.mjs` → the hole's share of the figure's frame at **238 px / 20 of 31 chips** against the voice's floor of 268 / 22 — seven pixels further under than the 245 the README prints, and a staging matter I have no vote on beyond the number.

---

## WHAT HOLDS — reproduced first-hand

- **The island belongs to the captures.** `python3 data.py --check` → `island matches the captures`, exit 0.
- **The face's figure, and every stop.** For all ten stops I ran the stop's own `check` command and compared four strings each — share, falling fraction, fixed fraction, certain count — plus the total. **Ten of ten identical**, 100/79/69/65/55/44/35/33/31/**26** and 11 of 42 / 11 of 22 / 11 certainly dark at the last. The quoted `output` block is byte-identical to `day.py 2026-08-04 | head -6` on this tree, at 30 captures, 10 editions, 11 contents, **19** bodies.
- **The thirtieth capture.** 200, 31,715 bytes, `ac75fe92…`, content `96fc683e…` — identical to the 29th's content and a new body, as claimed. The live page returns 31,715 bytes tonight, matching the capture exactly. Ledger row, edition date, 11 vessels and 265 examined all check.
- **The derived counts nobody printed.** `lede`: 11 named on the day, 31 later, **26** after the page printed its figure — 42 − 16 at the printed `as_of` of 2026-08-06T08:36:39Z. `since_note`: **22** of 31 windows still reach back to 4 August and **9** are ruled out by the list of 12 August, whose window opens on 5 August — 22 + 9 = 31, and the first list that could rule one out is indeed 12 August. `fall.moved`: 43 points, 69 → 26. `kept`: six to eleven names of 189 to 265 examined — min and max over all ten editions, exact. `cut.figures`: 230 / 82 / 5,641, the 4 August capture's own aggregates.
- **Every quotation on the face is on its source page.** The window sentence, `"The index counts all examined; the case and list show named vessels."` and the definition sentence all appear verbatim in the method sheet I fetched tonight (200, 27,100 bytes); the unquoted paraphrase *"at least 12 hours dark, at least 50 nautical miles offshore"* is a fair rendering of its `≥ 12 h, ≥ 50 nm offshore`.
- **All four distinct cited hosts answer 200** — `frankbueltge.de/ghost-fleet/` (31,715), `frankbueltge.de/werke/ghost-fleet/` (27,100), `hrdag.org/…` (122,503), `biblio.ugent.be/publication/8647789` (37,878), plus a sampled Global Fishing Watch vessel page.
- **The first beat is derived and not chosen.** 56 alphanumeric tokens in the gloss ÷ 238 wpm = 14,117.6 ms → the island's `14118`; 14,118 + 9 × 1,600 = 28,518 ms → the *"about twenty-nine seconds"* the run announces. `announce.mjs` returns 1 live region, 4 writes, 3 spoken, 11 figure rewrites, and the spoken lines now carry the stop's own share.
- **`tiers.mjs`** passes: every printed figure sits in a scope carrying a tier word — and, as its own footer says, it cannot say the word is the right one.
- **The three cuts are really cut.** `arrive.caption` and `arrive.constant` are gone from the island and their elements from the DOM; the island diff between `c6258a4` and `7b885d8` is 62 lines and contains nothing but the two deletions, the hedge on ten stops, the refusal pair, the thirtieth ledger row, `captures: 29 → 30`, `Seven lists → Eight lists`, and the rebuilt `output`. Nothing was changed under cover of the rebuild.

---

## THE VERDICT

**FAIL.** Six blocking items. Two are sentences on the work's face — the refusal, whose remaining reason is contradicted by the address printed beside it, and the hedge, whose new clause reaches a true conclusion by a route this record's own rows refute. One is a red provenance guard publishing three deleted paragraphs to the screen-reader record, a failure this file's own README already banked. Three are counts and comments in the process record that the night's own edits made false.

The house asked me to rule on one sentence and I will end on it, because it is the pattern rather than the exception. *"And no ship this record could name on the day itself is ever among the certain"* is the strongest thing this work has said about its own arithmetic: not observed, not tonight's, but provable, and I proved it. The eighteen words the house put after the colon to explain it are wrong, and they are wrong because the proof the house ran was read one column across — the earliest **list**, not the earliest **return**. A finding that is right does not make the sentence carrying it right, and this record has now written that down twice.
