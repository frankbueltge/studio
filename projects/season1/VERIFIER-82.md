# VERIFIER 82 — 2026-08-10 — blocking, and it blocked twice

Facts and tiers only; no vote on form. It fetched the live upstream pages and the cited paper
itself, ran this work's three self-checks and re-derived the published figure independently.
**Two of its six checks FAILED, both blocking, and both were repaired the same night before
anything was committed** — what it saw is below, verbatim and unedited, followed by what this
house did about it.

---

## 1. The new factual claim on the face — the definition paragraph

> **Source fetched:** `https://frankbueltge.de/ghost-fleet/` (HTTP 200, 32,189 bytes — note this
> is byte-identical in size to the ledger's newest capture) and
> `https://frankbueltge.de/werke/ghost-fleet/` (HTTP 200, 27,640 bytes). `WebFetch` returned 403
> on the first; `curl` with a browser user-agent returned 200. Both pages extracted to text and
> searched.
>
> The claim under test, from `still-dark/index.html` (`arrive.subject_gloss`, rendered at
> `#sd-arrive-gloss`, and confirmed present in the rendered face at `STATE-1.txt` line 7):
>
> > "dark — the ship's AIS transponder switched off, so it stops being tracked. The lists below
> > are the daily editions of The Ghost Fleet, a public register of such disappearances published
> > at frankbueltge.de, which can name a ship only once it has come back."
>
> **Limb by limb:**
>
> | Limb | Verdict | Upstream sentence relied on |
> |---|---|---|
> | "the ship's AIS transponder switched off, so it stops being tracked" | **PASS** | Method sheet, *What this is*: "The AIS picture of the seas looks complete. It is not — ships switch off their transponder on purpose to vanish." |
> | "daily editions" — is it in fact a daily register? | **PASS** | Method sheet §2 *Cadence*: "Daily. Window: disabling events that ended in the last 7 days (complete vanish-and-return stories)." |
> | "published at frankbueltge.de" | **PASS** | Served from `frankbueltge.de/ghost-fleet/`; footer "© 2026 Frank Bültge". |
> | "can name a ship only once it has come back" | **PASS** | Method sheet §2, "(complete vanish-and-return stories)"; §3 *Processing*: "filter (ended in window, plausible duration)". The front page's case of the day is written "vanished at 3.1°N, 89.8°W, resurfaced at 5.6°N, 92.7°W". |
>
> **Does the description overstate what upstream claims for itself? — PASS, with one qualification
> I am recording rather than softening.**
>
> Upstream nowhere calls itself a "register". It calls itself "An instrument — method and sources
> disclosed, source code open." More materially, its method sheet §4 *Limits of the method* carries
> two coverage disclaimers:
>
> > "Only offshore (≥ 50 nm) and well-observed: nearshore disabling is missing — so marine
> > protected areas (mostly coastal) almost never appear; what is measured is the open sea."
> >
> > "AIS only: vessels that never transmit („dark by default") do not appear at all."
>
> "A public register of such disappearances", read alone, asserts a completeness upstream
> explicitly disclaims. It does **not** stand alone on this face: three elements lower, `#sd-define`
> prints "The instrument this page reads counts only disabling its own source classifies as
> high-confidence and intentional: at least 12 hours dark, at least 50 nautical miles offshore",
> and the floor line prints "A method that counts a disappearance only when the ship comes back
> cannot see the ships that never come back." So the face carries the limits; the premise paragraph
> does not. I record this as a qualification, not a failure. (Related, same direction: `DEFINITION`
> in `data.py` renders upstream's §1 as "≥ 12 h, ≥ 50 nm offshore" and drops the third condition
> upstream states in the same breath — "good satellite coverage". A subset, not a contradiction.)
>
> **No load-bearing caveat of upstream's is dropped by the rewording.** The clause it replaced
> ("the public instrument this page reads") carried no upstream caveat either. The upstream
> restraint sentence is unaffected and still travels — see check 5.
>
> **The hedge that moved — PASS.** … It is on the face, **in full, character for character** …
> Confirmed at `STATE-1.txt` line 28. Its new position: inside the same `<section class="sd-arrive">`,
> immediately after the two name blocks and immediately before the button row … Its type size went
> **up**, from the gloss's `0.72rem` to `0.78rem`. It is not now smaller, not below the fold
> relative to where it was, and not separated from the names by any intervening element. On the
> facts, the move does not weaken it. Note also that it is no longer computed-inert: `data.py` now
> branches the hedge on the computed certain-end (`band[0] == 0`), so it cannot go on saying "not
> one" if that ever ceases to be true.

## 2. The 238 wpm claim in the page's machinery

> **URL fetched:** `https://biblio.ugent.be/publication/8647789` (HTTP 200), abstract read in full.
> Author, title, journal, volume, year, the 238 wpm figure, the "190 studies (18,573 participants)"
> count, and all three caveats — that it is a mean, that "most adults fall in the range of 175-300
> wpm", and that "Reading rates are lower for children, old adults, and readers with English as
> second language" — **all PASS, no discrepancy in the citation.**
>
> **The arithmetic — PASS.** `round(44/238*60*1000) = 11092`, island `first_dwell_ms = 11092`; the
> string it measures is `arrive["subject_gloss"]`, the same paragraph the note names. Correct
> paragraph, correct divisor, correct rounding.
>
> **One exact discrepancy in the word count, reported as found.** `len(gloss.split())` returns
> **44 tokens, of which one is a bare em dash**. By any ordinary sense of "word" the paragraph is
> **43 words**, and the published note reads "44 words at 238 wpm". The consequence is 11,092 ms
> where 43 words gives 10,840 ms — an overstatement of 252 ms, 2.3 %. In the direction that matters
> (giving the reader more time, not less) this is harmless; as a printed factual claim it is off by
> one.
>
> **FAIL — one traceability failure attached to this claim.** `index.html` stated "the page's
> README cites it". `grep -n "Brysbaert\|biblio\|238\|wpm" README.md` returns **nothing** (exit 1).
> The README does not cite it. Consequently `index.html` — which ships as one self-contained file —
> contains **no retrievable URL for this figure anywhere**. Under the house rule that a SOURCED
> claim carries a real retrievable URL, the URL exists — but the file making the claim points at a
> document that does not have it. Either the README gains the citation or the `index.html` comment
> must carry the URL itself.

## 3. The cut provenance paragraph

> **(a) Nothing else depended on it — PASS.** … `grep -rn "sd-arrive-check\|sd-arrive-tier-words\|
> check_lead"` across the repository returns **zero live references** … No dangling reference. The
> per-stop `check` string survives in the island and is printed nowhere — which is what `data.py`
> says it does, accurately.
>
> **(b) Tier legend and a runnable command still on the face — PASS.** … three of them, and I ran
> all three. All exit 0 and all reproduce the figure printed beside them.
>
> **(c) A claim now stands on the face without the tier mark it needs — FAIL.**
>
> The deleted string was the only text on the face marking **the share figure itself** as DERIVED.
> The surviving legend does not cover it: its DERIVED line names only "the dark-and-return spans",
> which is the per-vessel date band on the rows of the time field, not the percentage. After
> tonight's cut:
>
> - the head's running figure (`100 %–100 %` through `44 %–100 %`, the largest number on the page),
> - the struck row `69 %–100 %` and the live row `44 %–100 %` in the fall,
>
> carry **no tier word anywhere on the face**. The verbatim terminal block at the foot tier-marks
> the numerator only (`knowable on the day, DERIVED ...... 11`); its own share line is unmarked.
>
> Second, subordinate limb: the head now carries **no tier word at all**, so a reader who never
> scrolls past `#sd-arrive` gets twenty-five vessel names, six percentages and no tier legend.
> `data.py` concedes the loss of the *command* candidly and by name; it does not concede the loss
> of the *tier words* for that reader, stating only that "the tier legend … stand[s] in the body".
> That is true and it is below the head.
>
> I am not ruling on whether the cut was right. I am recording that the work's central published
> figure is now unlabelled by the work's own labelling law.

## 4. The numbers — PASS

> All three commands exit **0**: `data.py --check` → "island matches the captures";
> `tools/renders.py` → "RENDERS MATCH THE PAGE"; `capture/day.py 2026-08-04` → exit 0.
>
> **Independent re-derivation, line by line against the face — no mismatch.** All six lines of the
> `day.py` block are byte-identical to `data.output` in the island and to the "verbatim, unedited"
> block on the face. `--as-of 2026-08-06T08:36:39Z` → `69%–100% (11 of 0–16)` matches the struck
> row; `--as-of 2026-08-06T04:36:19Z` → `79%–100% (11 of 0–14)` matches head stop `+1 DAY`.
>
> Cross-checks: the head's six stop shares are `100/79/69/65/55/44 %`, running totals
> `11/14/16/17/20/25`; the field's six block counts are `11+3+2+1+3+5 = 25`, which equals the band's
> high end; the OBSERVED ledger has **17 rows**, equal to `17 capture(s) read`. The newest ledger
> row (`2026-08-10T04:36:45Z`, 32,189 bytes) is the same byte-length my own live `curl` of
> `/ghost-fleet/` returned tonight.
>
> **VERDICT: PASS. No mismatch of any kind.**

## 5. The standing obligations — PASS

> **The upstream restraint travels.** It stands **twice** on the face … Traced to upstream, both
> limbs, method sheet fetched tonight:
>
> > *AI/ML — disclosed:* "The „intentional" label comes from GFW's machine-learning model and **is
> > a probability, not proof** (GFW says „likely"). We pass that on openly and make no accusation."
> >
> > *§4 Limits of the method:* "„Intentional" is ML-estimated, not proof; disabling can have
> > legitimate reasons (e.g. piracy zones). **No claim of illegality against vessel or state.**"
>
> **The one verbatim quotation — PASS, word for word.** Programmatic exact-substring test against
> the live method sheet text: **True.** Em dash, apostrophes and all.

## 6. The README as first-read document — FAIL

> It was **last touched in commit `2c42458` (session 81)** and is **not in tonight's working tree
> changes**. It was not brought forward with the page. It has the same defect it was corrected for
> last session, in three places.
>
> **Now false:** (1) *"Each stop prints the command that reproduces its own figure"* — precisely
> what was deleted tonight. **This is the exact failure banked as failure 24 last session,
> recurring on the same paragraph's successor.** (2) *"with the act went … the button"* — the page
> carries **seven** buttons with live click handlers. (3) *"The total has now grown three times …
> tested three times … and has held three times"* — it has now grown **four** times; the README
> names six gained ships where the face names nine.
>
> **Now stale:** (4) *"as measured now, 14 saved copies / 5 lists | 55 %–100 % | 11 of 0–20"* — the
> measurement now is **17 / 6, 44 %–100 %, 11 of 0–25**. This is the identical construction the
> correction block below it was written to bank; it went stale in session 81 and was not caught
> then either. (5) *"Fourteen saved copies, seven bodies, five lists … Two lists have come back in
> more than one set of bytes"* — now seventeen, ten, six, and **four** lists. (6) *"the page's last
> words are its own verbatim output and not fourteen rows"* — the last words are not the verbatim
> output, and the ledger is seventeen rows.
>
> **Not false, and worth saying so:** *"Every figure in this file is typed by hand and every one of
> them goes stale. The authority is the command below, not this page"* remains true and is the
> document's own honest guard. It mitigates items 4–6. It does **not** cover items 1–3, which are
> prose claims about what the page is and does, not figures.
>
> **The README is silent on every one of tonight's changes.** Its account of the head is the
> session-81 object.

## Summary, as given

> | # | Check | Verdict |
> |---|---|---|
> | 1 | New definition paragraph vs live upstream; hedge moved | **PASS** (one recorded overstatement: "register") |
> | 2 | Brysbaert 238 wpm citation and build-time arithmetic | **PASS** on citation and arithmetic; **FAIL** on traceability. Word count "44 words" counts a bare em dash as a word; true count 43 |
> | 3 | The cut | (a) PASS · (b) PASS · **(c) FAIL** — the share figure now stands on the face with no tier mark |
> | 4 | The numbers | **PASS** — exit 0, 0, 0; no mismatch, line by line |
> | 5 | Standing obligations; verbatim quotation | **PASS** |
> | 6 | README as first-read document | **FAIL** — three false sentences, three stale, silent on every change tonight |
>
> Two blocking items: **3(c)** and **6**. **2** needs one line of repair in either file. Nothing
> else on this face is unsourced, and the numbers are clean.

---

## What this house did about it, the same night, before anything was committed

**3(c) — REPAIRED, and it cost one sentence.** The head carries again:
*"DERIVED — this share is worked out here, from saved copies of those lists. Nobody publishes it."*
Self-contained, because a tier mark whose key is 400 px further down is a mark the head's own reader
cannot read; not a command; identical at every stop. **The body's legend was wrong too and is
corrected with it** — its DERIVED line named the spans and never the share, which is why the cut
could take the figure's only mark without any instrument noticing. It now reads *"the
dark-and-return spans, and this page's share — worked out here, both ends printed"*.
**And this repair is also the staging voice's §3, which asked in the same night for six words saying
the page reads saved copies.** Two voices, two grounds, one sentence.

**2 — REPAIRED in both files.** The URL now stands in `index.html` itself, in the file making the
claim, and the README carries the citation and the caveat. **And the word count is fixed at the
root:** a word is now a token with a letter or a digit in it, so the note prints **43 words** and
the beat is **10,840 ms**, measured on the built page at **10,926 ms** from navigation. This house
published a hand-checkable count that a library call had produced and nobody had counted — banked.

**6 — REPAIRED, six items, corrections beside the errors.** Two false prose claims are corrected in
place with dated correction blocks (the printed command; "the button" against seven live buttons);
the growth count goes from three to four with the fifth list's five ships named; three stale figures
are brought to 17 copies / 10 bodies / 6 lists / 44 %–100 %; and the head's paragraph now carries
the first beat, its citation, its caveat and the tier sentence.

**1's "register" qualification is NOT repaired tonight and is banked as owed item (u)**, with the
Verifier's own reasoning: the word asserts a completeness upstream disclaims, and the face's limits
sit below the premise rather than in it. It is a wording question about a live upstream caveat and
it goes to a frozen pre-registration, not to a 5 a.m. edit.
