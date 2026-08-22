"use strict";
/*
 * OUTSTANDING — the room.
 *
 * Every currently open public promise about rain in the United States,
 * held as a field of lit points, settled live as the sky answers. No
 * caption, no legend, no title text. See ../CONCEPT.md and ../KRITIKER.md
 * for the piece this file is answerable to.
 *
 * Honesty rule this whole file obeys: nothing is settled at load. A period
 * only ever gets a verdict when this running room was already holding it
 * (recorded a heldSince before the observation existed) and a station
 * reading arrives, during this run, timestamped after that moment. See
 * settlePeriod() below — that function is the one place the concept's
 * central promise either holds or breaks.
 */

// ---------------------------------------------------------------------
// CONFIG — the one thing to edit for local development. Production reads
// the room's own origin; append ?relay=http://localhost:8000 while
// serving this directory locally to point at a scratch copy of the two
// files instead.
// ---------------------------------------------------------------------
const RELAY_BASE =
  new URLSearchParams(location.search).get("relay") ||
  "/studio/relay/outstanding";

const FORECASTS_URL = RELAY_BASE + "/forecasts.json";
const STATIONS_URL = RELAY_BASE + "/stations.json";

// The room polls more often than the relay is obliged to update (10 min
// floor) so a change lands on screen soon after it exists — polling a
// static same-origin file costs nothing the delivery constraints forbid.
const POLL_MS = 15000;

// If a feed's generated_at stops advancing for this long, settlement
// pauses (spec: "the field holds", never a pretended verdict). Set well
// above the 10-minute relay floor to absorb ordinary jitter.
const STALE_MS = 35 * 60 * 1000;

// Nominal forecast-period length. The contract carries no explicit window
// per period, only ordering — so the window a period is checked against is
// derived live from the bulletin's own issued_at plus the period's position
// in its own zone, at a flat 12-hour cadence (day/night, the ZFP's own
// structure). This is a scheduling approximation, not a statistic: it uses
// only fields present in this run's own files. See README "known
// simplifications".
const PERIOD_HOURS = 12;
const SETTLE_GRACE_MS = 5 * 60 * 1000; // let the observation clock catch up

// Afterglow: how long a settled ring stays visible before it is removed
// from the field entirely. Kept short on purpose — condition 4 forbids the
// field from becoming a tally of what is settled.
const AFTERGLOW_LOCK_MS = 70 * 1000;
const AFTERGLOW_RUPTURE_MS = 110 * 1000;

// Seed for every piece of generative behaviour in this room (idle phase
// per node, jitter, flare micro-variation). Same seed, same work.
const SEED = 0x4f55_5453; // "OUTS" — arbitrary, fixed, printed below.

const DEBUG = /[?&]debug=1\b/.test(location.search);

// ---------------------------------------------------------------------
// Seeded RNG — mulberry32. Deterministic given SEED; every stream used in
// this room is derived from it, never from Math.random().
// ---------------------------------------------------------------------
function mulberry32(seed) {
  let a = seed >>> 0;
  return function rng() {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function fnv1a(str) {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}
function seededFor(key) {
  return mulberry32((fnv1a(key) ^ SEED) >>> 0);
}
console.log(
  "%cOUTSTANDING%c seed=0x%s relay=%s poll=%dms debug=%s",
  "color:#e8b84b;font-weight:bold", "color:inherit",
  SEED.toString(16), RELAY_BASE, POLL_MS, DEBUG
);

// ---------------------------------------------------------------------
// DOM
// ---------------------------------------------------------------------
const fieldCanvas = document.getElementById("field");
const flareCanvas = document.getElementById("flares");
const fieldCtx = fieldCanvas.getContext("2d");
const flareCtx = flareCanvas.getContext("2d");
const liveRegion = document.getElementById("live");
const revealEl = document.getElementById("reveal");

let dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
let W = 0, H = 0;

function resize() {
  dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1));
  W = window.innerWidth;
  H = window.innerHeight;
  for (const c of [fieldCanvas, flareCanvas]) {
    c.width = Math.round(W * dpr);
    c.height = Math.round(H * dpr);
  }
  fieldCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
  flareCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
  fieldDirty = true;
  recomputeProjection();
}
window.addEventListener("resize", resize);

// ---------------------------------------------------------------------
// STATE
//
// periods: Map<key, PeriodState>  key = office|ugc|label
//   PeriodState {
//     office, ugc, place, lat, lon, label, text, percent, words, silent,
//     periodIndex, ringIndex, issuedAt (ms), windowEndMs, heldSinceMs,
//     settled: null | { verdict: 'lock'|'rupture', atMs },
//     flareUntilMs (for afterglow removal)
//   }
//
// nodes: Map<placeKey, { office, ugc, place, lat, lon, x, y, periodKeys[] }>
//   placeKey = office|ugc  (one geographic point; many periods/rings)
// ---------------------------------------------------------------------
const periods = new Map();
const nodes = new Map();
// A period just settled and pruned can still be sitting, byte-for-byte
// unchanged, in the live source (the office hasn't re-issued yet). Without
// this guard that reappears next poll as a brand-new "never seen" open
// claim and gets re-settled against the same fact, over and over, until
// the source finally rolls over. retired remembers the fingerprint for a
// bounded window so a still-current bulletin doesn't get re-litigated;
// once the window lapses it is treated as open again regardless, so a
// genuinely stuck source self-heals rather than staying silent forever.
const retired = new Map(); // key -> { text, percent, silent, retiredAtMs }
const RETIRE_HOLD_MS = 60 * 60 * 1000;
const stations = new Map(); // id -> station record
let nearestStationCache = new Map(); // placeKey -> station id
let stationIdSetSignature = "";

let forecastsGeneratedAt = null;
let forecastsLastAdvanceMs = 0;
let stationsGeneratedAt = null;
let stationsLastAdvanceMs = performance.now();
let sessionStartMs = Date.now();
let pollCount = 0;
let settleCount = 0;
let lockCount = 0;
let ruptureCount = 0;

let fieldDirty = true; // redraw the calm layer only when data actually changed
const activeFlares = []; // bounded list of currently-animating flare visuals
const MAX_ACTIVE_FLARES = 600;

// ---------------------------------------------------------------------
// PROJECTION — dynamic bounding box over whatever nodes are actually
// present this run (no hardcoded geography; the field draws whatever
// offices the relay is actually holding, CONUS or otherwise).
// ---------------------------------------------------------------------
let bounds = null; // { minLat, maxLat, minLon, maxLon }
const MARGIN = 46;

function recomputeBounds() {
  let minLat = Infinity, maxLat = -Infinity, minLon = Infinity, maxLon = -Infinity;
  let any = false;
  for (const n of nodes.values()) {
    if (n.lat == null || n.lon == null) continue;
    any = true;
    if (n.lat < minLat) minLat = n.lat;
    if (n.lat > maxLat) maxLat = n.lat;
    if (n.lon < minLon) minLon = n.lon;
    if (n.lon > maxLon) maxLon = n.lon;
  }
  if (!any) { bounds = null; return; }
  // pad a little so edge nodes aren't clipped
  const padLat = Math.max(0.6, (maxLat - minLat) * 0.06);
  const padLon = Math.max(0.6, (maxLon - minLon) * 0.06);
  bounds = {
    minLat: minLat - padLat, maxLat: maxLat + padLat,
    minLon: minLon - padLon, maxLon: maxLon + padLon,
  };
}

// A zone with no lat/lon is never dropped and never crashes the room — but
// how much of the source actually carries geometry is a live, discoverable
// fact, not a fixed assumption: the relay's own geometry fetch is costly
// and bounded (see its own docstring), so anywhere from none to all zones
// may lack coordinates on a given run. The unplaced layout below sizes its
// own reserved area from the ACTUAL counts each time, so it never overlaps
// the geographic field and never collapses every node onto one point —
// which a fixed-width strip and an early-return on "no placed nodes at
// all" both used to do.
function layoutUnplaced(list, reserveW) {
  const availH = Math.max(20, H - MARGIN * 2);
  let pitch = 16;
  while (pitch > 4) {
    const rows = Math.max(1, Math.floor(availH / pitch));
    const cols = Math.ceil(list.length / rows);
    if (cols * pitch <= reserveW) break;
    pitch -= 1;
  }
  const rows = Math.max(1, Math.floor(availH / pitch));
  list.forEach((n, i) => {
    const col = Math.floor(i / rows);
    const row = i % rows;
    n.x = MARGIN / 2 + col * pitch;
    n.y = MARGIN + row * pitch;
  });
}

function recomputeProjection() {
  const placed = [];
  const unplaced = [];
  for (const n of nodes.values()) {
    if (n.lat == null || n.lon == null) unplaced.push(n); else placed.push(n);
  }

  // Reserve just enough width on the left for however many unplaced nodes
  // there actually are this run — nothing if there are none, up to half
  // the screen if that's what a tight vertical fit requires.
  let reserveW = 0;
  if (unplaced.length > 0) {
    reserveW = placed.length === 0
      ? Math.max(50, W - MARGIN)
      : Math.min(W * 0.5, Math.max(60, Math.sqrt(unplaced.length) * 18));
    layoutUnplaced(unplaced, reserveW);
  }

  if (placed.length === 0 || !bounds) return;

  const usableW = Math.max(50, W - MARGIN * 2 - reserveW);
  const usableH = Math.max(50, H - MARGIN * 2);
  const latRange = Math.max(0.001, bounds.maxLat - bounds.minLat);
  const lonRange = Math.max(0.001, bounds.maxLon - bounds.minLon);
  // equirectangular w/ a cosine correction at the field's mean latitude
  const midLat = (bounds.minLat + bounds.maxLat) / 2;
  const cosMid = Math.max(0.2, Math.cos((midLat * Math.PI) / 180));
  const scaleX = usableW / (lonRange * cosMid);
  const scaleY = usableH / latRange;
  const scale = Math.min(scaleX, scaleY);
  const spanW = lonRange * cosMid * scale;
  const spanH = latRange * scale;
  const offX = MARGIN + reserveW + (usableW - spanW) / 2;
  const offY = MARGIN + (usableH - spanH) / 2;

  for (const n of placed) {
    const px = (n.lon - bounds.minLon) * cosMid * scale;
    const py = (bounds.maxLat - n.lat) * scale;
    n.x = offX + px;
    n.y = offY + py;
  }
}

// ---------------------------------------------------------------------
// DATA INGEST
// ---------------------------------------------------------------------
function periodKey(office, ugc, label) { return office + "|" + ugc + "|" + label; }
function placeKey(office, ugc) { return office + "|" + ugc; }

function classify(period) {
  if (period.silent) return "silent";
  if (typeof period.percent === "number" && !Number.isNaN(period.percent)) return "numeric";
  return "word";
}

async function pollForecasts() {
  let json;
  try {
    const res = await fetch(FORECASTS_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    json = await res.json();
  } catch (err) {
    if (DEBUG) console.warn("[outstanding] forecasts fetch failed", err);
    return;
  }
  const now = Date.now();
  if (json.generated_at !== forecastsGeneratedAt) {
    forecastsGeneratedAt = json.generated_at;
    forecastsLastAdvanceMs = now;
  }

  const seenPeriodKeys = new Set();
  const seenPlaceKeys = new Set();
  let anyStructuralChange = false;

  for (const office of json.offices || []) {
    const issuedAtMs = Date.parse(office.issued_at);
    for (const zone of office.zones || []) {
      const pk = placeKey(office.office, zone.ugc);
      seenPlaceKeys.add(pk);
      let node = nodes.get(pk);
      if (!node) {
        node = {
          office: office.office, ugc: zone.ugc, place: zone.place,
          lat: typeof zone.lat === "number" ? zone.lat : null,
          lon: typeof zone.lon === "number" ? zone.lon : null,
          x: 0, y: 0, periodKeys: [],
          phase: seededFor(pk)() * Math.PI * 2,
        };
        nodes.set(pk, node);
        anyStructuralChange = true;
      } else {
        // a place's own coordinates can arrive late (e.g. null on first
        // sight); accept an update, don't require it.
        if (typeof zone.lat === "number") node.lat = zone.lat;
        if (typeof zone.lon === "number") node.lon = zone.lon;
        node.place = zone.place || node.place;
      }
      node.periodKeys = [];

      const periodList = Array.isArray(zone.periods) ? zone.periods : [];
      for (let idx = 0; idx < periodList.length; idx++) {
        const p = periodList[idx];
        const key = periodKey(office.office, zone.ugc, p.label);
        seenPeriodKeys.add(key);
        const ringIndex = Math.min(6, Math.floor(idx / 2));
        const windowEndMs = Number.isFinite(issuedAtMs)
          ? issuedAtMs + (idx + 1) * PERIOD_HOURS * 3600 * 1000
          : now + (idx + 1) * PERIOD_HOURS * 3600 * 1000;

        const existing = periods.get(key);
        const sameContent = existing &&
          existing.text === p.text &&
          existing.percent === (typeof p.percent === "number" ? p.percent : null) &&
          existing.silent === !!p.silent &&
          !existing.settled;

        if (existing && existing.settled) {
          // A settled/afterglowing period keeps its own lifecycle; a fresh
          // re-issuance of the SAME label starts a new open claim only once
          // the afterglow entry is naturally pruned (see pruneSettled()).
          // Until then we leave it exactly as it is — settlement history is
          // never overwritten by a later bulletin. It stays reachable on
          // hold for as long as its own afterglow lasts.
          node.periodKeys.push(key);
          continue;
        }

        if (sameContent) {
          // unchanged open claim — heldSince is untouched. Only bookkeeping.
          existing.periodIndex = idx;
          existing.ringIndex = ringIndex;
          existing.windowEndMs = windowEndMs;
          existing.office = office.office;
          node.periodKeys.push(key);
          continue;
        }

        const r = retired.get(key);
        if (r && now - r.retiredAtMs < RETIRE_HOLD_MS &&
            r.text === (p.text || "") &&
            r.percent === (typeof p.percent === "number" ? p.percent : null) &&
            r.silent === !!p.silent) {
          // Same claim we already settled once, still sitting unchanged in
          // the live source — the source hasn't rolled it off yet. Not
          // re-opened, no fresh ring, not reachable on hold, until either
          // the source actually changes or this guard window lapses (the
          // self-heal for a source that never rolls it off at all).
          continue;
        }

        // New claim, or re-issuance replaced the content of a still-open
        // one. Either way this is freshly held as of *now* — never
        // pre-settled, per the concept's first law.
        retired.delete(key);
        node.periodKeys.push(key);
        periods.set(key, {
          office: office.office, ugc: zone.ugc, place: zone.place,
          label: p.label, text: p.text || "",
          percent: typeof p.percent === "number" ? p.percent : null,
          words: Array.isArray(p.words) ? p.words : [],
          silent: !!p.silent,
          periodIndex: idx, ringIndex,
          issuedAtMs: Number.isFinite(issuedAtMs) ? issuedAtMs : now,
          windowEndMs, heldSinceMs: now,
          settled: null, flareUntilMs: 0,
        });
        anyStructuralChange = true;
        if (existing) {
          if (DEBUG) console.log("[outstanding] re-issuance replaced open claim", key);
        }
      }
    }
  }

  // Prune periods/nodes no longer present in the current file (bounded
  // memory — condition against the field becoming an unbounded archive).
  // Never prune something mid-afterglow; pruneSettled() retires those.
  for (const key of Array.from(periods.keys())) {
    const rec = periods.get(key);
    if (!seenPeriodKeys.has(key) && !rec.settled) {
      periods.delete(key);
      anyStructuralChange = true;
    }
  }
  for (const key of Array.from(nodes.keys())) {
    if (!seenPlaceKeys.has(key)) {
      nodes.delete(key);
      anyStructuralChange = true;
    }
  }

  if (anyStructuralChange) {
    recomputeBounds();
    recomputeProjection();
    fieldDirty = true;
  }
  pollCount++;
  announceIfFirstLoad();
}

async function pollStations() {
  let json;
  try {
    const res = await fetch(STATIONS_URL, { cache: "no-store" });
    if (!res.ok) throw new Error("HTTP " + res.status);
    json = await res.json();
  } catch (err) {
    if (DEBUG) console.warn("[outstanding] stations fetch failed", err);
    return;
  }
  const now = Date.now();
  if (json.generated_at !== stationsGeneratedAt) {
    stationsGeneratedAt = json.generated_at;
    stationsLastAdvanceMs = now;
  }
  const ids = [];
  for (const s of json.stations || []) {
    if (typeof s.lat !== "number" || typeof s.lon !== "number") continue; // can't place it
    stations.set(s.id, {
      id: s.id, name: s.name, lat: s.lat, lon: s.lon,
      observedAtMs: Date.parse(s.observed_at) || null,
      precipMm: typeof s.precip_last_hour_mm === "number" ? s.precip_last_hour_mm : null,
      presentWeather: s.present_weather || null,
      text: s.text || null,
    });
    ids.push(s.id);
  }
  ids.sort();
  const sig = ids.join(",");
  if (sig !== stationIdSetSignature) {
    stationIdSetSignature = sig;
    nearestStationCache = new Map(); // station roster changed structurally; recompute lazily
  }
}

function stationIndicatesPrecip(st) {
  if (!st) return false;
  if (typeof st.precipMm === "number" && st.precipMm > 0) return true;
  const text = ((st.presentWeather || "") + " " + (st.text || "")).toLowerCase();
  return /(rain|shower|drizzle|thunderstorm|snow|sleet|hail|precipitation)/.test(text);
}

function nearestStationFor(node) {
  const pk = placeKey(node.office, node.ugc);
  if (nearestStationCache.has(pk)) return stations.get(nearestStationCache.get(pk));
  if (node.lat == null || node.lon == null || stations.size === 0) return null;
  let best = null, bestD = Infinity;
  for (const st of stations.values()) {
    const dLat = st.lat - node.lat, dLon = st.lon - node.lon;
    const d = dLat * dLat + dLon * dLon;
    if (d < bestD) { bestD = d; best = st; }
  }
  if (best) nearestStationCache.set(pk, best.id);
  return best;
}

// ---------------------------------------------------------------------
// SETTLEMENT — the honest core. See file header.
// ---------------------------------------------------------------------
function settlementsPaused() {
  return Date.now() - stationsLastAdvanceMs > STALE_MS;
}

function settlePass() {
  if (settlementsPaused()) {
    if (DEBUG) console.log("[outstanding] settlements paused — stations feed stale");
    return;
  }
  const now = Date.now();
  for (const rec of periods.values()) {
    if (rec.settled) continue;
    if (now < rec.windowEndMs) continue;
    const node = nodes.get(placeKey(rec.office, rec.ugc));
    if (!node) continue;
    const st = nearestStationFor(node);
    if (!st || st.observedAtMs == null) continue;
    // The whole rule: the observation must postdate the MOMENT THIS ROOM
    // started holding the claim, and postdate (with a little grace) the
    // window it claims about. An observation that predates heldSinceMs
    // cannot settle anything — it was not "new" information to this run.
    if (st.observedAtMs <= rec.heldSinceMs) continue;
    if (st.observedAtMs + SETTLE_GRACE_MS < rec.windowEndMs) continue;

    const claimedPrecip = !rec.silent; // a silence promises nothing; anything else promises something
    const observedPrecip = stationIndicatesPrecip(st);
    const matched = claimedPrecip === observedPrecip;
    const verdict = matched ? "lock" : "rupture";
    rec.settled = { verdict, atMs: now, stationId: st.id };
    rec.flareUntilMs = now + (verdict === "lock" ? AFTERGLOW_LOCK_MS : AFTERGLOW_RUPTURE_MS);
    spawnFlare(node, rec, verdict);
    settleCount++;
    if (verdict === "lock") lockCount++; else ruptureCount++;
    announceSettlement(node, rec, verdict);
    if (DEBUG) {
      console.log(
        `[outstanding] SETTLE ${verdict.toUpperCase()} ${node.place} / ${rec.label}` +
        ` claimed=${claimedPrecip} observed=${observedPrecip} station=${st.id}`
      );
    }
  }
}

function pruneSettled() {
  const now = Date.now();
  for (const [key, rec] of periods) {
    if (rec.settled && now > rec.flareUntilMs) {
      periods.delete(key);
      retired.set(key, {
        text: rec.text, percent: rec.percent, silent: rec.silent, retiredAtMs: now,
      });
      const node = nodes.get(placeKey(rec.office, rec.ugc));
      if (node) node.periodKeys = node.periodKeys.filter((k) => k !== key);
      fieldDirty = true;
    }
  }
  // bounded cleanup: a fingerprint whose key never reappears in a poll
  // (the source genuinely rolled it off) would otherwise sit here forever.
  for (const [key, r] of retired) {
    if (now - r.retiredAtMs >= RETIRE_HOLD_MS) retired.delete(key);
  }
}

// ---------------------------------------------------------------------
// ACCESSIBILITY — off-screen live region only. Never a visible caption.
// ---------------------------------------------------------------------
let announcedFirstLoad = false;
function announceIfFirstLoad() {
  if (announcedFirstLoad || periods.size === 0) return;
  announcedFirstLoad = true;
  const officeCount = new Set(Array.from(nodes.values()).map((n) => n.office)).size;
  say(`Field lit. ${nodes.size} places, ${periods.size} open forecast periods, across ${officeCount} offices. Nothing settled yet this session.`);
}
function announceSettlement(node, rec, verdict) {
  const word = verdict === "lock" ? "held" : "broke";
  const claim = rec.silent ? "a silence" : (rec.percent != null ? `a ${rec.percent} percent chance` : "a named chance");
  say(`${node.place}: ${rec.label.toLowerCase()} settled — ${claim} ${word}.`);
}
let sayQueue = [];
let sayTimer = null;
function say(text) {
  sayQueue.push(text);
  if (sayTimer) return;
  sayTimer = setTimeout(() => {
    liveRegion.textContent = sayQueue.join(" ");
    sayQueue = [];
    sayTimer = null;
  }, 400);
}

// ---------------------------------------------------------------------
// AUDIO — Web Audio. Lazy-started; resumed on first user gesture as a
// fallback since unattended playback may be blocked until then. Two
// timbres only: a clean steady tone for a lock, a rougher spreading one
// for a rupture — the same distinction the light carries.
// ---------------------------------------------------------------------
let actx = null;
let voiceCount = 0;
const MAX_VOICES = 8;

function ensureAudio() {
  if (actx) return actx;
  try {
    actx = new (window.AudioContext || window.webkitAudioContext)();
  } catch (e) {
    return null;
  }
  return actx;
}
function tryResumeAudio() {
  const ctx = ensureAudio();
  if (ctx && ctx.state === "suspended") ctx.resume().catch(() => {});
}
["pointerdown", "keydown", "touchstart"].forEach((ev) =>
  window.addEventListener(ev, tryResumeAudio, { passive: true })
);
tryResumeAudio();

function playLockTone(pan) {
  const ctx = ensureAudio();
  if (!ctx || voiceCount >= MAX_VOICES) return;
  voiceCount++;
  const t0 = ctx.currentTime;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  const panner = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
  osc.type = "sine";
  osc.frequency.setValueAtTime(660, t0);
  gain.gain.setValueAtTime(0, t0);
  gain.gain.linearRampToValueAtTime(0.05, t0 + 0.01);
  gain.gain.exponentialRampToValueAtTime(0.0008, t0 + 0.5);
  osc.connect(gain);
  if (panner) { panner.pan.value = pan; gain.connect(panner); panner.connect(ctx.destination); }
  else gain.connect(ctx.destination);
  osc.start(t0);
  osc.stop(t0 + 0.55);
  osc.onended = () => { voiceCount--; osc.disconnect(); gain.disconnect(); if (panner) panner.disconnect(); };
}

function playRuptureTone(pan) {
  const ctx = ensureAudio();
  if (!ctx || voiceCount >= MAX_VOICES) return;
  voiceCount++;
  const t0 = ctx.currentTime;
  const gain = ctx.createGain();
  const panner = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
  gain.gain.setValueAtTime(0, t0);
  gain.gain.linearRampToValueAtTime(0.055, t0 + 0.008);
  gain.gain.exponentialRampToValueAtTime(0.0008, t0 + 0.75);
  const oscA = ctx.createOscillator();
  const oscB = ctx.createOscillator();
  oscA.type = "sawtooth"; oscB.type = "sawtooth";
  oscA.frequency.setValueAtTime(300, t0);
  oscB.frequency.setValueAtTime(300 * 1.019, t0); // slight detune -> beating, rougher
  const filt = ctx.createBiquadFilter();
  filt.type = "bandpass"; filt.frequency.value = 900; filt.Q.value = 0.7;
  oscA.connect(filt); oscB.connect(filt); filt.connect(gain);
  if (panner) { panner.pan.value = pan; gain.connect(panner); panner.connect(ctx.destination); }
  else gain.connect(ctx.destination);
  oscA.start(t0); oscB.start(t0);
  oscA.stop(t0 + 0.78); oscB.stop(t0 + 0.78);
  let ended = 0;
  const onEnd = () => { ended++; if (ended === 2) { voiceCount--; oscA.disconnect(); oscB.disconnect(); filt.disconnect(); gain.disconnect(); if (panner) panner.disconnect(); } };
  oscA.onended = onEnd; oscB.onended = onEnd;
}

// ---------------------------------------------------------------------
// FLARES — bounded list of active settle animations, drawn on the
// overlay canvas every frame; removed once their animation completes
// (independent of the underlying period's own longer afterglow removal).
// ---------------------------------------------------------------------
function spawnFlare(node, rec, verdict) {
  if (activeFlares.length >= MAX_ACTIVE_FLARES) activeFlares.shift();
  const ringR = ringRadius(rec.ringIndex);
  activeFlares.push({
    x: node.x, y: node.y, ringR, verdict,
    startMs: performance.now(),
    durMs: verdict === "lock" ? 900 : 1300,
    seed: seededFor(rec.office + rec.ugc + rec.label + rec.periodIndex)(),
  });
  const pan = W > 0 ? Math.max(-1, Math.min(1, (node.x / W) * 2 - 1)) : 0;
  if (verdict === "lock") playLockTone(pan); else playRuptureTone(pan);
}

// ---------------------------------------------------------------------
// RENDER
// ---------------------------------------------------------------------
const RING_BASE = 5.5, RING_GAP = 4.6, RING_LW_SILENT = 3.2;
function ringRadius(ringIndex) { return RING_BASE + ringIndex * RING_GAP; }

function colorFor(rec) {
  const cls = classify(rec);
  if (cls === "silent") {
    return { stroke: "rgba(150,161,189,0.20)", lw: RING_LW_SILENT, edge: "rgba(180,190,214,0.34)" };
  }
  if (cls === "numeric") {
    const p = Math.max(0, Math.min(100, rec.percent));
    const alpha = 0.22 + 0.6 * (p / 100);
    const lw = 2.4 + 2.0 * (p / 100);
    return { stroke: `hsla(42, 88%, 62%, ${alpha.toFixed(3)})`, lw, edge: null };
  }
  // word-only
  return { stroke: "hsla(192, 75%, 58%, 0.55)", lw: 3.0, edge: null };
}

function drawField() {
  fieldCtx.clearRect(0, 0, W, H);
  fieldCtx.fillStyle = "#05060a";
  fieldCtx.fillRect(0, 0, W, H);

  // group periods by node for one pass
  for (const node of nodes.values()) {
    if (!node.periodKeys.length) continue;
    const breathe = 0.5 + 0.5 * Math.sin(performance.now() / 4000 + node.phase);
    for (const key of node.periodKeys) {
      const rec = periods.get(key);
      // Settled claims are drawn by the overlay's afterglow instead (see
      // drawFlares) so a resolved ring reads as lock/rupture alone, not a
      // blend with its old open-claim colour.
      if (!rec || rec.settled) continue;
      const r = ringRadius(rec.ringIndex);
      const c = colorFor(rec);
      fieldCtx.beginPath();
      fieldCtx.arc(node.x, node.y, r, 0, Math.PI * 2);
      fieldCtx.lineWidth = c.lw;
      fieldCtx.strokeStyle = c.stroke;
      fieldCtx.globalAlpha = 0.72 + 0.28 * breathe; // slow idle breathing, seeded phase per node
      fieldCtx.stroke();
      if (c.edge) {
        fieldCtx.lineWidth = 1;
        fieldCtx.strokeStyle = c.edge;
        fieldCtx.stroke();
      }
      // Settled rings keep their afterglow painted on the overlay canvas
      // (drawFlares), not here — this layer only redraws on data change,
      // the overlay redraws every frame so the fade reads smoothly.
    }
    fieldCtx.globalAlpha = 1;
    // core dot marking the place itself
    fieldCtx.beginPath();
    fieldCtx.arc(node.x, node.y, 1.6, 0, Math.PI * 2);
    fieldCtx.fillStyle = "rgba(220,226,242,0.5)";
    fieldCtx.fill();
  }
}

function drawFlares(nowPerf) {
  flareCtx.clearRect(0, 0, W, H);
  for (let i = activeFlares.length - 1; i >= 0; i--) {
    const f = activeFlares[i];
    const t = (nowPerf - f.startMs) / f.durMs;
    if (t >= 1) { activeFlares.splice(i, 1); continue; }
    const ease = 1 - Math.pow(1 - t, 3);
    if (f.verdict === "lock") {
      const r = f.ringR + ease * 3;
      flareCtx.beginPath();
      flareCtx.arc(f.x, f.y, r, 0, Math.PI * 2);
      flareCtx.lineWidth = 3.4;
      flareCtx.strokeStyle = `rgba(255,224,140,${(1 - ease) * 0.9})`;
      flareCtx.stroke();
      flareCtx.beginPath();
      flareCtx.arc(f.x, f.y, 2.2, 0, Math.PI * 2);
      flareCtx.fillStyle = `rgba(255,240,200,${(1 - ease) * 0.95})`;
      flareCtx.fill();
    } else {
      // rupture: sharper, spreads further, more saturated, brief particle scatter
      const r = f.ringR + ease * (14 + 10 * f.seed);
      flareCtx.beginPath();
      flareCtx.arc(f.x, f.y, r, 0, Math.PI * 2);
      flareCtx.lineWidth = 2.6;
      flareCtx.strokeStyle = `rgba(255,70,110,${(1 - ease) * 0.85})`;
      flareCtx.stroke();
      const nParticles = 5;
      for (let p = 0; p < nParticles; p++) {
        const ang = (p / nParticles) * Math.PI * 2 + f.seed * Math.PI * 2;
        const pr = r * (0.6 + 0.4 * ((p * 37 + 13) % 7) / 7);
        flareCtx.beginPath();
        flareCtx.arc(f.x + Math.cos(ang) * pr, f.y + Math.sin(ang) * pr, 1.3, 0, Math.PI * 2);
        flareCtx.fillStyle = `rgba(255,120,140,${(1 - ease) * 0.7})`;
        flareCtx.fill();
      }
    }
  }
  // afterglow: settled periods still inside their (longer) afterglow window
  // paint a small steady/decaying core independent of the short flare burst
  const now = Date.now();
  for (const rec of periods.values()) {
    if (!rec.settled) continue;
    const remain = rec.flareUntilMs - now;
    if (remain <= 0) continue;
    const total = rec.settled.verdict === "lock" ? AFTERGLOW_LOCK_MS : AFTERGLOW_RUPTURE_MS;
    const life = Math.max(0, Math.min(1, remain / total));
    const node = nodes.get(placeKey(rec.office, rec.ugc));
    if (!node) continue;
    const r = ringRadius(rec.ringIndex);
    flareCtx.beginPath();
    flareCtx.arc(node.x, node.y, r, 0, Math.PI * 2);
    flareCtx.lineWidth = rec.settled.verdict === "lock" ? 2.2 : 2.6;
    const col = rec.settled.verdict === "lock"
      ? `rgba(255,222,140,${(0.16 + 0.5 * life).toFixed(3)})`
      : `rgba(255,90,120,${(0.14 + 0.55 * life).toFixed(3)})`;
    flareCtx.strokeStyle = col;
    flareCtx.stroke();
  }
}

function frame() {
  const nowPerf = performance.now();
  if (fieldDirty) { drawField(); fieldDirty = false; }
  // idle breathing means the calm layer is cheap but not perfectly static;
  // redraw it at a low throttled cadence rather than every rAF tick.
  drawFlares(nowPerf);
  requestAnimationFrame(frame);
}
setInterval(() => { fieldDirty = true; }, 700); // slow breathing redraw cadence

// ---------------------------------------------------------------------
// HELD-NODE INTERACTION — the record's own sentence, verbatim.
// ---------------------------------------------------------------------
let heldNode = null;
let heldPointerId = null;

function hitTest(px, py) {
  let best = null, bestD = Infinity;
  for (const node of nodes.values()) {
    const maxR = node.periodKeys.length
      ? Math.max(14, ringRadius(Math.max(...node.periodKeys.map((k) => (periods.get(k) || { ringIndex: 0 }).ringIndex))) + 6)
      : 14;
    const dx = node.x - px, dy = node.y - py;
    const d = Math.sqrt(dx * dx + dy * dy);
    if (d <= maxR && d < bestD) { bestD = d; best = node; }
  }
  return best;
}

function renderReveal(node, px, py) {
  const parts = [`<p class="reveal-place">${escapeHtml(node.place)}</p>`];
  const recs = node.periodKeys
    .map((k) => periods.get(k))
    .filter(Boolean)
    .sort((a, b) => a.periodIndex - b.periodIndex);
  for (const rec of recs) {
    const cls = rec.silent ? "reveal-text is-silent" : "reveal-text";
    parts.push(
      `<div class="reveal-period"><span class="reveal-label">${escapeHtml(rec.label)}</span><br>` +
      `<span class="${cls}">${escapeHtml(rec.text || "")}</span></div>`
    );
  }
  revealEl.innerHTML = parts.join("");
  positionReveal(px, py);
  revealEl.classList.add("showing");
}
function positionReveal(px, py) {
  const pad = 14;
  let left = px + pad, top = py + pad;
  const rect = revealEl.getBoundingClientRect();
  if (left + rect.width > W - 8) left = Math.max(8, px - rect.width - pad);
  if (top + rect.height > H - 8) top = Math.max(8, H - rect.height - 8);
  revealEl.style.left = left + "px";
  revealEl.style.top = top + "px";
}
function clearReveal() {
  revealEl.classList.remove("showing");
  revealEl.removeAttribute("style");
  revealEl.style.left = "-9999px";
}
function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function pointerToLocal(ev) {
  const rect = fieldCanvas.getBoundingClientRect();
  return [ev.clientX - rect.left, ev.clientY - rect.top];
}
flareCanvas.style.pointerEvents = "auto";
flareCanvas.addEventListener("pointerdown", (ev) => {
  const [px, py] = pointerToLocal(ev);
  const node = hitTest(px, py);
  if (!node) return;
  heldNode = node;
  heldPointerId = ev.pointerId;
  renderReveal(node, ev.clientX, ev.clientY);
  say(`Holding ${node.place}.`);
  ev.preventDefault();
});
window.addEventListener("pointermove", (ev) => {
  if (heldNode == null || ev.pointerId !== heldPointerId) return;
  positionReveal(ev.clientX, ev.clientY);
});
function releaseHold() {
  if (heldNode == null) return;
  heldNode = null;
  heldPointerId = null;
  clearReveal();
}
window.addEventListener("pointerup", releaseHold);
window.addEventListener("pointercancel", releaseHold);
window.addEventListener("blur", releaseHold);

// ---------------------------------------------------------------------
// DEBUG SURFACE — no visible UI carries this; a developer reads it from
// the console, per the brief's staleness/observability requirement.
// ---------------------------------------------------------------------
window.OUTSTANDING_DEBUG = {
  seed: SEED,
  get pollCount() { return pollCount; },
  get placeCount() { return nodes.size; },
  get openPeriods() { return Array.from(periods.values()).filter((r) => !r.settled).length; },
  get settledActive() { return Array.from(periods.values()).filter((r) => r.settled).length; },
  get settleCount() { return settleCount; },
  get lockCount() { return lockCount; },
  get ruptureCount() { return ruptureCount; },
  get forecastsGeneratedAt() { return forecastsGeneratedAt; },
  get stationsGeneratedAt() { return stationsGeneratedAt; },
  get forecastsStale() { return Date.now() - forecastsLastAdvanceMs > STALE_MS; },
  get stationsStale() { return settlementsPaused(); },
  get stationCount() { return stations.size; },
  get sessionStartedAt() { return new Date(sessionStartMs).toISOString(); },
  // developer/test convenience only — never rendered, never read aloud.
  listNodes() {
    return Array.from(nodes.values()).map((n) => ({
      office: n.office, ugc: n.ugc, place: n.place, x: n.x, y: n.y,
      periodCount: n.periodKeys.length,
    }));
  },
};
if (DEBUG) {
  setInterval(() => console.log("[outstanding]", JSON.stringify({
    poll: pollCount, places: nodes.size,
    open: window.OUTSTANDING_DEBUG.openPeriods,
    settled: settleCount, lock: lockCount, rupture: ruptureCount,
    stationsStale: window.OUTSTANDING_DEBUG.stationsStale,
  })), 10000);
}

// ---------------------------------------------------------------------
// BOOT
// ---------------------------------------------------------------------
async function pollOnce() {
  await Promise.all([pollForecasts(), pollStations()]);
  pruneSettled();
  settlePass();
}
function pollLoop() {
  pollOnce().finally(() => setTimeout(pollLoop, POLL_MS));
}

resize();
clearReveal();
pollLoop();
requestAnimationFrame(frame);
