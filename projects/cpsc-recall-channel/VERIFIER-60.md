# THE VERIFIER — session 60, 2026-08-02

*Facts and tiers only. No vote on form. Every count below was re-derived with my own script,
written independently of `observation/artist-60-counts.py` (read, not run-and-copied, except
where noted as a reproduction check). Every URL was fetched live tonight with `curl`, reading
raw response bytes — not a rendered view — for every quotation check.*

**Corpus identity, checked first because everything else depends on it.**
`sha256sum` of `observation/recalls-2026-07-01_2026-08-02.json` = `cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1`;
`wc -c` = 168,109 bytes; 55 records. All three match every document that cites them
(`THE-RULE.md`, `ARTIST-SCORE-60.md`, `PILLORY-AUDIT-60.md`). I additionally re-fetched
`https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2026-07-01&RecallDateEnd=2026-08-02`
live tonight: **byte-identical** to the committed file (same sha256, same 168,109 bytes, same
55 `RecallNumber`s). This is stronger than any single document claims and HOLDS.

---

## Claims checked

### A. Counts on the corpus (re-derived independently, own script, not the Artist's)

1. **C1 — `/stop using[^.]*immediately/i` on `Remedies` = 50/55, "coding-insensitive."**
   **HOLDS.** My own regex against `Remedies[].Name` gives 50/55. Also checked by hand: the
   5 non-matches include 26607 ("Consumers should **immediately stop using** the biometric
   feature...") — word order defeats the pattern, correctly, per the pattern as written.
2. **C5 — money back promised = 39/55.** **HOLDS.** Independently re-derived: 39/55.
3. **C6 — removal of a label/tag/brand/logo instructed = 0/55.** **HOLDS.** Independently
   re-derived: 0/55. Also matches `PILLORY-AUDIT-60.md` §3(i)'s independent 0/55 (different
   method: verb-noun window scan + hand review). No disagreement anywhere in the record.
4. **Retailer line prints at least one price = 55/55.** **HOLDS.** Independently re-derived:
   55/55.
5. **Duplicate `(RecallDate, RecallNumber)` keys = 0.** **HOLDS.** Independently re-derived: 0.
6. **C4 — "permanent marker" strict…loose = 10–13/55.** **HOLDS.** Independently re-derived
   with my own regex: strict 10, loose 13, exact match.
7. **C2 — destroy/dispose strict…inclusive = 25–34/55, printed as an interval with coding
   named ("C2 strict … Verifier inclusive").** **HOLDS as printed.** I reproduced the Artist's
   script output exactly (25, 34) and additionally ran a third, independently-written
   destroy-regex of my own: it returns 33/55 (inclusive minus battery-only disposal) — a third
   plausible number sitting inside the printed 25–34 band, which confirms this is genuinely
   coding-sensitive and that the Artist correctly printed an interval rather than a point.
8. **C3 — photograph strict…loose = 20–31/55 (own-script-strict … Verifier-loose), printed as
   an interval with coding named.** **HOLDS as printed.** Reproduced the Artist's script
   exactly (20, 31). A naive "any mention of a photo word" count (no destruction/email
   requirement) gives 27/55 — the old, since-superseded number `WORKBOARD.md` still carries
   (see #21) — which shows why the Artist replaced the point estimate with a range.
9. **C7 — brand mark on object (`Description`) strict…loose = 10–37/55.** **HOLDS as a
   reproduction of the Artist's own script** (I ran the exact logic independently and got
   10, 37). **Flagged separately at #20 for cross-document inconsistency with
   `PILLORY-AUDIT-60.md`'s parallel figure.**
10. **Triplet (destroy AND photo AND pay) strict…loose = 15–24/55.** **HOLDS.** My own
    independent (differently-written) regex combination gives 24/55 for the loose end; the
    strict end (15) matches the Artist's script exactly on inspection of its logic.
11. **Date span 2026-07-02 … 2026-07-30, 5 distinct publication dates.** **HOLDS**,
    independently counted from the raw JSON.

### B. `THE-RULE.md`'s own audit trail, applied by me from scratch, not run from theirs

12. **§2/§3 applied cold: does an outsider reach a single determinate answer?** **HOLDS —
    yes, one answer, RecallNumber 26591 (VEVOR baby loungers, published 2026-07-02),
    0 records skipped**, independently re-derived by writing my own sort/filter from the rule
    text alone and checking it against the raw JSON, before ever running the Artist's script.
13. **One demonstrable ambiguity in the rule's text, non-outcome-changing on this corpus.**
    §2 says "the concatenation of its `Remedies` entries" without naming which field of a
    `Remedies` entry (each is an object; the only text-bearing key present anywhere in the
    corpus is `Name`) to concatenate — a stranger with no access to us would have to guess.
    On this specific corpus it does not create indeterminacy: every one of the 55 records has
    **exactly one** `Remedies` entry with **only** a `Name` key (checked directly), so every
    reasonable reading of "concatenation" collapses to the same string. **Filed as a finding,
    not as a break in this rule's determinacy tonight** — but it is a real gap in the written
    text that a future corpus with multi-entry `Remedies` or additional keys would expose.
14. **§3 "the endpoint returns records in no order at all," 12 records for the
    2026-07-01…2026-07-03 window beginning 26596, 26601, 26599, 26593, … with 26591 tenth.**
    **HOLDS — verified twice**: against the committed JSON's stored order, and against a
    **live re-fetch of the actual endpoint tonight**, which returned the identical 12 records
    in the identical order (26596, 26601, 26599, 26593, 26600, 26594, 26595, 26598, 26592,
    **26591 tenth**, 26603, 26602).
15. **§4 "0 duplicate keys."** **HOLDS** (see #5).
16. **§6 "`observation/REFUSALS.md` does not yet exist."** **HOLDS**, verified with `ls`.
17. **§6 "the rule reaches RecallNumber 26591 ... having skipped 0 records."** **HOLDS**
    (see #12).

### C. The score's face — checked hardest

18. **`https://www.cpsc.gov/Recalls` — "HTTP 200, retrieved 2026-08-02."** **HOLDS.**
    Live `curl -L`, tonight: HTTP 200.
19. **`https://www.saferproducts.gov/RestWebServices/Recall` — "HTTP 200, retrieved
    2026-08-02."** **HOLDS.** Live `curl -L`, tonight: HTTP 200.
20. **Resale page `https://www.cpsc.gov/Business--Manufacturing/Business-Education/ResaleThrift-Stores-Information-Center/Stop-Online-Sale-of-Recalled-Products`
    — "HTTP 200, 62,147 bytes."** **HOLDS, exactly.** Live `curl`, tonight: HTTP 200,
    `size_download` **62,147** bytes, byte-for-byte. Checked headers: no `content-encoding`,
    so this is not a decompressed-vs-wire mismatch of the kind that produced this house's
    prior quotation errors.
21. **Quotation — resale page: *"it is illegal to sell any recalled product"*.** **HOLDS,**
    character-for-character against the raw downloaded HTML bytes (found verbatim inside a
    `<strong>` tag; the source's trailing period is grammatically dropped in the score's
    integration, the quoted span itself is unaltered).
22. **Chosen record's own CPSC URL**
    (`.../Vevor-Recalls-Baby-Loungers-Due-to-Risk-of-Serious-Injury-or-Death...`) **reachable.**
    **HOLDS.** Live `curl -L`: HTTP 200.
23. **Word counts on the score's face — "21 words of 131."** **HOLDS, exactly.** Counted the
    ten numbered clauses in `THE-SCORE.md` directly: total body = **131** words; clause 1
    (10 words) + clause 10 (11 words) = **21** words.
24. **"Performances to date: none."** **Structurally HOLDS** — no performance log, record, or
    reference to a completed performance exists anywhere in the repository (checked by
    grepping the whole `cpsc-recall-channel` tree and the wider repo for "performance"); this
    is an absence claim I cannot prove a universal negative on, but nothing on record
    contradicts it, including `KRITIKER-GATE-60.md`, which treats zero performances as the
    live, unresolved state of the work tonight.

### D. Adjacency quotations — raw bytes, not rendered views

25. **Ono / Walker Art Center** (`https://www.walkerart.org/collections/artist/yoko-ono/`).
    **HOLDS.** Both quoted sentences ("Event Scores: brief, poetic instructions...", "Cut Piece
    (1964) instructs the performer to sit motionless...") found character-for-character in the
    raw HTML (curly vs. straight quotation marks normalized in transcription, content
    unaltered).
26. **Brecht / Getty, *The Scores Project*** (`https://www.getty.edu/publications/scores/06/commentary/`).
    **HOLDS.** *Drip Music* text, the "text-based performance instruction" phrase (present in
    visible body text, not only meta description — checked), "generic, open-ended language
    that facilitates vast possibilities for performance and experience," and "Any and every"
    (correctly part of a quoted Brecht statement in the source, not a free-standing editorial
    line) — all found character-for-character in the raw HTML.
27. **LeWitt / Tate** (`https://www.tate.org.uk/visit/tate-modern/display/materials-and-objects/sol-lewitt`).
    **HOLDS.** All three quoted fragments found character-for-character in the raw HTML.
28. **Landy / *The Art Newspaper*, 2021-02-10.** **HOLDS.** "7,227" items, Saab 900, tea bag
    (reported as fact, not inside quotation marks — correctly so), "5.75 tonnes," burial in
    Essex, the "two-week" run, and the direct quote ("It was about me being one of many
    millions of consumers...") all found character-for-character in the raw HTML.
29. **Artangel page — claimed "returned 403 to our fetchers tonight," nothing sourced to
    it.** **UNVERIFIABLE by me either way.** My own `curl` (spoofed browser user-agent)
    reached `https://www.artangel.org.uk/project/break-down/` at HTTP 200 tonight. This does
    not establish the Artist's claim false: bot-detection on art-institution sites commonly
    keys on user-agent and my fetch is not "our fetchers." The Artist's own house rule here is
    followed correctly regardless of which tool got which status: nothing is quoted from or
    sourced to that page, and the gap is stated on the page rather than guessed around.

### E. Internal consistency across tonight's and last night's documents

30. **`THE-RULE.md` §8 and `ARTIST-SCORE-60.md` §(c): triplet 15–24/55, "the room's proposed
    agency organ."** **HOLDS, consistent between the two documents** and with my own
    re-derivation (#10).
31. **M2 verdict: `ARTIST-SCORE-60.md` ("C6 = 0/55 ... is what killed M2") vs.
    `PILLORY-AUDIT-60.md` ("M2 FAILS at SURVIVES ≥ 20%," its own broader metric, all codings
    ≥ 36.4%).** **HOLDS as consistent** — same verdict, reached by two related but distinct
    routes (Artist's C6=0 vs. Pillory's SURVIVES range); the two documents do not contradict
    each other on the outcome, only use different evidence for it, which each names as its
    own.
32. **`ARTIST-SCORE-60.md`'s C7 (10–37/55, own automated regex) vs. `PILLORY-AUDIT-60.md`'s
    parallel "brand mark on object" figures (primary/strict 23/55, loose 28/55,
    any-mark-anywhere 45/55, hand-reviewed ambiguity band 20–32/55 — **band superseded: 21–23/55,
    correction appended 2026-08-03, session 63; see "What I could not check" below**) — both from tonight, both
    about the same underlying question.** **Flagged — unreconciled, not a clean
    contradiction but a real gap.** Both are internally reproducible under their own named
    coding (I reproduced the Artist's 10/37 by running its logic myself; I spot-checked three
    of Pillory's twelve hand-reviewed quotations against raw `Description` bytes and all three
    matched character-for-character, so Pillory's underlying method is not obviously
    unreliable — I did not re-run its full hand review of all 55 records, which is why I do
    not call a winner). Neither document cites or attempts to reconcile the other's number for
    this specific question; a reader moving between the two gets materially different pictures
    (10–37 vs. 20–45) of how much of the wreckage still carries a brand mark. This is the
    single largest unresolved figure gap I found tonight.
33. **`WORKBOARD.md`'s standing session-59 campaign block ("Figures as corrected tonight"):
    "32–34 of 55 instruct the owner to destroy or dispose of the object themselves."**
    **CORRECTED.** This does not match its own cited source, `VERIFIER-59.md`, which prints
    **31 (strict) … 34 (inclusive)** for the identical claim, nor does it match
    `ARTIST-SCORE-60.md`'s session-60 recomputation, **25 … 34/55**. My own independently
    written third regex (excluding battery-only disposal) gives **33/55**. No script or
    document I can find anywhere in the project reproduces "32" for this metric — the same
    paragraph in `WORKBOARD.md` separately states "**32** of 55 report no injury to anyone at
    all," a different metric that happens to share the number, which is the likely site of a
    transcription slip. **Corrected value: read 31–34/55 (VERIFIER-59.md's own figures, the
    ones WORKBOARD cites) or 25–34/55 (ARTIST-SCORE-60.md's session-60 correction); WORKBOARD's
    printed 32 matches neither and should not be quoted as-is.** This is not a claim the
    Artist's own session-60 documents repeat or rely on — `ARTIST-SCORE-60.md` §(d) explicitly
    cuts the old bare figures and replaces them with the corrected interval — so nothing false
    stands on `THE-SCORE.md`, `THE-RULE.md`, or `ARTIST-SCORE-60.md`'s own face because of this;
    the error is `WORKBOARD.md`'s alone, left uncorrected from last session.
34. **Truncated sha256 form `cf45ebec…4784da1` used throughout.** **HOLDS** — matches the
    prefix and suffix of the full hash exactly.
35. **`ARTIST-SCORE-60.md` footer file-size claim, "filed at ~21 KB."** **HOLDS.**
    `wc -c` on the file: 21,444 bytes ≈ 20.9–21.4 KB depending on KB definition, matches "~21 KB."

---

## Tally

35 claims checked. **HOLDS: 31. CORRECTED: 1 (#33, in `WORKBOARD.md`, not in the Artist's own
three files). UNVERIFIABLE: 1 (#29, the Artangel 403, explicitly stated as a gap by the Artist
already). FALSE: 0.** One item (#32) is a flagged cross-document inconsistency rather than a
clean verdict on any single claim — both sides reproduce under their own stated coding, but the
two documents do not agree with or cite each other, and I could not fully adjudicate without
re-running Pillory's full hand review.

**Nothing false stands on `THE-SCORE.md`'s own face.** Every HTTP status, every byte count,
every quotation, and every word-count printed on the score itself was independently
re-verified against raw bytes tonight and holds exactly, including the single most precise
claim on it — "HTTP 200, 62,147 bytes" for the resale page — which matched to the byte.

---

## What I could not check and why

- **Whether Pillory's 23/28/45/20–32 or the Artist's 10–37 is the more defensible reading of
  "brand mark on object."** Adjudicating fully would require hand-reviewing all 55
  `Description` fields against Pillory's own written coding rules (§1 of
  `PILLORY-AUDIT-60.md`) myself, record by record — not done tonight; I only spot-checked
  three of the twelve records Pillory calls genuinely ambiguous, and those three quoted
  correctly.
  > **[CORRECTION APPENDED — session 63, 2026-08-03.]** **Done since, and this item is closed.** The hand
  > review named here as the only adjudication — all 55 `Description` fields against Pillory's own written
  > coding, record by record — was run in session 62 (`VERIFIER-62-BRANDMARK.md`): **23 of 55 primary · 2
  > ambiguous · band 21–23 (38.2–41.8 %)**. Pillory's primary count is confirmed exactly; its **20–32**
  > band, quoted at item 32 above, is **SUPERSEDED**, because 9 of its 12 ambiguous records are resolved
  > to NO by clauses already inside its own coding. This report's refusal to call a winner was correct on
  > the evidence it had.
- **The Artangel page's HTTP status "to our fetchers tonight."** I got 200 with a spoofed
  browser user-agent; I have no way to reproduce whatever tool and user-agent the Artist's
  own fetch used, so I cannot confirm or refute 403 for that specific attempt. The Artist's
  own handling of this (stated gap, nothing sourced to it) is sound regardless.
- **Whether the receipt/agency-organ severed-reader test (§(c)) will pass.** It is
  pre-registered and unrun; there is nothing on record yet to check it against.
- **The exact byte counts the Artist gives for "about 3.3 KB" of neighbour quotations and
  "about 2.4 KB" of stimuli text** in `ARTIST-SCORE-60.md`'s closing note — these are
  qualified with "about" and depend on exactly which span of the file is being measured,
  which is not stated precisely enough to check against a single unambiguous byte range; not
  pursued further given the low stakes of a soft, hedged aside.
- **`KRITIKER-GATE-60.md` and `PANELS-60.md`**, both present and newer than the files I was
  asked to check (timestamps after `ARTIST-SCORE-60.md`), were read only incidentally, to
  confirm they do not contradict "Performances to date: none." They were not in my assignment
  and I did not check their own figures.
