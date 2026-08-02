#!/usr/bin/env python3
"""Every number printed in ARTIST-REFORM-59.md comes from this script.
Run: python3 analyse.py recalls-2026-07-01_2026-08-02.json
Reproducible by a stranger: the input file's sha256 is
cf45ebec3c0748cf644c1cf7da5fc99e2ebb00f477434dac0a0eeb09e4784da1
and it is the raw body of
https://www.saferproducts.gov/RestWebServices/Recall?format=json&RecallDateStart=2026-07-01&RecallDateEnd=2026-08-02
"""
import json, sys, re, collections

path = sys.argv[1] if len(sys.argv) > 1 else 'recalls-2026-07-01_2026-08-02.json'
R = json.load(open(path))
print("records:", len(R))

# dates
by_date = collections.Counter(r['RecallDate'][:10] for r in R)
print("dates:", sorted(by_date.items()))
print("distinct dates:", len(by_date))

# images
imgs = [len(r.get('Images') or []) for r in R]
print("images total:", sum(imgs), "mean %.2f" % (sum(imgs)/len(R)), "min", min(imgs), "max", max(imgs),
      "records with 0 images:", sum(1 for i in imgs if i==0))

# manufacturers / countries
def names(r, k): return [x.get('Name','') for x in (r.get(k) or [])]
mc = collections.Counter()
none_country = 0
for r in R:
    cs = [c.get('Country') for c in (r.get('ManufacturerCountries') or [])]
    if not cs: none_country += 1
    for c in cs: mc[c] += 1
print("ManufacturerCountries counter:", mc.most_common())
print("records with NO ManufacturerCountries:", none_country)

foreign = [r for r in R if any((c.get('Country') or '') not in ('United States','USA','US','') for c in (r.get('ManufacturerCountries') or []))]
print("records naming a non-US manufacturing country:", len(foreign), "of", len(R))

# how many records name a manufacturer firm at all, and how many of those strings end 'of China' etc
mf_named = [r for r in R if names(r,'Manufacturers')]
print("records with a named Manufacturer entity:", len(mf_named))
imp_named = [r for r in R if names(r,'Importers')]
print("records with a named Importer entity:", len(imp_named))
of_country = collections.Counter()
for r in R:
    for n in names(r,'Manufacturers') + names(r,'Importers'):
        m = re.search(r',\s*of\s+([A-Za-z ]+?)\s*$', n.strip())
        if m: of_country[m.group(1)] += 1
print("firm strings ending ', of <Country>':", of_country.most_common())

# distinct firm names across manufacturers+importers
firms = set()
for r in R:
    for n in names(r,'Manufacturers') + names(r,'Importers'):
        firms.add(n.strip())
print("distinct manufacturer+importer strings:", len(firms))

# retailers / amazon
ret = [' '.join(names(r,'Retailers')) for r in R]
print("records naming a retailer line:", sum(1 for s in ret if s.strip()))
print("records whose retailer line mentions Amazon:", sum(1 for s in ret if 'amazon' in s.lower()))
print("records whose retailer line mentions Online:", sum(1 for s in ret if 'online' in s.lower()))

# injuries
inj = [' | '.join(names(r,'Injuries')) for r in R]
print("records with Injuries == 'None reported':", sum(1 for s in inj if s.strip()=='None reported'))

# remedies: stop using immediately
rem = [' '.join(names(r,'Remedies')) for r in R]
print("records whose Remedies begin 'Consumers should':", sum(1 for s in rem if s.strip().startswith('Consumers should')))
print("records containing 'stop using':", sum(1 for s in rem if 'stop using' in s.lower()))
print("records containing 'immediately':", sum(1 for s in rem if 'immediately' in s.lower()))
pat = re.compile(r'stop using[^.]*immediately', re.I)
print("records matching /stop using[^.]*immediately/:", sum(1 for s in rem if pat.search(s)))
print("records whose remedy also says contact:", sum(1 for s in rem if re.search(r'\bcontact\b', s, re.I)))
print("records whose remedy names refund/replacement/repair:",
      sum(1 for s in rem if re.search(r'refund|replace|repair', s, re.I)))

# units
u = [' | '.join(p.get('NumberOfUnits','') for p in (r.get('Products') or [])) for r in R]
print("records with a units string:", sum(1 for s in u if s.strip()))

# closed selling window + price in retailer line
closed = sum(1 for s in ret if re.search(r'\bfrom .*through .*', s, re.I))
price  = sum(1 for s in ret if '$' in s)
print("retailer line with 'from ... through ...':", closed, " with a price:", price,
      " both:", sum(1 for s in ret if re.search(r'\bfrom .*through .*', s, re.I) and '$' in s))

# candidate selection for the etude, stated rule applied below
print("\n--- ORDERED (RecallDate asc, RecallNumber asc) ---")
order = sorted(R, key=lambda r: (r['RecallDate'], r['RecallNumber']))
for r in order[:8]:
    rem0 = ' '.join(names(r,'Remedies'))
    print(r['RecallDate'][:10], r['RecallNumber'], '|imgs', len(r.get('Images') or []),
          '|match', bool(pat.search(rem0)), '|', (r.get('Products') or [{}])[0].get('Name','')[:60])

print("\n--- FIRST IN SOURCE ORDER WHOSE REMEDY MATCHES /stop using[^.]*immediately/ ---")
for r in order:
    rem0 = ' '.join(names(r,'Remedies'))
    if pat.search(rem0):
        print(json.dumps(r, indent=1))
        break

print("\n=== REMEDY GRAMMAR: destruction and proof ===")
DESTROY = re.compile(r'\b(destroy|destruct|cut (the|it|in)|cut,|dispose|disposal|discard|render (it |the )?(unusable|inoperable)|throw away|break)\b', re.I)
PROOF   = re.compile(r'\b(photo|photograph|picture|image)\b', re.I)
d = p = both = 0
for r in R:
    s = ' '.join(x.get('Name','') for x in (r.get('Remedies') or []))
    hd, hp = bool(DESTROY.search(s)), bool(PROOF.search(s))
    d += hd; p += hp; both += (hd and hp)
print("remedies instructing destruction/disposal by the consumer:", d, "of", len(R))
print("remedies requiring a photograph as proof:", p, "of", len(R))
print("remedies requiring BOTH destruction and photographic proof:", both, "of", len(R))
print("\n--- the both-cases, verbatim ---")
for r in R:
    s = ' '.join(x.get('Name','') for x in (r.get('Remedies') or []))
    if DESTROY.search(s) and PROOF.search(s):
        print(r['RecallNumber'], '|', (r.get('Products') or [{}])[0].get('Name','')[:45], '::', s[:300].replace('\n',' '))
        print()
