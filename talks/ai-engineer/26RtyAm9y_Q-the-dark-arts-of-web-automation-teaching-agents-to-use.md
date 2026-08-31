---
id: 26RtyAm9y_Q
title: "The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore"
slug: the-dark-arts-of-web-automation-teaching-agents-to-use
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Corey Gallon"]
channel: null
duration_min: 22
published_at: 2026-08-14T15:30:00Z
video_id: 26RtyAm9y_Q
youtube_url: https://www.youtube.com/watch?v=26RtyAm9y_Q
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans — Corey Gallon, Rexmore

**Corey Gallon**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=26RtyAm9y_Q) · [Conference site](https://www.ai.engineer/)

## Description

Preparing this talk got Corey Gallon a warning from OpenAI that his account faced a ban for cyber abuse with a web browser. The offending work was an agent clearing Cloudflare Turnstile, two image captchas, and finally reCAPTCHA v2 with no human in the loop. His premise fits on one slide: a browser driven through the Chrome DevTools Protocol is just a meat bag with a mouse, because the agent's clicks and keystrokes travel the same path inside Chrome that yours do. Chrome stamps every event as trusted or untrusted, which is why a synthetic JavaScript click that works fine in Outlook gets silently dropped by Amazon's add to cart button.

The method is a loop of sense, act, verify, climbed up a three rung ladder only as high as the page forces. A synthetic click first, then a real CDP input event, then a human mouse path with jitter and a deliberate overshoot. He argues for a CLI over an MCP server on speed rather than capability, citing a study where both cleared tasks about 83% of the time while MCP took 71 round trips and eight minutes against seven turns and under a minute. That gap decides the last fight, because reCAPTCHA rounds expire on a clock. His solution splits the work: deterministic code drives the whole challenge and rearms itself, and the agent is called in only to look at the grid and name the tiles. Everything demonstrated runs on infrastructure and accounts he owns.

Speaker info:
- https://x.com/coreygallon
- https://www.linkedin.com/in/coreygallon
- https://gallon.me
- https://github.com/captivus/chrome-agent

Timestamps:
0:00 - Threatened with a ban for preparing this talk
1:50 - The premise: a CDP browser is a meat bag with a mouse
2:43 - Why a CLI beats an MCP server
4:06 - The DevTools Protocol and the agent's digital senses
5:47 - The loop: sense, act, verify
6:38 - The three rung ladder
8:27 - Rung one: batch emails, and the web UI as a permissionless API
10:44 - Rung two: trusted clicks and the add to cart button
12:51 - Rung three: Cloudflare Turnstile
14:26 - Image captchas, drag puzzles, and human motion
16:36 - Final boss: reCAPTCHA v2, solver and operator
19:47 - The methodology is the takeaway
