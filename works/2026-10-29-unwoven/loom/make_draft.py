"""UNWOVEN, the loom score: turns the work's own data.js into a weaving draft.

Run from the work's folder:  python3 -I loom/make_draft.py
Reads data.js and summary.json (both committed beside the work), writes into loom/:
  draft.png          indexed bitmap, one pixel per warp end x weft pick (1,626 x 2,000);
                     palette index = weave structure, listed in draft-summary.json
  knots.csv          every knot (an area written with no people and no phase): end, pick, area
  draft-summary.json the counts, each asserted against summary.json, and every rounding
  preview.png        the draft at 1100 px wide, against light, for the instruction
No third-party code: the PNG files are written by the standard library (zlib) below.
"""
import json, csv, os, struct, zlib


def png(path, w, h, rows, palette=None):
    """Write a PNG: indexed (8-bit, palette) when palette is given, else RGB; rows are bytes per line."""
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    ct = 3 if palette else 2
    raw = b''.join(b'\x00' + r for r in rows)
    out = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, ct, 0, 0, 0))
    if palette:
        out += chunk(b'PLTE', bytes(c for rgb in palette for c in rgb))
    out += chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(out)

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)
ENDS_PER_THREAD = 2
PICKS = 2000          # the cloth's length in picks, at 20 picks per cm = 100 cm
MIN_HOLE = 2          # a hole is never shorter than 2 picks (the screen's 2 px floor)

src = open(os.path.join(WORK, 'data.js'), encoding='utf-8').read()
U = json.loads(src[src.index('=') + 1:].rstrip().rstrip(';'))
S = json.load(open(os.path.join(WORK, 'summary.json')))
T, NAMES = U['threads'], U['names']
assert len(T) == S['threads'] == 813

# palette index -> structure. 0-4: IPC phases 1-5 in the IPC's colours, woven weft-faced.
# 5: hole, warp passes and no weft is bound into it. 6: a thread written with no people at all.
PAL = [(0xcd, 0xfa, 0xcd), (0xfa, 0xe6, 0x1e), (0xe6, 0x78, 0x00), (0xc8, 0x00, 0x00), (0x64, 0x00, 0x00),
       (0xff, 0xff, 0xff), (0x2a, 0x20, 0x17)]
STRUCT = ['phase 1, weft-faced, IPC colour #cdfacd', 'phase 2, weft-faced, #fae61e', 'phase 3, weft-faced, #e67800',
          'phase 4, weft-faced, #c80000', 'phase 5, weft-faced, #640000',
          'HOLE: bare warp, no weft bound in (see INSTRUCTION.md, the hole)',
          'a thread with no people written: plain weave in undyed dark weft, its knots tied on it']


def apportion(weights, total):
    """Largest-remainder rounding of weights to integers summing to total."""
    s = sum(weights)
    raw = [w / s * total for w in weights]
    out = [int(r) for r in raw]
    rest = total - sum(out)
    for i in sorted(range(len(raw)), key=lambda i: -(raw[i] - out[i]))[:rest]:
        out[i] += 1
    return out


W = len(T) * ENDS_PER_THREAD
grid = [bytearray([6] * W) for _ in range(PICKS)]
knots, holes_raised, holes_total, hole_picks = [], 0, 0, 0
nA = nB = nC = 0
zero_threads = 0

for k, t in enumerate(T):
    a = t['a']
    tot = sum(x[2] for x in a)
    e0 = k * ENDS_PER_THREAD
    for x in a:
        nA += x[8] == 'A'; nB += x[8] == 'B'; nC += x[8] == 'C'
    if not tot:
        zero_threads += 1
        for i, x in enumerate(a):
            knots.append((k, e0, int((i + .5) / len(a) * PICKS), NAMES[x[1]], x[8], t['c'], t['d'], t['v']))
        continue
    # each area its share of the thread's picks; holes floored at MIN_HOLE, taken from the largest area
    L = apportion([x[2] for x in a], PICKS)
    for i, x in enumerate(a):
        if x[8] == 'C':
            holes_total += 1
            if L[i] < MIN_HOLE:
                need = MIN_HOLE - L[i]; L[i] = MIN_HOLE; holes_raised += 1
                j = max((j for j in range(len(a)) if a[j][8] != 'C'), key=lambda j: L[j])
                L[j] -= need
    assert sum(L) == PICKS and min(L) >= 0
    y = 0
    for i, x in enumerate(a):
        if x[8] == 'C':
            idx = [5] * L[i]; hole_picks += L[i]
        elif x[8]:                       # A or B: no people, so no length; a knot at its place
            knots.append((k, e0, min(PICKS - 1, y), NAMES[x[1]], x[8], t['c'], t['d'], t['v']))
            idx = []
        else:
            ph = [x[3 + p] for p in range(5)]
            if sum(ph) and L[i]:
                parts = apportion(ph, L[i])
                idx = [p for p in range(5) for _ in range(parts[p])]
            else:
                idx = [6] * L[i]
        for n, v in enumerate(idx):
            for e in range(ENDS_PER_THREAD):
                grid[y + n][e0 + e] = v
        y += len(idx)

assert nA == S['totals']['A'] and nB == S['totals']['B'] and nC == S['totals']['C'] == holes_total
assert len(knots) == nA + nB, (len(knots), nA, nB)
assert zero_threads == S['threads_all_zero']
png(os.path.join(HERE, 'draft.png'), W, PICKS, [bytes(r) for r in grid], PAL)

with open(os.path.join(HERE, 'knots.csv'), 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['thread', 'end', 'pick_from_top', 'area', 'encoding', 'country', 'analysis', 'period'])
    w.writerows(knots)

# preview: the cloth hung in a window with daylight behind it: weft-faced cloth passes little light, so its
# colours are drawn at a quarter; a hole passes it all. Holes bright, 1100 px wide (each end ~0.68 px), with a 40 px margin of wall
PW, PH, M = 1100, 1080, 40
WALL = bytes((18, 16, 14))
prow = []
for yy in range(PH):
    if yy < M or yy >= PH - M:
        prow.append(WALL * PW); continue
    g = grid[(yy - M) * PICKS // (PH - 2 * M)]
    line = bytearray(WALL * M)
    for xx in range(PW - 2 * M):
        # a hole wins its pixel if any end under it is a hole, as on the screen (holes are never faded)
        e0, e1 = xx * W // (PW - 2 * M), max(xx * W // (PW - 2 * M) + 1, (xx + 1) * W // (PW - 2 * M))
        v = 5 if 5 in g[e0:e1] else g[e0]
        line += bytes((255, 253, 243)) if v == 5 else bytes(int(c * .26) for c in PAL[v])
    line += WALL * M
    prow.append(bytes(line))
png(os.path.join(HERE, 'preview.png'), PW, PH, prow)

counts = {p: 0 for p in range(7)}
for r in grid:
    for v in range(7):
        counts[v] += r.count(v)
summary = {
    'source': 'data.js and summary.json of this work (built from HDX ipc_global_area_long.csv, sha256 in raw-manifest.json)',
    'ends': W, 'picks': PICKS, 'ends_per_thread': ENDS_PER_THREAD,
    'sett': '20 ends and 20 picks per cm, so the cloth is 81.3 cm wide and 100 cm long before take-up',
    'order': 'threads left to right in the order of the record (the work\'s hang "by time"); areas top to bottom in the table\'s order',
    'threads': len(T), 'holes': holes_total, 'holes_raised_to_min_picks': holes_raised, 'min_hole_picks': MIN_HOLE,
    'knots': len(knots), 'knots_A': nA, 'knots_B': nB, 'threads_with_no_people': zero_threads,
    'hole_share_of_cloth': round(counts[5] / (W * PICKS), 5),
    'structures': {str(i): STRUCT[i] for i in range(7)},
    'cells_per_structure': {str(i): counts[i] for i in range(7)},
    'rounding': 'each area gets its share of 2,000 picks by largest remainder; a hole shorter than 2 picks is raised to 2, the 2 taken from the longest classified area of the same thread; a knot has no length and is tied at the pick where its area stands',
    'asserted_against_summary_json': ['threads 813', 'holes = C 1,041', 'knots = A 6,352 + B 16', 'threads with no people 6'],
}
json.dump(summary, open(os.path.join(HERE, 'draft-summary.json'), 'w'), indent=1)
print(json.dumps({k: summary[k] for k in ('ends', 'picks', 'holes', 'holes_raised_to_min_picks', 'knots', 'hole_share_of_cloth', 'cells_per_structure')}))
