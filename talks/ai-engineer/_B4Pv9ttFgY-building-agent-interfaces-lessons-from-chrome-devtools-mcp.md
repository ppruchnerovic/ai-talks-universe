---
id: _B4Pv9ttFgY
title: "Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google"
slug: building-agent-interfaces-lessons-from-chrome-devtools-mcp
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Michael Hablich"]
channel: null
duration_min: 23
published_at: 2026-06-05T00:00:00Z
video_id: _B4Pv9ttFgY
youtube_url: https://www.youtube.com/watch?v=_B4Pv9ttFgY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Building Agent Interfaces: Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google

**Michael Hablich**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=_B4Pv9ttFgY) · [Conference site](https://www.ai.engineer/)

## Description

Chrome DevTools MCP shipped with one tool: debug_webpage. Agents failed silently because they couldn't compose behaviors. The team decomposed it into 25 focused tools and assumed the problem was solved. It wasn't — now agents had 25 tools and no reliable way to pick the right one. Michael Hablich's talk is an honest account of building the same thing wrong three times and what the fixes actually looked like.

The concrete lessons: semantic summaries instead of raw 50,000 line JSON trace files, error messages rewritten so agents can self heal without a human in the loop ("Cannot navigate back, no previous page in history" instead of "Unable to navigate back in currently selected page"), a metric called tokens per successful outcome to measure interface fuel efficiency, and a deliberate decision to keep the autoconnect friction rather than remove it once they thought through prompt injection and the lethal trifecta.

Speaker info:
- https://x.com/MHablich
- https://www.linkedin.com/in/michael-hablich/
