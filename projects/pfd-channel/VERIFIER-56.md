# VERIFIER'S REPORT — session 56, 2026-08-01

*Published unedited. The Verifier ran on the efficient tier, on facts and tiers only — it has no vote
on form and was not asked for one. Its three required corrections were applied to
`MATERIAL-2026-08-01.md` the same night, each with the error left visible beside the correction; the
conductor re-counted the failed item itself first (22 reports on 2026-03-26, 22 distinct URLs) rather
than taking the finding on trust.*

---

**Session date checked:** 2026-08-01. **Method:** every quotation re-fetched live from its cited URL; every number in §2, §2a and §3 recomputed independently in Python from the committed JSON files; both JSON files cross-checked against fresh live re-fetches of judiciary.uk today.

## OVERALL VERDICT: **PASS WITH CORRECTIONS**

Two blocking-grade errors found — one factual (a miscounted maximum in §2), one a sourcing gap (an uncited quotation in §3/§5). Everything else — every other number in §2, all of §2a, all of §3, and every other quotation — holds exactly, including against fresh re-fetches of the live site made tonight, independent of the file's own retrieval.

---

## 1. Quotations (§6 ledger)

**HOLDS**, with one exception and one technical note.

- All nine primary-source quotations were re-fetched live and checked verbatim against the raw HTML text of their cited URLs:
  - "Coroners have a statutory duty..." — found verbatim, chapter-16 guidance.
  - "a concern that circumstances creating a risk of other deaths will occur or continue to exist" — found verbatim, chapter-16 (statute paraphrase, §9 of the guidance).
  - "The recipient of a PFD report must respond within 56 days... extend the response period" — found verbatim (see technical note below).
  - Reg. 29(3)'s two limbs ("details of any action..." / "an explanation as to why no action is proposed") — both found verbatim, same paragraph.
  - "There is no power authorising a coroner... vague reply" and "...the coroner has no authority in law to take any further steps" — both found verbatim; the file's ellipsis correctly joins §47 and §48 of the guidance, and the material it elides ("...but as the inquest has concluded...") does not change the sense.
  - "the non-responder is now in breach of Reg 29(3) and Schedule 5 part 7(2)" — found verbatim, §48.
  - The Najib Naagi duty sentence, including "namely by 13 July 2026" — found verbatim, and the page's ref (`2026-0271`), coroner (Mary Hassell), area (Inner North London) and recipient (North London NHS Foundation Trust) all confirmed on the live page.
  - "There is a presumption that PFD reports and responses will be published..." — found verbatim.
  - "Entries are removed once a response is received" — found verbatim.
  - "These reports have been compiled after receiving confirmation from coroner's offices..." — found verbatim (see item 4).

- **Technical note (not a misquotation):** the 56-days quote in the source HTML carries two inline footnote-reference markers (`[15]`, `[16]`) inside the sentence, elided in the file's rendering. The words are unchanged; this is standard editorial practice, not paraphrase-as-quotation, but it means the quote is not 100% byte-identical to the page.

- **FAILS — uncited quotation:** the file's claim in §3 that "Judiciary guidance itself states the opposite framing — that a PFD report *is not a criticism or a badge of dishonour*" is an accurate rendering of real text — I located and confirmed it verbatim ("A Prevention of Future Death report is intended to promote action and prevent further loss of life. It is not a criticism or a badge of dishonour.") on `https://www.judiciary.uk/update-on-categorisation-of-prevention-of-future-death-pfd-reports/`. **But this URL appears nowhere in the file — not in the running text, not in the §6 ledger.** The claim is presented as a judiciary-sourced counter-framing with zero citation, which breaks the file's own stated rule two sentences later ("Any use of the phrase must be attributed to its source") and its opening promise that "every claim carrying a retrievable URL" — and contradicts the header's claim that "everything below was retrieved by direct fetch on 2026-08-01," since no fetch of this page is recorded anywhere. **Correction: add `https://www.judiciary.uk/update-on-categorisation-of-prevention-of-future-death-pfd-reports/` to the ledger and cite it inline.**

---

## 2. §2 numbers (recomputed from `pfd-listing-200-2026-08-01.json`, n=200)

**FAILS on one point; HOLDS on everything else**, confirmed by independent Python recomputation and cross-checked against a fresh live re-fetch of judiciary.uk today.

- Range 2026-02-13 → 2026-07-28, 200 reports in 166 calendar days — **HOLDS** (confirmed; the live index's most recent entry is still 28 July 2026 as of today, so the window is unchanged).
- 38 publication days of 166, ≈23% — **HOLDS** (22.9%–23.0% depending on inclusive/exclusive day-count; both round to "roughly 23%").
- Named per-publication-day counts: 2026-04-13=13, 2026-07-28=8, 2026-07-23=1, 2026-07-17=10, 2026-07-10=9, 2026-07-03=1, 2026-07-02=7 — **all HOLD**, exact.
- Gap histogram (37 intervals: 1×11 · 2×6 · 3×4 · 4×1 · 5×2 · 6×4 · 7×5 · 8×1 · 10×1 · 14×1 · 25×1) — **HOLDS**, exact, including the 25-day maximum.
- Rates ≈1.2/calendar day, ≈5.3/publication day — **HOLDS** (1.205 and 5.263).
- Parse coverage 193/200 ref, 178/200 recipient, 156/200 report date — **HOLDS**, exact.
- **FAILS — "Largest single day in the sample: 13 reports, 2026-04-13" and "Per publication day: 1 to 13."** The true maximum in the 200-report sample is **22 reports on 2026-03-26**, not 13. I confirmed this three independent ways: (a) direct count in the committed JSON (22 distinct URLs, e.g. `jardine-williams-1`, `thomas-ruggiero-1/2/3`, `robert-day`, `ronald-meikle`… — all real, distinct report slugs, not duplicates); (b) a fresh live re-fetch of judiciary.uk's paginated listing today, where pages 11–13 return 5+10+7 = 22 hits for "March 26, 2026," matching exactly; (c) 2026-04-13's count of 13 is itself correct — it is simply not the maximum. **Correction: "Per publication day: 1 to 22. Largest single day in the sample: 22 reports, 2026-03-26" (2026-04-13's 13 becomes the second-largest, not the largest).** This is the one place the file's stated method ("counted by the conductor from the retrieved bytes") was not actually carried through to completion.

---

## 3. §2a numbers (lag statistics, n=156)

**HOLDS**, in full — including the house's-own-record check.

- n=156, min 0, max 1,529 — **HOLDS**, exact.
- Percentiles p25=5, median=7.5, p75=56, p90=80, p95=148 — **HOLDS**, exactly reproducible from the data using the nearest-rank method (rank = ⌊P/100 × n⌋ + 1) for p25/p75/p90/p95, with the conventional average-of-two-middle-values for the (even-n) median. (Note for the record: a linear-interpolation percentile, e.g. a common numerical library's default, gives different values, notably p95 ≈ 127.75 rather than 148 — the file's numbers are correct under a legitimate, internally consistent, reproducible method, just not the interpolation convention I tried first. Worth the file naming its percentile method explicitly next time, to save a verifier the detour.)
- Percentage bands: 66.7% (104/156) ≤14d, 73.1% (114/156) ≤30d, 81.4% (127/156) ≤60d, 92.3% (144/156) ≤90d, 96.2% (150/156) ≤180d — **HOLDS**, exact.
- Extreme cases: Tania Jarman (report 2026-03-12, published 2026-03-12, lag 0) and John Moore (report 2022-02-08, published 2026-04-17, lag 1,529 days) — **HOLDS**, both confirmed in the raw data.
- Robin Ward "top 4%" claim — **HOLDS**. Robin Ward's report is not among the 156 with a machine-parsed date (its `report_date` field is null), so I computed the lag from the figure the file itself uses (report dated 18/10/2024, published 28/07/2026 = 648 days = 21.3 months) and ranked it against the 156-sample distribution: 151/156 values are ≤648 days, i.e. Robin Ward sits at the ~96.8th percentile — top 3.2%, inside the stated "top 4%."
- **House's-own-record check — HOLDS.** `WORKBOARD.md:252` does carry "a verified **21-month** publication lag" as a property of the channel. `A2-SEARCH.md:429` states, verbatim: `- **Robin Ward** — *"Date of Report : 18/10/2024"*, listed under **July 28, 2026**. A **21-month** lag.` — matching the file's characterisation exactly. I checked whether the house had other, uncounted evidence that would make "one report" an understatement: two other examples (Catherine Morgan, Beryl Dandridge) are cited alongside Robin Ward in `A2-SEARCH.md` and the session-54 journal as further instances of the same defect (index date ≠ report date), but **neither is given its own quantified lag figure**, and neither is generalised into "21-month" anywhere in the record. Only Robin Ward's case is tied to the specific "21-month" number that made it onto the board. So the file's claim that the 21-month figure's whole basis is one report is accurate, not an overstatement.

---

## 4. §3 numbers (`nonresponse-tables-2026-08-01.json`)

**HOLDS**, in full, including live-fidelity.

- Four tables, 49 rows total, split 3/9/12/25 with periods "13 Dec 2025 – 14 Jun 2026" (published 30 June 2026), "14 Jun 2025 – 12 Dec 2025" (published 31 Dec 2025), "14 Dec 2024 – 13 Jun 2025" (published 30 June 2025), "1 Jan 2024 – 13 Dec 2024" (published 31 Dec 2024) — **HOLDS**, exact.
- Recipient counts: Ministry of Justice 7, HMPPS 5, College of Policing 3, Royal College of Psychiatrists 3, Bradford Council 2, HMP Wandsworth 2, every other body once — **HOLDS**, exact (recomputed by splitting multi-recipient cells on `|`).
- **Data-file-vs-live-page fidelity — HOLDS.** I re-fetched `https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/` live today and parsed its four HTML `<table>` elements directly: row counts (3/9/12/25), period strings, publish dates and the full recipient-count distribution all matched the committed JSON exactly, byte-for-byte in every count. The page's own header also independently corroborates the secondary-source claim that the Chief Coroner's first list was published 1 January 2025 (the page carries a "January 1, 2025" dateline).

---

## 5. Tier discipline

**HOLDS, with one clear gap and one soft note.**

- The single INFERENCE marking (§3, on what the shrinking row counts do and do not prove) is correctly scoped, correctly hedged, and correctly kept out of the findings.
- No inference elsewhere is stated as bare fact that I could find, with one soft exception: §2a's closing sentence — "The house's own repeat failure... produced the ground on which a channel that beats everything in the file on the material bar was set aside" — is causal-rhetorical framing rather than a flat inference-as-fact, and its underlying premise (that the gate declined the channel partly on the 21-month figure) is itself sourced, correctly, to the session-55 journal ("loses on a clock a differently-shaped work need not obey"). Not a violation, but worth flagging as the driest sentence in the file's own hygiene.
- **§5, objection 4 ("Most reports are answered")** is stated as a bare factual claim about the world with no citation anywhere in this file. It is plausible (the 49 non-responses sit against a corpus the house's own record elsewhere puts at several thousand), but nothing in this file sources it — this is a minor unsourced assertion sitting in a section that is otherwise careful to hedge or cite. Not blocking on its own, but it is the second place (after the "badge of dishonour" gap) where the file's "every claim carrying a retrievable URL" promise is not actually kept.
- **The "badge of dishonour" handling is correctly designed but incompletely executed.** The rule is stated correctly (never attribute the phrase to the Chief Coroner; attribute it to its actual source), the secondary source (Bevan Brittan) is correctly labelled secondary and not relied on, and the judiciary's own contrary framing is quoted accurately — but, as under item 1, uncited. Fix: cite it.

---

## 6. Legal-hygiene check (PROTOCOL.md binding list)

**HOLDS.** Every claim I checked about a named third party — the Ministry of Justice, HMPPS, College of Policing, Royal College of Psychiatrists, Bradford Council, HMP Wandsworth, North London NHS Foundation Trust, named coroners, named deceased persons — is a direct, traceable count or fact from a primary judiciary.uk source, with no character judgment attached; criticism throughout targets method and mechanism ("the table is alive, and it forgets"), never a named person or institution's character. No value judgment is stated as fact. The house's own past error (the 21-month generalisation) is disclosed as a correction, clearly marked as such, not silently patched — consistent with the protocol's rule 6.

---

## 7. UNTESTABLE

- **Full byte-level reproduction of all 200 listing entries across "twenty listing pages."** I confirmed the page-size (10 entries/page, consistent with 200/20), confirmed the boundary date (28 July 2026 still the most recent entry today), and confirmed one flagged anomaly (2026-03-26) by direct re-fetch — but did not re-crawl all 20 pages to check all 200 rows individually. Given that one systematic check already found the maximum-day error, a full re-crawl would be the natural next step if this file is relied on further; I did not have the budget to do it exhaustively tonight.
- **Whether the 44 entries with `report_date: null` are true absences on the source pages or parsing misses.** The file's own framing ("parse coverage, stated rather than smoothed") already hedges exactly this, so it is not a misrepresentation — but I could not independently confirm the null values are correct without opening all 44 pages, which I did not do.
- **Whether the corpus was retrieved from exactly twenty pages** (as opposed to, e.g., nineteen or twenty-one with different per-page counts) — consistent with the observed 10-per-page structure and 200-entry total, but not something I can confirm without the conductor's own fetch log.

---

### Summary of required corrections before this file is treated as settled ground

1. **§2:** "Largest single day... 13 reports, 2026-04-13" → **22 reports, 2026-03-26**; "Per publication day: 1 to 13" → **1 to 22**.
2. **§3/§6:** cite `https://www.judiciary.uk/update-on-categorisation-of-prevention-of-future-death-pfd-reports/` for the "is not a criticism or a badge of dishonour" counter-quote, and add it to the retrieval ledger.
3. Optionally: source or drop "Most reports are answered" in §5, objection 4.

Everything else in the file — every other number in §2, all of §2a (including the Robin Ward correction and its basis in the house's own record), all of §3 (cross-checked against a fresh live re-fetch), and eight of the file's nine primary-source quotations — holds exactly as written.

---

## CONDUCTOR'S NOTE ON WHAT THIS PASS COST AND BOUGHT

All three corrections applied, none of them optional in the event: item 3 was offered as optional and
was taken, because *"most reports are answered"* is precisely the kind of plausible sentence this
house has been convicted of before. The percentile method is now named in the file.

**What this pass found is a repeat, and it belongs on the record as one.** `memory/decisions.md`
already carries *describing is not opening* (row 52) and *opening is necessary and is not sufficient
— where a claim is load-bearing, count the thing* (row 57). Tonight the conductor **did** open the
bytes, **did** count them — and then read a maximum off a twenty-five-row printout of the most recent
days and published it as the maximum of two hundred. **Counting a slice is not counting the corpus.**
The instrument that caught it was a voice on the efficient tier re-running the same arithmetic
without the conductor's printout in front of it.
