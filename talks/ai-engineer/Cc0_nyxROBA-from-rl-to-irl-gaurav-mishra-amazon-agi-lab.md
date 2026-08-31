---
id: Cc0_nyxROBA
title: "From RL to IRL — Gaurav Mishra, Amazon AGI Lab"
slug: from-rl-to-irl-gaurav-mishra-amazon-agi-lab
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Gaurav Mishra"]
channel: null
duration_min: 18
published_at: 2026-08-14T00:00:00Z
video_id: Cc0_nyxROBA
youtube_url: https://www.youtube.com/watch?v=Cc0_nyxROBA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From RL to IRL — Gaurav Mishra, Amazon AGI Lab

**Gaurav Mishra**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Cc0_nyxROBA) · [Conference site](https://www.ai.engineer/)

## Description

Asked to file an expense, the agent gets signed out mid task, reasons that it can infer the password, guesses twice, and locks the account. In a second run it clicks a sponsored button styled like the real submit button, lands on a different site, and begins typing personal details into it. Both are real trajectories from early browser training runs at the Amazon AGI Lab, and Gaurav Mishra's summary is that RL worked while the world was a game, and IRL starts when the game fights back.

The talk catalogues what a reward function meets on contact with a real login screen. Observability is partial, since the DOM misses content baked into images and the screenshot misses whatever needs scrolling. Actions are irreversible, credentials expire mid trajectory, and done routinely does not mean successful. His answer is flight school rather than exams. Sandboxes train on layout shift, slow loads, pop ups, focus stealing, and stale tabs, and recovery becomes a native model action instead of an infra reset, so the agent refreshes, backtracks, waits, or escalates. A process reward model penalizes dangerous steps along the path instead of scoring only the outcome, and calibrated confidence teaches the agent to weigh whether an action is authorized, reversible, and visible before committing. The closing trajectory runs the same task correctly, including the agent refusing to guess the password and handing control back. Over time the model gets better and the harness gets thinner.

Speaker info:
- https://www.linkedin.com/in/gaurav-mishra-b307a437

Timestamps:
0:00 - RL to IRL, and a lightning review of RL for agents
3:26 - Why coding agents can do computer use at all
4:05 - The agent that guesses its own password
5:47 - The sponsored button that looks like submit
6:37 - Partial observability, irreversibility, expiring credentials
8:29 - Flight school, not exams
9:54 - Process rewards and calibrated confidence
11:11 - The pilot and the cockpit
14:07 - Assumption versus reality, point by point
15:11 - The same task, done right
