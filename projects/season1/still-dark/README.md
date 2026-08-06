# STILL DARK — increment 1

One screen, no scroll. `4 AUGUST 2026` held fixed while the reader is asked, before this house
says anything, to commit a number: **How many ships were dark on 4 August 2026?** Eleven vessels
stand above the question, each a bar drawn on a 2 June–5 August field and crossed by a labelled
rule at 4 August; both ends of every band hatched seven days wide.

**State 1 states no finding.** No share, no ceiling, no capture ledger, no null nights — nothing
that answers the question or previews the answer. Writing a number brings the turn: the reader's
figure held, then three more vessels arriving into the same day (dark on 4 August, first known
the night after), then `11 of 0–14 · 79 %–100 %`, then the ceiling that can only fall, then the
whole capture ledger, and last the blindness the method cannot solve. **The reader's number is
never stored and never sent** — there is no network call in this file.

**Three mechanisms are now dead, each killed by a threshold fixed in writing before its object
existed:** the return (66), the two-stop slider (69), and **number-entry (70, `../PANEL-70.md`)**
— three severed readers of three, all stopping on one true line of the house's own:
*"Write a number. Nothing on this screen will answer it for you."* Under the pre-registered
escalation the next form carries **no reader act at all**. The object stands as the readers saw
it; nothing was edited after they saw it.

**State 1 is a state of the reading, not of the file.** The page's JSON island holds all fourteen
rows and the turn's sentences at load, so view-source reaches what the turn withholds. Disclosed
on the work's own face, not hidden.

**Built from four committed captures** (`projects/season1/captures/`), and every figure on the
face is checkable against them:

| capture | body sha256 | content | edition | vessels |
|---|---|---|---|---|
| `2026-08-05T043932Z.json` | `ed3e54ec…` | `ee555746…` | 4 August 2026 | 11 |
| `2026-08-05T125400Z.json` | `17c07fc3…` | `47338b03…` | 5 August 2026 | 8 |
| `2026-08-05T191755Z.json` | `17c07fc3…` | `47338b03…` | 5 August 2026 | 8 |
| `2026-08-06T043619Z.json` | `aed92f4f…` | `47338b03…` | 5 August 2026 | 8 |

**Four captures, three bodies, two editions.** The fourth moved its body hash at an identical
byte count while every field this work reads stayed identical — so the face now prints a
**content** column beside the body hash and says why: a raw body hash is not an edition's
identity. What moved outside this work's reading is not claimed, because the earlier bodies were
never kept. See `../capture/edition.py`.

The turn's verbatim block is the output of `python3 projects/season1/capture/day.py 2026-08-04`;
the ledger is `python3 projects/season1/capture/edition.py`.

**Sources:** vessel data — <https://frankbueltge.de/ghost-fleet/>. Method quote — <https://frankbueltge.de/werke/ghost-fleet/>.

**Tiers on the face**, named in a three-line legend where the eye is:
- **SOURCED** — `name · flag · days dark · waters`, printed by the instrument; every vessel name
  links to its Global Fishing Watch page.
- **DERIVED** — `both ends of every date`: arithmetic on published durations and the published
  7-day window. Both ends always printed, and hatched on the bar.
- **OBSERVED** — this house's own record: `first seen` per vessel, and every capture's timestamp,
  status, byte count and both hashes.

**`render.mjs`** renders the built page in a headless browser and writes `STATE-1.txt` /
`STATE-2.txt` — what a screen reader receives, used unedited as panel material — plus
`render-1400.png`, `render-1400-state2.png` and `render-900.png`, the two legibility widths the
staging law names. Run: `NODE_PATH=<global node_modules> node render.mjs`. It types `11` into the
field for the state-2 render — the script's choice, deterministic, not the work's.
**Dependencies, named honestly:** node ≥ 18 and **playwright** (Apache-2.0) with Chromium (BSD-3-Clause).
They are the house's check on itself, **not the work's**: `index.html` is one self-contained
file with no runtime dependency, no build step and no network call.

Upstream's restraint, inherited and quoted on the face: *"intentional" is a machine
estimate by Global Fishing Watch, "a probability, not proof"; the instrument makes no
claim of illegality against any vessel or state, and neither do we.*
