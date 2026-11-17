"""OTHER HANDS — reading sheets for the second reading of the red line (session 250, 2026-11-17).

Usage: python3 -I voice_sheets.py <mongodump_full_snapshot/> <ulysses checkout> <out dir, outside the repository>

The red line on the sheet joined two readers' rules: the Field's wider "quotes or carries the harmed's own words"
(46 first reports) and the Atelier's finer one (own words 8, an organisation's statement 4, through someone else 10).
The Atelier's critique of 2026-11-15 (ulysses, artifacts/cycle-015/step-3-critique.md, Studio point 2) says a voice
and a telling should not look alike. This writes the sheets on which convened readers read them again by one rule,
the Atelier's stated rule: the Field's 46 and, mixed in and unmarked, the Atelier's own 30 as a measure of whether
the readers apply that rule as the Atelier did. The sheets carry the snapshot's text and are never committed.
"""
import csv, json, os, random, subprocess, sys

csv.field_size_limit(10**9)
SNAP, ATELIER, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
A_COMMIT = '5a1e763b08994ca31afc13d82d96c0ebb71a06b5'
t = open(os.path.join(HERE, '..', 'data.js'), encoding='utf-8').read()
D = json.loads(t[t.index('=') + 1:].rstrip().rstrip(';'))
FIELD = sorted(r[0] for r in D['inc'] if r[9] == 'f')
chk = subprocess.run(['git', '-C', ATELIER, 'show', f'{A_COMMIT}:artifacts/cycle-015/named-for-them/check.js'],
                     capture_output=True, check=True).stdout.decode('utf-8')
VOICE = sorted(x['id'] for x in json.loads(chk[chk.index('=') + 1:].rstrip().rstrip(';'))['voice'])
assert len(FIELD) == 46 and len(VOICE) == 30 and not set(FIELD) & set(VOICE)


def rows(name):
    with open(os.path.join(SNAP, name), newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


inc, rep = rows('incidents.csv'), rows('reports.csv')
rep_by_num = {}
for r in rep:
    try:
        rep_by_num[int(r['report_number'])] = r
    except ValueError:
        pass


def pubkey(r):            # the first report, as build.py and the Field choose it
    try:
        e = float(r['epoch_date_published'])
    except ValueError:
        e = None
    return (e is None, e if e is not None else 0, int(r['report_number']))


INC = {int(r['incident_id']): r for r in inc}
ids = FIELD + VOICE
random.Random(20261117).shuffle(ids)
QUOTES = '"“”‘’'
key, sheets = [], [[], []]
for n, i in enumerate(ids, 1):
    r = INC[i]
    nums = json.loads(r['reports']) if r['reports'] else []
    first = sorted((rep_by_num[x] for x in nums if x in rep_by_num), key=pubkey)[0]
    text = first['text'] or ''
    later = ''
    if len(text) > 6000:      # beyond 6,000 characters, every later paragraph that holds a quotation mark
        later = '\n'.join(p for p in text[6000:].split('\n') if any(q in p for q in QUOTES))[:3000]
    item = {'item': n, 'incident': i, 'report': int(first['report_number']), 'domain': first['source_domain'],
            'harmed_column': json.loads(r['Alleged harmed or nearly harmed parties'] or '[]'),
            'title': first['title'], 'text': text[:6000], 'later_quoted_paragraphs': later,
            'text_length': len(text)}
    sheets[0 if n <= len(ids) // 2 else 1].append(item)
    key.append({'item': n, 'incident': i, 'report': item['report'], 'set': 'field' if i in FIELD else 'atelier'})
os.makedirs(OUT, exist_ok=True)
for s, items in enumerate(sheets, 1):
    with open(os.path.join(OUT, f'sheet-{s}.json'), 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=1)
with open(os.path.join(OUT, 'key.json'), 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=1)
print(len(ids), [len(x) for x in sheets])
