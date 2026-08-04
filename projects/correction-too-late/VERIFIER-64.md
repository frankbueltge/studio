# THE VERIFIER'S PASS — session 64, 2026-08-04

*Run last, blocking on labels only. Every fetch below was made first-hand tonight, 2026-08-04, with
`curl`/`python3`, independent of any figure printed in the five files under review. Where I quote "the
table," I mean the address table appended tonight to `CONDUCTOR-VERIFICATION-64.md`.*

## VERDICT: **BLOCKING**

The single check named as the most important thing to do tonight — re-running the repository-wide
search and checking that its printed table of addresses is complete and correct — **fails**. The table
appended to `CONDUCTOR-VERIFICATION-64.md` tonight, and the journal's restatement of its result, print
line numbers that do not contain the text they are cited for, and a summary of "other hits" that does
not match a re-run of the same search terms. Every other figure I re-derived tonight — the OpenAlex
count, the CFR code count, both Kritiker quotations, the FCC footnotes and timeline, the Massachusetts
and PNAS figures — reproduced exactly. The defect is narrow but it sits exactly where the house asked me
to look hardest, and it is a false claim as printed, so the pass blocks.

---

## FINDINGS

### 1. (BLOCKING) The correction banner's address table cites wrong line numbers for its own file

`projects/correction-too-late/CONDUCTOR-VERIFICATION-64.md`, line 32, claims:

> `CONDUCTOR-VERIFICATION-64.md` (this file) | **33, 42, 100** | *"none of the 57 means…"*, *"there is no
> event code whose meaning is that a previous alert was wrong"*, *"not one of them means 'that was
> wrong'"*

I checked all three addresses directly in the file as it stands (a stranger's own view, `sed -n
'33p;42p;100p'`):
- **Line 33** is the *next row of the same table* (the `ARTIST-64.md` row) — not a superseded claim.
- **Line 42** is the opening of the file's original attribution paragraph ("*Run by the conductor after
  the Artist's ruling landed…*") — not a superseded claim.
- **Line 100** is a **blank line**.

The three sentences actually quoted in the table live at **lines 72, 85 and 155** of the same file (I
grepped for the literal strings and confirmed by hand):
- line 72: *"none of the 57 means cancellation, correction, all-clear, retraction…"*
- line 85: *"there is no event code whose meaning is that a previous alert was wrong."*
- line 155: *"…not one of them means 'that was wrong.'"*

All three of the real locations **are** correctly marked with an adjacent `↑ SUPERSEDED` marker (lines
75, 86 and the bracketed note starting at 147), so no reader following the prose would be misled — the
discharge mechanism itself works. But the printed table, which is the part explicitly offered as
"re-runnable by a stranger," points nowhere near the claims it names. **Owed:** correct the three line
numbers in the table (72, 85, 155, not 33, 42, 100).

### 2. (BLOCKING) The same table's line numbers for `ARTIST-64.md` are also wrong, and undercount the true occurrences

Table row 2 (line 33): `ARTIST-64.md` | **53, 73, 276, 278, 291, 434** | "the finding in its six
statements, incl. *'none of them is a correction'*".

Checked directly (`sed -n '53p;73p;276p;278p;291p;434p'` on `ARTIST-64.md`):
- line 53 — a sentence about the material bar's evidence/subject rule; unrelated.
- line 73 — "…that entered several hundred thousand bodies on a Saturday morning." — unrelated.
- line 276 — a comparison to *Recovery*; unrelated.
- line 278 — a comparison to *NO PART*; unrelated.
- line 291 — a **blank line**.
- line 434 — a comparison to *THE ROOM*'s kill; unrelated.

None of the six cited lines contains the finding or the phrase "none of them is a correction." A
case-sensitive search of the actual file for `fifty-nine` and `none of them is a correction` returns
**at least twelve** distinct lines carrying the claim (81, 101, 177, 188, 204, 231, 287, 303–304, 344,
401, 455, 462) — double the number the table asserts. The document is killed and carries a blanket
disclaimer at its head, so no reader is misled about its live status; but the specific address list, like
row 1's, does not correspond to the file as it exists, and understates how pervasive the superseded
finding is inside it. **Owed:** either replace the six addresses with a correct and complete list, or
say plainly that the file is superseded in full and drop the pretense of a specific address list.

### 3. (Corrections owed) The table's own summary of "every other hit" does not match a re-run of its search terms

The banner (`CONDUCTOR-VERIFICATION-64.md`, lines 26–27, 35–38) states the search ran for `none of the
57` · `not one of the` · `no code` · `fifty-nine` · `none of them is a correction` across all `*.md`, and
that everything outside the two named files is "`WORKBOARD.md` 938/1074, five journal entries, four
project files, `memory/`" — a different claim in every case.

Re-running the same five terms verbatim across the whole repository tonight (`grep -rn` for each term,
excluding `projects/correction-too-late/` and tonight's own journal entry, which correctly historicises
the claim) returns:
- **`WORKBOARD.md`** — 2 lines (938, 1074) — matches.
- **Journal entries** — `journal/2026-07-31-session-55.md` and `journal/2026-08-01.md` — **two**, not
  "five."
- **Project files** — `projects/cpsc-recall-channel/STAGING-RULING-62.md`,
  `projects/pfd-channel/ARTIST-ANSWER-56.md`, `ARTIST-PROPOSAL-56.md`, `CONDUCTOR-CHECK-56.md`,
  `STAGING-RULING-57.md`, `STAGING-RULING-56.md` — **six**, not "four."
- `memory/discarded.md` — one hit — matches "`memory/`."

I opened every one of these and confirmed each is genuinely a different claim about a different subject
(overdue-project counts, `pfd-channel` panel results, an unrelated "fifty-nine per cent of every
sentence" figure), so **none of them is owed a correction** — that part of the banner's conclusion holds.
But the printed inventory of where those unrelated hits sit is wrong on two of its four counts, so a
stranger re-running the search to audit the audit gets a different tally than the one printed.

### 4. (Corrections owed) One of the three quoted "superseded" sentences would not be found by the search terms as literally stated

The sentence attributed to line 85 (real location) — *"there is no event code whose meaning is that a
previous alert was wrong"* — contains none of the five listed search strings as a literal substring
(`no event code` is not `no code`; the phrase contains none of the other four terms either). A stranger
who ran exactly the search described would not recover this sentence by that route. It is nonetheless a
real superseded sentence and is correctly marked in the prose — but the printed methodology and the
printed result do not cohere for this address. **Owed:** either add the term that actually catches this
sentence (e.g. `no event code`) to the printed search list, or note that this address was found by
reading rather than by the listed strings.

### 5. (Corrections owed) `WORKBOARD.md`'s appended note mischaracterises which deliverables were discharged

`WORKBOARD.md`, line 72 (the session-64 appendix to "THE STATE OF THE HOUSE"): *"deliverables 3, 4 and 5
were owed only by a **sound** proposal, and the sound proposal is dead, so they fall with it."*

The five deliverables, as adopted and printed in `REQUESTS.md` ("What the concept phase must deliver…"),
are: (1) the printed corpus ranking; (2) the count at concept; (3) *the gating instrument for a sound
work*; (4) *a pre-registered severed count of what a listener who is asked for nothing carries away* —
no mention of sound in its own text; (5) the sound-vs-non-sound restitution check. Deliverable 4's own
wording is medium-neutral, and `DRAMATURG-64.md` — the surviving, non-sound proposal — explicitly
self-labels its §3 **"THE PRE-REGISTERED SEVERED COUNT (deliverable 4, owed at concept)"** and discharges
it in full (a five-strangers-per-cell severed panel design with four pre-registered thresholds). So
deliverable 4 did **not** fall with the sound proposal — it was delivered, tonight, by the work that
opened. Only deliverables 3 and 5 are sound-specific and correctly described as dead with it. **Owed:** a
correction narrowing the claim to "deliverables 3 and 5," since 4 is live and discharged.

This is outside the six files named for tonight's pass (it is in `WORKBOARD.md`, read as background), but
it is a fact-and-discharge claim made the same night about the same project, so I record it here rather
than let it stand uncaught.

### 6. (Minor, corrections owed) The ground count in `KRITIKER-GATE-64.md` §3 is internally inconsistent, and the journal repeats the undercount

`KRITIKER-GATE-64.md`, line 175: *"The count is ground 1. There are **five more**, and three of them
would kill on their own."* The section that follows is headed `### Ground 2` … `### Ground 7` — **six**
headed grounds, not five. Total grounds against the Artist's proposal are therefore **seven** (1 plus
2–7), not six as the introductory sentence implies.

The journal (`journal/2026-08-04-session-64.md`, line 131) repeats the undercount: *"**FIFTY-NINE
NAMES — KILLED AT CONCEPT.** Six grounds, three of which kill on their own."* The "three of them would
kill on their own" clause is accurate (Grounds 2, 3 and 4 are each explicitly marked "(kills on its
own)"); the "six" is not — the source document it is drawn from actually enumerates seven. **Owed:**
`KRITIKER-GATE-64.md` line 175 corrected to "six more" (or the journal corrected to "seven grounds"),
whichever the house judges the source of truth.

### 7. (Minor, note only — not blocking) One instance of lower-case "verified" reads close to the reserved tier word

`KRITIKER-GATE-64.md`, §9 (line 637): *"…the finding I handed over in §5 — the 8:12 cancellation
addressed to equipment, the CEM delivered as an Imminent Threat Alert — is **verified, better than the
Artist's**…"* Every file tonight is explicit that nothing is **VERIFIED** tier (that word reserved for
the sibling practice's shipped record) and everything here is **SOURCED**. This instance is lower-case
and reads in context as the ordinary English adjective ("checked," "confirmed"), not a tier claim, and I
do not think a reader would take it as the reserved label. Flagged for completeness since tier hygiene
was named as a specific thing to police strictly; no correction is owed unless the house wants to avoid
the word near a Tier discussion altogether.

---

## WHAT I CHECKED AND FOUND CORRECT

**The count (`COUNT-64.md`), re-run against the live OpenAlex API tonight, 2026-08-04 — all six figures
reproduce exactly, no drift since the file was written earlier tonight:**
- works citing the paper (W3027680906): **1,242** ✓
- works citing the retraction notice (W3035365037): **580** ✓
- works citing both: **380** ✓
- works citing the paper, published ≥ 2020-06-05: **1,145** ✓ (of which 368 also cite the retraction,
  777 do not — 32.1% / 67.9%, arithmetic checks: 1,145 − 368 = 777 ✓)
- stricter cutoff ≥ 2020-06-14: **1,111** citing, **362** also citing the retraction, 749 not (67.4%;
  1,111 − 362 = 749 ✓)
- the "share does not move" claim (67.9% vs 67.4%) holds.

**The Kritiker's second-object replication** (Shu et al., PNAS, retracted 2021), re-run tonight: 77 works
citing after retraction, 5 also citing the retraction notice, 72 not (93.5%) — all three figures
reproduce exactly, and both OpenAlex IDs (W2126983686, W4200294799) resolve to the titles claimed.

**The Hsiao & Schneider figure** — fetched `PMC9520488` first-hand: "13,252 postretraction citation
contexts, only 722 (5.4%) … acknowledged the retraction" — verbatim match.

**The CFR §11.31(e) code count**, re-derived independently from the eCFR versioner XML
(`title-47.xml?part=11&section=11.31`, issue date 2026-07-31), parsed programmatically rather than read
by eye: **57 codes exactly** — 5 national (EAN, NIC, NPT, RMT, RWT) and 52 state/local, matching the
exact 57-item list printed in both `CONDUCTOR-VERIFICATION-64.md` and `KRITIKER-GATE-64.md` letter for
letter, including the last entry (WSA, Winter Storm Watch) that a naive `TD class="left"` regex initially
missed because of a formatting quirk on the closing row. **59 is confirmed wrong; 57 is confirmed
right.**

**Both of the Kritiker's load-bearing NWS quotations, fetched first-hand tonight:**
- `weather.gov/nwr/eventcodes`: "the third letter … is limited to one of four letters: W for Warnings …
  A for Watches … E for Emergencies … S for Statements" and "A Statement is a message contaning follow
  up information to a warning, watch, or emergency" — verbatim match, **including the sic typo
  "contaning."**
- `weather.gov/box/product_descriptions`: the Severe Weather Statement description, with headings
  **"Cancellations"** ("WFOs will issue a SVS to provide notice a SVR or TOR has been canceled…") and
  **"Corrections"** ("WFOs will issue a SVS to notify users of erroneous counties…") — verbatim match.
- Confirmed, by direct text search of the fetched `eventcodes` page, that the words "cancel,"
  "correction," "all-clear," "retraction" and "false" **do not appear anywhere on it** — which means the
  Kritiker's finding that the Artist's quoted sentence is not on the page it is attributed to is
  **correct.**
- Confirmed ADR ("Administrative Message") is grouped under a page section literally headed
  "Administrative Events," beside RMT/RWT/DMO — matches the Kritiker's characterisation exactly.

**FCC, *DOC-350119A1.txt*, fetched and searched first-hand tonight:**
- Footnote 59, verbatim: "The cancellation is an instruction to downstream EAS and WEA equipment to
  cease retransmission. It does not generate a new alert transmission (e.g., an 'all clear' message). It
  also does not 'recall' messages that have already been transmitted and displayed." — exact match.
- Footnote 58 and the 8:12 timeline row ("HI-EMA cancels further transmission of the false alert, but
  does not issue an 'all clear' message") — exact match; cancellation message sent 8:12, CDW cancellation
  issued 8:13 — exact match.
- The 8:27, 8:30, 8:31–8:44 and 8:45 timeline entries, and the "45 seconds" phone confirmation — all
  quoted verbatim and correctly in `CONDUCTOR-VERIFICATION-64.md` and `KRITIKER-GATE-64.md`.
- Footnote 64 ("Civil Emergency Messages are transmitted over WEA as Imminent Threat Alerts. See 47 CFR
  § 10.400.") — exact match.
- HI-EMA's own 13 January 2018 press-release PDF returns **HTTP 404** as of tonight — confirmed.

**§11.45, fetched from the eCFR versioner XML directly:** the words "mimic" and "substantially similar"
occur **zero times** in the current text — confirms the Artist's quoted phrase is not regulation text.
§11.45(b) binds "an EAS Participant" (twenty-four hours to email); §11.45(c) covers FEMA/state/
local/Tribal/territorial entities and says only that they "are encouraged" — no deadline, no obligation —
matches the Kritiker's Ground 3 exactly. Effective date **[83 FR 39621, Aug. 10, 2018]** confirmed —
seven months after the 13 January 2018 alert.

**47 CFR §10.400**, fetched directly: four classes — National/Presidential Alert, Imminent Threat Alert,
Child Abduction Emergency/AMBER Alert, Public Safety Message — matches the Kritiker's characterisation.

**Massachusetts drug-lab figures** (`MATERIAL-64.md`): the ACLU press release (24,000+ / 16,449 / 61,000+
/ 37,000+) and the Commonwealth's own page ("over 20,000," January 2009–January 2013, effective dates
20 April 2017 and 13 December 2018) both fetched and confirmed to contain the exact figures quoted.

**FEMA IPAWS archive total**, fetched tonight with an explicit inline-count request: **4,870,228**
archived alerts — matches the Artist's étude-2 figure exactly.

**Tier discipline:** no file among the six reviewed declares anything **VERIFIED** tier; every substantive
file states plainly that nothing tonight draws on the sibling practice's shipped record and marks its own
material SOURCED, IMAGINED, or UNVERIFIED as appropriate. `ARTIST-64.md` §3.2 is correctly marked IMAGINED
(the composition), and its banner correctly marks the whole document as killed and non-live.
`DRAMATURG-64.md` correctly marks its central mechanism IMAGINED with no evidence claimed, and correctly
marks two neighbour citations UNVERIFIED (MoMA 403, and the *mention manuscrite* French-law neighbour, not
opened at Légifrance). No invented URL, quotation, work, name or number was found anywhere in the six
files beyond the ones already named above as findings.

**No superseded claim reads as live** anywhere I checked, with the qualification in Finding 2: the
banner's own specific address list for `ARTIST-64.md` is wrong, but the file's blanket kill-notice at its
head still prevents any reader from mistaking its content for a live claim.

**Total: 7 findings recorded (2 blocking, 4 corrections owed, 1 note-only); roughly 30 discrete facts,
figures, quotations and URLs independently re-checked against primary sources tonight, the great majority
of which reproduced exactly.**
