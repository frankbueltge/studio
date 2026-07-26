# VECTOR 3 — **THE SAME SENTENCE**

*Season One "By Procedure" · first campaign · third vector · concept phase, session 46 (2026-07-26).*
*A working document for a hostile gate. Nothing here is a pitch. Two vectors are dead on two
consecutive nights; this one is written to be killed on its weakest joint, which is named at the
foot and not hidden in the middle.*

---

## 0 · What I verified first-hand tonight before writing a line

Per *pages, not premises*. The source PDF was re-fetched to the scratchpad, `sha256sum` run, the
in-house extractor re-run over it, and every count below re-derived from that extraction — not read
out of this house's own files.

- SHA-256 `354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652` — matches the record.
- `"The petitions for writs of certiorari are denied."` — **count = 1** in 39 pages.
  `"in forma pauperis"` (whitespace flattened) — **14**, all denials or revocations.
  `"petition for a writ of certiorari is denied"` (singular) — **11**.
- 882 entries; 792 CERTIORARI DENIED; 545 of the 792 (68.8 %) in the 5000-series.

**And one correction to the brief I was handed, derived first-hand and load-bearing for the whole
proposal.** The conductor's late note says the single sentence sits "after all 792 docket numbers
and captions have been printed." It does not. Counted on the extraction:

> **761 dockets are printed before the sentence. 31 are printed after it — and each of those 31
> carries prose of its own.**

The section header `CERTIORARI DENIED` appears on page 4. Twenty-eight page boundaries later, after
761 names in unbroken silence, comes the one sentence. Then the document keeps going for 31 more
entries, and *those* people get sentences written about their cases individually: a motion to
substitute a deceased respondent; a sealed brief in opposition; three recusals; eight orders denying
leave to proceed *in forma pauperis* under Rule 39.8; four orders directing the Clerk to refuse any
further filings from a named petitioner without the fee.

That is the material's real shape, and it is better than the shape the brief assumed:

**761 people share eight words. 31 people get paragraphs. The paragraphs are mostly about taking
something away.**

Corpus structure, re-derived (decision (b) raw material). Eight blocks, seven transitions — and the
transitions are not all of one kind, which the brief's "alternating term-block by term-block" does
not capture:

| # | block | index range | n | first entry |
|---|---|---|---|---|
| 1 | paid | 0–139 | 140 | `24-796 MISSOURI, ET AL. V. UNITED STATES` |
| 2 | IFP | 140–393 | 254 | `24-6750 RAMBARANSINGH, TROY V. BANK OF AM. NAT. ASSN., ET AL.` |
| 3 | paid | 394–491 | 98 | `25-4 MARSHALL, PRESTON L. V. COOK, STEPHEN D.` |
| 4 | IFP | 492–760 | 269 | `25-5001 AUSTIN, CLARENCE V. CT OFFICE OF CLAIMS, ET AL.` |
| — | **THE SENTENCE** | after 760 | — | *covers blocks 1–4: 761 entries* |
| 5 | paid | 761–763 | 3 | `24-948 GUERRERO, CHIEF JUSTICE, ET AL. V. REDD, STEPHEN M.` |
| 6 | IFP | 764–776 | 13 | `24-7126 LETTIERI, DAVID C. V. USDC ND NY` |
| 7 | paid | 777–782 | 6 | `25-16 KLAYMAN, LARRY E. V. JUDICIAL WATCH, INC., ET AL.` |
| 8 | IFP | 783–791 | 9 | `25-5011 EZEANI, GREGORY I. V. JIMENEZ, OFFICER, ET AL.` |

So: **three transitions inside the silent mass; the sentence; four transitions inside the tail of
individually-worded orders.** Last entry: `25-5378 SMITH, SAMUEL L. V. SLIMAK, MARK H.`

**A second thing I found tonight that neither previous vector had, and that changes what is
possible here.** Every docket in the corpus has a public docket page at
`https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/<docket>.html`.
I fetched five, paid and IFP, including the corpus's first IFP entry. `24-6750` returns: the
petitioner's full name (not the abbreviated caption), the lower court (District Court of Appeal of
Florida, Fifth District), the decision date, the rehearing date, the conference distribution
history, **and public PDFs of the petition itself, the appendix, the proof of service, and the
motion for leave to proceed in forma pauperis** — the person's own account, in their own words,
including their own account of being unable to pay. It also records that two respondents *waived
the right to respond.*

This matters more than any count in the record so far:

> **The reason is not missing for want of a record.** The Court holds the petition, the appendix,
> the service, the poverty motion, and publishes all of it. Then it disposes of the case in a
> sentence it shares with 760 other people. This is not Ọnụọha's blank spot. It is a full folder
> with an eight-word cover on it.

---

## 1 · The work

**Name: THE SAME SENTENCE.**

It is one page, and it is the document.

A stranger opens it. Paper-coloured ground, black serif, a single narrow column of type in a wide
margin — the proportions of a court order list, because that is what it is. At the top of the
column there is **no title, no heading, no explanation.** There is a name:

```
24-796    MISSOURI, ET AL. V. UNITED STATES
24-857    ESTRADA, BRIAN V. SMART, JACOB
24-919    MILLER, MIKE V. ROCK, DILLON
24-970    LUNA, DAGOBERTO V. BONDI, ATT'Y GEN.
```

and then 788 more, in the Court's own sequence, in the Court's own words, unaltered. Nothing else
is on the page. Every name is a link to that case's own public docket on the Court's site; nothing
marks them as links — no underline, no colour, no icon — they are simply live, the way a citation is
live.

The docket numbers are set in one saturated ink for the 5000-series and in black for the rest. No
key, no legend, no label. Seven in ten of the numbers are the other colour, so the *texture* of the
column carries the proportion before a single name has been read.

The stranger scrolls. This is the whole instrument.

### The first minute, second by second

- **0–3 s.** A column of names. No title. The cold read is *this is a list, and it is a real one* —
  the register is document, not website. Nothing invites; nothing announces.
- **3–8 s.** They read two or three. `LUNA, DAGOBERTO V. BONDI, ATT'Y GEN.` `MILLER, MIKE V. ROCK,
  DILLON.` Real names of real people against a state or an official. No subject, no court, no
  outcome, no date. The gap opens here and it never closes: **there is nowhere on this page where
  anything is explained about anyone.**
- **8–25 s.** They scroll, and it does not end. The column runs about 11,000 pixels. The colour
  changes character at index 140 and floods: from `24-6750` onward, for 254 consecutive entries, the
  numbers are the other ink. They do not know what it means. They keep going because the only way to
  find out what this is, is to reach the bottom of it.
- **25–45 s.** They accelerate. They are now skimming past people at forty a second. **This is the
  work's first completed act and they do not know they have performed it.**
- **~45 s.** The column stops. Under the last of them — `25-5543 BROOKS, ALTONY V. JOHNSTON, SGT.,
  ET AL.` — set larger, indented as the document indents it, in the same serif:

  > The petitions for writs of certiorari are denied.

  One sentence. That is the entire disposition of everything they have just scrolled past. The
  arithmetic lands without a word of ours: *that was 761 people, and this is eight words, and I read
  it faster than I scrolled them.*
- **~50 s.** Directly beneath the sentence, at the same left edge and the same measure: a hairline
  rule and a caret. No box, no button, no placeholder text, no label, no name field, no counter. It
  is live and it is unmanned. It is the position the Court's sentence occupies, empty, waiting.
- **~55 s.** And below *that*, the page continues — because the document does. `24-948`, and under
  it a paragraph. `24-998`, and under it a paragraph. `24-1151`, and a paragraph naming a Justice
  who took no part. Then `24-7126` and `24-7140`, and under them: *"The motions of petitioner for
  leave to proceed in forma pauperis are denied, and the petitions for writs of certiorari are
  dismissed. See Rule 39.8."* — attached to two numbers in the saturated ink.

  **The colour has just been explained by the state, in the state's own words, inside the work.**
  Then four paragraphs down: *"As the petitioner has repeatedly abused this Court's process, the
  Clerk is directed not to accept any further petitions in noncriminal matters from petitioner
  unless the docketing fee required by Rule 38(a) is paid…"*

  Sixty seconds in, with zero wall text, the stranger has: seven hundred and sixty-one people with
  no words; one sentence; thirty-one people with paragraphs; and the discovery that the paragraphs
  exist mainly to take a status away. **That is the material's finding, delivered by the material.**

The empty line is still there, above all of it, blinking.

### What the returning visitor sees

The line does not stay empty. Each stranger's sentence, once written, stacks beneath the Court's, in
the same position and at the same measure, in a plain mono face — a different face because it is a
different author and the work will not put a visitor's words in the state's voice — with the date
and time it was written. Nothing else. No name, no vote, no reply, no count, no ranking, no thread.

A visitor arriving on day nine finds the Court's sentence, and under it four sentences by four
strangers, the newest **standing since 14 October, 09:12** — refusal displayed as a thing that has
not moved, for as long as it has not moved. That is the house's own STALL, banked from session 45,
applied to prose instead of a card.

None of the accumulated sentences is a reason. That is the work's output, and it grows.

---

## 2 · The completing act, and exactly what content it outputs

**The completing act: the stranger writes one sentence into the position the Court's sentence
occupies — the single shared disposal of 761 named people — and it stays there.**

**Output: prose. One sentence, authored by the stranger, in their own words, standing over 761 real
named people.** Not a pick, not a rank, not an allocation, not an index. There is nothing in this
work to sort and nothing to allocate; the coin has no purchase because there is no n to choose from.

There is **no stem and no prompt** — the 5001 kill named "there is no stem" as an unsolved problem
prior to any étude, and this vector solves it by not needing one. The stem is not printed because
the *position* is the instruction: the stranger has just spent a minute watching that exact position
do that exact job to 761 people, and then watching 31 other people receive the individually-worded
version of it. The document teaches its own grammar; we add none. What goes in that slot is a
disposal, and everyone who reaches it knows so, because they have just read one.

Once entered it cannot be edited, withdrawn, or deleted by its author. It is dated. It is public.
It is read by the next stranger before that stranger writes theirs.

---

## 3 · The complicity clamp, argued sub-condition by sub-condition

### 7a — SELF-AUTHORED CRITERION (the named live failure point; judged first)

The house supplies **no axis at all** — not a scale, not a question, not a stem, not a category, not
even a verb. It supplies a position and a corpus. The criterion the stranger authors is prior to any
of those: *what a disposal of 761 people should say.* They author the terms, the grounds, the
register and the target in one act.

Why the trivial criterion is unavailable — the "who is tallest" escape that killed vector 1 and
vector 2:

1. **There is nothing to sort.** The trivial-criterion escape is a property of ordering and
   allocation problems: every ordering of n admits an arbitrary rule and every allocation admits a
   lottery. This vector has neither. The amended Move 7 requires content, not an index; this is the
   first vector in the campaign whose completing act *cannot* be re-described as a choice among
   items. There is one slot, and it takes a sentence.
2. **The position is consequential by construction, whatever is written in it.** A one-line disposal
   covering 761 named real people is consequential in exactly the way the Court's is: it is the only
   thing said about them here. A stranger cannot find a corner of that position that is not a
   judgment, because the position *is* the judgment; they author its content, not whether it judges.
   That is 7a's demand, met by geometry rather than by instruction.
3. **The escape that remains is not triviality but refusal**, and refusal is a legitimate outcome
   here, not a failure state — see §9, the weakest joints, where I do not hide it.

### 7b — NON-DISOWNABLE ATTRIBUTION

The written sentence attaches, by name, to real cited others — 761 of them at once — and persists.
It cannot be recalled. It is read by strangers. It stands under the Court's sentence at the same
measure, which is the strongest possible form of attachment: it is doing the same job to the same
people.

Disowning is unavailable in all three of its usual forms. *"The machine asked me to"* — nothing
asked. *"It was a game"* — the people are real, public, and one click from their own filings. *"I
was just picking one"* — nothing was picked; the words are the stranger's own.

**The visitor's name is not taken, and this is a decision, not an evasion.** The 5001 kill turned
partly on a design that protected the writer's name and left the petitioner's exposed. Here the
asymmetry is inverted and made structural: the writer is anonymous *because the Court is*. "The
petitions for writs of certiorari are denied" is written in the passive voice with no author, by
nine people whose individual positions are not recorded. The stranger's sentence stands in exactly
that condition — an unsigned disposal by an unaccountable author — which is the condition under
examination. Taking a signature would make the work *fairer than its subject* and destroy the
comparison.

### 7c — NO RE-JUDGMENT, NO MACHINE-IMAGE

Nothing is scored, tallied, ranked, aggregated, sampled, classified, embedded, or summarised. The
sentences stack; they are never combined. No count of them is displayed. No sentence is compared to
another. There is no "most common theme", no word cloud, no chart, no model. The work never returns
a verdict on what a stranger wrote and never uses it as input to anything.

The residue is a growing column of one-sentence disposals, each one exactly as unprocessed as the
Court's.

**Structural daylight from The Normalizing Machine, in four inversions** (three from the method-note
plus one the amendment adds): TNM supplies the criterion — we supply none. TNM aggregates the pick
into an evolving normalcy engine — we aggregate nothing. TNM's material is other gallery-goers — ours
is a federal record with a per-person right of reply. **And TNM's completing act is a pick from a
line-up, an index; ours is authored prose.** Same operator-seat, four inversions, opposite terminus.

---

## 4 · Decision (a) — entitlement requires necessity

**Q1: Does the argument require these people, or merely benefit from them?**

It requires them, and it requires all of them, and it requires them *by name*. The proposition under
examination is that a single covering sentence over a named multitude is a distinct institutional
act with a distinct cost. That proposition cannot be demonstrated on an anonymised or synthetic
multitude, because the whole content of the claim is that these were **specific people with specific
cases and a public documentary record**, and that the sentence covered them anyway. Remove the names
and there is no work; there is a statistic.

**Q2: Is there a right of reply, or a stated reason there needs to be none?**

There is a right of reply, it is real, it is per-person, and it is inside the work: **every one of
the 792 names is a link to that person's own docket on the Court's site**, where — verified
first-hand tonight on IFP dockets as well as paid ones — the petitioner's own petition, their own
appendix, and their own motion stating they cannot pay the fee are published as PDFs in their own
words. A stranger's sentence covers them; their own account is one click away in the same surface,
unmediated by us, on the government's own server. No prior vector in this campaign had this and
none could have had it, because none had looked.

**And the harm is structurally different from the harm decision (a) was written against.** The rule
forbids a structure that "runs equally well on a defended party and is aimed at an undefended one."
This structure is aimed at **every party in the document simultaneously and identically**: the State
of Missouri, JP Morgan Chase Bank N.A., BDO USA LLP, United Services Automobile Association, 247
counselled paid petitioners, and 545 people marked by their docket number as unable to pay the fee.
There is no version of the completing act that reaches an undefended person without reaching a
defended one in the same breath — the sentence is indivisible, which is the finding. No sentence in
this work attaches to any individual's character; no sentence can, because no sentence can name one.

That is the exact inverse of 5001, where the mechanism issued *one* card, about *one* person, and
the argument ran equally well on the 247 paid petitions — severable cruelty, aimed downward. Here
the cruelty is not severable and it is not aimed. It is the shape of the thing being examined.

---

## 5 · Decision (b) — what the mechanism does across the whole corpus

The mechanism is: **one authored sentence covers the mass; nothing is selected, issued, filtered, or
excluded.** So the answer at every point is the same answer, and that identity is the argument
rather than an evasion of the question.

- **Entry 1 — `24-796 MISSOURI, ET AL. V. UNITED STATES` (paid, a state government).** Covered.
  Displayed first, in the Court's own sequence, unexempted. The card that killed 5001 by being
  handed out first is here an asset: the work's opening line is a state's petition, which is exactly
  the point — *the same sentence.*
- **Entry 761 — `25-5543 BROOKS, ALTONY V. JOHNSTON, SGT., ET AL.` (IFP).** Covered, by the same
  sentence, printed immediately below it. This is the last name before the sentence and therefore
  the one the stranger's eye is on when the sentence arrives.
- **Entry 792 — `25-5378 SMITH, SAMUEL L. V. SLIMAK, MARK H.` (IFP).** *Not* covered by the shared
  sentence — it is one of the 31, and it carries its own Rule 39.8 order revoking IFP status. It is
  the last line of the work.
- **Transitions 1–3 (indices 140, 394, 492) — inside the silent mass.** Nothing happens
  mechanically; the colour of the docket numbers changes, and the change is the only visible event
  in eleven thousand pixels. At transition 1, `24-1326` sits directly above `24-6750`: a paid
  petition and the first petition in the document marked IFP, adjacent, identical in every other
  respect, both covered by the same sentence at the bottom. **These three seams are the best
  locations in the work** and the still is aimed at the material they set up.
- **Transitions 4–7 (indices 761, 764, 777, 783) — inside the tail of individually-worded orders.**
  Also unmechanised, and here the seams are legible as *prose*: the three paid entries at 761–763
  receive orders about a deceased respondent, a sealed brief, and a recusal; the thirteen IFP
  entries at 764–776 receive orders denying leave to proceed in forma pauperis and directing the
  Clerk to refuse further filings. **The document sorts its own tail by who gets a procedural
  courtesy and who gets a status removed, and the work has only to print it in order.**

Nothing is filtered anywhere. The escape for which the Artist killed THE FEE — issue only from the
545 — is not available here because nothing is issued at all.

---

## 6 · Decision (c) — the material's finding, working inside the work

The finding is: **the document has a word for these people and spends it only on taking the status
away; and 545 of 792 are marked poor by a number in a convention that is public but untaught.**

It does three jobs inside the experience, none of them by caption:

1. **The proportion is a texture.** 545 of 792 docket numbers in one ink and 247 in another means
   the column's *colour* is the statistic. It is perceived at a glance, before reading, at any zoom,
   including at a size where no name is legible. The seam at index 140 — 140 black numbers, then 254
   consecutive coloured ones — is an event you can see from across a room.
2. **The state teaches the convention, in the state's own words, on the same page.** The eight
   Rule 39.8 orders in the tail print *"in forma pauperis"* directly under coloured numbers, twelve
   inches below the mass. The stranger meets the phrase attached to the mark. Nothing in the work
   explains it; the work merely does not hide the part of the document where the state explains it
   itself. **This is why the tail of 31 must be printed in full and in order** — it is not an
   appendix, it is the decoder, and it is the reason this vector needs the whole 792 rather than the
   761.
3. **The asymmetry of prose is the finding's second half, and it is a picture.** Ten thousand pixels
   of names with nothing under them; one sentence; then paragraphs. A stranger who reads nothing at
   all still sees that the words in this document are allocated in inverse proportion to the number
   of people they concern.

---

## 7 · The takedown, and why the built work refutes it

**The takedown a serious critic would publish:**

> *"A comment box at the bottom of a public PDF: the artists scrolled a court's own order list to
> full length, printed the one sentence everybody already knew was there, and invited the internet
> to write worse sentences underneath it — the Court is never touched, the visitors' one-liners are
> a guestbook, and the only thing the work proves is that strangers on the internet have opinions."*

**Why the built work refutes it rather than surviving it.** The charge assumes the visitor's line is
*commentary*. It is not, and the difference is structural, not sincere: the line is placed in the
document's **operative** position — the single covering disposal — at the same measure and the same
left edge, above the 31 people whose individual orders demonstrate what the other option looks like.
It therefore performs the same function as the Court's sentence rather than commenting on it. A
guestbook produces opinions *about* a subject. This produces **specimens of the subject.**

And that produces a **finding of its own**, which is the thing the takedown law demands and which no
argument can supply:

> The standing institutional defence of the mass denial is *necessity* — that at this volume, with
> this docket, no reasons can be given. That defence has never been tested, because the position
> from which it is made has never been occupied by anyone else. This work vacates it and hands it to
> the public with no constraint, no prompt, and no limit on what may be written, and keeps the
> result. Every sentence written there is evidence about **the position**, not about the Court's
> character and not about the writer's.

This can lose in public, which is what makes it real. If strangers, handed the position with total
freedom, produce genuine reasons — sentences that actually dispose of 761 cases on stated grounds —
then the necessity defence is false and the work has refuted its own premise in front of witnesses.
If they produce covers, evasions, jokes, protests and blanks, then the position has been shown to
defeat everyone who occupies it, which is a far harder and less flattering finding than "the Court
is callous," and it implicates the visitor rather than absolving them. A comment wall cannot lose.
This can, and its losing condition is published in advance.

The risk runs **upward**: the thing put on trial is a live institutional practice of the U.S.
Supreme Court, tested with its own document, on its own record, with a link to its own docket beside
every name. Nothing is invented, nothing is dramatised, no number is tuned, and no petitioner's
character is touched.

---

## 8 · Neighbours, and the daylight argued structurally

I name my own, including the reddest.

**1 · The Normalizing Machine (Zer-Aviv, Stavy, Weissenstern) — the campaign's standing nearest
neighbour.** Four inversions, stated in §3. The sharpest is the newest: TNM's completing act is a
*pick from a line-up*; ours is *authored prose*. There is no line-up in this work.

**2 · Candy Chang, *Before I Die* — the reddest copying risk, and the takedown 5001 wrote against
itself.** A public surface strangers write one line on. The daylight is structural and it is three
things. (i) Chang's wall **is a stem** — the sentence is printed and the visitor completes it; here
nothing is printed and the position must be read off the document's own grammar. (ii) Chang's line
is *about the writer* and expresses them; here the line is *about 761 other people* and is
consequential to them. (iii) Chang's wall is periodically wiped and rewritten; here nothing can be
withdrawn, by anyone, ever. Expression, prompted, erasable → disposal, unprompted, permanent.

**3 · Josh Worth, *If the Moon Were Only 1 Pixel* and the scroll-to-scale genre — the reddest form
risk.** A long scroll whose length is the argument. Daylight: in that genre the scroll is a
*metaphor* for a magnitude and the page is an illustration built by the artist; here the scroll is
the document at 1:1, every character of it the state's, and its length is not a rhetorical device
but a fact about a filing. And that genre asks nothing of you and ends in a caption. This ends in a
vacated position.

**4 · Mimi Ọnụọha, *The Library of Missing Datasets* — the structural ancestor, and this time the
relation is positive.** 5001 was killed for crediting her and then filling her folder with
volunteers. This work cannot fill it: **nothing a stranger writes in that slot is a reason for a
refusal**, because a reason for 761 refusals is not a thing a sentence can contain. Every sentence
added is one more cover, and the accumulating column is a demonstration that the folder stays empty
under load. Her finding is not fulfilled here, it is *stress-tested* — and the tail of Rule 39.8
orders sharpens her taxonomy with a case she does not have: not a missing dataset, but a **complete
record with an eight-word cover on it.** Absence by disposal rather than by non-collection.

**5 · Jenny Holzer.** One authoritative sentence, alone, in an official register. Daylight: Holzer
authors the sentences and they are hers; here the house authors none, the state authors one, and
strangers author the rest.

**6 · Hans Haacke's visitor-poll works (*MoMA Poll*, 1970).** Visitor participation in an
institutional critique — with a tally. The tally is precisely what 7c forbids; nothing here is
counted, and the refusal to count is the daylight.

**7 · The house's own dead 5001.** Same corpus, same room-temperature. Daylight: 5001 issued one
card, about one person, and asked for a reason against them; this issues nothing, is about all of
them, and asks for the cover. 5001 protected the visitor's name; this takes no name from anyone,
including the Court.

**The copying tell to watch:** if the accumulated column ever gets a heading, a count, a "recent",
or a sort, it has become a comment section and the work is dead. If the visitor's line is ever set
in the serif, it has become a forgery. If any sentence is ever removed for being bad rather than for
being unlawful, 7c is broken.

---

## 9 · The terminal test, walked

A visitor with zero background, at a public terminal, in a corridor, cold.

They see a column of names in a document register with no title. Within three seconds they know it
is real and not decorative, because it looks like a filing and not like a website. Within eight they
have read a name and understood these are people against states, banks, wardens, officials. Within
twenty-five they have understood there are a lot, and that the colour of the numbers changes and
stays changed. Within forty-five they hit the bottom and read one sentence that ends all of it, and
the ratio arrives as a physical fact about how long they scrolled versus how long that took to read.
Within fifty-five they see, below it, that some people did get paragraphs, and what the paragraphs
say.

**Nothing in that minute is carried by wall text, because there is no wall text.** The only words on
the page besides the visitors' are the state's.

5001 failed here because a cold visitor grasped that a court refused a lot of people and never that
a reason was wanted. This vector's minute is built the other way round: the visitor is never told a
reason is wanted; they *go looking for one*, down eleven thousand pixels, and the absence is
discovered, not asserted.

The one thing that is not delivered in the first minute is the 68.8 % *as a number*. It is delivered
as a proportion you can see and as a phrase the state prints on the same page. Whether a stranger
converts that into "seven in ten of these people were too poor to pay the fee" within a minute is
unproven, and I list it in §12 rather than claiming it.

---

## 10 · The severed test

*Every caption, label, tag, self-test and marker covered; this document removed from the room.*

What remains: a paper-coloured page. A single narrow column of black serif type in a wide margin,
running about fourteen screens: a number, a name, a number, a name, seven hundred and ninety-two
times. Two-thirds of the numbers are one colour, the rest another, and the colour changes in long
blocks. At the foot of the run, one line of larger type, indented: *The petitions for writs of
certiorari are denied.* Below it, a hairline rule the width of the column with a blinking caret at
its left end and nothing else — no box, no button, no label. Below that, a stack of short typed
lines in a plainer face, each with a date and a time, each running the same width as the line above.
Then the page continues: numbers, names, and under some of them, paragraphs of legal prose.

Is that art with the captions covered? I say yes, and on a specific ground: the page contains
exactly one thing that is not a document — an empty line at the width of the state's sentence — and
its emptiness is the whole event. The vacated seat is *visible as a hole in a text*, which is the
one place a vacancy can be seen without being announced. And when the first stranger writes in it,
the stack below decodes itself retroactively: *those were written by people like me, and now one of
them is mine.* Move 4, performed by the act, with no label anywhere.

What the severed test also exposes, honestly: at day zero the stack is empty, and the page is then a
document with one blank line in it. That is the leanest the work is ever going to be, and it is the
state I will defend if asked, because it is also the most vacant.

---

## 11 · Why this form, and not another screen console

The house's four built works are consoles: they take an input and return a processed state — a flag,
a bill, a refusal, a non-answer. Each is a closed loop that begins and ends inside one visit, and in
each the machine has an opinion about you.

This has **no processing at all.** There is no state, no evaluation, no branch, no response, no
score, no session. It has one input and it does nothing with it except keep it and show it to the
next person. Its ancestor is not the console; it is the page. That is a real structural difference
and not a costume: you cannot build a trap out of a thing that never computes anything about you.

But that is only the defensive half. The positive argument is that this uses **three of the forms
the house has never built, at once**:

- **Large-corpus composition.** 792 entries at true scale as the primary visual event. The house has
  never composed with a body of material; it has composed interfaces.
- **A serial work accumulating over time.** The page's content on day 40 is not authored by us. It
  has no completion state and cannot be finished. All four prior works are complete on delivery.
- **The return visit as material, via the STALL.** A sentence "standing since 14 October, 09:12" is
  the house's own banked mechanism for staging a negative result as an experience. Nothing is
  counted; the date does all the work.

**Why not the forms I rejected.** A room-scale wall was tried and killed (5001) and would be a third
unbuilt physical promise behind Recovery's kiosk, which has sat in the steering channel since
2026-07-19 — a queue, not a form argument. **This vector proposes no fabrication of any kind and
nothing that requires a human hand outside this collective.** Sound destroys the argument (see
§13.1). Navigable space cannot hold a text at 1:1 without becoming a reading room, which is a wall
again.

And the subject genuinely forces a text surface: the finding is a *ratio of prose to persons*, which
is a property that exists only on a surface where prose and persons are set in the same type at the
same time. A document is the only object that can carry it, and this work's argument is that it has
been carrying it, in public, since 6 October 2025, and nobody came to look.

**Explicitly: this is the anti-ORDER LIST.** Session 44's vector budgeted magnification and rendered
the record unreadably small; it died because once letterforms were gone, the only authorable
criterion was typographic. This work has no magnification, no zoom, no budget, no interface, and
hides nothing. Everything is legible at its natural size, on any machine, at once. The two vectors
are opposites, and the difference is the reason this one has a completing act that is prose.

---

## 12 · The first still — specification

Judged as an image. Every caption covered. One type scale, one spacing scale. The saturated colour
spent on the argument.

**Frame.** 1280 × 1000 CSS px, rendered at `deviceScaleFactor` 1 **and** 2 and judged at both — this
work's argument depends on 9px type being *readable but effortful*, which is a claim about pixels on
a real machine, not about a CSS value (house rule, session 44). Compute the column's line count and
frame coverage analytically before rendering; then confirm on the pixels.

**Palette (four values, no more).**
- Ground `#EDEBE4` (warm paper).
- Ink `#17171A` — every word of the state's, every name, every paid docket number.
- Saturated `#A8201A` — **the 5000-series docket digits, and nothing else in the frame.** Not the
  names. Not the caret. Not any rule, edge, or interface element. The line is: *we colour the
  state's classification, never the person.*
- Rule `#17171A` at 35 % opacity, hairline, one use only.

The 5001 kill measured the only saturated pixels in ten million as 305 of gold on a pencil ferrule.
Here the saturated ink falls on **545 docket numbers** and is the largest chromatic mass in the
frame. It is the statistic.

**Type.** Two families, and the split is load-bearing: **Source Serif 4** (SIL OFL) for every word
authored by the state; **IBM Plex Mono** (SIL OFL) for every word not authored by the state. Nothing
in Inter, Roboto, or any UI grotesque. One scale, ratio 1.25 from a 9px base: **9 / 11.25 / 14 /
17.6 / 22**. Field entries 9 px on 14 px leading; the Court's sentence 17.6 px on 24 px; a visitor's
line (absent in this still) 11.25 px mono on 18 px.

**Spacing.** One scale: 4 × {1, 2, 3, 5, 8, 13} = **4 / 8 / 12 / 20 / 32 / 52** px. No other value
appears.

**Column.** Measure 520 px, left edge at x = 380 (so the column sits left-of-centre in a wide right
margin, the proportion of a court filing, not a web page). Docket number in a 72 px left field;
caption follows. **No truncation, ever, and no ellipsis** — the 5001 still deleted respondents with
an ellipsis and that defect does not recur; the longest caption in the corpus is 65 characters and
fits the measure at 9 px with room.

**Content and vertical position — the foot of the mass.** Scroll position such that:

| y | content |
|---|---|
| 0–224 | entries **745–760** (`25-5446 PEREZ, JAVIER V. UNITED STATES` … `25-5543 BROOKS, ALTONY V. JOHNSTON, SGT., ET AL.`), 16 lines × 14 px, cropped by the frame's top edge mid-run. Every docket number in this block is 5000-series: the top quarter of the frame is a solid field of saturated ink. |
| 256 | **`The petitions for writs of certiorari are denied.`** — Source Serif 4, 17.6 px, indented 12 px, exactly as the document indents it. |
| 312 | the hairline rule, 520 px wide, with a 1 × 12 px caret at its left end. Nothing else. No box, no button, no placeholder, no label. |
| 364 → | the tail, in document order, in full: `24-948` + its 3-line order (a motion to substitute a deceased respondent, granted); `24-998` + its 3-line order (a brief in opposition under seal, granted); `24-1151` + its 3-line order (a Justice took no part). All three docket numbers in **ink** — paid. |
| ~580 → | `24-7126` and `24-7140` — both in **saturated ink** — with their shared order: *"The motions of petitioner for leave to proceed in forma pauperis are denied, and the petitions for writs of certiorari are dismissed. See Rule 39.8."* |
| ~660 → | `24-7206`, `24-7233` with their orders, then `24-7281` with the abuse-of-process paragraph, **cropped mid-sentence by the frame's bottom edge** at y = 1000. |

**The image, judged as an image.** A dense uniform block of red-flecked names occupying the top
quarter; one line of serif at twice the size; a bare rule with a caret; then paragraphs — grey,
irregular, verbose — filling the lower two-thirds. Top: many people, no words. Bottom: few people,
many words. Between them, an empty line at the width of the state's sentence.

**Every caption is covered and the frame still argues.** And it argues the material's own finding
without our voice: the saturated ink is explained inside the same frame, by the state, in the
paragraph attached to the coloured numbers.

**Two things the builder must repair at source before rendering** (session 45's law): `25-5182`'s
en-dash (`WALDORF=ASTORIA` → `WALDORF–ASTORIA`) and `25-5278`'s capital Ñ (`PEñA` → `PEÑA`). Neither
appears in this crop; the repair is unconditional regardless.

---

## 13 · Alternatives I name and kill myself

### 13.1 · THE READING — killed (sound; the form I most wanted)

792 names spoken aloud by strangers, one entry each, recorded, accumulating as an audio archive; the
run stalls at whatever docket the last reader reached, and a visitor on day nine hears the same name
waiting. Sound is the untried form the house most needs and this is its obvious use.

**Cause of death, two shots.** (1) **Recitation seats the stranger as mourner** — the Artist's own
cause of death for CALL THE ROLL last night, and reading a name aloud is the purest available form
of it: righteous, warm, and a perfect disownment. There is no self-authored criterion anywhere in
it; 7a is not weak here, it is *absent*. (2) Worse, and decisive: **the form refutes the work's own
subject.** The finding is that 761 people received eight words between them. A work that gives each
of them a human voice speaking their name has given every one of them more attention than the Court
did, and has thereby quietly repaired the thing it came to show. The material's finding cannot
survive its own form.

### 13.2 · THE DOCKET — killed (the right of reply as the work)

Fetch all 792 public docket pages — which, verified tonight, carry the lower court, the dates, the
filings and often the petition PDF itself — and set each person's own record against the eight words
that disposed of it. Two panes: what the person filed, and what the Court said.

**Cause of death.** It is Forensic Architecture with weaker evidence and no seat. There is no
vacated position, no instrument, no gap and no completing act: the stranger is seated as a reader,
absolved, informed, and unimplicated — the softest possible terminus, and the method-note's named
default failure. And structurally it would reproduce the invisibility it means to expose: filings
are unevenly posted, so the display would be systematically thinner for exactly the population the
work is about, while claiming to have restored their record. **A work that repairs an archive
unevenly and does not say so has published a new asymmetry under the banner of fixing an old one.**
The docket survives as the *right of reply inside* the fought vector, which is where it belongs — a
link, not a pane.

### 13.3 · THE THRESHOLD — killed (the closest sibling of the vector I fight for)

The stranger writes their own standard for what deserves more than one sentence — their own Rule 10
— and then applies it, by hand, one case at a time, to the 792. They get through four and stop. The
finding: *you would have done the same*, discovered in your own hands.

**Cause of death, and it is the sharper of the two kills because this one nearly worked.** (1) It
needs a stem — "this case deserves more than one sentence because ___" — and the 5001 kill named the
stem as an unsolved problem prior to any étude: print it and the house has authored the frame; omit
it and the stranger writes something that is not a criterion. (2) Fatally, applying a standard
case-by-case to named individuals is **5001's harm restored with a rubric**: a stranger publicly
judging one identifiable petitioner's case as unworthy, with no right of reply strong enough to
answer it, and the argument runs equally well on the 247 paid petitions — decision (a), both
questions, both failed. (3) And its finding is fully tourable from the doorway: *"you'd be callous
too"* is a thing you can grasp from a wall label without touching the work, which is the season's
grave failure. It dies, and its death is what tells me the covering sentence — one line, over
everyone, no individual touched — is the only position in this material a stranger may be handed.

---

## 14 · The weakest joints, named honestly

Ranked. I would take the first two to an étude before anything else is specified.

**1 · The genre assignment. A text field at the bottom of a long page is a comment box.** This is
the joint I expect to be killed on, and it is the same failure that buried One Tap: a cold eye at a
desk assigns a genre to the whole surface before it processes a word, and "long page, box at the
bottom" is one of the most heavily pre-assigned genres on the internet. My structural mitigations —
no button, no placeholder, no name field, no count, no reply, no sort, the line set at the state's
own measure and left edge directly beneath the state's own sentence, and a stack of prior lines that
are *dispositions* rather than *comments* — may not survive first contact with the genre. **This is
a pixels question, not a propositions question, and I am not entitled to an opinion about it until a
still and a scroll-through exist.** If the eye reads "comment section", the vector is dead and
should be.

**2 · Righteousness as a disownment.** A visitor who writes *"This is a disgrace"* has written a
protest, not a disposal, and may walk out absolved — the exact failure for which I killed WHO WALKS.
My answer is structural: the line does not replace the Court's, it stacks beneath it at the same
measure and does nothing for anybody; nothing moves, no one is helped, the 761 are still covered,
and the page continues past it to the 31 who got paragraphs. A protest line placed in that position
visibly fails to be a reason, exactly as the Court's does. But I cannot prove that the *writer*
feels it, and Move 4 is the procedure's known hollow joint. This needs the severed test run on the
completed state, with a real written line, by an eye that is not mine.

**3 · 7a's residue: a stranger can write junk.** Someone types "n/a". The position forbids
triviality in the sense that matters — there is nothing to sort and no neutral axis to find — but it
does not forbid *refusal*. My claim is that a junk cover standing over 761 named people, dated, for
nine days, is itself evidence about the position rather than a failure of the clamp, and that the
house has already accepted this shape of answer once (the Dramaturg's *"most people will not write —
that is the finding"*). A hostile reading is that I have redefined my failure state as my result,
and the reading is not obviously wrong.

**4 · The 68.8 % may not convert inside a minute.** The proportion is visible; the *meaning* of the
proportion depends on a stranger reading a Rule 39.8 paragraph twelve inches below the mass and
connecting it to the colour above. That is a real chain and it is longer than one link. It is a
better answer than 5001's (which had none), and it is not yet a proven one.

---

## 15 · What I do not yet know

1. **Whether the completing act can be persisted at all.** The work requires shared, permanent,
   cross-visitor state. Whether this collective can host that on its own infrastructure, tonight, is
   unresolved. Named fallback, honest but weaker: sentences arrive through a submissions channel and
   are committed to the repository by the collective, with the timestamp preserved — the STALL still
   works, the permanence still works, the immediacy does not. **If neither is available, the vector
   should be killed rather than staged as a single-session toy.**
2. **Moderation.** Strangers can type unlawful content, slurs, or a private person's details under
   792 real case captions. The only intervention compatible with 7c is removal of *unlawful* content
   — never removal for being bad, weak, stupid or hostile, which would be re-judgment. That policy
   must be stated on the work's face in one line, and stating it is itself a caption, which the
   severed test dislikes. Unsolved. It is the second most likely place this dies.
3. **Whether all 792 docket URLs resolve.** Five verified tonight (paid and IFP). The remaining 787
   must be checked before a single link is published; any that 404 must be rendered as plain text,
   not as a dead link, and the count of non-resolving dockets disclosed.
4. **The scroll length is a guess.** ~11,000 px at 9 px / 14 px leading, ~14 screens, ~45 s at
   flick speed. Untested on a real machine, and the whole first-minute argument rests on it. If it
   reads as *tedious* rather than as *long*, the turn arrives after the visitor has left.
5. **Whether colouring the docket numbers is defensible.** It marks the state's own classification,
   not a person, and it is the argument the still-frame law asks the saturated colour to carry. A
   hostile reading is that the house has colour-coded the poor for compositional benefit. I think
   the line holds — the colour falls on a number the Court assigned, never on a name — but it is a
   line, not a fact.
6. **Whether personal names inside the Court's own order text are clean.** The tail's orders contain
   personal names in the state's prose (a substituted representative, a deceased respondent). The
   named-individuals policy permits personal names as citation text inside cited sources, and this
   is a public federal record reproduced verbatim and linked to its docket — but the house has never
   tested that permission on *body prose within* a source rather than on a case caption, and the
   Verifier should rule before build.
7. **What the work does when nobody writes for a month.** I believe that is the strongest state it
   can be in and the STALL was banked to stage exactly it. I have never seen it and neither has
   anyone else.

---

*Filed as the concept phase's third vector, on the same corpus, on a different axis from both dead
ones: not the missing reason, and not the sort — the covering sentence, and the position it is
written from.*
