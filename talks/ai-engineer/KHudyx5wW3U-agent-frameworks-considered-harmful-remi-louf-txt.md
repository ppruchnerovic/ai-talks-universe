---
id: KHudyx5wW3U
title: "Agent Frameworks Considered Harmful — Rémi Louf, .txt"
slug: agent-frameworks-considered-harmful-remi-louf-txt
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rémi Louf"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-08-22T00:00:00Z
video_id: KHudyx5wW3U
youtube_url: https://www.youtube.com/watch?v=KHudyx5wW3U
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Agent Frameworks Considered Harmful — Rémi Louf, .txt

**Rémi Louf**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=KHudyx5wW3U) · [Conference site](https://www.ai.engineer/)

## Description

In the first week the daily brief posted to Slack twice, a voice note vanished entirely, and the market brief turned to garbage after prompt edits Rémi Louf had not versioned and could no longer recall. Each failure became a piece of what turned into a runtime. The lost note became an append only log where nothing is discarded and every event is causally linked to the one that triggered it. The duplicates became a real queue that counts attempts. The untraceable prompt became a content addressed store, and that one was the rabbit hole.

Every part of a prompt is hashed and stored separately, the system message, each skill description, each tool definition, the user question, so a prompt is a list of hashes rather than a rendered string. Diff two runs and you see exactly which component changed. Replay one against a different model and the request rebuilds from the graph. He wanted this because a live chat session does not show you what the model actually saw, not with compaction and unshared reasoning in play. The rest stays deliberately small. Agents are markdown files you drop in a folder, so people who do not write code can add one. They subscribe to events instead of living in a graph with edges to maintain. Typed tool calls and typed events are the two boundaries, because roughly 20% of his events were coming back malformed and getting rejected. He took two weeks away from running a 15 person company to build it. Twenty agents now run there.

Speaker info:
- https://x.com/remilouf
- https://www.linkedin.com/in/remilouf/
- https://thetypicalset.com

Timestamps:
0:00 - Two weeks away to find out what agents can do
1:57 - The morning he wanted, and the robot mower
2:49 - A terminal you still have to sit at
4:30 - Why the prompt ended up in markdown, not code
6:11 - Cron gets you when, events get you because
8:44 - What broke in week one
9:37 - The log: nothing lost, everything causally linked
12:11 - Content addressing the prompt, and free diffs and replays
15:32 - A kernel, not a framework
16:25 - Typed calls and typed events as boundaries
18:05 - Lessons, and build before you buy
