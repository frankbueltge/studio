# Sampled-frames harness (session 41, 2026-07-25)

Reproducible drives for the two probes, written for the session-41 sampled-frames pass — the
captures are timestamped still strips, not motion: no reader of these frames perceives
continuous movement, and the record must not call them a motion medium (Kritiker, session
41). Each
script opens its probe from disk in a headless browser, clears the probe's residue key so the
sitting starts at seat 47, performs the full interaction arc (Probe A: a three-round sitting,
drags event-driven against the probe's actual round state; Probe B: three press-hold-release
cycles plus one attempted press on the dead pane), and captures timestamped frames into
`frames-a/` / `frames-b/` beside a `manifest.json` recording only elapsed time and
mouse-button state per frame — the manifests deliberately carry no interpretive notes, so the
frames can be handed to a severed cold reader.

`cursor-overlay.js` is injected by both drives as a harness-side page script: it renders a
standard arrow cursor that follows pointer events, because a real desktop screen recording
shows the system cursor and headless screenshots do not. The probe files are untouched — the
session-41 evidence (README, "Session-41 evidence") depends on comparing cursor-less and
cursor-visible captures, and this overlay is how the cursor-visible condition was produced.

Run (requires a headless-capable browser driver for node; frames land beside the script):

```
node drive-a.js
node drive-b.js
```

Determinism: the probes are seeded (SEED 20260725) and the drives clear residue first, so a
run always reproduces the same sitting — Probe A ends with residue `{seat:47, family:1,
clauses:[2,2]}`, Probe B with `{seat:47, stage:2, pressIndex:3, dead:true}`, both with zero
console errors. The frame *timings* are schedule-sensitive on Probe A only in how they sample
the animation; the sitting itself is event-driven and cannot desynchronize (a fixed-schedule
first version did, under CPU contention — kept out of the record, the lesson kept in it).
