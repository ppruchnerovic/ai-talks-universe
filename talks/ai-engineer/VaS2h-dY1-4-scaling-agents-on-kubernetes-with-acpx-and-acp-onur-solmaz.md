---
id: VaS2h-dY1-4
title: "Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw"
slug: scaling-agents-on-kubernetes-with-acpx-and-acp-onur-solmaz
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Onur Solmaz"]
channel: null
duration_min: 19
published_at: 2026-05-21T15:00:06Z
video_id: VaS2h-dY1-4
youtube_url: https://www.youtube.com/watch?v=VaS2h-dY1-4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Scaling Agents on Kubernetes with acpx and ACP — Onur Solmaz, OpenClaw

**Onur Solmaz**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VaS2h-dY1-4) · [Conference site](https://www.ai.engineer/)

## Description

OpenClaw receives 300 to 500 pull requests per day. Most arrive AI generated, most are not mergeable, and every one of them is signal about something broken in the codebase. Onur Solmaz built acpx to process them without him in the loop.

acpx is a headless CLI for the Agent Client Protocol. It replaces PTY scraping with structured agent to client communication and drives sessions through a node based workflow graph: reproduce the bug, judge the implementation, check for conflicts, run a review loop, emit structured JSON. Onur runs parallel Codex sessions from Discord channels while traveling, one channel per task. The talk ends with disposable agent pods on Kubernetes, a Go operator that provisions a full compute environment per task, wires it into Slack, and tears it down when the work is done.

Speaker info:
- https://x.com/onusoz
- https://www.linkedin.com/in/osolmaz/
- https://github.com/osolmaz
