---
id: ZB7l4uxW3Yo
title: "Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson"
slug: breaking-the-chain-agent-continuations-for-resumable-ai
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Greg Benson"]
channel: "AI Engineer"
duration_min: 27
published_at: 2025-06-03T00:00:00Z
video_id: ZB7l4uxW3Yo
youtube_url: https://www.youtube.com/watch?v=ZB7l4uxW3Yo
tags: []
transcript: false
---

# Breaking the Chain: Agent Continuations for Resumable AI Workflows - Greg Benson

**Greg Benson**

`AI Engineer` · `AI Engineer` · `2025` · `27 min`

[Watch the recording](https://www.youtube.com/watch?v=ZB7l4uxW3Yo) · [Conference site](https://www.ai.engineer/)

## Description

AI agents are powerful—but brittle. Once an agent chain starts, you either let it run or you tear it down and lose state. Agent Continuations change that contract. Borrowing from programming‑language continuations, we capture an agent’s entire call stack—tools, goals, partial responses—in a compact JSON blob combined with the familiar messages array. The result is a protocol‑level "Agent State" that lets you:

- Pause anytime for human-in-the-loop approval gates, rate‑limit resets, or progressive UI updates.

- Migrate agents across nodes, clouds, even different agent execution platforms

- Checkpoint long‑running multi‑agent plans using off‑the‑shelf storage and enable restarting in the presence of agent failure

- Resume seamlessly through standard LLM function‑calling APIs, so every framework that speaks OpenAI JSON can speak continuations.

Our approach works with single-level agent loops and multi-level agents in which agents can call subagents.

Attendees will leave with open‑source Python snippets and a mental model that turns “monolithic” agents into restart‑able, human‑aware services—shrinking failure windows and unlocking new UX patterns for AI products.

**Key Takeaways**

- Why Continuations are a good construct for Agent State
- Protocol spec and reference JSON examples and a - Python implementation
Live demo: suspend a three‑layer agent with suspending for human approval

** Links **
