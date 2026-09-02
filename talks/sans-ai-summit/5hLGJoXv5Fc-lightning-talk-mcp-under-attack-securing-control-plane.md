---
id: 5hLGJoXv5Fc
title: "Lightning Talk: MCP Under Attack: Securing Control Plane"
slug: lightning-talk-mcp-under-attack-securing-control-plane
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "AI security"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 6
published_at: 2026-05-04T19:34:45Z
video_id: 5hLGJoXv5Fc
url: https://www.youtube.com/watch?v=5hLGJoXv5Fc
youtube_url: https://www.youtube.com/watch?v=5hLGJoXv5Fc
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Lightning Talk: MCP Under Attack: Securing Control Plane

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `6 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=5hLGJoXv5Fc) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

MCP Under Attack: Securing the New Trusted Control Plane

🎙️ Yevhen Pervushyn, Founder & Security Researcher, Red Asgard
📍 Presented at SANS AI Cybersecurity Summit 2026

Problem: AI agents are standardizing """"USB-like"""" access to enterprise data via unauthenticated MCP servers.
Solution: A red-team methodology for """"Context Manipulation"""" that treats AI intent as a trusted input to privileged systems.
Next: Why the future of AI security is about control-flow integrity, not just content filtering.

Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

## Transcript

*577 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=0s)** In 2004, we handed every developer a web browser and said, "Ship it." Then then we spent about 10 years retrofitting security XSS CSRF, session hijacking. In 2025, we handed every developer and AI agent and said, "Ship it." But did we build a security policy first? No, of course not. That's insane to expect. Welcome to AI error. Model context protocol or MCP is not an AI feature.

**[0:50](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=50s)** It is standardized plumbing that allows AI agents to run tools, access enterprise data and execute code. MCP is not just a convenience, it is a privilege uh access control. When you deploy MCP server, you're creating uh you you're giving your model a terminal to the infrastructure. Every MCP server is a delegation of trust. Delegating trust without verification creates systemic risk. So the traditional trust boundaries has

**[1:41](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=101s)** just breaking In in traditional system in deterministic system we know that code owns the execution. We know we know this boundary what happens but in the agentic world we put the probabilistic decision system inside the path of the execution of the trustful execution. So the AI context now is the what uh supposed to execute things. So uh the DI just depends on the context and and here uh you know I I want to be uh really honest with you for a second.

**[2:30](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=150s)** Uh like six months ago I have deployed an MCP server for a client. the properation scope access everything seems to be fine and in about 3 weeks I sat down to review what's the system is actually doing I I had model output tool results but the like exact decision pain why why model chose these arguments in this order with this exact data is completely unlocked is gone.

**[3:22](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=202s)** So the model actually did nothing wrong. It did what the context has told it to do and I find nothing wrong. But from the other side, I couldn't prove that nothing went wrong. And you know that's not a success story. That's an attack surface. We've been seeing lots of privilege escalations through the AI mediated surface AI mediated execution AI path. Now the privilege path and if

**[4:12](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=252s)** uh if if the tools uh contracts are weak, we the the attacker can use the AI surface just to uh get get out of the box uh from the scope to the broader system impact. just imple influencing the arguments that model chooses to run the tools and most of companies are trying to secure the AI security uh just implementing the content filtering like stopping the bad words from coming in or bad words coming

**[5:00](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=300s)** out but in the agentic world content filtering The second defense the the real challenge is the control flow integrity and this is a private the authorization is greater than interpretation. Uh AI agents can suggest actions they just cannot redefine what is pro proper to do what is what what they can do. So if you deploy the MCP server today, uh here are two hardening moves. So first externalize your policy. Make sure that agents are not uh like listening to the instructions. You you need to have the policy executor which is running outside of LM context and restricts your schemas and and full logging is just to

**[5:51](https://www.youtube.com/watch?v=5hLGJoXv5Fc&t=351s)** be without that you cannot investigate the abuse. Scan this QR code and you will get the everything you need to for for for an implementation.
