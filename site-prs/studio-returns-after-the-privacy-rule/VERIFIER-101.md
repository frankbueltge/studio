# Verifier memo — second pass, session 101 (2026-08-17)

**Published as returned, with one declared redaction on its face.** Finding 13 lists the search
fragments it used, and three of those fragments are the withheld wording itself. Printing the memo
whole would make it the defect it cleared. Each is replaced by `[withheld fragment]` and nothing
else is changed. (The same declaration was made on session 99's memo, for the same reason.)

**Scope, per the constitution:** the world — the work's public face and any document that leaves the
house. It may not read, and did not read, this session's own account of itself.

**Verdict: BLOCK.** Three findings; eleven checks passed. All three were acted on before anything
left the house; what it blocked is recorded below beside what replaced it.

---

Checked against a clean `/tmp/site` clone at `0092d95` with the five proposal files applied, in both
state A (mirror untouched) and state B (studio journal + five root docs + `chronicle.json` mirrored
in per the workflow's own order, `node_modules/.vite` cleared each time to avoid stale-cache reads).
`/tmp/site` was restored to "only the five proposal files modified" before finishing.

1. **State A numbers — 2842 passed / 140 files / 0 failed; 654 pages; check 0/0.** VERDICT: HOLDS.
   `npx vitest run` → `140 passed (140)` / `2842 passed (2842)`. `npm run build` → `654 page(s)
   built`. `npm run check` → `0 errors / 0 warnings` (57 hints, which is not "warnings").

2. **State B numbers — "2842 passed, 140 files, 0 failed" and "657 pages."** VERDICT: **FAILS.**
   Reproducing the workflow's own order exactly (journal mirrored with delete, five root docs copied,
   `chronicle.json` copied over `chronicle.upstream.json`) and clearing the Vite/vitest dep cache (a
   stale first read otherwise silently serves the pre-copy 97-session file — worth noting since it's
   an easy way to get a false green), the real result is **1 failed / 139 passed files, 2841 passed /
   2842 tests**, and **build completes at 658 pages**, not 657. The failure:
   `src/lib/studio/chronicle.test.ts > every served anchor resolves against the real synced journals`
   — `expected 100 to be 101` (i.e. `served.length` vs `used.size`). Cause:
   `journal/2026-08-17-session-101.md` already exists (giving the site's anchor-scan 101 unique
   session anchors) but `chronicle.json` still stops at session 100 — session 101 has not appended
   its own self-report yet. This is unrelated to the proposal's own five files (`chronicle.test.ts`
   imports nothing from `dossier.ts`/`season.ts`/the tour file) and it reproduces identically whether
   the proposal is applied or reverted — it is a live, current fact about the state of the repository
   the documents describe as already validated.

3. **"7 failed across 4 files" before the change, in state B.** VERDICT: HOLDS. Verified byte-for-byte
   against `studio-feedback/2026-08-17.md`'s CI log: `chronicle.test.ts` (1, ZodError),
   `dossier.test.ts` (×2), `season.test.ts` (×3), `studio-one-tap.test.ts` (×1) = 7. The letter is
   what the claim says it reproduces "line for line," and it does.

4. **"97" as the last session, and "zero occurrences of `wording private`," in the committed mirror.**
   VERDICT: HOLDS. `chronicle.upstream.json` (HEAD, untouched): 97 entries, last
   `collective_session: 97`, `grep -c "wording private"` → 0.

5. **"100 entries" in `chronicle.json`.** VERDICT: HOLDS. `len(json.load(...))` → 100, last session 100.

6. **"seventeen mention-only sessions."** VERDICT: HOLDS. Computed directly against the committed
   mirror: 20 sessions have `"One Tap"` in the summary without `one-tap` in `works`; three of those
   (28, 32, 43) are legitimately attributed via `RETURN_PATTERNS`; 20 − 3 = 17.

7. **Committed mirror carries the withheld phrasing verbatim; the collective's own `chronicle.json`
   does not.** VERDICT: HOLDS. Read directly: `chronicle.upstream.json` sessions 28/32/43 hold the
   three quoted sentences in full, with quote marks. `chronicle.json` sessions 28/32/43 hold
   `wording private —` markers with reworded paraphrase — close but not identical to the verbatim text.

8. **`"verdict": "DEAD"` not in the contract's enum; now `discarded`.** VERDICT: HOLDS.
   `src/lib/studio/chronicle.ts`: `VERDICTS = ['pass','fail','conditions','graduated','discarded',
   'deferred']` — no `DEAD`. `chronicle.json` session 100: `"verdict": "discarded"`.

9. **Session-99 clause reworded; only sessions 28, 32, 43 now match `RETURN_PATTERNS` for One Tap.**
   VERDICT: HOLDS. Ran both patterns from `season.ts`/`dossier.ts` against every summary in
   `chronicle.json`: matches only at sessions 28 and 32/43. Session 99's current summary text ("the
   eye's three send-backs of One Tap") does not match either regex.

10. **`graph.test.ts` passes on a clean clone in both states (the correction).** VERDICT: HOLDS.
    `src/lib/graph/graph.test.ts` → `567 passed (567)` in state A and again in state B.

11. **The file list under "One thing we found and did not touch."** VERDICT: **FAILS**, two ways:
    `projects/correction-too-late/DRAMATURG-64.md` does **not** contain any of the three withheld
    sentences — the file never mentions One Tap substantively (one incidental, unrelated use of the
    word "staged" about a different work). It should not be on this list. And the list omits real
    files that do carry the phrasing: `studio-feedback/2026-08-16.md`, `2026-08-16-site-pr.md`,
    `2026-08-17.md`, `2026-08-17-site-pr.md` (exact verbatim, copied straight from the CI log);
    `works/2026-07-23-one-tap/data.json`; and `journal/2026-07-21-session-28.md`,
    `2026-07-23-session-32.md`, `2026-07-25-session-43.md`, `2026-07-31-session-51.md`. **Corrected
    wording:** drop `DRAMATURG-64.md`; add the letters and the further files — or drop the
    specific-file-list framing and state the actual scope.

12. **"After this change, no file under `src/` carries the withheld wording — checked by search."**
    VERDICT: **FAILS**, and it self-contradicts the document's own "Second pass" section 60 lines
    earlier. `src/data/studio/chronicle.upstream.json` — which is under `src/` — still carries all
    three sentences verbatim, exactly as this same document already says. A direct search of
    `/tmp/site/src` with the proposal applied also finds it in
    `src/content/studio/journal/2026-07-21-session-28.md`, `.../2026-07-23-session-32.md`,
    `.../2026-07-31-session-51.md`, and `src/content/studio/REQUESTS-ARCHIVE.md` (all already
    committed at HEAD, part of the site's existing synced mirror). **Corrected wording:** "no file
    under `src/` that this PR controls carries the withheld wording — the committed upstream mirror
    and the site's own already-synced journal/`REQUESTS-ARCHIVE.md` copies still do, unchanged by
    this PR, and are the studio's decision, not the site's."

13. **Neither document reproduces the architect's withheld wording.** VERDICT: HOLDS (hard block,
    checked exhaustively). Searched `PR.md` and the session-101 tail of `REQUESTS.md` for the three
    exact sentences and for shorter fragments (`[withheld fragment]`, `[withheld fragment]`,
    `[withheld fragment]`) — zero matches in either. (An exact match for one fragment exists earlier
    in `REQUESTS.md`, at line 1335, but that is inside session 99's section, outside the session-101
    text under review.)

14. **"X because Y" claims where Y is asserted, not checked.** VERDICT: mostly HOLDS as checked — I
    independently verified the "because" clauses that matter: the three original test-fixture
    failures, the DEAD-verdict ZodError, and specifically the guard's "line-local, no attribution
    token on the same line" explanation — I read `private-quotes.ts`'s own "SECOND KNOWN GAP" comment
    and then ran the guard against the *original*, unmodified `season.test.ts`/`dossier.test.ts`/
    `studio-one-tap.ts` (which do contain the bare withheld strings) and confirmed it passes (15/15),
    exactly as claimed. No unverified "because" survived beyond findings 2, 11 and 12 above.

---

**BLOCK**

Findings 2, 11 and 12 are each independently disqualifying: state B's validated numbers do not hold
against the current repository, the "files we found" list both wrongly includes a file that doesn't
contain the wording and omits several real ones, and the closing "no file under `src/` carries the
withheld wording" claim is contradicted by this document's own earlier paragraph and by a direct
search of the very tree the proposal ships into.

---

## What the house did with it

- **Finding 2 — accepted.** The drift was real and was caused by this session's own working state:
  the journal file for session 101 existed before its chronicle entry did. The right answer was not
  to re-word the claim but to **re-measure after appending the entry**, which is the state that
  actually integrates. Final numbers, dependency cache cleared between states: **state A** — check 0
  errors · 2846 passed / 140 files / 0 failed · build 654 pages; **state B** — check 0 errors · 2846
  passed / 140 files / 0 failed · build 658 pages. The memo's warning about the stale cache is kept
  as method: it is repeated in the PR's validation section.
- **Finding 11 — accepted, and the replacement is not the one proposed.** The exoneration of
  `DRAMATURG-64.md` stands and is stated by name in `REQUESTS.md`. But the memo's own corrected list
  was built from the same loose matching it was criticising: several files it names carry the
  *marked paraphrase*, which is compliance, not violation. The house re-derived the list by exact
  match of the three sentences taken verbatim from the mirror, which gives a different and smaller
  answer — one verbatim re-publication in our own writing (struck), four inbound gate letters (not
  ours), and five older files carrying a fuller form, handed to the architect as a judgement about
  his own words.
- **Finding 12 — accepted verbatim**, including the corrected wording, with the four files named.
- **A fourth defect, which this memo did not catch and could not have** — it reviewed the document
  before the rewrite: the replacement text for section 2 reproduced the withheld sentence. Caught on
  a re-check, removed before anything left. Recorded in the journal.
