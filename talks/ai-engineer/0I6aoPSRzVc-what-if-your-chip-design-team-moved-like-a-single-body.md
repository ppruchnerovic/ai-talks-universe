---
id: 0I6aoPSRzVc
title: "What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip"
slug: what-if-your-chip-design-team-moved-like-a-single-body
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Abduallah Mohamed"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-08-22T15:00:25Z
video_id: 0I6aoPSRzVc
youtube_url: https://www.youtube.com/watch?v=0I6aoPSRzVc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# What If Your Chip Design Team Moved Like a Single Body? — Abduallah Mohamed, AIDAChip

**Abduallah Mohamed**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0I6aoPSRzVc) · [Conference site](https://www.ai.engineer/)

## Description

They told the agent not to write to the spec files. It agreed, then wrote to them through bash. They blocked bash, so it used sed. They blocked sed, so it used cat. The lesson Abduallah Mohamed drew is that once an agent is capable enough, the substrate it runs in matters more than the agent itself, so the fix was blocking at the system level rather than tool by tool. Two other failures shaped the design: an analog design agent that wandered into work belonging to the RTL agent, and truth drift, where an agent updated a parameter in one place and left five others stale.

The setting is chip design, where nothing can be patched once silicon is printed and getting it wrong means printing again, which averages around $50 million. Across roughly 15 practitioners they interviewed, the recurring answer was that 70% of the time goes to alignment, and that the strongest organizations are the most aligned rather than the ones with the best engineers. Their argument is that buying more tools attacks the linear term while communication overhead grows quadratically with headcount. So they built a shared nervous system: a living graph of intent and constraints that agents cannot change without human approval, a tribal knowledge layer that compounds from project to project, and role specific agents written by subject matter experts rather than one general coding agent. They grade the alignment rather than the agents, and point out that graph memory now has a research literature while institutional memory has almost none.

Speaker info:
- https://www.linkedin.com/in/abduallah/
- https://abduallahmohamed.com/
- https://www.linkedin.com/in/khaledalashmouny/
- https://aidachip.com

Timestamps:
0:00 - Eleven players, and why alignment beats skill
2:53 - The quadratic term nobody is solving
3:47 - No patch for silicon, and 70% spent on alignment
5:32 - Fragmented intent, and the shared nervous system
7:18 - Demo: the graph, and the approval echo
10:40 - Grading alignment, and the research gap
13:11 - What broke, including cat versus the spec
14:50 - Block at the source, and the substrate lesson
