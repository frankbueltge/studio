#!/usr/bin/env python3
"""
Independent verification script for ARTIST-REFORM-59.md.
Written from scratch by the Verifier, from the motion's own stated definitions,
WITHOUT reading observation/analyse.py's implementation choices.
Run: python3 verify59.py recalls-2026-07-01_2026-08-02.json
"""
import json, sys, re, hashlib

path = sys.argv[1]
raw = open(path, 'rb').read()
print("sha256:", hashlib.sha256(raw).hexdigest())
R = json.loads(raw)
N = len(R)
print("records:", N)

def field_text(r, key):
    """Join the 'Name' values of a list-of-dict field into one string."""
    return ' '.join(x.get('Name', '') for x in (r.get(key) or []))

remedies = [field_text(r, 'Remedies') for r in R]
injuries = [field_text(r, 'Injuries') for r in R]
retailers = [field_text(r, 'Retailers') for r in R]

# --- SS1: begins "Consumers should..." ---
begins = sum(1 for s in remedies if s.strip().startswith('Consumers should'))
print("\n[1] begins 'Consumers should...':", begins, "/", N)

# --- SS2: contains "stop using ... immediately" ---
# Reading A (motion's own §6 regex, same clause/sentence, no period between):
patA = re.compile(r'stop using[^.]*immediately', re.I)
readingA = sum(1 for s in remedies if patA.search(s))
# Reading B (looser: both words present anywhere in the remedy text, any order/distance):
readingB = sum(1 for s in remedies if re.search(r'stop using', s, re.I) and re.search(r'immediately', s, re.I))
print("[2] 'stop using ... immediately' -- reading A (motion's own regex, same sentence):", readingA, "/", N,
      "| reading B (both words present anywhere):", readingB, "/", N)

# --- SS3: instructs the OWNER to destroy/dispose of the object THEMSELVES ---
# Owner-performed destruction/disposal verbs, addressed to "consumers"/owner (not "return to store").
SELF_DESTROY = re.compile(
    r'\b(cut (the|it|them|in half)|cut,|destroy|discard|dispose of the|disposal of the|'
    r'break|render (it |the )?(unusable|inoperable)|remove the .* and cut|throw away)\b', re.I)
selfdestroy = sum(1 for s in remedies if SELF_DESTROY.search(s))
print("[3] owner instructed to destroy/dispose of the object themselves (my reading):", selfdestroy, "/", N)

# --- SS4: requires owner to photograph the destruction and email it ---
PHOTO_EMAIL = re.compile(r'(photo|photograph|picture|image).{0,120}?(email|e-mail|submit|send)', re.I)
PHOTO_EMAIL2 = re.compile(r'(email|e-mail|submit|send).{0,120}?(photo|photograph|picture|image)', re.I)
photo_email = sum(1 for s in remedies if PHOTO_EMAIL.search(s) or PHOTO_EMAIL2.search(s))
print("[4] requires photograph + email/submit of the destruction:", photo_email, "/", N)

# --- SS5: requires owner to first WRITE RECALL/RECALLED/DESTROYED in permanent marker ---
MARK = re.compile(r'permanent marker.{0,80}?(RECALL|RECALLED|DESTROYED)|(RECALL|RECALLED|DESTROYED).{0,80}?permanent marker', re.I)
mark = sum(1 for s in remedies if MARK.search(s))
print("[5] write RECALL/RECALLED/DESTROYED in permanent marker on own property:", mark, "/", N)

# --- SS6: reports no injury at all ---
none_reported = sum(1 for s in injuries if s.strip() == 'None reported')
print("[6] Injuries == 'None reported' exactly:", none_reported, "/", N)
none_reported_loose = sum(1 for s in injuries if 'none reported' in s.lower())
print("    (loose match 'none reported' anywhere):", none_reported_loose, "/", N)

# --- verbatim remedy quotes for records 26596, 26659, 26637 ---
print("\n--- verbatim remedies for cited records ---")
for rn in ('26596', '26659', '26637'):
    rec = next((r for r in R if r['RecallNumber'] == rn), None)
    if rec is None:
        print(rn, ": NOT FOUND IN CORPUS")
        continue
    print(rn, ":", repr(field_text(rec, 'Remedies')))

# --- SS2.2: closed selling window + price ---
closed = sum(1 for s in retailers if re.search(r'\bfrom .*through .*', s, re.I))
price = sum(1 for s in retailers if '$' in s)
both = sum(1 for s in retailers if re.search(r'\bfrom .*through .*', s, re.I) and '$' in s)
print("\n[2.2] retailer line w/ closed window:", closed, "| w/ price:", price, "| BOTH:", both, "/", N)

# --- SS2.3(c): 55/55 name a firm; 49/55 China country of manufacture ---
def firm_names(r):
    out = []
    for k in ('Manufacturers', 'Importers', 'Distributors'):
        out += [x.get('Name', '').strip() for x in (r.get(k) or []) if x.get('Name', '').strip()]
    return out

named_firm = sum(1 for r in R if firm_names(r))
print("[2.3c] records naming >=1 firm (mfr/importer/distributor):", named_firm, "/", N)

def mfg_countries(r):
    return [c.get('Country', '').strip() for c in (r.get('ManufacturerCountries') or []) if c.get('Country', '').strip()]

china_mfg = sum(1 for r in R if 'China' in mfg_countries(r))
print("[2.3c] records naming China as a country of manufacture:", china_mfg, "/", N)

# --- SS3.1: distinct firm strings, China-in-name, country tally, non-US, %, ", of China" endings ---
all_firms = set()
for r in R:
    all_firms.update(firm_names(r))
print("\n[3.1] distinct firm strings (mfr+importer+distributor):", len(all_firms))

china_in_name = sum(1 for n in all_firms if 'china' in n.lower())
print("[3.1] distinct firm strings containing 'China':", china_in_name)

of_china_exact = sum(1 for n in all_firms if n.endswith(', of China'))
print("[3.1] distinct firm strings ending exactly ', of China':", of_china_exact)

import collections
country_tally = collections.Counter()
no_country = 0
for r in R:
    cs = mfg_countries(r)
    if not cs:
        no_country += 1
    for c in cs:
        country_tally[c] += 1
print("[3.1] country-of-manufacture tally (by record, one entry assumed per record):", dict(country_tally),
      "| records with NO country listed:", no_country)

non_us = sum(1 for r in R if mfg_countries(r) and any(c != 'United States' for c in mfg_countries(r)))
print("[3.1] records naming a non-US country of manufacture:", non_us, "/", N,
      "=> %.1f%%" % (100.0 * non_us / N))
china_pct = 100.0 * china_mfg / N
print("[3.1] China %% of all records:", "%.1f%%" % china_pct)

print("\n[3.1] the exact quoted firm string check:")
target = "Changzhou Jiaxuan Intelligence Furniture Co., Ltd., of China"
print("  present verbatim among firm strings:", target in all_firms)

# --- SS6: the etude-selection rule ---
print("\n[6] etude selection rule")
order = sorted(R, key=lambda r: (r['RecallDate'], r['RecallNumber']))
patA = re.compile(r'stop using[^.]*immediately', re.I)
skipped = 0
chosen = None
for r in order:
    if patA.search(field_text(r, 'Remedies')):
        chosen = r
        break
    skipped += 1
print("  chosen RecallNumber:", chosen['RecallNumber'], "| RecallDate:", chosen['RecallDate'],
      "| records skipped before it:", skipped)
print("  chosen record Injuries:", field_text(chosen, 'Injuries'))
print("  chosen record Products[0]:", (chosen.get('Products') or [{}])[0])
print("  chosen record Retailers:", field_text(chosen, 'Retailers'))
print("  chosen record Remedies (verbatim):", repr(field_text(chosen, 'Remedies')))
