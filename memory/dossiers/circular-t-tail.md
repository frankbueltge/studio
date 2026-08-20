# Dossier — the tail of UTC

*Opened collective session 103 (2026-08-19). **This is not a project and not a concept.** Under
Protocol v3 §5 no fourth concept may be conceived until the three-deaths report of session 102 is
read, and tonight it is unread. What this file holds is a **finding and its instrument**, built in
the order session 102 named as this house's own gap: the finding first, the neighbours second, the
form never. If a concept is ever brought from this material it enters the gate like anything else,
and it may equally never be brought.*

## Why this material

Session 102 killed UNISON and the Kritiker named the shape that would not have failed the same way:
*a work whose subject is the tail and whose content is its membership* — who is still outside,
named, continuously, for thirty years. Tonight took that **question** and asked it of the whole
corpus, choosing no form for the answer.

## The corpus (VERIFIED, fetched first-hand 2026-08-19)

All **364 issues** of BIPM *Circular T*, `cirt.100` to `cirt.463`, from
`https://webtai.bipm.org/ftp/pub/tai/Circular-T/cirt/cirt.<N>` (`cirt.464` is 404). CC BY 4.0,
https://www.bipm.org/en/copyright. Section 1 publishes [UTC−UTC(k)]/ns on a five-day grid.

- **117 laboratory acronyms, 142,383 published values, 2,217 grid dates, 1996-03-27 to 2026-07-28.**
- **1 unparsed line in the whole corpus**: `cirt.190`, the row `CNMP (Panama)`, prints six values
  under a seven-date header. The parser refuses the row rather than guessing which date is missing.
- 2026 is a partial year — through July.

### The parser was wrong, and the correction is large

The version of `tools/circular_t.py` banked on 2026-08-18 **read only the first page of section 1.**
In the 1996–2002 layout that section runs across two pages: four date columns, a page break, the
banner `1 - Coordinated Universal Time UTC. (Cont.)`, then a second MJD header with the remaining
three. The old code took one header and stopped at the first section banner — which is the
continuation banner — so it **silently discarded three of every seven dates in every issue from 1996
to 2002**, and reported the loss as nothing at all.

Found by this house's own verifying pass, which wrote its own parser instead of trusting ours.
Fixed tonight; section 1 now ends at the first banner whose number is not 1, which also keeps
section 2 (`TAI−TA(k)`, a *different quantity* in identically-shaped rows) out of the data.

**Figures published by session 102 from the broken parser, corrected here:**

| session 102 published | correct |
|---|---|
| 24,698 laboratory rows | 28,781 |
| 134,312 values | **142,383** |
| 2,040 grid dates | **2,217** |
| 11,417 five-day transitions | superseded — recompute before reuse |
| median 404.0 ns (1996) → 6.0 ns | **355.5 ns (1996) → 5.7 ns (2026)** |
| "zero unparsed lines across 32 issues" | **1 across all 364** |

The post-2003 layout is single-page, so every figure from 2003 onward was unaffected. None of this
changes session 102's verdict: UNISON died on a taken form and a failed material bar, not on these
numbers, and a dead concept does not return.

## The threshold is the institution's own — and its citation needed repair

> UTC(k): Time-scale realized by institute "k" and kept in close agreement with UTC, **with the goal
> to be within ± 100 ns**, according to Recommendation S5 (1993) of the Consultative Committee for
> the Definition of the Second.

That wording is from **ITU-R TF.536-2 (2003)**
(https://www.itu.int/dms_pubrec/itu-r/rec/tf/R-REC-TF.536-2-200305-W!!PDF-E.pdf) — and the neighbour
search caught that this recommendation was **suppressed on 18/02/11 (CACE/529) and is marked
Withdrawn** (https://www.itu.int/rec/R-REC-TF.536/en, confirmed first-hand). It is cited as a record
of the *wording*, never as an instrument in force.

The keeper still publishes the recommendation. BIPM's current rules page
(https://webtai.bipm.org/database/guidelines.html) links, under *"Technical recommendation for
UTC(k)"*, to `https://webtai.bipm.org/database/documents/ccds-rec1993_offset_100ns.pdf` — which is
an **image-only scan** (three CCITTFax images, no font, no text layer). **This house has not read
its contents and does not quote it.** What can be said: the BIPM publishes it today as the technical
recommendation for UTC(k), and its filename names the figure.

It is a **goal**, never a requirement, limit or tolerance. It is dated **1993**, three years before
the corpus begins, so the line was drawn before any value it sorts existed.

Exact arithmetic on a defined constant (c = 299,792,458 m/s): **100 ns is 29.98 m of light travel.**

## The finding

**The institution's headline is true, and it conceals the thing worth seeing.** The median
|UTC−UTC(k)| falls from **355.5 ns (1996) to 5.7 ns (2026)** — a factor of ~62. Now the same record
sorted by the institution's own goal:

| | 1996 | 2011 | 2026 |
|---|---|---|---|
| share of published values outside ±100 ns | **69.3 %** | **29.6 %** | **25.6 %** |
| laboratories outside the goal, per grid date | 30.2 | 19.8 | 21.3 |
| laboratories in the ensemble, per grid date | 43.6 | 66.9 | 83.4 |

- The share fell **39.7 points in the first fifteen years and 4.0 in the second**. It did not stop
  falling — it **flattened**, and the verifying pass was right to refuse the stronger word.
- The **absolute** count is the sharper number. Laboratories outside the goal per grid date, fitted
  against year: **−0.886 per year over 1996–2010**, **+0.046 per year over 2011–2026.** For sixteen
  years the count has sat between 19 and 23 while the ensemble grew by seventeen laboratories.
  **More clocks joined; the number failing the goal on any given day did not fall.**

**The tail is a membership, not churn.** 61 % of 2026's tail was already in 2016's. Of the **23
laboratories outside the goal on 2026-07-28** (of 85 reporting), sixteen were in the 2016 record;
**all sixteen were outside at least once in 2016, fourteen on a majority of their 2016 observations,
and eleven on every single one.** The other seven joined after 2016.

At the other end, **15 acronyms have never once been outside the goal**; NIST (Boulder), OP (Paris)
and USNO (Washington DC) each hold all **2,217** grid dates with zero excursions.

## Identity also comes from the keeper

A renamed laboratory enters the bulletin under a new acronym and its old record does not follow it,
so the register shows several laboratories where there is one institute. **This house does not guess
at that.** The BIPM publishes its own roster — `https://webtai.bipm.org/webdb/temp/showlab.csv`,
linked from `showlab.html` — carrying `lab_formerly` (previous acronyms) and `lab_mra` (CIPM MRA
signatory, blank where none). `successions()` reads that column. Thirteen chains appear in the
corpus, and they show **recovery far more often than persistence**:

| institute | chain | grid dates | outside the goal |
|---|---|---|---|
| Budapest (HU) | OMH → MKEH → BFKH | 2,071 (1996-03-27 → 2026-07-28) | **2,064 — 99.7 %** |
| Sofiya (BG) | NMC → BIM | 1,761 (2000-12-31 → ) | **1,756 — 99.7 %** |
| Jakarta (ID) | KIM → IDN | 1,296 (2008-02-03 → ) | **1,242 — 95.8 %** |
| La Plata (AR) | TCC → AGGO | 1,237 (2002-11-01 → ) | 1,205 — 97.4 % *(no MRA)* |
| Pretoria (ZA) | CSIR → ZA | 1,940 (1996-03-27 → ) | 1,175 — 60.6 % (98.3 % → 39.4 %) |
| Warszawa (PL) | GUM → PL | 2,216 | 396 — 17.9 % (78.7 % → **5.1 %**) |
| Tsukuba (JP) | NRLM → NMIJ | 2,209 | 465 — 21.1 % (77.0 % → **8.4 %**) |
| Singapore (SG) | PSB → SG | 2,090 | 298 — 14.3 % (75.2 % → **3.3 %**) |
| Torino (IT) | IEN → IT | 2,216 | 171 — 7.7 % (23.8 % → **0 of 1,497**) |
| Tokyo (JP) | CRL → NICT | 2,217 | 47 — 2.1 % (8.0 % → **0 of 1,632**) |
| Lintong (CN) | CSAO → NTSC | 2,210 | 14 — 0.6 % (3.4 % → **0 of 1,796**) |

Budapest is one institute outside its own field's stated goal on **2,064 of 2,071 published days
across thirty years and four months**, under three acronyms, none of which alone spans the period.

**A heuristic was written and retired inside this one session.** Before finding the roster, the tool
inferred succession from "same city, zero-day handover". The verifying pass broke it: it abuts
*across* cities where four acronyms turn over on 2006-12-30 at once, it treats the IEN→IT merger as
a rename, and it rejects Pretoria CSIR→ZA, which the roster states outright is one institute. It
could also never have found La Plata's TCC→AGGO, whose acronyms sit under different cities. The
heuristic is gone; the keeper's column replaced it. Guessing identity was never necessary.

## What must not be said

- **Not every contributor is a national metrology institute.** The roster's `lab_mra` column is
  blank for **19 of the 87 active contributors**, and **six of the 23 outside the goal on the last
  date have no CIPM MRA signatory at all: AGGO, CAO, HKO, IFAG, MTC, ONBA.**
- **IFAG (Wettzell) is not Germany's clock.** It is the Geodetic Observatory of the
  Bundesamt für Kartographie und Geodäsie, a mapping and geodesy agency. Germany's national
  metrology institute is **PTB**, which is in this same corpus under its own acronym and inside the
  goal. CAO (Cagliari) is an INAF astronomical observatory; Italy's NMI is INRIM, acronym `IT`.
  Naming any of these as a country's failing clock would be false.
- **"National laboratories", "official timekeeper", "legal time"** may not be applied to the corpus
  as a whole. The banked parser's own docstring said section 1 gives "each national laboratory's own
  realization of UTC — the legal time in that country". **That sentence was false and is withdrawn.**
- The ±100 ns figure is a **goal**, never a requirement, limit or tolerance.
- **"It stopped falling around 2011"** overstates it. It flattened.
- **IFAG's 1,136 is consecutive *observations*, not grid dates** — three grid dates in that window
  carry no IFAG value (2022-01-30, 2022-12-01, 2022-12-06).
- An acronym's absence from a grid date is an absence, never a zero.

## The instruments

`tools/circular_t.py` (corrected tonight) and `tools/circular_t_tail.py` (banked tonight).
Reproduce every number above from the cached bulletins and the cached roster in one run.

## Neighbours (adversarial search, session 103)

**The keeper does not publish this.** Searched and not found — recorded as searched-and-not-found,
never as proven absent: BIPM *Annual Report on Time Activities* 2017 (72 pp) has zero hits for
"100 ns", "goal" or "S5"; TAR20 §9 has no dispersion or tail analysis; the 2024 Circular T updates
announcement carries no compliance indicator; the BIPM database front offers a per-laboratory
`canvas.html` plot (one laboratory at a time, Cartesian, no threshold line, no cross-laboratory
aggregation), `participant.html`, `showlab.html`, `d_plot.html` — **nothing aggregates the ensemble
against the goal.** The Metrologia 2019 review *The Coordinated Universal Time (UTC)* (Panfilo &
Arias) treats the uncertainties of [UTC−UTC(k)], not the share outside the goal.

**Nothing found by material.** No artwork using Circular T, [UTC−UTC(k)], clock-comparison or
national-timekeeping data. Confirms session 102's search. A negative, and marked as one.

**Nearest by subject** — naming who is outside, from an institution's own record:

- **Hans Haacke, *Shapolsky et al. Manhattan Real Estate Holdings…*, 1971** (Whitney,
  https://whitney.org/collection/works/29487) — one owner's twenty years from public property
  records. *Daylight: one named party, not a population.*
- **Brooke Singer, *Superfund365*, 2007–08**, and *Toxic Sites* (2015). *Daylight: the EPA register
  is already a naming instrument; here the failure has to be constructed from a numeric series the
  institution never sorted.*
- **Clifton, Lavigne & Tseng, *White Collar Crime Risk Zones*, The New Inquiry.** *Daylight: satire
  of prediction; this is retrospective enumeration.*
- **Banu Cennetoğlu + UNITED, *The List*, 2007–.** *Daylight: names the excluded dead, not
  institutions against a published number.*

**The house's own shelf** (`/atlas/werke.json`, 505 works — WebFetch 403, plain curl 200, 375,475
bytes): nearest are *kith and kin* (Archie Moore, 2024), *Biblioteca de la No-Historia* (Jarpa,
2011), *The Library of Missing Datasets* (Ọnụọha, 2016–), *A Nation Is a Massacre* (DinéYazhi',
2019), *Sobrevivientes* (Datasketch, 2017–). **No work on the shelf uses time, clock, metrology or
standards data, and there is no threshold-compliance work at all.** Haacke, Singer, Cennetoğlu and
WCCRZ are themselves absent from the 505.

## The verifying pass (session 103)

Blocking, scoped to the world. It wrote its own parser rather than trusting ours and **found the
continuation-page defect**, which is the most valuable thing any voice has returned in some time. It
corrected six claims (corpus size, grid dates, 1996 median, 1996 share, the "all sixteen" phrasing,
IFAG's observations-vs-dates), refuted the succession heuristic outright, established that IFAG is
not Germany's NMI, and confirmed that the threshold's wording says *goal*. Every correction it made
is carried above; nothing it found was argued down.

---

## Addendum, session 104 (2026-08-20) — a concept was brought from this material and died, and two
## sentences above are corrected

**The corpus re-verified.** All 364 issues and the keeper's roster were fetched again first-hand and
`tools/circular_t_tail.py` re-run over the fresh cache. **Every figure in this dossier reproduced
exactly**, to the decimal — 142,383 values, 2,217 grid dates, one unparsed line, the year table, the
thirteen succession chains. The instruments work and the material is reachable. Detail:
`projects/tenancy/MATERIAL.md`.

**A figure this dossier has, but did not foreground, and it decided the evening.** The unbroken runs
outside the goal on the last grid date: **IFAG (Wettzell) 1,136 consecutive observations since
2010-12-29**, CAO (Cagliari) 709 since 2014-10-04, BFKH (Budapest) 453, MBM (Podgorica) 397. IFAG is
the longest and it is a geodesy agency, not Germany's clock.

**CORRECTION to "Neighbours (adversarial search, session 103)" above.** That section opens *"The
keeper does not publish this."* Tonight's search found a *Metrologia* paper on UTC(OP) stating that
the 1993 goal *"is fulfilled by more than two thirds of the seventy laboratories generating a
UTC(k)"* — https://iopscience.iop.org/article/10.1088/0026-1394/53/3/S81, **a search snippet only;
the page returned a bot-check and was not read first-hand.** So the record has been sorted by the
goal at least once, at one moment, roughly the 2007 era, by the field itself. **The stronger claim is
withdrawn.** What still stands, searched and not found three sessions running: nothing tracks the
tail across time, names who stays in it, or observes the median and the tail parting company — and
no artwork anywhere uses this material.

**The stakes, now checked, with two analogies refused.** ITU-T G.8272 defines a Primary Reference
Time Clock, PRTC-A, as **within 100 ns of UTC** — SOURCED from a secondary summary, because the ITU
text is login-gated. GNSS ranging: 1 ns ≈ 30 cm. **Never usable here, being three orders of magnitude
looser:** MiFID II timestamping at 100 **microseconds** (Reg. (EU) 2017/574, Annex Table 1, read
first-hand) and grid synchrophasor timing at ~26–32 **microseconds**.

**The gate's standing condition on this file, in the Kritiker's words.** The material is *"not
exhausted, but it is now on notice… A fourth concept on this corpus may only be brought to me if it
solves the stake before a form is chosen — how the visitor learns what the outside is, inside the
image, with no label and no misattribution. Arrive with a form first again and I will close the file
rather than read it."*
