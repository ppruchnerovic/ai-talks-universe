---
id: UPwGaM2MKHY
title: "The Log Is The Agent - Ishaan Sehgal, Omnara"
slug: the-log-is-the-agent-ishaan-sehgal-omnara
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ishaan Sehgal"]
channel: null
duration_min: 15
published_at: 2026-06-25T21:15:06Z
video_id: UPwGaM2MKHY
youtube_url: https://www.youtube.com/watch?v=UPwGaM2MKHY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Log Is The Agent - Ishaan Sehgal, Omnara

**Ishaan Sehgal**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=UPwGaM2MKHY) · [Conference site](https://www.ai.engineer/)

## Description

Think about a character you've spent 100 hours playing in a video game like Skyrim or Elden Ring.

What exactly is your character?
- Is it the game engine (the loop)? No.
- Is it the PlayStation console (the compute)? No.
- Is it the controller (the tools)? No.

Your character is the save file (the data).

If your PlayStation bursts into flames, your character isn't dead. You just buy a new PlayStation, download your save file from the cloud, and your character is exactly where they were, mid-swing. The identity, history, and current state of your character live entirely in the data.

Today, most attention goes toward frameworks, orchestration layers, context engineering, specs, and tools. But as models become more capable and generally intelligent, the differentiator shifts away from these abstractions and toward the underlying infrastructure.

The Engine becomes interchangeable. The Brain (LLM) commoditizes. The Hands (tools) are just APIs.

What actually persists across models, runtimes, and machines is the session log.

That’s where continuity, identity, and state actually live.

A decade ago, Martin Kleppmann argued that databases should be understood as projections over an append-only log. I think the same thing is now happening with agents.

Today, agents are treated like complicated black boxes made of loops, models, and tool calls. But at its core, the agent is the session log (the save file). Everything else is swappable.

Once the log becomes the primitive, entirely new system properties emerge:
- durability — agents survive crashes, disconnects, and machine failure
- continuity — sessions can be resumed from anywhere, on any device
- forkability — timelines can branch for parallel execution and exploration
- addressability — agents become durable entities that can be referenced and revisited
- observability — execution can be monitored and steered in real time
- portability — models, runtimes, and machines become interchangeable

But this creates a new infrastructure question:

If the model provider owns the log, does the model provider own the agent?

This talk explores why the future of agent infrastructure isn't what we're focused on today, but rather durable, portable logs that make agents persistent across models, runtimes, and machines.

Speakers:
- Ishaan Sehgal (Omnara): Ishaan Sehgal is the CEO and cofounder of Omnara (YC S25), where he builds managed infrastructure for AI agents.
X/Twitter: https://x.com/ishaansehgal
