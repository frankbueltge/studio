// OTHER HANDS — open the page as a visitor does and compare what it says and draws with the Field's and the Atelier's files.
// Usage (repo root): node works/2026-11-15-other-hands/verify.mjs [out-dir-for-stills]
// The siblings' results are fetched from their repositories at the commits data.js names, not from this work's data.
// Third state (the check, session 248): one red rule, seals by side, three acts in the party's favour, the estimate as a range.
import { createRequire } from 'module'; import path from 'path'; import { fileURLToPath } from 'url';
const require = createRequire('/opt/node-tools/node_modules/'); const { chromium } = require('playwright');
const here = path.dirname(fileURLToPath(import.meta.url)); const out = process.argv[2];
const browser = await chromium.launch(); let bad = 0;
const ok = (name, cond, detail) => { if (!cond) bad++; console.log((cond ? 'ok   ' : 'FAIL ') + name + (detail ? ' — ' + detail : '')); };
// The three acts read in the check as in the party's favour, and the words of the Field's act text that say so.
const FOR = { 623: /declined to sanction/, 1677: /dismiss/, 1694: /did not create/ };
// The two press first reports by the harmed that are a publication writing about harm done to itself.
const SELF_PUBLICATION = { 1715: /Mother Jones/, 1725: /Policy Options/ };
let R77 = null, R75 = null, RA = null, ADJ = null, D77 = null, PS = null;
for (const [w, h] of [[1132, 900], [390, 800]]) {
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  const errors = []; page.on('pageerror', e => errors.push(String(e))); page.on('console', m => m.type() === 'error' && errors.push(m.text()));
  await page.goto('file://' + path.join(here, 'index.html')); await page.waitForTimeout(400);
  const M = await page.evaluate(() => OH.meta);
  if (!R77) {
    const base = `https://raw.githubusercontent.com/frankbueltge/field-research/${M.field_commit}/artifacts/cycle-015/what-harm-is-on-record/`;
    R77 = await (await fetch(base + 'results77.json')).json(); R75 = await (await fetch(base + 'results75.json')).json();
    ADJ = await (await fetch(base + 'check77/adjudication.json')).json();
    PS = await (await fetch(base + 'check77/press-sample.json')).json();
    const t = await (await fetch(base + 'data77.js')).text(); D77 = JSON.parse(t.slice(t.indexOf('=') + 1).trim().replace(/;$/, ''));
    RA = (await (await fetch(`https://raw.githubusercontent.com/frankbueltge/ulysses/${M.atelier_commit}/artifacts/cycle-015/named-for-them/check.json`)).json()).res;
  }
  const B = R77.B, P = R77.press, V = RA.voice, WR = R77.whole_record, FR = R75.first_reporter;
  const acts = Object.fromEntries(D77.acts.map(a => [a[0], a]));
  const forIds = Object.keys(FOR).map(Number);
  ok(`${w}px the acts in the party's favour, read from the Field's act text`, forIds.every(i => acts[i] && FOR[i].test(acts[i][4])) && ADJ.frontier.general_model_makers.for_the_maker.includes(1677), forIds.map(i => acts[i] && acts[i][4]).join(' | '));
  const found = R77.A.final_harmed + P.harmed;
  const field = {
    with_report: R75.incidents_with_first_report, press_research: FR['press and other'] + FR.research, public: FR['public body'],
    maker: FR.maker, self: FR['self-published'], wrote_found: found,
    first_read: R77.A.agreement.n + P.drawn + V.own + V.body + V.other + V.none - M.read_twice,
    estimate: WR.estimate, estimate_lo: WR.estimate_ci[0], estimate_hi: WR.estimate_ci[1],
    not_found_lo: WR.estimate_ci[0] - found, not_found_hi: WR.estimate_ci[1] - found,
    public_acted: B.public_final, on_user: B.target.user, on_maker: B.target.maker,
    user_opened: B.state['user opened'], maker_opened: B.state['maker opened'], for_party: forIds.length,
  };
  // the numbers a visitor reads, read from the page
  const said = await page.evaluate(() => [...document.querySelectorAll('[data-n]')].map(e => [e.dataset.n, +e.textContent.replace(/,/g, '')]));
  for (const [k, v] of said) ok(`${w}px number ${k}`, k in field && v === field[k], `${v} on the page, ${field[k]} in the siblings' files`);
  // what was drawn on the sheet
  const d = await page.evaluate(() => window.__oh), s = d.drawn, t = d.tally;
  const n = k => s[k] || 0;
  const forUser = forIds.filter(i => acts[i][6] === 'user'), forMaker = forIds.filter(i => acts[i][6] === 'maker');
  const opened = i => acts[i][8] === 'opened';
  ok(`${w}px sheet: the harmed's hand`, n('H') === R77.A.final_harmed && n('W') === P.harmed, `${n('H')} + ${n('W')}`);
  ok(`${w}px sheet: seals left and right`, n('Uc') + n('Uo') + n('Uf') === B.target.user && n('Kc') + n('Ko') + n('Kf') === B.target.maker, `${n('Uc')}/${n('Uo')}/${n('Uf')} left, ${n('Kc')}/${n('Ko')}/${n('Kf')} right`);
  ok(`${w}px sheet: half seals and empty rings`, n('Uf') === forUser.length && n('Kf') === forMaker.length &&
    n('Uo') === B.state['user opened'] - forUser.filter(opened).length && n('Ko') === B.state['maker opened'] - forMaker.filter(opened).length);
  const words = ['p', 'm', 'g', 's', 'H', 'W'].reduce((a, k) => a + n(k), 0);
  ok(`${w}px sheet: one word per attached report`, words === M.words && words === 6964, `${words}`);
  ok(`${w}px sheet: paragraphs without a report`, n('0') === R75.incidents - R75.incidents_with_first_report);
  ok(`${w}px sheet: marks large enough`, d.seal >= (w < 520 ? 4 : 6), `seal radius ${d.seal}`);
  // the counts under the sheet
  const firsts = ['p', 'm', 'g', 's', 'H', 'W'].reduce((a, k) => a + (t[k] || 0), 0);
  ok(`${w}px counts: first reports`, firsts === field.with_report && t.H === R77.A.final_harmed && t.W === P.harmed && t.m === FR.maker + R77.A.final_codes.maker && t.g === FR['public body'], `${firsts}`);
  const gh = d.ghosts;
  ok(`${w}px counts: the estimate drawn as its range`, t.G === field.not_found_hi && gh.lo === field.not_found_lo && gh.lo + gh.mid === WR.estimate - found, JSON.stringify(gh));
  ok(`${w}px counts: seals`, (t.Uc || 0) + (t.Uo || 0) + (t.Uf || 0) === B.target.user && (t.Kc || 0) + (t.Ko || 0) + (t.Kf || 0) === B.target.maker);
  // the sentences of the check, against the files
  const text = await page.evaluate(() => document.body.textContent.replace(/\s+/g, ' '));
  const selfPub = Object.keys(SELF_PUBLICATION).map(Number);
  const writers = Object.fromEntries(PS.items.map(i => [i.id, i]));
  ok(`${w}px check: two of the press four are a publication on itself`, selfPub.every(i => P.harmed_ids.includes(i) && SELF_PUBLICATION[i].test(writers[i].writer)) && text.includes('Two of the 4') && text.includes('(1715, 1725)'));
  const persons = P.harmed - selfPub.length, est = R77.A.final_harmed + Math.round(persons / P.drawn * P.population);
  ok(`${w}px check: about 26 when only people count`, est - (R77.A.final_harmed + persons) === 26 && text.includes('about 26 not found'), `${est}`);
  ok(`${w}px check: what held`, text.includes(`kappa ${R77.A.agreement.kappa}`) && R77.A.final_harmed - R77.A.final_harmed_firm === 2 && text.includes('marks two as borderline') &&
    text.includes(`(1,801; ${FR['press and other'].toLocaleString('en-US')}, ${FR['public body']}, ${FR.research}, ${FR.maker}, ${FR['self-published']})`) &&
    text.includes(`${B.public_final} public acts, ${B.target.user} and ${B.target.maker}, ${B.state['user opened'] + B.state['maker opened']} only begun`) && text.includes(`207 read (58 + 120 + 30, one read twice)`));
  ok(`${w}px check: the two rules`, text.includes(`the Field's ${P.own_words - P.harmed} that quote or carry, the Atelier's ${V.own} own words`));
  ok(`${w}px check: the same arrest twice`, acts[1500][4] === acts[1501][4] && acts[1500][5] === acts[1501][5] && text.includes('(1500, 1501)'));
  ok(`${w}px check: answers were the first reading`, B.counts.M.first === 79 && B.counts.O.first === 65 && text.includes('79 and 65 were the first reading'));
  const yr = await page.evaluate(() => [OH.inc.filter(r => r[1].slice(0, 4) === '2025').length, OH.inc.filter(r => r[1].slice(0, 4) <= '2021').length]);
  ok(`${w}px text: 2025 against the years up to 2021`, text.includes(`(${yr[0]})`) && text.includes(`(${yr[1]})`) && yr[0] === R75.years['2025'], yr.join(' / '));
  // the readings and the stepping
  await page.click('#rHand'); await page.waitForTimeout(700);
  const restText = await page.textContent('#say');
  ok(`${w}px reading: what the harmed wrote`, restText.includes(`${found} first reports`) && restText.includes(`of ${field.first_read}`), restText);
  const seen = new Set();
  for (let i = 0; i < found + 2; i++) { await page.click('#bNext'); seen.add(/Incident (\d+)/.exec(await page.textContent('#say'))[1]); }
  ok(`${w}px stepping: the harmed's paragraphs`, seen.size === found && P.harmed_ids.every(i => seen.has(String(i))), `${seen.size}`);
  if (out) await page.screenshot({ path: path.join(out, `hand-${w}.png`), fullPage: true });
  await page.click('#rSeal'); await page.waitForTimeout(700);
  const sealText = await page.textContent('#say');
  ok(`${w}px reading: what public bodies did`, sealText.includes(`${B.public_final} acts`) && sealText.includes(`${B.target.user} at the left`) && sealText.includes(`${B.target.maker} at the right`), sealText);
  const stepped = new Set(); let favour = 0;
  for (let i = 0; i < B.public_final + 2; i++) { await page.click('#bNext'); const st = await page.textContent('#say'); const id = /Incident (\d+)/.exec(st)[1]; if (!stepped.has(id) && /in favour of/.test(st)) favour++; stepped.add(id); }
  ok(`${w}px stepping: the acts`, stepped.size === B.public_final && B.admitted.every(i => stepped.has(String(i))) && favour === forIds.length, `${stepped.size}, ${favour} in favour`);
  await page.click('#rAll'); await page.waitForTimeout(700);
  if (out) await page.screenshot({ path: path.join(out, `all-${w}.png`), fullPage: true });
  const top = await page.evaluate(() => document.getElementById('sheet').getBoundingClientRect().top + scrollY);
  ok(`${w}px the sheet begins on the first screen`, top < h, `${Math.round(top)} px`);
  const side = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
  ok(`${w}px no sideways scroll`, side <= 0, `${side}`);
  ok(`${w}px no errors`, errors.length === 0, errors.join(' | '));
  await page.close();
}
await browser.close();
console.log(bad ? `${bad} FAILED` : 'all passed');
process.exit(bad ? 1 : 0);
