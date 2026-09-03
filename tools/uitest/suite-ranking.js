// Ranking quality. Two kinds of check:
//
//   * agreement with query.py, which ranks the same corpus in SQLite with a
//     different algorithm. Neither is ground truth, but a browser scorer that
//     has drifted badly from the CLI is worth knowing about.
//
//     The comparison is made at the web's top 40, not its top 10. The two
//     rankers disagree about *ordering* by design — talks.db tokenises with
//     Porter stemming, the browser matches token prefixes, and their field
//     weights differ — and on a corpus this size a query like "kubernetes" has
//     dozens of near-identical title matches, so which ten come first is a
//     coin toss between two good answers. Measured over the eight queries
//     below, the CLI's top 10 lands in the web's top 10 between 0 and 9 times,
//     and in its top 40 between 4 and 10 times. A drop below 4 at 40 means one
//     of the two has actually broken, which is what this is for.
//   * properties that hold regardless of algorithm: the best hit for an
//     unambiguous topic is a talk about that topic, and the same query twice
//     gives the same answer.
//
// The CLI half is skipped when data/talks.db has not been built — query.py
// would otherwise spend a minute building it mid-test.

const L = require('./lib');
const { execFileSync } = require('child_process');
const path = require('path');
const fs = require('fs');

const TOOLS = path.join(__dirname, '..');
const DB = path.join(TOOLS, '..', 'data', 'talks.db');

const CLI_QUERIES = ['prompt injection', 'context engineering', 'agent evaluation',
  'retrieval augmented generation', 'kubernetes', 'fine tuning', 'multi agent', 'inference'];

// A query whose answer is not in doubt, and the shape its top hit must have.
// Each is checked against the title and the badges, so a talk from the PyTorch
// conference counts as on topic for "pytorch" even when its title is coy.
const ON_TOPIC = {
  kubernetes: /kubernetes|k8s|cloud native/i,
  pytorch: /pytorch|torch/i,
  copilot: /copilot|github/i,
  langgraph: /langgraph|langchain/i,
};

L.suite('ranking', async browser => {
  const page = await L.newPage(browser);
  await L.boot(page);
  const meta = await L.meta(page);
  const vOf = new Map(meta.talks.map(t => [t.i, t.v]));

  if (!fs.existsSync(DB)) {
    L.skip('CLI agreement', 'data/talks.db not built (run: python3 build_index.py)');
  } else {
    for (const q of CLI_QUERIES) {
      // Lexical against lexical: query.py fuses in a vector layer when
      // data/embeddings exists, and the browser has no such layer to agree
      // with.
      const cli = JSON.parse(execFileSync('python3',
        ['query.py', q, '-n', '10', '--json', '--no-semantic'],
        { cwd: TOOLS, maxBuffer: 1 << 26 }).toString()).map(h => h.id);
      await L.search(page, q);
      // Two clicks of "Show more" — the first 40 results.
      for (let i = 0; i < 2; i++) {
        if (await page.locator('#more:visible').count()) {
          await page.click('#more');
          await page.waitForTimeout(250);
        }
      }
      const web = (await L.cardNs(page)).slice(0, 40).map(n => vOf.get(n));
      const overlap = web.filter(v => cli.includes(v)).length;
      L.check(`"${q}": the web top 40 contains what the CLI ranked first`,
        cli.length === 0 || overlap >= Math.min(4, cli.length),
        `${overlap} of the CLI's ${cli.length} hits are in the web top 40`);
    }
  }

  for (const [q, re] of Object.entries(ON_TOPIC)) {
    await L.search(page, q);
    const title = (await L.titles(page))[0] || '';
    const badges = await page.$$eval('#results .card:first-child .b',
      bs => bs.map(b => b.textContent).join(' '));
    if (!title) { L.skip(`"${q}": the top hit is on topic`, 'no hits in this corpus'); continue; }
    L.check(`"${q}": the top hit is on topic`, re.test(title) || re.test(badges), `${title} [${badges}]`);
  }

  await L.search(page, 'agents');
  const first = await L.cardNs(page);
  await L.search(page, 'zzz');
  await L.search(page, 'agents');
  L.check('the same query twice gives the same order',
    JSON.stringify(first) === JSON.stringify(await L.cardNs(page)));

  L.check('no uncaught errors', page.__errors.length === 0, page.__errors.join('; '));
});
