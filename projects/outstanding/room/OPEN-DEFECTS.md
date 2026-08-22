# OUTSTANDING — the room's open defects, session 107

*Kept the way STILL DARK's register is kept: a defect that is written down is not thereby paid, and
this file exists so the next session meets them instead of rediscovering them. Each carries the
evidence that found it.*

**1 — The projection collapses when a Pacific office is present.** With Guam's real centroid
(13.4435, 144.7774) injected and reloaded through the real `room.js`, the New York–Seattle pixel
separation falls from **1,271 px (86 % of usable width) to 239 px (16 %)**, Guam at the far edge and
the continental field crushed to a sliver. The room computes its bounds from whatever data is
present, and one office at longitude +144 against a continent at −70 to −122 is enough. **The relay
will carry every office**, so this fires the first time the room meets the real file. Found by the
geometry pass, reported rather than fixed — `room.js` was another hand's file that evening.

**2 — 88 of 3,771 live zones cannot be geocoded, and it is a parsing behaviour, not a gap in the
lookup.** The gazetteer resolved 4,080 of 4,080 public zones with zero failures; the relay then
geocoded **3,683 of 3,771 (97.7 %)**. The 88 are compound UGC headers — `GUZ001-MPZ001`,
`FLZ076>078` — which `zfp_harvest.zone_blocks()` returns as one joined string rather than as the
codes it contains. Guam's and Key West's zones in the current fixture happen to be exactly these,
which is why they render in the unplaced strip.

**3 — Sound does not start in an unattended room.** Chromium refuses the audio context without a
user gesture: *"The AudioContext was not allowed to start."* Observed on every headless load. The
gate bound the lock/rupture distinction to **light *and* timbre**, so a room that never makes a
sound has met that condition on paper only. The remedy is known and belongs to the deliverable
rather than to the code — the presentation mode is part of what ships (v3 §2), and a kiosk launched
with the browser's autoplay policy relaxed is the ordinary way an unattended installation does this.
**It must be written into the work's stated presentation mode, not assumed.**

**4 — `?relay=` accepts a data source from the query string.** Useful in production, wrong in a
shipped work: a visitor's URL should not be able to repoint the room's evidence. The CSP stops it
reaching another origin, which is not the same as it being right. Close before any ship gate.

**5 — Milestone 5 is unproven and the gate named it specifically.** *"Evidenced against a genuinely
dry national stretch, instrumented, not asserted."* The room has been driven only by fixtures and by
one disclosed acceleration; no hours-long run against live national data has happened, because no
live relay exists. This cannot be closed on our side alone.

**6 — The window-close estimate is a guess, and it is disclosed rather than hidden.** The relay's
shape carries no explicit valid-time per period, so the room estimates a period's close as
`issued_at + (index+1) × 12 h`. That is a scheduling approximation. **It is not a statistic and
nothing archive-derived enters it** — the gate's condition 2 is intact — but it will mis-time
settlements at the margins, and the honest repair is for the relay to carry the real window.

**7 — 58 stations settle 3,771 zones.** The station half of the relay resolves a fixed list of major
airports, because this service publishes no bulk latest-observations endpoint. Nearest-station
matching will therefore sometimes answer a claim in Montana with a reading a long way off. Recorded
in the letter to the team as a defect in our half rather than as a reason to widen the ask.
