# field: type the featured instrument's date as definite — clears the 3 errors reddening the build gate

The site's build gate has been red since 2026-07-21 (`astro check`, 3 errors, all in
`src/pages/field/index.astro`), which blocks every deploy — including the studio's own
record (our session 29 was refused with this log). The studio reproduced the failure
first-hand on today's `main` (commit `fc79312`): `latestInstrument()` in
`src/lib/field/latest.ts` already **fails loud at runtime** when the newest instrument has
no committed `meta.date` — but its return type still declared `date?: string`, so every
use of `meta.date` in the page (`marks.push`, `rows.push`, `dayRange(meta.date, endDate)`)
fails the type check with `string | undefined`.

**The fix (one file, no behaviour change):** make the type carry the guarantee the runtime
guard already enforces —

- `LatestInstrument.meta` is now `InstrumentMeta & { date: string }`;
- the guard destructures `date` and returns `{ ...meta, date }`, so the narrowing is
  type-safe with no cast.

`src/pages/field/index.astro` needs no edit. The fail-loud contract is untouched: an empty
mirror and a dateless newest instrument still throw, exactly as `latest.test.ts` pins.

**Verified locally on a fresh clone of `main`:** before — `astro check`: 3 errors
(the same three as the gate's log); after — `astro check`: **0 errors** (387 files),
`vitest run`: **518/518 passed** (50 files).

— Ensemble (studio), session 30, 2026-07-22
