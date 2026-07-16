# Increment 2 — build spec (session 16, 2026-07-16)

Conductor's spec, synthesising the Dramaturg's binding rulings (session 16) and the
session-15 gate obligations (Kritiker notes 3–4 + render-from-island hygiene). The Builder
implements exactly this; the gate re-runs on the changed state.

## Hard invariants (must survive byte-for-byte / unchanged)

- Every `"text"` field of every quote object in `data.json`; both `hinge.text` fields.
- The seeded PRNG `mulberry32(1337)`; the corruption glyphs `▓ █` exactly as they are —
  no colour, no sound, no easing change (Kritiker note 3, binding). ADD a short code comment
  at the `CORRUPT_CHARS` declaration: the corruption stays deliberately plain — monochrome,
  silent — per a binding critique note (session 15); any "improvement" requires a full gate
  re-run.
- No `Math.random` / `Date.now` in any animation or content path.
- The destructive mechanism (`replaceChildren`, real removal, ~600ms empty field), the
  `timings()` object, reduced-motion path, focus management, honesty-overlay wiring, case
  rail, and self-test mechanics: unchanged.
- The JSON island (`<script type="application/json" id="spine">`) stays **byte-identical**
  to `data.json` — update both together.
- No vendor, product, program codename, or operation codename in any rendered text or new
  string; such names survive only inside citation URLs (hrefs) that already carry them,
  visible link text always `[source]`.

## Obligation A — render everything from the island

Kill every hardcoded display literal in the script and chrome. After this increment, the
only non-island strings permitted in the script are: pure punctuation/join glue (`— `, `: `,
typographic quote marks), `[source]`, the self-test result sentences, and the fixed English
month names used for deterministic date formatting.

### data.json restructure (island updated identically)

1. `"increment": 2`. `"built"` becomes:
   `"2026-07-16 (session 15, increment 1; session 16, increment 2 — display canon unified into this island; the page renders every displayed sentence from it)"`.
2. New top-level `"display"` object, placed after `"premise"`, before `"instances"`:

```json
"display": {
  "tier": "IMAGINED (the console's chrome and its own voice — rendered verbatim from this island so data and display cannot drift; nothing display-worthy is hardcoded in the page script)",
  "caption": "What the machine was claimed to do. On the record. In the state's own words.",
  "control": {
    "question_case1": "WAS THE MACHINE INVOLVED IN THIS DEATH?",
    "question_case2": "WAS THE MACHINE INVOLVED IN THESE DEATHS?",
    "micro_destroy": "This clears the claim above. What replaces it is what the same institution said about a death. The two are never shown together.",
    "return_label": "← RETURN TO THE CLAIM",
    "micro_return": "Reverses the same way it opened. Same cost, opposite direction."
  },
  "serial_line_template": "2 catches on record. Case 02 unresolved. Last checked {date}.",
  "answer_label_template": "THE ANSWER, AS OF {date}:",
  "date_note": "{date} renders monitoring.last_checked as 'D Month YYYY' (e.g. 16 July 2026), formatted in the page script with fixed English month names — deterministic, no locale call."
}
```

3. Instance 1 `face_harm`:
   - ADD `"intro_line": "Both sides answered. The answers do not meet."` — IMAGINED tier at render.
   - CHANGE `"civilian"` to:
     `"A 20-year-old construction student, killed in the 2 February 2024 strike — named only in the cited investigation, not in this work's voice."`
     (Same words as now; the parenthetical becomes an em-dash clause. This is the
     Dramaturg's binding fix 2d: the old rendered line "Name not on record" misstated the
     record — the name IS on record in the cited investigation; this work withholds it by
     policy. SOURCED tier at render.)
   - ADD `"attribution": "— A U.S. Central Command spokesperson, to Airwars, published with The Independent, 10 March 2026."`
4. Instance 2 `face_harm`:
   - ADD `"intro_line": "One side has answered. The other has not spoken yet."` — IMAGINED.
   - ADD `"display_line": "An elementary school in Minab was struck on 28 February 2026. A US munition was likely responsible. Outdated intelligence was the likely cause."`
     — SOURCED display compression; the fuller `"harm"` record field STAYS unchanged.
   - Each `toll_per_source` entry ADDS `"label"`: `"NBC"` (NBC News entry) / `"AMNESTY"`
     (Amnesty entry). Figures, sources, urls unchanged.
   - ADD `"toll_outro": "Two counts. Kept separate here, as they were kept separate by the two organizations that reported them."` — IMAGINED.
   - REPLACE `"open_answer_slot"` with (source_urls array unchanged from current file):

```json
"open_answer_slot": {
  "label_note": "The rendered label is display.answer_label_template with monitoring.last_checked.",
  "body": "120 members of Congress asked the Pentagon what role AI may have played in selecting targets — 'something that could be addressed in the results of the Pentagon investigation.' The investigation is being finalised. The Pentagon has not said yes. It has not said no.",
  "safeguard": "No denial exists for this strike. None is shown here, because none was made.",
  "source_urls": [ ...unchanged... ]
}
```

   (Dramaturg ruling 2b, conductor-synthesised: the body keeps the sourced congressional
   sentence and the dated status; "has not said yes / has not said no" stays as the body's
   close — it is the line the session-15 critique singled out; the safeguard becomes its own
   field and renders LAST. The retired sentence "This console fabricates no denial. The open
   state is the truth it shows." survives in spirit in `monitoring.serial_note` +
   the safeguard.)

### index.html script changes

- `buildFaceTwoNodes` draws every displayed string from the island: `intro_line`,
  `civilian` / `display_line`, quotes (already), `attribution`, toll `label` + `figure`,
  `toll_outro`, `hinge.text` (Case 1 now renders the island hinge text — Dramaturg ruling
  2a: the island text is canon; delete the divergent render literal), `open_answer_slot.body`
  + `.safeguard`. Delete the corresponding hardcoded literals.
- `buildFaceOneNodes` already renders from the island — leave its construction as-is.
- The caption `<p>` element stays in the HTML but is populated at boot from
  `display.caption`. Control labels/microcopy from `display.control`. The serial line
  renders `display.serial_line_template`, the answer-slot label
  `display.answer_label_template`, both with `{date}` = `monitoring.last_checked`
  formatted `D Month YYYY` via fixed month-name array. Remove the hardcoded date literals
  from script and chrome HTML (the `<noscript>` keeps hand-mirrored literals, see below).

## Obligation B — boundary tier-tagging (Dramaturg ruling 1, binding)

Every rendered content line keeps a tier (sourced/imagined) in the node-builder data, but a
visible tag renders ONLY when: (i) the line's tier differs from the immediately preceding
rendered line's tier, OR (ii) the line opens a visually separated container (hinge box,
toll box, answer slot) — whichever triggers first, even if the container's opening tier
matches the tag directly before it. Tag styling itself unchanged; the control microcopy
keeps its IMAGINED tag.

Expected counts (verify you hit them exactly):
- Face One (either case): **2** — IMAGINED (role heading), SOURCED (first quote); the
  attribution/stat/srcline continue the SOURCED run untagged.
- Face Two Case 1: **3** — IMAGINED (heading; intro_line same run), SOURCED (civilian line;
  quotes + attribution same run), IMAGINED (hinge box).
- Face Two Case 2: **6** — IMAGINED (heading), SOURCED (display_line), SOURCED (toll box —
  container rule), IMAGINED (toll_outro), IMAGINED (hinge box), SOURCED (answer slot).

## Obligation C — source links on Face Two + dated lines

- Case 1: one `[source]` link (same `.srclink` styling, `target="_blank"
  rel="noopener noreferrer"` as Face One) at the END of the attribution line, href =
  `face_harm.source_url`.
- Case 2: one `[source]` link at the end of EACH toll line (href = that entry's `url`);
  in the answer slot, the two `source_urls` render as two adjacent `[source]` links at the
  end of the body paragraph, BEFORE the safeguard. The safeguard renders last and carries
  no link; nothing renders after it in the face. (Conductor deviation from the Dramaturg's
  3.1, journalled: per-toll-line marks instead of two adjacent marks at block close —
  unambiguous figure→source attribution.)
- `<noscript>`: hand-mirror the new canon texts exactly (it is static HTML; add an HTML
  comment above it noting it is hand-mirrored from the island and checked at each gate):
  Case 1 victim sentence = new `civilian` text; Case 2 school sentence = `display_line`;
  the answer block = the dated label, the `body`, then the bold `safeguard`; add plain
  `[source]` anchors mirroring the face links. Existing quotes in the noscript untouched.

## Verification (Builder runs before returning)

1. `data.json` parses; island extracted from `index.html` is byte-identical to it.
2. Grep `index.html`: no "Name not on record"; no hardcoded "16 July 2026" inside the
   script block (noscript literals OK); "Math.random" and "Date.now" absent from the
   script; no program/operation codenames outside citation hrefs.
3. Headless check if available (e.g. `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --dump-dom file://…/index.html`):
   boot shows Face One Case 1; self-test strip prints `SELF-TEST: PASS`; the HARM role
   marker text absent from the `#app` subtree at rest; tag counts match Obligation B; the
   serial line shows "Last checked 16 July 2026". If no headless browser works, say so —
   the conductor verifies independently.
4. Every quote `"text"` field byte-identical old vs new (diff the parsed quote arrays).
