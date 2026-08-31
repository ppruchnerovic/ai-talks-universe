---
id: XsvUhpnHepE
title: "The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs"
slug: the-missing-layer-in-agentic-ai-giedrius-steimantas-oxylabs
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 15
published_at: 2026-08-26T07:00:06Z
video_id: XsvUhpnHepE
youtube_url: https://www.youtube.com/watch?v=XsvUhpnHepE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XsvUhpnHepE) · [Conference site](https://www.ai.engineer/)

## Description

Point an agent at ten product pages, get real content back from three, and send all ten to the model anyway: seventy percent of those tokens go to reading CAPTCHAs. Giedrius Šteimantas says most teams never notice, because the status code and the response size both look fine. A 200 does not mean the page is real. He got here through a friend who vibe coded a personal shopping agent, a chatbot that talks through your style then hands a second agent prompts to go buy things. It ran a browser automation framework at every stage, which made it slow, expensive, and unreliable enough not to work. The gap was not model quality. It was the layer underneath that lets an agent work on the open web.

He rebuilds it on stage using rules from ten years of scraping at Oxylabs: cost matters, and use a browser only when you have to. Discovery drops the fixed retailer list for a search API returning compact JSON, under 2,000 tokens and about 700 milliseconds per call, so the agent fans out queries and picks its own URLs. The decision stage loses the browser for a scraper that returns markdown, fails loudly with an explicit error when blocked instead of passing a CAPTCHA to the model, runs hundreds of requests in parallel, and bills only for successful results. Checkout does need a browser, so Playwright MCP stays and a hardened headless browser slots in behind it, bringing stealth, a residential proxy, and geolocation that stops items showing in stock and vanishing at the till.

Speaker info:
- https://www.linkedin.com/in/steimantas
- https://oxylabs.io

Timestamps:
0:00 - A friend's personal shopping agent that did not work
2:32 - Ten years of scraping, and one rule: cost matters
5:09 - Discovery on a browser, and what it costs
6:50 - A search API instead: 2,000 tokens, 700 milliseconds
8:35 - The blocked pages you still pay tokens for
10:29 - Rebuilding the decision stage without a browser
12:14 - Checkout is where you actually need a browser
14:00 - Validate before you spend tokens
