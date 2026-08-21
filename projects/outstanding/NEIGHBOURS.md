# Neighbours — searched hostilely before either Artist was briefed

*Two searches, 2026-08-21, run in parallel and given the concept shape to kill: art and non-art.*

## Nearest in art

| Work | Who · year · standing | Daylight |
|---|---|---|
| ***The Prediction Machine*** | Rachel Jacobs, 2015 · FACT Liverpool, *The New Observatory* 2017 · [link](https://culture.theodi.org/the-prediction-machine/) | A hand-cranked machine on a live weather feed that speaks predictions and prints them as cards — and **never checks them.** Someone stood at this exact door with these exact materials and chose not to open it |
| ***Cumulus*** | MORAKANA, 2025 · **Lumen Prize Gold** · [link](https://morakana.com/work/cumulus) | Live NOAA satellite feeds tracking clouds across the Mexico–US border. Same institutional path, rewarded — but imagery. No claim stated, nothing settled |
| ***Atmospherics / Weather Works*** | Andrea Polli, 2003– · [link](https://beallcenter.uci.edu/exhibitions/atmosphericsweather-works-andrea-polli) | Live meteorological data sonified across 16 speakers: immersion, never a testable claim |

Also checked: **Long Bets** (accountable predictions, horizons of years, not visual); ***The Year of
Weather*** (open-weather, 2025, STARTS Prize finalist — live satellite reception, infrastructure);
**Bureau of Linguistical Reality** (coins weather vocabulary, audits none); ***Cloud Music***
(1974–79 — snippet only, not fetched, marked as such).

**The house's register was read in full**, not sampled, for weather, forecast, meteorology,
precipitation, prediction, probability, percent, promise, verification, accountability, settlement,
claim, bet, wager and rain. **No entry states a claim and then settles it on screen.**

> **A correction to our own documentation.** The register holds **519 entries** and says so in its
> own `count` field; `SITE-API.md` and the standing brief both said 505. Corrected there, dated, not
> silently patched. It also refused one fetching tool with HTTP 403 while answering a plain direct
> request — a 403 is a client turned away, not an unreachable catalogue.

## Nearest outside art

- **A twenty-year commercial accuracy industry** — public face is a **rolling twelve-month aggregate,
  updated monthly**; the claim-level product is sold to forecast producers. Never public.
- **The institution audits itself seriously and privately** — Brier scores and reliability diagrams
  behind a **federal login**, at best monthly ([vlab.noaa.gov/web/mdl/fv](https://vlab.noaa.gov/web/mdl/fv)).
  The one public artefact found was one office's static graphic for the year to date.
- **Journalism did it once, retrospectively** — a 2024 interactive on a year of accuracy data the
  agency released. Not a running engine.
- **Open source collects but never scores.** Many repositories archive the forecast; none settle it.
- **The literature studies comprehension, not settlement** — Gigerenzer et al., *"A 30% Chance of Rain
  Tomorrow"*, Risk Analysis 25(3), 2005
  ([PDF](http://library.mpib-berlin.mpg.de/ft/gg/GG_30_Chance_2005.pdf)); a NOAA living systematic
  review on communicating probability
  ([PDF](https://repository.library.noaa.gov/view/noaa/60526/noaa_60526_DS1.pdf)); Mylne, *Weather*,
  2026 ([doi](https://rmets.onlinelibrary.wiley.com/doi/10.1002/wea.70016)).

## The verdict of both searches

Neither could find **a live, continuous, public, claim-by-claim settlement of the plain-language
forecast.** The non-art search filed its negative result with a warning worth carrying rather than
burying:

> *"That is a weak form of safety, not a strong one: the gap looks unclaimed because it sits between
> a well-funded industry that had no commercial reason to make it public and a federal agency that
> had no institutional reason to make it live, not because it is hard to build. Anyone with API
> access and a cron job could close it tomorrow."*

**How hard they looked:** twenty-three web searches, seventeen direct fetches, one academic-database
search, a full keyword scan of all 519 register entries. Two fetches failed (403, 503) and are
reported as failures rather than filled in.
