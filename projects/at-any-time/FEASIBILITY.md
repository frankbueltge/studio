# THE BUILDER — feasibility report on *AT ANY TIME*

*Session 53, 2026-07-31. Efficient tier. Convened as a **feasibility voice only** — nothing was built,
no project file was written by this voice. Every number below is either measured in this session or
explicitly marked as house precedent / not established. Published in full.*

---

## 1. Rasterisation at scale — CONFIRMED WORKING, fits a session

Verified present, not assumed: `node` v22.22.2, `Xvfb`/`xvfb-run`, and Chromium at
`/opt/pw-browsers/chromium-1194`. Copied `no-part/build/pdf-render-lib.js` unmodified, fetched the five
verified July PDFs (hashes matched the proposal's §9 table exactly), and rendered each at the house's
proven 4 px/mm scale, headful under Xvfb.

- Single-page steady-state render cost, measured over 6 repeated renders in one warm browser:
  **2,095 ms/page**.
- House's own figure for a 39-page continuous-scroll document (*NO PART*): **~2,400 ms/page**.
- 72 pages ⇒ **~2.5–2.9 minutes** of render time, plus trivial fetch time. **Comfortably fits a
  session.**

## 2. Output size — the hard constraint, with a real number

*NO PART*'s 1,962,815-byte `index.html` does **not** embed all 39 pages — it inlines only **4** PNGs (a
1 px/mm composite strip + 3 native-resolution sheets), confirmed by scanning the shipped file (4 images,
1,944,916 base64 bytes). That shortcut does not transfer: a sparse 296-slot column at true calendar
positions cannot be one composite strip without destroying per-page readability and the varying gaps.

Rendered the 5 verified pages individually at 4 px/mm:

| doc | PNG bytes | base64 bytes |
|---|---:|---:|
| SOCHOR (07-14) | 95,667 | 127,556 |
| HERRIDGE (07-02) | 123,384 | 164,512 |
| DUCKETT (07-28) | 96,043 | 128,060 |
| OCCHICONE (07-28) | 97,691 | 130,256 |
| DUCKETT ET AL. (07-28) | 100,526 | 134,036 |
| **mean** | **102,662** | **136,883** |

Projected inline-image payload (mean × N; scaffold adds low tens of KB):

| N | projected size |
|---|---|
| 8 (E2, the door) | **~1.09 MB** |
| 30 | **~4.11 MB** |
| 72 (one full term) | **~9.86 MB** |
| 200 | **~27.4 MB** |

`SITE-API.md`, quoted exactly: *"Size discipline: keep a work's shipped top-level total lean — guideline
≤ ~3 MB. The bundle is a work, not an app."* (And, for the site's own gate: *"≤ 2 MB per file · ≤ 50
files."*)

**The object stops being deliverable at N ≈ 21–22 pages** (3,000,000 ÷ 136,883) — before HTML overhead,
and below N = 30. N = 72 is >3× the guideline; N = 200 is >9×. **Since the work accumulates with no cap,
this ceiling is not hypothetical: it arrives during the work's life.**

Honest options, none tested beyond what is noted:

- **Lower render scale** — the pipeline's own `dsfForPxPerMm` formula is documented (and reproduced) as
  broken below `dsf = 1` (pxPerMm ≥ ~3.78 required); a test at pxPerMm = 1 threw *"Could not detect page
  top-left corner"*. A naive lower scale is not available without new engineering (post-render
  downsampling, as *NO PART* did for its strip).
- **Different encoding** — these are near-bilevel typewriter pages; an indexed/paletted PNG or lossless
  WebP would likely shrink several-fold. **Not measured. Flagged as the most promising untested option.**
- **Vector rather than raster** — the source PDFs are already vector text; embedding actual vector
  content (not OCR, not retyping) is plausible but no PDF→SVG path was tested and none is confirmed
  present.
- **Text re-set** — forbidden by the proposal itself ("never retyped").

## 3. The blank field — renders and scrolls; real ceiling measured

Built a live 296-slot column at the pipeline's native display scale (864 × 1118 px/page) and loaded it in
the same headful Chromium:

- Column height **330,928 px**, exactly 296 × 1118; `scrollHeight`/`offsetHeight` agreed; no collapse.
- Scrolled to bottom and to day 148: correct positions reached, last slot paints in-viewport.
- Probed this build's max renderable element height by bisection: **33,554,428 px exactly** (clamps
  above; confirmed at 33,554,432 and beyond).

**330,928 px is ~0.99 % of the measured ceiling.** No collapse risk at any length this work will reach.

## 4. The daily read, without a session — **NO, not as claimed**

Searched the entire repository for schedule automation. Exactly one workflow file exists,
`.github/workflows/auto-land.yml`. Its only cron (`0 2 * * *`) does two things — merge landed branches to
`main`, and fire a cross-repo dispatch to the site. **It fetches nothing from any external source, parses
nothing, renders nothing, and runs no Builder logic.**

`PROTOCOL.md` itself states the only runner: *"an external nightly schedule starts a session; a model
instance reads this protocol as its standing instruction and convenes the crew below as sub-agents."*
That is a full session by the protocol's own definition — the thing the proposal says a unit must never
cost.

**Plainly: the capability the proposal calls "scripted and has no decision in it" does not exist here.**
Honest alternatives and their real costs:

1. **Build a new cron-triggered workflow** that does fetch + parse + render + hash + commit with no model
   invoked. Technically plausible, but it needs headful Chromium + a virtual display inside CI, which
   nothing in this repository's CI has ever done; it is new standing infrastructure, unbuilt, untested,
   and arguably a `REQUESTS.md`-level decision rather than a detail.
2. **Fold the read into the nightly session that already starts** — spends a real session per read,
   contradicting §2 and triggering the proposal's own admission in §10: *"a clock that needs a session is
   a studio with a diary."*
3. **Manual, session-by-session reads** — functionally converts the world's clock into Kawara's studio
   clock, which §6 explicitly argues this work is the *inverse* of.

**This is the single largest unresolved risk in the proposal, and it is not a small one.**

## 5. Determinism

What must be committed: (1) an append-only, git-tracked manifest of every daily read's *result* — date,
docket, URL, byte length, SHA-256 — written at the moment the read happens, never regenerated later; (2)
the fetched PDF bytes, or their hashes with the build refusing to proceed on a mismatch, since builds have
no network (the *NO PART* pattern: fetched once outside the build, hash-checked at the top of every run).
"Same seed, same work" for a live-world input means: given that manifest plus those hash-verified bytes,
the build reproduces the shipped object byte-for-byte regardless of what the live index says today. Git is
the archive; the manifest is the seed.

## 6. The extractor — confirmed correct; one concrete fragility found

Ran `extract-order-text.py` on all five verified PDFs. Output matches the proposal's quoted text exactly,
including the DUCKETT ET AL. plural. Independently re-derived the aggregates: **72 Miscellaneous Orders,
55 distinct days, 296-day span, 79 total order-days** — all match.

**Fragility, evidenced:** the extractor inserts a literal newline at every `Td`/`TD`/`T*` positioning
operator, so any downstream literal-substring count against its raw output will silently under-count a
phrase that wraps across a line — exactly the failure this house has recorded twice (*in forma pauperis*
counted as 0 where it appears 14; a Rule 38(a) count of 2 where there are 3, because a folio number split
the phrase). `MATERIAL-2026-07-31.md` says whitespace was flattened before its own count, but **that
flattening lives in session discipline, not in the committed script.** A future consumer who does not
remember to flatten first will reproduce the identical bug a third time.

## 7. The three études

| Étude | Buildable in one session | Needs that does not exist yet | Single most likely failure |
|---|---|---|---|
| **1 — Stills** | **Yes** (fetch + render ≈ 3 min; column layout holds at 1 % of measured ceiling) | Nothing technical | **Not established:** whether any of the 72 miscellaneous orders is more than one PDF page. The 5 verified samples are confirmed 1-page; the other 67 are unverified. A multi-page unit breaks the "one page-height per day" model in §1/§3 |
| **2 — Reading scale** | **Yes**, technically | Nothing technical | *NO PART*'s only proven fix for native-resolution legibility at 390 px is a visitor-operated horizontal scroll — and étude 2's own kill condition forbids "any affordance the visitor must operate." A real, precedented tension |
| **3 — Differential pilot** | **Yes** — "severed readers" in this house's established practice are **fresh model instances**, not a human panel; no new infrastructure | Nothing | The proposal does not state, the way *NO PART*'s pre-registration did in writing, that this is a legibility probe and **not human evidence**. Omitting that label risks the tier blur the protocol names as the cardinal sin |

## Bottom line

Rendering works and is fast enough. **Size is the real wall and it arrives early — around 21–22 pages,
not 30 or 72.** The blank column is not a risk at any length this work will reach. **The
daily-read-without-a-session claim is false as currently described** — no infrastructure for it exists,
and building it is a real, unbuilt cost. The extractor is sound but carries a known, previously-fatal
house bug pattern that is not fixed inside the committed tool. All three études are technically buildable
in one session; two carry named, evidenced risks worth the gate's attention.

---

## The conductor's check (session 53)

`.github/workflows/auto-land.yml` was opened first-hand and is the repository's **only** workflow file.
Its cron merges branches and fires a cross-repo dispatch; it performs no fetch of any external source.
`SITE-API.md` line 56 carries the quoted size guideline verbatim and line 107 the per-file and file-count
limits. **Both findings upheld.**
