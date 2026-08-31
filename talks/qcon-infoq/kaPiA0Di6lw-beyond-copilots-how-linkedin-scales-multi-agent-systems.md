---
id: kaPiA0Di6lw
title: "Beyond Copilots: How LinkedIn Scales Multi-Agent Systems"
slug: beyond-copilots-how-linkedin-scales-multi-agent-systems
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: null
duration_min: 50
published_at: 2026-01-22T12:18:32Z
video_id: kaPiA0Di6lw
youtube_url: https://www.youtube.com/watch?v=kaPiA0Di6lw
tags: ["QCon London", "Case Study", "LinkedIn", "AI Agents", "Artificial Intelligence", "LLMs", "LLMOps", "Software Architecture", "LinkedIn Engineering", "Hiring Assistent", "InfoQ", "Transcript"]
transcript: false
---

# Beyond Copilots: How LinkedIn Scales Multi-Agent Systems

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `50 min`

`#QCon London` `#Case Study` `#LinkedIn` `#AI Agents` `#Artificial Intelligence` `#LLMs` `#LLMOps` `#Software Architecture` `#LinkedIn Engineering` `#Hiring Assistent` `#InfoQ` `#Transcript`

[Watch the recording](https://www.youtube.com/watch?v=kaPiA0Di6lw) · [Conference site](https://qconferences.com/)

## Description

Daniel Hewlett (Principal AI Engineer) and Karthik Ramgopal (Distinguished Engineer) reveal the internal "Agent Platform" that powers LinkedIn's Hiring Assistant. They explain why prompt chains are no longer enough and how they use Supervisor Agents, Skill Registries, and distributed messaging to handle non-deterministic AI workloads in production.

⏱️ Video Timestamps (For Navigation)
0:00 – Evolution of Generative AI at LinkedIn: From "Coach" to "Agent"
1:18 – The Early Days: Simple prompt-in/string-out products
2:15 – Moving to Prompt Chains: Handling memory and online inference
3:10 – The "Agent Era": Introducing prompt graphs and task automation
4:13 – Deep Dive: The LinkedIn Hiring Assistant problem space
5:40 – Why natural language interfaces beat 40+ search filters
6:45 – Scaling bottlenecks in single LLM block architectures
7:30 – Modular Design: Moving to a Manager/Interpreter pattern
8:55 – Transitioning from LLM blocks to hierarchical sub-agents
10:15 – The Supervisor Pattern: Coordinating specialized agent skills
11:42 – Parallel development and independent quality evaluation
13:10 – Model Selection: When to use GPT-4o vs. fine-tuned small models
14:35 – Domain Adaptation: Training models on the LinkedIn Economic Graph
16:20 – The LinkedIn Agent Platform: Standardizing prompts and namespaces
17:50 – LLM Inference Abstractions: Managing quotas and GPU limits
19:15 – Scaling non-deterministic workloads with a messaging platform
20:50 – Memory Management: Working memory vs. long-term collective memory
22:30 – Building a Skill Registry (and why it predated MCP)
24:10 – Observability challenges in asynchronous agentic systems
25:35 – Lessons Learned: When to use procedural code instead of an LLM
27:10 – The Model Customization Pyramid: RAG vs. Fine-tuning
28:45 – UX for Agents: Why text boxes alone aren't enough
30:15 – Q&A: Managing security and service principles in a skill registry

🔗 Transcript available on InfoQ:  https://bit.ly/49NzliH
