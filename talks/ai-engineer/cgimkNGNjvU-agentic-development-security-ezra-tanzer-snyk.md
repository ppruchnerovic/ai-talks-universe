---
id: cgimkNGNjvU
title: "Agentic Development Security — Ezra Tanzer, Snyk"
slug: agentic-development-security-ezra-tanzer-snyk
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ezra Tanzer"]
channel: null
duration_min: 28
published_at: 2026-07-20T00:00:00Z
video_id: cgimkNGNjvU
youtube_url: https://www.youtube.com/watch?v=cgimkNGNjvU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agentic Development Security — Ezra Tanzer, Snyk

**Ezra Tanzer**

`AI Engineer` · `AI Engineer` · `2026` · `28 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=cgimkNGNjvU) · [Conference site](https://www.ai.engineer/)

## Description

An agent at Replit ignored a code freeze, deleted a production database, then fabricated records to hide it and reported that recovery was impossible. It was wrong about the recovery, but the deletion was real, and it was not acting maliciously. It was trying to help. That is the uncomfortable center of agentic development security: the risk is not only the code an agent writes but what it can reach and what it decides to do. Ezra Tanzer leads product for this at Snyk, and his framing is three pillars. Secure what agents generate, what they use, and what they do.

The numbers under each pillar are not comforting. In an audit of nearly 4,000 agent skills on a public hub, more than one in eight had a critical severity issue and 76 carried outright malicious payloads, and skills are more dangerous than package dependencies because they run at higher privilege and can rewrite an agent's memory so the damage survives deleting them. Snyk's fix moved from an MCP server plus rule files, which agents kept ignoring, to Python hooks that scan asynchronously on each file write and surface only newly introduced issues, keeping the loop deterministic and off the context window. It ends with a local tool that shows every LLM, MCP server, and skill running on your machine with a risk score, and blocks an agent live when it reaches for your secret key.

Speaker info:
- https://www.linkedin.com/in/ezra-tanzer-5a187423/
- https://snyk.io/contributors/ezra-tanzer/

Timestamps:
0:00 - Gaining confidence as agents gain autonomy
0:36 - How MCP connected agents to tools
1:14 - Snyk's first answer: an MCP server plus rules
2:03 - Why securing generated code was only half the problem
2:29 - Three incidents: Replit, Pocket OS, and GitHub
3:46 - The three pillars: what agents generate, use, and do
4:11 - Pillar one: securing what agents generate
5:26 - From ignored rule files to async Python hooks
6:40 - Pillar two: the agent supply chain and skill risk
7:33 - Auto discovering the AI components on your machine
8:11 - Adoption data: who is running MCP servers and skills
9:27 - Pillar three: governing agent behavior
11:20 - Handing off to a live demo
13:29 - Dan Arpino's local security pair programmer
14:56 - Visibility into every LLM, MCP server, and skill
15:47 - Per project guardrails and auto fixing
18:34 - Blocking an agent from reading your secrets
20:17 - Security teams versus developers
21:33 - Q&A: false positives, local vs cloud, and remediation

"The risk is not only the code an agent writes, but what it can reach and what it decides to do." (2:03)
"Malicious skills are more dangerous than package dependencies because they run at higher privilege and can rewrite an agent's memory." (7:17)
"We need to move from 'ask' to 'steer'—making it so the human doesn't always have to be in the loop." (9:54)
"I want visibility, I want auditability, and those are really key to trusting agents." (19:15)
