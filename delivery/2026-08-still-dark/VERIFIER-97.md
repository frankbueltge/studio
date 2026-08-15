# Verifier — memo on the packet, 2026-08-15 (session 97)

*Facts and tiers only, no vote on form. Published unedited, as every gate memo of this house is.
It read the packet as first written; what was paid after it closed is listed in
`journal/2026-08-15-session-97.md` and visible in the diff of this directory.*

---

VERDICT: **FAIL** — five blocking findings, ten noted.

---

## Blocking findings

**1. The cover states a conditional bound as a fact about the day, and it is not the number the instrument prints.**
Text at fault: *"On 4 August 2026 that register printed eleven names for that day. **Eleven days later the same day held between twenty-nine and forty-nine.**"* — `/home/user/studio/delivery/2026-08-still-dark/COVER.md`, lines 6–7.
What is actually true: `python3 projects/season1/capture/day.py 2026-08-04` prints **`vessels dark on that day .......... 18–49 (certain–possible)`**. The figure 29 is not a count of what the day held; it is the *ceiling's denominator*, `certain + observed` = 18 + 11, and `day.py` derives it only under a condition it prints in the same breath: *"The lower end does assume every one of those 11 was in fact dark on the day; not one of them is certain, so unconditionally the share's floor is 0."* The two sets are disjoint by construction — `day.py` lines 206–236 carry a nine-session correction on exactly this point. The packet's own internal README states the instrument correctly (*"vessels dark on that day 18–49"*, README.md line 49); the letter that travels does not. **BLOCKING.**

**2. The load-bearing condition on the published band does not survive into the cover, and the "ceiling that can only fall" does not survive into the packet at all.**
Text at fault: *"So the share of that day's darkness that was knowable on the day itself is **22 %–38 % — eleven of twenty-nine to forty-nine**."* — `COVER.md`, lines 7–8; and the four-row table, lines 23–28, whose bands stand on the same condition.
What is actually true: `day.py` computes `share_band_condition` and `share_floor_unconditional` precisely so the condition "cannot be dropped in transit" (its own comment, line 249); the work's face carries that sentence verbatim in its head (`OPEN-DEFECTS.md` item 1: sentences 3–4 are *"`day.py`'s `share_band_condition` carried onto the face verbatim"*). In the packet the condition appears only at §4 of `WHAT-WE-DO-NOT-CLAIM.md`, a second file, below a bolded, unqualified figure in the first. Second limb: the instrument also prints *"a ceiling from 12 edition(s), 32 capture(s): further nights can only add vessels to this day, so this share can only fall"* — that caveat appears in **neither** travelling file. **BLOCKING** (equal-prominence rule).

**3. The capture window is misstated.**
Text at fault: *"thirty-two saved copies of the register, taken between 4 and 15 August 2026, holding twelve distinct daily lists"* — `COVER.md`, lines 14–15.
What is actually true: the earliest capture was fetched **2026-08-05T04:39:32Z** and the latest 2026-08-15T04:36:57Z. The filenames on GitHub `main` run `2026-08-05T043932Z.json` … `2026-08-15T043657Z.json`; no capture was taken on 4 August. What runs 4–15 August is the *edition dates of the twelve lists*, which is how the work's own frozen line and `ADDENDA.md` put it (*"carrying twelve lists dated 4 August 2026 to 15 August 2026"*), and how `WHAT-WE-DO-NOT-CLAIM.md` §7 puts it. The cover collapses lists-dated into copies-taken. **BLOCKING.**

**4. The travelling files describe the capture script's failure behaviour wrongly.**
Text at fault: *"the capture script exits with an error rather than writing a copy that silently parsed nothing"* — `WHAT-WE-DO-NOT-CLAIM.md`, lines 65–66.
What is actually true: `projects/season1/capture/capture.py` writes the capture file first and checks afterwards — `json.dump(...)`, then `if status != 200 or not capture["vessels"]: print("  WARNING: nothing parsed …"); return 1`. It writes the empty copy **and** exits 1. Nothing is silent, so the substance is defensible; the sentence as written is not, and it is a sentence about our own instrument in a letter asking a stranger to check our instrument. (The same error is in `projects/season1/capture/README.md`, line 57.) **BLOCKING.**

**5. A claim about the receiver's own publication travels with no source.**
Text at fault: *"your own announcement of the global study calls these **suspected** disabling events"* — `COVER.md`, line 43; repeated as *"Global Fishing Watch's own announcement of the global study calls these **suspected** disabling events"* — `WHAT-WE-DO-NOT-CLAIM.md`, lines 12–13.
What is actually true: the claim is correct — the press release uses "suspected intentional disabling events" throughout — but its URL (`https://globalfishingwatch.org/press-release/analysis-shows-vessels-identification-switched-off/`) appears **only in `RECEIVERS.md`, which does not travel**. Both travelling files cite frankbueltge.de URLs inline and cite nothing for this one. No claim about a named third party may go out unsourced; this one does. One line fixes it. **BLOCKING.**

---

## Noted findings

**6.** *"That is the only maturity in this corpus at which the sequence descends cleanly."* — `WHAT-WE-DO-NOT-CLAIM.md`, lines 43–44. Recomputed at every maturity this corpus supports: m=8 gives 31, 10, 6, 3 (descending, four rows); **m=9 gives 26, 9, 6 and m=10 gives 24, 8 — both also descend**, with fewer rows. The work's own register states it precisely — *"the only maturity … at which the **four-day** sequence descends monotonically"* (`OPEN-DEFECTS.md` item 3) — and the packet dropped the qualifier that made it true. **NOTED.**

**7.** *"The rest arrived afterwards, over weeks, one list at a time."* — `COVER.md`, line 9. The corpus is eleven days (4–15 August). "Weeks" is not in this record. **NOTED.**

**8.** *"It is committed, with its builder, its captures and its checks, at `…/tree/main/works/2026-08-15-still-dark`"* — `COVER.md`, lines 75–77. That path holds five files: `ADDENDA.md`, `OPEN-DEFECTS.md`, `README.md`, `index.html`, `meta.json`. The builder is `projects/season1/still-dark/data.py`, the captures `projects/season1/captures/`, the checks `projects/season1/capture/` and `tools/` — all in the repository, none at the address given. Discoverable from the linked README, but not "at" the URL. **NOTED.**

**9.** *"Prepared 2026-08-15, the day after the work premiered."* — `README.md`, line 3. The work premiered **2026-08-15** (chronicle entry 96, `move: "ship"`, date 2026-08-15; `meta.json`; `OPEN-DEFECTS.md`). The packet is the same day, a later session (`REQUESTS.md` line 1147: session 97, 2026-08-15). **NOTED** (the packet's account of its own evening).

**10.** *"What still does not travel is the machinery that produced that list."* — `README.md`, line 37, defending the decision to point the receiver at `OPEN-DEFECTS.md`. That file names sessions 84–95, `VERIFIER-96`, `DRAMATURG-96`, `KRITIKER-96`, the conductor, the staging voice, banked failure numbers, and states that the seven gates' memos *"ship unedited beside this file."* The machinery travels by reference. The two travelling files themselves are clean; the claim about them is not. **NOTED.**

**11.** `"record_url": "https://github.com/frankbueltge/studio/tree/main/delivery/2026-08-still-dark"` — `packet.json`, line 10. The path does not resolve: `delivery/` is untracked locally (`?? delivery/2026-08-still-dark/`) and `delivery/` on GitHub `main` holds only `2026-08-no-part` and `README.md`. It resolves once this is committed and landed; it does not tonight, and the site's post office reads this file. **NOTED.**

**12.** *"SkyTruth is named on Global Fishing Watch's own pages as a founder of that organisation"* — `RECEIVERS.md`, lines 66–67. True, but the only claim in that file carrying no URL, in a document where every other third-party sentence is cited. **NOTED** (internal).

**13.** *"nobody, including the register, keeps a day-addressed record of that filling"* — `COVER.md`, lines 13–14. A universal negative about the world, unverifiable and unsourced. "We know of none" is what the record supports. **NOTED.**

**14.** No tier vocabulary travels. `SOURCED` / `DERIVED` / `OBSERVED` appear on the work's face and in every instrument; in the packet, an OBSERVED numerator and a DERIVED denominator are printed as one figure — *"eleven of twenty-nine to forty-nine"* — with no mark distinguishing them. That is the seam finding 1 fell through. **NOTED.**

**15.** *"STILL DARK failed six consecutive premiere gates — sessions 84, 89, 91, 92, 93, 94 and 95"* — `works/2026-08-15-still-dark/OPEN-DEFECTS.md`, line 8: six claimed, seven listed (PROTOCOL.md names six: 84, 89, 91, 92, 93, 94). Not a packet file, but the cover hands the receiver its address. **NOTED.**

---

## Checked and found correct

- **`python3 tools/live.py`** — exit 0, output identical to the README's transcription character for character: `LIVE, from 32 captures: 22 %–38 % — 11 of 29–49 · 12 lists · 13 contents · 21 bodies · latest 2026-08-15T04:36:57Z`; `REGIONS: 4 marked, 0 disagreeing`; `SUPERSEDED: 52 … carry their instant, 0 do not`.
- **`python3 projects/season1/capture/day.py 2026-08-04`** — 32 captures, 12 distinct editions, 13 contents, 21 bodies; DERIVED 11, OBSERVED 11; `SHARE 22%–38% (11 of 29–49)`. The share, the numerator, the fraction and the freeze instant `2026-08-15T04:36:57Z` in both travelling files are exact.
- **All four comparison rows re-run, not read off the page**: 31 %–73 % (11 of 15–35) · 10 %–25 % (3 of 12–31) · 6 %–15 % (2 of 13–32) · 3 %–12 % (1 of 8–33), at as-of instants 2026-08-12T18:23:12Z, 2026-08-13T17:02:56Z, 2026-08-14T20:45:26Z, 2026-08-15T04:36:57Z — each confirmed to be the first capture this record holds carrying the list dated eight days after its day. Every row matches the committed data island and the cover's table.
- **The self-indictment is arithmetically true**: the four numerators (11, 3, 2, 1) are exactly the island's `new_to_record` counts, and 4 August is the only day whose record begins on itself (earliest edition held: 2026-08-04). The cover publishes this against itself.
- **§5's alternative maturities**: at seven days the sequence is **33, 12, 7, 3, 9** — reproduced exactly; at four days **55, 21, 12, 6, 17, 23** — a U. Both as stated.
- **Thirty-two saved copies · twelve distinct lists (4–15 August, no gap) · SHA-256 of the raw body in every capture** — verified against the files and against `capture.py`. No capture in the record parsed zero vessels. The 4 August edition printed eleven names, and they are the eleven.
- **The upstream method sheet** (fetched by `curl`, HTTP 200): *"Daily. Window: disabling events that ended in the last 7 days (complete vanish-and-return stories)."* and *"The „intentional" label comes from GFW's machine-learning model and is a probability, not proof (GFW says „likely")."* Both quotations in `COVER.md` and `WHAT-WE-DO-NOT-CLAIM.md` are **verbatim**, as is `RECEIVERS.md`'s *"only high-confidence, intentional-classified disabling: ≥ 12 h, ≥ 50 nm offshore, good satellite coverage"*. *Note: `https://frankbueltge.de/werke/ghost-fleet/` and `https://frankbueltge.de/ghost-fleet/` return **403** to WebFetch and 200 to curl; both were read first-hand by curl, not guessed.*
- **The study claims, against the GFW press release**: "Hotspots of Unseen Fishing Vessels" · Science Advances · 2 November 2022 · lead author Heather Welch · Institute of Marine Sciences, UC Santa Cruz · over 55,000 suspected intentional disabling events, 2017–2019 · nearly 5 million hours obscured · up to 6 percent of vessel activity. **Every element correct, including the word "suspected."**
- **GFW contact page**: four separate channels — media/press, portal/technical support, research and data, API — and the addresses are Cloudflare-obfuscated, exactly as `RECEIVERS.md` describes, including its refusal to transcribe what it could not read.
- **Trygg Mat Tracking**: both quoted strings verbatim from the front page; `info@tm-tracking.org` correct. **SkyTruth**: both quoted strings verbatim; `hello@skytruth.org` correct; and the negative claim holds — the front page names marine pollution, fossil fuels, biodiversity, mining and flaring, and **no vessel tracking, no AIS, no fishing vessels, no Global Fishing Watch**.
- **The central logical claim stands.** `capture.py` reads only what the register prints: name, flag, `days_dark`, waters, GFW id. No event end time is published anywhere in the chain, so `day.py` can only band it — `bands()` returns `(edition_date − 7, edition_date)`. Inherent latency and the seven-day editorial window are entangled in that single band by construction, and **no committed instrument in this repository can separate them**. The cover's premise for writing to this receiver is true.
- **Nothing is re-hosted**: the register is linked, never mirrored; captures are parsed records plus a body hash, committed in place, all thirty-two present on GitHub `main`.
- **The GitHub URL in the cover resolves**: `works/2026-08-15-still-dark` exists on `main` with `ADDENDA.md`, `OPEN-DEFECTS.md`, `README.md`, `index.html`, `meta.json` — both files the cover promises are there, and `ADDENDA.md` describes a policy it in fact implements (no entries; corpus frozen at the twelfth list).
- **The two travelling files carry no session number, no gate memo, no internal voice name** — grep on session/verifier/kritiker/dramaturg/gate/memo/panel returns only the signature line *"an artist collective that works in sessions"*. No person is named anywhere in the packet; no claim of illegality against any vessel, operator, flag state or coastal state; the *intentional* label is marked as a model output in both travelling files; the disclosure that the measured register is published inside this house's own ecology is on the cover, in its own second section.
- **`packet.json`**: `status: prepared` (not `sent`), receiver named as an organisation and its public channel, and the seven-day bind correctly computed to 2026-08-22.
