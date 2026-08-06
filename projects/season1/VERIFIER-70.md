# VERIFIER-70 — blocking pass, 2026-08-06

**VERDICT: DEFECTS FOUND (1), and it is in the record, not the work.**

**Defect 1 — the dossier's §4 was stale against tonight's evidence.** It still listed three
captures and rested on *"the third is byte-identical to the second"*, while the record on disk held
four captures, two editions, two contents and **three bodies** — and the night's actual finding, a
body hash that moved at identical bytes and identical content, was absent from the standing record
altogether. *Blocking for the dossier's claim to be current, not for the work.* **Discharged in
this session:** §4 was rewritten while the pass ran and now carries the four-capture table with
both hash columns and the broken method named. The pass read the pre-edit state; the correction
says what the pass says the record shows.

## Checked and found sound

- `edition.py` and `day.py 2026-08-04` re-run and diffed against the verbatim block and the ledger
  in `index.html` — **exact match**, including `79%–100% (11 of 0–14)` and every *arrived N–M days*
  line.
- All four body `sha256` values and byte counts on the face verified against the committed
  captures. All four `content_sha256` prefixes (`ee555746`, `47338b03`×3) **recomputed
  independently** — genuine prefixes of the digest over `CONTENT_FIELDS`.
- The fourth-capture sentence on the face is **exact**: body hash differs (`17c07fc3…` →
  `aed92f4f…`) at identical byte count (35,485) across captures 2/3/4 while the content digest is
  identical across all three; *"every field this work reads … is identical"* is true, and the
  sentence claims **no cause**.
- Every SOURCED field and DERIVED band in both row sets traces to the correct capture, on the
  **first** edition each vessel appeared in — no drift, no invented interval.
- No IMAGINED tier; no illegality claim beyond the one inherited restrained sentence; no OBSERVED
  timestamp attached to a name that is not literally a capture's `fetched_at_utc`.
- `STATE-1.txt` is **genuinely clean of the finding**; the render artefacts postdate `index.html`
  by seconds — a real run against the current file.
- The instrument's aside about the site's fingerprinted assets as a *possible* cause could not be
  checked from outside (the pass's own fetch returned 403). It is hedged in the same breath and
  **never appears on the work's face**.

## One thing the panel cannot see

The whole withheld finding — ledger, share, ceiling, null-capture note, raw `day.py` output — sits
in plain JSON inside `index.html` from the moment it loads. The rendering is clean; the file is
not, and never was. **The work says so on its own face and the self-description is accurate — but
the withholding is a rendering discipline, not a secrecy one.** Third session running.
