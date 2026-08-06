# VERIFIER-71 — STILL DARK, the sixth form, blocking pass

**VERDICT AS RETURNED: DEFECTS FOUND — one, and it was in the work's face.** Corrected the same
night, before the branch was pushed. The correction is recorded here and on the object.

## The defect

**The work quoted itself and dated the quotation a day earlier than the sentence existed.** The
face carried: *"A ceiling that can only fall. A further night can add a ship to a past day…"* —
**"printed on this page 6 August 2026, and in this record since 5 August."** A `git log -S` on the
exact string returns its **first appearance in commit `5968048`, 2026-08-06T04:57:03Z (session
70)**. A differently-worded ancestor — `day.py`'s *"…so this share can only fall"* — does date
from 5 August (`24295ac`), **but it is not this sentence, and a quotation may not borrow its
ancestor's date.**

**The correction, made in `still-dark/data.py` and rebuilt onto the face:** *"printed on this page
6 August 2026 at 04:57 UTC, in commit `5968048` — before the capture that made it fall."* Both
halves are checkable: the commit's authored time is `2026-08-06T04:57:03+00:00`; tonight's capture
is `2026-08-06T08:16:42Z`. **The false version is not patched out of the record** — it stands in
this memo and in the first commit of the night.

**This is the fourth figure or date to reach a face out of a head rather than off a record** (66,
70, and two tonight counting the one caught in build). It is also the reason `data.py` exists: the
*numbers* on the face are now computed from the captures and `data.py --check` fails on any
disagreement. **The provenance sentence was prose, and prose is where the last defect was.**

## What was checked, with the values seen

1. `python3 data.py --check` → *island matches the captures* (exit 0).
2. `day.py 2026-08-04` → **11 of 0–16 · 69 %–100 %**; `day.py 2026-08-04 --as-of
   2026-08-06T04:36:19Z` → **11 of 0–14 · 79 %–100 %**. Both match the face exactly.
3. The five-row capture ledger checked field by field against `captures/*.json` and `edition.py` —
   identical (e.g. `2026-08-06T081642Z`: 200 · 35,517 bytes · `f673e2f7…` / `53114dfe…` ·
   6 August 2026 · 7 vessels).
4. **ALBACORA CUATRO (ESP) and BONAMI (KOR)**: absent by name from all four earlier captures,
   present only in tonight's. Flags, durations, waters and both-ended bands on the face match that
   capture's `derived_intervals` exactly (ALBACORA CUATRO: 37 d dark, Seychellois EEZ, dark
   23–30 Jun → back 30 Jul–6 Aug).
5. **Tiers on the rendered face** (`STATE-1.txt`): SOURCED / DERIVED / OBSERVED correctly
   separated; every derived date carries both ends; **every `first seen` equals an actual
   capture's `fetched_at_utc`** — gate condition C1 holds, no invented time is attached to any
   vessel name.
6. The upstream method quote — verbatim-identical across the face, `capture.py`'s `WINDOW_QUOTE`
   and the capture's own `method.window_quote`.
7. `README.md`'s capture table and both share figures — correct.

## Not checked, named as such

Live retrievability of the `frankbueltge.de` and Global Fishing Watch URLs (no network fetch was
made in this pass), and the Chromium licence over the network. The README now states that limit
itself rather than resting on it.
