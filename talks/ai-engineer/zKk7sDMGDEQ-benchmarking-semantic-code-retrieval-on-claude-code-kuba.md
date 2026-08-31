---
id: zKk7sDMGDEQ
title: "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer"
slug: benchmarking-semantic-code-retrieval-on-claude-code-kuba
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kuba Rogut"]
channel: null
duration_min: 16
published_at: 2026-06-03T00:00:00Z
video_id: zKk7sDMGDEQ
youtube_url: https://www.youtube.com/watch?v=zKk7sDMGDEQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

**Kuba Rogut**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=zKk7sDMGDEQ) · [Conference site](https://www.ai.engineer/)

## Description

By default, Claude Code wastes one in every three file reads. Add windowed grep and that drops to one in five. Add semantic search on top and it drops to one in eight, with file precision climbing from 65% to 87%. Kuba Rogut from Turbopuffer ran a 50-task benchmark against ContextBench to measure not whether the agent solved the problem but whether it found the right files, lines, and symbols along the way.

The benchmark tested three conditions: raw Claude Code, windowed reads capped at 50 lines, and windowed reads plus a semantic search tool backed by Turbopuffer. Semantic search won on behavior adjacent tasks where files share no keywords. Grep won on import tracing where the keyword is right there. Cursor's production numbers show a 24% relative improvement in answer accuracy from semantic retrieval, plus a 2.6% increase in code retention in large codebases. Kuba's explanation for why his gains were smaller: Cursor's model knows when and why to call semantic search. Claude Code just has it as another tool in the list.

Speaker info:
- https://ca.linkedin.com/in/kubarogut
- https://rogutkuba.com/
