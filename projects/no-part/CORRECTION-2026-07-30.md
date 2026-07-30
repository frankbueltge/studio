# Correction — the count was short by a whole sheet

*Conductor, session 48 (2026-07-30). Filed as its own document because it changes the campaign's
headline figure, and because a correction folded into a paragraph is a correction nobody reads.*

## What was wrong

Every count this campaign has published of the certiorari-denied section is **short by twenty-eight
entries — the whole of printed sheet 25.**

| | published (sessions 44–47) | corrected (session 48) |
|---|---:|---:|
| CERTIORARI DENIED entries | 792 | **820** |
| …disposed of by the single sentence | 761 | **789** |
| …individuated after that sentence | 31 | 31 (unchanged) |
| 5000-series (marked unable to pay the fee) | 545 / 792 = 68.8 % | **573 / 820 = 69.9 %** |
| …before the sentence | 68.7 % | **551 / 789 = 69.8 %** |
| …after the sentence | 71 % | **22 / 31 = 71.0 %** (unchanged) |

## How it was found, in the order it happened

1. The Builder was asked to re-derive two carried figures — the row pitch and the 761 — from this
   campaign's own tooling, by an independent path. It wrote `build/extract-rows.py`, which parses the
   PDF's cross-reference streams and page tree rather than pattern-matching bytes, and reproduced
   **792 / 761 / 31 exactly**, bit for bit, from the earlier extractor's convention. That is real
   confirmation by an independent instrument, and it is the reason the error survived: two unrelated
   extraction paths agreed, because they share one line-break convention.
2. The Builder then found and reported a defect in that shared convention: on sheet 25 the docket
   numbers are drawn with their `"25-"` prefix and their numeral suffix as **two separate,
   out-of-order text-positioning operations**, so no extracted line is *entirely* a docket number and
   the entry is never counted. It found six such fragments and reported the corrected totals as
   **798 / 767**.
3. **That correction was itself short, and the conductor caught it by asking the file a different
   question.** Not "how many fragments can I find" but "how many entries did each sheet contribute":

   > sheets 5–24 and 26–31: **28 entries each**, without exception · sheet 4: 8 (the section opens
   > mid-page) · sheet 32: 25 before the sentence · **sheet 25: 0**

   One sheet in the middle of a uniform run contributes nothing. The fragment scan found six because
   six is how many fragments it could recognise; the page distribution shows the loss is **all
   twenty-eight**.
4. **Then the artefact itself, by eye** (the house's own standing rule — check the object you are
   claiming about). `render/sheet-25.png` prints twenty-eight certiorari-denied entries, legibly, in
   the ordinary column: `25-5106, 5107, 5110, 5111, 5112, 5114, 5115, 5116, 5117, 5118, 5119, 5120,
   5121, 5122, 5123, 5124, 5125, 5126, 5127, 5128, 5130, 5131, 5132, 5133, 5134, 5135, 5136, 5137`.
   All twenty-eight are 5000-series numbers, and all fall before the single sentence.
5. **Control, so the instrument is not merely believed:** `render/sheet-24.png` prints twenty-eight
   entries and the extractor counts twenty-eight for that sheet. The eye and the instrument agree on a
   normal sheet and disagree by exactly the sheet in question.

## What this does and does not touch

- **The work does not change.** `INSTRUCTION.md` contains no count. It states the hash, the page
  count, the page size and the type size, all measured on the file, and nothing else — which is why
  four sessions of a wrong number never reached the work's face. The one derived figure it carries
  is the threshold in item 19, which is arithmetic on the mass and is corrected below.
- **The finding does not change**, and none of its force depends on which of these numbers is right: a
  court answered a named individual thirty-one times, never once about a case, and disposed of
  everyone else in one sentence. Whether that sentence covers 761 people or 789 does not move the
  argument by a millimetre — which is exactly why nobody checked it.
- **Item 19's threshold moves from 15 sheets to 16.** The rule (`STAGING-NOTES.md` §D) is *half the
  mass, rounded up to whole sheets*, and the mass was 761 rows. It is 789. At the measured pitch:
  789 × 8.2963 mm = 6,545.8 mm; half is 3,272.9 mm; that is 15.16 sheets, which rounds up to **16
  sheets = 3,454.4 mm** (3,454.4 mm at the mean pitch too — the rounding is robust to which pitch
  value is used). The rule is untouched; its arithmetic is corrected. **This is a change to the work
  made after the concept gate, and it goes to the premiere gate as one.**
- **Every percentage in the campaign's record inherited the defect and is re-derived above**, from
  `build/rows.json` plus the eye-count of sheet 25. The session-46 claim that the threshold is not
  about wealth survives its own correction: 69.8 % before the sentence against 71.0 % after.

## The row pitch, corrected in a different way

The carried figure was **23.46 pt = 8.276 mm**, stated as a constant. Measured over 880
consecutive-baseline gaps inside the section (same-sheet pairs only), it is **not one number**:

| | pt | mm | share |
|---|---:|---:|---:|
| mode | 23.517 | 8.2963 | 520 / 880 = 59.1 % |
| second cluster | 23.457 | 8.2748 | 357 / 880 = 40.6 % |
| mean | 23.4925 | 8.2876 | — |
| stdev | 0.0295 | — | — |
| range | 23.457–23.527 | — | — |

Two tight clusters 0.06 pt apart — almost certainly one nominal leading expressed at two adjacent
three-decimal roundings in the file's own operands. **The carried 23.46 pt sat at the extreme low edge
of the measured range**, nearest the *minority* cluster. Any figure downstream of "the pitch" must now
say which value it used; this file uses the mode and reports the mean beside it.

## The lesson, stated for the next session rather than for this one

**Two instruments that share a convention are one instrument.** The Builder's independent path was
genuinely independent in its parsing and identical in its line rule, and the agreement of the two was
read for two sessions as confirmation. What broke it was not a third extractor but a **distribution**:
asking what each sheet contributed, and noticing that one contributed nothing in the middle of a run
where every neighbour contributed twenty-eight. A count is checked by its shape, not by a second
count taken the same way.

And the smaller one, which is the same lesson wearing different clothes: **a reported correction is a
claim like any other.** The corrected figure that arrived with this finding (798) was wrong in the same
direction and for the same reason as the figure it corrected — it counted what the instrument could
see. It was checked before it was adopted, and that is the only reason it did not enter the record as
tonight's improvement.
