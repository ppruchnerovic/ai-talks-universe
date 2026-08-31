---
id: 7vn4WpqNpck
title: "Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs"
slug: benchmarking-coding-agents-on-new-vs-legacy-codebases-denys
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Denys Linkov"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-08-08T00:00:00Z
video_id: 7vn4WpqNpck
youtube_url: https://www.youtube.com/watch?v=7vn4WpqNpck
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Benchmarking Coding Agents on New vs Legacy Codebases — Denys Linkov, Wisedocs

**Denys Linkov**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=7vn4WpqNpck) · [Conference site](https://www.ai.engineer/)

## Description

Wisedocs processes medical claims that arrive as PDFs over 10,000 pages long, some of them larger than video files, through a pipeline of ML models spread across ten repositories nobody enjoyed touching. Denys Linkov's team spent six months collapsing that into a monorepo, and this talk is an honest audit of whether they should have just waited for the models to get good enough to do it for them. The benchmark he keeps coming back to is a single refactor task. With o3 it took three hours of back and forth in Cursor and still shipped ten major mistakes. Rerun on newer models, Sonnet 4.6 needed one extra iteration and Opus 4.8 essentially got it in one pass, at roughly a fifth of the original effort.

The counterweight is what happens when you hand a current model the whole job. GPT 5.5 extra high declared the refactor done in 10 minutes 22 seconds and wrote 2,000 lines, which turned out to be scaffolding with the actual models missing, something it admitted in its own output by noting it had not added the deployment or bootstrap command yet. That gap is why Linkov reads the METR task length curve at 80% or 90% success instead of the usual 50%. Launching an hour long agent run on coin flip odds mostly buys you a wasted hour and a broken attention span. His verdict is that doing the refactor beat deferring it, and the evidence is as much social as technical: commit velocity rose and never flattened, work that used to take months ships in under a week, and developers across the company now volunteer into the repo even outside their own area, which was never true of the ten it replaced.

Speaker info:
- https://x.com/denyslinkov
- https://www.linkedin.com/in/denyslinkov/
