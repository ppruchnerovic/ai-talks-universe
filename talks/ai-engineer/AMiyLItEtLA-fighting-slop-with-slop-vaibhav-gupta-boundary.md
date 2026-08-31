---
id: AMiyLItEtLA
title: "fighting slop with slop — Vaibhav Gupta, Boundary"
slug: fighting-slop-with-slop-vaibhav-gupta-boundary
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Vaibhav Gupta"]
channel: null
duration_min: 22
published_at: 2026-07-31T00:00:00Z
video_id: AMiyLItEtLA
youtube_url: https://www.youtube.com/watch?v=AMiyLItEtLA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# fighting slop with slop — Vaibhav Gupta, Boundary

**Vaibhav Gupta**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=AMiyLItEtLA) · [Conference site](https://www.ai.engineer/)

## Description

You cannot tell great engineers what to do, and you increasingly cannot tell what an agent did either, so Vaibhav Gupta's answer is to fight slop with slop. At Boundary the team turns the same cheap, sloppy generation loose as a tool: agents that run constantly over the transcripts of other agents, flagging hallucinations, spotting which tool calls produced errors, and comparing which approaches produced fewer. He pairs that with hard invariants, the design docs, rules, and CLI checks that do not change for months and tell you exactly where a codebase stops converging, so the messy detection layer sits on top of something stable.

The deeper move is to attack the foundational layer from first principles. Instead of trusting generated code, he leans on type systems that make whole classes of mistakes impossible: types get inferred without you writing them, a division by zero is guaranteed to be handled or the code will not build, and there are no silent unknowns left for an agent to guess at. That is the bet behind BAML, which lets you work across Python, TypeScript, or Rust with strong boundaries around each function so an agent can move fast inside walls it cannot breach. His closing challenge is to go build these sloppy tools yourself and constrain the systems underneath them, because that is what actually wins the war on slop.

Speaker info:
- https://x.com/vaibcode
- https://www.linkedin.com/in/vaigup
- https://www.youtube.com/@boundaryml

Timestamps:
0:00 - Fighting slop with slop
0:27 - Code reviews and invariants
2:08 - Building rules that don't change
3:00 - Design docs with notifications
4:03 - CLI tools that catch where things break
5:08 - Agents reading agent transcripts
5:57 - Detecting hallucinations and errors
9:24 - Attacking the foundational layer
11:03 - Execution traces from first principles
14:26 - Type safe tools across platforms
15:42 - Making whole error classes impossible
17:57 - BAML across languages
20:37 - Go build the sloppy tools
