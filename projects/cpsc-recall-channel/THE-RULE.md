# THE RULE — which notice this house takes

*Owed since session 58. Written session 60, 2026-08-02, by the Artist. Committed **before** its
next application. Every figure here is printed by `observation/artist-60-counts.py`, run against
`observation/recalls-2026-07-01_2026-08-02.json` (sha256 `cf45ebec…4784da1`).*

**What this rule is not.** It does not govern a performer of `THE-SCORE.md`. A performer chooses
an object they already own; that choice is theirs and this house never sees it. This rule governs
only **us** — which single notice this house takes when it performs the score itself, builds an
étude, or hands a realiser one unit for a room. It exists so that an outsider can check that we
did not pick the interesting one.

---

## 1. THE SOURCE

`https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=<start>&RecallDateEnd=<end>`
— the U.S. Consumer Product Safety Commission's own machine-readable recall record. `[S]` HTTP 200
on 2026-08-02. The human-readable form of the same record is `https://www.cpsc.gov/Recalls`
(HTTP 200, 2026-08-02). The raw response body for the window in use is committed to
`observation/` with its sha256 **before** any record is taken from it. The JSON is the source of
record, never the HTML page.

## 2. THE FILTER

A record is **admissible** if the concatenation of its `Remedies` entries matches
`/stop using[^.]*immediately/i` — case-insensitive, applied to the source's own characters with
no cleanup, no repair of stray glyphs, no re-typing. The campaign is named after that sentence; a
record without it cannot carry it. **50 of 55** records in the committed corpus are admissible;
that count is insensitive to every coding tried.

## 3. THE ORDER

Admissible records are sorted by `RecallDate` **ascending**, then `RecallNumber` ascending
(numeric). The rule takes **the first admissible record in that order that this house has not
already taken.**

**A property retrieved first-hand and worth stating, because an auditor will trip on it** `[S]`:
the endpoint returns records in **no order at all**. Fetched 2026-08-02 for the window
2026-07-01 … 2026-07-03, it returned twelve records beginning `26596, 26601, 26599, 26593, …`
with `26591` **tenth**. The sort is the rule's work, not the source's. An outsider who takes the
first row of the response gets a different object and should not conclude we cheated.

## 4. TIES

`(RecallDate, RecallNumber)` is unique across the committed corpus — **0 duplicate keys**. If the
source ever emits a duplicate pair, the lower `RecallID` is taken. No other tiebreak exists.

## 5. WHEN THE SOURCE PUBLISHES NOTHING

The clock is the Commission's. If a window closes with **no** published record, or with records
but **none admissible**, **no unit is issued.** Nothing is back-filled, nothing is substituted,
and the standing object is **not** destroyed — it stands another interval. The silence is recorded
as what it is: the window's dates, the query as run, and the record numbers returned if any. A
held night is a held night, written down.

## 6. DISCRETION — the whole of it, declared

Exactly one discretion exists, and it belongs to the human publisher (Frank Bültge), who carries
the legal and physical responsibility:

> **He may refuse a record on grounds of law or physical safety only** — an object a private person
> may not lawfully hold or destroy, or one whose destruction would endanger a body (pressurised,
> explosive, flammable, toxic).

A refusal is void unless it is recorded **before the next record is taken**, in
`observation/REFUSALS.md`, with: the record number, the date, and which of the two grounds. The
rule then takes the next admissible record in the same order. **There is no aesthetic, hazard-
severity, injury-count, unit-count, price, brand, retailer or country discretion, and none may be
added without superseding this file in a committed, dated edit.** On the corpus in hand the
discretion exercised is **null**: the rule reaches `RecallNumber` **26591** (published 2026-07-02)
having **skipped 0 records**, and `observation/REFUSALS.md` does not yet exist because nothing has
been refused.

## 7. HOW AN OUTSIDER AUDITS A CHOICE, AFTER THE FACT, WITHOUT US

1. Fetch the endpoint for the window we published.
2. Apply §2's regex; sort by §3's key.
3. Read `observation/REFUSALS.md` and remove any recorded refusal, and the list of records already
   taken.
4. The first remaining record must be the one we showed. If it is not, the choice is invalid and
   the work is wrong — not "interpreted differently".

Steps 1–3 are implemented and printed by `observation/artist-60-counts.py` (§"THE RULE, APPLIED"),
which a stranger can run against the committed JSON with no access to us.

## 8. WHAT THE RULE COSTS, STATED RATHER THAN HIDDEN

The rule takes what the Commission published, not what suits the room. Under my codings only
**15–24 of 55** admissible records produce a remedy that both destroys the object at the owner's
hand *and* requires a photograph *and* promises money back — the triplet §(c) of
`ARTIST-SCORE-60.md` argues is the room's agency organ. A floor built strictly by this rule is
therefore a floor where **most pieces have no receipt beside them.** Narrowing §2 to that triplet
would fix it mechanically and without human discretion — and would also mean the work no longer
shows what the state instructs, but a chosen third of it. **That narrowing is not adopted here.**
It is named as the one amendment the room would need, so that nobody performs it silently.
