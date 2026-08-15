# VERIFIER-96 — the seventh premiere gate on STILL DARK

**The object, hashed at the start of this pass and again at its end, unmoved:**

```
projects/season1/still-dark/index.html
  sha256 e0f41e9105658901b03f1653df45e9f9a6963c780a1374a7582fe29cc44bad0b   (start)
  sha256 e0f41e9105658901b03f1653df45e9f9a6963c780a1374a7582fe29cc44bad0b   (end)
git rev-parse HEAD
  2d11294240cc056b29c1d969109ad8088f913269   (start)
  2d11294240cc056b29c1d969109ad8088f913269   (end)
git status --porcelain — empty at both ends
```

Nothing in this repository was written by this pass but this file. Scratch work went to `/tmp`.
`data.py --write`, `tools/live.py --write`, `render.mjs` and `capture/capture.py` were not run here.

---

# VERDICT: **FAIL**

**Nine findings, seven of them IN SCOPE for the gate.** Two of the three things this session
built are false as published: **the corpus freeze does not hold** — a thirteenth list moves the
face and takes `data.py --check` to exit 1, which is the exact opposite of what `ADDENDA.md`
and the builder's own comment promise (finding 1) — and **the four-day comparison's headline
finding is an artefact of where this record begins, not a property of the days** (finding 2),
demonstrated by re-measuring all four rows under matched conditions.

Everything the gate asked me to check hardest that is **not** in the findings below checked out
exactly, and is enumerated in §B. **The ambition audit HELD** (§C).

---

## A. FINDINGS

### 1. THE FREEZE LEAKS, AND IT LEAKS INTO THE ONE BLOCK THE WORK USES TO PROVE ITSELF. — IN SCOPE

**Check.** I copied the repository to `/tmp` with its git history intact, synthesised one capture
dated after the freeze instant (`fetched_at_utc 2026-08-16T05:11:09Z`, `edition_date 2026-08-16`,
three new names, `days_dark 30` — a window reaching 4 August), dropped it into the `/tmp` copy's
`captures/`, and ran the committed builder there.

```
python3 <tmp>/projects/season1/still-dark/data.py --check
  ISLAND DIFFERS from the captures        EXIT=1
```

Diffing a fresh build of the doctored copy against a fresh build of this repository returns **one
changed field**, and it is `output`:

```
<  "output": "… 32 capture(s) read, 12 distinct edition(s) …  SHARE knowable on the day … 22%–38%  (11 of 29–49) …"
>  "output": "… 33 capture(s) read, 13 distinct edition(s) …  SHARE knowable on the day … 21%–34%  (11 of 32–52) …"
```

**Cause, in the committed source.** `build()` freezes every `load(CAPTURES)` at `FREEZE_AS_OF` —
except that `output` and `commands[0]` are built by `run_day()` (data.py:218), which shells out to
`day.py DAY` **with no `--as-of`**. Two island fields are live. One of them moved in the test; the
other (`head -{summary_lines(run_day())}`) is live too and merely happened not to move.

**What is therefore false, on the work and in the documents that travel with it:**

- `ADDENDA.md`: *"`data.py` loads the captures as of the frozen instant (`FREEZE_AS_OF`), so a
  thirteenth list changes neither the published band nor a single stop on the run, and
  `python3 data.py --check` keeps passing on the night one arrives."* — **the last clause is false
  by demonstration.** It exits 1.
- `data.py` lines 67–68: *"So a thirteenth list changes nothing on this face, `--check` keeps
  passing on the night one lands."* — **false.**
- `frozen.line`, printed at `#sd-frozen` on the face: *"every list that arrives after that instant
  … none of them moves a number on this face."* — the committed HTML is static, so nothing moves
  without a rebuild; but the number the face prints under **"verbatim, unedited"** is not a frozen
  number, and the first rebuild after a thirteenth list prints `21 %–34 % (11 of 32–52)` in that
  block while every other figure on the page stands at `22 %–38 % (11 of 29–49)`. One face, two
  bands, one of them captioned *verbatim*.

**And the second half of it, which the leak currently hides.** The two commands the face prints
for a stranger — `day.py 2026-08-04 | head -7` and `day.py 2026-08-04` — carry **no instant**. On a
page that declares its corpus frozen at an instant, the reproduction command the face hands the
reader is the live one, and from the first list after the freeze it disagrees with the output
printed directly beneath it. `ADDENDA.md` knows this and prints the frozen command — but
`ADDENDA.md` is named on the face only as where addenda are published, never as where the
reproducing command lives, and it is not linked.

*A note on the shape of the repair, because it matters to the next gate: if `output` is frozen
without more, then nothing in this house will notice finding 4 below. Today `--check` fires on the
next list. After the obvious fix, it will not.*

---

### 2. THE COMPARISON'S FINDING IS NOT ESTABLISHED. THE SPREAD IS THE RECORD'S OWN START. — IN SCOPE

`compare.finding`, printed at `#sd-compare-finding`:

> *"How badly a register under-reports the present is not a constant. It is a property of the day,
> and in this record four consecutive days of one sea, read at one age, differ by a factor of ten."*

**Check 1 — what the four numerators actually are.** Counting, off the frozen corpus, the names each
edition carries and how many of them are new to this record:

| edition | names in the list | new to this record | the row's numerator |
|---|---|---|---|
| 2026-08-04 | 11 | **11** | **11** |
| 2026-08-05 | 8 | **3** | **3** |
| 2026-08-06 | 7 | **2** | **2** |
| 2026-08-07 | 6 | **1** | **1** |

The four numerators are, exactly, the *new-to-this-record* counts. The top row's is 11 because
**this record has no list before 4 August**, so every name in the day's own list is new by
construction; the other three are only the increment, because names carried over from an earlier
list are pinned by `index()` to a window ending on or before that earlier edition and leave both
ends of the later day's quotient.

**Check 2 — measure all four the way the published one is measured.** For each day I built a
captures directory holding only the editions dated on or after that day — i.e. a record that
*begins* on the day, which is the only condition under which the top row's numerator was formed —
and ran the same committed instrument at the same as-of instant:

```
day 2026-08-04, record begins 2026-08-04 (32 captures):  31 %–73 %   (11 of 15–35)
day 2026-08-05, record begins 2026-08-05 (31 captures):  22 %–47 %   ( 8 of 17–36)
day 2026-08-06, record begins 2026-08-06 (28 captures):  19 %–39 %   ( 7 of 18–37)
day 2026-08-07, record begins 2026-08-07 (24 captures):  16 %–46 %   ( 6 of 13–38)
```

**A factor of 1.9 on the falling end and 1.6 on the ceiling — not ten.** The denominators barely
move across the four rows either way (35 · 36 · 37 · 38). The whole of the published spread lives
in the numerator, and the numerator is governed by the overlap between consecutive upstream lists
plus where this record starts.

**Why this is a Verifier finding and not a matter of taste.** The face itself prints the mechanism
eleven lines above the comparison, in `fall.held`: *"This record's first list is the day itself, so
the eleven is fixed from below by where this record begins — not by the sea."* That is banked
failure 80, paid on the face at the last gate. **The comparison block does not carry it**, its top
row is the only one of the four to which it applies, and the block draws a claim about a *class* of
record — *"It is a property of the day"* — out of the resulting spread. The published measurement of
each individual row is arithmetically sound; what is not established is that the four rows are
comparable, which is the entire claim the block exists to make.

*Nothing here says the true spread is 1.9 rather than 10 — my truncation is a different measurement
too. It says the evidence on the face does not distinguish a property of the day from a property of
where this record opens, and the sentence chooses one of the two.*

---

### 3. "DIFFER BY A FACTOR OF TEN" IS TRUE OF ONE END OF THE BAND AND FALSE OF THE OTHER — AND THE OTHER IS THE END THIS WORK CALLS UNCONDITIONAL. — IN SCOPE

**Check.** Taken off the four rows as printed:

- falling ends: 31 / 3 = **10.3** — the claim holds.
- ceilings: 73 / 12 = **6.1** — the claim does not hold. Unrounded, 0.7333 / 0.1250 = **5.87**.

The finding says *"four consecutive days … differ by a factor of ten"* without naming an end. The
end it is true of is the one `day.py`'s own `share_band_condition` says *"does assume every one of
those N was in fact dark on the day"*; the end it is false of is the one the same string calls
*"assumes nothing … a ceiling over all of them"* — the single unconditional result this work has,
won at the gate of 92 and defended at 94. **The headline number of tonight's largest new claim is
taken off the assumption-bearing end and is wrong by 40 % on the other.**

This is banked failure 73 (*the work hedging away its own result*) inverted: the same confusion
about which end carries the assumption, spent this time in the flattering direction.

---

### 4. THE FACE CALLS THE FROZEN FIGURE **LIVE**, ELEVEN LINES ABOVE THE SENTENCE THAT SAYS THE PAGE IS FROZEN. — IN SCOPE

**Check.** In `STATE-1.txt`, the committed screen-reader record of the committed page:

```
line 404:  LIVE · as this record measures it now, from 32 saved copies of 12 lists —
line 415:  This page is frozen. Its corpus is the thirty-two saved copies this record held at
           2026-08-15T04:36:57Z … none of them moves a number on this face.
```

and `announce.mjs`, run on the committed object, speaks:

```
31836 ms  [spoken]  The run has finished. The figure now standing is this record's live one, 22 %–38 % …
```

Three strings — `fall.now.status = "LIVE"`, `arrive.run_states.started`, `arrive.run_states.done` —
assert that the standing figure is what this record measures **now**. Today that is true only
because `FREEZE_AS_OF` happens to equal the newest capture's fetch instant. The freeze exists
precisely so that the record moves while the face does not; from the thirteenth list onward these
three strings are false, and no rebuild is required to make them so. `ADDENDA.md` states the
premise in terms: *"`capture.py` may still be run … and its output still lands."*

This is banked failure 42's shape exactly — *a false sentence with a delay fuse in it* — and 67's.
The README's own live regions carry their instant (*"Live, at the capture of 2026-08-15T04:36:57Z"*)
and survive; the face's do not. Per finding 1's closing note, once the leak is repaired nothing in
this house will fire when they go false.

---

### 5. `tools/frame.mjs` APPLIES A 390×844 READING AS A FLOOR AT 320×568. THAT IS A CATEGORY ERROR, AND THE FLOOR IS UNMEETABLE THERE BY ARITHMETIC. — IN SCOPE

The gate asked which it is. **Category error**, on three counts, and the third is decisive.

**Check.** Run on the committed object, `NODE_PATH=/opt/node22/lib/node_modules node tools/frame.mjs`:

```
small phone 320×568 — figure-top to controls-bottom: 411 px of 568 — HOLDS
  the hole sharing a frame with the whole figure: 0 px, 0 of 38 chips at the last stop
      — floor 268 px / 22 chips — UNDER
```

The floor is set by `const floorPx = vp.w <= 480 ? 268 : null;` — a width predicate deciding a
question about height.

1. **Provenance.** The instrument's own header states what 268/22 is: *"floored at session 89's own
   reading — 268 px and 22 of 24 chips at 390×844."* It is an empirical high-water mark taken on one
   viewport, not a derived requirement about the work. Its warrant does not travel to a viewport
   session 89 never measured.
2. **Dimension.** 268 px is 31.8 % of an 844 px screen and 47.2 % of a 568 px one. The same integer
   is a different demand.
3. **It cannot be met at 320×568 at any scroll position, under any staging.** From the instrument's
   own printed budget at that viewport: figure-top → controls-bottom **411 px**, then the day's own
   heading **30**, the names the day itself printed **135**, the hole's heading **59** — so the
   hole's first pixel stands **at least 635 px** below the figure's top, before inter-block margins,
   in a **568 px** viewport. With the whole figure on screen the viewport ends ≥ 67 px before the
   hole begins. The measured `0 px` is not a shortfall; it is the only value the geometry permits.
   **The instrument prints `UNDER` against a floor arithmetic forbids that viewport from ever
   reaching.**

And the instrument's own stated warrant for the floor being stable is falsified by the act of adding
the viewport: *"it cannot drift upward as the hole grows: more chips do not move the figure, **and
the viewport does not change size**."* Tonight the viewport changed size.

**The exit-code question: verified, still true.** `over` is assigned in exactly one place —
`if (hi > vp.h) over = Math.max(over, hi - vp.h)` — and `process.exit(1)` is guarded on `over`
alone. The hole span only `console.log`s. Confirmed by reading and by running: 320×568 printed
`UNDER` and the process exited **0**.

---

### 6. THE README'S GUARD TABLE DESCRIBES A SUPERSEDED OBJECT, AND SIX OF ITS CELLS ARE FALSE AGAINST THE ONE THAT SHIPS. — IN SCOPE

`README.md` travels with the work and is named in this gate's scope. Its guard section is headed
**"THE STATE OF EVERY GUARD, SESSION 95"**, its column header reads **"tonight, on this page"**, its
prose says *"Every figure below was taken tonight on the committed object; each line names the
command and what makes it pass"* — and its dateline names the object as
**`index.html` sha256 `52215bf9…`**. **The object that ships tonight is `e0f41e91…`.**

I re-ran every instrument in the table on the committed object. Nine of the twelve rows hold exactly
(§B). These do not:

| cell | README says | tonight, on `e0f41e91…` |
|---|---|---|
| `frame.mjs` criterion | "at **four** viewports including two short ones" | **five** — 320×568 added |
| `frame.mjs` criterion | "at 390×844 — **the one viewport the floor is enforced at**" | the floor verdict now prints at **two** viewports, and reads **UNDER** at the new one |
| `frame.mjs` reading | "1400×900: **700 of 900**" | **687 of 900** |
| `frame.mjs` reading | — | 320×568 is **absent from the table**: 411 of 568, hole 0 px / 0 of 38, UNDER |
| `live.py` reading | "**44** superseded figures, 0 of them unstamped" | **39 superseded figures, 0 of them unstamped** |
| dateline | object `52215bf9…` | object `e0f41e91…` |

The 1400×900 span moved because of this session's own DRAMATURG-95 cut 2 — the apposition leaving
ten stops shortened the head by 13 px. That is the table's stated failure mode verbatim: *"Every one
had moved because that session's own cuts changed the head, and the paragraph explaining them was
not re-run."*

**In mitigation, and stated because it is real:** the heading and dateline are honestly marked
SESSION 95 and honestly hashed to session 95's object, so nothing here is undated in the way
`VERIFIER-95` blocking 5 found. **Against it:** the column still reads *tonight*, `KRITIKER-89`
condition 3 requires each guard's **current** output printed truthfully, and a stranger who runs the
six commands beside the work tonight gets six different answers. The README is also silent on both
of tonight's two largest changes — the freeze and the comparison — and never names `ADDENDA.md`.

---

### 7. `ADDENDA.md` DIRECTS THE NEXT SESSION TO A FILE THAT DOES NOT EXIST. — IN SCOPE

**Check.** `ADDENDA.md`, closing paragraph: *"…that is a different matter and belongs in the register
beside this file, `OPEN-DEFECTS.md`, with the element paused."*

```
ls projects/season1/still-dark/OPEN-DEFECTS.md  → No such file or directory
ls projects/season1/OPEN-DEFECTS.md             → No such file or directory
```

Written as an existing address ("*the* register beside this file"), not as an instruction to create
one. Banked failure 68's shape: an address that opens onto nothing.

---

### 8. *"THE INSTRUMENT KEEPS PUBLISHING DAILY AND THIS RECORD KEEPS SAVING IT"* — HALF SOURCED, HALF A FORECAST WITH NO MECHANISM BEHIND IT. — IN SCOPE

The gate asked whether this sentence, printed at `#sd-frozen`, is consistent with what the
repository actually does.

- **First half, SOURCED and true.** The method sheet at <https://frankbueltge.de/werke/ghost-fleet/>
  says under *2. Cadence*: *"Daily. Window: disabling events that ended in the last 7 days
  (complete vanish-and-return stories)."* Fetched, 200, verbatim.
- **Second half is a claim about this house's future conduct, and nothing in this repository
  performs it.** `.github/workflows/` holds exactly one file, `auto-land.yml`, which merges research
  branches; there is no scheduled capture job anywhere. Every one of the 32 captures was written by a
  session running `capture/capture.py` by hand. The record has in fact saved a list on each of
  4–15 August, so the sentence is true of the past — but it is written in the present continuous, as
  the standing condition that makes the freeze meaningful, and the freeze's whole design assumes it.
  `ADDENDA.md` gets this right and the face does not: *"`../capture/capture.py` **may** still be run
  … and its output still lands."*

*Not blocking on its own; blocking as the load-bearing premise of finding 4.*

---

### 9. THREE COMMANDS THE GUARD TABLE NAMES EXIT 1 WHEN RUN AS NAMED. — IN SCOPE (minor)

**Check.** From the work's own directory, exactly as the table prints them:

```
node ../../../tools/tiers.mjs   → EXIT=1, unhandled navigation error:
    file:///…/still-dark/projects/season1/still-dark/index.html
node ../../../tools/width.mjs   → EXIT=1, same shape
```

Both resolve their default target against the working directory, so they only run from the
repository root, where both pass (`tiers` 0, `width` 0 — §B). The table states that *"each line names
the command"* and prints exit **0** beside both. Pre-existing, not tonight's; a premiere gate does
not inherit.

---

## B. WHAT I CHECKED AND FOUND TRUE

**Run without a pipe, on the committed object, exit codes as taken:**

| instrument | exit | result |
|---|---|---|
| `python3 data.py --check` | **0** | `island matches the captures` |
| `node announce.mjs` | **0** | 12 stops · dwell 14,118 · beat 1,600 · 11 beats, protected {5,9,10} · last state 30,118 · closing 31,718 · ceiling 45,000, 13,282 of room · 1 live region · 4 writes in 33,718 ms · 3 spoken · 13 figure rewrites · promise *"about thirty-two seconds"* agrees |
| `node gaps.mjs` | **0** | 0 of 49 rows failing, tightest 8.17 px · axis 0 collisions at 7 widths, tightest 11.12 px, 4 labels below 700 px and 10 at/above |
| `node tools/tiers.mjs` | **0** | every printed figure sits in a scope carrying a tier word |
| `node tools/width.mjs` | **0** | 280→1920 px, CLEAN |
| `node tools/turn.mjs` | **0** | 1400 px: hole's heading 13,167 px² · share 11,665 · three chips 6,343 · count that turns 8,958 = 30.1 % · six nodes — matches the README cell exactly |
| `python3 tools/renders.py` | **0** | RENDERS MATCH THE PAGE; `RENDERS.json` `index_sha256` = `e0f41e91…`, the shipping object |
| `node tools/frame.mjs` | **0** | all five viewports HOLD; see finding 5 |
| `node tools/fold.mjs` | **1** | 13 places, 156 sightings — **published red, as the README says** |
| `python3 tools/live.py` | **0** | 4 regions, 0 disagreeing · 39 superseded figures, 0 unstamped |

**The four-day comparison, every figure re-taken with one command per row.** Each row reproduces
**exactly**, including the fraction string:

```
day.py 2026-08-04 --as-of 2026-08-12T18:23:12Z → 31%–73%  (11 of 15–35)   face: 31 %–73 %, 11 of 15–35  ✓
day.py 2026-08-05 --as-of 2026-08-13T17:02:56Z → 10%–25%  ( 3 of 12–31)   face: 10 %–25 %,  3 of 12–31  ✓
day.py 2026-08-06 --as-of 2026-08-14T20:45:26Z →  6%–15%  ( 2 of 13–32)   face:  6 %–15 %,  2 of 13–32  ✓
day.py 2026-08-07 --as-of 2026-08-15T04:36:57Z →  3%–12%  ( 1 of  8–33)   face:  3 %–12 %,  1 of  8–33  ✓
```

- **The instants are the code's claim and none is typed.** For each day D I sorted every capture
  whose `edition_date` is D+8 and took the earliest fetch: `2026-08-12T18:23:12Z`,
  `2026-08-13T17:02:56Z`, `2026-08-14T20:45:26Z`, `2026-08-15T04:36:57Z` — the four printed. ✓
- **The fraction string obeys `day.py`'s own rule.** `day.py` prints `({obs} of {b[0]+obs}–{b[1]})`;
  `matched_maturity()` builds `f"{obs} of {b[0]+obs}–{b[1]}"`. Same rule, and the four outputs agree
  character for character with the four rows. ✓
- **"The published day is the highest of the four" — TRUE**, and on both ends: 31 > 10 > 6 > 3 and
  73 > 25 > 15 > 12. ✓
- **`compare.lead`'s "open for eleven days" — TRUE**: 2026-08-04 → 2026-08-15 is 11 days, computed
  from the corpus, not typed. ✓
- **`compare.heading`'s "EACH READ AT EIGHT DAYS OLD" — the gate asked whether eight days is the age
  of the day or of the record. It is the age of the DAY, and only approximately.** The exactly
  matched quantity is the *edition-date offset* of the newest list included (D+8 in all four,
  verified: 9, 10, 11 and 12 editions read respectively, each ending at D+8). Elapsed time from the
  start of day D to the as-of instant is **8 d 18 h 23 m · 8 d 17 h 02 m · 8 d 20 h 45 m ·
  8 d 04 h 36 m** — the four ages differ by 16 h 33 m, and none is eight days. **The record is not
  read at one age at all**: it is 9, 10, 11 and 12 editions deep, and — finding 2 — 0, 1, 2 and 3
  editions deep *before* the day. `lead`'s formulation ("each at the instant it first held the list
  dated eight days after its own day") is exact; the heading's compression is defensible to within a
  day; `lead`'s *"the same record read at one age"* is not true of the record.

**The freeze's own counts.** At `2026-08-15T04:36:57Z` the record holds **32** captures and **12**
distinct edition dates, and no capture in this repository has a fetch instant after it. The window's
two ends, `2026-08-04` and `2026-08-15`, **are edition dates** — the first and last of those twelve —
not fetch dates. `frozen.captures`, `frozen.editions` and `frozen.window` all reproduce. ✓
`ADDENDA.md`'s frozen command returns exactly what the face prints: `22%–38% (11 of 29–49)`. ✓

**DRAMATURG-95 cut 2, taken correctly.** The apposition prints at exactly one stop — `+1 DAY`,
`edition 2026-08-05`, the first stop with a non-zero lag — and reads *", a day after the day had
ended"*, which is right for a lag of one. At all 12 stops `when_fixed + " " + when_tail == when`,
byte for byte. No stop misstates its own lag: `days_after` runs 0…11 against editions 04…15 and each
`printed` label matches. Downstream: `announce.mjs` exits **0** and speaks nothing that turns on the
clause; `STATE-1.txt` carries stop 0's tail (`"counting the lists up to 4 AUG."`) with zero
occurrences of `"after the day had ended"`, correct for the resting page; `renders.py` confirms
`STATE-1.txt` and both PNGs were made from `e0f41e91…`. ✓

**Correction (a) — README ~1263, "ninety" → "seventy".** The arithmetic verifies:
`400 × 66 + 3 × 1,600 + 14,118 = 26,400 + 4,800 + 14,118 = 45,318 > 45,000`. ✓ And **seventy is the
right list count.** Re-deriving from `data.py`'s own budget (`budget = 45,000 − 14,118 − 3 × 1,600 =
26,082`, `free = N − 4`):

```
N = 68  free 64  free_beat 407  total 44,966  green
N = 69  free 65  free_beat 401  total 44,983  green
N = 70  free 66  free_beat 395 → floored to 400  total 45,318  RED
```

Seventy is the first count at which the floor binds and the total exceeds the published ceiling. ✓
The neighbouring claim *"at twenty-one lists the free beats begin to compress"* also verifies:
`free_beat` is 1,600 at N = 20 and 1,534 at N = 21. ✓

**Correction (b) — the withdrawal of "the turn recedes from the visitor at 1.6 s a night".** The
replacement is TRUE against the published derivation. `turn_stop = 7` (certain counts across the 12
stops: 0,0,0,0,0,0,0,**2**,4,11,15,18). Stop 7 lands at `first_dwell + sum(beats[:6]) = 14,118 +
6 × 1,600 = 23,718 ms`. Re-deriving the budget at **eleven** lists: 10 beats, protected {5,8,9}, 7
free, `26,082 // 7 = 3,726 → 1,600`, so every beat was 1,600 and stop 7 landed at **23,718 ms**
there too. It did not recede. And the replacement's forward claim holds: as N grows the free beats
shrink and beats[0…4] are free, so the turn can only move **earlier**, while `done_ms` — the last
state — grows toward the ceiling. ✓
*(`data.py`'s comment carries the same correction and matches the README's.)*

**Every external URL on the face resolves and says what the page says it says.** All fetched, all
200:

- <https://frankbueltge.de/werke/ghost-fleet/> — the four strings the work quotes from it are
  **verbatim**: *"The AIS picture of the seas looks complete. It is not — ships switch off their
  transponder on purpose to vanish."* · *"Daily. Window: disabling events that ended in the last 7
  days (complete vanish-and-return stories)."* · *"The index counts all examined; the case and list
  show named vessels."* · and the thresholds the face glosses — *"GFW returns only high-confidence,
  intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore."* The restraint the face repeats is
  faithful to *"is a probability, not proof"* and *"No claim of illegality against vessel or state."* ✓
- <https://frankbueltge.de/ghost-fleet/> — **byte-identical to the capture the freeze is anchored
  on**: 31,882 bytes, sha256 `4009e3b638611771…`, edition **15 August 2026**, case SHILLA EXPLORER
  (KOR) 53 days, aggregates 81 / 233 / 5,757 / 2,922 — all matching
  `captures/2026-08-15T043657Z.json` field for field. **No thirteenth list has arrived**, so
  `ADDENDA.md`'s *"no list has arrived since"* is true as I write. ✓
- <https://biblio.ugent.be/publication/8647789> — Brysbaert, *How many words do we read per minute?*,
  Journal of Memory and Language **109** (2019). Abstract: *"Based on the analysis of 190 studies
  (18,573 participants), we estimate that the average silent reading rate for adults in English is
  **238** words per minute (wpm) for non-fiction."* The face's `first_dwell_note` — *"56 words at 238
  wpm (Brysbaert 2019, mean adult silent reading of non-fiction English)"* — is exact, as is the
  comment's "190 studies and 18,573 participants". ✓
- <https://hrdag.org/2013/03/20/mse-stratification-estimation/> — *Multiple Systems Estimation:
  Stratification and Estimation*, **Amelia Hoover Green, March 20, 2013**, HRDAG, and it is about
  capture probabilities. The face's `refused_source` names all four correctly. ✓
- All 49 `globalfishingwatch.org/map/vessel/…` links — sampled and reachable, 200. ✓

**No upstream material re-served above its live status.** The word **VERIFIED** appears **zero**
times in `index.html`; no Meridian material appears anywhere in the work; the upstream instrument is
the ecology's own Ghost Fleet, and every value taken from it is tiered **SOURCED**, with upstream's
restraint travelling on the face beside the names it restrains. ✓

**The cut block's SOURCED figures, re-counted off the frozen corpus.** *"Of the 230 examined, 82 were
dark inside national waters · 5,641 events in the window"* ✓ for the edition of 4 August; *"11 of
230"* ✓; *"six to eleven names of the 189 to 265 disappearances"* ✓ (names 6–11, examined 189–265
across the twelve editions). ✓

**The tier line on the face.** The legend's three lines cover the material they name, and the new
comparison block carries its own (`"DERIVED from the OBSERVED captures by the same instrument as the
figure above"`). One small gap, reported without weight: the frozen line publishes a **count of
lists** (twelve), and no legend line names that quantity — SOURCED covers *"each list's own date"*,
DERIVED covers *"the count of names in each list"*, OBSERVED covers *"what this page saw"*. Failure
25's shape at its smallest; `tiers.mjs` passes because the page root carries all three words.

---

## C. THE AMBITION AUDIT — **THE FORECAST HELD**

`PROJECT.md`, "The forward record": *"one calendar day held open across **at least the seven nights
of its cited window**, publishing the measured share of that day's darkness knowable on the day
itself, checkable against the captures."*

On evidence:

1. **The cited window is seven days** — `method.window_days = 7` in every capture, and upstream's own
   *"ended in the last 7 days."*
2. **The day is held open across twelve editions**, dated 4 August to 15 August 2026 —
   **eleven nights past the day**, against a promise of seven. 32 saved copies over eleven distinct
   fetch dates, 5–15 August, with no gap.
3. **The share is published and measured, not asserted**: `22 %–38 % — 11 of 29–49`, built by
   `data.py` from the captures, with `--check` green on the committed island.
4. **It is checkable against the captures by a stranger with one command**, which I ran:
   `python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-15T04:36:57Z` returns
   `22%–38% (11 of 29–49)` — the number on the face, exit 0.
5. It is **not** the named failure mode (*"a single-sitting screen with seeded times"*): twelve
   states, each reproducible at its own instant off immutable saved bytes.

**HELD. Not a failed forecast.** *This ruling is on the promise as written, and is independent of
findings 1–9, none of which touches clauses 1–5.*

---

## D. WHAT IS OUT OF SCOPE

Under the architect's rule of 2026-08-15 I looked for errors in this session's account of its own
evening and **found none to bank** — this pass read `PROJECT.md`, `ADDENDA.md`, `README.md`,
`data.py`, `frame.mjs`, `day.py`, `announce.mjs` and `STATE-1.txt`, and every finding above attaches
to the work, the instrument, or a document that travels beside them. I did not read the journal or
`WORKBOARD.md`, which the rule places outside the gate.

**Findings 1–9 are all IN SCOPE.** The three that hold the premiere on their own are **1** (the
freeze is false as published, in the work's own documents and on its face), **2** (the largest new
claim on the face is not established by the evidence beside it) and **3** (its headline number is
wrong on the end of the band the work calls unconditional).

*This memo ships unedited beside the work.*
