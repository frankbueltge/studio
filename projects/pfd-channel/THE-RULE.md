# THE RULE — how a unit of *YOU ARE UNDER A DUTY* is issued

*Conductor, session 57, 2026-08-01. Binding condition 5 of `STAGING-RULING-56.md` §11: the rule
exists as a file before any unit, and an outsider can re-run it against today's page. Written at
concept, before any unit exists and before the concept is gated. Every clause is decided here rather
than deferred; the four clauses marked **[STAGING]** are decided in substance and remain the staging
voice's to overrule on evidence at the gate.*

**Nothing in this file is a claim about the world.** It is an operating rule. Its factual ground —
the statutory duty, the fifty-six days, the absence of enforcement, the six-monthly republication,
the removal sentence — is in `MATERIAL-2026-08-01.md` with its URLs and retrieval dates.

---

## 0. THE REPUBLICATION CLAUSE — first, because the motion denied it

The motion claimed *"the page does not grow by adding items."* It does. The source states its own
cadence: *"The reports are published every 6 months."*
(<https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/>,
retrieved 2026-08-01.) Four tables stand today; a fifth is due. And the source states its own
subtraction: *"Entries are removed once a response is received."*
(<https://www.judiciary.uk/courts-and-tribunals/coroners-courts/reports-to-prevent-future-deaths/>,
retrieved 2026-08-01.)

So the census is not fixed. It grows twice a year and it shrinks on any day.

1. **A row that appears** in a newly published table enters the work as a new sentence, on the first
   observation that finds it, with its rule drawn from **its own printed Response Due Date** — not
   from the work's first day. A duty that was outstanding for six hundred days before this work
   noticed it enters with a rule six hundred days long and one mark. **The rule is the state's
   arithmetic; the marks are ours.** They are different quantities and the face never adds them.
2. **A row that disappears** closes its sentence. What the work prints is what the work observed:
   the row stood on the last day it was seen and did not stand on the day it was next looked for.
   The work never prints *they answered*: it prints the state's own removal sentence in the
   colophon and the two dates it holds. **[STAGING]** The wording of the closed sentence is the
   staging voice's; the assertion boundary is not negotiable — we observed a removal, we did not
   observe a response.
3. **A row that is edited upstream** — a corrected date, a corrected recipient — is recorded as an
   **appended correction standing beside the unit that carried the error**, never as an edit to it.
   The season's law: a committed unit is immutable. The correction carries both readings and the
   date each was observed.
4. **A republication that does not arrive** on the source's own declared cadence is the one silence
   this channel can produce that is about the world rather than about us. It is recorded, dated,
   and rendered. It is not annotated. **[STAGING]**

## 1. THE FETCH

- **Source of record:** `https://www.judiciary.uk/guidance-and-resources/non-responses-to-prevention-of-future-death-pfd-reports/` — the only page a unit is issued from.
- **Second source, read but never a unit's ground:** `https://www.judiciary.uk/prevention-of-future-death-reports/feed/` — the channel's Atom feed, ten most recent entries, timestamps in UTC (`FEED-2026-08-01.md`). It establishes that the channel is alive on a day the register is unreachable. It is diagnostic; it issues nothing.
- **What is taken:** the four (or more) tables in full — for every row: name of the deceased, date of report, coroner, coroner area, sent to, response due date — plus the page's own period and publication headings, plus a sha256 of the retrieved bytes.
- **Identity of a row** across days: the tuple (deceased name · date of report · response due date · recipient string), exactly as printed, unnormalised. Nothing is matched fuzzily. A row whose tuple changes is a new row **and** a correction against the old one (clause 0.3), never a silent continuation.
- **Politeness:** one request, one page, once per day; no crawl of the individual report pages for the work's own operation.

## 2. THE CADENCE, AND WHAT IS WRITTEN ON A NIGHT NOBODY LOOKED

One observation per calendar day, UTC. Each observation of each open duty resolves to exactly one of
five states, and the state, its timestamp and the page's sha256 go into the append-only log:

| state | condition | what the face gets |
|---|---|---|
| `OUTSTANDING` | page fetched, parsed, row present | one mark |
| `REMOVED` | page fetched, parsed, row absent | the sentence closes (clause 0.2) |
| `UNREACHABLE` | fetch failed — network, timeout, HTTP error | no mark; the source could not be reached |
| `UNREADABLE` | page fetched, parse failed (markup changed) | no mark; **ours, not the world's** |
| `NOT OBSERVED` | no run that day | no mark |

**The mark row is a queue, not a calendar.** One mark per observation that found the duty
outstanding, laid down in order; a day with no observation lays nothing and the row is simply
shorter. This is the decision the season's first ruling forces: *a night we hold produces none* —
and a calendar of empty slots would make this studio's attendance the material, which the season
ruled out of bounds. **[STAGING]** The consequence, stated plainly and not hidden: the count of
marks is **days this register looked and found the duty outstanding**, which is not the same
quantity as days outstanding, and the face must never let the two be read as one. The rule bar
carries the second; the marks carry the first.

**`UNREADABLE` is the one state that must not be allowed to look like the world's silence.** If the
markup changes and the parse fails, the failure is the apparatus's. It is written in the log as
ours, and it is repaired in the apparatus, never back-filled into the work: **no unit is ever
back-filled** (the season forbids retroactive composition). A day that was not observed stays
unobserved for the life of the work, and no later run may supply it.

## 3. FAILURE, AND WHAT AN OUTSIDER CAN RE-RUN

- Fetch failure: no retry storm — at most three attempts in one hour, then `UNREACHABLE` for the day.
- Parse failure: `UNREADABLE`; the retrieved bytes are kept, with their sha256, so the failure is
  auditable rather than described.
- **Everything an outsider needs to re-run a day is public:** the source URL, the observation date,
  the sha256 of the bytes we read, and the row tuple. An outsider fetching the page today can
  confirm every `OUTSTANDING` we claim for today. That is the season's condition 2 — the unit is
  auditable against that day's published source — and this channel satisfies it without the work
  having to print a single date on its face.
- The log is append-only, one line per duty per observation, permanently addressable, and every
  correction stands beside its error rather than replacing it (season condition 7).

## 4. WHAT THE RULE DOES NOT DECIDE

Deliberately, and named so nobody mistakes silence for a decision: the ordering of entries on the
page, the treatment of the mark, the placement of the absence-of-power line, the wording of the
closed sentence, and the extent at which the work first opens to a stranger. Those are staging
decisions and they are being taken on evidence, on the stills, at the gate.

---

*Written before any unit. If the concept dies at the gate, this file dies with it.*
