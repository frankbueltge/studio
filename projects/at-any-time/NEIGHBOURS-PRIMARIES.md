# NEIGHBOURS ON PRIMARIES — Docket items 10 and 11

Convened as an ephemeral research commission to close two numbered items on
the concept gate's docket (`GATE-DOCKET.md` §Part C, items 10 and 11). Every
claim below carries a URL opened tonight and a retrieval date. Where a route
failed, it is logged in the "tried and could not open" lists, honestly, with
the failure mode. Nothing here is retyped from memory of what a source
"probably says." Speculation is marked **IMAGINED**; there is very little of
it, on purpose.

Retrieval date for everything below, unless otherwise marked: **2026-07-31**.

---

## ITEM 10 — THE DARBOVEN / OPAŁKA DAYLIGHT, ON PRIMARIES

### What was tried, and what happened

**Opened successfully:**

| Source | URL | Route that worked | What it is |
|---|---|---|---|
| Hanne Darboven Foundation, via Sprüth Magers (the gallery holding "the exclusive privilege of working with the Hanne Darboven Foundation, the foundation entrusted with the artist's estate" — its own words) | <https://spruethmagers.com/artists/hanne-darboven/> | plain `curl` with a browser user-agent; the earlier `WebFetch`-style extractor was never even tried here, a direct request sufficed | foundation-authorised biography and works page |
| Roman Opałka, official artist website | <http://opalka1965.com/en/statement.php?lang=en> | plain `curl`; the site is a small non-JS PHP site and returned full text immediately | the artist's own first-person "Statement" on his method |
| Roman Opałka, official artist website, biography page | <http://opalka1965.com/en/biographie.php?lang=en> | same | dated biographical timeline in the artist's own materials |

**Reached (HTTP 200) but the substantive text was not obtainable — logged as NOT OPENED for the claims that would require it:**

| Source | URL | What happened |
|---|---|---|
| MoMA, artist page | <https://www.moma.org/collection/artists/1388> | HTTP 403 on both the extractor and a direct `curl` with a browser user-agent; the direct fetch returned a Cloudflare "Just a moment..." challenge page, not the content. **Not opened.** |
| MoMA, *Month III (March)*, 1974 | <https://www.moma.org/collection/works/95761> | Same Cloudflare 403 via the extractor. Not retried by direct `curl` once the pattern was confirmed on the artist page. **Not opened.** |
| Tate, artist page | <https://www.tate.org.uk/art/artists/hanne-darboven-976> | HTTP 200 by direct `curl`, but the server-rendered HTML is navigation chrome only; the biographical/catalogue text is injected client-side by JavaScript this tool cannot execute. The words "Hanne Darboven 1941–2009" and the title of one held work are visible; nothing else. **Reached, not opened** for any structural claim. |
| Tate, *Card Index: Filing Cabinet, Part 2*, 1975 | <https://www.tate.org.uk/art/artworks/darboven-card-index-filing-cabinet-part-2-t03410> | Same — HTTP 200, same JavaScript wall. No catalogue entry text recovered. **Reached, not opened.** |
| Guggenheim, *OPALKA 1965/1–∞ Détail 1520432–1537871* | <https://www.guggenheim.org/artwork/3331> | HTTP 200. Traced the page's own WordPress REST API link (`https://www.guggenheim.org/wp-json/wp/v2/artwork/133099`) and fetched it directly — the JSON came back, but the `content.rendered` and `excerpt.rendered` fields are both empty strings; the artist taxonomy record (`/wp-json/wp/v2/artist/7915`) has an empty `description` field too. The museum's public API confirms this record carries no curatorial prose at all, only image/attribution metadata. **Opened, and it is empty of the structural text sought** — a different finding from a 403, worth recording as such. |
| Dia Art Foundation | guessed URL `https://www.diaart.org/collection/collection/opalka-roman-1965-1-detail-2891799-2921553-1998-9` | HTTP 200 but the slug was wrong (the page returned is a generic, title-less collection shell). **Not opened** — this is a failed guess, not a verified fetch, and is logged as such rather than quoted from. |

No other museum or foundation candidates were tried tonight beyond these.

### Darboven — the structure, in the source's own words

From the Hanne Darboven Foundation's gallery page (opened above):

> "She came up with a specific way of doing cross-sum calculations that she
> used to convert the numbers of a given calendar date into individual
> digits. Afterwards, she converted those digits into increasingly elaborate
> visual form of writing that employed vectors, boxes or wavy lines."

> "Darboven embodied LeWitt's idea of the artist operating 'merely as a
> clerk cataloging the results of the premise' more consistently than any
> other conceptual artist of the day."

- **What determines a unit:** a calendar date, run through her own cross-sum
  arithmetic (elsewhere called the "K-value") to produce a number, which is
  then written out by hand in an invented notational script.
- **What determines when a unit is made:** not stated in this source. The
  text says her life was "devoted almost entirely to her work" but gives no
  protocol for a day she does not write. **NOT ESTABLISHED** from anything
  opened tonight.
- **What happens on a day she does not work:** **NOT ESTABLISHED.** No
  primary opened tonight addresses this.
- **Is content generated by the system or received from outside it:**
  generated. The cross-sum operation is deterministic and internal to the
  date; nothing external supplies content — the artist supplies only the
  hand that writes what the arithmetic already determined.
- **Can the work be completed:** yes, at the scale of an individual work.
  The Foundation's own listing shows bounded, closed pieces: *Weltansichten
  00–99* covers dated compositions across a fixed span (1975–80, per the
  gallery's dating) and *Kulturgeschichte 1880–1983* (1980–83) is a named,
  closed historical interval — she chooses the date-range in advance, and
  the piece ends when that range is exhausted. The *method* is generalisable
  indefinitely; each *work* is not.

### Opałka — the structure, in the artist's own words

From the artist's own "Statement" page (opened above), quoted directly:

> "The fundamental basis of my work, to which I have dedicated my life,
> manifests itself in a process of recording a progression that both
> documents time and also defines it. It began on a single date in 1965,
> the one on which I undertook my first 'Detail'."

> "I inscribe the progression of numbers beginning with one, proceeding to
> infinity, on canvases of the same size, 77.17 x 53.15 in (196 x 135 cm),
> in white by hand with a paintbrush. Since 1972 I have been making each
> canvas' background about 1% whiter each time. Thus the moment will arrive
> when I will paint white on white."

> "After each work session in my studio, I take a photograph of my face in
> front of the 'Detail' that I have been working on. Each 'Detail' is
> accompanied by a tape recording of my voice saying the numbers out loud
> as I write them."

- **What determines a unit:** a "Détail" — one canvas of fixed dimensions.
  It ends when the canvas surface is full of consecutively painted
  integers, continuing wherever the previous canvas stopped.
- **What determines when a unit is made:** studio work sessions, not
  calendar days. The unit boundary is physical (the canvas fills up), not
  temporal — a Détail is not "one per day."
- **What happens on a day he does not work:** **NOT ESTABLISHED** by
  anything opened tonight. The Statement describes what happens *after*
  each session (photograph, recording) but says nothing about a skipped
  session, and — structurally, this is the important part — nothing in the
  object itself would record a skipped day even if one occurred: the
  sequence is pure count (1, 2, 3, ...), with no date attached to any
  number, so an absence leaves no mark. The biography page (opened above)
  states only "1970 Sole and exclusive concentration on his work" — implying
  near-total daily devotion, not a documented protocol for absence.
- **Is content generated by the system or received from outside it:**
  generated — but by counting, not by any operation on the calendar. The
  next mark is always "the previous number, plus one." Nothing about which
  actual date it is enters into what gets painted.
- **Can the work be completed:** explicitly, no — "proceeding to infinity"
  is the artist's own phrase for the whole project (*Opałka 1965/1–∞*).
  Individual Détails complete (a canvas fills); the total work is
  constructed never to.

### The daylight argument, re-argued on these primaries — and where it changes

The proposal's sentence, cut at the gate for resting on encyclopaedia pages,
was: *"both systems generate their own content from time itself; this one
generates nothing and receives everything."* It was written to apply evenly
to Darboven and Opałka together. On primaries, it does not apply evenly, and
that unevenness is the finding worth having.

**Against Darboven, the daylight holds, and is now sharper than before.**
The Foundation's own language gives a precise mechanism — cross-sum
arithmetic applied to a calendar date — that is a stronger, more literal
instance of "generates its own content from time itself" than the
encyclopaedia page supplied. *AT ANY TIME* does no arithmetic on the date at
all: it does not compute anything from what day it is, it only checks
whether an external institution acted that day and, if so, reproduces
whatever that institution supplied. Darboven's number is a function of the
date; *AT ANY TIME*'s page is a function of the Court's discretion, with the
date serving only as an index, not an input. **This half of the daylight
argument does not get thinner. It gets more precise.**

**Against Opałka, the daylight sentence as written is imprecise, and this is
the correction owed.** Opałka's numbers are not calendar-generated at all —
his "time" is durational (a lifetime's accumulated sessions), not calendric
(a specific date's digits). His system does not know what day it is any more
than a page counter does; it only knows what the last number was. So the
proposal's claim that Opałka's system "generates its own content from time
itself" is true only in a loose, biographical sense (the project documents
the artist's lifespan) and false in the specific, calendar-indexed sense the
sentence needs to make the contrast with *AT ANY TIME* work cleanly — because
*AT ANY TIME* **is** calendar-indexed (one page per calendar day, blank or
carrying a sheet, keyed to the date), and Opałka's count is explicitly *not*
keyed to the date. Where Darboven and *AT ANY TIME* share an axis (the
calendar) and diverge on what happens along it (arithmetic vs. reception),
Opałka and *AT ANY TIME* do not share that axis at all — his sequence would
look identical whether or not calendar days ever existed. **Bundling the two
artists into one sentence is the actual defect, not the choice of either
artist.** The correct daylight against Opałka is a different one: *AT ANY
TIME* marks absence — a day with no Miscellaneous Order is a visible blank
page, the same size as every other page. Opałka's object has no equivalent
mark for a session that did not happen; a skipped day (if one ever occurred)
is structurally invisible in the canvases, leaving no blank Détail, no gap in
the numbering, nothing. The count would read the same whether he worked
every day of his life or missed half of them. *AT ANY TIME*'s blank pages are
its argument-that-is-not-an-argument; Opałka's medium cannot produce a blank
page at all — there is no unit-per-day to leave empty.

One further correction, on completion, not claimed by the original sentence
but implied by placing Opałka beside Darboven: **on the specific axis of
"can the work be completed," Opałka is not a contrast to *AT ANY TIME* — he
is close kin.** Both projects are explicitly, by design, unfinishable in
their totality ("proceeding to infinity" / grows by a page-height daily with
no terminus set). Darboven's individual works, bounded by a chosen date
range, are the ones that actually contrast with *AT ANY TIME* on
completability; Opałka does not.

**Verdict on thinness:** the daylight argument against Darboven survives
opening the primaries intact, and is better evidenced than before. The
daylight argument against Opałka, as the proposal phrased it (jointly with
Darboven, on the same sentence), does not survive — it needs to be split
into its own sentence, resting on a different mechanism (marked absence vs.
unmarked absence), because the "generates content from time" clause does not
actually describe what Opałka's primary source says his system does.

---

## ITEM 11 — THE SHADOW-DOCKET LITERATURE, OPENED

### (a) The coinage — exact citation and URL

**William Baude, *Foreword: The Supreme Court's Shadow Docket*, 9 N.Y.U.
J.L. & LIBERTY 1 (2015).**

Opened directly (full text, not abstract): <https://www.law.nyu.edu/sites/default/files/Baude%20JLL%20Shadow%20Docket%20-ia%20remediated.pdf>,
retrieved 2026-07-31, extracted with `pdftotext`. The header on every page
confirms the journal, volume and year ("*New York University Journal of Law
& Liberty [Vol. 9:1]*" / "*2015] FOREWORD*"). SSRN mirror, not independently
re-verified beyond the title match: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2545130>.

The coining sentence, quoted verbatim from the abstract, page 1:

> "The 2013 Supreme Court Term provides an occasion to look beyond the
> Court's merits cases to the Court's shadow docket — a range of orders and
> summary decisions that defy its normal procedural regularity."

Baude uses the phrase "shadow docket" only twice more in the whole piece (a
scan of the extracted text found three total occurrences), and once uses
lowercase "miscellaneous orders" informally (p. 38 of the piece, discussing
the same non-merits material) — not as a citation to the Court's own
docketing vocabulary, just as an ordinary English adjective. This matters for
(b) below.

### (b) How the literature defines the category — and whether it is the Court's own "Miscellaneous Order" label

It is **not** the same set, and the difference is load-bearing for this
work's rule.

Opened directly: **Jonathan P. Kastellec & Robin A. Taboni, "A Database of
the United States Supreme Court's Shadow Docket, 1993–2025," *Journal of Law
and Courts* (2026) 14:1, 220–237**, DOI `10.1017/jlc.2025.10011`. Canonical
URL (resolved from the DOI): <https://www.cambridge.org/core/journals/journal-of-law-and-courts/article/database-of-the-united-states-supreme-courts-shadow-docket-19932025/266C0FA883BE4120FB4F37D387EFC61E>;
PDF fetched directly at <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/266C0FA883BE4120FB4F37D387EFC61E/S2164657025100119a.pdf/database_of_the_united_states_supreme_courts_shadow_docket_19932025.pdf>,
retrieved 2026-07-31, extracted with `pdftotext`. Open access, CC BY 4.0.

Their opening line, quoted directly: **"The shadow docket is not a term that
is officially used by the Supreme Court."** They then lay out, and this is
opened and quoted, not summarised secondhand:

- **Baude's own definition** (narrow): "a range of orders and summary
  decisions that defy its normal procedural regularity" — which, in their
  reading, "certainly includes things like summary reversals and cases on
  the Court's 'emergency docket'... But it would exclude more routine
  actions the Court takes in non-merits cases, including cert denials,
  inviting the solicitor general to file a brief, and grant, vacate, and
  remands (GVRs)."
- **Vladeck's definition** (broad), quoted by Kastellec & Taboni and marked
  here as a quotation-within-an-opened-secondary-source, since Vladeck's own
  2023 book was not independently opened tonight: "the entire body of
  decisions the Supreme Court hands down through 'orders' — which includes
  not just rulings on applications, but also rulings (1) granting or
  denying certiorari/leave to file an 'original' suit; and (2) respecting
  motions (like motions to recuse)."
- **Kastellec & Taboni's own working definition**, adopted for the database
  itself, broader still: "any order or decision the Court makes except the
  opinions in full merits cases."

None of these three is the Court's own printed label. The Court's own
category — the one *AT ANY TIME* actually uses — is narrower and purely
administrative: an order "issued in individual cases at any time," off the
Monday order list (`https://www.supremecourt.gov/orders/ordersofthecourt/25`,
already opened and quoted elsewhere in this project's material,
`MATERIAL-2026-07-31.md`). It says nothing about transparency, doctrine, or
procedural regularity — it is a scheduling/publication label, not an
analytic one.

The disjunction is measurable from data actually opened tonight. Kastellec &
Taboni's own table (their Table 1, quoted below) shows their broad
"shadow docket" is overwhelmingly certiorari traffic:

> "Perhaps not surprisingly, cert petitions are easily the modal category,
> comprising about 56% of all shadow docket actions" — Certiorari:
> 211,898 actions, out of a dataset that "exceeds 370,000 orders."

The great bulk of what scholars count as "shadow docket" is exactly the
Monday-order-list cert traffic that *AT ANY TIME* deliberately **excludes**
by design (`GATE-DOCKET.md` line 294: "off its calendar" is the whole
premise). Conversely, the material *AT ANY TIME* actually shows — individual
stay and injunction orders, including stays of execution — is a small
fraction of the scholars' category by their own count: **Stay: 2,878**,
**Injunction: 106**, against 370,000+ total actions, well under 1% each. So:
the Court's "Miscellaneous Order" label (this work's rule) and "the shadow
docket" (the scholarship's category) overlap heavily in the cases that draw
public attention, but are not coextensive sets — the scholarly category is
mostly the mundane cert traffic the work throws away, and the work's
material is a small, high-drama slice of the scholarly category. **Whether
the Court's own "Miscellaneous Order" documents correspond one-for-one to
any single section of the underlying "Journal of the Supreme Court" that
Kastellec & Taboni parsed is NOT ESTABLISHED tonight** — that would require
opening an actual Journal PDF and comparing section headers line by line
against the orders/ordersofthecourt page, which was not done this session.

### (c) Two to three central claims of the scholarship

**Baude (2015)**, quoted directly from the abstract of the opened PDF:

1. "Many of the orders lack the transparency that we have come to
   appreciate in its merits cases. Some of those orders merit more
   explanation, and should make us skeptical of proposals to depersonalize
   the Court."
2. Summary reversals split into "two main categories — a majority that are
   designed to enforce the Court's supremacy over recalcitrant lower
   courts, and a minority that are more akin to ad hoc exercises of
   prerogative, or 'lightning bolts.'"

**Vladeck (2019)**, opened directly: **Stephen I. Vladeck, "The Solicitor
General and the Shadow Docket," 133 Harv. L. Rev. 123 (2019)**. PDF opened
at <https://harvardlawreview.org/wp-content/uploads/2019/11/123-163_Online.pdf>,
retrieved 2026-07-31, extracted with `pdftotext`.

3. Empirically: the Solicitor General under the Trump Administration "filed
   at least twenty-one applications for stays in the Supreme Court
   (including ten during the October 2018 Term alone)," against a total of
   "eight such applications" across the full sixteen years of the Bush and
   Obama administrations combined — quoted directly from the text. His
   normative conclusion, quoted from the piece's final paragraph: the shift
   has occurred "without any visible backlash," and "we should all have
   common cause in encouraging the Court to formalize any such shift — and
   to bring it out of the shadows."

### (d) Has anyone already made this into a cumulative body, tracker, or artwork?

**Yes — several times over, and this is the inconvenient finding the gate
needs.** No artwork was found (a direct search for "shadow docket" combined
with "artwork," "art project," "visualized" returned nothing on point — see
below); but data trackers, plural, already exist:

1. **Kastellec & Taboni, "Supreme Court Shadow Docket Database"** (cited
   above) — a genuine cumulative academic database, opened and confirmed:
   "more than 265,000 actions on 220,000 unique dockets," "exceeds 370,000
   orders," covering the 1993 through 2024 Terms, downloadable with a
   codebook. Website opened directly: <https://www.shadowdocketdata.com>,
   retrieved 2026-07-31 — confirmed live, states "The Supreme Court Shadow
   Docket Database provides the first comprehensive dataset on the Court's
   use of the shadow docket. The database contains information on every
   order the Court issued between the 1993 and 2024 terms." Also archived
   at Harvard Dataverse (URL given in the paper's acknowledgments,
   `dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/89VEX8`
   — not independently opened tonight, logged as such).
2. **Shadow Docket Watch**, opened directly: <http://shadowdocket.net/>,
   retrieved 2026-07-31. A live, apparently continuously updated public
   table, confirmed with entries dated as recently as July 27–28, 2026 at
   the time of retrieval: docket number, case name, action type ("Stay,"
   "Extend deadline"), filing date, assigned Justice, and disposition,
   filterable by term and by Justice. This is the closest existing neighbour
   to *AT ANY TIME*'s underlying data — a running, docket-by-docket record
   of the same individual-case emergency orders — though presented as a
   searchable table for researchers, not as a spatial or temporal object.
3. **Brennan Center for Justice, "Supreme Court Shadow Docket Tracker —
   Challenges to Trump Administration Actions,"** opened directly:
   <https://www.brennancenter.org/our-work/research-reports/supreme-court-shadow-docket-tracker-challenges-trump-administration>,
   retrieved 2026-07-31 — page confirmed to exist and load (HTTP 200), title
   confirmed; the tracker's table content itself is rendered client-side and
   was **not** extracted, so its contents beyond the title are **not
   opened**.
4. **SCOTUSblog, "Interim Docket"** series, opened directly:
   <https://www.scotusblog.com/case-files/emergency/emergency-docket-2025/>,
   retrieved 2026-07-31. Confirmed text: "The Supreme Court's interim relief
   docket, also known as the emergency docket or the shadow docket, consists
   of applications seeking immediate action from the court... This page
   shows significant applications that have been filed during the term,"
   with a live count ("4 Pending," "50 Decided") at retrieval. This is a
   curated (not exhaustive) journalistic running list, per term, going back
   several years by URL pattern (`emergency-docket-2023`, `-2024`, `-2025`
   all found).

**Search for a prior artwork, run and returned nothing:** a search for
`"shadow docket" artwork art project visualized` returned only unrelated
craft-project results (shadow-puppetry and shadow-drawing tutorials for
children) — no hit naming the shadow docket as subject of a visual-art or
gallery project. This is a negative result from one search session, not
proof none exists; it is reported as what was found, not as a certainty.

### Does the scholarship's existence strengthen or weaken this work's claim to a finding of its own?

Tested honestly, the answer splits along exactly the line the proposal drew,
and the split holds on primaries — but one sentence already on this docket
needs to be withdrawn.

**On "the scholarship argues, we only show": holds, and is now better
evidenced.** Every piece of scholarship opened tonight ends in an argument
and a recommendation — Baude closes urging that the Court's summary-reversal
selection "could be rendered fairer"; Vladeck closes calling on the Court to
"formalize any such shift... and bring it out of the shadows." *AT ANY TIME*
recommends nothing and reforms nothing; it reproduces the Court's own sheets
unaltered and leaves the blank pages blank. That contrast is not weakened by
opening the primary literature — if anything, reading the actual conclusions
(rather than an encyclopaedia's summary of them) makes the contrast more
concrete: these are pieces built to end in a policy ask, and this work is
built not to.

**On "nobody has made the shadow docket into an extent": does not hold, and
must be corrected.** `GATE-DOCKET.md` line 258 currently states "Nobody has
made the shadow docket into an extent." That sentence is now contradicted by
what was opened tonight. Kastellec & Taboni's database and Shadow Docket
Watch's running table are both, in plain terms, exactly an extent of the
shadow docket — cumulative, chronological, docket-by-docket. The honest
narrowing of *AT ANY TIME*'s claim is therefore not "no one has aggregated
this material" (false, as of tonight's opening) but something more specific
and still defensible: **no one has aggregated it as a spatial/temporal object
built to be walked and read by a body, rather than queried as a table.** The
trackers are databases meant for filtering, sorting, and research; *AT ANY
TIME* is a fixed physical or durational sequence meant to be encountered in
order, at the pace of its blank days, with no filter and no search box. That
is a real and much narrower claim than "first to collect this," and it is
the one this work can actually still make after tonight's reading. The gate
should record that the wider claim was wrong and has been replaced by the
narrower one, not that the wider claim survived.

---

## Summary of everything tried and not opened tonight (both items)

- MoMA collection pages for Darboven (artist page and one specific work) —
  Cloudflare 403 on both the extractor and a direct browser-UA `curl`.
- Tate artist page and one Tate artwork page for Darboven — HTTP 200 reached,
  but catalogue/biographical text is client-side rendered and was not
  recovered; only navigation chrome was opened.
- Guggenheim artwork record for Opałka — HTTP 200, and its own WordPress
  REST API was traced and queried directly, but the API confirms the
  content and excerpt fields are empty; there is no curatorial prose to
  open at this specific record.
- Dia Art Foundation — a guessed URL for a specific Opałka *Détail* returned
  HTTP 200 but was the wrong page (a generic, untitled collection shell);
  not used for any claim.
- Vladeck's 2023 book, *The Shadow Docket* — not independently opened
  tonight; the one Vladeck quotation used here is sourced from Kastellec &
  Taboni's opened paper, and is marked as a quotation-within-a-secondary
  source rather than a primary opening.
- Harvard Dataverse listing for the Kastellec & Taboni dataset — URL
  recorded from their paper's acknowledgments but not independently fetched.
- Brennan Center tracker's actual table contents — page opened (HTTP 200,
  title confirmed) but the table itself is client-rendered and was not
  extracted.

## IMAGINED

Nothing in the factual material above is marked IMAGINED — every structural
claim traces to an opened URL, quoted directly, or is marked NOT ESTABLISHED.
The only speculative element is interpretive, not factual: the characterisation
of *why* Opałka's absence-marking and Darboven's date-arithmetic diverge
structurally (the paragraphs under "the daylight argument, re-argued") is this
researcher's own analysis built on the quoted primaries, not a claim any
opened source makes explicitly. It is reasoning from what was opened, not a
new fact, but it is fair to flag as constructed rather than found.
