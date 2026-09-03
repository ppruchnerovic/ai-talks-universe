# Search enrichment options

> **Status, 2026-09-02.** Built the same day, in four parallel strands —
> the write-up is *Search enrichment* in `HISTORY.md`. CLI Tier 1 entire,
> plus synonym groups from Tier 2 (as one shared table, `atu.SYNONYMS`); the
> skill's Tier A entire; browser items 1–11 and 15 plus the language badge;
> and the Tier B semantic layer as model2vec at talk level with chunk anchors,
> installed by `tools/install_semantic.sh`. Deliberately not built: browser
> related talks (12), typo tolerance (13), autocomplete (14), `_vocab.json`,
> talk pages, and everything needing a schema bump — `--lang`, `fts5vocab`
> did-you-mean, the trigram fuzzy speaker, `--related`, `--near`. The text
> below is the proposal as written; "nothing here is built" no longer holds.

An exploration, 2026-09-02, of how the three search surfaces — `tools/query.py`,
`index.html` and the `ai-conference-talks` skill — could be enriched. The brief
was: nothing new to install for the browser or the CLI; for the skill, at most
a light optional setup that can be prepared from the repo, no compiling.

Nothing here is built. Line numbers refer to the tree at `74883cbc`.

## Environment, verified

| Fact | Value |
|---|---|
| Python | 3.12.3, no third-party packages on the system interpreter |
| SQLite | 3.45.1 — FTS5 with `porter`, `unicode61`, **`trigram`** tokenisers and `fts5vocab` all available; `spellfix1` not compiled in; `load_extension` allowed |
| node | v24 (only needed by the Playwright suite) |
| `tools/.venv` (main checkout) | requests, youtube-transcript-api, yt-dlp; no numpy |

## What the data can support

A filter or sort is only worth adding on a field that is populated and varied.

| Field | Coverage | Verdict |
|---|---|---|
| conference, category, year | 100% | already exposed everywhere |
| `duration_min` | 100%, Q1 20 min, median 30, Q3 44; 429 under 10 min, 523 over 60 | **not exposed anywhere**; a sort and a length bucket are well supported |
| `edition` (95 values) | 100% | not exposed; a finer facet than conference for Ignite/Build/QCon |
| `published_at` | 81%, day precision | "newest" sort uses it; a date range is viable, with fallback to `year` for the 1,717 without it |
| speakers | 55% of talks, 5,510 distinct, 84% appear once | strong as a *search field* (already 4× weight), sparse as a *facet*; coverage is per-conference (ai-engineer 90%, re:Invent 0.3%) |
| tags | 50% of talks, 8,780 distinct, top 20 are channel branding | poor facet, fine at low weight; do not build UI on them |
| transcript `timing` | exact 2,946 / estimated 228 | filter is cheap, low value |
| transcript `language` | 3,143 `en`; 12 `hi` are mis-read English | a badge, not a filter; already an open TODO |
| description | 78%; the browser ships only a 300-char clip | full text is indexed in shards, not shipped |

Transcript coverage is skewed: 99% of 2026 talks, 6% of 2025, none earlier;
Ignite and re:Invent have zero. Any facet count or "compare across
conferences" mode will show this, which is the argument for building one.

## Already decided, so not relitigated here

- Embeddings/semantic search: rejected *for now, by choice* (TODO.md, "Not
  built, by choice"). Tier B below is the honest cost if that changes.
- Two rankers must agree by construction: same stemmer, weights, relaxation
  order, `shard_key()` = `shardKeyOf()`. Tokens, never substrings.
- Builds are idempotent and byte-identical. `search-meta.json` sits at 5.79 MiB
  of a 6 MiB trigger; a new per-talk field must be tiny or lazy-loaded.
- Any `talks.db` schema change bumps `DB_SCHEMA_VERSION` (`atu.py:516`).
- 183 Playwright checks and the six Python test files stay green.

## Two bugs found on the way

1. **Column filters are mangled in the CLI.** FTS5 supports `title:agent`,
   `speakers:"harrison chase"`, `{title tags}:rag` natively and they work on
   `talks_fts` directly. `query.py` breaks them: `title:agents` takes the bare
   path and `WORD_RE` (`query.py:128`) splits on the colon, giving
   `"title" AND "agents"`; `speakers:"harrison chase"` takes the explicit path
   and `quote_term()` (`:185`) wraps the prefix in quotes, giving a phrase that
   matches nothing (verified: zero results). Fix is small: recognise
   `\w+:` / `\{…\}:` in `EXPLICIT_RE` (`:127`), pass prefixes through
   unquoted, and strip prefixes other than `transcript:` on the segment layer.
2. **`year:2025` in the browser searches the stem "year".** Same root cause:
   the tokeniser charset (`index.html:329-349`) has no colon, so `year` becomes
   a required term that relaxation then drops with a status note.

A third finding is not a bug but a cost: `query.py` emits ANSI colour
unconditionally (`:576`, no `isatty()` check anywhere), so 13% of the bytes a
model reads through the skill are escape codes.

## CLI — `tools/query.py`

Everything below is stdlib plus the SQLite already present.

### Tier 1: no schema change, each an afternoon

| Option | Where | Notes |
|---|---|---|
| Fix column filters, gaining `title:`, `speakers:`, `tags:`, `transcript:` scoping | `parse_query` `:200-247`, `quote_term` `:185` | add cases to `test_query.py`; document at README "From the terminal" |
| Colour only on a TTY, honour `NO_COLOR` | `:576`, `render` `:601-636` | direct saving for the skill |
| `--speaker NAME` | `build_filters` `:259-273` | `LIKE` on the comma-joined column, or a `speakers:` MATCH intersected into the pool; a split-and-count gives did-you-mean |
| `--sort newest\|oldest\|duration\|title` | after `:415` | take a wider candidate set and keep a score floor, or sorting by date over thousands of hits loses relevance entirely |
| `--min-duration` / `--max-duration`, `--max-year`, `--since` / `--before` | `build_filters` | ISO strings compare lexically; `--since` falls back to `year` when `published_at` is null |
| `--exact-timing` | `build_filters` | column exists; `--stats` already counts it |
| `--explain` | `emit_json` `:649` | per-layer `meta`, `seg`, `together` are computed and then popped |
| `--fields a,b,c` for JSON | `emit_json` `:647` | `--brief` becomes a preset |
| `--md` markdown table | beside `render`/`emit_json` `:750-758` | all columns are in the hit dict |
| `--random [--seed]`, and allow filter-only listings with no query | `:732` errors today | |
| `-word` exclusion in bare queries | `parse_query` `:243`, pool at `:319` | subtract `talks_saying(word)`; ranking is unaffected. `NOT` already works via the explicit path |
| `--facets` | extend `Result` `:293` to return the pool; group by conference/year/category/has_transcript | measured ~4 ms; the model-facing reason is below under Skill |
| `--per-conference K` / `--per-year K` | window function over a larger ranked set | replaces the per-conference loop the skill currently prescribes |

### Tier 2: schema bump (`DB_SCHEMA_VERSION`), still zero dependencies

| Option | What it needs | Measured |
|---|---|---|
| `language` column, `--lang` | store `tr["language"]` at `build_index.py:265` | main value is excluding the 12 `hi` mis-detections |
| Did-you-mean for typos | an `fts5vocab(talks_fts,'row')` table in the schema; `difflib.get_close_matches(stem, vocab, cutoff≈0.75)` on any word whose `present` set is empty, in the relaxation loop at `:325` | 31,810 stems load in 50 ms; `retreival→retriev`, `kubernets→kubernet`, `harrisn→harrison` in ~30 ms each |
| Fuzzy `--speaker`, substring title match | a small `trigram`-tokenised FTS5 table over title+speakers+tags; OR the query's trigrams and rank by bm25 | table builds in 0.14 s, query 1-2 ms; note plain `MATCH` on a trigram table is substring, not fuzzy, so the OR-of-trigrams is the whole trick |
| `--like VIDEO_ID` / `--related` | none beyond `fts5vocab` for df; top ~12-20 tf-idf stems of the talk (title + tags + transcript `Counter`, minus stopwords, df capped at 1-2% of N) as one OR query through `rank()`, source excluded | mechanism verified at 10 ms; term selection quality is the work |
| Synonym map (`llm`, `rag`, `mcp`, `k8s`, `genai`) | expand at `parse_query` into OR groups; each group is one gate term | print the expansion on stderr as relaxation does; keep weak, since the ranking-agreement suite compares against the browser |
| `--near N` for bare queries | rewrite `together_q` `:333` to `NEAR(...)` | changes ranking; check the `ranking` suite |

## Browser — `index.html`

All vanilla JS inside the one file. "Free" means the data is already
client-side.

### Free

| # | Option | Where | Effort / risk |
|---|---|---|---|
| 1 | Field syntax `title:` `speaker:` `conf:` `year:` (fixes bug 2) | parse before `surface` in `search` `:570`; `year:`/`conf:` set the selects, others pass a field mask into `scoreMeta` `:459` | S/M, low |
| 2 | `-word` exclusion | parse before the dash is stripped; skip talks with the stem in `_tok`, `described` or `e.p` in `gather` `:550` | S, low |
| 3 | Real quoted phrase on metadata | `:473` is a boost today; make it a gate | S, low. True transcript phrase search would need word positions in shards (tens of MB): decline |
| 4 | "Said together" badge | `passageFactor` `:532` already knows `together > 0` | S, low |
| 5 | `OR` groups, then synonyms on top | gate at `:561` becomes every-group-has-a-member | M, low |
| 6 | Explicit `prefix*` | `fieldHit` length gate `:453`, `scoreTranscripts` keys `:498` | S, low |
| 7 | Speaker filter with typeahead | list from `fillFilters` `:406`; filter in `:690`; hash `spk` | M; needs `aria-label`, keep after the selects for the Tab-order check |
| 8 | Duration sort (`shortest`/`longest`) and a length bucket | sorts `:698-701`, hash whitelist `:879` | S, low |
| 9 | Facet counts on the selects ("AI Engineer (37)") | count `cs`/`g`/`y` over hits filtered by the *other* dimensions in `render` | S; change labels only, `suite-filters` reads values |
| 10 | Transcripts-only mode | gate on `tr?.matched`, drop `m.score` at `:564` | S, low |
| 11 | "Also matches in the full description" hint | expose `described` from `gather` to `card` `:651` | S, low |
| 12 | Related talks | cosine over idf-weighted title stems ∪ tags, computed on click; link in `card` `:663` | M, low |
| 13 | Typo tolerance, cheap form | when `talksWith(term)==0` at `:586`, scan the loaded shard's keys at Damerau distance ≤1, plus the swapped-first-pair shard | S; covers typos after character 2 |
| 14 | Autocomplete from tags + speakers + title tokens | prefix map built in `boot` | M; use `aria-activedescendant`, never move focus |
| 15 | Export (Markdown/CSV), copy link, j/k keyboard nav, newest-first preference in `localStorage` | `render`, `:858`, `:873` | S each |

### Needs `build_index.py` to emit more

| Option | Bytes | Notes |
|---|---|---|
| Language badge (`lg` only when not `en`) | ~300 B | closes the TODO item; label it "transcript language" since the `hi` ones are English |
| `_vocab.json` (stems + df) for full typo tolerance and vocabulary autocomplete | 150-450 KB, fetched only when relaxation triggers | zero boot cost |
| Talk page `#talk=<id>` with the full description | per-talk JSON files | do not raise `META_DESC_CHARS`; `pushState` would break the replace-only contract `suite-navigation` asserts |
| Inline transcript snippet on every card | none, but ~1.1 MB per page of 20 | don't; instead auto-open moments for the top 3 transcript cards |

## Skill — `.claude/skills/ai-conference-talks`

SKILL.md is not outdated: every flag it cites exists. Measured cost of the
canonical question ("agent reliability"): `--brief -n 15` is 7 KB, six
excerpts at `-n 6` are 27 KB, wall time under a second.

### Tier A — no dependencies

1. **Strip ANSI when piped** (above). The single cheapest win.
2. **`query.py … --excerpt`**: `excerpt.py` already imports `query` and shares
   `parse_query` and the bm25 (`excerpt.py:35,182-194`); one flag removes a
   tool round-trip and the `xargs` step. Print the relaxation note
   ("dropped X") into stdout, not stderr, where a model misses it.
3. **`--facets`**: the top-100 for "agent reliability" is 75% year-2026 and
   25% ai-engineer purely because that is where the transcripts are. Nothing
   tells the model this before it chooses a slice.
4. **`--per-conference K`**: replaces SKILL.md:118-119's five-call loop.
5. **`--max-year` / `--year 2024-2025`**: for "how did the framing change".
6. **Duplicate collapse**: 70 titles occur 2-3 times, nearly always
   same-conference re-uploads; a model reads them as independent agreement.
   Mark `dup_of` at build time or note "(also: id, id)" in `render`.
7. **`excerpt.py --quotes`**: only the sentence containing a query term, with
   timestamp and link; ~40 tokens a quote against ~400 a window. Tiles are 25
   words, so split on `[.?!]` across the hit tile ±1 and fall back to the tile.
8. **`excerpt.py --outline`**: 2-minute buckets, top tf-idf stems and query
   density per bucket, ~300 tokens for an hour. The density view is the
   reliable part; it tells the model where to aim a second `-q`.
9. **`--related <id>`** as in the CLI tier 2.
10. **`--words N` / `--total-words N`** on excerpt: the model reasons in
    tokens, `-n` is seconds. Rule of thumb worth writing down: `-n 6` ≈ 1,100
    tokens a talk, `-n 3` ≈ 850.

SKILL.md text changes, independent of code:
- `-n` means result limit in `query.py` and passage budget in `excerpt.py`;
  models copy `-n 15` from step 1 into step 2.
- Text `--brief` contains nothing quotable (`render(hits, moments and not
  brief)` at `query.py:753`); say so.
- Stemming is on, so OR chains should carry synonyms and adjacent vocabulary,
  not inflections. Add the loop: search once, harvest the corpus's own words
  from the snippets, re-query.
- Use `python3 tools/query.py` from the repo root; subagents reset cwd.
- Mention `NEAR(a b, 10)` for "X in the context of Y" questions.

### Tier B — optional semantic layer, honest costs

| Option | Pulls in | Build | Compiling | Gain |
|---|---|---|---|---|
| Pure-Python TF-IDF `related.json` | nothing | ~90 s, 1.5 MB | no | none over FTS5; superseded by `--related` |
| sentence-transformers | torch (CUDA wheel ~2.5 GB, CPU ~200 MB) + transformers | 10-30 min | no, but very heavy | high |
| fastembed (bge-small) | onnxruntime ~20 MB wheel, tokenizers, numpy, hf-hub; model 65-130 MB download | 1-3 min talk-level, 10-30 min chunk-level | no | high |
| **model2vec** (potion-base-8M) | numpy, tokenizers, safetensors; model ~30 MB; no torch, no onnx | 1-2 min for 17M words | no | moderate, well above lexical on vocabulary mismatch |
| sqlite-vec | prebuilt wheel <1 MB | storage only, needs vectors from above | no | none by itself; brute-force numpy is as fast at 85k vectors |
| sqlite-vss | faiss | — | yes | reject |
| Hosted embeddings at build | urllib + key | ~$0.50-0.80 once | no | high, but the *query* must be embedded too, so every skill user needs the key |

If a semantic layer is ever wanted, the simplest that gives a real improvement
with no compiling is **model2vec at talk level**: 9k × 384 fp16 ≈ 7 MB, could
be committed, fused with FTS5 by reciprocal rank. Chunk-level vectors (65 MB
fp16) would be derived and gitignored like `talks.db`. Three rules if it is
built: opt-in only (`build_index.py --embed`, never via `db_stale()`
auto-rebuild); `query.py` falls back silently to FTS5 when the file is absent;
fuse by *union* + RRF, not rerank, because the failure mode is recall. A
semantic hit may contain none of the `-q` words, so `excerpt.py` needs an
`--at SECONDS` companion or it falls into its "showing the opening" path.

## Suggested order

1. **CLI, one session:** column-filter fix, TTY-gated colour, `--speaker`,
   `--sort`, duration and date filters, `--exact-timing`, `--explain`,
   `--fields`, `-word`, `--facets`, `--per-conference`. No schema change; add
   `test_query.py` cases; document in README.
2. **Skill, same session or next:** `--excerpt`, `--quotes`, duplicate
   collapse, and the SKILL.md wording above.
3. **Browser, one session:** field syntax (with the `year:` fix), `-word`,
   duration sort, transcripts-only mode, facet counts, "said together" badge,
   language badge (tiny build change), export. Run the full Playwright suite.
4. **Schema bump, later:** `language`, `fts5vocab` did-you-mean, trigram
   fuzzy speaker, `--related`, synonyms on both sides at once so the rankers
   stay in agreement.
5. **Semantic layer:** only if step 4's `--related` and synonyms prove
   insufficient; model2vec at talk level.
