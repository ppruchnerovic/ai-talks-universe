# Transcripts — fetching YouTube captions

## What

`tools/fetch_transcripts.py` turns a talk record (`data/talks.json`, see
`data-model.md`) into a timed transcript file `data/transcripts/<video_id>.json`.
It is the only stage that talks to YouTube's caption endpoint, and the only
stage that spends money (Supadata credits). It is run by hand on a real
machine — never from CI, because YouTube blocks GitHub's IP ranges outright
(`.github/workflows/kb-refresh.yml:3-6`).

Responsible for:

- Choosing which talks to fetch (`select()`), re-derived from disk on every run.
- Walking a **route ladder** per talk — two free routes from this machine's IP,
  one paid and one free route from somebody else's — cheapest first, exact
  timings before estimates.
- Classifying every failure into one of **four classes**, exactly one of which
  (`LookupError`) is a fact about the video and is recorded in
  `data/transcripts/_misses.json`. The other three leave the talk retryable.
- Rationing the **per-IP quota** with an egress pool (direct IP plus optional
  proxies), benching a blocked identity and carrying on down the rest.

Not responsible for:

- InfoQ transcripts (`source: "infoq"`, 228 files): produced by `tools/infoq.py`
  — see `catalog-sync.md`. The 356 files carrying `imported_from` came in via
  `import_kb.py`, same spec.
- Folding transcripts into markdown or the indexes: `sync_catalog.py` then
  `build_index.py` (`catalog-sync.md`, `search-cli.md`, `search-browser.md`).
  A transcript on disk is invisible to every reader until both have run.
- Descriptions/metadata: `enrich.py` (`catalog-sync.md`). Note that its yt-dlp
  route draws on the **same** per-IP allowance as the free transcript routes.

Corpus as of 2026-09-03: 3,174 transcript files (`supa` 2,491 · `yt` 455 ·
`infoq` 228; `ytdlp` and `kome` have produced none that survive), 29 misses,
all `LookupError`. 2,946 are `timing: "exact"`, 228 `"estimated"` (all InfoQ).
Languages: 3,143 `en`, 12 `hi` (see How), a handful of `de/es/ja/no/lt/...`.

## Where

| Path | What |
|---|---|
| `tools/fetch_transcripts.py` | The fetcher. 1,213 lines; module docstring is an accurate short manual. |
| `tools/test_fetch_transcripts.py` | Offline suite (fake HTTP, fake allowances, ~1 s). `cd tools && python3 test_fetch_transcripts.py`. |
| `tools/atu.py` | Shared helpers the fetcher leans on (below). |
| `tools/requirements.txt` | `youtube-transcript-api>=1.0`, `yt-dlp>=2025.1.1` — the only third-party deps in the repo; installed in `tools/.venv` (gitignored). |
| `data/transcripts/<id>.json` | One file per YouTube id, compact JSON. |
| `data/transcripts/_misses.json` | `{video_id: {conference, reason, detail}}` — "this video has no captions". Permanent until `--retry-misses`. |
| `logs/` | Gitignored scratch (`.gitignore`: "run logs from local collection runs"). Nothing reads it. |
| `STATE.md` §"Handoff — running a transcript extraction", §"The quota" | Operational prose this spec distils. |
| `ARCHITECTURE.md` §"Fetching transcripts" | Mermaid diagrams of the ladder, the failure classes, the pool. |
| `README.md` §"Transcripts, and YouTube's quota", §"Beating the per-IP quota" | Measured yields and the reasoning. |
| `HISTORY.md` §"Bug 7 cannot be fixed by refetching", §"The 402 that was recorded as 'no captions'" | Why the invariants below exist. |

### `tools/fetch_transcripts.py` — map

Constants (`:82-103`): `KOME_API`, `SUPADATA_API`, `OFF_IP_WORKERS = 8`,
`UA` (an honest client string; a Chrome UA makes Zscaler return an HTML
interstitial at HTTP 200), `MISSES`, `LANGUAGES` (preference order, `en` first,
then `de es fr pt it nl ja pl uk`), `YTDLP_SUB_LANGS`.

| Symbol | Line | Purpose |
|---|---|---|
| `base_lang`, `named_lang`, `lang_ok`, `LANG_RANK`, `UNNAMED_LANGS` | 106-146 | Language tag folding (`en-US`/`en-orig` → `en`); `"none"/""` → `"und"`. `lang_ok` decides which track to *ask for*, never whether to keep a talk. |
| `BlockedError`, `AccountError`, `TransientError`, `RateLimited(TransientError)` | 149-182 | The three non-video failure classes. |
| `is_block(e)` | 185 | `BlockedError` or a youtube-transcript-api exception named `IpBlocked`/`TooManyRequests`/`RequestBlocked`. |
| `about_the_video(e)` | 193 | The gate before writing a miss: not a block, not Account, not Transient. Anything else (incl. `LookupError` and any unknown exception) is a miss. |
| `redact`, `normalise_proxy` | 206-226 | Strip creds from printed URLs; accept `host:port:user:pass` vendor lines. |
| `class Egress` | 229 | One identity: `url` (None = direct), `label`, `strikes`, `fetched`, `blocked_until`, lazy `.api`. |
| `class Pool` | 258 | `acquire()` leases the least-used free identity exclusively (returns None when all benched), `release`, `bench(e)` (cooldown, strikes reset), `all_benched`, `recovers_in`. |
| `fetch_kome` | 317 | Route 4. POST, 4 attempts; `<500 && !=429` → `LookupError`; exhausted → `TransientError`; `hasMore` (truncated) → `LookupError`. Returns text segmented by `atu.segment_plain_text`. **Language is `"en"` by assumption**: the response carries only `transcript`, `length`, `hasMore` — no track name — and the request asks for none. The module docstring (route 4) and a comment at the return say so; no per-record marker, so the file schema is unchanged. |
| `supadata_key` | 375 | Reads `SUPADATA_API_KEY` from the environment. |
| `_supadata_get` | 391 | GET with retries. 429 → backoff (honours `Retry-After`, capped `MAX_RETRY_AFTER=60`), then `RateLimited`; 401/402 → `AccountError` and sets module global `_supadata_off` (route retired for the process); other 4xx → `LookupError`; HTML at 200 → `TransientError`; 5xx/URLError/timeout ×4 → `TransientError`. |
| `_supadata_once` | 461 | One credit. `mode=native`, `lang=<want>`. 202 → poll `/{jobId}` every 6 s, 15-min deadline → `TransientError`; `status: failed` → `LookupError`. String `content` or 206 → `LookupError` ("no timed transcript"). ms → s. Returns `(segments, lang, availableLangs)`. |
| `fetch_supadata` | 512 | Asks for `en`; if the answer is off `LANGUAGES` **and** `availableLangs` offers an on-list one, re-requests once (second credit). Off-list-only → returned as is, never raised. |
| `ytdlp_binary` | 551 | `yt-dlp` beside the running interpreter (venv) else `PATH`. |
| `parse_json3` | 556 | YouTube json3 → segments; drops `aAppend` rollup events (otherwise text is duplicated). |
| `YTDLP_NETWORK_RE`, `fetch_ytdlp` | 580-635 | Route 2. `--sub-langs YTDLP_SUB_LANGS --sub-format json3`, 300 s timeout → `TransientError`. No file: stderr with `429`/`Too Many Requests`/`not a bot` → `BlockedError`; network-looking → `TransientError`; else `LookupError`. Best file by `LANGUAGES` rank. |
| `build_api`, `pick_and_fetch` | 638-694 | Route 1. Manual track on `LANGUAGES` > generated on `LANGUAGES` > any translatable track translated to `en` (falls back untranslated on failure) > first track. Reports the language of the text actually fetched. No tracks → `LookupError`. |
| `_route_yta/_route_ytdlp/_route_supadata/_route_kome` | 697-722 | Uniform `(segments, lang, generated, timing)`; kome is the only `"estimated"`. |
| `uses_our_ip(source)` | 725 | True for `auto/exact/youtube/ytdlp`. |
| `off_ip_sources(source, key)` | 734 | Is any route left that does not spend our IP (kome under auto/kome; supadata if key and not retired). |
| `fetch_one(eg, vid, source, key)` | 741 | **The ladder.** See below. |
| `load_misses`, `save` | 801-846 | `save` writes the file, filed under its real language; prints a note when off-list. |
| `select(talks, args, misses)` | 849 | What a run works on. See below. |
| `BLOCK_ADVICE`, `ACCOUNT_ADVICE`, `stop_advice` | 872-892 | Printed once when a round has nothing left to fetch with. |
| `attempt(pool, t, args, key)` | 895 | One talk: lease → pace (`--min-delay`..`--max-delay`) → `fetch_one` → on block, bench and retry on the next identity (budget `min(len(pool)+1, 8)`; 1 and no lease for off-IP-only sources) → `save`. `eg.fetched` counts only `yt`/`ytdlp` successes. |
| `probe` | 939 | One talk per identity through the *exact* routes only (never kome, so a spent IP cannot read as usable), plus one Supadata call if a key is present (1 credit). Exit 1 if nothing works. |
| `build_pool` | 980 | `--proxy` + `--proxy-file` lines, deduped. Direct IP is included only when there are no proxies or `--with-direct`. |
| `main` | 1001 | CLI, round loop, `--retry-after` parking. |
| `spent(pool, args, key)` | 1111 | "Nothing left to fetch with": all identities benched and no off-IP route; for off-IP-only sources, just "no off-IP route". |
| `run_parallel`, `run_serial` | 1123-1206 | Thread pool / serial round. Write misses only via `about_the_video`. |

### `tools/atu.py` — what the fetcher borrows

`TRANSCRIPTS` (`:20`), `WATCH` (`:29`), `is_youtube_id` (`:120`, filters out
InfoQ ids), `segment_plain_text` (`:138`, untimed prose → 25-word estimated
segments; shared with `infoq.py`), `add_year_args`/`year_wanted` (`:723-748`),
`load_talks` (`:751`), `transcript_path` (`:770`), `write_json` (`:782`).

### The route ladder (`fetch_one`, `:741-798`)

| # | Name in log | Supplier | Egress | Timing | Cost | Allowed under `--source` |
|---|---|---|---|---|---|---|
| 1 | `yt` | `youtube-transcript-api` | ours (leased `Egress`) | exact | free | `auto exact youtube` |
| 2 | `ytdlp` | `yt-dlp` subprocess, different Innertube client | ours (same lease, `--proxy` passed through) | exact | free | `auto exact ytdlp` |
| 3 | `supa` | supadata.ai `mode=native` | theirs | exact | 1 credit (2 on a language re-request) | `auto exact supadata`, needs key, not retired |
| 4 | `kome` | kome.ai (names no caption track; `language` assumed `en`) | theirs | **estimated** | free | `auto kome` only — never `exact` |

Rules the code enforces:

- Routes run in order; a non-block failure moves to the next. Route 1 is
  dropped for an identity after 3 consecutive failures under `auto`
  (`eg.strikes`); a success resets the count.
- A block on route 1 **skips route 2** (same IP, same allowance) but still
  tries 3 and 4. If nothing off-IP is configured the block is re-raised so
  `attempt()` can bench the identity.
- If an off-IP route gives a verdict after our IP was blocked, the verdict
  wins (e.g. Supadata "no captions" is a miss) but the block rides along as
  `e.egress_blocked` so the identity is still benched.
- A block never turns into a kome estimate under `--source exact`. An
  unfetched talk is recoverable; a mislabelled one is not.
- With a single-route plan (`--source supadata`, `--source kome`, ...) the
  exception propagates unchanged.
- Under `auto`, a Supadata `AccountError` falls through to kome (estimated).
  Under `exact` it propagates and ends the round. The module docstring's
  route 3 entry states this; check #11 in the route-planning tests pins it.

### Four kinds of failure (`about_the_video`, `:193`)

| Class | Means | Benches an identity? | Ends the round? | Written to `_misses.json`? |
|---|---|---|---|---|
| `BlockedError` / `IpBlocked` / `TooManyRequests` / `RequestBlocked` — YouTube 429 or "Sign in to confirm you're not a bot", incl. yt-dlp stderr | Verdict on **our IP** | yes, `--proxy-cooldown` min (default 45) | only when `spent()` | **never** |
| `AccountError` — Supadata 401 (bad key) / 402 (no credits) | Verdict on **our account** | no | retires the route; ends round if nothing else off-IP | **never** |
| `TransientError` (incl. `RateLimited`) — 5xx ×4, timeouts, DNS/proxy death, HTML-at-200, stalled job (15 min), Supadata 429 that outlasts backoff | No verdict | no | no; printed as `LEFT`, picked up by a rerun | **never** |
| `LookupError` and anything else — no tracks, empty track, 206, 404, members-only 403, `job failed`, kome `hasMore`, yt-dlp "no subtitles for the requested languages" | Verdict on **the video** | no | no | **yes** (`MISS` in log) |

Log line vocabulary: `ok`, `MISS`, `LEFT` (transient/account in parallel),
`BLOCKED`/`REFUSED`/`LEFT` (serial), plus the once-per-round `BLOCK_ADVICE` or
`ACCOUNT_ADVICE` block.

### The egress pool

- What YouTube meters is an allowance **per egress IP** that refills over
  hours (~20-52 talks a sitting on residential, 22 on mobile; slowing down
  does not raise it). The pool exists so no two workers spend one IP at once.
- Identities: the direct connection (None) and each `--proxy` / `--proxy-file`
  line (`host:port:user:pass` accepted). With proxies configured the direct IP
  is left out unless `--with-direct`. There is no VPN/rotation logic; a proxy
  URL is passed to `GenericProxyConfig` (route 1) and `yt-dlp --proxy` (route 2).
- A block benches only that identity; `attempt()` retries the talk on another
  one immediately rather than deferring it to the next round.
- Default `--workers`: `max(2, min(len(pool), 8))` when the source can use our
  IP; `OFF_IP_WORKERS = 8` when it cannot. Raising `--workers` past the pool
  size only queues — except for `--source supadata`/`kome`, where no lease is
  taken, no pacing sleep applies, and `--workers 32` is real parallelism
  (measured ~250 talks/min vs ~3/min under `exact`).
- No proxy pool has ever been bought for this corpus; Supadata is the lever
  in use (`STATE.md` §"The quota").

### What a run selects (`select`, `:849-869`)

All talks with a YouTube id (InfoQ-only skipped), narrowed by `-c/--conference`
(repeatable), `--priority N` (registry priority ≤ N), `--min-duration MIN`,
`--year YYYY` (repeatable) or `--min-year YYYY` (mutually exclusive; unknown
year excluded unless `--include-unknown-year`); minus any talk whose file
exists or whose id is in `_misses.json`. Sorted by `(priority, -duration_s)`:
priority-1 conferences first, longest talks first. `--limit N` truncates
after sorting and caps the run at one round. Nothing is stored between runs.

### CLI flags (`main`, `:1001-1071`)

| Flag | Default | Note |
|---|---|---|
| `--source {auto,exact,youtube,ytdlp,supadata,kome}` | `auto` | `exact` never estimates; `supadata` requires `SUPADATA_API_KEY`. |
| `-c/--conference`, `--priority`, `--min-duration`, `--year`, `--min-year`, `--include-unknown-year`, `--limit` | — | Selection. |
| `--workers N` | `max(2, min(pool, 8))` on our-IP sources; `OFF_IP_WORKERS = 8` under `--source supadata`/`kome` | The `--help` text states both defaults. |
| `--retry-misses` | off | Loads `{}` instead of `_misses.json`, so every miss is re-attempted. |
| `--probe` | off | One fetch per identity (+1 Supadata credit); exit 1 if nothing works. |
| `--proxy URL` (repeatable), `--proxy-file PATH`, `--proxy-cooldown MIN` (45), `--with-direct` | — | Pool. |
| `--min-delay` / `--max-delay` | 3 / 7 s | Per-request pacing on our-IP routes only. |
| `--retry-after MIN` | 0 | When every identity is blocked: sleep `max(this, pool.recovers_in())` and run another round. 0 = stop. Ignored with `--limit`. |
| `--max-rounds` | 24 | Cap on blocked rounds. |

Each round re-runs `select()` from disk, so an interrupted or blocked run is
resumed by repeating the command. `_misses.json` is rewritten after every
round and at exit. On success the script prints the follow-up:
`python3 sync_catalog.py && python3 build_index.py`.

### Transcript file format — `data/transcripts/<video_id>.json`

Written compact by `save()` (`:808`):

| Field | Type | Meaning |
|---|---|---|
| `video_id` | str | YouTube id, also the filename. 48 ids begin with `_`; count by exact id, never by prefix. |
| `title`, `conference` | str | Copied from the talk record at fetch time (may drift from `talks.json` later). |
| `language` | str | The language of the text actually saved, as the route named it (`en`, `en-US`, `hi`, ... or `"und"`). Never guessed — with one exception: a `source: "kome"` record says `en` because kome names no track, not because one was read (module docstring, route 4). No such file exists in the corpus today. |
| `auto_generated` | bool | False only for a manual track via route 1; every other route reports True. |
| `source` | `yt` / `ytdlp` / `supa` / `kome` / `infoq` | Route provenance. |
| `timing` | `exact` / `estimated` | `estimated` = starts interpolated from word position (kome, infoq). Downstream deep links trust this field. |
| `word_count` | int | Sum of whitespace-split words over segments. |
| `segments` | list of `{start: float s, duration: float s, text: str}` | Rounded to 2 dp; duration floored at 0.5 s on the yt-dlp and Supadata paths; whitespace squashed. |
| `imported_from` | str, optional | Present only on files brought in by `import_kb.py`. |

### `tools/test_fetch_transcripts.py` — what it exists to catch

Runs `fetch_transcripts` against a faked `urllib.request.urlopen`, faked
`subprocess.run`, faked youtube-transcript-api listings and fake `Pool`
allowances, with `time.sleep` stubbed. It also imports `enrich.py` to check
`BLOCK_MARKERS`. Sections, in file order (`grep -n '^print("\\n--'`):

- proxy parsing/redaction; pool leasing (exclusive, least-used first, bench
  expiry actually elapses in real time for one check).
- `select()` year filter semantics and the priority/duration sort; InfoQ ids excluded.
- `fetch_one` route planning: auto stops at `yt`; block skips `ytdlp` but
  reaches `supa`/`kome`; `exact` re-raises a block and **never** returns kome;
  3 strikes drop route 1; a verdict after a block wins but carries the block;
  a Supadata `AccountError` reaches kome under `auto` and propagates (not a
  block, not a miss) under `exact`.
- Supadata response shapes: 200 short, 202 job polling, `failed` job, 206,
  string content, 401/402 (`AccountError`, retires route, not a miss, not a
  block), 5xx retried, 429 backoff + `Retry-After` + `RateLimited`, 404 per-video.
- yt-dlp and kome: timeouts, DNS, dead proxy, outages are `TransientError`;
  bot wall is a block; private/no-file is a video verdict; a kome success
  reports the assumed `en`, pinned so a change there is deliberate.
- Language handling: tag folding, `und`, Supadata asks-then-checks and
  re-requests at most once, `pick_and_fetch` reports the fetched language,
  `save()` keeps a foreign-only track and says so.
- Full rounds against fake allowances: a pool multiplies yield, blocks are
  never misses, one dead IP does not stop the run, Supadata carries a round
  past a spent pool, credits running out mid-flight loses no talk, off-IP
  sources lease nothing.

Any change to a failure class, to `about_the_video`, to route ordering or to
`save()` should add a check here; the suite is the executable form of the
invariants above.

### `logs/`

Gitignored, hand-redirected output from local runs (`fetch-2026.log`,
`fetch-2026b.log` are the 2026-08-31 `--source supadata --min-year 2026` runs;
`build.log`, `sync.log`, `uitest*.log` are the follow-ups). Useful only as a
record of what a run printed; nothing in the code reads or writes them.

## How

Standard extraction (from `STATE.md` handoff; ~5 min for a few hundred talks):

```bash
cd ~/git/ai-talks-universe/tools
source ~/.bash_profile        # exports SUPADATA_API_KEY and YOUTUBE_API_KEY; a
                              # non-login/tool shell does not read it and the run
                              # silently degrades to the free routes
.venv/bin/python fetch_transcripts.py --probe                       # 1 credit
.venv/bin/python fetch_transcripts.py --source supadata --min-year 2026 --workers 32 \
  && .venv/bin/python sync_catalog.py \
  && .venv/bin/python build_index.py
```

Then, before committing `data/`, `talks/` and the counts in `README.md`/`STATE.md`:

```bash
python3 -c "import json; [print(v['detail']) for v in json.load(open('../data/transcripts/_misses.json')).values()]"
python3 test_fetch_transcripts.py
cd uitest && node run.js && cd ..
```

Rules a model gets wrong without being told:

- **Use `tools/.venv/bin/python`, not `python3`.** The deps and the `yt-dlp`
  binary live in the venv; `ytdlp_binary()` looks beside the interpreter first.
- **`--probe` first, then name the route.** If the probe says the IP is
  spent, run `--source supadata --workers 32`; `--source exact` would pay a
  refused API call plus a yt-dlp subprocess per talk while holding the lease.
  `--source exact` is right only when the probe says a free route works and
  you would rather spend a sitting (~25-50 talks) than credits.
- **Chain `sync_catalog.py && build_index.py` onto the fetch.** A transcript
  not folded in is invisible to every surface; this has cost 276 transcripts
  sitting unseen for 39 minutes. See `catalog-sync.md` for what they do.
- **Never write a network verdict into `_misses.json`.** New exceptions
  default to "miss" via `about_the_video()`, so a new failure path must raise
  (or subclass) `BlockedError`/`AccountError`/`TransientError` explicitly and
  get a test. After a big run read every `detail` — each should be "no
  captions" or a members-only 403.
- **Do not refetch the twelve `hi` talks.** Their only track is YouTube ASR
  misreading English as Hindi (`availableLangs: ['hi']`); every route returns
  the same bytes. Likewise, a rerun never upgrades `estimated` → `exact`;
  delete the file first if that is the intent.
- **Do not run `enrich.py`'s yt-dlp route and a free-route transcript run
  together** — same per-IP allowance (`STATE.md` §"The quota"). Prefer the
  Data API for metadata.
- **Do not add the fetcher to CI or the weekly workflow.** GitHub's ranges
  are blocked outright, and `--source supadata` from a schedule would spend
  credits unattended.
- **Corporate/VPN egress lies to the probe.** Zscaler returned `BLOCKED —
  spent` for an IP that fetched 15,871 words minutes later with the proxy
  stopped; a datacenter range is also blocked hardest. Drop it before
  trusting a block verdict or the quota table.
- **Known hole, documented not fixed** (`HISTORY.md:562`): route 2 limits
  `--sub-langs` to `LANGUAGES`, so on an our-IP run a video whose only track
  is off-list is recorded as a miss ("no subtitles for the requested
  languages") — violating the "foreign-only captions are never a miss"
  invariant that routes 1 and 3 honour. `--retry-misses` with
  `--source supadata` is the way back for such entries.
- **Credits ≈ talks.** Supadata charges nothing for a captionless video
  (206), so a budget needs no headroom beyond the selection count. Pro plan is
  3,000 credits/month; `STATE.md` tracks the month's spend.
- Docs vs code: `ARCHITECTURE.md`'s selection list omits `--min-duration`,
  which `select()` also honours. The code wins.
