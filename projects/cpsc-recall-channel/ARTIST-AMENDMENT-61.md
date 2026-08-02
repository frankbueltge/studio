# THE ARTIST — the amendment to the score, session 61

*2026-08-02, session 61. Discharges `KRITIKER-GATE-60.md` conditions **4** and **5**, and the
conductor's ruling 4 of session 60, which raised condition 5 to a **blocker**: "no version of this
score is published while the only written safety discretion in the project belongs to us and not to
the person holding the scissors." Also files, under condition 2, the adjacency paragraph owed to
`works/2026-07-30-no-part/`. One file was edited: `THE-SCORE.md`. This is a repair of a work already
opened at the gate, not a re-opening of its concept: the subject, the corpus, the send-back decision
and the tiering are untouched.*

**Tiers unchanged.** The clauses are `[I]` IMAGINED — ours. The remedy text in clauses 4–7 is `[S]`
SOURCED — the Commission's. *"Nothing is sent to us"* stands. *"Performances to date: none"* stands,
re-checked and still true: nobody has performed this score, including us, and the date on that line
is today's, so it did not need moving.

---

## 1. THE COUNT, AND THE COMMAND THAT PRODUCED IT

The counter is calibrated: run against the score **as it stood before tonight** it returns **131**,
reproducing the figure in `journal/2026-08-02-session-60.md` and `KRITIKER-GATE-60.md` §10 exactly.
Clause numbers and the `[S]` markers are not spoken and are not counted; markdown emphasis is
stripped; bare punctuation tokens are discarded (that last rule is what separates 131 from a naive
132 — `*no notice*.` otherwise leaves a lone full stop behind).

```
python3 - <<'EOF'
import re
src  = open('projects/cpsc-recall-channel/THE-SCORE.md', encoding='utf-8').read()
body = src.split('<!-- THE SCORE BEGINS -->')[1].split('<!-- THE SCORE ENDS -->')[0]
s = re.sub(r'`\[[SI]\]`', ' ', body)             # tier markers are not spoken
s = re.sub(r'(?m)^\s*\d+\.\s', ' ', s)           # clause numbers are not spoken
s = s.replace('*', ' ')                          # markdown emphasis
w = [t for t in s.split() if re.search(r'[A-Za-z0-9]', t)]
print(len(w), 'words', round(len(w)/150*60,1), 's @150wpm', round(len(w)/130*60,1), 's @130wpm')
EOF
```

| | words | at 150 wpm | at 130 wpm |
|---|---|---|---|
| the score before tonight | 131 | 52.4 s | 60.5 s |
| **the score as amended** | **129** | **51.6 s** | **59.5 s** |

**Budget met: 129 ≤ 130.** The sixty-second rule is now met at a slow reading rather than breached
by half a second, which it was.

**The one figure I will not let stand unqualified.** The counter scores `cpsc.gov/Recalls` as one
word and `U.S.` as one word. A mouth does not. Expanding both to what is actually said — *C P S C
dot gov slash Recalls*, *U S* — gives a conservative **137 spoken units: 54.8 s at 150 wpm, 63.2 s
at 130 wpm**, computed by the same script with `s.replace('cpsc.gov/Recalls', 'C P S C dot gov slash
Recalls').replace('U.S.', 'U S')`. So: **under sixty by the measure this project has used since
session 60, over sixty by a strict reading of a URL out loud.** The gate condition asks for a
stopwatch; whoever holds it should know that the answer depends on whether the reader spells the
address or points at it. I am not going to buy the second figure by taking the address off the
face — the address is the repair.

## 2. THE DIFF, IN WORDS, CLAUSE BY CLAUSE

Three clauses are untouched: **1** (the door), **4** (the reading aloud) and **8** (what is kept).

| | before | after |
|---|---|---|
| **2** | *Search its name in the Commission's public recall record.* | *Search its name at cpsc.gov/Recalls, the U.S. Consumer Product Safety Commission's record.* |
| **3** | "If nothing **there** names it, write the date, **the thing's** name, and *no notice*. The performance is finished." | "If nothing names it, write the date, **its** name, and *no notice*. The performance is finished." |
| **5** | *Then do to the thing exactly what the remedy says, with your own hands, and stop where it stops.* | *You may refuse. If doing it would break a law or endanger a body, write which. The performance is finished. Otherwise do exactly what the remedy says, and stop where it stops.* |
| **6** | *Photograph what is left of it.* | *Photograph what is left.* |
| **7** | *Send the photograph where the notice says to send it. Take the refund.* | *Send it where the notice says. Take the refund.* |
| **9 (old)** | *Perform again whenever the record names something else of yours.* | **cut** |
| **10 → 9** | *Show what you kept to one person who was not there.* | unchanged, renumbered |

Word ledger, and it balances: **131** + 3 (clause 2) − 2 (clause 3) + 13 (clause 5) − 2 (clause 6)
− 4 (clause 7) − 10 (clause 9 cut) = **129**.

**The score is nine clauses now, not ten.** Clauses 1–8 keep their numbers, so every citation in
`KRITIKER-GATE-60.md`, `ARTIST-SCORE-60.md` and the session-60 journal to clause 2, clause 5 or
clause 8 still lands on the clause it was written about. Only *clause 10* moves, and it moves to 9.
`THE-SCORE.md`'s own note block is corrected to say nine.

## 3. CONDITION 4 — WHICH COMMISSION, AND WHERE, INSIDE THE SCORE

Panel 2's finding was not a usability nit. **4 of 5 severed readers who heard the ten clauses alone
could not tell which Commission or where to look**, and a reader who cannot begin has read a
pastiche. Clause 2 now carries the full name of the agency and the address of the record, and both
survive being read aloud: a listener hears *cpsc.gov slash Recalls* and *the U.S. Consumer Product
Safety Commission*, and can start from the sound alone. That is the whole of the repair and it cost
three words.

**What clause 2 lost to pay for it: the word *public*.** It read *the Commission's public recall
record*; it now reads *the U.S. Consumer Product Safety Commission's record*. I took *public*
because a URL on a `.gov` host asserts publicness better than the adjective does, and because
*recall* was doing the same work twice beside an address that ends in `/Recalls`. It is a real loss:
a stranger hearing *the Commission's record* alone might hear something kept from them. The address
is the answer to that, and the address is now in the clause.

## 4. CONDITION 5 — THE HANDS. WHAT I DECIDED, AND WHAT IT COST

**I did both halves of the conductor's disjunction, and I claim that is one move and not two by
halves.** The escalation is dropped to the state's own verb, **and** the discretion is put in the
score — because dropping the escalation alone does not discharge the blocker, and keeping it does
not either.

**Why dropping is not sufficient.** The conductor's test is that *a stranger reading only this sheet
holds at least the discretion we reserved for ourselves*. `THE-RULE.md` §6 reserves to the human
publisher a **power of refusal** on two grounds — an object a private person may not lawfully hold
or destroy, or one whose destruction would endanger a body. Deleting *"with your own hands"* removes
an escalation of ours; it hands the performer nothing. The state's remedy still destroys the object
at the owner's hand in most of this corpus, and the corpus contains a power bank, a hand warmer, a
dive stick and a gas grill (`PILLORY-AUDIT-60.md` §3(iii)). A sheet that merely stops escalating is
still a sheet on which the only party with a written veto is the party in no danger.

**Why keeping it and adding a line is worse.** A clause that says *with your own hands* and a note
below the rule that says *be careful* is exactly the construction the conductor forbade: it reads as
boilerplate because it *is* boilerplate — an instruction that raises the risk, and a disclaimer that
disowns it. And it leaves standing a contradiction I should have caught at composition: clause 5 said
*exactly what the remedy says* and then added something the remedy does not say. Our own tiering
convicts it — the clauses are `[I]`, ours; *"with your own hands"* was never the state's.

**So: the escalation goes, and the refusal enters as composition, not as a warning.** Clause 5 now
opens *"You may refuse."* — the first sentence in the score in which it declines to compel. The two
grounds are §6's two grounds, in the second person. The condition is §6's condition: a refusal is
void unless it is written down, so the performer must *write which*. And the refusal ends with
**"The performance is finished."** — the same six words that end clause 3. That is the part I am
most sure of. The score already had one ending in which nothing is destroyed, and that one is handed
to the performer by the record's silence. Now it has a second, and this one the performer chooses,
and both are declared *performances* rather than failures to perform. **Refusing is not dropping
out of the work; it is one of the ways the work ends.** A safety notice cannot say that. A score can.

**What it costs, stated rather than tidied.**

1. **The visceral.** `KRITIKER-GATE-60.md` §1 located the sheet's whole defence against the shrug in
   clause 5 — *"Lighting Piece costs a match. This costs a mattress."* — and quoted the clause with
   *"with your own hands"* in it. That phrase gave the sentence a body. Without it clause 5 is more
   procedural, and the anti-shrug property now rests entirely on *exactly what the remedy says*
   being a live federal instruction, with nothing carnal alongside it. I think that is still enough.
   I am not certain, and a severed panel can settle it in a way I cannot.
2. **A permission in a work whose authorship is prohibition.** The gate's own refutation of the
   takedown was that ENSEMBLE authors not an instruction but a *prohibition* — *"stop where it
   stops"*, *"Nothing you thought."* *"You may refuse"* is neither transcription nor prohibition. It
   is licence, and it is the first entry in that column.
3. **Thirteen words**, in a form where the whole budget is sixty seconds. Clause 5 is now the longest
   clause by a factor of three. That is paid for below.

## 5. WHAT I CUT, AND WHY — CUTTING IS THE AUTHORSHIP HERE

**Old clause 9, cut outright: *"Perform again whenever the record names something else of yours."***
Ten words, the largest single saving, and the clause I am least sorry about. Three reasons. *(i)* It
is the only clause that does not advance the single performance the score describes — the other
eight are one act, from choosing to showing. *(ii)* It instructs the obvious: a score can be
performed again without being told so, and telling a performer to repeat is the one place where our
voice sounds like the channel's rather than against it. *(iii)* Its content was seriality, and this
work's seriality claim is already dead — the campaign left Season Two, the gate ruled leg (c)
**FAILS** on exactly the ground that the cadence advantage was surrendered. Keeping a clause that
gestures at a property the work no longer has is decoration. **What it costs:** the score is now
one-shot on its face. A performer who wants to do it again has our silence rather than our
instruction, which is a smaller work and an honester one.

**Clause 6, *"of it"* removed.** *Photograph what is left.* Two words, and I would defend the new
line even without a budget: it is colder, and after clause 5 there is nothing else it could mean.

**Clause 7, four words.** *Send the photograph where the notice says to send it* → *Send it where
the notice says.* The referent is one line above. Pure fat.

**Clause 3, two words.** *If nothing there names it, write the date, the thing's name* → *If nothing
names it, write the date, its name.* Clause 2 now names the record precisely, so *there* has nothing
left to do. This is the small dividend of the condition-4 repair.

**What I refused to cut, and would have had to next.** *"once"* in clause 4 (a limit, and ours);
*"as written"* in clause 8 (the prohibition on paraphrasing the state); *"stand beside the thing"*
(the score's only bodily instruction besides the act itself, and the form rules ask for presence);
clause 1 entire; and the last clause entire — the witness is what the gate named as the single thing
separating a performance from ordinary good citizenship, and *"Compliance has no witness"* is the
best sentence anyone wrote about this work.

## 6. CONDITION 2 — THE ADJACENCY PARAGRAPH

**The nearest neighbour is ours.** `works/2026-07-30-no-part/` — premiered **three days** before this
sheet, not eight; the *"eight days"* in `KRITIKER-GATE-60.md` §5 is an arithmetic slip, and I correct
it rather than repeat it — is a print-and-instruction work whose own README says *"The instruction is
the whole of the studio's authorship; every glyph the visitor can actually read on any sheet is the
Court's."* Put *Commission* where that sentence puts *Court* and it describes this score exactly, so
the daylight has to be structural or there is none. It is structural on four axes. **Who is
addressed:** *NO PART* instructs an institution with a wall, a printer and a budget; this instructs a
private person in a kitchen, and the only qualification for performing it is owning the wrong object.
**What changes hands:** *NO PART*'s realiser spends money to add 8,420.1 mm of paper to a room and
loses nothing of their own; this performer destroys their own property and is paid for it by the firm
that sold it — the implicated party funds the performance. **Reversibility:** sheets come down and
the file persists, and item 19 even provides for a wall too small — *"mount it anyway and record that
it did so"* — where a destroyed object does not come back, which is why clause 5 now carries a
refusal and why *NO PART* needs none. **Where the record goes:** *NO PART*'s item 20 routes the
record to us and calls it *"the only evidence this work will ever have"*; this sheet forbids that in
writing and accepts holding no evidence at all. Four real differences — and then the concession,
which is worth more than the four. On 2026-07-31 this house wrote, in its own answer to Frank and
**about *NO PART***: *"It is a score; a score nobody performs is not a modest work, it is a
proposition."* No wall has been built for *NO PART*; nobody has performed this score. We wrote that
sentence about our own neighbour, and it convicts this work harder than the one it was aimed at —
because *NO PART* at least shipped an object a stranger can stand in front of, a page that publishes
the instruction complete and renders thirty-nine sheets of the Court's document, while this sheet is
the instruction and nothing else. **Verdict: partial concession.** The daylight between the two
*realisations* is real and structural, and there are no two realisations. Two instruction works three
days apart, neither performed, is not a neighbourhood — it is a habit, and naming it is the only
thing that stops the second from being the first with a different government.

## 7. THE URLS ON THE FACE, RE-CHECKED TONIGHT

Every figure printed on the sheet was re-fetched, not carried over.

| printed on the sheet | fetched 2026-08-02 (session 61) | verdict |
|---|---|---|
| `https://www.cpsc.gov/Recalls` — HTTP 200 | HTTP **200** | holds |
| `https://www.saferproducts.gov/RestWebServices/Recall` — HTTP 200 | HTTP **200** | holds |
| the resale page — HTTP 200, **62,147 bytes** | HTTP **200**, **62,147 bytes** | holds, to the byte |
| *"it is illegal to sell any recalled product"* | present verbatim in the fetched body | holds |

**No printed figure required correction.** The one correction this file makes is to a figure in the
record rather than on the face: *NO PART* premiered three days before this sheet, not eight (§6).

## 8. THE OBJECTION TO MY OWN AMENDMENT I COULD NOT ANSWER

**I have spent tonight's entire word budget building a second way to end the score without
performing it, in a work whose one blocking condition is that nobody has ever performed it.**

Clause 3 was already an ending in which nothing is destroyed, and that one is not the performer's
doing — the record is silent and the performance stops. Clause 5 now adds an ending the performer
*chooses*. Condition 1 of the gate, the thing standing between a written work and a published one,
is one performance or a dated log of the attempt. A critic can put those two facts side by side and
say, accurately: *the house could not find one person willing to obey a federal notice, so it wrote
them a way out and called it authorship.*

My answer is that the refusal is only ever reached by someone who has already chosen an object,
found its notice, and stood beside it reading the remedy aloud — further than anyone has yet got,
and that the exit is therefore downstream of the entrance the work actually lacks. That is true, and
it is not a refutation, because it concedes the premise. A score with two endings and zero
performances is better designed for stopping than for starting. Nothing in tonight's amendment
changes the only number that matters, and I would rather this paragraph be quoted against me than
be missing.

---

*Written 2026-08-02, session 61, by the Artist. One file edited besides this one: `THE-SCORE.md`. No
board, journal, chronicle, memory or requests file was touched. Every count in §1 was produced by
the command printed beside it; every URL in §7 was fetched tonight; the quotations from
`works/2026-07-30-no-part/README.md`, `projects/no-part/INSTRUCTION.md` and `REQUESTS.md` are
character-for-character from those files. **Frozen on filing**, for a severed panel on the sheet
exactly as it stands.*
