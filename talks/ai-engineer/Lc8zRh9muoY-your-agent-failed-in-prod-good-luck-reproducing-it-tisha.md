---
id: Lc8zRh9muoY
title: "Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft"
slug: your-agent-failed-in-prod-good-luck-reproducing-it-tisha
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 14
published_at: 2026-06-29T00:00:39Z
video_id: Lc8zRh9muoY
youtube_url: https://www.youtube.com/watch?v=Lc8zRh9muoY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your Agent Failed in Prod. Good Luck Reproducing It. - Tisha Chawla & Susheem Koul, Microsoft

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Lc8zRh9muoY) · [Conference site](https://www.ai.engineer/)

## Description

When an autonomous agent fails in production and corrupts an enterprise data record, it rarely repeats the exact same execution trajectory twice. Standard application logs reveal what broke but completely fail to explain why, leaving platform teams unable to reproduce non-deterministic failures on demand. While durable execution engines excel at keeping an agent loop alive through state recovery, durability is fundamentally distinct from debuggability. State recovery reconstructs the present; it does not allow an engineer to re-enter the precise historical run that caused an erratic state mutation.

This session introduces the record and replay pattern for autonomous workflows, bringing the core engineering philosophy behind low level systems tools like Mozilla rr straight into the agent loop. By capturing every model invocation, tool execution payload, memory boundary read, and intermediate state transition into an append only event log, engineers can deterministically replay a failed execution trace for true postmortem root cause analysis. This architectural pattern moves entirely beyond basic API mocking or simple response caching. Attendees will leave this session knowing how to architect a framework agnostic recording layer, identify the exact state mutations required to guarantee replay determinism, understand where this approach complements durable execution architectures, and learn how to transform an unreproducible production anomaly into an execution path they can step through line by line.

Speakers:
- Tisha Chawla (Microsoft): Tisha Chawla is a Software Engineer at Microsoft working within the Commerce and Ecosystem Data Platform team, where she builds agentic systems designed to hold up against real production data. Her technical work spans core internal platform initiatives across Spec Driven Development, SRE Agent adoption, and enterprise SWE Agents, focusing on deterministic execution frameworks and agentic software development lifecycles. Alongside her infrastructure work, Tisha is a published researcher with peer reviewed papers in applied machine learning at venues including APNET SIGCOMM and ASONAM. She frequently delivers technical sessions to large engineering audiences across Microsoft, sharing high signal insights on deploying durable, production grade agentic workflows.
- Susheem Koul (Microsoft): ​Susheem Koul is a Software Engineer at Microsoft with over 7 years of experience in product development. Currently, his work is focused on the design and implementation of intelligent, agentic systems. Beyond his professional focus on agentic workflows and multi-agent coordination, he explores the philosophy of learning and software architecture through his Substack
