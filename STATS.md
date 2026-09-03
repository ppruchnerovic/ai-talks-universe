# Corpus by the numbers

Fun facts and hard numbers about how much information is in this knowledge
base. All figures derived from `data/talks.csv`, `data/transcripts/` and the
tracked files in this repository.

*Generated 2026-09-03.*

## 📊 The corpus

| | |
|---|---|
| **Talks** | **9,048** |
| Conferences | **53** (5 categories) |
| Full transcripts | **3,175** (35% of talks) |
| Unique speakers | **4,364** across 4,982 credited talks |
| Topic tags | 15 taxonomy topics, 11,395 assignments |
| Years covered | 2018 → 2026 (77% from 2025–26) |

Talks by category: Practitioner AI conferences 3,903 · General software
conferences 2,301 · Vendor events 1,796 · Security conferences 839 ·
Business & industry events 209.

## ⏱️ Watch time

- **304,117 minutes = 5,069 hours = 211 days** of continuous video.
- **Start it on New Year's Day and you finish at the end of July** — no sleep,
  no pausing.
- Transcribed audio alone: **1,754 hours (73 days)**.
- Median talk: 30 minutes. Mean: 33.6 minutes.
- Longest talk: **8h 52m** — *Microsoft Build 2026 Day 1 LIVE | Opening
  Keynote, Live Coding & Demos*.

## 📝 The words

| | |
|---|---|
| Transcript words | **17,101,152** |
| Estimated tokens (×1.33) | **~22.7 million** |
| Timestamped segments | **2,363,092** |
| Distinct word forms | **69,471** |
| Title + description words | 1,422,377 |
| Mean words per transcript | 5,386 (median 4,746) |

Fun scale checks on 17.1M words:

- **≈ 29× *War and Peace***, or **≈ 16× the entire Harry Potter series**.
- Read aloud at 200 wpm it would take **1,425 hours — 59 days nonstop**.
- It would fill the context window of a 1M-token model **23 times over**.
- Longest single transcript: **73,728 words** — a full-length novel, spoken.

## 🗣️ What the AI world actually says

Word frequencies across all 3,175 transcripts:

| Term | Count |
|---|---|
| agent / agents / agentic | **71,544** |
| context | 15,476 |
| LLM / LLMs | 11,072 |
| prompt / prompts | 11,934 |
| MCP | 11,041 |
| token / tokens | 9,189 |
| Claude | 5,607 |
| GPU / GPUs | 4,596 |
| eval / evals | 3,610 |
| Kubernetes | 3,245 |
| Copilot | 2,436 |
| GPT | 1,916 |
| RAG | 1,632 |
| "vibe" | 1,255 |
| hallucination(s) | **704** |
| LangChain | 220 |

> "Agent" is said **101× more often than "hallucination"** — and MCP, which
> did not exist before late 2024, already outranks RAG **6.8 to 1**.

## 🗂️ Storage, indexes and shards

- **13,059 tracked files**, ~2.64M lines, 688 MB of data.
- **399 MB SQLite** database with two FTS5 indexes (talks + 2.36M segments).
- **712 browser index shards** (46 MB) so search runs client-side, on a phone.
- 3,175 transcript JSON files (199 MB) + 9,048 Markdown talk pages (135 MB).
- Catalog caches: 26 MB. InfoQ cache: 372 KB.

## 💻 Code that produces it

| Language | Files | Lines | Non-blank |
|---|---|---|---|
| Python | 21 | 10,914 | 9,321 |
| JavaScript | 11 | 2,050 | 1,861 |
| HTML | 1 | 1,315 | 1,243 |
| YAML | 2 | 199 | 175 |
| Shell | 2 | 162 | 149 |
| **Total** | **37** | **14,640** | **12,749** |

Data/content files, which are not code:

| Type | Files | Lines |
|---|---|---|
| JSON | 3,961 | 1,851,232 |
| Markdown | 9,056 | 668,049 |
| CSV | 1 | 109,261 |

All of it is driven by roughly **14,600 lines of code** — a data-to-code ratio
of about **47,000 : 1**.

## 🏆 Biggest contributors

| Conference | Talks |
|---|---|
| AI Engineer | 899 |
| Microsoft Ignite | 761 |
| QCon / InfoQ Dev Summit | 579 |
| WeAreDevelopers World Congress | 553 |
| MLOps World / Toronto ML Summit | 503 |
| PyData | 407 |
| Microsoft Build | 366 |
| AI Council (formerly Data Council) | 357 |
| AI_dev / Open Source Summit | 328 |
| AWS re:Invent | 287 |

Smallest, but still worth having: OWASP Global AppSec (2), TEDAI Vienna (6),
Apple WWDC (7), Meta Connect + LlamaCon (9), Web Summit (11).

## 🎙️ Where the transcripts come from

| Source | Transcripts |
|---|---|
| Supadata (paid credits) | 2,491 |
| YouTube captions | 455 |
| InfoQ (hand-edited, free) | 228 |

**236 transcripts are human-written**, not machine-generated. Languages:
English 3,147, Hindi 12, German 3, Spanish 2.

Conferences with the deepest transcript coverage: AI Engineer (540),
WeAreDevelopers (433), QCon/InfoQ (334), PyData (206), Microsoft Build (187),
Berkeley Agentic AI Summit (159), KubeCon (151), NDC (149).
