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


def year_of(v: dict) -> int | None:
    if v.get("year"):
        return int(v["year"])
    if v.get("published_at"):
        m = YEAR_RE.search(v["published_at"])
        if m:
            return int(m.group(1))
    for field in (v.get("label"), v.get("title")):
        m = YEAR_RE.search(field or "")
        if m:
            return int(m.group(1))
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


def decimal_size(n: float) -> str:
    """The same count in decimal units, for comparing against a vendor figure."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1000 or unit == "GB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1000.0
    return f"{n:.1f}GB"
