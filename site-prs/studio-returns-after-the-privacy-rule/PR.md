# Studio: derive the eye's returns from a record that no longer quotes the architect

The studio's build gate has been red since 2026-08-16, on three assertions and no others. This
proposal makes it green, and it does so by following the rule that made it red rather than by
restoring what that rule removed.

**Note on this text:** the three sentences at the centre of this change are the architect's own
withheld wording. They are named here only by file and line, never reproduced — writing them into
this proposal would be the defect it repairs.

## What happened, in order

1. **2026-08-15** — the site's own guard `src/lib/record/private-quotes.test.ts` failed the studio's
   gate on one line of a mirrored journal entry. The standing privacy rule behind it: the
   architect's messages are recorded as dated, neutral paraphrase, never quoted verbatim.
2. **2026-08-16 00:24 UTC** — the studio redacted its record in response (commit `253c209`,
   authored by Frank). Three chronicle summaries changed: the three times the human eye returned
   *One Tap*, at collective sessions 28, 32 and 43. Each quotation became a parenthetical marked
   `wording private` carrying a paraphrase of the same substance.
3. **Every run since** — three assertions fail, because they require the pre-redaction wording:
   - `src/lib/studio/dossier.test.ts:188` — expects the first return's quote; gets `undefined`.
   - `src/lib/studio/season.test.ts:135` — expects the second return's quote as a mark label; gets
     the sentence that only announces the return.
   - `src/lib/tour/studio-one-tap.test.ts:35` — two tour scenes quote sentences that are no longer
     literal substrings of `src/data/studio/chronicle.upstream.json`.

The integrate workflow copies the studio's `chronicle.json` over the upstream mirror **before** it
validates and commits, so the failure recurs on every run while the committed mirror stays at its
last green state. Reproduced first-hand on a clean clone by copying the current studio chronicle
into place: the same three failures, with the same messages as the CI log.

## The reading this proposal is built on

The three tests are not stale fixtures. They assert a property the record deliberately no longer
has, and will not have again. Two repairs were available and only one of them is legal: teaching
the derivation to reach past the quotation marks into the parenthetical would re-extract and
re-publish exactly what the privacy rule withdrew. So the derivation stops looking for the
architect's words, and reads the paraphrase the record now puts in their place.

## The change

**`src/lib/studio/dossier.ts` and `src/lib/studio/season.ts`** (the two carry the same three
helpers over the same entries, as they did before):

- `hasQuote` → `carriesTheSaying`, which also recognises a passage the record marks `wording
  private`. Without this, `recordAround` stops at the sentence that only announces the second
  return, so the record states that a return happened and drops what it was. With it, the record
  carries the paraphrase — one entry changes, S32; S28 and S43 already state the return and its
  substance in a single sentence and are untouched.
- `quotedFragment` returns `''` for any passage marked `wording private`. The `quote` field is
  rendered by `Dossier.astro` as a blockquote of the eye's own words, and paraphrase placed there
  would be the withdrawn quotation put back by a regex. The suppression is whole-passage on
  purpose: a genuine quotation of someone else sharing a sentence with a withheld one is dropped
  too, which is the safe direction to fail in.
- **New in `season.ts`: `saidFragment`**, used for a return mark's label. Before the redaction the
  label was the eye's quoted words and the `|| record` fallback was a path the committed data never
  took. After it, all three returns fell through that fallback at once and two labels became a
  330-character sentence about a whole evening — carried into the floor figure's hover readout.
  `saidFragment` takes the quotation where one still exists, otherwise the paraphrase clause. Both
  branches are byte-exact spans of the mirror, which is what `season.test.ts`'s own honesty
  assertion (`expect(raw).toContain(m.label)`) requires of every label. Nothing is authored.

**`src/lib/tour/studio-one-tap.ts`** — the two unverifiable quotes are **cut**, one from each of
the scenes `the-eye-returns-it` and `the-third-return`, following that suite's own header: *a scene
whose quote cannot be verified is CUT, never paraphrased.* Only the quote is cut, not the scene:
each keeps two quotes that are the house's own sentences and still byte-exact, the five-scene arc
is unchanged, and neither return disappears from the tour.

**The two test files** are updated to assert what is now true, and in both directions: that the
three returns are still found, in order, at their sessions; that each record is marked as withheld
and yields **no** quote; that the second return's record reaches past its announcing sentence; and
that the labels are the paraphrases, none of them longer than the fallback would have produced.

## What this is worth beyond a green gate

After this change, no file under `src/` carries the withheld wording — checked by search. The last
three places holding it were one tour scene definition and two test fixtures, and the guard at
`src/lib/record/private-quotes.test.ts` passed over all three. **Not because they are out of its
scope** — `SCANNED_ROOTS` includes `src`, so it was reading those files. It missed them because it
is line-local and wants an attribution token on the same line as the quotation, which a bare string
literal in a test fixture does not have. That is the guard's own second stated limit, and this is
what it looks like when it bites. The guard passes with this change applied, as it did before.

*(This paragraph originally gave the wrong reason — that the guard scans the record and not the
source. Our own Verifier read `private-quotes.ts` and corrected it before this left the house; its
memo ships beside this file as finding 9.)*

## Validation

Run on a clean `--depth 1` clone of `main` at `ea1a8e6`, with the studio's current record mirrored
in as the workflow does it (integrator, the five root documents, the journal, `chronicle.json`,
then `npm run graph:build`):

- `node scripts/drift-check.mjs` — clean
- `npm run check` — 0 errors
- `npm test` — **2837 passed, 140 files, 0 failed**. Before the change, the same mirrored record
  produced **3 failed / 66 passed** across the three affected files, with the same three assertion
  messages as the CI log; the full suite was not run in that state, so the only "before" number
  stated here is the one that was measured.
- `npm run build` — complete, 650 pages

## What we are not deciding for you

`saidFragment` chooses what a return mark is called on a public figure. We think it restores the
original intent under the new rule rather than inventing one, and it is the one judgement in this
proposal that is yours rather than ours. Everything else is forced: the tour cut by that suite's
own header, the suppression by the privacy rule, the rest by the record.

— Ensemble, session 99, 2026-08-16
