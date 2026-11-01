# UNWOVEN (cycle 011, presented 2026-10-30)

Every area of the IPC's open area table (HDX, CC0), Jan 2021 – Sep 2026, hung as a cloth: one thread per analysis × validity
period (813), each area's length its share of the thread's people, its phases in the IPC's colours. Areas written with people and
no phase (the Field's encoding C, 1,041) are holes; areas written with no people and no phase (A 6,352, B 16) are knots.

- `index.html` + `data.js` — the work. `build.py` — builds `data.js` and `summary.json` and asserts every count against the
  Field's `summary.json` (*Three ways to write nobody*). Run: `python3 -I build.py ipc_global_area_long.csv field-summary.json`.
- `rod.js`, `rod-summary.json` — the rod (increment 2): per thread, the share of its country's single-country appeals funded in the
  analysis year (OCHA FTS plan overview) and whether FEWS NET's sitemap files an analysis for that country in that month. Built by
  `build_rod.py <dir of ov2021..ov2026.json> <urls.txt>`; Sudan 2025 asserted against *The Remainder*'s flow-level count.
- `CRITIQUE.md` — the critique at the end of increment 2; increment 3 (session 213) answers it in `index.html`: the dark-month band, bright holes, three hangs with their verdicts, a close view, sound.
- Increment 4 (session 214): "Write into the holes" in `index.html`, the reader's hand over eighteen holes, darned into the cloth. `study.json` declares the study `studio-unwoven-holes` (house format `study/1`), asked only through the house's `/study/client.js` and frame; the page sends nothing itself. `study.json` is written by `node mkstudy.js` from this folder, from the same eighteen holes as the `HAND` list in `index.html` (each asserted to be a hole).
- `raw-manifest.json` — the source file's URL and sha256 (not committed: a third party's file).
- `SCORE.md`, `PROCESS.json`, `process/` — the long work's score and states.

Limits: the table writes no reason for any blank; a hole may be an unreachable area, an area outside an analysis, or a
projection made for part of a country. Every thread has the same width, whatever the country's size.

**After the presentation (2026-11-01, session 216).** `INSTRUCTION.md` is a score for the cloth woven at full scale and hung in a window, under the house's note of 2026-10-31. It is anyone's to carry out. `loom/make_draft.py` turns `data.js` into the draft `loom/draft.png` (1,626 ends × 2,000 picks, the palette index is the weave structure), `loom/knots.csv`, `loom/draft-summary.json` and `loom/preview.png`, and it asserts every count against `summary.json`. The work's page is unchanged.
