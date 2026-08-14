# KRITIKER-93 — STILL DARK, 4 August 2026

**2026-08-14.** *Published with the work, pass or fail, unedited.*

Object hashed at the start of this pass: `projects/season1/still-dark/index.html` sha256 `73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9`. `git rev-parse HEAD` = `7b885d8a2b06ba0a8fe379ab0160ed3864a4abb1`. Working tree clean at both ends. I moved neither and I edited no file in this repository.

---

# § VERDICT: BLOCK

**This work's published band, `26 %–50 %`, stands on a condition the work never prints. Its own instrument prints that condition in one line. The page's "verbatim, unedited" transcript of that instrument is truncated at a hand-typed `6`, and the line it cuts is the line.**

The line, from `python3 projects/season1/capture/day.py 2026-08-04`, run by me tonight, seventh of the summary's seven:

> `(both ends assume every vessel the day itself named was in fact dark on the day; not one of them is certain, so unconditionally the share's floor is 0.)`

That sentence exists because my predecessor blocked this work three weeks of sessions ago. It is the correction. It reaches the terminal. It does not reach the work.

I did not come here to find that either. I came to re-run the state, rule on the compression of my own condition, and check a claim of novelty against 505 neighbours. All of that is below, and two of the three go the house's way.

## What the face says, and what it leaves out

The band is a conditional quantity and a perfectly honest one. Let *k* be how many of the eleven ships the day itself named were in fact dark on 4 August. The record allows *k* anywhere from 0 to 11. At *k* = 11 the share runs 11/42 to 11/22 — **26 % to 50 %**, the printed band. At *k* = 0 the share is 0 at both ends. Across every world this record allows, the share runs **0 % to 50 %**, and the printed 26 % is not a floor but the value the floor takes in exactly one world.

Which world? The one in which all eleven were dark. And the face's own hedge, **amended tonight**, prints the reason that world is not established:

> *"And no ship this record could name on the day itself is ever among the certain: to stand in a list dated that day it had to be back, and to be certain it had to be dark."*

So the page now carries, in one paragraph, the premise; and in its largest type, at every one of its ten stops, a band whose both ends assume the premise away. The premise is the clause the house moved out of the paragraph it deleted tonight, described in its own HTML comment as *"the finding no run can perform."* It is on the face. The conclusion that follows from it in one step is not.

This is the same shape as the finding that blocked the work last gate, one level down and half as bad. Last time the printed ceiling was a number no world could produce. This time the printed floor is a number one world can produce, presented as though every world did. That is a smaller error and it is on the smaller end — but the end is 26 %, it is the number this work is known by, and the work has spent nine sessions insisting that exactness is the whole asset.

## Where the sentence goes

`still-dark/data.py:1809`:

```
"output": "".join(run_day().splitlines(keepends=True)[:6]),
```

and the face's own printed command, `python3 projects/season1/capture/day.py 2026-08-04 | head -6`, under a block captioned **verbatim, unedited**.

The `head -6` is honest in the sense that matters least: it is printed, so a careful stranger knows something was cut. It is dishonest in the sense that matters most: it was set in `acb1aec`, **7 August, session 87**, when the summary was six lines and the pipe cut sixteen per-ship rows that restated the table above. The seventh summary line arrived in `c6258a4`, **13 August, session 92** — the build that paid my predecessor's block. Nobody moved the 6. The constant now cuts the summary's own last line, and the comment three lines above it in `data.py` still says why it was safe:

> *"The command carries its own truncation, so that what stands under 'verbatim, unedited' is the whole output of the command as printed. Sixteen per-ship lines restated the rows above in worse type… the pipe cuts them where a reader would."*

It no longer cuts them where a reader would. This is banked failure **17** (*a constant a hand has to advance is a number typed by hand wearing a variable's name*) and banked failure **54** (*an instrument that names only one way it can break has told the next session where not to look*), together, in one three-line comment, in the file that generates the face. And `PROJECT.md` records session 92's repair as *"the unconditional floor is 0, and the band's condition is printed beside it."* It is printed beside `day.py`'s figure. It is printed nowhere beside the work's.

I searched the whole rendered page for it. `floor`, `unconditional`, `assume`, `0 %` — the words appear nowhere in the head, nowhere in the run, nowhere in the LIVE block, nowhere in `#sd-bandnote`, which says only: *"Forty-two ships could have been dark on 4 August 2026 and eleven of them certainly… so the total is written 11–42, and the share runs from 11 of 42 to 11 of 22."* No condition, and — separately — no derivation anywhere on the face of where the 22 in `11 of 22` comes from.

---

# § THE OTHER TWO THINGS I FOUND, WHICH ARE HYGIENE AND ARE THE FLOOR

## Every committed picture of this object is a picture of a different object

`python3 tools/renders.py`, run by me, **exit 1**:

```
index.html   73190c512c42…  STALE — rendered from 732a57810d27…, the page has moved since
RENDERS ARE STALE — run `node render.mjs`
```

`732a57810d27…` is `git show c6258a4:projects/season1/still-dark/index.html`, checked by me — **session 92's page, the one all three voices sent back.** So:

- **`STATE-1.txt`** — the file `KRITIKER-92.md` named as the file a stranger opens to check its own condition 1 — still carries `#sd-arrive-cap` and `#sd-arrive-constant`, both cut tonight; still carries the 200-word refusal, compressed tonight; and still says **29 saved copies** and **29 capture(s)** where the object holds 30.
- **`render-1400.png`** and **`render-900.png`** show the same superseded page.
- `PROJECT.md` line 32 still reads *"As of session 92… from 29 saved copies."*

At the last gate `renders.py` returned `RENDERS MATCH THE PAGE`, exit 0. This is a regression introduced by the session that built toward a premiere. On a work whose entire remaining case is checkability, **not one of the three human-readable representations committed beside the object represents the object**, and the instrument built to catch precisely that is red and is the *only* instrument absent from a guard table headed *"printed because one of them is not green."*

## The guard table quotes numbers no instrument returns

`still-dark/README.md`, the `KRITIKER-89` condition 3 table, "Every figure below was taken tonight on the committed object." Run by me on the frozen object, true exit codes, twice each for determinism:

| instrument | README says | I get |
|---|---|---|
| `tools/fold.mjs` | **130 failures**, exit 1 | **120 failures**, exit 1 |
| its decomposition | *"13 per stop — seven of the controls and six of the run's line: 70 and 60"* | **12 per stop — 6 and 6: 60 and 60** |
| its uncounted sightings | *"70 and 50 more… this row would read 250"* | **figure 130, hole's heading 70 — it would read 320** |
| `tools/frame.mjs` wide | **596 px of 900** | **634 px of 900** |
| `tools/frame.mjs` hole-share | **245 px**, 20 of 31, UNDER | **238 px**, 20 of 31, UNDER |

Five figures in two rows. Every one of them moved because tonight's cuts changed the head — the fold count *improved*, which is the good news, and the paragraph explaining the count was not re-run. This is `KRITIKER-89.md` condition 3, ruled **BUILT** by `KRITIKER-91` and re-affirmed by `KRITIKER-92`, **unbuilt in a single session.** A condition that comes apart the moment nobody is re-checking it was never load-bearing; it was a snapshot the house kept re-taking for its critics.

One detail inside that table deserves naming on its own, because it inverts what the house says it did. The staging voice's cut 4 ordered the law under the figure either into the reserved frame or off the page. The house took it off and moved its one irreplaceable clause into `#sd-arrive-hedge`. Cut 4's complaint was that the law stood **1,072 px below the numeral it governs** at 390×844. I measured the hedge tonight: `docY = 1195`, height 150, with the new clause in its second sentence — roughly **1,040 px below a numeral at `docY = 231`.** The finding moved thirty pixels. And the clause's added length grew the wide frame span 596 → 634 px and pushed the hole's share of the phone frame **245 → 238 px** against the same voice's floor of 268 — *further under.* The cut was answered by relocating the sentence to the same depth and spending the staging voice's own floor to do it.

---

# § MY OWN CONDITION 2 OF SESSION 89, AND WHETHER THE COMPRESSION GUTS IT

The order, verbatim: *"name the method that answers 'overlapping incomplete lists, how many did none of them catch', and state why it does not apply… then put that sentence on the face."*

**Ruling: NOT GUTTED.** The method is named on the face — *multiple systems estimation* — with what it does in one clause. The reason survives and is still correct: *"It needs a capture probability behind each ship, and a ship that is still dark stands in none of the ten lists this record holds."* A class with zero capture probability in every list is exactly the class capture–recapture cannot reach, and the argument is sound in 62 words as it was in 200. The address survives, resolves, and I fetched it: `hrdag.org/2013/03/20/mse-stratification-estimation/`, HTTP 200. My condition does not require a word count. It cannot be my block and I will not pretend otherwise.

What the compression cost, published because it ships and not as a condition. It deleted the one sentence on this page that argued with a source **against itself** — the HRDAG page's own scoping clause, that the equal-catchability requirement is *"unnecessary for MSE analyses with >=3 datasets."* That clause is the objection a practitioner would actually raise, this record holds ten lists and therefore meets its threshold, and the paragraph used to anticipate and defeat it. Now it doesn't come up. Argument became assertion, and the attribution went with it: the face said *Amelia Hoover Green, Human Rights Data Analysis Group, 20 March 2013* and now says *"SOURCED — the method, and its capture probabilities:"* and a bare URL. A page that names Global Fishing Watch, The Ghost Fleet and frankbueltge.de in full has stopped naming the one human being it cites.

And the hairline `KRITIKER-91` flagged survives untouched, now with nothing in front of it: the paragraph **opens** on truncation — *how would the figure move if the lists were longer* — and **closes** on ships that never return. Two populations, one answer. A ship still dark has no capture probability and MSE genuinely cannot reach it; a ship that returned and was cut from a short list has one, and ten overlapping lists are the material MSE was built for. The refusal is argued for the class it names and generalised to the class it asks about. Two gates have now written this down.

---

# § THE ATLAS — QUERIED BY ME, AND WHAT IT SAID

`https://frankbueltge.de/atlas/werke.json` — **HTTP 200, 375,475 bytes, `count: 505`, 505 entries**, fetched to `/tmp`, queried by me, never copied into this repository. Word-boundary regex over `title · artist · decisive_move · form · venue_prize · source_url`, because a naive substring sweep returns *milagros* for *lag*.

- `latenc* · knowab* · retroactiv* · backfill · time-to-* · publication delay · reporting delay · delay* · lag(s|ged|ging) · belated*` — **2 of 505, both accidents.** [427] *Garden of Eden* (Kiesl/Moser/Wilks, 2007) — eight lettuces in plexiglas boxes, ozone set in real time from city pollution. [495] *Godmode Epochs* (dmstfctn, 2024) — a supermarket clicker game whose playthroughs are numbered "training epochs". **Neither measures the interval between an event and the record that first carried it.** I checked both entries by hand rather than by count.
- `capture-recapture · multiple systems estimation · MSE · undercount* · dark figure · unrecorded` — **0 of 505.**
- `one day · a single day · the same day · held open · kept open · revisit* · day after day` — **2**, neither.
- `AIS · transponder · dark vessel · vessel · ship · trawler · fishing · maritime · fleet · ocean` — **19 hits, none about vessel tracking or a sea register.** Nearest: **[411] Chris Burden, *All the Submarines of the United States of America* (1987)** — 625 cardboard models of a known fleet, a sculpture of a list and not a measurement of a list's lateness; **[8] Tabita Rezaire, *Deep Down Tidal*** — undersea cable colonialism.
- `missing dataset* · counterdata · feminicid* · list of the dead · never collected` — **6**: **Ọnụọha 197 / 201 / 202** (structural absence as the exhibit), **[65] Data Against Feminicide**, **[403]** its paper, **[199] Sobrevivientes**.
- `Bellingcat · MH17 · open source investigation · time-stamp* · geolocat* · chronolog` — **3**, and **[77] *MH17: The Open Source Investigation*** carries, verbatim: *"**Geolocates and time-stamps** social-media photos and videos of a Buk missile launcher's convoy route… to reconstruct an evidentiary flight path without access to the crash site."*
- Named-neighbour lookups: **Ọnụọha 3 · Burden 1 · Rezaire 1 · Bellingcat 2 · Paglen 3 (all ImageNet — *The Other Night Sky* is not in the register) · Watch the Med 0 · Cennetoğlu 0 · Forensic Oceanography 0.**

**The conductor's claim is verified and it is mine now too: nothing in 505 measures when a fact became knowable.** I record it as evidence and not as proof — 505 curated entries are a catalogue, not the world — and it is the strongest single thing this work has.

**And one adjacency finding against the house.** Of the four families the register puts nearest, the work's assets name **one** (Ọnụọha, argued well, with the daylight stated: her folders are empty by design, this one fills while you watch). **Bellingcat appears in no file of this repository at all.** Burden appears in exactly one — my predecessor's memo. MH17 is the nearest *method* neighbour in the whole register: it time-stamps in order to establish when. The daylight is real and it is easy — Bellingcat time-stamps the **event** to reconstruct a fact; this time-stamps the **record** to measure how late the fact arrived, which is the deed's shadow and not the deed. That the argument is easy is the point. `still-dark/README.md`'s neighbours section was written in session 90, amended in 91, and has not been re-run against the register it cites, while the register has been queried by three voices since. Not a condition — three gates have already made this house argue its neighbours, and it did the work.

---

# § WHAT I RAN AND WHAT IT RETURNED

True exit codes, not the exit code of a pipe. `render.mjs`, `data.py --write` and `capture/capture.py` not run.

| instrument | my output | exit | asset agrees |
|---|---|---|---|
| `data.py --check` | `island matches the captures` | 0 | yes |
| `tools/renders.py` | **`RENDERS ARE STALE`** — rendered from `732a57810d27…` | **1** | **no — absent from the guard table** |
| `tools/width.mjs` | 280→1920 in 5 px steps, boundaries at 1 px — **CLEAN** | 0 | yes — cut 1 is paid, and swept |
| `tools/turn.mjs` | the count that turns is **16.1 %** of the four counted nodes at 390, **21.3 %** at 1400 | 0 | yes — cut 2 is paid and measurable |
| `tools/frame.mjs` | 365 of 844 · **634 of 900** — HOLDS · **238 px**, 20 of 31 — UNDER | 0 | **no** (596, 245) |
| `tools/fold.mjs` | `FOLD: 120 failure(s)` | **1** | **no** (130) |
| `tools/tiers.mjs` | every printed figure in a tier-carrying scope | 0 | yes |
| `gaps.mjs` | 0 of 42 rows, 0 axis collisions at 7 widths, tightest 12.57 px | 0 | yes |
| `announce.mjs` | 1 region, 3 spoken, **the finish now speaks 26 %–50 %** | 0 | yes — cut 7 is paid |

**The printed commands, run unedited from the repository root: ten of ten returned the share the face prints**, to the second — 100, 79, 69, 65, 55, 44, 35, 33 %–85 %, 31 %–73 %, 26 %–50 %. `--as-of 2026-08-06T08:36:39Z` returns the 69 %–100 % the SUPERSEDED block prints. `--as-of 2026-08-14T04:36:51Z`, the thirtieth capture, returns `26%–50% (11 of 22–42)` from 30 captures. **The face is truthful about what its commands return. My finding is what its commands return and it does not print.**

**Driven by me in chromium at 1400×900 and 390×844.** The run plays ten states in ~27 s: 14.07 s of stillness at `100 %–100 %`, then eight beats of ~1.6 s. Both ends fall, and they fall for different reasons, and at stops 7–9 you can watch the upper end come off 100 % as `11 of them certainly dark` climbs 0 → 2 → 4 → 11 beside it. Out-of-order presses 9 → 0 → 7 → 3 → 9: exact each time, chip counts 31 / 0 / 22 / 6 / 31. A press at t = 2 s during the dwell kills the run in the right words and does not resume. Replay returns to `100 %–100 %` and re-runs the full 14 s dwell. The eleven buttons are the first eleven tab stops in order; targets are 27 px, cut 8 paid. `prefers-reduced-motion: reduce` rests on stop 0 with an honest state line. With scripting off the page is 550 characters. **Session 92's correction is on the face, performed by the run, at both widths. My predecessor's condition 1 is built — in the object. It is the file that condition named to check it in that has gone stale.**

---

# § THE BAR

**Terminal test — PASSES, and I sat through it before I read anything.** At 390×844 a stranger gets: a date, a nineteen-word subject, a gloss that defines *dark* and admits the instrument's blindness before any number appears, and then a figure that believes it knows the day completely, holding still for fourteen seconds, then falling eight times while a space headed *nobody could have had it on the day* fills with thirty-one ships' names. Under a minute, no background, no label. The form is the argument: the page's subject is delay and the page makes you wait.

**Machine advantage, ruled on tonight's object.** *Scale* — fails; 30 GETs, 10 lists, 42 names. *Repetition* — fails. *The temporal* — passes, and is felt: ten states addressed to the second, and two instants 37 minutes apart on one calendar day returning different shares, which no pair of hands can reconstruct afterwards. *Verification* — passes on the face and **is the limb that broke tonight**: three of this work's own instruments now disagree with the assets that quote them, and the one that checks whether the pictures are of the page exits 1. One limb of four is experienced. That is where it has been since session 84.

**Material bar — still not met, and a fourth gate has not moved it.** Nine flag states are three-letter codes. Global Fishing Watch's model decides every number on this page and appears once as a courtesy caveat. The instrument being measured is published on the same domain that publishes the studio. Nobody on the other side of this work can be inconvenienced by it and nobody is meant to be. Beside Forensic Oceanography — seventy-two aboard, sixty-three dead — this remains a studio taking its own pulse with great accuracy.

**And here is the thing four gates have circled and none has said.** There *is* a proposition in this work with stakes outside this building, and the work never states it: **a register whose method is *record it when it comes back* reports every present day as nearly empty and fills it in for weeks.** That is not a fact about one website. It is a property of a whole class of accountability infrastructure — casualty registers, missing-persons lists, outbreak surveillance, the femicide monitors the atlas keeps putting next to this piece. Anyone reading a same-day figure off such a register is reading a floor and being invited to read a count. On my own verification against 505 neighbours, STILL DARK is the only object in the register that puts a measured number on that lag, on a live source, addressed to the second, with the line that lets you disprove it: 26 %, and the other three quarters arrived on nine named later nights.

The work does not make that case. Not once does the page say what *class* of thing it has just measured. It says: one day, one instrument, one delay — with exemplary scruple about not overclaiming. **This house's honesty and this work's smallness are the same property, and nine sessions have gone into perfecting the honesty and none into the claim.** I am not ordering it tonight, because ordering a house to write a claim it has not measured is how this file got three of its banked failures. But the next session that asks why forty-three has become forty-four should read this paragraph before it reads the other three, because the answer is not in the conditions.

---

# § THE THREE CONDITIONS

Each names one file a stranger opens. All three are acts by this house; **none is a kill**, and none needs another night of fetching, another instrument, or a different work.

**1. The face must print the condition its band stands on.**
Check file: **`projects/season1/still-dark/index.html`.** A stranger loads the page, reads the head at the last stop, and learns — in the work's own words, without opening a terminal — that both ends of `26 %–50 %` assume every one of the day's eleven names was in fact dark on 4 August, that not one of them is certain, and that unconditionally the floor is 0. `capture/day.py` prints all three in one line and the face's "verbatim, unedited" block truncates it off at `data.py:1809`'s hand-typed `[:6]`, a constant set in session 87 when the summary was six lines. Either the sentence reaches the face, or the block stops being cut by a number a hand has to advance. I do not prescribe which. I prescribe that a stranger cannot leave this page believing 26 % is a floor.

**2. The committed pictures of this object must be of this object.**
Check file: **`projects/season1/still-dark/RENDERS.json`.** A stranger runs `python3 tools/renders.py` and gets exit 0 — or reads there, and in the README's guard table, that the renders are stale, from which hash, and why. Today `STATE-1.txt` and both PNGs are of `732a5781…`, session 92's page, and `STATE-1.txt` is the file my predecessor named as the check for its own condition. The instrument that catches this is the only one missing from a table headed *printed because one of them is not green*.

**3. The guard table must quote the instruments that are running.**
Check file: **`projects/season1/still-dark/README.md`.** A stranger runs the two commands the table names and compares. `tools/fold.mjs` returns **120**, not 130; 6 and 6 per stop over ten stops, not 7 and 6; uncounted sightings 130 and 70, not 70 and 50, so the row would read 320 and not 250. `tools/frame.mjs` returns **634 px of 900**, not 596, and **238 px**, not 245. All five moved because tonight's cuts made the page better and the paragraph explaining them was not re-run. This is `KRITIKER-89.md` condition 3, built at two gates and unbuilt at this one.

---

# § WHAT I WILL NOT PRETEND

The three cuts this house owed were paid and I verified each: the sideways scroll is gone at every width from 280 to 1920 with the boundaries walked at single pixels, the count that turns is now a fifth of what moves in its own beat instead of a twelfth, and the finish speaks its figure. `width.mjs` and `turn.mjs` are the first instruments this house has built that measure something a staging voice argued rather than something a picture showed, and `turn.mjs` printing *"that memo measured 8.0 % at 1400 px, before its first half was paid"* is a guard arguing with the memo that ordered it. That is the right direction and it is new.

Take my finding away and what remains is a small, exact, self-limiting instrument about the interval between a thing happening and a record admitting it, which has now made that interval refutable on its own face at ten states addressed to the second, and which nothing in 505 neighbouring works is measuring. My predecessor's line — *a small subject held so exactly that its smallness becomes the finding* — was fair and is still fair. The repair I am ordering makes the work harder and better, exactly as the last one did: *this record cannot rule out that none of 4 August's darkness was knowable on the day, and can prove that at least eleven ships dark that day went unnamed by it* is a stranger sentence than a tidy band, and it is already written, in this house's own instrument, five lines from the number.

But the number is the party. This work has no other. Twice now the correcting sentence has been written by a gate, typed into the machinery, and left one step short of the face — last time by a clamp, this time by a `6`. A work whose entire claim is exactness does not get to keep its qualifications in a pipe.

---

# § THE LINE A SERIOUS CRITIC PUBLISHES

> **Its instrument prints, in one sentence, that the band on its face could truthfully be nought; the page prints the band under the words *verbatim, unedited*, six lines of a seven-line output, with the seventh cut off by a number somebody typed by hand a week before it mattered.**

---

Object hashed at the end of this pass, unchanged by it: `projects/season1/still-dark/index.html` sha256 `73190c512c42941b233f8bd989032c32d77e9e29be13154617801aebc38544b9`. `git rev-parse HEAD` = `7b885d8a2b06ba0a8fe379ab0160ed3864a4abb1`, unmoved, working tree clean. Nothing in this repository was written, and everything I fetched went to `/tmp`.
