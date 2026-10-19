# Corpus by the numbers

Fun facts and hard numbers about how much information is in this knowledge
base. All figures derived from `data/talks.csv`, `data/transcripts/` and the
tracked files in this repository.

*Generated 2026-10-19.*

## 📊 The corpus

| | |
|---|---|
| **Talks** | **10,473** |
| Conferences | **53** (5 categories) |
| Full transcripts | **3,903** (37% of talks) |
| Unique speakers | **6,399** across 5,994 credited talks |
| Topic tags | 15 taxonomy topics, 15,219 assignments |
| Years covered | 2018 → 2026 (80% from 2025–26) |

Talks by category: Practitioner AI conferences 4,622 · General software
conferences 2,646 · Vendor events 2,044 · Security conferences 903 ·
Business & industry events 258.

## ⏱️ Watch time

- **354,541 minutes = 5,909 hours = 246 days** of continuous video.
- **Start it on New Year's Day and you finish on September 4** — no sleep,
  no pausing.
- Transcribed audio alone: **2,185 hours (91 days)**.
- Median talk: 30 minutes. Mean: 33.9 minutes.
- Longest talk: **8h 52m** — *Microsoft Build 2026 Day 1 LIVE | Opening
  Keynote, Live Coding & Demos*.

## 📝 The words

| | |
|---|---|
| Transcript words | **21,326,602** |
| Estimated tokens (×1.33) | **~28.4 million** |
| Timestamped segments | **2,979,254** |
| Distinct word forms | **81,543** |
| Title + description words | 2,003,412 |
| Mean words per transcript | 5,464 (median 4,744) |

Fun scale checks on 21.3M words:

- **≈ 36× *War and Peace***, or **≈ 20× the entire Harry Potter series**.
- Read aloud at 200 wpm it would take **1,777 hours — 74 days nonstop**.
- It would fill the context window of a 1M-token model **28 times over**.
- Longest single transcript: **73,728 words** — a full-length novel, spoken.

## 🗣️ What the AI world actually says

Word frequencies across all 3,903 transcripts:

| Term | Count |
|---|---|
| agent / agents / agentic | **90,549** |
| context | 19,208 |
| prompt / prompts | 15,331 |
| LLM / LLMs | 14,631 |
| MCP | 13,100 |
| token / tokens | 12,474 |
| GPU / GPUs | 7,308 |
| Claude | 6,577 |
| eval / evals | 4,896 |
| Kubernetes | 3,824 |
| Copilot | 2,787 |
| GPT | 2,094 |
| RAG | 2,024 |
| "vibe" | 1,449 |
| hallucination(s) | **893** |
| LangChain | 262 |

> "Agent" is said **101× more often than "hallucination"** — and MCP, which
> did not exist before late 2024, already outranks RAG **6.5 to 1**.

## 🗂️ Storage, indexes and shards

- **15,263 tracked files**, ~3.01M lines, 547 MB of data.
- **480 MB SQLite** database with two FTS5 indexes (talks + 2.98M segments).
- **724 browser index shards** (56 MB) so search runs client-side, on a phone.
- 3,903 transcript JSON files (238 MB) + 10,473 Markdown talk pages (144 MB).
- Catalog caches: 34 MB. InfoQ cache: 376 KB.

## 💻 Code that produces it

| Language | Files | Lines | Non-blank |
|---|---|---|---|
| Python | 23 | 11,166 | 9,538 |
| JavaScript | 11 | 2,058 | 1,868 |
| HTML | 1 | 1,315 | 1,243 |
| Shell | 4 | 459 | 427 |
| YAML | 6 | 196 | 178 |
| **Total** | **45** | **15,194** | **13,254** |

Data/content files, which are not code:

| Type | Files | Lines |
|---|---|---|
| JSON | 4,708 | 2,009,995 |
| Markdown | 10,500 | 833,317 |
| CSV | 1 | 157,120 |

All of it is driven by roughly **15,200 lines of code** — a data-to-code ratio
of about **36,000 : 1**.

## 🏆 Biggest contributors

| Conference | Talks |
|---|---|
| AI Engineer | 1,168 |
| Microsoft Ignite | 761 |
| QCon / InfoQ Dev Summit | 596 |
| WeAreDevelopers World Congress | 566 |
| PyData | 522 |
| MLOps World / Toronto ML Summit | 503 |
| Microsoft Build | 414 |
| AWS re:Invent | 382 |
| Devoxx | 373 |
| AI Council (formerly Data Council) | 357 |

Smallest, but still worth having: TEDAI Vienna (6), OWASP Global AppSec (7),
Web Summit (12), Meta Connect + LlamaCon (17), Y Combinator AI Startup School (17).

## 🎙️ Where the transcripts come from

| Source | Transcripts |
|---|---|
| Supadata (paid credits) | 3,221 |
| YouTube captions | 451 |
| InfoQ (hand-edited, free) | 231 |

**238 transcripts are human-written**, not machine-generated. Languages:
English 3,874, German 8, Hindi 8, Norwegian 3, Spanish 2.

Conferences with the deepest transcript coverage: AI Engineer (808),
WeAreDevelopers (440), QCon/InfoQ (351), PyData (247), Microsoft Build (187),
NDC (184), Berkeley Agentic AI Summit (159), AI DevCon (156).
