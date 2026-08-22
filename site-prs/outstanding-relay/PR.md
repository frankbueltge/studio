# The relay OUTSTANDING is held on — built, measured, and offered three ways

*Prepared by the studio, session 107, 2026-08-22. Not a patch to apply: a requirement, three
shapes it could take, and a working instrument to put behind whichever you choose.*

## What was asked last night, and what changed tonight

Session 106 asked for a scheduled job publishing two JSON files on the works origin, refreshed in
place every ten minutes or better. That request stands. **What has changed is that the studio has
now built the fetching half itself and measured it**, so nothing about this decision has to be
taken on an estimate.

`tools/relay.py` in the studio repository is complete, runs on the standard library alone, needs no
key and no account, and produces both files. Its measurements are in
`projects/outstanding/RELAY-MEASUREMENT.md`; every figure below comes from a run made tonight.

## The requirement, stated so it can be met without reading anything else

Two files reachable at same-origin paths — the work is written against
`/studio/relay/outstanding/forecasts.json` and `/studio/relay/outstanding/stations.json`, and that
prefix is a single constant we will change to whatever you prefer. Each must be **no more than ten
minutes old**. The gate refused sixty in advance and will not hear a waiver.

**One condition, and it is the only hard one: `forecasts.json` must be served gzipped.** Raw it is
**9,585,621 bytes**; gzipped, **370,588** — 25.9× — and 371 kB every ten minutes is unremarkable
while 9.6 MB is not. If gzip is impossible, a lossless de-duplication of repeated period text is
measured and ready (41–48 % off the raw bytes), but it changes the file's shape and we have not
applied it unilaterally.

## What a cycle actually costs, measured

| run | requests | bytes in | wall |
|---|---|---|---|
| cold | 183 | 8,690,140 | 14.0 s |
| incremental, 11.75 min later | 67 | 2,788,891 | 5.4 s |

The incremental run fetched exactly the seven offices whose issuance time had changed, and an
independent index diff over the same interval agreed: the same seven. So a ten-minute cycle is
**about 67 requests and 2.8 MB inbound**, roughly 400 requests and 17 MB an hour, against a public
service that returned no rate limit and no error across roughly 250 requests tonight.

## Three shapes, and which one we would choose

**A — a scheduled run that publishes the two files without rebuilding the site.** A direct upload
to the hosting platform, or any path that writes the two objects and nothing else. **This is the
one we would choose.** It is the only shape whose cost is the fetch itself.

**B — a scheduled workflow that commits the two files to the site repository.** We can hand this
over complete and it is the least new machinery. We also do not recommend it and would rather say
so than have it discovered later: at ten minutes it is **144 commits and 144 full site builds a
day**, for a file no page but this one reads. A starting point is in
`files/.github/workflows/outstanding-relay.yml`, written so it is easy to read and easy to refuse.

**C — a same-origin server route that fetches on demand behind a five-minute cache.** The best
cadence of the three and no scheduled job at all. It needs server-side execution on the works
origin, which we cannot tell from here whether you have. **If you do, say so and we will port the
instrument to it** — the parsing is about two hundred lines and we would rather write it twice than
have it drift.

**On the exfiltration guard, since C looks like a hole and should be argued rather than waved past.**
It is one, and it is narrow: the route would take no parameter from the page, so the page cannot use
it to reach an arbitrary host or carry anything outward. Two fixed upstream URLs, GET only, nothing
forwarded. `connect-src 'self'` stays exactly as strict as it is for the browser, which is where it
was doing its work.

## What we are not asking for

No CSP change. No new host in any policy. No key, no secret, no account. Nothing about this work is
blocked on anything else — if the answer is no, or is sixty minutes, the concept dies on our side
without argument, and we would rather that than ship it as playback.

## One thing you should know before deciding, because it is not in our favour

The station half of the relay currently resolves **58 stations** against **3,771 forecast zones**.
That is thin, and the work's nearest-station matching will sometimes settle a claim in Montana
against a reading a long way off. There is no bulk latest-observations endpoint on this service; the
only bulk feed we found is 54 MB, worldwide, and carries different units. **This is a defect in our
half, not a reason to widen the ask** — we are recording it here so the number does not arrive as a
surprise later, and it is the next thing we work on whichever shape you choose.
