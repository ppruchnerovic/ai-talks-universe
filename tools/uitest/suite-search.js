// Every search option the UI offers: free text over each indexed field, the
// transcript layer, quoted phrases, prefixes, and the tokenising rules that
// keep a search for "rag" out of every talk that says "program".

const L = require('./lib');

L.suite('search', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);
  const N = meta.talks.length;
  const count = q => L.search(page, q).then(() => L.resultCount(page));

  // ---------- one term ----------
  await L.search(page, 'kubernetes');
  const st = (await L.statusText(page)).trim();
  const n = await L.resultCount(page);
  L.check('a single term returns a bounded result set', n > 0 && n < N, st);
  L.check('the status line echoes the query', st.includes('matching') && st.includes('kubernetes'), st);
  const tops = await L.titles(page);
  L.check('the top hits are on topic', /kubernetes|k8s/i.test(tops.slice(0, 3).join(' | ')), tops[0]);

  const marks = await page.$$eval('#results mark', ms => ms.map(m => m.textContent.toLowerCase()));
  L.check('matched terms are highlighted',
    marks.length > 0 && marks.every(m => m.startsWith('kub')),
    [...new Set(marks)].slice(0, 5).join(','));

  // ---------- several terms are ANDed ----------
  const nAgents = await count('agents');
  const nSecurity = await count('security');
  const nBoth = await count('agents security');
  L.check('a multi-term query is AND, not OR',
    nBoth <= Math.min(nAgents, nSecurity) && nBoth > 0,
    `agents=${nAgents} security=${nSecurity} both=${nBoth}`);

  const idsA = await L.cardNs(page);
  await L.search(page, 'security agents');
  L.check('term order does not change the ranking',
    JSON.stringify(idsA) === JSON.stringify(await L.cardNs(page)), `${idsA.length} cards`);

  await L.search(page, 'evals evals evals');
  const dup = await L.resultCount(page);
  L.check('repeated terms are de-duplicated', dup === await count('evals'), `${dup}`);

  // ---------- tokens, not substrings ----------
  // "rag" is the corpus's best trap: it sits inside "program", "storage" and
  // "fragment", and a substring matcher lights all of them up.
  await L.search(page, 'rag');
  const ragMarks = await page.$$eval('#results mark',
    ms => [...new Set(ms.map(m => m.textContent.toLowerCase()))]);
  L.check('"rag" is never highlighted inside "program" or "storage"',
    ragMarks.every(m => m.startsWith('rag')), ragMarks.join(','));
  L.check('"rag" still finds the retrieval talks',
    /rag|retrieval/i.test((await L.titles(page)).join(' ')), (await L.titles(page))[0] || '(none)');

  // ---------- prefixes ----------
  const nAgentic = await count('agentic');
  L.check('a prefix search widens the result set ("agent" also finds "agentic")',
    nAgents >= nAgentic && nAgentic > 0, `agents=${nAgents} agentic=${nAgentic}`);
  await L.search(page, 'agent');
  const agentMarks = await page.$$eval('#results mark',
    ms => [...new Set(ms.map(m => m.textContent.toLowerCase()))]);
  // A hyphenated compound ("multi-agent") is marked whole when one of its
  // parts matches — that is the highlighter's rule — so the test is that
  // some part of every mark starts with the stem, never a bare "management".
  L.check('a prefix hit is highlighted at the stem',
    agentMarks.every(m => m.split(/[.\-]+/).some(p => p.startsWith('agent'))), agentMarks.join(','));

  // ---------- stemming ----------
  // talks.db tokenises with Porter; the browser index is keyed on the same
  // stems, so an inflection is not a different search.
  const nEvaluate = await count('evaluate');
  const nEvaluation = await count('evaluation');
  L.check('"evaluate" and "evaluation" are one search',
    nEvaluate > 0 && nEvaluate === nEvaluation, `evaluate=${nEvaluate} evaluation=${nEvaluation}`);
  await L.search(page, 'evaluating');
  const evMarks = await page.$$eval('#results mark',
    ms => [...new Set(ms.map(m => m.textContent.toLowerCase()))]);
  L.check('an inflected query highlights every inflection it matched, as whole words',
    evMarks.length > 0 && evMarks.every(m => m.startsWith('evalu')), evMarks.join(','));

  // ---------- relaxation ----------
  await L.search(page, 'kubernetes zzzqqqxyzzy');
  const relaxed = (await L.statusText(page)).trim();
  L.check('a word no talk says is dropped rather than emptying the result',
    (await L.resultCount(page)) === n && /dropped/.test(relaxed) && /zzzqqqxyzzy/.test(relaxed),
    relaxed.slice(0, 120));
  await L.search(page, 'kubernetes');
  L.check('a query that needs no relaxing says nothing about it',
    !/dropped/.test(await L.statusText(page)));

  // ---------- quoted phrase ----------
  await L.search(page, '"prompt injection"');
  const phraseN = await L.resultCount(page);
  const topN = (await L.cardNs(page))[0];
  const top = meta.talks.find(t => t.i === topN);
  const hay = [top.t, top.d, (top.a || []).join(' ')].join(' ').toLowerCase();
  L.check('a quoted phrase returns results', phraseN > 0, `${phraseN} hits, top: ${top.t}`);
  L.check('the phrase bonus puts an exact-phrase talk first', hay.includes('prompt injection'), top.t);
  L.check('quoting never widens the result set',
    phraseN <= await count('prompt injection'), `${phraseN}`);

  // ---------- each indexed field ----------
  const speaker = (meta.talks.find(t => (t.s || []).some(x => x.split(' ').length >= 2)) || {}).s;
  if (speaker) {
    const name = speaker.find(x => x.split(' ').length >= 2);
    await L.search(page, name);
    const who = await page.$$eval('#results .who', ws => ws.map(w => w.textContent.toLowerCase()));
    L.check(`a speaker name ("${name}") finds their talk`,
      who.some(w => w.includes(name.split(' ')[0].toLowerCase())), who[0]);
  } else {
    L.skip('a speaker name finds their talk', 'no speakers identified in the corpus yet');
  }

  const confName = meta.talks[0].c;
  const confHits = await count(confName);
  L.check(`a conference name ("${confName}") returns hits`, confHits > 0, `${confHits}`);

  // The conference type is a filter, not a searched field — see suite-filters.

  const tagged = meta.talks.find(t => (t.a || []).length);
  if (tagged) {
    const tag = tagged.a[0];
    L.check(`a tag ("${tag}") returns hits`, await count(tag) > 0);
  } else {
    L.skip('a tag returns hits', 'no YouTube tags collected yet — run enrich.py');
  }

  const described = meta.talks.filter(t => (t.d || '').length > 80);
  if (described.length > 20) {
    // A word that appears in a description but in no title anywhere: the only
    // way it can be found is if descriptions are really searched.
    const titles = new Set(meta.talks.flatMap(t => (t.t || '').toLowerCase().match(/[a-z]{6,}/g) || []));
    let probe = null;
    for (const t of described.slice(0, 400)) {
      probe = ((t.d || '').toLowerCase().match(/[a-z]{7,}/g) || []).find(w => !titles.has(w));
      if (probe) break;
    }
    if (probe) L.check(`a description-only word ("${probe}") is searchable`, await count(probe) > 0);
    else L.skip('a description-only word is searchable', 'no such word found');
  } else {
    L.skip('descriptions are searched', 'descriptions not collected yet — run enrich.py');
  }

  // The browser holds a 300-character clip of each description; the rest of
  // the text is searchable only if the shards really carry it. A word from the
  // tail of a long description that appears nowhere in the up-front payload
  // is findable only through them.
  const deep = await page.evaluate(async () => {
    const full = await fetch('data/talks.json').then(r => r.json());
    const meta = await fetch('data/search-meta.json').then(r => r.json());
    const hay = new Set(meta.talks.flatMap(t =>
      [t.t, t.d, (t.a || []).join(' '), (t.s || []).join(' '), t.c, t.e].join(' ')
        .toLowerCase().match(/[a-z]+/g) || []));
    for (const t of full.talks) {
      if ((t.description || '').length < 900) continue;
      const tail = t.description.slice(600).toLowerCase();
      const w = (tail.match(/\b[a-z]{9,}\b/g) || []).find(x => !hay.has(x));
      if (w) return { w, id: t.id };
    }
    return null;
  });
  if (deep) {
    L.check(`a word beyond the description clip ("${deep.w}") is found through the shards`,
      await count(deep.w) > 0, `from ${deep.id}`);
  } else {
    L.skip('a word beyond the description clip is searchable', 'no long description with a unique tail word');
  }

  // ---------- the transcript layer ----------
  if (meta.talks.some(t => t.w > 0)) {
    let spoken = null;
    for (const q of ['nginx', 'kafka', 'postgres', 'latency', 'hallucination', 'benchmark']) {
      await L.search(page, q);
      const s = (await L.statusText(page)).trim();
      if (/found only in the spoken transcript/.test(s)) { spoken = `${q} -> ${s}`; break; }
    }
    L.check('talks matched only by what was said are counted separately', !!spoken,
      spoken || 'no sampled query surfaced a transcript-only hit');
  } else {
    L.skip('transcript-only hits are counted separately', 'no transcripts fetched yet');
  }

  // ---------- compounds and punctuation ----------
  await L.search(page, 'ai assisted');
  L.check('"ai assisted" matches the hyphenated "AI-assisted"',
    /ai[- ]assisted/i.test((await L.titles(page)).join(' | ')),
    (await L.titles(page))[0] || '(none)');

  for (const q of ['.net', 'c#', 'ci/cd', 'gpt-4']) {
    await L.search(page, q);
    L.check(`a punctuation-bearing query ("${q}") resolves`, page.__errors.length === 0,
      (await L.statusText(page)).trim().slice(0, 55) || 'empty state');
  }

  // ---------- queries that match nothing, or everything ----------
  await L.search(page, 'zzzqqqxyzzy');
  L.check('a nonsense query shows the empty state',
    (await page.locator('.empty h3').textContent().catch(() => null)) === 'Nothing matched');

  await L.search(page, 'the and of');
  L.check('a stopword-only query falls back to browsing the catalogue',
    (await L.resultCount(page)) === N, `${await L.resultCount(page)} vs ${N}`);

  await L.search(page, '   ');
  L.check('a whitespace-only query resets to browsing', (await L.resultCount(page)) === N);

  await L.search(page, '""');
  L.check('bare quotes do not throw', page.__errors.length === 0, page.__errors.join(';'));

  // ---------- input handling ----------
  const lower = await count('kubernetes');
  L.check('the query is case- and whitespace-insensitive',
    lower === await count('KUBERNETES') && lower === await count('  Kubernetes  '), `${lower}`);

  await page.fill('#q', '');
  await page.type('#q', 'kubernetes', { delay: 20 });
  await page.waitForTimeout(800);
  L.check('typing settles on the same result as pasting (no lost race)',
    (await L.resultCount(page)) === lower, `${await L.resultCount(page)} vs ${lower}`);

  // The native ✕ on a type=search input fires `input` with an empty value.
  await page.evaluate(() => {
    const q = document.querySelector('#q');
    q.value = '';
    q.dispatchEvent(new Event('input', { bubbles: true }));
  });
  await page.waitForTimeout(500);
  L.check('the field\'s native ✕ clears the search', (await L.resultCount(page)) === N);

  L.check('no uncaught errors across the suite', page.__errors.length === 0, page.__errors.join('; '));
  L.check('no failed requests', page.__requests.length === 0, page.__requests.slice(0, 3).join('; '));
});
