# VERIFIER-87 — facts and tiers, session 87

**VERDICT: FAIL — 8 blocking**

**Hashes pinned at the head of this pass, as dispatched, and re-checked at the end — all four
unchanged, nothing moved under me:**

```
$ sha256sum projects/season1/still-dark/index.html projects/season1/still-dark/data.py \
            projects/season1/still-dark/README.md tools/frame.mjs
f43a481b59933f43806931c87c26cd8fbdf30f3ea87d735fae3da202a79b8eaa  .../still-dark/index.html
3a459aaa4a2f3f55d797bb18e4090cb468e4fcd665f60a9ed7ee63dd5359488f  .../still-dark/data.py
f1a1c8eabacdbef06ee57e739dcd866bee6fdb91ca86baf1a1fb85f8412c7eb2  .../still-dark/README.md
a0de698dae3fc6575a7929ef7cf69b33e94c900aa1ddaf92f0df9d2945ccb0dc  tools/frame.mjs
```

State: `git log -1` = `abecba4` (session 86's landing commit). Session 87's work is **uncommitted**
in the working tree; "last night's committed page" throughout this memo means
`git show HEAD:projects/season1/still-dark/index.html`, extracted to a temp directory and driven by
the same instrument, never read.

---

## 1. The 24th capture — PASS, and verified against the live instrument first-hand

```
$ python3 projects/season1/capture/day.py 2026-08-04
day 2026-08-04  ·  24 capture(s) read, 8 distinct edition(s), 9 distinct content(s), 14 distinct bod(y/ies)
  vessels dark on that day .......... 2–33 (certain–possible)
  SHARE knowable on the day ......... 33%–100%  (11 of 2–33)
```

24 / 8 / 9 / 14 exactly as claimed, and the published figure did not move. The two 11 August
captures compared field by field:

```
content_sha256 same? True   a7ab0eb1788c == a7ab0eb1788c
body sha same?     False
bytes              32333 → 32441
assets A: ["/_astro/Base.BDo6THrI.css", ".../Base.astro_...CRoAemHu.js"]
assets B: ["/_astro/Base.P8Knfq78.css", ".../Base.astro_...CRoAemHu.js"]
DIFFERS: fetch, page_assets   (vessels, aggregates, case_of_the_day all identical)
```

Only the body and the CSS fingerprint moved. Fetched first-hand rather than trusted:

```
$ curl -sS -o /tmp/gf.html -w "HTTP %{http_code}, %{size_download} bytes\n" https://frankbueltge.de/ghost-fleet/
HTTP 200, 32441 bytes
$ sha256sum /tmp/gf.html
e506a522983b6339a8a79ab7a4ba3914d4cc2c306b23ef306e07a43e78b301cb
$ grep -o "Base\.[A-Za-z0-9_-]*\.css" /tmp/gf.html
Base.P8Knfq78.css
```

Byte-for-byte the capture's recorded `fetch.sha256`. The capture is genuine and current. **PASS.**

Also re-derived independently: 6 of the 8 editions came back in more than one set of bytes,
9 distinct contents, 14 distinct bodies, 24 captures. That 6 is the subject of item 4 below.

## 2. The shortened `constant` — the arithmetic run, not read. TRUE, for the first time in four
   forms

The published sentence:

> "Neither end of this figure can rise. The upper end holds at 100 % until more of these ships are
> certainly dark on this day than the eleven the day itself named; only the lower end has moved so
> far, and the next list can lower it again."

`day.py:213–215` computes the upper end as `obs / max(n_lo, obs)`, with `obs = 11`. Run over the
range rather than reasoned about:

```
$ python3 projects/season1/capture/day.py 2026-08-04 --json  → band {'certain': 2, 'possible_extra': 31, 'band': [2, 33]}
upper = obs / max(n_lo, obs), obs = 11
  n_lo= 0..11  upper = 100.00%
  n_lo=12      upper =  91.67%
  n_lo=13      upper =  84.62%
lower = obs / n_hi = 11/33 = 0.3333
```

The upper end holds at exactly 100 % for every `n_lo ≤ 11` and falls at `n_lo = 12` — *more than
eleven*. The sentence's condition is the arithmetic's condition. `n_lo` is monotone non-decreasing
and `n_hi` monotone non-increasing in effect on the lower end, so neither end can rise; the upper
end has not moved and the lower has fallen eight times. Every limb checks. **PASS — the fourth form
of this sentence is true, and it is true because the clause that made the previous three false was
removed rather than re-branched.**

I did not attempt to prove that `n_hi` can never fall (a later edition re-printing a wider window
for a vessel already counted). That is the record's standing law, not a claim new tonight, and it is
outside what this pass was dispatched to rule on.

## 3. `11 of 230` and the tier word — PASS

```
$ NODE_PATH=$(npm root -g) node tools/tiers.mjs   → exit 0
  11 · 230                   SOURCED/DERIVED  (8 px)
      #sd-arrive · "11 of 230"
  4 · 230                    SOURCED/DERIVED  (0 px)
      #sd-arrive · "— the list of 4 AUG named eleven ships out of the 230 disappearances…"
TIERS: every printed figure stands in a scope carrying a tier word.
```

Structural coverage only, as the tool itself says. On the semantics, which is what was asked: the
figure mixes a house count with an upstream one, and its clause separates them by name —

> "— the list of 4 AUG named eleven ships out of the 230 disappearances **it says it examined**. No
> stop moves this figure. SOURCED — **the count of names is this house's own**."

`230` is attributed to the list (`it says it examined`); the `11` is attributed to this house. Both
checked against the source, not the sentence: `captures/2026-08-05T043932Z.json` is the only copy of
the 4 August edition, its `aggregates.disappearances_examined` is **230** and its `vessels` array
holds **11** entries, which is what `data.py:408` reads as `day_cut`. The construction is the same
one `cut.tier` has carried since the repair of banked failure 40, and it is the right one here.
"No stop moves this figure" is true: I drove all eight stops and read the element at each — `11 of
230` at every one. **PASS.**

## 4. The moved paragraphs, and the rendered DOM order — PASS on the tier line, with a coverage
   finding

Rendered order taken from the browser, not the source (freshly rendered STATE-1 from the frozen
`index.html`, line numbers its own):

```
 44  A ship reaches the list only after it comes back… **Eight lists, eight answers, one day** …
 46  WHAT THE LIST OF 4 AUG WAS THE TOP OF                     (cut.heading)
 48  11 names printed · 230 disappearances examined, 82 … · 5,641 …   (cut.figures)
 50  The instrument says so itself, in its method sheet: …     (cut.said)
 52  SOURCED — … The count of names, and the count of lists **below**, are this house's own.  (cut.tier)
 54  This record cannot tell a ship that came back later …     (since_note)
 56  Each of **the eight lists** this record holds prints six to eleven names …   (cut.kept)
```

**The count of lists is still below it.** `cut.kept`'s "the eight lists this record holds" — the
sentence `cut.tier` was written next to — stands at 56, four lines under the tier at 52. The claim
is not false. **PASS.**

**Not blocking, but named:** the run line's "Eight lists, eight answers, one day" (44) stood *below*
`cut.tier` on last night's committed page and stands *above* it now. That count is still inside a
scope carrying the section's `DERIVED` legend, so it is not orphaned — but the one sentence on the
face that says whose the list counts are now points past it by its own word. If a session touches
this line, "below" is the word to reconsider.

**No figure is orphaned (banked failure 25).** `tiers.mjs` exits 0 on the moved state, and the
figure promoted into the frame carries its own tier clause in its own row rather than inheriting one
from a paragraph that walked away. That was the failure mode and it was avoided.

## 5. The deleted clause — nothing TRUE is lost from the face, but the head's carrier is false at
   seven of eight stops — BLOCKING

The deleted clause said two things: (i) a list gives a return only to the nearest week; (ii) as of
now, thirty-one of the thirty-three are merely possible and two are certain.

Both survive somewhere on the face. Grepped out of the freshly rendered page:

```
 32  A list gives a ship's return only to the nearest week, so two of these names are certainly
     dark on this day and the rest are possible.                                    (hedge)
 54  … a list gives a return only to the nearest seven days, so the return window of every name
     added since 4 August still reaches back to it.                                 (since_note)
303  Thirty-three ships could have been dark on 4 August 2026 and two of them certainly, because
     the instrument publishes a return only as a week-wide window — so the total is written
     2–33, and the share runs from 11 of 33 to 11 of 11.                            (the LIVE band)
```

Line 303 states the deleted clause's whole content, stop-independently. **So the answer to the
question as put is: no, nothing true was lost.**

**But the claimed carrier does not carry it.** I read `#sd-arrive-hedge` at every one of the eight
stops. It is one string, unbranched, identical at all eight:

> "A list gives a ship's return only to the nearest week, **so two of these names are certainly dark
> on this day** and the rest are possible."

"These names" are the names standing above it. At stop 0 those are the eleven of 4 AUG, under a
heading reading "NAMED ONLY BY LATER LISTS — **nothing yet**." Per `day.py`'s own classification,
**none of those eleven is `certain`**; the two that are — PANOFI FORE RUNNER and HEATHER LYNN —
arrive with the list of 11 AUG, at stop 7. Counted at each stop, names displayed / certain among
them: `11/0, 14/0, 16/0, 17/0, 20/0, 25/0, 31/0, 33/2`. **The sentence is true at exactly one of the
eight stops.**

This is worse than a run-time transient. Under `prefers-reduced-motion` the head does not run —
the controls say so themselves: *"Your machine asks for no motion, so nothing runs: this is the
day's own answer."* A reduced-motion reader who never clicks sees stop 0 and only stop 0, and there
the sentence is false about every name on their screen.

The string and its position are **inherited from session 86, not typed tonight** — I diffed it
against the committed page and it is byte-identical. What tonight changed is that the `constant`,
which said the same fact about *the total* and was therefore true at every stop, no longer says it;
the head's only remaining statement of it is the stop-dependent one. **The README's claim that "one
fact is carried by one sentence now, which is the state in which the failure above cannot recur"
is the wrong description of the state that was reached.**

**BLOCKING.** `projects/season1/still-dark/data.py:715–722` (`hedge`), rendering to
`index.html:681`. What would make it right: say it of the total, as the deleted clause and the
`band` string both do — "two of the thirty-three names this record can place in this day are
certainly dark on it" — or branch it on the stop, as the stops already branch `heading_since`.

## 6. The figures in the record — six of eight reproduce exactly, two do not

Run, not read:

```
$ NODE_PATH=$(npm root -g) node tools/frame.mjs
phone 390×844 — figure-top to controls-bottom: 951 px of 844 — OVER by 107
    179 px  the frame: both figures and their clauses
     83 px  what the ends of the figure can do
     30 px  the day's own heading
    112 px  the names the day itself printed
     59 px  the hole's heading
    250 px  the names only later lists gave
     75 px  the caveat on the names
    116 px  the controls and the run's line
     47 px  the space between them
wide 1400×900 — figure-top to controls-bottom: 554 px of 900 — HOLDS

$ NODE_PATH=$(npm root -g) node tools/frame.mjs --dir=<git show HEAD:.../index.html>
phone 390×844 — figure-top to controls-bottom: 1094 px of 844 — OVER by 250
     87 · 167 · 30 · 112 · 59 · 250 · 75 · 116 · 198
wide 1400×900 — 650 px of 900 — HOLDS

$ NODE_PATH=$(npm root -g) node tools/fold.mjs                    → FOLD: 64 failure(s)
$ NODE_PATH=$(npm root -g) node tools/fold.mjs --dir=<HEAD copy>  → FOLD: 64 failure(s)
```

| figure in the record | my run | ruling |
|---|---|---|
| 1,094 → 951 px at 390×844 | 1094 → 951 | reproduces exactly |
| 650 → 554 px at 1400×900 | 650 → 554 | reproduces exactly |
| budget 179/83/30/112/59/250/75/116/47 | identical, in order | reproduces exactly |
| "material and controls alone are 642 px" | 30+112+59+250+75+116 = 642 | reproduces |
| "leaves 202 px … which stand at 262" | 844−642 = 202; 179+83 = 262 | reproduces |
| "the block was 151 px of the 250" | unnamed space 198 → 47 = **151**; HEAD over by **250** | reproduces |
| "closed by 143 px" | 1094 − 951 = 143 | reproduces |
| `fold.mjs` **64** unchanged | 64 and 64 | reproduces exactly |
| **`data.py:988` — "57 px of a phone frame"** | **84 px** | **does not reproduce** |
| **README:154 / `data.py:979` — "thirty-two words"** | **23, or 47** | **does not reproduce** |

**BLOCKING (a).** `data.py:988` reads: *"It is also 57 px of a phone frame this face is 250 px over
— the cut is measured in `tools/frame.mjs` and named in the record, not asserted."* `frame.mjs`
reports the `constant` at **167 px** on the committed page and **83 px** now: the cut is **84 px**
at 390×844 and **50 px** at 1400×900. I also built the hypothetical the comment might have meant —
last night's sentence with *only* the 23-word clause removed, nothing else — and drove it through
the same instrument: **117 px, a 50 px cut.** No construction of `frame.mjs` yields 57. And the
second half of the sentence is false too: `grep -n "57" still-dark/README.md` returns two hits,
neither this figure. The figure is asserted, in a comment whose own words are that it is not.

**BLOCKING (b).** README:154 *"thirty-two words left the `constant` line"*, and `data.py:979`
*"Thirty-two words of this sentence said what the `hedge` line says."* Counted:

```
the quoted clause                                          23 words
old constant 92 tokens → new 48; word-diff: 47 removed, 3 inserted, net 44
```

23 or 44 or 47 — never 32. This house has a banked failure for a hand-checkable word count
published without running the count (26), and `tools/record_words.py` exists because of it.

## 7. "Three lines" — false in three places, and self-contradictory in one file — BLOCKING

The load-bearing premise of tonight's deletion is that the clause and the `hedge` stood next to each
other. Measured in the browser at 390×844, bottom of `#sd-arrive-constant` to top of
`#sd-arrive-hedge`:

```
NOW   constant [451,534]  hedge [1019,1094]  gap = 485 px
HEAD  constant [359,525]  hedge [1162,1237]  gap = 637 px
```

Four elements stand between them — the day's heading, eleven names, the hole's heading, twenty-two
names. On last night's page the two sentences were **637 px apart on an 844 px phone**; they could
not be on the screen together. "Three lines" is not a rounding; it is the wrong order of magnitude,
and the sentence it justifies is the one whose removal is item 5 above.

Worse, this README says it in both directions:

- **README:100** (session 86 section) — *"the `hedge` line **three lines above** it on the same
  rendered page"*
- **README:156** (session 87 section, new tonight) — *"stood **three lines above** the `hedge`
  line"*
- **`data.py:979`** (new tonight) — *"three lines **below** it on the same rendered page"*

On the rendered page the constant is above the hedge, so README:100 is wrong in direction as well as
in distance. `VERIFIER-86.md` §4, where this phrasing comes from, said *"three lines above it **in
the same JSON island**"* — true of `data.py`'s source order, and the README dropped the qualifier
that made it true.

**BLOCKING.** README:100 and :156, `data.py:979`, and the same phrase in the new `index.html`
comment block. What would make it right: the measured distance, or "in the same builder."

## 8. `still-dark/README.md` — two sentences tonight made false — BLOCKING

Repository-wide sweep for `23 saved`, `thirteen bodies`, `Five lists`, `23 capture`, excluding
`archive/`, `.git/`, and the files (g) exempts:

| Address | String | Judgment |
|---|---|---|
| README:64 | `…from 23 saved copies holding 8 lists` | historical — inside the dated session-86 narration |
| README:371 | `as measured at session 86, 23 saved copies / 8 lists` | historical — the row carries its session |
| README:476 | `Twenty-three saved copies, thirteen bodies … as of session 86` | stale, not false — carries its date; the live face now reads 24 and 14 |
| **README:479** | **`Five lists have come back in more than one set of bytes each`** | **FALSE TONIGHT** |
| **README:51–52** | **`what stands between the names and the space is the figures the list published and their tier word`** | **FALSE TONIGHT** |

**BLOCKING (a).** README:479. Six lists have, as of tonight — derived independently over the
captures, and the session knew it: the same sentence on the face was changed from *"Five lists came
back in more than one set of bytes each"* to *"Six lists…"* in `index.html`'s ledger caption. The
face was corrected and the document a stranger reads first was not.

**BLOCKING (b).** README:51–52. Nothing stands between the eleven names and the reserved space now;
`#sd-arrive-names-then` is followed directly by `#sd-arrive-head-since`. The sentence is present
tense in a session-85 narration and the session-87 section ninety lines later contradicts it. This
is banked failures 24 and 28, third time.

`capture/README.md`: swept, holds no live count, nothing tonight made false.

## 9. Two quotations attributed to `DRAMATURG-85.md` that are not in it — BLOCKING

New tonight, in the committed page's own comment block:

```
index.html:1951   lists annotation and not staging — *"nothing in it moves between stops"* — and
index.html:1953   standing still in the same frame while the first falls."* Here it is.
data.py:891–893   prescribed a build rather than a cut — *"the disclosure inside the numeral, a
                  second figure standing still in the same frame while the first falls."*
```

Both strings are in quotation marks and attributed. Neither is in the file:

```
$ grep -n "nothing in it moves\|standing still in the same frame" projects/season1/DRAMATURG-85.md
(no output)
```

What the memo actually says, at :153 and :245 and :257, is *"does not move, does not brighten, does
not tick"* / *"0 mutations. Every time."* and *"Take the four fixed paragraphs out of the run's
spine and put the disclosure inside the numeral"* / *"`230` standing still in the same frame as
`35 %–100 %` while it falls."* The prescriptions are real and tonight's build answers them; what is
invented is the wording inside the quotation marks. The protocol's line is *no invented quotations,
in any tier*, and the fix is to drop the marks or quote what is there. (The README uses the same
phrase in italics without quotation marks, at :132 and :55 — that is the house's own shorthand and
is fine.)

## 10. The island and the renders — the island passes, the renders do not — BLOCKING

```
$ cd projects/season1/still-dark && python3 data.py --check
island matches the captures

$ python3 tools/renders.py projects/season1/still-dark
  index.html         f43a481b5993…  STALE — rendered from c30842a88625…, the page has moved since
  STATE-1.txt        f77facfc9bb5…  as written
  render-1400.png    2179dcd4dc13…  as written
  render-900.png     6d38abf7c553…  as written
  RENDERS ARE STALE — run `node render.mjs`      (exit 1)
```

All three outputs were made from an `index.html` that is not the one committed beside them. This is
not bookkeeping. I rendered the frozen page into a temp copy with the work's own `render.mjs` and
diffed:

```
$ diff still-dark/STATE-1.txt /tmp/sd-copy/STATE-1.txt
12c12
< names the list of 4 AUG printed, of the disappearances it says it examined. No stop moves it. SOURCED — the count of names is this house's own.
---
> — the list of 4 AUG named eleven ships out of the 230 disappearances it says it examined. No stop moves this figure. SOURCED — the count of names is this house's own.
```

One line, and it is the line the session built tonight. **The committed `STATE-1.txt` — the
screen-reader order, the material every panel of this house has ever been given — publishes a
sentence the page does not produce, and the superseded version is precisely the one without the
words.** It never says "eleven" and never says "230". Tonight's README argues at length that the
clause exists because *"`11 of 230` read as a phrase can be heard as eleven of two hundred and
thirty names — false by an order of magnitude"*; the committed screen-reader artefact carries the
version before that repair. A tier the eye can read and the ear cannot is banked failure 74's
finding, and this is its shape: the sighted page is repaired, the spoken record is not.

**BLOCKING.** Run `node render.mjs` in `projects/season1/still-dark` and commit all four outputs.

---

## What this pass could not check

- **The 230 of the 4 August edition against live upstream.** The instrument publishes only the
  current edition; 230 is checkable against `captures/2026-08-05T043932Z.json` and no further. That
  is the standard the brief sets and it is met, but it is not a second source.
- **Whether `n_hi` can fall** — the "the total can only grow" law. I verified that the sentence
  follows from `day.py`'s formula given that law; I did not test the law.
- **The staging voice's own series** (813 / 1,065 / 964 px, 37,448 changed pixels). Not
  reconstructable from any committed instrument; the record already says so and does not lean on it
  tonight.

## Summary of blocking items

1. **`still-dark/data.py:715–722` → `index.html:681`** — the `hedge`, now the head's only carrier of
   the deleted clause's fact, says "two of these names are certainly dark on this day" at all eight
   stops while the certain pair is on screen at exactly one; under reduced motion the reader sees
   only the stop where it is false. Fix: state it of the total, or branch it per stop.
2. **`still-dark/data.py:988`** — "57 px" reproduces under no run of `frame.mjs` (measured 84 px at
   390×844, 50 px at 1400×900, 50 px for the clause-only cut), and the same comment claims it is
   measured by that instrument and named in the record; it is in neither. Fix: print the measured
   figure or delete the claim.
3. **`still-dark/README.md:154` and `data.py:979`** — "thirty-two words" is 23 (the clause) or 47
   removed / 3 inserted (the whole edit). Fix: run the count.
4. **`still-dark/README.md:100`, `:156`, `data.py:979` and the new `index.html` comment** — "three
   lines" apart on the rendered page is 485 px now and 637 px on the committed page, with four
   elements between; README:100 also states the opposite direction to README:156. Fix: the measured
   distance, or "in the same builder."
5. **`still-dark/README.md:479`** — "Five lists have come back in more than one set of bytes each"
   is six tonight; the identical sentence was corrected on the face and not here. Fix: six.
6. **`still-dark/README.md:51–52`** — "what stands between the names and the space is the figures
   the list published and their tier word" is false: nothing stands there. Fix: past tense, or a
   pointer to the session-87 section.
7. **`still-dark/index.html:1951,1953` and `data.py:891–893`** — *"nothing in it moves between
   stops"* and *"the disclosure inside the numeral, a second figure standing still in the same frame
   while the first falls"* are in quotation marks and attributed to `DRAMATURG-85.md`; neither
   string is in that file. Fix: drop the marks or quote the memo.
8. **`still-dark/RENDERS.json`, `STATE-1.txt`, `render-1400.png`, `render-900.png`** —
   `tools/renders.py` exits 1; all three outputs were rendered from `c30842a8…`, not the committed
   `f43a481b…`, and the committed `STATE-1.txt:12` publishes a superseded standing-note that names
   neither "eleven" nor "230" — the exact defect tonight's clause was built to close. Fix:
   `node render.mjs` and commit all four.

**Hashes re-checked after every run above: all four unchanged from the head of this memo.**

VERDICT: FAIL — 8 blocking

---

## RE-RUN ON THE CHANGED STATE

**VERDICT: FAIL — 7 blocking.** Six of the eight banked items are paid and reproduce; item 4 is
paid at two of its four sites and its replacement carries three new false statements; and the
record's new session-87 section attributes to `DRAMATURG-87.md` a figure list and a finding that
memo does not contain.

**The object at the head of this re-run.** All five hashes as given:

```
a0fd3755219bbf96b236029d046f78bd3967634bb409ef6690c0662f9529b357  .../still-dark/index.html
a982bda19563acca5390e12b45b1a0fcde5cf9049b3da429afd87e78efb9cb13  .../still-dark/data.py
507119810f032fdd84e5343e6eafa611ab559f54dfa18497d2da2c2cb3a37ebd  .../still-dark/README.md
86cba4204e5ad64e7dd6f8e9256e34df08f9a6387ca4fffdf9ce6b5f1e38ce91  .../still-dark/STATE-1.txt
e10e5187f5d62e4db6731f3d789e380dfbf998fe90771cdb59ca42eda151a896  tools/frame.mjs
```

Note on one word used throughout the memo above: the page called *committed* in it is
`f43a481b…`, which was the working tree at that pass and was never committed. `HEAD`'s
`index.html` — session 86, the page that shipped — is `85eead78…`, and that is the control every
run below uses. Where the distinction changes a number it is stated.

### 1. The per-stop caveat — PASS

`hedge` is no longer a top-level island string: it is written per stop in `data.py:636` inside the
stop builder from `st[0]`, that stop's own certain count, and appears eight times in the island
(`index.html:781, 811, 837, 859, 889, 927, 969, 995`). It is written by `showStop()` at
`index.html:2321` and it is in the reservation list at `index.html:2432`.

Driven at 390×844 and 1400×900, all eight stops, reduced motion:

| stop | share | caveat | chips | certain chips on screen |
|---|---|---|---|---|
| 0 | 100 %–100 % | *not one of these names is certainly dark on this day* | 11 | 0 |
| 1 | 79 %–100 % | *not one…* | 14 | 0 |
| 2 | 69 %–100 % | *not one…* | 16 | 0 |
| 3 | 65 %–100 % | *not one…* | 17 | 0 |
| 4 | 55 %–100 % | *not one…* | 20 | 0 |
| 5 | 44 %–100 % | *not one…* | 25 | 0 |
| 6 | 35 %–100 % | *not one…* | 31 | 0 |
| 7 | 33 %–100 % | *two of these names are certainly dark on this day and the rest are possible* | 33 | 2 |

`python3 capture/day.py 2026-08-04` returns exactly two certain — **PANOFI FORE RUNNER** and
**HEATHER LYNN** — and both chips appear only at stop 7, added by the list of 11 August. The
caveat is true at eight of eight stops, and true at the stop a reader who asks for no motion
never leaves. The defect this house banked as failure 42's recurrence is closed.

**The reservation holds.** `#sd-arrive-hedge` occupies the identical box at every stop —
`[1147, 1222]`, 75 px at 390×844; `[595, 633]`, 37 px at 1400×900 — although the stop-7 string is
25 words against 20. Nothing below it moves either: the controls stand at `[455, 579]` at 390 and
`[641, 717]` at 1400 at all eight stops, and the run's line at `[508, 571]` and `[669, 717]`.
`frame.mjs` prints a single span and not a range at both viewports, which is the same fact from
the other side.

### 2. "57 px" → 84 px / 50 px — PASS, both runs

```
$ NODE_PATH=$(npm root -g) node tools/frame.mjs
phone 390×844 — 311 px of 844 — HOLDS   ·  wide 1400×900 — 554 px of 900 — HOLDS
   the constant: 83 px at 390 · 67 px at 1400

$ git show HEAD:.../index.html > /tmp/sd/index.html
$ NODE_PATH=$(npm root -g) node tools/frame.mjs --dir=/tmp/sd
phone 390×844 — 1094 px of 844 — OVER by 250  ·  wide 1400×900 — 650 px of 900 — HOLDS
   the constant: 167 px at 390 · 117 px at 1400
```

167 − 83 = **84 px**; 117 − 67 = **50 px**; the committed phone frame is **over by 250**. Every
number in `data.py:1032–1034` reproduces on the instrument it names. The sentence that carried 57
is gone, and the two surviving occurrences of the figure (`data.py:1034`, `README.md:216`) are
quotations of the corrected defect and are marked as such.

### 3. Twenty-three words, forty-seven removed, three inserted — PASS

Counted with `str.split()`, one of the two tokenizers `tools/record_words.py` prints:

```
committed constant  92 tokens        tonight  48 tokens
word-diff            47 removed · 3 inserted
the quoted clause    23 tokens
```

`README.md:193` *"A TWENTY-THREE-WORD CLAUSE"*, `data.py:1019` *"a twenty-three-word clause"* and
`data.py:1030` *"removes forty-seven words and inserts three"* all reproduce. Under a
punctuation-stripped count the same diff reads 43 removed / 1 inserted; the house's own
instrument counts whitespace tokens, and on that instrument the published figures are exact. No
"thirty-two" survives anywhere on the object except at `README.md:218`, where it is named as the
error.

### 4. "Three lines" — FAIL, at two unrepaired sites and in three new statements

Two of the four sites are paid. `README.md:156`'s *"three lines above the `hedge` line"* is gone;
the `index.html` comment no longer makes the claim. Two are not:

- **`still-dark/README.md:103`** — *"while the `hedge` line **three lines above** it on the same
  rendered page"*. Unrepaired, and it is the site this memo above called wrong in direction as
  well as in distance.
- **`still-dark/data.py:1011`** — *"while the `hedge` string **three lines above** it, **on the
  same rendered page**"*. Unrepaired, same string, same defect.

Re-measured tonight on the object as committed, 390×844, all eight stops:
`#sd-arrive-constant` `[575, 658]`, `#sd-arrive-hedge` `[1147, 1222]`. The constant is **above**
the hedge, by 489 px bottom-to-top and 572 px top-to-top, with four elements standing between
them. Both sentences state the opposite direction.

And the replacement carries three statements of its own that do not hold:

- **`data.py:1023`, *"The two are three lines apart in this builder"*.** In this builder they are
  not: `"hedge":` is at `data.py:636` and `"constant":` at `data.py:1039` — **403 lines apart**.
  Three lines stand between them in the *rendered island* (`index.html:995` and `:999`), and only
  at the last stop, the eighth of eight. The qualifier chosen is the one that makes the phrase
  false; the qualifier this memo cited from `VERIFIER-86.md` §4 — *in the same JSON island* — is
  the one that comes within a line of true.
- **`data.py:1020`, *"485 px lower at 390×844"*.** 485 px is this memo's §7 figure, taken on
  `f43a481b…` before cut 2 moved the controls. On the object it now describes the same method
  returns **489 px**. It is 4 px and it is the same class as item 2: a measured figure asserted of
  a page that has moved under it.
- **`data.py:1022`, *"measured by `DRAMATURG-87.md` §7's method"*.** That memo has §1–§6, a
  VERDICT and a WHAT I DID NOT MEASURE, and no §7. The distance is measured in its **§4**, which
  prints *"the `hedge` line says the same thing 278 px below (317 → 595 at 1400)"* — and that
  reproduces exactly on tonight's object: constant top 317, hedge top 595 at 1400×900.

### 5. "Five lists" → "Six lists" — PASS, and the attribution is true

`python3 capture/edition.py`, 24 captures. Editions returning more than one body hash:

| edition | bodies | contents | attributable |
|---|---|---|---|
| 5 Aug | `17c07fc3` → `aed92f4f` | one | no asset moved |
| 6 Aug | `f673e2f7` → `74f093f7` | one | `TopBar.SLcnmZbT.css` → `Base.BvXYJsAy.css` — **1st** |
| 8 Aug | `4110d2b0` → `680c1c71` | one | `Base.BvXYJsAy.css` → `Base.BC3Pps2G.css` — **2nd** |
| 9 Aug | `8bf3c1ff` → `95c28f17` | one | same stylesheet both sides |
| 10 Aug | `90bd7aec` → `e5ddbb89` | one across the body change | `Base.gah2t5G_.css` → `Base.BDo6THrI.css` — **3rd** |
| 11 Aug | `a3107ddd` → `e506a522` | one | `Base.BDo6THrI.css` → `Base.P8Knfq78.css` — **4th** |

**Six**, not five. Tonight's sixth: 32,333 → 32,441 bytes = **+108**, content `a7ab0eb1…`
unchanged, and the stylesheet fingerprint moved with it — so **the fourth of the six** is
attributable. Every clause of `README.md:511–514` holds.

### 6. `README.md:51–53` in the past tense — PASS

Reads *"what stood between the names and the space, from that night until session 87, was the
figures the list published and their tier word"*, with *"(Nothing stands there now: see the
session-87 section below.)"* The pointer is right: §8 of this memo is the section that found it.

### 7. The two quotations — PASS, verbatim

Both strings now in `index.html:1988–1990` and `data.py:927–930` are in `DRAMATURG-85.md`:

```
:245        Take the four fixed paragraphs out of the run's spine and put the disclosure
            inside the numeral.
:258–259    `230` standing still in the same frame as `35 %–100 %` while it falls
```

The second is verbatim across a soft line wrap; the comments cite it as `:257`, which is where its
sentence begins and one line above where its quoted words start. Noted, not blocking. The comments
also now say the marks were the offence, which is the finding this memo made.

### 8. The renders and `STATE-1.txt` — PASS

```
$ python3 tools/renders.py        → exit 0
  index.html      a0fd3755219b…  the page the renders were made from
  STATE-1.txt     86cba4204e5a…  as written
  render-1400.png fddd840e6649…  as written
  render-900.png  e9e5054db090…  as written
  RENDERS MATCH THE PAGE
```

`RENDERS.json`'s `index_sha256` is the object's own hash. `STATE-1.txt:12` now publishes the
repaired standing note — *"the list of 4 AUG named eleven ships out of the 230 disappearances it
says it examined. No stop moves this figure. SOURCED — the count of names is this house's own."*
— and `:32` carries the stop-0 caveat, *"not one of these names is certainly dark on this day."*
The severed reader now meets the sentence tonight's repair was built for.

### 9. `cut.figures` after `DRAMATURG-87.md`'s cut 1 — PASS, no figure lost its tier word

`data.py:848` prints *"Of those 230 examined, 82 were dark inside national waters · 5,641 events
in the window"* — **three** figures, all upstream's. The tier line below it (`STATE-1.txt:52`)
reads *"SOURCED — the three figures the list published… The count of names, and the count of
lists below, are this house's own."* Three figures stand under it and it claims three. The two
figures the cut removed did not lose a tier word by going: `11` and `230` now stand in the head's
own frame at `STATE-1.txt:11` under their own tier clause at `:12`, and the count of names and the
count of lists still stand in `cut.kept` at `:56`, below the line that assigns them. Banked
failure 25 is not committed.

### 10. `frame.mjs` and `fold.mjs` after cut 2 — PASS, and the record's breakdown is exact

```
frame.mjs  tonight            390×844   311 px of 844 — HOLDS at every stop
frame.mjs  HEAD (85eead78…)   390×844  1094 px of 844 — OVER by 250
fold.mjs   tonight   88 failure(s)  = 48 controls-off + 40 line-off + 0 chips covered
fold.mjs   HEAD      64 failure(s)  = 32 controls-off + 32 line-off + 0 chips covered
```

`README.md:183–184`'s breakdown — *"32 + 32"* and *"48 + 40, with 0 chips covered in both"* —
reproduces to the failure. So does the correction at `:186–188`: the figure is declared
`must: false` in `fold.mjs` and cannot count as a failure, so no part of either count is the
figure leaving the viewport.

### 11. `tools/frame.mjs`'s own two repairs — PASS

`--ref` appears nowhere in the argument parsing; the header now records the flag as removed and
gives the two `git show` lines instead. The budget places each part by measurement and prints
*"— outside the frame at this width"* against the six the phone frame no longer contains; the
space between prints 8 px at 390 and 47 px at 1400, and no negative.

### 12. The record's session-87 figures, ruled one at a time

| figure in `still-dark/README.md` | my run | ruling |
|---|---|---|
| 951 px → 311 px of 844 (`:168`) | 951 reconstructed, 311 measured | **reproduces** |
| 1,094 px, the committed page (`:208`) | 1094 | **reproduces exactly** |
| 554 px of 900 at 1400 (`:179`) | 554 | **reproduces exactly** |
| the three doors 859 / 864 / 868 (`:170–171`) | 858 / 863 / 868 | **reproduces to 1 px** |
| fold 64 = 32 + 32, 88 = 48 + 40, 0 chips (`:183–184`) | identical | **reproduces exactly** |
| the eight states 100 · 79 · 69 · 65 · 55 · 44 · 35 · 33 (`:157`) | identical, read off the DOM | **reproduces exactly** |
| *"`../DRAMATURG-87.md` §1 prints the middle four as 44, 38, 36, 35"* (`:159`) | the memo prints 65, 55, 44, 35 | **false** |
| *"`../DRAMATURG-87.md` §2 and §6 state that every one of the 64 is the figure"* (`:185`) | §6 does; §2 does not | **false in half** |
| −601 px, the budget's old print (`:213`) | not re-run — the defect is repaired and the old code is gone | not checked |

**The 951 and the three doors, and how they were reproduced.** Neither is measurable on the
committed page, so I rebuilt the state they were taken on: tonight's `index.html` with the
`max-width: 480px` rule of `index.html:543–548` overridden back to block flow. That baseline
returns **951 px** exactly, which is the strongest single check available that the figure is the
page's and not a hand's. Removing each candidate from that page and taking the maximum over eight
stops gives the standing figure row **−93 px**, the constant **−88 px**, the caveat **−83 px**,
against the memo's **−92 / −87 / −83**; read off the 951 baseline the doors are 858 / 863 / 868
against the published 859 / 864 / 868. The staging voice's numbers hold. The one reading of
*"reservation cleared"* that does not reproduce them is clearing every held block at once, which
drops the baseline to 920; the memo plainly cleared the reservation of the block it was deleting,
and on that reading it is right to a pixel on one door and to a pixel on the other two.

**`README.md:158–161` is false and it is the second invented attribution in two nights.** The
parenthetical says the staging memo prints the middle four states as *44, 38, 36, 35* and corrects
them. `DRAMATURG-87.md` §1 prints its eight states at `:64–69`:

```
stop 0  100 %–100 %     stop 4   55 %–100 %
stop 1   79 %–100 %     stop 5   44 %–100 %
stop 2   69 %–100 %     stop 6   35 %–100 %
stop 3   65 %–100 %     stop 7   33 %–100 %
```

— the same eight the README publishes, middle four included. `44, 38, 36, 35` appears nowhere in
that memo, nor anywhere in this repository outside the sentence that corrects it. This is not a
misquotation of a memo; it is a correction of a statement no memo made, and it is published in
the same paragraph that says *"a memo ships as it was written."* The related citation at `:185`
is half right: §6.3 (`:380–383`) does say every one of the 64 is the figure leaving the viewport,
and §2 says nothing about `fold.mjs` at all.

One figure I checked and found sound, against my own suspicion: `README.md:164` quotes the memo
as *"Placement was never the fault; units are."* — verbatim at `DRAMATURG-87.md:402`, though its
§1 puts it as *"Placement was never the problem; units were."* The quotation is genuine.
`index.html:526`'s *"Measured by the memo with the controls reparented: … 303 px of 844"* is
attributed to the memo and is the memo's own figure (`:176`); the built page measures 311, and the
README publishes 311 for the built page. Both are correctly addressed.

### What this re-run did not re-run

- **The staging voice's 813 / 1,065 / 964 series.** Still not reconstructable from a committed
  instrument, and the record still says so.
- **The law that the total can only grow.** As in the pass above: the sentences follow from it; I
  did not test the law.
- **`gaps.mjs`, `announce.mjs`, and the live upstream page.** Not re-fetched and not re-driven
  tonight; nothing in the eight items or the two cuts turns on them, and capture
  `2026-08-11T215800Z.json` is the same file this pass read.
- **The −601 px the budget printed before its repair.** The code that produced it no longer
  exists; I checked that the current budget cannot produce a negative, not that the old one did.

**Hashes re-checked after every run above — all five unchanged from the head of this re-run:**

```
a0fd3755…  index.html      a982bda1…  data.py      50711981…  README.md
86cba420…  STATE-1.txt     e10e5187…  tools/frame.mjs
```

VERDICT: FAIL — 7 blocking
