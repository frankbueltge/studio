# Étude 01 — does the past actually change?

*Session 98, 2026-08-15. Bounded, discardable, and built to kill the concept cheaply if the
answer had been no. It dies with its concept; that price is accepted.*

## The question it had to answer

A concept about a register rewriting its own past is worth nothing if the past does not move.
Before any form, any staging and any receiver, one number decides whether there is a work here:
**when this register republishes a figure about a month that is already over, does the answer stay
the same?**

If yes, the concept dies tonight for the price of a script.

## The corpus

U.S. Immigration and Customs Enforcement publishes detention statistics as a workbook, and
**version-stamps each release in the filename** (`FY25_detentionStats11212024.xlsx`). The live page
links only to the newest; the older dated URLs stay reachable but fall out of the page's navigation.
The Internet Archive captured them.

- **26 editions of fiscal year 2025**, published **21 November 2024 → 25 September 2025**, every one
  fetched from the Internet Archive at a pinned timestamp.
- `corpus-manifest.json` carries, for each: filename, archive timestamp, byte length, **sha256**.
- **The corpus itself is not committed** — 19 MB of a third party's files. `fetch.py` rebuilds it
  byte-for-byte from the manifest's timestamps; the hashes prove the rebuild is the same corpus.
- `ice.gov` itself returns **HTTP 403 to automated clients** (Akamai bot mitigation) — tested from
  this environment tonight against both the page and the workbook URLs. Every byte here therefore
  comes from the Internet Archive's captures of ICE's own files, and the record says so rather than
  implying we fetched the source directly.

## The first build was wrong, and it is kept

`compare-FIRST-BUILD-WRONG.py` reported that **38.1 %** of tracked figures changed. That number is
false and no session may cite it. Its keys collided across the sheet's stacked header blocks, so a
value from one block was compared against a different block's value in the next edition. Its output
was full of runs of `-> 0.0`, and a hand-check of the raw cells showed the two editions to be
**identical** exactly where it claimed a change.

It is committed unchanged, under a filename that says what it is. The rebuild
(`compare.py`) re-reads the header stack for every block, gives each block an ordinal, and **drops
any key that occurs more than once inside a single edition** rather than guessing — 330 of 708 keys
were discarded on that rule.

**The rebuild's own headline — 40.5 % of tracked keys changed — is ALSO not publishable**, and is
recorded here only as a reason to keep working. It rests on the same fragile row-label keying that
produced the first error, it drops nearly half its keys, and nothing in this étude has yet
established that the surviving keys are correctly matched across editions. **A rate is not claimed.
One instance is.**

## What is established, cell by cell

`trace.py` follows one row across all 26 editions. The row is the register's own words:

> **Single Adults with a Positive Fear Determination Still in Custody** — average days in custody

| the same question | 21 Nov 2024 | 11 / 12 / 18 Dec 2024 | 3 Jan 2025 → 25 Sep 2025 (22 editions) |
|---|---|---|---|
| average days in custody, **Aug 2024**, month end | **274.55** | 0 | **80.37** |
| average days in custody, **May 2024**, month end | 166.56 | 0 | 83.46 |
| average days in custody, **Oct 2023**, mid-month | 70.34 | 0 | 74.31 |

**22 consecutive month-points — October 2023 through August 2024 — were published as a rising
series, then set to exactly zero in the next edition twenty days later, then restated, and have not
moved since.** The November series rises steeply, 70 → 274 days. The restated series is flat.

> **RESTATED IN SESSION, session 98, on the Kritiker's condition 4 — and the first draft of this
> paragraph was drama where the material carried something better.** It said the restated series
> came back "at roughly a third of their original values" and that "the rise was erased". That is
> true of the 2024 end of the window and false of the 2023 end. `finding.py` computes it and any
> second hand can re-run it:
>
> - **16 material restatements** (first non-zero value vs last, differing by more than 5 %), and
>   **all 16 are in this one row** — out of 378 keys the instrument tracks.
> - **6 were revised UP and 10 DOWN**, and the split is exactly by month: every 2023 month rose
>   (2023-Dec-end **+74.1 %**, 84.20 → 146.55 days), every 2024 month fell (2024-Aug-end
>   **−70.7 %**, 274.55 → 80.37).
> - **The 108 points describing January–September 2023 never took more than one value** in any of
>   the 26 editions. Nothing outside the window moved.
>
> So it is not an erasure and not a flattening. **A steep climb was replaced by a flat line, by
> lifting one end and cutting the other** — and the window it happened in is exactly the published
> span of **U.S. federal fiscal year 2024** (October 2023 – September 2024), restated in editions
> dated December 2024 and January 2025, **after that fiscal year had closed**. The register's own
> and only public sentence promises the data are *"locked" at the conclusion of the fiscal year.*

**The zero editions are an artifact, and are labelled as one.** Three consecutive editions
(11, 12, 18 December 2024) carry exact zeros across the window; 173 of the instrument's 918 raw
change events are excursions to or from 0.0. A broken edition is not a disappearance and this record
does not stage it as one. What survives the artifact is the before and the after, which are twenty
months apart in publication and are the finding.

The change is verifiable by hand in two files: rows 4–6 (the year, month and mid/end header stack)
and row 8, in
`FY25_detentionStats11212024.xlsx` (sha256 `6a5274652d079cda…`) and
`FY25_detentionStats12112024.xlsx` (sha256 `a9820c3746bddb7f…`).

## What is NOT claimed, and this is the load-bearing part

- **Not that the old numbers were right and the new ones wrong.** A monotonic rise to 274 days has
  the shape of a computation that was itself in error. The restatement may be a correction, and a
  correction is a good thing for an agency to make.
- **Not that anything was concealed.** No intent is alleged, and none is knowable from these files.
- **Not a rate.** See above. One instance, fully shown.

**What IS claimed is narrower and survives all three:** the register gave two different answers to
the same question about the same finished month, **the change carried no notice, no date, and no
changelog**, and a reader of the live page today cannot discover that the earlier answer ever
existed. The keeper's entire published statement on the matter is one sentence, carried on the `Header` sheet
of the workbook itself, **byte-identical in all 26 editions** (checked across the corpus tonight):

> *"ICE confirms the integrity of the data as published on this site and cannot attest to subsequent
> transmissions.  Data fluctuate until “locked” at the conclusion of the fiscal year."*
> — `Header` sheet, every edition 2024-11-21 → 2025-09-25; verify in any file in `corpus-manifest.json`

*Data fluctuate* is the admission, in the flat present tense. What is missing is any record of the
fluctuation.

> **CORRECTED IN SESSION, session 98.** This paragraph first quoted the sentence as *"…**but** cannot
> attest… Data **may** fluctuate until **it is** locked…"* and cited it to
> `https://www.ice.gov/detain/detention-management`. That wording came from a scout's third-party
> extraction of the web page, which this house **cannot fetch** (ice.gov returns 403 to automated
> clients) and therefore could not check. The primary source we do hold — the workbook — says
> something flatter and stronger, and the citation now points at a file with a sha256 instead of a
> page we cannot open. The error stands here above its correction. **A house whose whole law is
> honesty by labelling put an unverified quotation on a work's face and caught it four hours later
> only because it went looking for the primary source.**

## The verdict this étude returns to the concept

**The past moves, and it moves by a factor of three.** The concept is not killed. It now owes the
harder thing: a form, and a demonstration that a stranger meets this in under a minute without
being handed a spreadsheet.

## Dependencies

`openpyxl` 3.1.5 (MIT) — analysis only, not shipped in any work. Python 3 standard library
otherwise. No network at analysis time; `fetch.py` is the only networked step.
