"""Shared helpers for the AI talks universe knowledge base.

Paths resolve relative to the repository root, so the tools can be run from
anywhere.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TALKS_MD = ROOT / "talks"
CATALOG = DATA / "catalog"
TRANSCRIPTS = DATA / "transcripts"
TINDEX = DATA / "tindex"

REGISTRY = ROOT / "conferences.json"
TALKS_JSON = DATA / "talks.json"
TALKS_CSV = DATA / "talks.csv"
SEARCH_META = DATA / "search-meta.json"
TALKS_DB = DATA / "talks.db"

WATCH = "https://www.youtube.com/watch?v={vid}"


def load_registry() -> dict:
    if not REGISTRY.exists():
        raise SystemExit(f"{REGISTRY} not found")
    with REGISTRY.open(encoding="utf-8") as f:
        reg = json.load(f)
    seen = set()
    for c in reg["conferences"]:
        if c["slug"] in seen:
            raise SystemExit(f"duplicate conference slug in the registry: {c['slug']}")
        seen.add(c["slug"])
    return reg


STOPWORDS = set(
    """a about above after again against all am an and any are aren as at be because been
before being below between both but by can cannot could couldn did didn do does doesn doing
don down during each few for from further had hadn has hasn have haven having he her here
hers herself him himself his how i if in into is isn it its itself just me more most mustn my
myself no nor not now of off on once only or other ought our ours ourselves out over own re
s same shan she should shouldn so some such t than that the their theirs them themselves then
there these they this those through to too under until up ve very was wasn we were weren what
when where which while who whom why will with won would wouldn you your yours yourself
yourselves ll m d o y ain aren couldn didn doesn hadn hasn haven isn ma mightn mustn needn
shan shouldn wasn weren won wouldn also get got going like make makes really thing things way
ways lot lots kind sort going gonna yeah okay ok right well actually basically just even
""".split()
)


def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text or "")
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text or "untitled"


VIDEO_ID_RE = re.compile(r"(?:v=|youtu\.be/|/embed/|/live/|/shorts/)([A-Za-z0-9_-]{11})")


def video_id(url: str | None) -> str | None:
    if not url:
        return None
    m = VIDEO_ID_RE.search(url)
    return m.group(1) if m else None


# A YouTube id is exactly 11 characters of the URL-safe alphabet. Records that
# come from a source with its own identifiers — InfoQ's presentation pages —
# are keyed by a prefixed slug instead, and anything that builds a youtube.com
# link has to ask first.
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

# Reserved: no YouTube id is ever read as one of ours, and none of ours is ever
# read as a YouTube id. The check below is not redundant with the length rule,
# because a short InfoQ slug lands on exactly 11 characters and in the URL-safe
# alphabet: "iq-rag-vllm" and "iq-green-it" both did, and both were handed a
# youtube.com/watch?v=iq-rag-vllm that leads nowhere.
INFOQ_ID_PREFIX = "iq-"


def is_youtube_id(vid: str | None) -> bool:
    if not vid or vid.startswith(INFOQ_ID_PREFIX):
        return False
    return bool(YOUTUBE_ID_RE.match(vid))


def watch_url(vid: str | None, page_url: str | None = None) -> str | None:
    """The canonical link for a record: the video where there is one.

    A YouTube id gives a watch URL; anything else has to carry its own page,
    and a record with neither has no link at all rather than a link to
    youtube.com/watch?v=iq-something.
    """
    if is_youtube_id(vid):
        return WATCH.format(vid=vid)
    return page_url or None


def segment_plain_text(lines, total_seconds: float, chunk_words: int = 25) -> list[dict]:
    """Untimed transcript prose into segments, starts interpolated by word position.

    Two routes produce text with no timings — kome.ai's caption dump and
    InfoQ's hand-edited transcripts — and both need the same thing: segments
    shaped like the exact-timing ones, so that every reader downstream (the
    markdown deep links, query.py's moments, the browser index) works on them
    unchanged. Position within the runtime is the only signal available, which
    is good enough to jump near a quote and not frame accurate; callers mark
    the result timing="estimated" so nothing presents it as more than that.

    With no runtime to scale onto, starts fall back to the word offset itself:
    monotonic and orderable, which is what the readers actually require.
    """
    lines = [" ".join(str(l).split()) for l in lines if str(l).strip()]
    if not lines:
        return []
    counts = [len(l.split()) for l in lines]
    n_words = sum(counts) or 1

    chunks, buf, buf_words, seen, start_words = [], [], 0, 0, 0
    for line, c in zip(lines, counts):
        if not buf:
            start_words = seen
        buf.append(line)
        buf_words += c
        seen += c
        if buf_words >= chunk_words:
            chunks.append((start_words, " ".join(buf)))
            buf, buf_words = [], 0
    if buf:
        chunks.append((start_words, " ".join(buf)))

    out = []
    for i, (sw, text) in enumerate(chunks):
        start = (sw / n_words) * total_seconds if total_seconds else float(sw)
        nxt = chunks[i + 1][0] if i + 1 < len(chunks) else n_words
        end = (nxt / n_words) * total_seconds if total_seconds else float(nxt)
        out.append({"start": round(start, 2),
                    "duration": round(max(end - start, 0.5), 2),
                    "text": text})
    return out


TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9+#.\-]*")


def tokenize(text: str) -> list[str]:
    """Lowercase word tokens, stopwords dropped, short junk dropped.

    Keeps things like `c++`, `gpt-4`, `.net` reasonably intact.
    """
    out = []
    for t in TOKEN_RE.findall((text or "").lower()):
        t = t.strip(".-")
        if len(t) < 2 or t in STOPWORDS:
            continue
        out.append(t)
        # Also index the parts of a compound, so "spec driven" finds
        # "spec-driven" and "ai assisted" finds "ai-assisted".
        if "-" in t or "." in t:
            for part in re.split(r"[.\-]+", t):
                if len(part) >= 2 and part not in STOPWORDS and part != t:
                    out.append(part)
    return out


# --- what counts as an AI talk -----------------------------------------------
#
# Conferences whose whole programme is AI carry `"scope": "all"` in the registry
# and skip this entirely. General conferences (NDC, GOTO, KubeCon, re:Invent…)
# carry `"scope": "ai"`, and only the sessions matching this survive — otherwise
# an "AI talks" corpus would be four fifths Kubernetes networking and iOS layout.
#
# Matching is on word boundaries, never substrings: "ai" must not fire on
# "email" or "chair", and "ml" must not fire on "html".
AI_TERMS = [
    r"a\.?i\.?", r"artificial intelligence", r"machine learning", r"deep learning",
    r"ml", r"mlops", r"llm(s)?", r"slm(s)?", r"gpt(-?\d\w*)?", r"gen-?ai",
    r"generative", r"foundation model(s)?", r"frontier model(s)?", r"multimodal",
    r"agent(s|ic)?", r"copilot(s)?", r"chatgpt", r"claude", r"gemini", r"llama",
    r"mistral", r"deepseek", r"qwen", r"grok", r"openai", r"anthropic",
    r"hugging ?face", r"transformer(s)?", r"diffusion", r"neural", r"embedding(s)?",
    r"vector (db|database|search|store)", r"rag", r"retrieval[- ]augmented",
    r"prompt(ing|s)?", r"fine[- ]?tun\w*", r"inference", r"tokeni[sz]\w*",
    r"langchain", r"langgraph", r"llamaindex", r"vllm", r"ollama", r"pytorch",
    r"tensorflow", r"cuda", r"gpu(s)?", r"mcp", r"model context protocol",
    r"vibe coding", r"nlp", r"computer vision", r"chatbot(s)?", r"assistant(s)?",
    r"reasoning model(s)?", r"evals?", r"hallucinat\w*", r"guardrail(s)?",
    r"alignment", r"red[- ]team\w*", r"context engineering", r"bedrock",
    r"agentforce", r"vertex ai", r"sagemaker", r"data science", r"recommender",
]
# The trailing boundary allows a hyphen — "AI-native", "AI-assisted" and
# "ML-powered" are the house style of half these programmes — while the leading
# one does not, so "chai-latte" and "html-first" stay out.
AI_RE = re.compile(r"(?<![\w-])(?:" + "|".join(AI_TERMS) + r")(?!\w)", re.I)


def looks_ai(*texts: str | None) -> bool:
    return any(AI_RE.search(t) for t in texts if t)


# Enumeration is flat and carries no publish date, so until a video is enriched
# its year is only knowable from the edition it was listed under or from its own
# title. sync_catalog stamps the result into the corpus; both metered stages
# select on it, which is why this lives here and not in one of them.
YEAR_RE = re.compile(r"(?<!\d)(20[12]\d)(?!\d)")

# A year that opens a span — "Production ML across 2015-2035", "2019–2024" — is
# the subject of the talk, not the edition that recorded it. The first match in
# free text is otherwise the answer, which filed a PyCon DE & PyData 2026 talk
# under 2015 and left it as the corpus's only 2015 record. Only the opening year
# is skipped: the closing one is still a year the text states, so "GOTO
# 2024-2025" resolves to 2025 rather than to nothing.
YEAR_SPAN_RE = re.compile(r"(?<!\d)20[12]\d\s*[-–—]\s*(?=\d{4}(?!\d))")


def year_in_text(text: str | None) -> int | None:
    if not text:
        return None
    spans = {m.start() for m in YEAR_SPAN_RE.finditer(text)}
    for m in YEAR_RE.finditer(text):
        if m.start() not in spans:
            return int(m.group(1))
    return None


def year_of(v: dict) -> int | None:
    if v.get("year"):
        return int(v["year"])
    if v.get("published_at"):
        m = YEAR_RE.search(v["published_at"])
        if m:
            return int(m.group(1))
    for field in (v.get("label"), v.get("title")):
        y = year_in_text(field)
        if y:
            return y
    return None


def add_year_args(ap: argparse.ArgumentParser) -> None:
    """The year filter, defined once so the two metered stages cannot drift.

    Enumeration is free and the corpus keeps everything; what is scarce is the
    per-IP allowance the other two stages spend, and on AI topics a 2023 talk is
    rarely worth a unit of it.
    """
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--year", action="append", type=int, metavar="YYYY",
                   help="only talks from this year; repeatable")
    g.add_argument("--min-year", type=int, metavar="YYYY",
                   help="only talks from this year onwards")
    ap.add_argument("--include-unknown-year", action="store_true",
                    help="also take talks whose year is still unknown — which is "
                         "what enrichment resolves, so a run that excludes them "
                         "can never discover one")


def year_wanted(year: int | None, args) -> bool:
    if year is None:
        return not (args.year or args.min_year) or args.include_unknown_year
    if args.year:
        return year in args.year
    if args.min_year:
        return year >= args.min_year
    return True


def load_talks() -> list[dict]:
    if not TALKS_JSON.exists():
        raise SystemExit(f"{TALKS_JSON} not found — run sync_catalog.py first")
    with TALKS_JSON.open(encoding="utf-8") as f:
        return json.load(f)["talks"]


def catalog_path(slug: str) -> pathlib.Path:
    return CATALOG / f"{slug}.json"


def load_catalog(slug: str) -> dict:
    p = catalog_path(slug)
    if not p.exists():
        return {"slug": slug, "videos": {}}
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def transcript_path(vid: str) -> pathlib.Path:
    return TRANSCRIPTS / f"{vid}.json"


def load_transcript(vid: str) -> dict | None:
    p = transcript_path(vid)
    if not p.exists():
        return None
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def write_json(path: pathlib.Path, obj, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=False)
            f.write("\n")


def human_size(n: float) -> str:
    """A byte count in binary units, labelled in binary units.

    This divides by 1024, so what it produces are kibibytes, mebibytes and
    gibibytes — and it now says so. It spent a long time dividing by 1024 while
    printing "KB"/"MB"/"GB", which made every size this repo has ever reported
    look decimal when it was not. That is not pedantry: `search-meta.json` sits
    at 6,045,370 bytes, which is *under* the 6 MiB rebuild trigger in
    build_index.py and *over* 6 MB decimal, so the label alone decided whether
    the description clip needed halving. Use decimal_size() if you ever want
    the other convention; do not change the divisor here.
    """
    for unit in ("B", "KiB", "MiB", "GiB"):
        if n < 1024 or unit == "GiB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024.0
    return f"{n:.1f}GiB"


# Bumped whenever build_index.py changes what talks.db holds — a column, a
# table, the passage shape. Written into the file as PRAGMA user_version, so a
# database built by an older script is recognised as stale rather than opened
# and queried: the day `url` was added to `talks`, every search died with
# "no such column: url" until someone knew to delete the file by hand.
DB_SCHEMA_VERSION = 5


def db_stale() -> str | None:
    """Why talks.db must be rebuilt before it is queried, or None if it is fine.

    Three reasons, each of which has actually happened: the file is missing
    (it is derived and gitignored); it was built by a script with a different
    schema; or the corpus changed under it — talks.json was re-derived, or a
    transcript was fetched into data/transcripts/ (a new file updates the
    directory's mtime) — so a query would silently miss the last refresh.
    """
    import sqlite3

    if not TALKS_DB.exists():
        return "no index yet"
    try:
        con = sqlite3.connect(f"file:{TALKS_DB}?mode=ro", uri=True)
        try:
            version = con.execute("PRAGMA user_version").fetchone()[0]
        finally:
            con.close()
    except sqlite3.Error as e:
        return f"index unreadable ({e})"
    if version != DB_SCHEMA_VERSION:
        return f"index schema v{version}, tools expect v{DB_SCHEMA_VERSION}"
    built = TALKS_DB.stat().st_mtime
    for src, what in ((TALKS_JSON, "talks.json"), (TRANSCRIPTS, "data/transcripts/")):
        if src.exists() and src.stat().st_mtime > built:
            return f"{what} is newer than the index"
    return None


def connect():
    """A read-only connection to talks.db, rebuilding it first if it is stale.

    Shared by query.py and excerpt.py so the two cannot drift on what "stale"
    means. The rebuild takes about half a minute and says so on stderr, where
    it cannot corrupt --json output.
    """
    import sqlite3
    import sys

    why = db_stale()
    if why:
        print(f"rebuilding the search index ({why}) — about 30 s…", file=sys.stderr)
        import build_index

        build_index.main(["--quiet"])
    return sqlite3.connect(f"file:{TALKS_DB}?mode=ro", uri=True)


def decimal_size(n: float) -> str:
    """The same count in decimal units, for comparing against a vendor figure."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1000 or unit == "GB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1000.0
    return f"{n:.1f}GB"
