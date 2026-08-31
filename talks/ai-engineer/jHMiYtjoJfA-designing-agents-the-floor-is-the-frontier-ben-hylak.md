---
id: jHMiYtjoJfA
title: "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop"
slug: designing-agents-the-floor-is-the-frontier-ben-hylak
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ben Hylak"]
channel: null
duration_min: 20
published_at: 2026-08-12T00:00:00Z
video_id: jHMiYtjoJfA
youtube_url: https://www.youtube.com/watch?v=jHMiYtjoJfA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop

**Ben Hylak**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=jHMiYtjoJfA) · [Conference site](https://www.ai.engineer/)

## Description

Build the thousand example eval suite everyone tells you to build, switch harnesses, and 80% of it stops meaning anything. Ben Hylak's complaint is that eval advice is still written for the chatbot era, back when you knew the answer to nearly every question a user would ask. His reframing is that the useful question is not what issues your agent has, since it will have effectively infinite issues, but which ones matter. That turns on the gap between your ceiling, the most impressive thing your agent can do, and your floor, the worst. The floor is what breaks trust: recommending a competitor, deleting data, sending slop to a customer because the agent happened to have email access.

The practical core is two numbers per issue, when it started and what share of users it hits. Learning that something began yesterday is what makes you ask what changed. Learning it hit three users rather than a hundred thousand is what tells you whether to care at all. From there he offers three findings from running this at Raindrop. Clustering traces is not issue detection, because boundaries drift, you do not control them, and what counts as one issue is specific to your product, so a cluster called price issues quietly merges a wrong quote with a wrong refund that have nothing in common. Code mode scales to traces, meaning you write classifiers and run them in a sandbox at production volume. And agents are poor at finding anomalies while being good at investigating them, so surface something deterministic like a keyword spike first and hand them that. Underneath all of it is the argument that evals now belong in your repo as tests rather than in a prompt playground, because the harness is the product.

Speaker info:
- https://x.com/benhylak
- https://www.linkedin.com/in/benhylak/

Timestamps:
0:00 - Raising the floor, and how little continual learning is real
2:07 - What agents looked like a year ago
3:23 - Why agent creativity cuts both ways
4:01 - Eval advice stuck in the chatbot era
4:38 - Switch harnesses and 80% of your evals break
5:16 - Safety without theater
5:57 - What Raindrop sees in production
7:12 - The real question: how do you make it better
8:26 - Benchmark maxer or floor raiser
9:05 - Why labs and companies have different jobs
9:42 - How much responsibility sits with the user
10:56 - Ceiling against floor, and which breaks trust
11:35 - Offline evals should look like tests
12:52 - Keep evals as code
13:30 - Two things you must know about every issue
14:45 - How many users do you actually have
16:02 - Lesson one: clusters are not issues
17:17 - Why cluster boundaries fail you
18:35 - Lesson two: code mode scales to traces
19:14 - Lesson three: agents cannot spot anomalies
