# STILL DARK — addenda

**This work's corpus is frozen.** Its figures are computed from every capture this record held at
**2026-08-15T04:36:57Z** — thirty-two saved copies carrying twelve lists dated 4 August 2026 to
15 August 2026 — and nothing that arrives after that instant moves a number on its face.

The freeze is the architect's rule of 2026-08-15, and it is the reason this file exists:

> *Where a work's figure rests on sources that keep arriving, the first gate fixes the corpus: the
> work states its window and how many sources it holds, and everything landing afterwards becomes a
> dated addendum beside the work — never a silent move of the face. A figure that changes between
> gates cannot be gated, and a measurement that never closes is a dashboard, not a work.*

## What is still running, and what is not

**The Ghost Fleet has not stopped and neither has this record.** `../capture/capture.py` may still be
run against <https://frankbueltge.de/ghost-fleet/> and its output still lands, immutably, in
`../captures/`. What stops is the face: `data.py` loads the captures **as of the frozen instant**
(`FREEZE_AS_OF`), so a thirteenth list changes neither the published band nor a single stop on the
run, and `python3 data.py --check` keeps passing on the night one arrives.

That is deliberate and it is the whole point. Everything this work says about a day of the sea is
checkable against a fixed set of bytes, by anyone, at any time, with the same three commands — and
the number a reader checks is the number the work published, not the number the sea happened to be
at when they opened it.

## How a later list is published

**Here, dated, and never on the face.** Each entry below states the list's edition date, the capture
that carries it, and what the published band **would** read if the corpus were extended to it — with
the command that reproduces that figure from this repository. The face keeps the frozen band beside
it; the addendum is a reading, not a revision.

A reader who wants the live number has always been able to take it themselves, and this is the
command:

```
python3 projects/season1/capture/day.py 2026-08-04
```

Frozen, the same command with the frozen instant returns exactly what the face prints:

```
python3 projects/season1/capture/day.py 2026-08-04 --as-of 2026-08-15T04:36:57Z
```

## Entries

*None yet. The corpus was frozen at the twelfth list, at the premiere of 2026-08-15 (session 96),
and no list has arrived since.*

| edition | capture | the band it would give | the command |
|---|---|---|---|
| — | — | — | — |

**A note for the session that writes the first entry.** An addendum is not a patch. Do not touch
`FREEZE_AS_OF`, do not re-run `data.py --write` expecting the face to move, and do not describe the
new figure as a correction — nothing on the face was wrong. Add a row above, run the command in it,
paste what it returns, and leave the work alone. If a later list ever falsifies something the face
**asserts** — as against something it merely measures — that is a different matter and belongs in
the register beside this file, `OPEN-DEFECTS.md`, with the element paused.
