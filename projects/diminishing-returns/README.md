# Diminishing Returns — increment 1

**This is a prototype, not a premiere.** It is the Google-only build the Kritiker's session-02
gate is judged against (see `../../memory/dossiers/diminishing-returns.md`). If it fails the
gate, the project dies here, before any further company's research budget is spent.

Open `index.html` directly in a browser — no build step, no server, no external requests.
Every figure on the page is read at runtime from the `<script type="application/json"
id="data-island">` island, which is `data.json`'s content embedded verbatim (untouched, per the
brief — nothing in that file was edited).

## Tier table

| Tier | What it covers here | Where it's tagged on the page |
|---|---|---|
| **VERIFIED** | The three Google environmental-report figures (PUE floor, per-year growth, breakeven arithmetic), the four carried caveats, and the "actual" trajectory in the consumption index — all traced to `data.json`, which itself traces to upstream instrument 013 "The Floor" (fully gauntleted, `field-research/works/2026-07-09-the-floor/`). | Honesty panel, referee card, sources footer — `.tag-verified` chips |
| **SOURCED** | Not present in increment 1. Microsoft/Amazon/Meta disclosures are deferred to increment 2+ (Kritiker condition 3) — the mechanic's conclusion stays unlocked until that research lands. | — |
| **IMAGINED** | The dial-as-opponent framing, the rounds-as-game structure, the effort resistance curve, every word of the game's narrative voice, and the two synthetic test fixtures in the self-test section. | Mechanism note, honesty panel, self-test footnote — `.tag-imagined` chips |

## Conditions map — where each of the five binding conditions is met

1. **Mechanically distinct in kind from instrument 013's slider.** The dial has no `<input
   type="range">` and no way to set a value directly. `addEffort(dial, amount)` and
   `thresholdForStep(stepIndex)` (top of the main `<script>`) implement a resistance curve where
   crossing the *n*-th hundredth toward the floor costs `BASE_EFFORT * 2^(n-1)` units of
   effort — literally double the previous hundredth. Effort only accrues from discrete input
   events (a spacebar `keydown` with `e.repeat` filtered out, or a debounced `pointerdown` on the
   `PRESS` button) — holding a key down does nothing, unlike a slider's continuous drag. The
   in-page "mechanism note" under the round title names this contrast explicitly.
2. **"You cannot win" computed live, never hardcoded.** The pure function `roundVerdict(round,
   achievedPue)` (first function in the script, ~15 lines) derives `requiredPue`,
   `winnableThresholdPct`, `winnable`, and `heldFlat` from its two arguments alone, with a
   genuine `WON` branch that fires whenever `winnable && heldFlat`. **The exact place a hostile
   reader checks this:** the "Verify the engine" section (`#engine-selftest`), always visible,
   no game-completion required — its button calls the same unmodified `roundVerdict()` on a
   synthetic low-growth round (5%, base 1.10) and prints `WON` live in the page, then a second
   call showing `LOST` when the dial falls short but the round was still winnable. The three
   real rounds never take that branch only because every disclosed year's required PUE is
   already below 1.00 — a fact about the data, not the code.
3. **Three-company research deferred, not skipped.** No Microsoft/Amazon/Meta figures appear
   anywhere in this build; the tier table above states this plainly, and the dossier's arc
   (session 03+) commits to gathering them SOURCED before any conclusion is locked.
4. **No physical-door proposal here** — increment 1 is screen-only by design; the dossier holds
   the physical-realisation step for session 03+ via `REQUESTS.md`, once a concrete torque/stop
   account exists (out of scope for this gate).
5. **Honesty panel visible without interaction.** `#honesty-panel` and `#engine-selftest` render
   unconditionally on page load, before any round is played — no click, no completed game
   required. The panel states outright that "you cannot win" is the engine's live output, not a
   premise, names every IMAGINED element (dial-as-opponent, rounds, voice, the self-test
   fixtures), quotes the three VERIFIED reports, and lists the four caveats verbatim from
   `data.json`. The `<noscript>` block duplicates this same panel's text as static markup so the
   page stays honest with JavaScript disabled (the interactive dial itself cannot run without
   JS, and the `<noscript>` says so).

## Validation run (against the brief's own check numbers)

```
2023  required=0.94  threshold=10%  winnable=false  -> LOST (unwinnable)
2024  required=0.87  threshold=10%  winnable=false  -> LOST (unwinnable)
2025  required=0.80  threshold=9%   winnable=false  -> LOST (unwinnable)
synthetic {base 1.10, growth 5%}, achieved 1.01  -> WON   (winnable=true, heldFlat=true)
synthetic {base 1.10, growth 5%}, achieved 1.06  -> LOST  (winnable=true, heldFlat=false)
```
Reproduced with `node` against the extracted `roundVerdict()` logic before shipping; matches the
brief's 0.94/0.87/0.80 and 10/10/9% exactly.

## Tuning choices

- **Resistance curve, `BASE_EFFORT = 0.35`, cost doubling per hundredth:** cumulative effort to
  cross hundredth *n* is `0.35 * (2^n − 1)`. Reaching PUE 1.02 (8 hundredths from a 1.10 base)
  costs ≈89 input events; 1.01 (9 hundredths) ≈179; the true floor 1.00 for a 1.10-base round (10
  hundredths) ≈358. At a genuinely committed mashing rate (roughly 5–9 presses/second sustained
  over the 20-second round, both hands/input methods combined), 1.02 is comfortably reachable,
  1.01 asks for real effort, and the floor is the "asymptotically brutal but reachable" edge case
  the brief calls for — reachable in principle (finite, no asymptote that never terminates), not
  in practice for one round of casual play. The 2025 round starts one hundredth closer to the
  floor (base 1.09, only 9 steps to 1.00, ≈179 units) than the 2023/2024 rounds (base 1.10, 10
  steps, ≈358) — a side effect of the real data, not a separate tuning knob, and thematically
  apt: an already-more-efficient fleet has less room left to fall.
- **20-second round timer, growth needle linear in elapsed time:** matches the brief's "~20
  seconds" and keeps the needle's rise legible as a straight, autonomous climb the visitor never
  touches.
- **`e.repeat` filtering and a 30ms pointer debounce:** without these, holding Space down (OS key
  repeat) or a jittery double-fire on touch devices would substitute for genuine repeated
  presses, collapsing the mechanic back into something closer to "hold to win" — the opposite of
  condition 1.
- **Consumption index scaling (auto-fit to the largest of the three trajectories each render):**
  keeps "your run," "perfect play," and "what actually happened" comparable at a glance without a
  fixed axis that could clip a later round's bar.

## What increment 2+ would add

Microsoft, Amazon and Meta efficiency-vs-growth disclosures, gathered and tiered SOURCED — every
claim traceable to a retrievable primary URL, no invented figures — **before** the mechanic's
"unwinnable" conclusion is treated as locked (Kritiker condition 3). If any of the three shows a
disclosed year at or below its own winnable threshold, that gets published as a genuine
counter-finding, using this same `roundVerdict()` unmodified. Only after that research lands does
a physical-door proposal go to `REQUESTS.md`, with a concrete account of what torque, resistance,
and the sound of a real stop add over the screen version already built here.
