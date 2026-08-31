---
id: wEc9aG7cRQc
title: "Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog"
slug: why-your-agent-disagrees-with-itself-and-what-to-do-about
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Diane Lin"]
channel: null
duration_min: 26
published_at: 2026-07-20T06:25:22Z
video_id: wEc9aG7cRQc
youtube_url: https://www.youtube.com/watch?v=wEc9aG7cRQc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Your Agent Disagrees With Itself (And What To Do About It) - Diane Lin, Datadog

**Diane Lin**

`AI Engineer` · `AI Engineer` · `2026` · `26 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=wEc9aG7cRQc) · [Conference site](https://www.ai.engineer/)

## Description

Run the same task twice, and sometimes you get two materially different answers. While many dismiss this as the "stochastic nature of LLMs," this inconsistency is a critical product flaw that destroys customer trust—especially in high-stakes fields like cybersecurity, where a "flip-flop" between a malicious threat and a benign alert can lead to disastrous outcomes.

This session explores why these flip-flops are usually not model failures. They occur in the "gray zone" near the decision boundary, where policies are ambiguous and even human experts may disagree. Instead of treating disagreement as a bug, we can use it as a signal to improve both the agent and the data.

You'll learn a practical workflow that combines active learning, semantic memory (domain knowledge and business policies), and episodic memory (past similar cases) to automatically identify ambiguous examples, focus human review where it matters most, and continuously adapt the agent to customer-specific preferences, without relying solely on expensive fine-tuning.

Key takeaways

1. Find the gray zone. Use model disagreement to identify the decisions that deserve human attention.
2. Turn inconsistency into a feature. Every flip-flop is an opportunity to clarify policies and improve the agent.
3. Teach, don't just fine-tune. Combine semantic memory and episodic memory to make agents more consistent with far less effort than retraining.
4. Build a continuous learning loop. Improve consistency, streamline quality control, and evolve your agent to match how your customers actually make decisions.

Speakers:
- Diane Lin (Datadog): Dr. Diane Lin is Tech Lead at Datadog, where she leads the development of self-evolving AI agents for cybersecurity, and previously co-founded Culminate (acquired by Datadog)
