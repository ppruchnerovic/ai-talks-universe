---
id: GqoNrUz8hEU
title: "Bringing agents onto the world wide web — Paul Klein IV, Browserbase"
slug: bringing-agents-onto-the-world-wide-web-paul-klein-iv
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-08-14T00:00:00Z
video_id: GqoNrUz8hEU
youtube_url: https://www.youtube.com/watch?v=GqoNrUz8hEU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Bringing agents onto the world wide web — Paul Klein IV, Browserbase

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=GqoNrUz8hEU) · [Conference site](https://www.ai.engineer/)

## Description

When OpenClaw shipped, people started buying Mac minis to run it from home, SSHing in and clearing captchas off a residential IP. Paul Klein IV points out he has yet to see a SOC 2 compliant Mac Mini setup at scale, and that this felt like a reasonable answer is itself the problem. His argument is that browser agents are no longer held back by the models. The capability is already there and the engineering around it is missing, which makes the overhang something any team can close rather than wait on a lab for.

That engineering has three parts. The most reliable browser agents in production are multimodal and write code alongside clicking, often intercepting network requests and replaying them rather than driving pixels. They carry a real harness, with skills and memory so a site is not rediscovered every run, and with page context compressed rather than dumped whole into the model. And they sit on infrastructure that renders a page identically every time, since a layout that comes back mobile on one run and desktop on the next produces results the agent cannot account for. He then turns to what the web owes agents: accessibility trees, Chrome's new Web MCP, and two unsolved problems, how an agent logs in on your behalf and who certifies that an agent can be trusted. The payoff is not in San Francisco. It is the logistics company in Singapore, the bank in South Africa, and the lumber factory in Mexico, all running on PHP forms with people clicking buttons every day.

Speaker info:
- https://x.com/pk_iv
- https://www.linkedin.com/in/paulkleiniv/
- https://github.com/browserbase/stagehand

Timestamps:
0:00 - Why web agents have not happened yet, and is it the models
3:17 - The missing piece is the harness
4:32 - Harnesses that beat the baseline model
6:01 - The capabilities overhang in computer use
7:05 - Multimodal agents, skills, and token efficiency
9:09 - Infrastructure, and the SOC 2 Mac Mini problem
10:24 - What the web owes agents: accessibility and Web MCP
11:40 - Authentication, trust, and who issues the certificate
14:07 - What a real platform has to provide
15:45 - The real economy runs on PHP forms
