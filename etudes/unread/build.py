"""UNREAD — build data.json from a hand reading of Ituri's line on the dead in INSP's daily reports.

Source: INSP, Rapport de Situation MVE (RDC), as archived in INRB-UMIE/BDBV2026-Data,
data/insp_sitrep/raw/, commit 338e5780443ad5ba2f4ae9dfbe1dc08d00aac189 (MIT). Texts made with
`pdftotext -layout`; no PDF or text is committed here.

Every row below was read by eye in the report's PCI/EDS paragraph for Ituri (and, where a
report writes Ituri's swab failures elsewhere, in that sentence). This script checks, for each row:
  - every quoted French string occurs in the report text (whitespace collapsed);
  - every number the row carries is written in its quote;
  - the report's date, taken from its own header.
It then writes data.json for the page and asserts the figures the page states.

Usage: python3 -I build.py <dir of SitRep_MVE_*.txt>
"""
import glob, json, os, re, sys
TXT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))

# report: (alerts, swabbed, swabbed_of, unread_written, quote, unread_quote)
# unread_written = bodies the report writes as swab failures or as 'could not be swabbed'
ROWS = {
 108: (83, 48, None, 9, "62 EDS réalisées sur 83 alertes et 48 corps swabés (9 échecs)", None),
 109: (93, 61, None, 10, "71 EDS réalisées sur 93 alertes et 61 corps swabés (10 échecs)", None),
 110: (126, 65, None, 42, "77 EDS réalisées sur 126 alertes et 65 corps swabés (42 échecs)", None),
 111: (91, 56, None, None, "72 EDS réalisées sur 91 alertes et 56 corps swabés", None),
 112: (83, 48, None, None, "83 alertes ont été enregistrées, dont 10 reports de la veille, 62 EDS réalisées et 48 corps swabés", None),
 113: (80, 52, None, None, "80 alertes ont été enregistrées, dont 6 reports de la veille, 59 EDS réalisées et 52 corps swabés, 7 dossiers étant reportés au jour suivant", None),
 114: (104, 56, None, 30, "104 alertes ont été enregistrées, dont 7 reports de la veille, 71 EDS réalisées et 56 corps swabés", "30 corps n’ayant pu l’être du fait de résistances communautaires"),
 115: (82, 50, 59, 5, "82 alertes ont été enregistrées, dont 3 reports de la veille, 59 EDS réalisées (72,0 %) et 50 corps swabés sur 59 (5 échecs)", None),
 116: (92, 67, 79, None, "92 alertes ont été enregistrées, 79 EDS réalisées (85,9 %) et 67 corps swabés sur 79", None),
 117: (75, 51, 62, None, "75 alertes ont été enregistrées, 62 EDS réalisés (82,7 %) et 51 corps swabés sur 62 (82,3 %)", None),
 118: (96, 65, None, None, "96 alertes ont été enregistrées (dont 7 reports de la veille), 77 EDS réalisés (80,2 %) et 65 corps swabés", None),
 119: (95, 54, None, None, "95 alertes ont été enregistrées (dont 13 reports de la veille), 71 EDS réalisés (74,7 %) et 54 corps swabés", None),
 120: (82, 56, None, None, "82 alertes ont été enregistrées dont 66 EDS réalisés (80,5 %) et 56 corps swabés", None),
 121: (92, 63, None, 9, "92 alertes ont été enregistrées, 74 EDS réalisés (80,4 %) et 63 corps swabés", "9 échecs enregistrés à Fataki et Mandima notamment"),
 122: (68, 54, 65, None, "68 alertes ont été enregistrées (dont 9 reports), 65 EDS réalisés sur 77 (84,4 %) et 54 corps swabés sur 65 (83,1 %)", None),
 123: (79, 54, 65, None, "79 alertes ont été enregistrées, 61 EDS réalisés sur 79 (77,2 %) et 54 corps swabés sur 65 (83,1 %)", None),
 124: (83, 61, 66, None, "83 alertes ont été enregistrées, 66 EDS réalisés sur 75 (88,0 %) et 61 corps swabés sur 66 (92,4 %)", None),
 127: (104, 69, 80, None, "104 alertes ont été enregistrées, 80 EDS réalisés (76,9 %) et 69 corps swabés sur 80 (86,3 %)", None),
 128: (99, 67, 79, 12, "99 alertes ont été enregistrées (dont 9 reports de la veille), 81 EDS réalisés sur 97 (82,0 %) et 67 corps swabés sur 79", "12 n'ont pas pu être swabés (15,2 %)"),
 129: (78, 52, None, 13, "78 alertes ont été enregistrées (dont 6 reports de la veille), 61 EDS réalisés (78,2 %) et 52 corps swabés", "13 corps n’ont pas pu être swabés"),
 130: (98, 68, None, None, "98 alertes ont été enregistrées (dont 4 reports de la veille), 76 EDS réalisés (80,9 % ; 76/94) et 68 corps swabés", None),
 131: (104, 71, None, 19, "104 alertes ont été enregistrées (dont 8 reports de la veille), 76 EDS réalisés (73,1 %) et 71 corps swabés", "19 n’ont pas pu être swabés (18,3 %)"),
 132: (91, 66, None, 25, "91 alertes ont été enregistrées (dont 9 reports de la veille), 55 EDS réalisés (60,4 %) et 66 corps swabés", "25 échecs de swab ont été notifiés"),
 133: (72, 52, None, 9, "72 alertes ont été enregistrées (dont 11 reports de la veille), 54 EDS réalisés (75,0 %) et 52 corps swabés", "9 échecs de swab ont été notifiés"),
 136: (87, 59, None, None, "87 alertes EDS a été rapporté, 60 EDS réalisés et 59 corps swabés", None),
 137: (82, 58, None, None, "Sur 82 alertes EDS (dont 8 reports), 58 EDS ont été réalisés (70,7 %) et 58 corps swabés", None),
 138: (82, 55, None, None, "Sur 82 alertes EDS (dont 5 reports), 60 EDS ont été réalisés (73,2 %) et 55 corps swabés", None),
 139: (76, 55, None, None, "Sur 76 alertes EDS (dont 5 reports), 54 EDS ont été réalisés (71,1 %) et 55 corps swabés", None),
 140: (92, 63, None, None, "Sur 92 alertes EDS (dont 4 reports), 57 EDS ont été réalisés (62,0 %) et 63 corps swabés", None),
 141: (69, 38, None, None, "Sur 69 alertes EDS (dont 8 reports), 49 EDS ont été réalisés (71,0 %) et 38 corps swabés", None),
 142: (99, 70, None, None, "Sur 99 alertes EDS (dont 10 reports), 68 EDS ont été réalisés (68,7 %) et 70 corps swabés", None),
 143: (94, 68, None, None, "Sur 94 alertes EDS (dont 10 reports), 83 EDS ont été réalisés (88,3 %) et 68 corps swabés", None),
 144: (96, 65, None, 29, "Sur 96 alertes EDS (dont 6 reports), 59 EDS ont été réalisés (61,5 %) et 65 corps swabés", "29 échecs et 8 reports ont été enregistrés en fin de journée"),
 145: (100, 69, None, None, "Sur 100 alertes EDS (dont 8 reports de la veille), 78 EDS ont été réalisés (78,0 %) et 69 corps swabés", None),
 146: (106, 74, None, 22, "Sur 106 alertes EDS (dont 8 reports de la veille), 78 EDS ont été réalisés (73,6 %) et 74 corps swabés, avec 22 échecs (20,8 %)", None),
 147: (99, 62, None, 32, "Sur 99 alertes EDS (dont 8 reports de la veille), 57 EDS ont été réalisés (57,6 %) et 62 corps swabés", "avec 32 échecs (32,3 %) liés aux refus à Bambu, Mambasa, Mangala, Fataki et Mandima"),
 148: (91, 63, None, 26, "Sur 91 alertes EDS (dont 10 reports de la veille), 57 EDS ont été réalisés (62,6 %) et 63 corps swabés", "avec 26 échecs (28,6 %) liés aux résistances à Komanda, Nyakunde, Mongbwalu, Nia-Nia, Fataki et Mandima"),
 149: (108, 82, None, 23, "Sur 108 alertes EDS (dont 8 reports de la veille), 70 EDS ont été réalisés (64,8 %) et 82 corps swabés", "avec 23 échecs (21,3 %) liés aux résistances à Bambu, Mangala et Mandima"),
 150: (68, 56, None, None, "Sur 68 alertes EDS (dont 15 reports de la veille), 55 EDS ont été réalisés (80,9 %) et 56 corps swabés", None),
 151: (113, 76, 102, None, "Sur 113 alertes EDS (dont 5 reports de la veille), 80 EDS ont été réalisés (70,8 %) et 76 corps swabés sur 102", None),
 152: (113, 88, 96, 32, "Sur 113 alertes EDS (dont 15 reports de la veille), 79 EDS ont été réalisés (69,9 %) et 88 corps swabés sur 96", "avec 32 échecs liés aux résistances à Bambu, Nia-Nia, Tchomia, Mangala et Mandima"),
 153: (94, 64, 81, None, "Sur 94 alertes EDS (dont 2 reports de la veille), 61 EDS ont été réalisés (64,9 %) et 64 corps swabés sur 81 (79,0 %)", None),
 154: (102, 69, 90, None, "Sur 102 alertes EDS (dont 14 reports de la veille), 64 EDS ont été réalisés (62,7 %) et 69 corps swabés sur 90 (76,7 %)", None),
 155: (99, 75, 92, None, "Sur 99 alertes EDS (dont 14 reports de la veille), 59 EDS ont été réalisés (59,6 %) et 75 corps swabés sur 92 (81,5 %)", None),
 156: (89, 65, 79, None, "Sur 89 alertes EDS, 74 EDS ont été réalisés (83,1 %) et 65 corps swabés sur 79 (82,3 %)", None),
 157: (76, 51, 67, None, "44 EDS ont été réalisés sur 76 alertes EDS, (57,9 %) et 51 corps swabés sur 67 (76,1 %)", None),
 165: (84, 40, None, None, "46 EDS réalisés sur 84 alertes (54,8 %) et 40 corps swabés", None),
 166: (72, 58, None, None, "44 EDS réalisés sur 72 alertes, dont 23 reports (61,1 %), et 58 corps swabés", None),
 167: (93, 58, None, 16, "66 EDS réalisés sur 93 alertes, dont 12 reports (71,0 %), et 58 corps swabés", "16 échecs de swab (17 %)"),
 168: (68, 40, None, 13, "47 EDS réalisés sur 68 alertes (69,1 %), 40 corps swabés", "13 échecs de swab ont été enregistrés"),
 169: (83, 56, 69, None, "60 EDS réalisés sur 83 alertes (72,3 %) et 56 corps swabés sur 69", None),
 170: (91, 59, 78, 13, "66 EDS réalisés sur 91 alertes, dont 10 reports (72,5 %), 59 corps swabés sur 78", "13 échecs de swab ont été enregistrés (16,7 %)"),
 171: (73, 49, None, 11, "49 EDS réalisés sur 73 alertes, dont 11 reports (67,1 %), 49 corps swabés avec 11 échecs de swab", None),
 173: (115, 75, None, None, "83 EDS réalisés sur 115 alertes, dont 6 reports (72,2 %), et 75 corps swabés", None),
 174: (90, 49, None, 22, "53 EDS réalisés sur 90 alertes, dont 16 reports (58,9 %), 49 corps swabés", "22 échecs de prélèvement ont été enregistrés sur les corps"),
}
# reports in the window whose Ituri paragraph this reading found writing no bodies swabbed
NO_LINE = [125, 126, 134, 135, 164]
# a sentence about burials, not swabs, that the next day's report rewords as swabs (kept out of the counts)
NOTES = {166: "16 échecs d’EDS (22 %)", 167: "16 échecs de swab (17 %)"}

MO = {'janvier':1,'février':2,'mars':3,'avril':4,'mai':5,'juin':6,'juillet':7,'août':8,'septembre':9,'octobre':10,'novembre':11,'décembre':12}
texts = {}
for p in glob.glob(os.path.join(TXT, 'SitRep_MVE_*.txt')):
    n = int(re.search(r'_(\d+)[-_]', p).group(1))
    if n >= 108: texts[n] = re.sub(r'\s+', ' ', open(p, encoding='utf-8').read())
def date_of(t):
    m = re.search(r'Date de rapportage\s*:\s*(\d{1,2})(?:er)?\s+(\w+)\s+2026', t)
    if m and m.group(2).lower() in MO: return '2026-%02d-%02d' % (MO[m.group(2).lower()], int(m.group(1)))
    m = re.search(r'N°\s*\d+\s*/MVE-?BDBV?/(\d\d)/(\d\d)/2026', t)
    return '2026-%s-%s' % (m.group(2), m.group(1))

days = []
for n in sorted(set(texts)):
    t = texts[n]; d = date_of(t)
    if n in ROWS:
        A, S, M, U, q, uq = ROWS[n]
        for s in (q, uq):
            if s: assert s in t, (n, s)
        nums = [int(x) for x in re.findall(r'\d+', q + ' ' + (uq or ''))]
        for v in (A, S, M, U):
            if v is not None: assert v in nums, (n, v)
        days.append({'report': n, 'date': d, 'alerts': A, 'swabbed': S, 'of': M, 'unread': U,
                     'q': q, 'uq': uq, 'note': NOTES.get(n)})
    else:
        assert n in NO_LINE, n
        days.append({'report': n, 'date': d, 'alerts': None, 'note': None})
for n, s in NOTES.items(): assert s in texts[n], (n, s)
# reports the archive does not hold inside the window
held = sorted(texts)
gaps = [n for n in range(108, 175) if n not in held]

ws = [x for x in days if x.get('alerts')]
written = [x for x in ws if x['unread'] is not None]
assert len(days) == 60 and len(ws) == 55 and len(written) == 22, (len(days), len(ws), len(written))
assert gaps == [158, 159, 160, 161, 162, 163, 172], gaps
tot_A = sum(x['alerts'] for x in ws); tot_S = sum(x['swabbed'] for x in ws); tot_U = sum(x['unread'] for x in written)
assert (tot_A, tot_S, tot_U) == (4954, 3315, 422), (tot_A, tot_S, tot_U)
over = [x['report'] for x in ws if x['swabbed'] + (x['unread'] or 0) > x['alerts']]
assert over == [152], over
d1 = next(x for x in ws if x['report'] == 110); assert (d1['date'], d1['alerts'], d1['swabbed'], d1['unread']) == ('2026-09-01', 126, 65, 42)
# 30 Aug and 3 Sep write the same three numbers
a, b = ROWS[108], ROWS[112]; assert a[:2] == b[:2]
json.dump({'source': 'INSP SitRep MVE via INRB-UMIE/BDBV2026-Data@338e5780', 'gaps': gaps, 'days': days,
           'totals': {'reports': len(days), 'with_line': len(ws), 'written': len(written), 'alerts': tot_A, 'swabbed': tot_S, 'unread': tot_U}},
          open(os.path.join(HERE, 'data.json'), 'w'), ensure_ascii=False, indent=1)
open(os.path.join(HERE, 'data.js'), 'w').write('window.UNREAD = ' + open(os.path.join(HERE, 'data.json'), encoding='utf-8').read() + ';\n')
print('ok', len(days), 'reports;', len(ws), 'with a line;', len(written), 'write the unread;', tot_A, tot_S, tot_U, 'gaps', gaps)
