# VERIFIER 84 — 2026-08-10 — premiere gate — blocking, and it blocks on six

Facts and tiers only; no vote on form, staging or taste. Upstream fetched live tonight, directly,
at 200. Everything below was run by me on this machine against the files as committed in
`c28f01b`; every command is printed so a stranger can run it again.

**What I ran, in order.** `capture/day.py 2026-08-04` · the same with `--as-of` at seven instants ·
`capture/day.py 2026-08-01` · `capture/edition.py` · `still-dark/data.py --check` · `gaps.mjs` ·
`announce.mjs` · `render.mjs` · `tools/fold.mjs` (on the committed page, on `HEAD~` and on a copy
of tonight's page with the new media block deleted) · `tools/renders.py` · `tools/selftest.sh` ·
`tools/tiers.mjs` (default and `--stop=6`) · a headless browser at 390×844 sweeping every scroll
position inside the head · `curl` on `https://frankbueltge.de/ghost-fleet/`,
`https://frankbueltge.de/werke/ghost-fleet/` and `https://biblio.ugent.be/publication/8647789` ·
two synthetic capture directories built beside the record, never inside it, to make the head's own
rule falsifiable.

---

## 1. THE FACE, FIGURE BY FIGURE — (a)

Reading order is `STATE-1.txt`, which is what a screen reader receives. "where the word stands" is
measured from the figure, in reading order.

| figure on the face | tier word, and where it stands relative to the figure |
|---|---|
| `4 AUGUST 2026` (title, L1) | none. A chosen subject, not a measurement. Carried. |
| `100 %–100 %` → `79` → `69` → `65` → `55` → `44` → `37 %–100 %` (head, L9) | **DERIVED**, L43, four blocks *after* the figure: *"DERIVED — this share is worked out here, from saved copies of those lists."* Marked, not adjacent. `tiers.mjs` passes it on section scope. |
| `100 %` inside the constant line (L12) | same DERIVED line, after. Marked. **But the sentence around it is false — §2.1.** |
| "eleven ships" (heading_then, L14) | no adjacent word; governed only by the section's DERIVED line four blocks below. Carried, unblocked, as in 83. |
| "three / five / six / nine / fourteen / nineteen ships" and "the last three / two / of them / three / five / five" (heading_since, stops 1–6) | same: no adjacent word. **These strings were rewritten tonight and no mark was added with them.** Carried. |
| "Seven lists, seven answers … six days after … The eleven names" (caption, L41) | none adjacent; section DERIVED line follows two lines later. |
| "seven states over about twenty-four seconds" (run line, under the buttons) | **no tier word, no arithmetic, no citation on the face.** DERIVED in fact (14,118 + 6×1,600 = 23,718 ms → 24). Carried from 83. |
| "Eleven … Nineteen … fourteen of them" (lede, L47) | **DERIVED**, in the same sentence group: *"All three counts are DERIVED."* Marked. 83's repair holds. |
| "at least 12 hours dark, at least 50 nautical miles offshore" (L49) | attributed in prose (*"its own source classifies"*); no tier word. SOURCED in fact. Carried. |
| `56 d dark`, name, flag, waters (30 rows) | **SOURCED**, legend L53: *"name · flag · days dark · waters · each list's own date and ship count — printed by the instrument"*. Marked, before. |
| "dark 2–9 Jun → back 28 Jul–4 Aug" (30 rows) | **DERIVED**, legend L54. Marked, before. |
| "this page first saw all eleven on 5 AUG" (7 blocks) | **OBSERVED**, legend L55. Marked, before. |
| edition strip `2 JUN … 4 AUG` (L57–66) | no tier word covers dates. Carried from 83. |
| block heads "IN THE LIST OF 4 AUG — the day itself (11 ships)", "(3 ships)", "(2 ships)"… | legend's SOURCED line now reads *"each list's own date and ship count"*, which is **not** what these counts are: the 5 AUG list carried **eight** ships, the block says three. The ledger caption discloses the difference in words. Carried, disclosed, not blocking. |
| `69 %–100 %`, `11 of 0–16`, `37 %–100 %`, `11 of 0–30`, "5 saved copies of 3 lists", "19 saved copies of 7 lists", "It fell 32 points", "Thirty ships … 11 of 30 to 11 of 11", "6 August 2026 at 08:36 UTC, in commit 91ee19b" | **NO TIER WORD IN THE SECTION.** `#sd-fall` contains none. This house's own instrument, built and committed tonight, says so and exits 1 — **§3.3.** |
| ledger `fetched / status / bytes / body / content` | **OBSERVED**, caption above. Marked. |
| ledger `edition` and `ships in that list` | **SOURCED**, legend, repaired in 83. Marked — **and the value in the last column is wrong for the two 10 August rows, §3.2.** |
| terminal block | *"verbatim, unedited"*; matches `day.py` byte for byte tonight (checked against my own run). |

**FAIL** — the nine figures in `#sd-fall`, the page's live headline among them.

## 2. TONIGHT'S SENTENCES, AGAINST THE ARITHMETIC THEY DESCRIBE — (b)

### 2.1 The constant line is still false, in its repaired form — BLOCKING

`index.html:868`, built at `data.py:651-657`:

> *"Neither end of this figure can rise. The upper end has not moved at all: it holds at 100 %
> while no ship here is CERTAINLY dark on this day — a list gives a return only to the nearest week,
> so every one of them is merely possible — **and it falls the moment one of them becomes certain.**
> Only the lower end has moved so far, and the next list can lower it again."*

`capture/day.py:208-216` computes the upper end as `obs / max(n_lo, obs)` — the numerator eleven,
`n_lo` the count of vessels **certainly** dark on the day. `max(n_lo, 11)` is eleven for every
`n_lo` from nought to eleven. **The upper end does not fall when one ship becomes certain. It falls
when the twelfth does.**

Run against the work's own instrument, on copies of the record with one probe edition added
(edition 2026-08-11, vessels dark 20 days — certain for 4 August under every feasible end):

```
python3 capture/day.py 2026-08-04 --captures <record + 1 probe vessel>
  vessels dark on that day .......... 1–31      SHARE ... 35%–100%  (11 of 1–31)
python3 capture/day.py 2026-08-04 --captures <record + 11 probe vessels>
  vessels dark on that day .......... 11–41     SHARE ... 27%–100%  (11 of 11–41)
python3 capture/day.py 2026-08-04 --captures <record + 12 probe vessels>
  vessels dark on that day .......... 12–42     SHARE ... 26%–92%   (11 of 12–42)
```

One certain: 100 %. Eleven certain: 100 %. Twelve certain: 92 %.

This is banked failure 31 **inside its own repair**. Last night this house caught *"The upper end
never moves"*, withdrew a 4-of-4 score for it, banked the failure, and wrote a replacement sentence
that states a threshold the code does not have. The first clause of the same sentence — *"Neither
end of this figure can rise"* — I checked and it is **true**: `n_lo` and `n_hi` are both monotonic
non-decreasing across further editions, so both ends are non-increasing.

The face contradicts itself on this within the same page: `#sd-fall` says, correctly, *"the share
runs from 11 of 30 to 11 of 11"* — a denominator floored at eleven, which is exactly what the head
denies four blocks above.

### 2.2 The (w) repair — PASS

`data.py:511-525`. Every stop's second heading now reads *"NAMED ONLY BY LATER LISTS — N ships that
could have been dark on that same day and that nobody could have had on it."* Checked at all seven
stops in a browser. Counts: 0, 3, 5, 6, 9, 14, 19 — each equals the running total minus the eleven
of the first block, and 11 + 19 = 30, which is `day.py`'s band. The word *"dark"* no longer stands
as an assertion, and the heading now agrees with the hedge (*"not one of these names is certainly
dark on this day"*) and with the band (*"could have been dark … and not one of them certainly"*).
The item is genuinely paid.

### 2.3 The (z) repair — PASS on its arithmetic

Each heading ends with a sentence naming the mark. Checked stop by stop against the DOM:

| stop | heading says | chips in the block | chips carrying `.sd-arrive-new` |
|---|---|---|---|
| 1 | "The last three, in darker ink, … 5 AUG" | 3 | 3 |
| 2 | "The last two … 6 AUG" | 5 | 2 |
| 3 | "The last of them … 7 AUG" | 6 | 1 |
| 4 | "The last three … 8 AUG" | 9 | 3 |
| 5 | "The last five … 9 AUG" | 14 | 5 |
| 6 | "The last five … 10 AUG" | 19 | 5 |

The marked names are appended last, so *"the last N"* is true of DOM order as well as of paint. The
mark is real in the stylesheet (`index.html:197-201`: `color: var(--sd-ink)`, `border-color:
var(--sd-ink)`, `font-weight: 700`). The heading names one of the three (ink) and not the other two;
that is under-description, not falsehood. Arithmetic clean.

### 2.4 The (y) repair does less than the sentence that describes it — BLOCKING

See §3.4. The CSS is real and `fold.mjs` is real; the **claim published about them** is false.

### 2.5 "Since session 84 the head says only what its own arithmetic says" — FALSE

`README.md:83`. The head's constant line is the counter-example, §2.1. This is the sentence that
introduces tonight's three repairs, and it is the class of well-put sentence this gate was told to
distrust.

### 2.6 The first beat — PASS

`data.py:797`: `gloss_words / 238 * 60000`. Hand count of the gloss, letter-or-digit tokens: 12 in
the first sentence, 24 in the second, 20 in the third = **56**. `first_dwell_note` prints "56 words
at 238 wpm" ✓. 56 ÷ 238 × 60000 = 14,117.6 → `first_dwell_ms: 14118` ✓. `run_seconds =
round((14118 + 6×1600)/1000) = 24` ✓, and the run line says "about twenty-four seconds" ✓.
`announce.mjs` re-run tonight: figure states at 76, 14182, 15782, 17382, 18982, 20582, 22182 ms —
seven states, run 23.7 s, **3 spoken announcements**, 1 live region. The README's numbers hold.

Citation checked live: `https://biblio.ugent.be/publication/8647789` → 200, and carries *"Based on
the analysis of 190 studies (18,573 participants), we estimate that the average silent reading rate
for adults in English is 238 words per minute (wpm) for non-fiction"*, JOURNAL OF MEMORY AND
LANGUAGE 109, 2019. ✓ The URL stands in the shipping file (a comment above the run code). It does
not stand on the face; the face prints "about twenty-four seconds" with no citation. Carried from 83.

**Carried, not blocking:** the `waiting` state says *"a pause as long as the paragraph under the
title takes to read"*. The page's title is `4 AUGUST 2026`; the paragraph under it is the subtitle,
sixteen words. The paragraph the beat is derived from is the third. 83's repair replaced one wrong
label with an ambiguous one.

**FAIL** (2.1, 2.4, 2.5).

## 3. CONTRADICTIONS AND WHAT IS TRUE INSTEAD — (c)

### 3.1 "eleven ships, all that the day held about itself" is false of the 4 August edition — BLOCKING

`index.html:626` (`data.py:619-621`). The 4 August edition also printed an aggregate block, which
this house's own capture script records as SOURCED and this house's face has never printed. From
the committed capture `captures/2026-08-05T043932Z.json`:

```
aggregates: dark_inside_national_waters 82 · disappearances_examined 230
            in_the_window 5641 · vessel_days_of_darkness_approx 3712
```

Every capture holds one (the live page tonight prints *"91 ships went dark inside national waters
lately — of 213 disappearances examined (5,645 in the window). Together about 2,941 vessel-days of
darkness."*). So on the day whose eleven names this face calls *all that the day held about itself*,
the day's own edition also held eighty-two. The heading overclaims against the instrument it reads.
Confirmed first-hand from the committed bytes; `KRITIKER-84.md` reached the same block independently
tonight.

### 3.2 The record lost a vessel upstream printed, and the headline figure moves — BLOCKING

`capture/capture.py:64-69`. `CASE_RE` requires the case-of-the-day flag to match `\(([A-Z]{3})\)`.
The 10 August edition prints:

```
<p class="mt-2 text-lg font-semibold">HY928-21%-81% <span class="font-mono text-sm text-fg-faint">(—)</span></p>
<p class="mt-3 leading-snug text-fg-muted"> A vessel flagged — switched off its transponder for 50
days — vanished at 2.7°S, 177.7°E, resurfaced at 3.1°S, 175.2°W, in Kiribati EEZ (Gilbert Islands). </p>
```

The flag is an em dash. The regex does not match, `case_of_the_day` is written `null`, and the
vessel is dropped with no error. **Both 10 August captures — the eighteenth and tonight's
nineteenth — hold ten vessels where the page names eleven.** Every one of the other seventeen
captures holds its case of the day (TUNAMAR, MICRONESIA103, ALBACORA CUATRO, TUNA PESCA); TUNAMAR is
the first row on this face. `day.py:108` has an explicit branch for `role == "case_of_the_day"`, so
this is a parse failure, not a rule.

What it costs, run on a copy of the record with that one vessel restored:

```
python3 capture/day.py 2026-08-04 --captures <record + the dropped case of the day>
  vessels dark on that day .......... 0–31 (certain–possible)
  SHARE knowable on the day ......... 35%–100%  (11 of 0–31)
```

The face prints **37 %–100 %, 11 of 0–30**. With the vessel the instrument actually published, it is
**35 %–100 %, 11 of 0–31**. The band sentence *"Thirty ships could have been dark on 4 August 2026"*
is thirty-one. And the OBSERVED ledger's last column, marked **SOURCED** by last night's repair as
*"each list's own date and ship count — printed by the instrument"*, prints **10** for a list on
which the instrument printed eleven vessels.

Nothing in this house can catch this: the captures keep no body, so no check re-parses the bytes;
`data.py --check`, `edition.py`, `renders.py` and `selftest.sh` all compare the face to the captures
and all passed tonight. The failure is upstream of every instrument here.

### 3.3 Nine printed figures stand in a section with no tier word — BLOCKING

`tools/tiers.mjs`, written and committed tonight by this house, run by me at width 1400 at the
resting stop and at `--stop=6`:

```
NODE_PATH=... node tools/tiers.mjs          → exit 1
NODE_PATH=... node tools/tiers.mjs --stop=6 → exit 1
TIERS: 9 printed figure(s) stand in a scope with no tier word.
```

All nine are in `#sd-fall`: the superseded provenance line, `69 %–100 %`, `11 of 0–16`, *"It fell 32
points…"*, *"…from 19 saved copies of 7 lists"*, **`37 %–100 %`**, **`11 of 0–30`**, the band
sentence, and the commit line. That section contains no tier word at all. This is banked failure 25 —
the page's largest number standing unmarked — standing again, on the night this house built the
instrument that was written down to catch it. The commit message discloses the finding. **The page
ships with it.** A check that reports a failure and is committed anyway is not a check.

### 3.4 The (y) claim against what the (y) repair does — BLOCKING

`README.md:100-101`: *"They are now inside the viewport at every stop and at every scroll position
within the head (`tools/fold.mjs`, committed, which exits non-zero if either leaves it)."*

`fold.mjs` tests **two** scroll positions per viewport (`0`, and the head's bottom aligned to the
viewport bottom), not every one. I swept every 20 px at 390×844 in a headless browser and then
bisected:

```
head section #sd-arrive spans page y 85–1438 at 390×844
the controls  leave the viewport from scrollY 1027
the run's line leaves the viewport from scrollY 1081
```

From scrollY 1027 to 1438 — **411 px, about 30 % of the head's own scroll range** — a phone reader
is still inside the head, reading its caption, its DERIVED tier line and its restraint line, with the
controls gone; from 1081, with the live line gone too. That is the defect (y) was written to repair,
at a scroll position the instrument does not visit. Screenshot taken at scrollY 1100 and looked at:
neither element is on screen.

Second measurement, same repair: the pinned band is opaque (`background: var(--sd-bg)`, `z-index: 2`)
and at scroll 0 it occupies page y 720–844, while the later-list name chips occupy 719–946. Counted
in the browser at 390×844, stop 6, scroll 0:

```
tonight's page with the media block deleted : 10 of 19 chips fully inside the viewport
the page as committed                       : 10 inside the viewport, 0 of them above the band
                                              (band top y=720) — none visible
```

I took the screenshot and looked at it: the heading *"…The last five, in darker ink, arrived with the
list of 10 AUG"* stands directly above the button row with no names between them. **The (y) repair
paints over the names the (z) repair added words about**, at the first-encounter view on the width
(y) was built for — ten chips visible before, none after. Whether that trade is acceptable is the
staging voice's ruling, not mine; that it happens is a measurement, and the README's account of the
repair does not contain it.

**What in the README's (y) bullet is true:** *"measured at 390×844, the controls stood at y=1004 and
the live line at y=1057"* — I reproduced both on the page as committed before tonight
(`fold.mjs --dir=<HEAD copy>`), and *"On the page as committed before tonight it returns 14 losses;
on tonight's, none"* — I reproduced both counts. (`index.html`'s own comment on the same repair cites
`DRAMATURG-83.md`'s y=938 / y=991 instead; the two records of one measurement differ by 66 px and
neither says which instrument produced it. Not blocking; the README's pair is the reproducible one.)

**FAIL** (3.1, 3.2, 3.3, 3.4).

## 4. THE NUMBERS — (d)

> `day.py 2026-08-04`: *"19 capture(s) read, 7 distinct edition(s), 7 distinct content(s), 11
> distinct bod(y/ies)"*; *"0–30"*; *"11"*; *"37%–100% (11 of 0–30)"*. `edition.py`: 19 rows, 7
> edition dates, 11 bodies — identical to the face's ledger row for row, hash for hash, including
> the two new rows for `2026-08-10T17:47:21Z` and `2026-08-10T22:04:56Z`. `data.py --check`:
> *"island matches the captures"*. `gaps.mjs`: **PASS**, 30 rows, 1.42 px own against 9.59/11.52 px
> next. `renders.py`: **RENDERS MATCH THE PAGE**. `selftest.sh`: **PASSED**.
>
> **The nineteenth copy added nothing to the number, and nothing on the face or in the README claims
> it did.** `--as-of 2026-08-10T20:00:00Z` (before tonight's fetch) already returns *"37%–100% (11 of
> 0–30)"* from 18 captures and 7 editions; the new capture is byte-identical to the eighteenth
> (`90bd7aec…` / `7b3444ad…`, 32,240 bytes) and matches the live page I fetched tonight. The README's
> table row *"as measured at session 84, 19 saved copies / 7 lists · 37 %–100 % · 11 of 0–30"* is
> correct, and the README correctly does **not** claim a sixth fall.
>
> Ladder of `--as-of` reproductions, all run: 79 % at `2026-08-06T04:36:19Z` (4/2), 69 % at
> `08:36:39Z` (5/3), 65 % at 8 Aug 00:00 (9/4), 55 % at 9 Aug 00:00 (13/5), 44 % at 10 Aug 00:00
> (16/6), 37 % at 10 Aug 20:00 (18/7). The head's seven stops print exactly this ladder.
> Arithmetic on the face: 11+3+2+1+3+5+5 = 30 ✓ · 30−11 = 19 ✓ · 1+3+5+5 = 14 ✓ · 69−37 = 32 ✓ ·
> 11/30 = 36.67 → 37 ✓ · 55−44 = 11 ✓ · 44−37 = 7 ✓. The first beat: §2.6.
>
> **PASS on internal consistency — and every one of these numbers is subject to §3.2**, which is a
> defect in the denominator itself and not in any arithmetic done on it.

## 5. THE README, LINE BY LINE — (e)

> **False now:**
> - **L83** *"Since session 84 the head says only what its own arithmetic says"* — §2.1.
> - **L77** *"it holds at 100 % only while no ship is **certainly** dark on the day"* — **false, in
>   the block correcting last night's falsehood about the same clause.** It holds at 100 % while up
>   to **eleven** are certain. Same arithmetic as §2.1.
> - **L100-101** *"inside the viewport at every stop and at every scroll position within the head"* —
>   §3.4.
> - **L201** *"a stranger reads *"the button went"* three paragraphs after reading that the head has
>   six"* — the head has **seven** stop buttons, and the README itself says *"seven buttons"* at L34.
>   **`VERIFIER-83.md` §4 named this string and `VERIFIER-83.md`'s own table reported item 7
>   REPAIRED, every one listed.** It was not. A claimed repair that did not happen is banked
>   failure 7's shape.
> - **L210** *"rather than eighteen rows of truncated sha256"* — **nineteen** since tonight's copy.
>   Repaired from "seventeen" to "eighteen" last night and stale again twenty-four hours later; the
>   fourth session running that this document has carried a false figure.
>
> **Stale by omission:**
> - **L298** *"`tools/fold.mjs` is the third"* — session 84 committed **two** instruments;
>   `tools/tiers.mjs` appears nowhere in this document, and it is the one that currently fails.
> - **L12** *"six buttons a visitor presses"* — named false by `VERIFIER-83.md` and not repaired. It
>   sits inside a session-81 correction block and is defensible as history (session 81's head had six
>   stops, `2c42458`), but the house should say which it is.
>
> **Checked and true tonight:** L21-22 (`ON THE DAY` through `+6 DAYS`, seven buttons ✓) · L24-27
> (56 words, 238 wpm, 14,118 ms ✓, citation resolves and carries the sentence ✓) · L30-31 (8 words =
> 2,017 ms and 5 words = 1,261 ms, summing to 14,118 − 10,840 = 3,278 ✓) · L56-57 (three spoken
> announcements, seven figure states, twenty-four-second run — re-measured ✓) · L87-95 (the (w) and
> (z) accounts match the built page ✓) · L96-99 (y=1004 / y=1057 reproduced ✓) · L138-142 (the
> three-row table, all three rows reproduced by `--as-of` ✓) · L169-180 (five falls, every ship named
> against `day.py`'s own list ✓; eleven points on 9 Aug ✓, seven on 10 Aug ✓) · L248 (nineteen copies,
> eleven bodies, seven lists ✓; four lists with more than one body — 5, 6, 8, 9 Aug ✓) · L253-258
> (554 bytes = 36,071 − 35,517 ✓, and `page_assets` moves `/_astro/TopBar.SLcnmZbT.css` →
> `/_astro/Base.BvXYJsAy.css` between those two captures ✓) · L295 (1.42 px against 9.59 px, 0 of 30
> rows failing ✓) · L304-305 (14 losses on the committed page, none on tonight's ✓).
>
> **FAIL.**

## 6. MEASUREMENTS NOBODY TOOK — (f)

> One on the face, none in the arithmetic, two in the README.
> - **§3.4** is the pure case: a claim about *"every scroll position"* attributed to an instrument
>   that visits two, and false at the positions it does not visit.
> - **§2.1** is its sibling: a threshold asserted about the work's own code that the code does not
>   have, and that nobody ran the code to check — the second night running for the same sentence.
> - Everything else this house published tonight as measured, I re-measured, and it held: the 14
>   fold losses, the y-coordinates, the three announcements, the 30-row gap field, the 14,118 ms
>   beat, the five falls, the 554 bytes and their asset attribution.
> - `PROJECT.md` still reads *"As of session 83 … from 18 saved copies"* and is not yet rewritten for
>   tonight. Noted, not blocking: it is the record kept at the end of a session, not the work's face.

## 7. UPSTREAM, FETCHED LIVE — standing obligations

> `curl https://frankbueltge.de/ghost-fleet/` → **200, 32,240 bytes, sha256 `90bd7aec…`** — the
> identical body this record saved at 17:47 and again at 22:04 tonight.
> `curl https://frankbueltge.de/werke/ghost-fleet/` → **200, 27,640 bytes**.
>
> Exact-substring tests of the face's quotations and restraint sentences against tonight's live text,
> character by character, all **True**:
> - *"The AIS picture of the seas looks complete. It is not — ships switch off their transponder on
>   purpose to vanish."* — present verbatim on the method sheet, em dash and all.
> - *"is a probability, not proof"* — present: *"The „intentional" label comes from GFW's
>   machine-learning model and is a probability, not proof (GFW says „likely"). We pass that on
>   openly and make no accusation."*
> - *"No claim of illegality against vessel or state."* — present, §4 Limits of the method.
> - *"GFW returns only high-confidence, intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore,
>   good satellite coverage"* — present. The face carries the first two limbs and not *"good
>   satellite coverage"*; carried from 83, disclosed here again.
> - *"Daily. Window: disabling events that ended in the last 7 days"* — present, and it is the warrant
>   for the seven-day band and for *"every list holds only the seven days before its own date"*.
>
> All thirty vessel names on the face carry a live link to a Global Fishing Watch vessel page (30
> `a[href*=globalfishingwatch]` counted in the browser), which is what *"linked name by name"* claims.
> The restraint stands twice, head and floor, verbatim and unaltered. **PASS.**

---

**BLOCKING: 6 item(s)**

1. The head's constant line — *"and it falls the moment one of them becomes certain"* (`index.html:868`,
   `data.py:654`) — is false of `day.py:214`, which computes the upper end as `obs / max(certain, obs)`:
   it holds at 100 % until the **twelfth** ship is certainly dark, as three runs of the work's own
   instrument show (1 certain → 100 %, 11 certain → 100 %, 12 certain → 92 %), and the same false rule
   is repeated at `README.md:77` inside the block correcting last night's version of it.
2. `capture/capture.py:66` requires a three-letter flag, so the 10 August edition's case-of-the-day
   vessel — flagged `(—)`, fifty days dark, Kiribati EEZ — is silently dropped from both 10 August
   captures: the face prints **37 %–100 %, 11 of 0–30** where the record's own rule gives
   **35 %–100 %, 11 of 0–31**, the band says thirty for thirty-one, and the ledger's SOURCED *"ships
   in that list"* prints **10** for a list on which the instrument printed eleven vessels.
3. Nine printed figures stand in `#sd-fall` with no tier word in that section — the page's live
   headline `37 %–100 %` and `11 of 0–30` among them — as this house's own `tools/tiers.mjs`, built
   and committed tonight, reports on exit 1 at both the resting stop and stop 6; the page shipped with
   the failure disclosed in the commit message and unrepaired.
4. `README.md:100-101` claims the controls and the run's line are *"inside the viewport at every stop
   and at every scroll position within the head"*, and they are not: at 390×844 the controls leave the
   viewport from scrollY 1027 and the live line from 1081, with the head running to page y 1438 —
   411 px, about 30 % of the head's scroll range — and `fold.mjs`, the instrument the claim cites,
   tests two scroll positions and passes.
5. The (y) repair's pinned opaque band paints over the later-list names on the screen it was built
   for: at 390×844, stop 6, scroll 0, ten of the nineteen chips stood inside the viewport before the
   repair and **none is visible after it** (all ten lie under the band, top edge y=720), directly
   below a heading reading *"The last five, in darker ink, arrived with the list of 10 AUG"* —
   measured and photographed; the trade is staging's to rule on, its absence from the README's
   account of the repair is not.
6. The README carries two live false figures — `L201` *"the head has six"* (seven stop buttons; named
   by `VERIFIER-83.md` and reported repaired when it was not) and `L210` *"eighteen rows of truncated
   sha256"* (nineteen since tonight) — the fourth session running that this document has been stale,
   and `tools/tiers.mjs` is committed and undocumented in it.

**Sections: 1 FAIL · 2 FAIL · 3 FAIL · 4 PASS (internal consistency only, subject to blocking 2) ·
5 FAIL · 6 FAIL · 7 PASS.**
