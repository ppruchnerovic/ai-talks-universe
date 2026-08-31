---
id: HvMyYLTfvhg
title: "Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked"
slug: building-agents-is-trivial-now-context-is-the-next-frontier
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jeff Ng"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-08-21T00:00:00Z
video_id: HvMyYLTfvhg
youtube_url: https://www.youtube.com/watch?v=HvMyYLTfvhg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Building Agents Is Trivial Now, Context Is the Next Frontier — Jeff Ng, Unblocked

**Jeff Ng**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=HvMyYLTfvhg) · [Conference site](https://www.ai.engineer/)

## Description

An agent built to enrich Linear tickets read a report that time to first character in Unblocked's own QA pipeline had gone from hundreds of milliseconds to three or four seconds, and recommended turning async dispatch back on. The recommendation was wrong. A support engineer had explicitly disabled that setting days earlier because it caused an outage. The agent had the ticket and the repository and reasoned soundly from both, but never saw the Slack thread where the engineers worked through the failure, or the postmortem that came out of it. Jeff Ng's point: standing an agent up has become the easy part, and missing context is what still breaks them.

Six months ago the same build took a team a quarter, because checkpointing, sandbox isolation, and observability all had to be solved first, none of which improves what an agent can do. Cloud primitives and agent frameworks have absorbed that work, so defining an agent now comes down to a model, instructions, tools, and a sandbox. What that removes is the plumbing, not the judgment a person supplies on every turn: why the code is the way it is, what broke last time, what the team decided to do about it. Something has to carry that load once nobody is babysitting, and Ng argues MCP does not, because access is not understanding and an agent left to reconcile contradictory results picks badly. He reruns the same agent against a context engine spanning docs, code, tickets, and conversations, and the recommendation flips from repeating the outage to preventing it.

Speaker info:
- https://getunblocked.com

Timestamps:
0:00 - Six months ago this took a team a quarter
1:02 - The taxes: state, sandboxes, observability
3:02 - Primitives and frameworks remove the plumbing
4:21 - Demo: enriching a Linear ticket
5:36 - The fix that had already caused an outage
7:00 - Why this does not happen locally
8:17 - What a context engine does
10:36 - The same agent, grounded
