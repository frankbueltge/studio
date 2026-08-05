# The nightly capture — STILL DARK's evidence chain

Two scripts, no dependencies beyond Python 3 and `curl`.

```
python3 capture.py                      # fetch tonight's edition, write one immutable capture
python3 day.py 2026-07-15               # hold one calendar day open and ask the work's question
python3 day.py 2026-07-15 --json        # the same, machine-readable
```

`capture.py` writes `../captures/<UTC timestamp>.json` and never overwrites. Each capture
records the URL, the UTC fetch time, the HTTP status, the byte count and the **sha256 of the raw
body**, so anyone can re-fetch the page, hash it, and check that our parse belongs to those bytes.

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
