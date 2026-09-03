// The controls the script shows and hides as state changes: pagination, the
// description unfold, tag chips and the keyboard shortcut.
//
// The first two checks are a regression guard inherited from the corpus this
// explorer grew out of. `#more` and `.abs-more` are hidden by setting the
// `hidden` property, and an author rule that sets `display` on either of them
// outranks the UA stylesheet's [hidden] — which silently turns both into
// permanent fixtures. That shipped once: a four-hit search offered
// "Show more (-16 left)".

const L = require('./lib');

const visibility = sel => `(() => {
  const b = document.querySelector('${sel}');
  return b && { hiddenAttr: b.hidden, display: getComputedStyle(b).display,
                visible: b.offsetParent !== null, text: b.textContent };
})()`;

L.suite('controls', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);

  // ---------- "Show more" hides when there is nothing more ----------
  await L.search(page, 'zzzqqqxyzzy');
  const onEmpty = await page.evaluate(visibility('#more'));
  L.check('"Show more" is hidden on an empty result set', !onEmpty.visible,
    `hidden=${onEmpty.hiddenAttr} display=${onEmpty.display} text="${onEmpty.text}"`);

  // A query narrow enough to fit on one page, found rather than guessed.
  let narrow = null;
  for (const q of ['gpt-4', 'webassembly', 'lakehouse', 'quantisation', 'homomorphic']) {
    await L.search(page, q);
    const c = await L.cardCount(page);
    if (c > 0 && c < 20) { narrow = `${q} (${c} cards)`; break; }
  }
  if (narrow) {
    const oneShort = await page.evaluate(visibility('#more'));
    L.check('"Show more" is hidden when every hit already fits on one page',
      !oneShort.visible,
      `${narrow}, hidden=${oneShort.hiddenAttr} display=${oneShort.display}`);
  } else {
    L.skip('"Show more" is hidden when every hit fits on one page',
      'no sampled query returned between 1 and 19 hits');
  }

  // ---------- the unfold appears only where text is truncated ----------
  //
  // Both directions have to be on screen at once: a description long enough to
  // overflow the four-line clamp, and one short enough not to. An empty query
  // sorts newest first, and the newest few hundred are all Data-API
  // descriptions clipped at 600 characters — every one of them overflows a
  // clamp that fits roughly 300, so the sample used to be "0 wrong of 0" and
  // the check asserted nothing. The short ones exist, they are just not the
  // newest, so pick the conference that has the most of them and browse that.
  const SHORT = 280;   // comfortably inside the clamp at 1280px
  const short = meta.talks.filter(t => {
    const d = (t.d || '').trim();
    return d.length > 0 && d.length <= SHORT;
  });
  const long = meta.talks.filter(t => (t.d || '').trim().length > SHORT);
  if (short.length && long.length) {
    // Most short descriptions per conference — the filter needs a slug, and a
    // conference with both kinds gives one sample that exercises both branches.
    const tally = new Map();
    for (const t of short) tally.set(t.cs, (tally.get(t.cs) || 0) + 1);
    const slug = [...tally].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))[0][0];

    await L.search(page, '');
    await page.selectOption('#f-conf', slug);
    await page.waitForTimeout(400);
    // Show the whole conference, not the first twenty of it.
    for (let i = 0; i < 40; i++) {
      const more = page.locator('#more');
      if (!(await more.isVisible())) break;
      await more.click();
      await page.waitForTimeout(120);
    }
    await page.waitForTimeout(600);
    const abs = await page.evaluate(() => {
      const rows = [...document.querySelectorAll('#results .card')].map(c => {
        const p = c.querySelector('.abs'), b = c.querySelector('.abs-more');
        if (!p || !b) return null;
        return { overflows: p.scrollHeight > p.clientHeight + 2, visible: b.offsetParent !== null };
      }).filter(Boolean);
      return { total: rows.length,
               short: rows.filter(r => !r.overflows).length,
               long: rows.filter(r => r.overflows).length,
               wrong: rows.filter(r => !r.overflows && r.visible).length,
               missing: rows.filter(r => r.overflows && !r.visible).length };
    });
    // This one first: it is the guard that stops the next check passing as
    // "0 wrong of 0", which is what it did while the sample held no short
    // descriptions at all.
    L.check('the sample really contains untruncated descriptions, so the next check means something',
      abs.short > 0 && abs.long > 0,
      `${slug}: ${abs.short} untruncated, ${abs.long} truncated, ${abs.total} cards ` +
      `(corpus has ${short.length} descriptions of <=${SHORT} chars)`);
    L.check('the unfold button appears only where the clamp actually hides something',
      abs.wrong === 0 && abs.missing === 0,
      `${abs.wrong} shown over untruncated text, ${abs.missing} missing over truncated text, ` +
      `of ${abs.total} cards in ${slug}`);
    await page.selectOption('#f-conf', '');
    await page.waitForTimeout(300);
  } else {
    L.skip('the unfold button appears only where text is truncated',
      `need both kinds of description: ${short.length} of <=${SHORT} chars, ${long.length} longer`);
  }

  // ---------- pagination ----------
  await L.search(page, 'agents');
  const total = await L.resultCount(page);
  L.check('the first page is 20 cards', (await L.cardCount(page)) === 20);
  L.check('the button reports how many are left',
    (await page.textContent('#more')) === `Show more (${(total - 20).toLocaleString()} left)`,
    await page.textContent('#more'));
  await page.click('#more');
  await page.waitForTimeout(350);
  L.check('a click adds another 20', (await L.cardCount(page)) === 40);
  await page.click('#more');
  await page.waitForTimeout(350);
  L.check('and again', (await L.cardCount(page)) === 60);
  await L.search(page, 'rag');
  L.check('a new query resets to the first page', (await L.cardCount(page)) <= 20,
    `${await L.cardCount(page)} cards`);

  // ---------- description unfold ----------
  const card = page.locator('#results .card').filter({ has: page.locator('.abs-more:visible') }).first();
  if (await card.count()) {
    const read = () => card.evaluate(c => ({
      h: c.querySelector('.abs').clientHeight,
      clamped: c.querySelector('.abs').classList.contains('clamped'),
      label: c.querySelector('.abs-more').textContent,
    }));
    const before = await read();
    await card.locator('.abs-more').click();
    await page.waitForTimeout(250);
    const opened = await read();
    L.check('unfolding expands the paragraph and relabels the button',
      !opened.clamped && opened.label === 'Show less' && opened.h >= before.h,
      `${before.h}px "${before.label}" -> ${opened.h}px "${opened.label}"`);
    await card.locator('.abs-more').click();
    await page.waitForTimeout(250);
    const closed = await read();
    L.check('folding restores the clamp and the label',
      closed.clamped && closed.label === 'Show full description', JSON.stringify(closed));
  } else {
    L.skip('the description unfold works', 'no clamped description on screen');
  }

  // ---------- tag chips ----------
  if (meta.talks.some(t => (t.a || []).length)) {
    await L.search(page, 'agents');
    await page.evaluate(() => window.scrollTo(0, 600));
    const chip = page.locator('#results .b.tag').first();
    if (await chip.count()) {
      const tagVal = await chip.getAttribute('data-tag');
      await chip.click();
      await page.waitForTimeout(600);
      L.check('clicking a tag chip searches for it',
        (await page.inputValue('#q')) === tagVal, `q="${await page.inputValue('#q')}"`);
      L.check('the tag search returns something', (await L.cardCount(page)) > 0);
      L.check('the page scrolls back to the top', (await page.evaluate(() => window.scrollY)) < 50);
    } else {
      L.skip('clicking a tag chip searches for it', 'no tagged talk on this result page');
    }
  } else {
    L.skip('tag chips run a search', 'no YouTube tags collected yet — run enrich.py');
  }

  // ---------- keyboard ----------
  await page.evaluate(() => document.querySelector('#q').blur());
  await page.keyboard.press('/');
  await page.waitForTimeout(150);
  const focus = await page.evaluate(() => document.activeElement.id);
  L.check('"/" focuses the search box without typing a slash',
    focus === 'q' && !(await page.inputValue('#q')).includes('/'), `focus=${focus}`);
  // Once the box has focus the shortcut must get out of the way and let the
  // slash through. Where it lands depends on the caret, which is not the point.
  const v = await page.inputValue('#q');
  await page.keyboard.press('/');
  await page.waitForTimeout(150);
  const typed = await page.inputValue('#q');
  L.check('"/" types normally once the box already has focus',
    typed.length === v.length + 1 && typed.includes('/'), `"${v}" -> "${typed}"`);

  // ---------- j/k ----------
  await L.search(page, 'agents');
  await page.evaluate(() => document.querySelector('#q').blur());
  const curN = () => page.evaluate(() =>
    [...document.querySelectorAll('#results .card')].findIndex(c => c.classList.contains('cur')));
  L.check('no card is current before j is pressed', (await curN()) === -1);
  await page.keyboard.press('j');
  await page.keyboard.press('j');
  await page.waitForTimeout(150);
  const afterJJ = await curN();
  await page.keyboard.press('k');
  await page.waitForTimeout(150);
  const afterK = await curN();
  L.check('j moves the current card down and k moves it up',
    afterJJ === 1 && afterK === 0, `j,j -> ${afterJJ}; k -> ${afterK}`);
  L.check('only one card is ever current',
    (await page.locator('#results .card.cur').count()) === 1);
  await page.focus('#q');
  await page.keyboard.press('j');
  L.check('j typed into the search box is just a letter',
    (await page.inputValue('#q')).includes('j'), await page.inputValue('#q'));

  // ---------- export ----------
  await L.search(page, 'agents');
  L.check('the export bar shows with results',
    await page.evaluate(() => !document.querySelector('#tools').hidden &&
      ['x-md', 'x-csv', 'x-link'].every(id => document.getElementById(id))));
  const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 5000 }).catch(() => null),
                                  page.click('#x-md')]);
  L.check('Markdown export downloads a file', !!dl && /\.md$/.test(dl.suggestedFilename()),
    dl ? dl.suggestedFilename() : 'no download');
  await L.search(page, 'zzzqqqxyzzy');
  L.check('the export bar hides on an empty result set',
    await page.evaluate(() => document.querySelector('#tools').hidden));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
