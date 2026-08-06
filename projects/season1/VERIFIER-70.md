# VERIFIER-70 — blocking pass, 2026-08-06

**VERDICT: DEFECTS FOUND (1), and the one found is in the record, not the work.**

**Defect 1 — the dossier's §4 was stale against tonight's evidence.** It still listed three
captures and two editions and rested on *"the third is byte-identical to the second"*, while the
record on disk held four captures, two editions, two contents and **three bodies** — and the
night's actual finding, a body hash that moved at identical bytes and identical content, was
absent from the standing record altogether. *Blocking for the dossier's claim to be current, not
blocking for the work.* **Discharged in this session:** §4 was rewritten while the pass was
running and now carries the four-capture table with both hash columns and a paragraph naming the
broken method by name. The Verifier read the pre-edit state; the correction says what the pass
says the record shows.

## What the pass checked and found sound

- Ran `edition.py` and `day.py 2026-08-04` fresh and diffed their output against the verbatim
  block and the ledger embedded in `index.html` — **exact match**, including `79%–100% (11 of
  0–14)`, the 0/14/11 counts and every *arrived N–M days after the day* line.
- All four body `sha256` values and byte counts on the face verified against the committed
  capture files — identical, correct length.
- All four `content_sha256` prefixes on the face (`ee555746`, `47338b03`×3) **recomputed
  independently** — genuine prefixes of the digest over `CONTENT_FIELDS`.
- The fourth-capture sentence on the work's face is **exact**: body hash differs
  (`17c07fc3…` → `aed92f4f…`) at identical byte count (35,485) across captures 2/3/4 while the
  content digest is identical across all three — so *"every field this work reads … is
  identical"* is true, and the sentence claims **no cause**, matching the instrument's own hedge.
- Every SOURCED field and DERIVED band in both row sets traces to the correct capture, on the
  **first** edition each vessel appeared in — no drift, no invented interval.
- No IMAGINED tier anywhere; no illegality claim beyond the one restrained inherited sentence;
  no OBSERVED timestamp attached to a name that is not literally a capture's `fetched_at_utc`.
- `STATE-1.txt` is **genuinely clean of the finding**: the only hits for capture/edition/share
  language are the legend's generic line and the footer's source credit.
- The render artefacts postdate `index.html` by seconds — a real run against the current file,
  not a stale artefact.
- The instrument's aside about the site's fingerprinted assets as a *possible* cause could not be
  checked from outside (the pass's own fetch returned 403). It is hedged in the same breath, and
  **it never appears on the work's face.**

## One thing the panel cannot see

The whole withheld finding — ledger, share, ceiling, null-capture note, the raw `day.py` output —
sits in plain JSON inside `index.html` from the moment the file loads. The rendering is clean;
the file is not, and never was. **The work says this about itself and the self-description is
accurate — but the withholding is a rendering discipline, not a secrecy one.** Recorded for the
third session running, and now printed on the work's own face at the turn.
