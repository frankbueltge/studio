# Neighbour search — session 98, 2026-08-16

Commissioned by the conductor at the concept gate, with an explicitly adversarial brief: *find
the works that already exist so the studio cannot claim novelty it has not earned.* Published
here **unedited**, exactly as returned, including the parts that damage the proposal — that is
the point of commissioning it.

Two of its load-bearing claims were re-checked first-hand by the conductor before this file was
written, because the concept's material rests on them. Both hold, and one of them is worse for us
than the report says. The check is recorded at the foot of this file, after the report.

---

# Neighbour Search: ClinicalTrials.gov Version-History Artwork

## 1. Artworks (versioning / diffs / revision history as material)

**James Bridle — "The Iraq War: A Historiography of Wikipedia Changelogs" (2010)**
Twelve bound volumes, ~7,000 pages, printing all ~12,000 edits to Wikipedia's Iraq War article, Dec 2004–Nov 2009. Decisive move: makes the *edit history itself* — not the article — the object, converting an invisible metadata trail into a monumental physical archive. Exhibited in galleries in the US and Europe. Closest antecedent for "versioning as material," but the form is static/print, not time-based or generative, and not about institutional promises or medical stakes.
URL: https://jamesbridle.com/works/iraq-war-wikihistoriography

**Fernanda Viégas & Martin Wattenberg — "History Flow" (IBM, c. 2003)**
Algorithmic visualization turning an article's full edit history into a single flowing, color-banded image (used first on Wikipedia's "chocolate" article, then broadly). Exhibited at MoMA, ICA London, Whitney. Decisive move: renders the *shape* of collaborative revision over time as a static print image. Direct ancestor of "revision-history-as-image" but not time-based/live, not about registry data.
URL: http://hint.fm/projects/historyflow/

**Hatnote (Mahmoud Hashemi & Stephen LaPorte) — "Listen to Wikipedia" (2013)**
Live, generative, unattended web installation: real-time Wikipedia edits become ambient sound (celesta for additions, clavichord for deletions) and an animated world map, color-coded by editor type. Won Silver, Kantar Information is Beautiful Awards 2013. Decisive move: exactly the proposed form — a public record visibly, continuously rewriting itself on a screen, unattended, generative, unfolding in real time. Content is unrelated (Wikipedia edits, not trial-outcome promises; no before/after revelation tied to withheld results).
URL: https://listen.hatnote.com/ ; https://github.com/hatnote/listen-to-wikipedia

**Ed Summers / GovTrack — "@congressedits" (2014)**
Bot that tweets anonymous Wikipedia edits originating from US Congress IP ranges. Decisive move: turns institutional edit-tracking into a public accountability feed. Text/social-media form, not a screen installation; content is political vandalism-watching, not amendment-of-promises.
URL: https://www.thewikipedian.net/p/congressedits-twitter-suspended ; https://botwiki.org/bot/congressedits/

**NewsDiffs (Jennifer 8. Lee, Eric Price, Greg Price, 2012)** — *not art*, included because it is the structural analog. Scrapes and diffs news articles (NYT, CNN, WaPo, BBC, Politico) over time to expose silent post-publication edits. Decisive move: the same "the current page lies about its own past" logic the concept proposes, applied to journalism instead of trials. No exhibition form.
URL: http://www.newsdiffs.org/ ; https://github.com/ecprice/newsdiffs

Checked, not close neighbours: Ben Grosser's surveillance-interface works ("ScareMail," "Tracing You") — about platform behavior, not record-versioning (searched "Ben Grosser artwork data surveillance revision"). Jill Magid's "Evidence Locker" — about personal surveillance-system relationships, not diffs or public registries (searched "Jill Magid artwork surveillance archive records artist"). "Political TV Ad Archive" (Internet Archive/Duplitron) — archives and fingerprints TV ad airings, not amendment/diff of a single evolving record (searched "'Political Ad Archive' Internet Archive project description"). Forensic Architecture — searched "Forensic Architecture clinical trial pharmaceutical drug," found nothing; their case work does not include a clinical-trial-registry investigation.

Searched and found nothing: "ClinicalTrials.gov 'history' API art project artist visualization NCT records"; "art installation drug trial data pharma transparency exhibition media art biennale"; "artwork data visualization clinical trials pharmaceutical registry"; "net art 'diff' artwork edit history generative screen unattended visitor watches records change." No artwork using ClinicalTrials.gov's version history, or clinical-trial data generally, as its material turned up in any search.

## 2. Non-art instruments already performing this measurement

**COMPare (Goldacre et al., CEBM/Oxford, 2015–2016)** — compare-trials.org. Checked all 67 trials published in the five top medical journals over a defined window against their pre-registered protocols/registry entries. Found each trial reported on average only 62% of its pre-specified outcomes and silently added 5.3 new ones. This is the foundational, already-public finding that "what a trial says it will measure" routinely diverges from what gets reported — but it compares *publication vs. protocol*, not the full chain of registry versions.
URL: https://www.compare-trials.org/

**EU TrialsTracker (Bennett Institute for Applied Data Science, Oxford)** — eu.trialstracker.net. Monitors compliance with EU rules requiring results within 12 months of completion, using EUCTR data. Per the page content fetched, it is a point-in-time compliance dashboard, not a version-history/diff tool — it does not track how records change over time.
URL: https://eu.trialstracker.net/about

**cthist R package (Benjamin Gregory Carlisle, Berlin Institute of Health, PLOS ONE, July 2022)** — this is the closest technical precedent to the artwork's proposed data engine. It programmatically walks ClinicalTrials.gov's (and DRKS.de's) full registry-entry version histories by version number to extract outcome measures, enrollment, dates, and status at each version — explicitly built to study outcome switching, recruitment-goal changes, and status drift over the life of a record. Notably, as of 2022 the paper states "the ClinicalTrials.gov API does not allow access to historical clinical trial registry data" — meaning it scrapes rendered history pages rather than a documented history API endpoint, which is worth checking against the `/history` endpoint the concept names (it may be newer/internal).
URL: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0270909

**Holst et al. — "Hidden changes to prespecified primary outcomes... in German University Medical Centres" (medRxiv preprint 2023; PMC10645365, 2023)** — this is the paper that most directly pre-empts the artwork's central "reveal." Sampling 292 trials from 1,746 completed at German university centres (2009–2017) and analyzing the *full registration history*, not just the latest version, they found primary outcomes differed from the registry's final entry in 41% of trials, with major, hidden discrepancies in 18% — discrepancies invisible if you only compare a publication to the current registry page. This is precisely the phenomenon ("no reader of the current page can see what it said before") already measured and published.
URL: https://www.medrxiv.org/content/10.1101/2023.02.20.23286182v1 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10645365/

**ClinicalTrials.gov's own "Record History" feature** — every study page natively exposes a `?tab=history` view listing every past version of the record (e.g., https://clinicaltrials.gov/study/NCT04296916?tab=history). This means the registry itself already publicly surfaces per-record version history to any visitor; the artwork's data-access claim ("publicly stores every past version") is not a discovery, it is documentation of an existing government feature.

**Earlier cross-sectional study (PMC4032105, 2014)** — "Funding source and primary outcome changes... associated with statistically significant primary outcome" — an earlier, independent finding that primary-outcome changes on ClinicalTrials.gov correlate with reporting significant results, reinforcing that this exact data source has already yielded this exact class of finding more than once.
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4032105/

## 3. Overlap of art + this instrument

Searched directly (see queries above) and found nothing: no artwork was found that uses ClinicalTrials.gov registry-version data, or clinical-trial data in general, as its material, and no work was found combining a "records rewriting themselves" form with pharmaceutical/medical registry content specifically. This is a genuine, verified gap — but it is a gap in *form applied to this content*, not a gap in the underlying finding (already published, see §2) or the generic form (already exhibited, see Bridle, Viégas/Wattenberg, Hatnote in §1).

---

## THE THREE NEAREST

**Headline: the finding is already published and the form is already an established genre — the concept's unclaimed territory is narrow: applying that exact live, unattended, generative "record rewriting itself" form to clinical-trial data specifically has not, as far as searching can verify, been done.**

1. **cthist (Carlisle, PLOS ONE 2022).** Daylight: it is a headless research package producing CSV-style datasets for scientists, with no visitor-facing, temporal, or exhibited form at all. No daylight: it already performs the artwork's claimed "machine advantage" — programmatically walking registry version histories at a scale no human could read by hand, on this exact data source, to detect outcome-measure changes — so the *method* is not new.

2. **Holst et al., German University Medical Centres study (2023).** Daylight: it is a peer-reviewed statistical paper (41%/18% prevalence figures), not an artwork, and makes no aesthetic or temporal claim. No daylight: the artwork's central dramatic premise — that reading only the current record hides amendments made after results were knowable, and that this is only visible via full version history — is already a quantified, published, citable finding, not an insight the work can claim to originate.

3. **Hatnote, "Listen to Wikipedia" (2013).** Daylight: entirely different content (Wikipedia edit events, not the amendment of a scientific promise) and no before/after "what did this used to say" revelation. No daylight: the proposed exhibition form itself — a live, generative, unattended screen/soundscape showing a public database rewriting itself in real time — is already built, awarded, and eight-plus years old as a genre convention; the studio cannot claim that form as novel, only its application to this content.

---

## The conductor's re-check of two load-bearing claims (2026-08-16)

Both were checked first-hand, because a concept gate may not rest on a sub-agent's report of a
fact it can verify itself.

**1. "The registry itself already publicly surfaces per-record version history to any visitor."
CONFIRMED, and it is the more damaging of the two.** `https://clinicaltrials.gov/study/NCT00884585?tab=history`
returns HTTP 200 and a 94,295-byte page. There is no lock to pick here. Whatever this concept is,
it is not an exposure: the keeper publishes the whole history, on the record's own page, to anyone.

**2. The cthist paper's 2022 remark about the API. CONFIRMED, and the report understates the
consequence for us.** `GET https://clinicaltrials.gov/api/v2/studies/{NCT}/history` returns **404**.
The history route this studio's capture uses lives in the `int` namespace —
`https://clinicaltrials.gov/api/int/studies/{NCT}/history` — which is not part of the documented
v2 API. It answered every one of tonight's requests, and it carries no stability guarantee
whatsoever. Any work built on it must freeze its own corpus and must never promise a visitor that
the route still answers tomorrow. This is written into the capture script's own docstring so it
cannot be lost.
