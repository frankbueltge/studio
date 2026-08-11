# VERIFIER — STILL DARK, increment of session 85

**FAIL — three blocking items.**

Everything below was established by running the command named beside it against the files
themselves. Nothing here is taken from the session's description of its own work; where I
could not check something I say so and say why.

**The state I checked.** The tree moved twice under this pass (finding 10). Every finding
is against these bytes, at 2026-08-11 05:06:42 UTC:

```
7fbd3d5f498955cf…  projects/season1/still-dark/index.html
1124d8683ebb6b0d…  projects/season1/still-dark/data.py
7ac516f9fd7b2c17…  projects/season1/capture/capture.py
687eeb0b05fa04b8…  projects/season1/still-dark/README.md
835583afd8282a3d…  projects/season1/captures/2026-08-11T044745Z.json
```

---

## 1. BLOCKING — the new block's SOURCED claim is not exactly right, and one number now carries two tier words on one face

`still-dark/data.py:826`, printed at `still-dark/index.html:646`:

> `SOURCED — every figure in this block is read off the saved copies, in the words the parser matched in them.`

It is a universally quantified claim ("every figure"), and it is false for at least two of
the figures standing under it.

**(a) `11 names printed` is not a figure any saved copy prints, and no parser pattern
matched those words.** It is this house's own count of parsed vessel entries —
`data.py:388` builds the name set, `data.py:401` takes its length, `data.py:796` prints it.
Upstream publishes 82 / 230 / 5,641 / 3,712 in its aggregates and publishes no count of the
names it printed. I recomputed it:

```
$ python3 - (over projects/season1/captures/*.json)
2026-08-04 copies 1 percopy [11] union 11 examined 230 window 5641 natwaters 82
```

The count is right. The tier sentence over it is not: it was not "read off … in the words
the parser matched", because the parser matched no words for it.

**(b) `the seven lists it holds` is a fact about this record, not about a saved copy.**
It is `len(cut_rows)` — the number of distinct editions this house has fetched. By
`capture/capture.py:22–23`'s own definitions that is OBSERVED ("this house's own record of
when it could first know"), not SOURCED. It sits inside the block the SOURCED line closes.

**(c) The same `11` stands under a DERIVED word four blocks lower on the same face.** From
the built island:

```
lede: "Eleven of the ships this record can place in 4 August 2026 stood in the list dated
4 August itself. … All three counts are DERIVED: worked out here, from saved copies of
those lists."
```

Both labels are individually arguable — counting names on a page is direct reading; placing
a ship in a day is band arithmetic — and the two quantities happen to coincide at 11. A
visitor cannot tell that. This is the shape of banked failure 25, and the same confusion is
written into the source: `index.html:2329–2332` calls them "four aggregate figures the
lists themselves publish", which is untrue of one of the four.

**(d) What a match of `AGG_RE` does and does not prove.** I checked this directly rather
than reasoning about it. The pattern (`capture/capture.py:89–94`) contains the literal runs
`ships went dark inside national waters lately`, `— of`, `disappearances examined (`,
`in the window).`, with no wildcard inside them — so a match *does* prove those words stood
in those bytes in that order with those two numbers in them. That part of the claim holds.
But the first group is separated from the sentence by `.*?`, so the parser binds the
"82" to the sentence only by its being the first `tabular-nums">…</p>` in the document. I
fetched the live edition myself:

```
$ curl -sS -o gf.html -w "%{http_code} %{size_download}\n" https://frankbueltge.de/ghost-fleet/
200 32348
$ sha256sum gf.html
e5ddbb89a5875accae0aa794dc6ea2a749c5b7225e8e4f0cea9458c4507decd2
$ grep -o 'tabular-nums[^<]*<' gf.html
tabular-nums">91<
```

Exactly one such element, so the binding holds today, and today's capture
(`2026-08-11T044745Z.json`) confirms it in its own new `aggregates_text`:
`"91 ships went dark inside national waters lately — of 213 disappearances examined (5,645 in the window)."`
For the list of **4 August** this cannot be checked at all: the captures store the body's
sha256, not its bytes, and that edition is gone from the wire. The claim "in the words the
parser matched in them" is therefore strongest precisely where it is least checkable, and
the face does not say so.

**The repair is one sentence.** Something of the shape: *the three aggregate figures are
read off the saved copies in the words the parser matched in them; the count of names, and
the count of lists, are this house's own.*

**What is NOT wrong here, checked and cleared:** nothing in the new block is set in
quotation marks, so nothing is offered as a quotation the record cannot support. The two
quotations elsewhere on the face I verified verbatim against the live method sheet
(`curl -sS https://frankbueltge.de/werke/ghost-fleet/` → 200, 27,748 bytes): both
`Daily. Window: disabling events that ended in the last 7 days (complete vanish-and-return stories).`
and `The AIS picture of the seas looks complete. It is not — ships switch off their transponder on purpose to vanish.`
stand there word for word.

## 2. BLOCKING — the since-note's last sentence collapses the one distinction this work exists on

`still-dark/data.py:757`, printed at `still-dark/index.html:639`:

> `By the last stop twenty names stand in that space, and not one of them can be ruled out
> of the list dated 4 AUG: … The first list that could add a name ruled out of that day
> would be one dated 12 August 2026.`

**Both numbers are right.** I re-derived them from the captures and `capture/day.py`'s band
logic without reading the page's code first:

```
$ python3 -  (day.bands / day.analyse over projects/season1/captures)
certain 0 possible 31 total 31
band [0, 31] obs 11 share [0.3548, 1.0]
later 20
not_ruled_out 20
```

`bands(row)` returns `(first_edition_date − 7, first_edition_date)`. A name can be excluded
from the list dated 4 August only when `first_edition_date − 7 > 2026-08-04`, i.e. from
`2026-08-12`. An edition of 11 August gives a band opening exactly on 4 August and is *not*
excluded. So `first_excluding = DAY + 8 days = 2026-08-12` (`data.py:426`) is correct, and
20 of 20 is correct.

**The defect is the referent.** The clause that governs the computation says *"ruled out of
the list dated 4 AUG"* — correct. The closing clause says *"ruled out of that day"* — a
different object. Under the literal reading the sentence is false: names ruled out of the
*day* never enter that block at all (`analyse` drops them), and every list since 5 August
has added such names. The page's own ledger caption, three blocks lower, is the sentence
that makes this a blocking matter rather than a quibble: *"a ship leaves the list as that
window moves past it. It never leaves the day."* The work cannot spend one caption drawing
that line and one sentence erasing it.

Repair: `a name ruled out of that list`. One word.

**The structural disclosure itself is adequate.** The face does not present 20 of 20 as a
finding: it gives the mechanism ("a list gives a return only to the nearest seven days") and
names the date after which the number can differ. A reader can see the result is forced.
That check passes.

## 3. BLOCKING — `still-dark/README.md:21` points a stranger at a document that does not say what it is said to say

> `that ../capture/capture.py has parsed since the first night, that ../capture/README.md
> tiers SOURCED`

```
$ grep -cEi "sourced" projects/season1/capture/README.md
0
```

`capture/README.md` contains no tier word for the aggregates at all; it tiers only DERIVED
and OBSERVED, for `day.py`'s two answers (lines 36–42). The aggregates are tiered SOURCED in
`capture/capture.py` (docstring line 17, and the `tiers` block at line 297) and in every
capture's own `tiers.SOURCED` field. `PROJECT.md` says this correctly ("tiered SOURCED in
our own capture file"); the README, rewritten tonight, does not. This is the document
`PROJECT.md` says a stranger reads first, and the claim is a one-grep check that was not run
— which is the exact species of banked failures 24 and 28.

Same paragraph, same sentence: "four figures that stand in every capture this record holds"
is untrue of one of the four (see finding 1a) — `11` stands in no capture as a figure.

## 4. NOTED — the refusal is defensible and the critic's §2 arithmetic is not, and this should be said plainly

`KRITIKER-84.md` §2: *"Double the list length and the figure roughly halves; publish all 213
and it collapses."* **That is wrong, and the house was right to decline it.** The claim
holds the numerator fixed at 11. The numerator is the count of names in the list dated
4 August — one of the lists being lengthened. Double every list and both ends of the
quotient roughly double, leaving the share roughly where it stands; publish every examined
disappearance and the numerator becomes every disappearance that ended by 4 August, which is
a real ratio, not a collapse.

The house's own sentence (`data.py`, `arrive.cut.refused`) — *both ends would grow and
nothing in this record measures by how much* — is exactly right, and its first limb is not
hypothetical: I verified that all 20 later names have `bands()[0] ≤ 2026-08-04`, so all 20
are names a longer list dated 4 August could have carried. Declining to publish a direction
is not a false claim; publishing the critic's would have been the third false sentence about
this quotient in three sessions.

The critic's *second* claim in that paragraph — that the cut is by duration and so favours
long gaps — **is** supported by the record, and the house neither adopts nor disputes it.
Both editions I opened are ordered strictly descending by `days_dark` (4 August: 56, 39, 31,
26, 22, 18, 17, 17, 17, 17, 16), and upstream's own method sheet says it outright:
*"case of the day by region brisance, then duration. The index counts all examined; the case
and list show named vessels."*

## 5. NOTED — upstream says the thing the face infers, in words, at a retrievable address

That last sentence — *"The index counts all examined; the case and list show named vessels"*
(<https://frankbueltge.de/werke/ghost-fleet/>, fetched by me at 200, 27,748 bytes) — is the
strongest possible support for the whole block and is cited nowhere on the face or in the
README. The block currently rests on this house's inference from the four numbers. Not a
defect. It would make finding 1 easier to repair.

## 6. NOTED — the union rule is in the source only, and it happens not to matter tonight

`data.py:379–383` states that names-printed per edition is the UNION over that edition's
saved copies, and why (the 10 August edition holds ten names in its two earlier copies and
eleven in its three later ones, after the parser repair of session 84). Nothing on the face
says this. I checked whether it changes any printed figure:

```
2026-08-04 percopy [11] union 11        2026-08-08 percopy [6,6,6,6]     union 6
2026-08-05 percopy [8,8,8] union 8      2026-08-09 percopy [9,9]         union 9
2026-08-06 percopy [7,7,7,7] union 7    2026-08-10 percopy [10,10,11,11,11] union 11
2026-08-07 percopy [6,6,6] union 6
printed min/max 6 11   ·   examined min/max 213 250
```

Min 6 and max 11 are identical under both rules (the 11 also comes from 4 August, whose only
copy holds eleven), so "six to eleven names of the 213 to 250 disappearances" is true either
way and the 10 August edition is not being flattered. The rule becomes load-bearing the
moment a per-edition count reaches the face; it does not tonight. Handled honestly, said in
the wrong place.

## 7. NOTED — the ledger caption stopped pointing by position and started pointing at names the table does not use

`data.py:1197` and `data.py:1207`, printed at `index.html:1759`:

> `The SHIPS column counts …` … `EXAMINED is what that same copy says the instrument
> examined …`

The rendered header row (`index.html:2572`, confirmed in `STATE-1.txt:291`) reads:

```
fetched (UTC)	status	bytes	body sha256	content	edition	ships in that list	disappearances examined
```

There is no column named SHIPS and none named EXAMINED. The positional pointer is correctly
gone and the caption's two sentences are in the table's own column order, so nothing is
false — but a caption that names a column should use the column's name. Recommend
*"the `ships in that list` column"* and *"`disappearances examined` is …"*.

The column's values are right: I recomputed `examined` for all 22 rows against the captures
and every one matches (230 / 236×3 / 234×4 / 242×3 / 250×4 / 227×2 / 213×5). The null branch
at `index.html:2585` (em dash, never a nought) never fires — every capture in the record
carries an aggregates block.

## 8. NOTED — the SOURCED legend covers one of the two upstream figures the face began printing tonight

`index.html:2332–2333`:

> `SOURCED  name · flag · days dark · waters · each list's own date and ship count · what
> each list says it examined — printed by the instrument`

The face now prints three upstream aggregates. `examined` is covered; `5,641 events in the
window` and `82 … dark inside national waters` are not. The source comment beside it
(`index.html:2329–2332`) says the addition is made "in the same commit as the figures"
because "a legend that does not cover a published value is failure 25 waiting to happen a
fourth time" — by its own standard it is two values short. The block carries its own tier
word, so no figure stands unmarked (finding 9); this is the legend, not the mark.

Same line, pre-existing and worth one sentence: *"each list's own date and ship count —
printed by the instrument"* is not true of the ship count. The instrument prints names; this
house counts them. That is finding 1(a) already living in the legend.

## 9. NOTED — the instruments all pass, and one of them says what it does not prove

```
$ cd /home/user/studio/projects/season1/still-dark && python3 data.py --check
island matches the captures                                          (exit 0)

$ (extract #sd-data from index.html, compare to `python3 data.py`)
byte identical: True

$ cd /home/user/studio && python3 tools/renders.py
  RENDERS MATCH THE PAGE                                             (exit 0)

$ cd /home/user/studio && NODE_PATH=/opt/node22/lib/node_modules node tools/tiers.mjs
TIERS: every printed figure stands in a scope carrying a tier word.  (exit 0)
```

`--check` compares parsed JSON, not bytes (`data.py:1298`), so I did the byte comparison
separately; it holds. `tiers.mjs` prints its own limit — *"Scope is structural, not semantic:
this says a tier word is present, never that it is the right one"* — and findings 1 and 8
are exactly what it cannot see. No DERIVED figure stands unmarked; the defects are in which
word, not whether there is one.

**The figures re-derived from `captures/2026-08-05T043932Z.json`, first-hand:**
11 names · 230 disappearances examined · 5,641 in the window · 82 dark inside national
waters. All four confirmed. `content_sha256` did not move on the night the parser changed:
`2026-08-10T224112Z`, `2026-08-11T043904Z` and `2026-08-11T044745Z` all compute
`423c17df1ef6…`, so `aggregates_text` is genuinely outside `edition.CONTENT_FIELDS`
(`('edition_date_printed', 'edition_date', 'aggregates', 'case_of_the_day', 'vessels')`), and
`2026-08-11T044745Z.json` is indeed the first and only capture holding the verbatim spans.
Both new captures are `200`, 32,348 bytes, sha256 `e5ddbb89…` — identical to a body I fetched
myself.

## 10. NOTED — the object changed twice while it was being verified, and the change list I was given was incomplete

`index.html`, `data.py`, `README.md`, `STATE-1.txt` and both renders were rewritten at
05:01–05:02 UTC and again at 05:05 UTC, during this pass. The differences are not cosmetic:
the block's figures line I first read was

> `11 names printed · 230 disappearances examined · 5,641 in the window · 82 of them dark inside national waters`

and what now stands is

> `11 names printed · 230 disappearances examined, 82 of them dark inside national waters · 5,641 events in the window`

— which is a genuine improvement (in the first version the nearest antecedent of "of them"
was 5,641, not 230), and `arrive.cut.said` was rewritten in the second edit. I re-ran every
instrument and re-derived every figure against the final state; that is why the hashes are
at the head of this memo. **This is banked failure 29's shape** — a face changing under the
voice measuring it — and the record should say so whichever way tonight goes.

Separately: **the largest correction of the night was not in the change list I was given.**
`data.py:514` changed `min` to `max` in the stops' as-of instant. It is right, and it repairs
something that shipped in session 84: with `min`, the run's last stop stood at
`2026-08-10T17:47:21Z`, when this record held ten names of that list, so the head ended on
`37 %–100 %` — the share of a total of thirty — under a block of thirty-one chips, while the
body of the same page published `35 %–100 %, 11 of 0–31`. I verified both states:

```
$ python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-10T17:47:21Z
  SHARE knowable on the day ......... 37%–100%  (11 of 0–30)
$ python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-10T22:41:12Z
  SHARE knowable on the day ......... 35%–100%  (11 of 0–31)
$ python3 projects/season1/capture/day.py 2026-08-04
  SHARE knowable on the day ......... 35%–100%  (11 of 0–31)
```

Every one of the seven stops now reproduces under `--as-of` (100, 79, 69, 65, 55, 44, 35),
and the last stop equals the live figure, so `run_states.done` — *"The figure now standing is
this record's live one"* — is true again. A verifier who had only been given the list of
changes would have passed over the correction that mattered most.

## 11. NOTED — smaller things, none of them blocking

- `arrive.cut.said`: *"this record has saved them every night since the first"*. Read with
  "them" = the four figures of the 4 August list, that is false — the 4 August edition has
  exactly one saved copy. Read with "them" = the aggregates block, it is true, and every
  night is covered (5–11 August, no gap). Third sentence in this block whose nearest
  antecedent gives the false reading; the other two were repaired mid-pass and in finding 2.
- `still-dark/README.md:18–19` keeps the ordering the face abandoned at 05:02: *"5,641 events
  in its window, of which 82 ships dark inside national waters"*. Harmless — 82 ⊂ 230 ⊂ 5,641
  on upstream's own construction, so both readings are true statements — but the README now
  disagrees with the face it documents.
- `arrive.tier` (`DERIVED — … each of which prints six to eleven names of the 213 to 250
  disappearances it says it examined. Nobody publishes it.`) puts four SOURCED figures inside
  a sentence whose only tier word is DERIVED. The words *"it says it examined"* attribute
  them to upstream in plain language, which is why this is not blocking; the DERIVED word
  governs the share, and the share alone. It is the weakest joint left after finding 1 is
  repaired.
- A fourth SOURCED aggregate — `vessel_days_of_darkness_approx`, 3,712 for 4 August — is
  parsed, stored, given a verbatim span from tonight, and printed nowhere. The choice is
  argued in the source. Recording it so the next pass does not have to rediscover it.
- Checked and correct: *"fifteen of them after this page had printed its figure"* (recomputed
  as of `91ee19b`, 2026-08-06T08:36:39Z → 15); *"Five lists came back in more than one set of
  bytes each"* (recomputed → 5); `first_dwell_ms` 14,118 (56 words / 238 wpm); *"It fell
  thirty-four points"* (69 → 35); *"the last of them six days after the day had ended"*.

---

## What has to change before this ships

1. The SOURCED line at `data.py:826` must stop claiming every figure in the block, or the
   two figures it does not cover must leave the block.
2. `data.py:757`: `that day` → `that list`.
3. `still-dark/README.md:21`: the aggregates are tiered SOURCED in `capture/capture.py`, not
   in `capture/README.md`.

All three are one-line repairs. Findings 4, 5, 7, 8 and 11 are not blocking and I do not ask
for them tonight. **Any repair re-runs this pass on the changed state** — and on tonight's
evidence that is not a formality.

*Facts and tiers only. This memo takes no position on the block's placement, its typography,
its length or its prose, which are not mine to judge.*

---

## RE-RUN ON THE REPAIRED STATE

**Verdict at the foot of this section.** Everything below was re-established first-hand
against the files as they now stand; I re-derived every load-bearing figure again rather
than carrying anything over from the pass above.

**The state I checked**, at 2026-08-11 05:25:42 UTC (unchanged throughout this pass):

```
5ad761941e486f29…  projects/season1/still-dark/index.html
9a4e25e502ab916b…  projects/season1/still-dark/data.py
7ac516f9fd7b2c17…  projects/season1/capture/capture.py
c398d0a62609944d…  projects/season1/still-dark/README.md
9cb7f91f0decde27…  projects/season1/still-dark/STATE-1.txt
```

### R0. The instruments, all five

```
$ cd projects/season1/still-dark && python3 data.py --check
island matches the captures                                          (exit 0)

$ (extract #sd-data from index.html, compare to `python3 data.py`)
byte identical: True

$ python3 tools/renders.py
  index.html   5ad761941e48…  the page the renders were made from
  RENDERS MATCH THE PAGE                                             (exit 0)

$ NODE_PATH=/opt/node22/lib/node_modules node tools/tiers.mjs
TIERS: every printed figure stands in a scope carrying a tier word.  (exit 0)

$ python3 tools/chronicle.py
CHRONICLE: 84 entries, all inside the contract in SITE-API.md        (exit 0)
```

**No figure moved.** Re-derived from the captures, not from the page: band `[0, 31]`,
numerator 11, share `[0.3548, 1.0]`; 7 editions; names printed per edition 6 to 11;
examined 213 to 250; the list of 4 August at 11 names / 230 examined / 5,641 in the window /
82 dark inside national waters; `later` 20, `not_ruled_out` 20, `first_excluding`
2026-08-12; all seven stops reproducing at 100, 79, 69, 65, 55, 44, 35 with the last equal
to the live figure; all 22 `examined` cells matching their captures.

### R1. §1 PAID — the SOURCED claim is now honest, and under-claims where it used to over-claim

`arrive.cut.tier` now reads:

> `SOURCED — the three figures the list published, read off the saved copies in the words the
> parser matched in them. The count of names, and the count of lists below, are this house's own.`

Checked figure by figure. The block prints three upstream figures (230 · 82 · 5,641), and
they are exactly the three the list of 4 August published in that sentence; the count of
names (11) and the count of lists (seven) are now excepted in words and are exactly the two
figures I found standing wrongly under the old sentence. The exception is not decorative —
the legend follows it: the ship count has moved off the SOURCED line and onto the DERIVED
line, and the lede has always called it DERIVED, so the same number no longer carries two
tier words on one face. **Finding 1(a), 1(b) and 1(c) are discharged.** `tiers.mjs` still
exits 0 and `arrive.cut.tier` is `SOURCED/DERIVED` in scope.

Residual, NOTED, not blocking: `cut.kept` prints `213 to 250 disappearances` — upstream
figures belonging to the lists of 10 and 8 August, not among "the three figures the list
published", and not covered by "the count of names" or "the count of lists". The
enumeration now under-claims where it used to over-claim, which is the safe direction, and
each of those figures carries its own in-words attribution (*"it says it examined"*). Worth
one word next time (*"the figures the lists published"*).

Also NOTED: the one figure in the new material with no tier word of its own is the derived
date `12 August 2026`. Its derivation is spelled out in the same sentence that prints it
("a list gives a return only to the nearest seven days, so …"), which is stronger than a
label, which is why I do not block on it.

### R2. §2 PAID — the sentence is true, and the branch is true tonight

`data.py:766–776`, printed at `index.html`'s `since_note`:

> `This record cannot tell a ship that came back later from a ship the list did not print: a
> list gives a return only to the nearest seven days, so the return window of every name
> added since 4 August still reaches back to it. The first list that could add a name ruled
> out of that list would be one dated 12 August 2026.`

`that day` → `that list` ✓. Re-derived independently: `bands(row) = (first_edition_date − 7,
first_edition_date)`; all 20 later names have `bands()[0] ≤ 2026-08-04`; exclusion first
becomes possible at `2026-08-04 + 8 = 2026-08-12`; an edition of 11 August opens its band
exactly on 4 August and is not excluded. Both numbers right, the date right, and the
structural nature still disclosed in the sentence itself.

**The branch, checked as asked** (`data.py:769–774`). At `k < n` it produces *"the return
window of {k} of the {n} names added since 4 August still reaches back to it"* — true, and
grammatical. NOTED: in that branch the **opening** clause stays absolute — *"This record
cannot tell a ship that came back later from a ship the list did not print"* — while the
clause after the colon then says only k of n. With one name excluded, the record *can* tell
that one apart, so the opening would be over-broad. It is true tonight because k = n, and it
cannot become false before 12 August; repairing it now is cheap and repairing it later is
the same failure family as 31 and 33.

NOTED: the repair traded an explicit antecedent for an implicit one. `the list dated 4 AUG`
is gone from the sentence, and after the restaging the sentence stands below the controls,
where the nearest preceding list-nouns are `those lists` (plural) and the caption's generic
`the list`. Nothing is false; a cold reader has to reach up to the block's heading for the
referent.

### R3. §3 PAID — and the same document now contradicts the face somewhere else

```
$ grep -cEi "sourced" projects/season1/capture/README.md
0
```

`still-dark/README.md:20–23` now says the aggregates are tiered SOURCED by `capture.py` —
its docstring and the `tiers` block it writes into every capture — and states plainly that
`capture/README.md` tiers only `day.py`'s two answers. Both halves are true against the
files. The same paragraph now names three upstream figures in the face's own order and marks
the count of eleven names apart as this house's own. **Findings 3 and 11(README ordering) are
discharged.**

### R4. BLOCKING — the README's tier legend now states the opposite of the face's

`still-dark/README.md:377–378`, rewritten tonight:

> `- **SOURCED** — `name · flag · days dark · waters`, each list's own date and ship count,
>   and **what each list says it examined**, printed by the instrument …`
> `- **DERIVED** — `the dark-and-return spans, and this page's share` …`

The legend on the page it documents (`STATE-1.txt:76–77`, built from `index.html`) reads:

```
SOURCED name · flag · days dark · waters · each list's own date · what each list says it
        examined, how many of those were inside national waters, and how many events were
        in its window — printed by the instrument
DERIVED the dark-and-return spans, this page's share, and the count of names in each list
        — worked out here, both ends printed
```

Two contradictions, both about tiers:

1. **The ship count.** The README puts it under SOURCED and calls it *"printed by the
   instrument"*. The face, on this pass's own finding 8, moved it to DERIVED — *"the count
   of names in each list — worked out here"* — and `arrive.cut.tier` says the same thing in
   the head (*"The count of names … are this house's own"*). The document a stranger reads
   first now assigns a tier the work itself denies, to the figure this whole increment was
   about.
2. **The two other aggregates.** The README's SOURCED bullet names one of the three upstream
   figures the face's legend now names; `82 … inside national waters` and `5,641 events in
   the window` are absent, and the DERIVED bullet is missing the count of names.

`git show HEAD:…/README.md` shows this bullet read only *"name · flag · days dark · waters,
printed by the instrument"* before tonight, so both lines were **written tonight**, against
an intermediate state of the face, and were not re-read after the legend moved. That is
banked failures 24 and 28 in the same paragraph as their own correction. It is two lines.

### R5. §4 PAID — the quotation is verbatim, and SOURCED is the right tier for it

```
$ curl -sS -o gfm2.html -w "%{http_code} %{size_download}\n" https://frankbueltge.de/werke/ghost-fleet/
200 27748
$ sha256sum gfm2.html
a702381f7e98172e1ea50b27499327ea12dd2601fc62897e2b5bf21303da8e44
```

The quoted span on the face is

> `The index counts all examined; the case and list show named vessels.`

and it stands in the method sheet's raw HTML as one uninterrupted run — no tags, no
entities, no normalisation — semicolon and closing full stop included:

```
…→ case of the day by region brisance, then duration. The index counts all examined; the
case and list show named vessels.</p>
```

It opens and closes on sentence boundaries, so no ellipsis is owed. The curly quotes are the
page's own; the quoted text does not contain any. **Word for word, punctuation included, it
holds.**

**Ruling on the tier.** SOURCED is right. It is a genuine short quotation (eleven words) from
a named third-party document, attributed on the face (*"in its method sheet"*), publicly
retrievable, and it says in upstream's own words the thing the block otherwise had to infer
from four numbers — which was my finding 5. PROTOCOL's legal-hygiene rule (4) permits
exactly this. Two qualifications, both NOTED:

- The block's tier line says its figures are *"read off the saved copies"*. This sentence is
  **not** from a saved copy — the method sheet is not captured by `capture.py`, and no
  capture in this record holds it. The tier line enumerates figures only, and the quotation
  carries its own attribution, so nothing is misstated; but the block's declared basis and
  this sentence's actual basis are two different things and the face does not say so.
- Its attribution carries no address of its own. The method sheet's URL is on the page
  exactly once — as the href behind the word `frankbueltge.de` in the definition block
  (`index.html:2297–2299`), twelve lines lower. That is a retrievable address on the same
  page, so banked failure 27 is not repeated; naming it at the new quotation would cost
  three words.

For completeness I re-verified the other three quotations the face carries: the window
sentence and the AIS-picture sentence both stand verbatim on the method sheet fetched
tonight, and the self-quotation *"A ceiling that can only fall…"* opens at the commit the
face names —

```
$ git show 91ee19b:projects/season1/still-dark/index.html | grep -c "A ceiling that can only fall…"
1
$ git show -s --format=%cI 91ee19b
2026-08-06T08:36:39+00:00
```

— matching the face's *"printed on this page 6 August 2026 at 08:36 UTC, in commit 91ee19b"*.

### R6. §5 PAID — the caption names the columns the table prints

`STATE-1.txt:290` against `STATE-1.txt:293`:

```
caption: … The “ships in that list” column counts … “Disappearances examined” is what that
         same copy says the instrument examined …
header:  fetched (UTC) status bytes body sha256 content edition ships in that list
         disappearances examined
```

Both names now match the printed headers exactly, in the table's own column order. NOTED and
trivial: the second is capitalised (`Disappearances`) because it opens a sentence, so the
quoted string is one character off the header it quotes.

### R7. §6 PAID — the confession is true, and its referent is now fixed

`arrive.cut.kept`, rendered below the controls (`STATE-1.txt:53`):

> `Each of the seven lists this record holds prints six to eleven names of the 213 to 250
> disappearances it says it examined. This record has saved that block every night since the
> first, and no face of this work printed one of its figures until tonight.`

`that block` — the aggregates block — replaces the pronoun I flagged. Checked: all 22
captures carry an `aggregates` block, on every night from 5 to 11 August with no gap, and
none of its figures reached any face before tonight. **True as written.** Finding 11's first
item is discharged.

### R8. §7 — the restaging moved no figure, and the head's DERIVED label still holds

Reading order on the built page (`STATE-1.txt`): the figure and its constant, the eleven
names, then `WHAT THE LIST OF 4 AUG WAS THE TOP OF` + the four figures + the SOURCED word,
then the reserved space, the hedge and the controls; below them the caption, the method-sheet
quotation, the since-note, `kept`, `refused`, and the share's DERIVED line. Every string is
present, in the island, from the same build. No figure changed.

`arrive.tier` is now back to `DERIVED — this share is worked out here, from saved copies of
those lists. Nobody publishes it.` — which is verbatim the string `KRITIKER-84.md` §2 ruled
*"does not hold"*, because its declared basis was true and its real basis unstated. **I rule
that it holds now**, and the reason is positional and checkable rather than a matter of
taste: the real basis is stated twice above that line — once in the block that stands between
the names and the controls, where a reader who scrolls no further meets it, and once again
in `kept` two paragraphs before the tier line itself. The critic's objection was to a face on
which the basis appeared nowhere. That is no longer this face. NOTED for the record that the
head's tier line is now carrying the label on the strength of a block above it, so any future
cut to that block re-opens the critic's finding — this is banked failure 25's exact geometry
and deserves a comment where the cut would be made.

### R9. NOTED — the OBSERVED table now holds a third column that is not OBSERVED

The ledger's own heading is `OBSERVED — every saved copy this page holds`
(`index.html:2586`). Under it stand `edition` (the list's own date — SOURCED by the face's
own legend), `ships in that list` (DERIVED as of tonight) and, new tonight,
`disappearances examined` (SOURCED). `README.md:429` names this condition as the thing
`tiers.mjs` structurally cannot catch — *"two ledger columns captioned OBSERVED were in fact
SOURCED"* — without naming which two; tonight's column joins that set while another leaves
it. I am not blocking: the caption directly above the table attributes the new column to the
instrument in words (*"what that same copy says the instrument examined"*), the same figure
is printed and correctly tiered in the head, and the house discloses the limitation itself.
But the sentence in the README should name the columns, or the heading should stop being a
tier word.

### R10. NOTED — findings I closed, and what I could not check

Discharged and not repeated below: 1(a)(b)(c), 2, 3, 5, 7, and both remaining items of 11
(the `saved them every night` referent, and the README's figure ordering). Findings 4 (the
house is right about the quotient and `KRITIKER-84.md` §2 is not), 6 (the union rule lives in
the source only and changes no printed figure), 8's first half (the legend's coverage — now
paid on the face, unpaid in the README, R4) and 10 (the tree moved twice during the first
pass; it did not move during this one) stand as written.

What I still cannot check, unchanged: whether the `82` of 4 August stood beside that
sentence in those bytes. The captures store the body's sha256, not its bytes, and that
edition is off the wire. Today's edition binds its own number adjacently — verified against
`aggregates_text` in `2026-08-11T044745Z.json` and against a body I fetched myself — but
4 August is an inference from the template, and the face does not say so.

---

**FAIL — one blocking item (R4): the README's tier legend, rewritten tonight, assigns the
ship count to SOURCED where the work's own face and head now assign it to DERIVED, and names
one of the three SOURCED aggregates the face's legend names. Two lines. Everything else that
blocked in the pass above is paid, and paid properly.**
