# THE VERIFIER — session 62, 2026-08-03, FACE check

*Facts and tiers only. No vote on form. Blocking check on the frozen publication
candidate at `projects/cpsc-recall-channel/candidate/` (`index.html`, `meta.json`,
`README.md`), built by `observation/build-page-62.py` from `STAGING-RULING-62.md`.
Nothing in `candidate/`, `THE-SCORE.md`, or the build script was edited to produce
this report. Every figure below was re-derived independently — from the committed
JSON, from the candidate's own bytes, and (where named) from a live fetch — not
copied from the build script's own printout.*

---

## A. Every claim on the page's face

### A1 — The remedy quotation

Independently re-derived from **both** sides, not trusted from the build script:

- From `observation/recalls-2026-07-01_2026-08-02.json`, record with `RecallNumber
  26591`: `Remedies[0].Name` is 326 characters, `sha256
  b987f91130185652d3f3ebce96d736af6c5220f720578e54ac83ae9c6fdd476b`.
- From `candidate/index.html`: extracted the `<p class="remedy-text">…</p>` span,
  un-escaped `&amp; &lt; &gt;` myself (independent of the build script's own
  `unescape_html`), got a 326-character string, `sha256`
  `b987f91130185652d3f3ebce96d736af6c5220f720578e54ac83ae9c6fdd476b`.
- Both strings are byte-identical. The stray `?` glyph in `pieces to?recalling@` is
  present, unrepaired, on both sides — and is present in the raw JSON source itself
  (not introduced by escaping/rendering).
- Corpus integrity: `sha256` of the full committed JSON file is
  `cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1`, matching the
  prefix/suffix `THE-RULE.md` cites (`cf45ebec…4784da1`).

**A1: HOLDS.**

### A2 — The citation

Against the same JSON record: `RecallNumber` = `26591` ✓. `RecallDate` =
`2026-07-02T00:00:00` → `2 July 2026` ✓ (matches the page's human-readable date and
the build script's own `human_date()` output for that ISO string). `URL` =
`https://www.cpsc.gov/Recalls/2026/Vevor-Recalls-Baby-Loungers-Due-to-Risk-of-Serious-Injury-or-Death-from-Entrapment-and-Fall-Hazards-Violate-Mandatory-Standard-for-Infant-Sleep-Products`
— matches the page's citation text character for character.

**A2: HOLDS.**

### A3 — The selection claim

Applied `THE-RULE.md` §2–§3 myself against the committed corpus (55 records), from
scratch, independent of `artist-60-counts.py` and the build script:

- Admissibility: concatenation of a record's `Remedies[*].Name` matches
  `/stop using[^.]*immediately/i`. **Result: 50 of 55 records admissible** (matches
  `THE-RULE.md` §2's stated count).
- All 50 admissible records carry exactly one `Remedies` entry, so the concatenation
  equals `Remedies[0].Name` in every case (checked directly — 0 admissible records
  have more than one remedy entry).
- Sort by `RecallDate` ascending, then `RecallNumber` ascending (numeric). **First
  record in that order: `RecallNumber` 26591, `RecallDate` 2026-07-02.**
- `(RecallDate, RecallNumber)` uniqueness across the corpus: confirmed, 55 unique
  keys, 0 duplicates (§4's "0 duplicate keys" claim holds too, though not directly
  asked).
- `observation/REFUSALS.md` does not exist — confirmed by directory listing — so no
  refusal record exists to remove from the candidate pool, consistent with
  `THE-RULE.md` §6's claim that discretion exercised is null.

The rule reaches 26591 with **0 records skipped**, exactly as the page's selection
line and `THE-RULE.md` §6 state.

**A3: HOLDS.** (Admissible count independently reproduced: 50.)

### A4 — "50 of 55" and the "open with" sentence

The count itself reproduces cleanly: **50 of 55** committed records are admissible
under `THE-RULE.md` §2's regex (see A3). That part of the figure is correct and
matches `README.md`'s own phrasing of it ("admissible records are those whose
concatenated `Remedies` match `/stop using[^.]*immediately/i` (50 of 55)" — which
does **not** claim the notices "open with" the sentence, only that they match it).

The page's own sentence is stronger: *"50 of 55 recall notices published in the
window this record was drawn from **open with** the sentence that gives this score
its name."* Checked literally, word by word, against `Remedies[0].Name` for all 50
admissible records:

- **0 of 50** begin, as their literal first word(s), with "Stop using…immediately."
  Every one of the 50 — including record 26591, the one quoted on the page itself —
  opens instead with a subject clause: `"Consumers should stop using…"` (46 of 50),
  `"Pool owners, pool operators and consumers should stop using…"` (3 of 50), or
  `"Consumers should unplug and stop using…"` (1 of 50). Record 26591's own remedy,
  quoted in movement I, literally begins `"Consumers should stop using the recalled
  baby loungers immediately…"` — not `"Stop using…immediately."`
- The matched phrase does sit inside the **first sentence** of all 50 remedies (no
  admissible record's match falls in a second or later sentence), so a weaker claim
  — *the first sentence of 50 of 55 remedies instructs the reader to stop using the
  named product immediately* — would be accurate. That is not the claim printed.

As written, *"open with the sentence that gives this score its name"* asserts a
literal opening that no record in the corpus has, including the one record shown on
the page. This is a false claim on the page's own face, per the check's own
instruction to flag it as such.

**A4: FALSE**, as written — the notices contain that sentence at the head of their
first sentence, not literally open with it, and the record count underneath (50 of
55) is otherwise correct.

### A5 — Movement II counts

`PERFORMANCE-LOG.md`'s own state line: *"State as of the last entry below:
performances 0 · people asked 1 · answers received 0 · publication blocked."* The
page: *"performed 0 · asked 1 · answered 0."* Same three numbers (0, 1, 0), abbreviated
labels, same meaning; entries 1–4 of the log support each figure (one ask, filed in
`REQUESTS.md`; no answer to date; the house's own inability to perform recorded as
fact, not counted toward the log).

**A5: HOLDS.**

### A6 — The `[S]`/`[S]`/`[I]` notes and the retrieval-date question

Extracted all five `<p>` elements of movement IV from `candidate/index.html` and
compared them, clause by clause, to `THE-SCORE.md`'s own note block (the four
paragraphs starting `**\`[S]\` SOURCED — not ours.**`, `**\`[S]\` SOURCED — one
thing…**`, `**\`[I]\` IMAGINED — ours.**`, `**Nothing is sent to us.**`, plus the
`50 of 55` sentence, which is the page's own addition, not in `THE-SCORE.md`). All
four score-sourced paragraphs match `THE-SCORE.md` word for word (markdown → HTML
conversion only: backtick marks → `<span class="mark">`, `*emphasis*` → `<em>`,
`<https://…>` autolinks → `<a href>`).

**Retrieval-date honesty.** The page (`meta.json` date, and the state line's "As of
3 August 2026") is dated 2026-08-03. Its two `[S]` notes carry retrieval dates of
2026-08-02 for `cpsc.gov/Recalls`, `saferproducts.gov/RestWebServices/Recall`, and
the resale/thrift page. I independently re-fetched two of the three live today
(2026-08-03):

- `https://www.cpsc.gov/Business--Manufacturing/Business-Education/ResaleThrift-Stores-Information-Center/Stop-Online-Sale-of-Recalled-Products`
  loaded successfully and contains, verbatim, *"it is illegal to sell any recalled
  product."*
- `https://www.cpsc.gov/Recalls/2026/Vevor-Recalls-Baby-Loungers-…` loaded
  successfully and its remedy text matches `Remedies[0].Name` in substance (the
  fetch tool's markdown conversion smooths the raw `?` glyph and does not preserve
  byte-exact spacing, which is why `THE-RULE.md` §1 correctly names the JSON, not
  the HTML page, as the source of record).

Both are consistent with the report that the conductor separately confirmed HTTP 200
on all three live on 2026-08-03, including the 62,147-byte figure for the resale
page. A retrieval date that is one day older than the publication date is not a
discrepancy: it states when the evidence was gathered, not when the page is dated,
and nothing about the underlying facts changed in the interval — confirmed by the
independent same-day re-check. Dating a page 2026-08-03 while citing evidence
retrieved 2026-08-02 is honest as written; it would only be dishonest if the facts
had moved between the two dates or if the page implied simultaneity it doesn't
claim.

**A6: HOLDS** (notes match `THE-SCORE.md` word for word; retrieval-date framing is
honest as written).

### A7 — The nine clauses

Extracted all nine `<li>` elements of movement III and compared them, in order, to
the nine numbered clauses between `<!-- THE SCORE BEGINS -->` and `<!-- THE SCORE
ENDS -->` in `THE-SCORE.md`. All nine match word for word, in the same order, with
only markdown → HTML conversion (backtick `` `[S]` `` → `<span class="mark">[S]</span>`,
`*no notice*` → `<em>no notice</em>`). No clause is split, reordered, or annotated.

**A7: HOLDS.**

---

## B. The tiers

Everything on the page except two sentences carries an explicit mark or sits inside
an element whose mark is stated once for the whole block: the remedy quotation and
its citation carry `[S]`; clauses 2 and 4 of the score carry `[S]`; the four notes of
movement IV are headed `[S]`, `[S]`, `[I]`, and (for "Nothing is sent to us")
unheaded but self-evidently a statement about the house's own non-collection, not a
claim about the world. Nothing ENSEMBLE composed is presented as the state's: the
remedy blockquote is visually and typographically set apart (border, larger italic
type, its own citation line) from the house's prose. Nothing the state's is presented
as ours: the `[S]` mark precedes the remedy and both score clauses that quote CPSC
language.

**The two exceptions are exactly the two sentences named in the check: the selection
line (movement I) and the "50 of 55" line (movement IV).** Both are unmarked prose.
Both are factual claims, not stage directions or captions:

- The selection line asserts a specific, checkable fact about method (a committed
  rule, not the house, chose the record; discretion null; 0 skipped) — verified
  TRUE in A3, but printed with no `[S]` or `[I]` mark of any kind.
- The "50 of 55" line asserts a specific, checkable statistic about the corpus and
  a specific textual property of the 50 records — verified FALSE as worded in A4 —
  again printed with no mark.

Under `PROTOCOL.md`'s tier law (`SOURCED` = "your own research: every factual claim
about the world … has a real, retrievable URL," with the tiers "visible on every
work" and blurring named the studio's "cardinal sin"), both sentences are `SOURCED`-
class claims in substance — they are traceable to `THE-RULE.md` and the corpus, and
one of them is checkable enough to be found false by that same standard — yet
neither carries a `SOURCED` mark or any other. This is a factual gap, not a matter of
taste: a visitor reading the page's own labelling convention (every other assertion
of fact about the state's material or the house's process carries `[S]` or `[I]`)
has no mark to tell them these two sentences are asserted as fact rather than
composed commentary, and in the one case that matters most (A4), the unmarked
sentence is also the one that turns out not to be true as written. **They need a
mark** — the absence is a labeling omission on a page whose organizing law is
exactly this label, and it is more consequential here than it would be elsewhere on
the page, because A4 shows an unmarked factual sentence can be wrong without the
page's own apparatus flagging it as anything other than plain truth.

Every other element on the page is assignable to `VERIFIED` / `SOURCED` / `IMAGINED`
without blurring.

---

## C. Legal hygiene

The page names one firm, **Vevor**, and reproduces one company email address,
`recalling@vevor.com` — both occur **only** inside the verbatim CPSC remedy
quotation (`Remedies[0].Name` of record 26591) set off in the `.remedy` blockquote
with its `[S]` mark, record number, and URL beside it.

- **Traceability.** Both the firm's name and the email address are the U.S.
  Consumer Product Safety Commission's own published words for this record, quoted
  character for character (A1) and cited by record number and URL (A2) to the
  primary source. There is no factual claim about Vevor anywhere else on the page —
  movement II (the house's own prose about performance) never names the firm, and
  per `STAGING-RULING-62.md` condition 4, the selection line does not either. I
  checked every sentence on the page mentioning Vevor or the email: there is exactly
  one, the quotation itself.
- **No claim of its own.** ENSEMBLE makes no assertion about Vevor — not about its
  conduct, its product, its response, or anything else. It reproduces what the
  regulator published and marks that reproduction `[S]`. `PROTOCOL.md`'s legal-
  hygiene rule 1 ("every factual claim about a named third party … traceable to a
  cited primary source") is satisfied trivially and directly: the one claim present
  is CPSC's, cited to CPSC, not a claim the house is making about the firm.
- **CPSC's own permission.** Verified live today at
  `https://www.cpsc.gov/About-CPSC/Policies-Statements-and-Directives/Privacy-Policy`:
  the page states, verbatim, **"You may freely copy and distribute recall notices,
  including photographs of recalled items, without permission."** — matching the
  quotation given in the check exactly. The same page adds that "web page text,
  brochures, and posters presented on CPSC websites are public information. You may
  freely distribute, copy, or link to any of this information," with the caveat that
  reproduction must not suggest CPSC endorsement (the page's own `[S]` note states
  "CPSC has not endorsed this work," satisfying that caveat directly) and that
  licensed stock images (not at issue here — zero images ship) may carry separate
  restrictions.

**Risk as found: low.** The only third-party material on the page is a short,
verbatim, sourced quotation of a government recall remedy, explicitly covered by
CPSC's own published no-permission-needed policy for recall notices, carrying its
own non-endorsement disclaimer, with no independent claim of any kind made about the
named firm. This is a finding of fact, not a ruling on whether the house should name
a firm at all — that question is the Kritiker's, per the check's own framing, and
per `STAGING-RULING-62.md` condition 4, which already routes it there.

---

## D. `meta.json` and `README.md`

**`meta.json`.** Valid, well-formed JSON; parses cleanly with the standard library.
Same shape (`title`, `date`, `author`, `medium`, `embodies`) as
`works/2026-07-30-no-part/meta.json`, in the same key order. Every factual statement
checked against the same sources as section A:

- `"date": "2026-08-03"` — matches the state line's publication date and the
  candidate's own build date.
- `"RecallNumber 26591 (published 2026-07-02)"` — matches the JSON record (A2).
- `"reached by a committed, pre-published selection rule … with its discretion null
  and nothing skipped"` — matches A3.
- `"Its Remedies[0].Name field is quoted character for character, stray glyph
  included"` — matches A1.

**`meta.json`: HOLDS**, in full.

**`README.md`.** Every factual statement checked:

- The four-movement description matches the page's actual structure and
  `STAGING-RULING-62.md` §1's specification of it.
- The selection-rule paragraph — 55-record corpus, admissibility regex, 50 of 55,
  sort key, first-not-yet-taken, RecallNumber 26591, 0 records skipped — matches A3
  exactly, and (unlike the page itself, see A4) does **not** claim the 50 records
  "open with" the sentence; it correctly says they "match" the regex.
- The quotation section's 326-character length and `sha256
  b987f911…6b` match A1 exactly, and correctly attribute the stray `?` glyph to the
  source, not to the build.
- The "What was refused" list matches `STAGING-RULING-62.md` §4 items 1–7 one for
  one (internal file names; unsettled figures — brand-mark-on-object count, the
  25–31 photograph range, the 10–13 marker range; the publisher's name in movement
  II; every photograph; any collection surface; every link inside the nine clauses;
  navigation/credits/about/extra hairlines/second byline).
- The pointer to `projects/cpsc-recall-channel/` for the working record is accurate
  — this is that directory.

**`README.md`: HOLDS**, in full. (Note for the record: `README.md` is the one place
in this campaign that states the corpus figure without the "open with" overstatement
found on the page itself in A4 — the page's phrasing is a build-time addition not
present in `README.md`'s own account of the same figure.)

---

## E. The technical contract (`SITE-API.md`)

Checked directly against `candidate/`'s three files:

- **Top-level files only.** `candidate/` contains exactly `index.html`, `meta.json`,
  `README.md` at top level; no subdirectory exists inside `candidate/`.
- **No `<script>`.** Zero matches for `<script` in `index.html`.
- **No inline `style=`.** Zero matches for a ` style=` attribute; all styling is in
  the single scoped `<style>` block under `.work`.
- **No inline event handlers.** Zero matches for an `on[a-z]+=` pattern that is an
  actual attribute (the only near-hit is the `content=` attribute of the viewport
  `<meta>` tag, not a handler).
- **No external request.** The only external references are four `href="https://
  www.cpsc.gov/…"` / `"https://www.saferproducts.gov/…"` links — anchors, not
  fetched resources. No `<img>`, `<link>`, `@import`, or script-initiated request of
  any kind.
- **No `data:` payload.** Zero matches for `data:` anywhere in `index.html`
  (consistent with "zero images ship").
- **Self-contained.** The page has no dependency outside its own three committed
  files.
- **Byte size.** `index.html` 8,530 bytes; `meta.json` 1,037 bytes; `README.md`
  3,527 bytes (13,094 bytes total) — well under the 30 KB ceiling
  `STAGING-RULING-62.md` §6 sets for `index.html`, and in the intended contrast with
  `works/2026-07-30-no-part/index.html`'s 1,962,815 bytes.

**E: HOLDS**, in full.

---

## Contradictions found elsewhere in the project

None. `README.md`'s account of the "50 of 55" figure (A4/D) is, if anything, more
careful than the page's own sentence — it does not itself carry the "open with"
overstatement, so no other file in the project needs correcting; only the one
sentence on the page (`index.html`, movement IV, last paragraph) does, and per the
brief I report it rather than edit it.

---

*Written 2026-08-03, session 62, by the Verifier. One file written in this
repository: this one. `candidate/index.html`, `candidate/meta.json`,
`candidate/README.md`, `THE-SCORE.md`, and `observation/build-page-62.py` were read
only, never edited.*
