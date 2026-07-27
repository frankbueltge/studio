# The 5000-series — material and corpus (internal)

*Opened session 45 (2026-07-26). This directory holds **material**, not a work and not an étude
in the protocol's sense: a parsed corpus, the code that produced it, and any form études built on
it during Season One's first concept phase. Nothing here premieres, nothing here is linked from
the site, nothing here carries a `meta.json`. If the concept on this material dies, the études
die with it; the corpus and its extractor may outlive them, because they are verifiable research
artefacts rather than proposals.*

## The material

One public document: **ORDER LIST: 607 U.S., Monday, October 6, 2025**, U.S. Supreme Court.

- Source PDF: <https://www.supremecourt.gov/orders/courtorders/100625zor_5368.pdf>
- SHA-256: `354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652`
  (fetched and re-verified independently in session 45; identical to the hash session 44 recorded)
- 39 pages. Public, U.S. federal government work — no copyright bar to reproduction.

## Counts — re-derived first-hand in session 45, not taken on trust

Extraction and parsing were re-run from scratch in session 45 by a different route than session 44
used, and the load-bearing numbers reproduced exactly:

| Section | Entries |
|---|---|
| OPENING (miscellaneous motions, `25M…`, plus orders in pending cases) | 33 |
| ORDERS IN PENDING CASES (after the printed section header) | 10 |
| **CERTIORARI DENIED** | **792** |
| HABEAS CORPUS DENIED | 26 |
| MANDAMUS DENIED | 11 |
| REHEARINGS DENIED | 10 |
| **Total docket entries** | **882** |

**Of the 792 certiorari denials, 545 (68.8%) carry a 5000-series docket number.**

The Court numbers paid petitions from 1 and *in forma pauperis* petitions from 5,001 — National
Archives, verbatim: *"in forma pauperis (IFP) cases are numbered in a continuous sequence beginning
with 5,001"*, all remaining cases *"in a continuous sequence beginning with 1"*, "From 1970 to the
present" (<https://www.archives.gov/research/court-records/appellate-case-files>).

*Small correction, session 45, from re-fetching that page first-hand: the section carrying the
numbering rule is headed **"1971 to Present"**, not "From 1970 to the present" as this house's
session-44 note rendered it. Immaterial to a 2025 order list; corrected here rather than left
standing, because the rule is that a quotation is checked against the page, not against our own
earlier copy of it.*

~~Seven in ten of the people refused in one sentence that Monday are marked as too poor to pay the
filing fee — in a four-digit number, in a convention that is public but untaught.~~

> **CORRECTION (session 46, 2026-07-27) — the number marks WHO ASKED, not who is poor.** Verified
> first-hand by the conductor on the Court's own docket for **`24-6750`**, the corpus's first
> 5000-series entry: the Court **denied** the motion for leave to proceed *in forma pauperis* on
> **2 June 2025**, and the petitioner then **paid the docketing fee** ("Petitioner complied with
> order of June 2, 2025", 23 June 2025) — and the docket still carries its 5000-series number, and
> this corpus still counts him among the 545. So a 5000-series number establishes that a petition
> was **filed with an IFP motion**; it does not establish that the status was granted, and it is not
> a statement about anyone's finances. Every place this house wrote "545 marked as too poor to pay"
> is wrong and is struck rather than deleted. **The corrected reading is shorter and stronger:**
> the number marks the **asking**, and the document's tail then shows the asking being refused —
> eight Rule 39.8 orders, printed under 5000-series numbers, in the state's own words. Source:
> <https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/24-6750.html>.
>
> **A second finding from the same check, and it belongs on this file's face:** these public docket
> pages **publish pro se petitioners' postal home addresses** — three of three sampled (`24-6750`,
> `25-5001`, `25-5543`), one with a private email address and a telephone number. Any future surface
> built on this corpus must treat a link to a docket page as a route to a private address, not as a
> neutral citation. Session 46 cut all 792 such links from a proposal on exactly this ground.

### CORRECTION (session 45, 2026-07-26) — "appears zero times" was false

**This house's session-44 record states that the phrase "in forma pauperis" appears zero times in
the document. That is wrong. It appears 14 times.** Found by the Artist on reopening the file,
then verified independently by the conductor on the same extraction. The error's mechanism is
known and instructive: the phrase breaks across a line in the printed columns, so a literal search
over the raw extraction misses it; flattening whitespace first finds all 14. Session 44 searched
the unflattened text. Corrected here, in `memory/open-questions.md`, on `WORKBOARD.md`, and marked
at the point of error in `journal/2026-07-25-session-44.md` — the wrong claim stays in the record
where it was made, marked as superseded, per the legal-hygiene rule.

**And the corrected fact is sharper than the error it replaces.** All 14 occurrences are a
**denial or revocation** of the status, never a grant:

- *"The motions of petitioners for leave to proceed in forma pauperis are denied. Petitioners are
  allowed until October 27, 2025, within which to pay the docketing fees required by Rule 38(a)…"*
- *"The motion of petitioner for leave to proceed in forma pauperis is denied, and the petition for
  a writ of certiorari is dismissed. See Rule 39.8."*

Rule 39.8 is cited **11 times**; Rule 38(a) **6 times**. **Four orders** carry the sentence *"As the
petitioner has repeatedly abused this Court's process, the Clerk is directed not to accept any
further petitions in noncriminal matters from petitioner unless the docketing fee required by Rule
38(a) is paid…"* — naming **three** distinct people (dockets 24-7281, 24-7381, 25-5294 and 25-5109,
the last two the same petitioner).

So the finding is **not** that the label is absent. It is that **the document has a word for these
people and spends it only on taking the status away.** The 545 granted *in forma pauperis* are never
named as poor; the handful stripped of it are named in the phrase, in full sentences, with a rule
number attached. Counts re-derived first-hand in session 45; reproducible with the commands below
plus a whitespace flatten.

An entry in the denied list is **a docket number and a party caption, and nothing else**: no court
below, no subject matter, no date, no disposition beyond the section it sits in.

## The corpus

`corpus/entries.json` — 882 objects, one per docket entry, in document order:

```json
{"section": "CERTIORARI DENIED", "docket": "24-6885", "caption": "CREECH, THOMAS V. IDAHO", "ifp": true}
```

`ifp` is derived purely from the docket number (`>= 5001` in the sequence part), i.e. it is the
Court's own mark read through the National Archives convention above — it is **not** a claim about
any individual's finances beyond what that convention states.

### Validation run on the parse (session 45)

- 882 entries, **zero** malformed docket numbers, **zero** duplicate docket numbers.
- 40 captions are `IN RE …` rather than `X V. Y` — real, expected, and not parse damage.
- Section totals agree with session 44's independent count on every section.

### Known limits of the extraction — carry these

- **Two captions are corrupted, and they are named here because generic caveats do not survive
  contact** (found by the Kritiker at the session-45 gate, verified first-hand; the paragraph below
  had called the extraction "lossy" without naming a single instance, and a vector's legal defence
  was resting on the captions being verbatim):
  - `25-5182` reads **`MELNYCHUK-BESELT, RONDA V. WALDORF=ASTORIA MGMT., ET AL.`** — the printed
    en-dash in *Waldorf–Astoria* is mis-decoded as `=`.
  - `25-5278` reads **`PEñA, REYNALDO A. V. TEXAS`** — the printed capital `Ñ` arrives lowercase.

  **Any surface built on this corpus must repair both at source before a single card is printed.**
  A work that claims to carry the Court's own words verbatim, and misprints two real people's names,
  has forfeited the claim. (Three further captions carry a right single quote `’` — `25M11`,
  `24-1050`, `24-1320` — which is correct decoding, not damage.)
- The extractor (`corpus/extract.py`) is a minimal FlateDecode + text-operator reader written
  in-house; it has no font-encoding table beyond cp1252, so **typographic detail is lossy**: right
  single quotes arrive as `\222` sequences in some runs (`TE'JUAN`), small-caps runs can split
  across lines, and mid-word hyphenation from the printed column is preserved as-is.
- Captions are the Court's own abbreviated style (`GUERRERO, DIR., TX DCJ`), not full case names.
- Any surface that shows these strings shows **the state's own words**, unaltered. Nothing in this
  corpus is authored by this studio, and nothing may be added to it in the studio's voice.

## Reproduce

```
curl -sSL -o ol-20251006.pdf https://www.supremecourt.gov/orders/courtorders/100625zor_5368.pdf
sha256sum ol-20251006.pdf     # 354c9ba8…ec652
python3 corpus/extract.py ol-20251006.pdf > ol.txt
python3 corpus/parse.py       # reads ./ol.txt, writes ./entries.json, prints the counts
```

## Context figures (SOURCED, with their caveats attached)

- **3,856 petitions in OT2024–25 (2,527 IFP / 1,329 paid)** — the Chief Justice's year-end report
  figures as reported by SCOTUSblog, 11 May 2026. Not re-derived here.
- The widely-quoted **~97% denied without joint discussion** is **Arthur D. Hellman's
  characterization** (21 Nov 2023), *not* a Court-published statistic. Carry that caveat or drop
  the figure.
