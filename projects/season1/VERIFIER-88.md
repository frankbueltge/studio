# VERIFIER-88 — session 88, 2026-08-12

Facts and tiers only, checked against the things themselves: the eight stops re-run out of
`day.py`, the strings read out of the built island and out of `STATE-1.txt`, the memo quotations
grepped in the memo, the 25th capture checked against the live source page, and the new span in
`tools/frame.mjs` run twice — once on tonight's object and once on an extraction of last night's
(`658a6fd`) as its control. Tonight's build landed as `1003f95` while this pass ran; every figure
below is re-checked against that commit's tree.

**VERDICT: FAIL — three blocking, six noted.** Eleven numbered findings; four of them record that
nothing is wrong, and say so plainly. Every blocking item is cheap to pay, and none of them is in
the arithmetic, which is right at every one of the eight stops.

---

## What was run

```
python3 projects/season1/capture/day.py 2026-08-04
python3 projects/season1/capture/day.py 2026-08-04 --as-of <each of the eight stops' instants>
cd projects/season1/still-dark && python3 data.py --check
cd projects/season1/still-dark && python3 data.py --write --into <scratch copy of index.html>
NODE_PATH=/opt/node22/lib/node_modules node tools/tiers.mjs --dir=projects/season1/still-dark
NODE_PATH=/opt/node22/lib/node_modules node tools/frame.mjs
mkdir -p /tmp/sd87 && git show 658a6fd:projects/season1/still-dark/index.html > /tmp/sd87/index.html
NODE_PATH=/opt/node22/lib/node_modules node tools/frame.mjs --dir=/tmp/sd87
python3 tools/renders.py
bash tools/selftest.sh
python3 tools/record_words.py
curl -sS https://frankbueltge.de/ghost-fleet/ | sha256sum
```

---

## 1. The arithmetic of both fractions, at all eight stops — PASS, nothing wrong

`day.py` computes the two ends as `obs / n_hi` and `obs / max(n_lo, obs)` — checked in the source,
not in a sentence about it: `projects/season1/capture/day.py:209-218`, the
`share_knowable_OBSERVED` block, with its own comment saying it at `:202-206` (*"the low end of the
band is obs / possible, the high end obs / max(certain, obs)"*). `data.py:230-231` builds
`fraction_falling = f"{n} of {b[1]}"` and `fraction_fixed = f"{n} of {max(b[0], n)}"` from the same
`n` and `b` the percentages at `:218-219` are rounded from. Same two quotients, same source fields,
one function.

Every stop re-run with its own `check` command. The face's numbers against the instrument's:

| stop (`--as-of`) | `day.py` prints | face percentage | face fraction | division |
|---|---|---|---|---|
| 2026-08-05T04:39:32Z | 100%–100% (11 of 0–11) | 100 % | 11 of 11 | 11/11 = 100 % |
| 2026-08-05T12:54:00Z | 79%–100% (11 of 0–14) | 79 % | 11 of 14 | 11/14 = 78.6 → 79 % |
| 2026-08-06T08:16:42Z | 69%–100% (11 of 0–16) | 69 % | 11 of 16 | 11/16 = 68.75 → 69 % |
| 2026-08-07T18:15:53Z | 65%–100% (11 of 0–17) | 65 % | 11 of 17 | 11/17 = 64.7 → 65 % |
| 2026-08-08T21:37:19Z | 55%–100% (11 of 0–20) | 55 % | 11 of 20 | 11/20 = 55 % |
| 2026-08-09T20:36:58Z | 44%–100% (11 of 0–25) | 44 % | 11 of 25 | 11/25 = 44 % |
| 2026-08-10T22:41:12Z | 35%–100% (11 of 0–31) | 35 % | 11 of 31 | 11/31 = 35.5 → 35 % |
| 2026-08-11T11:19:15Z | 33%–100% (11 of 2–33) | 33 % | 11 of 33 | 11/33 = 33.3 → 33 % |

The run therefore prints `11 of 11 → 11 of 33`, which is the prescription. The fixed end is
`11 of 11` at all eight, including the last, where `max(n_lo, obs) = max(2, 11) = 11`. The island is
byte-identical to a fresh build (`data.py --write --into` a scratch copy, then `diff`), so no
fraction on the face was typed.

## 2. `fraction_note` — the description is true, the tiers are right — PASS

- **Numerator.** `knowable_on_the_day_OBSERVED` = vessels this record places in 4 August that stood
  in an edition dated on or before it. Exactly one committed capture carries the 4 August edition
  (`2026-08-05T043932Z.json`, 11 vessels), and all eleven of its names are placed in the day
  (`day.py --as-of 2026-08-05T04:39:32Z` returns band 0–11 with OBSERVED 11). So *"the names the
  day's list had already given"* is a true description of the numerator as the record stands.
- **Denominator.** `b[1]` = certain + possible = 33, which the face's own band sentence already
  calls the ships that *could have been dark* on the day. True.
- **"The other end is 11 of 11 at every stop."** True — verified at all eight above — and computed,
  not typed: `data.py:693-702` branches on `len(set(fixed_fracs)) == 1` and carries an else-arm that
  prints both ends if the set ever splits.
- **"OBSERVED over DERIVED".** Right for both terms: the numerator is `day.py`'s OBSERVED count
  (`day.py:31-34`), the denominator is the band built from the published 7-day window, which is what
  this record calls DERIVED. Consistent with the legend at `still-dark/README.md:575-586`, which
  puts the spans and the share in DERIVED and this record's own accumulation in OBSERVED.

## 3. `cut.standing_note` — 11 and 230 are right, the tier word over them is not — BLOCKING

The two figures check out against the capture itself, not against a sentence:
`projects/season1/captures/2026-08-05T043932Z.json` holds 11 vessels and
`aggregates.disappearances_examined = 230`; it is the only committed copy of that edition.
`tools/tiers.mjs --dir=projects/season1/still-dark` exits 0 — no figure on the face lost its tier
word to the cut.

What the cut did lose is the clause that kept the numerator out of SOURCED.

- was: `— the list of 4 AUG named eleven ships out of the 230 disappearances it says it examined. No
  stop moves this figure. SOURCED — the count of names is this house's own.`
- is (`data.py:1012-1015`, island `index.html:734`, `STATE-1.txt:14`):
  `— eleven ships named, of 230 disappearances the list says it examined. SOURCED.`

This house's own legend says the count of names in a list is **DERIVED** — `the dark-and-return
spans, this page's share, and the count of names in each list` — and says why, in the sentence that
records the correction: *"upstream prints names, and this house counts them. Banked failure 41."*
(`still-dark/README.md:575-583`; failure 41 at
`git show abecba4:projects/season1/PROJECT.md`, line 260). The face now prints the words *eleven
ships named* with the single tier word `SOURCED` beside them. That is failure 41's error moved from
the legend onto the face, by subtraction — the shape of banked failure 25.

The defence recorded in the source is `data.py:1007-1008`: *"the numerator is the same eleven as the
row above and that row says whose count it is."* Two objections. First, the row above labels that
eleven **OBSERVED**, so the same numeral now carries two tier words in two adjacent rows and DERIVED
in the legend — a reader has three answers and no key. Second, the two elevens are not the same
quantity: the standing row's is `day_cut["printed"]`, the count of distinct names across copies of
the 4 August edition (`data.py:400,413`); the fraction row's is `knowable_on_the_day_OBSERVED`. They
are equal in the record as it stands and by nothing else, and no check asserts it.

**To pay:** put the attribution back on the row whose numerator this house counted — one clause, the
one that was there last night.

## 4. The stated justification for that cut is false about its own string — NOTED

`data.py:1004-1006` says of the shortened note: *"What survives is what no run can show — that these
two hundred and thirty are disappearances and not names, and whose count the numerator is."* The
surviving string does not say whose count the numerator is, and the very next sentence of the same
comment (`:1007`) says so: *"AND THE ATTRIBUTION IS NOT REPEATED HERE."* Two sentences of one comment
give opposite accounts of one string. Pays with finding 3.

## 5. The owed item's own figure is refuted by the instrument built tonight — BLOCKING

`tools/frame.mjs` was extended to report figure-top to hole-bottom, and it is sound: run against a
`git show 658a6fd` extraction of last night's page it reproduces session 87's hand figure exactly.

```
git show 658a6fd:projects/season1/still-dark/index.html > /tmp/sd87/index.html
NODE_PATH=… node tools/frame.mjs --dir=/tmp/sd87  → 390×844: hole-bottom 867 px of 844 — OVER by 23
NODE_PATH=… node tools/frame.mjs                  → 390×844: hole-bottom 943 px of 844 — OVER by 99
```

The head's frame block goes 179 → 255 px and the span 867 → 943: tonight's row costs 76 px, and the
owed item stands at **99 px, 943 of 844**, not 23. `PROJECT.md:150` (*"OWED AFTER 87. 23 px:
figure-top to hole-bottom at 390×844 is 867 of 844"*) and `WORKBOARD.md:64` (*"NOT FIXED, AND NOT
CLAIMED TO BE: 23 px"*) both stand in the live-state sections a stranger is sent to, and the build
commit `1003f95` touched neither: eight files, none of them the record's own state. The record now
publishes a figure its own new instrument refutes on the night it built it. The frame test proper
still holds — figure-top to controls-bottom 311 → 387 px of 844 — and that number moved tonight too.

**To pay:** restate both, with the cost of the row named. The instrument is not at fault; it is the
first thing tonight that could tell us, and it reproduces last night's hand figure to the pixel.

## 6. `142 px` is a measurement of a draft that no longer exists — BLOCKING

`data.py:1027-1029`: *"Cut to three short sentences before it was ever committed, on this head's own
arithmetic: the first draft of this clause cost 142 px of a phone frame for one row of numerals."*
The clause is indeed three sentences; the 142 px is not retrievable by anyone. No draft, no command,
no output records it; `grep -rn "142" projects/season1/still-dark/data.py` returns this line and
nothing else. I did not find it false. I found that it cannot be run, which is the shape banked as
failure 46 one session ago — *unrun figures in this house's own prose* — and this house does not get
to publish a px figure that only its author can vouch for.

**To pay:** the command that produced it, or the figure goes and the sentence keeps its argument.

## 7. Every quotation in tonight's changed comments — no invented quotation; one loose citation, NOTED

Checked byte for byte, ignoring only line-wrapping and bold markers.

- `data.py:221-227` and `index.html:2053-2062`, the ruling attributed to `DRAMATURG-87.md`:
  *"Placement was never the problem; units were … the falling figure must print its own fraction, not
  only its percentage, so that the run shows `11 of 11 → 11 of 33` while `11 of 230` stands
  underneath. Then the numerator repeats down the column, the denominators diverge, the run does the
  arguing, and the 11.52 px sentence can go."* — **present, verbatim**, at
  `DRAMATURG-87.md:105-110`. The ellipsis elides two whole sentences and nothing else.
- `data.py:999`, *"No stop moves this figure"* — verbatim in the string it replaced
  (`git show 658a6fd:projects/season1/still-dark/data.py`, the old `standing_note` at its `:957-960`).
- `tools/frame.mjs:67-68`, *figure-top to hole-bottom at 390×844* — verbatim at `PROJECT.md:150` and
  `WORKBOARD.md:64`.

**NOTED, the citation and not the quotation:** both files cite `:402` for that ruling
(`data.py:221`, `index.html:2053`). `DRAMATURG-87.md:402` restates it in different words —
*"Placement was never the fault; units are."* — and contains none of the quoted text, which runs
105–110. `index.html:2053` cites only `:105 and :402` for a quotation that ends at `:110`. A reader
sent to `:402` does not find what the marks promise.

## 8. Three further attributions in tonight's prose, each short of what it claims — NOTED, three

- `data.py:225`: *"The two figures in the frame had no digit in common at any of the eight stops."*
  False as written — `100 %` and `11 of 230` share the digits 1 and 0, at stop 0 and elsewhere. The
  memo's own words were *"the two figures in the frame do not share a term"* (`DRAMATURG-87.md:401`)
  and *"Eight states, and not one of them prints `11`. Not one prints a denominator either."*
  (`:71`), both of which are true. One word.
- `index.html:2050-2052`: *"the bottom row lost one sentence."* It lost one sentence, had its first
  sentence rewritten, and lost the attribution clause of finding 3. The description understates
  exactly the part that is blocking.
- `data.py:1029-1030`: *"a clause that outweighs the figure it labels is the thing `DRAMATURG-85.md`
  and `DRAMATURG-87.md` have now convicted twice on this face."* Both convictions are real
  (`DRAMATURG-85.md:145-147` at `994f214:`, `DRAMATURG-87.md:25`, `:78-79`), but their stated ground
  is *prose beside a run is annotation*, not weight. No quotation marks were used, so this is a
  recast attribution and not an invented quotation.

Nothing else in tonight's changed comments and strings carries a number, name or quotation I could
not run down. Banked failures 12, 25 and 31 are cited accurately (`e4cb780:` line 155, `f6ca3b0:`
line 178, `11bb78f:` line 185); *"this house has published that one twice"* is right — 31 and 33
(`11bb78f:` line 201). `DRAMATURG-82.md §3`'s rule is paraphrased accurately at
`f6ca3b0:projects/season1/DRAMATURG-82.md:134-139` (*"The head re-renders an unchanging clause 55
characters long on every beat while the visitor is looking for what changed. The clause should be
static and only the tail should move."*). The `11.52 px` sentence is `.sd-arrive-standing-note` at
`0.72rem` (`index.html:141`), which is 11.52 px at a 16 px root — and it is the class tonight's new
clause is set in.

## 9. The figure of the work as a whole, and the 25th capture — PASS, and the capture is genuine

```
$ python3 projects/season1/capture/day.py 2026-08-04 | head -6
day 2026-08-04  ·  25 capture(s) read, 8 distinct edition(s), 9 distinct content(s), 15 distinct bod(y/ies)
  SHARE knowable on the day ......... 33%–100%  (11 of 2–33)
```

25 / 8 / 9 / 15 and `33 %–100 %, 11 of 2–33` — the island's terminal block and `STATE-1.txt:346`
carry that output verbatim, and `data.py --check` prints *island matches the captures*.

The new capture's content digest is `a7ab0eb1…`, identical to the 24th: the edition stood still and
the **body moved**, 32,441 → 31,631 bytes, `e506a522…` → `e21f57d8…`. `page_assets` moved with it —
`/_astro/Base.P8Knfq78.css` → `/_astro/Base.yW6q2ssk.css` — so the move is attributable and not
guessed at. That is the **fifth of seven** such body moves in this record that `page_assets`
attributes (recomputed over all 25 captures), the fourth having been session 87's.

Checked first-hand rather than internally: `curl` of `https://frankbueltge.de/ghost-fleet/` returns
31,631 bytes whose sha256 is `e21f57d8c1e789832bf46f08e6b0b77fb21e66b78bbb4b2177ae8deadefc5067`,
byte-identical to the capture's recorded hash, with `/_astro/Base.yW6q2ssk.css` in the bytes. All 11
vessel names, all four aggregates, the case of the day and the printed edition date are present in
the live bytes. The capture is real.

## 10. `data.py --check`, renders, self-test, word ceiling — PASS

- `cd projects/season1/still-dark && python3 data.py --check` → *island matches the captures*, exit 0.
  Stronger, since `--check` compares parsed JSON and not bytes: rebuilding into a scratch copy with
  `--write --into` gives a file byte-identical to the committed one.
- `python3 tools/renders.py` → *RENDERS MATCH THE PAGE*, exit 0; `RENDERS.json` names index
  `0e212c99…`, which is the working tree's `index.html`.
- `bash tools/selftest.sh` → **SELFTEST PASSED**, exit 0.
- `python3 tools/record_words.py` → exit 0. **The word ceiling: 2,997 of 3,000 by `wc -w`, UNDER by
  3** (PROJECT.md 2,318 · WORKBOARD.md's live block 679; `str.split()` reference 3,084). Session 88's
  board entry and any repair to findings 3, 5 and 6 have three words of headroom, so something must
  come out by subtraction, which is this house's own rule for that ledger.

## 11. The stranger's figure is two sessions old — NOTED

`PROJECT.md:32` reads *"As of session 86: 33 %–100 % — 11 of 2–33, from 23 saved copies holding 8
distinct lists"*. Correctly dated, so not false; but the record now holds 25 copies, and this is the
section a stranger is sent to — the staleness session 86 banked against itself. `WORKBOARD.md:29`'s
*24 saved copies, 8 lists, 9 contents, 14 bodies* stands inside the block headed *live state as of
session 87* and is true of that night.

---

## VERDICT

**FAIL — three blocking (3, 5, 6), six noted (4, 7, 8 × three, 11).** Findings 1, 2, 9 and 10 found
nothing wrong and nothing was invented to fill them.

The build is arithmetically clean: eight stops re-run against the instrument agree with the face at
every one, both new fractions are the divisions the percentages already were, the branch that writes
*"The other end is 11 of 11 at every stop"* is computed and its sentence is true, the island is a
byte-exact build, and the 25th capture is verified against the live source page rather than against
itself. Tonight's prescription is genuinely built.

What fails is what the build cut and what it did not restate. A count this house makes itself now
stands on the face under the word SOURCED, which is the error this record banked as failure 41 and
which the deleted clause was there to prevent. The owed item the new instrument was built to measure
grew from 23 px to 99 px tonight and the record still says 23. And a px figure nobody can re-run went
into the source in the session after this house banked unrun figures as failure 46.

---
---

# RE-RUN — the object moved three times under this pass

**The original above is untouched.** It was measured on the build committed as `1003f95`
(`index.html` `0e212c99…`). Since then the session took the staging voice's §4 cuts, paid five of my
findings, and moved the page twice more. **Everything below is measured on `index.html`
`5325c15a7a30…`**, the state at the close of this pass — the hash was read immediately before and
immediately after every run in this section, and it did not move under any of them. Nothing here is
taken from the note that re-put me: every instrument was re-run.

## R1. Findings 3 and 4 — PAID, and the repair is right

`cut.standing_note` (`data.py:1010-1014`, island `index.html:734`, `STATE-1.txt:13`) now reads
`— eleven ships named, of 230 disappearances the list says it examined. SOURCED — the count of names
is this house's own.` The exception is back on the row whose numerator this house counts, and the
120-character string is 46 shorter than the 166 it replaced, so the repair was not a revert.

The comment beside it (`data.py:1009-1014`) now records the second objection as well: the two elevens
are `day_cut["printed"]` and `knowable_on_the_day_OBSERVED`, *"equal in the record as it stands and by
nothing else — no law joins them and no check asserts one"*. That is a true statement of what I found,
and it is now in the file rather than only in this memo. Finding 4 falls with it: the comment that
gave two accounts of one string is gone, and *"whose count the numerator is"* is true of the string
again.

## R2. Finding 6 — PAID by deletion

`grep -n "142" projects/season1/still-dark/data.py` returns nothing. The unrunnable px figure went
out with the block it stood in.

## R3. Findings 7 and 8 — PAID

- `data.py:221` and `index.html:2053` now cite `DRAMATURG-87.md:105-110`, which is the quotation's own
  range. The comment records why in the file (`data.py:224-229`).
- *"no digit in common"* is now *"shared no TERM at any of the eight stops — not one of them printed
  `11`, and not one printed a denominator"* (`data.py:229-230`), which is true and is the memo's own
  measurement.
- The comment that said the bottom row *"lost one sentence"* now names the rewrite and the attribution
  clause, and records that it understated it for an hour (`index.html:2047-2052`).

## R4. THE CUT I DID NOT SEE — `fraction_note` deleted, and it takes no tier word with it

The element, its write and the string are gone (`index.html`, the `#sd-arrive-frac-note` span,
`arrive.fraction_note`). The falling fraction now stands with no clause. Checked semantically and not
on the exit code:

- The head's own tier words are now `SOURCED` (on the standing row) and `DERIVED` (`arrive.tier`,
  *"DERIVED — this share is worked out here, from saved copies of those lists. Nobody publishes it."*).
  `11 of 33` is the share in ships — the same quotient as the percentage above it — and DERIVED is the
  word this record's legend gives the share (`still-dark/README.md:575-583`). The right word covers it.
- **The word OBSERVED is not in the head's scope, and was not before tonight either.** `tiers.mjs` on
  the published page (`658a6fd`) reports `#sd-arrive` as `SOURCED/DERIVED`; on tonight's commit it
  briefly read `SOURCED/DERIVED/OBSERVED`, which was the deleted clause; it reads `SOURCED/DERIVED`
  again now. The deletion restores the arrangement this session inherited. It is not a regression, and
  I am not going to bank it as one.
- What the deletion did lose is precision, and it should be known: the clause was the only place the
  face said in words that the numerator is OBSERVED and the total DERIVED. The numeral is not
  mislabelled; it is labelled once instead of twice.
- The claim the clause carried — *"The other end is 11 of 11 at every stop"* — is not orphaned: the
  fixed end still prints as `–100 %` in the row above, and `arrive.constant` still states the condition
  under which it holds. Nothing tonight's edits deleted has left a claim on the face without its source.
- `tiers.mjs --dir=projects/season1/still-dark` exits 0.

## R5. `#sd-arrive-constant` — byte-identical, moved, and the move is measured — NOTED

The string is unchanged, character for character, across all three states: comparing the parsed island
of `658a6fd`, `1003f95` and the working tree, `arrive.constant` is the same 235-character sentence.
It is not deleted; it is in the reading order at `STATE-1.txt:45`, after the controls and the names,
before the tier line.

Where it now stands, measured at both widths, at stop 0 and stop 7 (playwright, positions of
`#sd-arrive-constant` relative to the viewport top with no scroll):

| state | 390×844 | 1400×900 |
|---|---|---|
| published `658a6fd` | y 575–658 — on the first screen | y 317–384 — under the figure |
| committed `1003f95` | y 651–734 — on the first screen | y 380–446 — under the figure |
| now `5325c15a` | **y 1322–1434 — 478 px below the fold**, and below the 22 chips | y 765–821 — still on the first screen |

So on a phone the sentence stating the condition on the fixed end — this face's only statement of it,
and the sentence this house published false twice (banked 31 and 33) — is now off the first screen and
reached after the names it is not about. At 1400 it travels 448 px but stays inside the 900 px screen,
below the controls instead of above them. The staging voice ordered the
element cut for its 87 px *"subject to §7.5"*, and §7.5 says of that cut *"I have not decided that, and
I do not order it"* (`DRAMATURG-88.md:375-377`, `:334-336`). Moving it instead keeps the sentence,
which is the better half of the trade; the cost is a phone reader who meets `–100 %` at y 359 and its
condition 963 px later. Noted, not blocked: no figure is unlabelled and no source is deleted.

## R6. Finding 5 — PAID in the object, and the owed item is GREEN for the first time

```
NODE_PATH=… node tools/frame.mjs        (index 5325c15a7a30…)
  phone 390×844 — figure-top to controls-bottom: 317 px of 844 — HOLDS
                  figure-top to hole-bottom:     786 px of 844 — HOLDS
  wide 1400×900 — figure-top to controls-bottom: 495 px of 900 — HOLDS
                  figure-top to hole-bottom:     364 px of 900 — HOLDS
```

**786 of 844 — 58 px of slack.** The item that stood 23 px over for a session, and 99 px over at
tonight's commit, holds. Every px figure the two voices used reconciles across the four states I
measured myself, and none of them had to be taken on anybody's word:

```
867  published 658a6fd (frame 179 px)
+104  the new row as first built
 −28  standing_note trimmed 166 → 79 characters
=943  committed 1003f95 (frame 255 px)   ← this is the 99 px over
 −86  the clause deleted            → 857, the staging voice's own predicted figure
 +16  the attribution restored (79 → 120 characters), my finding 3
 −87  #sd-arrive-constant out of the spine
=786  now, 5325c15a (frame 185 px at 390, 161 px at 1400)   ← HOLDS
```

**The record has not caught up.** `PROJECT.md:150` still reads *"OWED AFTER 87. 23 px: figure-top to
hole-bottom at 390×844 is 867 of 844"* and `WORKBOARD.md:64` still reads *"NOT FIXED, AND NOT CLAIMED
TO BE: 23 px"*. Until they land, the record publishes a stale figure in the section a stranger is sent
to, and the true one is the line above: **786 of 844 at 390×844, HOLDS, 58 px of slack, at index
`5325c15a…`** — measured, not predicted. Neither *857* nor *168 px* nor *−11 px on a phone* is a figure
of the shipped object: those were measured on a page whose standing note was 41 characters shorter than
the one that ships.

## R7. The eight fractions after the rebuild — still exact — PASS

The island was rebuilt twice more tonight; `data.py --check` prints *island matches the captures* and
`--write --into` a scratch copy still returns a byte-identical file. The eight `share_falling_of`
values read out of the current island are `11 of 11 · 14 · 16 · 17 · 20 · 25 · 31 · 33`, unchanged
from the table in finding 1 and still equal to the percentages beside them, and every
`share_fixed_of` is `11 of 11`. `share_fixed_of` now has no consumer on the face and is kept in the
island deliberately (`data.py:691-693`); it is computed at every stop and prints nowhere, which is a
field, not a claim.

## R8. One miscitation in the new comments — NOTED

`data.py:683-690` and `index.html:2064` both attribute to **`DRAMATURG-88.md` §3** the sentence
*"The row is worth it. The clause is not, and the clause is 86 of the 104 px."* and the 86/104 px
measurement. The quotation is real and byte-exact — but it stands at **`:258-259`, in §4**, and the
104 px accounting with it at `:235`. The other four items in that same list are §3's
(`:134` the 166 → 307 characters, the heading at `:125` for the re-told sentence, `:163-165` for
`11 of 11` printed twice at stop 0, `:173-177` for the 92 px). §3 ends at `:196`. One character of
repair; the same class as finding 7, one file later.

## R9. Everything else on the closing state — PASS

- `python3 tools/renders.py` → *RENDERS MATCH THE PAGE*, and the page it names is `5325c15a7a30…`.
  (Between the two edits this pass caught it STALE, with `STATE-1.txt` still printing the deleted
  clause; the session re-rendered. It matches now.)
- `bash tools/selftest.sh` → **SELFTEST PASSED**, exit 0.
- `NODE_PATH=… node tools/fold.mjs` → **88 failure(s)**, the committed page's own count, unmoved by
  tonight's edits.
- `python3 tools/record_words.py` → exit 0, **2,997 of 3,000 by `wc -w`, UNDER by 3**. Unchanged: the
  two files it measures have not been touched tonight, which is the same fact as R6's last paragraph.
- `python3 projects/season1/capture/day.py 2026-08-04` → 25 captures, 8 editions, 9 contents, 15
  bodies, `33 %–100 %  (11 of 2–33)`, as in finding 9. The 25th capture is still the one I checked
  against the live source page by hash.
- No new number, name or quotation in the changed comments is unrun: the character counts (166 → 79,
  228, 307) I re-measured on the strings themselves; the px figures reconcile in R6; the quotations
  are byte-exact at the lines named, with the one exception in R8.

---

## RE-RUN VERDICT

**PASS on the object — three blocking findings all paid, two noted (R5, R8), one item open outside
it.**

The face is right where it counts: every fraction is the division its percentage is, at all eight
stops; the count this house makes itself is attributed again; the numeral the staging voice ordered
built stands with the right tier word over it; nothing that was deleted tonight took a claim's source
with it; and the item that has been red since it was first measured is green at 786 of 844, by the
instrument this session built for it and which reproduces last night's hand figure to the pixel.

The open item is not in the work but in the record: `PROJECT.md:150` and `WORKBOARD.md:64` still carry
23 px. I will re-check them when they land. Until then, this memo, not the board, holds the true
figure.
