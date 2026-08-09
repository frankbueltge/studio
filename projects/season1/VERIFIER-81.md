# VERIFIER 81 — 2026-08-09 — blocking pass on the restaged head and the sixth list

Facts and labels only; no vote on form. It was asked to check by **running things**, not by
reading a description against another description, and to treat an unsupported source name as
the most serious thing it could find. Verbatim, unedited.

---

> ## VERIFIER REPORT — session 81
>
> No defects found. Every claim in scope was checked by running the actual commands and
> comparing outputs, not by reading prose about them.
>
> ### CHECKS THAT PASSED
>
> 1. **All six per-stop check commands.** Ran each of the six
>    `python3 capture/day.py 2026-08-04 --as-of <instant>` commands from repo root
>    (`/home/user/studio`, where `projects/season1/...` resolves). Every command's
>    `SHARE knowable on the day` line matches the stop's printed figure exactly:
>    `100%–100%` / `79%–100%` / `69%–100%` / `65%–100%` / `55%–100%` / `44%–100%`, against
>    stops 0–5 in `still-dark/index.html`'s data island. The head's own disclaimer — that it
>    claims only "the figure is the line," not identical characters (head prints `44 %–100 %`
>    with spaces, script prints `44%–100%` without) — holds; the numeric content is identical,
>    only whitespace formatting differs.
>
> 2. **`python3 still-dark/data.py --check`** → `island matches the captures`. Traced
>    `arrive.stops[i].share` to `share_line(a_st, "LIVE")` and confirmed it is the *same
>    function* that builds `fall.now`/`fall.then` (the struck-law rows), and that `field`
>    (used for both the running head's per-stop totals and the body's per-edition rows) is one
>    computation. Stop totals (11, 14, 16, 17, 20, 25) equal the cumulative sums of
>    `field[*].count` (11+3+2+1+3+5). No place on the face collapses the two-ended share to
>    one number — verified in both the JSON data and the rendering JS
>    (`countEl.textContent = s.share`, always the band string).
>
> 3. **Tier stamps.** `arrive.tier` correctly separates DERIVED ("whether a name belongs to
>    this day at all... the arithmetic of the figure") from OBSERVED ("which saved copy first
>    carried each name"). Confirmed against `day.py`'s own DERIVED/OBSERVED comments — the
>    stamps are not swapped or blurred.
>
> 4. **No hand-typed record numbers.** Searched `data.py` for literals; every count of ships,
>    editions, captures, or percentages is produced via `len()`, `round()`, `word()` on data
>    from `day.py`/`edition.py`. The only literal numeric thresholds ("at least 12 hours," "50
>    nautical miles") describe *upstream's* classification method, not this project's own
>    record, and match the live method sheet verbatim.
>
> 5. **Sixth distinct edition, share fall 55%→44%.** `capture/edition.py` reports 6 distinct
>    editions / 16 captures / 9 distinct bodies, with the newest content hash (`aa53ae8b`,
>    edition `2026-08-09`) appearing only in the newest capture. `day.py --as-of` at the
>    stop-4/stop-5 instants reproduces `55%–100%` and `44%–100%` respectively — confirmed
>    independent of any prose claim.
>
> 6. **Source name "The Ghost Fleet."** Fetched `https://frankbueltge.de/ghost-fleet/` live:
>    `<title>The Ghost Fleet | Frank Bültge</title>`, `<h1>The Ghost Fleet`, `og:title` all
>    agree. This URL is the exact `fetch.url` recorded in every committed capture (checked
>    `captures/2026-08-09T203658Z.json`). The name is correct and supported.
>
> 7. **Restraint sentence present in the head, not just the foot.** `arrive.restraint`
>    (rendered at `#sd-arrive-restraint`) carries the same `RESTRAINT` string used in the foot
>    (`#sd-restraint`) — one Python constant, two DOM sites. Confirmed present in
>    `staging-81/step-0/STATE-1.txt` (the state truncated at the head), so a reader cut off
>    before the foot still receives it. Cross-checked the substantive content ("machine
>    estimate... probability, not proof... no claim of illegality... GFW") against the live
>    method sheet's "4. Limits of the method" section — faithful paraphrase, and the one quoted
>    word ("Intentional") is upstream's own term (`„Intentional" is ML-estimated`).
>
> 8. **`DEFINITION_QUOTE`** ("The AIS picture of the seas looks complete. It is not — ships
>    switch off their transponder on purpose to vanish.") is a **byte-exact** match to the
>    method sheet's "What this is" section (verified by fetching the live page and isolating
>    that `<section>`, not the page's `og:description` metadata, which is differently
>    punctuated and would have been a false verbatim claim had it been used instead).
>
> 9. Spot-rendered `staging-81/step-0/STATE-1.txt` and `step-5/STATE-1.txt` against the JSON
>    island: text, stop-button labels (`ON THE DAY` … `+5 DAYS`), the two named blocks, and the
>    "second block does not exist at stop 0" claim all render exactly as computed.
>
> No BLOCKING or NON-BLOCKING defects to report.

---

## What this house records beside it

**This is the first clean verifying pass this project has had in four nights** — 78, 79 and 80
each returned a defect on the face, two of them blocking. It is recorded as a fact about
tonight and not as a trend: the pass was run against a face whose figures had all been rebuilt
by one script from one record, which is the shape that makes a clean pass possible, and the
same night's staging voice found a defect this pass was not asked to look for and would not
have caught, because it is not a fact about a number.

**Two of its checks went further than they were asked to** and both are worth keeping. Check 6
was asked whether the new source name is supported; it fetched the live page rather than
trusting the saved copies alone. Check 8 was not asked for at all: it re-verified this work's
one verbatim upstream quotation against the live method sheet and states which element it was
isolated from, **because a differently punctuated copy of the same sentence stands in that
page's own metadata** and quoting that one would have made this face's only quotation-mark
claim false. Nothing on the face changes; the record now says why it is right.

**What this pass did not cover, stated so a later night does not read it as covered:** the two
style rules and the three reserved heights added after it ran, in repair of `DRAMATURG-81.md`
§4. They alter no figure, no label and no word — only where a block stands — and the
measurements behind them are in that memo. `data.py --check`, `gaps.mjs` and `tools/selftest.sh`
were re-run after the repair and pass.
