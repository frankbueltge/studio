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

**The two test files** are updated to assert what is now true — and, after the second pass below,
to assert it as a *property* rather than as a string, so the suite holds whichever side of the
redaction the committed mirror happens to be on.

## Second pass, 2026-08-17: why the first attempt was red, and what changed

The first version of this proposal was refused by the gate. Its two failures both received the
**pre-redaction** wording, which the studio's `chronicle.json` has not carried since `253c209`.
Session 100 read that from the log alone and offered a hypothesis it could not check. **It is now
checked, first-hand, and it holds:** `src/data/studio/chronicle.upstream.json` as committed on
`main` (at `0092d95`) stops at collective session 97, contains **zero** occurrences of `wording
private`, and still carries the withheld phrasing verbatim. The site-PR gate validates against
that file as committed; the integrate workflow copies the studio's current record over it *before*
validating. **The two gates read two different records, and a fixture pinned to either one is red
on the other.** The first attempt pinned the paraphrases and so was correct for integrate and
refused by the gate.

So no string is pinned any more. What the two suites now assert is what is true on both sides:

- the three returns are found, in order, at their sessions;
- **where the record marks a passage as withheld, nothing reaches the `quote` field** — the
  privacy property itself, asserted directly instead of via a fixture that stands in for it;
- each return's record still reaches past the sentence that only announces it;
- each mark's label is short (never the whole-evening fallback), non-empty, never the withheld
  marker itself — and, by the assertion that was already there, a byte-exact span of the mirror.

**Two fixtures that had rotted are repaired in the same pass**, because both are red on `main`
today against the studio's current record and neither is a behaviour change:

- `season.test.ts` — the undated-strike fixture named session **`S99`** to stand for an evening the
  mirror cannot carry. S99 was in the future when it was written and arrived on 2026-08-16, at
  which point the fixture began asserting the opposite of what it says. It now **derives** the absent
  session from the newest one in the committed mirror, so no literal number can rot again.
- `dossier.test.ts` — the attribution test pinned One Tap's history to the literal list
  `['S28','S31','S32','S43']`. That was the answer on the day it was written; it stopped being the
  answer the first time the studio declared the work in a later entry's `works` array — S99, whose
  evening was spent on this derivation. The assertion now computes the same two inputs the rule
  itself uses (declared + stated-outright) off the committed record, and additionally checks that
  the two rules really reach different evenings, so it still proves what it was written to prove.
  The seventeen mention-only sessions are untouched and still excluded.

### What a hostile reading of this pass then found, and what it changed

The property assertions above were put in front of a fresh reader with no stake, briefed to break
them. Two of its findings are in these files:

- **The privacy assertion is a no-op on the record the gate reads.** `if (PRIVATE_MARKER.test(...))`
  never fires against a mirror that contains no marked passage — which is exactly the mirror the
  site-PR gate uses. It proved this by deleting the suppression from `quotedFragment` and watching
  the whole suite still pass. **Answered with fixture coverage:** two tests in `dossier.test.ts` (a
  withheld passage yields no quote; an unwithheld one still yields its quotation) and two in
  `season.test.ts`, all synthetic and therefore live in both states. Both suites already keep a
  fixture layer "for the shapes the record does not currently contain"; this is one of those shapes.
- **`saidFragment` truncated at a nested bracket.** Its capture stops at the first `)`, so a
  paraphrase carrying its own parenthetical came back cut mid-clause — and at 38 characters it sat
  inside every length bound a test would set, so nothing downstream noticed. A capture that opens a
  bracket it never closes, or that has swallowed a second withheld passage, now falls back to the
  whole record, with a fixture holding it.

Three further findings are **reported and deliberately not fixed here**, so the choice is visible:
`recordAround` can swallow a following sentence when a paraphrase carries no terminating period;
whole-passage suppression drops a third party's genuine quotation sharing a sentence with a withheld
one (already documented above as the safe direction); and the attribution test's hand-transcribed
regex could miss a return phrasing neither author anticipated — which is the price of a second
witness, since importing the production regex would make that test truly circular.

**The studio repaired its own two defects on its side of the line**, and they are named here
because this PR is red without them: its session-100 entry carried `"verdict": "DEAD"`, which is
not in the chronicle contract's enum and failed the Zod validation at the head of the integrate
gate; and its session-99 summary contained the sentence *"…the three chronicle summaries where the
human eye returned One Tap…"*, which `RETURN_PATTERNS` correctly matched, minting a **fourth
return** of a work that has been returned three times. Both are fixed in the studio's record, not
here. The tripwire behaved exactly as its comment in `season.ts` says it should; the false positive
is the studio writing *about* returns in prose a scraper reads as *declaring* one, and it will fire
again the next time the practice discusses this history. It is left armed on purpose — a
notification is the right behaviour — but it is worth knowing that is what it is.

## What this is worth beyond a green gate

After this change, **no file this PR controls carries the withheld wording** — checked by search. The
last three places holding it were one tour scene definition and two test fixtures, and the guard at
`src/lib/record/private-quotes.test.ts` passed over all three. **Not because they are out of its
scope** — `SCANNED_ROOTS` includes `src`, so it was reading those files. It missed them because it
is line-local and wants an attribution token on the same line as the quotation, which a bare string
literal in a test fixture does not have. That is the guard's own second stated limit, and this is
what it looks like when it bites. The guard passes with this change applied, as it did before.

**What still carries it, and this PR does not touch any of it:**
`src/data/studio/chronicle.upstream.json`, the committed mirror — as this letter's own second-pass
section says, it predates the redaction; and the site's already-synced copies of the studio's older
record, `src/content/studio/journal/2026-07-21-session-28.md`, `…/2026-07-23-session-32.md`,
`…/2026-07-31-session-51.md` and `src/content/studio/REQUESTS-ARCHIVE.md`. All four are refreshed
from the studio's repository by the integrate workflow, not written here, and the studio's side of
that is a decision its architect has been asked for and has not yet given.

*(Two corrections, both made before this left the house by our own Verifier, whose memos ship beside
this file. The paragraph above first gave the wrong reason for the guard passing — that it scans the
record and not the source; and its first sentence first read "no file under `src/`", which is false
and is contradicted by this letter's own second-pass section four paragraphs earlier.)*

## Validation

Because the two gates read two different records, this pass was validated **in both states**, on a
clean `--depth 1` clone of `main` at `0092d95`.

**A — the state the site-PR gate sees** (these five files applied, `chronicle.upstream.json` left
exactly as committed, at session 97):

- `npm run check` — 0 errors, 0 warnings
- `npm test` — **2846 passed, 140 files, 0 failed**
- `npm run build` — complete, 654 pages

**B — the state the integrate workflow builds** (the same five files, plus the studio's journal
mirrored with `--delete`, the five root documents, and its corrected `chronicle.json` copied over
the mirror, in the workflow's own order):

- `npm run check` — 0 errors, 0 warnings
- `npm test` — **2846 passed, 140 files, 0 failed**
- `npm run build` — complete, 658 pages

**Before the change, in state B, on `main` as it stands:** 7 failed across 4 files —
`chronicle.test.ts` (ZodError on the invalid verdict), `dossier.test.ts` ×2, `season.test.ts` ×3,
`studio-one-tap.test.ts` ×1 — reproducing the CI log in this letter's build feedback line for line.

**One correction to what session 100 reported.** It read `graph.test.ts` in the gate log as a
failure that was not the studio's and would fail on any PR opened that day. On a clean clone today
it passes in both states above; whatever the cause, it is no longer present, and the claim should
not be carried forward.

## What we are not deciding for you

`saidFragment` chooses what a return mark is called on a public figure. We think it restores the
original intent under the new rule rather than inventing one, and it is the one judgement in this
proposal that is yours rather than ours. Everything else is forced: the tour cut by that suite's
own header, the suppression by the privacy rule, the two rotted fixtures by the calendar, the rest
by the record.

— Ensemble, session 99, 2026-08-16 · second pass session 101, 2026-08-17
