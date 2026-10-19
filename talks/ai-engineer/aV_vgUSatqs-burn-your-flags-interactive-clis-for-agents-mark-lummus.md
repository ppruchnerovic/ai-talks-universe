---
id: aV_vgUSatqs
title: "Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal"
slug: burn-your-flags-interactive-clis-for-agents-mark-lummus
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Mark Lummus", "Navinkumar Patil"]
channel: "AI Engineer"
duration_min: 54
published_at: 2026-10-11T20:30:04Z
video_id: aV_vgUSatqs
url: https://www.youtube.com/watch?v=aV_vgUSatqs
youtube_url: https://www.youtube.com/watch?v=aV_vgUSatqs
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Prompting & context engineering"]
transcript: false
---

# Burn Your Flags: Interactive CLIs for Agents — Mark Lummus & Navinkumar Patil, PayPal

**Mark Lummus, Navinkumar Patil**

`AI Engineer` · `AI Engineer` · `2026` · `54 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=aV_vgUSatqs) · [Conference site](https://www.ai.engineer/)

## Description

An agent can miss an interactive terminal prompt without producing an error. The human sees a question and arrow key options; the agent sees a redraw loop and loses the interface state. PayPal's Mark Lummus and Navinkumar Patil use that failure to challenge the standard fix of adding more command flags. Flags work when inputs are independent and the path is known in advance. They become awkward when later questions depend on earlier answers or live API responses. Interactive workflows already contain guidance, choices and guardrails that an agent should be able to follow.

The workshop puts that idea into practice with Barista 9000, a coffee ordering CLI that participants adapt for an agent, with a leaderboard and a Mac Mini prize. Patil introduces three approaches: tmux sessions for sending keys and capturing terminal state, IPC side channels that expose structured JSON instead of screen scraping, and context injection that makes options and constraints explicit. Lummus also asks participants to try less expensive models rather than brute force the task with maximum reasoning. Audience solutions push the benchmark toward deterministic parsers and very low response latency, prompting a discussion of what the competition actually rewards. The closing lesson is to keep the CLI predictable while giving the agent enough context and access to navigate its decisions.

Speaker info:
Mark Lummus:
- https://www.linkedin.com/in/marklummus
Navinkumar Patil:
- https://www.linkedin.com/in/navinpatil

Timestamps:
0:00 - Introduction and the interactive CLI challenge
2:29 - Why agents silently miss terminal prompts
4:35 - Where command flags stop working
5:19 - Agents, scripts and accessibility
6:32 - Barista 9000 and the workshop competition
8:01 - Navinkumar Patil on the return of CLIs
10:33 - Getting the CLI and registering a coffee order
16:10 - Model choice and the token budget
25:51 - Hint one: tmux sessions and terminal state
28:28 - Hint two: IPC side channels and JSON
31:35 - Hint three: context injection
35:10 - Scoring accuracy and response time
39:52 - Audience solutions and benchmark limitations
41:36 - Keeping the CLI deterministic
47:30 - Winning solution and an agent built solver
49:16 - A participant's first CLI
51:53 - Context, side channels and tmux

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---
