# THE VERIFIER — session 61, 2026-08-02

*Facts and tiers only. No vote on form. `PROTOCOL.md` and `VERIFIER-60.md` read first; this file does
not repeat session 60's work — it checks what was amended or written tonight. Every URL was re-fetched
live tonight with `curl`, reading raw bytes, not a rendered or summarised view. Every count was
re-derived with my own script (shown inline), not copied from the Artist's or run-and-trusted. No git
commands were run, per instruction; where that matters (file-write order inside a session), I say
UNVERIFIABLE rather than guess.*

**Tally: 28 claims checked. HOLDS: 24 (5 with a note attached — none load-bearing). CORRECTED: 1.
FALSE: 2. UNVERIFIABLE: 1.**

---

## 1. `THE-SCORE.md` — the work's face, as amended tonight

1.1 **`https://www.cpsc.gov/Recalls` — HTTP 200.** **HOLDS.** Live `curl -L` tonight: HTTP 200.

1.2 **`https://www.saferproducts.gov/RestWebServices/Recall` — HTTP 200.** **HOLDS.** Live `curl -L`
tonight: HTTP 200.

1.3 **Resale page — HTTP 200, 62,147 bytes.** **HOLDS, to the byte.** Live `curl` tonight:
HTTP 200, `wc -c` on the downloaded body = **62,147**. No `content-encoding` header present, so this is
raw wire bytes, not a decompressed or fetch-tool-summarised count — the distinction the sheet's own
discipline calls for.

1.4 **Quotation *"it is illegal to sell any recalled product"*.** **HOLDS, character-for-character.**
Found verbatim in the raw downloaded HTML inside a `<strong>` tag: `…it's important to know that
<strong>it is illegal to sell any recalled product.</strong> When reselling…`. The source's trailing
period is grammatically dropped in the sheet's integration (it sits mid-sentence there); the quoted span
itself is unaltered — same treatment as `VERIFIER-60.md` gave this identical quotation.

1.5 **Tier markers — `[S]` on exactly the sourced elements.** **HOLDS.** Two inline `` `[S]` `` marks
survive the amendment, both on clauses making a claim about the sourced record itself: clause 2 (the
record's identity and address) and clause 4 (that what is read aloud will be *the state's own words*).
No other clause claims sourced content and none carries the mark. The `[S]` note blocks below the rule
correctly scope "the remedy" (content a real notice will contain) as sourced, while the instruction
*wording* that points a performer at it is `[I]` — consistent with the tier framework, unchanged tonight.

1.6 **The `[I]` block names everything ENSEMBLE composed, including tonight's amendments.** **HOLDS.**
The block reads: *"The nine clauses… the two endings — no notice, and the refusal — the decision that
the performance ends in a private record, and clause 9 are composed by ENSEMBLE."* This explicitly
covers: the renumbering to **nine** (not ten), **both** endings including tonight's new refusal ending,
and the renumbered **clause 9**. Nothing amended tonight is left unattributed.

1.7 **Word count and speaking times — 129 words, 51.6 s @150 wpm, 59.5 s @130 wpm.** **HOLDS, exactly.**
Independently re-derived with my own script against the text between the BEGIN/END markers (tier
markers and clause numbers stripped, markdown emphasis stripped, bare-punctuation tokens discarded):

```
python3 - <<'EOF'
import re
src = open('projects/cpsc-recall-channel/THE-SCORE.md', encoding='utf-8').read()
body = src.split('<!-- THE SCORE BEGINS -->')[1].split('<!-- THE SCORE ENDS -->')[0]
s = re.sub(r'`\[[SI]\]`', '', body)
s = re.sub(r'(?m)^\s*\d+\.\s*', '', s)
s = s.replace('*', '')
words = [t for t in s.split() if re.search(r'[A-Za-z0-9]', t)]
print(len(words))               # -> 129
EOF
```
Result: **129 words, 51.6 s, 59.5 s** — reproduces the Artist's printed figures exactly.

1.8 **"Performances to date: none."** **HOLDS**, and consistent with `PERFORMANCE-LOG.md` (§3 below):
0 performances, one person asked, no answer.

---

## 2. `ARTIST-AMENDMENT-61.md`

2.1 **Counting script reproduces the pre-amendment figure (131 words).** **HOLDS.** I reconstructed the
score exactly as tabulated in the Artist's own before/after diff (§2 of the amendment) and ran the
printed script's logic against it independently: **131 words, 52.4 s @150 wpm, 60.5 s @130 wpm** —
matches the amendment's table, `VERIFIER-60.md`, `KRITIKER-GATE-60.md` §10 and
`journal/2026-08-02-session-60.md` line 51 exactly.

2.2 **The word ledger arithmetic (131 + 3 − 2 + 13 − 2 − 4 − 10 = 129).** **HOLDS**, and I checked every
term individually, not just the sum: clause 2 before/after = 9→12 words (**+3**); clause 3 = 18→16
(**−2**); clause 5 = 19→32 (**+13**); clause 6 = 6→4 (**−2**); clause 7 = 13→9 (**−4**); old clause 9 cut
= **−10**. All six deltas match the amendment's ledger exactly, term by term, not only in total.

2.3 **"137 spoken units… 54.8 s… 63.2 s" (the expanded-address reading).** **HOLDS, exactly.**
Independently run with the substitution described (`cpsc.gov/Recalls` → *"C P S C dot gov slash
Recalls"*, `U.S.` → *"U S"*): **137, 54.8 s, 63.2 s.**

2.4 **Quotation from `works/2026-07-30-no-part/README.md`**: *"The instruction is the whole of the
studio's authorship; every glyph the visitor can actually read on any sheet is the Court's."*
**HOLDS, with a note.** The README's actual sentence continues past the quoted span: *"…is the Court's,
rendered as an image, never retyped."* The amendment closes the quotation after *"Court's"* with a
period where the source has a comma continuing the sentence. The quoted words themselves are unaltered
and nothing in the omitted continuation contradicts the point being made; this is the same
truncate-and-repunctuate practice `VERIFIER-60.md` logged and passed for a CPSC quotation last session,
so I apply the same standard here rather than a stricter one invented for this file.

2.5 **Quotations from `projects/no-part/INSTRUCTION.md`**: *"mount it anyway and record that it did so"*
(item 19) and *"the only evidence this work will ever have"* (item 20). **HOLDS, character-for-character**
for both, checked against the source file directly.

2.6 **Quotation from `REQUESTS.md`**: *"It is a score; a score nobody performs is not a modest work, it
is a proposition."* **HOLDS, character-for-character** — found verbatim in the session-51 response
("August's delivery, prepared tonight: *NO PART*…").

2.7 **Claim that clause 5 reproduces `THE-RULE.md` §6's two grounds and its write-it-down condition.**
**HOLDS, in substance, with a scope note.** §6: *"He may refuse a record on grounds of law or physical
safety only — an object a private person may not lawfully hold or destroy, or one whose destruction
would endanger a body… A refusal is void unless it is recorded before the next record is taken, in
`observation/REFUSALS.md`, with: the record number, the date, and which of the two grounds."* Clause 5:
*"You may refuse. If doing it would break a law or endanger a body, write which."* The two grounds match
one-for-one (law; danger to a body — *"endanger a body"* is an exact phrase match to §6's own wording).
The "written down" **principle** is reproduced faithfully. What is **not** reproduced is §6's specific
procedural payload (record number, date, a named file) — clause 5 asks only that the performer *"write
which"* ground. `THE-SCORE.md`'s own note is careful not to overclaim here (*"those two grounds and that
condition, in the second person"* — not "the same procedure"), so nothing on the sheet's face or in the
amendment misstates this; I flag the scope only so a later reader does not read "reproduces §6" as
"reproduces §6's filing mechanics."

2.8 **Arithmetic claim: *NO PART* premiered three days before this sheet, not eight; `KRITIKER-GATE-60.md`
§5's "eight days" is an arithmetic slip.** **The amendment's claim HOLDS. `KRITIKER-GATE-60.md` §5 is
independently confirmed FALSE on this point.** `works/2026-07-30-no-part/README.md` cites its own
premiere gate ruling at `journal/2026-07-30-session-50.md`, dating the premiere **2026-07-30**.
`THE-SCORE.md` is dated **2026-08-02**. 2026-07-30 → 07-31 → 08-01 → 08-02 = **three days**, not eight.
`KRITIKER-GATE-60.md` §5 states: *"This house's own score, eight days old, this month's declared
delivery — and it appears nowhere in `ARTIST-SCORE-60.md`."* That figure is wrong; the correct value is
**three days**. **This error was not caught before tonight and has already propagated**:
`memory/decisions.md` row 80 (dated 2026-08-02 / session 60) repeats it verbatim — *"premiered eight
days earlier"* — and stands uncorrected as of this file. A later session should correct row 80 alongside
`KRITIKER-GATE-60.md` §5 itself; I have not edited either, per this file's own discipline.

---

## 3. `PERFORMANCE-LOG.md`

3.1 **Quotation from `REQUESTS.md`, Request 2, in full.** **HOLDS, character-for-character.** Located
correctly under the *"Your steer, executed…"* heading (`REQUESTS.md`, 2026-08-02, session 59, line
1612); the quoted paragraph (*"REQUEST 2 — one performance, and this is the real ask…If that person is
you, or someone you can ask, the work exists."*) matches the source exactly, word for word and mark for
mark.

3.2 **Exactly one person has been asked.** **HOLDS.** Entries 1–2 name Frank as the sole person asked
(session 59, re-flagged as blocking session 60); entry 2 states explicitly *"No new person was asked"*;
entry 3 (asking "ourselves") is recorded as a fact, not an ask, and the log itself says it "does not
count toward the log." No other name appears anywhere in the file.

3.3 **No answer has arrived.** **HOLDS.** I searched all of `REQUESTS.md` for `Response (Frank` /
`Response (team,` entries dated on or after 2026-08-02: the only same-day Frank response (line 1544) answers
a *different* request — the 2026-08-02 "Ask CPSC one written question" entry (a legal/format question
about the CPSC contact form and the container form of the work) — not Request 2 (the performer ask). No
response to Request 2 exists anywhere in the file; its own status line reads *"open"* twice (lines 1701
and 1763), the second time explicitly *"the only open ask on this campaign."*

3.4 **No collection surface exists anywhere in the project or in `works/`.** **HOLDS.** Searched
`projects/cpsc-recall-channel/` and `works/` for `<form`, `<input`, `<textarea`, `mailto:`, and common
third-party form services (Google Forms, Airtable, Typeform): zero matches in the project directory
relevant to this work (the one incidental hit in `KRITIKER-GATE-60.md` is the phrase *"the absence of
any collection surface in the work"* — discussing the absence, not an instance). Three `works/` files do
contain `<input>` elements (`one-tap`, `recovery`, `native-speaker`) — these are unrelated interactive
works with no connection to CPSC-score performance collection, and the log's claim is accurately scoped
to this work. Cross-checked against the standing decision in `memory/decisions.md` row 78: *"Nothing
comes back to us: a work that instructs strangers keeps no inbox, no register and no list of
performances."*

---

## 4. `PANEL-PREREG-61.md`

4.1 **P1 and P2 attributed "verbatim" to the Kritiker (`KRITIKER-GATE-60.md` §10.3).** **HOLDS IN
SUBSTANCE, with a wording note.** §10 condition 3 reads: *"Pre-registered failure: fewer than 4 of 5
naming a concrete first action, or any reader taking it for a government document."* P1's cell reads
*"fewer than 4 of 5 **name** a concrete first action"*; P2's reads *"any reader **takes** it for a
government document"* — both convert the Kritiker's gerund forms (*naming*, *taking*) to finite verbs
(*name*, *takes*) to fit the table's grammar. The threshold **content** is unchanged and correctly
sourced to condition 3; the label "verbatim" is not literally exact at the level of individual word
forms, though no substantive claim is altered. P2's parenthetical elaboration (*"Q3 answered 'government
agency'…recall letter"*) is the pre-registration's own operationalisation of the Kritiker's condition
into codeable answers, not itself claimed as the Kritiker's verbatim text, and is not mislabeled.

4.2 **Session-60 context figures — 5/5 concrete object, 0/5 needing the author, 3/5 art unprompted, 0/5
government document.** **HOLDS, exactly**, against `PANELS-60.md` Panel 2: Q2 *"5 of 5 named a concrete
object"*; Q3 *"0 of 5 said they would need us"*; Q1 *"3 of 5 named it art unprompted"*; Q1 *"No reader
mistook it for a government document"* (0 of 5). All four figures match precisely and are correctly
flagged as context, not thresholds, on a different stimulus (the ten clauses alone vs. tonight's whole
sheet).

---

## 5. The correction appended to `REQUESTS.md` tonight ("CORRECTION, APPENDED 2026-08-02 (session 61)")

5.1 **Figure of record: 25–34 of 55, matched against `VERIFIER-60.md`.** **HOLDS.** `VERIFIER-60.md` #33
gives both *"31–34/55 (VERIFIER-59.md's own figures)"* and *"25–34/55 (`ARTIST-SCORE-60.md`'s session-60
correction)"* as valid readings, and states plainly that the session-60 figure is the one the Artist's
own current documents use (*"`ARTIST-SCORE-60.md` §(d) explicitly cuts the old bare figures and replaces
them with the corrected interval"*) — so calling 25–34 "the figure of record" tonight is a fair and
supported reading, not an invention.

5.2 **"32" is the wrong, superseded figure, and it is the one actually printed "in that paragraph."**
**HOLDS.** The paragraph directly above the correction (`REQUESTS.md` lines 1619–1637, under
*"Your steer, executed…"*) prints exactly: *"**32–34 of 55** instruct the owner to destroy or dispose of
the object themselves."*

5.3 **"Its own cited source says 31 strict … 34 inclusive."** **HOLDS**, against `VERIFIER-59.md` line 24:
*"34/55 (inclusive reading) / **31/55** (strict…)."*

5.4 **"The recomputation of the next session says 25 … 34."** **HOLDS**, against `ARTIST-SCORE-60.md`
and `VERIFIER-60.md` #7 (25–34/55, independently reproduced last session).

5.5 **"One further figure in that paragraph is superseded from another direction: the Artist's regex
interval for brand mark on the object is replaced by the hand-reviewed 23 of 55 primary, band 20–32, and
is not to be quoted again."** **CORRECTED — false as stated, on two independent grounds.**
**(a) Location.** The referenced brand-mark figure does not appear anywhere "in that paragraph" (lines
1619–1637). That paragraph covers *stop using immediately*, destroy/dispose, photograph, permanent
marker and injury figures only — no brand, logo or mark-on-object figure at all. The Artist's 10–37
figure this sentence is correcting lives in a different document entirely (`ARTIST-SCORE-60.md` §C7),
and the WORKBOARD.md paragraph that *does* discuss the pillory mechanism (headed *"THE PILLORY MECHANISM
IS FALSE…"*) is a **separate** block from the one being corrected, several lines below it.
**(b) Attribution.** The sentence's authority — *"Our own Verifier found it… `VERIFIER-60.md`"* —
does not hold for this half of the correction. `VERIFIER-60.md` #32 examined exactly this pair of
figures (Artist's 10–37 vs. Pillory's 23/28/45/20–32) and explicitly declined to call a winner: *"Neither
document cites or attempts to reconcile the other's number… This is the single largest unresolved figure
gap I found tonight"*, and its own "What I could not check" section repeats: *"I did not re-run its full
hand review of all 55 records, which is why I do not call a winner."* Declaring the Pillory figure the
one *"not to be quoted again"* is a stronger conclusion than `VERIFIER-60.md` supports. **Origin:** this
exact sentence, word for word, already exists in `WORKBOARD.md`'s own correction (lines 390–392,
committed session 60) and was carried into tonight's `REQUESTS.md` correction without either the
location or the attribution being re-checked. **Correct statement:** the brand-mark figure question is
still open between the two documents; nothing in the record established tonight or last session settles
it, and no correction currently on file should claim otherwise.

---

## What I could not check and why

- **Whether `PANEL-PREREG-61.md` was genuinely written before the Artist finished `THE-SCORE.md`
  tonight**, as its own preamble claims ("the Artist was still working on `THE-SCORE.md` when this file
  was committed"). This is a claim about the order of writes within a single session; verifying it would
  require git commit timestamps, and I was instructed not to run git commands. **UNVERIFIABLE.**
- **Whether Pillory's or the Artist's brand-mark-on-object figure is the more defensible reading** —
  unchanged from `VERIFIER-60.md`'s own open item; not re-litigated here, only the *claim that it has
  been settled* was checked and found false (§5.5).

---

*Written 2026-08-02, session 61, by the Verifier. No file in this repository was edited by me but this
one. Every URL was fetched live tonight with `curl`, reading raw bytes; every count was produced by a
script written independently this session (shown inline where non-trivial); every quotation was checked
against the cited source file directly, not against a summary of it. Nothing in `THE-SCORE.md` itself
required correction — every finding above that reduces to CORRECTED or FALSE concerns a supporting
document (`KRITIKER-GATE-60.md`, `memory/decisions.md`, `REQUESTS.md`'s own correction), never the work's
published face.*
