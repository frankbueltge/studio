// Builder — Ensemble, still-v3 (CONCEPT)
//
// The order text for the 31-entry tail (indices 761-791, 0-based, in
// entries.json's CERTIORARI DENIED section) is NOT present in
// ../corpus/entries.json — that file carries only docket + caption for all
// 792 entries. This still needs the order prose printed under 24-948,
// 24-998, 24-1151, 24-7126/24-7140, 24-7206, 24-7233 and 24-7281 (the still's
// crop ends mid-sentence inside 24-7281's paragraph; entries after it are
// not needed for this render and are not transcribed here).
//
// Source: the source PDF (SHA-256 354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652,
// https://www.supremecourt.gov/orders/courtorders/100625zor_5368.pdf), run through
// ../corpus/extract.py. The extractor's raw output for this stretch is preserved
// in the session scratchpad; see README.md "The tail text" for exactly how it
// was cleaned to reach the strings below.
//
// Cleaning applied (declared, not silent): the extractor breaks each PDF
// text-showing operator onto its own output line, which routinely lands
// mid-word (e.g. "in forma" / " pauperis" as two lines because the source
// PDF italicises "in forma pauperis" as a separate run), and it interleaves
// page-number footers ("32", "33"...) and internal object markers
// ("%%% obj 67") at page boundaries because those are artifacts of the
// extractor's page/object bookkeeping, not document text. Those two kinds of
// line breaks were closed up with a single space and the footer/marker lines
// were dropped; no word, character, or punctuation mark of the actual order
// text was added, removed, or reworded. Every string below was re-checked
// character by character against the extractor's raw output after cleaning.

module.exports = [
  {
    dockets: ['24-948'],
    caption: 'GUERRERO, CHIEF JUSTICE, ET AL. V. REDD, STEPHEN M.',
    order:
      "The motion to substitute Melissa Powe, authorized representative, as respondent in place of Stephen M. Redd, Deceased is granted. The petition for a writ of certiorari is denied.",
  },
  {
    dockets: ['24-998'],
    caption: 'BOYD, OFFICER, ET AL. V. WATSON, FRED',
    order:
      "The motion of respondent for leave to file a brief in opposition under seal with redacted copies for the public record is granted. The petition for a writ of certiorari is denied.",
  },
  {
    dockets: ['24-1151'],
    caption: 'BDO USA, LLP V. NEW ENGLAND CARPENTERS, ET AL.',
    order:
      "The petition for a writ of certiorari is denied. Justice Sotomayor took no part in the consideration or decision of this petition.",
  },
  {
    dockets: ['24-7126', '24-7140'],
    captions: {
      '24-7126': 'LETTIERI, DAVID C. V. USDC ND NY',
      '24-7140': 'LETTIERI, DAVID C. V. VILARDO, LAWRENCE J.',
    },
    order:
      "The motions of petitioner for leave to proceed in forma pauperis are denied, and the petitions for writs of certiorari are dismissed. See Rule 39.8.",
  },
  {
    dockets: ['24-7206'],
    caption: 'BOCHRA, MARK V. USDC ND IL',
    order:
      "The petition for a writ of certiorari is denied. The Chief Justice took no part in the consideration or decision of this petition.",
  },
  {
    dockets: ['24-7233'],
    caption: 'DANIELS, JOSEPH A. V. GORE, DOCTOR',
    order:
      "The motion of petitioner for leave to proceed in forma pauperis is denied, and the petition for a writ of certiorari is dismissed. See Rule 39.8.",
  },
  {
    dockets: ['24-7281'],
    caption: 'WATSON, LAWRENCE B. V. IFILL, PAMERSON',
    order:
      "The motion of petitioner for leave to proceed in forma pauperis is denied, and the petition for a writ of certiorari is dismissed. See Rule 39.8. As the petitioner has repeatedly abused this Court's process, the Clerk is directed not to accept any further petitions in noncriminal matters from petitioner unless the docketing fee required by Rule 38(a) is paid and the petition is submitted in compliance with Rule 33.1. See Martin v. District of Columbia Court of Appeals, 506 U. S. 1 (1992) (per curiam).",
  },
];
