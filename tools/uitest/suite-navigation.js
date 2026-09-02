// How the page loads, what it costs, and whether a URL someone sends you shows
// them what you were looking at.

const L = require('./lib');
const { spawn, spawnSync } = require('child_process');
const net = require('net');
const os = require('os');
const path = require('path');

const ROOT = path.join(__dirname, '..', '..');

const freePort = () => new Promise((resolve, reject) => {
  const s = net.createServer();
  s.once('error', reject);
  s.listen(0, '127.0.0.1', () => { const { port } = s.address(); s.close(() => resolve(port)); });
});

// pages.yml publishes what tools/assemble_site.sh copies, not the checkout.
// Every other suite serves the repository root, where every path exists, so
// none of them can notice a file the site lacks. This serves the assembled
// tree on its own port and walks the page through everything it fetches.
async function assembledSite() {
  const dir = path.join(os.tmpdir(), `atu-site-${process.pid}`);
  const built = spawnSync('bash', [path.join(ROOT, 'tools', 'assemble_site.sh'), dir],
    { encoding: 'utf8' });
  if (built.status !== 0) throw new Error(`assemble_site.sh failed: ${built.stderr}`);
  const port = await freePort();
  const server = spawn('python3', ['-m', 'http.server', String(port), '-d', dir],
    { stdio: 'ignore' });
  const base = `http://127.0.0.1:${port}/`;
  for (let i = 0; i < 100; i++) {
    try { if ((await fetch(base + 'index.html')).ok) break; } catch (_) {}
    await new Promise(r => setTimeout(r, 100));
  }
  return { base, dir, close: () => { server.kill(); spawnSync('rm', ['-rf', dir]); } };
}

L.suite('navigation', async browser => {
  const page = await L.newPage(browser);

  // ---------- cold load ----------
  const t0 = Date.now();
  await L.boot(page);
  const bootMs = Date.now() - t0;
  const perf = await page.evaluate(() => {
    const r = performance.getEntriesByType('resource');
    return {
      n: r.length,
      kb: Math.round(r.reduce((a, x) => a + (x.transferSize || x.encodedBodySize || 0), 0) / 1024),
      biggest: r.map(x => [x.name.split('/').slice(-2).join('/'), Math.round((x.encodedBodySize || 0) / 1024)])
        .sort((a, b) => b[1] - a[1]).slice(0, 3),
    };
  });
  // The local test server does not compress; GitHub Pages does, so the figure a
  // visitor actually pays is roughly a quarter of this.
  L.check('the catalogue is usable within a few seconds', bootMs < 8000,
    `${bootMs}ms, ${perf.n} requests, ~${perf.kb}KB uncompressed — ${JSON.stringify(perf.biggest)}`);
  // The whole point of sharding the transcript index is that a visitor who
  // never searches never downloads it.
  L.check('the transcript shards are not loaded up front',
    perf.n <= 3, `${perf.n} requests before any query`);

  const before = await page.evaluate(() => performance.getEntriesByType('resource').length);
  await L.search(page, 'observability');
  const after = await page.evaluate(() => performance.getEntriesByType('resource').length);
  L.check('a query lazily fetches only the shards it needs',
    after - before <= 3, `${after - before} extra fetches`);

  const warm = Date.now();
  await L.search(page, 'observability platform');
  L.check('a warm query stays responsive', Date.now() - warm < 2500, `${Date.now() - warm}ms`);

  // ---------- history ----------
  // Searching rewrites the hash in place rather than pushing an entry, so Back
  // leaves the explorer instead of stepping backwards through queries. That is a
  // deliberate trade: it keeps a session of typing out of the back stack.
  await L.search(page, 'rag');
  const h1 = await page.evaluate(() => location.hash);
  await L.search(page, 'kubernetes');
  const h2 = await page.evaluate(() => location.hash);
  await page.goBack().catch(() => {});
  await page.waitForTimeout(600);
  const h3 = await page.evaluate(() => location.hash);
  L.check('searching updates the URL in place', h1 !== h2 && h3 !== h1,
    `"${h1}" -> "${h2}" -> back gives "${h3}"`);

  // ---------- a shared link ----------
  await L.boot(page);
  await L.search(page, 'prompt injection');
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(500);
  const url = await page.evaluate(() => location.href);
  const mine = await L.cardNs(page);

  const theirs = await L.newPage(browser);
  await theirs.goto(url);
  await theirs.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
    null, { timeout: 30000 });
  await theirs.waitForTimeout(900);
  L.check('pasting the URL into a fresh tab reproduces the same view',
    JSON.stringify(mine) === JSON.stringify(await L.cardNs(theirs)),
    `${mine.length} vs ${(await L.cardNs(theirs)).length} cards`);
  await theirs.close();

  // ---------- the page says where its data came from ----------
  await L.boot(page);
  const out = await page.evaluate(() =>
    [...document.querySelectorAll('footer a')].map(a => a.getAttribute('href')));
  L.check('the footer links to the curated source list and the repository',
    out.some(h => /ai-conferences\.md$/.test(h)) && out.some(h => /github\.com/.test(h)),
    out.join(', '));

  L.check('no failed requests', page.__requests.length === 0, page.__requests.slice(0, 3).join('; '));

  // ---------- the published site, not the checkout ----------
  const site = await assembledSite();
  try {
    const pub = await L.newPage(browser);
    await pub.goto(site.base, { waitUntil: 'load' });
    await pub.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
      null, { timeout: 30000 });
    await L.search(pub, 'observability');
    const n = await L.resultCount(pub);
    L.check('the assembled site loads the catalogue and searches it', n > 0, `${n} hits`);

    // A transcript-bearing hit, opened — the one fetch that goes outside the
    // index, to data/transcripts/<id>.json.
    const link = pub.locator('.mo-load').first();
    if (await link.count()) {
      await link.click();
      await pub.waitForFunction(() => !document.querySelector('.mo-slot .spinner'),
        null, { timeout: 15000 }).catch(() => {});
      const mo = await pub.locator('.moments .mo').count();
      L.check('the assembled site serves the transcript behind "Find this in the talk"',
        mo > 0, `${mo} moments`);
    } else {
      L.skip('the assembled site serves a transcript', 'no transcript-bearing hit for the probe');
    }

    // Every relative link on the page has to resolve on the site, not only on
    // the checkout — the footer's ai-conferences.md was the one at risk.
    const hrefs = await pub.$$eval('a[href]', as => as.map(a => a.getAttribute('href'))
      .filter(h => h && !/^(https?:|#|\/\/)/.test(h)));
    const dead = [];
    for (const h of new Set(hrefs)) {
      const r = await fetch(site.base + h).catch(() => ({ ok: false }));
      if (!r.ok) dead.push(h);
    }
    L.check('every relative link resolves on the assembled site', dead.length === 0,
      dead.join(', ') || `${new Set(hrefs).size} checked`);

    L.check('the assembled site has no failed requests', pub.__requests.length === 0,
      pub.__requests.slice(0, 3).join('; '));
    L.check('the assembled site has no uncaught errors', pub.__errors.length === 0,
      pub.__errors.join('; '));
    await pub.close();
  } finally {
    site.close();
  }
});
