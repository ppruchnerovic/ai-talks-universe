// Conference / conference type / topic / year filters, the five sort orders, Reset,
// and the hash that makes any view a shareable link.

const L = require('./lib');

// The years in the corpus, newest first.
const years0 = meta => [...new Set(meta.talks.map(t => t.y).filter(Boolean))].sort((a, b) => b - a);

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
  L.check(`conference type "${cat}" returns exactly its talks`,
    (await L.resultCount(page)) === expCat, `${await L.resultCount(page)} vs ${expCat}`);

  // ---------- topics: multi-valued, so the test is membership ----------
  // `k` is absent on a talk with no topic, and holds indices into the file's
  // `topics` list; the option list is the union of the names.
  const topicsOf = t => (t.k || []).map(i => meta.topics[i]);
  const topics = [...new Set(meta.talks.flatMap(topicsOf))].sort();
  await page.selectOption('#f-cat', '');
  if (!topics.length) {
    L.skip('topic filter', 'no talk carries a topic — run sync_catalog.py');
  } else {
    const topicOpts = await page.$$eval('#f-topic option', os => os.map(o => o.value));
    L.check('the topic options are the union of every talk\'s topics, sorted',
      JSON.stringify(topicOpts.slice(1)) === JSON.stringify(topics),
      `${topicOpts.length - 1} options vs ${topics.length} topics`);

    const topic = topics[Math.floor(topics.length / 2)];
    await page.selectOption('#f-topic', topic);
    await page.waitForTimeout(400);
    const expTopic = meta.talks.filter(t => topicsOf(t).includes(topic)).length;
    L.check(`topic "${topic}" returns exactly the talks carrying it`,
      (await L.resultCount(page)) === expTopic, `${await L.resultCount(page)} vs ${expTopic}`);
    L.check('every card shown carries that topic',
      (await L.cardNs(page)).every(i => topicsOf(byN.get(i)).includes(topic)));

    // A talk with two topics is under both — the facet is a set, not a column.
    const twice = meta.talks.find(t => topicsOf(t).length >= 2);
    if (twice) {
      const [a, b] = topicsOf(twice);
      const countA = meta.talks.filter(t => topicsOf(t).includes(a)).length;
      const countB = meta.talks.filter(t => topicsOf(t).includes(b)).length;
      await page.selectOption('#f-topic', a);
      await page.waitForTimeout(300);
      const gotA = await L.resultCount(page);
      await page.selectOption('#f-topic', b);
      await page.waitForTimeout(300);
      const gotB = await L.resultCount(page);
      L.check('a talk with two topics is counted under both',
        gotA === countA && gotB === countB, `${gotA}/${countA}, ${gotB}/${countB}`);
    }

    // Stacks with conference and year like the other filters do.
    const confWithTopic = meta.talks.find(t => topicsOf(t).includes(topic) && t.y);
    await page.selectOption('#f-topic', topic);
    await page.selectOption('#f-conf', confWithTopic.cs);
    await page.selectOption('#f-year', String(confWithTopic.y));
    await page.waitForTimeout(400);
    const expStack = meta.talks.filter(t => topicsOf(t).includes(topic)
      && t.cs === confWithTopic.cs && t.y === confWithTopic.y).length;
    L.check('topic stacks with conference and year',
      (await L.resultCount(page)) === expStack, `${await L.resultCount(page)} vs ${expStack}`);
    await page.selectOption('#f-conf', '');
    await page.selectOption('#f-year', '');

    // The chip on a card is the same filter.
    await page.selectOption('#f-topic', '');
    await page.waitForTimeout(300);
    const chip = page.locator('#results .card .b.topic').first();
    const chipText = await chip.textContent();
    await chip.click();
    await page.waitForTimeout(400);
    L.check('clicking a topic chip sets the topic filter',
      (await page.inputValue('#f-topic')) === chipText
        && (await L.cardNs(page)).every(i => topicsOf(byN.get(i)).includes(chipText)),
      `chip=${chipText}, select=${await page.inputValue('#f-topic')}`);
    await page.selectOption('#f-topic', '');
    await page.waitForTimeout(300);
  }

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

  // ---------- duration ----------
  const minutes = async () => (await L.cardNs(page)).map(i => byN.get(i).m || 0);
  await page.selectOption('#f-sort', 'short');
  await page.waitForTimeout(450);
  const asc = await minutes();
  L.check('Shortest first is ascending by duration',
    asc.length > 1 && asc.every((v, i) => i === 0 || asc[i - 1] <= v), JSON.stringify(asc.slice(0, 5)));
  await page.selectOption('#f-sort', 'long');
  await page.waitForTimeout(450);
  const desc = await minutes();
  L.check('Longest first is descending by duration',
    desc.length > 1 && desc.every((v, i) => i === 0 || desc[i - 1] >= v), JSON.stringify(desc.slice(0, 5)));
  L.check('the duration sort is in the URL', /sort=long/.test(await page.evaluate(() => location.hash)));
  await page.selectOption('#f-sort', 'rel');

  await page.selectOption('#f-len', 'lt10');
  await page.waitForTimeout(450);
  const short = await minutes();
  L.check('the "Under 10 min" bucket keeps only such talks',
    short.length > 0 && short.every(m => m > 0 && m < 10), JSON.stringify(short.slice(0, 5)));
  L.check('the length bucket is in the URL', /len=lt10/.test(await page.evaluate(() => location.hash)));
  await page.selectOption('#f-len', '');
  await page.waitForTimeout(300);

  // ---------- speaker ----------
  const bySpeaker = new Map();
  meta.talks.forEach(t => (t.s || []).forEach(s => bySpeaker.set(s, (bySpeaker.get(s) || 0) + 1)));
  const spk = [...bySpeaker].filter(([s, n]) => n >= 2 && s.split(' ').length >= 2)
    .sort((a, b) => b[1] - a[1])[0];
  if (spk) {
    await L.search(page, '');
    await page.fill('#f-spk', spk[0]);
    await page.waitForTimeout(500);
    const exp = meta.talks.filter(t => (t.s || []).some(x => x.toLowerCase().includes(spk[0].toLowerCase()))).length;
    L.check(`the speaker box ("${spk[0]}") keeps only their talks`,
      (await L.resultCount(page)) === exp &&
        (await L.cardNs(page)).every(i => (byN.get(i).s || []).some(x => x.includes(spk[0]))),
      `${await L.resultCount(page)} vs ${exp}`);
    L.check('the speaker box has a typeahead list',
      await page.evaluate(() => document.querySelector('#f-spk').getAttribute('list') === 'spk-list' &&
        document.querySelectorAll('#spk-list option').length > 100));
    L.check('the speaker filter is in the URL',
      /spk=/.test(await page.evaluate(() => location.hash)), await page.evaluate(() => location.hash));
    await page.fill('#f-spk', '');
    await page.waitForTimeout(300);
  } else {
    L.skip('the speaker box filters', 'no speaker with two talks in the corpus yet');
  }

  // ---------- facet counts ----------
  // With a year chosen, a conference's label counts its talks in that year.
  const year = years0(meta)[0];
  await page.selectOption('#f-year', String(year));
  await page.waitForTimeout(450);
  const facet = await page.$$eval('#f-conf option', os =>
    os.filter(o => o.value).map(o => [o.value, o.textContent]));
  const facetOk = facet.every(([v, label]) =>
    label.endsWith(`(${meta.talks.filter(t => t.cs === v && t.y === year).length.toLocaleString()})`));
  L.check(`conference labels count the talks the other filters leave (year ${year})`,
    facet.length > 0 && facetOk, facet.slice(0, 2).map(f => f[1]).join(' | '));
  L.check('facet counts change the labels, not the values',
    facet.every(([v]) => !/\(\d/.test(v)));
  await page.selectOption('#f-year', '');

  // ---------- spoken only ----------
  if (meta.talks.some(t => t.w > 0)) {
    await L.search(page, 'kubernetes');
    const before = await L.resultCount(page);
    await page.click('#f-spoken');
    await page.waitForTimeout(600);
    const st = (await L.statusText(page)).trim();
    const n = await L.resultCount(page);
    const onlySpoken = Number(((st.match(/(\d[\d,]*) found only in the spoken/) || [])[1] || '0').replace(/,/g, ''));
    L.check('"Spoken only" matches transcripts and nothing else',
      n > 0 && n <= before && onlySpoken === n, `${before} -> ${n}, ${onlySpoken} transcript-only`);
    L.check('"Spoken only" is in the URL', /spoken=1/.test(await page.evaluate(() => location.hash)));
    await page.click('#f-spoken');
    await page.waitForTimeout(400);
  } else {
    L.skip('"Spoken only" matches transcripts and nothing else', 'no transcripts fetched yet');
  }

  // ---------- reset ----------
  await L.search(page, 'kubernetes');
  await page.selectOption('#f-conf', conf);
  if (topics.length) await page.selectOption('#f-topic', topics[0]);
  await page.selectOption('#f-sort', 'title');
  await page.selectOption('#f-len', 'gt60');
  await page.fill('#f-spk', 'a');
  await page.waitForTimeout(400);
  await page.click('#clear');
  await page.waitForTimeout(450);
  const after = await page.evaluate(() => ({
    q: document.querySelector('#q').value,
    conf: document.querySelector('#f-conf').value,
    cat: document.querySelector('#f-cat').value,
    topic: document.querySelector('#f-topic').value,
    year: document.querySelector('#f-year').value,
    len: document.querySelector('#f-len').value,
    spk: document.querySelector('#f-spk').value,
    sort: document.querySelector('#f-sort').value,
    tr: document.querySelector('#f-tr').classList.contains('on'),
    spoken: document.querySelector('#f-spoken').classList.contains('on'),
    hash: location.hash,
  }));
  L.check('Reset clears the query, the filters and the sort',
    after.q === '' && !after.conf && !after.cat && !after.topic && !after.year && !after.len && !after.spk &&
      after.sort === 'rel' && !after.tr && !after.spoken,
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
  L.check('conference type round-trips, and tr=1 is honoured only while that toggle is shown',
    rt.cat === cat && rt.tr === !rt.trHidden, JSON.stringify(rt));

  await reload(`#q=agents&len=gt60&spk=${encodeURIComponent('a')}&sort=short`);
  const rt2 = await page.evaluate(() => ({
    len: document.querySelector('#f-len').value, spk: document.querySelector('#f-spk').value,
    sort: document.querySelector('#f-sort').value }));
  L.check('length, speaker and duration sort round-trip through the hash',
    rt2.len === 'gt60' && rt2.spk === 'a' && rt2.sort === 'short', JSON.stringify(rt2));

  // Newest first is the one order worth remembering across visits: chosen
  // once, it applies to a link that says nothing about the order, and never
  // to one that says something else.
  await page.selectOption('#f-sort', 'new');
  await page.waitForTimeout(300);
  await reload('#q=agents');
  const remembered = await page.evaluate(() => document.querySelector('#f-sort').value);
  await reload('#q=agents&sort=title');
  const explicit = await page.evaluate(() => document.querySelector('#f-sort').value);
  L.check('"Newest first" is remembered for links that do not say otherwise',
    remembered === 'new' && explicit === 'title', `${remembered}, ${explicit}`);
  await page.selectOption('#f-sort', 'rel');
  await page.waitForTimeout(300);

  if (topics.length) {
    await reload(`#topic=${encodeURIComponent(topics[0])}&q=agents`);
    const rtTopic = await page.evaluate(() => ({
      topic: document.querySelector('#f-topic').value,
      cards: document.querySelectorAll('#results .card').length,
    }));
    L.check('topic round-trips through the hash',
      rtTopic.topic === topics[0] && rtTopic.cards > 0
        && (await L.cardNs(page)).every(i => topicsOf(byN.get(i)).includes(topics[0])),
      JSON.stringify(rtTopic));
    await L.search(page, 'evals');
    L.check('the hash carries the topic',
      new URLSearchParams((await page.evaluate(() => location.hash)).slice(1)).get('topic') === topics[0],
      await page.evaluate(() => location.hash));
  }

  await reload('#conf=no-such-conference&sort=bogus&year=1999&topic=no-such-topic&q=agents');
  const bad = await page.evaluate(() => ({
    conf: document.querySelector('#f-conf').value,
    year: document.querySelector('#f-year').value,
    topic: document.querySelector('#f-topic').value,
    sort: document.querySelector('#f-sort').value,
    cards: document.querySelectorAll('#results .card').length,
  }));
  L.check('unknown filter and sort values fall back safely',
    bad.conf === '' && bad.year === '' && bad.topic === '' && bad.sort === 'rel' && bad.cards > 0,
    JSON.stringify(bad));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
