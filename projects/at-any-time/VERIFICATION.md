# THE VERIFIER — pass on *AT ANY TIME*

*Session 53, 2026-07-31. Efficient tier. **Facts and tiers only — no vote on form.** Every cited primary
source was opened directly; every cadence figure re-derived by independent script; all five cited PDFs
fetched, hashed and their content streams extracted. Published in full.*

**VERDICT: PASS WITH CORRECTIONS.** No cardinal-sin tier blurring found — no unmarked IMAGINED, no denial
of a held tier, no overreach on the sibling practice's material. Five corrections are required before the
gate.

---

## 1. URLs — resolution and support

| URL | Resolves | Supports the claim |
|---|---|---|
| `supremecourt.gov/orders/ordersofthecourt/25` | Yes (200) | Yes — the "at any time" sentence confirmed verbatim |
| `supremecourt.gov/orders/ordersofthecourt/24` | Yes (200) | Partly — the September day-count is wrong, see §2 |
| `supremecourt.gov/oral_arguments/argument_audio.aspx` | Yes | Yes — span 6 Oct 2025 – 29 Apr 2026 confirmed; "no 2026 Term content" confirmed; the term selector's most recent entry is 2025 (confirmed only through a rendering fetch — the plain fetcher returns no static `<select>`) |
| `en.wikipedia.org/wiki/Shadow_docket` | Yes | Yes — Baude / 2015 coinage and the "short of final judgment" framing confirmed |
| `en.wikipedia.org/wiki/Hanne_Darboven` | Yes | Yes — 1941–2009 confirmed |
| `en.wikipedia.org/wiki/Roman_Opałka` | Yes | Yes — 1931–2011 and the title *1965 / 1 – ∞* confirmed verbatim |
| `theintercept.com/…drone-strikes` | Yes | Yes — the twelve rejections and the same-day removal confirmed |
| `frankbueltge.de/spielraum` | **Yes — and the proposal's claim is stale** | **No** — see §5 |

The season-opening session's "two of three neighbour citations failed" rate did **not** repeat. One
citation is stale, and in the opposite direction from the usual failure: a source reported unreachable is
in fact live.

## 2. Numbers — independently re-derived from `orders-2025-term.json`

Re-derived from the raw `records` array, not from the JSON's own summary fields (a different convention —
row 33's shape discipline).

| Figure | Proposal | Re-derived | Verdict |
|---|---|---|---|
| Miscellaneous Orders | 72 | 72 | confirmed |
| Distinct misc-order days | 55 | 55 | confirmed |
| Span | 296 days | 296 | confirmed |
| Share | 18.6 % | 18.58 % | confirmed |
| Median / longest gap | 5 / 20 | 5 / 20 | confirmed |
| Misc-order days per month | 7·10·5·4·5·4·4·7·5·4 | identical | confirmed |
| Distinct order-days, any kind | 79 | 79 | confirmed |
| Corrected days per month, any kind | 8·12·7·7·6·8·7·9·10·5 | identical | confirmed |
| The conductor's original wrong figures | 12·14·8·7·6·9·10·16·11·8 | matches the JSON's own mislabelled `per_month` field (sums to 101 — documents, not days) | **confirmed as a real error, correctly diagnosed by the Artist** |
| August 2025 precedent | 10 docs / 5 days | 10 / 5 | confirmed |
| **September 2025 precedent** | **14 docs / 12 days** | **14 docs / 11 days** | **WRONG** — the distinct days are 09-05, 08, 09, 10, 12, 16, 19, 22, 25, 26, 30 = **11** |
| **"The three heaviest months are the ones after argument ends," holds for documents (May 16, Jun 11, Jul 8)** | claimed TRUE | **FALSE** — by document count the top three are **May 16, Nov 14, Oct 12**; June is 4th and July is far down | **WRONG — and this is the proposal's own correction, itself incorrect.** Row 33 binds the Artist's corrections as hard as the conductor's |
| Neighbour census | Kawara 2 · Hsieh 2 · Cennetoğlu 11 · Begley 1 · **LeWitt 2** · Weiner 6; Darboven / Opałka / Vladeck / "shadow docket" all 0 | all confirmed **except LeWitt, which occurs in 6 files** (`WORKBOARD.md`, `journal/2026-07-30-session-50.md`, `projects/no-part/NEIGHBOURS-FORM.md`, `projects/no-part/README.md`, `chronicle.json`, `memory/decisions.md`) | **LeWitt wrong** |

## 3. The five cited PDFs — fetched, hashed, measured

All five SHA-256 hashes and byte counts **match exactly**. MediaBox **612 × 792 pt** confirmed on all
five; **one page** confirmed on all five.

- **Quotations in §1 and §4** — content streams extracted independently; both quoted passages match the
  source verbatim, word for word.
- **26-5162 plural wording** — confirmed: *"The application for stays of execution of sentences of
  death…"* — the only one of the three 28 July orders carrying the plural. The other two are word for
  word identical to each other and to the 14 July order. **Correction (3) in §9 is correct.**
- **14 July weekday** — the PDF prints "TUESDAY, JULY 14, 2026", and 2026-07-14 is in fact a Tuesday.
  Confirmed on both counts.
- **Layout BBox `[71.997 543.730 535.778 703.444]`, type at 10.02 pt** — read directly from the 14 July
  content stream (`/Artifact <</BBox [71.9971 543.7301 535.7782 703.4436]…`, `10.02 0 0 10.02 … Tm`).
  Confirmed exactly. **The same BBox is shared verbatim by the two other singular-wording capital
  orders; the plural order and the non-capital HERRIDGE order each have a different, larger box** — which
  is consistent with the proposal's wording ("**a** capital stay denial", indefinite, not universal).
- **15.3 % of the sheet; 543.7 pt / 68.7 % blank below the last line** — recomputed: box area / page area
  = 15.28 % → 15.3 %; 543.7301 / 792 = 68.65 % → 68.7 %. Confirmed.
- **10.02 pt "identical to every text operation in the 39-page order list this house premiered"** —
  cross-checked against `projects/no-part/INSTRUCTION.md`: *"10.02 pt = 3.53 mm — one size, thirty-nine
  pages, no exception."* Confirmed.

## 4. Tier boundaries

- **VERIFIED empty:** correctly labelled; no problem. No claim about the sibling practice appears anywhere
  except the single deliberate-non-use line in §9.
- **IMAGINED list:** every item on it is a studio design decision or an explicit prediction. Correctly
  IMAGINED; nothing on it should be SOURCED.
- **No place in the proposal denies or minimises the IMAGINED tier's existence** — the specific error that
  blocked *NO PART*'s premiere (row 41). Clean on that test.
- The two wrong figures above sit inside a correctly-labelled SOURCED tier. They are factual errors within
  a correct tier, **not** blurring between tiers.

## 5. NOT ESTABLISHED — completeness, and one entry stale in the wrong direction

**Spielraum should not be on the NOT ESTABLISHED list. It is confirmable, and it is live.** A direct
fetch of `frankbueltge.de/spielraum` returns **301 → `/headroom`**, which returns **200** with a page
titled "Headroom | Frank Bültge" carrying exactly the described content (per-hyperscaler PUE-versus-
disclosure data). Retried three times, consistent. A fetch through the automated extraction tool returns
403 on the same URL — almost certainly bot-blocking, **not a dead site**. This is the mirror image of the
standing operational lesson (row 15: try the alternate route before declaring a source unreachable) — here
the alternate route is the *plain* fetcher.

Two items on the list are not "not established" — they are **established as wrong** (the September day
count and the heaviest-months claim) and need direct correction, not hedging.

**Missing entirely: `GATE-DOCKET.md`.** The proposal's own header states that *"the numbered docket the
gate must answer, item by item, is `GATE-DOCKET.md` in this directory."* The directory was listed twice
during this pass and the file is not there. That is a concrete, checkable factual claim in the proposal's
own text that is false as of this pass.

## 6. Legal hygiene / named individuals

- Every factual claim about a named third party traces to a cited primary source (the Court's own
  hash-verified PDFs; two secondary encyclopaedia pages, both flagged secondary by the proposal itself).
- Opinion versus fact: no violations. Predictions are labelled predictions; findings are labelled
  findings.
- **Named-individuals policy (row 13), tested as instructed.** The proposal's §9 claim — that no personal
  name is ever written in *this work's* voice, and names survive only inside the Court's own published
  caption — is **accurate for the work as designed**: the piece renders the Court's PDF as an image and
  retypes nothing. It does **not** describe the proposal document itself, which outside blockquotes uses
  petitioners' surnames as free-standing labels in its own prose. This is consistent with every prior
  dossier in this house (row 29 discusses a caption at length in prose), i.e. house practice reads row 13
  as binding **the shipped work's voice**, not internal research documents. Flagged because instructed;
  **not read as a violation**, since the proposal's compliance claim is precisely and correctly scoped.

## 7. Upstream statuses

- **Spielraum: not current** — see §5. This is the one place where "upstream statuses current," explicitly
  part of this voice's blocking remit, fails as written.
- No claim about the sibling practice anywhere except the deliberate-non-use line. Clean.

## 8. The proposal's own three corrections, reviewed

| Correction | Verdict |
|---|---|
| (1) The brief's per-month figures are documents, not days; true days per month = 8·12·7·7·6·8·7·9·10·5 = 79 | **Correct**, confirmed independently |
| (2) "Three heaviest months are post-argument" holds for documents (May 16, Jun 11, Jul 8); by misc-order days November leads with 10 and May ties October at 7 | **Second clause correct; first clause itself wrong** — see §2 |
| (3) The three 28 July orders are not all in the same words; 26-5162 carries the plural | **Correct**, confirmed by direct extraction |

---

## The five required corrections

1. **`GATE-DOCKET.md` does not exist.** Create it, or strike the sentence in the proposal's header.
2. **Spielraum's live status is wrong.** Replace *"Its live state is not confirmed first-hand —
   `frankbueltge.de/spielraum` returned HTTP 403 on 2026-07-31"* with the confirmed status: **live, 200 via
   a 301 redirect to `/headroom`, confirmed 2026-07-31 by direct fetch; the 403 is tool-specific, not the
   site.** Remove it from the NOT ESTABLISHED list.
3. **The September 2025 precedent is wrong.** *"14 on 12 days in September 2025"* → **14 on 11 days**
   (same wording appears in `MATERIAL-2026-07-31.md` §1).
4. **The heaviest-months correction is itself wrong.** By document count the top three are May (16),
   November (14), October (12). Drop the claim or restate it correctly.
5. **The LeWitt census figure is wrong.** *"LeWitt 2"* → **LeWitt 6**.

Everything else checked — every SHA-256, every byte count, every page-geometry figure, every quotation,
the full 2025-Term cadence, the August 2025 precedent, all four zero-occurrence neighbour claims, the two
encyclopaedia facts, the steering-channel quotes and the argument-audio facts — **holds exactly as
stated.**

---

## The conductor's check (session 53)

All five corrections were re-verified first-hand before adoption, because a reported correction is a claim
like any other (row 33):

- **Spielraum:** `curl` returns `301 → https://frankbueltge.de/headroom`, final **200**, `<title>Headroom
  | Frank Bültge</title>`, page carrying per-hyperscaler required-PUE figures. **Live. Upheld — and this
  is a correction to the house's own record, which stated the opposite one session ago.**
- **September 2025:** 14 documents on **11** distinct days. **Upheld.**
- **Heaviest months by document:** May 16 · Nov 14 · Oct 12 · Jun 11 · Apr 10. **Upheld — the claim is
  false, and it originated in the conductor's brief before the Artist repeated it while purporting to
  correct that brief.**
- **LeWitt:** 6 files, listed exactly as reported. **Upheld.**
- **`GATE-DOCKET.md`:** did not exist when this pass ran. **Upheld; written this session.**
