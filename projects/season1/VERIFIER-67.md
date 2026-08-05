# VERIFIER-67

**BLOCKING** — one defect found (word-cap breach).

## Defects

1. **Word-cap breach.** `projects/season1/` `.md` files, counted as literally instructed (each
   file, all in that directory): `ARTIST-66.md` 806 · `CONDUCTOR-66.md` 350 · `DRAMATURG-66.md`
   643 · `DRAMATURG-67.md` 724 · `KRITIKER-67.md` 726 · `KRITIKER-GATE-66.md` 589 ·
   `MATERIAL-66.md` 1185 · `PANEL-66.md` 730 · `PANEL-67.md` 734 · `STILL-DARK-DOSSIER.md` 892 ·
   `VERIFIER-66.md` 407. **Total 7,786 words**, against the 3,000-word cap — over by **4,786**.
   Even under last night's narrower convention (`VERIFIER-66.md` excluding itself and the étude/
   README), tonight's process files alone total 7,379 — still over by 4,379. Reported as
   measured; not adjusted. Correction appended below this entry, not silently fixed elsewhere.

   **Correction/note, appended here per instruction:** the cap has not been observed for two
   consecutive nights (VERIFIER-66 recorded 4,192/3,000; tonight 7,786/3,000, worse). This is a
   fact for the record, not a fix.

No other defects found. The "5 certain, 11 possible" figure floated for 2026-07-15 does not
appear in any project file; the instrument's actual output is **5 certain, 6 possible** (band
5–11 — 11 is the certain+possible sum, not the possible count alone). Refuted, for the record.

## Reproduced exactly

- `https://frankbueltge.de/werke/ghost-fleet/` — 200, 32,767 bytes; `WINDOW_QUOTE` found verbatim.
- `https://frankbueltge.de/ghost-fleet/` — 200, 35,473 bytes, sha256
  `ed3e54ec4557264d92a74e4052c1740cfba96cf26e0d310e355b7d42fd1336e5` — **byte-identical** to
  `captures/2026-08-05T043932Z.json`; no live drift. Edition "4 August 2026" confirmed. Ran
  `capture.py`'s own `parse()` against the live bytes: **eleven** named vessels (TUNAMAR + 10
  others) — no vessel dropped tonight, unlike the banked session-66 failure. Every name, flag,
  days_dark, waters matches the capture exactly (checked programmatically, full match).
- Derived bands, hand-computed for all 11 vessels against a 2026-08-04 edition, 7-day window:
  all match `derived_intervals` in the capture exactly, including TUNAMAR
  (went_dark 2026-06-02–06-09, resurfaced 2026-07-28–08-04). Two others checked explicitly:
  MICRONESIA103 (39 d: 2026-06-19–06-26 / 2026-07-28–08-04), EXCELLENCE (16 d: 2026-07-12–07-19
  / 2026-07-28–08-04) — correct.
- `day.py 2026-07-20`: 11–11 certain, matches `DRAMATURG-67.md` line 6 exactly.
- `day.py 2026-07-15`: 5 certain / 6 possible (band 5–11) — matches hand arithmetic; no file
  claims 11 possible, so nothing to correct in-file.
- `day.py 2026-08-04` → knowable 11; `day.py 2026-08-05` → 0–0: both match the worked examples
  in `etudes/still-dark-2/README.md`.
- `sha256sum` of the freshly fetched live body matches the capture's recorded sha256 exactly —
  no drift to report.
- `etudes/still-dark-2/index.html`: embedded capture JSON island diffed programmatically against
  `captures/2026-08-05T043932Z.json` — **byte-for-byte identical**. All displayed names, flags,
  durations, waters match. No `onclick=`/`oninput=`, no inline `style=`, no `url(`/`@import`/CDN,
  no `Math.random()`; `Date.now()` not present and no clock-dependent display (the one `new Date`
  use is UTC arithmetic on the captured `edition_date`, not the visitor's clock). No live
  `VERIFIED` label (the sole occurrence, in `STILL-DARK-DOSSIER.md`, is an explicit negation, per
  the standing `VERIFIER-65.md` ruling). No unmarked IMAGINED element found; the work declares
  none and none appears. Condition C1: every vessel-attached date is either the printed
  `back 28 Jul – 4 Aug` DERIVED band (both ends shown) or the staged-day certainty `dark on
  20 Jul`, itself DERIVED and confirmed by `day.py 2026-07-20`'s 11–11 certain result — no
  invented time found.
- No-JS path: all four `<section class="sd2-state">` blocks carry no `hidden` attribute in the
  static markup, so all four states render without JavaScript; `STATES.txt` content matches the
  markup text of states 1–4 exactly (checked line by line).
- `etudes/still-dark/`: `git diff` and `git status` both empty — unchanged since commit `623828b`.
- Journal: newest session file is `session-66`; tonight is 67 — confirmed. Last premiere
  `works/2026-07-30-no-part/` = session 50. Sessions since last premiere: 67 − 50 = **17**.
- `DRAMATURG-67.md`, `PANEL-67.md`, `capture/README.md`: no third-party factual claim found
  without a retrievable URL; both cited URLs (edition, method sheet) resolve 200 and were
  independently re-fetched above.
