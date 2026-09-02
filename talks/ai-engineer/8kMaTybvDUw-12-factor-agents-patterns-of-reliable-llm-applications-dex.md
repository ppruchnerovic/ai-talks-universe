---
id: 8kMaTybvDUw
title: "12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer"
slug: 12-factor-agents-patterns-of-reliable-llm-applications-dex
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Dex Horthy"]
channel: "AI Engineer"
duration_min: 17
published_at: 2025-07-03T00:00:00Z
video_id: 8kMaTybvDUw
url: https://www.youtube.com/watch?v=8kMaTybvDUw
youtube_url: https://www.youtube.com/watch?v=8kMaTybvDUw
tags: []
transcript: false
---

# 12-Factor Agents: Patterns of reliable LLM applications — Dex Horthy, HumanLayer

**Dex Horthy**

`AI Engineer` · `AI Engineer` · `2025` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=8kMaTybvDUw) · [Conference site](https://www.ai.engineer/)

## Description

Hi, I'm Dex. I've been hacking on AI agents for a while.

I've tried every agent framework out there, from the plug-and-play crew/langchains to the "minimalist" smolagents of the world to the "production grade" langraph, griptape, etc.

I've talked to a lot of really strong founders who are all building really impressive things with AI. Most of them are rolling the stack themselves. I don't see a lot of frameworks in production customer-facing agents.

I've been surprised to find that most of the products out there billing themselves as "AI Agents" are not all that agentic. A lot of them are mostly deterministic code, with LLM steps sprinkled in at just the right points to make the experience truly magical.

Agents, at least the good ones, don't follow the "here's your prompt, here's a bag of tools, loop until you hit the goal" pattern. Rather, they are comprised of mostly just software.

So, I set out to answer:

What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?

# The Short  Version: The 12 Factors

Even if LLMs continue to get exponentially more powerful, there will be core engineering techniques that make LLM-powered software more reliable, more scalable, and easier to maintain.

How We Got Here: A Brief History of Software
Factor 1: Natural Language to Tool Calls
Factor 2: Own your prompts
Factor 3: Own your context window
Factor 4: Tools are just structured outputs
Factor 5: Unify execution state and business state
Factor 6: Launch/Pause/Resume with simple APIs
Factor 7: Contact humans with tool calls
Factor 8: Own your control flow
Factor 9: Compact Errors into Context Window
Factor 10: Small, Focused Agents
Factor 11: Trigger from anywhere, meet users where they are
Factor 12: Make your agent a stateless reducer

---
