# VERIFIER — session 69

Re-ran first-hand: `day.py 2026-08-04` (plain, `--json`, `--as-of`, and `2026-07-10`); all three
capture files by hand; `render.mjs` against tonight's build **and** last night's; the md5s cited in
`PANEL-69.md`; the embedded output against a fresh run; `DRAMATURG-69.md` §D (commit `6dd04f4`) against `PANEL-69.md`.

**REPRODUCED.** `--as-of` filters strictly on `fetched_at_utc <= as_of`, exactly as its help text
says: 1 capture, 1 edition, 100 %–100 %. Full run: 3 captures, 2 editions, 79 %–100 % (11 of 0–14).
`2026-07-10` still prints **not yet measurable** and refuses the DERIVED substitution. `editions_read`
matches the files. The 19:17 capture carries edition 2026-08-05, 8 vessels, and its **fetched-page**
sha256 is identical to the 12:54 capture's — the capture *files* differ only in `fetched_at_utc`, so
"the same edition, byte for byte" is true and precisely scoped. `render.mjs` reproduces tonight's
`STATE-1.txt` md5 `8d57c794…` and, against last night's build, panel 68's `e4014c75…` exactly. The
embedded stop-2 output is byte-identical to a fresh run. **No threshold was loosened between
`DRAMATURG-69.md` §D and `PANEL-69.md`; Q2 stands at 3 of 3 as written**, and the scoring arithmetic
holds for all four questions. The restraint sentence is present verbatim; every vessel row links its
Global Fishing Watch id; no claim of illegality anywhere.

**DEFECTS.**
1. **Non-blocking, and a disclosure this house owes:** `index.html` carries all fourteen rows, the
   three arriving names and the `79%–100%` figure in its JSON island **at load**, before the control
   is moved. `STATE-1.txt` — what a screen reader receives — is clean of all of them, confirmed by
   fresh render. But **view-source at state 1 reaches every one**. No document said so until this
   one. State 1 is a state of the *reading*, not of the *file*, and the work should say that where a
   reader can see it.

**Verdict: CLEAN.**
