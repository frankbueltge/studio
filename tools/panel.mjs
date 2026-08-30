// panel.mjs — the instrument that carries OUTSTANDING to a reader who has never heard of it.
//
// WHY THIS EXISTS. The constitution's ship gate has a limb this house cannot argue its way
// past: before a work ships, severed readers meet it cold, are asked what they understood and
// what they take it to be about, and their answers are published beside the work unedited. A
// severed reader cannot stand in the room. What can be carried to them is a strip of frames of
// the actual field, taken from an actual watch, at a stated cadence — and the honest statement
// of what that strip does NOT carry, which for this work is two whole channels: the motion
// between frames, and the sound.
//
//   NODE_PATH=/opt/node22/lib/node_modules node tools/panel.mjs --dir=<room dir> \
//       --minutes=50 --sample=30 --out=<frames dir> --json=<index.json>
//   NODE_PATH=/opt/node22/lib/node_modules node tools/panel.mjs --pick --json=<index.json> \
//       --frames=20
//   NODE_PATH=/opt/node22/lib/node_modules node tools/panel.mjs --cut --json=<index.json> \
//       --at=<elapsed seconds> --frames=20 --out=<cohort dir>
//
// THE THREE MODES ARE DELIBERATELY SEPARATE. Capture watches once, continuously, and knows
// nothing about cohorts. `--pick` reads that one watch and reports every candidate window by
// the rule it is given, so the choice of strip is a printed consequence of a stated rule and
// not a conductor's taste. `--cut` copies the frames of one window into a directory, renamed
// 01..N, with an index of what is in it. Nothing here judges what a reader says, and nothing
// here writes a word a reader will see: the question sheet is written by hand and committed
// beside the answers.
//
// WHAT IT DOES NOT DO. It does not start the relay. It does not choose which window is
// flattering. It does not remove a frame.

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

const SETTLEMENTS = ["lock", "rupture", "silence"];

/* ------------------------------------------------------------------ pick and cut */

if (args.pick || args.cut) {
  const idx = JSON.parse(fs.readFileSync(path.resolve(args.json), "utf8"));
  const N = Number(args.frames || 20);
  const frames = idx.frames;
  const span = (N - 1) * idx.watched.sampleSeconds;

  // A window is N consecutive frames. What is "in" it is every settlement the room raised
  // between the first and last frame of the window — read from the room's own event log,
  // not from the pixels, because a frame is a sample and an event is a fact.
  const windows = frames.map((f, i) => {
    if (i + N > frames.length) return null;
    const t0 = f.at, t1 = frames[i + N - 1].at;
    const inside = idx.log.filter(e => e.at >= t0 && e.at <= t1);
    const settle = inside.filter(e => SETTLEMENTS.includes(e.kind));
    return {
      startFrame: f.i, startElapsed: f.elapsed, endElapsed: frames[i + N - 1].elapsed,
      settlements: settle.length,
      offices: [...new Set(settle.map(e => e.office))],
      instants: [...new Set(settle.map(e => Math.round(e.at / 1000)))].length,
      sweeps: inside.filter(e => e.kind === "sweep").length,
      framesWithFading: frames.slice(i, i + N).filter(s => s.fading > 0).length
    };
  }).filter(Boolean);

  if (args.pick) {
    const byS = [...windows].sort((a, b) => b.settlements - a.settlements);
    const empty = windows.filter(w => w.settlements === 0);
    process.stdout.write(JSON.stringify({
      framesPerWindow: N, windowSeconds: span, candidates: windows.length,
      richest: byS.slice(0, 5),
      emptyWindows: empty.length,
      firstEmpty: empty[0] || null,
      emptiest: empty.filter(w => w.framesWithFading === 0)[0] || null,
      all: windows
    }, null, 2) + "\n");
    process.exit(0);
  }

  const at = Number(args.at);
  const start = frames.reduce((b, f) => Math.abs(f.elapsed - at) < Math.abs(b.elapsed - at) ? f : b);
  const i0 = frames.indexOf(start);
  const chosen = frames.slice(i0, i0 + N);
  const OUT = path.resolve(args.out);
  fs.mkdirSync(OUT, { recursive: true });
  chosen.forEach((f, k) => fs.copyFileSync(path.join(path.dirname(path.resolve(args.json)), f.file),
                                           path.join(OUT, `frame-${String(k + 1).padStart(2, "0")}.png`)));
  const t0 = chosen[0].at, t1 = chosen[chosen.length - 1].at;
  const inside = idx.log.filter(e => e.at >= t0 && e.at <= t1);
  fs.writeFileSync(path.join(OUT, "strip.json"), JSON.stringify({
    fromWatch: path.resolve(args.json),
    sampleSeconds: idx.watched.sampleSeconds,
    frames: chosen.map((f, k) => ({ shown: k + 1, sourceFrame: f.i, elapsed: f.elapsed,
                                    at: new Date(f.at).toISOString(), fading: f.fading,
                                    events: f.events, arcs: f.arcs })),
    settlementsInside: inside.filter(e => SETTLEMENTS.includes(e.kind)),
    sweepsInside: inside.filter(e => e.kind === "sweep").length
  }, null, 2) + "\n");
  process.stdout.write(`cut ${chosen.length} frames from ${chosen[0].elapsed}s to ` +
    `${chosen[chosen.length - 1].elapsed}s into ${OUT}; ` +
    `${inside.filter(e => SETTLEMENTS.includes(e.kind)).length} settlements inside\n`);
  process.exit(0);
}

/* ---------------------------------------------------------------------- capture */

const DIR = path.resolve(args.dir || "projects/outstanding/room");
const MINUTES = Number(args.minutes || 50);
const SAMPLE = Number(args.sample || 30) * 1000;
const WIDTH = Number(args.width || 1920);
const HEIGHT = Number(args.height || 1080);
const OUT = path.resolve(args.out || "frames");
fs.mkdirSync(OUT, { recursive: true });

const MIME = { ".html": "text/html", ".json": "application/json", ".js": "text/javascript" };
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split("?")[0]).replace(/^\/+/, "") || "index.html";
  const file = path.join(DIR, rel);
  if (!file.startsWith(DIR)) { res.writeHead(403).end(); return; }
  fs.readFile(file, (err, buf) => {
    if (err) { res.writeHead(404).end(); return; }
    res.writeHead(200, { "content-type": MIME[path.extname(file)] || "application/octet-stream",
                         "cache-control": "no-store" });
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

// Same wrap as tools/watch.mjs: the room is watched while it decides, not asked afterwards.
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

await page.goto(`http://127.0.0.1:${PORT}/index.html` + (args.query ? "?" + args.query : ""),
                { waitUntil: "load" });
await page.waitForFunction(() => typeof offices !== "undefined" && offices.length > 0,
                           null, { timeout: 60000 });
const openedAt = Date.now();

const STATE_FN = () => {
  const now = performance.now();
  let arcs = 0, told = 0, unheard = 0;
  for (const n of offices) { arcs += n.arcs.length; if (n.unheard) unheard++; else told++; }
  let fading = 0, flaring = 0;
  for (const ev of events) {
    if (["unwitnessed", "sweep", "heard"].includes(ev.kind)) continue;
    if (now - ev.t0 > 700) fading++; else flaring++;
  }
  return { arcs, told, unheard, events: events.length, fading, flaring,
           settled: settledKeys.size,
           relayAt: typeof relayAt === "undefined" ? null : relayAt,
           stale: typeof stale === "undefined" ? null : stale(),
           withheld: typeof withheld === "undefined" ? null : withheld(),
           heap: performance.memory ? Math.round(performance.memory.usedJSHeapSize / 1048576) : null,
           scrollX: document.documentElement.scrollWidth - document.documentElement.clientWidth };
};

const frames = [];
const deadline = openedAt + MINUTES * 60000;
process.stdout.write(`capturing ${DIR} at ${WIDTH}x${HEIGHT}, every ${SAMPLE / 1000}s, ` +
                     `for ${MINUTES} min, into ${OUT}\n`);
let i = 0;
while (Date.now() < deadline) {
  await page.waitForTimeout(SAMPLE);
  i++;
  const file = `frame-${String(i).padStart(3, "0")}.png`;
  // The state is read first and the frame taken immediately after, so the numbers written
  // beside a frame are the numbers of that frame and not of the second before it.
  let s;
  try { s = await page.evaluate(STATE_FN); }
  catch (e) { errors.push("sample: " + String(e)); break; }
  await page.screenshot({ path: path.join(OUT, file) });
  const rec = { i, file, at: Date.now(), elapsed: Math.round((Date.now() - openedAt) / 1000), ...s };
  frames.push(rec);
  process.stdout.write(`${String(rec.elapsed).padStart(5)}s  ${file}  arcs ${rec.arcs}  ` +
    `ev ${rec.events}  fading ${rec.fading}  settled ${rec.settled}  heap ${rec.heap}MB\n`);
}

const log = await page.evaluate(() => window.__log);
const spoken = await page.evaluate(() => document.getElementById("reader").textContent);
await browser.close();
server.close();

const tally = {};
for (const e of log) tally[e.kind] = (tally[e.kind] || 0) + 1;
const out = {
  watched: { dir: DIR, minutes: MINUTES, sampleSeconds: SAMPLE / 1000, width: WIDTH,
             height: HEIGHT, from: new Date(openedAt).toISOString(), frames: frames.length },
  events: tally,
  relayStamps: new Set(frames.map(f => f.relayAt)).size,
  staleEver: frames.some(f => f.stale),
  withheldEver: frames.some(f => f.withheld),
  heapMaxMB: frames.reduce((m, f) => Math.max(m, f.heap || 0), 0),
  overflowMax: frames.reduce((m, f) => Math.max(m, f.scrollX || 0), 0),
  spoken, errors, frames, log
};
fs.writeFileSync(path.resolve(args.json || path.join(OUT, "index.json")),
                 JSON.stringify(out, null, 2) + "\n");
process.stdout.write(`\n${frames.length} frames · ` + JSON.stringify(tally) +
  ` · relay stamps ${out.relayStamps} · stale ${out.staleEver} · withheld ${out.withheldEver}` +
  ` · errors ${errors.length}\n`);
process.exit(errors.length ? 1 : 0);
