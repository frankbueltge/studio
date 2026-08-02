# VERIFIER — session 59, pass on ARTIST-REFORM-59.md
*Facts and tiers only. No vote on form. Retrieved 2026-08-02.*

sha256 of the source JSON re-verified independently: `cf45ebec…4784da1` — **matches**.
Own script, not `analyse.py`: `observation/verifier-59-check.py` (re-runnable: `python3
observation/verifier-59-check.py observation/recalls-2026-07-01_2026-08-02.json`).

## VERDICT: **PASS WITH CORRECTIONS**

The étude's load-bearing numbers (the record, the skip-count, the remedy, the units, the price,
the photograph bytes) are **all exact**. Two real errors survive from the counting step: a
same-sentence internal-consistency break in §3.1 (17 → **32**) and a definition/count mismatch
in §1's marker row (13 → **10** on a literal reading). One world-quotation in §2.4 carries
fetch-tool-rendering spacing that is not in the raw bytes — the exact failure named in
VERIFIER-58, recurring in a new spot. One claimed date range in §4 (Gagosian, self-flagged by the
motion as unverified) does not appear in the source at all.

## 1. Corpus counts (§1, §2.2, §2.3c, §3.1)

| Claim | Motion | My count | Status |
|---|---|---|---|
| begins "Consumers should…" | 52/55 | 52/55 | **VERIFIED** |
| "stop using…immediately" (motion's own §6 regex) | 50/55 | 50/55 | **VERIFIED** |
| destroy/dispose themselves | 34/55 | 34/55 (inclusive reading) / **31/55** (strict: excludes component-only battery disposal 26595, and future-note-only disposal 26610) | **VERIFIED, ambiguous** — 34 requires counting disassembly-without-cutting (26646) and component disposal as "destroying the object"; defensible but not the only reading |
| photo + email the firm | 27/55 | 27/55 reproduces by the *same* method as the motion, but that method is internally inconsistent: it counts 26595 (photo is of a battery model number, not of any destruction, delivered by website upload, no email) and misses 26646 (explicitly requires marker + photo + **email**, but has no "destroy" keyword). Strict count (photo *of the destruction*, delivered to a named **email address**): **25/55**. Loose count (any required evidentiary photo, any delivery method): **31/55** | **CORRECTED-CAVEAT** — 27 is not a clean number under either strict or loose reading; report as a range 25–31 |
| write RECALL/RECALLED/DESTROYED **in permanent marker**, first | 13/55 | Literal phrase "permanent marker" occurs in **10/55**. Reaching 13 requires adding 26592 and 26636 ("a marker", not "permanent") and 26605 ("black sharpie marker") | **CORRECTED** — true count on the stated definition is **10/55**. Worse: 26605's marking step happens *last* (after the refund and after the destruction photo), directly contradicting "first" |
| "None reported" injuries | 32/55 | 32/55 | **VERIFIED** |
| §2.2 closed window **and** price | 52/55 | 52/55 | **VERIFIED** |
| §2.3c ≥1 firm named | 55/55 | 55/55 | **VERIFIED** |
| §2.3c China manufacture | 49/55 | 49/55 | **VERIFIED** |
| §3.1 distinct firm strings | 64 | 64 | **VERIFIED** |
| §3.1 China in name | 33 | 33 | **VERIFIED** |
| §3.1 country tally | China49·US2·PH1·TW1·Cambodia1·Vietnam1·Mexico1·France1 | identical | **VERIFIED** |
| §3.1 non-US country | 53/55 | 53/55 | **VERIFIED** |
| §3.1 China % | 89.1% | 89.1% (49/55) | **VERIFIED** |
| §3.1 firm strings ending exactly ", of China" | **17** | **17** only if the count is restricted to Manufacturers+Importers (a 44-string universe); over the **same 64-string universe** the sentence's other two figures ("64 distinct", "33 carrying China") are drawn from, the true count is **32** | **CORRECTED** — the sentence silently mixes two different denominators |
| §3.1 "two firm strings quoted verbatim" | 2 | **1** — only "Changzhou Jiaxuan Intelligence Furniture Co., Ltd., of China" is quoted anywhere in the file, and it is accurate. No second quoted firm string exists in the text | **CORRECTED (premise)** — there is one quoted firm string, not two; the one that exists checks out |

## 2. The three named quotations (26596, 26659, 26637)

Only **26659** is actually quoted with an attributed record number anywhere in the motion (§1,
lines 38–39). **26596 and 26637 do not appear anywhere in ARTIST-REFORM-59.md** — no quote, no
record number, nothing to check. (They do surface in `analyse.py`'s own debug printout as other
records satisfying its destroy+photo regex — that is not the same as the motion asserting a quote
from them.)

The 26659 quote, checked character for character against the source: **verbatim as far as it
goes**, but silently truncated. The file's actual sentence is: *"Consumers will be asked to write
in permanent marker "RECALLED" on the hand warmer and submit a photo showing that marking **on the
hand warmer, the model number and the product's three-digit batch number to
https://www.ocoopa.com/pages/product-recalls.**"* The motion's quote stops at "that marking" with
a closing quotation mark and no ellipsis — unlike its own correct use of "…" elsewhere (§3.2, §4)
to mark a cut. **VERIFIED for the characters shown; the silent truncation should be flagged or
given an ellipsis.**

## 3. The étude record (§6)

Independently implementing the stated rule (`RecallDate` asc, then `RecallNumber` asc, first
`Remedies` match on `/stop using[^.]*immediately/i`) returns **RecallNumber 26591**, **0 records
skipped** — **VERIFIED**. "None reported" injuries, **237** units, **$30**, the retailer line, and
the full remedy text (including the stray `?` before `recalling@vevor.com`) all match the source
**character for character** — **VERIFIED**. Third-image caption artifact ("ecalled VEVOR Baby
Lounger…") — **VERIFIED**, present exactly as claimed.

**Budget.** `MANIFEST.json`'s five sha256s match the actual files in `observation/26591/` exactly.
100,760+80,844+66,119+48,532+108,747 = **405,002 — VERIFIED**. Base64 (five separate `data:` URIs,
as the étude builds them): actual **540,008 B / 527.35 KB**; motion states "≈540,003 B ≈527 KB" —
off by 5 bytes, immaterial under "≈" — **VERIFIED as an approximation**.

## 4. World claims, raw bytes

| Source | Claim | Result |
|---|---|---|
| CPSC Resale/Thrift page | HTTP 200, 62,147 bytes | **VERIFIED exactly** (curl, raw) |
| same | *"it is illegal to sell any recalled product"* | **VERIFIED exact** |
| same | *"It is unlawful to offer recalled products for sale under Section 19 of the Consumer Product Safety Act ( 15 U.S.C. § 2068 )."* | **CORRECTED** — raw bytes read `...Act (15 U.S.C. § 2068).` with **no spaces** inside the parentheses. The motion's spaces (`( 15`, `2068 )`) are not in the source — a fetch-tool-rendering artifact presented as raw-byte fact, the exact error VERIFIER-58 was written to catch |
| tarynsimon.com/works/contraband/ | HTTP 200, 26,443 bytes | **VERIFIED** — 26,443 is the *decompressed* body size (wire content-length is 5,425, gzip); both are legitimate, but a stranger re-running this must use `curl --compressed` |
| same | *"Contraband (2010) comprises 1,075 photographs…entering the United States from abroad."* | **VERIFIED exact** (an `<em>` tag splits "Contraband" from "(2010)" in the markup; visible characters are unaffected) |
| same | *"23 Archival Inkjet Prints in 4 Plexiglas boxes and Letraset on wall"* | **VERIFIED exact** |
| same | *"Anabolic Steroids (Illegal)"*, *"Animal Corpses (Prohibited)…"* | **VERIFIED exact**, ellipsis correctly marks a longer list |
| gagosian.com exhibition page | Beverly Hills, 22 Sept – 6 Nov 2010 | **VERIFIED** — page title reads "Taryn Simon: Contraband, Beverly Hills, September 22–November 6, 2010" |
| same | "on site 16–20 Nov 2009" | **UNVERIFIABLE / NOT SUPPORTED** — the raw page says only *"For five days in November 2009, Simon lived at John F Kennedy International Airport…"*. No day-range (16–20) appears anywhere in the page. The motion itself flagged this line as a fetch-tool rendering, not raw bytes; on inspection, the raw bytes do not contain it |
| `memory/decisions.md` | Row 13 quote, both fragments + "the team does not publish a pillory" | **VERIFIED exact** (ellipsis correctly marks the cut). "Row 13" = file line 13, which is correct — it is the table's 6th data row, but "row 13" naturally reads as the line number, and that is exact |
| CPSC permission restatement (§8) | *"copy and distribute recall notices"* | **VERIFIED** — unaltered substring of the wording VERIFIER-58 confirmed exact; not re-verified beyond that, per instruction |

## 5. Tier check

- **No design assertion found carrying a wrongful `[S]` mark.** §2.4 and §6 correctly split
  sourced content from imagined design within the same section.
- **§3.2 carries no tier mark at all** — it quotes a real, retrievable internal document
  (`memory/decisions.md`) and then rules on what it means for this work, with neither an `[S]` nor
  an `[I]` anywhere in the section. The quote should carry `[S]`.
- **§3.4 and §7** (the severed-reader test designs) carry no tier mark either, unlike §2/§3.3/§6
  which correctly tag their design content `[I]`. Minor inconsistency, not a factual error.
- **§5's claim** — "every premiered work of this house has been a screen apparatus" — is an
  unmarked factual claim (about the collective's own record, not a third party) with no citation.
- **Nothing found stating as fact something unknowable about an unbuilt room or a reader's future
  behavior** — §2's room claims are correctly scoped under its `[I]` header, and §8 explicitly
  names the room's untested perceptual premise as its own largest assumption. This is the
  discipline VERIFIER-58 asked for, and it is present.

## 6. Corrections to carry before a gate sits

1. §3.1: "17 firm strings…of China" → **32** (same 64-string universe as the sentence's other two
   numbers).
2. §1: "permanent marker…13/55" → **10/55** on a literal reading of the definition as printed; if
   the looser reading (13) is kept, say so explicitly and drop 26605 (its marking step is last, not
   first) or fix the ordering claim.
3. §1: "photograph…and email…27/55" → state as a range, **25–31/55**, or tighten the definition
   and recompute cleanly.
4. §3.1: "the two firm strings quoted verbatim" → there is **one**.
5. §2.4: the CPSC quotation's spacing — `(15 U.S.C. § 2068).` not `( 15 U.S.C. § 2068 )` — fix to
   match raw bytes.
6. §4: either drop "on site 16–20 Nov 2009" or re-source it; it is not on the cited page.
7. §1: the 26659 quote should either end at the true sentence break or take an ellipsis, matching
   the discipline already used elsewhere in the same document.
8. Tag §3.2's quote `[S]`.

*Verifier's pass complete, session 59, 2026-08-02. No vote on form cast or implied.*
