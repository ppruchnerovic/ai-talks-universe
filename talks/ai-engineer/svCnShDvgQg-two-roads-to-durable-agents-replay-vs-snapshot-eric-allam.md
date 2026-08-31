---
id: svCnShDvgQg
title: "Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev"
slug: two-roads-to-durable-agents-replay-vs-snapshot-eric-allam
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Eric Allam"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-05-10T20:00:06Z
video_id: svCnShDvgQg
youtube_url: https://www.youtube.com/watch?v=svCnShDvgQg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Two Roads to Durable Agents: Replay vs. Snapshot — Eric Allam, CEO, Trigger.dev

**Eric Allam**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=svCnShDvgQg) · [Conference site](https://www.ai.engineer/)

## Description

Replay-based durability — wrapping every step in a journal, replaying on recovery, requiring deterministic code — is how everyone makes agents durable today. It works until it doesn't: the journal grows with every turn, the structure starts constraining how you write code, and an agent that needs to run for hours starts looking less like a transaction and more like a session.

This talk separates the problem in two: context durability (the append-only log of everything the LLM saw, which already fits in a database) and execution durability (the files, memory, and subprocesses that live in the compute layer, which don't). The answer to the second half isn't a smarter log — it's OS-level snapshot and restore. Eric Allam walks through how Trigger.dev built this on Firecracker microVMs, getting snapshots down to 14 megabytes compressed with sub-second save and hundred-millisecond restore times, and why IBM mainframes in 1966 got there first.

Speaker info:
- https://x.com/maverickdotdev
- https://www.linkedin.com/in/eric-allam/
- https://github.com/ericallam
