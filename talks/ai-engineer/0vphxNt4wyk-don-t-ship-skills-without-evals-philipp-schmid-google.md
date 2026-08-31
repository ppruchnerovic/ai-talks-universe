---
id: 0vphxNt4wyk
title: "Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind"
slug: don-t-ship-skills-without-evals-philipp-schmid-google
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Philipp Schmid"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-07-14T00:00:00Z
video_id: 0vphxNt4wyk
youtube_url: https://www.youtube.com/watch?v=0vphxNt4wyk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Don't Ship Skills Without Evals — Philipp Schmid, Google DeepMind

**Philipp Schmid**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0vphxNt4wyk) · [Conference site](https://www.ai.engineer/)

## Description

There are thousands of agent skills. Almost none of them are tested. They get vibe-checked with two manual runs, maybe a thumbs-up from a colleague, then shipped. You wouldn't merge code without tests — so why are we shipping skills without evals? This talk covers the full lifecycle of building reliable agent skills: what a skill actually is (and isn't), how to write one that triggers correctly, and how to build a lightweight eval harness that catches failures before your users do.

### Philipp Schmid
Staff Engineer · Google DeepMind
[X/Twitter](https://x.com/_philschmid) · [LinkedIn](https://www.linkedin.com/in/philipp-schmid-a6a2bb196/) · [Website](https://www.philschmid.de/) · [Blog](https://www.philschmid.de)

Philipp Schmid is a Staff Engineer at Google DeepMind working on Gemini and Gemma. His work focuses on helping developers build and benefit from AI responsibly.

Timeline:

0:00 Introduction: Why skills need evals
0:25 The problem with current agent workflows
1:25 Agents we use vs. agents we build
2:28 Defining a 'Skill' and progressive disclosure
3:08 Capability skills vs. preference skills
4:17 Do skills actually work? (Skillsbench data)
5:39 Model-triggered vs. user-invoked skills
6:39 Best practices for writing skill descriptions
8:30 Structuring complex, multi-layered skills
9:04 Defining goals and constraints (avoiding rigid steps)
9:56 Don't skip negative cases
10:36 Testing strategy: Evals and regressions
11:05 Removing 'no-ops' for cost efficiency
11:47 Knowing when to retire a skill
12:22 Practical example: Gemini interactions API
13:36 Building a lightweight eval harness
14:35 Using regex and LLMs as judges
17:14 Top 10 best practices summary
20:20 Homework: How to start testing your skills
Viral Pull Quotes:

(0:22) "You wouldn't merge code without tests—so why are we shipping skills without evals?"
(1:13) "Agents are really nondeterministic. You might not know if your task fails because your skill is bad or if your task fails because it's way too challenging for the model."
(9:15) "If the process or the workflow is always the same, you should not use skills. Maybe you should write a script."
(11:53) "Skills are not there to live forever. Models get better, behaviors change, environments change."
