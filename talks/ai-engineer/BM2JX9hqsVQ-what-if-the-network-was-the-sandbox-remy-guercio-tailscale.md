---
id: BM2JX9hqsVQ
title: "What if the network was the sandbox? — Remy Guercio, Tailscale"
slug: what-if-the-network-was-the-sandbox-remy-guercio-tailscale
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Remy Guercio"]
channel: "AI Engineer"
duration_min: 24
published_at: 2026-06-01T15:00:31Z
video_id: BM2JX9hqsVQ
youtube_url: https://www.youtube.com/watch?v=BM2JX9hqsVQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# What if the network was the sandbox? — Remy Guercio, Tailscale

**Remy Guercio**

`AI Engineer` · `AI Engineer` · `2026` · `24 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=BM2JX9hqsVQ) · [Conference site](https://www.ai.engineer/)

## Description

Standard sandboxing puts the API key inside the sandbox. The agent has the key, which it can exfiltrate, misuse, or — if it runs long enough — find creative ways to leverage beyond its intended scope. Remy Guercio from Tailscale argues that sandboxing conflates two separate problems: execution isolation and access control. You can fully isolate a runtime and still have the agent holding credentials it can abuse.

Their answer is Aperture, an LLM gateway built on Tailscale's WireGuard identity network. Every connection carries verified identity — user, tag, or group — and the agent gets a placeholder instead of a real key. There is nothing to exfiltrate. Every LLM call has to pass through the network layer, so Aperture sees every tool call, bash command, and MCP request without instrumentation inside the container. Internally at Tailscale, bash dominates over structured tool calls — and now they can actually see that.

Speaker info:
- https://www.linkedin.com/in/remyguercio/

Timestamps:
0:00 - Introduction and the concept of a sandbox
1:15 - Breaking down the components of a sandbox (boundary and permissions)
1:52 - How permissions are typically handled (API keys vs. OIDC)
3:18 - Introducing Tailscale and WireGuard for network-level identity
5:42 - Introduction to Aperture (AI Gateway)
7:28 - Live demo: Viewing usage metrics and logs in Aperture
9:47 - Live demo: Inspecting GitHub Actions PR review bot logs
10:39 - Visibility into tool calls, bash commands, and MCP requests
11:46 - Agent setup and configuration in Aperture
13:59 - Advanced features: Cost controls, quotas, and webhooks
15:35 - Using tsnet to build custom internal identity-aware services
17:03 - Q&A: How to configure permissions (Grants vs. ACLs)
18:46 - Q&A: Network-layer transparency for base URLs
20:25 - Q&A: Permissioning based on users vs. model/provider
21:28 - Q&A: Handling non-tool call agent behaviors (direct code execution)
