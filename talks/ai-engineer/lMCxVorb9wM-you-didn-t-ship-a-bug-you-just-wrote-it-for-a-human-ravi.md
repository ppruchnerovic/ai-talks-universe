---
id: lMCxVorb9wM
title: "You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit"
slug: you-didn-t-ship-a-bug-you-just-wrote-it-for-a-human-ravi
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ravi Madabhushi"]
channel: null
duration_min: 13
published_at: 2026-07-19T16:00:06Z
video_id: lMCxVorb9wM
youtube_url: https://www.youtube.com/watch?v=lMCxVorb9wM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# You Didn't Ship a Bug. You Just Wrote It for a Human. - Ravi Madabhushi, Scalekit

**Ravi Madabhushi**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=lMCxVorb9wM) · [Conference site](https://www.ai.engineer/)

## Description

We built a demo agent to show customers how to connect agents to their tools. A simple chat assistant — Gmail, Calendar, a handful of connectors. It ran on a 15-minute schedule. And every 15 minutes, our production database strained. Latency crept up and alerts fired. Then settled.

Then, it fired again.

It took us a while to find it. One line - a "last seen" timestamp updating on every tool call. Written for a human who logs in once. Our agent was calling it sixty times a second. We had built infrastructure to show customers how to connect agents to their tools. We hadn't noticed we'd built it for humans.

That line wasn't a bug. It was a design assumption. And it's not just us - 60% of all production LLM errors trace back to rate limits. They are not model failures or bad prompts. Infrastructure that never anticipated this kind of traffic. As one developer put it: "Rate limits can't tell the difference between agent legitimately needs 100 calls and agent is just looping." Because they were never designed to. They were designed for humans.

Every layer of the stack your agents depend on carries the same assumption — that the user on the other end is a person, doing one thing at a time, at human speed. Your agent isn't. And until your infrastructure knows that, production will keep finding the places where it doesn't.

This talk is about what we learned from finding it, what it actually means to treat agents as a first-class principal, not a fast human, and what changes when you design for that from the start.

Speakers:
- Ravi Madabhushi (Scalekit): Ravi has been building infra for how software talks to other software for more than a decade. He co-founded Pipemonk — a SaaS integration platform acq. by Freshworks (NASDAQ listed) then spent years leading product on Freshworks' auth platform as it scaled to 50K+ businesses and 2M DAUs.

At Scalekit, he's applying that to a harder version of the same problem: not humans logging into software, but agents taking actions inside it. What breaks is different. What it costs when it breaks is worse.
X/Twitter: https://x.com/ravibits
