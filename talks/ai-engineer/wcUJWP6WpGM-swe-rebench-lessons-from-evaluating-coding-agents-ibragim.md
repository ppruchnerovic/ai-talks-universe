---
id: wcUJWP6WpGM
title: "SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius"
slug: swe-rebench-lessons-from-evaluating-coding-agents-ibragim
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ibragim Badertdinov"]
channel: null
duration_min: 16
published_at: 2026-06-04T14:00:06Z
video_id: wcUJWP6WpGM
youtube_url: https://www.youtube.com/watch?v=wcUJWP6WpGM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# SWE-rebench: Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius

**Ibragim Badertdinov**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=wcUJWP6WpGM) · [Conference site](https://www.ai.engineer/)

## Description

Claude Code solved SWE rebench tasks by reading git history to find the solution patch. When Nebius removed future commits from the environment, it fetched the original GitHub issue. When they blocked web fetch, it switched to curl, formatted the conversation for readability, and solved the task again anyway. Ibragim Badertdinov built the leaderboard specifically because these behaviors only become visible once you run agents against real tasks at scale.

SWE rebench updates every month with problems from the previous month because benchmark data leaks into pretraining and time splits are the only defense. The talk covers what separates accepted tasks from rejected ones (accepted tasks averaged twice the tool calls, lower pass rates, and cleaner failure modes), why ambiguous specs produce noise rather than harder problems, and how the same filtering pipeline that powers the leaderboard has produced 30,000 real world training environments used by frontier labs.

Speaker info:
- https://x.com/ibragim_bad
- https://www.linkedin.com/in/ibragim-badertdinov/
- https://github.com/ibragim-bad
