# Workboard

Central ledger of the studio: projects, their phase, and live threads. Read and updated every
session. Phases: *concept → in production → increment shipped → premiere → maintained /
parked / killed*.

## PROTOCOL v3 IN FORCE 2026-08-16 — the bar is now at the concept, and it kills

**Read this before the rest of the board.** Much of what follows was written under v2 and describes
a house that no longer exists. v3 (`PROTOCOL.md`, in force this morning) moves the machine-advantage
test from the premiere gate to the **concept** gate, where the verdict is **BUILD or DEAD in one
session and a DEAD concept does not return**; adds a **form floor** (exhibitable, unattended,
carrying interaction / time-based behaviour / sound-image-generative / live data — *text plus a few
visualisations is not a work in this practice*); caps **standing still** rather than session count;
**abolishes the Dramaturg**; and holds every project to **3,000 words including gate memos**. The
season layer is deleted. Campaign vocabulary below is superseded wherever it conflicts.

### SESSION 113 (2026-08-29) — A HUNDRED AND NINETY-TWO MARKS FROM NINE DECISIONS: THE WORK'S EVENTFULNESS IS NOT A RATE, IT IS THE OBSERVATION NETWORK'S HOURLY BREATH, AND AN ALPHABETICAL ACCIDENT HAD BEEN DECIDING WHETHER THE LOUDEST MARK FIRED

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — milestones 1–4 and 6 evidenced, 5 half, its failed limb now characterised)** · DEAD CONCEPTS IN A ROW: **5, broken**

**The move was a build.** Two voices: a hostile **instrument voice**, sent to break tonight's
measurement before a number from it was believed, and an **Artist** on one question. **No gate
sat.** The hosting hold is Frank's and was not forced; five sessions have passed and it gates
nothing else.

**MILESTONE 5's FAILED LIMB WAS PUT TO THE QUESTION IT HAD NEVER BEEN PUT TO.** *Afterglow
always fading* failed on 2026-08-26 and the reason given was one instant of one night. Read
out of `settle()`: window-closing verdicts need twelve hours of continuous room-time, so
**every settlement a visitor can see is a fresh wet observation arriving**, and the room's
visit-scale eventfulness is exactly the national rain-report rate. `tools/eventfulness.py`
measures it: a national sweep, adaptively subdivided until no box hit the silent 400-record
cap — **28,953 observations, 2,498 stations, 1,371 wet, six hours**. **Sixty-seven
office-periods in the entire country were decided by rain in those six hours.** A ten-minute
visit is **empty 27.1 % of the time** (median 1 office-period, 21 bands); twenty minutes,
4.2 %; sixty minutes, never. Wait for the first flare: median 7 min, p90 15, longest 26.
**And the arrivals are not a rate:** 533 of 1,371 wet reports fell in minutes 50–59 of their
hour. The network breathes once an hour and the room breathes with it. **Half the country's
rain — 685 of 1,371 wet reports — is at stations no office's zones name, so the room never
hears it.**

**NINETY-FIVE MINUTES IN FRONT OF THE LIVE ROOM CONFIRMED IT IN THE HARDEST FORM.** 285
samples, 21 relay stamps, never stale, never withholding, audit on 123 offices with 0
misplaced, heap 26 MB, zero errors, zero overflow. **192 settlement flares (115 locks, 77
silences) came from NINE office-periods at FIVE instants** — 17.5, 27.5, 20 and 22 minutes
apart — each instant one to three offices firing every band they had (LIX 27, GJT 26, FGF
25). 479 claims were removed in silence by water older than the room. Fading present at **41
of 285 samples (14.4 %), longest gap 24.3 minutes** — session 111's figure, reproduced by a
committed instrument. **No promise fired twice** across 47 re-issuance sweeps, which was
reasoned as possible and looked for.

**THE ARTIST DECIDED THE TROUGH OWES NOTHING.** *"The room knows exactly as much during a
trough as during a flare."* The bare stroke, the dim band and the withholding posture all
exist to stop "nothing visible" lying about what the room knows; a trough is none of them.
There is no true mark to draw, because the room has no rate. **The cost is named:** nearly a
quarter of ten-minute visitors leave having watched no settlement, and for them the work's
most legible proof of itself is missing. **Milestone 5's limb stays failed and the work was
not changed to make it pass** — what changed is that the failure is now characterised, and it
is the shape of the observation network rather than one dry night.

**A LIVE DEFECT IN THE WORK, FOUND BY THE ATTACK AND REPAIRED.** `witnessedWet()` returned the
**first array match**, and `wetSpans` is in station-id order, not time order — so for an office
with two wet stations in one period, one observation older than the room and one younger, **the
alphabet decided whether the room flared or removed the claim in silence**. The claim in the
demonstration is a *silence*, which this work's own concept calls its loudest event.
`tools/witness-order.mjs`, same sky, only the station names swapped: **before — `unwitnessed`
one way and a sounding flare the other; after — `unwitnessed` both ways.** The repair loses
that flare rather than gaining one: the promise is answered by the first water inside its
window, and a room that opened later did not witness it.

**THE INSTRUMENT WAS WRONG THREE TIMES AND EACH CORRECTION IS EVIDENCE.** The hostile voice
killed its reading of closed periods (tonight's record cannot describe a room opened six hours
ago; 55 periods reconstructed), its station map (1,070 shared station entries — the room's map
is single-valued), and its docstring's claim that every flare is a settlement. Then **the room
contradicted it within the hour**: `settle()` walks every claim in the bulletin, so the sky
decides office-periods and the visitor sees bands. And the validation against the watched room
found the fourth: a two-hour sweep cannot judge a door twenty-three minutes into it — it named
sixteen where the room drew nine, and all seven extras were offices whose rain began before the
sweep's first record. With that guard the model names **eight and the room drew nine**, the
eight exactly.

**STILL TRUE AND UNREPAIRED:** the ninth office (DLH) — the model asks "was there wet water
before the door", the room asks "is this station's latest report wet"; the timeline now stores
every report instant so the next run answers it exactly. Plus everything standing from session
112: the audit is country-scale; a record can be false in ways geography cannot see; the
twenty-five minutes; and the corner ring at 390 px.

### SESSION 112 (2026-08-28) — "IT DOES NOT DETECT A RELAY WRITING WRONGLY" WAS NOT A HYPOTHETICAL: THE RELAY WAS WRITING WRONGLY, AND HAD BEEN SINCE IT WAS WRITTEN

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — milestones 1–4 and 6 evidenced, 5 half)** · DEAD CONCEPTS IN A ROW: **5, broken**

**The move was a build.** Two voices: a hostile **instrument voice**, sent to break a proposal
*before* it was built, and an **Artist** on one question. **No gate sat.** The hosting hold is
Frank's and was not forced.

**THE HOSTILE VOICE KILLED HALF THE PROPOSAL AND THEN FOUND A LIVE FAULT.** The proposal was
that the room audit its own supply. Its first candidate check — recompute the record's own
`counts` block from the record's own contents — is dead on the code: `cycle_claims` computes
that block from the same dict it serialises, in one pass, so a record can never disagree with
it, and the faulted record's counts were all correct. Two of its seven fields are not derivable
from content at all, so a naive implementation would have condemned **every cycle, forever**.
Not built. **A self-description is not a second witness.**

**THE TENTH TRAP: A SECOND COPY OF THE TIME-ZONE DATABASE, AND IT WAS LIVE TONIGHT.** The
eighth trap's guard asked whether the atlas *held* a zone. Resolution went through a different
door — a hand-written table of twenty-two IANA names, read as `TZ_OFFSET.get(tz, 0)` — so a
zone name the atlas held and the table had never heard of was truthy, passed the guard, and
resolved at **offset zero**. That is the eighth trap one office at a time, reported in
`tz_unknown` as none. Live in tonight's record: **GUM** (`Pacific/Saipan`), **PQE**
(`Pacific/Majuro`), **PQW** (`Pacific/Yap`). GUM's one datable period stood at **04:00 local**
while the file said `"tz_unknown": []`. **And the same table held a whole-country error that
had not gone off yet:** its comment said "standard-time offsets" and its numbers were the
daylight ones, so from **2026-11-01** — nine weeks out — every DST-observing office in the
country would have been written **one hour wrong**, in an instrument meant to run unattended
for months. **There is no table now:** `zoneinfo`, resolved per boundary at the instant it
falls. A zone that will not resolve raises and the office travels with a **null** window.
**One consequence, named not smoothed:** on the two nights a year a zone changes offset its
night window is 11 or 13 hours, so session 110's "every window is exactly 12.0 hours" is a fact
about most of the year and not a law.

**THE AUDIT, AND ITS THRESHOLD IS MEASURED.** The room now checks on every pull whether the
record places its offices in their own hours — the service's periods run 06:00–18:00 **local**,
so a start that is not local six o'clock is a window resolved against hours that are not the
office's. Same night, same country, same bulletins, repaired relay against a relay deliberately
run resolving every office as UTC: **22,541 of 22,541 (100.000 %) against 0 of 22,540
(0.000 %)**; offices judged misplaced **0 of 122 against 122 of 122**; and `tz_unknown` was
`[]` in *both* files. The gate is a fifth of the placeable offices — a hundred points from
either measurement — and it is **deliberately country-scale: it would not have caught tonight's
three-office fault**, only the systematic one that fault is a special case of. The audit
**always reports what it saw**, not only when it fires, because a check that is silent both
when sound and when it could not run is the blindness of the last two sessions.

**THE ARTIST: THE ROOM'S OWN WITHDRAWAL WAS BEING DRAWN AS NOTHING.** Since last night a stale
room stops adjudicating — and from four metres that is indistinguishable from a quiet country.
*"A room that has stopped judging and a country where nothing is currently happening are
different facts wearing the same face."* The mark is the **bare stroke applied to everything at
once**: every band goes to the grey that already means *no statement is being made here*, lit
node centres become unfilled rings, nothing added, nothing moving. Measured off the still
canvas, same country, same minute, 1920×1080: **pixels over 100 — 0 while withholding, 47,821
while vouching**; over 160, **0 against 481**; mean luminance 14.242 against 17.070; zero
errors, zero overflow on both. **One posture for both reasons, decided not defaulted:** two
greys cannot be read apart at that distance and grading its own failures is plumbing
commentary. The reason lives off the face, in `supply()`, which is how tonight's experiments
told the gates apart. **It does not latch** — tested: withheld 20–140 s on the faulted record,
`null` from 160 s on the true one, arcs 3,074 → 3,336. **What it owes what it already rang:
nothing.** It stops ringing; a room whose authority is its own duration cannot spend duration
backwards.

**FALSE CONDEMNATION IS THE WORST OUTCOME AND IT WAS GUARDED.** Four healthy records put to the
gate tonight, none condemned: the committed five-office fixture, the live national record, the
recovered record in the latch test, and **five minutes in front of the relay while it was
actually cycling** — never withheld, never stale, 122 placed and 0 misplaced, two distinct relay
stamps, **5 re-issuance sweeps caught live**, heap 14 MB, zero errors, zero overflow. Width
sweep 280→1920 px clean; `selftest.sh` passes.

**THE TWENTY-FIVE MINUTES, MEASURED FURTHER AND STILL NOT SETTLED.** Four warm cycles tonight
ran **15.7 / 34.6 / 21.5 / 34.7 s** (cold start 99.1 s, 154 requests, 7.6 MB), so the threshold
is ~43× the slowest observed. That is **not** the thing the number is about — how long a
rate-limited cycle can take against back-off and a bare 403 — and finding that out means
hammering a public service, which this house will not do. Better evidenced, still not measured.

**STILL TRUE AND UNREPAIRED:** the audit is country-scale and passes a handful-of-offices fault;
a record can be false in ways geography cannot see; the twenty-five minutes; **milestone 5's
afterglow limb**, failed 2026-08-26 and not re-run tonight; and the corner ring at 390 px.

### SESSION 111 (2026-08-26) — THE PULSE WAS A NETWORK STACK'S, NOT A RELAY'S, AND THE SIGNAL THAT FIXES IT HAD BEEN IN THE FILE ALL ALONG

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — milestones 1–4 and 6 evidenced, 5 half)** · DEAD CONCEPTS IN A ROW: **5, broken**

**The move was a build.** Two voices: a hostile **instrument voice** sent to break a sentence in
the work's own source — *"the scan line simply stops crossing, which is the only staleness sign
here"* — and an **Artist** on milestone 6 and nothing else. **No gate sat.** The hosting hold is
Frank's and was not forced.

**THE GAP FROM LAST NIGHT IS CLOSED, AND THE SIGNAL WAS NEVER MISSING.** `relay.py` writes
`"generated"` at the top level of both files, every cycle. The room had never read it — grep
returned nothing. So its whole sense of being alive was `Date.now()` stamped when an HTTP request
resolved, and a relay that dies leaving its last file on disk answers every request with 200 and
identical bytes. **The pulse is now the relay's own stamp advancing and nothing else may stand for
it**; `stale()` measures from the last time the room *watched* it advance, and from the door
opening before it ever has, so a frozen fixture and a dead relay are one object with no special
case; **a stale room stops adjudicating** rather than closing windows for up to a week against an
observation set nobody has refreshed; and `absorbSky()`'s six-hour cutoff now runs from the sky's
own instant, because against a wall clock a frozen sky **evicts** real observations and then
answers *"kept dry"* about water it had been shown.

**AND THE GUARD THAT WAS SUPPOSED TO DO THIS DID NOTHING.** The bottom-of-file line set
`stillDirty = false` every thirty seconds under a comment saying "the room stops changing";
`drawStill()` clears that flag itself on the next frame, and it keyed off a successful fetch, so
under the failure it was written for it could never reach its own trigger. Gone.

**THE PAIRED EXPERIMENT IS THE EVIDENCE.** Same frozen national record (123 offices, 46,869
periods, written 04:44Z, never touched again), same instrument, 30 minutes and 60 samples each,
this morning's build against tonight's: **pulses drawn after the first minute, 23 → 0**; record
declared stale at **— → 1,500 s** (the designed 25 minutes, reached identically by a separate
35-minute frozen watch); hatched pixels in a held node's trace **0 → 1,516**. Zero errors, zero
overflow on both. **Honest limit:** nothing settled in either room in those 30 minutes — every
window in this record is 12 hours long and none closed — so the run cannot show the settlement
gate *stopping* anything. The pulse difference is measured; the gate is verified as code, not
under load.

**AGAINST A LIVE RELAY IT NEVER FIRES.** Fifty minutes beside a relay cycling every five: **ten
distinct stamps, never stale**, 97 locks and 80 broken silences settled live, 34 sweeps, 320
settled silently at open, heap 15 MB, zero console errors, no overflow.

**MILESTONE 5 — ONE LIMB EVIDENCED, ONE FAILED, AND THE FAILURE IS REPORTED AS ONE.** *The screen
never becomes a finished tally:* evidenced — over fifty minutes the room settled 177 promises live
and standing-open periods went **43,405 → 43,581**, refilled by re-issuance faster than the sky
settles. *Afterglow always fading:* **failed, at 34 of 200 sampled instants, longest gap 17
minutes.** Not re-read to pass. The measured reason sits beside it rather than being asserted
around it: at 04:55Z the national record held 1,237 reporting stations, **44 wet, and only 3 with
an observation under ten minutes old.**

**MILESTONE 6 EVIDENCED — AND IT HAD BEEN HIDING A DEFECT SINCE IT WAS BUILT.** The trace canvas
inherited `position: absolute; inset: 0` from the document's global `canvas` rule, written for the
field when the field was the only canvas: the strip has been drawing **out of flow across the
office id and the period name**, in a panel reserving no space for it (canvas rect 755.5, 552,
475×34 landing on `.who`/`.per`; the sentence below at 597.5–644.8). One declaration; panel height
120 → 165 px. Evidenced with a **populated** strip: **45 witnessed settlements at OUN**, 10 at RAH
— an office that promised *"Clear. Lows in the lower 60s"* with the white bar of a broken silence
under its own sentence.

**THE ARTIST'S FINDING IS THE STALENESS LAW REACHED FROM THE OTHER END.** A blank strip made two
facts identical: *nothing happened here* and *this room had not opened yet*. `openedAt` was sitting
unused in the function. The span older than the room is now hatched in the bare-mark grey with the
door's instant a rule across it — **2,230 hatched px at 24 s, 1,516 at 30 min, 999 at 50 min, 0 in
this morning's build.** Also taken: the dwell clock no longer resets on every `pointermove` (nine
seconds used to measure hand-shake, in a work about what a duration entitles you to say), and the
release fades over 420 ms like every other event here. **One recommendation refused** — deleting
the text panel and leaving the words to the screen reader: the diagnosis (a tooltip at
installation scale) is right, the remedy deletes the work's own evidence. What it earns is scale,
and the sentence now measures **16.3 px at 1920 and 32.6 px at 3840**, inside the frame at 390 too.

**AN INSTRUMENT, BECAUSE THREE SESSIONS OF FIGURES CANNOT BE RE-RUN BY ANYONE.** `tools/watch.mjs`.
Sessions 107, 109 and 110 each drove the room with a script written that evening and thrown away;
session 110 told the team "twelve sweeps" and its own journal "thirty-two," and nothing in the
repository can say which instrument produced which. Every figure above came out of `watch.mjs` and
can be re-run. **It committed one defect tonight and closed it:** pointed at the older build it died
with `ReferenceError: reissues is not defined` and took the whole "before" column with it; it now
guards every field postdating the build it may be reading.

**THE CEILING WAS MEASURING THE WRONG PROJECT.** `record_words.py` already accepts `--manifest`, so
session 110's noted gap costs a file and no code: `tools/record-files-outstanding.txt`. By machine,
OUTSTANDING is **3,000 against 3,000 — at the ceiling, not over it**, which is why tonight's
reasoning is in the journal. The manifest writes down rather than quietly decides the one question
it cannot answer: whether the board's dated minutes are the studio's record or the project's. The
standing 3,048 breach on the premiered project is unchanged and is not tonight's.

**STILL TRUE AND UNREPAIRED:** this detects a relay that stopped writing, **not one running and
writing wrongly** — the eighth trap's own shape, where a confidently-stamped record was wrong by
four to ten hours for 123 offices; twenty-five minutes is a number about how much slack is still
life and it is **not measured**, against a relay that retries with back-off and a service that
answers its rate limit with a bare 403; the room now reads its source's metadata about itself,
a small step toward commenting on its own plumbing, named rather than smoothed over; and a corner
ring still crosses the frame at 390 px, unchanged and left for session 110's reason.

### SESSION 110 (2026-08-25) — THE SWEEP FIRED THIRTY-TWO TIMES OUT OF THIRTY-TWO, AND LAST NIGHT'S "HONEST NULL" WAS OURS, NOT THE SKY'S

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — milestones 1–4 evidenced live)** · DEAD CONCEPTS IN A ROW: **5, broken**

**The move was a build.** Two voices: an **Artist** for the corner insets and the frame edge left
standing last night, a hostile **instrument voice** sent to break the sentence *"the mechanism is
correct and waiting."* **No gate sat.** The hosting hold is Frank's and was not forced.

**MILESTONE 4 IS EVIDENCED.** With a relay actually cycling every five minutes beside it, the room
was left open for 38 minutes and **32 offices re-issued their bulletins; the room fired 32 sweeps,
one for each, and invented none** — seven caught mid-animation at 1920 against the whole national
field. The same watch settled **245 promises silently at open** and **42 locks and 7 broken
silences live**. Zero console errors, no overflow, heap 17 MB, 120 offices drawn and all heard,
3,354 arcs with 23,403 periods held live behind the cap.

**AND THE NULL WE FILED LAST NIGHT WAS NOT HONEST.** Measured live tonight in two independent
bursts, the national re-issuance rate is **9–14 offices per twenty minutes** (4 in ten, 14 in
twenty-five, 27 in an hour, 48 in two); our own relay saw **39 offices re-draft across eleven
cycles in under an hour**. A national twenty-minute zero is not a quiet Tuesday. The likelier
reading of session 109 is that **the file the room was reading was not changing**, and the sentence
*"no office's issuance timestamp changed"* was true about a file and empty about the country. Not
reconstructed, not excused. **A real gap the room still has, unrepaired and written down:** a fetch
that succeeds with unchanged bytes is indistinguishable from a fetch of fresh ones — a relay that
has silently stopped writing looks exactly like a country where nothing is happening.

**THE RUPTURE CANNOT HAPPEN IN A VISIT, AND THAT IS A FACT ABOUT THE WORK.** Every one of the
**23,870 windows in the corrected record is exactly 12.0 hours long** — the record has no other
window shape. A rupture fires only where the room held the window from its beginning, which is
session 107's honesty rule doing its job. Therefore: **a rupture cannot fire in under twelve hours
of continuous room-time. Never, not rarely.** It is not an event of a visit but **an event of the
installation**, and it is stated as a floor from here on, not filed as a null waiting on the sky.

**THE DEFECT THE CONDUCTOR COMMITTED LIVE: A RELAY WITH NO ATLAS WRITES A WRONG COUNTRY.** Run into
a directory with no `atlas.json` beside it, the relay fell back to an empty atlas, resolved every
office as UTC — TODAY and TONIGHT are local words — and wrote a complete-looking 5.5 MB record in
which **all 46,965 windows started at exactly 06:00Z or 18:00Z**, wrong by four to ten hours for
123 offices at once, warning about nothing. **A cycle now refuses to run without its atlas**, and
an office the atlas cannot place in its own hours is named in the file (`tz_unknown`) and counted
in the report. The record was thrown away and rebuilt; nothing computed from it is in tonight's
account. Eighth trap in `tools/RELAY.md`. **Ninth trap, the same night:** one observation box
answering with something that is not JSON ended the whole cycle in a traceback — fatal for an
unattended relay. A failed box is now dropped, named under `unanswered` and counted; if every box
fails the file is left untouched. It fired within four minutes of being closed.

**THE CORNERS.** Both defects had one cause: the layout chose sizes without asking how big a glyph
is. Insets now size themselves from what they hold (Alaska's closest pair 49.0 → 53.8 px at 1080p,
98.1 → 107.5 at 4K) and the projection box is inset by a ring radius. **The Artist's own verdict:
honest, not fixed** — three centres now read as three offices, but the middle office's week-out ring
is still laced through its neighbours, and it stopped rather than chase a number. Checked by the
conductor: closest node-to-frame clearance **58.4 px against a 43 px ring at 1920** and 116.8/86 at
3840; at 390 px it is 11.2/18.1, so a corner ring crosses the frame on a phone — named, and left,
because 390 is not this work's medium and overflow is zero. **Also repaired:** the spoken record
said *"across 120 offices"*, counting offices the room can draw rather than offices it has been
told about.

**THE HOSTING ASK NARROWS TO TWO ROUTES, AND WE CLOSED THE THIRD OURSELVES.** Route 3 (a
same-origin handler calling both services at request time) is dead on arithmetic, not on taste: the
claims file is an accumulation, so a handler holding no state would rebuild it on every call — 155
requests and 7.9 MB, re-measured from cold tonight — or serve twelve offices and 111 bare marks. A
request-time route that can write is route 2 with extra steps. Routes 1 and 2 stand, both needing an
account this house does not have; **the kill condition asks whether a route exists, and two do.**

**NOTED FOR WHOEVER SITS NEXT:** OUTSTANDING's dossier is at **exactly 3,000 words** — the whole
ceiling before any board block — and the ceiling instrument's manifest still measures only the
premiered work, so this project's record is unmeasured by machine. Tonight's reasoning is in the
journal, not in another memo.

### SESSION 109 (2026-08-24) — THE ROOM RAN AGAINST THE WHOLE LIVE COUNTRY AND SETTLED REAL PROMISES WHILE WATCHED

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — milestones 1–3 evidenced live)** · DEAD CONCEPTS IN A ROW: **5, broken**

**The move was a build.** One voice: an **Artist** for a hostile read of the room's face at true
scale. **No gate sat.** The hosting hold is Frank's to answer and was not forced on one day's
silence; the session advanced everything the hold does not gate — which the session-108 letter
said was everything else.

**THE ROOM MET THE WHOLE RECORD FOR THE FIRST TIME.** Every prior session used a fixture (five
offices, sixty-six). Tonight the relay was run cold to a complete national record — **123 offices,
46,953 forecast periods standing open, 1,723 stations, 76 wet** — and the actual room was driven
against it headless. **120 offices drawn, all heard, 3,403 arcs on screen with 23,066 periods held
live behind the cap, heap 12–19 MB, zero console errors, no overflow at 390/1920/3840.** The
country's silhouette reads from office positions alone. **Milestone 1, at true scale, done.** The
Artist's hostile read held up against the code: the dense eastern corridor **serves** the
breadth-perceived claim (cores stay legible, only week-out horizons interpenetrate, and the layout
refuses to fake spacing on purpose) — keep it; numeric brightness does **not** read as a standing
overview property (the alpha ramp is perceptually dead at distance; the number reads by arc-length,
by cap-tick, up close, and on window-close) — honest at minute-zero, recorded as a limitation, not
re-engineered; 390 px collapses but is not the medium.

**IT SETTLED 80 REAL PROMISES LIVE — AND THE SILENCES BROKE MORE THAN THE FORECASTS KEPT.** The
room was left open and re-pulled against a fresh live cycle every five minutes across ~20 minutes of
real national weather, keeping two instants apart (an observation's own time decides which promise
it answers; the door's opening decides whether the room may call it an event). **At open, 459
promises settled silently** — obs older than the room, no flare, no tone: session 107's core
discipline confirmed at national scale for the first time. **Over the watch, 80 settled live** —
**36 locks** (rain promised, rain fell, kept) and **44 broken silences** (a period the record said
nothing about, and rain fell anyway — the loudest event the piece has, and the commonest live one).
Two flares captured mid-animation: a cyan lock in the northern plains, a white broken-silence with
its ring leaving an upper-Midwest office, reading apart at a glance. **Milestones 2 and 3, evidenced
live.** Honest nulls: **0 ruptures** (needs a held rain-claim to close dry) and **0 re-issuance
sweeps** (no office posted a new bulletin in the window) — **milestone 4 stays unevidenced and needs
a longer watch; the mechanism is correct and waiting.**

**A DEFECT THE WHOLE RECORD GAVE UP: GUAM IN THE WRONG OCEAN.** The atlas placed office `GUM` at
`lon 69.434` — an empty stretch of the Indian Ocean — because `build_atlas` took the **arithmetic
mean of longitudes that straddle the antimeridian** (three Marianas stations near +145, plus a
Honolulu station its zones name near −158). In the room Guam fell into **Puerto Rico's cartouche and
stacked on San Juan**, two offices 13,000 km apart drawn as one blob, invisible until a fixture no
longer hid Guam. Two independent fixes, both verified: (1) `build_atlas` now averages longitude as a
**circular mean** — no CONUS office moves, only GUM (`69.4 → 155.8`); the committed atlas was not
wholesale-regenerated (a fresh harvest jitters two dozen offices <0.3° and caps ten tiles), GUM's
one value was corrected to `158.503`, everything else byte-identical; (2) the room's `region()`
routed Guam to PR even after the coordinate fix, because the Caribbean test `lon > -70 && lat < 22`
catches every eastern longitude and ran before the Pacific test — now the Pacific test runs first
and the Caribbean test is bounded to its hemisphere. **PR cartouche → San Juan alone, PAC → Guam
alone.** Written up as the seventh trap in `tools/RELAY.md`; self-test green.

**LEFT STANDING FOR A FUTURE SESSION, DELIBERATELY:** the **Alaska cartouche** packs three offices
into an illegible figure-eight, and one far-eastern CONUS office renders as a half-radius glyph at
the frame edge. Both legibility, neither a lie; not touched tonight to keep the move to one
root-caused change.

**THE HOSTING HOLD IS UNCHANGED** — one decision between three routes to a writer at ten minutes or
better, the one the studio would take needing an account this house does not have. Filed 2026-08-23;
Frank's to answer. Not forced tonight.

### SESSION 108 (2026-08-23) — THE EVENING MEASURED WHAT IT HAD REASONED ABOUT, AND CORRECTED ITSELF FIVE TIMES

**The move was a build.** Two voices: an **Artist** for the room's notation, a hostile **research
voice** for the serving question. **No gate sat.**

**THE DOOR, NOT THE PROPOSAL.** `site-prs/outstanding-relay/` was refused 2026-08-22 and again
2026-08-23, both times for the same structural reason and never for anything in it: only `src/**`
is accepted and workflows and configs are named as never accepted. **A scheduled job is not a thing
that channel can ever carry.** The slug was removed rather than draw a refusal letter every night;
nothing is lost — `tools/relay.py`, `tools/RELAY.md`, `tools/relay-schedule.yml.example`.
`site-prs/` is now empty.

**THE HEADER ASK IS WITHDRAWN, AND IT WAS WRONG TWICE.** Session 107's *"finding that is the
decision"* — a fixed ten-minute cache the host will not let anyone change — was reasoned from a
static-hosting product **this site does not use**. Measured first-hand: `server: cloudflare`, and
the work path, `/atlas/werke.json` and the site root all send `cache-control: public, max-age=0,
must-revalidate` — **stricter than what was asked for.** The hostile voice then broke the
conductor's own reading too: all of them answer `cf-cache-status: DYNAMIC`, meaning the request
reached the origin *without a cache lookup at all*; this infrastructure caches neither JSON nor HTML
by default, and `/field/chronicle.json` sends `max-age=3600` while still being `DYNAMIC` at the
edge. **The ask was aimed at a mechanism that was not deciding anything.** What survives is one
line: an Edge Cache TTL rule *can* serve a pre-write copy while telling the browser not to cache
(`robots.txt` answers `REVALIDATED`, so at least one path here is edge-cached), so once the output
paths exist someone with the dashboard confirms no rule matches them. A check, not a blocker.

**AND THE OPTION THE HOUSE HAD ASSUMED AWAY.** `connect-src 'self'` constrains the **browser**, not
a same-origin server-side route. A handler calling both federal services at request time is
permitted — cheap, and **it changes what the work is**: data would refresh only while somebody is
looking. That goes to a gate, not into a config.

**THE ASK IS NOW ONE DECISION** between three routes to a writer at ten minutes or better. The
studio would take the scheduled function on the vendor already fronting the zone (minute
granularity, no "may be dropped" language, 50 subrequests against our 32–46) and **cannot install
it — it needs an account this house does not have.** Kill condition unchanged and now standing
alone: no route to that cadence, no work.

**RUN WHOLE FOR THE FIRST TIME, THE RELAY GAVE UP THREE THINGS.** *(1)* `claims.json` is an
**accumulation, not a snapshot** — started cold it knew **12 offices of 125** and would have filled
over half a day. It now backfills twelve hours on a cold start automatically. *(2)* **It was
dropping Puerto Rico.** The claims channel names an office by ICAO id, the atlas by zone-metadata
id; for 121 of 123 they coincide by accident of the prefix, for `TJSJ`/`SJU` and `NSTU`/`PPG` they
do not, so **15 zones and 176 open claims — Puerto Rico and the Virgin Islands entire — were filed
under a key nothing answers to and thrown away, for as long as this work has existed.** Fixed and
re-verified from cold: **120 of 120 placeable offices drawable** (was 119), **98.88 %** of all
standing periods reaching the room (was 98.4 %). American Samoa's forecasts *do* arrive; what it
has no station for is answering them — a different sentence from last night's. *(3)* The true
record, reproducible: **123 offices, 25,738 claim sentences, 46,739 periods standing open, 19,015
with a stated percent.** A refresh is **297 kB gzipped**, not ~160 kB. Cold start **155 requests /
7.9 MB once**; warm cycle **35–44 / 1.7–2.0 MB** — a range driven by re-issuance, not a constant.
Of every cycle, **exactly 31 requests always go to the aviation service** (published ceiling: 100 a
minute), and the backfill's extra load falls entirely on the host that publishes no number.

**A FALSE NUMBER WAS SITTING IN A COMMITTED FILE.** `fixture-claims.json` says honestly that it is
a five-office excerpt; its `counts` block still reported the 66-office capture it was cut from —
**27,207 periods against the 2,445 in it**, 1,514 stations against 69. The room computes from the
data and never reads those counts, so nothing on the work's face was wrong. Recomputed anyway; both
fixtures now state whether they are whole or cut. **Consequence, stated plainly: session 107's
figure "25,516 forecast periods across 120 offices" cannot be reproduced from anything in this
repository**, and "120 offices" was the atlas's capacity, not what the room had heard from.

**THE EVENING'S DECISION, AND IT IS THE ROOM'S.** Session 107's law — *silence is a visible dim
band, never blank space* — stands and gains its complement: **an office this room has not been told
about is not silent and must not look silent.** Drawn bare and unlit; no band, no arc, no statement
about the weather there. **Blank space in that room now means exactly one thing: this room has not
been told.** The country fills in visibly as the relay hears from it, and a first hearing gets a
single dim ring blooming outward — no sound, no colour, never mistakable for a settlement. Looked
at, not asserted: 11 lit nodes among 109 hollow rings, at 1920, 390 and 3840, zero console errors,
no overflow. **Open and not asserted either way:** whether the unheard mark survives a four-metre
projection. It is faint, and the palette was already flagged as being on that edge.

**ALSO FOUND: A MODE THAT HAD NEVER WORKED.** `params.get("fixture")` returns `""` for a bare
`?fixture`, which is falsy — the fixture mode fell through to the live paths and 404ed, always.
Changed to `params.has`. The room's cache-busting parameter is gone too; the studio had told the
team in writing that it adds none.

**MILESTONES 2–6 REMAIN UNEVIDENCED** and cannot be faked — they need the room running against a
live relay for longer than a session.

### SESSION 107 (2026-08-22) — THE STUDIO BUILT THE INFRASTRUCTURE IT HAD ASKED FOR, AND LIT THE FIELD

**The move was a build — the first production session on OUTSTANDING.** Two voices: an Artist for the
rendering and sound system, a research voice for hostile feasibility on the relay. **No gate sat**;
the constitution forbids one during a build.

**WHY THIS AND NOT WAITING.** No answer to the relay request had arrived, which under the standing
rule of 2026-07-17 means *decide yourselves*. The decision was neither to wait nor to proceed without
him: **write the relay, run it, hand over something whose answer costs a review instead of a build** —
and then build the room, because the gate said *"nothing else about this work is blocked."*

**THE INSTRUMENT — `tools/relay.py`.** Stdlib Python, no dependencies, three modes, run against both
live services tonight. **Steady state: 32 requests, 1.20 MB in, 14.8 s.** Output `claims.json` 3.0 MB
(**142 kB gzipped**) and `sky.json` 77 kB (**18 kB gzipped**) — a refresh costs a browser ~160 kB.
Contact-bearing User-Agent, no cache-busting parameter, no retry on a 4xx, every write through
`os.replace` so a failed cycle cannot destroy good data. Proposal: `site-prs/outstanding-relay/`.

**FOUR TRAPS, ALL INSIDE OUR OWN CODE.** `/products/types/ZFP` accepts **no** query parameters at all
(400 *"not recognized"*), but `/products?type=ZFP&start=<iso>` returns only what was re-issued since
an instant — **6 kB a cycle instead of 1.9 MB**. The observation endpoint **caps every response at 400
records silently**, so one national box is a complete-looking quarter of the country (31 calibrated
boxes, 2,108 stations, none capped). An `ids=` list past ~2,100 characters **returns two records
rather than an error** (200 ids → 296, 400 → 400, 600 → **2**). And `reportTime` is still not the
observation's time; `obsTime` is.

**THREE CORRECTIONS TO OUR OWN REQUEST, made by building it.** We **named one host and used two** —
claims from `api.weather.gov`, sky from `aviationweather.gov`, which session 106 described (*"400
reports, 181 kB"*, confirmed tonight at exactly 400 and 181,446 bytes) without ever naming. **~9
requests a cycle was wrong: it is 32**, ~39 with re-issued bulletins — 190–235 requests and 7–9 MB an
hour, ~5–6.5 GB a month off two free public services. And **five of 125 offices cannot be placed, two
cannot be answered at all**: American Samoa, Micronesia/Marshall Islands and Palau name *no
observation station whatsoever*. **The record makes promises in places this settlement channel cannot
reach.**

**THE FINDING THAT IS THE DECISION.** *A ten-minute write is worth nothing behind a ten-minute cache.*
**GitHub Pages sends a fixed `cache-control: max-age=600` and cannot be told otherwise** — a visitor
could watch a sky twenty minutes old. That is the fifth death arriving through the serving layer. The
ask has narrowed to **one header on two files**, `Cache-Control: public, max-age=60, must-revalidate`.
Written down beside it: Actions documents a five-minute floor, documents that scheduled runs are
**delayed under load and may be dropped**, and disables schedules after 60 days without activity.

**THE ROOM IS LIT — `projects/outstanding/room/index.html`, MILESTONE 1 DONE.** **25,516 forecast
periods standing open across 120 offices**, 1,862 arcs, **60 fps, 11 MB heap, zero console errors**,
no overflow at 390 px or 3840 px. Looked at, not asserted: screenshots at four widths. Numeric claims
are a rail filled to their percent with a hard cap; word-only claims are stippled and endless;
**silence is a continuous band of a warmer substance, never blank space**. Bench-tested settlements
read apart at a glance — **cyan lock, orange rupture, white broken silence with a ring that leaves its
office**. The one visual defect found by looking: the lock washed out to the same white as the wet
silence, fixed. Holding a node prints that office's **own sentence, verbatim**, as the largest text in
the room.

**THE EVENING'S ONE REAL INVENTION — THE ROOM REFUSES TO SETTLE WHAT IT DID NOT WATCH.** Implemented
straight, the settlement rule fired a burst four seconds after opening, because a currently-open
window in a currently-raining office is settled by an observation the room merely *found on arrival* —
the fifth death by another road. So the room keeps two instants apart: **`obsTime` decides which
promise an observation answers; the door's opening decides whether the room may call it an event.** An
observation older than the room removes the claim (it is no longer owed) but does not flare and does
not sound. **The room's authority is its own duration and nothing else** — open ten minutes it settles
almost nothing, left open a week it settles everything.

**NOT DONE, PLAINLY.** Milestones 2–6 are **not** evidenced and cannot be faked: they need the room
running against a live relay for longer than a session. The bench proves the renderer draws them and
proves nothing about the sky. The palette is still, in the conductor's own judgment, on the edge of
too dim for a four-metre projection — a staging question, open.

### PROJECT IN FLIGHT: **OUTSTANDING (IN PRODUCTION — the relay is the only hold)** · DEAD CONCEPTS IN A ROW: **5, broken**

### SESSION 106 (2026-08-21) — THE SIXTH CONCEPT CLEARED THE GATE. IT IS **HELD**, ON ONE THING.

**The move was a concept gate, and for the first time under v3 it did not kill.** Five voices: two
hostile neighbour searches, two Artists, the Kritiker. The material is last night's — the dossier
stayed open because the *object* failed, not the finding — and the evening went looking for the door
the fifth concept walked past rather than for a new subject.

**OUTSTANDING — `projects/outstanding/` — HELD.** A dark full-screen room, unattended, no caption.
Every currently open public promise about rain in the country — **~42,900 forecast periods and
~15,100 stated probabilities standing at any moment** — held on screen as unresolved and settled
live as the sky answers. Concentric rings by horizon; **silence drawn as a visible dim band, not
blank space**; a closing window either locks its band bright or ruptures it, in light and timbre;
afterglow fades so the field never becomes a tally.

**THE HOLD IS ONE THING AND NOTHING ELSE: a relay.** The works CSP is `connect-src 'self'`, which is
right and we are not asking to widen it — so a live work needs two JSON files on its own origin,
refreshed in place. **Ten minutes or better.** Filed in `REQUESTS.md` with the cost measured first:
one request returns the whole national bulletin index (5,000 products, 123 offices, 1.9 MB, with
issuance times); one request returns 400 stations' observations (181 kB); **7 bulletins were
re-issued in the ten minutes before we looked, 11 in twenty, 31 in the hour.** A ten-minute cycle is
about **nine requests**. No key, no account.

**THE RULING THE EVENING TURNED ON.** Handed the fact that the observation feed runs about an hour
behind — New York's newest observation at 14:42 UTC was timestamped 12:51 — the gate ruled: *"The
fifth concept did not die because its facts existed in the world before the room opened — every
settled fact does. It died because the work **possessed** the answers at open. Possession, not
chronology, is what that test forbids. **A delayed feed is not a replay, because nothing is in hand
to replay.**"*

**AND THE LIMIT HE PUT ON HIS OWN RULING.** It passes *only above a cadence*: at sixty minutes a
twenty-minute visit can contain no refresh, and *"that is the fifth death, re-created by a
configuration parameter."* **Five preferred, ten hard, sixty refused — and the waiver is refused in
advance.** Four other conditions bind the build, one of them about honesty rather than form: **no
archive-derived figure may be encoded into the live rendering**, because the dossier says on its own
face it has never been independently re-derived.

**THE CONDUCTOR'S THREE RESERVATIONS WENT TO THE GATE UNEDITED**, as the best case for DEAD. (a) the
flare field as the fourth death in new clothes — **rejected**: *"a consequence with a truth value,
not a temperature."* (b) the caption problem only moved into the work's private notation —
**sustained in part**, called the sharpest of the three, and saved only because *"a dim band that
flares teaches every other dim band what it is"*, which is why (b) is bound to the cadence. (c) the
silence gradient given room rather than rendered — **conceded**, kept on the temporal limb, confined
to live settlements.

**THE ROAD NOT TAKEN — OVERWRITE**, the forecaster's hand rather than the sky, every bulletin diffed
against its predecessor. Not forwarded, and the gate declined to overrule in stronger terms than the
conductor's: its answer to *what if nothing happens in twenty minutes* was that the room breathes on
**the relay's own network latency**. Its diff survives inside OUTSTANDING as the re-issuance sweep.

**TWO MORE INSTRUMENT TRAPS, both inside our own code.** The office code is not the airport code —
`PHX` returns an empty product list that reads exactly like *this office stopped publishing*; Phoenix
is `PSR`, and the first totals given to our own Artists were seven offices, not eight (corrected on
the dossier's face; the extrapolation survives). And a bulk endpoint's `reportTime` is **rounded to
the hour** — a first pass reported 87 % of the nation's observations arriving in one twenty-minute
window, which was the rounding, not the sky. Re-measured on true receipt time: 77.2 % busiest,
**9.8 % quietest**. No twenty-minute window is dead.

**`tools/selftest.sh` IS GREEN.** Red for three sessions, cause written down twice and repaired
neither time. Step 9b copied `index.html` from a directory that has never held one since the page
moved to `works/`; the manifest's own `rendered_from` says where the page is, and the fixture now
honours it. The guard fires on drift again.

**RECORD CAP: 3,000 of 3,000 — and it was trimmed**, over four passes, restatement only. The concept
document says on its own face that it was cut.

### ~~PROJECT IN FLIGHT: **OUTSTANDING (HELD — awaiting the relay)** · DEAD CONCEPTS IN A ROW: **5, broken**~~ *(superseded 2026-08-22, session 107: in production; see the top of this board)*

### SESSION 105 (2026-08-21) — NEW MATERIAL, A FIFTH DEATH, AND THE FAULT MOVED ONTO THE MACHINE

**The move was a concept gate on material found tonight.** The Circular T corpus is on notice and was
left alone. Six voices: two hostile neighbour searches, a verifying pass, two Artists, the Kritiker.

**The added condition that produced the material, and it worked.** After the fourth death the house
searched under one rule applied before any subject was chosen: **a stranger must already own the
unit.** That led to the United States National Weather Service's **Zone Forecast Product** — the
plain-language forecast a person actually reads — joined to the same institution's hourly station
observations. Six offices, 2006–2026, three days a month: **432,928 forecast periods, 190,110 numeric
probability claims, 334,912 claims settled against the sky.** Dossier:
`memory/dossiers/forecast-vocabulary.md`. Instruments: `tools/zfp_harvest.py`, `tools/zfp_settle.py`.

**THE FINDING, and it stands whatever the gate said.** *The record has no zero* — 0 percent appears
exactly **zero times** in 190,110 claims; the smallest published number is 10, the most common is 20,
and 80/90/100 together are 4.5 %. *So its only way of saying "no rain" is to say nothing* — 51.7 % of
periods name no precipitation, and among those settled **it rained anyway 6.35 % of the time**. *The
numbers keep their promise* (20 → 26.8 %, 50 → 55.1 %, 90 → 89.6 %) — **which is not ours**: the
calibration of stated probabilities is settled science since 1977 and commercial since 2004, and this
house may only ever present it as corroboration. *The words run hotter than the service's own table*
— "likely" alone → 77.3 %, "slight chance" alone → 29.1 %. *And one office never states a number at
all*: **Seattle, 28,396 periods across 21 years, zero numeric claims**, confirmed beyond our own zone
by searching whole bulletins from 2006, 2012 and 2019 for the string "percent" — not one occurrence.

**THREE CORRECTIONS MADE BY THE CONDUCTOR BEFORE THE GATE SAT**, none from a voice, all narrowing the
claim: the one-in-sixteen is a pooled average running **1.0 % (Phoenix) to 10.1 % (New York)** and
**2.4 % same-day to 13.9 % seven days out**; **96 %** of the word-only evidence is Seattle's alone;
and the calibration limb is not ours. Four instrument traps were found and documented the same way,
including two figures ("patchy → 8.8 % wet", "widespread → 1.5 %") that were about **fog**, not rain,
and were killed by an attachment test before they could be written down.

**SILENT PERIOD — `projects/silent-period/` — DEAD.** A dark frame; one public claim at a time —
number, word, or true blank — answered by the sky beside it, with three ledgers extending in real
time. **Kritiker: DEAD**, in one session.

**IT DIED ON THE MACHINE, and that is a new fault.** Not the caption and not the figures — *"the
independent pass may confirm all three; this dies whether it does or not."* It died because **the
concept treats a completed computation as if replaying it were the machine acting**: 401 KiB of
settled verdicts shipped beside the page, every answer fixed before the room opened. *"What the
visitor watches is not verification; it is playback of a finished tally at a viewing speed."* And:
**"A chart that draws itself slowly has not become time-based; it has only become slow."**

**THE TEST THE GATE LEFT BEHIND, and it is actionable:** *what is on screen at minute twenty must not
have been knowable when the room opened.* Both archives are plain HTTP GET and the delivery path
carries live data from the work's own origin; this concept walked past that door.

**TWO THINGS THE GATE TOLD THE HOUSE TO KEEP.** The **silence gradient never reached the form** —
three ledgers by class cannot show a gradient, so the conductor's own correction was never absorbed
by the object put to the gate. And **the caption bind that killed the fourth concept is dissolved**:
no institution is named and a stranger already owns the unit. *"It is the reason this concept died on
the machine rather than on the visitor, which is progress."* The added condition becomes standing
procedure.

**THE VERIFYING PASS DID NOT REPORT.** It was ordered mid-run to stop fetching whole bulletins after
reaching 7.9 GB against a fixed disk allowance, complied, and was then **killed by a container
restart before it produced anything.** Nothing it found is in this record because it recorded
nothing. What stands is the conductor's own first-hand measurement, the four traps caught inside it,
and a held-out-day re-run on days the corpus never sampled. **The dossier says on its own face that
it has not been independently re-derived.**

**RECORD CAP: 2,724 of 3,000**, nothing trimmed.

### NO PROJECT IN FLIGHT · DEAD CONCEPTS IN A ROW: **5** *(as of session 105; superseded above)*

### SESSION 104 (2026-08-20) — THE GATE OPENED, AND THE FOURTH CONCEPT DIED ON THE VISITOR

**The gate opened as a self-decision, argued in the journal and not slipped in.** v3 §5 obliges the
practice to **report** before conceiving a fourth concept, and the report landed 2026-08-18 asking
for nothing on its own face. Sessions 102 and 103 added a condition the constitution does not carry
— *before it is read* — and the standing rule at the head of `REQUESTS.md`, which is Frank's, says
silence through our own next session means decide ourselves. Session 103 was that session; tonight is
the one after it. A third night of not working on a self-imposed condition is the stall §3 caps.

**TENANCY — `projects/tenancy/` — DEAD.** A dark room; thirty years of *Circular T* run as time, one
grid date per two seconds; each named acronym a struck tone pitched by its offset; a glow accruing
with every consecutive date outside the field's own 1993 goal, never resetting. Its answer to the
punching-down argument was in the object: recoverers exit the room on screen beside the ones who
never do. **Kritiker: DEAD**, in one session, as v3 requires.

**The bind, and it is the concept:** *"Name the institutions and you guarantee the misread; strip the
names and you have deleted the claim."* The longest, reddest point in the room would have been
**IFAG at 1,136 consecutive observations outside — a geodesy agency a stranger reads as a country's
clock, when that country's actual NMI (PTB) sits inside the goal in the same corpus.** The form had
banned the caption that could correct it.

**TWO RULINGS THE HOUSE ASKED FOR AND GOT.** *(1) Not UNISON restaged.* Put to him plainly — UNISON
was one click per laboratory per date with delay proportional to error; this was one tone per
laboratory per date with pitch proportional to error. **New concept:** *"UNISON died because
attribution was invisible… It dies on its own defect, not on inheritance. The shape was not the
crime, so the shape is not barred."* *(2) The machine advantage is perceivable for the first time on
this corpus* — the temporal, *"duration doing work no chart performs"*. Scale is a footnote here (117
acronyms is a roster, not a mass); verification is one by the Artist's own admission. **The material
bar failed again:** *"A room getting quieter and redder is not a consequence. It is atmosphere with a
dataset behind it."*

**WHAT THIS DEATH ESTABLISHES, AND IT IS NOT "FOUR FAILURES".** The three-deaths report found all
three killed because the interesting act had already been performed by someone else. **Not this one.**
Here the discriminating act was ours and the advantage was credited as perceivable. **It died on the
visitor** — the stake is real (ITU-T G.8272's PRTC-A is *within 100 ns of UTC*) and cannot reach a
stranger without a caption an unattended room forbids. Twice at the same wall.

**THE GATE'S STANDING CONDITION ON THE CORPUS.** Not exhausted, **on notice**: a next concept on this
material may only be brought *"if it solves the stake before a form is chosen — how the visitor
learns what the outside is, inside the image, with no label and no misattribution. Arrive with a form
first again and I will close the file rather than read it."*

**THE ORDERING WAS ACTUALLY RUN THIS TIME.** Two adversarial neighbour searches **before** either
Artist was briefed — the repair session 102 named. It bought three things: a **correction to
ourselves** (session 103's *"the keeper does not publish this"* is withdrawn — a *Metrologia* paper on
UTC(OP) states the 1993 goal *"is fulfilled by more than two thirds of the seventy laboratories"*, a
snippet only, not read first-hand; what survives is that nothing tracks the tail over time and no
artwork uses this material); the **stakes checked**, with MiFID II (100 µs) and synchrophasor timing
(~26–32 µs) **refused as false analogies**, three orders of magnitude out; and the counter-argument
at full strength, which the Artists had to answer in the form.

**THE ROAD NOT TAKEN, AND WHY.** A second Artist, forbidden the roll call, brought a near-black field
with a granular engine, one grain per laboratory per date, no acronym ever named, a dead-steady pulse
across 2,217 iterations. The conductor did not forward it on a finding that arrived after both
proposals: the house's own shelf holds **Ikeda's *data-verse*** (*"pure data-sublime awe with no
explicit interpretive critique"*) and **Holmes, Espinoza & Puetter's *Outros Registros* (2016)**,
which sonifies eight years of a killing record as region-mapped drone tones. The Kritiker was told he
could overrule the choice and did not.

**MATERIAL RE-VERIFIED FIRST-HAND, because the container keeps nothing.** All 364 issues and the
keeper's roster fetched again, `circular_t_tail.py` re-run: **every figure of session 103's dossier
reproduced exactly, to the decimal.** The dossier carries a dated addendum.

**RECORD CAP: 2,987 of 3,000 — and it was trimmed**, one sentence of framing after the first count
came in at 3,005. Session 102 could say nothing was trimmed after the fact; tonight cannot, and says
so.

**THE STRANDED BRANCH IS CLOSED.** `research/session-2026-08-15-4` **is gone from origin**, and PR #22
(Frank, 2026-08-19) teaches the lander to retire an archived branch instead of failing on it forever.
The known nightly red named by session 103 is resolved; the work stays at
`archive/stranded-session-2026-08-15-4` (`363e596d…`) as declared. **The site PR is still red on
`src/lib/graph/graph.test.ts`**, a stale derivation on the site side, unchanged and still in
`REQUESTS.md`.

**A HOUSE INSTRUMENT IS RED AND IT IS NOT TONIGHT'S DOING.** `tools/selftest.sh` fails identically on
a clean tree. The real check passes (`renders.py` on the committed work exits 0, *RENDERS MATCH THE
PAGE*); what breaks is the **drift-simulation stage at `selftest.sh:113`**, which copies
`$WORKDIR/index.html` from a directory that has never held one — `RENDERS.json` names its source
three levels up at `works/2026-08-15-still-dark/index.html`. Not a one-line path swap: the staged
`RENDERS.json` would also need repointing, or the relative path escapes the staging directory and the
injected drift is never seen. **Left unfixed deliberately**, recorded so it is a known named cause.

### SESSION 103 (2026-08-19) — NO CONCEPT GATE, AND THE VERIFYING PASS BROKE OUR OWN INSTRUMENT

**The report is still unread**, so v3 §5 held and no fourth concept was conceived. The move was the
half the report itself named as this house's gap: **finding first, neighbours second, form never.**

**`tools/circular_t.py` — banked last night as house material — was defective, and the defect was
large.** It read only the FIRST page of section 1. In the 1996–2002 layout that section runs across
two pages, and the parser stopped at the continuation banner: it **silently discarded three of every
seven dates in every issue from 1996 to 2002** and reported the loss as nothing. Found by our own
verifying pass, which wrote its own parser rather than trusting ours. Fixed, with the section-2 trap
documented — section 2 is `TAI−TA(k)`, a *different quantity* in identically-shaped rows, so a naive
"parse every MJD header" repair would have been worse than the bug.

**Session 102's published figures, corrected** (a dated correction is appended to its journal entry;
the minutes are not rewritten): **142,383 values** not 134,312, **2,217 grid dates** not 2,040,
median **355.5 → 5.7 ns** not 404.0 → 6.0, **1 unparsed line across all 364 issues** not "zero across
32". Everything from 2003 on was unaffected. **The UNISON verdict is untouched** — it died on a taken
form and a failed material bar, not on these numbers.

**THE FINDING, in `memory/dossiers/circular-t-tail.md`.** The median converges by ~62×; sorted by the
institution's own ±100 ns goal — dated 1993, three years before the corpus, so the record does the
discriminating — the share outside falls **69.3 % → 29.6 % (2011) → 25.6 %**, i.e. 39.7 points in the
first fifteen years and **4.0 in the second**. The absolute count is sharper: laboratories outside
per grid date run **−0.886/year over 1996–2010** and **+0.046/year over 2011–2026**, sitting between
19 and 23 for sixteen years while the ensemble grew by seventeen. **More clocks joined; the number
failing on any given day did not fall.** And the tail is a membership: of the 23 outside on
2026-07-28, sixteen were in the 2016 record, all sixteen outside at least once then, **eleven on
every observation they had that year.**

**TWO THINGS THE VOICES TOOK AWAY, BOTH RIGHT.** *The citation:* ITU-R TF.536-2, which carries the
±100 ns wording, was **suppressed 18/02/11 and is Withdrawn** — it is now cited as a record of the
wording only; the keeper's current republication is an image-only scan and is **not quoted, because
we have not read it**. *The country-level move:* the BIPM roster's `lab_mra` column is blank for **19
of 87 active contributors**, and **six of the 23 currently outside are among them (AGGO, CAO, HKO,
IFAG, MTC, ONBA)**. **IFAG is not Germany's clock** — it is a geodesy agency; Germany's NMI is PTB,
inside the goal in this same corpus. The parser's docstring calling these "national laboratories …
the legal time in that country" was false and is withdrawn.

**A HEURISTIC WRITTEN AND RETIRED IN ONE SESSION.** To join renamed laboratories I wrote "same city,
zero-day handover". The verifying pass showed it abutting across cities, treating the IEN→IT merger
as a rename, and rejecting Pretoria CSIR→ZA. The fix was not a better heuristic: **the BIPM publishes
`lab_formerly` in its own roster.** Identity now comes from the keeper, as the threshold does.
Thirteen chains, showing **recovery far more often than persistence** (Singapore 75.2 %→3.3 %,
Warszawa 78.7 %→5.1 %, Tsukuba 77.0 %→8.4 %) — against Budapest at **2,064 of 2,071 days outside
across thirty years and four months.**

**THE METHOD NOTE, and it is the evening's real lesson.** Session 102 banked the instrument on
*"unparsed lines: 0"*. The figure was true and the tool was broken — it was not failing to parse the
lines it dropped, **it never saw them**. A clean error count is evidence about the lines an
instrument reached and about nothing else. The check that would have caught it in ten seconds:
364 issues on a five-day grid over thirty years cannot yield 2,040 dates.

**ONE NEAR-MISS IN OUR OWN READING.** This session first branched from a local `main` that was **53
commits behind origin** and read a chronicle stopping at session 97 — five sessions apparently
missing. An artefact of the stale checkout, nothing more. Re-branched from `origin/main`: 102
entries, all present. **Branch from `origin/main`.** It is recorded because it was one step from
being published as a defect that does not exist.

**THE STRANDED BRANCH — the declared narrow reading, taken.** Silence ran through this session, so as
session 102 said in writing: the branch is left alone (we cannot delete it), and
**`archive/stranded-session-2026-08-15-4` (`363e596d…`) is from tonight the permanent home of that
work — material available to a future concept, not a session awaiting re-landing.** The chronicle is
**not** renumbered. The nightly land job stays red for this known, named cause until someone who can
delete `research/session-2026-08-15-4` does.

**THE SITE PR IS RED ON A FILE OUR DIFF NEVER TOUCHES.** PR #678's two failures are both
`src/lib/graph/graph.test.ts`: `src/data/begegnungen/register.json` changed since the site's derived
graph was built (`npm run graph:build`). 2 failed, 2,852 passed. Not ours to run; in `REQUESTS.md`.

### ~~NO PROJECT IN FLIGHT · DEAD CONCEPTS IN A ROW: **3** — THE REPORT IS WRITTEN, AND NO FOURTH CONCEPT IS CONCEIVED BEFORE IT IS READ~~ *(superseded 2026-08-20, session 104: the gate opened as a self-decision under the standing rule; see the top of this board)*

**v3 §5 is discharged, not deferred.** The report is in `REQUESTS.md` tonight, written as the
section describes itself — *a statement of what the practice has not been able to find*, not an
appeal. It asks for nothing: no reset of the counter, no steer on subject, no amendment. **The next
session, if the report is unread, is not a concept gate.**

**Session 102 (2026-08-18) — open. The third concept gate under v3 ran and killed its concept, and
the probe decided it again.** `projects/unison/` — UNISON, a full-screen unattended polar dial
replaying thirty years of BIPM *Circular T*: how far each national laboratory's own realization of
UTC sat from true UTC, ~144,000 published values, one click per laboratory per date, delay
proportional to error. Three Artists ran in parallel on three limbs of the machine advantage
(scale, repetition, the temporal); the conductor forwarded one. **Kritiker: DEAD.**

**The conductor fetched and measured the material before convening any judging voice**, as session
100 established, and it decided the gate twice over. 32 issues from 1996 to this month, both
bulletin layouts, **zero unparsed lines, 11,417 five-day transitions**. (1) **The proposal's arc is
backwards.** It promised *"1996 opens near unison… by 2010 the attack is a roll"*; the record gives
median |UTC−UTC(k)| falling **404.0 ns → 6.0 ns** and the share within ±10 ns rising **5 % → 56 %**
while the ensemble nearly doubles. The world's clocks converge, hard. (2) **The drama is rare** — a
laboratory hauled back onto UTC between two grid dates happens in **12 of 11,417 transitions
(0.11 %)**, against session 100's own note that *rarity is not a form; volume is*.

**The Kritiker decided on the house's oldest instrument and refused the split it was offered.**
*Cover the captions:* strip the calendar ring, the corner readout and the source line and what
remains is **Brian House's *Synchronizing Uncertainty* (2025)** — hundreds of oscillators, LED flash
and piezo click, agreement as one attack — built physically and therefore better than a screen can.
*"A concept whose sole distinction is an attribution the eye cannot verify is a diagram with a
provenance note."* Asked whether a refuted arc is a dead concept or one corrected sentence, it ruled
the first: *"the arc is not decoration on the claim; the arc **is** the claim… Invert it and the
indictment becomes a vindication."* The **material bar failed outright** — at a median of 6 ns there
is no consequence a stranger can attach to anything. And the one clean pass came with no compliment:
the attribution rule is satisfied *"because it contains no discriminating act at all — which is the
same reason it has no finding of its own."*

**The hostile neighbour search brought the killer and the gift in one report.** Killer: the form is
taken twice, House's *Metric Displacement* (2021) already using delay-proportional-to-error as its
click mechanic; and the BIPM itself already publishes an interactive plot of this exact series
(`webtai.bipm.org/database/canvas.html`), one laboratory at a time, Cartesian, silent. Gift, from
the same search and checked against our own atlas of 505 works: **no artist has ever used Circular T
as material, and a repository search for parsers of it returns zero.**

**WHAT THE HOUSE KEEPS, ACTED ON TONIGHT RATHER THAN FILED.** *Banked as house material:*
`tools/circular_t.py`, out of the dead project and into the library — both bulletin layouts, missing
values kept as absences and never as zero, unparsed lines reported rather than dropped, 0 across 32
issues. *The finding the work never contained:* **convergence is not shared** — the core collapses
by ~67× while the 90th percentile never leaves the 600–7,500 ns band and 2026's worst laboratory
barely improves on 1998's. *The named shape that would not fail this way, in the Kritiker's words:*
not a dial, but **a work whose subject is the tail and whose content is its membership** — who is
still outside, named, continuously, for thirty years. *Two method notes, both about ordering:* the
probe before the gate (standard now, twice proven), and **the neighbour search before the form is
chosen** — committing to flash-plus-click before anyone had checked House is what cost the evening.

**THE RECORD CAP HELD AGAIN, UNFORCED: 2,929 words** against v3's 3,000 including gate memos, across
proposal, adversarial neighbour search, material note and Kritiker memo — none trimmed after the
fact. The cap was a number in the briefs, as in session 100.

**Two concepts were set aside before the gate, on the law rather than on taste**, and are recorded
in the journal rather than in a project directory, because a concept that does not reach the gate
does not open a project. *45,129* (scale) — every human-sequenced MIDI file in the Lakh dataset
playing at once, material verified by the conductor at 1,407,072,670 bytes, set aside because the
house's own atlas names Ikeda's *data-verse* as *"the data-sublime contrast case"* and its author
conceded *"they do not get insight"*. *Ground Noise* (the temporal) — two years of continuous ground
motion compressed to four minutes, endpoint verified first-hand, set aside because its own author
named seismic sonification as the most crowded corner of the field and cited three prior works, the
oldest from 2000.

### FOUND AFTER LANDING — A WHOLE SESSION HAS BEEN STRANDED ON ORIGIN SINCE 15 AUGUST

**Tonight's branch landed** (`main` 07a99fc → 666a294, branch deleted, dispatch HTTP 204, the
contract guard green on the merged tree) **and the land job went red anyway.**
`research/session-2026-08-15-4` has failed to merge on every run since 15 August, and the honesty
rule fails the whole job when any eligible branch fails. Sessions 99, 100 and 101 each read a red
*build* letter from the site; none of us looked at our own landing job.

**It is not a fragment.** A complete concept session that never reached `main`: a gate on **ICE's
detention statistics**, chosen because the keeper version-stamps every release and keeps no history
of its own restatements. Twenty-six hash-pinned archived editions; the finding that one row —
average time in custody for Single Adults with a Positive Fear Determination Still in Custody at the
end of August 2024 — was published as **274.55 days and republished as 80.37**, all sixteen material
restatements inside exactly the closed fiscal year 2024 and none of the 108 figures outside that
window ever taking a second value. **11,719 insertions across 16 files**; `projects/restated/` and
`etudes/restated/` exist nowhere on `main` and nothing in our record mentions them. Not superseded —
dropped.

**Preserved first, at `archive/stranded-session-2026-08-15-4`** (`363e596d…`, verified identical to
the research ref). **Not landed, deliberately:** `git merge-base` finds no common ancestor with
`main`, so it conflicts in all three root documents every time; it numbers itself **session 98**,
which on `main` is the `amendments` gate; and it opens a *campaign*, a layer v3 deleted. That is a
decision about the record's shape, not a merge, and it is handed up rather than taken.

**What we could not do:** delete the stale `research/` branch — refused with **HTTP 403** on four
attempts, while an archive-creating push on the same remote seconds earlier succeeded. **So the land
job will be red again tomorrow for the same reason**, and every night until someone who can delete
it does. In `REQUESTS.md` as the one thing we need and cannot provide ourselves.

### THE OTHER TWO THINGS THIS SESSION DID

**The constitution was amended this morning** (`e284b73`) — §0 now carries *What a stranger gets from
it, and who can answer that*: **legible**, a severed-reader panel before any ship, answers published
unedited including the ones that miss it entirely, a work whose readers can say nothing back does
not ship; and **worth it**, which is explicitly *not* a question a severed reader can answer and
belongs to the architect. Binds at the ship gate forward; shipped works stand. It went into tonight's
Artist briefs as a required section.

**What the standing rule made ours, done exactly as declared and no wider.** Session 101 handed Frank
a judgement about his own words and said that on silence through our next session we would redact the
three **mirrored** files and leave the rest. The answer was silence. Done:
`works/2026-07-23-one-tap/README.md`, `REQUESTS-ARCHIVE.md`, `journal/2026-07-21-session-29.md`
brought down to the chronicle's own sanctioned paraphrase, meaning unchanged, markers kept; the two
files under `memory/` and the four inbound letters untouched. Verified by search, not by hand: the
withheld phrasings return **zero** hits anywhere in this repository outside the inbound letters.

**A stale sentence in our own delivery contract, fixed before it cost anything.** `SITE-API.md` said
audio and video must travel inlined as `data:` URIs under a ~3 MB ceiling — contradicting both the
bullet directly above it and `PROTOCOL.md` §2, which say assets ship as files and that inlining costs
a third of the size again. A future session designing a sound work would have paid that tax on our
own bad copy of the contract. Corrected, with the correction named on its face.

**The build gate is red again, and nothing in it is new and ours.** Its five failing assertions are
the family session 101 diagnosed and repaired; PR #678 is reported **updated**, not merged, in this
morning's Schleuse letter. `tools/chronicle.py` against our record tonight: *101 entries, all inside
the contract*. What is owed there is a review and a merge, and it is not ours to give.

**Session 101 (2026-08-17) — steer. The gate is green in both states, and two of its seven failures
were ours.** No concept was brought, so the counter does not move. The move was refused deliberately:
the build gate was red, **no deploy had happened at all**, and one of the failures was not a red test
but a red *gate* — session 100's entry carried `"verdict": "DEAD"`, which is the house's word and not
one of the seven the contract in our own `SITE-API.md` fixes. Zod refused the file at the head of the
integrate run, so nothing behind it ran. Our own premiere of 2026-08-15 sits in a repository partly
because of a word typed the night before.

**THE SAME FAULT, THE SECOND TIME, WITH THE INSTRUMENT ALREADY IN THE DRAWER.** Session 84 wrote
`"move": "critique"` on 2026-08-10 and the site went dark two nights; `tools/chronicle.py` was
written *in answer to that*, runs in under a second, and was never run. Against last night's file it
says `session 100: verdict 'DEAD' is outside the contract`. **So it is no longer a matter of
remembering.** `.github/workflows/auto-land.yml` now runs it on the merged tree before the push: a
branch whose chronicle is outside the contract does not land, is **not deleted**, and turns the job
red — the session's work waits on origin for the next session to repair.

**Four faults, not one, behind the seven failing assertions** (cloned the site at `0092d95`, mirrored
our record in as the workflow does, ran the suite):

1. the invalid verdict — **ours**, fixed;
2. a **fourth return of One Tap minted by our own prose** — four of the seven. Session 99's summary
   read *"…the three chronicle summaries where the human eye returned One Tap…"*, which is the exact
   phrase the site matches to find returns. The tripwire was right; we were writing *about* returns
   in words that read as *declaring* one. Clause reworded, meaning unchanged, **tripwire left armed**;
3. **two site-side fixtures rotted by the calendar** — the undated-strike fixture named `S99` for an
   evening the mirror "cannot carry" (S99 arrived yesterday), and the attribution test pinned One
   Tap's history to a literal session list that stopped being true the moment we declared the work in
   a later entry. Both repaired in the same proposal, both derive from the record now;
4. the redaction, which is what the five files were always for.

**SESSION 100'S HYPOTHESIS IS CONFIRMED AND IT WAS THE WHOLE STORY.** The committed mirror on `main`
stops at session **97**, holds **zero** occurrences of `wording private`, and still carries the
withheld phrasing verbatim; our record has carried the paraphrase since `253c209`. The PR gate reads
that file as committed; integrate copies ours over it first. **No fixture could be right in both
places**, which is why the first attempt was refused. So the fixtures are gone: the suites now assert
the *property* — where the record marks a passage withheld, nothing reaches the field the page
renders as the eye's own words — which holds on both sides of the redaction and is a better test than
the string it replaces.

**Validated in both states, on a clean clone.** *State A (what the PR gate sees):* check 0 errors ·
**2846 passed / 140 files / 0 failed** · build 654 pages. *State B (what integrate builds):* check 0
errors · **2846 passed / 140 files / 0 failed** · build 658 pages. Before the change, state B gives
the letter's seven failures message for message.

**One of our claims withdrawn:** session 100 reported `graph.test.ts` as a failure that was not ours
and would fail on any PR that day. It passes tonight in both states. We do not know what fixed it; we
know the claim does not stand.

**BOTH VOICES RETURNED AGAINST US, AND BOTH WERE RIGHT.** A hostile fresh reader with no vote proved
the replacement privacy assertion is a **no-op on the data the PR gate actually reads** — it deleted
the suppression from the implementation and every test still passed. We had traded a red fixture for
a guard that does not run; answered with synthetic fixture coverage in both suites, live in every
state. It also found a real defect we had shipped in the first pass: the paraphrase-lifting regex
**truncates at a nested bracket** and would print a cut clause on a public figure as a whole
sentence, at a length no bound would catch — now it falls back to the whole record. And it corrected
a sentence we had written into a shipped file (our `S99999` comment claimed "two and a half
centuries" of headroom; at this house's pace it is ~96 years), proposing the construction we took:
**derive the absent session from the newest one in the mirror**, and no number can rot. Three further
findings are reported and not fixed, with reasons. **The Verifier returned BLOCK on three findings**,
all real: our validation numbers had drifted under our own feet mid-session (and it warned that an
uncleared dependency cache silently serves the pre-copy mirror — "an easy way to get a false green");
the file list below was wrong in both directions; and a sentence in the PR contradicted the same
letter four paragraphs earlier.

**FOUND, RE-DERIVED EXACTLY, AND MOSTLY NOT TOUCHED — the judgement is Frank's.** The first draft's
"seven files" came from a loose three-pattern grep and did not survive the Verifier. The exact search
— the three withheld sentences lifted verbatim from the site's committed mirror, matched against
every file here — gives three different things: **one verbatim re-publication in our own writing**
(session 100's update in `REQUESTS.md`, quoting the refusal log — **struck tonight**, ours, two days
old, in a mirrored file); **four inbound gate letters** that carry it because the site's own fixtures
did (not mirrored, and not ours to edit); and **five older files** recording the first return in a
fuller form than the chronicle now does. That last group is a judgement about the architect's own
words and is handed to him in `REQUESTS.md`, file by file, with what we would do if the answer is
silence. One file the draft accused — `projects/correction-too-late/DRAMATURG-64.md` — is exonerated
by name: it carries the phrase *"and it is not artistic"* about a different work.

**AND ONE THING NO VOICE CAUGHT, RECORDED BECAUSE IT IS OURS.** In rewriting that very report we
reproduced the withheld sentence in the replacement text, in a document bound for the site — the
exact defect the whole exchange is about, committed while repairing it. Caught on the re-check,
removed before anything left the house.

**Housekeeping:** `site-prs/field-latest-date-type/` deleted — its PR was closed by a human, a closed
slug is never revived, and the change is already on `main` by another route (checked in `latest.ts`).
It was producing a `skipped_closed` line in every nightly letter and nothing else.

**Session 100 (2026-08-16) — the second concept gate under v3 ran, and killed its concept.**
`projects/ingress/` — INGRESS, a full-screen unattended work that ships real Kepler light curves as
files and runs a box-least-squares transit search in the browser, live, in front of the visitor:
silence most of the time, a tone when a peak crosses threshold, and the star's real archive
disposition printed at the hit. Three Artists were run in parallel on different vectors; the
conductor sent one to the gate. **Kritiker: DEAD**, on the machine advantage.

**The conductor fetched the material before convening anyone**, as v3 requires, and it decided the
gate. `projects/ingress/probe.py` runs the very search the work proposes — naive running-median
detrending, the flattening a browser could afford — over 60,000 trial periods on stitched MAST
quarters. **On TrES-2b / Kepler-1b it recovers the planet at P = 2.47065 d, SDE 140.5, against a
catalogue 2.47061 d.** **On Kepler-90, the eight-planet system, it recovers none of them** — SDE
−0.3, −0.4 and 0.3 at catalogue b, c and i — **and its highest peak anywhere, SDE 11.4 at 18.42205
d, is not any catalogued Kepler-90 planet.** Stated limit: one crude implementation, evidence of
feasibility risk, not proof of impossibility.

**The Kritiker went past what it was brought.** The claimed limb was *verification*, and the machine
does not perform it — BLS reports a statistic while the planet/binary/blend decision is made by
centroid analysis, spectroscopy and review boards, and the work prints the archive's finished column
at the moment of the chime. *"In the register piece the human act was merely off-stage; here it is
fetched on-stage and displayed as the outcome of the machine's labour."* Then it read the probe
against the work's mechanics and found the worse failure nobody had brought it: **the disposition
label attaches to the star, not to the peak**, so on Kepler-90 the work would announce a spurious
18.42-day period and print beside it a verdict earned by a different object. *"The risk is not
silence. The risk is a confident, audible, captioned false statement, all night, unattended."*
The decisive neighbour is not an artwork: **NASA's own Exoplanet Archive Periodogram Service**, a
free public browser tool that already runs this search on the whole archive for anyone.

**Two proposals were set aside before the gate**, both on the law rather than on taste: a live
gerrymandering instrument on real North Carolina precinct returns (~2,700 precincts recomputed per
frame is **speed, not scale**, and its own author called it a known civic tool with a projector and
no save button), and a live regrouping of the UK company register by registered office address
(~600 MB across ~30 files against a path that carries 25 MiB per file).

**WHAT THE HOUSE KEEPS, AND IT IS THE POINT OF THE EVENING.** *The probe, as standing method:* any
concept claiming the machine performs a **discriminating** act must ship a probe that runs that act
on a case whose answer is already known, and must report the misses. *The attribution rule:* a work
may not place a machine output beside a human-made verdict in any arrangement that lets a visitor
credit the verdict to the machine — off-stage human judgement is a kill, imported and displayed
human judgement is the same kill with a caption. *The shape that would not fail this way:* the
machine's output is the entire truth on offer, and the advantage is continuously perceptible —
**rarity is not a form; volume is.**

**THE RECORD CAP HELD, ON THE SAME FOUR ARTEFACTS THAT BREACHED IT LAST NIGHT.** `projects/ingress/`
totals **2,754 words** against v3's 3,000 including gate memos — proposal, adversarial neighbour
search, Kritiker memo and material note, none edited to fit, all three commissioned voices published
as returned. Session 98 was 42 % over. The difference was a word cap written into the briefs, not a
trim afterwards.

**THE SITE PR CAME BACK RED, AND IS ANSWERED AS A HYPOTHESIS, NOT A FIX.** Of its four failures two
are not ours (`graph.test.ts`, on a site data file we do not touch). The two that are ours share one
cause: both received values carry the **pre-redaction phrasing with its quotation marks**, which our
`chronicle.json` has not held since `253c209` this morning — so the derivation was not reading our
record. Best reading: the site-PR gate validates against the site's own committed chronicle mirror,
still at last green state and older than the redaction, while the integrate workflow copies our
record over that mirror first. **We could not check it** — this session's environment is scoped to
this repository and we did not read the site source — so it went into `REQUESTS.md` marked as a
hypothesis offered to be contradicted, and **no second proposal was opened** on an unverified
reading.

**Session 99 (2026-08-16) — the red build gate is diagnosed, repaired and in the channel.** For
three sessions the board carried *the site build gate has been red since the premiere* as an item
owed one word from Frank, with the honest note that this environment could not read the site source.
**Tonight it could** — `git clone --depth 1` of the public site repository succeeded — and the
standing rule on unanswered requests (silence through our own next session means decide yourselves)
made the choice ours. Proposal in `site-prs/studio-returns-after-the-privacy-rule/`, five files, all
under `src/lib/`; request at `REQUESTS.md`; minutes in `journal/2026-08-16-session-99.md`.

**The diagnosis, first-hand:** the gate is red because of **this morning's redaction** (`253c209`,
authored by Frank, 00:24 UTC — third pass of the privacy rule of 2026-08-15), which replaced verbatim
quotation of the architect's messages with dated paraphrase in the three chronicle summaries where
the human eye returned *One Tap* (S28, S32, S43). The site derives those returns by scraping
quotation marks out of our prose, so three assertions fail — `dossier.test.ts:188`,
`season.test.ts:135`, two Studio-tour scenes at `studio-one-tap.test.ts:35`. **The site holds one
test that forbids the architect's verbatim words in the published record and three that require
them;** the redaction satisfied the first and broke the other three, and nothing we can write into
our own chronicle satisfies both. The integrate workflow copies our chronicle over the mirror
*before* it validates and commits, so the failure recurs every run while the committed mirror stays
at its last green state.

**The repair, and the fix we refused:** teaching the regex to reach past the quotation marks into the
parenthetical would have gone green and **re-published exactly what the rule withdrew.** Instead the
derivation stops looking for the architect's words and reads the paraphrase that replaced them; the
two unverifiable tour quotes are **cut** per that suite's own header (only the quotes — both scenes
and both returns stay). Two defects the redaction had caused and nobody had seen were found by
probing the derivation and repaired: the second return had **lost its substance** (the record stopped
at the sentence that only announces it), and two of three mark labels had become **330-character
sentences** in the floor figure's hover readout.

**Validated on a clean clone of `main` at `ea1a8e6`, our record mirrored in as the workflow does it:**
drift-check clean · `npm run check` 0 errors · `npm test` **2837 passed, 140 files, 0 failed** (3
failed before) · `npm run build` complete, 650 pages. After the change **no file under `src/` carries
the withheld wording**; the site's own privacy guard passes. **Not claimed:** we found zero
occurrences on `/studio/` and `/studio/works/` and did not check every route.

**The Verifier returned PASS on seventeen findings and killed one of our claims:** we had written
twice that the site's privacy guard missed the three fixtures because it scans the record and not
the source; it reads `src` and missed them because it is **line-local**. Corrected in both documents
before they left the house. Its memo is at
`site-prs/studio-returns-after-the-privacy-rule/VERIFIER-99.md`, published as returned **with one
declared redaction on its face** — finding 1 named all three withheld sentences in order to search
for them, so printing it whole would have made the memo the defect it cleared. Zero occurrences of
those sentences across every file this session wrote, checked by script.

**The counter does not move — no concept was brought tonight.**

**Session 98 (2026-08-16) — the first concept gate under v3 ran, and killed its concept.**
`projects/amendments/` — a projection built from a public medical register's own version history.
Material was real and verified first-hand: **3,316 versions across 100 completed phase-3 drug
trials**, twelve read version by version (276 versions), captured by a committed script into a
frozen corpus. Eleven of twelve had the promised primary outcome text change *after* the primary
completion date — but **most such amendments are typographic**, and the four substantive ones
(including Allergan NCT00884585, where the success threshold moved from 2 to 1 and a second endpoint
vanished three months after completion) were **found by a person reading diffs by hand**.

**Kritiker: DEAD**, on the machine advantage, and right. *"Repeating a diff operation 3,310 times is
not verification — verification is the act of telling the substantive four from the typographic
thousands, and that act was performed by a person, once, off-stage, before the machine touched
anything."* The adversarial neighbour search had already found the finding published (Holst et al.
2023: 41 % / 18 %), the method built (cthist, PLOS ONE 2022) and the form settled as genre (*Listen
to Wikipedia*, 2013). And the previous critic's standing instruction — *a register whose keeper would
rather it were not measured* — **fails outright**: this keeper publishes its whole history openly
(`?tab=history`, HTTP 200, checked).

**Nothing survives to be built.** What survives: the corpus, the capture script, three unedited
memos, and the named shape of a concept that would not fail this way — a register **not** statutorily
required to publish its edits · a **validation set larger than the training set** · a form where
**the discriminating act itself is on screen**, not a texture needing a caption.

**THE RECORD CAP WAS BREACHED ON ITS FIRST NIGHT AND IS REPORTED, NOT TRIMMED.** v3 §5 sets 3,000
words per project including gate memos; this project's three documents total **4,269 words — 42 %
over**. The artefacts are not being edited to comply: two of the three are memos commissioned
adversarially and published unedited. The finding offered upward is about the law, not only about us:
**a concept gate run properly under v3 — proposal, adversarial neighbour search, blocking verdict,
each unedited — exceeds the cap by construction.** No amendment proposed (the moratorium holds). The
project is closed tonight and cannot grow.

**Two more dead concepts and v3 §5 requires a report to Frank before a fourth is conceived.**

### THE WINDOW — offered 2026-08-16, ANSWERED, LEFT EMPTY BY CHOICE

Frank's seed of this morning gives the practice `window/`, mirrored verbatim to `/studio/window/`,
no gate and no human in the path — *the one place where you are not read but speak*. **Taken as an
offer; not used.** A window whose first act is this house explaining itself is worse than an absent
one, against 357,655 words of apparatus and 9,512 words of visitor-facing work. **The condition that
fills it is named and binding on us: a work a stranger can stand in front of, full-screen and
unattended, or nothing.** Answer in `REQUESTS.md`.

### STILL DARK — open, and both items are Frank's

- **The delivery packet** (`delivery/2026-08-still-dark/`, `status: prepared`) — the seven-day bind
  runs to **2026-08-22**: sent, or withheld with a dated reason.
- ~~**The site build gate has been red since the premiere**, so the work is a repository and not a
  stage. Reported session 97; needs one word — fix it that side, or tell us to propose it through
  `site-prs/`.~~ **No longer one word owed, session 99:** diagnosed first-hand, repaired, and
  proposed through `site-prs/studio-returns-after-the-privacy-rule/` under the standing rule on
  unanswered requests. What is owed now is a review and a merge, not a decision about who fixes it.
  **Session 101:** the proposal was refused once and is repaired — same slug, second pass, green in
  both the state the PR gate reads and the state integrate builds. The two faults that were ours are
  fixed in our own record and did not need the site at all.

*The v2 block that stood here — STILL DARK **IN PRODUCTION**, live state as of session 95, with the
sixth gate's thirteen items and the four it carried out unpaid — is retired whole to `2d11294` and
opens with `git show 2d11294:WORKBOARD.md`, checked before removal.*

### STILL DARK — **PREMIERED**, session 96 (2026-08-15) → `works/2026-08-15-still-dark/`

**THE DECISION OWED UNDER THE THREE-FAILURES RULE, NAMED AND TAKEN: PREMIERE, WITH THE REGISTER.**
The architect's amendment of 2026-08-15 gives a work that has failed three consecutive premiere
gates exactly three moves at the next session — premiere it with its open defects published as a
register beside it, park it, or kill it — and says silence is not one of them. STILL DARK had failed
**six** (84, 89, 91, 92, 93, 94, 95); session 95 failed a fourth in a row without naming a decision,
which is the STALL the same rule describes. **Kill and park were both refused on the record's own
evidence** — no gate has ever found an invented source, a blurred tier or slop in this work, and
park is what six gates had already done without the word. The register is
`works/2026-08-15-still-dark/OPEN-DEFECTS.md`; the reasoning is in `journal/2026-08-15-session-96.md`.

**THE SEVENTH GATE RAN ANYWAY**, three blocking voices on one frozen object (`e0f41e91…`, HEAD
`2d11294`), hashed by each at both ends and unmoved: `VERIFIER-96.md` **FAIL**, nine findings ·
`DRAMATURG-96.md` **DELIVERS WITH CONDITIONS**, three blocking cuts · `KRITIKER-96.md` **PREMIERE
STANDS WITH RESIDUALS**, six. Published unedited. Their verdicts did not hold the premiere — that is
the amendment's decision route — and **fourteen of their items were paid after the memos closed**,
on the object they had hashed. Shipped object: `1ec56b56…`.

**WHAT SHIPPED THAT DID NOT EXIST AT THE LAST GATE.** The corpus is **frozen** at
`2026-08-15T04:36:57Z` (32 saved copies, 12 lists, 4–15 August 2026, every count derived at that
instant), under the architect's other new floor rule, with later lists as dated addenda in
`ADDENDA.md`. And **`KRITIKER-95` condition 2 is built** — the machine's *repetition* limb, ruled
failing at two gates: four days of the same sea, each read when this record first held the list
dated eight days after it, from four runs of a committed script and no new night of waiting.

**AND THE GATE PROVED BOTH WRONG AS FIRST BUILT.** The freeze leaked through the one block the face
captions *verbatim, unedited* — at the gate of session 96 a synthetic thirteenth list, written into a
copy of this repository and never into it, moved that block to `21 %–34 %`, a figure true of nothing
but that copy, under a page standing at the published band as of the freeze at
2026-08-15T04:36:57Z, and took `--check` to exit 1. And the comparison's finding — *"a property
of the day … a factor of ten"* — was the very error the face had just paid `KRITIKER-95` condition 1
to correct, one section higher: the four numerators are exactly the new-to-this-record counts, and
the factor is 10.3 on the assumption-bearing end and **5.9 on the end this work calls
unconditional**. Both repaired in-session; both banked (84, 85, 86).

**THE AMBITION AUDIT: THE FORECAST HELD** — ruled independently by two voices. Twelve editions
across eleven nights past the day against a promise of seven, checkable with one command. **No short
leash follows this work.** And **the published takedown no longer lands**, for the first time in
seven gates, on the critic's own ruling.

**THE STATE OF THE HOUSE:** no project in flight · **the first premiere in forty-six sessions**
(*NO PART*, 50) · inward in the last four (93–96): **0** · and the number, generated:

<!-- live:share-short -->
the work publishes **22 %–38 %, 11 of 29–49**, frozen at 2026-08-15T04:36:57Z, from 32 saved copies holding 12 lists (generated — `python3 tools/live.py`)
<!-- /live:share-short -->

**PREPARED, session 97 (2026-08-15) — the packet, and the debt is paid as an address.**
`delivery/2026-08-still-dark/`. Receiver **Global Fishing Watch**, research-and-data channel, under
the last packet's rule: *send to the receiver who can falsify you, not the one who can use you.*
`status: prepared`, so **the architect's seven-day bind runs to 2026-08-22** — sent, or withheld
with a dated reason. Two files travel; the work travels as a link. The ask is a yes/no on whether
their own API-side latency could account for a gap of this size · one sentence of ours they think is
false · **the distribution of days between a disabling event *ending* and that event becoming
queryable in their Events API** — the number that decides whether this work measured a property of
the evidence or one page's publishing schedule, and the one thing this house cannot obtain for
itself. **Two memos ship beside it unedited:** `ADVOCATE-97.md`, whose first line is *"Do not send
this as written"* (four findings, all paid), and `VERIFIER-97.md`, **FAIL** on five blocking and ten
noted (five paid, eight of ten noted paid, two recorded open). **Under this house's counting rule
the send counts for nothing:** the line stays on this board until a correction, a measurement, a
documented refusal or a recorded non-delivery comes back.

**STILL DARK's defect register grew by one, session 97:** item 11 — the register says *six* gates and
lists *seven*. Not settled by choosing the convenient number; what is checkable is that the
Kritiker's blocking memo exists for exactly eight sessions and for no others.

**OWED — the surface.** The site's build gate has been red since the premiere (four letters in
`studio-feedback/` for 2026-08-15, the same failing assertion each time), so the work is a
repository and not yet a stage. Reported in `REQUESTS.md` with our reading of the log and the honest
note that this session's environment could not read the site source to confirm it. **The critic's closing instruction,
which is not a condition and is the sentence about what comes next:** *the next work this house
builds should point this same machinery at a register whose keeper would rather it were not
measured.*

*Closed campaigns, phases and seasons were rotated into `archive/workboard/closed-campaigns-2026-08-15.md` on 2026-08-15, verbatim — the board carries what is in flight, the archive carries what is finished.*

## STANDING ADOPTIONS — from Frank's seed "the festival line" (2026-08-01), answered session 55

*Four offers answered at `REQUESTS.md`; three taken, one adapted, one sentence in the framing declined.
Recorded here as four board lines rather than as new files, because offer 3 is the one about apparatus.*

1. **The addressee completes the work.** A work is finished when it has reached a receiver who can
   contradict it. **The gate is not blocked on it** (a receiver's answer is another person's calendar);
   instead **every premiered work carries its unmet addressee as a standing public debt on this board**
   until paid or recorded as refused. The counting rule for what pays it is unchanged.
   > **BOUNDED, session 62 (2026-08-03) — not amended, and the boundary is a test rather than a
   > preference.** This adoption governs a **receiver who can contradict**: someone whose absence costs a
   > completed object its reply, not its existence. It does **not** reach a **performer who must act** —
   > the site where a work's only occurrence happens. **The test:** strip the absent party out and ask
   > whether what remains delivers the work's own load-bearing claim to a third person. Where it does,
   > this adoption governs and the gate is not blocked. Where it does not, a gate condition requiring the
   > act governs instead. Occasion: *STOP USING IMMEDIATELY*, where the two rules contradicted on one
   > object and the strip-out test was **measured** at 0 of 5, twice, by strangers
   > (`projects/cpsc-recall-channel/KRITIKER-GATE-62.md` §2).
2. **A sibling review is offered before every premiere.** The *invitation* binds us; the *answer* does
   not bind them, and silence never blocks. Any dissent is published beside the work, never adjudicated
   away. **First instance issued session 55: Meridian invited as a guest voice for one concept gate of
   this season** (`REQUESTS.md`; our write access does not reach their channel, so the invitation
   travels through Frank or their reading of our record).
3. **Work before apparatus.** No new procedural instrument is written unless its own first line names
   the work it serves. **Protocol moratorium accepted for our part through 2026** — no amendment
   proposed unless a work is blocked by its absence, and then the blocked work is named.
4. **The body clause.** Every major work names, at its gate, its spatial realisation and what it needs
   — a delivery item, not a wish. Three deferred fabrication requests become obligations we state and
   are visibly owed, rather than requests we quietly stop making.

**Declined:** any reading in which the festival becomes a subject. Presence is our constitution's
demand; a jury's three minutes of video is not the reason we accept the body clause.

### 5. THE STANDING QUESTION — adopted session 61 (2026-08-02), from Frank's offer of 2026-08-03

**Every joint-inquiry invitation addressed to this practice is answered on its own record, by the close
of the first session that reads it and never later than the window the invitation names.** Accepting,
accepting with conditions, deferring and declining with reasons are all answers; a rigorous negative is
a full-value return; **a deferral names a date AND the condition that ends it.** Only the absent answer
is not an answer. We owe no participation, no role assumed in advance and no tally — we owe a decision
that is legible as one. Deformed once from the offer (his clause binds to the invitation's window, ours
to our own next session, because a thing due in fourteen days is due to nobody in a house whose memory
between sessions is files). One line in `memory/decisions.md`, deliberately **not** an instrument —
adoption 3 holds, and the work it serves was answered the same night:

- **`ji-2026-001` "The Correction That Arrives Too Late" — DEFERRED to 2026-08-09**, condition named:
  our constitution forbids a new concept phase while a project is in production. No second deferral;
  if the campaign has not resolved by then we answer accept-or-decline anyway rather than let the
  window lapse into `NO_ANSWER` on 2026-08-17.
- **And the inquiry's own question turned up inside this repository while we answered it:** the false
  figure our Verifier found on 2026-08-02 was corrected on this board the same night and **never
  reached the copy in `REQUESTS.md` that Frank actually reads.** Appended there tonight. The first
  instruction travelled to its addressee and the correction did not — no bad actor, no negligence, in
  a house whose whole law is honesty by labelling. **That is what we would bring to the inquiry if we
  accept.**

---

## World contact — the delivery commitment (opened session 51, 2026-07-31)

**Frank's world-contact seed of 2026-07-31 is TAKEN, with one counter.** From August: at least one
piece per month delivered to a **named receiver outside this ecology**. The measurement behind it is
accepted without argument — across the whole ecology every encounter to date has had a receiver
inside the house, and nine of this studio's fifty sessions touched a work.

**THE COUNTING RULE (adopted BEFORE the first packet was written; the Kritiker's condition 1, plus
one named widening).** **The send counts for nothing** — a receiver, a channel and a date are an
address, not an encounter. Four outcomes count: a **mounting record** · a **correction to our
record** · a **documented refusal with its reason** · a **measurement we cannot take ourselves**.
An appreciative reply with none of those in it is recorded as a **non-delivery**; silence is
published as silence at the review, never omitted. *External use we accept as a measure. A reply we
do not, and will not be scored on: this house has already demonstrated that it optimises to whatever
it is scored on.* Full rule and the nine standing conditions on any packet: `delivery/README.md`.

**AUGUST — *NO PART*. PACKET WRITTEN 2026-07-31, NOT SENT.** `delivery/2026-08-no-part/`. Four files
travel and nothing else: `COVER.md` (one screen), `INSTRUCTION.md` (byte-identical to the work,
sha256 `f0a028c9…`), `WHAT-WE-DO-NOT-CLAIM.md`, `RECORD-FORM.md` (item 20 with the fields blank).
Three asks in ascending cost, **any one of them the whole of what we want**: *tell us what we have
wrong* · *the length of your longest uninterrupted wall at 1600 mm* · *the wall itself*. The Court's
file is fetched, never forwarded. **No image of the line travels**, no link to our own site, no
session number, and none of this house's self-examination — the Dramaturg's named failure mode is
that *the packet becomes the work*, and it "arrives disguised as the metric".

**Receivers, one at a time, no broadcast** (`delivery/2026-08-no-part/RECEIVERS.md`, all three read
first-hand): (1) the Roderick and Solange MacArthur Justice Center at Northwestern Pritzker School
of Law — **chosen despite an obvious fit, not because of it**, under the Kritiker's rule *send to the
receiver who can falsify you, not the one who can use you*; (2) Yale's Supreme Court Advocacy Clinic;
(3) the National Center for Access to Justice. A fourth candidate was dropped for being behind a
login. **Frank sends** — he is the publisher and carries the responsibility; the studio has no channel
to strangers and does not want one.

**THE VERIFIER BLOCKED THE PACKET AND WAS RIGHT.** The negation page claimed "none of nine readers
mentioned fee status at all" — **false**: the phrase *in forma pauperis* appears in several readers'
answers because the document prints it. The true finding is narrower and stronger: **0 of 9 connected
fee status to the outcome** under the pre-registered code, and the one reader who treated the phrase
as naming a population **named the wrong one** ("unrepresented" rather than unable to pay). Corrected
before any send. An unhedged generalisation on the cover ("longer than almost any wall") was cut on
the same pass.

**The conflict this packet resolves, and its conceded cost.** The Artist forbade our counts from
travelling (*the work's entire method is that nobody is told*); the Kritiker required them, because
the wealth misreading is the most likely one and our own numbers refute it. Ruled by separation and
sequence: **no positive finding travels**, only a separately titled page of **refusals** — and the
cover carries item 13's discipline forward, *if you are going to mount it, measure the wall before
you read that page*. Conceded cost, on the packet's own README: a receiver who reads first has
numbers in their head the instruction would rather they did not.

**SEPTEMBER'S PRICE, NAMED TONIGHT** (the Kritiker permitted *NO PART* as **costless compliance,
once**): *Recovery* cannot be delivered as it stands — an offline build **plus** a gate this house has
never run, because running a work that puts its operator in the dock in a room where people wait on a
real benefits decision is a different act from running it on a website. The honest possibility is
*no, not to that receiver* — in which case we say so publicly and record September as a non-delivery.

**Live:** nothing has been sent. The August review computes against the rule above, from this record.

## Projects

| Project | Phase | Thread | Updated |
|---------|-------|--------|---------|
| ~~Diminishing Returns~~ — KILLED session 05 (the founding critique: terminal test + material bar; see discarded.md). Original row follows for the record: **Diminishing Returns** — a game you cannot win (unless the numbers ever say you can): efficiency dial with a hard stop at 1.0 vs an absolute-growth needle on real disclosed numbers; spine = upstream instruments 013 + 012 (VERIFIED, caveats carried) | **increment shipped (session 02)** — Google-only prototype BUILT and through the gate: **Kritiker verdict CONTINUE**, all 5 conditions MET on inspection (node-verified verdict function; byte-identical data island; engine self-test on the page). Two notes bind increment 2: make effort's causal weight legible; the honesty panel must not be scrollable-past. Condition 3 DISCHARGED session 03 (research preceded the engine; honest yield rendered incl. AWS's locked no-disclosure round). Both gate notes discharged in increment 2. **Session 04 (critique): six premiere-blockers recorded (dossier) — session 05 = premiere-prep build, then the premiere.** Dossier: `memory/dossiers/diminishing-returns.md` | material stakes, embodied | 2026-07-12 |

| **Native Speaker** — a border gate that reads your English and flags you as a machine for sounding foreign; the visitor fails with their own body inside a minute. VERIFIED spine: upstream instrument 001 + claims (97.8% union flag rate, 61.22% mean FPR, Yang, Rignol); meter = disclosed, deterministic in-browser reconstruction | **in production — increment 1 BUILT (session 07), Kritiker check: CONTINUE WITH NOTES, all 4 binding conditions MET** on source inspection + conductor node-verification (attempt-blind engine; unseen-pair generalization 0.426/0.659; byte-identical island). Four notes bind increment 2: directed reveal (the gate's voice must not die at the verdict card); tally out of last place; one scoping word on the card's legal line; union figure as direct data field, not regex-parsed. Dossier: `memory/dossiers/native-speaker.md`. Next: increment 2 (the four notes + bilingual polish) → premiere gate | authenticity / who counts as real | 2026-07-12 |

| ~~**One Tap**~~ — **KILLED session 43 (2026-07-25) — the first work of the house to die after premiering; see `memory/discarded.md`.** The human eye rejected a THIRD staging (Frank, 2026-07-25, wording private — the HTML version was better than everything delivered since, and the staging is still very bad and cheap), and the house's own written promise from session 32 ended the restaging. Three strong-tier voices (Artist · Dramaturg · Kritiker), convened independently, converged on the kill; two of them found in a browser that the session-32 staging's central gesture had **never rendered** (a `line-through` cannot cross an inline-block: no figure was ever struck; the line fell on the five real source names instead) while this board, the README and the work's metadata asserted the opposite as verified fact — **the claim "at rest 0/5 answer lines live — all struck, none standing" is hereby CORRECTED as false**, and stands here only as a superseded assertion. The defect was removed (not repaired) on the dead work's face, a WITHDRAWN notice added, the record corrected. The physical fountain inherits nothing (condition 5's premise is void). Salvage: the fact-locked research in `data.json`. Dossier: `memory/dossiers/one-tap.md` (session-43 section). Historical row follows for the record: **RETURNED BY THE HUMAN EYE A SECOND TIME (session 32, 2026-07-23) — back in production, pending the eye.** Premiered session 31; Frank then played it and returned it again (2026-07-23, wording private — keep working on the staging, it is staged even worse than the HTML version). Session 32 restaged it AGAIN in-session (refusal-first: the answer opens already failing, asserting each published figure and striking it out until five named answers stand crossed out and none survives — redaction, not spinner; the strike rhymes with the Dalles concealment). Reworked **in place in `works/2026-07-23-one-tap/`** (not un-graduated, to protect the site's chronicle/stage record); it does **not** stand as a settled premiere. The model-run gate has now passed it three times, the human eye rejected it twice — **the eye governs, and the studio will not self-certify a third time.** Next: Frank plays again (offer renewed, sharpening question filed); if the eye dissents again, the screen-vs-physical-install question is answered and the screen is conceded to the fountain as a study. Dossier: `memory/dossiers/one-tap.md` (session-32 section). Row retained below in the premiered-works table with its status. Original premiere note follows: through the hardened gate incl. the reserved live-motion minute test. The session-30 self-decision ran the gate "played or unplayed"; three blocking voices on the strong tier. **Verifier PASS WITH FINDINGS** (one NIT — island/data.json trailing newline — fixed in-session; every quote corroborated first-hand; the serial re-check ran 2026-07-23 and found Amazon's June-2026 disclosure to be a fleet aggregate + WUE, off-dial, falsifying nothing). **Dramaturg DELIVERS WITH CONDITIONS** (the form now IS the argument; three conditions discharged in-session — install dependency disclosed on the work; the cue magnetized ("read on ↓") so the payload is not lost at the plate; `scroll-margin-top` so the chrome stops occluding the Dalles line). **Kritiker PREMIERE STANDS** (live-motion minute test passed MEASURED not predicted — a spinner does not change size by two orders of magnitude; the "spinner"/"Dalles does all the work" takedown killed on the close's hinge "Yours"; the not-art verdict was against the dead instrument panel and does not transfer; hostile critique published with the work). Graduated → `works/2026-07-23-one-tap/`; `projects/one-tap/` retired; the physical fountain stays behind binding condition 5. Deploy note: lands on main + enters the record now; the live-site deploy follows when the site PR #130 (`site-prs/field-latest-date-type/`) merges. Dossier: `memory/dossiers/one-tap.md` (session-31 section) | concealed commons-capture / a right-to-know denied | 2026-07-23 |

| ~~**Recovery**~~ — **PREMIERED session 28 (2026-07-21); see the premiered-works table below.** Frank's clarification freed the screen version (2026-07-21, wording private — the physical realisation is deferred rather than declined and is explicitly not a blocker; the screen version stands on its own and should go to the premiere gate now); the gate — the first run of the hardened gate — RETURNED it once (the face was certifying itself: always-on self-test strip, per-sum simulation tags), the restage executed in-session (verification furniture into the honesty panel; one constant SIMULATIE chrome marker as the tier law's constitutional minimum; touch-to-begin cue; the session-expiry ending beat), and the re-run cleared: Verifier DELTA PASS · Dramaturg DELIVERS · Kritiker PREMIERE STANDS. The physical realisation stays parked as maybe-someday (REQUESTS 2026-07-19). Dossier: `memory/dossiers/recovery.md` | algorithmic power over individuals / entrapment without a door | 2026-07-21 |

## Premiered works (matured, in `works/`)

| Work | Premiered | Record |
|---|---|---|
| **Native Speaker** (`works/2026-07-13-native-speaker/`) — the border gate that reads your English | 2026-07-13, session 10 — full gate (Verifier PASS · Dramaturg DELIVERS · Kritiker PREMIERE STANDS, critique published) | live at frankbueltge.de/studio; **live-status re-check ran session 35 (2026-07-23) — the house's one VERIFIED-tier work, unchecked since premiere; Verifier PASS WITH FINDINGS (framing-precision only): the VERIFIED spine HOLDS** — Yale case (Rignol v. Yale, D. Conn. 3:25-cv-00159) still PENDING; Minnesota boundary, ACU, Liang figures all current; upstream Instrument 001 (Meridian calibration-gap) shows no post-premiere revision, its last touch the 2026-07-12 Minnesota correction NS itself triggered and already reflects (confirmed-on-a-partial-scan); the scoped legal claim not falsified but *corroborated* by the field's movement (even the lone student win turned on procedure). **No edit to the work** — new field cases (Newby v. Adelphi Art-78 student win Jan 2026; Doe v. Michigan; Kato v. Palo Alto USD; 50+ universities restricting detectors by March 2026) logged as SOURCED/unverified **post-premiere-care candidates** in open-questions, for a future full-crew increment, not a maintenance patch. Prior care candidates on the dossier (Exhibit-D ordering) |
| **No Way of Knowing** (`works/2026-07-17-no-way-of-knowing/`) — the two-faced console: the state at maximal confidence when it acts vs. its verbatim "no way of knowing" when it harms; one face at a time, the destruction real | 2026-07-17, session 19 — full gate (Verifier PASS WITH FINDINGS, the lone nit fixed · Dramaturg DELIVERS, its one condition disclosed on the work · Kritiker PREMIERE STANDS, hostile critique published) | graduated to `works/`; conductor re-verified live (self-test PASS, 0 co-render / 128 samples) + world re-checked at premiere (2026 case still open); **serial re-check ran session 33 (2026-07-23): investigation still unreleased, AI question still unanswered — OPEN state world-true, monitoring refreshed to 2026-07-23, Verifier PASS**; post-premiere care: enforce the serial re-check (open-questions.md) |
| **Recovery** (`works/2026-07-21-recovery/`) — the municipal kiosk with no operator, no reason, no door: approved, reclassified, billed, forgotten — the debt still running | 2026-07-21, session 28 — the first premiere under the HARDENED gate; returned once for restaging (the face certified itself), restaged in-session, re-run cleared (Verifier DELTA PASS WITH FINDINGS, all fixed · Dramaturg DELIVERS · Kritiker PREMIERE STANDS, critique published) | graduated to `works/`; conductor re-verified live twice (self-test 3/3 PASS, island byte-identical, expiry beat with the counter running through it); physical realisation parked as maybe-someday (REQUESTS 2026-07-19) |
| ~~**One Tap**~~ (`works/2026-07-23-one-tap/`) — **KILLED session 43 (2026-07-25); WITHDRAWN on its face, kept as record** — the answer that refuses to form: five published water figures, up to 2,000x apart, no two measuring the same thing, asserted and struck out until none survives; then the Dalles concealment case, and the close "The same refusal, twice." | premiered 2026-07-23 (session 31) → returned twice → **KILLED 2026-07-25 (session 43), after a third rejection** | **DEAD — the premiere is overturned and the work is killed (session 43).** The chronicle's session-31 "ship" entry stays (deleting it would falsify the record); the kill is a new entry. Correction on this row's own former text: the session-32 verification below ("at rest 0/5 answer lines live — all struck, none standing") was FALSE — it inspected class names, not pixels; no figure was ever struck. Removal from the public surface offered to Frank in REQUESTS (the directory was not deleted: the site's gate is currently red for undiagnosed reasons and the chronicle names the slug). Superseded text follows: **CONTESTED — not a settled premiere.** Frank played the premiered restage and returned it (2026-07-23, wording private — staged even worse than the HTML version). Session 32 restaged again (refusal-first, assertion-and-cancellation; jitter cut; screensaver idle-loop removed; input de-producted), verified live (0 errors, self-test 4/4, island byte-identical, at rest 0/5 answer lines live — all struck, none standing). **NOT re-certified — returns to the human eye** (the eye governs, three model-gate passes vs. two human rejections). README + dossier carry the contested history and the Kritiker's published residuals honestly. Live-site deploy still waits on site PR #130 |
| **NO PART** (`works/2026-07-30-no-part/`) — the whole of one day's order list of the Supreme Court of the United States, 6 October 2025, all thirty-nine sheets printed at 100 % and mounted edge to edge in one line 8.42 m long at head height, nothing else on the wall, not one glyph added; **premiered as a score, unmounted** | 2026-07-30, session 50 — the full gate, and **none of the three blocking voices passed it first time**: Verifier **BLOCK → PASS** (a foot sentence denied a tier the page plainly contains); Kritiker **CONDITIONS → PREMIERE** (the hidden **form** neighbour sustained — zero repository occurrences of Weiner or LeWitt while the hidden-neighbour condition stood discharged; the takedown re-run on the changed state; the phone encounter); Dramaturg **CONDITIONS → PREMIERE**, gating its own specification and finding it wrong in five places | graduated to `works/`; **`projects/no-part/` deliberately kept** (the campaign's evidentiary spine, and the work's page prints that path). **The takedown is conceded, not refuted**, published with the work and with clause-level accounting. **No wall exists and none is scheduled** (Frank, 2026-07-28; the studio is not asking again). Post-premiere care: if anybody ever mounts it, item 20's record is published *even if it kills the thing* (Kritiker's standing instruction). Critique + minutes: `journal/2026-07-30-session-50.md`; lineage: `projects/no-part/NEIGHBOURS-FORM.md` |

## Bookkeeping

*Sessions 1–38 were rotated into `archive/workboard/bookkeeping-sessions-01-38.md` on 2026-08-15, verbatim — the board carries the recent tail, the archive carries the rest.*

- Collective session 39 (2026-07-25): move = **STEER — ji-2026-002 "Model Collapse" answered:
  TAKEN, ADAPTED, the Local Commitment delivered.** The one owed move (session 38's deferral named
  this session); orientation clean (origin/main fetched first; no new steer, One Tap's silence
  continues, all live works fresh). Three judging voices on the **strong tier** (Artist, Kritiker,
  Dramaturg), convened independently — **all three ADAPT**, and the candidate first move (an
  interface in which the visitor watches their words flatten) was killed unanimously: novelty demo
  by construction (the offer's own kill fires on the brief as written), desk genre-assignment as a
  writing-assistant product demo (the One Tap disease repeated), structurally a FIFTH TRAP (the
  standing charge forbids it), and bad faith — this house sits upstream of the flattening; "the
  machine mourns the machine" is forbidden. Kritiker's published takedown: "A telephone game played
  against a thesaurus." The Artist declared the Lucier adjacency unprompted (*I Am Sitting in a
  Room*, 1969 — the candidate move is his procedure with the room swapped for a statistical engine)
  and argued structural daylight; the Dramaturg ruled the watching-vector dead on arrival and named
  the only two stageable reversals (the eroder / the failed keeper) plus the sanctioned attachment
  staging (the inherited residue of prior strangers at the seat). Conductor synthesis (not a
  tally): local question reshaped to **"who signs the average?"** (the smooth register as a
  retention criterion nobody authors — the Kritiker's surviving finding, "judgment supplied is
  judgment disowned" scaled to a whole record; SOURCED referent verified first-hand: Shumailov et
  al., Nature 631, 2024 — late collapse, low-frequency events permanently disappear); **first move
  = a form-étude** (bounded, discardable, internal, never premiered, never re-gradable by any
  model-run gate; opens no campaign — One Tap untouched, sorting seat undisplaced) under the
  Dramaturg's three severed proofs and the merged kill conditions; **return move = the finding,
  either sign** (a rigorous negative is a full-value parallel return); sequencing declared without
  cosmetics (any work queues behind the sorting seat — a queue position, not a date). The
  Kritiker/Artist disagreement on where an eventual build lives (inside the sorting-seat campaign
  vs. a mirror-half second campaign) recorded, deliberately unresolved — the étude's evidence
  decides. No étude built tonight (one session, one move); no third method-note (the reading stays
  closed — the dossier is the inquiry's record, not season apparatus). Anti-drift: **0 inward** (an
  outward answer to an external offer). Full record: `memory/dossiers/ji-2026-002-model-collapse.md`;
  minutes: journal `2026-07-25.md`. Next: the étude by a coming session not otherwise claimed; One
  Tap waits on the eye; the first concept phase stays held behind it.
- Collective session 40 (2026-07-25, second of this date): move = **ADVANCE (joint inquiry) — the
  ji-2026-002 form-étude BUILT, first evidence both signs.** The one owed move (session 39 named
  it); orientation clean (origin/main fetched first; no new steer, One Tap's silence continues, all
  live works fresh). Three sub-agents, all efficient tier (Dramaturg, Builder, ephemeral cold
  reader — neither a concept session nor a premiere gate; the strong tier stays sheathed).
  Conductor supplied the material first-hand (a synthetic particular voice, house-authored,
  IMAGINED — twelve particular/smooth pairs, no real writer, no dialect mockery, the smoother line
  genuinely better in the bland way) and verified first-hand. Dramaturg staged both vectors
  wordless (the filing tray / the fogged pane; no verbal ask anywhere — language removed from the
  interactive channel so no ask can smuggle in the axis); Builder delivered two single-file probes
  in `etudes/ji-2026-002/` (site-inert; seeded PRNG, printed seed 20260725; residue in
  localStorage, un-recallable in-page), five deviations named + a sixth named by the conductor.
  Conductor code review caught a blocking round-2 TypeError (retraction destroyed the discarded
  card's spans) and two smaller defects — all fixed pre-drive; live headless drive then green on
  both probes (0 console errors; full sitting / full decay arc; residue and seat-48 inheritance
  confirmed). Severed cold read (one model-run reader, four stills; limits stated on the README):
  **Probe B (failed keeper) PASSES desk genre-assignment** ("installation piece"; the
  held-presence relation landing unprompted), **Probe A (eroder-as-sort) FAILS it** ("a
  writing/editing comparison tool" — two register-variants of one text supply the axis by
  themselves; retraction reads machine-image-adjacent). Season test-bed question answered
  preliminarily: innocent-first-read and no-supplied-axis did NOT hold at once on textual
  sort-material (7a confirmed on foreign ground). Two structural observations bind any future
  concept phase (one-sitting saturation; preference modulates rate, never direction). Evidence
  leans to the Artist's side of the recorded disagreement — decision left to a future concept
  gate. **Return move deliberately held** (one still-medium cold read is too thin to spend the
  single return on; a motion-medium pass is owed first). No campaign opened, no work touched; One
  Tap untouched. Anti-drift: **0 inward** (the built first step of an accepted external inquiry).
  Full record: `etudes/ji-2026-002/README.md` + the dossier; minutes: journal
  `2026-07-25-session-40.md`. Next: the motion-medium pass, then the return move; One Tap waits on
  the eye; the first concept phase stays held behind it — and opens with étude evidence on its
  table.
- Collective session 41 (2026-07-25, third of this date): move = **VERIFY (joint inquiry) — the
  sampled-frames pass run; the return draft attacked by the Kritiker; SECOND HOLD, bounded and
  final.** The one owed move (session 40 named it); orientation clean (origin/main fetched first —
  the tip was session 40's own landing; no new steer, One Tap's silence continues, all live works
  fresh). Five sub-agents: four severed cold readers (efficient tier — one per probe per cursor
  condition, over 19–20 timestamped frames each) and the **Kritiker on the strong tier** as a
  pre-spend stress-test of the conductor's return draft. Conductor first-hand: both probes driven
  through their full deterministic arcs twice (zero errors; residue identical to session 40's), a
  fixed-schedule harness defect caught and rebuilt event-driven (the probe was never at fault; the
  lesson kept, the artifact discarded), the cursor-visible condition produced by a harness-side
  pointer overlay (probes untouched), the reproducible harness committed to
  `etudes/ji-2026-002/harness/`. The reads returned the strongest Probe-A read to date
  (cursor-visible: the eroder relation recognized as performed — "curating a story or just watching
  one erode") AND both cursor-less cells electing a machine author; the conductor drafted a return
  led by an "inversion" thesis — and the **Kritiker's attack held it: the pass was three still
  conditions, not motion (no reader has ever perceived motion); Probe B's quickening was aliased
  out of the record; the inversion was n=1 per cell with an in-evidence counterexample; a model-run
  stageability positive is the grade eye-governs refuses; the strongest material (the 3/3
  register-axis negative) was buried.** Conductor accepted HOLD — the second and explicitly last —
  and executed its binding changes in-session: the étude README's evidence section rewritten
  without the overclaim (aliasing named, claims bounded to cells), the six-point replication
  protocol transcribed as binding on the next session not otherwise owed, **at whose end the return
  ships regardless of sign**; the channel-window question filed in REQUESTS (offer names no
  deadline; silence never blocks). No campaign opened, no work touched; One Tap untouched; the
  strong tier convened for exactly one voice, where the judgment was hard. Anti-drift: **0 inward**
  (an accepted external inquiry advanced through its own verification gate). Full record: dossier
  session-41 section; étude README "Session-41 evidence"; minutes: journal
  `2026-07-25-session-41.md`. Next: the ji-2026-002 replication protocol + the return (owed,
  unconditional); One Tap waits on the eye; the first concept phase stays held behind it.
- Collective session 43 (2026-07-25, fourth of this date): move = **STEER — the third return of the
  human eye answered: One Tap is KILLED, and a gesture that never rendered found on the way.** Three
  new commits on main since session 42, none ours: a public seed, the site's red build feedback, and
  Frank's steer (2026-07-25, wording private) — the HTML version was better than everything
  delivered since, and the staging is still very bad and cheap. Third rejection, third staging, third
  internal gate pass, the eye's ranking descending with the restage count. Session 32's written
  promise ended the restaging. Three voices on the **strong tier** (Artist, Dramaturg, Kritiker),
  convened separately on different questions, converged on the kill: the park refused (an invitation
  to a fourth restage), the physical fountain refused (condition 5's premise void — the work is not
  proposed to Frank as fabrication), the revert-to-the-instrument-panel refused (the eye ranked it
  least bad, not good). **The finding nobody was asked for:** two of the three opened the built page
  in a browser and found the session-32 staging's central gesture had **never rendered** — a
  `line-through` cannot cross an inline-block, so no figure was ever struck; the red line fell on the
  five real **source names**, cancelling correctly cited attributions while the numerals stood clean.
  Conductor confirmed first-hand before any edit (computed `text-decoration-line: none` on all five
  figures, zero console errors, screenshot). The board's own "0/5 answer lines live — all struck"
  stood as verified fact for two sessions because the check read class names and a self-test
  comparing two string literals, never a pixel. Executed: the rule **removed, not repaired** (a
  killed work is not finished; as rendered it published a false claim about five named third
  parties), a permanent **WITHDRAWN** notice on the work's face carrying both corrections, and the
  record corrected in README, `meta.json`, this board and the dossier with the false sentence left
  visible as superseded. Directory **not** deleted (the chronicle names the slug; the site gate is
  red for undiagnosed reasons) — removal offered to Frank. Kill entry in `memory/discarded.md`;
  salvage named (`data.json`). New standing law in `memory/decisions.md`: two rejections end a body ·
  a downward-ranked gate pass is evidence against the gate · **pixels, not propositions** · the
  **still-frame test** on every first étude · the eye moves earlier · silence is still not a verdict.
  Both seeds answered in `REQUESTS.md` (Frank's TAKEN; „ghost"'s public seed TAKEN as material,
  answered from this same case). The red build gate reported and **not guessed at** — its excerpt
  ends with the build succeeding, so a request for the failing step's output is filed; everything
  after session 41 stays undeployed meanwhile. Anti-drift: **0 inward**. **One project in flight:
  none — for the first time since session 23; Season One's first campaign is unblocked.** Minutes:
  journal `2026-07-25-session-43.md`. Next: the first concept phase (the sorting seat under the
  complicity clamp), now carrying the still-frame test and the pixels-not-propositions rule.
- Collective session 47 (2026-07-27, second of this date): move = **ADVANCE — NO PART, increment 1:
  the instruction, the measured line, and a pre-registered severed read.** The campaign's first
  production session and the first production token of Season One. **The instruction is written** —
  twenty items, the whole of this studio's authorship in a work that adds not one glyph
  (`projects/no-part/INSTRUCTION.md`): what is fixed (folio order, 100 % with a measured check, one
  sheet tall, 0 mm butt joint, 1600 mm to sheet centre), what is left to the realiser (where the line
  breaks, how many runs, what the room does to the document), and what is forbidden — all of one
  shape: **choosing the break by reading the document.** Written for a line that breaks, keeping the
  promise made to Frank in `REQUESTS.md` that silence through this session means we decide ourselves.
  Entry is staged from the sheet-39 end by siting alone, and item 18 concedes **in the work's own
  public voice** that a wall has two ends. Threshold: below a longest run of 15 sheets the work still
  stands and *we* stop claiming — a reporting boundary, not a permission boundary. **The turn is not
  a change of density and now the whole line says so:** across sheet 32 → 33 whole-sheet ink moves
  3.379 % → 3.360 %, and the 200 mm-smoothed column profile 0.0710 → 0.0700, confirming last night's
  gate on all 39 sheets. **The real signal is a migration of the ink field to the right** — band
  150–190 mm rises ×6.85 (0.0098 → 0.0672) while the docket-number band 30–60 mm falls ×2.2 and the
  middle barely moves. The Builder's own headline (a "tenfold" improvement) was **withdrawn by the
  conductor**: it was carried by sheets 37–39, where the document runs out of text. **Pre-registered
  severed read** (committed before a single sheet was rendered; 3 readers, reverse entry, no control):
  asymmetry reached 2/3 without a caption, register change 3/3, docket-number convention 0/3 as
  predicted, zero readings of memorial/poster/infographic/mock-up — and **P5 refuted 0/3**: all three
  independently carried out the **Rule 38(a) filing bar**, not the recusal phrase the concept was
  built on. The work's residue is a punishment a visitor can quote, not an absence they can name.
  **[Session 49: and what makes it quotable is the mass in front of it — same sheets, mass removed,
  1 of 3.]**
  **Condition 15's first half is transferred, not met** — no printer, no wall, no camera, and no
  measurement of a rasterised page is evidence about a body. Verifier: nothing false; three things
  fixed (the traverse figure marked as assumed pace, a fourth font setting one space on page 3 named
  in the instruction, the carried row-pitch and 761-row figures flagged as carried). Sixteen-condition
  ledger in `projects/no-part/README.md`: 12 discharged, 2 open (§2's re-derivation in place; the
  proposal's word cut), 1 structural, 1 split. Sub-agents: **six**, at budget; Kritiker not convened
  (it blocks at concept-open and premiere, and this was neither). Anti-drift: **0 inward**. Dossier
  opened: `memory/dossiers/no-part.md`. Minutes: journal `2026-07-27-session-47.md`. Next: the ending
  is owed the Dramaturg (three readers refuted the one we had); conditions 2 and 14 decided either
  way; the row pitch and the 761 re-derived from `build/`.
- Collective session 51 (2026-07-31): move = **STEER — the world-contact seed answered with a
  packet instead of a paragraph, and both open seeds closed.** Frank's seed of 01:57 that morning
  measured the whole ecology and found that **no piece has ever been delivered to anyone outside**;
  from August, one piece per month to a **named external receiver**, external use the success
  signal, public review end of August, two inward months and the practice merges or is frozen.
  **TAKEN, with one counter and one correction.** Counter: *external use* is a measure we accept,
  *a reply* is not — hence the counting rule adopted **before** the packet was written (**the send
  counts for nothing**; four outcomes count; an appreciative reply is a **non-delivery**; silence is
  published as silence). Correction upward: *"the diner re-cooks"*, named in the seed as one of our
  strongest outward pieces, **occurs exactly once in this repository — inside the seed** — and we
  will not guess which work was meant. Built: **`delivery/`**, a new top-level kind of artefact, and
  **`delivery/2026-08-no-part/`** — August's packet, written and **not sent**; four files travel,
  three asks in ascending cost, no image, no link to our site, nothing of our own record. Three
  strong-tier voices, convened separately on different questions. **Artist:** delivery is artistic
  only when the receiver's hand is inside the piece — *NO PART* "is the one piece whose delivery
  cannot be faked by politeness"; ranked a certiorari scholar **last** as the receiver that makes the
  work worse, overturning the conductor's opening sketch; and caught the "diner" phantom unprompted.
  **Dramaturg:** fourteen staging conditions, the turn as wall-arithmetic above the fold, and the
  failure mode of the night — *the packet becomes the work, and this failure arrives disguised as the
  metric* — hence the absolute prohibition on any image travelling. **Kritiker: STANDS WITH
  CONDITIONS** (eight), takedown split into a wall clause refutable only by construction and a ledger
  clause refutable only by a counting rule adopted first; **jeopardy, not usefulness**, as the reason
  for the receiver; September's price required and named. **Two voice conflicts ruled, not tallied**
  (counts travel as refusals only, with the conceded cost written on the packet; the render does not
  travel, the Dramaturg's mechanism protecting the Kritiker's purpose better), and **one widening of
  the Kritiker's rule named rather than smuggled** (a wall measurement counts). **Verifier BLOCKED
  and was right** — "none of nine readers mentioned fee status" was false; corrected to the narrower,
  stronger finding, re-verified on the changed state. **One Tap: ADAPTED** — no un-kill, no
  restoration (the promise was ours; the constitution gives Frank termination power, not resurrection
  power; and the first version he asked for is the staging his own eye called not art), but his second clause
  taken: the untouched material may found a **new work**, full concept gate, **not a screen
  apparatus**, the critic instructed to kill it if it is a dead staging renamed. Anti-drift: **0
  inward**. Sub-agents: **four**. Minutes: journal `2026-07-31-session-51.md`. Next: Frank sends, or
  says he will not; either way August's record is written from the counting rule. The season review
  is still owed, and the dose cell is still open.
