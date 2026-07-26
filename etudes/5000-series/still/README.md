# Still — session 45 (CONCEPT)

One frame, rendered from real data, looked at and fixed until it matched the
brief. This is the artefact; nobody had specified the form before this
existed, so the concrete values below are the Builder's choices, made and
recorded, not house standard.

## Re-running it

```
cd /home/user/studio/etudes/5000-series/still
NODE_PATH=/opt/node22/lib/node_modules node build.js
```

Reads `../corpus/entries.json`, filters to the 792 `CERTIORARI DENIED`
entries, writes `page.html` (the full rendered document — open it directly
in a browser to inspect), then screenshots it twice with Playwright/Chromium:
`still-1x.png` (2000×1250, deviceScaleFactor 1) and `still-2x.png`
(4000×2500, deviceScaleFactor 2). Chromium at `/opt/pw-browsers`, nothing
else required.

Every docket number and caption in the image is copied verbatim from
`entries.json` — 791 distinct real entries fill the grid, one more real
entry (`24-796`, `MISSOURI, ET AL. V. UNITED STATES`) sits on the ledge, and
the corresponding grid slot is left empty (the "gap"). No entry repeats, no
text is invented. The one string that legitimately repeats on every card is
`The petitions for writs of certiorari are denied.`, verbatim, as instructed.

## What I chose

**Typeface.** Liberation Mono (metric-compatible with Courier New; already
on the machine, no Inter/Roboto). Confirmed it actually resolved via
`document.fonts.check()` rather than trusting the CSS — it did. A monospace
reads as typed/administrative rather than designed, which matters for the
"working document, not memorial" instruction.

**Grid geometry.** 36 columns × 22 rows = 792 cells, matching the entry
count exactly (791 filled + 1 gap). Card unit 200×310px with a 12px gutter.
Card face `#eee6d5` (pale, warm, matte) on a khaki wall backing `#b8ae98`;
ink `#17130a` for the printed docket/caption, `#7a7462` for the repeating
sentence and ruled lines, both flat colors, no gradients. Each card carries
docket line (15px bold), caption line (12.5px bold, ellipsis-truncated if
longer than the card — same truncation the real object would need), the
repeating sentence (9px, grey), 6 faint ruled lines (`rgba(23,19,10,.16)`),
and a single centered foot rule near the bottom, unlabelled. A 3px flat
drop-shadow under each card stands in for the card sitting in a shallow
slot.

**The camera.** A single flat plane in real CSS 3D (`perspective`,
`rotateX`, `rotateY`, `transform-style: preserve-3d`) — no manual per-card
scaling; the browser's own perspective projection does the foreshortening,
so recession is a side effect of geometry, not an effect I painted on.
Final values: `perspective: 2600px`, `rotateX: 8deg` (a small standing-height
tilt — this reads as a wall, not a floor), `rotateY: -60deg` (the dominant
recession: the wall swings away to the upper left), pivoted from its own
bottom-right corner, which I then placed off-canvas at screen (2500, 1700)
so the near corner is comfortably past the frame and the far corner's
falloff still lands inside it.

**The ledge.** A flat khaki shelf (`#97896a` front edge) rendered as a
separate near-camera layer, not part of the 3D wall — physically it's an
object jutting toward the viewer, so it doesn't need the wall's perspective
distortion. One real card lies on it face-up, undistorted, at roughly 1.6×
the wall-card's near-field scale; a plain dark rounded-rect pen sits beside
it, off-center, with a small brass tip. The grid cell directly above the
ledge is left empty and rendered near-black (`#100e09`) with an inset
shadow — that gap and the ledge card are the only two asymmetric elements
in the frame, as instructed.

## What I actually saw, round by round

I rendered, read the PNG, wrote down what was wrong, and fixed it. This
took more than three rounds — the geometry fought back harder than
expected. Compressed history:

1. **First render**: recession ran backward (large/legible cards at the
   *top*, tiny ones at bottom-left) and a black wedge of bare background
   showed through the bottom-left corner where the rotated plane didn't
   reach the frame. Fixed the rotation direction; void remained.
2. **Second render**: fixed near/far to bottom-right/top-left as intended,
   but eliminating the corner void by brute-force scaling produced a
   composition zoomed in so far that only ~30 cards were visible — losing
   "hundreds of cards read as texture first," which is a more central
   requirement than a perfectly clean corner. Backed off.
3. **Third+ rounds**: worked out that the corner-pivot's `transform-origin`
   only stays visually fixed if `translateZ` is zero in that step of the
   chain (translateZ shifts the pivot itself once later rotations act on
   it) — once I pinned that down, I could hold the near corner in place,
   push it slightly off-canvas, and independently tune card size, rotation
   angle and perspective distance to trade off coverage against legibility
   gradient without the composition drifting unpredictably. Card size went
   through 168px → 220px → 340px → back to 200px: too small lost density
   at working scale, too large lost the "hundreds of cards" texture in
   favor of a handful of huge ones.
4. **Gap/ledge alignment** broke on almost every geometry change, since the
   gap's screen position is a function of the whole transform. I ended up
   debugging this by temporarily hiding the foreground ledge layer and
   flooding the gap cell red to find its actual screen coordinates each
   time, then moving the ledge under it — cheaper than reasoning about the
   matrix by hand.
5. **Final check**: a thin dark strip remains along the bottom-left edge
   where the plane's true corner still doesn't quite reach the frame. I
   judged it a floor-shadow read rather than a "black field" — it's a
   narrow strip at the base of the composition, not a dominant mass, and
   the stage background behind it is a warm dark brown (`#1c1a13`), not
   pure black. I would keep pushing on this with more time; see below.

## The five questions, answered from the rendered PNG

**1. Can you read real captions at the near edge?** Yes. Reading directly
off `still-1x.png`, bottom-right quadrant: **25-5471, LEE, JAKARI A. V.
UNITED STATES**; **25-5468, MOYLAN, ROBERT A. V. ILLINOIS**; **25-5108,
GRIFFITH, HOWARD V. NEW YORK**. Also clearly legible nearby: 25-5297 ELLIS,
CHRISTOPHER J. V. UNITED STATES; 25-5230 BRITO, VICTOR S. V. UNITED STATES;
25-5386 MARSHALL, AURELIAS V. DOUGLAS, WARDEN — well past twenty names are
readable without zooming if you keep going across the near third of the
frame.

**2. Does the repeating sentence read as a grey band, or noise?** Both,
depending on distance, which is what was asked for. On near/mid cards it's
readable text ("The petitions for writs of / certiorari are denied.") sitting
under the caption in visibly lighter grey. On the far third of the frame
(upper-left) individual letterforms are gone and it reads as a flat grey
horizontal band repeated card after card — texture, not noise; it doesn't
break down into speckle, it holds together as a band because every card's
sentence sits in the same relative position.

**3. Does the ledge card read as separate, and is the gap legible?** Yes to
both. The ledge card is undistorted, larger, and sharply in front of the
receding wall texture, with its own shelf and a cast shadow line under the
shelf's front edge — it doesn't get confused with the wall grid. The slot
above it renders as an unambiguous near-black rectangle, clearly the size
and shape of a missing card, not an artifact.

**4. Administrative or memorial?** Administrative. Flat cream and khaki,
no candle-warmth, no vignette, no symmetry, no black field dominating the
frame, horizontal and off-centre with real crop on multiple edges — it
reads as a filing wall mid-shift, closer to a card catalog or a DMV queue
than a memorial. The one thing that pushed toward solemnity in an early
draft was a large flat black rectangle behind the ledge, meant to stop the
wall from showing through the gaps between the card and the pen — at full
size it read like a plinth or a mourning backdrop. I shrank it to a tight
khaki-colored backing sized just to the card and pen (matching the shelf
material instead of going to black), which killed that reading; the
remaining dark elements are the single card-sized gap (correctly small and
specific, not a field) and a thin strip of shadow at the very bottom edge
of the frame. I'd call the concept cleared on this question, not marginally.

**5. Anything asked for that isn't there, or that I couldn't get right?**
Two honest gaps. First, the "cropped on three sides, plainly continuing
past the edges" is fully true on the top, right, and — functionally — the
left; the bottom edge instead shows a thin strip of the stage's dark
background rather than wall texture continuing to the frame edge. It's
minor at this size and reads as shadow rather than void, but it's not the
clean crop the brief describes, and if I kept iterating this is the first
thing I'd chase, probably by increasing the physical card grid's raw size
further rather than fighting the rotation angle. Second, I did not attempt
any texture/paper-grain rendering on the cards — they're flat CSS color.
The brief didn't ask for that explicitly ("ordinary stock, ordinary pale,
matte" is satisfied by a flat matte color), so I don't count it as a miss,
but it's the most obvious place a second pass would go before this stopped
being a first sketch.
