# The nightly capture — STILL DARK's evidence chain

Two scripts, no dependencies beyond Python 3 and `curl`.

```
python3 capture.py                      # fetch tonight's edition, write one immutable capture
python3 day.py 2026-07-15               # hold one calendar day open and ask the work's question
python3 day.py 2026-07-15 --json        # the same, machine-readable
python3 edition.py                      # every capture: body hash, edition hash, edition, vessels
```

`capture.py` writes `../captures/<UTC timestamp>.json` and never overwrites. Each capture
records the URL, the UTC fetch time, the HTTP status, the byte count and the **sha256 of the raw
body**, so anyone can re-fetch the page, hash it, and check that our parse belongs to those bytes.

**The case of the day's waters, since 2026-08-06 (session 73).** Upstream prints one vessel per
edition as a prose sentence rather than as a row, and this parser wrote `waters: null` for it. So
TUNAMAR stood on the work's face with an empty waters column for five nights while the fact sat in
our own capture, inside its sentence. The parser now takes the sentence's trailing *"…, in
&lt;waters&gt;."* — upstream's words, verbatim; only the cut is ours, so the value stays SOURCED —
and `data.py` performs the same cut at build time for the captures already committed, because
**captures are immutable and none was rewritten.** Where a sentence carries no waters, the field
stays null rather than guessing.

**Two hashes, since 2026-08-06 (session 70), because the record contradicted the instrument.**
Until that night an edition was identified by the sha256 of the raw body, and on that test the
19:17 capture of 5 August was "the same edition, byte for byte" as the 12:54 one. The capture of
2026-08-06T04:36:19Z broke the test: **the body hash moved at an identical byte count while every
field this work reads stayed identical.** So `edition.py` computes a second digest,
`content_sha256`, over the edition's own material only — the printed edition date, the
aggregates, the case of the day, the vessels. A body hash answers *did the response change*; the
content hash answers *did the edition change*. It is computed from a capture file alone, so it
applies to captures written before it existed, and **no committed capture was rewritten to add
it**: captures are immutable, and a record that gets edited when the method improves is not a
record. From that night's capture onward, `page_assets` also records the site's own fingerprinted
asset paths — outside the edition and outside every tier, kept only so that a body hash which
moves while the edition stands still can be attributed rather than guessed at. For the
2026-08-06 capture it cannot: the earlier bodies were never kept, only their hashes, and this
house does not claim to know what moved.

`day.py` reads every committed capture and answers: for one calendar day, how many vessels were
dark on it, and how many of them were knowable on the day itself. It prints **two** answers and
never merges them —

- **DERIVED** — from a single capture. The upstream window is *"disabling events that ended in the
  last 7 days"*, so an event's end is known only as a 7-day band, and every interval derived from
  it is a band. A vessel is `certain` for a day if it was dark on that day under **every** end in
  the band, `possible` if under **some**. The answer is a range because the input is a range.
- **OBSERVED** — from our own accumulation. A vessel was knowable on day T if it stands in a
  capture whose edition date is on or before T. Where no capture from on or before T exists, the
  script says *not yet measurable* and **refuses to print the DERIVED share in its place.**

That refusal is the point. Substituting a derivation for a measurement is the blur this work
exists to refuse, and gate condition C1 forbids it: no time is ever attached to a vessel name
unless it is observed in a committed capture or derived from a published duration with both ends
of its uncertainty printed.

**Restraint inherited from upstream, and repeated wherever these numbers travel:** *"intentional"*
is a machine estimate by Global Fishing Watch, *"a probability, not proof"*; the instrument
**makes no claim of illegality** against any vessel or state, and neither do we.

Sources — `https://frankbueltge.de/ghost-fleet/` (the edition) ·
`https://frankbueltge.de/werke/ghost-fleet/` (the method sheet, from which the window sentence is
quoted verbatim in `capture.py`).

If the page's markup changes, `capture.py` exits non-zero with a warning rather than writing a
capture that silently holds nothing. A gap in the nightly record is a fact about the record; a
capture that quietly parsed nothing would be a lie in it.
