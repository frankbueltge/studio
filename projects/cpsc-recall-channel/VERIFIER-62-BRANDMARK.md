# THE VERIFIER — session 62, 2026-08-03

*Facts and tiers only. No vote on form. Single-issue session: close the one figure
`VERIFIER-61.md` named as the thing it most wanted re-checked — how many of the 55
recall records describe an object carrying the manufacturer's or seller's brand mark
**on the object itself**. Every count below was produced by reading all 55
`Description` fields myself, one at a time, and recording a YES/NO/AMBIGUOUS call for
each. The extraction script named in §2 prints text for a human to read; it does not
classify anything, and no regex produced any figure in this file.*

---

## 1. The written coding, quoted verbatim

From `PILLORY-AUDIT-60.md` §1 (lines 25–41):

> **MARK-ON-OBJECT (primary coding, "strict").** A record is coded YES only if
> its `Description` states, in terms that locate it physically, that **the
> firm's brand name, logo, or trademark** is printed, stamped, engraved,
> embroidered, moulded, or affixed (as a label/tag/plate) **directly on the
> product itself, or on a component that is structurally part of the product
> as sold** — a base, a door, a handle, a sole, a seam, a ceiling canopy, a
> trolley body, or a bottle/pouch that *is* the product's own housing. It is
> coded NO where the mark described is on: the outer box, polybag, or
> shrink-wrap; an included instruction manual; a purchase receipt or order
> confirmation; or a component of a *different*, non-recalled item bundled
> with the recalled one (a lunch box the recalled cup came in, for instance).
> A bare model number, catalog number, serial number, batch number, or date
> code with **no brand name or logo stated alongside it** does not by itself
> count — a part number identifies a unit, not a firm. Where the notice
> explicitly denies any mark on the product itself ("has no labeling or
> product identification on the product itself"), that is a clean NO
> regardless of what the packaging carries.

This is the same primary/strict coding used to produce PILLORY's headline 23/55 — I
applied *this* coding, not the LOOSE or ANY-MARK-ANYWHERE alternatives named alongside
it in the same file, since it is the one the house currently quotes.

### Where it is under-specified, and my tightening (VERIFIER, 2026-08-03, session 62)

Applying the coding to every one of the 55 records by hand surfaced three places its
text does not decide the call on its own. Two of them I close in writing here; one I
leave open, deliberately, and report the record it affects as AMBIGUOUS rather than
resolve it by fiat.

**(a) Attached storage components (pouches, pockets) — CLOSED.** The coding lists "a
bottle/pouch that *is* the product's own housing" as an on-object example, but does
not say whether an attached pouch or pocket that is *part of* a larger item (rather
than the item's entire housing) counts the same way. **Tightening:** a pouch, pocket,
sleeve, or similar soft container sold as an integral, attached component of the
recalled item — not a separately packaged accessory — is treated as structurally part
of the product under this clause, whether or not it constitutes the item's entire
housing. This resolves record 26630 (label on a bed rail's own fabric pouch) and 26608
(brand name on a bed rail's own storage pocket) to a definite YES rather than leaving
them as open calls.

**(b) Partial-unit qualifiers ("some of the trolleys…", "some of the seats…") —
NOT closed; reported as AMBIGUOUS.** The coding does not say whether a record counts
when the Description states an on-object mark for only an explicitly named *subset* of
the recalled units, rather than the recalled population as a whole. I decline to
resolve this silently in either direction: **tightening** — where a Description
qualifies the on-object statement with "some of," code the record AMBIGUOUS, not YES
or NO, and report it separately rather than absorbing it into either tally without
comment. This affects record 26632 (TT Trsmima) only.

**(c) A record's own wording versus a near-identical sibling record's wording — left
open.** Record 26602 states "the product has… a label"; its evident sibling, 26603
(same firework format, same firm's-mark-on-a-colored-label pattern), states "the
product packaging has… a label." The coding turns entirely on this location word, and
nothing in its text says whether to read each record's own wording literally (which
would split the two records) or to harmonize apparent siblings (which would treat both
alike). I did not invent a rule to force this closed — importing an assumption about
CPSC's drafting consistency is outside what the coding's own text licenses. Record
26602 is reported AMBIGUOUS; 26603's own wording is unambiguous ("packaging" is
explicit) and is coded NO on its own text.

---

## 2. Source of record

- File: `observation/recalls-2026-07-01_2026-08-02.json`
- **sha256 (computed tonight):**
  `cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1`
- **Matches** the abbreviated value stated in `THE-RULE.md` line 5
  (`cf45ebec…4784da1`) — full digest checked character-for-character, not just
  the printed prefix/suffix.
- Byte size: 168,109 bytes — matches `PILLORY-AUDIT-60.md` §7's stated size.
- Record count: **55**, confirmed by `len(json.load(...))`. No filter, no date cut,
  no sample, no exclusion — all 55 records in the file were read and coded.
- Extraction script (prints fields only, classifies nothing):
  `observation/verifier-62-extract.py`, re-runnable by a stranger:
  `python3 verifier-62-extract.py recalls-2026-07-01_2026-08-02.json`

---

## 3. The count

**Primary count (my best-call resolution of the two AMBIGUOUS records, leaning toward
the reading each record's own literal text supports): 23 of 55 = 41.8%.**

**AMBIGUOUS: 2 of 55** — record 26632 (partial-unit qualifier, §1(b)) and record 26602
(product-vs-packaging wording, §1(c)).

**Band, floor to ceiling:**

| resolution of the 2 ambiguous records | count | % of 55 |
|---|---|---|
| **floor** — both coded NO (excluded) | **21 / 55** | **38.2%** |
| **primary** (my best call) | **23 / 55** | **41.8%** |
| **ceiling** — both coded YES (included) | **23 / 55** | **41.8%** |

The floor and my best-call primary differ by exactly the 2 ambiguous records; my
primary call happens to land on the same value as the ceiling because I lean YES on
both of them (26632: at least one on-object instance is explicitly stated in the
recalled population, even though not stated of all of it; 26602: its own text says
"product," not "packaging," and I read it at face value). A stricter reader who
resolves both the other way lands on the floor, 21/55. **The full defensible band is
21–23 of 55 (38.2%–41.8%).**

### Comparison against the standing figure

The standing figure, currently quoted by the house (`PILLORY-AUDIT-60.md` §3(ii),
carried into `WORKBOARD.md` and `KRITIKER-GATE-60.md`): **23 of 55, band 20–32.**

**Verdict: CONFIRMS the primary count (23/55) exactly. CORRECTS the band.**

My independent hand review, applying PILLORY's own coding text literally to all 55
records, finds only **2** genuinely undecided records, not the 12 PILLORY's own
ambiguity table lists. Of PILLORY's 12 flagged-ambiguous records, **9 are resolved to
NO by clauses already written into PILLORY's own coding**, not left open by it:

| recall # | PILLORY called it "ambiguous" | resolved by which clause already in the coding |
|---|---|---|
| 26651, 26658, 26605, 26609, 26599, 26619 | bare model/catalog/serial number, no brand name | the coding's own sentence: *"A bare model number… with no brand name or logo stated alongside it does not by itself count"* |
| 26623 | mark on the lunch box, not the recalled cup | the coding's own worked example: *"a component of a different, non-recalled item bundled with the recalled one (a lunch box the recalled cup came in, for instance)"* — this is the coding's own example, verbatim |
| 26593 | mark on the wipe packet and outer box | the coding's own exclusion: *"the outer box, polybag, or shrink-wrap"* |
| 26639 | personalized embroidery, not a stated firm mark | the coding requires *"the firm's brand name, logo, or trademark"*; personalized buyer decoration is not the firm's mark under any reading of that phrase |

None of these 9 required a new rule from me — the coding as PILLORY itself wrote it
already answers them. Only 3 of PILLORY's 12 involved a real gap in the coding's text
(§1 above), and of those, my tightening closes 1 outright (26630 — resolved YES, same
call PILLORY made, but no longer resting on an open question) and leaves 2 genuinely
open (26632, 26602 — both of which PILLORY also called YES, so its primary count of
23 is unaffected either way).

**Net effect: the headline number holds. The claimed sensitivity — that the on-object
count could plausibly be as low as 20 or as high as 32 — does not hold under the
coding's own written terms.** The correct band, read strictly, is **21–23/55
(38.2%–41.8%)**, a span of 2 records, not 12.

---

## 4. Claim found CORRECTED elsewhere (not edited — reported per house discipline)

**`PILLORY-AUDIT-60.md` §3(ii) and §3(iii), and every place that repeats "band
20–32"** (`WORKBOARD.md` line 340 and line 369's "36.4–58.2%", `KRITIKER-GATE-60.md`
line 219's "23 of 55… SURVIVES"): the **23/55 point figure HOLDS** and is confirmed
above. The **"band 20–32" (36.4%–58.2%) is CORRECTED** — it is not supported by
PILLORY's own coding once that coding is applied literally to the 12 records it lists
as ambiguous; 9 of the 12 are determinate NO under clauses already written into that
same coding. The defensible band is **21–23/55 (38.2%–41.8%)**. I have not edited
`PILLORY-AUDIT-60.md` or any file that repeats its band — this file reports the
correction; the conductor appends it.

No other FALSE claim was found in the course of this review. `VERIFIER-61.md` §5.5's
finding — that the brand-mark figure was wrongly declared "settled" in a
`REQUESTS.md` correction, and that the underlying gap was still open — is confirmed
consistent with what this session found: the gap **was** still open when VERIFIER-61
wrote that, and is closed, to the band above, only as of tonight's hand review.

---

## 5. Per-record table — all 55 records

Coded by hand against §1's coding (as tightened in §1(a)–(c)). Object name is the
`Products[0].Name` field (or the Title's leading noun phrase where no `Products` entry
exists). Quotations are drawn from each record's own `Description` field.

| # | RecallNumber | Object | Code | Reason (where not obvious from the coding alone) |
|---|---|---|---|---|
| 1 | 26645 | EnHomee 15-Drawer 51" Dressers | NO | no mark or label of any kind described anywhere in the text |
| 2 | 26646 | KAIFAM 5-Drawer Dressers | NO | SKU/item text is on "the product packaging," not the dresser; no brand name stated there either |
| 3 | 26647 | BenQ GV31 Portable Projectors | YES | brand name and model printed on a label on the underside of the projector's own base |
| 4 | 26649 | Galanz Retro Refrigerators | YES | "Galanz" printed on the freezer door front; also on a label on the back of the unit |
| 5 | 26650 | Fantastic Four Cups / Captain America Helmet Containers | NO | no mark location described anywhere |
| 6 | 26651 | Nordi Foldable Toddler Tower Stools | NO | only a bare model number ("HANS0002") on-object; brand name HARPPA never stated there |
| 7 | 26652 | OCTROT Electric Throws and Blankets | NO | brand name and model stated on "the product packaging" only |
| 8 | 26653 | World Class Fireworks "Skull Strobe" Rockets | NO | brand, product name, SKU all on the box/packaging |
| 9 | 26654 | Sloosh Dive Sticks (40041, 40003, 16154) | YES | "Joyin's name" printed "on top of one end of the dive stick" itself, for every listed model |
| 10 | 26655 | Mangohood Direct Kids Kitchen Standing Towers | NO | no mark location described anywhere |
| 11 | 26656 | Mommy's Baby Lovely Deluxe Baby Doll Playsets | NO | bare model sticker on the box, not on the doll/playset; and no brand name stated |
| 12 | 26659 | OCOOPA Rechargeable Hand Warmers | YES | "OCOOPA" printed "on the top of the hand warmers" themselves |
| 13 | 26657 | Cpzzkq Baby Loungers | YES | "CPZZKQ" printed on a side label of the lounger itself |
| 14 | 26632 | TT Trsmima Zipline Kits and Spring Brakes | AMBIGUOUS | on-object brand text explicit for "some of" the trolleys and "some of" the seats — not stated of the recalled population as a whole (§1(b)) |
| 15 | 26658 | Woodure Toddler Kitchen Step Stools | NO | only a bare model number engraved on-object; brand name never stated there |
| 16 | 26634 | Romorgniz 12-Drawer Fabric Dressers | NO | no mark location described anywhere |
| 17 | 26635 | Sili Factory / Aojieni Pull String Teething Toys | NO | brand name and batch number are on the packaging only |
| 18 | 26638 | CuddleCubs Creations Highchair Teething Toy Sets | NO | no mark location described anywhere |
| 19 | 26633 | EnHomee 9-Drawer Fabric Dressers | NO | no mark location described anywhere |
| 20 | 26637 | OeyUoc Pool Drain Covers | NO | notice explicitly states "no labeling or product identification on the product itself" |
| 21 | 26639 | Personalized Baby Bibs and Stroller Bags | NO | "personalized" embroidery is buyer-chosen decoration, not a stated firm brand mark |
| 22 | 26636 | Sviyatp Pool Drain Covers | NO | notice explicitly states "no labeling or product identification on the product itself" |
| 23 | 26621 | Nottaway Chandelier Fixtures | YES | "Currey & Company" printed on a label "atop the fixture's ceiling canopy" — the coding's own worked example |
| 24 | 26624 | Hollis 200LX Second Stage Diving Regulators | YES | "Hollis" and "200LX" "engraved on top of the regulator" itself |
| 25 | 26626 | Jobon Butane Torch Lighters | YES | "JOBON" "printed on the side of the lighter" itself |
| 26 | 26619 | Liizousuda Paint Thinner | NO | bottle's wraparound label states product-description text; firm name Liizousuda never stated to be on it |
| 27 | 26625 | Madewell Double V-Neck Pullover / V-Neck Cardigan Sweaters | YES | "Madewell" printed on the sewn-in neck label |
| 28 | 26630 | MNIENT Adult Portable Bed Rails | YES | brand and model on the label on the rail's own black fabric pouch (§1(a) tightening) |
| 29 | 26627 | Noerishia Adult Portable Bed Rails | NO | brand name appears on packaging and on the instruction manual only; never stated on the rail itself |
| 30 | 26617 | Oitnlaughter LED Finger Lights | NO | no mark location described anywhere |
| 31 | 26618 | Panasonic Electric Toaster Ovens (Model NB-G200) | YES | "the brand name Panasonic is written on the front of the product" itself |
| 32 | 26628 | SDADI Kitchen Step Stools (LT01, LT05) | NO | no mark location described anywhere |
| 33 | 26629 | Cat & Jack Children's Sandals | YES | "the brand is printed on the shoe's sole and bottom" — the coding's own "sole" example |
| 34 | 26620 | Boon PIVOT Collapsible Toddler Tower Kitchen Step Stools | YES | "'boon' is visible along the top rail" of the stool itself |
| 35 | 26622 | Wade Logan Annyka 9-Drawer Fabric Dressers | NO | SKU/color label is on "the outer packaging"; no brand name stated there |
| 36 | 26623 | Space King "No Girls Allowed" Relic Lunch Boxes (cups only) | NO | mark ("Space King") is on the lunch box, a different bundled item — the coding's own worked example; the recalled cup itself carries no stated mark |
| 37 | 26606 | Insignia Front Control Gas Ranges | YES | "the 'Insignia' label" is "on the bottom of the oven door" itself |
| 38 | 26607 | BBRKIN and MouTec Biometric Firearm Safes | YES | brand name "on the upper right corner of the front of the safes" themselves |
| 39 | 26605 | Cuisinart Propel+ Four Burner 3-in-1 Gas Grill | NO | only a bare model/serial number on the door label; brand name Cuisinart never stated there |
| 40 | 26610 | Flaunt MagSafe Battery Chargers | YES | "'FLAUNT' is engraved on the front… of the power bank" itself |
| 41 | 26611 | Kobalt 24V/48V Trimmers, Blowers, Mowers, Chainsaws, Pruning Saws | NO | "Kobalt-branded" is stated generically, with no on-object location given anywhere in the record |
| 42 | 26608 | Moodooy Adult Portable Bed Rails | YES | brand and model "printed on the storage pocket," an attached component of the rail (§1(a) tightening) |
| 43 | 26609 | WonderStone Infant Walkers | NO | only a bare model number on the under-tray label; brand name never stated there |
| 44 | 26596 | AMASKY Nursing Pillows | YES | "'Brand: AMASKY'… printed on a label attached to the pillow" itself |
| 45 | 26601 | Metal Wire Bristle Grill Brushes (Cuisinart) | YES | "the word 'Cuisinart' is stamped on the brush handle" itself |
| 46 | 26599 | Metalux Optimized High Bay (OHB) LED Light Fixtures | NO | only catalog number and date code on the label; brand name Metalux never stated there |
| 47 | 26593 | CVS Health Medicated Hemorrhoidal Wipes | NO | mark is on "the front of the packet and the box," not the wipe itself |
| 48 | 26600 | Junpower CR2032 Batteries | NO | brand text is on the outer box only; nothing stated about the battery cells themselves |
| 49 | 26594 | POPOOO Jungle Safari LED Finger Lights | NO | brand text is on "the product's blue packaging" only |
| 50 | 26595 | Rowenta Cordless Vacuum Cleaners | NO | no on-object mark location described anywhere |
| 51 | 26598 | Gigglescape™ Under the Sea Popping Toy | YES | brand "imprinted on the bottom of the blue plastic base" itself |
| 52 | 26592 | Topyond Pool Drain Port with Cover | NO | notice explicitly states "no labeling or product identification on the product itself" |
| 53 | 26591 | VEVOR Baby Loungers | YES | "'VEVOR' is printed on an attached tag on the outside of the baby lounger's cover" |
| 54 | 26603 | Roman Candles 8 Shot 3-Pack Firework Devices | NO | label text is explicitly on "the product packaging" |
| 55 | 26602 | Unity 7 Shot 200 Gram Aerial Cake Firework Devices | AMBIGUOUS | text says "the product has… a label" (not "packaging"), unlike sibling 26603's explicit "packaging" — real distinction or drafting variance, undecidable from the coding's text (§1(c)) |

**Tally: YES = 21 · AMBIGUOUS = 2 · NO = 32. Total = 55.**

---

## 6. What this closes, and what it still does not

This closes the one figure `VERIFIER-61.md` flagged: a hand review of all 55
`Description` fields against the house's own written coding has now been done, by one
reader, with every call recorded above. It reproduces the standing 23/55 exactly and
narrows the standing 20–32 sensitivity band to 21–23 — a materially tighter claim than
the house has been able to make about this figure since it first appeared.

It does not, and cannot, adjudicate between the STRICT coding used here and the LOOSE
or ANY-MARK-ANYWHERE alternatives named in `PILLORY-AUDIT-60.md` §1 — that is a choice
about which coding to use, not a fact this review can settle. It also does not revisit
`PILLORY-AUDIT-60.md`'s SURVIVES finding or its M2 verdict; those stood on the on-
object figure only at the level of "which side of the 20% threshold," and 21–23/55
(38.2%–41.8%) does not move that answer.

A single reader coded all 55 records once. A second, independent hand-coding of the
same 55 fields against the same written coding — checking not the extraction, which is
mechanical, but the 55 individual calls — would be the only way to test this figure
further, and is the honest limit of what one reviewer, reading once, can close.

---

*Written 2026-08-03, session 62, by the Verifier. Files read: `PILLORY-AUDIT-60.md`,
`THE-RULE.md`, `VERIFIER-61.md`, `WORKBOARD.md`, `KRITIKER-GATE-60.md`,
`STAGING-RULING-59.md`, `ARTIST-SCORE-60.md`, `VERIFIER-60.md`,
`observation/recalls-2026-07-01_2026-08-02.json`. Files written:
`observation/verifier-62-extract.py` (extraction only, no classification logic), this
file. No other file in this repository was edited.*
