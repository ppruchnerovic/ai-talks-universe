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
  if (meta.talks.filter(t => (t.d || '').length > 40).length > 40) {
    await L.search(page, '');
    await page.evaluate(() => { for (let i = 0; i < 8; i++) document.querySelector('#more').click(); });
    await page.waitForTimeout(600);
    const abs = await page.evaluate(() => {
      const rows = [...document.querySelectorAll('#results .card')].map(c => {
        const p = c.querySelector('.abs'), b = c.querySelector('.abs-more');
        if (!p || !b) return null;
        return { overflows: p.scrollHeight > p.clientHeight + 2, visible: b.offsetParent !== null };
      }).filter(Boolean);
      return { total: rows.length, short: rows.filter(r => !r.overflows).length,
               wrong: rows.filter(r => !r.overflows && r.visible).length };
    });
    L.check('the unfold button appears only where the clamp actually hides something',
      abs.wrong === 0, `${abs.wrong} wrong of ${abs.short} untruncated / ${abs.total} cards`);
    L.check('the corpus contains untruncated descriptions, so that check means something',
      abs.short > 0, `${abs.short} of ${abs.total}`);
  } else {
    L.skip('the unfold button appears only where text is truncated',
      'descriptions not collected yet — run enrich.py');
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

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
