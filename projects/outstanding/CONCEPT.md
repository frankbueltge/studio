# OUTSTANDING — concept put to the gate, 2026-08-21 (session 106)

*Artist's document, forwarded by the conductor. Sixth concept under v3. Trimmed after the gate to
bring the project under the 3,000-word cap — restatement only, in §2, §5 and §9. No argument dropped.*

## 1. The claim, in one sentence

Right now, across 126 forecast offices, a public promise about rain is standing unresolved — and
this room shows the moment, live, when the sky decides whether to keep it.

## 2. The machine advantage

**Verification, at scale.** A person can watch one office's forecast and wait to see whether it
rains; that is an evening's hobby. This work holds every currently open forecast period in the
country — on the order of forty thousand unsettled public claims — and checks each the instant that
becomes possible, for as long as the room is open. The visitor does not read a claim of
thoroughness. They see hundreds of lit places, each independently live, at a breadth no pair of eyes
holds by refreshing pages one at a time.

## 3. How this clears the minute-twenty test

Nothing on screen at minute zero is a finished answer: every node shows a claim still open — a
number, a word, or a silence — with no verdict, because the sky has not spoken for it. Between
minute zero and minute twenty, two things happen that were not knowable in advance. Offices re-issue
their bulletins on their own clocks and replace what a node was showing; and periods reach the end
of their window and are checked against an observation that did not exist when the door opened. What
the visitor watches at minute twenty is the accumulation of *those* events, not a slower reveal of a
number already fixed. That is the fault line the previous death fell on; this work holds nothing
pre-settled.

## 4. The form, and why

A dark full-screen field, shaped loosely like the geography the offices cover — points of light, no
labels, no legend. Each point carries concentric rings: inner for the next few hours, widening
outward to a horizon of about a week. Numeric claims glow at a brightness set by their stated
number; word-only claims carry a hue; and — the thing the last attempt never built — **silent
periods are not blank space, they are a visible dim band**, because silence is this record's
commonest way of making a promise.

When a period's window closes, its band flares: locking bright and steady if the sky matched it,
rupturing into a sharper spreading colour if it did not. **A silence that turns out wet is the
loudest event the piece has** — the record's least visible failure made impossible to miss. A soft
tone carries the same distinction in timbre, which is what lets the piece work at the room's real
viewing distance with no text. Afterglow fades within minutes, so the field stays what is currently
*owed* rather than a tally of what has been paid. Touch is optional and releases on its own; nothing
about the stake depends on a visitor finding it.

## 5. Three nearest neighbours

*Sourced in `NEIGHBOURS.md`.* ***The Prediction Machine*** speaks predictions from a live weather
feed and deliberately never checks them; this work exists to check them, on screen. ***Cumulus***
shows the sky as live imagery but states no claim that could be wrong; here the claim is the whole
subject. ***Atmospherics / Weather Works*** sonifies weather as immersion; sound here is not
atmosphere but a verdict landing on a specific promise.

## 6. The visitor on the other side

A stranger stands in a dark room and, without reading anything, understands two things at once:
something is being promised right now, everywhere, by place and by hour; and some of those promises
are breaking while they watch. What they carry away is not a statistic. It is the felt fact that the
throwaway sentence *chance of rain 20 percent* is a bet still open somewhere the moment they leave
— and that most of the time this record does not name a number at all. It goes quiet. And quiet
breaks too.

## 7. The material, and the relay

Committed and reachable, read first-hand on 2026-08-21: live Zone Forecast Product bulletins from
the 126 issuing offices, and live hourly station observations carrying `precipitationLastHour`,
`presentWeather` and `textDescription`.

The work's origin cannot fetch either (`connect-src 'self'`). **Relay needed on the work's own
origin:** two small JSON files, refreshed in place — one carrying per office the period name, issue
timestamp, valid window, raw claim text and extracted number if any; one carrying per station the
timestamp, precipitation and present weather. **Cadence: 15 minutes preferred, 60 minutes the hard
floor** — superseded by the gate; see the corrections.

## 8. Milestones

1. **Field lit** — every office's nodes drawn, all rings open, nothing settled yet this session.
2. **First flare** — a claim settles live, the tone sounds, the node locks.
3. **A silence ruptures** — a dim band turns out wet, unmistakable without a word of text.
4. **A re-issuance sweep** — a node's outer rings replace themselves, timing unannounced.
5. **Sustained field** — afterglow always fading; the screen never becomes a finished tally.
6. **A held node** — a visitor's touch traces one place's recent rhythm, then lets go.

## 9. What would kill this

On a quiet, dry national stretch, flares could be sparse inside any twenty minutes, leaving the room
under-eventful. The Artist concedes rather than dissolves this: the stake was never the flare rate.
A field of hundreds of open, unresolved public promises is already the tension; the flares are
punctuation on a held state that is never idle.

---

## Corrections, 2026-08-22 (session 107) — on the face, not by rewriting

Three figures above are wrong, and are struck here rather than edited out: this document is the
object a gate passed. **The full account, with the instruments and instants, is the addendum in
`memory/dossiers/forecast-vocabulary.md`; the evidence is `VERIFIER-107.md` and
`RELAY-MEASUREMENT.md`.** What must be legible on this page is which figures no longer hold.

- **§1, §7 — "126 offices" → 123.** 126 counts forecast-*area* subdivisions, several sharing one
  issuing office. We divided by the wrong denominator.
- **§2 — "on the order of forty thousand" → 47,445, counted, not estimated.** At
  **2026-08-22T00:35:19Z: 123 offices, 3,771 zones, 47,445 periods — 20,217 numeric (42.6 %),
  25,766 silent (54.3 %), 1,462 word-only.** Our extrapolation from eight large offices and an
  independent refutation from twelve small ones were both wrong, in opposite directions, and
  neither bracketed the census.
- **§7 and the gate's ruling — "delayed by about an hour" → about twenty minutes.** Two national
  samples, medians 20.5 and 20.9. **This strengthens the ruling rather than disturbing it:** it
  passed a delayed feed because nothing possesses the verdict at open, and a shorter delay
  possesses less.
- **§7's cadence line is superseded, not corrected.** The gate set **five preferred, ten hard,
  sixty refused, no waiver.**

**What does not change.** Silence came back at 54.3 % of live national periods against the archive's
51.7 % — different material, different instrument, so corroboration in kind and not the independent
re-derivation the dossier is still owed. Condition 2 stands: no archive-derived figure goes into the
rendering.
