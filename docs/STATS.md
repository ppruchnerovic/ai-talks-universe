# Corpus by the numbers

Fun facts and hard numbers about how much information is in this knowledge
base. All figures derived from `data/talks.csv`, `data/transcripts/` and the
tracked files in this repository.

*Generated 2026-09-14.*

## 📊 The corpus

| | |
|---|---|
| **Talks** | **9,831** |
| Conferences | **53** (5 categories) |
| Full transcripts | **3,437** (35% of talks) |
| Unique speakers | **6,160** across 5,673 credited talks |
| Topic tags | 15 taxonomy topics, 14,070 assignments |
| Years covered | 2018 → 2026 (79% from 2025–26) |

Talks by category: Practitioner AI conferences 4,084 · General software
conferences 2,542 · Vendor events 2,044 · Security conferences 903 ·
Business & industry events 258.

## ⏱️ Watch time

- **334,319 minutes = 5,572 hours = 232 days** of continuous video.
- **Start it on New Year's Day and you finish on August 20** — no sleep,
  no pausing.
- Transcribed audio alone: **1,913 hours (80 days)**.
- Median talk: 31 minutes. Mean: 34.0 minutes.
- Longest talk: **8h 52m** — *Microsoft Build 2026 Day 1 LIVE | Opening
  Keynote, Live Coding & Demos*.

## 📝 The words

| | |
|---|---|
| Transcript words | **18,670,301** |
| Estimated tokens (×1.33) | **~24.8 million** |
| Timestamped segments | **2,592,578** |
| Distinct word forms | **73,518** |
| Title + description words | 1,862,295 |
| Mean words per transcript | 5,432 (median 4,795) |

Fun scale checks on 18.7M words:

- **≈ 32× *War and Peace***, or **≈ 17× the entire Harry Potter series**.
- Read aloud at 200 wpm it would take **1,556 hours — 65 days nonstop**.
- It would fill the context window of a 1M-token model **25 times over**.
- Longest single transcript: **73,728 words** — a full-length novel, spoken.

## 🗣️ What the AI world actually says

Word frequencies across all 3,437 transcripts:

| Term | Count |
|---|---|
| agent / agents / agentic | **76,608** |
| context | 16,762 |
| prompt / prompts | 13,364 |
| LLM / LLMs | 12,663 |
| MCP | 11,774 |
| token / tokens | 10,024 |
| Claude | 5,921 |
| GPU / GPUs | 5,062 |
| eval / evals | 3,686 |
| Kubernetes | 3,353 |
| Copilot | 2,516 |
| GPT | 1,909 |
| RAG | 1,756 |
| "vibe" | 1,346 |
| hallucination(s) | **803** |
| LangChain | 225 |

> "Agent" is said **95× more often than "hallucination"** — and MCP, which
> did not exist before late 2024, already outranks RAG **6.7 to 1**.

## 🗂️ Storage, indexes and shards

- **14,153 tracked files**, ~2.89M lines, 489 MB of data.
- **424 MB SQLite** database with two FTS5 indexes (talks + 2.59M segments).
- **723 browser index shards** (50 MB) so search runs client-side, on a phone.
- 3,437 transcript JSON files (209 MB) + 9,831 Markdown talk pages (128 MB).
- Catalog caches: 33 MB. InfoQ cache: 376 KB.

## 💻 Code that produces it

| Language | Files | Lines | Non-blank |
|---|---|---|---|
| Python | 23 | 11,166 | 9,538 |
| JavaScript | 11 | 2,050 | 1,861 |
| HTML | 1 | 1,315 | 1,243 |
| Shell | 4 | 459 | 427 |
| YAML | 6 | 196 | 178 |
| **Total** | **45** | **15,186** | **13,247** |

Data/content files, which are not code:

| Type | Files | Lines |
|---|---|---|
| JSON | 4,241 | 1,970,752 |
| Markdown | 9,858 | 758,769 |
| CSV | 1 | 145,028 |

All of it is driven by roughly **15,200 lines of code** — a data-to-code ratio
of about **32,000 : 1**.

## 🏆 Biggest contributors

| Conference | Talks |
|---|---|
| AI Engineer | 930 |
| Microsoft Ignite | 761 |
| QCon / InfoQ Dev Summit | 584 |
| WeAreDevelopers World Congress | 565 |
| PyData | 518 |
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
| Supadata (paid credits) | 2,755 |
| YouTube captions | 451 |
| InfoQ (hand-edited, free) | 231 |

**238 transcripts are human-written**, not machine-generated. Languages:
English 3,413, Hindi 8, German 3, Norwegian 3, Spanish 2.

Conferences with the deepest transcript coverage: AI Engineer (571),
WeAreDevelopers (440), QCon/InfoQ (339), PyData (244), Microsoft Build (187),
NDC (177), Berkeley Agentic AI Summit (159), KubeCon (151).
