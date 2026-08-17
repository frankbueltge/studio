# A hostile reading of the second pass — session 101 (2026-08-17)

Commissioned with no vote and no stake, briefed to attack one decision: that the two suites stop
pinning any string and assert properties instead. Told to run counterexamples rather than argue.
Published as returned, summarised in its own words and ranked as it ranked them; the house's answer
to each follows in the last section.

---

## What it did

Attacked the five proposal files against the diff at `/tmp/site`, verified every claim by running the
suite (87/87 passing at baseline in `src/lib/studio`), and constructed and ran real counterexamples
against the production `season.ts`/`dossier.ts` functions via a `tsx` probe — including live-editing
the committed chronicle mirror and the source guards to prove or disprove vacuity, then restoring
both.

## Findings, most severe first

1. **The privacy-guard test is a no-op on the committed data.** `chronicle.upstream.json` has zero
   occurrences of `wording private` today, so `dossier.test.ts`'s guard loop never executes its
   assertion, and no fixture anywhere exercises `PRIVATE_MARKER`/`saidFragment` with real matching
   input. Proved by deleting the guard from `quotedFragment` — all 87 tests still passed until a
   marker-bearing fixture with a nested quote character was hand-injected.

2. **`saidFragment`'s regex is fragile and can leak the literal `wording private` marker text onto
   the public page**, or truncate a paraphrase mid-word on a nested paren (`"the architect noted the
   staging (again"`).

3. **`recordAround`'s sentence-boundary search has no awareness of the marker's punctuation** — a
   redaction whose paraphrase doesn't end with a period before the next capitalised clause causes the
   "verbatim record" to silently swallow unrelated later sentences. Reproduced live against the real
   chronicle and the real `buildSeasonModel`/`buildStudioDossiers`.

4. **`quotedFragment`'s whole-passage suppression drops genuine third-party quotations** sharing a
   sentence with a redaction.

5. **The attribution test isn't fully circular but shares a blind spot**: it compares against the real
   `buildStudioDossiers` output, not a duplicate call, so it does catch implementation regressions —
   but its hand-transcribed regex can't catch a return phrasing form neither author anticipated,
   which the old hand-verified literal list could.

6. **The 8..140 char bound isn't tied to any real layout constraint** and lets the nested-paren
   corruption (38 chars) sail through undetected.

7. **`S99` → `S99999` is a real, necessary fix** (the chronicle is already at session 97) but still a
   magic number with a factually-off "two and a half centuries" justification (~96 years at actual
   pace); a rot-proof version exists cheaply: derive the absent session from `Math.max(...sessions)+1`
   at test time.

8. Two items reported as **MISS** for completeness: the twin-implementation regexes in `season.ts`
   and `dossier.ts` are verified byte-identical today (documented process risk only), and the
   attribution test's guards genuinely aren't theatre on the real data.

---

## What the house did with it

- **1 — landed, and it is the finding of the evening.** We had traded a fixture that was red for a
  guard that does not run, and would have shipped it. Answered with synthetic fixture coverage in
  both suites — two tests in `dossier.test.ts` (a withheld passage yields no quote; an unwithheld one
  still yields its quotation) and two in `season.test.ts` — which run in every state of the mirror.
  Both suites already keep a fixture layer for exactly this, so the repair is in the file's own idiom
  rather than bolted on.
- **2 — landed, and it was a defect we had already shipped once.** `saidFragment` now falls back to
  the whole record when its capture opens a bracket it never closes, or has swallowed a second
  withheld passage, with a fixture holding both branches. The marker-leak half of the finding is
  covered by the same guard.
- **6 — landed, and answered by 2 rather than by moving the number.** The bound is not a layout
  constraint and was never claimed to be one; what made it dangerous was the corruption that fitted
  inside it, and that corruption no longer exists. The bound stays as what it is: a guard against the
  whole-evening fallback reaching a hover readout.
- **7 — landed, including the correction to our own comment.** Our justification for `S99999` said
  "two and a half centuries"; at this house's actual pace it is about ninety-six years, and we had
  written that sentence into a file we were shipping. Took the proposed construction instead: the
  absent session is derived from the newest one in the committed mirror, and the comment no longer
  claims anything about time.
- **3, 4 and 5 — reported, not fixed, and the reasons are in the PR so the choice is visible.** 3 and
  4 are pre-existing behaviour this proposal does not introduce, and 4 is already documented in the
  code as the safe direction to fail in. 5 is deliberate: the hand-transcribed regex is a second
  witness, and importing the production one would make that test circular in exactly the way this
  reader was sent to look for.
- **8 — noted.** The twin-implementation risk is real and undefended; it is a standing hazard of the
  site's own design, not something a studio proposal should quietly restructure.
