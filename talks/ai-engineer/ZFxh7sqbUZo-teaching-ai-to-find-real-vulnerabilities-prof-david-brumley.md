---
id: ZFxh7sqbUZo
title: "Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd"
slug: teaching-ai-to-find-real-vulnerabilities-prof-david-brumley
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Prof. David Brumley"]
channel: "AI Engineer"
duration_min: 27
published_at: 2026-08-01T00:30:06Z
video_id: ZFxh7sqbUZo
youtube_url: https://www.youtube.com/watch?v=ZFxh7sqbUZo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Teaching AI to Find Real Vulnerabilities — Prof. David Brumley, Bugcrowd

**Prof. David Brumley**

`AI Engineer` · `AI Engineer` · `2026` · `27 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ZFxh7sqbUZo) · [Conference site](https://www.ai.engineer/)

## Description

David Brumley has spent two decades turning people into hackers, from founding picoCTF to recruiting pwn2own winners at Carnegie Mellon, and his argument is that you teach a model to hack the same way: a ladder of tasks that climbs from triggering a crash to reading and writing arbitrary memory to a full working exploit. The catch is measurement. Hacking has no single answer, so the usual benchmark setup breaks down when a target has multiple vulnerabilities and a language model can always claim it found one, and grading oracles that just ask the model whether it succeeded are hopeless.

So Brumley's team builds real reinforcement learning environments instead: reproducible, sandboxed, and scored by deterministic graders that check whether an exploit actually triggers the specific bug, borrowing precision and recall from his DARPA Cyber Challenge work where he designed the scoring. He shows it on V8, the JavaScript engine in Chrome, running against 41 real vulnerabilities where the strongest models reached about 95% and, in the hard cases, produced genuine out of sandbox exploits including a real zero day. The point that lands is a warning against benchmaxxing security: build environments grounded in real bugs and honest graders, because that is what separates a model that looks like it can hack from one that actually can.

Speaker info:
- https://www.linkedin.com/in/thedavidbrumley

Timestamps:
0:00 - Two decades of teaching hacking
1:54 - From CTF scoreboards to CMU
3:34 - A ladder of exploitation tasks
6:44 - Why measuring hacking is hard
7:46 - Flawed grading oracles
10:30 - When a target has many bugs
13:22 - Deterministic graders and AIXCC scoring
14:49 - Precision and recall for vulnerabilities
17:35 - Attacking V8 in Chrome
21:10 - 41 vulnerabilities and a real zero day
25:24 - Don't benchmaxx security
