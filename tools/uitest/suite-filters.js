// Conference / category / year filters, the three sort orders, Reset, and the
// hash that makes any view a shareable link.

const L = require('./lib');

L.suite('filters', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);
  const N = meta.talks.length;
  const byN = new Map(meta.talks.map(t => [t.i, t]));

  // ---------- each filter, against the data ----------
  const conf = [...new Set(meta.talks.map(t => t.cs))].sort()[1];
  await page.selectOption('#f-conf', conf);
  await page.waitForTimeout(400);
  const expConf = meta.talks.filter(t => t.cs === conf).length;
  L.check(`conference "${conf}" returns exactly its talks`,
    (await L.resultCount(page)) === expConf, `${await L.resultCount(page)} vs ${expConf}`);
  L.check('every card shown belongs to that conference',
    (await L.cardNs(page)).every(i => byN.get(i).cs === conf));

  const yearsIn = [...new Set(meta.talks.filter(t => t.cs === conf).map(t => t.y).filter(Boolean))];
  if (yearsIn.length) {
    await page.selectOption('#f-year', String(yearsIn[0]));
    await page.waitForTimeout(400);
    const expBoth = meta.talks.filter(t => t.cs === conf && t.y === yearsIn[0]).length;
    L.check(`conference and year stack (${yearsIn[0]})`,
      (await L.resultCount(page)) === expBoth, `${await L.resultCount(page)} vs ${expBoth}`);
    await page.selectOption('#f-year', '');
  } else {
    L.skip('conference and year stack', `no dated talks for ${conf} — run enrich.py`);
  }

  const cat = [...new Set(meta.talks.map(t => t.g).filter(Boolean))].sort()[0];
  await page.selectOption('#f-conf', '');
  await page.selectOption('#f-cat', cat);
  await page.waitForTimeout(400);
  const expCat = meta.talks.filter(t => t.g === cat).length;
  L.check(`category "${cat}" returns exactly its talks`,
    (await L.resultCount(page)) === expCat, `${await L.resultCount(page)} vs ${expCat}`);

  // ---------- a filter narrows a search rather than replacing it ----------
  await page.selectOption('#f-cat', '');
  await page.waitForTimeout(250);
  await L.search(page, 'agents');
  const allHits = await L.resultCount(page);
  await page.selectOption('#f-cat', cat);
  await page.waitForTimeout(450);
  const catHits = await L.resultCount(page);
  L.check('a filter narrows an existing search',
    catHits > 0 && catHits < allHits && (await L.cardNs(page)).every(i => byN.get(i).g === cat),
    `agents=${allHits} -> agents+"${cat}"=${catHits}`);

  const impossible = [...new Set(meta.talks.map(t => t.cs))]
    .find(cs => !meta.talks.some(t => t.cs === cs && t.g === cat));
  await page.selectOption('#f-conf', impossible);
  await page.waitForTimeout(400);
  L.check('contradictory filters show the empty state',
    (await page.locator('.empty h3').textContent().catch(() => null)) === 'Nothing matched');

  // ---------- sorting ----------
  await page.selectOption('#f-conf', '');
  await page.selectOption('#f-cat', '');
  await L.search(page, 'kubernetes');
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(450);
  const alpha = await L.titles(page);
  L.check('Title A–Z sorts alphabetically',
    JSON.stringify(alpha) === JSON.stringify([...alpha].sort((a, b) => a.localeCompare(b))),
    alpha.slice(0, 2).join(' | '));

  await page.selectOption('#f-sort', 'new');
  await page.waitForTimeout(450);
  const when = t => (t.p ? new Date(t.p).getTime() : (t.y ? new Date(t.y, 0, 1).getTime() : -Infinity));
  const dates = (await L.cardNs(page)).map(i => when(byN.get(i)));
  L.check('Newest first is reverse-chronological',
    dates.every((v, i) => i === 0 || dates[i - 1] >= v), JSON.stringify(dates.slice(0, 3)));

  await page.selectOption('#f-sort', 'rel');
  await page.waitForTimeout(450);
  const ranked = await L.titles(page);
  L.check('Most relevant restores the ranked order',
    /kubernetes|k8s/i.test(ranked[0]) && JSON.stringify(ranked) !== JSON.stringify(alpha), ranked[0]);

  // Relevance means nothing without a query, so it degrades to newest first and
  // the status line says so rather than leaving the picker looking broken.
  await L.search(page, '');
  L.check('relevance without a query explains its fallback',
    /newest first/.test((await L.statusText(page)).trim()),
    (await L.statusText(page)).trim().slice(0, 70));

  // ---------- reset ----------
  await L.search(page, 'kubernetes');
  await page.selectOption('#f-conf', conf);
  await page.selectOption('#f-sort', 'title');
  await page.waitForTimeout(400);
  await page.click('#clear');
  await page.waitForTimeout(450);
  const after = await page.evaluate(() => ({
    q: document.querySelector('#q').value,
    conf: document.querySelector('#f-conf').value,
    cat: document.querySelector('#f-cat').value,
    year: document.querySelector('#f-year').value,
    sort: document.querySelector('#f-sort').value,
    tr: document.querySelector('#f-tr').classList.contains('on'),
    hash: location.hash,
  }));
  L.check('Reset clears the query, the filters and the sort',
    after.q === '' && !after.conf && !after.cat && !after.year && after.sort === 'rel' && !after.tr,
    JSON.stringify(after));
  L.check('Reset restores the whole catalogue', (await L.resultCount(page)) === N);
  L.check('Reset clears the URL hash', after.hash === '', `hash="${after.hash}"`);

  // ---------- the conference badge is also a filter ----------
  await L.search(page, 'agents');
  await page.locator('#results .card .b.conf').first().click();
  await page.waitForTimeout(500);
  const clicked = await page.evaluate(() => document.querySelector('#f-conf').value);
  L.check('clicking a conference badge filters to that conference',
    !!clicked && (await L.cardNs(page)).every(i => byN.get(i).cs === clicked), clicked);
  L.check('the query survives the badge click', (await page.inputValue('#q')) === 'agents');

  // ---------- the hash ----------
  const reload = async hash => {
    await page.goto(L.BASE + hash);
    await page.reload();
    await page.waitForFunction(() => !/Loading/.test(document.querySelector('#sub').textContent),
      null, { timeout: 30000 });
    await page.waitForTimeout(600);
  };

  await reload(`#q=kubernetes&conf=${encodeURIComponent(conf)}&sort=title`);
  const restored = await page.evaluate(() => ({
    q: document.querySelector('#q').value,
    conf: document.querySelector('#f-conf').value,
    sort: document.querySelector('#f-sort').value,
  }));
  L.check('q, conference and sort are restored from the hash',
    restored.q === 'kubernetes' && restored.conf === conf && restored.sort === 'title',
    JSON.stringify(restored));

  await L.search(page, 'rag');
  const hash = await page.evaluate(() => location.hash);
  L.check('the hash tracks the live state', /q=rag/.test(hash) && /sort=title/.test(hash), hash);

  await reload(`#cat=${encodeURIComponent(cat)}&tr=1`);
  const rt = await page.evaluate(() => ({
    cat: document.querySelector('#f-cat').value,
    tr: document.querySelector('#f-tr').classList.contains('on'),
    trHidden: document.querySelector('#f-tr').hidden,
  }));
  // tr=1 must not switch on a filter the UI is deliberately hiding.
  L.check('category round-trips, and tr=1 is honoured only while that toggle is shown',
    rt.cat === cat && rt.tr === !rt.trHidden, JSON.stringify(rt));

  await reload('#conf=no-such-conference&sort=bogus&year=1999&q=agents');
  const bad = await page.evaluate(() => ({
    conf: document.querySelector('#f-conf').value,
    year: document.querySelector('#f-year').value,
    sort: document.querySelector('#f-sort').value,
    cards: document.querySelectorAll('#results .card').length,
  }));
  L.check('unknown filter and sort values fall back safely',
    bad.conf === '' && bad.year === '' && bad.sort === 'rel' && bad.cards > 0, JSON.stringify(bad));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
