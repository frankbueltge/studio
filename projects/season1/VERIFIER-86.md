# VERIFIER-86 — facts and tiers, session 86

**Hashes pinned before this pass began** (all matched at time of writing this memo; re-checked
after every run below and unchanged):

```
sha256 projects/season1/still-dark/index.html                = 0d8187f5c6e048d4e655105b4d938ea85babca510964b4dd02e79be290a39398
sha256 projects/season1/still-dark/README.md                  = 0e4ab8f0f8f1d929b527618995a3606ade36d1b9aab205011430c13a46216bb4
sha256 projects/season1/captures/2026-08-11T111915Z.json      = d75d8de169fe43719f0d5ac31d229958102d1bdf37e74c77d72dc7a6c35db02f
```

State: `git log -1` = `b416e4e` (session 86's own commit — it was already made when this pass
began; the file's hashes above match the committed content exactly, so nothing changed under me).

---

## 1. The eighth list, and the moved share

```
$ python3 projects/season1/capture/day.py 2026-08-04
day 2026-08-04  ·  23 capture(s) read, 8 distinct edition(s), 9 distinct content(s), 13 distinct bod(y/ies)
  vessels dark on that day .......... 2–33 (certain–possible)
  SHARE knowable on the day ......... 33%–100%  (11 of 2–33)
$ python3 projects/season1/still-dark/data.py --check
island matches the captures
```
Matches the README's claim (`33 %–100 %, 11 of 2–33`, `23 saved copies holding 8 lists`) exactly.
**PASS.**

## 2. PANOFI FORE RUNNER and HEATHER LYNN, checked against the capture file

`day.py`'s own output lists both as `certain`. Checked directly against the saved bytes, not the
README's sentence:
```
$ python3 -c "... load 2026-08-11T111915Z.json, print the two vessels ..."
{'name': 'PANOFI FORE RUNNER', 'flag': 'GHA', 'days_dark': 27, 'waters': 'Ghanaian EEZ', ...}
{'name': 'HEATHER LYNN', 'flag': 'USA', 'days_dark': 21, 'waters': 'United States EEZ', ...}
```
Both match the README's figures exactly, and `day.py`'s `certain` list (band held under every
feasible end) places both there. **PASS.**

## 3. "The lower end of the total left zero for the first time in this work's life"

```
--as-of 2026-08-05T04:39:32Z  → band 0–11
--as-of 2026-08-06T08:16:42Z  → band 0–16
--as-of 2026-08-07T18:15:53Z  → band 0–17
--as-of 2026-08-08T21:37:19Z  → band 0–20
--as-of 2026-08-09T20:36:58Z  → band 0–25
--as-of 2026-08-10T22:41:12Z  → band 0–31
(tonight, no --as-of)          → band 2–33
```
Every prior edition boundary in the record's life shows a lower end of 0; tonight is the first at
2. **PASS.**

## 4. The upper end, and the reason given — BLOCKING

The stated mechanism is correct: `day.py` computes the upper end as `obs / max(n_lo, obs)` with
`obs = 11` fixed (the vessels first appearing in the 4 August edition). It stands at 100 % while
`n_lo ≤ 11` and falls once `n_lo ≥ 12`; `n_lo = 2` tonight, so "two is not more than eleven" is
arithmetically correct and the upper end correctly holds at 100 %.

**But the same sentence, on the same face, contains a separate clause that is false tonight.**
`still-dark/index.html:932` (= `still-dark/data.py:938–946`, the `"constant"` string), reaching
the DOM/screen-reader order at `STATE-1.txt:12`:

> "...it holds at 100 % while no more of these ships are CERTAINLY dark on this day than the
> eleven the day itself named — a list gives a return only to the nearest week, **so all
> thirty-three are merely possible today** — and it falls as soon as one more than those eleven
> is certain..."

`word(now['vessels_dark_on_day']['band'][1])` is hard-coded to describe the *entire* band as
"merely possible." That was true every night this figure has existed, because `band[0]` (certain
count) was 0 every night — but tonight `band[0] = 2` (item 3, item 2). Two of the thirty-three are
not "merely possible," they are `certain`, by `day.py`'s own classification and by this file's own
`hedge` string three lines above it in the same JSON island (`index.html:651`): *"...so two of
these names are certainly dark on this day and the rest are possible."* The two sentences directly
contradict each other on the same rendered page. `data.py`'s `hedge` field (`data.py:715–722`) was
correctly rewritten tonight with a conditional branch on `band[0] == 0`; the `constant` field
(`data.py:938–946`) was not given the equivalent branch, so it kept publishing last night's
(then-true) sentence unchanged into a night where it became false.

Checked against `/tmp/index-prev.html` (= `git show 994f214:.../index.html`, last night's
committed page): the identical template read *"all thirty-one are merely possible today,"* true
at the time because `band[0]` was 0 then too. The defect is structural and was silently waiting
for the first night `band[0] > 0` — tonight.

This is the pattern named in the brief: a false sentence about this exact end, published a third
time, tonight, by omission rather than by a new hand-typed claim — the same effect as the two
prior published falsehoods (sessions 83–84, banked failure 31).

**BLOCKING.** File: `projects/season1/still-dark/data.py`, line 943 (`f"merely possible today — and it falls..."`),
propagating to `still-dark/index.html:932` and `still-dark/STATE-1.txt:12`. What would make it
right: give the `constant` string the same conditional the `hedge` string already has — naming
only the *possible* count (`band[1] - band[0]`, i.e. 31 tonight) as "merely possible," not the
whole band.

## 5. `HY928-21%-81%` — fetched first-hand

```
$ curl -sS -o /tmp/ghost-fleet-live.html -w "HTTP %{http_code}, %{size_download} bytes\n" https://frankbueltge.de/ghost-fleet/
HTTP 200, 32333 bytes
$ grep -o ".\{80\}HY928.\{200\}" /tmp/ghost-fleet-live.html
...text-fg-faint"> The case of the day </p> <p class="mt-2 text-lg font-semibold">HY928-21%-81% <span class="font-mono text-sm text-fg-faint">(—)</span></p> <p class="mt-3 leading-snug text-fg-muted"> A vessel flagged — switched off its transponder for 50 days — vanished at 2.7°S, 177.7°E, resurfaced at 3.1°S, 175.2°W, in Kiribati EEZ (Gilbert Islands).
```
The string is genuinely upstream's, live, tonight, no flag printed, exactly as claimed. Byte count
(32,333) and status (200) also match the README's and REQUESTS.md's figures exactly. **PASS.**

## 6. The em dash

Upstream's own live markup prints `(—)` in the flag position — an em dash. `flagText()` in
`index.html` (line ~2171) renders `"—"` for `null`/`undefined`/`""`, in both the name chips and
the OBSERVED ledger's flag column (line ~2509, with a comment noting the ledger previously
painted a blank there and now says the same thing). The SOURCED legend's new clause reads
`“—” is what the list shows in that place` — checked against the fetch above, true. **PASS.**

## 7. The counts: 23 / 13 / 8 / 9

```
$ python3 projects/season1/capture/edition.py
...
23 capture(s) · 8 distinct edition date(s) · 9 distinct content(s) · 13 distinct bod(y/ies)
```
Matches `day.py`'s own header line exactly (`23 capture(s) read, 8 distinct edition(s), 9 distinct
content(s), 13 distinct bod(y/ies)`) and the README's "Twenty-three saved copies, thirteen bodies,
eight lists — and nine distinct contents." The subtler claim — that the 8th *new* content
chronologically is the 10 August parser-repair artifact (`423c17df…`, first seen
`2026-08-10T22:41:12Z`) and the 9th is the genuine 11 August list (`a7ab0eb1…`, first seen
tonight) — checks out against `edition.py`'s row order. **PASS.**

## 8. Tier coverage on the rendered face

```
$ NODE_PATH=/opt/node22/lib/node_modules node tools/tiers.mjs
...
TIERS: every printed figure stands in a scope carrying a tier word.
Scope is structural, not semantic: this says a tier word is present, never that it is the right one.
```
Exit 0 — every figure tonight has a covering tier word structurally. The tool itself disclaims
semantic correctness, and item 4 above is exactly such a semantic failure: the `constant` string
sits inside a section scoped `SOURCED/DERIVED` (confirmed in `tiers.mjs`'s own listing) and
states something false, which no structural tool can catch. The SOURCED legend's new clause
(item 6) is true and correctly tiered — it describes what upstream prints, unrepaired.
**PASS on structural coverage; the semantic defect is carried under item 4, not double-counted
here.**

## 9. Measurements re-run, not trusted

```
$ NODE_PATH=/opt/node22/lib/node_modules node tools/fold.mjs
FOLD: 64 failure(s)
$ NODE_PATH=/opt/node22/lib/node_modules node tools/fold.mjs --dir=<last night's committed page, git show 994f214>
FOLD: 56 failure(s)
```
64 vs 56 confirmed exactly, and the reasoning (56/7 ≈ 8 per stop, one more stop added ⇒ +8) is
internally consistent.

```
scrollWidth, tonight's committed page, viewport 390 → 390; viewport 360 → 360
scrollWidth, last night's committed page (994f214), viewport 390 → 665
```
665 → 390 confirmed exactly by re-measuring both the prior and current committed files in a real
browser (playwright/chromium), not by reading the claim. **PASS.**

## 10. `REQUESTS.md`'s newest entry (session 86)

- Byte count / status: `curl` above returned `HTTP 200, 32333 bytes` — matches "HTTP 200, 32,333
  bytes" exactly.
- Chronicle count: `curl -sS https://frankbueltge.de/studio/chronicle.json` → a JSON array of
  length **85** — matches "now holds 85 entries."
- The build-letter judgment: `studio-feedback/2026-08-11.md` quotes failures in
  `src/lib/graph/graph.test.ts` against `src/data/begegnungen/register.json`. This repository has
  no `src/` directory at all (`ls src` → no such file or directory) — neither path named in the
  failing lines exists here, so the judgment "not ours" is defensible on the evidence quoted.
  **PASS.**

---

## Stale-figure sweep (repository-wide)

Searched for `"35 %"`, `"0–31"`, `"seven lists"`, `"22 saved"` across `.md .html .json .py .txt`,
excluding `archive/`.

| Address | String | Judgment |
|---|---|---|
| `still-dark/README.md:64` | `35 %–100 %, 11 of 0–31 → 33 %–100 %...` | correctly historical — explicit arrow to tonight's value |
| `still-dark/README.md:220,232` | `35 %–100 %, 11 of 0–31` | correctly historical — describes session 84/85's repair |
| `still-dark/index.html:872–873` | `"share": "35 %–100 %"` | correctly historical — the +6 DAYS stop's own frozen snapshot |
| `still-dark/data.py:505` | `35 %–100 %, 11 of 0–31` | correctly historical — code comment about session 85 |
| `VERIFIER-85.md`, `DRAMATURG-85.md`, `REQUESTS.md:3393,3461` | various | correctly historical — frozen, dated memos/log entries |
| `journal/2026-08-10-session-84.md`, `journal/2026-08-11-session-85.md` | various | correctly historical — dated journal entries |
| **`projects/season1/PROJECT.md:31`** | `**As of session 85: 35 %–100 % — 11 of 0–31**, from **22 saved copies** holding **7 distinct lists**` | **STALE AND BLOCKING** |
| `projects/season1/PROJECT.md:193` | `35 %–100 %, 11 of 0–31` | correctly historical — describes banked failure 38, a past event |

`PROJECT.md` — the file `still-dark/README.md` itself points to as "**the whole of it**" for the
work's live state — contains no "SESSION 86" section at all (`grep -i "session 86"
projects/season1/PROJECT.md` → no output) and its headline "The number, and how a stranger checks
it" section still reads session 85's figures, one full session after they were superseded. This is
the same class of failure the house has banked before (item 28, "the README was stale again, one
session after 24"), now on `PROJECT.md` rather than a README, one session after item 4 above.
`WORKBOARD.md` (which states its own rule as "Read and updated every session") also still reads
"live state as of session 85 (2026-08-11)" with no session-86 section — flagged for the same
reason, not separately blocking since `PROJECT.md` is the file the work's own README names as
authoritative.

**BLOCKING.** File: `projects/season1/PROJECT.md`, line 31. What would make it right: a session-86
entry advancing "As of session 85: 35 %–100 % — 11 of 0–31, from 22 saved copies holding 7
distinct lists" to the current figures (33 %–100 %, 11 of 2–33, from 23 saved copies holding 8
lists), as every prior session's increment has done in this same section.

---

## Summary of blocking items

1. **`projects/season1/still-dark/data.py:943`** (→ `index.html:932`, `STATE-1.txt:12`) — the
   `constant` sentence's clause "so all thirty-three are merely possible today" is false: 2 of the
   33 are `certain` per `day.py`'s own arithmetic and per this page's own `hedge` sentence three
   lines above it. Fix: give `constant` the same `band[0] == 0` branch `hedge` already has.
2. **`projects/season1/PROJECT.md:31`** — "As of session 85: 35 %–100 % — 11 of 0–31, from 22
   saved copies holding 7 distinct lists" is stale; no session-86 section exists in the file at
   all. Fix: add the session-86 entry and advance the headline figure.

VERDICT: FAIL — 2 blocking
