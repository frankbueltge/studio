# Diminishing Returns — increment 2

**This is a prototype, not a premiere.** Increment 1 (Google-only) passed the Kritiker's
session-02 gate (see `../../memory/dossiers/diminishing-returns.md`, "Verdicts"). This build
discharges the gate's three increment-2 obligations and extends the same unmodified engine to
three more companies' disclosures, gathered SOURCED per Kritiker condition 3.

Open `index.html` directly in a browser (or serve the folder statically) — no build step, no
external requests. Every figure on the page is read at runtime from the `<script
type="application/json" id="data-island">` island, which is `data.json`'s content embedded
verbatim — nothing in `data.json` was edited for this increment (it arrived already extended
with `sourced_companies`, conductor-owned).

## The four acts

| Act | Company | Rounds | Tier | Note |
|---|---|---|---|---|
| **I** | Google | 3 (2023, 2024, 2025) | VERIFIED | Carried unchanged from increment 1. |
| **II** | Meta | 2 (2023, 2024) | SOURCED | Runs closest to the floor of all four: winnability threshold 8% growth, total remaining headroom 7.4% — once. |
| **III** | Microsoft | 1 (FY2024) | SOURCED | Scope-mismatch and base-PUE-approximation asterisks sit on the referee card itself. PUE disclosed as WORSENING FY24→FY25 (1.16→1.17). |
| **IV** | Amazon / AWS | 0 — locked | LOCKED | Cannot be played: an efficiency ratio (1.14 as reported 2025) with no consumption figure means `required_PUE = base/(1+growth)` has no growth to divide by. Rendered with the same sober dignity as the playable acts — a finding, not an error. |

Acts play in sequence by default. `enterAct(idx)` (the act lifecycle function) unlocks the next
act's nav button (`#act-nav`, built by `renderActNav()`) once its predecessor is reached
(`state.highestActReached`); reaching Act IV for the first time sets `state.allUnlocked = true`,
after which every act tab is freely clickable — "selectable after first playthrough," per the
brief.

## Tier table — every figure, its tier, its caveat

| Company | Figure | Tier | Caveat |
|---|---|---|---|
| Google | fleet PUE, breakeven arithmetic, floor 1.0 | VERIFIED | Four caveats carried from `data.json.verified.caveats_carried` — not a concealment claim; owned-and-operated campuses only; 27%-vs-37% wording shift; per-year base discipline. |
| Meta | PUE 1.08 flat, dc electricity growth (+34.1%, +20.6%) | SOURCED | `data.json.sourced_companies.meta.caveats`: PUE scope UNCONFIRMED against the owned+leased electricity figure; "data centers total" combines owned+leased; closest to the floor (threshold 8%, headroom 7.4%, once). |
| Microsoft | global PUE (FY24 1.16, FY25 1.17), org electricity growth (+26.6%) | SOURCED | `data.json.sourced_companies.microsoft.caveats` + `pue_direction_note`: SCOPE MISMATCH (datacenter-only PUE vs org-wide electricity); base-PUE approximation (FY23 PUE undisclosed, FY24's own 1.16 used); fiscal not calendar years; PUE disclosed as worsening FY24→FY25. |
| Amazon/AWS | PUE as reported (2024: 1.15, 2025: 1.14) | LOCKED | `data.json.sourced_companies.aws`: report-year ambiguity (`pue_ambiguity`); no consumption disclosure found at the primary source (`consumption_disclosure`); `no_round` — the absence itself is the finding. |

## Obligation (a) — effort's causal weight is the felt center

- **Discharged on every referee card** via `#ref-dent-climb`, rendered first in
  `renderRefereeCard()` — before the base/growth/achieved/required rows and before the WON/LOST
  outcome. Computed in `endRound()`: `dent = indexNoEffort − newIndexYourRun` (the index-point gap
  your effort actually carved out of a hypothetical zero-effort baseline this round) and
  `climb = indexNoEffort − prevIndex` (the growth-only increase, holding PUE at base). Verified
  live: Google 2023 (base 1.10, growth 17%, dial mashed to the floor) prints "−10.6 points… +17.0
  points"; a round with zero presses prints "−0.0 points" — the formula degrades correctly to no
  effect when no effort is spent.
- **The end-of-act primary visual** is the existing three-trajectory bar chart in
  `#consumption-index` (your run / perfect play / as reported), now paired with a fixed thesis
  line (`.thesis-line`, always visible, not act-specific): *"The dent is the metric's whole
  remaining lifetime headroom — it spends once and does not repeat. The climb repeats every
  year."* The per-round caption (`renderConsumptionIndex()`) also states the dent and climb in
  words, not just as bars.
- Each act's consumption index resets to 100 independently (`newActRuntime()`) — four different
  companies' own baselines, not one combined economy.

## Obligation (b) — the honesty panel is load-bearing

- **A fixed, always-visible notice** (`#honesty-nudge`, `position: fixed; top: 0`) reads "This game
  computes; it does not assert — honesty panel below ↓" and anchor-links to `#honesty-panel`
  (`scroll-margin-top` set so the jump lands cleanly). Styled with a heavy ink background, paper
  text, and a solid danger-colored bottom border — a flat color block, deliberately not a
  gradient.
- **`#honesty-panel` itself is fully inverted** (`background: var(--ink); color: var(--paper);
  border: 4px solid var(--ink)`), unmistakably distinct from the plain, light-bordered
  `#sources-footer` and `#engine-selftest` directly below it, which are left deliberately
  un-inverted for contrast.
- **Content extended, not just restyled:** a new `<dl id="tier-legend-detail">` explains
  VERIFIED / SOURCED / LOCKED / IMAGINED in plain language; three new blocks
  (`#meta-caveats-list`, `#microsoft-caveats-list`, `#aws-caveats-list`) render each company's
  caveats verbatim from `data.json`, built by `renderStaticSourced()`.

## The winnability line and the pure function

Every referee card, every act, computes and shows its own line: *"This round would be winnable if
growth ≤ (base−1.0)×100 = X% — disclosed growth: Y%."* This comes from the same
`roundVerdict(round, achievedPue)` used in increment 1, **unchanged** — it only ever reads
`round.base_pue` and `round.growth_pct`, so it works identically for Google, Meta and Microsoft
rounds without modification. Per-company data is normalized into that shape by
`normalizeGoogleRound()` / `normalizeMetaRound()` / `normalizeMicrosoftRound()`; only the
normalization differs, never the verdict logic or the dial engine (`makeDial()`,
`addEffort()`, `thresholdForStep()`, `currentPue()` — all byte-identical to increment 1).

The self-test (`#engine-selftest`, `$('selftest-btn')`) now runs four cases through
`roundVerdict()`: the two increment-1 synthetic fixtures (WON, LOST) plus two real rounds pulled
straight from the data island — Meta 2024 and Microsoft FY2024 — both correctly returning LOST.

## Validation run

Extracted `roundVerdict()` verbatim from the shipped `index.html` and ran it under Node:

```
Google  [1.10, 17%] -> required=0.94  threshold=10.0%  winnable=false
Google  [1.10, 27%] -> required=0.87  threshold=10.0%  winnable=false
Google  [1.09, 37%] -> required=0.80  threshold=9.0%   winnable=false

Meta 2024:       required=0.896  threshold=8.0   winnable=false -> LOST (structurally unwinnable)
Microsoft FY2024: required=0.916  threshold=16.0  winnable=false -> LOST (structurally unwinnable)
```

Matches the brief's own check numbers exactly (Meta 0.896/8.0/LOST; Microsoft 0.916/16.0/LOST) and
reproduces increment 1's Google numbers unchanged. Also driven end-to-end in a real browser
(Playwright, headless): played all three Google rounds (one to the floor, two at zero effort),
Meta's two rounds, Microsoft's one round — confirming the dent/climb line, the tier tag, and the
Microsoft/Meta extra-notes lists all render on the referee card as required — then confirmed the
Act IV locked card's text, the act-nav auto-unlocking after reaching Act IV, and the in-page
self-test output byte-matches the Node run above.

## Judgment calls

- **"Actual" (as-reported) trajectory for Meta and Microsoft**, since neither publishes a field
  named `achieved_fleet_pue_that_year` the way Google does: Meta uses that year's own
  `pue_series` entry (flat at 1.08 both rounds, since Meta's PUE hasn't moved 2022→2024).
  Microsoft uses **FY25's** disclosed PUE (1.17) for the FY2024 round — deliberately, so the "as
  reported" bar shows the real, disclosed backslide (1.16→1.17) rather than silently repeating the
  base value.
- **Self-test achieved-PUE inputs** for the two new real-round tests pass `round.base_pue` itself
  as the achieved value (i.e., "if you hadn't touched the dial at all") — irrelevant to the
  LOST/WON branch here since both rounds are unwinnable regardless of `heldFlat`, but chosen for
  narrative honesty over an arbitrary number.
- **Per-act index reset to 100:** treated as required, not optional — Google's, Meta's and
  Microsoft's absolute consumption scales are incomparable, so a single running index across acts
  would misrepresent all three as one economy.
- **Act nav unlock rule:** acts unlock strictly in order until Act IV is first reached, then all
  four become freely selectable. This reads as "played in sequence (or selectable after first
  playthrough)" without building a full save/replay system, which felt out of scope for a
  prototype.
- **Microsoft's round year label** is kept as the raw `"FY2024"` string from `data.json` (not
  reformatted) so the fiscal-year caveat is visible in the data itself, not just in prose.

## What increment 3+ would add

**Premiere polish** — this build is still visually and mechanically a prototype: transitions
between acts are a plain button, not a scene change; the resistance curve and 20-second timer are
untuned for the shorter Meta/Microsoft rounds (a 16-hundredths Microsoft climb costs far more
effort than a Google round did, unexamined here); no sound, no larger-format presentation. The
physical-door proposal (Kritiker condition 4) stays parked in `REQUESTS.md` — it was never in
scope for increment 2, and a concrete torque/resistance/stop account for four companies' worth of
dials would need its own design pass, not a paragraph bolted onto this README.
