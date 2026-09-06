# Corpus by the numbers

Fun facts and hard numbers about how much information is in this knowledge
base. All figures derived from `data/talks.csv`, `data/transcripts/` and the
tracked files in this repository.

*Generated 2026-09-06.*

## 📊 The corpus

| | |
|---|---|
| **Talks** | **9,797** |
| Conferences | **53** (5 categories) |
| Full transcripts | **3,409** (35% of talks) |
| Unique speakers | **6,145** across 5,653 credited talks |
| Topic tags | 15 taxonomy topics, 14,019 assignments |
| Years covered | 2018 → 2026 (78% from 2025–26) |

Talks by category: Practitioner AI conferences 4,059 · General software
conferences 2,537 · Vendor events 2,044 · Security conferences 899 ·
Business & industry events 258.

## ⏱️ Watch time

- **333,492 minutes = 5,558 hours = 232 days** of continuous video.
- **Start it on New Year's Day and you finish on August 20** — no sleep,
  no pausing.
- Transcribed audio alone: **1,904 hours (79 days)**.
- Median talk: 31 minutes. Mean: 34.0 minutes.
- Longest talk: **8h 52m** — *Microsoft Build 2026 Day 1 LIVE | Opening
  Keynote, Live Coding & Demos*.

## 📝 The words

| | |
|---|---|
| Transcript words | **18,538,716** |
| Estimated tokens (×1.33) | **~24.7 million** |
| Timestamped segments | **2,574,199** |
| Distinct word forms | **76,438** |
| Title + description words | 1,852,354 |
| Mean words per transcript | 5,438 (median 4,807) |

Fun scale checks on 18.5M words:

- **≈ 32× *War and Peace***, or **≈ 17× the entire Harry Potter series**.
- Read aloud at 200 wpm it would take **1,545 hours — 64 days nonstop**.
- It would fill the context window of a 1M-token model **25 times over**.
- Longest single transcript: **73,728 words** — a full-length novel, spoken.

## 🗣️ What the AI world actually says

Word frequencies across all 3,409 transcripts:

| Term | Count |
|---|---|
| agent / agents / agentic | **75,399** |
| context | 16,585 |
| LLM / LLMs | 12,486 |
| prompt / prompts | 13,307 |
| MCP | 11,647 |
| token / tokens | 9,860 |
| Claude | 5,747 |
| GPU / GPUs | 4,975 |
| eval / evals | 3,665 |
| Kubernetes | 3,351 |
| Copilot | 2,489 |
| GPT | 1,874 |
| RAG | 1,747 |
| "vibe" | 1,327 |
| hallucination(s) | **802** |
| LangChain | 222 |

> "Agent" is said **94× more often than "hallucination"** — and MCP, which
> did not exist before late 2024, already outranks RAG **6.7 to 1**.

## 🗂️ Storage, indexes and shards

- **14,063 tracked files**, ~2.88M lines, 490 MB of data.
- **421 MB SQLite** database with two FTS5 indexes (talks + 2.57M segments).
- **722 browser index shards** (49 MB) so search runs client-side, on a phone.
- 3,409 transcript JSON files (215 MB) + 9,797 Markdown talk pages (146 MB).
- Catalog caches: 33 MB. InfoQ cache: 376 KB.

## 💻 Code that produces it

| Language | Files | Lines | Non-blank |
|---|---|---|---|
| Python | 21 | 10,968 | 9,372 |
| JavaScript | 11 | 2,050 | 1,861 |
| HTML | 1 | 1,315 | 1,243 |
| YAML | 2 | 199 | 175 |
| Shell | 2 | 162 | 149 |
| **Total** | **37** | **14,694** | **12,800** |

Data/content files, which are not code:

| Type | Files | Lines |
|---|---|---|
| JSON | 4,207 | 1,967,262 |
| Markdown | 9,814 | 754,127 |
| CSV | 1 | 144,428 |

All of it is driven by roughly **14,700 lines of code** — a data-to-code ratio
of about **35,000 : 1**.

## 🏆 Biggest contributors

| Conference | Talks |
|---|---|
| AI Engineer | 914 |
| Microsoft Ignite | 761 |
| QCon / InfoQ Dev Summit | 583 |
| WeAreDevelopers World Congress | 561 |
| PyData | 517 |
| MLOps World / Toronto ML Summit | 503 |
| Microsoft Build | 414 |
| AWS re:Invent | 382 |
| AI Council (formerly Data Council) | 357 |
| AI_dev / Open Source Summit | 328 |

Smallest, but still worth having: TEDAI Vienna (6), OWASP Global AppSec (7),
Web Summit (12), Meta Connect + LlamaCon (17), Y Combinator AI Startup School (17).

## 🎙️ Where the transcripts come from

| Source | Transcripts |
|---|---|
| Supadata (paid credits) | 2,723 |
| YouTube captions | 455 |
| InfoQ (hand-edited, free) | 231 |

**238 transcripts are human-written**, not machine-generated. Languages:
English 3,381, Hindi 12, German 3, Norwegian 3, Spanish 2.

Conferences with the deepest transcript coverage: AI Engineer (555),
WeAreDevelopers (436), QCon/InfoQ (338), PyData (243), Microsoft Build (187),
NDC (177), Berkeley Agentic AI Summit (159), KubeCon (151).
