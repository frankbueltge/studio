# STOP USING IMMEDIATELY — a record of this build

This file is not load-bearing. `index.html` is complete without it; nothing here is
required to read, verify, or reproduce the page. It exists so a reader of this
directory has the record in one place, per `STAGING-RULING-62.md` §6.

## The four movements, as built

1. **THE SENTENCE** — title, byline, and one recall remedy quoted verbatim and set at
   the largest type on the page, with its `[S]` mark, the recall number, the recall
   date, and the record's URL beside it (as text, not a link). One line under it,
   ours: this house did not choose that notice — a committed rule did, with its
   discretion null, and it skipped nothing. Nothing else appears on the first screen.
2. **THE SILENCE** — three counts (performed 0 · asked 1 · answered 0), two refusals
   (this house cannot perform the score itself; it refused to recruit a performer in
   public), and the state line required by ruling §3, dated to publication.
3. **THE SCORE** — the nine clauses of `THE-SCORE.md`, entire and unaltered, as an
   ordered list. Not split, not annotated between clauses, no links inside them.
4. **THE NOTES** — the two `[S]` source notes and the `[I]` note from `THE-SCORE.md`'s
   block below its own rule, the sentence that nothing is sent to us, and the one
   permitted corpus figure (50 of 55). Below that: the empty append region, marked
   *Appended after publication*; the one-line replacement for the cut apparatus block
   (no file names); and the exit — `cpsc.gov/Recalls`, alone.

## The selection rule and the record it reached

The record is chosen by `THE-RULE.md` §2–§3, applied to the committed corpus
`observation/recalls-2026-07-01_2026-08-02.json` (55 records): admissible records are
those whose concatenated `Remedies` match `/stop using[^.]*immediately/i` (50 of 55),
sorted by `RecallDate` ascending then `RecallNumber` ascending, first record not yet
taken. That record is **RecallNumber 26591**, published 2026-07-02. Discretion under
`THE-RULE.md` §6 is **null**: **0 records were skipped** to reach it.

## The quotation

`Remedies[0].Name` of RecallNumber 26591, taken verbatim, is 326 characters:

```
sha256 b987f91130185652d3f3ebce96d736af6c5220f720578e54ac83ae9c6fdd476b
```

It carries one stray `?` glyph, in `pieces to?recalling@`, that is the source's own
and is not repaired. `observation/build-page-62.py` generates `index.html`, extracts
the rendered string back out of the file it just wrote, un-escapes it, and checks its
hash against the value above before it will report PASS. Reproduce with:

```
python3 projects/cpsc-recall-channel/observation/build-page-62.py
```

## What was refused (`STAGING-RULING-62.md` §4)

- Every internal file name.
- Every unsettled figure from the corpus (brand-mark-on-object count, the 25–31
  photograph range, the 10–13 marker range). The one figure that does appear, 50 of
  55, is settled and insensitive to coding.
- The publisher's name, anywhere in movement II.
- Every photograph. Zero images ship.
- Any collection surface — no form, no address of ours, no counter, no *tell us*.
- Every link inside the nine clauses — the address in clause 2 is spoken text.
- Navigation, credits, an about-this-work block, any hairline not separating the four
  movements, and a second byline.

## Pointer

The working record — the corpus, the selection script, the performance log, the full
staging history — is `projects/cpsc-recall-channel/` in this repository.
