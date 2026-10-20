// node verify_browser.mjs — TAKE COVER, AGAIN in a real browser at 390 px (light) and 1100 px (dark)
// Session 187: increment 1 (a county dealt, take cover / stay, the dark wait, the record's answer, the ledger).
import { createRequire } from 'module';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
import { dirname, join } from 'path'; import fs from 'fs'; import { fileURLToPath } from 'url';
const here = dirname(fileURLToPath(import.meta.url));
const S = JSON.parse(fs.readFileSync(join(here, 'summary.json')));
const D = JSON.parse(fs.readFileSync(join(here, 'data.js'), 'utf8').replace(/^window\.TCA=/, '').replace(/;\s*$/, ''));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--autoplay-policy=no-user-gesture-required', '--allow-file-access-from-files'] });
let pass = 0, fail = 0; const t = (n, ok) => { ok ? pass++ : fail++; console.log(ok ? 'ok  ' : 'FAIL', n) };

// data checks, outside the browser
t('data: arrays align', ['dur', 'met', 'rep', 'wfo'].every(k => D[k].length === D.issue.length) && D.issue.length === S.warnings);
t('data: met count', D.met.reduce((a, x) => a + x, 0) === S.met);
t('data: every met warning has a report, no empty one has', D.rep.every((r, i) => (r >= 0) === (D.met[i] === 1)));
t('data: county sequences in order of issue', D.counties.every(c => c[2].every((w, i) => i === 0 || D.issue[c[2][i - 1]] <= D.issue[w])));
t('data: durations 1..240', D.dur.every(x => x >= 1 && x <= 240));
let after3 = 0; for (const c of D.counties) { let r = 0; for (const w of c[2]) { if (D.met[w]) { if (r >= 3) after3++; r = 0; } else r++; } }
t('data: the fable count recomputed (' + after3 + ')', after3 === S.fable_met_after_3plus_empty);

const HOME = D.counties.find(c => c[1] === 'Cleveland OK');
for (const [w, scheme] of [[390, 'light'], [1100, 'dark']]) {
  const ctx = await b.newContext({ viewport: { width: w, height: 900 }, colorScheme: scheme });
  const p = await ctx.newPage(); const errs = [];
  p.on('pageerror', e => errs.push(String(e))); p.on('console', x => x.type() === 'error' && errs.push(x.text()));
  await p.goto('file://' + join(here, 'index.html') + '?speed=60&county=' + HOME[0]);
  await p.waitForSelector('#strip i');
  t(w + ' no errors on load', errs.length === 0);
  t(w + ' no horizontal overflow', await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
  t(w + ' in progress, dated, at the top', /In progress · increment 1 of 5 · 2026-10-20/.test(await p.locator('#wip').textContent()));
  t(w + ' Cleveland OK dealt with all its warnings', (await p.locator('#strip i').count()) === HOME[2].length &&
    (await p.locator('#cname').textContent()).includes(HOME[2].length + ' warnings'));
  const first = HOME[2][0];
  t(w + ' first warning shows its issued minutes', (await p.locator('#clen').textContent()).includes(`Issued for ${D.dur[first]} minutes`));
  // stay on the first
  await p.click('#stay');
  const a1 = await p.locator('#answer').textContent();
  t(w + ' the record answers after staying', D.met[first] ? a1.includes('A tornado was reported') && a1.includes('You stayed') : a1.startsWith('No tornado was reported'));
  // cover on the second; speed 60 makes a minute pass in a second of the test
  await p.click('#next');
  const second = HOME[2][1];
  await p.click('#cover');
  t(w + ' the dark comes up', await p.locator('#dark').isVisible());
  await p.waitForSelector('#dark', { state: 'hidden', timeout: 15000 });
  const a2 = await p.locator('#answer').textContent();
  t(w + ' after the full wait the answer, and the seconds paid', D.met[second] ? a2.includes('A tornado was reported') : a2.includes(`You sat ${D.dur[second]} seconds`));
  // cover and come out early on the third
  await p.click('#next'); await p.click('#cover'); await p.click('#out');
  const ledger = await p.locator('#ledger tbody tr').count();
  t(w + ' ledger holds three rows', ledger === 3);
  const tally = await p.locator('#tally').textContent();
  t(w + ' tally counts three answered', tally.includes('3warnings you have answered'));
  t(w + ' drift table drawn', (await p.locator('#drift tr').count()) === 6);
  t(w + ' the fable line carries the record count', (await p.locator('#fable').textContent()).includes(S.fable_met_after_3plus_empty.toLocaleString('en-US')));
  // persistence: reload keeps the county and the position
  await p.goto('file://' + join(here, 'index.html') + '?speed=60');
  await p.waitForSelector('#strip i');
  t(w + ' reload resumes the county at warning 4', (await p.locator('#cnum').textContent()).startsWith('Warning 4 of'));
  await p.click('#reset');
  t(w + ' reset starts again at 1', (await p.locator('#cnum').textContent()).startsWith('Warning 1 of'));
  await p.click('#deal');
  t(w + ' a dealt county has 20 or more warnings', parseInt((await p.locator('#cname').textContent()).split('·')[1]) >= 20);
  t(w + ' no errors after play', errs.length === 0);
  await p.screenshot({ path: join(here, `shot-${w}.png`), fullPage: false });
  await ctx.close();
}
await b.close();
console.log(`${pass}/${pass + fail}`); process.exit(fail ? 1 : 0);
