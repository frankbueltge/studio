// witness-order.mjs — the same two observations, only the station names swapped.
//
// WHY THIS EXISTS. Until 2026-08-29 the room's `witnessedWet()` returned the FIRST match
// in `wetSpans`, and `wetSpans` is appended in the order stations are first seen wet —
// station-id order within a pull. So for any office with two wet stations inside one
// forecast period, one of them older than the room and one younger, the room's verdict was
// decided by the alphabet: if the younger observation's station sorted first, the room
// flared; if the older one did, the room removed the claim in silence as `unwitnessed`.
// Nothing about the sky differed between those two cases. Only the names did.
//
// This drives two builds of the room over two fixtures that differ ONLY in which station
// carries which observation, and prints what each did. A repaired room answers the same
// way in both columns; the old one does not.
//
//   NODE_PATH=/opt/node22/lib/node_modules node tools/witness-order.mjs \
//     --before=<path to old index.html> --after=<path to new index.html> [--work=<dir>]
//
// The fixture is synthetic and says so on its face: one office, two stations, one claim.
// Its window is a real local 06:00/18:00 window in UTC so that the room's supply audit
// (session 112) passes and the room actually adjudicates rather than withholding.

import { createRequire } from "node:module";
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright");

const args = Object.fromEntries(process.argv.slice(2).map(a => {
  const m = a.match(/^--([^=]+)(?:=(.*))?$/);
  return m ? [m[1], m[2] === undefined ? true : m[2]] : [a, true];
}));
const WORK = path.resolve(args.work || "/tmp/witness-order");
const BUILDS = { before: path.resolve(args.before), after: path.resolve(args.after) };

/* THE ARRIVAL PATTERN THE DEFECT NEEDS, and the first draft of this file did not have it.
 *
 * A room that finds a wet observation in the sky it reads at the door settles that claim
 * immediately and once — `unwitnessed`, because the water fell before the room opened — and
 * no later observation can reach it. So two observations sitting in the opening snapshot
 * cannot show the ordering: the older one always wins by arriving first in time, whichever
 * way the array runs.
 *
 * The case is a LATER pull that brings two wet observations for one office at once, one
 * older than the door and one younger. That happens for real: the observation sweep drops
 * boxes (four failed in tonight's own six-hour sweep) and a station's report can therefore
 * reach the room minutes after it was filed. So the fixture opens dry, and the sky is
 * rewritten under the running room.
 */
const OLD_MIN = 5, NEW_SEC = 20;

function fixture(dir, earlyStation, lateStation, wet) {
  fs.mkdirSync(path.join(dir, "data"), { recursive: true });
  const now = Date.now();
  // The window: yesterday 18:00Z to today 06:00Z, a real night period in UTC, so the
  // office is placed in its own hours and the room's audit has nothing to say.
  const today = new Date(now); today.setUTCHours(6, 0, 0, 0);
  const end = today.getTime() > now ? today.getTime() : today.getTime() + 86400000;
  const start = end - 12 * 3600000;
  const iso = t => new Date(t).toISOString().replace(/\.\d+Z$/, "Z");
  fs.writeFileSync(path.join(dir, "data", "atlas.json"), JSON.stringify({
    built: iso(now), note: "synthetic fixture for tools/witness-order.mjs — not a record",
    offices: { TST: { lat: 39.0, lon: -95.0, tz: "UTC", zones: 1,
                      stations: [earlyStation, lateStation].sort() } },
    counts: { offices: 1, placed: 1, zones: 1, stations: 2 },
  }));
  fs.writeFileSync(path.join(dir, "data", "claims.json"), JSON.stringify({
    generated: iso(now), note: "synthetic fixture — one office, one claim",
    counts: { offices: 1, claims: 1, periods: 1, numeric: 0, silent: 0, reissued: 1,
              tz_unknown: 0 },
    tz_unknown: [],
    offices: { TST: { issued: iso(start), zones: 1, claims: [
      { p: "TONIGHT", t: "Clear. Lows in the lower 60s.", n: null, w: false, z: 1,
        s: iso(start), e: iso(end) }] } },
  }));
  sky(dir, earlyStation, lateStation, wet, now);
}

/* `wet` false: both stations reporting and neither raining — the room opens with nothing to
   settle. `wet` true: the same two stations, both raining, one observed OLD_MIN before the
   room's door and one NEW_SEC after it.
   THE KEYS ARE WRITTEN IN STATION-ID ORDER, because that is how `cycle_sky` writes them
   (`sorted(latest.items())`) and therefore the order `absorbSky()` walks and `wetSpans`
   ends up in. What the two cases vary is which NAME carries which observation — which is
   the only thing that differs between them, and under the old rule it decided the verdict. */
function sky(dir, olderStation, youngerStation, wet, openedAt) {
  const now = Date.now();
  const iso = t => new Date(t).toISOString().replace(/\.\d+Z$/, "Z");
  const st = (lat, lon, t, r) => r ? { la: lat, lo: lon, t: Math.round(t / 1000), w: "-RA", r: 1 }
                                   : { la: lat, lo: lon, t: Math.round(t / 1000), w: "" };
  const at = { [olderStation]: openedAt - OLD_MIN * 60000,
               [youngerStation]: openedAt + NEW_SEC * 1000 };
  const stations = {};
  [olderStation, youngerStation].sort().forEach((id, i) => {
    stations[id] = st(39.0 + i * 0.1, -95.0 - i * 0.1, at[id], wet);
  });
  fs.writeFileSync(path.join(dir, "data", "sky.json"), JSON.stringify({
    generated: iso(now), note: "synthetic fixture — two stations, one office",
    counts: { stations: 2, reporting_weather: wet ? 2 : 0, wet: wet ? 2 : 0,
              boxes: 0, boxes_failed: 0 },
    stations: stations,
  }));
}

async function run(build, dir, older, younger) {
  fs.copyFileSync(build, path.join(dir, "index.html"));
  const server = http.createServer((req, res) => {
    const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
    const file = path.join(dir, rel);
    if (!file.startsWith(dir)) { res.writeHead(403).end(); return; }
    fs.readFile(file, (err, buf) => {
      if (err) { res.writeHead(404).end(); return; }
      res.writeHead(200, { "content-type": rel.endsWith(".json") ? "application/json"
                                                                 : "text/html",
                           "cache-control": "no-store" }).end(buf);
    });
  });
  await new Promise(r => server.listen(0, "127.0.0.1", r));
  const port = server.address().port;
  const browser = await chromium.launch({ args: ["--autoplay-policy=no-user-gesture-required"] });
  const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
  const errors = [];
  page.on("pageerror", e => errors.push(String(e)));
  // An unwitnessed mark is removed from `events` 900 ms after it is raised, so asking the
  // room afterwards what it did would catch nothing. Every fire() is recorded as it happens.
  await page.addInitScript(() => {
    window.__log = [];
    const iv = setInterval(() => {
      if (typeof window.fire !== "function" || window.__wrapped) return;
      window.__wrapped = true;
      const fire0 = window.fire;
      window.fire = function (node, item, kind) {
        window.__log.push({ kind: kind, office: node.id, at: Date.now() });
        return fire0.apply(this, arguments);
      };
    }, 20);
    setTimeout(() => clearInterval(iv), 30000);
  });
  await page.goto(`http://127.0.0.1:${port}/index.html`, { waitUntil: "load" });
  await page.waitForFunction(() => typeof offices !== "undefined" && offices.length > 0,
                             null, { timeout: 30000 });
  const openedAt = await page.evaluate(() => openedAt);
  // Both observations must be eligible at the SAME settle tick, or the array order decides
  // nothing: `settle()` runs every second and takes the first match that is already in the
  // past, so an older observation delivered early always wins on time alone. So the room is
  // left dry until the younger observation's own instant has passed, and only then is the
  // sky rewritten with both of them at once — which is exactly the shape a delayed box
  // produces in the live relay.
  await page.waitForTimeout((NEW_SEC + 6) * 1000);
  // The sky changes under the running room, and the room is asked to read it with its own
  // pull — the same function its own interval calls, called early so four runs of this
  // experiment take minutes rather than a quarter of an hour.
  sky(dir, older, younger, true, openedAt);
  await page.evaluate(() => pull(false));
  await page.waitForTimeout(6000);                     // settle ticks and the draw loop
  const out = await page.evaluate(() => ({
    log: window.__log,
    settled: settledKeys.size,
    recent: recent.length,
    withheld: typeof withheld === "function" ? withheld() : null,
  }));
  out.kinds = out.log.reduce((a, e) => (a[e.kind] = (a[e.kind] || 0) + 1, a), {});
  delete out.log;
  out.errors = errors.length;
  await browser.close();
  await new Promise(r => server.close(r));
  return out;
}

const rows = [];
for (const [name, build] of Object.entries(BUILDS)) {
  for (const [order, [older, younger]] of Object.entries({
    // which NAME carries the observation older than the door, and which the younger one
    "older observation sorts first": ["KAAA", "KZZZ"],
    "younger observation sorts first": ["KZZZ", "KAAA"],
  })) {
    const dir = path.join(WORK, `${name}-${order.split(" ")[0]}`);
    fs.rmSync(dir, { recursive: true, force: true });
    fixture(dir, older, younger, false);
    const r = await run(build, dir, older, younger);
    rows.push({ build: name, order, ...r });
    process.stdout.write(`${name.padEnd(7)} ${order.padEnd(32)} ` +
      `kinds ${JSON.stringify(r.kinds).padEnd(24)} settled ${r.settled} ` +
      `recent ${r.recent} withheld ${r.withheld} errors ${r.errors}\n`);
  }
}
process.stdout.write("\n" + JSON.stringify(rows, null, 1) + "\n");
