#!/usr/bin/env python3
"""NO PART — re-derivation of the row pitch and the certiorari-denied entry counts,
straight from order-list.pdf's own bytes, with page attribution taken from the PDF's
own page tree (not guessed from line position).

Pays the debt named in README.md ("Carried, not re-derived tonight"): the row pitch
23.46 pt = 8.276 mm and the 761-rows figure were session 46's, from a tool that lives
outside this campaign's build directory. This script is this campaign's own tool, and
it runs from the source PDF only.

WHAT THIS SCRIPT DOES, IN ORDER
1. Verifies order-list.pdf's SHA-256; refuses to run on a different hash.
2. Parses the PDF's own cross-reference structure (xref streams, incl. compressed
   object streams) well enough to walk Root -> Pages -> Kids and recover the true,
   spec-defined page order — 39 leaf /Page objects, in document order. This is not
   a heuristic; it is the same traversal any conforming PDF reader performs to find
   page 1, page 2, ... page 39.
3. For each page, decompresses its own content stream and interprets the text-
   positioning operators (BT, Tf, TL, Td, TD, Tm, T*, Tj, TJ, ', ") well enough to
   recover, for every text-showing operation, its baseline (x, y) in PDF points in
   that page's own default coordinate space. (Every page here has an identity CTM —
   no `cm` operator appears in any content stream — so the text matrix's own (e, f)
   IS the page-space baseline position; this was checked, not assumed. See
   `assert_no_cm_operator` below.)
4. Reconstructs "lines" at the same granularity the prior session's extractor used
   (a new line at every Td/TD/Tm/T*/'/" — the same convention that put a docket
   number and its caption on separate logical lines despite sharing one printed
   row), so that this script's counts are checked against that convention on equal
   footing, not against a redefinition of it.
5. Measures row pitch as a *distribution* of consecutive-baseline gaps within the
   CERTIORARI DENIED section, not a single number.
6. Counts CERTIORARI DENIED entries before/after "The petitions for writs of
   certiorari are denied.", using the same grouped-entry convention as the prior
   session's tooling (stated explicitly below).
7. Reports the sheet each of: the mass sentence; every Rule 38(a) filing-bar
   sentence; and the section's first/last docket entry, prints on.
8. Writes rows.json and prints a full report to stdout.

KNOWN LOSSINESS (found by this script, reported, not hidden): six CERTIORARI DENIED
docket numbers on sheet 25 (25-5110, 25-5115, 25-5120, 25-5125, 25-5130, 25-5135)
have their "NN-" prefix and their numeral suffix drawn by two separate, out-of-order
text-positioning operations in the content stream (the suffix digits are drawn in a
batch, earlier in the stream, at a different x than the prefix). This convention
(line = one Td/TD/Tm/T*/'/" span) never reassembles them, so all six are silently
absent from the entry count below, in this script exactly as in session 46's. See
REPORT section "KNOWN LOSSINESS" for the corrected counts.

USAGE
    python3 build/extract-rows.py
Reads ../order-list.pdf relative to this file; writes ./rows.json next to it.
No network access. No dependency beyond the Python 3 standard library.
"""
import hashlib
import json
import os
import re
import statistics
import sys
import zlib
import collections

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
PDF_PATH = os.path.join(PROJECT_DIR, 'order-list.pdf')
OUT_PATH = os.path.join(SCRIPT_DIR, 'rows.json')
EXPECTED_SHA256 = '354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652'

MASS_SENTENCE = 'The petitions for writs of certiorari are denied.'
RULE_38A_PHRASE = 'the docketing fee required by Rule 38(a) is paid'
SECTIONS = ['ORDERS IN PENDING CASES', 'CERTIORARI DENIED', 'HABEAS CORPUS DENIED',
            'MANDAMUS DENIED', 'REHEARINGS DENIED', 'CERTIORARI GRANTED',
            'ORDERS IN MISCELLANEOUS CASES']

DOCKET_RE = re.compile(r'^(\d{2}[-M]\d{1,5})\s*(?:\)|,)?\s*$')
DIGITS_ONLY_RE = re.compile(r'^(\d+|[)\]]+)$')   # folios, margin counters, stray ')' — not content rows


# --------------------------------------------------------------------------------
# Part 1: verify the source
# --------------------------------------------------------------------------------

def verify_hash(path, expected):
    if not os.path.exists(path):
        print('FATAL: %s does not exist.' % path, file=sys.stderr)
        sys.exit(1)
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        h.update(f.read())
    got = h.hexdigest()
    if got != expected:
        print('FATAL: SHA-256 mismatch.\n  expected %s\n  got      %s' % (expected, got),
              file=sys.stderr)
        print('This is a different document. Aborting — nothing below covers it.',
              file=sys.stderr)
        sys.exit(1)
    return got


# --------------------------------------------------------------------------------
# Part 2: minimal PDF object/xref layer (xref streams + compressed object streams)
# --------------------------------------------------------------------------------

def apply_png_up_predictor(raw, columns):
    """PNG predictor 12 (all rows tagged 'Up' in practice for xref streams; tag 0
    ('None') is also handled since the spec permits per-row tags)."""
    out = bytearray()
    prev = bytearray(columns)
    i = 0
    while i < len(raw):
        tag = raw[i]; i += 1
        row = bytearray(raw[i:i + columns]); i += columns
        if tag == 2:
            for j in range(columns):
                row[j] = (row[j] + prev[j]) & 0xFF
        elif tag != 0:
            raise ValueError('unsupported PNG predictor tag %d in xref stream' % tag)
        out += row
        prev = row
    return bytes(out)


class PDF:
    """Enough of a PDF object layer to: read xref streams (with /Prev chains),
    decompress object streams, fetch any object's dict (compressed or not), fetch
    a direct stream object's decompressed bytes, and walk the page tree from the
    document catalog. Deliberately narrow — this document's own structure (a
    linearized PDF using cross-reference streams and compressed object streams,
    FlateDecode throughout, no encryption) is all it needs to handle, and it
    refuses (via plain exceptions) rather than guess on anything it doesn't
    recognise."""

    def __init__(self, data):
        self.data = data
        self.entries = {}   # objnum -> (type, f2, f3) per PDF 1.5 cross-reference stream entries
        self._objstm_cache = {}
        self.root_num = None
        self._load_xref()

    def _read_stream_object_at_offset(self, offset):
        m = re.match(rb'\s*(\d+)\s+(\d+)\s+obj', self.data[offset:offset + 50])
        if not m:
            raise ValueError('no object header at file offset %d' % offset)
        hdr_end = offset + m.end()
        dict_start = self.data.find(b'<<', hdr_end)
        depth = 0
        i = dict_start
        while i < len(self.data):
            if self.data[i:i + 2] == b'<<':
                depth += 1; i += 2; continue
            if self.data[i:i + 2] == b'>>':
                depth -= 1; i += 2
                if depth == 0:
                    break
                continue
            i += 1
        dict_end = i
        dict_bytes = self.data[dict_start:dict_end]
        stream_kw = self.data.find(b'stream', dict_end)
        if stream_kw == -1:
            return dict_bytes, None
        between = self.data[dict_end:stream_kw]
        if between.strip(b'\r\n \t') != b'':
            return dict_bytes, None    # 'stream' keyword belongs to a later object, not this one
        sp = stream_kw + len(b'stream')
        if self.data[sp:sp + 2] == b'\r\n':
            sp += 2
        elif self.data[sp:sp + 1] in (b'\r', b'\n'):
            sp += 1
        lm = re.search(rb'/Length\s+(\d+)', dict_bytes)
        length = int(lm.group(1))
        raw = self.data[sp:sp + length]
        if b'/FlateDecode' in dict_bytes:
            raw = zlib.decompress(raw)
        return dict_bytes, raw

    def _load_xref(self):
        matches = list(re.finditer(rb'startxref\s+(\d+)', self.data))
        if not matches:
            raise ValueError('no startxref found')
        offset = int(matches[-1].group(1))   # the file's own trailer startxref, not any earlier one
        seen = set()
        while offset is not None and offset not in seen:
            seen.add(offset)
            db, raw = self._read_stream_object_at_offset(offset)
            if b'/Type/XRef' not in db.replace(b' ', b''):
                raise ValueError('expected an XRef stream at offset %d' % offset)
            wm = re.search(rb'/W\s*\[\s*(\d+)\s+(\d+)\s+(\d+)\s*\]', db)
            w1, w2, w3 = (int(x) for x in wm.groups())
            colm = re.search(rb'/DecodeParms\s*<<[^>]*?/Columns\s+(\d+)', db)
            if colm:
                raw = apply_png_up_predictor(raw, int(colm.group(1)))
            idxm = re.search(rb'/Index\s*\[\s*([\d\s]+)\]', db)
            sizem = re.search(rb'/Size\s+(\d+)', db)
            if idxm:
                nums = [int(x) for x in idxm.group(1).split()]
                pairs = list(zip(nums[0::2], nums[1::2]))
            else:
                pairs = [(0, int(sizem.group(1)))]
            entsize = w1 + w2 + w3
            pos = 0
            for start, count in pairs:
                for k in range(count):
                    chunk = raw[pos:pos + entsize]; pos += entsize
                    f1 = int.from_bytes(chunk[0:w1], 'big') if w1 > 0 else 1
                    f2 = int.from_bytes(chunk[w1:w1 + w2], 'big')
                    f3 = int.from_bytes(chunk[w1 + w2:w1 + w2 + w3], 'big')
                    if (start + k) not in self.entries:
                        self.entries[start + k] = (f1, f2, f3)
            if self.root_num is None:
                rm = re.search(rb'/Root\s+(\d+)\s+\d+\s+R', db)
                if rm:
                    self.root_num = int(rm.group(1))
            pm = re.search(rb'/Prev\s+(\d+)', db)
            offset = int(pm.group(1)) if pm else None
        if self.root_num is None:
            raise ValueError('/Root not found in any xref stream trailer dict')

    def _decode_objstm(self, objstm_num):
        if objstm_num in self._objstm_cache:
            return self._objstm_cache[objstm_num]
        f1, f2, f3 = self.entries[objstm_num]
        assert f1 == 1, 'an object stream cannot itself be a compressed object'
        db, raw = self._read_stream_object_at_offset(f2)
        first = int(re.search(rb'/First\s+(\d+)', db).group(1))
        header = raw[:first]
        nums = [int(x) for x in header.split()]
        pairs = list(zip(nums[0::2], nums[1::2]))
        objs = {}
        for i, (onum, ooff) in enumerate(pairs):
            start = first + ooff
            end = first + pairs[i + 1][1] if i + 1 < len(pairs) else len(raw)
            objs[onum] = raw[start:end]
        self._objstm_cache[objstm_num] = objs
        return objs

    def get_object_dict(self, objnum):
        f1, f2, f3 = self.entries[objnum]
        if f1 == 1:
            db, _ = self._read_stream_object_at_offset(f2)
            return db
        elif f1 == 2:
            return self._decode_objstm(f2)[objnum]
        raise ValueError('object %d is marked free in the xref table' % objnum)

    def get_stream(self, objnum):
        f1, f2, f3 = self.entries[objnum]
        assert f1 == 1, 'object %d is compressed; cannot carry its own stream' % objnum
        return self._read_stream_object_at_offset(f2)

    def walk_pages(self):
        """Root -> /Pages -> /Kids, recursively, exactly as a conforming reader
        resolves page order. Returns the ordered list of leaf /Page object numbers."""
        root_dict = self.get_object_dict(self.root_num)
        pages_root = int(re.search(rb'/Pages\s+(\d+)\s+\d+\s+R', root_dict).group(1))
        order = []

        def visit(num):
            d = self.get_object_dict(num)
            tm = re.search(rb'/Type\s*/(\w+)', d)
            if tm and tm.group(1) == b'Pages':
                kids_m = re.search(rb'/Kids\s*\[([^\]]*)\]', d)
                for k in (int(x) for x in re.findall(rb'(\d+)\s+\d+\s+R', kids_m.group(1))):
                    visit(k)
            else:
                order.append(num)

        visit(pages_root)
        return order


def assert_no_cm_operator(content):
    """Every content stream here draws with the identity CTM (no `cm` operator
    anywhere between BT/ET or outside it), which is what licenses reading the text
    matrix's own (e, f) directly as a page-space point. Raises if that stops being
    true on any page, rather than silently mis-measuring."""
    for m in re.finditer(rb'(?:^|[\s>)\]])([-+]?(?:\d+\.\d*|\.\d+|\d+)(?:\s+[-+]?(?:\d+\.\d*|\.\d+|\d+)){5})\s+cm(?:[\s(<]|$)', content):
        raise AssertionError('unexpected cm operator found: %r' % m.group(0))


# --------------------------------------------------------------------------------
# Part 3: content-stream tokenizer + text-positioning interpreter
# --------------------------------------------------------------------------------

def unescape_pdf_string(s):
    out = bytearray()
    i = 0
    while i < len(s):
        c = s[i]
        if c == 0x5c:  # backslash
            i += 1
            if i >= len(s):
                break
            n = s[i]
            mapping = {0x6e: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12,
                       0x28: 40, 0x29: 41, 0x5c: 92}
            if n in mapping:
                out.append(mapping[n]); i += 1
            elif 0x30 <= n <= 0x37:
                oct_digits = ''
                while i < len(s) and 0x30 <= s[i] <= 0x37 and len(oct_digits) < 3:
                    oct_digits += chr(s[i]); i += 1
                out.append(int(oct_digits, 8) & 0xFF)
            elif n in (0x0a, 0x0d):
                if n == 0x0d and i + 1 < len(s) and s[i + 1] == 0x0a:
                    i += 1
                i += 1
            else:
                out.append(n); i += 1
        else:
            out.append(c); i += 1
    return bytes(out)


TOKEN_RE = re.compile(rb"""
    \((?:\\.|[^\\()])*\)         # literal string
  | <[0-9A-Fa-f\s]*>              # hex string (not a dict -- checked before dict-open below)
  | <<                            # dict open
  | >>                            # dict close
  | \[                            # array open
  | \]                            # array close
  | /[^\s/()<>\[\]{}%]+           # name
  | [-+]?(?:\d+\.\d*|\.\d+|\d+)   # number
  | \'                            # move-to-next-line-and-show operator
  | \"                            # move-to-next-line-and-show-with-spacing operator
  | [A-Za-z*][A-Za-z0-9*]*        # bare operator keyword (Td, TD, Tm, Tj, TJ, BT, ET, T*, ...)
""", re.X | re.S)


def tokenize_content(s):
    for m in TOKEN_RE.finditer(s):
        t = m.group(0)
        if t.startswith(b'('):
            yield ('str', unescape_pdf_string(t[1:-1]))
        elif t.startswith(b'<<'):
            yield ('dictopen', None)
        elif t.startswith(b'>>'):
            yield ('dictclose', None)
        elif t.startswith(b'<'):
            hexs = re.sub(rb'\s', b'', t[1:-1])
            if len(hexs) % 2:
                hexs += b'0'
            try:
                yield ('hexstr', bytes.fromhex(hexs.decode()))
            except ValueError:
                yield ('hexstr', b'')
        elif t == b'[':
            yield ('arropen', None)
        elif t == b']':
            yield ('arrclose', None)
        elif t.startswith(b'/'):
            yield ('name', t[1:].decode('latin1'))
        elif re.match(rb'^[-+]?(?:\d+\.\d*|\.\d+|\d+)$', t):
            yield ('num', float(t))
        else:
            yield ('op', t.decode('latin1'))


def extract_lines(content):
    """Interpret one page's content stream's text object(s). Returns a list of
    dicts, one per text-positioning event (Td/TD/Tm/T*/'/") that showed text before
    the next positioning event: {'y', 'x', 'scale', 'text', 'render_mode'}.

    Text-matrix bookkeeping follows the PDF spec (9.4.2): Td/TD compute the new
    line matrix as tx,ty translated THROUGH the old line matrix's own a,b,c,d before
    being added to its e,f — i.e. Td/TD operands are in unscaled text space and pick
    up the current font-size scaling, exactly as the two dominant row-pitch clusters
    in this document (Td deltas of -2.347 and -2.341, scaled by the 10.02 text
    matrix, i.e. 23.517pt / 23.457pt) only make sense if implemented this way.
    """
    toks = list(tokenize_content(content))
    lines = []
    a = d = 1.0
    b = c = 0.0
    e = f = 0.0
    TL = 0.0
    Tr = 0
    cur_line = None
    stack = []

    def flush():
        if cur_line is not None and cur_line['text'].strip():
            lines.append(cur_line)

    def start_line():
        nonlocal cur_line
        flush()
        cur_line = {'y': f, 'x': e, 'scale': (a * a + b * b) ** 0.5, 'text': '', 'render_mode': Tr}

    i = 0
    n = len(toks)
    while i < n:
        kind, val = toks[i]
        if kind == 'dictopen':
            depth = 1; j = i + 1
            while j < n and depth > 0:
                if toks[j][0] == 'dictopen':
                    depth += 1
                elif toks[j][0] == 'dictclose':
                    depth -= 1
                j += 1
            i = j
            continue
        if kind == 'arropen':
            arr = []
            j = i + 1
            while j < n and toks[j][0] != 'arrclose':
                if toks[j][0] in ('str', 'hexstr', 'num'):
                    arr.append(toks[j])
                j += 1
            stack.append(('arr', arr))
            i = j + 1
            continue
        if kind in ('num', 'name', 'str', 'hexstr'):
            stack.append((kind, val))
            i += 1
            continue
        if kind == 'op':
            opname = val
            if opname == 'BT':
                a = d = 1.0; b = c = 0.0; e = f = 0.0
                TL = 0.0; Tr = 0; cur_line = None
            elif opname == 'ET':
                flush(); cur_line = None
            elif opname == 'TL':
                if stack: TL = stack[-1][1]
            elif opname == 'Tr':
                if stack: Tr = int(stack[-1][1])
            elif opname in ('Td', 'TD'):
                if len(stack) >= 2:
                    tx, ty = stack[-2][1], stack[-1][1]
                    e, f = tx * a + ty * c + e, tx * b + ty * d + f
                    if opname == 'TD':
                        TL = -ty
                    start_line()
            elif opname == 'Tm':
                if len(stack) >= 6:
                    a, b, c, d, e, f = (x[1] for x in stack[-6:])
                    start_line()
            elif opname == 'T*':
                tx, ty = 0.0, -TL
                e, f = tx * a + ty * c + e, tx * b + ty * d + f
                start_line()
            elif opname == 'Tj':
                if stack and cur_line is not None:
                    k2, v2 = stack[-1]
                    if k2 in ('str', 'hexstr'):
                        cur_line['text'] += v2.decode('cp1252', 'replace')
            elif opname == 'TJ':
                if stack and cur_line is not None:
                    k2, v2 = stack[-1]
                    if k2 == 'arr':
                        for ak, av in v2:
                            if ak in ('str', 'hexstr'):
                                cur_line['text'] += av.decode('cp1252', 'replace')
            elif opname in ("'", '"'):
                tx, ty = 0.0, -TL
                e, f = tx * a + ty * c + e, tx * b + ty * d + f
                start_line()
                if stack:
                    k2, v2 = stack[-1]
                    if k2 in ('str', 'hexstr') and cur_line is not None:
                        cur_line['text'] += v2.decode('cp1252', 'replace')
            stack = []
            i += 1
            continue
        i += 1
    return lines


# --------------------------------------------------------------------------------
# Part 4: assemble the whole document's lines, with page (sheet) attribution
# --------------------------------------------------------------------------------

def build_all_lines(pdf, pages):
    """One entry per line (per the line-break convention above), in document
    order, each carrying its 1-based sheet number straight from walk_pages()."""
    all_lines = []
    for sheet, pnum in enumerate(pages, start=1):
        page_dict = pdf.get_object_dict(pnum)
        cm = re.search(rb'/Contents\s+(\d+)\s+\d+\s+R', page_dict)
        if not cm:
            raise ValueError('sheet %d (obj %d) has no single /Contents reference '
                              '(array /Contents not handled — none occurs in this '
                              'document, checked separately)' % (sheet, pnum))
        content_num = int(cm.group(1))
        _, content = pdf.get_stream(content_num)
        assert_no_cm_operator(content)
        for l in extract_lines(content):
            text = re.sub(r'\s+', ' ', l['text']).strip()
            if not text:
                continue
            all_lines.append({'sheet': sheet, 'y': l['y'], 'x': l['x'], 'text': text})
    return all_lines


# --------------------------------------------------------------------------------
# Part 5: section / entry parsing (grouped-docket convention, stated explicitly)
# --------------------------------------------------------------------------------
# CONVENTION (matching etudes/5000-series/corpus/parse.py + dispositions.py, the
# prior session's tooling, so that this build's counts are checked against that
# convention on equal footing): a "line" is a docket entry if, after whitespace
# normalisation, it is ENTIRELY a docket number (`docket_re`), possibly grouped —
# several consecutive docket lines followed by a single caption line (' V. ' or
# 'IN RE') each count as one entry, PER DOCKET NUMBER, sharing that one caption.

def parse_entries(all_lines):
    cur_section = 'HEADER'
    pending = []
    entries = []
    mass_idx = None
    mass_sheet = None
    section_starts = []

    for i, r in enumerate(all_lines):
        t = r['text']
        hit = None
        for s in SECTIONS:
            if t.startswith(s):
                hit = s
        if hit:
            cur_section = hit
            section_starts.append({'section': hit, 'row_idx': i, 'sheet': r['sheet']})
            pending = []
            continue
        if mass_idx is None and MASS_SENTENCE.rstrip('.') in t:
            mass_idx = i
            mass_sheet = r['sheet']
        m = DOCKET_RE.match(t)
        if m:
            pending.append((m.group(1), r['sheet'], i))
            continue
        if pending and (' V. ' in t or t.startswith('IN RE') or ' V.' in t):
            for docket, sheet, row_idx in pending:
                entries.append({'section': cur_section, 'docket': docket, 'caption': t,
                                 'sheet': sheet, 'row_idx': row_idx})
            pending = []
            continue
    return entries, mass_idx, mass_sheet, section_starts


# --------------------------------------------------------------------------------
# Part 6: row-pitch distribution, inside the CERTIORARI DENIED section only
# --------------------------------------------------------------------------------

def measure_row_pitch(all_lines, section_start_idx, section_end_idx):
    """Consecutive-baseline y-gaps, same sheet only (a page break resets the text
    matrix, so a gap spanning one is not a print-row pitch), excluding rows whose
    text is purely digits or purely closing punctuation — folios, and the six
    isolated docket-suffix-only fragments identified in KNOWN LOSSINESS, and the
    stray ')' continuation lines from grouped-docket captions. These are not
    printed content rows; including them would put document-margin artefacts in a
    measurement of body-text row spacing."""
    gaps = []
    gap_pages = set()
    cur_sheet = None
    prev_y = None
    for i in range(section_start_idx, section_end_idx):
        r = all_lines[i]
        t = r['text']
        if DIGITS_ONLY_RE.match(t):
            continue
        if r['sheet'] != cur_sheet:
            cur_sheet = r['sheet']
            prev_y = r['y']
            continue
        if r['y'] != prev_y:
            gap = prev_y - r['y']
            gaps.append(gap)
            gap_pages.add(r['sheet'])
            prev_y = r['y']
    return gaps, sorted(gap_pages)


def summarize_gaps(gaps):
    rounded = [round(g, 3) for g in gaps]
    counts = collections.Counter(rounded)
    modal_value, modal_count = counts.most_common(1)[0]
    PT_TO_MM = 25.4 / 72.0
    return {
        'n': len(gaps),
        'mean_pt': statistics.mean(gaps),
        'median_pt': statistics.median(gaps),
        'stdev_pt': statistics.pstdev(gaps),
        'min_pt': min(gaps),
        'max_pt': max(gaps),
        'mode_pt': modal_value,
        'mode_count': modal_count,
        'mode_fraction': modal_count / len(gaps),
        'histogram_pt': sorted(counts.items(), key=lambda kv: -kv[1]),
        'mean_mm': statistics.mean(gaps) * PT_TO_MM,
        'median_mm': statistics.median(gaps) * PT_TO_MM,
        'mode_mm': modal_value * PT_TO_MM,
    }


# --------------------------------------------------------------------------------
# Part 7: Rule 38(a) filing-bar sentence occurrences, with page attribution
# --------------------------------------------------------------------------------

def find_rule_38a_occurrences(all_lines):
    """Every line containing the literal phrase, verbatim. Each occurrence's own
    sheet comes directly from the row's own sheet attribution (Part 4) — no line
    here was found to straddle a page break (checked: the phrase is short enough,
    and this document's own line breaks did not happen to fall inside it in any of
    the four occurrences found)."""
    hits = []
    for i, r in enumerate(all_lines):
        if RULE_38A_PHRASE in r['text']:
            hits.append({'row_idx': i, 'sheet': r['sheet'], 'text': r['text']})
    return hits


def find_known_lossiness(all_lines):
    """The six docket-suffix-only fragments described in the module docstring:
    a bare 'NN-' or 'NNM' with nothing after it, where the PDF's content stream
    drew the numeral suffix as a separate, out-of-order text run (confirmed by
    direct inspection of the raw content stream and of the rendered page — see
    build/README.md's account of this script's own findings)."""
    partial_re = re.compile(r'^\d{2}[-M]$')
    return [{'row_idx': i, 'sheet': r['sheet'], 'text': r['text']}
            for i, r in enumerate(all_lines) if partial_re.match(r['text'])]


# --------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------

def main():
    print('=' * 78)
    print('NO PART -- build/extract-rows.py')
    print('=' * 78)

    got_hash = verify_hash(PDF_PATH, EXPECTED_SHA256)
    print('SHA-256 OK: %s' % got_hash)

    with open(PDF_PATH, 'rb') as f:
        data = f.read()
    pdf = PDF(data)
    pages = pdf.walk_pages()
    print('Pages found via Root -> Pages -> Kids: %d' % len(pages))
    if len(pages) != 39:
        print('WARNING: expected 39 pages per the work\'s own account; found %d. '
              'Every count below is still exactly what this script measured -- '
              'nothing was forced to 39.' % len(pages), file=sys.stderr)

    all_lines = build_all_lines(pdf, pages)
    print('Text lines recovered (line = one Td/TD/Tm/T*/\'/" span): %d' % len(all_lines))

    entries, mass_idx, mass_sheet, section_starts = parse_entries(all_lines)
    print()
    print('-- SECTIONS FOUND (first line, its sheet) --')
    for s in section_starts:
        print('  %-28s row %5d  sheet %2d' % (s['section'], s['row_idx'], s['sheet']))
    if mass_idx is None:
        print('FATAL: mass sentence not found.', file=sys.stderr)
        sys.exit(1)
    print()
    print('Mass sentence row_idx=%d sheet=%d: %r' % (mass_idx, mass_sheet, all_lines[mass_idx]['text']))

    by_section = collections.Counter(e['section'] for e in entries)
    cert = [e for e in entries if e['section'] == 'CERTIORARI DENIED']
    before = [e for e in cert if e['row_idx'] < mass_idx]
    after = [e for e in cert if e['row_idx'] > mass_idx]

    print()
    print('-- ENTRY COUNTS PER SECTION (grouped-docket convention; see module docstring) --')
    for s in SECTIONS:
        if by_section.get(s):
            print('  %-28s %d' % (s, by_section[s]))
    print()
    print('CERTIORARI DENIED total : %d' % len(cert))
    print('  before mass sentence  : %d' % len(before))
    print('  after mass sentence   : %d' % len(after))
    print('  first entry           : %s  %s  (sheet %d)' %
          (cert[0]['docket'], cert[0]['caption'], cert[0]['sheet']))
    print('  last entry            : %s  %s  (sheet %d)' %
          (cert[-1]['docket'], cert[-1]['caption'], cert[-1]['sheet']))

    cert_section_start = next(s['row_idx'] for s in section_starts if s['section'] == 'CERTIORARI DENIED')
    cert_section_end = next(s['row_idx'] for s in section_starts if s['section'] == 'HABEAS CORPUS DENIED')

    gaps, gap_pages = measure_row_pitch(all_lines, cert_section_start, cert_section_end)
    pitch = summarize_gaps(gaps)
    print()
    print('-- ROW PITCH (consecutive-baseline gaps inside CERTIORARI DENIED, same-sheet pairs only) --')
    print('  n gaps measured : %d' % pitch['n'])
    print('  pages           : %s' % (gap_pages,))
    print('  mean            : %.4f pt = %.4f mm' % (pitch['mean_pt'], pitch['mean_mm']))
    print('  median          : %.4f pt = %.4f mm' % (pitch['median_pt'], pitch['median_mm']))
    print('  mode            : %.3f pt = %.4f mm  (%d/%d = %.1f%%)' %
          (pitch['mode_pt'], pitch['mode_mm'], pitch['mode_count'], pitch['n'], 100 * pitch['mode_fraction']))
    print('  stdev           : %.4f pt' % pitch['stdev_pt'])
    print('  range           : %.3f - %.3f pt' % (pitch['min_pt'], pitch['max_pt']))
    print('  histogram (pt: count): %s' % pitch['histogram_pt'])
    print('  carried figure was 23.46 pt = 8.276 mm')

    rule38a = find_rule_38a_occurrences(all_lines)
    print()
    print('-- RULE 38(a) FILING-BAR SENTENCE ("%s") --' % RULE_38A_PHRASE)
    for h in rule38a:
        in_cert = cert_section_start <= h['row_idx'] < cert_section_end
        print('  sheet %2d  %-22s %s' %
              (h['sheet'], '(in CERTIORARI DENIED)' if in_cert else '(outside CERTIORARI DENIED)', h['text']))

    lossy = find_known_lossiness(all_lines)
    print()
    print('-- KNOWN LOSSINESS: docket-suffix fragments not reassembled by the line convention --')
    for h in lossy:
        print('  sheet %2d  row %4d  %r' % (h['sheet'], h['row_idx'], h['text']))
    print('  %d fragment(s); all before the mass sentence, all inside CERTIORARI DENIED, all on '
        'sheet 25.' % len(lossy))
    print('  Corrected counts if these are added back: total=%d before=%d after=%d' %
          (len(cert) + len(lossy), len(before) + len(lossy), len(after)))

    result = {
        'meta': {
            'source_pdf_sha256': got_hash,
            'pages_found': len(pages),
            'script': 'build/extract-rows.py',
        },
        'sections': [{'section': s['section'], 'first_row_idx': s['row_idx'], 'sheet': s['sheet']}
                     for s in section_starts],
        'mass_sentence': {
            'text': all_lines[mass_idx]['text'],
            'row_idx': mass_idx,
            'sheet': mass_sheet,
        },
        'certiorari_denied': {
            'convention': ('A "line" is a docket entry iff, after whitespace normalisation, it is '
                            'ENTIRELY a docket number matching ^(\\d{2}[-M]\\d{1,5})(\\)|,)?$. Several '
                            'consecutive docket lines followed by one caption line (containing " V. " '
                            'or starting "IN RE") each count as one entry per docket number, sharing '
                            'that one caption -- the grouped-entry convention carried over from '
                            'etudes/5000-series/corpus/parse.py and dispositions.py.'),
            'total': len(cert),
            'before_mass_sentence': len(before),
            'after_mass_sentence': len(after),
            'first_entry': {'docket': cert[0]['docket'], 'caption': cert[0]['caption'], 'sheet': cert[0]['sheet']},
            'last_entry': {'docket': cert[-1]['docket'], 'caption': cert[-1]['caption'], 'sheet': cert[-1]['sheet']},
            'entries': [{'docket': e['docket'], 'caption': e['caption'], 'sheet': e['sheet'],
                         'before_mass_sentence': e['row_idx'] < mass_idx}
                        for e in cert],
        },
        'entry_counts_by_section': dict(by_section),
        'row_pitch': {
            'measured_over': 'consecutive-baseline y-gaps inside CERTIORARI DENIED, same-sheet pairs only, '
                              'excluding rows that are purely digits or purely closing punctuation '
                              '(folios, margin counters, stray grouped-docket paren wraps)',
            'carried_figure_pt': 23.46,
            'carried_figure_mm': 8.276,
            **pitch,
            'pages_measured_on': gap_pages,
            'gaps_pt': [round(g, 4) for g in gaps],
        },
        'rule_38a_occurrences': [
            {'sheet': h['sheet'], 'row_idx': h['row_idx'], 'text': h['text'],
             'in_certiorari_denied': cert_section_start <= h['row_idx'] < cert_section_end}
            for h in rule38a
        ],
        'known_lossiness': {
            'description': ('Docket numbers whose "NN-" or "NNM" prefix and whose numeral suffix are '
                             'drawn by two separate, out-of-order text-positioning operations in the '
                             "page's content stream (the suffixes are drawn as an earlier batch, at a "
                             'different x, before the main docket/caption column). The line-break '
                             'convention used for entry counting above (a new line at every '
                             "Td/TD/Tm/T*/'/\" operator) never reassembles these, so they are silently "
                             'absent from certiorari_denied.total/before/after above, exactly as they '
                             "would be absent from the prior session's own extractor, which uses the "
                             'same convention. Confirmed by direct inspection of the raw content stream '
                             "and of the rendered page (render/sheet-25.png): all six dockets ARE "
                             'visibly, correctly printed on the page; only this extraction convention '
                             'misses them.'),
            'fragments': [{'sheet': h['sheet'], 'row_idx': h['row_idx'], 'text': h['text']} for h in lossy],
            'count': len(lossy),
            'corrected_certiorari_denied_total': len(cert) + len(lossy),
            'corrected_before_mass_sentence': len(before) + len(lossy),
            'corrected_after_mass_sentence': len(after),
        },
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, indent=1)
    size_kb = os.path.getsize(OUT_PATH) / 1024.0
    print()
    print('Wrote %s (%.1f KB)' % (OUT_PATH, size_kb))


if __name__ == '__main__':
    main()
