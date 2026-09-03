"""Shared helpers for the AI talks universe knowledge base.

Paths resolve relative to the repository root, so the tools can be run from
anywhere.
"""

from __future__ import annotations

import argparse
import functools
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


# Query-time synonym groups, shared by the two rankers so they keep agreeing:
# query.py expands a bare word into an OR over its group (one gate term per
# group), and index.html does the same from the copy build_index.py writes into
# tindex/_manifest.json. Membership is tested by stem, so "databases" belongs to
# the `db` group. Kept short and weak on purpose: the ranking-agreement suite
# compares the two rankers, and every group here widens both the same way.
SYNONYMS: tuple[tuple[str, ...], ...] = (
    ("llm", "llms", "language model", "language models"),
    ("rag", "retrieval augmented generation", "retrieval-augmented generation"),
    ("mcp", "model context protocol"),
    ("k8s", "kubernetes"),
    ("genai", "generative ai"),
    ("eval", "evals", "evaluation", "evaluations"),
    ("db", "database", "databases"),
    ("ml", "machine learning"),
    ("fine-tuning", "finetuning", "fine tuning"),
    ("vector db", "vector database", "vector store"),
    ("cot", "chain of thought", "chain-of-thought"),
    ("rl", "reinforcement learning"),
    ("rlhf", "reinforcement learning from human feedback"),
    ("sre", "site reliability"),
    ("ci", "continuous integration"),
    ("infra", "infrastructure"),
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


# --- stemming -------------------------------------------------------------------
#
# talks.db tokenises with FTS5's `porter unicode61`, so query.py finds
# "evaluation" for "evaluate". The browser index had no stemmer, so index.html
# did not — and its prefix rule fired only when the exact key was absent, and
# then took an arbitrary first twelve keys of the shard. This is Porter's 1980
# algorithm, step for step; index.html carries the same function in JavaScript
# and test_stem.py checks the two agree on every word in the corpus, because
# the failure would be silent: a shard keyed on one spelling of a stem and a
# query asking for the other simply match nothing.
#
# Only [a-z]* words are stemmed. tokenize() emits tokens that may carry digits,
# `+`, `#`, `.` or `-` ("gpt-4", "c++", ".net"), and those pass through
# untouched: Porter is defined on English words, and a stem of "c++" is "c++".

_VOWELS = set("aeiou")


def _is_consonant(w: str, i: int) -> bool:
    c = w[i]
    if c in _VOWELS:
        return False
    if c == "y":
        return i == 0 or not _is_consonant(w, i - 1)
    return True


def _measure(stem: str) -> int:
    """The m of Porter's [C](VC){m}[V]: how many VC sequences the stem has."""
    m = 0
    i = 0
    n = len(stem)
    while i < n and _is_consonant(stem, i):
        i += 1
    while i < n:
        while i < n and not _is_consonant(stem, i):
            i += 1
        if i >= n:
            break
        m += 1
        while i < n and _is_consonant(stem, i):
            i += 1
    return m


def _has_vowel(stem: str) -> bool:
    return any(not _is_consonant(stem, i) for i in range(len(stem)))


def _ends_double_consonant(w: str) -> bool:
    return len(w) >= 2 and w[-1] == w[-2] and _is_consonant(w, len(w) - 1)


def _ends_cvc(w: str) -> bool:
    """…consonant-vowel-consonant, the last not w, x or y."""
    if len(w) < 3:
        return False
    if not (_is_consonant(w, len(w) - 1) and not _is_consonant(w, len(w) - 2)
            and _is_consonant(w, len(w) - 3)):
        return False
    return w[-1] not in "wxy"


def _replace(w: str, suffix: str, repl: str, min_m: int = 0) -> str | None:
    """w with suffix swapped for repl, if the stem before it has m > min_m - 1."""
    if not w.endswith(suffix):
        return None
    stem = w[:len(w) - len(suffix)]
    if _measure(stem) >= min_m:
        return stem + repl
    return w


_STEP2 = (("ational", "ate"), ("tional", "tion"), ("enci", "ence"), ("anci", "ance"),
          ("izer", "ize"), ("bli", "ble"), ("alli", "al"), ("entli", "ent"), ("eli", "e"),
          ("ousli", "ous"), ("ization", "ize"), ("ation", "ate"), ("ator", "ate"),
          ("alism", "al"), ("iveness", "ive"), ("fulness", "ful"), ("ousness", "ous"),
          ("aliti", "al"), ("iviti", "ive"), ("biliti", "ble"), ("logi", "log"))
_STEP3 = (("icate", "ic"), ("ative", ""), ("alize", "al"), ("iciti", "ic"), ("ical", "ic"),
          ("ful", ""), ("ness", ""))
_STEP4 = ("al", "ance", "ence", "er", "ic", "able", "ible", "ant", "ement", "ment", "ent",
          "ion", "ou", "ism", "ate", "iti", "ous", "ive", "ize")


@functools.lru_cache(maxsize=None)
def stem(word: str) -> str:
    """Porter-stem one lowercase English word; anything else is returned as is.

    Memoised: the corpus has ~30 million transcript tokens and ~100 thousand
    distinct ones, and stemming each token afresh took the index build from
    48 s to nearly two minutes.
    """
    w = word
    if len(w) <= 2 or not w.isascii() or not w.isalpha():
        return w
    # Step 1a
    if w.endswith("sses"):
        w = w[:-2]
    elif w.endswith("ies"):
        w = w[:-2]
    elif w.endswith("ss"):
        pass
    elif w.endswith("s"):
        w = w[:-1]
    # Step 1b
    if w.endswith("eed"):
        if _measure(w[:-3]) > 0:
            w = w[:-1]
    else:
        stripped = None
        if w.endswith("ed") and _has_vowel(w[:-2]):
            stripped = w[:-2]
        elif w.endswith("ing") and _has_vowel(w[:-3]):
            stripped = w[:-3]
        if stripped is not None:
            w = stripped
            if w.endswith(("at", "bl", "iz")):
                w += "e"
            elif _ends_double_consonant(w) and w[-1] not in "lsz":
                w = w[:-1]
            elif _measure(w) == 1 and _ends_cvc(w):
                w += "e"
    # Step 1c
    if w.endswith("y") and _has_vowel(w[:-1]):
        w = w[:-1] + "i"
    # Step 2
    for suffix, repl in _STEP2:
        if w.endswith(suffix):
            if _measure(w[:-len(suffix)]) > 0:
                w = w[:-len(suffix)] + repl
            break
    # Step 3
    for suffix, repl in _STEP3:
        if w.endswith(suffix):
            if _measure(w[:-len(suffix)]) > 0:
                w = w[:-len(suffix)] + repl
            break
    # Step 4
    for suffix in _STEP4:
        if w.endswith(suffix):
            base = w[:-len(suffix)]
            if _measure(base) > 1 and (suffix != "ion" or (base and base[-1] in "st")):
                w = base
            break
    # Step 5a
    if w.endswith("e"):
        base = w[:-1]
        m = _measure(base)
        if m > 1 or (m == 1 and not _ends_cvc(base)):
            w = base
    # Step 5b
    if _measure(w) > 1 and _ends_double_consonant(w) and w.endswith("l"):
        w = w[:-1]
    return w


def stems(text: str) -> list[str]:
    """tokenize(), then stem each token — what the browser index is keyed on.

    A stem shorter than two characters is dropped ("ies" stems to "i"), so
    that every key has the two characters build_index.shard_key() reads.
    """
    out = []
    for t in tokenize(text):
        s = stem(t)
        if len(s) >= 2:
            out.append(s)
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


# --- topics --------------------------------------------------------------------
#
# The per-talk topic facet. `category` is a fact about the *conference* — every
# talk inherits one of five labels from the registry — so it cannot follow a
# subject inside a programme: AI Engineer alone spans agents, evals, RAG,
# inference and coding tools. These fifteen are multi-valued and derived per
# talk, by keyword rules over the title, the tags and the description, the way
# the AI-relevance test above is. Transcripts are left out on purpose: a third
# of talks have one, and a label that moved when a transcript arrived would make
# the facet drift with every fetch.
#
# Each topic is a list of phrases; the whole list is compiled into one regex
# with the boundaries AI_RE uses. Scoring (topic_scores): any phrase in the
# title scores TITLE_HIT; each *distinct* phrase in the tags or the description
# scores one; a topic is assigned at TOPIC_THRESHOLD. So a title mention is
# enough on its own, and the tags and description together have to say two
# different things about a topic before it counts — matching a description on
# any one word was measured too loose (three topics a talk, "image" and
# "customer" pulling in whatever said them once), and a tag was measured to be
# a channel's habit more often than a fact about the talk.
#
# Two boundaries are rules rather than accidents. "enterprise" alone never
# fires *Enterprise adoption* — on this corpus it is mostly a product tier —
# and a bare tool name (Copilot, Cursor) never fires *AI in the SDLC*, which is
# about the process (review, CI, the team), not the keyboard. "Copilot" alone
# is not a coding assistant either: half of Microsoft's are M365 or Studio.
TOPICS: list[tuple[str, list[str]]] = [
    ("Agents & orchestration", [
        r"agents?", r"agentic", r"multi-?agents?", r"tool[- ](?:calling|use)",
        r"function calling", r"mcp", r"model context protocol", r"a2a", r"agent2agent",
        r"(?:agent|ai|llm|workflow)s?[- ]orchestrat\w*", r"orchestrat\w+ (?:agents|llms)",
        r"autonomous (?:agents?|systems?|ai|workflows?)", r"langgraph", r"crewai", r"autogen",
        r"agent (?:frameworks?|sdks?|protocols?|memory|runtimes?)",
    ]),
    ("Coding assistants & agents", [
        r"github copilot", r"copilot (?:chat|workspace|cli|coding agent|agent mode|sdk)",
        r"copilot (?:for|in) (?:vs ?code|visual studio|jetbrains|xcode|github)",
        r"cursor", r"claude code", r"codex", r"windsurf", r"cline", r"aider",
        r"gemini cli", r"vibe[- ]cod\w*", r"coding (?:agents?|assistants?|tools?|copilots?)",
        r"code (?:generation|gen|completion|assistants?)", r"pair[- ]programm\w*",
        r"ai[- ](?:assisted|powered|augmented|driven|native) (?:coding|programming)",
        r"ai (?:coding|code)", r"code (?:with|using) (?:ai|llms?|agents?)",
    ]),
    ("AI in the SDLC & engineering orgs", [
        r"sdlc", r"software development life ?cycle", r"spec[- ]driven",
        r"code reviews?", r"pull requests?", r"prs", r"ci/?cd",
        r"continuous (?:integration|delivery|deployment)",
        r"developer (?:productivity|experience|velocity|workflows?)",
        r"engineering (?:teams?|orgs?|organi[sz]ations?|productivity|leaders?|leadership|"
        r"managers?|culture|practices?)",
        r"ai[- ]native (?:engineering|development|software|teams?|sdlc)",
        r"agentic (?:sdlc|engineering|software development|development)",
        r"ai[- ](?:assisted|driven|powered|augmented|native) (?:development|engineering|"
        r"software (?:development|engineering))",
        r"legacy (?:code|systems?|modernization|migration)",
        r"(?:code|application|app) (?:migration|modernization|modernisation)",
        r"test(?:ing)? (?:generation|automation)", r"unit tests?", r"technical debt",
        r"10x (?:developers?|engineers?)", r"software teams?",
    ]),
    ("RAG, retrieval & knowledge", [
        r"rag", r"retrieval[- ]augmented(?: generation)?", r"retrieval",
        r"vector (?:db|database|search|store|index|embeddings?)",
        r"embeddings?", r"semantic search", r"hybrid search", r"knowledge (?:graphs?|bases?)",
        r"graph[- ]?rag", r"re-?rank\w*", r"chunking", r"pgvector", r"pinecone", r"weaviate",
        r"qdrant", r"milvus", r"chroma", r"llamaindex", r"search (?:relevance|quality)",
        r"grounding",
    ]),
    ("Evals, observability & reliability", [
        r"evals?", r"evaluat\w*", r"benchmark\w*", r"observability", r"llmops", r"tracing",
        r"traces", r"hallucinat\w*", r"reliab\w*", r"(?:llm|agent|ai|model) monitoring",
        r"testing (?:llms?|agents?|ai|models?)", r"(?:llm|agent|ai)[- ]testing",
        r"langsmith", r"langfuse", r"arize", r"braintrust", r"opentelemetry",
        r"quality (?:assurance|gates?|metrics)", r"failure modes?", r"regression testing",
        r"llm[- ]as[- ]a[- ]judge", r"human[- ]in[- ]the[- ]loop",
    ]),
    ("Prompting & context engineering", [
        r"prompt engineering", r"prompting", r"prompts?(?! injection| attacks?| hacking)",
        r"context engineering", r"context windows?", r"few[- ]shot", r"zero[- ]shot",
        r"chain[- ]of[- ]thought", r"system prompts?",
        r"prompt (?:design|optimi[sz]ation|tuning|management|templates?|libraries|caching)",
        r"dspy", r"long[- ]context", r"context (?:management|compression|rot|length)",
        r"in[- ]context learning",
    ]),
    ("Security, safety & red teaming", [
        r"prompt injection", r"jailbreak\w*", r"red[- ]team\w*", r"adversarial",
        r"guardrails?", r"threats?", r"threat model\w*", r"vulnerabilit\w*", r"owasp",
        r"(?:data|model) poisoning", r"secur(?:e|ity|ing)", r"safe(?:ty|guards?)", r"attacks?",
        r"exploits?", r"malware", r"exfiltrat\w*", r"cves?", r"pentest\w*",
        r"penetration test\w*", r"zero[- ]trust", r"appsec", r"cybersecurity", r"deepfakes?",
        r"backdoors?", r"supply chain (?:attacks?|security)", r"secrets", r"phishing",
        r"privacy[- ]preserving",
    ]),
    ("Governance, ethics & regulation", [
        r"responsible ai", r"ethic\w*", r"governance", r"regulat\w*", r"(?:eu )?ai act",
        r"complian\w*", r"bias(?:es|ed)?", r"fairness", r"privacy", r"alignment",
        r"trustworthy", r"transparen\w*", r"explainab\w*", r"accountab\w*", r"gdpr",
        r"(?:ai|public|data) polic(?:y|ies)", r"sovereign\w*", r"risk management",
        r"nist", r"iso 42001", r"audit\w*", r"copyright", r"intellectual property",
        r"legislation", r"regulators?", r"misinformation",
    ]),
    ("Inference, serving & GPU infra", [
        r"inference", r"model serving", r"serving", r"vllm", r"sglang", r"tensorrt(?:-llm)?",
        r"triton", r"latency", r"throughput", r"gpus?", r"cuda", r"quantiz\w*",
        r"kubernetes", r"k8s", r"accelerators?", r"tpus?", r"npus?", r"on[- ]device",
        r"edge (?:ai|inference|deployment|devices?|computing)", r"nvidia", r"llama\.?cpp",
        r"ollama", r"kv[- ]cache", r"speculative decoding", r"batching", r"kserve",
        r"(?:ai|ml|llm|gpu) infrastructure", r"hardware", r"chips?", r"silicon",
        r"distributed inference", r"scaling (?:inference|llms|models)",
        r"cost (?:optimi[sz]ation|efficiency)", r"token economics", r"clusters?",
    ]),
    ("Training, fine-tuning & model building", [
        r"fine[- ]?tun\w*", r"pre[- ]?training", r"post[- ]training", r"rlhf", r"rlaif",
        r"reinforcement learning", r"rl", r"lora", r"qlora", r"peft", r"distill\w*",
        r"foundation models?", r"pytorch", r"jax", r"open[- ]weights?",
        r"open[- ]source (?:models?|llms?)", r"(?:model|llm|distributed) training",
        r"training (?:llms?|models?|data|pipelines?|runs?|a model)", r"scaling laws?",
        r"mixture of experts", r"moe", r"tokeniz\w*", r"synthetic data", r"dpo", r"grpo",
        r"sft", r"supervised fine", r"hugging ?face", r"small language models?", r"slms?",
        r"from scratch", r"model (?:architectures?|building|development|weights)",
        r"transformer architecture", r"attention mechanism",
    ]),
    ("Data engineering & MLOps", [
        r"mlops", r"feature stores?",
        r"data (?:pipelines?|platforms?|lakehouses?|lakes?|warehouses?|engineering|quality|"
        r"mesh|infrastructure|governance|catalogs?|contracts?|products?)",
        r"spark", r"databricks", r"snowflake", r"dbt", r"airflow", r"kafka", r"flink",
        r"iceberg", r"delta lake", r"model registr(?:y|ies)", r"experiment tracking",
        r"mlflow", r"kubeflow", r"etl", r"elt", r"sql", r"bigquery", r"ml platforms?",
        r"feature engineering", r"data engineers?", r"(?:event|data|stream) streaming",
        r"streaming (?:data|pipelines?|platforms?)", r"batch (?:jobs?|processing)",
        r"model deployment", r"ml pipelines?", r"data teams?",
    ]),
    ("Multimodal, vision, speech & robotics", [
        r"multi-?modal\w*", r"computer vision", r"machine vision",
        r"vision (?:models?|language|transformers?|ai|systems?|encoders?)", r"vision[- ]language",
        r"vlms?", r"(?:facial|face) recognition", r"generative media", r"remote sensing",
        r"satellite (?:imagery|images?)",
        r"image (?:generation|recognition|classification|models?|understanding|analysis|"
        r"segmentation|synthesis)",
        r"video (?:generation|understanding|models?|analysis|analytics)",
        r"generat\w+ (?:images?|videos?)", r"text[- ]to[- ](?:image|video|speech|3d)",
        r"speech (?:recognition|synthesis|to text|models?|ai)", r"speech[- ]to[- ]text",
        r"voice (?:agents?|assistants?|ai|bots?|interfaces?|apps?|applications?|models?)",
        r"real[- ]time voice", r"audio (?:models?|generation|ai|processing)", r"tts", r"asr",
        r"whisper", r"robot\w*", r"embodied", r"humanoids?", r"diffusion(?: models?)?",
        r"stable diffusion", r"midjourney", r"dall-?e", r"sora", r"ocr",
        r"self[- ]driving", r"autonomous (?:vehicles?|driving|cars?)", r"drones?",
        r"object detection", r"3d",
    ]),
    ("Enterprise adoption & strategy", [
        r"adopt\w*", r"roll-?outs?", r"upskill\w*", r"reskill\w*", r"change management",
        r"(?:ai|digital) transformation", r"enterprise ai",
        r"ai (?:in|for|at|across) the enterprise", r"startups?", r"founders?",
        r"roi", r"return on investment", r"leadership", r"leaders", r"future of work",
        r"product (?:management|managers?|design|strategy|teams?|thinking|leaders?)",
        r"ux", r"user experience",
        r"business (?:value|strategy|case|impact|outcomes?|models?|leaders?|users?)",
        r"go[- ]to[- ]market", r"ceos?", r"ctos?", r"c-suite", r"executives?",
        r"(?:ai|business|data|product|platform|enterprise|agent|genai) strateg(?:y|ies)", r"strategic",
        r"culture", r"organi[sz]ational", r"workforce",
        r"(?:pilot|poc|prototype)s? to production", r"proof of concept", r"scaling ai",
        r"ai[- ](?:first|native) (?:compan(?:y|ies)|organi[sz]ations?|business(?:es)?)",
        r"venture", r"investors?", r"vcs?", r"pricing", r"monetiz\w*", r"revenue",
        r"ai literacy", r"transformation", r"buy (?:vs\.?|or|versus) build",
        r"build (?:vs\.?|or|versus) buy", r"customer (?:service|support|experience)",
    ]),
    ("Science, healthcare & applied ML", [
        r"health\w*", r"medical", r"medicine", r"clinical", r"clinicians?", r"patients?",
        r"hospitals?", r"biolog\w*", r"bio", r"biotech", r"drug discovery", r"pharma\w*",
        r"proteins?", r"genom\w*", r"climate", r"weather", r"energy", r"physics",
        r"chemistry", r"materials science", r"astronomy", r"neuroscience",
        r"scientific (?:discovery|research|computing)", r"finance",
        r"financial", r"fintech", r"banking", r"insurance", r"trading", r"manufacturing",
        r"industrial", r"legal", r"law firms?", r"lawyers?", r"education", r"teachers?",
        r"classrooms?", r"agriculture", r"farming", r"retail", r"e-?commerce",
        r"logistics", r"supply chains?", r"automotive", r"aerospace", r"telecom\w*",
        r"government", r"public sector", r"defen[cs]e", r"mathematics", r"math",
        r"theorem\w*", r"journalism", r"game (?:development|dev|studios?|engines?)",
        r"video games?", r"gaming", r"sports?", r"accessibility", r"nonprofits?",
        r"humanitarian", r"real estate", r"construction",
    ]),
    ("Classic ML & data science", [
        r"machine learning", r"data science", r"data scientists?", r"scikit[- ]learn",
        r"sklearn", r"xgboost", r"lightgbm", r"catboost", r"regression", r"classification",
        r"clustering", r"forecasting", r"time[- ]series", r"statistic\w*", r"bayesian",
        r"recommend(?:er|ation) (?:systems?|engines?|models?)", r"recommenders?", r"pandas",
        r"polars", r"numpy", r"julia", r"jupyter", r"notebooks?", r"anomaly detection",
        r"causal (?:inference|ml|models?)", r"a/b test\w*", r"experimentation",
        r"feature (?:engineering|selection)", r"gradient boost\w*", r"random forests?",
        r"neural networks?", r"deep learning", r"predictive (?:models?|analytics|modeling)",
        r"tabular", r"dimensionality", r"probabilistic", r"simulation", r"matplotlib",
        r"visuali[sz]ation", r"dashboards?", r"analytics", r"scipy", r"r language",
    ]),
]
TOPIC_NAMES = [name for name, _ in TOPICS]

TITLE_HIT = 2        # a phrase in the title
TOPIC_THRESHOLD = 2  # what a topic needs to be assigned

# The tags and the description carry the channel's habits as well as the
# talk's: PyData's every description says "data science" and "machine
# learning", AI Engineer's every upload is tagged "startups". That is the
# caller's problem, not this module's: sync_catalog.py measures, per
# conference, which description lines (>10% of talks, verbatim) and tags
# (>30%) are stock, strips them, and passes the cleaned tags and description
# in. Titles are never stripped, since a title is written per talk.


def _phrase_re(pattern: str) -> re.Pattern:
    return re.compile(r"(?<![\w-])(?:" + pattern + r")(?!\w)", re.I)


# (name, [one regex per phrase], the regex of all of them) — the combined one
# scans a text once; a match is attributed to its phrase by fullmatch, which is
# what makes "distinct phrases" countable without fifteen passes per topic.
TOPIC_RES = [(name, [_phrase_re(p) for p in phrases], _phrase_re("|".join(phrases)))
             for name, phrases in TOPICS]


@functools.lru_cache(maxsize=65536)
def _phrase_index(topic_i: int, matched: str) -> int:
    _, phrases, _ = TOPIC_RES[topic_i]
    for i, p in enumerate(phrases):
        if p.fullmatch(matched):
            return i
    return -1


def _said(topic_i: int, text: str) -> set[str]:
    """The phrases of one topic this text says, lowercased."""
    _, _, whole = TOPIC_RES[topic_i]
    return {m.group().lower() for m in whole.finditer(text)}


def _body(tags, description: str | None) -> str:
    return unicodedata.normalize("NFKC", f"{' '.join(tags or [])}\n{description or ''}")


def topic_scores(title: str | None, tags, description: str | None) -> dict[str, int]:
    """Every topic that scored, and what it scored. See TOPICS for the rule."""
    head = title or ""
    body = _body(tags, description)
    out = {}
    for i, (name, _, whole) in enumerate(TOPIC_RES):
        score = TITLE_HIT if whole.search(head) else 0
        if body.strip():
            score += len({_phrase_index(i, s) for s in _said(i, body)})
        if score:
            out[name] = score
    return out


def topics_of(title: str | None, tags, description: str | None) -> list[str]:
    """The topics a talk is filed under, sorted; [] when nothing reaches the bar."""
    return sorted(name for name, s in topic_scores(title, tags, description).items()
                  if s >= TOPIC_THRESHOLD)


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
DB_SCHEMA_VERSION = 6


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
