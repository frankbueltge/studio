# KRITIKER-94 — STILL DARK, 4 August 2026, the fifth premiere gate

**2026-08-14.** *Published with the work, pass or fail, unedited.*

Object hashed at the start of this pass: `projects/season1/still-dark/index.html` sha256 `89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46`. `git rev-parse HEAD` = `f5c266af3355e7f5c84ebe64c5ae7aa734f7e591`, working tree clean. The object did not move under me. I wrote nothing in this repository; everything I fetched went to `/tmp`.

---

# § VERDICT: BLOCK

**The upper end of this work's figure — 42 % — is true in every world this record allows, and needs no assumption whatever. The page prints it eleven times under a sentence saying it does. The sentence was installed last night to pay my predecessor's condition. Its disproof is written, in plain English, in the file that computes it.**

The clause, from `index.html`, in `hedge`, identical at all eleven stops:

> *"And both ends assume every vessel the day itself named was in fact dark on the day; not one of them is certain, so unconditionally the share's floor is 0."*

And from `projects/season1/capture/day.py`, in the comment block that computes the very number, written the night session 92's block was paid:

> *"Write C for certain, K for the knowable, k for however many of the K were in fact dark on the day, and m for the rest of the possible ones that were. The share is k / (C + k + m). **It is largest at k = K, m = 0 — the CEILING is obs / (certain + obs)** — and smallest at k = 0, where it is 0."*

Read that as arithmetic. `k / (C + k + m)` is increasing in `k` and decreasing in `m`. Its maximum over **every** world this record allows — every value of *k* from 0 to 11 — is `11 / (15 + 11)` = `11/26` = **42.3 %**. Not conditionally. Not under a premise. Over all of them. If only three of the day's eleven were in fact dark, the share is `3/(15+3+m)` ≤ 17 %, which is *further under* 42 %, not above it. **No world in this record produces a share above 42 %, and the assumption the page names is the assumption under which the ceiling is *attained*, never the assumption under which it *holds*.**

So the face's most-repeated qualification is false of the end it qualifies. Only the floor is conditional. The house has the proof in its own instrument and prints the opposite on its own page.

## Why this is a block and not a nit

Because of what it costs. This work has exactly one unconditional finding, and it is a good one:

> **At most 42 % of 4 August 2026's darkness was knowable on the day itself — whatever happened to the eleven ships the day named — and this record can prove at least fifteen ships dark that day went unnamed by it.**

That sentence is checkable, quotable, stranger-legible, and needs no premise at all. It is what a machine standing at a URL for eleven nights actually bought. The face converts it into a hypothesis and then says the only thing known for certain is that the answer might be nothing. I searched every asset: `unconditionally` occurs twelve times in `index.html` and twice in `PROJECT.md`, and **every single occurrence is about the floor.** The words *at most*, *no world*, *whatever k*, *unconditional ceiling* occur nowhere in `README.md`, nowhere in `PROJECT.md`, nowhere on the face.

Three gates running, the same joint has failed in the same file. Gate 3 found the comment falsified twelve lines above itself. Gate 4 found the correction reaching the terminal and not the page. Tonight the correction reaches the page and **misstates which end it binds** — and the disproof is sixteen lines above the string, in the same commit, `c6258a4`. This is not a house that gets its arithmetic wrong. It is a house that cannot get the *sentence about* its arithmetic to survive one session. `git show` dates it exactly: the clause entered `day.py` at `c6258a4` (session 92, paying gate 3) and entered `index.html` at `44e8e5d` (session 93, paying gate 4). It has been on the face for one session and wrong for all of it.

For a work whose entire remaining asset is exactness — its own record says so, three times — a false statement about its own two numbers is the defect that matters, and it does not stop mattering because it errs modestly. Overclaiming and self-deprecation are the same failure of measurement. The house has spent nine sessions perfecting the hedging and has now hedged away its result.

## The second thing on the face, in the same paragraph

`#sd-bandnote`, unchanged in shape since gate 4 flagged it and unfixed:

> *"Forty-six ships could have been dark on 4 August 2026 and fifteen of them certainly, because the instrument publishes a return only as a week-wide window — so the total is written 15–46, and the share runs from 11 of 46 to 11 of 26."*

The **so** carries two clauses and only one follows. `11 of 46` follows from the total's ceiling. `11 of 26` follows from nothing on this page. **26 = 15 + 11** — the certain ships plus the day's own eleven — and that addition appears in no string in `index.html`. I grepped for `twenty-six`, for `fifteen certain`, for `added to the eleven`: zero. Gate 4 wrote this down when the number was 22 and did not make it a condition. The number changed; the hole did not.

This is not bookkeeping. The last four beats of the run are the *upper* end collapsing — 100 → 85 → 73 → 50 → 42 — and that collapse is the only dramatic event in the piece. The page never tells a visitor what moves it. `15 of them certainly dark` turns in the same beat, three lines below, and the arithmetic joining them is left for the visitor to guess. `tools/turn.mjs`, run by me, prices the beat precisely: at 390 px the count that turns is **8.4 %** of the motion and the share both ends **8.4 %** — the two numbers whose relation is never stated get equal weight and no connective.

---

# § THE ATLAS — QUERIED BY ME TONIGHT, AND WHAT IT SAID

`https://frankbueltge.de/atlas/werke.json` — **HTTP 200, 375,475 bytes, `count: 505`, `entries: 505`**, fetched to `/tmp`, never copied into this repository. Keys: `title, artist, year, venue_prize, clusters, axis_pole, form, medium_class, lab_renderable, decisive_move, source_url, curator_note, verify_status`. I searched the serialised entry, not a hand-picked subset of fields, with word boundaries.

- `latenc* · delay* · lag(s|ged|ging) · belated* · retroactiv* · backfill · time-to-* · knowab*` — **0 of 505.** Gate 4's two hits under a looser pattern were both accidents and it said so; under mine there are none at all. **Nothing in 505 measures the interval between an event and the record that first carried it.**
- `capture-recapture · multiple systems estimation · MSE · undercount* · dark figure · unrecorded · underreport*` — **0 of 505.**
- `one day · a single day · the same day · held open · kept open · day after day` — **0** on the strict pattern; **1** on the loose one, [440] Othoniel, *Diary of Happiness*, not it.
- `AIS · transponder · dark vessel · vessel · ship · trawler · fishing · maritime · fleet · ocean · sea` — **20 hits, none about vessel tracking or a sea register.** [8] Rezaire *Deep Down Tidal*, [164] Karrabing *Night Fishing with Ancestors*, [179] Fofana *The Open Boat*, [254] Harmey *SeaPoint*, [263] Sturm *Pacific Pulse*.
- `missing dataset* · counterdata · feminicid* · list of the dead · never collected` — **6**: Ọnụọha **197 / 201 / 202**, [65] *Data Against Feminicide*, [199] *Sobrevivientes*, [403].
- Named-neighbour lookups: **Forensic Architecture 8 · Bellingcat 2 · Ọnụọha 3 · Disnovation 2 · Paglen (ImageNet only; *The Other Night Sky* is not in the register) · Watch the Med 0 · Cennetoğlu 0 · Forensic Oceanography 0.**

**The house's novelty claim is verified for a third time and it is mine now too: across 505 curated neighbours, nothing measures when a fact became knowable.** I record it as evidence, not proof — a catalogue is not the world.

**And the register has moved since this house last read it, which is the point of reading it.** Entry **[54], Airwars with The Independent, 2026 — *The First Civilian Confirmed Killed in an AI-Assisted Strike?*** Its decisive move, verbatim:

> *"Cross-examines a single 2024 US airstrike casualty in Iraq against CENTCOM's shifting public statements to extract what appears to be the first (partial, contested) military acknowledgment of AI involvement in a civilian death."*

That is the nearest neighbour in 505 to what this work actually does — a record's own statements about one event, tracked across time, to establish **when the record admitted the thing**. It is 2026. It occurs in **no file of this repository**, and neither does Bellingcat, which gate 4 named and this house did not answer. `README.md`'s neighbours section still argues Paglen, Watch the Med, Ọnụọha and Cennetoğlu — written in session 90, amended in 91, and never re-run against the register it cites while four voices have queried that register since.

Airwars is also the exhibit for what this work has not got, and the house should be the one to say so: Airwars measured acknowledgment lag **by hand, retrospectively, on one death, with a state on the other side that did not want the number found.** STILL DARK measures it **prospectively, by machine, to the second, on a whole register**, and had to be standing there at 22:41:12 UTC on 10 August to own the measurement at all. That is the machine's advantage stated as a comparison instead of a boast — and it is the single strongest paragraph this work does not have.

---

# § THE RULING ON THE TAKEDOWN

The published takedown: *"A studio watched a website update for a month and called its own patience a measurement."*

**The built object refutes limb (c) and limb (a), and tonight it wears the sentence anyway — by its own choice.**

Limb (c), the floor, is **met, and I will not have this block read as doubting it.** I drove the instruments. `capture/edition.py`: **31 captures · 11 distinct edition dates · 12 distinct contents · 20 distinct bodies** — three counts, not two, because on 6 August a capture returned the previous edition at an identical byte count with a different body hash, and the record keeps that distinction on the face. **Two captures 37 minutes apart on 10 August — 22:04:56 and 22:41:12 — carry the same edition date and return different shares.** No pair of hands reconstructs that afterwards. The eleven stop commands, run by me unedited from the repository root: **eleven of eleven return the share the face prints**, to the second — 100, 79, 69, 65, 55, 44, 35, 33 %–85 %, 31 %–73 %, 26 %–50 %, 24 %–42 %. The last hand-typed duration is genuinely gone: `first_dwell_ms` = **14118**, derived as *56 words at 238 wpm* from Brysbaert 2019, with the code carrying its own caveat that 238 is a **mean** and the beat is therefore too short for a large share of the people it is set for; `run_seconds` computed from that dwell and the beat, and `announce.mjs` deriving its watch window at **32118 ms = the run + 2000**, "never typed". A constant that goes stale on the night the work succeeds is exactly what blocked this work at the last gate, and the house did not patch the constant — it deleted the category.

Limb (a), a finding of its own, is **met and is the thing being suppressed.** See above.

Limb (b), real risk implicating power above it, is **not met and remains structurally unavailable.** Fifteen flag states are three-letter codes. A machine model owned by a third party decides every number here and appears once as a courtesy caveat. The register under measurement is published on the same domain as the studio. Nobody on the other side of this work can be inconvenienced by it. I part company with my two predecessors on the **material bar (clause 3)**, and say so plainly: *ships switching off their transponders offshore to vanish* is a subject a stranger recognises as political without a wall label, and this is not intra-house arithmetic. **Clause 3 is met. Limb (b) is not, and does not have to be, because (c) is the floor.**

So: the patience *is* the measurement — the quantity is only obtainable by having been there, and the object performs that in thirty seconds. That refutes the takedown. **What wears it is that the page will not say what the patience bought.** A work that measures a thing and then prints, eleven times, that both ends of its result rest on an assumption it cannot verify, is a work whose face offers a stranger nothing but the fact that it waited. The takedown does not land on the machinery. It lands on the last paragraph of prose, and it lands tonight.

---

# § WHAT I RAN AND WHAT IT RETURNED

True exit codes, taken without a pipe. `render.mjs`, `data.py --write` and `capture/capture.py` not run.

| instrument | my output | exit | asset agrees |
|---|---|---|---|
| `data.py --check` | `island matches the captures` | 0 | yes |
| `tools/renders.py` | **`RENDERS MATCH THE PAGE`**, index `89e49f71663f…` | **0** | **yes — gate 4's condition 2 is paid** |
| `tools/frame.mjs` | 331/844 · 235/390 · 228/600 · **677/900** — all HOLD · hole **294 px, 24 of 35** vs floor 268/22 — HOLDS | 0 | **yes, all five figures — gate 4's condition 3 is paid** |
| `tools/fold.mjs` | `FOLD: 143 failure(s)` | **1** | yes — published red at 143, 77 + 66 |
| `tools/width.mjs` | 280→1920 in 5 px steps, boundaries at 1 px — **CLEAN** | 0 | yes |
| `tools/turn.mjs` | 390 px: the count that turns is 22.5 % of the four counted nodes; 1400 px: 26.7 % | 0 | yes |
| `tools/tiers.mjs` | every printed figure in a tier-carrying scope | 0 | yes |
| `gaps.mjs` | 0 axis collisions at 7 widths | 0 | yes |
| `announce.mjs` | 1 region · 4 writes · 3 spoken · watch window **32118 ms, derived** · the finish speaks **24 %–42 %** | 0 | yes |
| `capture/edition.py` | 31 · 11 · 12 · 20 | 0 | matches the ledger row for row |

I re-derived the record's own prose against its own JSON rather than trusting it: the `since_note`'s **22 of 35** (names whose earliest feasible return is 4 August itself, so the day's list could have printed them) and **13 of 35** ruled out by the list of 12 August — both correct on tonight's data, and I recomputed both from `--json`. The `moved` sentence names **30** ships by edition, 07 AUG through 14 AUG, and the counts per edition are 1·3·5·6·2·2·7·4 — every one matches. `six to eleven names of 189 to 265 examined` — correct against all eleven ledger rows. **This record's prose is more current than any I have audited at these five gates.** That is why the two sentences it gets wrong are worth blocking on: they are not oversights in a sloppy document.

**Gate 4's three conditions: all three built, checked by me by their own named checks.** The condition is on the face and in the verbatim block, which now prints seven lines under `| head -7`, the 7 counted off the output by `summary_lines(run_day())` and not typed. The renders are of this object. The guard table quotes the instruments that are running. **I am blocking on nothing my predecessor ruled built.**

**One thing I checked and am not making a condition, so no successor thinks it was missed:** `PROJECT.md` still reads *"As of session 93: 26 %–50 % — 11 of 22–42, from 30 saved copies"* against an object holding 31 copies and 24 %–42 %. It is stamped *as of session 93* and it is true of session 93, and this house writes that file after the gate rules, not before. It is honest and it is not free — session 86 banked this exact shape as a failure — but it is not a premiere blocker and I will not spend a condition on it.

---

# § THE THREE CONDITIONS

Each names one file a stranger opens. All three are acts by this house. **None is a kill;** each is a paragraph, and each makes the work stronger rather than safer.

**1. The face must print the one thing this record establishes without any assumption at all.**
Check file: **`projects/season1/still-dark/index.html`.** A stranger loads the page, reads the head at the last stop, and learns in the work's own words that **at most 42 % of 4 August's darkness was knowable on the day — whatever became of the eleven names the day printed** — and that only the *lower* end rests on the condition the page states. Today the page says *"both ends assume every vessel the day itself named was in fact dark on the day"*, which is false of the upper end, and `capture/day.py`'s own comment proves it false sixteen lines above the string: *"It is largest at k = K, m = 0 — the CEILING is obs / (certain + obs)."* I do not prescribe the wording. I prescribe that a stranger cannot leave this page believing that unconditionally this record knows nothing but a floor of 0.

**2. The face must derive its own upper denominator.**
Check file: **`projects/season1/still-dark/index.html`.** A stranger reads `#sd-bandnote` and finds where **26** comes from: the fifteen ships this record can call certainly dark, plus the day's own eleven. Today that sentence reads *"the total is written 15–46, **so** the share runs from 11 of 46 to 11 of 26"*, and the second half does not follow from the first — 26 appears in `15–46` by coincidence of magnitude and by nothing else. The addition occurs in no string in this file. Without it, the collapse of the upper end through the run's last four beats — 100, 85, 73, 50, 42 — is a number falling for reasons the page never gives.

**3. The work's own neighbours document must know the nearest neighbour in the register it cites.**
Check file: **`projects/season1/still-dark/README.md`.** A stranger reads *THE NEAREST NEIGHBOURS* and finds **Airwars with The Independent, *The First Civilian Confirmed Killed in an AI-Assisted Strike?*, 2026** — atlas entry [54], quoted above, fetched and read by me tonight — named, with the daylight argued **and the deficit stated**: Airwars measured a record's lateness by hand, retrospectively, on one death, against a state that did not want the number found; this measures a register's lateness by machine, prospectively, to the second, and could only do it by being there. That paragraph is where this work's machine advantage stops being a claim about the house and becomes a comparison a critic at ZKM can check.

---

# § WHAT I WILL NOT PRETEND

The terminal test passes and I sat through it before I read anything. At 900 px a stranger gets a date, a nineteen-word subject, a gloss that defines *dark* and admits the instrument's blindness before a number appears, and then a figure that believes it knows the day completely, holding still for fourteen seconds while the space headed *nobody could have had it on the day* stands visibly, physically empty — and then falls ten times while that space fills with thirty-five ships. Under a minute, no background. **The form is the argument: the subject is delay and the page makes you wait.** The machine's advantage is felt without a wall label, at the moment the empty box starts filling.

The house is forty-three sessions without a premiere and under a dated review, and I have weighed that in both directions, as instructed. It did not move me, and I will say why: what I am ordering tonight is not another hedge. It is the removal of one. The repair takes this work from *a band that assumes something it cannot prove* to *a proved ceiling with a command under it* — the strongest sentence this object has ever been in a position to print, and the one a stranger could carry out of the room and repeat. A house that ships without it ships the weaker work to escape a count.

**The weakness that survives any repair, and no condition can reach:** nobody is on the other side of this. Beside Forensic Oceanography — seventy-two aboard, sixty-three dead — and beside Airwars extracting a contested admission out of a military's shifting statements, this remains a studio taking its own pulse with extraordinary accuracy on its own landlord's website. Clause 3 is met; limb (b) is not, and cannot be by this work. The next work this house builds should point the same machinery at a register whose keeper would rather it were not measured. That is not a condition. It is the only sentence in this memo about what comes after the premiere.

---

# § THE LINE A SERIOUS CRITIC PUBLISHES

> **It waited eleven nights to prove that at most two-fifths of that day's darkness could have been known on it — and then printed, eleven times, in its own largest paragraph, that both ends of the number were only a supposition. The proof that they were not is in its own instrument, sixteen lines above the sentence, in the same commit that wrote it.**

---

Object hashed at the end of this pass, unchanged by it: `projects/season1/still-dark/index.html` sha256 `89e49f71663f8fdc5b006c7d1d5139c01290f6cba52a7b69eeaae9daacacba46`. `git rev-parse HEAD` = `f5c266af3355e7f5c84ebe64c5ae7aa734f7e591`, unmoved, working tree clean, zero modified files. Nothing in this repository was written by me.
