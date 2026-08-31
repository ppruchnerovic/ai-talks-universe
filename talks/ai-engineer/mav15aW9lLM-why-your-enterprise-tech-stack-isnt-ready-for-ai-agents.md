---
id: mav15aW9lLM
title: "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard"
slug: why-your-enterprise-tech-stack-isnt-ready-for-ai-agents
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 19
published_at: 2026-08-19T18:30:15Z
video_id: mav15aW9lLM
youtube_url: https://www.youtube.com/watch?v=mav15aW9lLM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Your Enterprise Tech Stack Isn’t Ready for AI Agents — Christopher Lovejoy & Saul Howard

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=mav15aW9lLM) · [Conference site](https://www.ai.engineer/)

## Description

The proof of concept works. It hits the accuracy targets, it is fast, it is cheap, and the room is happy. Then someone from compliance raises a hand and asks to see the audit trail, and the whole thing stops. Christopher Lovejoy and Saul Howard have watched that meeting happen repeatedly, and their point is that an audit trail is not a developer log. Under the frameworks enterprises actually answer to, it is a complete record of every action an agent took, every place it touched data, and the authorization behind each one, durable enough to stand up as a chain of evidence if the decision were ever examined in court.

Their answer is to take the constraints seriously first and rebuild toward the accuracy afterwards, rather than bolting requirements onto a demo. An immutable append only event log makes auditability fall out of the storage model instead of being reconstructed later, at the cost of harder reads. Patient data lives in schema driven object storage alongside that log rather than inside it, so the events hold only references, which lets engineers debug what an agent did without being exposed to the health data itself, and gives a natural place to enforce zero trust and constrain prompt injection. Escalation works because humans and models are both treated as agents, so any action either can take, the other can take too. Evaluation then emerges from those three primitives rather than being attached to the side, including on production data that never leaves the customer's environment.

Speaker info:
- https://x.com/ChrisLovejoy_
- https://www.chrislovejoy.me
- https://x.com/saulhoward
- https://linkedin.com/in/saulhoward

Timestamps:
0:00 - Why healthcare is hard, and what transfers to other regulated work
1:57 - The enterprise proof of concept
2:49 - What the buildout actually connects to
3:39 - Everyone assumes the hard part is done
4:28 - The questions that arrive the next day
5:19 - An audit trail is not a developer log
7:03 - The immutable event log, and its tradeoff
8:46 - What shape healthcare data actually has
10:28 - Object storage beside the log, not inside it
11:20 - Debugging an agent without seeing the data
12:15 - Zero trust and the lethal trifecta
13:07 - Escalation when you cannot predict it
13:58 - Treating humans and models as the same kind of agent
14:49 - Why evals are hard here
15:39 - Evaluation as a byproduct of the primitives
17:20 - Architecture as choosing what stays simple
18:08 - Where it goes wrong, and where it goes right
