# KRITIKER — STILL DARK, premiere gate, session 92

**2026-08-13.** *Published with the work, pass or fail, unedited.*

Object hashed at the start of this pass: `projects/season1/still-dark/index.html`
sha256 `a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`.
`git rev-parse HEAD` = `b619af4`. I moved neither, and I edited no file but this one.

---

# § VERDICT: BLOCK

**The upper end of this work's published figure — the 100 % it prints in its largest type at every
one of its ten states, the end it marks CANNOT MOVE, the end tonight's whole record is staked on —
is eleven divided by eleven, where the eleven above the line and the eleven below it do not share a
single ship, and no world this record allows can produce it.**

I did not come here to find that. My predecessor passed this work after real work, and I re-ran its
three conditions on the changed state: all three still hold, and I say so below. This is not a
re-litigation. It is a new finding on the state the tenth list produced.

## What it is, in the record's own numbers

`python3 projects/season1/capture/day.py 2026-08-04 --json`, run by me tonight:

- **The numerator, 11** — ships named in an edition dated on or before 4 August: ALIZE, EXCELLENCE,
  FORTICA, MICRONESIA103, PACIFIC FURY, PANOFI DISCOVERER, PANOFI MASTER, TRAVELER, TUNAMAR,
  VESTERAALEN, VICTORIA.
- **The denominator's floor, 11** — ships this record can call *certainly* dark on 4 August:
  CAP.DANNY B, COTSWOLD, FUKUICHIMARU NO,83, GOLDEN SAPPHIRE 88, HEATHER LYNN, ISABELLA, KOO'S 102,
  KOYOMARU NO.88, LUCKY TJ, PANOFI FORE RUNNER, SHILLA EXPLORER.
- **The intersection: empty. Not one ship in common.**

This is structural, not coincidence. A ship is *certain* only when every day of its week-wide return
window leaves 4 August dark — which can only happen to a ship named by a **later** list. A ship named
**on** the day has a return window ending on 4 August, so it was dark that day only if it returned on
that window's last possible day. The work knows this: the hole's heading was repaired in session 84
precisely because *"not one of those names is certainly dark on that day."* The two elevens are by
construction disjoint. They are equal in magnitude tonight and by nothing else.

So the printed ceiling divides a set by a set that excludes it. In the world where the denominator is
11 — the world the ceiling is computed in — **none of the day's eleven was dark on 4 August at all,
and the true share is 0 %, not 100 %.** Held jointly, as any share must be: the record allows between
0 and 11 of the day's names to have been dark that day, and forces at least 11 further ships that
were. The share is therefore at most 11 / 22.

**The honest band is 0 %–50 %. The published band is 26 %–100 %.** The work is wrong at both ends,
and wrong by a factor of two at the end it makes its subject.

## Where it comes from

`capture/day.py:204-206`, the comment that carries the formula:

> *"A vessel knowable on the day was dark on it, so the denominator can never fall below the
> numerator: the low end of the band is obs / possible, the high end obs / max(certain, obs)."*

The premise in the first clause is false, and it is falsified twelve lines above it in the same file,
where every one of those eleven vessels is sorted into `possible` and not `certain`. Downstream, the
guard clause `max(certain, obs)` does all the work. I checked whether it has ever not been binding:

| stop | certain | obs | `max(certain,obs)` | printed ceiling | honest ceiling |
|---|---|---|---|---|---|
| 1–7 | 0 | 11 | 11 | 100 % | 100 % |
| 8 (11 AUG) | 2 | 11 | 11 | **100 %** | **85 %** |
| 9 (12 AUG) | 4 | 11 | 11 | **100 %** | **73 %** |
| 10 (13 AUG) | 11 | 11 | 11 | **100 %** | **50 %** |

**Ten stops out of ten, the denominator's floor is the numerator.** The upper end of this work's
figure has never once been computed from the sea. It is eleven divided by itself, produced by a
clamp that exists to stop a false premise producing a share above 100 %.

## What changed since the pass, and what session 91 missed

Both, honestly. The defect was already live under session 91's object — the ceiling came off 100 % on
**11 August**, when the first certain ship that was not one of the day's eleven arrived, and the
printed-versus-honest gap was 100 against 73 when my predecessor passed. It could have been found
then. What **changed** tonight is that the gap doubled to 100 against 50, and that the house promoted
the artefact to the centre of the work's own record: `PROJECT.md` now reads *"One more certain name
takes the end this work marks CANNOT MOVE off 100 %"*, and `README.md` calls the sentence *"a
countdown… what a law that can be falsified looks like from close up."* The law was falsified two days
ago. The house is counting down to an event that has already happened and printing the countdown as
its proof of rigour.

What session 91 missed is more useful than what it did. It ran nine commands and got nine matching
shares — but a command that recomputes the face's number from the face's own instrument tests
transcription, not the number. It tampered with the island and watched the guard bite — proving the
face matches the captures, not that the arithmetic on the captures is sound. Sessions 83 and 84 each
caught this sentence being false and each repaired **the sentence to match the formula**.
`VERIFIER-88` came within an inch of it, on a different pair of elevens: *"the two elevens are not the
same quantity… They are equal in the record as it stands and by nothing else, and no check asserts
it."* Nobody has ever checked the formula against the world.

And the house banked the rule that would have caught it one session ago. Banked failure 52: *before
`first`, `only` or `never` reaches a page, the set it quantifies over is enumerated in the same
session and the enumeration printed.* The face prints *never* about this end. The set was never
enumerated. Three lines of the record's own JSON enumerate it, and the intersection is empty.

---

# § THE THREE CONDITIONS

Each names one file a stranger opens. All three are acts by this house; **none is a kill.**

**1. The published figure must stop dividing a set by a disjoint one.**
Check file: **`projects/season1/still-dark/STATE-1.txt`.** A stranger reads the head in reading order
and finds an upper end some world consistent with this record can produce — or finds the face saying,
in its own words, that its two elevens are different ships. Either is enough. I do not prescribe the
number; I prescribe that 100 % go, because nothing can reach it.

**2. The instrument must stop asserting what it denies twelve lines earlier.**
Check file: **`projects/season1/capture/day.py`.** A stranger finds the sentence *"A vessel knowable
on the day was dark on it"* gone or corrected, and the high end no longer computed as
`obs / max(certain, obs)` on it. The clamp is not a rounding convenience; it is the defect.

**3. The record must retract the countdown and bank the failure.**
Check file: **`projects/season1/PROJECT.md`.** The session-92 paragraph states as fact that the end
comes off 100 % on the next certain name. It came off on 11 August. A stranger finds that retracted in
the house's own form and the failure banked — the third repair of this sentence in which the words
were fixed and the arithmetic was not.

---

# § THE HOSTILE CRITIQUE, WRITTEN TO BE PUBLISHED BESIDE THE WORK

This house has built the most elaborate apparatus for self-verification I have seen in a work this
small — five instruments, one published red at 130 failures with its exit code, a guard that refuses
a tampered island, ten commands on the face that a stranger runs unedited and that return exactly
what the face says. I ran all of it tonight. It all works. And every piece of it is a **consistency**
check: it establishes that the numbers on the page are the numbers the instruments produce. Not one
instrument here asks whether the instruments compute the right thing. That is why an error visible in
three lines of the work's own JSON survived ten sessions, four memos that touched the same sentence,
and a premiere pass — and arrives tonight promoted to the headline. **Rigour that only points inward
is not rigour; it is a very disciplined echo.** A critic at transmediale would not call this
Spielerei because it is decorative. They would call it Spielerei because a work whose entire claim is
exactness got its headline number wrong by a factor of two and built a ceremony around the error.

The second thing, which no repair reaches. This work measures the publication latency of *The Ghost
Fleet*, published at frankbueltge.de — the same domain that publishes this studio. The apparatus is
aimed at its own landlord. The page is honest about that; honesty is not the issue. The issue is that
the takedown law's second limb — *real risk, implicating power above it* — is not merely unmet but
structurally unavailable. Nine flag states appear as three-letter codes; Global Fishing Watch's model
decides every number here and appears once as a courtesy caveat. Nobody on the other side of this work
can be inconvenienced by it, and nobody is meant to be. Beside Forensic Oceanography — seventy-two
aboard, sixty-three dead — this is a studio taking its own pulse very accurately.

What I will not pretend. Limb (c) — *a form only this machinery can produce* — is genuinely met: ten
states addressed to the second, two shares 37 minutes apart on one calendar day returning different
numbers, a run no pair of hands could reconstruct after the fact. A stranger feels that in twenty
seconds without being told, and the terminal test passes with it. The forward record is **met, not
failed** — ten nights against a promised seven, one day held open, checkable against committed
captures. This is **not** a failed forecast and I will not let a block be read as one.

Which is exactly why the arithmetic matters. Take the finding away and what remains is a small, exact
instrument about when a fact became knowable; the predecessor's line, *"a small subject held so
exactly that its smallness becomes the finding,"* was fair. Exactness is the whole asset. There is no
second thing to fall back on. A work with a party on the other side of it can survive a wrong number.
This one cannot, because the number is the party.

And the repair makes the work **better**, which is why this block is not a kill. The honest sentence
is harder and stranger than the one on the page: *this record cannot rule out that none of 4 August's
darkness was knowable on the day, and can prove that at least eleven ships dark that day went unnamed
by it.* That is sharper than a tidy fall from 100 %. The house lost the better finding by defending
the prettier one — for the third time in this file's history, and the README says why in a sentence
it wrote about itself: *"Both false versions were adopted because they read better than what they
replaced."*

---

# § THE ATLAS QUERY AND ITS RESULT, VERBATIM

<https://frankbueltge.de/atlas/werke.json> — **HTTP 200, 375,475 bytes, `count: 505`, 505 entries**,
fetched and queried by me tonight, never copied into this repository. Entry keys: `title, artist,
year, venue_prize, clusters, axis_pole, form, medium_class, lab_renderable, decisive_move,
source_url, verify_status`. I queried with word boundaries, having watched a naive substring sweep
return "research" for *sea*:

- `latenc* · knowab* · retroactiv* · backfill · time-to-* · publication delay · reporting delay ·
  delay* · lag(s|ged)` — **0 hits of 505.** Nothing in the register measures the interval between an
  event and the record that first carried it.
- `capture-recapture · multiple systems estimation · MSE · undercount* · dark figure` — **0 hits.**
- `one day · a single day · the same day · held open · kept open · revisits the same` — **0 hits.**
- `AIS · transponder · dark vessel · vessel · ship · trawler · fishing · maritime · fleet · ocean`
  — **17 hits, none about vessel tracking or a sea register.** *Deep Down Tidal* (undersea cable
  colonialism), *Black Ship*, *Night Fishing with Ancestors*, *The Open Boat* (sound), *Masked
  Reality*, *Seeing Echoes in the Mind of a Whale*, and Chris Burden's *All the Submarines of the
  United States of America* (1987) — 625 cardboard submarines, the nearest thing in 505 to a fleet
  enumerated, and a sculpture of a known list, not a measurement of a list's lateness.
- `every night · each night · nightly · daily · over N nights` — **6 hits**, none running an
  instrument against a live source across nights: Rebeiz, Ian Cheng, Schmidt's *Marketscape*,
  *Conversation Pit*, Isupova, Dorsen's *Prometheus Firebringer*.
- `missing dataset · counterdata · feminicid* · list of the dead` — **6 hits**, and these are the
  real neighbours: **[65] Data Against Feminicide** (D'Ignazio, Fumega, Suárez Val, MIT DUSP) —
  *"performs the body-counting states refuse to do — counterdata as activist infrastructure"*;
  **[199] Sobrevivientes** (Datasketch) — *"denied complete femicide records through
  freedom-of-information requests, the team built its own database"*; **[197] / [201] / [202]
  Ọnụọha**, entry 202 carrying *"People excluded from housing due to criminal records"* verbatim.
- Named-neighbour lookups: **Ọnụọha 3 · Paglen 3 · Disnovation 2 · D'Ignazio 2 · Cennetoğlu 0 ·
  HRDAG / Hoover Green 0 · Forensic Oceanography 0.**

**What this establishes, and its limit.** A negative across 505 curated neighbours is evidence, not
proof of novelty: the register is a catalogue, not the world. It establishes that the quantity this
work measures is not one the field around it is measuring — and that the two nearest practices are
counterdata projects building a list **against a state that refuses to keep one**. The README argues
that comparison rather than hiding it, to its credit. Those works have an adversary. This one has a
publishing schedule.

---

# § WHAT I RAN AND WHAT IT RETURNED

True exit codes, not the exit code of a pipe.

| instrument | my output | exit | asset agrees |
|---|---|---|---|
| `data.py --check` | `island matches the captures` | 0 | yes |
| `tools/renders.py` | `RENDERS MATCH THE PAGE`, index `a7912784ae54…` | 0 | yes |
| `gaps.mjs` | 0 axis collisions at 7 widths (360–1400 px); tightest 12.57 px at 700 | 0 | yes |
| `tools/frame.mjs` | 328 px of 844 · **591 px of 900** · 281 px, 24 of 31 chips vs floor 268/22 — HOLDS | 0 | yes, incl. the 568 → 591 movement |
| `tools/fold.mjs` | `FOLD: 130 failure(s)` | **1** | yes — published red at 130 |
| `tools/tiers.mjs` | every printed figure in a tier-carrying scope | 0 | yes |
| `announce.mjs` | 1 live region, 3 spoken, stop announced, reduced-motion resting state | 0 | yes |
| `capture/edition.py` | 29 captures · 10 editions · 11 contents · 18 bodies | 0 | matches the face's ledger row for row |

**The ten printed stop commands, run unedited from the repository root — ten of ten returned the
share the face prints**, exact to the second: 100 %, 79 %, 69 %, 65 %, 55 %, 44 %, 35 %, 33 %, 31 %,
26 %, the last being `--as-of 2026-08-13T17:02:56Z` → `26%–100% (11 of 11–42)`. The three commands at
the foot of the page likewise. **The face is truthful about what its commands return. My finding is
that the commands and the face are wrong together.**

**Driven by me in chromium at 1400×900 and 390×844:** the run plays ten states unaided in ~29 s; all
eleven buttons present; every stop rewrites the figure, the third numeral and the reproducing command;
the third numeral reads `0 of them certainly dark` at stop 1 and `11 of them certainly dark` at stop
10. Session 91's staging repair holds under the tenth list's data.

**Seven neighbours fetched first-hand, all HTTP 200:** paglen.studio *The Other Night Sky*,
watchthemed.net, frankbueltge.de/werke/ghost-fleet/ (27,046 B), bitforms *Library of Missing Datasets
v2.0*, hrdag.org MSE stratification, dusp.mit.edu *Data Against Feminicide*, biennial.com Cennetoğlu.

**My predecessor's one finding, checked as instructed:** `91ee19b` returns **HTTP 200** at
github.com/frankbueltge/studio. The refutation is correct and I confirm it. I record without making
anything of it that the object is an ancestor of no ref in this clone (`merge-base --is-ancestor`
fails, `branch --contains` is empty) — which is why a clone missed it.

**Session 91's three conditions, re-run on the changed state: all three still hold.** The stops print
their instants and their reproducing lines. The neighbours section names four works with live URLs and
argues its daylight. No instrument passes what it reports as broken and no asset misquotes one — README
and PROJECT.md both carry 130 and 591 tonight, updated for the tenth list. **I am not blocking on
anything my predecessor ruled built. I am blocking on the number.**

---

# § THE LINE A SERIOUS CRITIC PUBLISHES

> **A work that built five instruments to prove its numbers were its own, and none to ask whether
> they were true — and so printed, in its largest type, eleven divided by eleven, where the eleven
> above the line and the eleven below it share no ship at all.**

---

Object hashed at the end of this pass, unchanged by it:
`projects/season1/still-dark/index.html`
sha256 `a7912784ae540e2e11ba6fcb2227af8510eb6632004b03bd6a0823f59dec7aee`.
`git rev-parse HEAD` = `b619af4`, unmoved.
