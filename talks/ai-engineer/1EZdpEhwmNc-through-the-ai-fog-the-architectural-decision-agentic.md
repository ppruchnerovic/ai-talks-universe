---
id: 1EZdpEhwmNc
title: "Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk"
slug: through-the-ai-fog-the-architectural-decision-agentic
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Manoj Nair"]
channel: null
duration_min: 23
published_at: 2026-07-20T17:17:54Z
video_id: 1EZdpEhwmNc
youtube_url: https://www.youtube.com/watch?v=1EZdpEhwmNc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Through the AI Fog: The Architectural Decision Agentic Security Depends On — Manoj Nair, Snyk

**Manoj Nair**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=1EZdpEhwmNc) · [Conference site](https://www.ai.engineer/)

## Description

Ask the latest frontier models, the ones not even public yet, to find the same vulnerability five times, and only half of those runs catch it. Against a plain deterministic checker they found at most 75% of the issues, a 40% F1 score. That number sits underneath the whole talk: the generator and the validator cannot be the same system. Manoj Nair leads the team securing roughly 5,000 enterprises at Snyk, half of the Fortune 500, and the data he brought is not comforting. Across 4,800 customers, security backlog grew 108% quarter over quarter, because agents writing code faster are also manufacturing vulnerabilities faster than anyone closes them.

The new attack surface is not hypothetical. More than a third of the agent skills researchers studied carry malware or hostile instructions, three lines of English that can take a system down, and MCP servers wire agents into enterprise data with almost no security built in. In one Fortune 100 environment an agent quietly copied PII into an untrusted database it had spun up, just in case it needed the data later. Under Snyk's own red team attacks one hot new model gave up PII 100% of the time while a frontier model held at zero, which is the whole point: you cannot trust one probabilistic system to police another, and which model is safe shifts week to week. The answer is not a better model but a deterministic layer that keeps verifying what the agents ship, inside the loop where they work.

Speaker info:
- https://www.linkedin.com/in/mnair1
- https://labs.snyk.io/contributors/manoj-nair/

Timestamps:
0:00 - Welcome to the first AI security track
1:46 - Manoj takes the stage: securing 5,000 enterprises
3:07 - The core question: can the generator also be the validator?
4:25 - Autonomous attacks and the attacker that never sleeps
5:43 - Why AI generated code makes old problems worse
7:02 - Real data: 108% more security backlog, quarter over quarter
8:04 - The Five Eyes warning and chained exploits
8:34 - Toxic skills and poisoned environments
9:27 - MCP servers and the GitHub MCP exploit
9:53 - When an agent squirrels away your PII
10:34 - You can't govern what you can't see
11:16 - Red team data: which models leak PII
12:08 - The generator vs validator benchmark
13:38 - What Snyk built: prevention and Snyk Studio
14:20 - Remediation at scale: 16,000 critical issues
15:37 - Live demo: package health in the coding loop
19:03 - Live demo: assessing a risky agent skill
21:02 - Building EVO with the AI security community
