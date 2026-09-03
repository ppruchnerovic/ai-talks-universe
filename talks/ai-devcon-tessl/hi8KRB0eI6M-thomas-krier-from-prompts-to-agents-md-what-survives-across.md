---
id: hi8KRB0eI6M
title: "Thomas Krier - From Prompts to AGENTS.md: What Survives Across Thousands of Runs | DevCon Fall 2025"
slug: thomas-krier-from-prompts-to-agents-md-what-survives-across
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2025
speakers: ["Thomas Krier"]
channel: "AI Native Dev"
duration_min: 24
published_at: 2025-11-27T22:19:49Z
video_id: hi8KRB0eI6M
url: https://www.youtube.com/watch?v=hi8KRB0eI6M
youtube_url: https://www.youtube.com/watch?v=hi8KRB0eI6M
tags: ["ainativedev"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Prompting & context engineering"]
transcript: false
---

# Thomas Krier - From Prompts to AGENTS.md: What Survives Across Thousands of Runs | DevCon Fall 2025

**Thomas Krier**

`AI DevCon (Tessl)` · `Tessl` · `2025` · `24 min`

`#ainativedev`

[Watch the recording](https://www.youtube.com/watch?v=hi8KRB0eI6M) · [Conference site](https://tessl.io/devcon/)

## Description

We stress‑test coding agents Claude Code and codex at scale and report the patterns that actually survive. Across thousands of runs on a representative golden set of agentic coding issues, we compare orchestration (single vs. parallel vs. lightweight hierarchy), reasoning styles (ReAct, Reflexion, Self‑Refine, Least‑to‑Most), and context practices (refresh, compaction, dedup). The core move is turning ephemeral prompt tweaks into durable, versioned central and per-component AGENTS.md so improvements persist across repos and projects. We’ll augment this with a GitHub study of AGENTS.md in popular projects (adoption, typical sections, section sizes), then show how we applied the findings to Claude Code and Codex to stabilize outcomes under load. Attendees leave with defaults that improved speed, cost, size, and performance and a template you can adopt immediately.

20‑minute run‑of‑show
- 2’ Why results drift and why rules beat one‑off prompts
- 4’ Orchestration ladders and reasoning styles (what held up at scale)
- 5’ AGENTS.md in practice, central vs. distributed, ordering, decision criteria
- 5’ Context engineering that sticks and trace‑driven updates
- 4’ “In the wild” snapshot (GitHub stats) and quickstart templates

Top‑3 takeaways
1. A reproducible template to convert traces into AGENTS.md rules that survive across runs.
2. When to use parallel runs vs. light hierarchy and how to stage reflection without ballooning tokens.
3. Context defaults that reduce cost and latency without cratering quality.

You can also find Thomas' comments on his presentation in this piece: https://ainativedev.io/news/from-prompts-to-agents-md-what-survives-across-thousands-of-runs

🎙️ AI DevCon is back in New York on November 2 to 4! Dev talks on harness engineering, agent enablement, software factories, and scaling AI-native development. Join the sessions online or use code YT15 to book your seat at https://tessl.co/5re

🌐 Try Tessl - we help you build a software factory, one step at a time: https://tessl.co/ddd
🔔 Subscribe for weekly episodes on AI-native development
