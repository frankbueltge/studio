# Toolchain — the workshop's pinned starter

Provenance: added by the architect (Frank Bültge), 2026-07-21, with the workshop amendment
(PROTOCOL.md "The workshop", SITE-API.md "Built works"). This directory never travels to the
site; it exists so a build workspace starts from house-compatible defaults instead of being
re-invented per project.

## Usage

```bash
cp -R toolchain/template projects/<slug>/src
cd projects/<slug>/src
npm install        # first time: resolves and writes package-lock.json — COMMIT the lockfile
npm ci             # every later time: reproduces exactly from the lockfile
npm run build      # emits the built work to the PROJECT'S TOP LEVEL (../index.html, ../bundle.js, …)
npm run dev        # local dev server while composing
```

Add libraries as regular `dependencies` (`npm install three d3 …`) — the lockfile pins them.
Permissive licenses only (MIT/BSD/ISC/Apache-2.0/public domain); list every dependency and
its license in the work's README (SITE-API "Built works", licenses law).

## Why the template is configured the way it is

- **Fixed output names, no content hashes** (`bundle.js`, `[name][extname]`): deterministic,
  diffable builds — same source, same bytes; git is the archive.
- **`assetsInlineLimit` effectively infinite:** only `.html .js .mjs .css .json .svg` travel
  to the site; raster images, fonts and audio must ship inline as `data:` URIs, so the
  bundler inlines everything by default.
- **`cssCodeSplit: false`:** one stylesheet, predictable name.
- **`emptyOutDir: false`:** the build emits INTO the project's top level and must never wipe
  it — `data.json`, `README.md` and `meta.json` live there.
- **`base: './'`:** works are served from a subpath (`/studio/werke-html/<slug>/`); all
  references must stay relative.
- **The data island stays the law:** keep the `<script type="application/json">` island in
  `index.html` byte-identical to the committed `../data.json` — the Verifier checks it, the
  site CSP forbids fetching it at runtime.
- **Runtime is offline:** no external requests, ever — the works CSP blocks them anyway.
  Everything a work needs ships in its committed files.
- **Seeded generation:** same seed, same work; print the seed on the work's face
  (`main.js` carries the house RNG as a starting point).
