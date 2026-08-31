---
id: 8ehQZx39OyE
title: "OWASP Agent MAS Threat Modeling"
slug: owasp-agent-mas-threat-modeling
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 18
published_at: 2026-01-13T00:48:36Z
video_id: 8ehQZx39OyE
youtube_url: https://www.youtube.com/watch?v=8ehQZx39OyE
tags: []
transcript: false
---

# OWASP Agent MAS Threat Modeling

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `18 min`

[Watch the recording](https://www.youtube.com/watch?v=8ehQZx39OyE) · [Conference site](https://genai.owasp.org/)

## Description

🧩🛡️ MAESTRO: Threat Modeling Multi-Agent Systems (Including MCP) Beyond STRIDE
This session from the OWASP GenAI Security Project Virtual Summit (October 2025) introduces MAESTRO—a threat modeling framework designed for agentic and multi-agent systems, where traditional methods (STRIDE, DREAD, PASTA, OCTAVE, LINDDUN) fall short. The speakers explain why agentic AI changes the game: non-determinism, autonomy + tool execution, cross-cloud trust boundaries, ephemeral/token-based identities, agent-to-agent delegation, and blast-radius amplification when one agent is compromised.

MAESTRO uses a seven-layer approach to map threats across an agent’s full stack, including:

Foundation model risk

Data operations (RAG/vector DB/memory; poisoning & leakage)

Agent frameworks (e.g., LangGraph/AutoGen/ClaudeAI)

Deployment infrastructure (Kubernetes/serverless)

Evaluation/observability (logs, monitoring, verifier integrity)

Security & compliance as a vertical layer

Agent ecosystem (marketplaces, discovery, impersonation, protocols like MCP/A2A/ACP)

They also demo an open-source tool that ingests your agent architecture description, generates diagrams, and produces layer-by-layer threat analysis. The second half dives into MCP-specific threat modeling, including transport-layer weaknesses and runtime tool-chain attacks (e.g., injected/poisoned MCP services). A concrete mitigation pattern is discussed: maintaining hash-based baselines for tool calls and enforcing micro-segmentation policy controls to detect and block suspicious tool invocation at runtime.

👉 Learn more about the OWASP GenAI Security Project:
