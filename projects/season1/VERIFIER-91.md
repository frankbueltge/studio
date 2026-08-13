# VERIFIER-91 — the premiere gate, second putting

**Session 91 · 2026-08-13 · STILL DARK, `projects/season1/still-dark/`**

**Object hash at the start of this pass:**
`sha256sum projects/season1/still-dark/index.html` →
`05ea10f04d6455e36ca64df8e330bfd35b5c463e5bd886dcf419c65aaad3853f`
`git rev-parse HEAD` → `babd179e884bb9d590309c18a8b65bf785f54d75`

Remit: facts and tiers, against the sources themselves. No vote on form. I wrote exactly one file,
this one. I ran no writing instrument: no `render.mjs`, no `capture.py`, no `data.py --write`, no git
command that moves HEAD or the tree. Everything below was taken read-only on the frozen object and
on the frozen render (`STATE-1.txt`, `RENDERS.json`, both PNGs), which I read and did not regenerate.

Six blocking. Four of them are in the paragraphs this session wrote or re-took tonight; two of those
four are novelty claims, and the house's own record refutes both.

---

## § BLOCKING

### 1. The new paragraph says the earlier body is recorded tonight. No capture in this record has ever held a body.

**Open:** `projects/season1/still-dark/README.md:635-637`.

> *"That is the shape of the 2026-08-06 movement, which this work has always printed as
> unattributable; the difference is that in August the earlier bodies were not kept and the assets
> were not recorded, so nothing could be said. **Tonight both are recorded and both are identical**,
> which rules the site's own build fingerprints out and rules nothing in."*

"Both" takes its antecedent from the clause before it: *the earlier bodies* and *the assets*. Neither
half of the sentence survives its own record.

- **The bodies are not recorded tonight either.** `capture.py:274-279` writes `fetch.bytes` and
  `fetch.sha256` and no body; I walked every key of `../captures/2026-08-13T043640Z.json` and there
  is no response text in it, exactly as there is none in the capture of 2026-08-06. The work's own
  second asset says so in the same words the new paragraph borrows: `../capture/README.md` —
  *"For the 2026-08-06 capture it cannot: **the earlier bodies were never kept, only their hashes**,
  and this house does not claim to know what moved."* Nothing changed about that tonight. What was
  "not kept" on 6 August is not kept now, so it is not the difference between the two cases.
- **And the bodies are not identical.** The paragraph's own headline three lines above is *"and a
  different body hash"* — `14ddeb5c…` → `1a3e76fe…`. A sentence that says both are identical, on the
  page whose subject is that one of them moved, is false on its face.

The real difference between 2026-08-06 and tonight is one thing and it is worth saying: **the asset
fingerprints**. `page_assets` is `null` in all three captures of the 5 August edition and carries two
paths in tonight's, identical to the copy before it. (Not the content digest: `edition.py` recomputes
`content_sha256` for captures written before the field existed — it prints `47338b03…` for all three
of those 5 August copies — so the record *can* say the content stood still on 6 August too.)

**Smallest repair that discharges it, checked before proposing it:** cut the bodies out of the
sentence and let it claim only what is recorded — *"…the difference is that on 6 August the asset
fingerprints were not recorded, so nothing could be said. Tonight both are recorded and both are
identical, which rules the site's own build fingerprints out and rules nothing in."* I checked the
repair against the captures: `page_assets` null in `2026-08-05T125400Z`, `2026-08-05T191755Z`,
`2026-08-06T043619Z`; two identical paths in `2026-08-12T232100Z` and `2026-08-13T043640Z`. True as
written, and it no longer claims a difference that does not exist.

---

### 2. "The first unattributable movement this record can bound" — an earlier one is bounded by the same test, in this record, already printed on the face.

**Open:** `projects/season1/still-dark/README.md:638-639`.

> *"**Four of the seven are attributable; this one is not, and it is the first unattributable
> movement this record can bound rather than only report.**"*

**The first half is true and I verified it name by name.** Grouping all 28 captures by
`content_sha256` and counting distinct `fetch.sha256` inside each group gives seven contents that
came back in more than one body — `47338b03` (5 Aug), `53114dfe` (6 Aug), `5c89d9ec` (8 Aug),
`aa53ae8b` (9 Aug), `423c17df` (10 Aug), `a7ab0eb1` (11 Aug, three bodies), `005c4e9f` (12 Aug).
An asset fingerprint moves with the body in exactly four of them — `53114dfe` (TopBar.SLcnmZbT.css →
Base.BvXYJsAy.css), `5c89d9ec` (→ Base.BC3Pps2G.css), `423c17df` (→ Base.BDo6THrI.css), `a7ab0eb1`
(→ Base.P8Knfq78.css → Base.yW6q2ssk.css). **Four of seven attributable: correct.**

**The second half is false, and the paragraph itself supplies the test that kills it.** The bound it
claims is *"both are recorded and both are identical, which rules the site's own build fingerprints
out"*. That bound was available once before, on the fourth of the seven:

```
2026-08-09T203658Z  36,897  8bf3c1ff…  aa53ae8b…  ["…CRoAemHu.js", "…Base.gah2t5G_.css"]
2026-08-10T043645Z  32,189  95c28f17…  aa53ae8b…  ["…CRoAemHu.js", "…Base.gah2t5G_.css"]
```

Same edition, same content digest, **both asset fingerprints recorded and identical**, body moved,
no attribution available. The site's build fingerprints were ruled out there on 10 August in exactly
the way they are ruled out tonight. Tonight's movement is not the first the record can bound; it is
the first in which the **byte count** stood still as well.

**And the obvious repair is itself false** — banked failure 51's trap, so I tested mine before
writing it. *"the first unattributable movement whose byte count did not move either"* is refuted by
the 2026-08-06 movement, which held at **35,485 bytes** across `17c07fc3…` → `aed92f4f…`.

**Smallest repair that discharges it:** delete the clause. *"Four of the seven are attributable;
this one is not."* — both halves verified above, and the paragraph loses nothing it can support. If
the house wants the distinction kept, the only formulation I could not falsify against all seven is
that this is the one movement in which the content digest, the byte count **and** both asset
fingerprints all stood still together; that is a description, not a first, and it should not be
dressed as one.

---

### 3. "The first night this number has held still" — `fold.mjs` returned 88 on two consecutive committed pages, and I reproduced both tonight.

**Open:** `projects/season1/still-dark/README.md:903-904`.

> *"**Session 91 re-ran it on a page carrying one more capture row and it returned 108 again**,
> which is the first night this number has held still."*

Run tonight, on pages taken read-only out of git with `git show` into a scratch directory, with the
instrument that is committed now:

```
git show 658a6fd:projects/season1/still-dark/index.html   (session 87)
  node tools/fold.mjs --dir=<scratch>/s87 → FOLD: 88 failure(s), exit 1
git show baaeb13:projects/season1/still-dark/index.html   (session 88)
  node tools/fold.mjs --dir=<scratch>/s88 → FOLD: 88 failure(s), exit 1
```

The number held still across sessions 87 and 88, on two different objects, and this house published
it at the time: `../VERIFIER-88.md` — *"**`fold.mjs` stays at 88 and the count tracks scroll range**
— reproduced across all three states: `658a6fd` 88 failures … and the final page 88"* — and
`../DRAMATURG-88.md` — *"88 failures — level with `658a6fd`, as §5 said it would be."* A novelty
claim contradicted by two memos standing in the same directory is the cheapest kind of unchecked
claim, and the protocol names it: no claim of novelty unchecked.

**Smallest repair that discharges it:** delete *"which is the first night this number has held
still"*. The sentence before it — that 91 re-ran the instrument on a page with one more capture row
and got 108 again — is true; I reproduced 108, exit 1, on the committed object tonight. Nothing else
in the paragraph depends on the deleted clause.

---

### 4. The live record says the share has fallen seven times. It has fallen eight, and the work's own asset says eight.

**Open:** `projects/season1/PROJECT.md:36-38`.

> *"**The total can only grow, so the share is a ceiling that can only fall — and it has fallen seven
> times from later lists**, on 6, 7, 8, 9, 10, 11 and 12 August."*

`python3 projects/season1/capture/day.py 2026-08-04 --as-of <each capture's own instant>`, run
tonight across all 28:

| first instant showing it | share | the list that caused it |
|---|---|---|
| 2026-08-05T12:54:00Z | 100 % → **79 %** | the list dated 5 August |
| 2026-08-06T08:16:42Z | → 69 % | 6 August |
| 2026-08-07T18:15:53Z | → 65 % | 7 August |
| 2026-08-08T21:37:19Z | → 55 % | 8 August |
| 2026-08-09T20:36:58Z | → 44 % | 9 August |
| 2026-08-10T17:47:21Z | → 37 % | 10 August |
| 2026-08-11T11:19:15Z | → 33 % | 11 August |
| 2026-08-12T18:23:12Z | → 31 % | 12 August |

**Eight falls from later lists, on 5 through 12 August** — the 37 → 35 movement of 2026-08-10T22:41
is the parser and is excluded, as this file rightly insists. The paragraph's own enumeration says the
same thing: nine prior values plus the present one is nine transitions, minus the parser is eight.
So does the work's own asset, `still-dark/README.md:738-739` — *"the share falls 100 · 79 · 69 · 65 ·
55 · 44 · 35 · 33 · 31 — **eight movements of degree**"*. The record and the work disagree by one,
and the work is right.

The date list is what hides it: **5 August is missing**. It is not saved by reading the dates as
publication nights either — the face published `79 %–100 %` at **04:57 UTC on 6 August** (the
superseded block of the earliest committed `STATE-1.txt` says so in its own words) and `69 %–100 %`
at 08:36 the same day, so under that reading 6 August carries two falls and the count is still eight.
`../VERIFIER-89.md` §4 licensed "seven" when it added 12 August to a list of six; it was one short
then and it is one short now, and I record that against my predecessor rather than around it.

**Smallest repair that discharges it:** *"…and it has fallen eight times from later lists, on 5, 6,
7, 8, 9, 10, 11 and 12 August."* Checked both ways before proposing: the eight dates are the same
whether they are read as the edition dates of the lists that lowered it or as the dates of the
captures that first showed each fall. The neighbouring sentence — *"the record has tested it six
times, and it has held"* — is **not** touched by this and is correct: the law was printed at 08:36
UTC on 6 August, and six later lists (7–12 August) have arrived since.

---

### 5. The guard table is headed SESSION 90 and every figure in it was taken in session 91.

**Open:** `projects/season1/still-dark/README.md:877-893`.

> `## THE STATE OF EVERY GUARD, SESSION 90 — printed because one of them is not green`
> … *"Every figure below was taken tonight on the committed object"* … column header *"tonight, on
> this page"* … and, inside the table's own body, *"**Session 91 re-ran it** … and it returned 108
> again"*.

Every number under that heading is tonight's: I reproduced all of them (see § WHAT HOLDS), including
the two that could not have been session 90's — `data.py --check` now passes against a 28-capture
island, and the fold row names session 91 in its own text. A stranger is told the guards were read on
one night and shown figures from another, in a section whose whole purpose is to say truthfully what
the guards print. This is the class banked as failure 51, arriving through a heading rather than an
adverb.

**Smallest repair that discharges it:** `SESSION 90` → `SESSION 91` in the heading. Checked: the
section's other session references stay true under it — *"`KRITIKER-89.md` condition 3, paid in
session 89 and re-run here"* is unaffected, and the frame row's *"this row was blocking during
session 90"* is about a past state and is correctly dated already.

---

### 6. The instrument inventory tells a stranger `fold.mjs` returns nothing on the committed page. It returns 108, and the same document says so 176 lines later.

**Open:** `projects/season1/still-dark/README.md:716-717`.

> *"On the page as committed before tonight it returns **14 losses**; on tonight's, none."*

`NODE_PATH=… node tools/fold.mjs` on the committed object tonight: **108 failure(s), exit 1**. The
sentence sits in the undated instrument inventory — the stretch from line 687 to line 728 carries no
session heading at all, the previous heading is the top of the file and the next is `## SESSION 90` —
so its "tonight" is unanchored, and read now it flatly contradicts `README.md:893`
(*"**108 failures — RED**"*) and the paragraph under it. This is the sweep the session was asked to
run and it stopped one section short of it.

**Smallest repair that discharges it:** strike the two clauses and point at the guard table, which
prints the current reading with its exit code — *"…exits non-zero if the controls or the live line
leave the viewport at any stop below 481 px. What it returns on the page as committed is in the guard
table below."* I deliberately do **not** propose re-dating it to session 84: those two figures were
taken with the instrument as it stood before it was rebuilt the same night (its own header says so),
today's instrument does not reproduce them, and putting a stale number back in the record with a date
on it would hand this house a figure no run can return. That is the mistake my predecessor made in 89
and I am not repeating its shape.

---

## § NOTED

1. **`README.md:636` — "in August" is not a contrast.** The movement being contrasted with tonight's
   happened on 6 August and tonight is 13 August. The repair in blocking 1 removes the phrase.
2. **`PROJECT.md:38` — "These six figures" now has no referent.** It points at the six stale figures
   `../VERIFIER-89.md` §4 named; none of them is in this file any more. True as history, unreadable
   as prose, and a reader will count the nine percentages in the sentence above it.
3. **The announce row's `3.199 s` is inside the jitter it declares.** Three runs tonight:
   **3.182 s · 3.215 s · 3.207 s**. I could not reproduce 3.199 s and the row says in its own words
   that I would not. The other four figures on that row (1 live region · 4 writes in 30 s · 3 spoken
   · 10 figure rewrites) reproduced exactly, three runs out of three.
4. **`README.md:783-784` — "in it three times — entries 197, 201 and 202 — at the same address this
   section cites for it."** Entries 201 and 202 carry the bitforms address; **entry 197 carries
   `github.com/MimiOnuoha/missing-datasets`**, which this section explicitly declines to cite two
   lines later. The parenthetical that follows repairs it in practice; the sentence overreaches.
5. **The atlas indices are 0-based and nothing says so.** `werke.json` fetched tonight, 200,
   `count: 505`: the 198th record is Ọnụọha's companion list (cited as 197), the 200th is
   *Sobrevivientes* (cited as 199), the 202nd and 203rd are the two *Library of Missing Datasets*
   entries (cited as 201 and 202). Every citation lands correctly at 0-base; a stranger counting from
   one lands one short every time.
6. **`tools/record_words.py` measures HEAD, not tonight's file.** It reports `PROJECT.md` at 2,437
   words and passes UNDER by 168. The working tree holds **2,453** words, so the standing total is
   **2,848 of 3,000** — still under, but the instrument that guards the ceiling is a session behind
   the file it guards, and session 87 banked a breach that happened exactly where an instrument was
   not looking.
7. **`tools/fold.mjs`'s header documents `--dir <path>`; the code parses only `--dir=<path>`
   (line 38).** Anyone following the header gets a run against the default directory and will think
   they measured the page they named.
8. **The OBSERVED ledger's heading still covers two SOURCED columns and one DERIVED one** — `edition`
   and `disappearances examined` are upstream's, `ships in that list` is this house's count. The face
   assigns all three correctly in the legend and the README names this as precisely what `tiers.mjs`
   cannot catch. Standing, not new tonight, not blocking — recorded so it does not become invisible
   by age.
9. **Memory rule 5 — the superseded-string search is owed and it comes back clean.** Tonight
   superseded *"Six lists came back in more than one set of bytes"*, *"two hours ago"*,
   *"THE CERTAIN END DOUBLED TONIGHT"*, *"27 saved copies"*, *"16 bodies"*, *"As of session 90"*.
   Repository-wide `grep -rn` over `.md`, `.html`, `.py`, `.mjs`, `.json`: every surviving instance is
   inside a frozen memo quoting it (`VERIFIER-89.md`, `VERIFIER-90.md` §N9) or inside
   `chronicle.json` / `REQUESTS.md` as published history. **No live assertion of a superseded string
   remains**, and *"two hours ago"* returns nothing anywhere. The session still owes the printing of
   that search in its own record; this paragraph is not a substitute for it.
10. **Upstream is byte-identical to the last row of the ledger at the moment of this pass.** I fetched
    `https://frankbueltge.de/ghost-fleet/` myself: 200, 31,635 bytes,
    sha256 `1a3e76fec6129ec4ec2622cd8792b95f792dcf4cdb03928e52070e53a2c4866d` — the same body the
    28th capture records. No tenth list has appeared behind this gate.

---

## § WHAT HOLDS

**The 28th capture is real, current and honestly described.** `../captures/2026-08-13T043640Z.json`:
`fetched_at_utc 2026-08-13T04:36:40Z`, status 200, 31,635 bytes, body `1a3e76fe…`, content
`005c4e9f…`, edition printed *12 August 2026*, 10 vessels, 257 examined. Against the copy before it
(`2026-08-12T232100Z`): same content, same byte count, same two asset fingerprints, different body —
exactly as `PROJECT.md` and the new paragraph say. The share does not move: **31 %–100 %, 11 of 4–35**.

**The island is the captures.** `python3 data.py --check` → `island matches the captures`. The
ledger's 28th row matches the capture file field by field. The caption's *"Seven lists"* is
**computed, not typed**: `data.py:1601-1612` groups by content digest and counts groups with more
than one body through `word(n)` — I counted the same seven by hand from `edition.py` and got the same
seven. `python3 ../capture/edition.py` → **28 captures · 9 distinct editions · 10 distinct contents ·
17 distinct bodies**, which is what `PROJECT.md` now prints and what the face prints.

**Every stop still reproduces itself — 9 of 9.** I ran each stop's own printed command:

```
--as-of 2026-08-05T04:39:32Z → 100%–100% (11 of 0–11)   certain 0   ✓ ON THE DAY
--as-of 2026-08-05T12:54:00Z →  79%–100% (11 of 0–14)   certain 0   ✓ +1 DAY
--as-of 2026-08-06T08:16:42Z →  69%–100% (11 of 0–16)   certain 0   ✓ +2 DAYS
--as-of 2026-08-07T18:15:53Z →  65%–100% (11 of 0–17)   certain 0   ✓ +3 DAYS
--as-of 2026-08-08T21:37:19Z →  55%–100% (11 of 0–20)   certain 0   ✓ +4 DAYS
--as-of 2026-08-09T20:36:58Z →  44%–100% (11 of 0–25)   certain 0   ✓ +5 DAYS
--as-of 2026-08-10T22:41:12Z →  35%–100% (11 of 0–31)   certain 0   ✓ +6 DAYS
--as-of 2026-08-11T11:19:15Z →  33%–100% (11 of 2–33)   certain 2   ✓ +7 DAYS
--as-of 2026-08-12T18:23:12Z →  31%–100% (11 of 4–35)   certain 4   ✓ +8 DAYS
```

Share, fraction, total and the count that turns, all four, at every stop. This is the strongest thing
the work owns and it is intact on the object as frozen.

**`PROJECT.md`'s claim that `--as-of` reproduces every prior figure is true, including the one that
looks impossible.** `100 · 79 · 69 · 65 · 55 · 44 · 37 · 35 · 33` all come back, the `37 %` at
`--as-of 2026-08-10T17:47:21Z` — the pre-repair parse of the 10 August list — and the `35 %` at
`22:41:12Z`, which is the parser movement the file correctly refuses to count as a fall.

**The superseded block on the face is exact.** `--as-of 2026-08-06T08:36:39Z` → *5 captures, 3
editions, 69 %–100 %, 11 of 0–16*, which is what the face prints beside *"as this page published it
at 08:36 UTC on 6 August, from 5 saved copies of 3 lists"*. `git cat-file -t 91ee19b` → commit,
authored 2026-08-06 08:36:39 +0000, and its diff touches `still-dark/index.html` and `STATE-1.txt` —
the citation on the face opens. The fall is *"thirty-eight points"* (69 → 31) and the nineteen names
listed in that paragraph are nineteen, and 35 − 16 = 19.

**The island's terminal output is verbatim.** I ran `python3 projects/season1/capture/day.py
2026-08-04 | head -6` and compared it byte for byte with the `output` string in the data island:
**identical**. The face's word for it, *"verbatim, unedited"*, is earned.

**The day's own figures are upstream's.** The first capture (`2026-08-05T043932Z`) carries
`disappearances_examined 230`, `dark_inside_national_waters 82`, `in_the_window 5641` and 11 vessels
— the face's *"11 of 230"* and *"Of the 230 examined, 82 were dark inside national waters · 5,641
events in the window"*. The face's *"six to eleven names of the 189 to 257 disappearances"* is the
true min and max across the nine lists (vessels 6–11; examined 189–257).

**Both upstream quotations are verbatim and I fetched the source myself, not the capture.**
`https://frankbueltge.de/werke/ghost-fleet/`, 200, tonight:
- *"The index counts all examined; the case and list show named vessels."* — verbatim, §3.
- *"The AIS picture of the seas looks complete. It is not — ships switch off their transponder on
  purpose to vanish."* — verbatim, under *What this is*, and correctly attributed to the method sheet.
- *"Daily. Window: disabling events that ended in the last 7 days (complete vanish-and-return
  stories)"* — verbatim, §2.
- *"GFW returns only high-confidence, intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore"* —
  the face's *"at least 12 hours dark, at least 50 nautical miles offshore"* is a faithful rendering.

**Upstream's restraint travels, and it travels correctly.** The method sheet: *"The „intentional"
label comes from GFW's machine-learning model and is **a probability, not proof**"* and *"**No claim
of illegality against vessel or state**."* The face repeats both, twice — at the head of the
disclosure and at the foot of the page — and `../capture/README.md` repeats them a third time. The
quoted fragment *"a probability, not proof"* is upstream's own string, not a paraphrase in quotation
marks. I checked this specifically because session 87 banked two paraphrases inside quotation marks.

**The MSE passage survives its own source — the finding session 90 nearly shipped is genuinely
repaired.** `https://hrdag.org/2013/03/20/mse-stratification-estimation/`, fetched first-hand, 200,
Amelia Hoover Green, March 20 2013. Q13's table: *"Equal probability of capture: For every data
system, **each individual has an equal probability of being captured**."* — the face's quotation is
exact. And the scoping sentence the face now carries: *"the two final assumptions—equal catchability
and list independence—are **unnecessary for MSE analyses with >=3 datasets, because both individual
differences in catchability and dependence between lists can be parameterized and modeled**."* — also
exact, and correctly used: the page does not support refusing MSE on that ground at nine lists, and
the work no longer says it does. The reason that survives — that modelling a capture probability
needs one to exist, and a ship still dark stands in no list in all nine — is the work's own argument
and is not attributed to HRDAG.

**The atlas claims check out against the file.** `https://frankbueltge.de/atlas/werke.json`, 200,
`count: 505`, licence CC0 — **505 entries** as printed. Ọnụọha is in it three times at 0-based 197,
201, 202; entry 202 is the one that actually carries *"People excluded from housing due to criminal
records"*, which is where the record now cites it; *Sobrevivientes* is 0-based 199 and its entry does
carry the title, the year `2017–ongoing` and the word *testimony*, as the record says the page itself
does not. The correction 90 blocked on has held.

**The guards, re-run tonight on the frozen object, every number in the table:**

```
python3 data.py --check                    island matches the captures                    exit 0
node gaps.mjs                              35 rows, 0 failing · own 1.42 px · next 9.59 px exit 0
                                           (tightest margin 8.17 px, both widths PASS)
node ../../../tools/tiers.mjs              every printed figure sits in a scope with a
                                           tier word — and it prints that it cannot say
                                           the word is the right one                       exit 0
node ../../../tools/frame.mjs              328 px of 844 · 568 px of 900 — HOLDS
                                           273 px, 24 of 24 chips vs floor 268 / 22 — HOLDS exit 0
node ../../../tools/fold.mjs               108 failure(s) — RED, published red             exit 1
node announce.mjs                          1 region · 4 writes / 30 s · 3 spoken · 10
                                           figure rewrites                                 exit 0
bash tools/selftest.sh                     SELFTEST PASSED
```

**The fold decomposition is right, and I counted it rather than took it.** At 390 px the instrument
counts only must-hold elements (`fold.mjs:124`): the controls leave the viewport at six of the nine
probe positions and the run's line at the same six, on all nine stops — **6 + 6 = 12 per stop × 9 =
108**, and **zero `✗COVERS`** anywhere in the run, so the *"zero occlusions"* claim is true. The
1400 px section's losses are correctly not counted. The README's account of what the instrument is
red about is accurate.

**No tier is blurred and no tier word is missing where the face prints a figure.** The face carries
`SOURCED` (4), `DERIVED` (6), `OBSERVED` (5) and **no `VERIFIED` and no `IMAGINED` anywhere** in
`index.html` or `STATE-1.txt` — which is exactly what `PROJECT.md` promises for this work. The floor
line is intact: *"No number closes this. A method that counts a disappearance only when the ship
comes back cannot see the ships that never come back."*

**The certain end, and the two names that made it.** ISABELLA and LUCKY TJ are both back `5–12 Aug`,
so neither window reaches 4 August; every other one of the twenty-four added names does, which is the
face's *"twenty-two of the twenty-four"*. Four certain — PANOFI FORE RUNNER, HEATHER LYNN, ISABELLA,
LUCKY TJ — is what `day.py` returns and what the frame prints at the last stop.

**Nothing moved under this pass.** The object hash is unchanged at both ends of it; `RENDERS.json`
and both PNGs are the conductor's frozen render and I read them without touching them; the only file
I wrote is this one. `git rev-parse HEAD` is `babd179e884bb9d590309c18a8b65bf785f54d75`, where it was
when I started.

---

## VERDICT: FAIL, 6 blocking

The work's spine — the number, its nine reproductions, its tiers, its sources, its inherited
restraint — is sound, and I could not fault it anywhere. What fails is the prose written *about*
tonight: two novelty claims the house's own record refutes, a sentence whose subject is not recorded
anywhere in the evidence chain, a fall count the work's own asset contradicts, a heading a night
behind its table, and an undated line telling a stranger a red instrument is green.

**Object hash at the end of this pass:**
`sha256sum projects/season1/still-dark/index.html` →
`05ea10f04d6455e36ca64df8e330bfd35b5c463e5bd886dcf419c65aaad3853f`
`git rev-parse HEAD` → `babd179e884bb9d590309c18a8b65bf785f54d75`
