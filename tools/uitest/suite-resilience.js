// What the explorer does when its data does not arrive, and what it does with
// input written to break it.
//
// The index is layered on purpose: metadata search works without the transcript
// index, and the transcript index works one shard at a time. Each layer is
// knocked out here to prove the one beneath it still stands.

const L = require('./lib');

L.suite('resilience', async browser => {
  // ---------- a single index shard is unreachable ----------
  {
    // Shard names come from shardKeyOf() in index.html: two characters, [a-z]
    // kept as-is, digits folded to "0" and anything else to "_". So "kubernetes"
    // is served out of data/tindex/ku.json, and the fault pattern has to be two
    // characters wide. It was one until the index was resharded, after which it
    // matched nothing and this check ran against a perfectly healthy page.
    const SHARD_RE = /\/data\/tindex\/[a-z0-9_]{2}\.json$/;    // never _manifest.json
    const QUERY = 'kubernetes';                                // -> data/tindex/ku.json

    const page = await L.newPage(browser);
    await L.boot(page);
    const meta = await L.meta(page);
    const hasTranscripts = meta.talks.some(t => t.w > 0);

    if (!hasTranscripts) {
      L.skip('a broken index shard falls back to metadata-only search',
        'no transcripts collected yet — there is no shard to break');
      await page.close();
    } else {
      // The baseline has to be read with the transcript layer actually live.
      // On a cold page the shard fetch can fail or land late, and the page then
      // renders metadata-only hits — which is exactly the number the faulted
      // page is supposed to produce, so the comparison below would compare a
      // broken page against a broken page and pass. Wait for the shard the
      // query needs to arrive, and for the render that used it.
      const shardLanded = page.waitForResponse(
        r => SHARD_RE.test(new URL(r.url()).pathname) && r.ok(), { timeout: 30000 }
      ).then(r => new URL(r.url()).pathname).catch(() => null);
      await L.search(page, QUERY);
      // search() gives up on a timer, so the render it kicked off may still be
      // awaiting the shard. The page's own state is out of reach — index.html
      // runs inside an IIFE — but the status line reports the one thing only a
      // loaded shard can produce: hits found nowhere but the spoken words.
      const landed = await shardLanded;
      const settled = await page.waitForFunction(q => {
        const s = document.querySelector('#status').textContent;
        return s.includes(`matching ${q}`) && /found only in the spoken transcript/.test(s);
      }, QUERY, { timeout: 20000 }).then(() => true).catch(() => false);
      const full = await L.resultCount(page);
      const spoken = ((await L.statusText(page)).match(/(\d[\d,]*) found only in the spoken/) || [])[1];
      L.check('the baseline is measured with the transcript shard actually loaded',
        landed !== null && settled && Number((spoken || '0').replace(/,/g, '')) > 0,
        `${landed || 'no shard response'}, ${full} hits, ${spoken || 0} of them transcript-only`);
      await page.close();

      const p2 = await L.newPage(browser);
      let faulted = 0;
      await p2.route(u => SHARD_RE.test(u.pathname),
        r => { faulted++; return r.fulfill({ status: 500, body: 'x' }); });
      await L.boot(p2);
      await L.search(p2, QUERY);
      const n = await L.resultCount(p2);
      // Assert the fault was injected at all: a pattern that matches no real
      // shard name is how this check stopped testing anything in the first
      // place, and it fails silently rather than loudly.
      L.check('the shard fault pattern matches a shard that is really requested',
        faulted > 0, `${faulted} tindex request(s) intercepted`);
      // Strictly fewer: with the shard served the query also matches talks that
      // only ever say "kubernetes" out loud, so an equal count means the fault
      // did nothing.
      L.check('a broken index shard falls back to metadata-only search',
        n > 0 && n < full && p2.__errors.length === 0,
        `${n} hits vs ${full} with the shard`);
      await p2.close();
    }
  }

  // ---------- no transcript index at all ----------
  {
    const page = await L.newPage(browser);
    await page.route('**/data/tindex/_manifest.json', r => r.fulfill({ status: 404, body: '' }));
    await L.boot(page);
    await L.search(page, 'kubernetes');
    L.check('with no transcript index, metadata search still works',
      /^[\d,]+ talks? matching/.test((await L.statusText(page)).trim()) && page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 70));
    await page.close();
  }

  // ---------- the catalogue itself fails ----------
  {
    const page = await L.newPage(browser);
    await page.route('**/data/search-meta.json', r => r.fulfill({ status: 500, body: 'boom' }));
    await page.goto(L.BASE);
    await page.waitForTimeout(2000);
    const sub = await page.textContent('#sub');
    const empty = await page.textContent('.empty h3').catch(() => null);
    L.check('a failed catalogue load says so instead of hanging on "Loading…"',
      /Could not load/.test(sub) && empty === 'Failed to load', `${sub} / ${empty}`);
    await page.close();
  }

  // ---------- hostile input ----------
  {
    const page = await L.newPage(browser);
    await L.boot(page);

    // The status line echoes the query back, so it is the obvious injection point.
    await L.search(page, '<img src=x onerror=alert(1)> kubernetes');
    const status = await page.evaluate(() => document.querySelector('#status').innerHTML);
    const smuggled = await page.evaluate(() =>
      document.querySelectorAll('#status img, #results img').length);
    L.check('the echoed query is HTML-escaped', !/<img/i.test(status) && smuggled === 0,
      status.replace(/\s+/g, ' ').slice(0, 110));

    await L.search(page, '"><script>window.__x=1</script>');
    L.check('script injection through the query does not execute',
      !(await page.evaluate(() => window.__x === 1)));

    // highlight() builds a RegExp out of the query terms.
    for (const q of ['c++ (*)', 'a\\b', '[test]', '$^.*+?']) {
      await L.search(page, q);
      L.check(`regex metacharacters in "${q}" are treated literally`,
        page.__errors.length === 0, page.__errors.join(';'));
    }

    await L.search(page, 'a'.repeat(400));
    L.check('a 400-character query is handled', page.__errors.length === 0,
      await page.locator('.empty h3').textContent().catch(() => '(results)'));

    await L.search(page, '日本語 テスト');
    L.check('non-Latin input does not throw', page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 40) || 'no matches');

    await L.search(page, 'ai — agents');
    L.check('punctuation-only tokens are dropped', page.__errors.length === 0);

    await L.search(page, 'agents security evaluation kubernetes inference retrieval latency guardrails');
    L.check('an eight-term AND query resolves', page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 55) || 'empty state');
    await page.close();
  }

  // ---------- a talk missing half its fields ----------
  {
    const page = await L.newPage(browser);
    await page.route('**/data/search-meta.json', async route => {
      const json = await (await route.fetch()).json();
      // A conference that publishes no description, no speaker, no duration and
      // no date is not hypothetical — it is what a flat playlist listing gives
      // before enrich.py has run.
      Object.assign(json.talks[0], { d: '', s: [], a: [], m: null, p: null, y: null, e: null });
      await route.fulfill({ json });
    });
    await L.boot(page);
    const card = await page.evaluate(() => {
      const c = document.querySelector('#results .card');
      return c && { html: c.innerHTML.length, undef: /undefined|null|NaN/.test(c.textContent) };
    });
    L.check('a talk with only a title and a video id still renders',
      card && card.html > 0 && !card.undef, JSON.stringify(card));
    L.check('no uncaught errors from the sparse record',
      page.__errors.length === 0, page.__errors.join('; '));
    await page.close();
  }

  // ---------- a phone ----------
  {
    const page = await L.newPage(browser,
      { viewport: { width: 390, height: 780 }, isMobile: true, hasTouch: true });
    await L.boot(page);
    await L.search(page, 'kubernetes');
    const m = await page.evaluate(() => ({
      overflowX: document.documentElement.scrollWidth > window.innerWidth + 1,
      scrollW: document.documentElement.scrollWidth,
      inner: window.innerWidth,
      cardW: document.querySelector('.card')?.getBoundingClientRect().width,
      inputW: document.querySelector('#q').getBoundingClientRect().width,
      wrap: getComputedStyle(document.querySelector('.filters')).flexWrap,
    }));
    L.check('no horizontal overflow at 390px', !m.overflowX, `${m.scrollW} vs ${m.inner}`);
    L.check('cards and the search box fit the viewport',
      m.cardW <= m.inner && m.inputW <= m.inner,
      `card=${Math.round(m.cardW)} input=${Math.round(m.inputW)}`);
    L.check('the filter row wraps', m.wrap === 'wrap', m.wrap);

    // Rewrapping at a new width changes what fits in four lines, so the unfold
    // buttons have to be measured again.
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.waitForTimeout(500);
    const stale = await page.evaluate(() =>
      [...document.querySelectorAll('.abs.clamped')].filter(p => {
        const b = p.nextElementSibling;
        return b && b.hidden !== (p.scrollHeight <= p.clientHeight + 2);
      }).length);
    L.check('the unfold buttons are re-measured after a resize', stale === 0, `${stale} stale`);
    await page.close();
  }
});
