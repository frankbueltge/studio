#!/usr/bin/env python3
"""
build-page-62.py — generates candidate/index.html for *STOP USING IMMEDIATELY*
per STAGING-RULING-62.md.

What this script does, in order:
  1. Loads the committed corpus (observation/recalls-2026-07-01_2026-08-02.json).
  2. Selects the record with RecallNumber 26591 and takes Remedies[0].Name
     VERBATIM — no cleanup, no repair of the stray "?" glyph.
  3. Escapes ONLY &, <, > in that string for HTML, inserts it into the page,
     then re-reads the generated file, extracts the rendered string, undoes
     the same three escapes, and checks its sha256 against the value fixed
     in the staging ruling. Prints PASS/FAIL and the hash.
  4. Also takes RecallNumber, RecallDate and URL from the same record, to
     print beside the quotation.
  5. Reads the nine clauses and the [S]/[S]/[I]/"nothing is sent to us"
     notes out of THE-SCORE.md mechanically (regex extraction against known
     lead-in text), so their wording cannot drift from the source file.

Run: python3 build-page-62.py
Requires only the Python standard library.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent
CORPUS_PATH = HERE / "recalls-2026-07-01_2026-08-02.json"
SCORE_PATH = PROJECT_DIR / "THE-SCORE.md"
OUT_PATH = PROJECT_DIR / "candidate" / "index.html"

RECALL_NUMBER = "26591"
EXPECTED_SHA256 = "b987f91130185652d3f3ebce96d736af6c5220f720578e54ac83ae9c6fdd476b"
EXPECTED_LEN = 326

MONTHS = ["", "January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def escape_html(s: str) -> str:
    """Escape ONLY &, <, > — in that order, so & is not double-escaped."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def unescape_html(s: str) -> str:
    """Exact inverse of escape_html, applied in reverse order."""
    return s.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")


def human_date(iso_date: str) -> str:
    """'2026-07-02T00:00:00' -> '2 July 2026' (from the record's own field)."""
    y, m, d = iso_date[:10].split("-")
    return f"{int(d)} {MONTHS[int(m)]} {y}"


def load_record():
    with open(CORPUS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    for rec in data:
        if str(rec.get("RecallNumber")) == RECALL_NUMBER:
            return rec, len(data)
    raise SystemExit(f"RecallNumber {RECALL_NUMBER} not found in corpus")


def extract_between(text, start_marker, end_marker):
    i = text.index(start_marker) + len(start_marker)
    j = text.index(end_marker, i)
    return text[i:j]


def extract_paragraph(text, lead_in, next_lead_in):
    """Grab the paragraph that starts with lead_in, up to (not including)
    the next paragraph, identified by next_lead_in appearing at a line
    start after a blank line. Returns the raw paragraph text, collapsed
    to single spaces, still carrying its own **bold**/`code`/<url> markup."""
    i = text.index(lead_in)
    j = text.index(next_lead_in, i)
    para = text[i:j]
    # trim trailing blank-line(s) before the next paragraph's lead-in,
    # and collapse internal markdown line-wraps to single spaces
    para = re.sub(r"\s+", " ", para).strip()
    return para


def md_inline_to_html(s: str) -> str:
    """Minimal, targeted markdown->HTML for the score/notes text only:
    backtick `[S]`/`[I]` marks -> <span class="mark">, *emphasis* -> <em>,
    bare <https://...> autolinks -> <a href>, **bold** -> <strong>."""
    # backtick marks, e.g. `[S]` or `[I]`
    s = re.sub(r"`(\[[SI]\])`", r'<span class="mark">\1</span>', s)
    # bold
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    # emphasis (single asterisk, not already consumed by bold above)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    # autolinked bare URLs in angle brackets: <https://...>
    s = re.sub(r"<(https?://[^\s>]+)>", r'<a href="\1">\1</a>', s)
    # backtick code spans left over, e.g. `THE-RULE.md` — render as code,
    # but no such spans should survive into the page (file names are cut);
    # left here only as a safety net so a stray backtick never leaks raw.
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def extract_clauses(score_text: str):
    body = extract_between(score_text, "<!-- THE SCORE BEGINS -->", "<!-- THE SCORE ENDS -->")
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    clauses = []
    for p in paras:
        m = re.match(r"^\d+\.\s+(.*)$", p, re.DOTALL)
        if not m:
            raise SystemExit(f"unexpected clause paragraph: {p!r}")
        clauses.append(md_inline_to_html(m.group(1).strip()))
    if len(clauses) != 9:
        raise SystemExit(f"expected 9 clauses, found {len(clauses)}")
    return clauses


def extract_notes(score_text: str):
    lead_s1 = "**`[S]` SOURCED — not ours.**"
    lead_s2 = "**`[S]` SOURCED — one thing to know before you perform it.**"
    lead_i = "**`[I]` IMAGINED — ours.**"
    lead_refusal = "**The refusal in clause 5"
    lead_nothing = "**Nothing is sent to us.**"
    lead_performances = "**Performances to date: none.**"

    note_s1 = extract_paragraph(score_text, lead_s1, lead_s2)
    note_s2 = extract_paragraph(score_text, lead_s2, lead_i)
    note_i = extract_paragraph(score_text, lead_i, lead_refusal)
    note_nothing = extract_paragraph(score_text, lead_nothing, lead_performances)

    return [md_inline_to_html(n) for n in (note_s1, note_s2, note_i, note_nothing)]


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>STOP USING IMMEDIATELY — Ensemble</title>
<style>
  html, body {{
    margin: 0;
    padding: 0;
    background: #f2f0ec;
  }}

  /* ================= scoped under .work ================= */
  .work {{
    --ink: #141210;
    --ink-dim: #55504a;
    --paper: #f2f0ec;
    --rule: #cbc6bc;

    max-width: 46em;
    margin: 0 auto;
    padding: 0 1.1rem 4rem;
    background: var(--paper);
    color: var(--ink);
    font-family: Charter, "Bitstream Charter", "Iowan Old Style", "Sitka Text", Georgia, "Times New Roman", serif;
    line-height: 1.5;
  }}
  .work *, .work *::before, .work *::after {{ box-sizing: border-box; }}

  .work a {{ color: var(--ink); text-decoration-thickness: 1px; text-underline-offset: 0.15em; }}

  /* -------- movement I : the sentence -------- */
  .work .m1 {{
    padding-top: 1.6rem;
  }}
  .work h1 {{
    margin: 0;
    font-size: clamp(1.2rem, 4.6vw, 2rem);
    font-weight: 600;
    letter-spacing: 0.02em;
    line-height: 1.15;
  }}
  .work .byline {{
    margin: 0.45rem 0 0;
    font-size: clamp(0.72rem, 2vw, 0.85rem);
    color: var(--ink-dim);
    font-style: italic;
  }}
  .work .remedy {{
    margin: 1rem 0 0;
    padding: 0 0 0 0.85rem;
    border-left: 3px solid var(--ink);
  }}
  .work .remedy-text {{
    margin: 0;
    font-size: clamp(1.05rem, 4.6vw, 1.7rem);
    line-height: 1.28;
    font-style: italic;
  }}
  .work .remedy-cite {{
    margin: 0.55rem 0 0;
    font-size: clamp(0.68rem, 1.8vw, 0.8rem);
    font-style: normal;
    color: var(--ink-dim);
    line-height: 1.4;
    word-break: break-word;
  }}
  .work .mark {{
    font-style: normal;
    font-weight: 600;
    letter-spacing: 0.04em;
  }}
  .work .selection {{
    margin: 0.75rem 0 0;
    font-size: clamp(0.78rem, 2.1vw, 0.92rem);
    color: var(--ink-dim);
    line-height: 1.4;
  }}

  .work hr {{
    border: none;
    border-top: 1px solid var(--rule);
    margin: 2.2rem 0;
  }}

  /* -------- movement II : the silence -------- */
  .work .m2 {{
    font-size: 0.92rem;
    max-width: 34em;
  }}
  .work .counts {{
    font-size: 1rem;
    letter-spacing: 0.01em;
    margin: 0 0 0.9rem;
  }}
  .work .m2 p {{
    margin: 0 0 0.7rem;
  }}
  .work .state {{
    margin: 1.3rem 0 0;
  }}

  /* -------- movement III : the score -------- */
  .work .m3 ol {{
    font-size: 1.12rem;
    line-height: 1.6;
    padding-left: 1.4em;
    margin: 0;
  }}
  .work .m3 li {{
    margin: 0 0 1.05em;
  }}
  .work .m3 li:last-child {{ margin-bottom: 0; }}

  /* -------- movement IV : the notes -------- */
  .work .m4 {{
    font-size: 0.76rem;
    line-height: 1.55;
    color: var(--ink-dim);
    max-width: 36em;
  }}
  .work .m4 p {{
    margin: 0 0 0.85rem;
  }}
  .work .m4 p:last-child {{ margin-bottom: 0; }}

  .work .append {{
    margin: 1.6rem 0 0;
    font-size: 0.76rem;
    color: var(--ink-dim);
    max-width: 36em;
  }}
  .work .append h2 {{
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 600;
    margin: 0 0 0.5rem;
  }}
  .work .append-entries {{
    margin: 0;
    padding: 0;
    list-style: none;
  }}
  .work .append-empty {{
    margin: 0;
    font-style: italic;
  }}

  .work .repo-line {{
    margin: 1rem 0 0;
    font-size: 0.76rem;
    color: var(--ink-dim);
    max-width: 36em;
  }}

  .work .exit {{
    margin: 3rem 0 0;
    text-align: center;
    font-size: 1.05rem;
    letter-spacing: 0.02em;
  }}
</style>
</head>
<body>
<div class="work">

  <div class="m1">
    <h1>STOP USING IMMEDIATELY</h1>
    <p class="byline">a score &middot; ENSEMBLE</p>

    <blockquote class="remedy">
      <p class="remedy-text">{REMEDY_HTML}</p>
      <p class="remedy-cite"><span class="mark">[S]</span> CPSC Recall {RECALL_NUMBER} &middot; {RECALL_DATE_HUMAN} &middot; {URL_TEXT}</p>
    </blockquote>

    <p class="selection">This house did not choose that notice &mdash; a committed rule did, with its discretion null, and it skipped nothing.</p>
  </div>

  <hr>

  <div class="m2">
    <p class="counts">performed 0 &middot; asked 1 &middot; answered 0</p>
    <p>This house cannot perform it: it has no home, no hands, and no address a refund could reach.</p>
    <p>It refused to recruit a performer in public.</p>
    <p class="state">As of 3 August 2026, no performance of this score is known to this house. This house asks for no reports and keeps no register; it will not learn of one unless somebody tells it.</p>
  </div>

  <hr>

  <div class="m3">
    <ol>
{CLAUSES_HTML}
    </ol>
  </div>

  <hr>

  <div class="m4">
    <p>{NOTE_S1}</p>
    <p>{NOTE_S2}</p>
    <p>{NOTE_I}</p>
    <p>{NOTE_NOTHING}</p>
    <p>50 of 55 recall notices published in the window this record was drawn from open with the sentence that gives this score its name.</p>
  </div>

  <div class="append">
    <h2>Appended after publication</h2>
    <ol class="append-entries">
      <!-- APPEND-BELOW: a later session adds <li> entries here, in date order, editing nothing above this comment. -->
    </ol>
    <p class="append-empty">Nothing appended yet.</p>
  </div>

  <p class="repo-line">The working record, how the notice was chosen, what was refused, and who was asked, is public in this studio's repository.</p>

  <p class="exit"><a href="https://www.cpsc.gov/Recalls">cpsc.gov/Recalls</a></p>

</div>
</body>
</html>
"""


def build():
    rec, corpus_n = load_record()
    remedy_raw = rec["Remedies"][0]["Name"]

    if len(remedy_raw) != EXPECTED_LEN:
        raise SystemExit(f"remedy length {len(remedy_raw)} != expected {EXPECTED_LEN}")
    got_sha = hashlib.sha256(remedy_raw.encode("utf-8")).hexdigest()
    if got_sha != EXPECTED_SHA256:
        raise SystemExit(f"remedy sha256 {got_sha} != expected {EXPECTED_SHA256}")

    remedy_html = escape_html(remedy_raw)
    recall_number = str(rec["RecallNumber"])
    recall_date_human = human_date(rec["RecallDate"])
    url = rec["URL"]

    score_text = SCORE_PATH.read_text(encoding="utf-8")
    clauses = extract_clauses(score_text)
    clauses_html = "\n".join(f"      <li>{c}</li>" for c in clauses)
    note_s1, note_s2, note_i, note_nothing = extract_notes(score_text)

    html = TEMPLATE.format(
        REMEDY_HTML=remedy_html,
        RECALL_NUMBER=recall_number,
        RECALL_DATE_HUMAN=recall_date_human,
        URL_TEXT=url,
        CLAUSES_HTML=clauses_html,
        NOTE_S1=note_s1,
        NOTE_S2=note_s2,
        NOTE_I=note_i,
        NOTE_NOTHING=note_nothing,
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(html, encoding="utf-8")

    # ---- verification: mechanical, against the file just written ----
    rendered = OUT_PATH.read_text(encoding="utf-8")
    m = re.search(r'<p class="remedy-text">(.*?)</p>', rendered, re.DOTALL)
    if not m:
        print("FAIL — could not locate remedy-text element in rendered file")
        sys.exit(1)
    rendered_escaped = m.group(1)
    rendered_raw = unescape_html(rendered_escaped)
    rendered_sha = hashlib.sha256(rendered_raw.encode("utf-8")).hexdigest()

    ok = (rendered_raw == remedy_raw) and (rendered_sha == EXPECTED_SHA256) and (len(rendered_raw) == EXPECTED_LEN)
    print("PASS" if ok else "FAIL", "—", rendered_sha)
    print(f"length: {len(rendered_raw)} (expected {EXPECTED_LEN})")
    print(f"record: RecallNumber {recall_number}, RecallDate {rec['RecallDate']}, corpus N={corpus_n}")
    print(f"written: {OUT_PATH} ({OUT_PATH.stat().st_size} bytes)")
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    build()
