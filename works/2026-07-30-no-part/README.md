# NO PART

A print-and-instruction work. The page at `index.html` is the score and the
stock, not documentation of either — it publishes `projects/no-part/INSTRUCTION.md`
complete and verbatim (title, epigraph, all twenty numbered items, the `---`
rule, the closing paragraph), plus a render of the source document at two
scales and three of its thirty-nine printed sheets at native resolution. No
wall has been built. The instruction is the whole of the studio's authorship;
every glyph the visitor can actually read on any sheet is the Court's, rendered
as an image, never retyped.

## Assets, provenance

Four PNGs are inlined as base64 `data:` URIs, read and encoded byte-for-byte
with no re-compression, resampling, cropping or metadata stripping:

| asset | source path | pixels | sha256 |
|---|---|---|---|
| the strip | `projects/no-part/line-strip.png` | 8424 × 280 | `cd6e8af32b614f3a97ce03bb41c4960bf09ca4d1f074d1429e0ba63293ea35a3` |
| sheet 32 | `projects/no-part/render/sheet-32.png` | 864 × 1118 | `bb8f34c012bff2df6997325d44333896f9620fb4edbf48ac19b402a6d012ef5a` |
| sheet 33 | `projects/no-part/render/sheet-33.png` | 864 × 1118 | `997dcd784631262efe3eef562d7b41e2f21e3f7895cc99ff04b41b2a2adc0283` |
| sheet 34 | `projects/no-part/render/sheet-34.png` | 864 × 1118 | `317c59bd7a86710ff0ad6983b155a36c08d4047c287f7d700e1eb6a68e78b28b` |

Each hash was verified by decoding the embedded `data:` URI back to bytes and
comparing sha256 against the source file — all four match exactly. The strip's
~1 MB payload is embedded exactly once, as a CSS custom property
(`--strip-url`) referenced by two different elements (the reduced full-bleed
plate and the native pannable plate), so it is never duplicated in the file.

The document itself — `ORDER LIST: 607 U.S.`, the Supreme Court's order list
for Monday, 6 October 2025, 39 pages — lives at `projects/no-part/order-list.pdf`,
sha256 `354c9ba8dbc6e5104a6a6b84ee53a91a6f8e5e87b2d900e8c26f4a67ef6ec652`,
228,850 bytes. It is a work of the United States Government and carries no
copyright, which is why this page can reproduce it entire.

## No script, no network

`index.html` contains zero `<script>` tags, zero inline `style=` attributes,
zero inline event handlers, and zero `<a href>` links — every URL on the page
is printed as plain text. All styling lives in one `<style>` block scoped
under a single wrapping container class. The only interaction is native
scrolling; five elements (two renders of the strip, three sheet renders) are
individually `overflow-x:auto` so the page body itself never scrolls
horizontally. Nothing on the page makes any external request of any kind.

## Size

Shipped `index.html` is 1,961,328 bytes (~1.87 MB), against a guideline
ceiling of 2.2 MB. No `data.json`, no subdirectories, no loose `.png` files
ship alongside it — the site integrator only copies top-level files, and
raster assets do not travel unless inlined.

## The full record

`projects/no-part/` carries the complete working record this page draws
from and does not restate: `STAGING-NOTES.md`, the render log, the three
severed-reader preregistrations and session logs (`READS-SESSION-47/48/49.md`,
`READS-PREREGISTRATION*.md`), and `CORRECTION-2026-07-30.md`, which documents
the four sessions in which the "What we counted" petition count was published
wrong and how it was corrected.
