# VERIFIER — STILL DARK, premiere gate, session 90

*Blocking voice. Facts and tiers only; no vote on form, staging or worth. Nothing below is taken on
the brief's word, the record's word or a memo's word: every figure was recomputed, every sentence
read off the built object, every quotation and every URL fetched first-hand tonight.*

---

## The object, hashed at both ends of this pass

| | at start (23:41 UTC) | at end (23:56 UTC) |
|---|---|---|
| `projects/season1/still-dark/index.html` | `e98d1507f71bb0dc9ecfca3db587a366db3eb764f8e1116bbb58960cd834f4fb` | `e98d1507f71bb0dc9ecfca3db587a366db3eb764f8e1116bbb58960cd834f4fb` |
| `projects/season1/still-dark/README.md` | `e8d6a95ee15df81668555bb51e87d2699e331daebac12d4f25d1dc12e9faf576` | `e8d6a95ee15df81668555bb51e87d2699e331daebac12d4f25d1dc12e9faf576` |

**Neither object moved, and nothing beside them moved either.** No commit, no staging, no `render.mjs`,
no `data.py --write`. `RENDERS.json` names `index_sha256` `e98d1507…` — the object under test — and
its three output hashes (`STATE-1.txt` `f67e32c8…`, `render-1400.png` `5f4248ba…`, `render-900.png`
`bcc25552…`) all recompute exactly tonight, so the sighted material is of this page and it did not
move under the gate. Banked failure 50 is not repeated in this pass: every script of mine is in a
scratchpad outside the repository, and the only file I created inside it is this memo.

## What was run

```
sha256sum projects/season1/still-dark/{index.html,README.md}            (start and end)
git status --porcelain · git log · git diff -U3 (index.html, data.py, README.md)
python3 projects/season1/capture/day.py 2026-08-04
python3 projects/season1/capture/day.py 2026-08-04 --as-of <the nine printed instants>
python3 projects/season1/capture/day.py 2026-08-04 --as-of <six instants of my own choosing>
cd projects/season1/still-dark · python3 data.py --check · node announce.mjs · node gaps.mjs
NODE_PATH=… node tools/tiers.mjs · node tools/frame.mjs (twice) · node tools/fold.mjs (no pipe)
```

Written against the captures, outside the repository: an independent re-derivation of every stop's
`as_of` from the 27 saved copies, and a per-element tally of `fold.mjs`'s failure count.

## What was fetched, first-hand

| URL | status | bytes |
|---|---|---|
| `https://hrdag.org/2013/03/20/mse-stratification-estimation/` | **200** | 122,503 |
| `https://frankbueltge.de/werke/ghost-fleet/` | **200** | 27,046 |
| `https://frankbueltge.de/atlas/werke.json` | **200** | 375,475 |
| `https://www.bitforms.art/artwork/the-library-of-missing-datasets-v-2-0/` | **200** | 13,513 |
| `https://www.biennial.com/artists/banu-cennetoglu/` | **200** | 93,630 |
| `https://www.fidh.org/IMG/pdf/fo-report.pdf` | **200** | 7,241,916 |
| `https://forensic-architecture.org/investigation/the-left-to-die-boat` | **200** | 931 (a script shell) |
| `https://dusp.mit.edu/projects/data-against-feminicide` | **200** | 34,379 |
| `https://datoscontrafeminicidio.net/en/art-and-data-to-make-feminicide-visible/` | **200** | 144,626 |
| `https://paglen.studio/2020/05/22/the-other-night-sky/` | **200** | 92,377 |
| `https://watchthemed.net/` | **200** | 93,397 |
| `https://github.com/MimiOnuoha/missing-datasets` | **403** | — |

**No cited URL is dead.** The single 403 is issued by this session's own tooling policy, not by the
host, and the README already says it did not open that address — that is honest and it stands.

---

# VERDICT

## **FAIL — five blocking, fourteen noted.**

Tonight's arithmetic is clean, and it is not close: every figure the brief named checks, the two
conditions built on the face are built correctly and precisely, and last session's three blocking
items on this object are all discharged. What fails is **sourcing**, in the two places this session
went outside itself for the first time: a method it names and a register it searched. The face now
says why it refuses to estimate, and the reason it gives is contradicted by the page it cites, two
paragraphs under the sentence it quotes. The README says the house's atlas holds none of the four
works it argues against, and the atlas holds one of them twice.

Blocking items 1, 2, 3 and 5 are all of one shape: **a true quotation carrying a claim it does not
support.** None of them asks this work to be a different work, and item 1's repair makes the
sentence stronger than the one it replaces.

---

# BLOCKING

## 1. The face gives, as MSE's requirement, an assumption its own cited source scopes to two lists and calls unnecessary with three or more. This record holds nine.

**Open:** `projects/season1/still-dark/index.html:754` (island `arrive.cut.refused`) · rendered at
`projects/season1/still-dark/STATE-1.txt:63` / `#sd-arrive-cut-refused` · generated at
`projects/season1/still-dark/data.py:1017-1030` · the same claim in
`projects/season1/still-dark/README.md:797-799`.

The face, as a stranger reads it tonight:

> *"The method that would try has a name: multiple systems estimation, which reads the overlaps
> between several incomplete lists to say how many none of them caught. **It asks of each list that
> "each individual has an equal probability of being captured". These lists carry no such
> probability.**"*

The quotation is **verbatim** and the attribution is **exact**: the HRDAG page fetched tonight
(200, 122,503 bytes) prints *"Equal probability of capture: For every data system, each individual
has an equal probability of being captured"*, over the byline *"Amelia Hoover Green March 20,
2013"*, under the title *"Multiple Systems Estimation: Stratification and Estimation"*. The source
line at `index.html:755` is true in every particular.

**What is not true is the claim built on it.** That sentence stands in a table whose own column
heading is **"2-System Assumption"**, in a section headed *"Q13. What are the assumptions of
two-system MSE (capture-recapture)? **Why are they not necessary with three or more systems?**"*
The table's own answer in that row is **"Yes. Can stratify or model directly."** and the paragraph
immediately below the table reads, verbatim:

> *"As the table above suggests, the two final assumptions—equal catchability and list
> independence—**are unnecessary for MSE analyses with >=3 datasets**, because both individual
> differences in catchability and dependence between lists can be parameterized and modeled."*

The face's own next clause says this record holds **nine** lists. So the reason the face gives for
refusing the method is the one requirement its cited source says drops away at exactly the number of
lists this record has. A stranger who follows the link — which this build added precisely so that
they could — reads the refutation on the same page, below the quotation.

**This is not a finding against the refusal.** The paragraph's second argument — that membership of
an edition is decided by a published rule rather than drawn, so the overlaps measure the rule — is
untouched by this, and it is the argument `KRITIKER-89.md` condition 2 actually asked for
(*"why it does not apply to lists truncated by rank rather than sampled"*). It is also the stronger
argument: a rank cut does not give a ship an unequal capture probability that could be modelled, it
gives some ships no capture probability at all. What must go is the framing that makes the *quoted*
requirement load-bearing.

**Smallest repair that discharges it:** let the quotation carry its own scope and let the
deterministic-membership clause carry the reason — e.g. *"…the assumption its two-list form makes,
'each individual has an equal probability of being captured', which HRDAG says can be stratified or
modelled away with three or more lists. Modelling it still needs a capture probability to exist, and
these lists give some ships none: a ship enters an edition …"*. One string in `data.py`, and the same
correction in `README.md:797-799`.

**The search this correction owes** (memory decision 5): `grep -rn "equal probability of being
captured" .` — four files tonight, `index.html:754`, `data.py:1024`, `README.md:798`,
`STATE-1.txt:63`, plus the two PNG renders, which a re-render carries.

---

## 2. The face quotes upstream's rule for the *case of the day* as the rule for who gets into the *list*. Upstream's own sentence distinguishes the two.

**Open:** the same string, `index.html:754` / `STATE-1.txt:63` · `README.md:800-802`.

> *"A ship enters an edition when its return falls in that edition's seven-day window and **it ranks
> high enough to be printed** — **"case of the day by region brisance, then duration"** — so
> **membership is a published rule** and not a draw…"*

Both quoted strings are **verbatim** on the method sheet fetched tonight (200, 27,046 bytes) — the
window sentence in §2 Cadence, the ranking sentence in §3 Processing. But the ranking sentence is
upstream's rule for choosing **the case of the day**, and its own next clause, which this face drops,
is *"The index counts all examined; **the case and list** show named vessels."* — upstream naming
case and list as two different things in the same breath. `data.py:966` quotes that fuller sentence
correctly in a comment; the face's compression is what loses it.

I searched the whole method sheet: it states the fetch is *"paginated, capped"* and that processing
uses *"filters, region weight, aggregates"*, and it **nowhere states how the daily list is cut or
ranked**. So *"it ranks high enough to be printed"* and *"membership is a published rule"* are this
record's inference — a reasonable one, given nine lists of six to eleven names out of 189 to 257
examined — presented with a quotation as its warrant. A named third party's method is described on
this face as more disclosed than that third party discloses it.

**Smallest repair:** either drop the quotation from that clause and say plainly that the list is a
short selection from all examined and that upstream publishes a ranking rule for its case of the day,
or quote the sentence whole so the reader sees the distinction. The refusal's conclusion survives
either way: a selection whose rule is not a draw is still not a sample.

**The search:** `grep -rn "region brisance" .` — `index.html:754`, `data.py:966` and `:1027`,
`README.md:801`, `STATE-1.txt:63`.

---

## 3. The README says none of the four works it argues against is in the house's atlas. The atlas holds the first of them twice, at the very URL the README cites beside it.

**Open:** `projects/season1/still-dark/README.md:765-766`.

> *"Searched for ship · vessel · AIS · … · missing · absence · … : **no entry in it measures when a
> fact became knowable, and none of the four works argued below is in it.** A negative result across
> 505 neighbours is evidence and is recorded as evidence…"*

`https://frankbueltge.de/atlas/werke.json`, fetched tonight, 200, 375,475 bytes: `count` = **505**
and `entries` has length **505** — that figure is right. The negative result is not.

- entry **201**, *"The Library of Missing Datasets"*, Mimi Ọnụọha, `source_url`
  `https://www.bitforms.art/artwork/the-library-of-missing-datasets-v-2-0/` — the same address the
  README prints on the same page;
- entry **202**, *"The Library of Missing Datasets (v2.0)"*, Mimi Ọnụọha, same `source_url`;
- entry **197**, *"Missing Datasets (list/essay)"*, Mimi Onuoha, `https://github.com/MimiOnuoha/missing-datasets`.

Three of the four are genuinely absent — I searched the whole file for *Cennetoğlu / Cennetoglu*,
*Hoover Green*, *HRDAG*, *Multiple Systems*, *Forensic Oceanography*, *Left-to-die*: **0 hits each**,
and the twelve Forensic Architecture entries are other investigations. The first of the four is
present, and it surfaces under the README's own search terms — *missing*, *absence*, *migrant* all
return it. The README's next paragraph half-says so itself: *"Her open companion list,
`MimiOnuoha/missing-datasets`, is recorded in the atlas entry above."*

A negative result printed as evidence has to be the result. **Smallest repair:** *"…none of the other
three works argued below is in it; Ọnụọha's Library of Missing Datasets is, at entries 197, 201 and
202, and the atlas's own address for it is the one cited below."* That is a stronger sentence than
the one it replaces, because it shows the search ran.

**The search:** `grep -rn "none of the four works" .` and `grep -rn "no entry in it measures" .` —
one file, `README.md:766`.

---

## 4. The guard table misquotes its own instrument at the wide width: it prints 568 px of 900 where `frame.mjs` prints 597 on this object.

**Open:** `projects/season1/still-dark/README.md:847`.

> `| node ../../../tools/frame.mjs | … | 328 px of 844 · **568 px of 900** — HOLDS · 273 px and 24 of
> 24 chips against the floor of 268 and 22 — HOLDS | 0 |`

`NODE_PATH=/opt/node22/lib/node_modules node tools/frame.mjs`, run twice tonight on the object under
test, both runs identical:

```
phone 390×844 — figure-top to controls-bottom: 328 px of 844 — HOLDS
  the hole sharing a frame with the whole figure: 273 px, 24 of 24 chips at the last stop — floor 268 px / 22 chips — HOLDS
wide 1400×900 — figure-top to controls-bottom: 597 px of 900 — HOLDS
```

**328 ✓ · 273 ✓ · 24 of 24 ✓ · 568 ✗ — the instrument says 597.** The string `568` appears nowhere in
either run. This is a line written tonight, not one carried over: last night's row said *"327 px of
844 · 479 px of 900"*, so both numbers were re-taken and one of them was re-taken wrong. The verdict
word — HOLDS — is correct either way, which is what makes this the exact defect the last gate called
blocking: **a README that misquotes its own instrument in the row built to make the instrument
checkable.**

**Smallest repair:** `568` → `597`. **The search:** `grep -rn "568 px" .` — one file, `README.md:847`.

---

## 5. Two quoted details in the neighbours section are cited to pages that do not carry them.

**Open:** `projects/season1/still-dark/README.md:770-772` and `:813-817`.

- **`README.md:771`** — *"filing cabinets of empty labelled folders, e.g. **"People excluded from
  housing due to criminal records"**"*, followed by the bitforms address and *"fetched 2026-08-12,
  200"*. I fetched it: 200, 13,513 bytes. The page gives the title, the artist, *"Powder-coated steel
  filing cabinet, folders"* and *"a physical compendium of nonexistent datasets related to
  blackness"*. **The quoted folder label is not on it.** It is verbatim in atlas entry **202**.
- **`README.md:815`** — *"**Sobrevivientes** (Datasketch, **2017–**, `datoscontrafeminicidio.net/en/art-and-data-to-make-feminicide-visible/`) … build the count a state refuses to keep, **from news
  reports and testimony**"*. I fetched it: 200, 144,626 bytes, titled *"Art and Data to Make Feminicide
  Visible"*. It names DataSketch; it contains **no "Sobrevivientes", no "2017", and no "testimon-"
  anywhere in the raw bytes.** All three are verbatim in atlas entry **199**, whose `source_url` is
  that page.

Neither detail is false — both are sourced, in the atlas this section already cites and quotes.
What is wrong is the address a stranger is sent to. The companion bullet is the house's own standard:
*"this house … does not cite an address it did not open."* Opening an address is not the same as the
address carrying the claim. By contrast `dusp.mit.edu` supports its bullet fully — D'Ignazio, Fumega,
Suárez Val, MIT Data + Feminism Lab, 2019, counterdata, the AI news-alert system, all on the page.

**Smallest repair:** attribute both to the atlas entry (*"atlas entry 202"*, *"atlas entry 199"*) as
this section already does for the companion list, or move the quoted label and the year behind a
source that carries them. **The searches:** `grep -rn "People excluded from housing" .` and
`grep -rn "Sobrevivientes" .` — one file each, `README.md:771` and `:815`.

---

# NOTED — not blocking

**N1. Condition 1 is built, and it is exactly right — this is the best-verified thing on the face.**
Every one of the nine printed `check` commands was run tonight as a stranger would run it, from the
repository root, and **9 of 9 return their own stop's printed share, printed fraction and printed
certain count**: `100 %–100 % · 11 of 11 · 0` … `33 %–100 % · 11 of 2–33 · 2` … `31 %–100 % · 11 of
4–35 · 4`. The instants are not decorative either. `arrive.proof` claims OBSERVED — *"the instant
below is when this record first held every name the stop adds, read off the captures and not
chosen"* — and I re-derived all nine independently from the 27 capture files: **9 of 9 exact**,
including the one that proves the claim is precise rather than approximate. Stop 6's instant is
`2026-08-10T22:41:12Z` and **not** `…T17:47:21Z`, when the 10 August edition first appeared: the
17:47 copy held ten of that stop's names and the 22:41 copy held the eleventh. The face prints the
later instant, which is the true one under its own sentence. The OBSERVED word matches the page's own
legend for it — *"what this page saw, and when it first saw it"*.

**N2. The certain count entered the frame without the cardinal sin, and that is what session 89
blocked on.** `certain_of` reads `0 · 0 · 0 · 0 · 0 · 0 · 0 · 2 · 4` across the stops; I reproduced
each from the captures (`day.py --as-of` prints exactly 0, 2 and 4 `certain` rows at the matching
instants, and the four at the last stop are `PANOFI FORE RUNNER`, `ISABELLA`, `LUCKY TJ`,
`HEATHER LYNN`). The tier line was widened to name it — *"DERIVED — this share, **and the count of
names certainly dark beside it**, are worked out here, from saved copies of those lists. Nobody
publishes either."* — and **both halves of that sentence are true of both quantities**: both are
computed here from the week-wide return bands in the saved copies, and upstream publishes neither and
could not. DERIVED is the right word: the page's own legend gives DERIVED *"the dark-and-return
spans, this page's share…"* and OBSERVED only what the page saw. The numeral therefore stands under
the same tier line, in the same section, as the two numerals it rides beside — which is the settled
structure of this head and not a new inheritance.

**N3. Session 89's three blocking items on this object are discharged, and I checked each on the
built page.** §1: `since_note` now reads *"The first list that could add a name ruled out of that list
**is** the one dated 12 August 2026, **and it has arrived: two of the twenty-four are ruled out of
it.**"* §2: the same string now carries its own tier clause — *"Both counts are this record's own:
the names are OBSERVED in the saved copies, and how far each window reaches is DERIVED from the
duration the list published."* §3: *"until tonight"* is gone from both face strings; the eight
remaining instances are all in code comments, where this house has always allowed them.

**N4. The caveat stopped counting and stopped branching, and what is left is true.** One string at
all nine stops: *"a name counts as certain here only when every day of that week leaves it dark on
this one; the rest are possible."* That is `day.py:143-163`'s rule stated correctly — `in_all` over
every candidate end of the published window.

**N5. Every guard in the README's table was re-run tonight and every number matches except the one in
blocking item 4.** `data.py --check` → *"island matches the captures"*, exit 0. `gaps.mjs` → *"35
rows, 0 failing … 1.42 px own · 9.59 px next"*, PASS, exit 0. `tiers.mjs` → pass, exit 0.
`announce.mjs` → 1 live region, 4 writes in 30 s, 3 spoken, 10 figure rewrites, stop pressed at
3,000 ms announced at **3,195 ms**, exit 0 — the README's *"3.0 s … 3.19 s"* is right to the
millisecond. `fold.mjs` → **108 failures, exit 1**, taken without a pipe. `frame.mjs` → exit 0.

**N6. The README's account of what `fold.mjs` is red about is correct, and I checked it by counting
the instrument's own marks.** `fold.mjs:124` counts a failure only for a span with `must: true` at
viewport width ≤ 480. The two must-hold spans are `#sd-arrive-ladder` and `#sd-arrive-state`
(`fold.mjs:52-53`); the figure and the hole's heading are reported and **not** counted. Tally of
tonight's run: controls off-viewport **54**, run's line off-viewport **54**, total **108** — exactly
the README's *"12 failures per stop … six of the controls and six of the run's line, at 390 px, on
all nine stops"*. **`✗COVERS` appears zero times in the whole run**, so the occlusion defect
`KRITIKER-84.md` condition 2 was built for stays fixed at nine stops.

**N7. Nothing moved under this pass, and `RENDERS.json` proves the renders are of this object.**
`index_sha256` matches the object byte for byte, and all three output hashes recompute. This is the
first gate in three where the sighted material did not change under the voices judging it
(`VERIFIER-89.md` N7).

**N8. The 27th capture is real, current, and not yet in git.** `projects/season1/captures/2026-08-12T232100Z.json`
is untracked. Its `fetch` block — 200, 31,635 bytes, `14ddeb5c…`, content `005c4e9f…`, edition
12 August 2026, 10 vessels, 257 examined — matches the island's 27th ledger row exactly, and its body
is byte-identical to the 26th copy, which is why 27 copies still give 9 editions, 10 contents and 16
bodies. **But the face's headline `27 capture(s)` and `data.py --check` both depend on a file that is
not committed**, so a stranger cloning HEAD tonight would read 26. The session's own commit closes
this; it is noted so that it is closed and not assumed.

**N9. The ledger caption still measures true at 27 copies.** *"Six lists came back in more than one
set of bytes each"* — I counted distinct body hashes per edition from the capture files: 1, 2, 2, 1,
2, 2, 2, 3, 1 → **six editions with more than one**, 16 distinct bodies. ✓

**N10. `arrive.constant` — this house's most expensive sentence — is still true.** *"The upper end
holds at 100 % until more of these ships are certainly dark on this day than the eleven the day
itself named"*: certain = 4, 4 < 11, fixed end `–100 %`. It survived the night the certain end
doubled.

**N11. Two figures on the face I could not fault, checked at instants of my own choosing.** At
`2026-08-11T23:59:59Z` and `2026-08-12T00:00:00Z` the record still reads 33 %–100 %, 11 of 2–33, 24
copies; at `2026-08-12T18:23:11Z` — one second before the ninth edition's first copy — 33 %, 25
copies; at `18:23:12Z` and after, 31 %, 11 of 4–35. The ceiling only falls, and it falls at the
instant the face says it does.

**N12. The Left-to-die Boat figures are supported, but not from the raw bytes of either address.**
`forensic-architecture.org/investigation/the-left-to-die-boat` returns **200** and **931 bytes of
script shell** — no text at all in the HTML; `fidh.org/IMG/pdf/fo-report.pdf` returns **200** and
7,241,916 bytes of genuine report (I confirmed its identity from its own bookmark titles: *"NATO
MARITIME SURVEILLANCE AREA (MSA)"*, *"DRIFT MODEL"*, *"2.10 DRIFTING BACK TO THE LIBYAN COAST"*), but
this environment has no PDF text extractor and I could not read it. Through a rendering extractor the
Forensic Architecture page yields, verbatim: *"with seventy-two migrants on board"*, *"they were left
to drift for 14 days"*, *"only nine of the passengers survived"* (72 − 9 = **63**), *"it remained
within the NATO maritime surveillance area"*, publication date 11 Apr 2012. **README's 72 / 63 / 14
days / NATO / 2012 all hold.** I record the route because the reader who clicks with scripting off
sees nothing.

**N13. Cennetoğlu is verbatim and correctly hedged.** The biennial.com page carries, word for word,
*"The List of 34,361 documented deaths of asylum seekers, refugees and migrants who have lost their
lives within or on the borders of Europe since 1993. Documentation as of 5 May 2018 by UNITED for
Intercultural Action"*, and *"Since 2007 … Banu Cennetoğlu has facilitated up-to-date and translated
versions of The List using public spaces"*. The README's caveat — *"that figure is the 2018 edition's
and the list has been updated since"* — is supported by the same page (*"Compiled and updated each
year"*). The atlas half of the claim is also right for this work: 0 hits.

**N14. Five hairlines, for the record, none of them worth a night.**
(a) The new paragraph's *"seven-day window"* is upstream's published figure and stands with no tier
word of its own — but so do the three other places this face prints that window, so tonight adds a
fourth instance of a standing pattern rather than a new defect.
(b) The certain band's candidate ends run `edition − 7 … edition` **inclusive — eight days**, which
the caveat calls *"that week"*. One day looser than the arithmetic, in language the work has used
since it had a head.
(c) `index.html:311-318`, a CSS comment, says the two proof strings are *"a fixed 20 and 78
characters at every stop"*. Measured at all nine stops: **20 and 79**. The claim it exists to make —
that the block cannot change height mid-run — is unaffected.
(d) The README's *"where it was 11 (six and five) last night"* is the one guard figure I could not
check, because checking it means running the instrument against a superseded object.
(e) `projects/season1/PROJECT.md` is unchanged tonight and says **26 saved copies**; the record holds
27. It is stamped *"As of session 89"*, its share, editions, contents and bodies are all still right,
and session 89's blocking items 4 and 5 against that file were paid. Outside the object; noted so the
end of this session does not forget the one figure that moved.

---

## What I looked for and could not fault

- Every stop's share, fraction, total, added names and heading, at all nine stops, against `day.py`
  run at that stop's own instant.
- The tier line's truth for both quantities it now names (N2), and the proof block's OBSERVED against
  the page's own legend (N1).
- The de-branched caveat against `day.py`'s `in_all` rule (N4).
- The whole guard table except one number (N5, N6), and the ledger's 27th row against the capture
  file it is drawn from (N8, N9).
- The two upstream method-sheet quotations, both **verbatim** (they are quoted correctly; item 2 is
  about what the second one is made to say).
- The HRDAG author, title, publisher and date, all **exact** (item 1 is about the claim, not the
  citation).
- `505` and the three genuinely absent neighbours (item 3 is about the fourth).
- No claim of illegality is made on this face against any vessel or state; upstream's restraint is
  printed twice from one string.

---

*Published with the work, pass or fail. The five blocking items cost one rewritten clause, one
corrected sentence, one number, and two addresses — and four of the five are the same lesson, learned
the first night this work cited anything outside itself: **a quotation is evidence for what it says,
and for nothing standing next to it.** The work's own arithmetic has never been in better order than
it is tonight.*
