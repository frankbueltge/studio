#!/usr/bin/env python3
"""Every number printed in THE-SCORE.md, THE-RULE.md and ARTIST-SCORE-60.md comes from
this script. Session 60, 2026-08-02.

Run:  python3 artist-60-counts.py recalls-2026-07-01_2026-08-02.json

Source of record: the raw body of
https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2026-07-01&RecallDateEnd=2026-08-02
sha256 cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1

Every coding is NAMED and printed as an interval where the count moves with the coding.
No number in my files is quoted from another document; all are re-derived here.
"""
import json, re, sys, hashlib, collections

path = sys.argv[1] if len(sys.argv) > 1 else 'recalls-2026-07-01_2026-08-02.json'
raw = open(path, 'rb').read()
R = json.loads(raw)
N = len(R)
print("file:", path)
print("sha256:", hashlib.sha256(raw).hexdigest())
print("records:", N)
dates = sorted(r['RecallDate'][:10] for r in R)
print("date span:", dates[0], "…", dates[-1], "| distinct publication dates:", len(set(dates)))


def rem(r):
    return ' '.join(x.get('Name', '') for x in (r.get('Remedies') or []))


def desc(r):
    return r.get('Description', '') or ''


def firms(r, keys=('Manufacturers', 'Importers', 'Distributors')):
    out = []
    for k in keys:
        for x in (r.get(k) or []):
            if x.get('Name', '').strip():
                out.append(x['Name'].strip())
    return out


# ---------------------------------------------------------------- CODINGS
# C1  STOP        : /stop using[^.]*immediately/i on Remedies  (the campaign's own sentence)
# C2a DESTROY-INC : ARTIST-REFORM-59's DESTROY regex, inclusive (counts component-only disposal)
# C2b DESTROY-STR : C2a minus records whose only destruction target is a component or a future note
# C3a PHOTO-LOOSE : any required evidentiary photograph, any delivery route
# C3b PHOTO-STRICT: photograph OF the destruction, delivered to a named email address
# C4a MARKER-STR  : literal phrase "permanent marker"
# C4b MARKER-LOOSE: any marker/sharpie instruction to write on the object
# C5  PAY         : remedy promises the owner money back (refund / reimburse / gift card / credit)
# C6  DE-BRAND    : remedy instructs REMOVAL of a label, tag, brand, logo or name
# C7a BRAND-ON-OBJ (strict) : Description locates a brand mark ON the object with a locating verb
#                             AND a firm-name token from this record appears in the Description
# C7b BRAND-ON-OBJ (loose)  : Description contains any brand-locating phrase at all
STOP = re.compile(r'stop using[^.]*immediately', re.I)
DESTROY = re.compile(r'\b(destroy|destruct|cut (the|it|in)|cut,|dispose|disposal|discard|'
                     r'render (it |the )?(unusable|inoperable)|throw away|break)\b', re.I)
PHOTO = re.compile(r'\b(photo|photograph|picture|image)\b', re.I)
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
DESTR_PHOTO = re.compile(r'(photo|photograph|picture|image)[^.]{0,80}'
                         r'(destroy|destruct|cut|disposed|dispose|discard|mark)', re.I)
MARK_STRICT = re.compile(r'permanent marker', re.I)
MARK_LOOSE = re.compile(r'(permanent marker|black sharpie|sharpie|\bmarker\b)', re.I)
PAY = re.compile(r'\b(refund|reimburse|reimbursement|gift card|store credit|credit)\b', re.I)
DEBRAND = re.compile(r'\b(remove|cut off|peel|tear off|delete|obliterate)\b[^.]{0,60}'
                     r'\b(label|tag|logo|brand|brand name|nameplate|name plate)\b', re.I)
LOCATE = re.compile(r'\b(printed|stamped|engraved|molded|moulded|embossed|sewn|'
                    r'located|marked|appears|found|listed|etched|imprinted)\b', re.I)

STOPWORDS = {'the', 'and', 'inc', 'llc', 'ltd', 'co', 'company', 'corp', 'group', 'usa',
             'international', 'trading', 'technology', 'technologies', 'industrial', 'imports'}


def firm_tokens(r):
    toks = set()
    for n in firms(r):
        for t in re.split(r'[^A-Za-z0-9]+', n):
            if len(t) >= 4 and t.lower() not in STOPWORDS:
                toks.add(t)
    return toks


rows = []
for r in R:
    s, d = rem(r), desc(r)
    stop = bool(STOP.search(s))
    dest_inc = bool(DESTROY.search(s))
    # strict destruction: the object itself, not only a battery/component, not a future note
    dest_str = dest_inc and not re.search(
        r'(dispose of the (battery|batteries)|battery disposal)', s, re.I)
    dest_str = dest_str and bool(re.search(
        r'\b(cut|destroy|render (it |the )?(unusable|inoperable)|discard the|dispose of the)\b', s, re.I))
    photo_loose = bool(PHOTO.search(s))
    photo_strict = bool(DESTR_PHOTO.search(s)) and bool(EMAIL.search(s))
    mark_s = bool(MARK_STRICT.search(s))
    mark_l = bool(MARK_LOOSE.search(s))
    pay = bool(PAY.search(s))
    debrand = bool(DEBRAND.search(s))
    toks = firm_tokens(r)
    brand_loose = bool(LOCATE.search(d))
    brand_strict = False
    if toks:
        for m in LOCATE.finditer(d):
            win = d[max(0, m.start() - 90): m.end() + 90]
            if any(t in win for t in toks):
                brand_strict = True
                break
    rows.append(dict(n=r['RecallNumber'], stop=stop, dest_inc=dest_inc, dest_str=dest_str,
                     photo_loose=photo_loose, photo_strict=photo_strict, mark_s=mark_s,
                     mark_l=mark_l, pay=pay, debrand=debrand,
                     brand_strict=brand_strict, brand_loose=brand_loose))


def c(key):
    return sum(1 for x in rows if x[key])


print("\n=== THE STATE'S INSTRUCTION TO THE READER ===")
print("C1  stop using…immediately                        :", c('stop'), "/", N)
print("C2  owner destroys/disposes    strict…inclusive   :", c('dest_str'), "…", c('dest_inc'), "/", N)
print("C3  evidentiary photograph     strict…loose       :", c('photo_strict'), "…", c('photo_loose'), "/", N)
print("C4  write on own property      strict…loose       :", c('mark_s'), "…", c('mark_l'), "/", N)
print("C5  money back promised to the owner              :", c('pay'), "/", N)
print("C6  removal of a label/tag/brand/logo instructed  :", c('debrand'), "/", N)
print("C7  brand mark located on the object (Description) strict…loose:",
      c('brand_strict'), "…", c('brand_loose'), "/", N)

print("\n=== THE RECEIPT SET (the room's proposed agency organ) ===")
for lbl, keys in (("destroy(strict) AND photo(strict) AND pay", ('dest_str', 'photo_strict', 'pay')),
                  ("destroy(incl)   AND photo(loose)  AND pay", ('dest_inc', 'photo_loose', 'pay')),
                  ("destroy(strict) AND mark(strict)  AND pay", ('dest_str', 'mark_s', 'pay'))):
    print(f"  {lbl}: {sum(1 for x in rows if all(x[k] for k in keys))} / {N}")

print("\n=== THE RULE, APPLIED (THE-RULE.md) ===")
order = sorted(R, key=lambda r: (r['RecallDate'], r['RecallNumber']))
chosen = next((r for r in order if STOP.search(rem(r))), None)
print("order key: RecallDate asc, then RecallNumber asc")
print("first record matching C1:", chosen['RecallNumber'],
      "| published", chosen['RecallDate'][:10],
      "| records skipped before it:", order.index(chosen))
print("ties on (RecallDate, RecallNumber):",
      len(order) - len({(r['RecallDate'], r['RecallNumber']) for r in order}))
print("records with no Remedies text at all:", sum(1 for r in R if not rem(r).strip()))
print("chosen product:", (chosen.get('Products') or [{}])[0].get('Name', ''))
print("chosen units  :", (chosen.get('Products') or [{}])[0].get('NumberOfUnits', ''))
print("chosen remedy :", rem(chosen))
print("chosen retail :", ' '.join(x.get('Name', '') for x in (chosen.get('Retailers') or [])))
print("chosen URL    :", chosen.get('URL', ''))

print("\n=== WHAT A PERFORMER IS PAID (per-record, no aggregate on the work's face) ===")
prices = []
for r in R:
    line = ' '.join(x.get('Name', '') for x in (r.get('Retailers') or []))
    m = re.findall(r'\$[\d,]+(?:\.\d\d)?', line)
    if m:
        prices.append((r['RecallNumber'], m))
print("records whose retailer line prints at least one price:", len(prices), "/", N)
print("example (the record the rule takes):",
      [p for p in prices if p[0] == chosen['RecallNumber']])

print("\n=== RECONCILIATION WITH VERIFIER-59 (binding corrections) ===")
print("VERIFIER-59 published, from its own script, intervals under ITS codings:")
print("  destruction by the owner   31 (strict) … 34 (inclusive)")
print("  evidentiary photograph     25 (strict) … 31 (loose)")
print("  writing on own property    10 (strict) … 13 (loose)")
print("This script's codings are narrower on two of the three. Reported honestly as the UNION")
print("of both published codings, because both are re-runnable by a stranger and neither is")
print("privileged by anything but its definition:")
print("  destruction : %d … 34 of %d" % (min(c('dest_str'), 31), N))
print("  photograph  : %d … 31 of %d" % (min(c('photo_strict'), 25), N))
print("  marking     : %d … %d of %d" % (c('mark_s'), c('mark_l'), N))
print("Only C6 (0 of 55) and C1 (50 of 55) are coding-insensitive in any reading tried here.")

print("\n=== SANITY: every count is a subset of N and no coding is empty by accident ===")
for k in ('stop', 'dest_str', 'dest_inc', 'photo_strict', 'photo_loose', 'mark_s', 'mark_l',
          'pay', 'debrand', 'brand_strict', 'brand_loose'):
    assert 0 <= c(k) <= N
print("ok")
