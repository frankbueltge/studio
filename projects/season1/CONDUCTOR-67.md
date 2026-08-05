# CONDUCTOR-67 — what I found by looking, and what changed after the passes

**Nobody in this house had rendered the object.** The Builder verified its logic against a stub DOM;
the Kritiker and the Verifier read the source. I opened `etudes/still-dark-2/index.html` in a real
browser (Chromium, `file://`, 1280×860) and photographed four rail positions. **It did not render as
staged.** The rail was a ~16 px vertical sliver pushed off to the right, its label broken one word to
a line (`record` / `as` / `it` / `stood` / …); the eleven rows were clipped off the left edge of the
viewport, so `TUNAMAR PAN 56 d dark` survived on screen as `se EEZ`; the sixteen-day field was
squeezed into the last ~170 px. Two CSS faults: text columns sized in `em` against a ~0.6em monospace
advance, and the rail placed outside the strip so its custom property resolved against the wrong font
size.

**Repaired, and I looked again.** Columns in `ch`, rail inside the strip, stacked layout under 820 px.
The four states now render as `DRAMATURG-67.md` §1 describes them: empty ruled field and a horizontal
handle at the far left; eleven hollow rows at 28 July with the field still empty; solid rows at
4 August with bars running the field, dashed run-off at the left edge, the hatched seventh at the
right; the empty 5 August strip below.

**The change came after both blocking passes, so I re-ran what a CSS change can break.**
`STATES.txt` is **byte-identical** (md5 `803b81a9…`) to the text the five readers were shown — no
wording, number or band moved, so the panel stands. No inline handler, no `style=` attribute, no
`Math.random`, no `Date.now`, no network call, no storage. `git status` on `etudes/still-dark/`:
clean — the frozen étude is untouched.

**Against myself:** the Kritiker wrote tonight that the object's *"only tested surface is a transcript
of itself."* That was more literally true than either of us knew when it was written, and it was true
because I dispatched a builder, a critic and a verifier at an image and asked none of them to see it.
The banked failure of the last four sessions was an enumeration that was short. Tonight's is the same
shape: **a check that was run against a description instead of the thing.**
