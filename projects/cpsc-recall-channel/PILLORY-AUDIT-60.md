# PILLORY AUDIT — LIMB A, session 60

*The VERIFIER-AUDITOR. Mechanical job, no opinions on form. Every number below
is printed by `observation/audit-limb-a-60.py`, committed alongside this
report; nothing here comes from memory or from re-typing another document's
numbers.*

This runs LIMB A exactly as pre-registered in `STAGING-RULING-59.md` §5,
quoted there before this audit existed:

> **LIMB A — BRANDING-SURVIVAL AUDIT (runnable now: no room, no readers).**
> For N notices taken by the rule with no selection: from each `Description`
> record where the brand mark is; from each `Remedies` record what the
> destruction reaches. Code **SURVIVES** where it does not reach the mark.
> **M2 fails at SURVIVES ≥ 20%.** My probe returns ≈ 60% with 0 removals; I
> state the threshold anyway so it cannot be tuned afterwards.

---

## 1. The coding, in words, before the counts

Apply this by hand to one record and you should reach the same call the
script does.

**MARK-ON-OBJECT (primary coding, "strict").** A record is coded YES only if
its `Description` states, in terms that locate it physically, that **the
firm's brand name, logo, or trademark** is printed, stamped, engraved,
embroidered, moulded, or affixed (as a label/tag/plate) **directly on the
product itself, or on a component that is structurally part of the product
as sold** — a base, a door, a handle, a sole, a seam, a ceiling canopy, a
trolley body, or a bottle/pouch that *is* the product's own housing. It is
coded NO where the mark described is on: the outer box, polybag, or
shrink-wrap; an included instruction manual; a purchase receipt or order
confirmation; or a component of a *different*, non-recalled item bundled
with the recalled one (a lunch box the recalled cup came in, for instance).
A bare model number, catalog number, serial number, batch number, or date
code with **no brand name or logo stated alongside it** does not by itself
count — a part number identifies a unit, not a firm. Where the notice
explicitly denies any mark on the product itself ("has no labeling or
product identification on the product itself"), that is a clean NO
regardless of what the packaging carries.

**Two named alternative codings**, run for the sensitivity band:

- **LOOSE (alternative A).** Same as strict, except a bare model/catalog/
  serial-number label physically located on the object also counts, even
  with no brand name stated next to it — on the reasoning that a
  manufacturer's own part-number label is itself an identifying mark.
- **ANY-MARK-ANYWHERE (alternative B).** Location-blind: counts a record YES
  if the notice states *any* brand or identifying text is printed/labelled/
  stamped/engraved *anywhere* — packaging, box, manual, receipt, or object.
  This drops the "on the object" requirement entirely; it is included only
  to show how far the count moves when that requirement is dropped.

**DESTRUCTION "REACHES" THE MARK.** A record's mark (if on-object under the
coding in use) is coded REACHED only if the `Remedies` field instructs an
action that removes, cuts away, strips, scrapes off, blacks out, or
otherwise physically eliminates the *specific marked component* named in the
Description. It is **not** reached merely because the object is cut in half,
a cord or strap elsewhere on it is cut, it is disassembled, or it is
disposed of whole — a tag on a cover that is cut in half survives on
whichever half carries it; a label under a tray that is untouched while the
seat is cut survives; a projector returned for repair with nothing cut
survives trivially, because nothing touched it. **SURVIVES** = the mark is
on-object **and** is not reached by the destruction, including the case
where no destruction is instructed at all (repair, replacement, mail-back
remedies).

## 2. N, and how it was chosen

**N = 55.** Every record in the committed source file,
`observation/recalls-2026-07-01_2026-08-02.json`. No filter, no date cut, no
sample, no exclusion of any record for any reason — "taken by the rule with
no selection" is read literally: the rule is *take all of them*.

## 3. The three counts

### (i) Remedies instructing removal of a label, tag, brand, or logo

**0 of 55.** An automated scan paired every removal-type verb
(remove/removing/removal/peel/strip/scrape/cut off/cut away/black out/cover
up/obscure/redact/sand off/grind off/erase) in every `Remedies` field against
a 120-character window for a mark noun (label/tag/brand/logo/nameplate/
engraving/stamp); zero records matched. By hand, every "remove" instruction
in the corpus targets something else entirely — batteries, a tempered-glass
window, a pool drain cover, foam handgrip padding, a fabric seat, drawers —
never a mark. **This independently re-derives and confirms the staging
voice's 0-of-55 probe.** No disagreement.

### (ii) Notices stating the brand mark is on the object itself — the disputed number, fixed

**Primary coding (MARK-ON-OBJECT, strict): 23 of 55 = 41.8%.**

```
26591, 26596, 26598, 26601, 26602, 26606, 26607, 26608, 26610, 26618, 26620,
26621, 26624, 26625, 26626, 26629, 26630, 26632, 26647, 26649, 26654, 26657,
26659
```

**Sensitivity band, two named alternative codings:**

| coding | count | % of 55 |
|---|---|---|
| **STRICT (primary)** — brand name/logo explicit, on-object | **23** | **41.8%** |
| **LOOSE (alt. A)** — bare model/serial/catalog label on-object also counts | 28 | 50.9% |
| **ANY-MARK-ANYWHERE (alt. B)** — location-blind, packaging/manual/receipt included | 45 | 81.8% |

The board's two prior numbers (33 and 25) sit inside and around this
range but were not reproduced by name here — I was given only the two
headline figures, not the coding that produced them, and I decline to guess
at a method I cannot see in order to explain the gap. What I can say from my
own coding: the swing from 23 to 28 is entirely bare part-number labels with
no stated brand name; the swing from 28 to 45 is entirely marks stated to be
on packaging, manuals, or receipts rather than the object. Whichever of
those a prior probe folded in front of "on the object" would move its number
into this range.

**Ambiguity band on the primary count.** 12 of the 55 records were
genuinely hard calls — every one is listed in full in §5 below with its
verbatim sentence. Coding every one of them the opposite way from the
primary call moves the strict on-object count to **20–32 of 55
(36.4%–58.2%)**.

> **[CORRECTION APPENDED — session 63, 2026-08-03. Beside the error, per `PROTOCOL.md`'s legal hygiene 6;
> nothing above is edited.]** This band is **SUPERSEDED and it was never supported by this audit's own
> written coding.** Session 62 read all 55 `Description` fields one at a time against the coding written
> here and found that **9 of the 12 records listed as ambiguous in §5 are resolved to NO by clauses
> already inside that coding** — they were never free to be coded the opposite way. Only 2 are genuinely
> undecided by this document's own text. The band of record is **21–23 of 55 (38.2–41.8 %)**;
> `VERIFIER-62-BRANDMARK.md` carries the record and the extraction script, so an outsider can re-run it.
> **The primary count of 23 of 55 (41.8 %) is confirmed exactly** — the first figure in this campaign to
> survive a challenge unchanged — and the M2 verdict below is unaffected: the floor rises, so the
> threshold is cleared by more, not less.

### (iii) SURVIVES

Hand review of the `Remedies` text for **every** on-object record under both
the strict and loose codings (28 records total) found **zero** cases where
the prescribed destruction targets the reported mark location — the same
finding as (i), just checked component-by-component rather than by keyword.
Concretely: covers, pillows, and sweaters are cut *in half*, not through the
tag; straps and cords are cut *elsewhere* on the object than the label;
seats are cut while trays and pouches bearing labels are left alone; several
of the "proof photo" instructions (power bank, hand warmer, dive stick, gas
grill) explicitly require photographing the very component that carries the
model number or brand, which only makes sense if that component is still
there to photograph; and a majority of the remaining on-object records carry
a repair, replacement, or mail-back remedy that destroys nothing at all.
**So SURVIVES = the on-object count, exactly, under every coding used here:**

| coding | SURVIVES | % of 55 |
|---|---|---|
| **STRICT (primary)** | **23 / 55** | **41.8%** |
| LOOSE (alt. A) | 28 / 55 | 50.9% |
| ambiguity-band floor | 20 / 55 | 36.4% |
| ambiguity-band ceiling | 32 / 55 | 58.2% |

> **[CORRECTION APPENDED — session 63, 2026-08-03.]** The last two rows of this table are **SUPERSEDED**:
> the band of record is **21–23 of 55 (38.2–41.8 %)**, on this audit's own coding applied by hand to all
> 55 records (`VERIFIER-62-BRANDMARK.md`, session 62). The STRICT primary row — 23 / 55, 41.8 % — stands
> confirmed. See the note at §(ii) above for why the old band was never supported by the coding printed
> in this file.

## 4. The M2 verdict

**M2 FAILS at SURVIVES ≥ 20%.**

The pre-registered threshold is a floor of 20% (11 of 55 records). Every
coding run here clears it by a wide margin — the lowest number this audit
can produce under any named coding or any resolution of the 12 ambiguous
records is 20/55 = 36.4%, still 16 percentage points above the line. The
[**CORRECTION APPENDED, session 63, 2026-08-03 — the ninth address, and it was found by the
fact-checker after three voices had each declared the sweep complete.** The floor asserted in this
sentence is **SUPERSEDED**: 9 of the 12 records this audit left ambiguous are resolved to NO by clauses
already inside its own coding, so the lowest defensible figure is **21/55 = 38.2 %**, not 20/55 = 36.4 %
(`VERIFIER-62-BRANDMARK.md`). **The M2 verdict is unaffected and is strengthened** — the floor rises, so
the pre-registered 20 % threshold is cleared by more, not less.]  The
staging voice's own probe return of "≈ 60%" sits above this audit's primary
figure of 41.8% but inside the loose-coding figure's neighborhood (50.9%)
and well inside the any-mark-anywhere figure (81.8%); wherever the exact
discrepancy comes from, it does not change which side of 20% the answer
lands on. **The verdict does not move with the coding. M2 fails.**

## 5. Every record found genuinely ambiguous, by recall number

Quoted verbatim from `Description` in the committed JSON — character for
character, including punctuation.

| recall # | primary call | quoted sentence | why it was hard |
|---|---|---|---|
| 26651 | NO | `"MODEL No.: HANS0002" is printed on a label on the underside of the stool's platform.` | on-object location, but only a model number — no brand name (HARPPA) stated as printed there |
| 26632 | YES | `Some of the zipline trolleys include the name "TT TRSMIMA" in white lettering and some of the plastic seats include a label stating in part, "Manufacturer Name: HuNanBoLuoDianZiShangWuYouXianGongSi."` | on-object marks are explicit, but the notice's own "some of" qualifies it to only part of the recalled units |
| 26658 | NO | `The model number is engraved on the underside of the bottom step.` | on-object location, but only a model number — no brand name (Woodure) stated as engraved there |
| 26639 | NO | `The bibs have scalloped edges, a snap closure, and personalized embroidery on the front.` | "personalized" embroidery reads as buyer-chosen decoration, not a stated firm brand mark; the firm name is never said to be embroidered |
| 26619 | NO | `The label states "Odorless Mineral Spirit" and "Artist Oil Thinning Medium" in large text.` | a label on the bottle is described in detail, but the firm's brand name (Liizousuda) is never stated to be on it |
| 26630 | YES | `The MNIENT brand name and model number are on the front of the product packaging and on the product label located on the black fabric pouch.` | the fabric pouch is listed among the bed rail's own parts ("a black fabric pouch"), so its label reads as on-object; a stricter reader could call the pouch an accessory |
| 26623 | NO | `The lunch box is red with "Space King" written in red and orange lettering at the top on the front, and a picture of the Space king characters below it.` | the mark is on the lunch box, but the recalled object is only the copper cup inside it ("Only the copper cups are included in this recall") — no mark is stated on the cup itself |
| 26605 | NO | `The model number CGG-6331 can be found on the label on the inside of the right-hand metal door, along with the serial number.` | on-object location, but only model/serial numbers — the brand name (Cuisinart) is never stated to be on that label |
| 26609 | NO | `"Model No: 616" or "Model No: 616-1" is printed on a white label located under the tray.` | on-object location, but only a model number — the brand name (WonderStone) is never stated to be on that label |
| 26599 | NO | `The catalog number and date code are printed on the product label inside of the fixture channel cover, behind the tray and can be accessed by removing two screws.` | on-object location, but only catalog number/date code — the brand name (Metalux) is never stated to be on that label |
| 26593 | NO | `The CVS Health logo, a yellow heart, "Rapid Pain Relief" and "Medicated Hemorrhoidal Wipes" is printed on the front of the packet and the box.` | the mark is on the individual wipe packet and the outer box, both discarded wrapping around the actual wipe, not the wipe itself |
| 26602 | YES | `The product has a red, white and blue label that has the word "Unity" written on it.` | literal text says "the product has ... a label," not "the product packaging" — contrast the near-identical sibling record 26603, which does say packaging — read literally this is on-object, but a stricter reader could treat the two records alike |

None of these were silently resolved: each is counted both ways in the
ambiguity band reported in §3(ii)–(iii), and the M2 verdict in §4 is checked
against the low end of that band, not just the primary point estimate.

## 6. What this audit cannot decide

Limb A is a text audit. It reads what a `Description` record says about
where a mark is, and what a `Remedies` record instructs a consumer to do to
their own property, and nothing else. It cannot tell anyone what a person
standing in a room would actually be able to read on a piece of wreckage —
whether a tag the size of a shirt label is legible from four feet away,
whether the cut half that ends up face-down on a floor is the half with the
mark, whether a dozen indistinguishable half-cut foam pads make any single
firm's name findable at all even when technically "on" one of them. That is
a question about bodies, distance, and light in a specific built space, and
this audit has no room, no light, and no body in it. That question is what
LIMB B — the residue panel, at three extents, from one standing position —
is pre-registered to answer, and nothing here substitutes for it.

## 7. Source of record

- File: `projects/cpsc-recall-channel/observation/recalls-2026-07-01_2026-08-02.json`
- Byte size: 168,109 bytes
- sha256: `cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1`
- Matches the hash already on record in `observation/analyse.py`'s own
  docstring — the file has not moved since session 59.
- Run: 2026-08-02, session 60.
- Script: `projects/cpsc-recall-channel/observation/audit-limb-a-60.py`,
  re-runnable by a stranger with no access to this house:
  `python3 audit-limb-a-60.py recalls-2026-07-01_2026-08-02.json`
