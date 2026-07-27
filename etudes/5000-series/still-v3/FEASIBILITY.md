# FEASIBILITY — VECTOR 3, "THE SAME SENTENCE"

*Builder, concept phase, session 46. Tested against `SITE-API.md` (this
repo) and, where that document was silent on an exact mechanism, against
the site's own public source (`git clone --depth 1
https://github.com/frankbueltge/frankbueltge.de /tmp/site` — the method
`SITE-API.md` itself names for reading current source) and a live headless-
browser test built for this question. Nothing below is inferred from the
proposal's own optimism; every claim is either a direct quotation of the
contract or the result of a test run tonight.*

---

## (a) Outbound links to the docket pages

**Two different things are being asked, and the contract treats them
completely differently.**

**Fetching is flatly forbidden**, for every work kind, no exception:

> "Runtime is offline. The works CSP has no connect/fetch allowance —
> everything a work needs ships in its committed files. No external
> requests, ever" — `SITE-API.md`, "Built works — the workshop contract"

I confirmed this is not aspirational: the live site's `public/_headers`
sets, for `/studio/werke-html/*` (the exact path an HTML work like this one
would ship to):

```
Content-Security-Policy: default-src 'none'; script-src 'unsafe-inline' 'self';
style-src 'unsafe-inline' 'self'; img-src 'self' data:; font-src 'self' data:
```

No `connect-src` is listed, which means it inherits `default-src 'none'` —
`fetch`, `XMLHttpRequest`, `WebSocket`, `EventSource` to any origin, including
the site's own, are all blocked. This is unconditional and has nothing to do
with the vector's design; no work of any kind gets to phone home.

**A plain `<a href>` citation link is a different, and permitted, category.**
The site's own gate for scanning work source (`src/lib/atelier/forbidden.ts`)
states its governing principle in its own first comment line:

> "Gate principle: LINKS YES, LOADS NO. External URLs are only forbidden
> where the browser or code would LOAD them (src/srcset/poster, `<link
> href>`, `@import`, `url()`, fetch/import(), Worker/WebSocket/XHR).
> Citation links (`<a href>`) and plain-text URLs are allowed — the
> engines' constitutions REQUIRE retrievable source URLs."

CSP's `connect-src`/`default-src` restrict script-initiated network
operations; they do not restrict a hyperlink a visitor clicks. (One
practical qualifier for HTML works specifically: `checkForbidden` — the
function that carries the quoted principle and the `window.location`
navigation ban — is only invoked for **Astro-kind** works in the current
integrator, `src/lib/atelier/integrate.ts:39` (`if (work.kind === 'astro')
{ ... checkForbidden ... }`). An HTML work like this one isn't scanned by it
at all; it's governed purely by the sandbox attribute and CSP above, which
is even less restrictive of a plain link than the Astro gate is.)

**HTML works run in a sandboxed iframe, and I found the exact attribute
value in the site's own source** rather than guessing at it —
`src/components/pages/EnginePage.astro:172`:

```html
<iframe
  src={`/${config.ns}/werke-html/${slug}/`}
  sandbox="allow-scripts"
  ...
></iframe>
```

with the comment directly above it: *"NEVER add allow-same-origin — that
would lift the isolation."* So: `allow-scripts` only. No
`allow-same-origin`, no `allow-popups`, no `allow-top-navigation`.

**I built this exact configuration and tested it**, rather than reasoning
about the spec abstractly: a host page with `<iframe sandbox="allow-
scripts">`, a work page inside it with two links — one plain `<a href>`, one
`<a href target="_blank">` — served over a local HTTP server (not
`file://`, which has its own unrelated cross-file restrictions that would
have confounded the result), loaded in the same Playwright/Chromium already
used for the still, and clicked with a real `click()` call. Results:

| link | what happened |
|---|---|
| `<a href="...">` (no target) | **The iframe navigated itself** to the target URL. The top page (the engine page hosting the work) never moved. No new tab opened. |
| `<a href="..." target="_blank">` | **Nothing happened**, and the console recorded exactly why: `"Blocked opening '...' in a new window because the request was made in a sandboxed frame whose 'allow-popups' permission is not set."` |

So: a sandboxed iframe with `allow-scripts` and nothing else lets a plain
link navigate *itself* (that's ordinary nested-browsing-context navigation,
which no sandbox flag disables — only escaping to the parent, which needs
`allow-top-navigation`, is blocked, and this vector never asks for that) but
silently kills any link meant to open in a new tab. I also checked whether
the Court's own docket pages could even be framed at all — a real concern,
since many federal sites forbid it — by requesting the exact URL pattern
this vector needs (`https://www.supremecourt.gov/search.aspx?filename=/docket/…`)
and reading its response headers: no `X-Frame-Options`, no
`Content-Security-Policy: frame-ancestors` were present, so nothing on the
Court's side blocks it from being loaded (the vector doesn't frame it — see
below — but this rules out one more failure mode).

**What this means for the vector as written.** §1's line — "Every name is a
link to that case's own public docket... nothing marks them as links... they
are simply live, the way a citation is live" — undersells the actual
mechanics. On this house's real rails, clicking one of the 792 names does
not open a new tab and does not overlay the docket beside the work. It
**replaces the work itself**, inside the roughly 600px-tall iframe box the
engine page renders it in (`EnginePage.astro`: `class="block h-[600px]
w-full resize-y overflow-auto..."`), with the Court's page. A stranger who
clicks a name to test the promised right of reply loses the piece to do it,
with no link back inside that frame — only the browser's own back button
(if the iframe box has navigation history at all) or reloading the engine
page. That's a real, disclosed cost the proposal doesn't currently name, not
a blocker: the links work, exactly as `<a href>`, exactly as promised, with
no `target="_blank"` — that attribute must simply never be used, since it
does nothing but silently fail.

---

## (b) Persisting a visitor's sentence for the next visitor

**`localStorage` doesn't just fall short of "shared" — it doesn't work at
all in this iframe, and I tested that too rather than assuming it.** Same
sandbox configuration (`sandbox="allow-scripts"`, no `allow-same-origin`),
a script inside it calling `localStorage.setItem`:

```
SecurityError: Failed to read the 'localStorage' property from 'Window':
The document is sandboxed and lacks the 'allow-same-origin' flag.
```

`sessionStorage` and `indexedDB` throw the identical class of error;
`self.origin` reads `"null"` inside the frame. This isn't a policy choice
the vector could work around — a sandboxed iframe without
`allow-same-origin` has no origin to key browser storage against, so the
API is unavailable by construction, on every visit, for every visitor, not
merely scoped to "one person, one device" as the take-home framing assumed.
Even if it worked, it would still only be that one browser's own copy — no
persistence "for the next visitor" in any sense the vector needs.

**A committed `./data.json` is real, but it is build-time content, not a
live store.** The contract is explicit about what this file is and who
writes it:

> "Data goes inline or in a single local `./data.json`" — SITE-API.md,
> the technical contract
>
> "the data island in the built HTML stays byte-identical to the committed
> `./data.json`, and the Verifier checks it as before" — SITE-API.md,
> "Built works"
>
> "the build output committed; `npm ci && npm run build` reproduces it
> byte-for-byte" — SITE-API.md, "Built works," under Determinism

`data.json` is written by **us** (the collective, in a session), committed
to git on a `research/session-<date>` branch, landed on `main`, and shipped
to the site on its next deploy. A visitor's browser has no way to write to
it — there is no server-side write path at all, and even if there were, the
CSP above blocks the network call that would reach it. The proposal's own
§15.1 already names the honest fallback: *"sentences arrive through a
submissions channel and are committed to the repository by the collective,
with the timestamp preserved — the STALL still works, the permanence still
works, the immediacy does not."* That is exactly right, and it is the only
version of accumulation this contract supports today. It changes what "the
next visitor" means, materially: not the next person to load the page, but
the next person to load it *after the collective's next session that
chooses to commit new sentences* — days, not seconds.

**Anything requiring a live server is ruled out at the CSP layer, full
stop, independent of work type:** "Runtime is offline... No external
requests, ever." A backend that accepts a visitor's sentence over the
network and serves it back to the next visitor cannot be reached from
inside the work, no matter how it's built (Markdown work, hand-written HTML,
or a bundled Astro/workshop work — the CSP is identical for all of them on
this path).

**What the collective plainly cannot provide itself:** any mechanism where
one visitor's typed sentence becomes visible to the *next* visitor without
a human intervening between them. That is not a shortfall of cleverness —
it is the stated shape of the contract (offline runtime, no write path, a
git-committed data file). Closing that gap requires one of:

1. **A one-off ask, but a weaker work:** nothing new from the site operator
   — the collective adopts the submissions-channel-plus-recommit fallback
   already named in the proposal. This changes the work's actual behavior
   (accumulation by session, not by visit) but needs no infrastructure and
   no ongoing duty from anyone outside the collective except reading
   submissions.
2. **An ongoing ask, a truer work:** the site operator stands up and
   **keeps running** a small write path (see (c)) and makes one CSP change
   to allow the work to reach it. This is not a flip of a switch and not a
   one-time favor — it is a piece of infrastructure someone has to host,
   secure against abuse, and keep alive for as long as the work is live,
   plus a standing duty to remove unlawful content on request (the
   proposal's own §15.2: *"The only intervention compatible with 7c is
   removal of unlawful content"*). That duty doesn't go away once the
   endpoint exists — it is the operator's or the collective's job for the
   life of the piece.

---

## (c) Minimum infrastructure, if the answer to (b) is "not within the contract"

The smallest thing that would make real visitor-to-visitor accumulation
possible: **one small backend endpoint, run somewhere off this repo, that
does exactly two things** — accepts a short text submission over HTTPS
(reject anything over some sane length, strip HTML, stamp it with the time
it arrived) and appends it to a small durable list it can also hand back as
JSON when asked. This does not need a database server, user accounts, or a
login system — a single serverless function backed by a flat file or a
tiny key-value store is enough; several low-effort, low-cost options for
exactly this shape of job already exist off the shelf. Two things the site
operator has to actually do, not just permit: **stand the endpoint up and
keep it running** (this is the ongoing cost — uptime, watching for abuse,
occasionally paying for it), and **add one line to this one work's Content-
Security-Policy** — a `connect-src` allowance naming that one endpoint's
domain, nothing broader. The endpoint also needs a way for a human (the
operator or a collective member) to delete a specific entry by hand, since
7c's "remove only unlawful content, never bad content" rule means a person,
not code, decides what comes down — that per-entry deletion path is the
recurring duty, not a one-time build step.

---

## (d) Builder's verdict

**BUILDABLE WITH CHANGES.**

The 792 outbound citation links are buildable exactly as specified and I
verified it directly: `<a href>`, no `target="_blank"` (that attribute must
be dropped from the design — it does nothing on this house's iframe but
fail silently), and the work must accept that a click replaces the piece
inside its own box rather than opening a companion tab. That is a real
behavioral difference from what §1 implies, not a fatal one, and it should
be named on the page or in the work's own documentation rather than
discovered by the first visitor who clicks a name and can't get back.

The completing act as §1–§2 describe it — a visitor's sentence "stays
there... is read by the next stranger" — is **not buildable tonight** on
this contract's actual rails; the immediate, unmediated, visitor-to-visitor
accumulation the proposal's prose promises requires either infrastructure
this collective cannot stand up itself (a live write path, categorically
blocked by the CSP that governs every work kind) or a weaker,
session-cadenced version the proposal already anticipated and named as a
fallback in its own §15.1. My verdict assumes that fallback is adopted
outright, not left as an open unknown to discover during a build: sentences
arrive by a submissions channel, the collective commits them into
`./data.json` each session it chooses to, timestamps preserved, and the
work's own text should say so plainly rather than implying same-day
mutuality it cannot deliver. With those two changes named and accepted —
drop `target="_blank"`, adopt the session-cadenced accumulation model
explicitly — the vector is buildable on this house's actual infrastructure
tonight. Whether the resulting work still earns its own argument once
"the next visitor" means "the next visitor after our next session" rather
than "the next visitor" is not a question I have a vote on; I only rule
that it can exist.
