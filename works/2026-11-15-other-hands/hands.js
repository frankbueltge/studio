/* OTHER HANDS — the Studio, cycle 015. Own code, Apache-2.0, no library.
   One paragraph per incident, one word per report, set in the hand of whoever wrote it.
   Third state (the check): one rule for red (the harmed wrote it), seals placed by whom they land on
   (left margin: the person who used the AI; right margin: whoever made or ran it), larger marks,
   the estimate drawn as its range. Everything drawn follows from data.js; the only arbitrary thing is
   the length of a word. */
(function () {
  'use strict';
  var D = window.OH, M = D.meta, INC = D.inc;
  var C = { paper: '#f5f2ea', ink: '#1b1a17', soft: '#6d685d', type: '#9a958a', faint: '#d9d3c4', red: '#c4301c', blue: '#1d4fb8' };
  // Three of the 60 acts move in favour of the party they concern, read in the check (session 248) from the act
  // text in the Field's data77.js: 623 (a judge declined to sanction the filer), 1677 (a motion to dismiss a suit
  // against the maker; adjudication.json lists it as "for the maker"), 1694 (a court found the firm did not create
  // the entry). They are drawn as an empty ring on their side.
  var FOR = { 623: 1, 1677: 1, 1694: 1 };
  var sheet = document.getElementById('sheet'), sx = sheet.getContext('2d');
  var say = document.getElementById('say');
  var S = null;                       // sizes, set by the width
  var L = null;                       // the layout
  var layers = {};                    // offscreen canvases
  var LAYERS = ['years', 'type', 'hand', 'seal'];
  var alpha = { years: 1, type: 1, hand: 1, seal: 1 }, want = { years: 1, type: 1, hand: 1, seal: 1 };
  var reading = 'all', picked = -1, playing = false, shown = 0, raf = 0;
  var counts = {};                    // what was actually drawn, for the check

  function rnd(a, b) {                // a fixed number in [0,1) from two integers
    var x = (Math.imul(a + 1, 73856093) ^ Math.imul(b + 7, 19349663)) >>> 0;
    x = Math.imul(x ^ (x >>> 13), 1274126177) >>> 0; x ^= x >>> 16;
    return (x >>> 0) / 4294967296;
  }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

  /* what the first word of a paragraph is, by who wrote it */
  function firstKind(r) {
    if (r[4] === 'H') return 'H';                 // on a platform, by the person harmed
    if (r[9] === 'W') return 'W';                 // by the harmed, printed by a publication
    if (r[4] === 'm') return 'm';                 // the maker, on a platform
    if (r[4]) return 's';                         // on a platform, by someone else (a witness, a note, unreadable)
    var b = r[2][0];
    return b === 'r' ? 'p' : b === 'u' ? 'p' : b; // press and research are one grey
  }
  function sealKind(r) {
    if (r[5].indexOf('P') < 0) return '';
    return (r[6] === 'u' ? 'U' : 'K') + (FOR[r[0]] ? 'f' : r[7] === 'o' ? 'o' : 'c');
  }

  /* ---------- layout: one virtual column, cut into the columns that fit; each column has a seal margin on both sides ---------- */
  function sizes(W) {
    var phone = W < 520;
    return phone
      ? { phone: true, ROW: 5, BAR: 2.6, GAP: 1.8, PARA: 2, YEARH: 11, gut: 5, m: 9, target: 60, sc: 0.62, R: 4.2, hamp: 3.4, hlw: 1.5 }
      : { phone: false, ROW: 6.5, BAR: 3.2, GAP: 2.4, PARA: 3, YEARH: 13, gut: 10, m: 15, target: 150, sc: 1, R: 6.2, hamp: 5.2, hlw: 1.9 };
  }
  function layout(W) {
    var cols = Math.max(2, Math.floor((W + S.gut) / (S.target + 2 * S.m + S.gut)));
    var colW = (W - S.gut * (cols - 1)) / cols, cw = colW - 2 * S.m;
    var words = [], paras = [], years = [], seals = [];
    var y = 0, year = '';
    for (var i = 0; i < INC.length; i++) {
      var r = INC[i], id = r[0], hands = r[2];
      var yr = r[1].slice(0, 4);
      if (yr !== year) { year = yr; years.push({ y: y, t: yr }); y += S.YEARH; }
      var x = 0, y0 = y, items = [];
      if (!hands) items.push({ t: '0', l: 16 * S.sc });
      for (var j = 0; j < hands.length; j++) {
        var t = hands[j] === 'r' || hands[j] === 'u' ? 'p' : hands[j], l = (6 + rnd(id, j) * 9) * S.sc;
        if (j === 0) {
          l += 5 * S.sc; t = firstKind(r);
          if (t === 'H') l = (44 + rnd(id, 99) * 14) * S.sc;
          else if (t === 'W') l = (40 + rnd(id, 99) * 10) * S.sc;
          else if (t === 's') l = (18 + rnd(id, 99) * 8) * S.sc;
        }
        items.push({ t: t, l: Math.min(l, cw) });
      }
      for (var k = 0; k < items.length; k++) {
        var it = items[k];
        if (x > 0 && x + it.l > cw) { x = 0; y += S.ROW; }
        words.push({ x: x, y: y, l: it.l, t: it.t, i: i, k: k });
        x += it.l + S.GAP;
      }
      var sk = sealKind(r);
      if (sk) seals.push({ y: y0, t: sk, i: i, w: words.length });
      y += S.ROW + S.PARA;
      paras.push({ y0: y0, y1: y });
    }
    var hc = Math.ceil(y / cols / S.ROW) * S.ROW + S.ROW;
    return { W: W, cols: cols, colW: colW, cw: cw, gut: S.gut, m: S.m, hc: hc, H: hc + 10, words: words, paras: paras, years: years, seals: seals };
  }
  function place(v) {                 // virtual y -> the column's left edge (outside the margin) and y on the sheet
    var c = Math.min(L.cols - 1, Math.floor(v / L.hc));
    return { c0: c * (L.colW + L.gut), x: c * (L.colW + L.gut) + L.m, y: v - c * L.hc + 6 };
  }

  /* ---------- the marks ---------- */
  function scribble(g, x, y, l, id, amp, col, lw) {
    var f = 0.62 + rnd(id, 3) * 0.5, ph = rnd(id, 4) * 6.28, n = Math.ceil(l * 2);
    g.strokeStyle = col; g.lineWidth = lw; g.lineJoin = 'round'; g.lineCap = 'round';
    g.beginPath();
    for (var s = 0; s <= n; s++) {
      var t = s / 2, env = 0.55 + 0.45 * Math.sin(t * 0.21 + rnd(id, 5) * 6.28);
      var px = x + t + Math.sin(t * f + ph) * 1.7;
      var py = y + S.BAR / 2 - Math.cos(t * f + ph) * amp * env - Math.sin(t * 0.09 + ph) * 0.8;
      if (s) g.lineTo(px, py); else g.moveTo(px, py);
    }
    g.stroke();
  }
  function word(g, h, t, x, y, l, id) {   // one word, by who wrote its report
    counts[t] = (counts[t] || 0) + 1;
    if (t === 'p') { g.fillStyle = C.type; g.fillRect(x, y, l, S.BAR); }
    else if (t === 'm') { g.fillStyle = C.ink; g.fillRect(x, y - 0.4, l, S.BAR + 0.8); }
    else if (t === 'g') { g.fillStyle = C.blue; g.fillRect(x, y - 0.2, l, S.BAR + 0.4); }
    else if (t === 's') { scribble(g, x, y, l - 1, id, S.hamp * 0.4, C.type, 0.9); }
    else if (t === '0') { g.strokeStyle = C.type; g.lineWidth = 0.7; g.strokeRect(x + 0.5, y - 0.4, l - 1, S.BAR + 0.8); }
    else if (t === 'H') { scribble(h, x, y, l, id, S.hamp, C.red, S.hlw); }
    else if (t === 'W') {              // the harmed wrote it and a publication printed it: their hand in a frame of type
      g.strokeStyle = C.type; g.lineWidth = 1.2; g.strokeRect(x + 0.5, y - S.hamp * 0.75, l - 1, S.BAR + S.hamp * 1.5);
      scribble(h, x + 3, y, l - 7, id, S.hamp * 0.55, C.red, S.hlw * 0.9);
    }
    else if (t === 'G') {              // estimated, not found
      scribble(g, x, y, l, id, S.hamp, C.red, S.hlw * 0.8);
    }
  }
  function seal(g, t, cx, cy, R) {    // a public body's act; the side it stands on says on whom it lands
    counts[t] = (counts[t] || 0) + 1;
    g.fillStyle = C.blue; g.strokeStyle = C.blue; g.lineWidth = 1.4;
    if (t[1] === 'f') { g.beginPath(); g.arc(cx, cy, R - 0.7, 0, 6.2832); g.stroke(); return; }
    g.beginPath();
    if (t[1] === 'o') {                // begun, not concluded: half a seal, the open side toward the text
      var a = t[0] === 'U' ? Math.PI / 2 : -Math.PI / 2;
      g.arc(cx, cy, R, a, a + Math.PI); g.closePath(); g.fill();
      g.beginPath(); g.arc(cx, cy, R - 0.7, 0, 6.2832); g.lineWidth = 0.8; g.stroke();
    } else { g.arc(cx, cy, R, 0, 6.2832); g.fill(); }
  }
  function markWord(w) {
    var p = place(w.y), id = INC[w.i][0];
    word(layers.type.g, layers.hand.g, w.t, p.x + w.x, p.y, w.l, id * 31 + w.k);
  }
  function markSeal(s) {
    var p = place(s.y), left = s.t[0] === 'U';
    seal(layers.seal.g, s.t, left ? p.c0 + L.m / 2 : p.c0 + L.m + L.cw + L.m / 2, p.y + S.BAR / 2, S.R);
  }
  function yearsOn(g) {
    g.font = (S.phone ? 8 : 9) + 'px ui-monospace,Menlo,Consolas,monospace'; g.textBaseline = 'alphabetic';
    for (var i = 0; i < L.years.length; i++) {
      var p = place(L.years[i].y);
      g.fillStyle = C.ink; g.fillText(L.years[i].t, p.x, p.y + 6);
      g.fillStyle = C.faint; g.fillRect(p.x + 26, p.y + 3, L.cw - 26, 0.7);
    }
  }

  /* ---------- canvases ---------- */
  var DPR = 1;
  function make(name) {
    var c = document.createElement('canvas'); c.width = Math.round(L.W * DPR); c.height = Math.round(L.H * DPR);
    var g = c.getContext('2d'); g.setTransform(DPR, 0, 0, DPR, 0, 0);
    layers[name] = { c: c, g: g };
  }
  function drawAll() {
    LAYERS.forEach(function (k) { layers[k].g.clearRect(0, 0, L.W, L.H); });
    counts = {};
    yearsOn(layers.years.g);
    for (var i = 0; i < L.words.length; i++) markWord(L.words[i]);
    for (var j = 0; j < L.seals.length; j++) markSeal(L.seals[j]);
    shown = L.words.length;
  }
  function build() {
    var W = Math.floor(sheet.parentNode.clientWidth - 32);
    W = Math.max(280, Math.min(1100, W));
    S = sizes(W);
    DPR = Math.min(2, window.devicePixelRatio || 1);
    L = layout(W);
    sheet.style.height = L.H + 'px'; sheet.style.maxWidth = W + 'px';
    sheet.width = Math.round(W * DPR); sheet.height = Math.round(L.H * DPR);
    LAYERS.forEach(make);
    drawAll();
    window.__oh = { drawn: counts, words: L.words.length, cols: L.cols, height: L.H, seal: S.R };
    tally(); key();
    paint();
  }
  function paint() {
    sx.setTransform(1, 0, 0, 1, 0, 0);
    sx.fillStyle = C.paper; sx.fillRect(0, 0, sheet.width, sheet.height);
    LAYERS.forEach(function (k) { sx.globalAlpha = alpha[k]; sx.drawImage(layers[k].c, 0, 0); });
    sx.globalAlpha = 1;
    if (picked >= 0) {
      var pa = L.paras[picked], a = place(pa.y0), b = place(pa.y1 - S.PARA - 0.01);
      sx.setTransform(DPR, 0, 0, DPR, 0, 0);
      sx.strokeStyle = C.ink; sx.lineWidth = 1.5;
      if (a.c0 === b.c0) sx.strokeRect(a.c0 + 0.5, a.y - S.ROW, L.colW - 1, b.y - a.y + S.ROW * 2);
      else {
        sx.strokeRect(a.c0 + 0.5, a.y - S.ROW, L.colW - 1, L.hc - a.y + S.ROW);
        sx.strokeRect(b.c0 + 0.5, 0.5, L.colW - 1, b.y + S.ROW);
      }
    }
  }
  function tick() {
    var moving = false;
    LAYERS.forEach(function (k) {
      var d = want[k] - alpha[k];
      if (Math.abs(d) > 0.004) { alpha[k] += d * 0.14; moving = true; } else alpha[k] = want[k];
    });
    if (playing) { step(); moving = true; }
    paint();
    raf = moving ? requestAnimationFrame(tick) : 0;
  }
  function kick() { if (!raf) raf = requestAnimationFrame(tick); }

  /* ---------- the counts under the sheet, one mark per incident, counted from the rows ---------- */
  function onto(g, fn) {               // lend the marks a single canvas for a while
    var keep = layers, keepCounts = counts;
    layers = { type: { g: g }, hand: { g: g }, seal: { g: g }, years: { g: g } }; counts = {};
    fn();
    var c = counts; layers = keep; counts = keepCounts; return c;
  }
  function label(g, t, x, y, col, align) {
    g.font = (S.phone ? 9.5 : 11) + 'px ui-monospace,Menlo,Consolas,monospace'; g.textBaseline = 'alphabetic';
    g.textAlign = align || 'left'; g.fillStyle = col || C.ink; g.fillText(t, x, y); g.textAlign = 'left';
  }
  var ORDER = 'pgmsWH';
  function tally() {
    var c = document.getElementById('tally'), W = L.W, g = c.getContext('2d');
    var firsts = [];
    INC.forEach(function (r) { if (r[2]) firsts.push(firstKind(r)); });
    firsts.sort(function (a, b) { return ORDER.indexOf(a) - ORDER.indexOf(b); });
    var unit = S.phone ? 2.4 : 4, row = S.phone ? 9 : 12, LEN = { H: 30 * S.sc + 6, W: 30 * S.sc + 6, s: 9 * S.sc + 3 };
    var ops = [], labels = [], y = 22, x = 0;
    labels.push(['who wrote the first report of each incident · ' + fmt(firsts.length), 0, 11, C.ink]);
    firsts.forEach(function (t) {
      var l = LEN[t] || unit;
      if (x + l > W) { x = 0; y += row; }
      ops.push(['w', t, x, y, l]); x += l + ('pgm'.indexOf(t) >= 0 ? 1 : 3);
    });
    // the estimate as its range: at least, about, at most — not found
    y += 40; x = 0;
    var lo = M.estimate_lo - M.wrote_found, mid = M.estimate_not_found, hi = M.estimate_hi - M.wrote_found;
    labels.push(['written by the harmed and never found, estimated · at least ' + lo + ' · about ' + mid + ' · at most ' + hi, 0, y - 15, C.ink]);
    var gl = S.phone ? 15 : 24, gy = y, ghosts = { lo: 0, mid: 0, hi: 0 };
    for (var i = 0; i < hi; i++) {
      if (x + gl > W) { x = 0; y += row + 3; }
      var band = i < lo ? 'lo' : i < mid ? 'mid' : 'hi'; ghosts[band]++;
      ops.push(['g', band, x, y, gl]); x += gl + 4;
    }
    // what public bodies did: on the user at the left, on whoever made or ran it at the right
    y += 46;
    labels.push(['what public bodies did · ' + M.public_acted + ' acts', 0, y - 22, C.ink]);
    labels.push(['on the person who used the AI · ' + M.on_user, 0, y - 9, C.soft]);
    labels.push(['on whoever made or ran it · ' + M.on_maker, W, y - 9, C.soft, 'right']);
    var d = S.R * 2 + 3, perRow = Math.max(4, Math.floor((W / 2 - 20) / d));
    function group(list, right) {
      list.forEach(function (t, j) {
        var inRow = Math.min(perRow, list.length - Math.floor(j / perRow) * perRow);
        var cx = right ? W - inRow * d + S.R + 3 + (j % perRow) * d : S.R + (j % perRow) * d;
        ops.push(['s', t, cx, y + S.R + Math.floor(j / perRow) * d]);
      });
      return Math.ceil(list.length / perRow) * d;
    }
    var us = [], ks = [];
    INC.forEach(function (r) { var k = sealKind(r); if (!k) return; (k[0] === 'U' ? us : ks).push(k); });
    var so = { Uc: 0, Uo: 1, Uf: 2, Kc: 0, Ko: 1, Kf: 2 };
    us.sort(function (a, b) { return so[a] - so[b]; }); ks.sort(function (a, b) { return so[a] - so[b]; });
    var h1 = group(us, false), h2 = group(ks, true);
    var H = y + Math.max(h1, h2) + 8;
    c.style.height = H + 'px'; c.style.maxWidth = W + 'px';
    c.width = Math.round(W * DPR); c.height = Math.round(H * DPR);
    g.setTransform(DPR, 0, 0, DPR, 0, 0);
    window.__oh.tally = onto(g, function () {
      ops.forEach(function (o, n) {
        if (o[0] === 'w') word(g, g, o[1], o[2], o[3], o[4], 900000 + n);
        else if (o[0] === 'g') { g.save(); g.globalAlpha = o[1] === 'lo' ? 0.55 : o[1] === 'mid' ? 0.28 : 0.1; word(g, g, 'G', o[2], o[3], o[4], 800000 + n); g.restore(); }
        else seal(g, o[1], o[2], o[3], S.R);
      });
    });
    window.__oh.ghosts = ghosts;
    labels.forEach(function (l) { label(g, l[0], l[1], l[2], l[3], l[4]); });
  }

  /* ---------- the key: who wrote, who acted ---------- */
  var KEY = [
    ['p', 'the press or research'], ['m', 'the maker'], ['g', 'a public body'], ['s', 'on a platform, someone else'],
    ['H', 'the harmed'], ['W', 'the harmed, printed by a publication'],
    ['Uc', 'act on the person who used the AI (left)'], ['Kc', 'act on whoever made or ran it (right)'],
    ['Uo', 'half: begun, not concluded'], ['Kf', 'empty: in the party\'s favour']
  ];
  function key() {
    var c = document.getElementById('key'), W = L.W, g = c.getContext('2d');
    var fs = S.phone ? 10 : 11.5;
    g.font = fs + 'px ui-monospace,Menlo,Consolas,monospace';
    var x = 0, y = 14, pos = [], lh = S.phone ? 17 : 20;
    KEY.forEach(function (k) {
      var seal = k[0].length > 1;
      var l = seal ? S.R * 2 : k[0] === 'H' || k[0] === 'W' ? 34 * Math.max(S.sc, 0.8) : 18;
      var w = l + 6 + g.measureText(k[1]).width + 18;
      if (x + w - 18 > W && x > 0) { x = 0; y += lh; }
      pos.push({ t: k[0], seal: seal, x: x, y: y, l: l, text: k[1] }); x += w;
    });
    var H = y + 10;
    c.style.height = H + 'px'; c.style.maxWidth = W + 'px';
    c.width = Math.round(W * DPR); c.height = Math.round(H * DPR);
    g.setTransform(DPR, 0, 0, DPR, 0, 0);
    onto(g, function () {
      pos.forEach(function (p, n) {
        if (p.seal) seal(g, p.t, p.x + S.R, p.y - S.BAR / 2 + 1, S.R);
        else word(g, g, p.t, p.x, p.y - S.BAR, p.l, 700000 + n);
      });
    });
    g.font = fs + 'px ui-monospace,Menlo,Consolas,monospace'; g.textBaseline = 'alphabetic'; g.fillStyle = C.ink;
    pos.forEach(function (p) { g.fillText(p.text, p.x + p.l + 6, p.y + 2); });
  }

  /* ---------- readings, stepping, pointing ---------- */
  var sets = { all: [], hand: [], seal: [] };
  INC.forEach(function (r, i) { sets.all.push(i); var f = r[2] ? firstKind(r) : ''; if (f === 'H' || f === 'W') sets.hand.push(i); if (sealKind(r)) sets.seal.push(i); });
  var FIRST = { p: 'the press or another edited address', r: 'a research address', m: 'the maker\'s own address', g: 'a public body\'s address', s: 'a platform without an editor', u: 'an unknown address' };
  var VOICE = {
    W: 'Read by the Field: <span class="hand">written by the harmed</span>, printed by a publication',
    q: 'Read by the Atelier: the harmed speak in it in their own words',
    b: 'Read by the Atelier: the harmed is an organisation, and its statement is quoted',
    o: 'Read by the Atelier: the harmed\'s words reach it through someone else',
    f: 'Read by the Field: it quotes or carries words of the harmed',
    e: 'Read for the harmed\'s words: none'
  };
  var HAND = { H: 'the person harmed', w: 'a witness', n: 'the database\'s own note', x: 'unreadable in the snapshot', m: 'the maker, on a platform' };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function describe(i) {
    var r = INC[i], n = r[2].length, s = '<b>Incident ' + r[0] + '</b> · ' + r[1] + ' · ' + n + (n === 1 ? ' report' : ' reports') + '. ';
    if (!n) s += 'No report is attached. ';
    else {
      s += 'First written from ' + FIRST[r[2][0]];
      if (r[4]) s += ', by ' + (r[4] === 'H' ? '<span class="hand">' + HAND.H + '</span>' : HAND[r[4]]) + (D.na[r[0]] ? ' (' + esc(D.na[r[0]]) + ')' : '');
      s += '. ';
      if (r[9]) s += VOICE[r[9]] + (D.nv[r[0]] ? ' (' + esc(D.nv[r[0]]) + ')' : '') + '. ';
    }
    var k = sealKind(r);
    if (k) {
      var a2 = D.act[r[0]];
      s += '<span class="seal">' + esc(a2[0]) + '</span>: ' + esc(a2[1]) + (a2[2] ? ' (' + esc(a2[2]) + ')' : '') + '. ' +
        (k[1] === 'f' ? 'An act in favour of ' + (r[6] === 'u' ? 'the person who used the AI' : 'whoever made or ran it') + ', not against them' :
          (r[7] === 'c' ? 'Concluded' : 'Begun, not concluded in the record') + ', on ' +
          (r[6] === 'u' ? 'the person who used the AI' : r[8].indexOf('b') >= 0 ? 'whoever ran it, itself a public body' : r[8].indexOf('g') >= 0 ? 'a maker of a general model' : 'whoever made or ran it')) + '. ';
    }
    return s + '<a href="https://incidentdatabase.ai/cite/' + r[0] + '/" target="_blank" rel="noopener">Open it in the database</a>';
  }
  var REST = {
    all: function () { return fmt(M.incidents) + ' incidents, ' + fmt(M.words) + ' reports. ' + (('ontouchstart' in window) ? 'Tap' : 'Point at') + ' a paragraph, or step with the arrows.'; },
    hand: function () { return 'The type is lifted off. What stays: <span class="hand">' + M.wrote_found + ' first reports the harmed wrote</span>, of ' + M.first_read + ' read for it. ' + fmt(M.with_report - M.first_read) + ' were never read for it.'; },
    seal: function () { return 'What stays: <span class="seal">' + M.public_acted + ' acts of public bodies</span>, ' + M.on_user + ' at the left, ' + M.on_maker + ' at the right.'; }
  };
  function rest() { say.innerHTML = REST[reading](); }
  function setReading(r) {
    reading = r; picked = -1;
    want = r === 'all' ? { years: 1, type: 1, hand: 1, seal: 1 } : r === 'hand' ? { years: 0.5, type: 0.035, hand: 1, seal: 0 } : { years: 0.5, type: 0.05, hand: 0.1, seal: 1 };
    [['rAll', 'all'], ['rHand', 'hand'], ['rSeal', 'seal']].forEach(function (b) { document.getElementById(b[0]).setAttribute('aria-pressed', String(b[1] === r)); });
    rest(); kick();
  }
  function pick(i, scroll) {
    picked = i;
    if (i < 0) { rest(); } else {
      say.innerHTML = describe(i);
      if (scroll) {
        var p = place(L.paras[i].y0), rct = sheet.getBoundingClientRect();
        var top = rct.top + window.scrollY + p.y - window.innerHeight * 0.55;
        if (Math.abs(top - window.scrollY) > window.innerHeight * 0.3) { quiet = performance.now() + 1200; window.scrollTo({ top: top, behavior: 'smooth' }); }
      }
      if (snd.on) voice(INC[i]);
    }
    kick();
  }
  function stepSet(d) {
    var s = sets[reading], at = s.indexOf(picked);
    if (at < 0) {
      at = d > 0 ? -1 : s.length;
      if (picked >= 0) for (var i = 0; i < s.length; i++) { if (s[i] < picked) at = d > 0 ? i : i + 1; }
    }
    pick(s[(at + d + s.length) % s.length], true);
  }
  function hit(e) {
    var rc = sheet.getBoundingClientRect(), px = e.clientX - rc.left, py = e.clientY - rc.top;
    var c = Math.floor(px / (L.colW + L.gut));
    if (c < 0 || c >= L.cols || px - c * (L.colW + L.gut) > L.colW + 2) return -1;
    var v = c * L.hc + py - 6, lo = 0, hi = L.paras.length - 1;
    while (lo < hi) { var m = (lo + hi) >> 1; if (L.paras[m].y1 <= v) lo = m + 1; else hi = m; }
    return (v >= L.paras[lo].y0 - 3 && v < L.paras[lo].y1) ? lo : -1;
  }
  var quiet = 0;
  sheet.addEventListener('mousemove', function (e) { if (playing || performance.now() < quiet) return; var i = hit(e); if (i !== picked && (i >= 0 || !('ontouchstart' in window))) pick(i, false); });
  sheet.addEventListener('mouseleave', function () { if (!playing && performance.now() >= quiet && !('ontouchstart' in window)) pick(-1, false); });
  sheet.addEventListener('click', function (e) { if (playing) return; pick(hit(e), false); });

  /* ---------- sound: keys for type, a pen for the harmed, a stamp for a seal (left or right by whom it lands on) ---------- */
  var snd = { on: false, ac: null, noise: null, out: null };
  function soundOn() {
    if (!snd.ac) {
      var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return;
      snd.ac = new AC();
      var n = snd.ac.sampleRate * 2, b = snd.ac.createBuffer(1, n, snd.ac.sampleRate), d = b.getChannelData(0);
      for (var i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
      snd.noise = b; snd.out = snd.ac.createGain(); snd.out.gain.value = 0.8; snd.out.connect(snd.ac.destination);
    }
    snd.ac.resume(); snd.on = true;
  }
  function burst(freq, q, dur, gain, pan, when, shape) {
    var ac = snd.ac, t = ac.currentTime + (when || 0), s = ac.createBufferSource(); s.buffer = snd.noise;
    var f = ac.createBiquadFilter(); f.type = 'bandpass'; f.frequency.value = freq; f.Q.value = q;
    var g = ac.createGain(); g.gain.setValueAtTime(0.0001, t);
    if (shape === 'pen') {
      var k = 7, u = dur / k;
      for (var i = 0; i < k; i++) { g.gain.linearRampToValueAtTime(gain * (0.45 + 0.55 * Math.random()), t + i * u + u * 0.3); g.gain.linearRampToValueAtTime(gain * 0.12, t + (i + 1) * u); }
      f.frequency.setValueAtTime(freq, t); f.frequency.linearRampToValueAtTime(freq * 1.5, t + dur);
    } else { g.gain.exponentialRampToValueAtTime(gain, t + 0.002); }
    g.gain.exponentialRampToValueAtTime(0.0001, t + dur + 0.02);
    var last = g;
    if (pan && ac.createStereoPanner) { var p = ac.createStereoPanner(); p.pan.value = pan; g.connect(p); last = p; }
    s.connect(f); f.connect(g); last.connect(snd.out);
    s.start(t, Math.random() * 1.5, dur + 0.05);
  }
  function thud(pan) {
    var ac = snd.ac, t = ac.currentTime, o = ac.createOscillator(), g = ac.createGain();
    o.frequency.setValueAtTime(120, t); o.frequency.exponentialRampToValueAtTime(46, t + 0.18);
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.7, t + 0.006); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.34);
    var last = g; if (ac.createStereoPanner) { var p = ac.createStereoPanner(); p.pan.value = pan; g.connect(p); last = p; }
    o.connect(g); last.connect(snd.out); o.start(t); o.stop(t + 0.4);
    burst(900, 0.7, 0.03, 0.25, pan, 0);
  }
  function voice(r) {
    var f = r[2] ? firstKind(r) : '';
    if (f === 'H' || f === 'W') burst(2300, 1.6, 0.55, 0.5, 0, 0, 'pen'); else burst(3600, 2.5, 0.014, 0.12, 0, 0);
    if (sealKind(r)) setTimeout(function () { thud(r[6] === 'u' ? -0.75 : 0.75); }, 180);
  }

  /* ---------- the sheet writes itself ---------- */
  var t0 = 0, DUR = 32000, sealAt = 0;
  function play() {
    playing = true; picked = -1; shown = 0; sealAt = 0; t0 = performance.now();
    LAYERS.forEach(function (k) { layers[k].g.clearRect(0, 0, L.W, L.H); });
    counts = {}; yearsOn(layers.years.g);
    document.getElementById('bPlay').setAttribute('aria-pressed', 'true');
    document.getElementById('bPlay').textContent = 'stop';
    say.setAttribute('aria-live', 'off');
    kick();
  }
  function stop() {
    drawAll(); playing = false;
    document.getElementById('bPlay').setAttribute('aria-pressed', 'false');
    document.getElementById('bPlay').textContent = window.innerWidth < 520 ? 'write' : 'write it from 1983';
    say.setAttribute('aria-live', 'polite');
    rest();
  }
  function step() {
    var p = Math.min(1, (performance.now() - t0) / DUR);
    // the first decades are few paragraphs: they get four seconds, not ten
    var e = p < 0.12 ? (p / 0.12) * 0.035 : 0.035 + (p - 0.12) / 0.88 * 0.965;
    var to = Math.floor(e * L.words.length), keys = 0, hands = 0, pan = 0, seals = 0;
    for (var i = shown; i < to; i++) {
      var w = L.words[i]; markWord(w);
      if (w.t === 'H' || w.t === 'W') hands++; else keys++;
    }
    while (sealAt < L.seals.length && L.seals[sealAt].w <= to) { markSeal(L.seals[sealAt]); pan = L.seals[sealAt].t[0] === 'U' ? -0.75 : 0.75; seals++; sealAt++; }
    if (to > shown) {
      var r = INC[L.words[to - 1].i], h = (counts.H || 0) + (counts.W || 0), sc = sealAt;
      say.innerHTML = '<b>' + r[1].slice(0, 4) + '</b> · ' + fmt(L.words[to - 1].i + 1) + ' incidents · <span class="hand">' + h + ' by the harmed</span> · <span class="seal">' + sc + ' acts</span>';
      if (snd.on) {
        for (var k = 0; k < Math.min(keys, 4); k++) burst(3000 + Math.random() * 1800, 2.5, 0.012, 0.05, Math.random() * 0.6 - 0.3, k * 0.012);
        if (hands) burst(2300, 1.6, 0.6, 0.6, 0, 0, 'pen');
        if (seals) thud(pan);
      }
    }
    shown = to;
    if (p >= 1) stop();
  }

  /* ---------- wiring ---------- */
  document.getElementById('rAll').addEventListener('click', function () { setReading('all'); });
  document.getElementById('rHand').addEventListener('click', function () { setReading('hand'); });
  document.getElementById('rSeal').addEventListener('click', function () { setReading('seal'); });
  document.getElementById('bPrev').addEventListener('click', function () { if (playing) stop(); stepSet(-1); });
  document.getElementById('bNext').addEventListener('click', function () { if (playing) stop(); stepSet(1); });
  document.getElementById('bPlay').addEventListener('click', function () { if (playing) { stop(); kick(); } else play(); });
  document.getElementById('bSound').addEventListener('click', function () {
    if (snd.on) { snd.on = false; } else soundOn();
    this.setAttribute('aria-pressed', String(snd.on));
  });
  document.addEventListener('keydown', function (e) {
    if (e.target && /INPUT|TEXTAREA/.test(e.target.tagName)) return;
    if (e.key === 'ArrowRight') { if (playing) stop(); stepSet(1); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { if (playing) stop(); stepSet(-1); e.preventDefault(); }
  });
  var flat = {
    press_research: M.first.press + M.first.research, public: M.first.public, maker: M.first.maker, self: M.first.self,
    not_found_lo: M.estimate_lo - M.wrote_found, not_found_hi: M.estimate_hi - M.wrote_found,
    for_party: Object.keys(FOR).length
  };
  Array.prototype.forEach.call(document.querySelectorAll('[data-n]'), function (el) {
    var k = el.getAttribute('data-n'); el.textContent = fmt(k in flat ? flat[k] : M[k]);
  });
  // on a phone the buttons say less, so that the bar holds one row and the sheet keeps the screen
  var SHORT = { rAll: 'all', rHand: 'the harmed', rSeal: 'public bodies', bPlay: 'write', bSound: 'sound' }, LONG = {};
  function labels() {
    var phone = window.innerWidth < 520;
    Object.keys(SHORT).forEach(function (id) {
      var el = document.getElementById(id); if (!(id in LONG)) LONG[id] = el.textContent;
      if (id === 'bPlay' && playing) return;
      el.textContent = phone ? SHORT[id] : LONG[id];
    });
  }
  var lastW = 0, rt = 0;
  function rebuild() { var w = sheet.parentNode.clientWidth; if (w === lastW) return; lastW = w; labels(); if (playing) stop(); picked = -1; build(); rest(); }
  window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(rebuild, 150); });
  labels(); lastW = sheet.parentNode.clientWidth; build(); rest();
})();
