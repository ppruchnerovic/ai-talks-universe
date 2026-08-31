---
id: ghJmWQCIHRM
title: "The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google"
slug: the-agent-ready-web-simplify-user-actions-with-webmcp-tara
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Tara Agyemang"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-06-11T16:00:06Z
video_id: ghJmWQCIHRM
youtube_url: https://www.youtube.com/watch?v=ghJmWQCIHRM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google

**Tara Agyemang**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ghJmWQCIHRM) · [Conference site](https://www.ai.engineer/)

## Description

Buying two concert tickets costs an AI agent the entire DOM, the accessibility tree, a screenshot, pixel coordinate math, and then a click that might miss because an ad just loaded and shifted the layout. Tara Agyemang from the Google Chrome team introduces WebMCP, a proposed web standard that replaces that process with structured tools: instead of guessing what your site does, agents get a menu of named, typed, described actions they can call directly.

The talk covers two implementation paths. The declarative API adds a few HTML attributes to existing forms and the browser generates the JSON schema automatically. The imperative API lets you register custom tools in JavaScript for complex multi step flows, with an execute block that runs normal DOM code and returns state back to the agent. The live demo completes a concert ticket purchase in three tool calls: search by name, open the concert page, call purchase with quantity and section. Still experimental and in early preview on Chrome 146, but an eval CLI and inspector extension are available now for testing your own sites.

Speaker info:
- https://x.com/tara_ojo
- https://uk.linkedin.com/in/taraojo
- https://github.com/taraojo
