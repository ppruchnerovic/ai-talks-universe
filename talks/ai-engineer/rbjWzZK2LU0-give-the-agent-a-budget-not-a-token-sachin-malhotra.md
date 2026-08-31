---
id: rbjWzZK2LU0
title: "Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic"
slug: give-the-agent-a-budget-not-a-token-sachin-malhotra
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sachin Malhotra"]
channel: null
duration_min: 20
published_at: 2026-08-22T00:00:00Z
video_id: rbjWzZK2LU0
youtube_url: https://www.youtube.com/watch?v=rbjWzZK2LU0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Give the Agent a Budget, Not a Token — Sachin Malhotra, Anthropic

**Sachin Malhotra**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=rbjWzZK2LU0) · [Conference site](https://www.ai.engineer/)

## Description

An agent tidying up after itself listed the workloads it no longer needed and deleted them. One stage of the pipeline evaluated to nothing, the filter dropped out, and the selector matched everything: about 200 workloads gone in 90 seconds, roughly 20 engineers affected, some of it long running training jobs that were never checkpointed. Nothing malicious happened, and the agent did nothing Sachin Malhotra could not have done himself, because it was using his token. The failure was handing unbounded power to something nobody was watching closely.

A token is a boolean, a static list of scopes you hold or you do not, and the standard fix of narrowing it fails the way it would with a new hire. You do not take the verb away, you bound it. A budget has four dimensions: how much, how fast, what can be undone, and who notices. That becomes three things you enforce and one question you ask. Asymmetric verbs, meaning give the agent the operations that fail loudly, like unskipping a test, and keep a human on the ones that fail silently, like skipping one. Rate limits on every write, refilling on their own so nobody files a ticket for more. Trip wires rather than allow lists, because a list written up front goes stale while aggregate counts tell you what actually happened. The undo test sizes all three. Underneath it all, identity has to be stamped by a proxy and never claimed by the caller, or the agent simply changes the header and its limit resets.

Speaker info:
- https://x.com/edorado93
- https://www.linkedin.com/in/edorado93
- https://bruteforced.dev/

Timestamps:
0:00 - The demo, and what happens after it ships
1:02 - 200 workloads deleted in 90 seconds
2:42 - Why a narrower token scope is the wrong fix
4:23 - A token is a boolean, a budget has dimensions
6:05 - Asymmetric verbs, and skip versus unskip
8:34 - Rate limits: a ceiling that refills
10:16 - Trip wires beat allow lists
12:47 - The undo test, and the second key
13:37 - Feature flags: canary versus production
15:19 - Where the policy lives, text and infrastructure
17:49 - Why the proxy stamps identity, not the caller
