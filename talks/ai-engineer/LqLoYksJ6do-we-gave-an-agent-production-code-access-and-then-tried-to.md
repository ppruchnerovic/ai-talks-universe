---
id: LqLoYksJ6do
title: "We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3"
slug: we-gave-an-agent-production-code-access-and-then-tried-to
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Moritz Johner"]
channel: null
duration_min: 22
published_at: 2026-07-20T17:17:53Z
video_id: LqLoYksJ6do
youtube_url: https://www.youtube.com/watch?v=LqLoYksJ6do
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# We Gave an Agent Production Code Access and Then Tried to Sleep at Night — Moritz Johner, Form3

**Moritz Johner**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=LqLoYksJ6do) · [Conference site](https://www.ai.engineer/)

## Description

A single PatchPilot PR that bumped a few dependencies changed 70,000 lines of code, and the whole problem hides somewhere in that diff. Moritz Johner's team at Form3 built the agent to patch CVEs across thousands of repositories, the backlog that never empties, and ran it in production. Then infosec asked the question that reframes the whole project: is this automation, or a supply chain incident waiting to happen? The moment a coding agent has the repository access, CI logs, credentials, and Docker socket it needs to be useful, it becomes a supply chain actor, whether you planned for that or not.

Their answer is architectural. PatchPilot splits in two: a boring deterministic Go layer that keeps the dangerous powers, GitHub write access and the ability to trigger CI, and an agent layer that only edits files on disk and hands control back. Where you draw that line is the actual security model, because it caps the blast radius when the agent gets prompt injected by one of the 70,000 lines it did not write. The Docker socket is the part that kept him up at night: hand it over so the agent can build and verify its own work, and a prompt injection can break out into a privileged container, so they moved the whole thing inside a firecracker microVM with its own kernel and a separate network policy for each layer.

Speaker info:
- https://www.linkedin.com/in/moritz-johner/
- https://github.com/moolen
- https://github.com/external-secrets/external-secrets
