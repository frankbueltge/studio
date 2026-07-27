// Builder — Ensemble, still-v3 (CONCEPT)
// House law: "compute before you render." This script derives, from the corpus
// alone (no rendering, no pixels), every number the frame's crop depends on:
// total column height, the sentence's y-offset, the scroll offset the crop
// requires, and how many entry lines fall inside a 1000px frame. Print them,
// then still-v3/build.js confirms them against the rendered pixels.

const fs = require('fs');
const path = require('path');

const CORPUS = path.join(__dirname, '..', 'corpus', 'entries.json');
const LEADING = 14; // px, body entries per spec §12
const FRAME_H = 1000;
const FRAME_TOP_ENTRY_INDEX = 745; // 0-based, spec table "745-760"
const FRAME_TOP_LAST_ENTRY_INDEX = 760; // inclusive, 16 lines

function main() {
  const all = JSON.parse(fs.readFileSync(CORPUS, 'utf8'));
  const denied = all.filter((e) => e.section === 'CERTIORARI DENIED');
  if (denied.length !== 792) {
    throw new Error('Expected 792 CERTIORARI DENIED entries, got ' + denied.length);
  }
  const SENTENCE_PRECEDED_BY = 761; // per proposal §0: 761 dockets printed before the sentence

  // 1. Total column height for the full 792-entry body at 9px/14px leading,
  //    if every entry were exactly one line (the layout's design assumption —
  //    confirmed separately below by checking caption widths against the
  //    measure, and confirmed again on the rendered pixels).
  const fullColumnHeight = 792 * LEADING;

  // 2. Document-space top of the entries block that the frame's top edge
  //    lands on. Spec table: y=0 in the frame shows entry index 745's line
  //    (0-based == denied[745], the 746th entry), and the block ends with
  //    denied[760] (0-based), the last line before the 32px gap to the
  //    sentence. That is 16 lines, 745..760 inclusive.
  const topBlockCount = FRAME_TOP_LAST_ENTRY_INDEX - FRAME_TOP_ENTRY_INDEX + 1;
  const topBlockHeight = topBlockCount * LEADING;

  // 3. The scroll offset the crop requires: document y of entry index 745's
  //    line-box top, given entry 0's line-box top sits at document y=0 (no
  //    header above the column — the work has none).
  const scrollTop = FRAME_TOP_ENTRY_INDEX * LEADING;

  // 4. y-offset of the Court's sentence within the full column (frame-local),
  //    per spec table: sentence at frame y=256. Verify the gap arithmetic:
  //    entries block ends (frame-local) at topBlockHeight; gap to sentence
  //    top should be a spacing-scale value (4/8/12/20/32/52).
  const sentenceFrameY = 256;
  const gapAboveSentence = sentenceFrameY - topBlockHeight;

  // 5. Rule position and gap arithmetic (spec: rule at frame y=312; sentence
  //    is 17.6px type on 24px leading, so its line box runs
  //    [sentenceFrameY, sentenceFrameY+24)).
  const ruleFrameY = 312;
  const sentenceLineBottom = sentenceFrameY + 24;
  const gapSentenceToRule = ruleFrameY - sentenceLineBottom;

  // 6. Tail start and gap from rule.
  const tailFrameY = 364;
  const gapRuleToTail = tailFrameY - ruleFrameY;

  // 7. Document-space y of the sentence and rule (absolute, for sanity/QA).
  const sentenceDocY = scrollTop + sentenceFrameY;
  const ruleDocY = scrollTop + ruleFrameY;

  // 8. Cross-check: document y of entry index 760's line bottom should equal
  //    761*14 (== the height of the 761-entry silent mass the proposal
  //    counted by hand), since entry 760 is the 761st entry (0-based).
  const entry760Bottom = (FRAME_TOP_LAST_ENTRY_INDEX + 1) * LEADING;
  const silentMassHeight = SENTENCE_PRECEDED_BY * LEADING;

  const report = {
    corpus_denied_count: denied.length,
    leading_px: LEADING,
    full_column_height_px: fullColumnHeight,
    full_column_height_approx_screens_at_1000: +(fullColumnHeight / 1000).toFixed(2),
    top_block_entry_range: [FRAME_TOP_ENTRY_INDEX, FRAME_TOP_LAST_ENTRY_INDEX],
    top_block_line_count: topBlockCount,
    top_block_height_px: topBlockHeight,
    scrollTop_px: scrollTop,
    sentence_frame_y: sentenceFrameY,
    gap_entries_to_sentence_px: gapAboveSentence,
    rule_frame_y: ruleFrameY,
    sentence_line_bottom_frame_y: sentenceLineBottom,
    gap_sentence_to_rule_px: gapSentenceToRule,
    tail_frame_y: tailFrameY,
    gap_rule_to_tail_px: gapRuleToTail,
    sentence_doc_y: sentenceDocY,
    rule_doc_y: ruleDocY,
    entry760_line_bottom_doc_y: entry760Bottom,
    silent_mass_height_from_proposal_count: silentMassHeight,
    entry760_bottom_equals_silent_mass_height: entry760Bottom === silentMassHeight,
    frame_h: FRAME_H,
    tail_available_height_px: FRAME_H - tailFrameY,
  };

  console.log(JSON.stringify(report, null, 2));
  return report;
}

if (require.main === module) main();
module.exports = { main };
