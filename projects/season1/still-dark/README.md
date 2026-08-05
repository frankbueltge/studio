# STILL DARK — increment 1

One screen, no scroll. `4 AUGUST 2026` held fixed while a two-stop control moves the
*observer's* date from 4 August to 5 August. Eleven vessels dark on 4 August, each a bar
drawn on a 2 June–5 August field and crossed by a labelled rule at 4 August; both ends of
every band hatched seven days wide.

**State 1 states no share.** It prints the measured count — eleven vessels in the edition of
4 August — its capture's evidence, and two blanks: `knowable on 4 Aug — 11 of ____ · ____%`.
Moving the control adds three more vessels beneath — ships dark on 4 August but not yet known
then — fills the blanks with `11 of 0–14 · 79%–100%`, and only there prints the finding: a
ceiling that can only fall. **Rebuilt in session 69** after three severed readers, given state 1
alone, refused to move a control whose ending the page had already told them (`../PANEL-68.md`
in commit `24295ac`).

**The two-stop control is RETIRED as a mechanism** (session 69, `../PANEL-69.md`): a second
consecutive panel below the pre-registered threshold. The object stands as the readers saw it.

**State 1 is a state of the reading, not of the file.** The page's JSON island holds all
fourteen rows at load, so view-source reaches what the turn withholds. Disclosed, not hidden.

**Built from:** `projects/season1/captures/2026-08-05T043932Z.json` (edition of 4 August, 11
vessels, sha256 `ed3e54ec…`), `…T125400Z.json` (edition of 5 August, 8 vessels, sha256
`17c07fc3…`) and `…T191755Z.json` (the same 5 August edition, byte for byte — a night that added
nothing, printed). The counter and its verbatim block are the output of
`python3 projects/season1/capture/day.py 2026-08-04`, with the first screen's state re-runnable as
`… day.py 2026-08-04 --as-of 2026-08-05T05:00:00Z`.

**Sources:** vessel data — <https://frankbueltge.de/ghost-fleet/>. Method quote — <https://frankbueltge.de/werke/ghost-fleet/>.

**Tiers on the face:** a single column header binds them where the eye is —
- **SOURCED** — `name · flag · days dark · waters`, printed by the source; every vessel name
  links to its Global Fishing Watch page.
- **DERIVED** — `both ends of every date`: arithmetic on published durations and the published
  7-day window. Both ends always printed, and hatched on the bar.
- **OBSERVED** — this house's own record: the count of vessels in an edition, carried in one
  string with the capture's timestamp, status, byte count and hash.

**`render.mjs`** renders the built page in a headless browser and writes `STATE-1.txt` /
`STATE-2.txt` — what a screen reader receives, used unedited as panel material — plus
`render-1400.png`, `render-1400-state2.png` and `render-900.png`, the two legibility widths the
staging law names. Run: `NODE_PATH=<global node_modules> node render.mjs`.
**Dependencies, named honestly:** node ≥ 18 and **playwright** (Apache-2.0) with Chromium (BSD-3-Clause).
They are the house's check on itself, **not the work's**: `index.html` is one self-contained
file with no runtime dependency, no build step and no network call.

Upstream's restraint, inherited and quoted on the face: *"intentional" is a machine
estimate by Global Fishing Watch, "a probability, not proof"; the instrument makes no
claim of illegality against any vessel or state, and neither do we.*
