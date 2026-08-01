# VERIFIER'S REPORT — session 57, 2026-08-01

*Facts and tiers only. No vote on form. All fetches direct via `curl` from this session, cached to
scratch, dated 2026-08-01 throughout — no fetch in this report is more than a few hours old at time
of writing.*

---

## VERDICT: **PASS WITH CORRECTIONS**

The work's substantive legal-hygiene finding — *an empty response slot on a report page is not
evidence of non-response* — **holds** when the test is re-run properly, and holds at almost exactly
the ratio the Artist reported (94.6% vs. the Artist's claimed 94.1%). But the **population of 34
report pages the Artist's proposal cites is not reproducible** from the committed listing JSON under
the rule as stated; the reproducible population is **111**, matching the conductor's own
re-derivation exactly. This is a correction the Artist's proposal must carry, not a silent patch — the
finding survives, the stated sample size does not. Two further corrections: the intended face text
*"«Recipient» is under a duty to respond to this report on the prevention of future deaths, namely by
«date»"* (`STAGING-RULING-56.md`) **misquotes the state's actual wording** in three separate ways and
must not be printed as the state's words without revision; and a shortened form of the "no power"
quotation ending at "take any steps" is **misleading** if used alone. Item 3 (source fidelity) holds
in full — all 49 rows, all four period/publish strings, and the feed's newest entry all confirmed
byte-for-byte against fresh fetches, with one cosmetic parsing note recorded below (not a data error).

---

## ITEM 1 — THE RESPONSE-SLOT TEST, RE-RUN

### 1.1 Reproducing the population of 34

**Rule as stated** in `ARTIST-PROPOSAL-56.md` §9 (the sentence beginning *"And the work never infers
non-response..."*): take every record in `data/pfd-listing-200-2026-08-01.json` with a non-null
`report_date` (format `DD/MM/YYYY`); compute `due = report_date + 56 days`; select records where
`67 ≤ (2026-08-01 − due).days ≤ 197`.

Applied mechanically, in Python, against the committed JSON as it stands today:

```
non-null report_date records: 156 of 200
population under the stated rule: 111
```

**111, not 34.** This matches the conductor's own independent re-derivation cited in the brief
exactly. I tried several nearby variants of the window in case a shifted or narrower interval was
what had actually been run (`97–197` → 46, `127–197` → 6, `67–167` → 107, `150–197` → 6, `170–197` →
4, `97–167` → 42, `67–100` → 72) — **none produces 34**, and none is close enough to look like a
transcription slip of the stated `67–197`. I did not go further than this; per instruction, I am not
guessing at what the Artist actually did.

**Finding, not failure, stated plainly: the population of 34 in `ARTIST-PROPOSAL-56.md` §9 cannot be
reproduced from the committed data under the rule as stated. What is missing is the Artist's actual
selection method — it is not recorded anywhere retrievable, and I have not invented one.** The
figure may be a hand-count from an earlier or different snapshot, a different due-date convention, or
an error; there is no way to tell from what is committed, and the file that states the rule does not
show its working.

### 1.2 Running the test properly, on the reproducible population (n = 111)

**Detection rule, stated verbatim for a third hand to re-run:** I fetched three report pages first
(Rebekah Arter, Peter Campbell, Timothy Reading) to establish the markup. Each report page carries a
`<div class="related-content__downloads">` block, headed by an `<h2 id="related_content">Related
content</h2>`, containing one `<li class="related-content__item">` per attached document, each with a
`<span class="related-content__filename">…</span>`. Response documents are consistently named either
`Response from <body>` or `<ref> - Response from <body>` (observed variants also include a bare
`Response <body>` with no "from", e.g. "Response Ordnance Survey"). **Rule applied mechanically to all
111 pages: a page carries at least one published response if any `related-content__filename` span on
that page contains the substring `"response"`, case-insensitive.** I checked the same 111 pages for a
`"reply"`-without-`"response"` variant that this rule would miss — none exists in the sample. Some
`related-content__item` entries are entirely empty placeholders (no link, no filename) — these do not
count as a response and were not miscounted as one in either direction.

**Fetch:** all 111 population URLs fetched by direct `curl`, 1-second delay between requests, cached
to scratch (`pages111/`). **111 of 111 succeeded (HTTP 200), zero failures.**

**Result:**

| | count | of 111 |
|---|---|---|
| pages with ≥1 published response | **105** | 94.6% |
| pages with none | **6** | 5.4% |

This is close to the Artist's claimed ratio (32/34 = 94.1% with, 2/34 = 5.9% without) even though the
population itself does not match — the *substantive* finding replicates on an entirely different,
independently-derived sample five times its size.

### 1.3 The six without a published response, checked against the 49-row non-response table

| deceased | URL | on the 49-row list? |
|---|---|---|
| [REDACTED] (ref 2026-0178, Fiona Wilcox, Inner West London) | `https://www.judiciary.uk/prevention-of-future-death-reports/2026-0178/` | **No** |
| Barry Harmer (ref 2026-0203) | `https://www.judiciary.uk/prevention-of-future-death-reports/barry-harmer-prevention-of-future-deaths-report/` | **No** |
| John Tarrant (ref 2026-0199) | `https://www.judiciary.uk/prevention-of-future-death-reports/john-tarrant-prevention-of-future-deaths-report/` | **No** |
| Thomas Ruggiero — page (1) only (ref 2026-0170; the (2) and (3) report pages for the same name each carry a response and are correctly counted "YES" above) | `https://www.judiciary.uk/prevention-of-future-death-reports/thomas-ruggiero-1-prevention-of-future-deaths-report/` | **No** |
| John Loannou (listed "John Loannou," page title "John Ioannou" — ref 2026-0137) | `https://www.judiciary.uk/prevention-of-future-death-reports/john-loannou-prevention-of-future-deaths-report/` | **No** |
| Susan Samson — the earlier of two same-named report pages (ref 2026-0120; the other Susan Samson page, ref differs, carries a response and is counted "YES" above) | `https://www.judiciary.uk/prevention-of-future-death-reports/susan-samson-prevention-of-future-deaths-report-2/` | **No** |

Checked by exact and substring match (case-insensitive) against all 49 names in
`data/nonresponse-tables-2026-08-01.json`. **None of the six appears on the list, in any of the four
tables.** (Full name list re-derived from the committed JSON for this check; see §3 below for its own
fidelity check against a fresh fetch.)

### 1.4 Conclusion

**The evidence supports:** on a reproducible population of 111 report pages whose 56-day response
window closed between 67 and 197 days before 2026-08-01, 6 (5.4%) carry no published response on the
page itself, and none of those 6 appears on the Chief Coroner's own published non-response list —
so an empty response slot on a report page is not, by itself, evidence that the recipient failed to
respond within the statutory framework the Chief Coroner tracks.

**The evidence does NOT support:** any claim about *why* those 6 pages carry no visible response
(late-but-arriving response not yet re-published, an extension granted, a response held elsewhere, or
a genuine gap in the state's own publishing pipeline are all left open — I did not investigate
further, and neither did the Artist's claim). It also does not support the specific figures "34 / 32 /
2" as printed in `ARTIST-PROPOSAL-56.md` §9 — those numbers are not reproducible from the committed
data and must be corrected or the method behind them recovered and shown.

---

## ITEM 2 — THE TWO QUOTATIONS

### 2(a) The duty sentence

**Fetched:** `https://www.judiciary.uk/prevention-of-future-death-reports/najib-naagi-prevention-of-future-deaths-report/`
(2026-08-01). Duty sentence, verbatim, character for character (source has a double space before "I,"
— preserved):

> "You are under a duty to respond to this report within 56 days of the date of this report, namely by
> 13 July 2026.  I, the coroner, may extend the period if an appropriate application is made."

**The phrase "this report on the prevention of future deaths" does not appear anywhere on the page.**
The duty sentence says only **"this report."** The fuller description ("Prevention of future deaths
report") exists elsewhere on the page — in the page title, the `<h1>`, and the table heading "Report
to Prevent Future Deaths" — but not inside the duty clause itself. I searched the full raw HTML of all
four sampled report pages (Naagi plus the three below) for the literal string "this report on the
prevention of future deaths" — **found in none of them.**

**The studio's intended face text** (`STAGING-RULING-56.md` lines 49 and 315): *"«Recipient» is under
a duty to respond to this report on the prevention of future deaths, namely by «date»."* **This
construction is NOT faithful to the state's wording, in three separate respects:**

1. **Person.** The state addresses the recipient directly, second person ("**You** are under a duty
   …"). The studio's construction recasts this in the third person, naming the recipient ("«Recipient»
   is under a duty …"). This is not what the sentence says; every sampled page confirms "You," never
   the recipient's name, inside the duty clause.
2. **The inserted phrase.** "on the prevention of future deaths" is not part of the duty sentence on
   any page checked; it does not exist as spoken text there at all.
3. **The dropped clause.** The state's sentence pins the 56 days into the clause itself — "**within 56
   days of the date of this report**, namely by [date]." The studio's construction drops this clause
   entirely, going straight from "respond to this report" to ", namely by «date»" — which, read on its
   own, no longer explains what "namely by" is namely-by *of*.

**The state's exact wording** (from Naagi, reproducible on any report page): *"You are under a duty to
respond to this report within 56 days of the date of this report, namely by [date]. I, the coroner,
may extend the period if an appropriate application is made."*

**Wording across coroner areas — fetched for comparison** (2026-08-01):

| page | area | wording |
|---|---|---|
| Beryl Dandridge | Oxfordshire | `https://www.judiciary.uk/prevention-of-future-death-reports/beryl-dandridge-prevention-of-future-deaths-report/` — core sentence identical, but **omits** "if an appropriate application is made": "…namely by **6 August 2024**. I, the coroner, may extend the period. " |
| Trevor Evans | Carmarthenshire and Pembrokeshire | `https://www.judiciary.uk/prevention-of-future-death-reports/trevor-evans-prevention-of-future-deaths-report/` — date given with an HTML superscript ordinal: "namely by 6`<sup>`th`</sup>` July 2026," and a doubled space before "appropriate" |
| Elsie Jones | Birmingham and Solihull | `https://www.judiciary.uk/prevention-of-future-death-reports/elsie-jones-prevention-of-future-deaths-report/` — core sentence identical, full clause present, only the date is bolded |

**Variation found:** the core sentence text and word order are standard across all four areas
sampled; what varies is (i) whether the closing clause "if an appropriate application is made" is
present at all (Dandridge drops it), (ii) inline formatting — bold spans around the date and/or "56
days," an HTML ordinal superscript on the day number, stray double-spacing — none of which changes
the words. No page in the sample used any construction resembling the studio's intended third-person
face text.

### 2(b) The absence of enforcement

**Fetched:** `https://www.judiciary.uk/guidance-and-resources/chapter-16-reports-to-prevent-future-deaths-pfds/`
(2026-08-01). The passage, verbatim, with its full surrounding sentence (paragraph 47 in full, under
the heading "Absent or inadequate reply to a PFD report"):

> "47. Just as there is no power in the Regulations to withdraw a PFD report, there is no power
> authorising a coroner to take any steps if they receive an inadequate or vague reply. Once the PFD
> report has been sent out the coroner will have completed their functions in respect of that report
> and no longer has a mandate to take any further steps. Where no reply is received or an inadequate
> response is made a coroner would exceed their powers if they chased a missing reply or requested
> additional detail in respect of an inadequate response."

The studio's citation in `ARTIST-PROPOSAL-56.md` table (§8, line 141) reads: *"no power authorising a
coroner to take any steps"* — **truncated exactly at "take any steps," dropping the conditional clause
"if they receive an inadequate or vague reply."**

**A shortened form ending at "take any steps" is misleading in context.** Cut there, the sentence
reads as an unqualified claim that a coroner has no power to do *anything at all* once a report is
sent — but paragraph 47's own second sentence, and paragraphs 48–50 (also on this page, not re-quoted
here in full), show the coroner *does* retain some powers: to write and inform the bereaved that a
recipient is "now in breach of Reg 29(3) and Schedule 5 part 7(2)" (§48), and to forward an inadequate
reply to "another person who may find it useful or of interest" (§50). The clipped form erases the
distinction the source itself draws between *"no power to compel or chase a response"* and *"some
narrow residual powers of notification."* The truncation used in the table entry is a shorthand label
inside a tier-audit table, not text printed on the work's face — but if it is ever lifted onto the
face as a quotation, it must not stop at "take any steps."

**Shortest faithful printable form** (a complete independent clause, nothing dropped that changes the
scope): *"there is no power authorising a coroner to take any steps if they receive an inadequate or
vague reply."* This is exactly the form already used correctly in `MATERIAL-2026-08-01.md` §1 (joined
by ellipsis to paragraph 48's "no authority in law to take any further steps," previously checked and
passed by `VERIFIER-56.md`). The table-entry shorthand in `ARTIST-PROPOSAL-56.md` §8 is the one place
in the current file set where the truncated form appears without qualification, presented inside
quotation marks as if verbatim.

---

## ITEM 3 — IS THE SOURCE STILL AS RECORDED?

**Fetched:** `https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/`
(2026-08-01).

- **Table count:** 4 `<table>` elements — matches.
- **Row counts:** 3, 9, 12, 25 data rows (4, 10, 13, 26 `<tr>` including header row in each) —
  matches the committed JSON exactly.
- **Period / publish strings**, extracted from the live page's own lead-in sentences and compared to
  the committed `period`/`published` fields — **all four match exactly**:
  - "13 December 2025 – 14 June 2026. Published 30 June 2026."
  - "14 June 2025 – 12 December 2025. Published 31 Dec 2025."
  - "14 December 2024 – 13 June 2025. Published 30 June 2025."
  - "1 January 2024 – 13 December 2024. Published 31 Dec 2024."
- **All 49 rows, cell by cell:** parsed the live page's raw table HTML and diffed every cell against
  the committed JSON. **Zero mismatches** once HTML `<br>` line-breaks and `&nbsp;` entities are
  normalized to a single space on both sides (a first, naive pass showed two apparent "mismatches" —
  both were artifacts of my own extraction script mishandling a `<br>` in "Hampshire, Portsmouth<br>and
  Southampton" and an `&nbsp;` in "Barts Health NHS Foundation&nbsp;Trust"; re-parsing correctly showed
  the committed JSON is in fact **byte-for-byte faithful to the source**, including preserving the
  literal non-breaking space `\xa0` in "Foundation\xa0Trust" and the source's own typo "Graeme lrvine"
  — lower-case L, not capital I — rather than silently correcting it. This is a good sign for the
  committed data's fidelity, not a finding against it.).
- **Spot-checked three rows character for character** as instructed (Samuel Vass; Anthony Wood; Dave
  Onawelo, chosen from tables 1, 2 and 4 respectively) — all three match the committed JSON exactly,
  including the "Graeme lrvine" typo on the Onawelo row.

**No drift found.** The page as fetched today is identical, in every table, every row and every
metadata string, to what is committed in `data/nonresponse-tables-2026-08-01.json`.

**Fetched:** `https://www.judiciary.uk/prevention-of-future-death-reports/feed/` (2026-08-01). Newest
entry:

- **Title:** "Catherine Morgan – Prevention of future deaths report"
- **`<published>`:** 2026-07-28T17:08:44Z
- **`<updated>`:** 2026-07-29T10:48:18Z
- Feed-level `<updated>`: 2026-07-29T10:49:02Z

This is consistent with `pfd-listing-200-2026-08-01.json`'s newest listing entry (Catherine Morgan,
published "July 28, 2026").

---

## RETRIEVAL LEDGER

All fetches direct `curl`, this session, 2026-08-01, ≥1 second between requests, cached to
`/tmp/claude-0/-home-user-studio/a46cebac-f70d-5f97-9513-50d8d85662d5/scratchpad/`.

| URL | used for |
|---|---|
| 111 individual report pages, the full reproducible Item-1 population (list of all 111 URLs and per-page result recorded in scratch file `item1_population_results.tsv`; full derivation script in scratch) | Item 1.2–1.3 — response-slot detection |
| `https://www.judiciary.uk/prevention-of-future-death-reports/najib-naagi-prevention-of-future-deaths-report/` | Item 2(a) — duty sentence, primary sample |
| `https://www.judiciary.uk/prevention-of-future-death-reports/beryl-dandridge-prevention-of-future-deaths-report/` | Item 2(a) — wording variation, Oxfordshire |
| `https://www.judiciary.uk/prevention-of-future-death-reports/trevor-evans-prevention-of-future-deaths-report/` | Item 2(a) — wording variation, Carmarthenshire and Pembrokeshire |
| `https://www.judiciary.uk/prevention-of-future-death-reports/elsie-jones-prevention-of-future-deaths-report/` | Item 2(a) — wording variation, Birmingham and Solihull |
| `https://www.judiciary.uk/guidance-and-resources/chapter-16-reports-to-prevent-future-deaths-pfds/` | Item 2(b) — the enforcement passage, paragraph 47 in full |
| `https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/` | Item 3 — table/row fidelity check |
| `https://www.judiciary.uk/prevention-of-future-death-reports/feed/` | Item 3 — newest feed entry |

**Data files used, not re-committed:** `data/pfd-listing-200-2026-08-01.json` (200 records, as
committed); `data/nonresponse-tables-2026-08-01.json` (49 rows, as committed) — both consulted for
Item 1's population derivation and Item 3's fidelity check respectively.

---

## SUMMARY OF REQUIRED CORRECTIONS

1. **`ARTIST-PROPOSAL-56.md` §9:** the population "34 report pages… 32 carry… 2 do not" is not
   reproducible from the committed data under the stated rule. The reproducible population under that
   rule is **111** (105 with a response, 6 without, ratio 94.6%/5.4% — both numbers close to, but not
   identical to, the claim). Either the method must be shown and corrected, or the sentence must be
   restated against the reproducible population and figures given here. **The underlying finding —
   empty slot ≠ non-response, and none of the without-response pages appear on the 49-row list —
   survives the correction and is independently confirmed on the larger sample.**
2. **`STAGING-RULING-56.md`, lines 49 and 315:** the face-text construction *"«Recipient» is under a
   duty to respond to this report on the prevention of future deaths, namely by «date»"* is not the
   state's wording. If the work's claim to print "the state's own words and nothing else" is to hold,
   this line needs to become either the state's actual second-person sentence with the recipient named
   separately, or be explicitly marked as a paraphrase, not the state's construction.
3. **`ARTIST-PROPOSAL-56.md` §8, line 141:** the quotation `"no power authorising a coroner to take any
   steps"` is a truncation that changes the sense if read alone. Extend to `"…if they receive an
   inadequate or vague reply"` wherever this is used as a quotation rather than a shorthand label.

Everything else checked in this pass — all 111 fetches, all four §3 tables and their metadata, the
feed's newest entry — holds exactly.
