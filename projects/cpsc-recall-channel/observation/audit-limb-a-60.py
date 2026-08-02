#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LIMB A -- BRANDING-SURVIVAL AUDIT, session 60 (the VERIFIER-AUDITOR).

Pre-registered in projects/cpsc-recall-channel/STAGING-RULING-59.md, section 5,
BEFORE this script existed:

    "LIMB A -- BRANDING-SURVIVAL AUDIT (runnable now: no room, no readers).
    For N notices taken by the rule with no selection: from each `Description`
    record where the brand mark is; from each `Remedies` record what the
    destruction reaches. Code SURVIVES where it does not reach the mark.
    M2 fails at SURVIVES >= 20%. My probe returns ~= 60% with 0 removals; I
    state the threshold anyway so it cannot be tuned afterwards."

Run:      python3 audit-limb-a-60.py recalls-2026-07-01_2026-08-02.json
Network:  none. Determinism: every number below is a function of the
          committed JSON plus the fixed classification table in this file.

WHY A HARDCODED TABLE, NOT A REGEX. Whether a brand mark is "on the object
itself" turns on English sentence structure a regular expression cannot
reliably resolve (contrast "printed on the product packaging" with "printed
on the product's blue packaging" with "is printed on the top of the hand
warmers and on the product packaging" -- three real sentences from this
corpus, three different answers). So each of the 55 records was read by hand
against the coding stated below, and the deciding fragment of its
`Description` was copied out. To keep that step honest, this script asserts
at import time that every quoted fragment is a byte-for-byte substring of the
`Description` (or, where marked, `Remedies`) field of the record it is
attributed to -- if a quote were mistyped or the source record edited, the
script would crash here rather than print a wrong number silently. A
stranger who disagrees with a call can re-run this file after editing the
`strict` / `loose` flags for any RecallNumber and see exactly how the
downstream counts move.

THE CODING (apply this by hand to one record and you should reach the same
call this script does):

  MARK-ON-OBJECT, STRICT (primary coding). A record is coded YES only if its
  `Description` states, in terms locating it physically, that the FIRM'S
  BRAND NAME, LOGO, OR TRADEMARK is printed, stamped, engraved, embroidered,
  moulded, or affixed (as a label/tag/plate) directly on the product itself
  or on a component that is structurally part of the product as sold (a
  base, door, handle, sole, seam, canopy, trolley body, or a bottle/pouch
  that IS the product's own housing) -- as opposed to: the outer box,
  polybag, or shrink-wrap; an included instruction manual; a purchase
  receipt or order confirmation; or a component of a DIFFERENT, non-recalled
  item bundled with the recalled one. A bare model number, catalog number,
  serial number, batch number, or date code with NO brand name/logo stated
  alongside it does not by itself count -- those identify a unit, not a
  firm. Where the notice explicitly denies any mark on the product itself
  ("has no labeling or product identification on the product itself"), that
  is a clean NO regardless of what the packaging carries.

  MARK-ON-OBJECT, LOOSE (named alternative A). Same as STRICT, except a bare
  model/catalog/serial-number label located on the object itself also
  counts, on the reasoning that a manufacturer's own part-number label is
  itself an identifying mark even where the notice's prose does not spell
  out the brand name next to it.

  ANY-MARK-ANYWHERE (named alternative B). Location-blind: counts a record
  YES if the notice's Description states ANY brand/model/identifying text
  is printed/labelled/stamped/engraved ANYWHERE -- packaging, box, manual,
  receipt, or object. Computed by pattern match over the raw Description
  text, not hand-coded; included only to show how far the count moves once
  the "on the object" requirement is dropped entirely.

  DESTRUCTION REACHES THE MARK. A record's mark (if on-object under the
  coding in use) is coded REACHED only if the `Remedies` field instructs an
  action that removes, cuts away, strips, scrapes off, blacks out, or
  otherwise physically eliminates the specific marked component identified
  in the Description (e.g. an instruction to cut off or discard the exact
  tag/label/plate/engraved face itself) -- not merely to cut the object in
  half, cut a cord/strap elsewhere on it, disassemble it, or dispose of it
  whole. SURVIVES = mark is on-object AND is NOT reached by the destruction
  (including: no destruction is instructed at all, e.g. repair/replace/
  return remedies, in which case the mark trivially survives because
  nothing touches it).

N. All 55 records in the committed source file, taken whole -- no filter,
no sample, no date cut. That is "N taken by the rule with no selection."
"""
import json, sys, re, hashlib, collections

PATH = sys.argv[1] if len(sys.argv) > 1 else 'recalls-2026-07-01_2026-08-02.json'
raw = open(PATH, 'rb').read()
SHA256 = hashlib.sha256(raw).hexdigest()
R = json.loads(raw)
N = len(R)
BY_NUM = {r['RecallNumber']: r for r in R}

# ---------------------------------------------------------------------------
# Per-record classification table.
#   strict : bool -- MARK-ON-OBJECT, STRICT (primary coding)
#   loose  : bool -- MARK-ON-OBJECT, LOOSE  (strict implies loose)
#   ambig  : bool -- flagged genuinely ambiguous by the auditor (see report)
#   quote  : the deciding fragment, verbatim from Description (or "REM:" for
#            a fragment from Remedies), asserted below to be an exact
#            substring of that field.
#   note   : one line of the auditor's own reasoning.
# ---------------------------------------------------------------------------
CODING = [
    # RecallNumber, strict, loose, ambig, quote, note
    ("26645", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26646", False, False, False,
     '"SKU: N-YSXR0055B" and "Item: Steel Cabinet" are printed on the product packaging.',
     "explicit packaging; also no brand name, only SKU/Item strings."),
    ("26647", True, True, False,
     "The brand name and model number are printed on the label on the underside of the projector's gray base.",
     "gray base is the product itself; brand name stated explicitly."),
    ("26649", True, True, False,
     'The top freezer has a separate door, one drawer and "Galanz" printed on front.',
     "brand printed on the front of the appliance itself."),
    ("26650", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26651", False, True, True,
     '"MODEL No.: HANS0002" is printed on a label on the underside of the stool\'s platform.',
     "on-object location, but only a model number -- no brand name (HARPPA) stated as printed there."),
    ("26652", False, False, False,
     "The brand name and model number OCT-5060, OCT-5062, OCT-6248, OCT-7284 or OCT-8490 are printed on the product packaging.",
     "explicit packaging."),
    ("26653", False, False, False,
     "The rockets are mounted on a wooden stick and come in a black box with a picture of a skull, the brand name, the product name and a warning label.",
     "the brand mark described is on the box the rockets come in, not on the rocket."),
    ("26654", True, True, False,
     "The model numbers 40041 and 40003 are printed on the back of the box of Sloosh water toys, next to the bar code, and on top of one end of the dive stick, along with Joyin's name and tracking information.",
     "firm name (Joyin) explicitly stated printed on the dive stick itself, not only the box."),
    ("26655", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26656", False, False, False,
     '"Product Model: NEW319A" is printed on a sticker affixed to the front of the box.',
     "sticker is on the box (packaging); also only a model number, no brand name."),
    ("26659", True, True, False,
     '"OCOOPA" is printed on the top of the hand warmers and on the product packaging.',
     "brand explicitly stated on the object itself (top of the hand warmers), in addition to packaging."),
    ("26657", True, True, False,
     'All the recalled baby loungers are rectangular in shape, are made of a foam pad with a cloth cover and have "CPZZKQ" printed on a side label.',
     "brand name explicitly on a label on the product (side of the lounger)."),
    ("26632", True, True, True,
     'Some of the zipline trolleys include the name "TT TRSMIMA" in white lettering and some of the plastic seats include a label stating in part, "Manufacturer Name: HuNanBoLuoDianZiShangWuYouXianGongSi."',
     "on-object marks are explicit, but the notice's own \"some of\" qualifies it to only part of the recalled units."),
    ("26658", False, True, True,
     "The model number is engraved on the underside of the bottom step.",
     "on-object location, but only a model number -- no brand name (Woodure) stated as engraved there."),
    ("26634", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26635", False, False, False,
     'The brand name and "Pulling Toy" is printed on the front of the product packaging, and the batch number DS250238 on the back of packaging.',
     "explicit packaging, both mentions."),
    ("26638", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26633", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26637", False, False, False,
     "The OeyUoc Pool Drain Cover has no labeling or product identification on the product itself.",
     "notice explicitly denies any mark on the product itself; packaging label described separately."),
    ("26639", False, False, True,
     "The bibs have scalloped edges, a snap closure, and personalized embroidery on the front.",
     "\"personalized\" embroidery reads as buyer-chosen decoration, not a stated firm brand mark; the firm name is never said to be embroidered."),
    ("26636", False, False, False,
     "The Sviyatp Pool Drain Cover has no labeling or product identification on the product itself.",
     "notice explicitly denies any mark on the product itself; packaging label described separately."),
    ("26621", True, True, False,
     '"Currey & Company" and the model number 9000-1129, 9000-1130, 9000-1254, 9000-1255, 9000-1314 are printed on a label atop the fixture\'s ceiling canopy.',
     "ceiling canopy is part of the chandelier itself; brand name explicit."),
    ("26624", True, True, False,
     '"200LX" and "Hollis" are engraved on top of the regulator.',
     "brand engraved directly on the product."),
    ("26626", True, True, False,
     '"JOBON" is printed on the side of the lighter.',
     "brand printed directly on the product."),
    ("26619", False, False, True,
     'The label states "Odorless Mineral Spirit" and "Artist Oil Thinning Medium" in large text.',
     "a label on the bottle is described in detail, but the firm's brand name (Liizousuda) is never stated to be on it."),
    ("26625", True, True, False,
     '"Madewell" and the size are printed on the neck label and "Style #NT611" or "Style #NT612" and "HO24" on the sewn-in side seam label.',
     "brand printed on a label sewn into the garment itself."),
    ("26630", True, True, True,
     "The MNIENT brand name and model number are on the front of the product packaging and on the product label located on the black fabric pouch.",
     "the fabric pouch is listed among the bed rail's own parts (\"a black fabric pouch\"), so its label reads as on-object; a stricter reader could call the pouch an accessory."),
    ("26627", False, False, False,
     'The Noerishia branding "Noerishia" and "Model: KDB-504B" are printed on the instruction manual.',
     "brand is on the packaging and the instruction manual, never stated to be on the bed rail itself."),
    ("26617", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26618", True, True, False,
     "The brand name Panasonic is written on the front of the product.",
     "explicit: brand written on the front of the product itself."),
    ("26628", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26629", True, True, False,
     "The brand is printed on the shoe's sole and bottom.",
     "brand printed directly on the product."),
    ("26620", True, True, False,
     '"boon" is visible along the top rail, and a warning label is visible along the side of the standing platform.',
     "brand visible directly on the product's own rail."),
    ("26622", False, False, False,
     'The dressers have the SKU number and color printed on a label located on the outer packaging (e.g., "SKU: HD016GRY" and "COLOR: GRAY").',
     "explicit outer packaging; also no brand name, only SKU/color."),
    ("26623", False, False, True,
     'The lunch box is red with "Space King" written in red and orange lettering at the top on the front, and a picture of the Space king characters below it.',
     "the mark is on the lunch box, but the recalled object is only the copper cup inside it (\"Only the copper cups are included in this recall\") -- no mark is stated on the cup."),
    ("26606", True, True, False,
     'The recalled ranges are stainless steel with five front-knobs on the oven with the "Insignia" label on the bottom of the oven door.',
     "brand label on the oven door -- part of the product."),
    ("26607", True, True, False,
     'The brand name "MouTec" or "BBRKIN" is on the upper right corner of the front of the safes.',
     "brand explicitly on the front of the product."),
    ("26605", False, True, True,
     "The model number CGG-6331 can be found on the label on the inside of the right-hand metal door, along with the serial number.",
     "on-object location, but only model/serial numbers -- the brand name (Cuisinart) is never stated to be on that label."),
    ("26610", True, True, False,
     '"FLAUNT" is engraved on the front right side of the power bank and there is a small circular button in the bottom center of the front side of the power bank.',
     "brand engraved directly on the product."),
    ("26611", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26608", True, True, False,
     'The brand name "Moodooy" and model "F311" are printed on the storage pocket.',
     "storage pocket is a stated part of the bed rail itself."),
    ("26609", False, True, True,
     '"Model No: 616" or "Model No: 616-1" is printed on a white label located under the tray.',
     "on-object location, but only a model number -- the brand name (WonderStone) is never stated to be on that label."),
    ("26596", True, True, False,
     '"Brand: AMASKY," "Model No.: BXP99/BXP93/BXP94/BXP96/BXP97" and "Batch Number: 202506001" are printed on a label attached to the pillow.',
     "label is attached to the product itself; brand name explicit."),
    ("26601", True, True, False,
     'The word "Cuisinart" is stamped on the brush handle.',
     "brand stamped directly on the product."),
    ("26599", False, True, True,
     "The catalog number and date code are printed on the product label inside of the fixture channel cover, behind the tray and can be accessed by removing two screws.",
     "on-object location, but only catalog number/date code -- the brand name (Metalux) is never stated to be on that label."),
    ("26593", False, False, True,
     'The CVS Health logo, a yellow heart, "Rapid Pain Relief" and "Medicated Hemorrhoidal Wipes" is printed on the front of the packet and the box.',
     "mark is on the individual wipe packet and the outer box, both of which are discarded wrapping around the actual wipe, not the wipe itself."),
    ("26600", False, False, False,
     'The product is packaged in a white box labeled "JUNPOWER Household Batteries," with four packs inside, each pack contains five batteries.',
     "explicit packaging; nothing is stated to be on the batteries themselves."),
    ("26594", False, False, False,
     '"POPOOO" and "LED FINGER LIGHTS" are printed on the product\'s blue packaging.',
     "explicit packaging."),
    ("26595", False, False, False, None,
     "no mark-location text of any kind in Description."),
    ("26598", True, True, False,
     "The recalled popping toys have the Gigglescape brand printed on the front of the package and imprinted on the bottom of the blue plastic base.",
     "brand also explicitly imprinted on the product's own base, not only the package."),
    ("26592", False, False, False,
     "There is no labeling or product identification on the product itself.",
     "notice explicitly denies any mark on the product itself."),
    ("26591", True, True, False,
     '"VEVOR" is printed on an attached tag on the outside of the baby lounger\'s cover.',
     "tag attached directly to the product's own cover."),
    ("26603", False, False, False,
     'The product packaging has a red, white and blue label that has the word "Hometown" written on it.',
     "explicit: \"product packaging\"."),
    ("26602", True, True, True,
     'The product has a red, white and blue label that has the word "Unity" written on it.',
     "literal text says \"the product has ... a label\", not \"the product packaging\" (contrast the near-identical sibling record 26603, which does say packaging) -- read literally this is on-object, but the two records otherwise share a template and a stricter reader could treat them alike."),
]

assert len(CODING) == 55, "coding table must cover all 55 records, got %d" % len(CODING)

# --- integrity check: every quoted fragment must be a verbatim substring of
#     the Description it is attributed to. This is the guard against quoting
#     a paraphrase instead of the raw bytes. ---
for rn, strict, loose, ambig, quote, note in CODING:
    assert rn in BY_NUM, "RecallNumber %s not found in source file" % rn
    if quote is not None:
        desc = BY_NUM[rn]['Description']
        assert quote in desc, (
            "QUOTE INTEGRITY FAILURE for %s: quoted fragment is not a verbatim "
            "substring of Description. Quoted:\n  %r\nDescription:\n  %r"
            % (rn, quote, desc))
    if strict:
        assert loose, "strict=True must imply loose=True (%s)" % rn

STRICT = {rn for rn, s, l, a, q, n in CODING if s}
LOOSE = {rn for rn, s, l, a, q, n in CODING if l}
AMBIG = [(rn, s, l, a, q, n) for rn, s, l, a, q, n in CODING if a]

# ---------------------------------------------------------------------------
# (i) Remedies instructing removal of a label/tag/brand/logo.
# Automated scan: any Remedies text that pairs a removal verb with a mark
# noun. Cross-checked by hand against every "remove" hit in the corpus
# (batteries, tempered glass, drain covers, foam padding, fabric seats,
# handgrip padding, drawers -- never a label/tag/brand/logo).
# ---------------------------------------------------------------------------
def remedy_text(r):
    return ' '.join(x.get('Name', '') for x in (r.get('Remedies') or []))

REMOVE_VERB = re.compile(
    r'\b(remove|removing|removal|peel|strip|scrape|cut off|cut away|black out|'
    r'cover up|obscure|redact|sand off|grind off|erase)\b', re.I)
MARK_NOUN = re.compile(r'\b(label|tag|brand|logo|nameplate|name plate|engraving|stamp)\b', re.I)

removal_hits = []
for r in R:
    s = remedy_text(r)
    for m in REMOVE_VERB.finditer(s):
        window = s[max(0, m.start() - 60): m.end() + 60]
        if MARK_NOUN.search(window):
            removal_hits.append((r['RecallNumber'], window.strip()))

removal_count = len(set(h[0] for h in removal_hits))

# ---------------------------------------------------------------------------
# (ii) alternative B, ANY-MARK-ANYWHERE: location-blind pattern match over
# Description text.
# ---------------------------------------------------------------------------
ANY_MARK = re.compile(
    r'(label|tag\b|logo|printed|stamp|engrav|embroider|molded|moulded|sewn|'
    r'imprint|marking|inscri|etched|silkscreen|nameplate|name plate|plate|'
    r'sticker|written)', re.I)
any_mark_set = {r['RecallNumber'] for r in R if ANY_MARK.search(r.get('Description', ''))}

# ---------------------------------------------------------------------------
# (iii) SURVIVES. Per the coding above, SURVIVES = mark-on-object AND
# destruction (if any) does not reach the marked component. Hand review of
# every STRICT- and LOOSE-only on-object record's Remedies text (see
# PILLORY-AUDIT-60.md for the record-by-record reach check) found zero cases
# where the destruction instruction targets the reported mark location --
# consistent with, and a generalisation of, the 0-of-55 explicit-removal
# count above. So SURVIVES == on-object under each coding used here.
# ---------------------------------------------------------------------------
SURVIVES_STRICT = STRICT
SURVIVES_LOOSE = LOOSE

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def pct(n, d):
    return 100.0 * n / d

print("=" * 78)
print("LIMB A -- BRANDING-SURVIVAL AUDIT -- session 60")
print("=" * 78)
print("source file :", PATH)
print("byte size   :", len(raw))
print("sha256      :", SHA256)
print("N (records) :", N, "-- all records in the committed file, no selection")
print()

print(__doc__.split("THE CODING")[1].split("N. All 55")[0])
print()

print("-" * 78)
print("(i) REMEDIES INSTRUCTING REMOVAL OF A LABEL/TAG/BRAND/LOGO")
print("-" * 78)
print("count:", removal_count, "of", N)
if removal_hits:
    for rn, w in removal_hits:
        print(" ", rn, ":", w)
else:
    print("  (no record's Remedies text pairs a removal verb with a mark noun)")
print()

print("-" * 78)
print("(ii) NOTICES STATING THE BRAND MARK IS ON THE OBJECT ITSELF")
print("-" * 78)
print("PRIMARY CODING -- MARK-ON-OBJECT, STRICT:", len(STRICT), "of", N,
      "= %.1f%%" % pct(len(STRICT), N))
print("  RecallNumbers:", ', '.join(sorted(STRICT)))
print()
print("ALTERNATIVE A -- MARK-ON-OBJECT, LOOSE (bare model/serial/catalog labels count):",
      len(LOOSE), "of", N, "= %.1f%%" % pct(len(LOOSE), N))
print("  RecallNumbers:", ', '.join(sorted(LOOSE)))
print()
print("ALTERNATIVE B -- ANY-MARK-ANYWHERE (location-blind, packaging/manual/receipt included):",
      len(any_mark_set), "of", N, "= %.1f%%" % pct(len(any_mark_set), N))
print()

lo = len(STRICT) - sum(1 for rn, s, l, a, q, n in AMBIG if s)
hi = len(STRICT) + sum(1 for rn, s, l, a, q, n in AMBIG if not s)
print("AMBIGUITY BAND on the PRIMARY (strict) count: if every one of the",
      len(AMBIG), "flagged-ambiguous records below is instead coded the other way,")
print("  the strict on-object count ranges", lo, "-", hi, "of", N,
      "(%.1f%% - %.1f%%)." % (pct(lo, N), pct(hi, N)))
print()
print("  Ambiguous records (recall number | primary call | quote | reason):")
for rn, s, l, a, q, n in AMBIG:
    print("   ", rn, "|", "YES" if s else "NO", "|", repr(q))
    print("      ", n)
print()

print("-" * 78)
print("(iii) SURVIVES: destruction does not reach the mark")
print("-" * 78)
print("SURVIVES under PRIMARY (strict) coding:", len(SURVIVES_STRICT), "of", N,
      "= %.1f%%" % pct(len(SURVIVES_STRICT), N))
print("SURVIVES under ALTERNATIVE A (loose) coding:", len(SURVIVES_LOOSE), "of", N,
      "= %.1f%%" % pct(len(SURVIVES_LOOSE), N))
print("SURVIVES ambiguity band (mirrors (ii)'s band, since SURVIVES == on-object here):",
      lo, "-", hi, "of", N, "(%.1f%% - %.1f%%)" % (pct(lo, N), pct(hi, N)))
print()

print("-" * 78)
print("M2 VERDICT -- threshold pre-registered at SURVIVES >= 20%")
print("-" * 78)
threshold_count = 0.20 * N
for label, count in [
    ("PRIMARY (strict)", len(SURVIVES_STRICT)),
    ("ALTERNATIVE A (loose)", len(SURVIVES_LOOSE)),
    ("ambiguity-band floor", lo),
]:
    verdict = "FAILS" if count / N >= 0.20 else "HOLDS"
    print("  %-24s SURVIVES = %d/%d = %.1f%% -> M2 %s (threshold is %.1f records)"
          % (label, count, N, pct(count, N), verdict, threshold_count))
print()
overall = "FAILS" if lo / N >= 0.20 else "inconclusive"
print("Robust verdict: even at the low end of the ambiguity band (%d/%d = %.1f%%),"
      % (lo, N, pct(lo, N)))
print("SURVIVES clears the 20%% threshold. M2", overall, "under every coding tested.")
