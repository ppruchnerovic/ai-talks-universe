// What the explorer looks like before anyone has typed anything: the catalogue
// loaded, the filters populated from the data rather than hardcoded, and one
// card rendered correctly end to end.

const L = require('./lib');

L.suite('load', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);

  const meta = await L.meta(page);
  const n = meta.talks.length;
  const withTr = meta.talks.filter(t => t.w > 0).length;
  const confs = new Set(meta.talks.map(t => t.cs)).size;

  const sub = await page.textContent('#sub');
  L.check('subtitle reports the corpus size and conference count',
    /[\d,]+ talks from \d+ conferences/.test(sub), sub);
  L.check('subtitle counts match the data',
    sub.includes(n.toLocaleString()) && sub.includes(String(confs)),
    `${sub} vs ${n} talks / ${confs} conferences`);

  const cards = await L.cardCount(page);
  L.check('first page renders 20 cards', cards === 20, `got ${cards}`);

  const status = (await L.statusText(page)).trim();
  L.check('status shows the total and the default-order note',
    status.includes(n.toLocaleString()) && /newest first/.test(status), status);

  // ---------- filter dropdowns are built from the data ----------
  const opts = await page.evaluate(() => ({
    conf: [...document.querySelectorAll('#f-conf option')].map(o => o.value),
    cat: [...document.querySelectorAll('#f-cat option')].map(o => o.value),
    topic: [...document.querySelectorAll('#f-topic option')].map(o => o.value),
    year: [...document.querySelectorAll('#f-year option')].map(o => o.value),
    sort: [...document.querySelectorAll('#f-sort option')].map(o => o.value),
  }));
  const confSlugs = [...new Map(meta.talks.map(t => [t.cs, t.c])).entries()]
    .sort((a, b) => a[1].localeCompare(b[1])).map(e => e[0]);
  L.check('conference options match the data, ordered by display name',
    JSON.stringify(opts.conf.slice(1)) === JSON.stringify(confSlugs),
    `${opts.conf.length - 1} options vs ${confSlugs.length} conferences`);
  L.check('conference-type options match the data',
    JSON.stringify(opts.cat.slice(1)) ===
      JSON.stringify([...new Set(meta.talks.map(t => t.g).filter(Boolean))].sort()),
    `${opts.cat.length - 1} options`);
  const topicsOf = t => (t.k || []).map(i => meta.topics[i]);
  const topics = [...new Set(meta.talks.flatMap(topicsOf))].sort();
  L.check('topic options are the union of every talk\'s topics, sorted',
    JSON.stringify(opts.topic.slice(1)) === JSON.stringify(topics),
    `${opts.topic.length - 1} options vs ${topics.length} topics`);
  L.check('year options are newest first',
    JSON.stringify(opts.year.slice(1)) ===
      JSON.stringify([...new Set(meta.talks.map(t => t.y).filter(Boolean))]
        .sort((a, b) => b - a).map(String)),
    opts.year.slice(1, 4).join(', '));
  L.check('sort offers relevance / newest / title',
    JSON.stringify(opts.sort) === JSON.stringify(['rel', 'new', 'title']));

  // A filter that matches every talk is a dead control, so the UI hides the
  // transcript toggle until coverage is actually partial.
  const trHidden = await page.locator('#f-tr').isHidden();
  L.check('"Transcript only" is hidden exactly when every talk has a transcript',
    trHidden === (withTr === n), `hidden=${trHidden}, ${withTr}/${n} with transcripts`);

  // ---------- default order ----------
  const byN = new Map(meta.talks.map(t => [t.i, t]));
  const when = t => (t.p ? new Date(t.p).getTime() : (t.y ? new Date(t.y, 0, 1).getTime() : -Infinity));
  const dates = (await L.cardNs(page)).map(i => when(byN.get(i)));
  L.check('the unsearched listing is newest first',
    dates.every((v, i) => i === 0 || dates[i - 1] >= v), JSON.stringify(dates.slice(0, 3)));

  // ---------- one card, in full ----------
  const first = page.locator('#results .card').first();
  const a = await first.evaluate(c => ({
    href: c.querySelector('h2 a')?.getAttribute('href'),
    target: c.querySelector('h2 a')?.getAttribute('target'),
    rel: c.querySelector('h2 a')?.getAttribute('rel'),
    badges: [...c.querySelectorAll('.badges .b')].map(b => b.textContent),
    confBadge: c.querySelector('.b.conf')?.dataset.conf,
    site: [...c.querySelectorAll('.links a')].map(x => x.getAttribute('href'))[1],
    findLink: !!c.querySelector('.mo-load'),
  }));
  const firstTalk = byN.get((await L.cardNs(page))[0]);
  // `l` is the talk's own page, present only when there is no YouTube video —
  // an InfoQ presentation. Newest-first browsing can put one of those first.
  const expectHref = firstTalk.l || `https://www.youtube.com/watch?v=${firstTalk.v}`;
  L.check(`the title links to the recording (${firstTalk.l ? "the talk's own page" : 'YouTube'})`,
    a.href === expectHref, a.href);
  L.check('external links open in a new tab with noopener',
    a.target === '_blank' && a.rel === 'noopener');
  L.check('the conference badge carries the slug the filter uses',
    a.confBadge === firstTalk.cs, `${a.confBadge} vs ${firstTalk.cs}`);
  L.check('the conference site is linked', /^https?:\/\//.test(a.site || ''), a.site);
  L.check('badges carry at least the conference and one more fact',
    a.badges.length >= 2, JSON.stringify(a.badges));
  L.check('"Find this in the talk" is absent until something is searched for',
    a.findLink === false);

  // Topic chips: one per topic the talk carries, and none on a talk with none.
  const chips = await page.$$eval('#results .card', cs => cs.map(c => ({
    n: Number(c.dataset.n),
    chips: [...c.querySelectorAll('.b.topic')].map(b => ({ text: b.textContent, data: b.dataset.topic })),
  })));
  const chipsRight = chips.every(({ n, chips: cc }) =>
    JSON.stringify(cc.map(x => x.text)) === JSON.stringify(topicsOf(byN.get(n)))
    && cc.every(x => x.text === x.data));
  const withChips = chips.filter(c => c.chips.length).length;
  if (!topics.length) L.skip('topic chips', 'no talk carries a topic — run sync_catalog.py');
  else L.check('each card shows exactly its topics as chips, and the chip carries its value',
    chipsRight && withChips > 0, `${withChips} of ${chips.length} cards carry chips`);

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
  L.check('no failed requests', page.__requests.length === 0, page.__requests.join('; '));
  L.check('no console errors', page.__console.length === 0, page.__console.join('; '));
});
