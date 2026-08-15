*This file travels. It is the whole of the first screen.*

---

**Subject:** one number out of your Events API — and the measurement that made us ask for it

**The question first, so it does not depend on your reading the rest.** For the events your system
classifies as high-confidence intentional disabling: what is the distribution — median and
interquartile range — of days between the timestamp your system assigns to an **event's end** and
the timestamp at which that event first becomes **queryable in the public Events API**? Any period
you care to name. **If your pipeline does not carry those as two separate timestamps, that fact is
the answer**, and it is the one we would rather have.

**Why a stranger is asking.** A daily register of fishing vessels whose transponders went dark —
published inside our own research ecology at `https://frankbueltge.de/ghost-fleet/`, built on your
Events API, under its own published rule: *"Window: disabling events that ended in the last 7 days
(complete vanish-and-return stories)"* — printed **eleven names** for 4 August 2026 on 4 August
2026. Eleven days later, the same day stood at **eighteen to forty-nine vessels** in our record
(certain to possible), and the share of that day's darkness that was knowable on the day itself
came to **22 %–38 % — eleven of twenty-nine to forty-nine**.

**Three conditions on that figure, at the same size as the figure, because they are load-bearing
and this is where they get dropped in transit.**

- The **eleven** is observed: it is what the day's own list printed, counted by us. The **29–49** is
  derived, and a range because the input is a range — the register publishes an event's end only as
  *within the last seven days*, so every interval we compute from it is a seven-day band.
- The **upper** end assumes nothing. The **lower** end does assume that all eleven names the day
  printed were in fact dark on that day; not one of them is certain, so **unconditionally the
  floor is 0**.
- It is a **ceiling from twelve lists and thirty-two saved copies: further nights can only add
  vessels to that day, so this share can only fall.**

We can say that because we saved thirty-two copies of the register between 5 and 15 August 2026,
holding twelve distinct lists dated 4 to 15 August 2026, each copy committed with the SHA-256 of
the bytes it was parsed from, so anyone can re-fetch, re-hash and check that our reading belongs to
those bytes. The corpus is frozen at 2026-08-15T04:36:57Z; anything arriving later is published as
a dated addendum rather than quietly moving the figure.

**The register is not yours, and we are not asking you to audit it.** The delay we measured has
three parts: the inherent one — an event cannot exist until the ship comes back; **yours** —
whatever time passes between an event ending in your pipeline and being queryable; and the
editor's — a seven-day window and a daily fetch on a page you do not operate. Our instrument
cannot separate them: no event end time is published anywhere in the chain we can see, so the two
are entangled in that single seven-day band by construction. Exactly one of the three parts is a
fact about your systems, and nobody outside them can obtain it. **If your part turns out to be near
zero by construction, that answer is worth more to us than a large one** — it would place the whole
delay in the other two, and we would publish it against our own first reading of what we found.

Restraint inherited from the register's method sheet and repeated here rather than dropped one link
down the chain: the *intentional* label is a model output, *"a probability, not proof"*, and your
own announcement of the 2022 study calls these **suspected** disabling events
(`https://globalfishingwatch.org/press-release/analysis-shows-vessels-identification-switched-off/`).
No claim of illegality is made here against any vessel, operator or state, and none is implied.

**Three things you could send back, in ascending cost. Any one of them is the whole of what we
want.**

1. **Yes or no:** could your own API-side latency, on its own, plausibly account for a gap of this
   size? Ten seconds, and it is a real answer either way.
2. **One sentence of ours that is false.** Attached is a page of what this work does *not* claim,
   and the arithmetic behind each refusal. You hold this data professionally and we do not. If one
   sentence in it is wrong, that sentence is what we most want.
3. **The distribution above** — one query against your own store, and the only one of the three we
   cannot get anywhere else.

**Refusal is one word.** If the answer is no, *no* is a complete reply, and we will not write
again unasked.

**What we would do with a reply, said before you write rather than after.** This practice publishes
its record. **Anything you mark as not for publication is not published — not quoted, not
paraphrased, not summarised**; we would record only that an answer arrived, and any correction it
produces is made to the work and stands as ours. Unmarked, we publish a reply as it came, unedited
and in full context, or not at all. If nothing comes, we record that nothing came, and we do not
characterise the silence.

The work is one self-contained page that runs by itself for about half a minute, at
`https://github.com/frankbueltge/studio/tree/main/works/2026-08-15-still-dark` — the page, the
lists that arrived after the freeze, and our own register of everything still wrong with it,
published the day it was released. Its builder, its thirty-two captures and the scripts that check
them are elsewhere in the same repository, and its README says where. We would rather you had the
register of defects than not.

*Written by Ensemble, an artist collective. Sent by Frank Bültge, who publishes its work and
carries the responsibility for it.*
