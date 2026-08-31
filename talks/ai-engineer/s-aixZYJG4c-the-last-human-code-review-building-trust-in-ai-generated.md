---
id: s-aixZYJG4c
title: "The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo"
slug: the-last-human-code-review-building-trust-in-ai-generated
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Itamar Friedman"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-20T13:30:38Z
video_id: s-aixZYJG4c
youtube_url: https://www.youtube.com/watch?v=s-aixZYJG4c
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Last Human Code Review: Building Trust in AI-Generated Code — Itamar Friedman, Qodo

**Itamar Friedman**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=s-aixZYJG4c) · [Conference site](https://www.ai.engineer/)

## Description

If you are shipping AI generated code faster than your humans can review it, Itamar Friedman's position is that you are inside the problem rather than ahead of it. He asks the room whether developers will still be reading diffs line by line by the end of the year, then reports finding two incompatible camps among engineering leaders the night before: one holding that every line must be human trusted, the other content to ship bugs and fix them quickly because velocity wins. Which camp you sit in decides what you have to build.

His claim is that models stopped being the constraint. Code review benchmarks have barely moved across recent model releases, and the difference between a review that catches a real contract break and one that asks whether you considered error handling is context, not reasoning. That context is scattered across competing instruction files, differs between teams inside the same company, and largely is not written down at all, living instead in senior developers' heads and in Slack threads. Codifying it means building for two audiences at once, because the format an agent parses cleanly is not the format developers will actually maintain. The deeper version encodes the architecture itself, including which service contract broke production three months ago, so that review shifts from reading one pull request to reading a graph and noticing that three changes in flight are about to collide.

Speaker info:
- https://twitter.com/itamar_mar
- https://www.linkedin.com/in/itamarf
- https://www.qodo.ai/authors/itamar-f

Timestamps:
0:00 - Where the bottleneck moved, and why code review exists
3:38 - Two camps: trust every line, or ship and fix fast
5:19 - Models are not the barrier, context is
7:03 - Context scattered across competing instruction files
8:48 - The knowledge lives in heads and in Slack
9:42 - Codifying for agents and humans at once
10:34 - Interfaces for both: rules shown, and a note to the next agent
12:19 - Fewer human comments as the readiness signal
13:11 - Encoding architecture, contracts, and past outages
14:05 - Automatic approve and block, added gradually
16:38 - Reviewing the software graph instead of the PR
