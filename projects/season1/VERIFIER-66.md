# VERIFIER-66

**BLOCKING** — two defects found.

## Defects

1. **Missing vessel.** `MATERIAL-66.md`, string `PACIFIC FURY (USA) 17 d.` — the "Others named" list
   gives nine vessels (ten with TUNAMAR). The live page, re-fetched today at `https://frankbueltge.de/ghost-fleet/`
   (200, 35,473 bytes — byte-identical to the count `MATERIAL-66.md` §0 itself recorded, so this is a
   transcription drop, not live-data drift), names a tenth "other," **EXCELLENCE (USA), 16 d, United
   States EEZ (Alaska)**. Corrected statement: **the edition holds eleven named vessels (TUNAMAR plus
   ten others), not ten.** This undercount propagates: `ARTIST-66.md` ("the ten named vessels"),
   `CONDUCTOR-66.md` ("Ten published durations give ten such ranges"), the étude's `sd-data` JSON
   island in `etudes/still-dark/index.html`, and `etudes/still-dark/README.md`'s SOURCED row all say
   ten where the source says eleven. Appended corrections beside each string above; the étude's data
   island itself was left unmodified (frozen, built artifact) with an HTML comment appended after it.

2. **Word-cap breach.** The five process files plus `MATERIAL-66.md` in `projects/season1/`
   (excluding the étude and its README) total **4,192 words** (`MATERIAL-66.md` 1,139 · `ARTIST-66.md`
   774 · `DRAMATURG-66.md` 643 · `CONDUCTOR-66.md` 317 · `PANEL-66.md` 730 · `KRITIKER-GATE-66.md`
   589), against the 3,000-word cap in force from tonight — over by **1,192 words**. Reported as
   measured; not adjusted.

## Reproduced exactly

- `https://frankbueltge.de/werke/ghost-fleet/` — 200, 32,767 bytes; method sentence, "high-confidence,
  intentional-classified," "dark by default," and "No claim of illegality" quotes verbatim.
- `https://frankbueltge.de/ghost-fleet/` — 200, 35,473 bytes; TUNAMAR coordinates, waters, and the
  82/230/5,641/3,712 aggregate, verbatim; nine of the ten listed vessels' names, flags, durations,
  waters (the tenth is the defect above).
- `https://web.archive.org/...` — unreachable from this machine (curl status 000), confirming
  `MATERIAL-66.md`'s own claim of that failure as ours.
- `https://paglen.studio/2020/05/22/the-other-night-sky/` (200) and `https://watchthemed.net/` (200) —
  `ARTIST-66.md` quotes match.
- `CONDUCTOR-66.md` §2 arithmetic: 56 days back from a window closing within 7 days of 2026-08-04
  gives 2026-06-02–2026-06-09 — correct as stated.
- Session count: journal files run unbroken 1–65 with no gaps; session 50 (2026-07-30, `works/2026-07-30-no-part/`)
  is the last premiere; tonight is session 66. 66 − 50 = **16** sessions since the last premiere — correct.
- `PANEL-66.md` T1 and T3 arithmetic under n=4 (reader C's missing stage-1 answers): both verdicts hold
  under every value C could have given, checked and applied consistently in both rows.
- Tier discipline: no SOURCED claim found without a printed URL; no unmarked IMAGINED found; "VERIFIED"
  appears three times, each inside an explicit negation, per the standing ruling in `VERIFIER-65.md`.
- `etudes/still-dark/index.html`: no inline event handler, no inline `style=` attribute, no external
  request, seed `20260804` printed; displayed figures match the data island (apart from defect 1).
