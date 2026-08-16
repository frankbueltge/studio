# VERIFIER-99 — the outgoing package, session 99 (2026-08-16)

**Published as returned, with one class of redaction, marked.** Finding 1 required the Verifier to
name the three withheld sentences in order to search for them, and it named them in full. Printing
them here would make this memo the defect it just cleared — and would fail the site's own privacy
guard on the next run. So the three sentences are replaced below by `[withheld — the pre-redaction
wording of One Tap's Nth return]`, and **nothing else in this memo is altered**: no verdict, no
finding, no wording, no ordering. The conductor's own check (an independent script over every
removed span in `253c209`) agrees with finding 1 and is in the record.

*This is the honest shape of the conflict rather than a tidy one: the constitution says a
commissioned memo ships unedited, and the standing privacy rule says the architect's wording never
stands in this repository. Where they meet, the privacy rule wins and the edit is declared.*

---

VERDICT: PASS

1. BLOCKING — Neither outgoing document reproduces the withheld wording. Checked: located the three pre-redaction sentences via `git show 253c209 -- chronicle.json` in /home/user/studio ([withheld — the pre-redaction wording of One Tap's first return]; [withheld — the pre-redaction wording of One Tap's second return]; [withheld — the pre-redaction wording of One Tap's third return]), then grepped both PR.md and the final REQUESTS.md entry for these phrases and sub-phrases. Zero matches in either document. Also checked the five replacement source files under `files/` — they contain the redacted paraphrase text only (e.g. season.test.ts:139/141/144 assert the paraphrase, not the original). TRUE.

2. Commit `253c209` — full hash `253c20986be422929025158e96a378e7be612731`, author "Frank Bültge <f.bueltge@gmail.com>", date `2026-08-16 02:24:21 +0200` = `00:24:21 UTC`. `git show 253c209 -- chronicle.json` shows exactly three `summary` fields changed, for collective_session 28, 32, 43 — matching the claim precisely. TRUE.

3. Three failing locations (dossier.test.ts:188, season.test.ts:135, studio-one-tap.test.ts:35) — checked against `git show HEAD:<path>` in the site clone (line numbers refer to the pre-change committed files). Line 188 is exactly `expect(d.returns[0].quote).toBe(...)`; line 135 is exactly `expect(words[1]).toBe(...)`; line 35 is exactly `).toEqual([])` closing the tour-quote assertion. All three match the CI log in `studio-feedback/2026-08-16.md` verbatim, including error text. TRUE.

4. Integrate workflow copies chronicle.json before validating/committing — read `.github/workflows/studio-integrate.yml` directly: the "Integrate works" step runs `cp /tmp/studio/chronicle.json src/data/studio/chronicle.upstream.json`, then a separate "Validate (check+test+build)" step runs, then a separate "Commit" step runs only `if: success()`. Confirmed order matches the claim exactly. TRUE.

5. Validation numbers — re-ran independently in the site clone (base `ea1a8e6`, change + mirror applied): `node scripts/drift-check.mjs` → "drift-check: clean (static only)"; `npm run check` → "0 errors, 0 warnings, 57 hints"; `npm test` → "Test Files 140 passed (140)", "Tests 2837 passed (2837)"; `npm run build` → "650 page(s) built". All four numbers match the documents exactly. TRUE.

6. "3 failed before the change" — reverted the five source/test files to `git show HEAD:<path>` (pre-fix state) in a scratch copy and reran `npx vitest run`. Result: "Test Files 3 failed | 137 passed (140)", "Tests 3 failed | 2834 passed (2837)" — the three failures are byte-identical in assertion text/line to both the claimed locations and the `studio-feedback/2026-08-16.md` CI log. TRUE.

7. "No file under src/ carries the withheld wording" after the change — grepped all three withheld sentences against `src/` in the fixed clone: zero matches anywhere. TRUE.

8. `src/lib/record/private-quotes.test.ts` passes with the change applied — ran it directly: "Test Files 1 passed (1)", "Tests 15 passed (15)". Also confirmed it passed in the reverted (pre-fix) state too, supporting "as it did before." TRUE.

9. NOTED — The PR's stated *reason* the guard misses the withheld wording is inaccurate. PR.md says the guard "does not reach [the fixtures] because it scans the published record and not the source that produces it." I read `private-quotes.ts` directly: `export const SCANNED_ROOTS = ['docs', 'src', 'scripts', '.github']`, with the code's own comment reading `/** Roots that are part of the published record. */` — `src` (the source that produces the record) is explicitly included. I confirmed by running `scanRecord()` against the reverted (pre-fix) tree containing the raw withheld quotes in the three fixture files: it returned 34 unrelated findings and none from those three files — so the guard genuinely misses them, but because it requires a line-local "Frank" attribution token co-occurring with the quote (as the guard's own test suite documents: "is line-local, and that is a second stated limit"), not because `src` is out of scope. The bottom-line claims ("no file under src/ carries the wording," "the guard passes") are both independently true — only the causal explanation offered is wrong.

10. Only the quotes were cut from the tour, not the scenes; five-scene arc unchanged; both returns stay — read `git diff HEAD -- src/lib/tour/studio-one-tap.ts`: two `text:`/`source:`/`locator:` quote objects were removed and replaced with comments, all surrounding scene sentences kept intact. Counted scene `id:` entries in the current file: `the-premiere`, `the-eye-returns-it`, `the-third-return`, `what-two-voices-found-unasked`, `what-it-cost-and-what-it-bought` — exactly 5, both One Tap return scenes present. TRUE.

11. S28 and S43 untouched by `carriesTheSaying`, only S32 changes — reimplemented `recordAround` exactly (old `hasQuote` vs new `carriesTheSaying`) and ran it against the live chronicle text for all three sessions. S28 output identical old vs new; S43 output identical old vs new; S32 output differs (extends into the second sentence under the new logic, as claimed — this is exactly the fix for the "announces but doesn't carry" problem). TRUE.

12. Both branches of `saidFragment` return byte-exact spans of the mirror — confirmed indirectly but concretely: `season.test.ts`'s own assertion loop (`expect(raw).toContain(m.label)`) runs over every returned mark including all three One Tap returns, and the full suite passes (finding 5/6/8 above). Also read the `saidFragment` source: both the `quotedFragment` branch and the `/wording private\s*[—–-]\s*([^)]{8,})\)/` branch extract literal regex-captured substrings of the input text (only `.trim()` applied, which only removes from the ends), so both are contiguous verbatim spans. TRUE.

13. Live site "zero occurrences" claim on `/studio/` and `/studio/works/` — fetched both URLs live via curl just now (HTTP 200 both) and grepped the fetched HTML for all three withheld sentences: zero matches on both pages, right now. TRUE (as of this check; matches the document's own hedge that it checked only these two routes, not "everywhere").

14. Clone's base commit `ea1a8e6` — `git log --oneline` in the site clone shows a single commit, `ea1a8e6 nightly line: integrate 2026-08-16`, and `git rev-parse HEAD` = `ea1a8e6077b4ed07985bf50c261fa05a4e7241cf`. TRUE.

15. Five replacement source files — `git diff --stat HEAD -- src/lib` in the site clone shows exactly 5 changed files (`dossier.test.ts`, `dossier.ts`, `season.test.ts`, `season.ts`, `studio-one-tap.ts`), matching the file set under `site-prs/.../files/src/lib/`. TRUE.

16. NOT CHECKED — "STILL DARK premiered on 2026-08-15 into a repository rather than a stage" and "its delivery packet — due by 2026-08-22." Partially confirmed only that a work directory `works/2026-08-15-still-dark` exists in /home/user/studio (consistent with the premiere date), but I did not verify the 2026-08-22 delivery-packet due date or the "repository rather than a stage" characterization before being told to stop further checking.

17. NOT CHECKED / out of scope — Claims about session 97/98 history ("Session 97 asked for one word... two of our own sessions have passed since") in the REQUESTS entry. Verifying these would require reading earlier REQUESTS.md entries and/or journal material, which is the session's own account and outside my permitted scope (I was told to read only the final REQUESTS.md entry and not the journal/workboard).
