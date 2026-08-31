---
id: imFedndyXYQ
title: "Using LLMs to Secure Source Code — Eugene Yan, Anthropic"
slug: using-llms-to-secure-source-code-eugene-yan-anthropic
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Eugene Yan"]
channel: null
duration_min: 22
published_at: 2026-07-17T21:27:20Z
video_id: imFedndyXYQ
youtube_url: https://www.youtube.com/watch?v=imFedndyXYQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Using LLMs to Secure Source Code — Eugene Yan, Anthropic

**Eugene Yan**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=imFedndyXYQ) · [Conference site](https://www.ai.engineer/)

## Description

Mozilla shipped about 20 security fixes a month across Firefox in early 2025. In April it shipped 400, a 20x jump, and it credited roughly two thirds of them to a frontier model. That is the shift Eugene Yan came to describe: models are now finding and fixing real vulnerabilities at scale. Anthropic's own scan of more than a thousand open source repos surfaced 6,200 high or critical issues out of 23,000 candidates, reported 1,600 to maintainers, and saw about 100 patched upstream. Finding bugs, it turns out, is no longer the hard part. The bottleneck has moved to verifying, triaging, and patching them.

The talk walks a six step workflow through one running example: a five line order lookup with a SQL injection hiding in a Python string. The two setup steps are a threat model and a sandbox. A written threat model alone pushes the true positive rate to 90%, because a model has great context of the code but poor context of the system, all the design decisions that live only in someone's head. The four loop steps read like a machine learning pipeline: discovery optimizes for recall, then a separate verification agent, kept independent and adversarial so it never sees the discovery reasoning, optimizes for precision by detonating the exploit in a fresh container. Triage protects the scarcest resource, engineer attention, and patching closes the loop so the same bug cannot return. His parting advice: start this week on open source dependencies, keep your hands on the wheel before automating, and remember that scanning was never the bottleneck.

Speaker info:
- https://x.com/eugeneyan
- https://github.com/eugeneyan
- https://eugeneyan.com

Timestamps:
0:00 - Working with security teams to find and fix vulnerabilities
0:49 - Three trends in model security capability
1:16 - Cybersecurity benchmarks and the step jump in capability
1:54 - Mozilla's 20x jump in monthly security fixes
2:44 - Log4Shell, Heartbleed, and why this matters
3:22 - Anthropic's scan of a thousand open source repos
3:35 - The bottleneck shifts to verify, triage, and patch
3:48 - Why agentic harnesses changed the game
4:29 - The six step workflow
5:31 - A running example: the order service
5:45 - Step 1: the threat model and 90% true positives
7:42 - Step 2: the sandbox for isolation and reproducibility
9:24 - Step 3: discovery and the five line SQL injection
11:44 - Step 4: independent adversarial verification
13:36 - Step 5: triage and the scarcity of engineer attention
15:52 - Step 6: patching and closing the loop
17:19 - It all looks like a machine learning pipeline
17:43 - The non technical bottlenecks are harder
18:47 - Organizational bottlenecks: routing, severity, bandwidth
20:05 - Three takeaways and how to start this week

"The bottleneck has now shifted to verification, triage, and patching." (3:39)
"A model has great context of the code but poor context of the system." (6:06)
"Things that can be solved with money are not really problems. But human attention doesn't scale." (18:14)
"Scanning was never the bottleneck." (20:38)
