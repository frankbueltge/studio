# STILL DARK — increment 1

**One screen. No interaction, no state, nothing withheld.** `4 AUGUST 2026` held fixed while
sixteen vessels stand on a 2 June–6 August field, crossed by a labelled rule at 4 August, both
ends of every band hatched seven days wide. The rows are grouped by the list that first carried
them: **eleven in the list of 4 August — the day itself**, three added by the list of 5 August,
two added by the list of 6 August.

**Since session 72 the house's filing words are off the face.** *Edition* and *capture* are what
this house calls the things it collects; on the page they are **the list** the instrument publishes
and **the saved copy** this page holds, and both survive as columns of the OBSERVED ledger, where
the filing system is itself the object on show. The three tier words stay — they are the labeling
law — and each now earns itself on a plain verb phrase before it is used anywhere else. Three
severed readers placed all three tiers correctly with the nouns gone in 72, and three more in 73
(`../PANEL-73.md`, Q2 3 of 3).

**Since session 73 the lede names its day.** It said *"that day"* and never named it, and 72's
unaided-recall question was refuted at 2 of 3 on exactly that. The day is now written where the
anaphor stood and named once more in the same sentence; nothing else on the page moved, and the
question, put back verbatim, went to 3 of 3. TUNAMAR's waters joined its row the same night: the
instrument prints the case of the day as prose and never as a list row, so the string is recovered
from that prose at read time — SOURCED, with no saved copy rewritten (`../capture/edition.py`).

**Since session 74 the denominator carries one glossing sentence** (`../DRAMATURG-74.md` §A),
computed like every other figure here: *"Sixteen ships could have been dark on 4 August 2026 and not
one of them certainly, because the instrument publishes a return only as a week-wide window — so the
total is written 0–16, and the share runs from 11 of 16 to 11 of 11."* Three of three readers now say
what the 0 and the 16 count — and **two of three still read `11 of 0–16` itself as broken**, so the
notation is refuted on legibility and the sentence is credited with nothing under its own
pre-registered scoring rule (`../PANEL-74.md`, Q5).

**Session 74 was also the first panel of this house that could see the drawing.** Readers had always
been given only the text extraction; from 74 they are given the two renders as images as well. The
first night with eyes returned six findings no text panel could reach, and they are listed in
`../PANEL-74.md` — including that the strike-through on the superseded figure is carried by one CSS
declaration and by nothing in the text, so a reader hearing this page gets two live percentages for
one day.

**The turn is the record's, not the reader's.** This work published a law on its own face — *a
ceiling that can only fall* — and on 6 August it fell, unaided:

| | share knowable on the day | |
|---|---|---|
| as published, 4 saved copies / 2 lists, to `2026-08-06T04:36:19Z` | **79 %–100 %** | 11 of 0–14 |
| as measured now, 8 saved copies / 3 lists | **69 %–100 %** | 11 of 0–16 |

The numerator did not move and cannot: no later night can put a name into a list that did not
carry it. The total moved, by **ALBACORA CUATRO** (ESP) and **BONAMI** (KOR), two ships that
entered the record with the list of 6 August — two days after the day. **The eighth saved copy, taken
2026-08-07T04:38:28Z, returned the 6 August list unchanged in every field this work reads — the
fourth night running**, and the share stands unchanged. Both figures are re-runnable by anyone:

```
python3 projects/season1/capture/day.py 2026-08-04
python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-06T04:36:19Z
```

**Five mechanisms of a reader act were built; three died by pre-registered threshold** — the
return (66), the two-stop slider (69), number-entry (70). All three severed readers of the last
panel stopped on one true line of this house's own: *"Write a number. Nothing on this screen will
answer it for you."* The ruling of five nights: **this house cannot stand a reader in front of an
act without also telling them, truthfully, what the act is worth.** Under the pre-registered
escalation this form carries **no reader act at all** — and with the act went the two-state
apparatus, the keypad, the button and everything the turn used to withhold.

**Every figure on the face is computed from the committed captures, never typed.**
`data.py` builds the page's JSON island from `../captures/*.json`; `data.py --check` fails if the
island and the captures disagree. Two figures had previously reached a face out of a head instead
of off a record (sessions 66 and 70); both were caught, neither should have been possible.

| capture | body sha256 | content | edition | vessels |
|---|---|---|---|---|
| `2026-08-05T043932Z.json` | `ed3e54ec…` | `ee555746…` | 4 August 2026 | 11 |
| `2026-08-05T125400Z.json` | `17c07fc3…` | `47338b03…` | 5 August 2026 | 8 |
| `2026-08-05T191755Z.json` | `17c07fc3…` | `47338b03…` | 5 August 2026 | 8 |
| `2026-08-06T043619Z.json` | `aed92f4f…` | `47338b03…` | 5 August 2026 | 8 |
| `2026-08-06T081642Z.json` | `f673e2f7…` | `53114dfe…` | 6 August 2026 | 7 |
| `2026-08-06T142217Z.json` | `f673e2f7…` | `53114dfe…` | 6 August 2026 | 7 |
| `2026-08-06T152800Z.json` | `f673e2f7…` | `53114dfe…` | 6 August 2026 | 7 |
| `2026-08-07T043828Z.json` | `74f093f7…` | `53114dfe…` | 6 August 2026 | 7 |

**Eight saved copies, five bodies, three lists.** Two lists have now come back in more than one set
of bytes each while every field this work reads stayed identical — so the face prints a **content**
column beside the body hash and says why: a copy's fingerprint is not the list's identity. See
`../capture/edition.py`.

**And on 7 August a moved body hash was ATTRIBUTED for the first time rather than guessed at.** The
`page_assets` field, recorded since session 70 for exactly this purpose and read by no part of the
work, moved with it: the response's stylesheet reference went from `/_astro/TopBar.SLcnmZbT.css` to
`/_astro/Base.BvXYJsAy.css`, so the site was rebuilt between the two fetches. **That is one observed
difference and it is the whole of the claim** — whether it accounts for all 554 bytes of the change
is *not* asserted, because the 15:28 body itself was never kept. The guard this house built in
session 70 has now, once, done the job it was built for.

**Sources:** vessel data — <https://frankbueltge.de/ghost-fleet/>. Method quote —
<https://frankbueltge.de/werke/ghost-fleet/>.

**Tiers on the face**, named in a three-line legend where the eye is:
- **SOURCED** — `name · flag · days dark · waters`, printed by the instrument; every vessel name
  links to its Global Fishing Watch page.
- **DERIVED** — `both ends of every date`: arithmetic on published durations and the published
  7-day window. Both ends always printed, and hatched on the bar.
- **OBSERVED** — this house's own record: `first seen` per vessel, which edition first carried it,
  and every capture's timestamp, status, byte count and both hashes.

**`render.mjs`** renders the built page in a headless browser and writes `STATE-1.txt` — what a
screen reader receives, used unedited as panel material — plus `render-1400.png` and
`render-900.png`, the two legibility widths the staging law names. **The text extraction is not
enough on its own:** session 72 found the labelled rule at 4 August clipped in half at both widths
by the field wrapper's overflow, a defect invisible in `STATE-1.txt`, where the label reads
perfectly. It was found by cropping the render and looking at it, and fixed. **Nor was the render
enough while nobody was given it:** in 73 all three severed readers reported that the drawn field
never reached them at all, so every reading panel this house had run up to that night had scored a
work whose largest element the readers could not see. **Closed in 74** — the renders now go to the
panel with the extraction, and the first sighted panel found the misalignment of every bar with its
label, which eight text panels had passed (`../PANEL-74.md`). Run:
`NODE_PATH=<global node_modules> node render.mjs`.
**Dependencies, named honestly:** node ≥ 18 and **playwright** (Apache-2.0) with Chromium
(BSD-3-Clause; its bundled third-party components carry their own licences — the Verifier's
session-71 pass did not re-check either over the network, and says so). They are the house's check
on itself, **not the work's**: `index.html` is one self-contained file with no runtime dependency,
no build step and no network call. `data.py` (Python 3, standard library only) builds the page's
data island from the captures; it is a build-time check, not a runtime dependency.

Upstream's restraint, inherited and quoted on the face: *"intentional" is a machine estimate by
Global Fishing Watch, "a probability, not proof"; the instrument makes no claim of illegality
against any vessel or state, and neither do we.*
