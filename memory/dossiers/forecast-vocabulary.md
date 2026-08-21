# Dossier — the vocabulary of the public forecast

*Opened collective session 105 (2026-08-21). A **finding and its instruments**, built in the order
this house named as its own gap: the finding first, the neighbours second, the form last. It is
banked here whatever the gate decides, because the finding is true whether or not a work is made
from it.*

## Why this material

Four concepts have died at the gate in a row. The first three died because the interesting act had
already been performed by someone else; the fourth died on the visitor — its stake could not reach a
stranger without a caption, and an unattended room forbids captions. So the search this time ran
against one added condition: **a stranger must already own the unit.** Nobody has to be told what
"a 30 percent chance of rain" is supposed to mean, and nobody can check it. That is a claim shaped
for a machine: a probability is unfalsifiable on any single day, and only repetition at scale
settles it.

## The corpus (VERIFIED, fetched first-hand 2026-08-21)

The United States National Weather Service **Zone Forecast Product** (ZFP) — the plain-language
forecast a member of the public reads — from the Iowa Environmental Mesonet's AFOS text archive,
`https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=ZFP<OFFICE>&sdate=..&edate=..&fmt=text&limit=9999`,
joined to hourly station precipitation from the same institution's ASOS archive,
`https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=<ID>&data=p01i&...`.

Six offices, chosen for climate spread, each read only in the one zone whose header names the
office's own city: Des Moines (DSM), Seattle (SEA), Miami (MIA), Phoenix (PHX), New York (NYC),
Denver (DEN). 2006–2026, sampled the 1st, 11th and 21st of each month.

- **432,928 forecast periods** reached; **190,110 numeric probability claims**; **334,912 claims
  settled** against the sky.
- **74 of 4,536 office-days (1.6 %)** were not answered by the archive and are counted as missing,
  not as empty.
- Of the periods reached, 77.4 % could be scored. The rest: **47,273** whose label is not one of the
  service's own twelve-hour blocks (ranges like "WEDNESDAY THROUGH SUNDAY", partial periods like
  "REST OF TONIGHT"), **50,182** whose block the station did not observe, **556** with an unreadable
  issuance line, 5 stale.
- Measurable precipitation is **≥ 0.01 inch**, the threshold the service states its own probability
  against. A block counts as dry only if at least nine of its twelve hours were observed.

## The service's own published mapping

From `https://www.weather.gov/hun/zfp_terminology` (read first-hand; the same table appears at
`https://www.weather.gov/bgm/forecast_terms`):

| PoP | expression of uncertainty | areal qualifier |
|---|---|---|
| 0 % | none | none |
| 10 % | ISOLATED or none | ISOLATED or none |
| 20 % | SLIGHT CHANCE | ISOLATED |
| 30–50 % | CHANCE | SCATTERED |
| 60–70 % | LIKELY | NUMEROUS |
| 80–100 % | **(none)** | OCCASIONAL or PERIODS OF |

The governing directive is NWS Instruction 10-503; its PDF was fetched but not readable as text, so
it is cited as existing and **not quoted**.

## The finding

**1. The record has no zero.** In 190,110 numeric claims the value **0 percent appears exactly zero
times**. The smallest number ever published is 10 (5.0 % of claims); the most common is 20
(27.7 %). Every stated value sits on the ten-point grid — not one claim off it.

**2. Certainty is nearly absent.** 80, 90 and 100 together are **4.5 %** of all numeric claims;
"100 percent" is **1.1 %**.

**3. The only way the record says "no rain" is to say nothing.** **223,632 periods (51.7 %)** name no
precipitation at all. Audited against a wider precipitation vocabulary than the one that selected
them, only 0.20 % were misclassified. Among those settled: **it rained anyway 6.35 % of the time**
(169,039 claims). One time in sixteen.

**That single figure is a pooled average and must never travel alone.** It is not one number but a
range and a gradient, and both are part of the finding:

| | silence, scored | rained anyway |
|---|---|---|
| Phoenix | 30,325 | **1.0 %** |
| Denver | 9,692 | 4.0 % |
| Seattle | 9,437 | 4.2 % |
| Des Moines | 49,256 | 5.7 % |
| Miami | 36,390 | 9.4 % |
| New York | 33,939 | **10.1 %** |

And silence has a shape in time. The same day: wrong **2.4 %** of the time (n = 19,075). One day
ahead: 3.7 %. Three days: 5.8 %. Five days: 9.0 %. **Seven days ahead: 13.9 %** (n = 6,775). Near
silence is fairly reliable; far silence is not, and the record marks the two identically.

**4. The numbers keep their promise.** Stated → observed, all offices, all lead times:
10 → 15.5 %, 20 → 26.8 %, 30 → 37.8 %, 40 → 45.7 %, 50 → 55.1 %, 60 → 64.9 %, 70 → 71.7 %,
80 → 83.8 %, 90 → 89.6 %, 100 → 94.3 %. At one day's lead the line is tighter: 10 → 10.6 %,
20 → 28.1 %, 50 → 58.5 %, 90 → 92.4 %, 100 → 97.0 %.

**5. The words run hotter than the mapping says — and this is one city's finding, not the nation's.**
Where the record gives a word and no number, and a precipitation noun attaches to that word:
**"likely" → it rained 77.3 %** of the time (n = 3,666; the table says 60–70), **"slight chance" →
29.1 %** (n = 3,013; the table says exactly 20).

**Scope, stated because it would otherwise be found later by someone else:** 3,535 of those 3,666
"likely" claims (96 %) and 2,697 of the 3,013 "slight chance" claims (90 %) come from **Seattle**.
That is not a sampling accident — it is finding (6) restated. The only place where a word regularly
stands alone is the office that never publishes a number, so the honest form of this finding is: *in
the office that gives its public no number, the words are worth more rain than the service's own
national table assigns them.*

**6. One office never states a number at all.** Seattle: **28,396 periods across 21 years, zero
numeric claims**, while 59 % of its periods name precipitation in words only. In Miami a number
appears in 62 % of all periods. Seattle's words settle at "likely" 77.3 % (n = 3,535) and "slight
chance" 27.7 % (n = 2,697). Checked beyond the one zone we read: whole Seattle bulletins for
2006-11-15, 2012-11-15 and 2019-11-15 were fetched and searched across *every* zone in them, and the
string "percent" does not occur once in any of the three. That office's own header states that
probabilities of measurable precipitation exist "for tonight, Thursday, Thursday night, and Friday"
— they are simply not in this product; a separate numeric product may carry them, and we have not
established which.

**7. Where the record pairs one word with one number itself**, the word that hedges least is the one
that holds: "likely" sits inside its published band 94 % of the time and "scattered" 96 %, while
**"slight chance" sits on its single published value 41 % of the time** and reaches 50 in 12 % of
cases — the same phrase covering a fivefold range.

## What is ours and what is not

**Not ours, and never to be presented as a discovery:** whether the numbers are calibrated is
settled science — Murphy & Winkler (1977), *J. Royal Statistical Society Ser. C* 26(1):41–47,
https://rss.onlinelibrary.wiley.com/doi/abs/10.2307/2346866; Bickel & Kim (2008), *Monthly Weather
Review* 136(12):4867–4881, https://journals.ametsoc.org/view/journals/mwre/136/12/2008mwr2547.1.xml
(**403 to us; SOURCED through https://en.wikipedia.org/wiki/Wet_bias, not read first-hand**) — and
it has been run commercially since 2004 by ForecastWatch, https://forecastwatch.com/. Our figures at
(4) reproduce that known result and are corroboration, not news.

**Also not ours:** that people misread "a 30 % chance of rain" as an area or a duration rather than a
probability at a point — Gigerenzer et al. (2005), *Risk Analysis* 25(3),
http://library.mpib-berlin.mpg.de/ft/gg/GG_30_Chance_2005.pdf. And the National Academies (2006),
https://www.nationalacademies.org/read/11699/chapter/6, states that the verbal categories are
interpreted by users across a wide range of probabilities.

**Ours, as far as two hostile searches could establish:** the count of the vocabulary itself — which
values the public record uses and refuses, what the words are worth when they stand alone, and that
the record's only "no" is silence. Neither search found this performed anywhere: not in the
verification literature, not in NOAA's own studies, not in journalism, not on GitHub or Kaggle, and
not in this house's register of 505 neighbouring works.

## The instruments, and the traps they carry

`tools/zfp_harvest.py` (fetch) and `tools/zfp_settle.py` (parse, join, settle). Four traps are
documented in them because each was found the hard way tonight:

1. The archive's date window is **half-open**: `sdate=X&edate=X` returns the string
   "ERROR: Could not Find" inside a 200 response.
2. Without `limit=9999` the archive returns **one product per call**. The first version of this
   instrument fetched a month at a time and silently kept the last bulletin of each month.
3. **"Chance" is boilerplate.** Every numeric period carries "chance of precipitation N percent", so
   counting that phrase as the categorical word "chance" reports the word in 100 % of numeric
   periods. The first pass did exactly this and its word/number pairing was noise.
4. **A likelihood word is not a claim about rain unless a precipitation noun attaches to it.**
   "Patchy" attaches in 12 % of its appearances and "widespread" in 32 %; the rest are fog and
   frost. A first pass scored "patchy → 8.8 % wet" and "widespread → 1.5 % wet" and both figures
   were about fog. Neither is reported here.

## This finding has NOT been independently re-derived

Say it plainly, because the next session must not assume otherwise. A verifying pass was convened to
re-derive three load-bearing figures from the same archives **with its own code and a different
sample** (the 5th, 15th and 25th of each month, against our 1st/11th/21st). It began by fetching
whole bulletins, reached 7.9 GB against a fixed disk allowance, was ordered mid-run by the conductor
to delete what it had parsed and sample days instead, complied — and was then **killed by a container
restart before it reported anything.** It produced no findings, so none are recorded here.

What stands in its place is weaker and is described exactly:

- the conductor's own first-hand measurement, with four instrument traps caught inside it (above);
- one genuinely separate check on finding (6): whole Seattle bulletins for three widely separated
  years fetched again and searched across every zone for the string "percent" — not one occurrence;
- a re-run on **held-out days the corpus never sampled** (the 5th and 25th, 2019–2021, all six
  offices), reported in the session 105 journal. This tests the *sampling*, not the *code*: it runs
  the same parser, so it cannot catch a parser error, which is precisely what the verifying pass
  existed to catch.

**An independent re-derivation is still owed on this material** before any figure here is put in
front of a stranger.

## Caveats that travel with any use of this finding

- A stated probability is for a **point in the zone**; it is verified here at one station inside that
  zone, which is the service's own definition but not the whole zone's weather.
- Where a period pairs a word with a number, the word may describe part of the period or one
  precipitation type while the number covers the whole period. Finding (7) is therefore about what
  the record *puts together*, not proof that a forecaster departed from the directive.
- The sample is three days a month, six cities. It is not the nation and does not claim to be.
- 2026 is a partial year.

---

## Addendum, 2026-08-21 (session 106) — the same record, read live

Session 105 measured this material as an **archive**. Tonight the conductor read it **live**, over
plain unauthenticated HTTP GET, and the archive's central findings reproduce on today's bulletins.
All figures below are first-hand, taken between 14:10 and 15:00 UTC on 2026-08-21.

- **126 forecast offices issue the Zone Forecast Product live** (`/products/types/ZFP/locations`).
  The archive read six of them; the live channel carries all of them.
- **Eight offices sampled, one current issuance each: 2,722 forecast periods, 960 numeric
  probability claims, 231 zone headers.** Sampled issuance times spanned 06:22 to 13:47 UTC — the
  offices re-draft on their own rhythms, not on a shared clock.
- **Seattle's live bulletin tonight: 442 periods, zero numeric claims.** The 21-year finding holds
  on today's paper.
- **Phoenix's live bulletin: 260 periods, 14 numeric claims.** The desert office states a number in
  5 % of its periods — consistent with, and not the same fact as, the 1.0 % wet-silence figure.
- Hourly station observations carry `precipitationLastHour`, `presentWeather` and a plain
  `textDescription`. One read tonight was timestamped 12:51 UTC.

### A fifth instrument trap, caught tonight

**The office code in this API is not the city's airport code.** The conductor's first live probe
asked for `PHX` and received an empty product list, which reads exactly like "this office has
stopped issuing the product". Phoenix's office identifier is **`PSR`**. The archive harvester
(`tools/zfp_harvest.py:46`) had it right; the live probe did not. The first totals published inside
this session — *"eight offices, 2,462 periods, 946 numeric"* — were in fact **seven** offices, and
are superseded by the eight-office line above. The extrapolation drawn from them (~40,000 open
periods and ~15,000 stated probabilities standing nationally at any moment) is unchanged by the
correction: 2,722 / 8 × 126 ≈ 42,900 and 960 / 8 × 126 ≈ 15,100.

### What the live channel does NOT give, and this is load-bearing

Measured, not assumed — see the session 106 journal for the numbers. The settlement of a forecast
claim does not arrive continuously. Station observations reach this API in an **hourly pulse**, and
a snapshot taken at 14:37 UTC found **not one** of 62 sampled stations carrying an observation
younger than 20 minutes; the median observation on hand was **67.5 minutes old**. Any work built on
"the sky answers while you watch" must be designed against that pulse rather than against an
imagined continuous stream.
