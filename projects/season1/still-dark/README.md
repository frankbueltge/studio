# STILL DARK — increment 1

One screen, no scroll. `4 AUGUST 2026` held fixed while a two-stop control moves the
*observer's* date from 4 August to 5 August. Eleven vessels dark on 4 August, each a bar
drawn on a 2 June–5 August field and crossed by a labelled rule at 4 August; both ends of
every band hatched seven days wide. Moving the control adds three more vessels beneath —
ships dark on 4 August but not yet known then — and the knowability counter falls from
`11 of 0–11 · 100%` to `11 of 0–14 · 79%–100%`.

**Built from:**
`projects/season1/captures/2026-08-05T043932Z.json` (edition of 4 August, 11 vessels, sha256
`ed3e54ec…`) and `projects/season1/captures/2026-08-05T125400Z.json` (edition of 5 August, 8
vessels). The counter and its verbatim block are the output of
`python3 projects/season1/capture/day.py 2026-08-04`.

**Sources:** vessel data — <https://frankbueltge.de/ghost-fleet/>. Method quote — <https://frankbueltge.de/werke/ghost-fleet/>.

**Tiers on the face:**
- **SOURCED** — vessel identity and edition dates, printed by the source; every such
  string links to it (vessel name → its Global Fishing Watch page).
- **DERIVED** — the date bands: arithmetic on published durations and the published
  7-day window. Both ends always printed, and hatched on the bar.
- **OBSERVED** — this house's own record of when it could first know: the `11 · first
  seen 2026-08-05T04:39:32Z` stamp, and the two captures' fetch metadata in the footer.

Upstream's restraint, inherited and quoted on the face: *"intentional" is a machine
estimate by Global Fishing Watch, "a probability, not proof"; the instrument makes no
claim of illegality against any vessel or state, and neither do we.*
