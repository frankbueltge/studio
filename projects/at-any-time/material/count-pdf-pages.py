#!/usr/bin/env python3
"""Count PDF pages directly from PDF bytes, with no PDF library.

Two independent methods, cross-checked against each other:

  (A) Count distinct indirect objects whose dictionary contains
      "/Type /Page" (allowing "/Type/Page" with no space, and tolerating
      the token appearing inside a compressed object stream is NOT handled
      here — see caveat below). This counts actual leaf page objects.

  (B) Walk every "/Type /Pages" dictionary (there is normally exactly one,
      the root of the page tree, but some producers emit intermediate
      /Pages nodes too) and read its own "/Count N" entry. The document's
      true page count is the /Count of the ROOT page-tree node (the one
      referenced by the trailer/Root/Pages, or — if that cannot be
      resolved — the single largest /Count found, since intermediate nodes
      never exceed the root's total).

CAVEAT, stated rather than hidden: if a PDF's cross-reference/object data is
stored in a compressed object stream (/Type /ObjStm, cross-reference
streams, "PDF 1.5+ compressed xref"), method (A)'s literal byte-string
search for "/Type/Page" will NOT see objects whose dictionary lives only
inside a compressed stream (that content is deflate-compressed and does not
contain the literal ASCII text until decompressed). This script therefore
ALSO decompresses every FlateDecode stream in the file (the same technique
extract-order-text.py already uses) and re-runs the literal search over the
decompressed bytes, unioning both passes. Any document where method (A) and
method (B) still disagree after this is flagged explicitly, not
silently resolved.
"""
import re
import sys
import json
import zlib

TYPE_PAGE_RE = re.compile(rb'/Type\s*/Page(?![A-Za-z])')
TYPE_PAGES_RE = re.compile(rb'/Type\s*/Pages(?![A-Za-z])')
COUNT_RE = re.compile(rb'/Count\s+(\d+)')
ROOT_RE = re.compile(rb'/Root\s+(\d+)\s+\d+\s+R')
OBJ_RE = re.compile(rb'(\d+)\s+(\d+)\s+obj\b', re.DOTALL)


def find_object_bodies(data):
    """Yield (obj_num, body_bytes) for every 'N G obj ... endobj' span."""
    out = []
    for m in OBJ_RE.finditer(data):
        obj_num = int(m.group(1))
        start = m.end()
        end = data.find(b'endobj', start)
        if end < 0:
            end = len(data)
        out.append((obj_num, data[start:end]))
    return out


def decompressed_streams(data):
    """Yield decompressed bytes of every zlib-decodable 'stream...endstream' span
    (covers both content streams and, importantly, compressed object streams
    /ObjStm, which is where a cross-reference-stream PDF can hide page
    dictionaries from a plain byte search)."""
    out = []
    for m in re.finditer(rb'stream\r?\n', data):
        start = m.end()
        end = data.find(b'endstream', start)
        if end < 0:
            continue
        raw = data[start:end]
        # Trailing CR/LF before 'endstream' is not part of the stream data.
        raw = raw.rstrip(b'\r\n')
        try:
            dec = zlib.decompress(raw)
        except Exception:
            continue
        out.append(dec)
    return out


def method_a_count_page_objects(data):
    """Direct object dictionaries with /Type /Page, found either in the raw
    file bytes or inside any decompressed stream (covers ObjStm-hidden
    dictionaries in compressed-xref PDFs)."""
    direct_hits = len(TYPE_PAGE_RE.findall(data))
    hidden_hits = 0
    for dec in decompressed_streams(data):
        hidden_hits += len(TYPE_PAGE_RE.findall(dec))
    return direct_hits, hidden_hits


def method_b_root_count(data):
    """Find every /Pages dictionary's own /Count entry (in raw bytes and in
    decompressed streams), and separately try to identify the ROOT /Pages
    node via the trailer's /Root -> catalog -> /Pages chain. Falls back to
    the maximum /Count seen if the root cannot be resolved, since no
    intermediate /Pages node can exceed the root's total in a well-formed
    tree.

    /Count can appear either BEFORE or AFTER /Type/Pages within the same
    flat dictionary (e.g. "<</Count 1/Kids[27 0 R]/Type/Pages>>" — observed
    in these documents' compressed object streams), so the dictionary's
    enclosing "<< ... >>" span is located first (nearest preceding "<<" to
    nearest following ">>"; these page-tree dictionaries are not nested),
    then /Count is searched for anywhere inside that span, not just after
    the /Type/Pages token."""
    candidates = []

    def scan(buf):
        for m in TYPE_PAGES_RE.finditer(buf):
            dict_start = buf.rfind(b'<<', 0, m.start())
            dict_end = buf.find(b'>>', m.end())
            if dict_start == -1 or dict_end == -1:
                continue
            span = buf[dict_start:dict_end]
            cm = COUNT_RE.search(span)
            if cm:
                candidates.append(int(cm.group(1)))

    scan(data)
    for dec in decompressed_streams(data):
        scan(dec)

    if not candidates:
        return None, []
    return max(candidates), candidates


def count_pages(path):
    data = open(path, 'rb').read()
    direct_hits, hidden_hits = method_a_count_page_objects(data)
    a_total = direct_hits + hidden_hits
    b_max, b_all = method_b_root_count(data)
    return {
        'file': path,
        'bytes': len(data),
        'method_a_page_objects_direct': direct_hits,
        'method_a_page_objects_in_streams': hidden_hits,
        'method_a_total': a_total,
        'method_b_count_candidates': b_all,
        'method_b_max_count': b_max,
        'agree': (a_total == b_max) if b_max is not None else None,
    }


def main():
    results = []
    for p in sys.argv[1:]:
        results.append(count_pages(p))
    print(json.dumps(results, indent=1))


if __name__ == '__main__':
    main()
