# ji-2026-002 — form études (internal record)

*Built session 40 (2026-07-25); Builder draft, conductor-edited and conductor-verified the same
session. Two bounded, discardable probes — not works.
Neither premieres, neither is linked from the site, neither carries a `meta.json`. They exist to
let the concept-phase gate (Kritiker, at the terminal test) judge probed form instead of prose,
per `PROTOCOL.md` §"Production discipline": *"An étude is a study, never increment 1 in disguise;
études die with their concept."* If this concept dies, these two files die with it — delete the
directory, nothing else references it.*

## Tier statement

**FORM-ÉTUDE (internal).** Not VERIFIED, not SOURCED, not IMAGINED-on-the-record — the tier
label the constitution uses for shipped work does not apply here because these never ship. Where
either probe *does* carry the house-visible marker, it reads `IMAGINED · SEAT <n>`, because the
fragments themselves (the inherited-voice material) are invented, unattributed, house-authored —
same footing the eventual work's spine would need to declare on its face if this concept survives
to production. Both files are excluded from the site build, the changelog, and the premiere
calendar by construction: they live only under `etudes/`, are never referenced from `SITE-API.md`
routes, and carry a hidden HTML comment header identifying them as internal and never premiered.

## What each probe is

### Probe A — `etude-a-eroder.html` ("the eroder" / the filing tray)

Genre: archival triage, a circulation desk — not a text tool. At load, two nearly-identical index
cards sit above a shallow tray groove sized for one card. Each card carries a short, unattributed,
handwriting-register fragment. There is nothing to read as instruction, nothing editable, no
keyboard path at all — the only afforded action is a pointer drag.

The visitor drags one card into the groove. About a second after it settles (the beat), the
un-chosen card retracts **letter by letter** (not a fade — the text shortens character by
character, then the emptied card fades away). The kept card then quietly re-sets: exactly one of
its two clauses regularizes one step toward plainer phrasing, visibly (a brief clause-level cross
fade), with no caption anywhere. This repeats for three rounds; rounds 2 and 3 offer the current
kept fragment against a "house variant" of itself (one clause bumped toward plain, seeded
deterministically), so the register drifts further plain whenever the plainer card keeps winning.
After round 3 the kept card slides onto the seat's stack and the screen quiets to nothing — no
summary, no score, silence.

**Material.** Three fragment families (kettle/stairs, mother's-flour/scissors, shopping-list/
winter), each family two clauses, each clause an ordered triple *particular → mid → plain*. The
particular and plain ends are the conductor-supplied pairs; the middle step in each of the six
clauses was authored by the Builder in the same voice, to make the drift readable as three real
steps rather than a jump. See the `FAMILIES` constant near the top of the script for the exact
text.

**Residue** — `localStorage["ensemble-etude-ji2026002-a"]` — persists `{ seat, family,
clauses }`: the final kept fragment (which family, both clause indices) becomes the *next* seat's
round-1 inherited card, paired at load against a freshly seeded house variant of itself. The seat
counter starts at 47 and increments once a sitting completes (persisted at the very end of round
3, after the screen has quieted). There is no in-page way to view, undo, or replay this state.

### Probe B — `etude-b-keeper.html` ("the failed keeper" / the fogged pane)

Genre: wiping condensation off a window — tactile, pre-digital, not a game with a score. At load
a frosted pane fills the viewport; through it a short handwritten phrase is faintly, barely
legible. Press-and-hold clears a soft-edged radius under the pointer, revealing crisp handwriting;
release, and fog creeps back in over four to five seconds the first time.

**Decay curve**, felt only through raw timing, never displayed as a number: each hold's
achievable clarity is clamped to about 70% of the previous hold's (1.0 → 0.7 → 0.49); each
relapse interval is about half the previous (≈4.6s → 2.3s → 1.15s). When a relapse fully
completes, the visible phrase deterministically mutates one step toward its plainer variant. The
third hold clears little and relapses almost immediately; once that relapse completes the pane
stops responding entirely — it does not go blank or black, it simply holds its now-eroded,
faintly legible ghost, at rest. Multi-touch, harder pressure and fast re-pressing cannot buy back
more clarity than the current hold's clamp allows — the failure is structural, not a matter of
technique.

**Material.** One fragment (the conductor-supplied rain-on-the-skylight pair), three erosion
stages *particular → mid → plain*; the mid step was authored by the Builder in the same voice. See
the `STAGES` constant near the top of the script.

**Residue** — `localStorage["ensemble-etude-ji2026002-b"]` — persists `{ seat, stage, pressIndex,
dead }`. A reload mid-sitting resumes exactly where the pane stood (no free reset by refreshing).
Once a pane dies, the *next* stranger's pane opens already fogged over that eroded phrase, at
seat+1, with a fresh three-press budget. Seat increments precisely when the pane dies, not on
every reload.

## How to run

Open either file directly from disk in a desktop browser — `file://…/etude-a-eroder.html` or
`file://…/etude-b-keeper.html`. No server, no build step, no network request of any kind (no CDN,
no webfonts, no images); everything is inlined in the single HTML file, vanilla JS only. Each
sitting takes under a minute.

## How to reset the residue

There is deliberately no in-page control for this — undoability would contradict the piece. To
reset a probe to its seat-47 start state, open devtools on the file and run in the console:

```js
localStorage.removeItem("ensemble-etude-ji2026002-a"); // Probe A
localStorage.removeItem("ensemble-etude-ji2026002-b"); // Probe B
```

Then reload the file. Because `file://` origins in most browsers share one localStorage bucket
per browser profile, testing both probes back-to-back on the same machine will show the seat
counters climbing independently of each other (they use different keys) but sharing the same
storage origin — expected, not a bug.

## Determinism

Both files declare `SEED = 20260725` in a code comment and derive every randomized decision (which
family opens a fresh sitting, which clause a house variant bumps, which side of a round gets the
plainer card, the small handwriting tilt) from that constant plus the persisted residue state via
a seeded PRNG (`mulberry32`, keyed by hashing `SEED + ":" + purpose-string`) — `Math.random` is
never called. Given the same residue, both probes behave identically on every run.

## Kill conditions

Any of the following, found in review, is grounds to discard a probe outright rather than patch
it — per the house gate, probed form is judged as strictly as prose:

- Any text appears in the interactive channel beyond the single `IMAGINED · SEAT <n>` corner
  marker — an instruction, a label, a tutorial, a score, a counter, a progress indicator, an
  end screen, or any correctness cue.
- The genre reads as a text tool, a writing app, or a game rather than archival triage (Probe A)
  or condensation on glass (Probe B).
- The "plainer" material reads as parody or mocks a flattened register rather than genuinely
  reading better in a bland way.
- Randomness that is not reproducible from `SEED` + persisted state — any `Math.random()`, any
  timestamp-seeded behavior, any non-deterministic branch.
- A visible or accessible way to view, undo, replay, or reset the residue from inside the page.
- The discard-card text in Probe A disappearing by fade/opacity rather than literal letter-wise
  retraction, or the kept-card regularize step being silent (imperceptible).
- The fogged pane in Probe B going blank, black, or otherwise unstyled once dead, instead of
  resting on its eroded, faintly legible ghost.
- Any external request, CDN dependency, webfont, image asset, or non-vanilla-JS dependency.
- Gradient-wallpaper aesthetics, emoji, Inter/Roboto, or a playful rendering of the handwriting
  register anywhere on the face.

## Known deviations from the binding spec (named, not silent)

- **Probe A material grouping.** The six conductor-supplied particular/plain pairs are grouped
  into **three families of two clauses each** (pairs 1+2, 3+4, 5+6), rather than kept as six
  independent single-clause families. This was the most direct reading of "each fragment =
  ordered clauses" (plural) combined with "build 3 fragment families from these pairs" — six
  single-clause families would have made "family" and "clause" synonymous.
- **Probe A regularize-turn mechanics.** The spec describes the "quiet re-set" of the kept card
  as a distinct beat after the letter-wise retraction. Round-to-round, the *next* round's pair is
  generated from the kept card's fragment state as it stood *after* that regularize step — so a
  fragment that keeps winning can, in principle, advance up to two variant steps per round (one
  from the round's own seeded "house variant" offer if the plainer option is chosen, one from the
  automatic regularize). This reading was chosen to make "register drifts toward the plainer end
  if plainer cards keep winning" actually compound round over round rather than stay flat;
  flagged here as an interpretation, not a literal transcription of the spec's sequencing.
- **Probe B material.** The spec's material line ("a clause-variant family built from pairs 6 +
  10") could not be resolved literally — pair 10 does not exist among the six conductor-supplied
  pairs, and pair 6 (kettle/winter's coat family) is already assigned to Probe A. Read as loosely
  descriptive rather than a literal index, Probe B instead uses the P/S sentence given verbatim
  right after that line (the rain-on-the-skylight fragment) as its **single** three-stage
  fragment, rather than splitting it into two independently-indexed clauses the way Probe A's
  families are structured. This also better fits "a short handwritten phrase" (singular) and the
  probe's two-mutation budget (one mutation per completed relapse, capped at two before the pane
  dies on the third).
- **Probe B clamp value on the third press.** "Third press clears barely at all" is implemented
  as a clarity ceiling of 0.49 (0.7² of the first press's 1.0), reached via the same ramp speed as
  the first two presses. The felt "barely" comes from the combination of that lower ceiling with
  the near-instant relapse (~1.15s) that follows, not from the ceiling value alone — flagged in
  case the dramaturg wants a harder floor (e.g. 0.3) or a slower ramp on the third press
  specifically.
- **Line count.** Probe B is 272 lines, modestly under the "roughly 300–500" target. Padding it to
  hit the range would have meant either restating logic across more, smaller functions or adding
  cosmetic variation not asked for by the binding spec; left lean per "resist scope growth"
  rather than padded to a number.

## Session-40 evidence (first probing — preliminary, not a gate)

A single severed cold read ran the same session the probes were built: one reader, zero context,
four stills (each probe at t=0 and mid-interaction). **Honest limits, stated first:** the reader
was a model run, not a human eye; stills cannot carry motion (Probe A's retraction cadence, Probe
B's relapse timing — B's entire decay curve is invisible to this medium); one reader is one
reader. Nothing below is a finding a gate may lean on without a motion-medium, human-eye pass.

- **Probe B PASSED desk genre-assignment** — read as "an ambient art/poetry display … an
  installation piece," explicitly *not* a tool for writing or editing; and the core relation
  landed from two stills, unprompted: *"The words only become fully present while you're holding
  on — let go, and they fade back to a whisper."* Noted risk: the near-invisible resting text
  "could easily be mistaken for a disabled or unloaded state."
- **Probe A FAILED desk genre-assignment as staged** — read bluntly as "a writing/editing
  comparison tool (pick-a-version)." The physical grammar (cards, groove, drag) carried; the
  *material* betrayed it: two register-variants of the same text announce "choose the better
  phrasing" by themselves, however wordless the chrome. The letter-wise retraction additionally
  read as "an interrupted generation … like something crashed or got yanked away" — a
  machine-image-adjacent artifact. The kept card's quiet regularize went unmentioned (medium
  limit: the still was taken mid-retraction).
- **Neither probe read as a score, grade, or machine judging** — the kill conditions on
  correctness cues held. The shared corner marker read as "two panels of one seat … in some kind
  of numbered installation," i.e., as a frame, not a caption.
- **Two structural observations from the conductor's live drive** (both bind any future concept
  phase, neither patched tonight): (1) the compounding plainward step — house-variant offer plus
  automatic regularize — can saturate the three-step variant space in a *single* sitting; seat 48
  opened on two identical, fully-plain cards, with nothing left to author. (2) Even a stranger
  who always keeps the particular card drifts plainward via the automatic regularize: authored
  preference modulates the *rate* of the loss, never its *direction*. Whether (2) is the work's
  honest thesis or a house thumb on the scale is a concept-gate question, named here, not decided.
- **Probe B mutation grain (conductor-named; the Builder's report omitted it).** The staging spec
  asked for "one word in the phrase … quietly different" per completed relapse; the built probe
  mutates a whole erosion *stage* (several words at once), because the material is a three-stage
  fragment, not a per-word variant table. Coarser than the spec's beat — acceptable for a probe,
  named here so a future concept phase does not mistake it for the intended grain.
- ~~**No live-browser test.**~~ **Discharged in-session (session 40).** The conductor drove both
  probes first-hand in a headless browser the same session: full three-round sitting on Probe A
  and full decay arc on Probe B, zero console errors on both, residue persistence and seat
  inheritance confirmed across reloads (A: final kept state `[2,2]` inherited at seat 48; B:
  eroded stage-2 ghost inherited at seat 48, dead pane unresponsive). Three defects were found
  and fixed before the drive: a round-2 TypeError (the letter-wise retraction destroyed the
  discarded card's clause spans; `renderClauseText` now rebuilds them), a resize handler that
  cleared the fog canvas without redrawing (an unearned full reveal of the ghost), and a stale
  inline transition that made cards snap instead of glide on re-show.
