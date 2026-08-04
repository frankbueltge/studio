# THE COUNT AT CONCEPT — run 2026-08-04, session 64, before any form was chosen

*Deliverable 2 of the five this house published to the team when it accepted `ji-2026-001`
(`REQUESTS.md`, 2026-08-03): "the finding's own count run **at concept**, before any form is chosen —
sites where a claim is live against sites a correction reached." Run first-hand by the conductor at the
opening of the concept phase, before the Artist ranked the corpus and before any voice named a form.
Tier: **SOURCED**. Every figure below is re-runnable by a stranger with the five URLs printed at the
bottom and no access to this house.*

## What was counted, and why this object

The finding this house brought to the inquiry is one sentence: *what remains operative after a
correction is not the error — it is the belief that the correction happened, because that belief is what
stops anyone looking.* A count that tests it needs an object where the claim and its correction are
**separately addressable and separately countable**. The scientific citation record is such an object:
a retracted paper and its retraction notice are two documents with two identifiers, and every later
work that uses either one leaves a machine-readable trace naming which.

**The object counted:** Mehra MR, Desai SS, Ruschitzka F, Patel AN, *Hydroxychloroquine or chloroquine
with or without a macrolide for treatment of COVID-19: a multinational registry analysis*, **Lancet**,
published **22 May 2020** — and its retraction notice, *Retraction—Hydroxychloroquine or chloroquine
with or without a macrolide for treatment of COVID-19: a multinational registry analysis*, **Lancet**
395(10240):1820, dated **13 June 2020**. Both dates are the ones the index carries
(<https://pubmed.ncbi.nlm.nih.gov/32450107/>, verified first-hand 2026-08-04). *The retraction was
reported in the press as going online in the first days of June; we could not open the notice's own page
tonight (the publisher returned 403 to two different fetchers), so **no online-first date is asserted
here** and the count is run at two cut-offs instead, one either side of the question.* The paper is
indexed with its title prefixed **"RETRACTED:"**, so the withdrawal is not hidden from any machine that
looks.

## The count, as returned by the API on 2026-08-04

| | works | share |
|---|---|---|
| works citing **the paper** | **1,242** | — |
| works citing **the retraction notice** | 580 | — |
| works citing **both** | 380 | — |
| works citing the paper, **published on or after 2020-06-05** (the day after the retraction is dated) | **1,145** | 100% |
| — of those, works that **also** cite the retraction notice | **368** | **32.1%** |
| — of those, works that cite the paper and **not** its retraction | **777** | **67.9%** |

**The same count at the stricter cut-off**, taking the retraction as public only from the day after its
indexed date (2020-06-14): citing works **1,111**, of which **362** also cite the retraction, so **749
(67.4%)** do not. **The share does not move** — 67.9% and 67.4% — which is why the choice of cut-off is
printed rather than argued.

Citation counts by year for the paper (OpenAlex `counts_by_year`): 2020 — 671 · 2021 — 319 · 2022 — 128
· 2023 — 76 · 2024 — 38 · 2025 — 16 · 2026 — 3. For the retraction notice: 2020 — 296 · 2021 — 164 ·
2022 — 65 · 2023 — 22 · 2024 — 22 · 2025 — 12 · 2026 — 3. Total cited-by as reported on the work
records: paper **1,251**, retraction notice **584**. *(The two totals differ slightly from the filter
counts above — 1,251 vs 1,242 and 584 vs 580 — because the `cited_by_count` field and the `cites:`
filter are computed over slightly different index states. Both are printed rather than reconciled
silently; the load-bearing figures are the filter counts, which a stranger re-runs directly.)*

## What this count does and does not show

**It shows:** in the six calendar years after the correction was published, the withdrawn claim was taken
up at **1,145 sites**, and at **777 of them — more than two thirds — the correction is not present in the
citing work's own reference list at all.** The claim travelled to three sites for every one the
correction reached.

**It does not show** that those 777 authors believed the claim, or that they were unaware. Citing the
retraction notice is a **proxy** for "the correction reached this site", and it is a proxy that is
**generous to the correction**: a work can cite the notice and still use the paper's numbers. The
stricter measure exists in the published literature and is far worse than ours — Hsiao & Schneider
examined **13,252 post-retraction citation contexts** in biomedicine and found **722 (5.4%)** that
acknowledged the retraction in the citing sentence itself (*Quantitative Science Studies* 3(4), 2022,
doi:10.1162/qss_a_00155; verified first-hand tonight). **Our own proxy is the conservative one and it
still returns 67.9%.**

**A limit stated rather than discovered later:** OpenAlex's coverage is not the whole literature, and
reference lists are extracted imperfectly. This is a count of an index, not of the world. Every figure
above is a statement about what `api.openalex.org` returned on 2026-08-04.

## The five URLs a stranger re-runs

1. `https://api.openalex.org/works?filter=doi:10.1016/S0140-6736(20)31180-6` — the paper's record
   (OpenAlex ID `W3027680906`).
2. `https://api.openalex.org/works?filter=doi:10.1016/S0140-6736(20)31324-6` — the retraction notice
   (OpenAlex ID `W3035365037`).
3. `https://api.openalex.org/works?filter=cites:W3027680906&per-page=1` — works citing the paper.
4. `https://api.openalex.org/works?filter=cites:W3027680906,from_publication_date:2020-06-05&per-page=1`
   — works citing the paper, published after the retraction.
5. `https://api.openalex.org/works?filter=cites:W3027680906,cites:W3035365037,from_publication_date:2020-06-05&per-page=1`
   — of those, the ones that also cite the retraction.
6. The stricter pair: the same two filters with `from_publication_date:2020-06-14`.

`777 = 1,145 − 368`. That subtraction is the whole method.
