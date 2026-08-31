---
id: EUsPvBeIx70
title: "Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra"
slug: semantic-blindness-500-000-sensors-confused-an-llm-raahul
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 16
published_at: 2026-07-12T16:00:36Z
video_id: EUsPvBeIx70
youtube_url: https://www.youtube.com/watch?v=EUsPvBeIx70
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Semantic Blindness: 500,000 Sensors Confused an LLM - Raahul Singh & Vanč Levstik, Phaidra

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=EUsPvBeIx70) · [Conference site](https://www.ai.engineer/)

## Description

You cannot solve a combinatorial engineering problem with a next token prediction engine. We learned this the hard way.

Modern LLMs can write code, summarize research papers, and reason across massive datasets. But what happens when you connect them to mission-critical physical infrastructure with 50,000 live sensors, deterministic dependencies, and real-world thermodynamic constraints?

We deployed state-of-the-art LLMs to manage real time operations within industrial and AI factory environments to tackle root cause analysis, alarm triage, and operational decision support. What we discovered was a fundamental architectural mismatch between probabilistic language models and deterministic engineering systems.

In this talk, we introduce a failure mode we call Semantic Blindness: the inability of general-purpose LLMs to maintain structural awareness of physical systems, even when provided enormous amounts of context.

This talk dissects three specific failure modes we encountered — and why each one exposes a gap in how the industry thinks about scaling LLMs to complex systems:

1) The Topology Trap. Vector embeddings don't understand pipes, wires, or physical causality. Sensor_445_Temp is just a string. But in reality, it's attached to Valve B, which controls coolant to Generator 3.
2) The Illusion of Scale. At a small scale, dumping 100 sensors into the context window works surprisingly well. It’s a reasonable solution and it holds up. At 500,000 sensors, the same approach collapses. It creates new problems: attention degrades, critical anomalies get buried in the middle, and latency spikes to unusable levels for real-time response.

3) The Repetition Kill Switch. Industrial tag naming conventions are nearly identical at scale. Feeding the same naming conventions across hundreds of variants, you’ll trip the model’s repetition penalty. It thinks it’s stuck in a degenerate loop and it will literally stop. The data is correct. The model just can’t handle it.
Rather than focusing on prompt engineering tricks, this session explores the architectural patterns required to make AI reliable in real-world engineering environments.

We’ll present a practical hybrid design approach that combines:

- semantic ontologies,
- deterministic query systems,
- structured synthesis layers,
- and LLM orchestration architectures purpose-built for operational infrastructure.

Attendees will leave with a clear understanding of:

- why naive RAG architectures fail in industrial environments,
- how to design AI systems that respect physical reality,
- how to make LLMs work reliably against massive scale of data
- and what the next generation of “AI-enabled intent resolution” actually looks like beyond semantic search.

This session is designed for senior AI engineers, infrastructure architects, CTOs, and technical leaders building AI systems that must operate reliably under real-world constraints — not just benchmark well in demos.

Speakers:
- Raahul Singh (Phaidra): Raahul Singh is a Staff AI Research Engineer at Phaidra and the lead architect behind the company's agentic AI platform for data center infrastructure.
- Vanč Levstik (Phaidra): Vanč Levstik is a Senior Engineering Manager at Phaidra and leading the teams developing Phaidra Prism
