# VERIFIER — session 58, pass on ARTIST-PROPOSAL-58.md
*Verifier's remit: facts and tiers only. No vote on form. Retrieved 2026-08-02.*

## VERDICT: **PASS WITH CORRECTIONS**

The load-bearing legal claim (§4, THE PERMISSION) is **EXACT**, word for word, against the raw
bytes of the live page — the concept does not die here. The unit (§5) and the two news-release
titles (§9) are also **EXACT**. But the cadence numbers in §2/§3 — labelled "M2, verbatim in
substance" and treated as directly-sourced fact — are **wrong**, understating the true recall
counts on all three cited dates by 35–58%, because they were taken from a fetch-tool's rendering
of the JSON rather than the raw response. This is exactly the failure mode the motion's own
preamble warned about for quotations, but the same discipline was not applied to the numeric data.
The error does not weaken the concept — corrected, the "repeat" finding is *stronger*, not weaker
— but it must be fixed before anything with these numbers is printed. §15's open question about
image fields is resolved, and resolved in the concept's favor.

---

## 1. Claims table

| # | Claim (motion location) | Status | Note |
|---|---|---|---|
| 1a | "You may freely copy and distribute recall notices, including photographs of recalled items, without permission." (§4) | **EXACT** | Verified against raw HTML bytes of the live page, not just a tool rendering |
| 1b | "Any other use of photographs found in recall notices and elsewhere on CPSC websites may require permission from a copyright holder." (§4) | **EXACT** | Same paragraph, immediately following 1a |
| 1c | "Web page text, brochures, and posters presented on CPSC websites are public information. You may freely distribute, copy, or link to any of this information." (§4) | **EXACT** | Raw bytes confirm |
| 1d | "credit CPSC" / "in a way that states or implies CPSC endorsement" (§4) | **EXACT** | Both phrases appear verbatim in the surrounding sentence |
| 1e | Authoritative alternate page for this text | **CHECKED — none found** | Targeted search for the exact phrase returns only `https://www.cpsc.gov/About-CPSC/Policies-Statements-and-Directives/Privacy-Policy`; no other CPSC page carries this language |
| 2a | 2026-07-16, 2026-07-23, 2026-07-30 are all Thursdays (§3) | **EXACT** | Independently re-derived: 2026-01-01 = Thursday, day 211 = 2026-07-30 = Thursday, 2026-08-02 = Sunday |
| 2b | Counts: 9 / 6 / 10 recalls on those three dates (§2, §3) | **CORRECTED** | Actual: **14 / 7 / 15 recalls**. See §2 below |
| 2c | "three dressers, two pool drain covers, two portable bed rails, two toddler step stools" (§2) | **CORRECTED** | Actual, on the corrected full lists: **five dresser-type recalls**, two pool drain covers (confirmed), two portable bed rails (confirmed), **at least four step/tower-stool-type recalls**. The repeat is understated, not overstated |
| 2d | Thursday pattern is real over six months, not a 3-week artefact (§3, §11, §15) | **CONFIRMED, and stronger than claimed** | Every one of 26 consecutive Thursdays (2026-02-05 to 2026-07-30) carried at least one recall (4 to 27 recalls each) |
| 2e | Existence of "the hole" — a week with no recall dated (§3, §11) | **CORRECTED / NOT OBSERVED** | Zero such weeks occurred in the six-month window checked. The hole is the work's own premise, not yet an observed fact |
| 2f | Median / range of recalls per publication day | **NEW FINDING** | Across 29 distinct publication days (Feb–Aug 2026): median 10 recalls per publication day, range 1 to 27 recalls per publication day (the single-recall days are three off-Thursday anomalies, see 2g) |
| 2g | "Publication happens only on Thursdays" (implicit in §3, §11) | **CORRECTED, minor** | Three non-Thursday, single-recall dates occurred in the six-month window: 2026-02-04 (Wed), 2026-02-09 (Mon), 2026-02-24 (Tue), one recall each |
| 3 | JSON endpoint returns image URLs (§15, open question) | **RESOLVED — YES** | Field `Images`, an array of `{URL, Caption}` objects, hosted on `www.cpsc.gov/s3fs-public/*` (not `saferproducts.gov`). Example fetched successfully: `https://www.cpsc.gov/s3fs-public/Picture20_3.jpg` — HTTP 200, `content-type: image/jpeg`, 58,943 bytes |
| 4a | Recall Date: July 30, 2026 (§5) | **EXACT** | |
| 4b | Recall Number: 26-651 (§5) | **EXACT** | Page prints "Recall number: 26-651" |
| 4c | Name of Product: "Nordi Foldable Toddler Tower Stools" (§5) | **EXACT** | |
| 4d | Hazard quote: "...a risk of serious injury and death due to tip over, fall and entrapment hazards" (§5) | **EXACT** | Substring of the full sentence, verbatim |
| 4e | Remedy: Repair (§5) | **EXACT** | |
| 4f | Units: 47,166 (§5) | **EXACT** | |
| 4g | Incidents/Injuries: three reports, two injuries (§5) | **EXACT in substance** | Motion paraphrases (no quote marks used); raw text adds "including scrapes, cuts and bruises," which the motion omits but does not misstate |
| 4h | Sold At: Harppababy.com and Amazon.com, Sept 2023–June 2026, ~$130 (§5) | **EXACT in substance, label differs** | Page's actual field label is "Sold Online At:", not "Sold At:" — trivial, noted for completeness |
| 4i | Importer: HARPPA, Inc., Denver, Colorado (§5) | **EXACT in substance, label differs** | Page's actual field label is "Importer(s):" — trivial |
| 4j | Manufactured In: China (§5) | **EXACT** | |
| 4k | Consumer instruction: "Consumers should stop using the recalled stools immediately and store them away from children." (§5) | **EXACT** | Verified against raw HTML bytes |
| 4l | "Two product photographs" (§5) | **EXACT** | JSON `Images` array for RecallNumber 26651 contains exactly two entries |
| 5a | News release title/date: "Statement of Acting Chairman Peter A. Feldman Regarding the Supreme Court's Decision in Trump v. Slaughter", June 29, 2026 (§9) | **EXACT** | Verified in raw HTML of the News Releases index; date shown as "June 29, 2026" |
| 5b | News release title/date: "CPSC Exercises Section 12 Imminent Hazard Authority for First Time in Nearly 40 Years, Warns Consumers to Stop Using Lakkzoom Immersion Water Heaters", July 22, 2026 (§9) | **EXACT** | Verified in raw HTML; date shown as "July 22, 2026" |
| 6 | `frankbueltge.de/headroom` returns 403 to the plain fetcher (§13, §15) | **CONFIRMED** | Plain WebFetch returns "The server returned HTTP 403 Forbidden." A raw curl through the proxy stalled after the TLS Certificate step rather than confirming a clean 403, so this is confirmed via the fetch tool, not independently via curl — consistent with, not contradicting, the motion's account |

---

## 2. The cadence, corrected — full numbers

Fetched directly (raw JSON, via curl, bypassing any summarizing tool) from
`https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2026-07-01&RecallDateEnd=2026-08-02`
— **the same endpoint and the same date-range parameters the motion itself cites as M2** — twice,
independently, with identical results both times:

| date | motion's claimed count | actual count (verified) | recalls missing from the motion's list |
|---|---|---|---|
| 2026-07-16 | 9 recalls | **14 recalls** | 5: Oitnlaughter Projecting Finger Light Toys · Panasonic Electric Toaster Ovens · SDADI Kitchen Step Stools · Wade Logan Annyka 9-Drawer Fabric Dressers · Warren James Copper Cup (Flashgitz Relic Lunch Boxes) |
| 2026-07-23 | 6 recalls | **7 recalls** | 1: CuddleCubs Creations Teething Toy Sets |
| 2026-07-30 | 10 recalls | **15 recalls** | 5: Mangohood Direct Kids Kitchen Standing Towers · Mommy's Baby Lovely Deluxe Baby Doll Playsets · Cpzzkq Baby Loungers Expanded · Trsmima Zipline Kits and Zipline Spring Brakes · Woodure Toddler Kitchen Step Stools |

11 recalls across three dates (36 actual vs. 25 claimed) are missing from the motion's account.
Every recall the motion *did* list is confirmed present and correctly attributed to its date — the
error is one of **omission**, not fabrication: the fetch tool that rendered M2 for the Artist
undercounted, it did not invent.

**Widened window — six months, 2026-02-01 to 2026-08-02, 306 recall records, 29 distinct
publication days:**

- **(a) Is the Thursday pattern real over six months, or a three-week artefact?** It is real, and
  stronger than the motion's evidence suggested. Every one of the **26 consecutive Thursdays**
  from 2026-02-05 through 2026-07-30 carried at least one recall — a range of 4 to 27 recalls per
  Thursday. Three additional, isolated single-recall dates fell on non-Thursdays in the same
  window (2026-02-04, a Wednesday; 2026-02-09, a Monday; 2026-02-24, a Tuesday; one recall each).
  So the cadence is a strong, repeated weekly pattern with rare single-item exceptions — not an
  artefact of the three-week window the motion sampled.
- **(b) How many weeks had no recall dated at all — the "hole" the work depends on?** **Zero**, in
  the 26 weeks checked. The hole that §3 and §11 treat as the normal, expected state of the channel
  did not occur even once across six months of the Commission's actual publication record. This is
  a correction against the motion's own premise, not a confirmation of it: the "hole" is presently
  a hypothetical the rule (§7) must handle, not an observed fact about this channel's behavior.
- **(c) Median and range of recalls per publication day.** Across the 29 distinct publication days
  in the six-month window, the median is **10 recalls per publication day**, and the range is
  **1 recall to 27 recalls per publication day** (the single-recall days are the three non-Thursday
  anomalies above). Restricted to the 26 Thursdays only, the median is 10.5 recalls per Thursday,
  with a range of 4 to 27 recalls per Thursday.

**Consequence for §2's "repeat" claim.** With the corrected, complete lists, the true repetition is
undercounted, not overstated, by the motion: dresser-type recalls across the three dates number
**five** (12-Drawer Fabric Dressers, EnHomee 9-Drawer Fabric Dressers, Wade Logan Annyka 9-Drawer
Fabric Dressers, 15-Drawer Dressers, 5-Drawer Dressers), not three; toddler/kitchen step-stool-type
recalls number at least **four** (Boon PIVOT, SDADI Kitchen Step Stools, HARPPA Nordi, Woodure
Toddler Kitchen Step Stools — Mangohood Kids Kitchen Standing Towers is a fifth, arguable case), not
two. Pool drain covers (two) and portable bed rails (two) are confirmed exactly as stated.

---

## 3. Image fields — full answer to §15's open question

The JSON record for each recall carries an `Images` field: an array of objects, each with a `URL`
and a `Caption`. Example, from RecallNumber 26651 (the Nordi Toddler Tower Stools, §5's unit):

```json
[
  {"URL": "https://www.cpsc.gov/s3fs-public/Picture20_3.jpg",
   "Caption": "Recalled HARPPA Nordi Foldable Toddler Towers - model HANS0002"},
  {"URL": "https://www.cpsc.gov/s3fs-public/Picture21_3.jpg",
   "Caption": "Recalled HARPPA Nordi Foldable Toddler Towers (model number HANS0002 on label under platform)"}
]
```

`https://www.cpsc.gov/s3fs-public/Picture20_3.jpg` was fetched directly and returned **HTTP 200**,
`content-type: image/jpeg`, `content-length: 58943` bytes, served from Amazon S3 behind
`www.cpsc.gov` — not `saferproducts.gov`. This settles §15's open question: the ingest does **not**
need to scrape the HTML notice pages for images; the API record itself carries them, on a
predictable host, at a resolvable URL. This is better news for the concept's build plan (§7) than
the motion assumed.

---

## 4. Tier check

- **The most significant tier-boundary problem is the one described above**: §2's M2 figures were
  presented as "verbatim in substance" — i.e., as directly-sourced, SOURCED-tier fact — but were in
  fact a fetch-tool's summarization of the JSON, not a reading of the raw response. The motion's own
  preamble commits to exactly this discipline for *quotations* ("Where a quotation is a fetch-tool's
  rendering of a page rather than my own reading of the raw bytes, I say so") but did not extend it
  to the numeric/count data drawn from the same tool call. The corrected numbers do not change the
  concept's viability — if anything they strengthen §2's "repeat" observation — but the figures as
  printed are wrong and the SOURCED label on them was not earned by the process the motion itself
  requires.
- **An unmarked speculative claim**: §3's "the next expected publication day is Thursday
  2026-08-06 — four days from now, inside this season, with six to ten units on it" states a
  specific numeric range as if derived from evidence. It is not marked as a projection/estimate the
  way §10's rehearsal stills are marked IMAGINED, and on the corrected six-month data (Thursdays
  range 4–27 recalls, median 10.5) "six to ten" is not a well-supported prediction — it is simply
  the motion's own (already-incorrect) three-week sample restated as a forecast. This should either
  be struck or explicitly marked as a low-confidence guess.
- **Correctly marked speculation**: §10's Cell N rehearsal stills are marked IMAGINED and dated
  before the first unit, as the house's staging condition requires. §13's "failed products
  collection" neighbour is explicitly flagged by the motion itself as "named from genre, not from a
  source I retrieved tonight" — correct self-discipline, and it is properly listed in §15 as needing
  a URL or a strike before the gate.
- **Boundaries between retrieved / tool-rendered / reasoned are otherwise clean.** §4 and §5
  explicitly flag themselves as fetch-tool renderings pending Verifier check (now closed, both
  EXACT). §9 explicitly disclaims any assertion about the two news releases' contents, checking only
  titles and dates — the motion is right to say nothing more, and I said nothing more.
- No other unmarked IMAGINED material found in the sections reviewed.

---

## 5. What I could not check, and why

- **Whether CPSC considers a 200-notice standing room "distributing recall notices" or "any other
  use."** Not checkable from a desk — requires an answer from CPSC itself, exactly as §14 already
  states. Not checked.
- **The contents of the *Trump v. Slaughter* decision or the Section 12 release.** Out of scope by
  the task's own instruction — only titles and dates were to be confirmed, and both are exact.
- **Alarm Phone's faster channels (social, WatchTheMed)**, cited in §12/§15 as unretrieved by the
  Artist. Not checked — outside this pass's assigned scope (§12's runner-up reasoning carries no
  vote-bearing claim this pass was asked to verify) and would draw on the shared extraction budget
  for a non-load-bearing question.
- **The "failed products collection" neighbour** (§13) — not retrieved by the Artist and not
  retrieved by me; it remains unverified and, per the motion's own §15, must be given a URL or
  struck before the gate.
- **Whether any existing artwork already uses this exact channel** (§15's last open item) — an
  adjacency search was not run; out of this pass's assigned scope.
- **`frankbueltge.de/headroom`** — confirmed 403 via the plain fetcher (WebFetch), consistent with
  the motion's account; a raw curl through the proxy did not complete cleanly (stalled after the TLS
  Certificate step) so it does not independently corroborate the 403, but it does not contradict it
  either. Not further pursued; peripheral to this pass's five assigned checks.
- **M1** (`cpsc.gov/Recalls` listing page) and the rest of **M5** (news release index beyond the two
  cited dates) were not independently re-verified beyond what §5's checks above required.

---

*Verifier's pass complete, session 58, 2026-08-02. No vote on form cast or implied.*
