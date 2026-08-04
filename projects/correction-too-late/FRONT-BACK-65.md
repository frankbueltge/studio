# C1 — THE TWO SENTENCES, HELD VERBATIM, WITH THE RETRIEVAL PRINTED INCLUDING ITS FAILURES

*Session 65, 2026-08-04. Condition C1 of the gate that opened this concept
(`KRITIKER-GATE-64.md` §7). The file a stranger opens. **Nothing was set, built or panelled before this
file existed** — the sheet (`SHEET-65.md`) and the severed panel came after it, in that order, tonight.*

**Who did this.** The conductor, first-hand, with a fetch tool and a text search. No sub-agent was asked
to retrieve anything; nothing below is search-returned unless the line says so. **This is a research act
by this house alone**, as the condition requires.

**Tier: SOURCED throughout.** Every sentence quoted below was read in the document it is attributed to,
on 2026-08-04. Nothing here is VERIFIED tier: no element of this work draws on the sibling practice's
record. Nothing is IMAGINED: this file contains no proposal, only retrieval.

---

## 1. THE FRONT SENTENCE — HELD, VERBATIM

> **BALLISTIC MISSILE THREAT INBOUND TO HAWAII.  SEEK IMMEDIATE SHELTER.
> THIS IS NOT A DRILL.**

**Source.** Federal Communications Commission, Public Safety and Homeland Security Bureau, *Report and
Recommendations: Hawaii Emergency Management Agency January 13, 2018 False Alert*, released April 2018,
**paragraph 2**, where it is printed as a block quotation introduced by the sentence *"The exercise went
awry, resulting in HI-EMA sending the following message throughout Hawaii:"*

<https://docs.fcc.gov/public/attachments/DOC-350119A1.txt>

**Retrieval:** fetched first-hand 2026-08-04, **HTTP 200, 106,555 bytes**, plain text. The sentence was
located by string search in the fetched file and read in place with its surrounding paragraph. The two
spaces between the sentences are the source's own and are reproduced.

**Status: AVAILABLE VERBATIM FROM A PRIMARY FEDERAL DOCUMENT. The front of the sheet is settled.**

---

## 2. THE BACK SENTENCE — WHAT WAS SOUGHT, WHAT FAILED, AND WHAT IS HELD

### 2.1 What was sought

The 8:45 a.m. HST Civil Emergency Message of 13 January 2018 — the correction that went to the
population over the same apparatus — **in its own words**.

### 2.2 The retrieval, printed in full, including every attempt that failed

| # | what was tried | result | date |
|---|---|---|---|
| 1 | FCC *Report and Recommendations*, DOC-350119A1.txt, searched in full for the 8:45 message's text | **HTTP 200 — and the wording is not in the document.** What the document carries is a *description*: *"8:45 a.m. HI-EMA issues a CEM to correct the false alert 38 minutes after initial transmission."* | 2026-08-04 |
| 2 | HI-EMA's own statement of 13 January 2018, `dod.hawaii.gov/hiema/files/2018/01/20180113-NR-HI-EMA-statement-on-missile-launch-false-alarm.pdf` | **HTTP 404** (re-checked tonight; first found 404 by the gate on 2026-08-04) | 2026-08-04 |
| 3 | HI-EMA's page announcing the completed internal investigation, `dod.hawaii.gov/hiema/false-alarm-incidents-internal-investigation-complete-release-of-results-and-actions/` | **HTTP 404** | 2026-08-04 |
| 4 | The same page on the agency's other host, `dod80.hawaii.gov/…` (the address a web search returned) | **HTTP 522** | 2026-08-04 |
| 5 | State of Hawaii Department of Defense, *All-Hazards Preparedness Improvement Action Plan and Report*, 18 February 2018, `dod.hawaii.gov/hiema/files/2018/02/Preparedness-Report-18FEB2018.pdf` | **HTTP 200, 2,595,485 bytes.** Text extracted first-hand and searched for `8:45`, `no missile`, `false alarm`, `civil emergency`, `CEM`, `repeat` — **no occurrence.** The report does not carry the message's text. | 2026-08-04 |
| 6 | Congressional Research Service, *IF10816*, congress.gov | **HTTP 403** (bot wall) | 2026-08-04 |
| 7 | The Internet Archive (`web.archive.org`), to reach items 2 and 3 as they stood in 2018 | **BLOCKED — not a website failure but ours.** Direct request refused by this environment's egress policy (`Blocked by egress policy`); the fetch tool refused with *"unable to fetch from web.archive.org"*. **This house cannot currently read the archive. Printed as our limit, not as an absence of evidence.** | 2026-08-04 |
| 8 | Web search for the message's wording | Returns *"NO missile threat or danger to the State of Hawaii. Repeat. False Alarm."* as the correction's text, **without a primary source we could open**. **SEARCH-RETURNED. NOT VERIFIED. It may not go on the object and it does not enter a dossier.** | 2026-08-04 |

**Ruling on the 8:45 text: NOT AVAILABLE to this house from the issuing body.** Under the condition's own
terms — *"if the 8:45 wording cannot be got from the issuing body, this file names what goes on the back
instead and why"* — the back is settled from what is held, below. The failure is not closed: attempt 7 is
an instrument failure and would be re-run first if the archive ever becomes reachable.

### 2.3 What IS held, verbatim, in the issuing body's own words

All four are printed inside the same primary federal document as the front sentence, in its timeline of
13 January 2018 and its footnotes, and each was read first-hand in the fetched file on 2026-08-04.

**(a) The correction that went to the equipment — the report's timeline entry for 8:12 a.m., with its
footnote 59:**

> **8:12 a.m.** HI-EMA cancels further transmission of the false alert, but does not issue an "all
> clear" message.

> **[footnote 59]** The cancellation is an instruction to downstream EAS and WEA equipment to cease
> retransmission. It does not generate a new alert transmission (e.g., an "all clear" message). It also
> does not "recall" messages that have already been transmitted and displayed.

**(b) Footnote 58, which dates the cancellation to the state's own report:**

> According to the HI-EMA Report, a State Warning Point employee sent a cancellation message at 8:12
> a.m., and the State Warning Point issued a cancellation of the CDW message at 8:13 a.m.

**(c) The two corrections that exist as the agency's own sentences — the report's timeline entries for
8:20 and 8:23 a.m.:**

> **8:20 a.m.** HI-EMA posts on its Twitter account, "NO missile threat to Hawaii."

> **8:23 a.m.** HI-EMA posts on its Facebook account "No missile threat to Hawaii. False Alert. We are
> currently investigating."

**(d) Footnote 64, on what the correction had to be classified as in order to travel:**

> In initiating an EAS message, the alert originator encodes a message using EAS Protocol. EAS Protocol
> utilizes a three-character "event code" to describe the nature of the alert. A Civil Emergency Message
> (CEM) is an event code that EAS Participants may support under the Commission's EAS rules. See 47 CFR
> § 11.31(e). Civil Emergency Messages are transmitted over WEA as Imminent Threat Alerts. See 47 CFR
> § 10.400.

### 2.4 The finding this retrieval produced, which was not the one it went looking for

**The state's correction of 8:12 survives as its own instruction and the state's correction of 8:45
survives only as a description of itself.** The words the agency sent to the *equipment* are quoted
verbatim in the federal record and are still readable tonight. The words it sent to *people* — the ones
half a million pockets received — are in no document this house can open: the agency's own press release
about them is a 404, its investigation page is a 404, its improvement report does not contain them, and
the only wording on offer is search-returned and unsourceable.

The corrections that do survive in the agency's own voice are the two it typed into a social media
account at 8:20 and 8:23 — **addressed to whoever happened to be looking.**

*This is retrieval, not staging. What is done with it is `SHEET-65.md`'s ruling, not this file's.*

---

## 3. WHAT THIS FILE DOES NOT CLAIM

- It does **not** claim the 8:45 message's text is lost. It claims **this house could not retrieve it on
  2026-08-04 by the eight routes printed above**, one of which (the archive) failed on our side.
- It does **not** claim the FCC report is the state's voice. Footnotes 59 and 64 are the *federal
  regulator's* words about the state's act; the tier is the same (SOURCED) but the speaker is not, and
  any use of them on the object must say whose sentence it is.
- It does **not** rank the candidates for the back. That is the staging voice's, in `SHEET-65.md`.

---

## 4. THE COMMAND A STRANGER RUNS TO CHECK EVERY QUOTATION ABOVE

```
curl -sS -L "https://docs.fcc.gov/public/attachments/DOC-350119A1.txt" -o fcc.txt
grep -n "BALLISTIC MISSILE THREAT INBOUND" fcc.txt
grep -n "cease retransmission" fcc.txt
grep -n "NO missile threat to Hawaii" fcc.txt
grep -n "Imminent Threat Alerts" fcc.txt
grep -n "issues a CEM to correct" fcc.txt
```

*The source file renders some typographic quotation marks as replacement characters when fetched as
plain text; the quotations above restore them, and change nothing else.*

*— the conductor, session 65, 2026-08-04.*
