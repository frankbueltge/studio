# KRITIKER — STILL DARK, premiere gate, session 84

*Published with the work, pass or fail. Written after driving the built page at 390×844 and 1400×900,
running `announce.mjs`, `tools/fold.mjs`, `data.py --check` and `day.py` at seven instants, opening
every capture in `projects/season1/captures/`, and fetching the upstream instrument and every
neighbour named below. Nothing here is taken on the record's word.*

---

## 1. What is actually on the screen

A calendar day is pinned open. A number falls from `100 %–100 %` to `37 %–100 %` over
twenty-four seconds, in seven stops labelled `ON THE DAY` through `+6 DAYS`, and under it a block of
ship names grows. Below: thirty vessels on a dated field, a ledger of nineteen fetches with hashes,
and the command that reproduces the figure. I ran that command at seven instants. It returns
100, 79, 69, 65, 55, 44, 37 — the record's five falls, exactly as published. The arithmetic is sound,
the island matches the captures, the page types nothing. On the craft of self-verification this is
the most disciplined object this house has produced.

That is the last unqualified sentence in this critique.

## 2. The number is not a share of what the page says it is a share of

The headline reads: **how much of 4 August 2026's darkness was knowable on the day itself.**
The denominator is thirty ships. Thirty is the union of seven daily lists, and each of those lists
names **six to eleven vessels**. I opened the saved bytes. Every capture carries an
`aggregates` block that the house's own `capture/capture.py` parses at lines 131–132 and that
nothing in the work has ever printed:

| saved copy | list dated | names published | disappearances examined | events in the window |
|---|---|---|---|---|
| `2026-08-05T043932Z.json` | 4 August 2026 | **11** | **230** | **5,641** |
| `2026-08-10T220456Z.json` | 10 August 2026 | **10** | **213** | **5,645** |

The instrument this page reads is a *top-of-list display*: it prints the longest gaps and one case
of the day, out of a couple of hundred it examines, out of five and a half thousand in its window.
The page's most prominent heading — *"IN THE LIST DATED 4 AUG — eleven ships, **all that the day
held about itself**"* — is refuted by the file the page saved that morning. The day held eleven
**printed names** and 5,641 **events**. The face never says this. Not in the lede's honest hedge
(*"only offshore switch-offs a machine model classed as intentional"* — that is upstream's *filter*,
not its *display cut*), not in the ledger column headed *"ships in that list"*, not in the floor line,
not once in `README.md`, `PROJECT.md` or any memo beside them.

The consequence is not a rounding matter. The share is roughly `11 / (7 lists × ~3 new names each)`.
Its magnitude is governed by how many names the upstream page chooses to print. Double the list
length and the figure roughly halves; publish all 213 and it collapses. **The measured quantity is
the churn of a ten-item display, wearing the name of a day's darkness.** And the truncation is
biased, not neutral: the cut is by duration, so it systematically favours long gaps, whose week-wide
return windows cover many past days — which loads the denominator and depresses the share. Nineteen
sessions, five severed panels, three blocking voices and four instruments passed over this, because
every one of them checked whether the page agreed with the captures and none asked what the captures
are a sample of.

This is the house's own cardinal sin in its subtlest form: not a tier mark removed, but a
DERIVED figure whose declared basis (*"worked out here, from saved copies of those lists"*) is true
and whose real basis (*ten names a day out of thousands*) is unstated. Under the labeling law that
label does not hold.

The bitter part: **the disclosure is the finding the work has been looking for.** `11` against
`5,641`, printed side by side and computed from the island the page already carries, is a harder,
stranger, more publishable fact than a share sliding from 100 to 37. The work captured it on night
one and has never looked at it.

## 3. The machine-advantage test — ruled explicitly

**Scale: fails.** Nineteen HTTP GETs over six nights. A person with a browser and a calendar does
this in five minutes a day.

**Repetition: fails.** Seven distinct lists. Not one operation performed ten thousand times.

**Verification: passes, and is invisible.** `data.py --check`, `gaps.mjs` (0 of 30 rows misaligned),
`announce.mjs`, `tools/fold.mjs` — genuine machine labour, exhaustively honest, and experienceable by
a stranger as nothing but a table of truncated hashes.

**The temporal: passes, narrowly, and it is the only limb that carries the work.** The figure exists
only because something was present at 04:39 on six consecutive mornings; the archive cannot be
reconstructed after the fact, and a stranger looking at nineteen timestamped rows and a number that
falls does feel that this was not made in one sitting. That feeling is real. It is also modest: what
they feel is *diligence*, not *a machine*. Nineteen rows is a quantity a human hand plainly reaches.

**Ruling: the line is met at its floor and not above it, and it is met by the wrong limb.** The
machine advantage this subject was begging for sat in the same saved files — 5,645 events in the
window, seven overlapping incomplete lists, the textbook setup for estimating what none of them
caught. The work declined to estimate and printed `0–30` instead. It chose to be the most honest
possible counter of ten names when it could have been the only instrument that estimated the unseen.
**A machine's advantage that is spent entirely on checking itself is not an advantage a visitor can
experience.**

## 4. Terminal test — passes. Material bar — thin. The headline eats itself.

A stranger gets it in twenty seconds: a day, a number, the number falls. That is genuinely good
staging and the strongest formal thing here.

But the number they meet first is `100 %–100 %` — a range whose two ends are identical, which reads
as a stutter — and the number they leave with is `37 %–100 %`, a range so wide it asserts almost
nothing. Directly beneath sits a five-line disclaimer about the behaviour of an upper bound that has
never moved. **The page's second-most prominent text is a footnote about a constant.** A visitor
whose machine asks for no motion gets `100 %–100 %`, seven buttons, and no work at all.

The material bar: ships going dark carries real stakes — forced labour, sanctions, plundered EEZs.
This work touches none of them. Thirty vessel names are arithmetic furniture; not one is
investigated, and the piece would be identical if they were rows of a bus timetable. The stakes on
this page are borrowed from the instrument it measures, and what it measures about that instrument
is a publication lag.

## 5. Takedown law

*"A studio watched a website update for a month and called its own patience a measurement."*

- **(c) a form only this machinery can produce** — the floor, and it is **met**: a day-addressed
  record of when each disappearance became knowable does not exist upstream or anywhere else, and
  cannot be made retroactively.
- **(a) a finding of its own** — **not met.** The fall from 100 to 37 is a property of an upstream
  display cut, not of the sea. The one real finding is in §2 and unpublished.
- **(b) real risk, implicating power above it** — **not met, and it is worse than absent.** The only
  institution this work implicates is the daily publication cadence of an instrument on
  `frankbueltge.de` — the same domain that publishes this page. Global Fishing Watch, whose model
  and cut actually determine every number here, is thanked and never examined. This is an in-house
  audit wearing a sea chart.

The takedown is **answered, not refuted.** The patience was real, the arithmetic checks — and the
thing measured is still, precisely, a website's update behaviour.

## 6. Adjacency — three neighbours the record has not named

Named by the record: the Ghost Fleet itself; Trevor Paglen, *The Other Night Sky*
(<https://paglen.studio/2020/05/22/the-other-night-sky/> — checked); Watch the Med. The daylight
against Paglen holds.

Not named, and each closer than Paglen:

- **Mimi Ọnụọha, *The Library of Missing Datasets*** (<https://zkm.de/en/artwork/the-library-of-missing-datasets> — checked). A work whose entire subject is the blank spot in a data-saturated space. STILL DARK's claim — *"the number exists in no dataset"* — is Ọnụọha's premise, and the collective's own protocol names her as a benchmark. Omitting her from the neighbours is not an oversight, it is the neighbour that most needs daylight argued against it.
- **Banu Cennetoğlu, *The List*** (<https://www.biennial.com/artists/banu-cennetoglu/> — checked): a count of the dead compiled by others, republished as art precisely because it is never complete and keeps growing — an always-incomplete accumulating list, publicly restaged. That is this form, two decades earlier, with stakes.
- **HRDAG, multiple systems estimation** (<https://hrdag.org/mse/> — checked). Not art, and that is why it stings: the professional answer to *"overlapping incomplete lists, how many did none of them catch"* is a solved method, and this work has the inputs for it and prints `0–30`.

And **Forensic Architecture / Forensic Oceanography, *The Left-to-die Boat***
(<https://forensic-architecture.org/investigation/the-left-to-die-boat> — checked) is the standard
this house says it wants to stand beside: the same maritime traces, the same machine-readable
absences, sixty-three deaths and a named chain of responsibility. Beside it, STILL DARK is a
latency chart with excellent footnotes.

No copying. The daylight is real. But a proposal that names Paglen and misses Ọnụọha has not
searched its own field.

## 7. Tonight's repair broke the thing it was built to protect

Item (y) pinned the controls to the foot of the phone screen. I drove the built page at 390×844.
At the end of the run, `#sd-arrive-names-since` — the nineteen names, the block the work calls
the only element meant to be seen changing — spans y = 719→946. The pinned control bar spans
y = 720→844, opaque, on top of it. **One pixel of the growing names is visible.** Scrolled to the
foot of the head, the bar cuts through the last row of chips: of the five darker-ink ships the new
heading tells the reader to count by position — *"The last five, in darker ink, arrived with the
list of 10 AUG"* — a phone shows two. The other three are under the bar. The repair that made the
words honest and the repair that made the phone usable contradict each other on the same screen.

`tools/fold.mjs`, written tonight for exactly this class of defect, exits **0**. It watches the
figure, the hole's *heading*, the controls and the live line. It does not watch the names. Banked
failure 6 — *rendered, not looked at* — recurs at the width most visitors use, one session after
the instrument against it was built. (It also prints `✗OFF` for the figure itself at
`scroll:head-bottom` on the phone and passes anyway.)

## 8. Ambition audit

Promise: *one calendar day held open across at least the seven nights of its cited window,
publishing the measured share of that day's darkness knowable on the day itself, checkable against
the captures.*

Shipped: one day held open; seven distinct lists; nineteen copies over **six** nights of fetching
(2026-08-05 → 2026-08-10); the share published and reproducible at every past instant. The named
failed forecast — a single-sitting screen with seeded times — is comfortably avoided.

**Ruling: MET on substance, one night short on the letter, not exceeded.** The day's own answer was
never observed on the day: the 4 August list first reached this record at 04:39 UTC on 5 August.
The face discloses that (*"this page first saw all eleven on 5 AUG"*), and the disclosure is to the
house's credit — but the phrase *"knowable on the day itself"* is carried by a copy saved the
morning after.

## 9. The line a serious critic publishes

> **A studio fetched a ten-name list for six nights and published the interval as the unknowability
> of the sea — while the same saved bytes recorded 5,641 events it never counted.**

---

## VERDICT

**BLOCKED.**

Two conditions. Both are cheap, both are checkable by a stranger in a named file, and the first one
hands this work the finding it has been missing for nineteen sessions.

1. **The face states what its denominator is a sample of, computed and not typed.** From the
   `aggregates` block already parsed into every `projects/season1/captures/*.json`, the page must
   print — beside the figure, not in a footnote — how many names each list published against how
   many disappearances that same saved copy recorded as examined and as in the window (11 against
   230 and 5,641 on 4 August; 10 against 213 and 5,645 on 10 August), and must say plainly that the
   share is a share of the names published. The heading *"eleven ships, all that the day held about
   itself"* must go; it is false against the file saved that morning.
   *Check:* `projects/season1/still-dark/index.html` and `STATE-1.txt` against
   `projects/season1/captures/2026-08-05T043932Z.json`.

2. **The phone stops occluding the material.** The pinned control bar must not cover
   `#sd-arrive-names-since` at any stop or scroll position, and `tools/fold.mjs` must fail when it
   does — the guard must watch the names, not only their heading.
   *Check:* `projects/season1/still-dark/tools/fold.mjs` (must exit non-zero on the page as
   committed tonight) and a 390×844 render at stop 6.

Nothing else is owed. The form stands, the archive stands, the arithmetic stands. What does not
stand is a page that prints a fraction of a day's darkness while holding, in its own evidence, the
number that says what fraction it really is.
