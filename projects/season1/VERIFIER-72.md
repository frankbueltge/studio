# VERIFIER-72 — blocking pass: **DEFECTS FOUND**, four, all corrected the same night

*Two of the four were introduced tonight, by the very rewrite that took the house's filing words
off the face.*

**D1 — the legend blurred a tier, and it was the line the panel scored against.** The face printed
*"DERIVED — every date on this page."* False: the list dates are SOURCED (the footer says so), the
fetch times and `first seen` are OBSERVED, the commit time neither. **Only the dark-and-return
spans are derived**, and that is what it now says. Written tonight, in this session's own rewrite
of the legend.

**D2 — the struck figure contradicted the page's own provenance line.** The face printed *"as this
page published it … until 2026-08-06T04:36:19Z"* — the last saved copy it was computed from, not a
publication time — while four lines below the same page dated its publication 04:57:03Z. As written
it said the page published a figure until twenty-one minutes before it printed it. Corrected to
*"as this page published it at 04:57 UTC on 6 August"*; the as-of instant survives as the third
command's argument. **The time is now read from git** (`data.py: commit_time`), not typed.

**D3 — a publication event this record never observed.** The lede claimed ships *"stood in the
list published on the day itself."* The earliest saved copy is 2026-08-05T04:39:32Z; **there is no
capture from 4 August**, and upstream prints a bare date plus *"Daily."*, not a publication
instant. The two changeovers we did observe support the inference; they are not it. Corrected to
*"the list dated the day itself."* Also written tonight.

**D4 — a false first in this house's own record.** `README.md` called the sixth saved copy *"the
first night that added nothing to this day."* The 19:17:55Z and 04:36:19Z copies added nothing
either. Corrected there and in `PROJECT.md`, which carried it too.

**Two notes, not defects, entered so they are not lost.** TUNAMAR's waters cell is blank on the
face while capture 1's case-of-the-day prose carries *"Ecuadorian EEZ (Galapagos)"* — a SOURCED
value dropped by the parser, not invented; changing the parser would change how every future copy
reads, so it is owed, not done. And at `5968048` the quoted law stood behind a reader's action;
*"printed on this page"* is true and unqualified.

**Checked sound:** `data.py --check` exit 0 · `day.py … | head -6` byte-identical to the face, so
*"verbatim, unedited"* holds · `--as-of` reproduces 79 %–100 %, 11 of 0–14 · all sixteen vessels
match the captures, none invented, none dropped · the ledger matches all six copies field for
field · the byte-difference caption verified against content `47338b03` across bodies `17c07fc3`
and `aed92f4f` · the lede's 11 / 5 / 2 reproduce · both new ships first seen 08:16:42Z, after
04:57:03Z · `5968048` carries the quotation verbatim and introduced it · upstream's restraint
intact · the 4 AUG rule label whole at both widths.
