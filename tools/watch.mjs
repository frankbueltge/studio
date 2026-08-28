// watch.mjs — the instrument that sits in front of OUTSTANDING for an hour and writes down
// what it saw, so that the next night's figures can be compared to tonight's.
//
// WHY THIS EXISTS. Every session that has evidenced a milestone of this work — 107, 109, 110 —
// drove the room with a script written that evening and thrown away before the commit. The
// numbers in the record are therefore not reproducible by anyone, including us: session 110
// reported "twelve re-issuances, twelve sweeps" to the team and "thirty-two out of thirty-two"
// in its own journal, from two watches of the same night, and nothing in the repository can
// say which instrument produced which. This house already knows the shape of that failure —
// `tools/frame.mjs` was written to end it for another measurement, and its header says so.
// This ends it for the room.
//
//   NODE_PATH=/opt/node22/lib/node_modules node tools/watch.mjs --dir=<room dir> --minutes=45
//
//   --dir      directory holding index.html and data/ (claims.json, sky.json, atlas.json)
//   --minutes  how long to keep the door open (default 20)
//   --sample   seconds between samples of the field (default 10)
//   --width --height   the window, in CSS pixels (default 1920×1080)
//   --query    query string for the room (e.g. "fixture" or "cold"); it picks its own record from it
//   --shots    directory to drop a frame into whenever an event is caught mid-animation
//   --json     write the whole sample series here, not just the summary
//
// WHAT IT DOES NOT DO. It does not judge. It prints what it counted and nothing else; every
// sentence about what those counts mean belongs in the journal, written by someone who looked.
// It also does not start the relay: point `--dir` at a directory something else is writing to,
// or at a static one, and the difference will show up in the record it prints — which is the
// whole point of the staleness work of session 111.

import { createRequire } from "node:module";
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(import.meta.url);   // ESM does not read NODE_PATH; this does
const { chromium } = require("playwright");

const args = Object.fromEntries(process.argv.slice(2).map(a => {
  const m = a.match(/^--([^=]+)(?:=(.*))?$/);
  return m ? [m[1], m[2] === undefined ? true : m[2]] : [a, true];
}));
const DIR = path.resolve(args.dir || "projects/outstanding/room");
const MINUTES = Number(args.minutes || 20);
const SAMPLE = Number(args.sample || 10) * 1000;
const WIDTH = Number(args.width || 1920);
const HEIGHT = Number(args.height || 1080);
const SHOTS = args.shots ? path.resolve(args.shots) : null;
if (SHOTS) fs.mkdirSync(SHOTS, { recursive: true });

const MIME = { ".html": "text/html", ".json": "application/json", ".js": "text/javascript" };

/* A server that answers only from DIR, and answers `no-store` so the room's own cache
   discipline is what is being watched and not the server's. */
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
  const file = path.join(DIR, rel);
  if (!file.startsWith(DIR)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404).end(); return; }
    res.writeHead(200, {
      "content-type": MIME[path.extname(file)] || "application/octet-stream",
      "cache-control": "no-store"
    });
    res.end(buf);
  });
});
await new Promise(r => server.listen(0, "127.0.0.1", r));
const PORT = server.address().port;

const browser = await chromium.launch({ args: ["--autoplay-policy=no-user-gesture-required"] });
const page = await browser.newPage({ viewport: { width: WIDTH, height: HEIGHT } });

const errors = [];
page.on("pageerror", e => errors.push(String(e)));
page.on("console", m => { if (m.type() === "error") errors.push("console: " + m.text()); });

/* The room's own functions are top-level declarations in a classic script, so they are
   properties of the global object and can be wrapped without touching the file. Every
   settlement and every re-issuance the room raises is recorded here with the instant it
   was raised — the room is not asked afterwards what it did, it is watched while it does it. */
await page.addInitScript(() => {
  window.__log = [];
  const install = () => {
    if (typeof window.fire !== "function" || window.__wrapped) return;
    window.__wrapped = true;
    const fire0 = window.fire, rebuild0 = window.rebuild;
    window.fire = function (node, item, kind) {
      window.__log.push({ at: Date.now(), kind, office: node.id, ring: item.ring,
                          period: item.c && item.c.p });
      return fire0.apply(this, arguments);
    };
    window.rebuild = function (first) {
      const before = events ? events.length : 0;
      const r = rebuild0.apply(this, arguments);
      const evs = events || [];
      for (let i = before; i < evs.length; i++)
        if (evs[i].kind === "sweep" || evs[i].kind === "heard")
          window.__log.push({ at: Date.now(), kind: evs[i].kind, office: evs[i].node.id });
      return r;
    };
  };
  const iv = setInterval(install, 20);
  setTimeout(() => clearInterval(iv), 20000);
});

// The room chooses its record from its own query string (`?fixture`, `?cold`), so an
// instrument that can only open the bare path can only ever watch one of the three
// records this work can be pointed at. Session 112 wanted the committed fixture, which
// is the cheapest way to ask whether a new gate falsely condemns a healthy record.
const URL0 = `http://127.0.0.1:${PORT}/index.html` + (args.query ? "?" + args.query : "");
await page.goto(URL0, { waitUntil: "load" });
await page.waitForFunction(() => typeof offices !== "undefined" && offices.length > 0,
                           null, { timeout: 60000 });
const openedAt = Date.now();

/* One sample of the field. Everything here is read out of the room's own state; nothing
   is computed about the world. `fading` counts the events still visibly decaying — the
   quantity milestone 5 is about. */
const SAMPLE_FN = () => {
  const now = performance.now();
  let arcs = 0, live = 0, open = 0, told = 0, drawn = 0, unheard = 0;
  for (const n of offices) {
    drawn++;
    if (n.unheard) { unheard++; } else { told++; }
    arcs += n.arcs.length; live += n.live.length;
    for (const it of n.live) open += it.c.z;
  }
  let fading = 0, flaring = 0;
  const by = {};
  for (const ev of events) {
    const age = now - ev.t0;
    by[ev.kind] = (by[ev.kind] || 0) + 1;
    if (ev.kind === "unwitnessed" || ev.kind === "sweep" || ev.kind === "heard") continue;
    if (age > 700) fading++; else flaring++;
  }
  return {
    t: Date.now(), arcs, live, open, told, drawn, unheard,
    events: events.length, fading, flaring, by,
    settled: settledKeys.size,
    recent: recent.length,
    logged: window.__log.length,
    // Guarded so this instrument can also be pointed at a build of the room from before
    // these fields existed, which is the only way to measure what changed.
    relayAt: typeof relayAt === "undefined" ? null : relayAt,
    relayMoved: typeof relayMoved === "undefined" ? null : relayMoved,
    stale: typeof stale === "undefined" ? null : stale(),
    // The room's own standing: null while it vouches for what it draws, "quiet" when the
    // record has stopped advancing, "false" when the record it holds does not place its
    // offices in their own hours. The face does not distinguish the last two, deliberately;
    // this instrument may, which is the whole reason the reason is kept off the face and
    // reachable here. `fault` carries the audit's count when it fired, else null.
    withheld: typeof withheld === "undefined" ? null : withheld(),
    // `audit` is what the check SAW — how many offices it could put a question to and how
    // many were out of place — reported whether or not it fired. A gate that reports only
    // when it trips cannot be told apart from a gate that never ran.
    audit: typeof supply === "undefined" ? null : supply().audit,
    // How long ago the room last drew its pulse. On a record that has stopped advancing
    // this is the whole question: a pulse that keeps beating is the room claiming to have
    // been told something.
    heartbeatAgo: Math.round(now - heartbeat),
    heap: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null,
    scrollX: document.documentElement.scrollWidth - document.documentElement.clientWidth
  };
};

const samples = [];
const deadline = openedAt + MINUTES * 60000;
let shot = 0;
process.stdout.write(`watching ${DIR} at ${WIDTH}x${HEIGHT} for ${MINUTES} min\n`);

while (Date.now() < deadline) {
  await page.waitForTimeout(SAMPLE);
  let s;
  try { s = await page.evaluate(SAMPLE_FN); }
  catch (e) { errors.push("sample: " + String(e)); break; }
  s.elapsed = Math.round((s.t - openedAt) / 1000);
  samples.push(s);
  process.stdout.write(
    `${String(s.elapsed).padStart(5)}s  arcs ${String(s.arcs).padStart(5)}  open ${String(s.open).padStart(6)}` +
    `  told ${String(s.told).padStart(3)}  ev ${String(s.events).padStart(3)}` +
    `  fading ${String(s.fading).padStart(3)}  settled ${String(s.settled).padStart(6)}` +
    `  logged ${String(s.logged).padStart(4)}  heap ${s.heap}MB\n`);
  if (SHOTS && s.flaring > 0 && shot < 12) {
    shot++;
    await page.screenshot({ path: path.join(SHOTS, `flare-${String(shot).padStart(2, "0")}.png`) });
  }
}

const log = await page.evaluate(() => window.__log);

/* The field's own brightness, counted rather than described.
 *
 * Session 112 gave the room a posture for withholding its authority: while it is not
 * vouching for what it draws, every band goes to the bare mark and the lit node centres
 * go out, so the picture flattens to one cool grey. That is a claim about pixels and it
 * is measured here as pixels. Read off the STILL canvas — the field's own drawing, before
 * any afterglow is composited over it — so what is counted is the field's standing state
 * and not an animation that happened to be running. No judgement: four counts and a mean. */
let fieldReport = null;
try {
  fieldReport = await page.evaluate(() => {
    const d = still.getContext("2d").getImageData(0, 0, still.width, still.height).data;
    let sum = 0, n = 0, a60 = 0, a100 = 0, a160 = 0;
    for (let i = 0; i < d.length; i += 4) {
      const l = 0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2];
      n++; sum += l;
      if (l > 60) a60++;
      if (l > 100) a100++;
      if (l > 160) a160++;
    }
    return { pixels: n, meanLuma: Math.round(sum / n * 1000) / 1000,
             over60: a60, over100: a100, over160: a160,
             withheld: typeof withheld === "undefined" ? null : withheld() };
  });
} catch (e) { fieldReport = { error: String(e) }; }

/* The held node, measured rather than asserted: press on the office that has had the most
   settlements in this watch, read back what the panel says and what its trace strip holds. */
let heldReport = null;
try {
  const busiest = {};
  for (const e of log) if (["lock", "rupture", "silence"].includes(e.kind))
    busiest[e.office] = (busiest[e.office] || 0) + 1;
  const target = Object.entries(busiest).sort((a, b) => b[1] - a[1])[0];
  heldReport = await page.evaluate(id => {
    const node = id ? byId.get(id) : offices.find(n => n.arcs.length);
    if (!node) return { error: "no node to hold" };
    window.hold(node.x, node.y);
    const p = document.getElementById("panel");
    const cv = p.querySelector("canvas");
    // The strip is drawn on a transparent canvas over a flat rgba(...,0.03) wash, so
    // alpha is what separates ground from figure: the wash lands near 7, the hatch that
    // means "the room was not open yet" near 56, a verdict tick near 229.
    let hatch = 0, ticks = 0;
    if (cv) {
      const d = cv.getContext("2d").getImageData(0, 0, cv.width, cv.height).data;
      for (let i = 3; i < d.length; i += 4) {
        if (d[i] > 150) ticks++; else if (d[i] > 20) hatch++;
      }
    }
    return {
      office: node.id,
      on: p.className === "on",
      who: (p.querySelector(".who") || {}).textContent,
      period: (p.querySelector(".per") || {}).textContent,
      sentence: (p.querySelector(".say") || {}).textContent,
      tracePixelsHatched: hatch,
      tracePixelsInked: ticks,
      traceSettlements: recent.filter(r => r.office === node.id).length,
      // Guarded like the fields above: pointed at a build of the room from before this
      // array existed, the held report used to die with a ReferenceError and take the
      // whole comparison with it — which is how the first paired run of 2026-08-26 lost
      // its "before" side.
      traceReissues: typeof reissues === "undefined" ? null
                     : reissues.filter(r => r.office === node.id).length,
      roomAgeSeconds: Math.round((Date.now() - openedAt) / 1000),
      reader: document.getElementById("reader").textContent.slice(0, 200),
      // The one place this work puts words on a screen, measured rather than assumed:
      // what size they actually resolve to at this medium, and whether the box that
      // holds them stays inside the frame.
      panelFontPx: Math.round(parseFloat(getComputedStyle(p).fontSize) * 10) / 10,
      sayFontPx: p.querySelector(".say")
        ? Math.round(parseFloat(getComputedStyle(p.querySelector(".say")).fontSize) * 10) / 10 : null,
      panelBox: (r => ({ x: Math.round(r.x), y: Math.round(r.y),
                         w: Math.round(r.width), h: Math.round(r.height),
                         inside: r.x >= 0 && r.y >= 0 &&
                                 r.right <= innerWidth && r.bottom <= innerHeight }))(p.getBoundingClientRect())
    };
  }, target ? target[0] : null);
  // The panel fades in over .28s. A frame taken the instant the hold is made catches it
  // half-transparent and shows the looker nothing, which is how a shot of it went into
  // the record once already.
  await page.waitForTimeout(500);
  if (SHOTS) {
    await page.screenshot({ path: path.join(SHOTS, "held.png") });
    // And the panel on its own, at 1:1, because the one place this work puts words on a
    // screen cannot be judged from a frame in which it is forty pixels across.
    const b = heldReport && heldReport.panelBox;
    if (b && b.w > 0 && b.h > 0)
      await page.screenshot({ path: path.join(SHOTS, "held-panel.png"),
                              clip: { x: b.x, y: b.y, width: b.w, height: b.h } });
  }
} catch (e) { heldReport = { error: String(e) }; }

const spoken = await page.evaluate(() => document.getElementById("reader").textContent);
await browser.close();
server.close();

/* ------------------------------------------------------------------------ the record */
const tally = {};
for (const e of log) tally[e.kind] = (tally[e.kind] || 0) + 1;
const withFading = samples.filter(s => s.fading > 0).length;
const gaps = [];
let runStart = null;
for (const s of samples) {
  if (s.fading === 0 && runStart === null) runStart = s.elapsed;
  if (s.fading > 0 && runStart !== null) { gaps.push(s.elapsed - runStart); runStart = null; }
}
if (runStart !== null && samples.length) gaps.push(samples[samples.length - 1].elapsed - runStart);

const out = {
  watched: { dir: DIR, minutes: MINUTES, sampleSeconds: SAMPLE / 1000,
             width: WIDTH, height: HEIGHT, from: new Date(openedAt).toISOString(),
             samples: samples.length },
  events: tally,
  sustained: {
    samplesWithFading: withFading,
    ofSamples: samples.length,
    longestGapSeconds: gaps.length ? Math.max(...gaps) : 0,
    arcsFirst: samples.length ? samples[0].arcs : null,
    arcsLast: samples.length ? samples[samples.length - 1].arcs : null,
    openFirst: samples.length ? samples[0].open : null,
    openLast: samples.length ? samples[samples.length - 1].open : null
  },
  held: heldReport,
  field: fieldReport,
  spoken,
  staleFrom: (samples.find(s => s.stale) || {}).elapsed ?? null,
  withheldFrom: (samples.find(s => s.withheld) || {}).elapsed ?? null,
  withheldReasons: [...new Set(samples.map(s => s.withheld).filter(Boolean))],
  audit: samples.length ? samples[samples.length - 1].audit ?? null : null,
  pulsesAfterFirstMinute: samples.filter(s => s.elapsed > 60 && s.heartbeatAgo < 60000).length,
  relayStamps: samples.length ? new Set(samples.map(s => s.relayAt)).size : 0,
  heapMaxMB: samples.reduce((m, s) => Math.max(m, s.heap || 0), 0),
  overflowMax: samples.reduce((m, s) => Math.max(m, s.scrollX || 0), 0),
  errors
};
process.stdout.write("\n" + JSON.stringify(out, null, 2) + "\n");
if (args.json) fs.writeFileSync(path.resolve(args.json),
  JSON.stringify({ summary: out, samples, log }, null, 2));
process.exit(errors.length ? 1 : 0);
