# VERIFIER — session 68

Re-ran: `curl` on `https://frankbueltge.de/ghost-fleet/`; `day.py 2026-08-04` (plain, `--json`,
and against a 1-capture copy); hand count of both capture JSONs; `git diff chronicle.json`; `wc -w`.

**Reproduced.** Live fetch = 35,485 bytes, sha256 `17c07fc3...5b3a8` — identical to
`captures/2026-08-05T125400Z.json`, edition "5 August 2026". The 4 Aug capture can't be
re-checked the same way: the live edition has turned, no raw HTML is stored (by design), so its
sha256 `ed3e54ec...1336e5` has no live bytes left to hash against — a fact, not a gap. 4 Aug = 11
vessels, 5 Aug = 8, exactly {SOUTHERN SEAS NO.302, RICKY, ALTAR 10} are new and "possible" (not
"certain") dark on 4 Aug by hand — `day.py` matches: band 0–14, OBSERVED 11, SHARE 79%–100%
(11 of 0–14), byte-identical to `index.html`'s embedded `day_py_output`. `share_knowable_OBSERVED`
and `share_is_a_falling_ceiling` match their doc comments exactly (obs ≤ n_hi, obs ≤ max(n_lo,obs)
by construction). `STATE-1.txt` contains no `79%` and none of the three names. Duration
("56 d dark") is genuinely SOURCED — live page prints "39 days"/"29 days"/"28 days" verbatim;
page styling groups it with flag/waters (dimmed), apart from the full-ink DERIVED band. Face's
restraint sentence quotes only "Intentional" (verbatim both upstream pages); "a probability, not
proof" is also genuinely verbatim, from the werke page's AI/ML section — not fabricated.
`chronicle.json` session 67's `verdict` was `"conditions-discharged"` (outside SITE-API.md's
enum) before tonight, now `"conditions"` — all 67 entries valid.

**DEFECTS.**
1. `still-dark/index.html` footer — SOURCED legend names only "name, flag, waters" and edition
   dates; never names the duration it prints every row. No false label, but unreadable off the
   legend alone.
2. `projects/season1/*.md` totals 10,791 words vs the 3,000-word ceiling — grandfathered
   ("existing records stand"), but tonight added ~2,101 net words (`DRAMATURG-68.md` 697 +
   `PANEL-68.md` 623 + `STILL-DARK-DOSSIER.md` +781) to an already-over corpus.

**Verdict: CLEAN** (no blocking label failure; both items above are non-blocking).
