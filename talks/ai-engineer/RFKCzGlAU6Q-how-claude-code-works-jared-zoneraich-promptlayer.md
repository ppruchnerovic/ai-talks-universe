---
id: RFKCzGlAU6Q
title: "How Claude Code Works - Jared Zoneraich, PromptLayer"
slug: how-claude-code-works-jared-zoneraich-promptlayer
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2025
speakers: ["Jared Zoneraich"]
channel: "AI Engineer"
duration_min: 66
published_at: 2025-12-26T22:04:34Z
video_id: RFKCzGlAU6Q
url: https://www.youtube.com/watch?v=RFKCzGlAU6Q
youtube_url: https://www.youtube.com/watch?v=RFKCzGlAU6Q
tags: []
topics: ["Agents & orchestration", "Coding assistants & agents", "Enterprise adoption & strategy", "Evals, observability & reliability", "Prompting & context engineering"]
transcript: false
---

# How Claude Code Works - Jared Zoneraich, PromptLayer

**Jared Zoneraich**

`AI Engineer` · `AI Engineer` · `2025` · `66 min`

[Watch the recording](https://www.youtube.com/watch?v=RFKCzGlAU6Q) · [Conference site](https://www.ai.engineer/)

## Description

Deep dive into what we have independently figured out about the architecture and implementation of Claude's code generation capabilities. Not officially endorsed by Anthropic.

Speaker: Jared Zoneraich  |  Founder & CEO, PromptLayer

Jared Zoneraich from PromptLayer dissects the architecture of "Claude Code" (Anthropic's CLI agent), arguing that its success stems not from complex agentic frameworks but from a radical simplification: a single-threaded "Master Loop" paired with highly capable models. He contrasts this "give it tools and get out of the way" approach with earlier, brittle DAG-based (Directed Acyclic Graph) architectures. The talk breaks down the specific internal tools (Bash, FileEdit, Grep), the "Todo" planning mechanism, and the critical role of sandboxing and system prompts in making the agent reliable for production engineering tasks.

**Timestamps:**

00:00 Introduction to Claude Code & AI Coding Agents
04:35 The Evolution and Breakthroughs of Coding Agents
07:54 Core Philosophy: Simple Architecture & Better Models
12:11 Key Tools and Their Functionality in Claude Code
15:52 The Power of Bash and Implementation of To-Do Lists
19:25 Structure of To-Do Lists vs. Complex DAGs
23:24 Relying on the Model & Importance of Sandboxing
27:23 Sandboxing, Sub-Agents, and System Prompts
31:55 System Prompts and the Use of "Skills"
36:05 Challenges with Skills & Future Innovations
39:21 Alternative Architectures: The "AI Therapist" Problem
42:14 Perspectives on Different Agents: Codex vs. Amp
45:03 Context Management in Amp & Cursor
48:42 Evaluating Coding Agents & Rigorous Tools
52:01 Testing Tools & Future of Headless SDKs
55:11 Key Takeaways & Building the Slide Deck with Claude Code
57:25 Discussion on DAGs and Sequential Execution
01:00:15 The Future of LLM Calls and Spec-Driven Development
