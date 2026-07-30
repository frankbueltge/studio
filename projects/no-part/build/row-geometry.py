#!/usr/bin/env python3
"""NO PART — read-only row-geometry helper, session 49.

Sits next to extract-rows.py and imports it directly (rather than
re-deriving anything) to answer one narrow question extract-rows.py's own
committed rows.json does not carry: the PDF-point (x, y) baseline position
of specific rows, by row_idx, straight from the PDF's own content streams.

extract-rows.py's build_all_lines() already computes this per line
({'sheet','y','x','text'}) but only writes row_idx/text/sheet into rows.json
(row_pitch's gaps_pt aside). This script re-runs the same, unmodified
extraction (verify_hash -> PDF -> walk_pages -> build_all_lines) and prints
the requested rows' own {sheet, x, y, text}, plus each requested sheet's own
/MediaBox height in pt (read directly off the page dict, not assumed), as
JSON on stdout. It writes nothing, mutates nothing, and re-derives nothing
that extract-rows.py didn't already derive — it only exposes fields that
were computed but not persisted.

Usage:
    python3 build/row-geometry.py 1756 1757 1953 1954
Prints: {"pages_mediabox_h_pt": {<sheet>: <h_pt>, ...},
         "rows": [{"row_idx":..., "sheet":..., "x":..., "y":..., "text":...}, ...]}
"""
import importlib.util
import json
import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_extract_rows_module():
    # extract-rows.py has a hyphen, so it can't be `import`ed by name;
    # load it by file path instead. Nothing in the module's own top-level
    # code has side effects beyond defining functions/constants (its work
    # happens in main(), which this script never calls).
    spec = importlib.util.spec_from_file_location('er', os.path.join(SCRIPT_DIR, 'extract-rows.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    row_indices = [int(a) for a in sys.argv[1:]]
    if not row_indices:
        print('Usage: python3 row-geometry.py <row_idx> [row_idx ...]', file=sys.stderr)
        sys.exit(1)

    er = load_extract_rows_module()
    er.verify_hash(er.PDF_PATH, er.EXPECTED_SHA256)
    with open(er.PDF_PATH, 'rb') as f:
        data = f.read()
    pdf = er.PDF(data)
    pages = pdf.walk_pages()
    all_lines = er.build_all_lines(pdf, pages)

    rows = []
    sheets_needed = set()
    for idx in row_indices:
        r = all_lines[idx]
        rows.append({'row_idx': idx, 'sheet': r['sheet'], 'x': r['x'], 'y': r['y'], 'text': r['text']})
        sheets_needed.add(r['sheet'])

    mediabox_h = {}
    for sheet in sorted(sheets_needed):
        pnum = pages[sheet - 1]
        d = pdf.get_object_dict(pnum)
        m = re.search(rb'/MediaBox\s*\[\s*([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s+([\d.\-]+)\s*\]', d)
        if not m:
            raise ValueError('sheet %d: no /MediaBox found on its own page dict' % sheet)
        x0, y0, x1, y1 = (float(v) for v in m.groups())
        mediabox_h[str(sheet)] = y1 - y0

    print(json.dumps({'pages_mediabox_h_pt': mediabox_h, 'rows': rows}, indent=1))


if __name__ == '__main__':
    main()
