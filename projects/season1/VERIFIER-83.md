# VERIFIER 83 — 2026-08-10 — blocking, and it blocked on seven

Facts and tiers only; no vote on form. Convened after the panel and in parallel with the staging
voice, shown neither. Upstream fetched live tonight. **Verbatim, unedited, below the line.**

**WHAT THIS HOUSE DID WITH IT, above the memo so nothing below reads as merely noted.** Of the seven
blocking items, **five were repaired before commit** and **two are owed with their reasons printed**:

| | item | outcome |
|---|---|---|
| 1 | *"The upper end never moves"* is **false of `day.py`'s own arithmetic** | **REPAIRED.** Re-run first-hand: `day.py 2026-08-01` returns **thirteen certain**, so a day's upper end falls as soon as its bands close. The sentence now says what is true — neither end can rise, the upper end has not moved *yet*, and what would move it. **Banked failure 31.** |
| 2 | the lede's three counts carry **no tier word** | **REPAIRED.** The lede now marks all three DERIVED, in the sentence itself. Failure 25's shape, on the page's first line. |
| 3 | the OBSERVED ledger's `edition` and `ships in that list` columns are **SOURCED** | **REPAIRED.** The legend's SOURCED line now names each list's own date and ship count. |
| 4 | stop headings *"N ships dark on that same day"* contradict the hedge | **OWED.** Real, and older than tonight. Not repaired: those headings are the material four severed readers were scored on hours ago, and rewriting them after the reading, unpre-registered, is the defect this house banked as 29. It goes to the gate with its own pre-registration. |
| 5 | *"never a whole day's darkness"* reads as a **duration** filter its own rows refute | **REPAIRED.** Now: *"They carry only offshore switch-offs a machine model classed as intentional, so they are never all of a day's darkness."* |
| 6 | *"a pause as long as the sentence above"* mis-describes a 51-word, two-sentence derivation | **REPAIRED**, and the staging voice found the same thing independently and priced it at 2.2×. It now names the paragraph under the title. |
| 7 | the README's thirteen stale or false statements | **REPAIRED**, every one listed below, plus the paragraph the README owed on tonight's changes. The third session running that this document was stale; the guard it carries covers its figures and has never covered its prose. |

**The repairs of 1, 5 and 6 changed words that four severed readers had already been scored on**,
and item 1 changed the very sentence Q6 measured at 4 of 4. **Q6's discharge is therefore withdrawn
in `PANEL-83.md`'s ruling and re-opened**: this house does not keep a score earned by a sentence its
own instrument refutes.

---

## 1. THE PAGE'S FACE

> **(a) Every published figure, and the tier word that marks it.** Reading order per `STATE-1.txt`:
>
> | figure on the face | tier word, and where it stands |
> |---|---|
> | `100 %–100 %` / `79` / `69` / `65` / `55` / `44` / `37 %–100 %` (head) | **DERIVED** — "*this share is worked out here, from saved copies of those lists*", four blocks below the figure, under the buttons. Marked. |
> | "eleven ships" / "nineteen ships" (run headings) | none adjacent; covered by nothing. |
> | **"Eleven … Nineteen arrived later — fourteen of them after this page had printed its figure."** (lede) | **no tier word anywhere near it, and it stands *before* the legend in reading order.** Three DERIVED counts, unmarked. |
> | "Seven lists, seven answers … six days after" (caption) | none. |
> | `56 d dark`, name, flag, waters | **SOURCED**, legend: "*name · flag · days dark · waters — printed by the instrument*". |
> | "dark 2–9 Jun → back 28 Jul–4 Aug" | **DERIVED**, legend: "*the dark-and-return spans, and this page's share*". |
> | "this page first saw all eleven on 5 AUG" | **OBSERVED**, legend. |
> | `69 %–100 %`, `11 of 0–16`, `37 %–100 %`, `11 of 0–30`, "5 saved copies of 3 lists", "18 saved copies of 7 lists", "It fell 32 points" | **DERIVED** via the legend's "*this page's share*", three blocks above. Marked, not adjacent. |
> | ledger: fetched/status/bytes/body/content | **OBSERVED**, caption. |
> | ledger: **edition** column ("4 August 2026") and **ships in that list** | captioned OBSERVED — but these are upstream's own printed values, i.e. **SOURCED**. The legend's SOURCED line names no dates. Wrong tier word visible. |
> | edition strip "2 JUN … 4 AUG"; "IN THE LIST OF 5 AUG" | SOURCED in fact; no tier word covers dates. |
> | terminal block figures | "verbatim, unedited"; matches `day.py` byte for byte. |
> | run line: "**about twenty-two seconds**" | DERIVED (12,857 + 6×1,600 = 22,457 ms → 22 s ✓). No tier word, no arithmetic, no citation on the face. |
>
> **FAIL** — the lede's three counts and the ledger's two SOURCED columns.
>
> **(b) Tonight's sentences.**
>
> - "*published at frankbueltge.de*" — **true**. Editions are at `https://frankbueltge.de/ghost-fleet/`
>   (`capture.py:46`), method sheet at `/werke/ghost-fleet/`; the face's sources line agrees.
> - "*only offshore switch-offs a machine model classed as intentional*" — **true to upstream**:
>   "*GFW returns only high-confidence, intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore,
>   good satellite coverage*"; "*The „intentional" label comes from GFW's machine-learning model and
>   is a probability, not proof*". The ≥12 h limb is carried later on the face; "good satellite
>   coverage" is carried nowhere.
> - "*never a whole day's darkness*" — **the parse is false.** Following "only offshore switch-offs …",
>   it reads as a second filter on *switch-offs*, i.e. that darkness lasting a whole day is excluded.
>   The face's own rows refute that ("56 d dark"); upstream's exclusions are nearshore, <12 h,
>   never-transmitting ("*dark by default*"), low-confidence. Must be reworded to say what it means:
>   these lists are never all of a day's darkness.
> - **The constant line — "The upper end never moves." FALSE of this work's own arithmetic.**
>   `day.py` computes the upper end as `obs / max(n_lo, obs)` where `n_lo` = vessels **certainly**
>   dark. It is 100 % only while `n_lo ≤ 11`. Run tonight's same instrument on an older day:
>   `day.py 2026-08-01` → "*vessels dark on that day .......... 13–30 (certain–possible)*". Thirteen
>   certain. The moment 4 August's certain count passes eleven — which begins with the edition of
>   11 August, since any vessel dark ≥ 8 days in an edition dated ≥ t+7 is certain under every
>   feasible end — the upper end falls below 100 %. And the reason the sentence offers ("*a list …
>   can never rule out one that never comes back*") argues for an unbounded **total**, which lowers
>   the *lower* end; it does not touch the upper end. That is a rhetorical claim wearing a proof's
>   clothes, and the claim it dresses is false.
> - **Run states**, five, checked against the built page: `waiting` mis-describes its own arithmetic
>   — "*a pause as long as the sentence above takes to read*". The pause is derived from the whole
>   two-sentence gloss, 51 words → 12,857 ms (`data.py:742`). The *sentence* alone is 39 words →
>   9,832 ms. Either the word or the arithmetic is wrong. `done`, `stopped`, `held`, `rest` are
>   accurate to the code.
>
> **(c) Said twice, two values.** The stop headings "*N ships dark on that same day*" assert as fact
> what the hedge two lines away denies: "*not one of these names is certainly dark on this day*", and
> the band: "*Thirty ships could have been dark … and not one of them certainly*". Stop 0 avoids it
> ("nothing yet"); stops 1–6 do not. No numeric contradiction found otherwise: 11+3+2+1+3+5+5 = 30;
> 30−11 = 19; 1+3+5+5 = 14; 69−37 = 32. **FAIL** (b and c).

## 2. THE NUMBERS

> `day.py 2026-08-04`: "*18 capture(s) read, 7 distinct edition(s), 7 distinct content(s), 11
> distinct bod(y/ies)*"; "*0–30*"; "*11*"; "*37%–100% (11 of 0–30)*". `edition.py`: 18 rows, 7 edition
> dates, 11 bodies — identical to the face's ledger row for row. `data.py --check`: "*island matches
> the captures*". 11/30 = 36.67 → 37 ✓. `--as-of 2026-08-06T08:36:39Z` → "*69%–100% (11 of 0–16)*",
> 5 captures / 3 editions ✓. Fifth fall confirmed against the commit record: 79→69 (`91ee19b`, s71),
> 69→65 (s75), 65→55 (s78), 55→44 (s81), 44→37 tonight. "*The eleven names the day itself held cannot
> grow*" — sound: the numerator counts vessels whose first edition date ≤ 2026-08-04, and no future
> fetch of a daily page can return an edition dated 4 August. **PASS.**

## 3. THE FIRST BEAT

> Hand count of the gloss, letter-or-digit tokens, em dashes excluded: dark(1)…tracked(12);
> The(13)…darkness(51). **51.** Page prints "*51 words at 238 wpm*" ✓. 51 ÷ 238 × 60000 = 12,857.1 →
> `first_dwell_ms: 12857` ✓. Citation stands in the shipping file — `index.html:1926-1930`,
> Brysbaert, *JML* 109 (2019), `https://biblio.ugent.be/publication/8647789` — which resolves and
> carries "*the average silent reading rate for adults in English is 238 words per minute (wpm) for
> non-fiction*", from "*190 studies (18,573 participants)*" ✓. Arithmetic and citation clean; the
> **label** is not (see 1b: "the sentence above"). The 238 wpm figure reaches the face inside "about
> twenty-two seconds" with no citation on the face. **FAIL** (label only).

## 4. THE README — stale a third time

> False or stale as of tonight, line by line:
> - **L12, L30, L140** "six buttons" / "*what they have instead is six buttons*" / "*the head has
>   six*" — **seven** stop buttons now.
> - **L21-22** "`ON THE DAY` through `+5 DAYS`" — through **`+6 DAYS`**.
> - **L24-27** "*43 words at 238 words per minute … which is 10,840 ms*" — **51 words, 12,857 ms**.
> - **L23-24** "*the first stop is held for the time its own definition paragraph takes to read*" —
>   it is derived from the subject **gloss**, not the definition paragraph.
> - **L30-31** "*Under the figure the head carries one sentence naming the figure's tier … and
>   nothing else*" — false tonight: the constant line and the run's state line were added.
> - **L83** table row "*as measured at session 82, 17 saved copies / 6 lists · 44 %–100 % · 11 of
>   0–25*" — now 18 / 7 · 37 %–100 % · 11 of 0–30; a session-83 row is owed.
> - **L111** "*The total has now grown four times*" — **five**; the list of 10 August (ATLANTIC
>   PRINCE, GENPUKUMARU NO.18, DIVA MARIA, OCEAN WARRIOR, ST. MARIANNE) is missing from L112-117.
> - **L118** "*tested four times … held four times*" — **five**.
> - **L149** "*seventeen rows of truncated sha256*" — **eighteen**.
> - **L186** "*Seventeen saved copies, ten bodies, six lists, as of session 82*" — **eighteen,
>   eleven, seven**. ("Four lists have come back in more than one set of bytes" is still true: 5, 6,
>   8, 9 Aug.)
> - **L205-206** DERIVED bullet "*both ends of every date*" — the face's legend was repaired in 82 to
>   "*the dark-and-return spans, and this page's share*"; the README still describes the pre-82
>   legend, i.e. it omits the share.
> - **L231-232** "*0 of 20 rows failing*" — the field is now 30 rows; `gaps.mjs` has not been re-run.
> - Nowhere does the README record that the run now announces its own state, or that the premise
>   names the publisher and the filter.
>
> **FAIL.**

## 5. STANDING OBLIGATIONS

> The restraint stands twice on the face, head and floor, verbatim: "*"Intentional" is a machine
> estimate by Global Fishing Watch — a probability, not proof; the instrument makes no claim of
> illegality against any vessel or state, and neither do we.*" Upstream: "*is a probability, not
> proof*" and "*No claim of illegality against vessel or state.*" — both present in tonight's fetch.
> Exact-substring test of the face's quotation against the live method-sheet text: `'The AIS picture
> of the seas looks complete. It is not — ships switch off their transponder on purpose to vanish.'
> in page` → **True** (the island's unrendered `window_quote` also tests **True**). **PASS.**
>
> **BLOCKING: 7 item(s)** — (1) "The upper end never moves" is false of `day.py`'s own arithmetic and
> its stated reason does not entail it; (2) the lede's "Eleven / Nineteen / fourteen" carry no tier
> word; (3) the OBSERVED ledger's `edition` and `ships in that list` columns are SOURCED and the
> legend names no dates; (4) stop headings "N ships dark on that same day" contradict the hedge and
> the band; (5) "never a whole day's darkness" reads as a duration filter its own rows refute; (6) "a
> pause as long as the sentence above takes to read" mis-describes a 51-word two-sentence derivation;
> (7) the README's thirteen stale or false statements above.

---

## What the numbers became after the repairs

`gaps.mjs` re-run on the thirty-row field: **PASS — every bar stands nearer its own label at both
widths.** `data.py --check`: island matches the captures. `tools/renders.py`: renders match the page.
`tools/selftest.sh`: PASSED. The run's own line now says **"about twenty-four seconds"**, because the
premise grew by the repair of item 5 and the beat is derived from it: **14,118 ms declared, 14,223 ms
measured.**
