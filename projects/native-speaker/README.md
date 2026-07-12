# Native Speaker — increment 1

**This is a prototype, not a premiere.** The concept passed the Kritiker's session-06 gate with
four binding conditions (see `../../memory/dossiers/native-speaker.md`). This build is the
terminal: a self-contained interactive border-control fiction whose meter is real code, not a
scripted flip. Revised in session 08 for the team's named-individuals policy and the conductor's
Minnesota correction (both below); `data.json` is conductor-owned and was applied verbatim.

Open `index.html` directly in a browser — no build step, no server, no external requests. Every
VERIFIED figure, case, URL and caveat on the page is read at runtime from the
`<script type="application/json" id="data-island">`, which is `data.json`'s content embedded
byte-identical — nothing in `data.json` was edited or retyped for display.

## What this is

A fictional "English Verification Gate" that asks a visitor to describe their morning twice:
once quickly, the way they'd text a friend, and once as if English were a second language
learned carefully at fifteen. A live meter — the studio's own deterministic, disclosed
reconstruction of the documented AI-detector mechanism, not a commercial product — scores both
samples with the same unmodified function. The gate then opens a verdict card that puts the
visitor's own two scores next to the real research record: a population study where 89 of 91
non-native essays were flagged by at least one of seven detectors; an institution that logged
roughly 6,000 misconduct allegations in a year before abandoning its AI detector; a student
whose suspension after a detector flag is being litigated right now; and the finding that in the
cases retrieved here, no court reviewed the machine's judgment of a human's words itself. The
border-checkpoint dramaturgy is fiction. The figures underneath it are not.

## Naming policy (team steer, 2026-07-12)

No personal names in this work's own voice — headlines, dramaturgy, verdicts, body prose. People
appear as role + institution + consequence. Personal names survive only as citation text inside
linked sources (official case captions, bylines), where they are evidence, not spectacle.
Companies and tools are named where every claim is traceable to a cited primary source. The
policy statement is rendered verbatim from `data.json.naming_policy` in the work's honesty
panel, and this README follows the same rule: case captions appear only in citation lines.

## The three tiers on this page

- **VERIFIED** — taken from the research wing's record (`data.json`, extracted and revised
  first-hand by the conductor from upstream instrument 001 and the claims ledger): the Liang et
  al. 2023 detector study, the institutional scale case, the Yale detector case, the boundary
  case, the legal-void framing, the counter-evidence, the short-text caveat. Every one of these
  is read from the data island at runtime and rendered verbatim or near-verbatim — never retyped
  as a bare literal in the JS logic. No personal name appears as a literal anywhere in the
  page's script; the case captions are read from the island's `caption` fields.
- **RECONSTRUCTION** — the meter itself (`scoreText()`). Not GPTZero, not Turnitin, not any
  commercial detector: a deterministic, in-browser rebuild of the documented
  perplexity-and-burstiness-style mechanism, built by this studio so the mechanism can be
  experienced and checked rather than taken on faith. Its verdict proves nothing about any one
  visitor; the VERIFIED figures above it prove the pattern at population scale.
- **IMAGINED** — the border-checkpoint premise, the gate's voice, the prompts, the stamps, and
  the two self-test sentences. Marked as fiction on the work's face (tier legend on the gate
  screen, and again in the honesty panel).

## The two cases on the verdict card — and the one deliberately not on it

- **The scale case (VERIFIED):** Australian Catholic University, 2024 — roughly 6,000
  academic-misconduct allegations (around 90% AI-related); about 25% dismissed; a Deputy
  Vice-Chancellor called the figures "substantially overstated"; the university abandoned
  Turnitin AI detection in March 2025. Rendered first on the card, before the individual case.
- **The detector case (VERIFIED, strictly PENDING):** an EMBA student at Yale School of
  Management, a French national writing in his second language — one-year suspension and a
  failing grade after a GPTZero flag; his federal lawsuit is pending (D. Conn. 3:25-cv-00159),
  injunction denied May 2025. The amber discipline note ("PENDING — never state as decided")
  sits on the card itself. Citation: Rignol v. Yale (pending), Yale Daily News.
- **The boundary case (VERIFIED — deliberately NOT on the verdict card):** the most widely
  reported consequence case — a PhD student expelled from the University of Minnesota, visa
  revoked, expulsion upheld on appeal in February 2026 — is *not* presented as detector harm,
  because the Minnesota Court of Appeals noted the disciplinary panel did not rely on
  AI-detection evidence (it credited graders' assessment, irrelevant sources, missing citations
  and inconsistent testimony). A work about machine judgment may not borrow stakes the record
  does not attribute to the machine. The case appears instead as its own honesty-panel block
  ("A case deliberately not on this card"), with the same typographic seriousness as the
  discipline notes, rendering the claim and note verbatim from
  `data.json.verified.case_minnesota_boundary`. Citation: Yang v. University of Minnesota
  (Minn. Ct. App., Feb 2026), Minnesota Lawyer. Per the island's `note`, the appellate framing
  was reported upstream to the research wing on 2026-07-12, whose instrument 001 lists this case
  in its harm register.

## Load-bearing caveats

- **Union statistic, not a single detector:** 97.8% (89 of 91) is the share of TOEFL essays
  flagged by *at least one of seven* detectors — the copy never says "one detector flagged
  97.8%."
- **Mean, not per-tool:** 61.22% is the *average* false-positive rate across the seven detectors
  studied; it is never attributed to a named tool.
- **Population effect, not a per-visitor guarantee — the non-flip is designed in:** if a
  visitor's careful second attempt comes back ADMITTED, the verdict card opens with the grace
  copy from `data.json`'s `tally.non_flip_disclosure` ("89 of 91 flagged means 2 walked
  through... it makes you one of the two") — the dramaturgy has no dead end and no disappointment
  framing in that branch. Verified live in this build (see below).
- **The Yale case: always pending, never decided.** The verdict card carries the discipline
  string verbatim, on its face.
- **The Minnesota correction:** see "the boundary case" above — that consequence may not be
  presented as detector harm, and this work does not.
- **Counter-evidence is load-bearing, not a footnote:** a 2026 Czech-language study found no bias
  (its detectors don't key on perplexity), and Turnitin's own research reports no significant
  bias against English-language learners at 300+ words — and Turnitin was not one of Liang's
  seven detectors. The verdict card gives this one line plus a pointer to the honesty panel,
  which carries all three counter-evidence claims and both sources in full. "Documented, not
  universal."
- **Short-text gap:** texts under the meter's 8-word floor show `INSUFFICIENT SAMPLE` with the
  sourced Turnitin note that short documents carry a larger false-positive gap than the
  document-level claim covers.

## The four binding Kritiker conditions, and how increment 1 answers each

1. **The honest meter — computed live, never a scripted flip.** `scoreText(text)` is a pure
   function between the `// ENGINE-BEGIN` / `// ENGINE-END` markers in `index.html`. It takes
   *only* a text string — no attempt number, no prompt text, no global state, no `Date`, no
   `Math.random`. Verified with `node`: identical input produces byte-identical output every
   time (stronger than "seeded" — deterministic), and the function's arity is checked to be
   exactly one argument. Both attempts call the same function; the live gauge updates on every
   keystroke. The session-08 revision did not touch a single character between the engine
   markers — re-verified after the edit.
2. **The non-flip is designed and disclosed.** See "Load-bearing caveats" above. Verified live in
   a full Playwright run: attempt 2 scored deliberately below threshold, and the grace banner
   opened the verdict card with the exact `tally.non_flip_disclosure` text before anything else
   rendered. The running tally (`localStorage['native-speaker-tally']`) carries the aggregate
   argument, with the honesty panel stating its scope is "this terminal only... never
   transmitted."
3. **The legal hook, reframed — and now scoped on the card.** The verdict card and honesty panel
   render the revised `verified.legal_void.claim_frame` verbatim: Article 50 governs *providers
   marking machine output*; "in the cases retrieved here, no court reviewed the machine's
   judgment of a human's words itself — where consequences were challenged, review ran on whether
   the institution followed its own procedures, not on whether the detector was right." The
   scoping words ("in the cases retrieved here") now sit in the card copy itself — this
   discharges the Kritiker's increment-2 note 3 (a scoping word on the card) early, in
   increment 1.
4. **Statistic discipline.** 97.8% is rendered as the union figure with its own explanatory
   sub-line; 61.22% is only ever described as the seven-detector mean; the Yale case is rendered
   PENDING everywhere it appears (the card's discipline note and the island's single
   `discipline` string, so there is only one place this could drift).

## The meter mechanism

`scoreText(text)` → `{ score, components, words, verdict }`. `score` is 0..1, 1 = machine-ward.
`verdict` is `FLAGGED` iff `score >= THRESHOLD`, `ADMITTED` otherwise, or `INSUFFICIENT` under 8
words (no verdict rendered in that state; the gauge shows the sourced short-text note instead).

Five components, each 0..1, machine-ward high, combined by fixed weight:

| Component | Weight | What it measures |
|---|---|---|
| COMMONNESS | 0.34 | Share of tokens found in the embedded ~980-word common-English lexicon — a perplexity proxy. Constrained, careful vocabulary scores machine-ward; rare words, names and typos pull human-ward. |
| BURSTINESS | 0.22 | 1 − normalized rhythm variation: coefficient of variation of sentence lengths, combined with standard deviation of word lengths (word-length variation alone for single-sentence input). Even, careful rhythm scores machine-ward. |
| IRREGULARITY | 0.18 | Inverted presence of contractions, informal tokens (`gonna`, `lol`, `ugh`...), loose punctuation (`!!`, `...`, missing terminal punctuation, lowercase sentence start) and numerals. Their absence scores machine-ward. |
| DIVERSITY | 0.14 | 1 − moving-average type-token ratio (window ≤ 10 tokens). A narrow working vocabulary scores machine-ward. |
| REPETITION | 0.12 | Share of repeated bigrams. |

Weights sum to 1.00. `THRESHOLD = 0.55`, `MIN_WORDS = 8` — both named constants, shown on every
gauge on the page (the dashed threshold tick and its label), never hidden or varied per visitor.

The lexicon (`LEXICON`, ~980 lowercase common English words — function words, common
verbs/nouns/adjectives, and specifically the words a careful L2 writer reaches for: *morning,
breakfast, coffee, work, school, early, wake, eat, go, walk, take, bus, then, after, before,
because...*) sits between the engine markers, labeled in source as part of the disclosed
mechanism.

**Determinism, not seeding.** The engine has no random number generator and no clock anywhere in
it. "Same input, same output, always" is a stronger guarantee than "seeded, so reproducible with
the same seed" — there is no seed to lose or misapply.

**Attempt-blindness.** `scoreText` takes exactly one parameter. It has no way to know whether the
string it receives is attempt 1 or attempt 2, casual or careful, typed by a visitor or pasted
from the self-test strip. Verified by static check (`scoreText.length === 1`) and by scoring
identical strings from different call sites and diffing the JSON output.

**Calibration discipline.** All tuning (component weights within the brief's stated range,
burstiness normalization constants, the threshold) was done exclusively against the two embedded
self-test sentences — never against the gate's own prompt wording or any runtime visitor input.
The engine contains no string-matching against prompt text anywhere (checked by grep in the
verification pass below).

## Self-test

At page load, `scoreText` runs live on two IMAGINED sentences written by this studio (explicitly
not real TOEFL material):

- Casual: *"ugh, overslept again... skipped breakfast, chugged my coffee on the 8:15 and
  honestly? still half asleep lol"*
- Constrained: *"I woke up early in the morning. I ate my breakfast and drank a cup of coffee.
  Then I took the bus to my work."*

The always-visible strip above the honesty panel prints both computed scores and verdicts, the
threshold, and an `attempt-blind: PASS`/`FAIL` line (scores the casual string twice and compares).
If the constrained case ever fails to flag, or the two scores come back missing or equal, the
strip prints `SELF-TEST FAILED` honestly rather than faking a pass.

## Tally disclosure

`localStorage['native-speaker-tally'] = { tried, flagged }`, incremented once per attempt-2
submission (`tried` always, `flagged` only on a FLAGGED verdict). Rendered as "AT THIS TERMINAL: N
presented a careful sample; M were flagged as machine," with `data.json`'s `tally.scope` line
directly underneath: this-terminal-only, local, never transmitted — the aggregate argument is
carried by the VERIFIED population figures, not by this counter. If `localStorage` throws
(private browsing, storage disabled), the tally line reads "Tally unavailable on this device"
instead of crashing or silently showing zero.

## Upstream sources

- `data.json`'s `upstream.source`: field-research (Meridian) `works/2026-07-01-calibration-gap`
  (Instrument 001, Calibration Certificate) + `memory/claims.md` rows on detector bias, harm
  cases and the legal record. Revised 2026-07-12 (session 08).
- Live-status contract (`upstream.contract`, rendered in full in the honesty panel): live status
  travels with every derived element; load-bearing caveats survive re-voicing; corrections flow
  upstream, never silently sideways. If upstream revises or discards Instrument 001, this work
  updates on the same cycle or pauses. The Minnesota appellate framing was reported upstream on
  2026-07-12 (per the island's boundary-case `note`).
- Primary sources, all as visible plain-text links in the honesty panel and sources footer: Liang
  et al. 2023 (Cell Patterns / arXiv); the ABC News report on the Australian Catholic University
  figures; the Yale Daily News report (citation label: Rignol v. Yale (pending)); the Minnesota
  Lawyer report (citation label: Yang v. University of Minnesota (Minn. Ct. App., Feb 2026));
  the OIA and Turnitin pages behind the legal-void framing; the Czech-language study and
  Turnitin's ELL-bias research behind the counter-evidence; and Turnitin's short-text
  false-positive research.

## Verification run (2026-07-12, session-08 revision)

1. **Data-island byte-identity.** Extracted the text content of `<script id="data-island">` and
   diffed it character-for-character against the revised `data.json` in Python:
   `island length: 10370, data.json length: 10370 — MATCH`.

2. **Engine untouched + `node` test.** Extracted the block between `// ENGINE-BEGIN` and
   `// ENGINE-END` and ran the full suite under `node` after the revision:

   ```
   CASUAL       → score 0.378  verdict ADMITTED
   CAREFUL      → score 0.658  verdict FLAGGED
   THRESHOLD    = 0.55

   PASS — casual score below threshold
   PASS — casual verdict ADMITTED
   PASS — careful score at/above threshold
   PASS — careful verdict FLAGGED
   PASS — clean separation (careful > casual)
   PASS — same input -> identical output (JSON deep-equal)          [determinism]
   PASS — scoreText.length === 1 (only takes text)                  [attempt-blindness]
   PASS — attempt-blind: identical text scores identically
   PASS — 3-word input returns INSUFFICIENT                         [degenerate input]
   PASS — 8-word input (== MIN_WORDS) returns a verdict
   PASS — empty input returns INSUFFICIENT
   PASS — no functional match against prompt-specific words
   PASS — engine source does not reference attempt number / global state

   ALL CHECKS PASSED
   ```

   Scores identical to the pre-revision build — the engine was not touched.

3. **Union-figure regex.** `liang_2023.claim` is unchanged in the revised island; the card's
   parse regex still matches: captures `89` / `97.8%`, rendering "89 of 91 flagged — 97.8%".

4. **Naming-policy grep.** Searched `index.html` and this README for all four personal-name
   tokens from the steer: every hit in `index.html` is either an `<a>…</a>` citation label
   (two in the noscript block) or a `caption` string inside the data island (two, required
   byte-identity);
   zero hits in body prose, headers, dramaturgy or JS logic — the page's script contains no name
   literal at all (captions are read from the island's `caption` fields at runtime). A DOM-level
   walk of the rendered page confirmed every visible name occurrence sits inside an `<a>`
   element. This README's hits are the two captions in citation lines only.

5. **HTML well-formedness.** Parsed with Python's `html.parser`: no unclosed or mismatched tags.

6. **Live browser run (Playwright, headless, served over localhost).** Full flow: casual
   attempt 1 (ADMITTED) → careful attempt 2 (FLAGGED) → verdict card. Confirmed: the scale-case
   block (Australian Catholic University) renders first with its ABC News link; the detector-case
   block renders de-named ("An EMBA student at Yale School of Management...") with its amber
   PENDING discipline note; the reworded, scoped legal frame renders verbatim; the honesty panel
   shows the naming-policy statement and the "A case deliberately not on this card" block with
   role line, claim, upstream note and caption-as-citation-link; the sources footer labels are
   the official case captions read from the island. No `undefined` or `null` text anywhere in
   the rendered page; zero real console errors (only the dev server's harmless `favicon.ico`
   404). The non-flip grace-banner branch and the 360px-width no-overflow check were verified in
   the pre-revision build of this same session; the session-08 edit touched no layout or flow
   code paths beyond the blocks re-tested above.

7. **File size.** `index.html`: 1,506 lines, 74,555 bytes (74.6 kB). No external requests of any
   kind.

## Increment status

Increment 1 of the arc: **terminal** (this build, revised session 08) → bilingual polish →
premiere (the full gate, Kritiker gate re-run) → the physical turnstile, proposed through
`REQUESTS.md` per the studio's physical-realisation channel — a literal one-person barrier is
explicitly not in scope here and would need its own concrete torque/resistance/stop account, not
a paragraph bolted onto this README.
