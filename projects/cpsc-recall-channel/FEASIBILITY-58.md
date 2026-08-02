# THE BUILDER — feasibility finding on *STOP USING IMMEDIATELY*

*Session 58, 2026-08-02. Efficient tier. Convened as a **feasibility voice only** — nothing was
built, no project file was written except this one. Every number below is measured tonight against
real files and real HTTP responses, or is explicitly marked "not measured." I invented nothing.*

*Method: `curl` against the live API and a real image host; Python 3 + Pillow 12.3.0 (installed
this session — not previously present in this repo's environment) for pixel dimensions and
re-encoding. All source images and API JSON are kept in the session scratchpad, not this repo,
except the two contact-sheet PNGs named in §5, which are evidence and are committed.*

---

## 1. THE INGEST — the API carries images; exact field names

**Fetched directly**, no fetch-tool intermediary:
`https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2026-06-01&RecallDateEnd=2026-08-02`
→ **HTTP 200**, 300,096 bytes, 99 recall records. Refetched a second time: **byte-identical**
(same md5, `a28b2b4a114b27b2d3b70f7921365bb2`) — the endpoint is at least stable within one session.

**The proposal's open question (§15) is answered: yes, the JSON carries image URLs directly.**
Every one of the 99 records in the window carried a non-empty `Images` array (0 records with no
image). Exact top-level field names, as returned:

```
RecallID, RecallNumber, RecallDate, Description, URL, Title, ConsumerContact,
LastPublishDate, Products[], Inconjunctions[], Images[], Injuries[], Manufacturers[],
Retailers[], Importers[], Distributors[], SoldAtLabel, ManufacturerCountries[],
ProductUPCs[], Hazards[], Remedies[], RemedyOptions[]
```

`Images[]` items are `{"URL": "...", "Caption": "..."}`. Field-to-notice mapping, confirmed against
the exact record the proposal quotes in full (M3, recall `26651`, retrieved here byte-for-byte
identical in substance to the proposal's §5 quotation):

| draft rule's field (§7.3) | actual JSON field |
|---|---|
| First product image | `Images[0].URL` |
| RecallNumber | `RecallNumber` — `"26651"` |
| RecallDate | `RecallDate` — `"2026-07-30T00:00:00"` |
| Hazard sentence | `Hazards[].Name` |
| Sold-at | `Retailers[].Name` (free text, not structured — `SoldAtLabel` is `null` in every record checked) |
| Importer/manufacturer | `Importers[].Name`, `Manufacturers[].Name`, `ManufacturerCountries[].Country` |
| Consumer instruction | `Remedies[].Name` |
| Incidents/injuries | `Injuries[].Name` (free text, e.g. *"HARPPA has received three reports of tower stools collapsing or tipping over, resulting in two injuries..."* — matches the proposal's M3 quotation exactly) |
| Notice URL | `URL` |

**A real image, fetched and measured:**
`https://www.cpsc.gov/s3fs-public/Picture20_3.jpg` (recall `26651`, HARPPA Nordi Toddler Tower
Stools — the exact object in the proposal's §5) →

- **Host:** `www.cpsc.gov`, backed by **AmazonS3** (response headers: `server: AmazonS3`,
  `x-amz-request-id`, `x-amz-version-id` present — this is a versioned S3 bucket fronted by the
  cpsc.gov domain; see §4 for what that implies).
- **HTTP status:** 200.
- **Content-Type:** `image/jpeg`.
- **Content-Length:** 58,943 bytes.
- **Pixel dimensions (measured with Pillow):** 758 × 575.

The proposal's stated uncertainty — *"I did **not** inspect the API's image fields... If the images
are only on the HTML pages, the ingest is a different job"* (§15) — is resolved: **it is not a
different job.** The API is a complete, single-fetch ingest: one request per date range returns
every field the draft rule needs, images included, at a real, dereferenceable, versioned-S3 URL.

---

## 2. THE BYTE CEILING — the decisive measurement

`SITE-API.md` read first (this repo, root). Binding facts, quoted:

> *"Runtime is offline. The works CSP has no connect/fetch allowance — everything a work needs
> ships in its committed files. No external requests, ever."*
> *"raster images, fonts, audio, wasm do **not** travel. The build must **inline** such assets as
> `data:` URIs (the works CSP allows `img-src data:`...)"*
> *"Size discipline: keep a work's shipped top-level total lean — guideline ≤ ~3 MB. The bundle is
> a work, not an app."*

Read together, these three sentences force the actual engineering shape of this work: because
nothing can be fetched at runtime, **every image the visitor could ever open — thumbnail and
hand-size, for every object ever admitted — must already be inlined in the shipped bundle at
build time.** There is no lazy-load route inside this contract (see §3, option 3).

### The sample

Downloaded **25 real, first-listed product images** (`Images[0].URL`), spread across all three
publication Thursdays the proposal names (2026-07-16, 2026-07-23, 2026-07-30) — the same weeks as
the proposal's §2 table. All 25 downloads returned HTTP 200. As CPSC actually serves them:

| stat | value |
|---|---|
| n | 25 |
| mean bytes (as served) | 179,033 |
| median bytes | 70,905 |
| min / max | 8,443 / 818,812 |
| formats seen | JPEG (12), PNG (11), GIF (2) — CPSC ships whatever the recalling firm submitted, uncompressed for the web in most PNG cases |

These raw bytes are **not** what would ship — they must be resized and re-encoded for both
entrance and hand-size, then base64-inflated for the `data:` URI. Measured, not estimated:

### Per-object bytes at a plausible shipped encoding

| scale | encoding | mean raw bytes | mean base64 (data URI) bytes |
|---|---|---:|---:|
| **entrance thumbnail** — 64px longest edge | JPEG q75 | 1,391 | **1,856** |
| entrance thumbnail — 32px (comparison, §3) | JPEG q75 | 864 | 1,152 |
| **hand-size** (opened notice) — 480px longest edge | JPEG q82 | 24,495 | **32,662** |
| hand-size — 480px | WebP q82 | 16,696 | 22,262 |
| hand-size — 480px | AVIF q50 | 8,257 | 11,011 |

Measured base64 inflation on this sample: **1.335×** raw (e.g. 24,495 → 32,662), consistent with
the ~1.37× rule of thumb.

**Verbatim text fields** (RecallNumber, RecallDate, Title, Description, Hazard, Remedy, Injuries,
Sold-at/Retailers, Importer, ManufacturerCountry, notice URL) measured across the **full 99-record**
window, plain UTF-8, no base64 inflation: **mean 1,735 bytes/object** (median 1,606, range
1,099–4,006). Text is not the problem — it is ~4.8% of a baseline object's shipped weight.

### Total per object (thumbnail + hand-size + text — both images ship, per the offline-runtime rule)

**Baseline plausible encoding (64px JPEG thumbnail + 480px JPEG hand-size):**
**36,253 bytes/object ≈ 35.4 KB/object.**

### The table asked for

| extent | objects | total shipped bytes | total MB | vs. ~3 MB guideline |
|---|---:|---:|---:|---|
| 1 week (~8 objects) | 8 | 290,024 | 0.28 MB | under |
| **20 weeks (~160 objects)** | 160 | 5,800,480 | **5.53 MB** | **OVER — ~1.85×** |
| 52 weeks (~420 objects) | 420 | 15,226,260 | **14.52 MB** | **OVER — ~4.84×** |

### At what extent does this hit the guideline?

Guideline taken as 3 MiB = 3,145,728 bytes (SITE-API.md's "≤ ~3 MB"). At the baseline encoding, the
guideline is crossed at **≈ 87 objects**. Converting objects to weeks requires a weekly rate, and I
measured two, honestly reported because they disagree:

- **The proposal's own sample** (three Thursdays, 10 + 6 + 9 = 8.33/week): **≈ 10.4 weeks.**
- **My own broader sample** (nine consecutive Thursdays in the JSON window, 2026-06-04 through
  2026-07-30 — counts 9, 16, 9, 10, 12, 7, 14, 7, 15 — mean **11.0/week**, a larger and more
  representative sample than the proposal's three weeks): **≈ 7.9 weeks.**

**Either way, the size guideline is hit in the second month — well under a season, and roughly
half of extent 20.**

### Does extent 20 fit? **No.**

The accumulation test in §10 needs 160 objects live and inlined simultaneously (Cell N is explicit
that "simulated extents are never issued as units and never enter the stock" — the differential
must run on the *real* built stock, not a mock). At the baseline encoding this is **5.53 MB, about
1.85× the guideline.** The size ceiling named in §14 item 5 as one of six things that could kill
this concept **does, in fact, bite before the test the concept requires can be run.**

---

## 3. THREE HONEST OPTIONS, EACH MEASURED

**Checked before proposing anything:** `SITE-API.md` (this repo, root) — the only place this repo
states the works CSP and the size guideline. No per-file byte limit is stated for *works*
specifically (the "≤ 2 MB per file · ≤ 50 files" language in the file applies to **Site PRs**
changing the site's own source, a different mechanism — §"Site PRs" — not to a work's shipped
assets). The guideline that binds a work is the single sentence: *"a work's shipped top-level
total"* — i.e. **the sum across every top-level file in the work directory**, not per file. That
closes off one route before it's proposed: splitting hand-size images across several top-level
`.html` files does **not** evade the ceiling, because the guideline sums across all of them.

### Option A — shrink the entrance thumbnail (32px instead of 64px)

**Measured saving: 704 bytes/object** (1,856 → 1,152 base64 bytes) — **1.9% off the per-object
total.** New ceiling: ≈88.5 objects, i.e. ≈10.6 weeks (proposal's rate) or ≈8.0 weeks (my rate) —
**not a meaningfully later wall.** The entrance thumbnail is a rounding error against the budget:
hand-size images are **94.6%** of a baseline object's shipped weight; the thumbnail is 5.1%; text
is 4.8%(rounding). Shrinking the thing that costs almost nothing does almost nothing.

**Cost measured, not asserted, per the house's own rule against inventing capabilities:** I built
two real contact sheets from the same 25 downloaded images, one per candidate entrance scale (§5).
At 64px, most category distinctions survive (dresser vs. cup vs. stool vs. bottle). At 32px,
several genuinely collapse into indistinguishable blobs — the two toddler step-stools and the
diving regulator in particular. **This route trades legibility the entrance depends on for a
saving too small to move the wall.**

### Option B — a modern codec at hand-size (measured, not assumed)

The task's own caution is warranted: this house was burned once assuming a codec would be "several-
fold smaller" and measuring it 3% larger. So this was measured on the actual 25 sampled images, not
assumed:

| hand-size codec (480px) | mean base64 bytes | ratio to JPEG q82 baseline |
|---|---:|---:|
| JPEG q82 (baseline) | 32,662 | 1.00× |
| WebP q82 | 22,262 | 0.68× |
| **AVIF q50** | **11,011** | **0.337×** |

AVIF at q50 is a **real, substantial** saving on this specific material — not a rounding effect and
not a repeat of the past false assumption. New per-object total (64px JPEG thumb + 480px AVIF hand
+ text): **14,602 bytes ≈ 14.3 KB.** New ceiling: **≈ 215 objects.**

| rate assumption | weeks to ceiling | extent-20 object count | extent 20 fits? |
|---|---:|---:|---|
| proposal's 8.33/week | 25.9 weeks | 167 objects → 2.33 MB | **fits, ~26% headroom** |
| my measured 11.0/week | 19.6 weeks | 220 objects → 3.06 MB | **does not fit — 2% over** |

**This is a genuinely marginal result, reported honestly rather than rounded to a comfortable
answer:** whether AVIF alone rescues extent 20 depends on which weekly rate is trusted, and my
broader nine-week sample (a larger, more representative measurement than the proposal's own
three-week window) puts it **just over** the line, not under it. Extent 52 does not fit under
either rate (5.85 MB). A further squeeze — 320px AVIF q50 instead of 480px — measured at 6,283 mean
base64 bytes, total 9,874 bytes/object, ceiling ≈319 objects ≈ 29–38 weeks depending on rate: closer
to a full season but still short of 52 weeks, and 320px hand-size is a visibly smaller "opened
notice" than the 480px this section started from (not separately contact-sheeted; flagged as
untested for legibility).

**What the contract permits:** `SITE-API.md` names only `img-src data:` and `font-src data:` for
the works CSP; it states no format restriction, so an AVIF `data:` URI is not forbidden by anything
in this file. **What is not established:** the actual browser/runtime AVIF decode support for
whatever the lab site's audience uses — I did not check this (no browser-matrix document found in
this repo) and it is not asserted here as safe. It is a genuine open question, not a decided one.

### Option C — the structural finding: the wall is the hand-size image, and it cannot be deferred

Measured: if a hand-size image were never shipped at all — entrance thumbnail and text only, for
every object, forever — the ceiling moves to **≈876 objects, ≈80–105 weeks (1.5–2 years)**, nearly
5× past the extent-52 test. **The hand-size image is not a fifth of the problem; it is essentially
the whole problem** (94.6% of the baseline per-object weight, 75% even after the AVIF swap in
Option B).

The obvious mitigation — keep a rolling window of hand-size images live and drop older ones back to
thumbnail-only — is **technically compliant with `SITE-API.md`** (nothing there requires the corpus
to stay whole) but **is not permitted by the concept's own draft rule**, checked directly against
`ARTIST-PROPOSAL-58.md`: §6 states *"Every state is permanently addressable"*, and §7.4/§7.5
("no revision," "nothing is edited," "a build whose hash does not match its committed data fails")
make an object's hand-size image a committed, permanent fact once admitted, not a cache entry that
can be evicted. **A route exists, but it is a concept-level trade this Builder voice is not
authorized to make — it removes a promise the Artist wrote, not a technical convenience.** I name it
rather than decide it.

**No combination of the first two options makes an ever-growing, never-closing corpus fit
permanently inside a fixed ~3 MB guideline.** They buy weeks — Option B roughly doubles or triples
the runway — but the proposal's own words are exact: the work *"accumulates one publication day at
a time and can never close."* A fixed ceiling and an unbounded corpus are not reconcilable by
compression; compression only moves the date.

---

## 4. DETERMINISM

**What already holds, measured:** refetching the same date-range URL twice in this session returned
**byte-identical** JSON (same md5). The image at `Picture20_3.jpg` returned a `last-modified` and an
`etag`, consistent within this session.

**What would have to be committed for reproducibility to hold**, following this house's own
precedent (quoted in the prior `FEASIBILITY.md` for `at-any-time`, same pattern applies here):

1. An append-only, git-tracked manifest of every observation — `RecallDate` range fetched, every
   `RecallNumber` admitted that day, and a SHA-256 of each admitted image's raw bytes and of the
   JSON record itself — written at the moment of observation, never regenerated later.
2. The fetched image bytes themselves (or their hashes, with the build refusing to proceed on
   mismatch), since the build has no network per `SITE-API.md`'s "no external requests, ever."
   `npm ci && npm run build` must reproduce the committed output byte-for-byte from committed inputs
   only — that is the workshop contract's own determinism clause, quoted directly.

**Where the source could change under us, evidenced, not hypothesized:**

- **`LastPublishDate` proves CPSC has a mechanism to touch a record after `RecallDate`.** Of the 99
  records in this session's window, **90** carry a `LastPublishDate` one day after `RecallDate` —
  most plausibly a routine indexing lag, but the field's existence is itself proof the API can
  report a record as touched after admission. No content diff is exposed by the API — if a
  `Description` or `Hazards[].Name` string changes between two observations, nothing in the JSON
  says so; only a re-hash of the full record against the committed manifest would catch it.
- **The image host is versioned S3 behind an unversioned URL.** The response headers for
  `Picture20_3.jpg` carry `x-amz-version-id: Pn7boVVNrdFZbh4SjbYaQJmwZj91KJuc` and
  `server: AmazonS3` — the backing store keeps object versions, but the URL the JSON API hands out
  (`Images[].URL`) carries no version pin. **If CPSC replaces a file at the same path (a corrected
  photo, a re-crop), the same URL can silently start resolving to different bytes**, and the only
  defense is the SHA-256-at-observation-time discipline in point 1 above — the API gives no signal
  that this happened.
- Not measured tonight: whether this has ever actually occurred for a CPSC recall photo. Flagged as
  a real, evidenced mechanism, not an observed event.

---

## 5. ONE MEASURED PICTURE — a measurement, not a staging proposal

Two plain contact sheets, assembled from the same 25 real downloaded images, at the two entrance
thumbnail scales measured in §3, on a flat pale ground with no other treatment. **This is evidence
about legibility and density at the byte-scale actually measured above — not a design, and not
this Builder's call to make about how the work should look.**

- `/home/user/studio/etudes/stop-using-immediately/contact-sheet-entrance-scale-MEASUREMENT.png`
  — 25 images at 64px longest edge, 5×5 grid, 4px gutters — **344 × 344 px, 123,138 bytes.**
- `/home/user/studio/etudes/stop-using-immediately/contact-sheet-32px-comparison-MEASUREMENT.png`
  — the same 25 images at 32px longest edge (Option A's candidate) — **178 × 178 px, 36,654 bytes.**

Looking at the two side by side is the entire basis for the Option A finding in §3: at 64px, a
dresser, a step-stool, a refrigerator, a cup, and a bottle read apart; at 32px, several of the same
objects stop reading apart. Both PNGs are committed here as the measurement's record; the 25 source
images they were built from are not (kept in the session scratchpad, out of the repo, per
instruction).

---

## BOTTOM LINE

The API carries images — confirmed, field `Images[].URL`, a real fetch of
`https://www.cpsc.gov/s3fs-public/Picture20_3.jpg` returned HTTP 200, `image/jpeg`, 758×575px,
58,943 bytes. The ingest is a single-endpoint job, not the two-stage job the proposal feared.

The size ceiling is real and it arrives early: **≈8–10 weeks** at a plausible baseline encoding,
against a season that needs **20 weeks** to run its own pre-registered accumulation test.
**Extent 20 does not fit at baseline (5.53 MB, ~1.85× the ~3 MB guideline).** A measured, real
codec swap (AVIF at hand-size, not assumed) roughly doubles the runway to 20–26 weeks depending on
which weekly rate is trusted — and lands **right on the line for extent 20**, fitting under the
proposal's own optimistic three-week sample but **falling ~2% short under my own broader
nine-week sample**. No combination of the two cheap levers (thumbnail size, codec) makes a corpus
that by the concept's own words *"can never close"* fit inside a *fixed* ~3 MB guideline forever —
they buy weeks, not permanence. The single thing most likely to make this unbuildable as specified
is exactly that: **the concept's core commitment (every object permanently addressable at hand-size,
forever, all inlined, no external requests) is structurally incompatible with a fixed shipped-size
guideline once the corpus is large enough — and "large enough" arrives in about two months, not in
a season.**

---

*Written 2026-08-02, session 58, by the Builder. Feasibility voice only. Nothing here rules on
whether the work should open — that is the Dramaturg's and the gate's question. This is what I
measured.*
