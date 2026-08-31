---
id: ZSQb5fzRFPw
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua"
slug: computer-use-2-0-agents-just-got-multi-cursor-francesco
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Francesco Bonacci"]
channel: null
duration_min: 17
published_at: 2026-07-15T00:00:00Z
video_id: ZSQb5fzRFPw
youtube_url: https://www.youtube.com/watch?v=ZSQb5fzRFPw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Computer-Use 2.0: Agents Just Got Multi-Cursor — Francesco Bonacci, Cua

**Francesco Bonacci**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ZSQb5fzRFPw) · [Conference site](https://www.ai.engineer/)

## Description

Three agents click, type, and scroll through three different apps on one desktop at the same time, and the user's own mouse and keyboard never move. That's the live demo behind cua driver, a tool the team built in a single weekend after Codex shipped its own computer use model. Instead of taking over the hardware cursor, it talks straight to the accessibility layer underneath the operating system: UI Automation on Windows, AT SPI on Linux, AX on macOS. Those undocumented APIs let a click land on a background window or a keystroke reach a hidden one, so any number of agents can act without stealing focus from each other or from the human sitting at the machine.

To know whether any of this can be trusted, the team built CUABench: over 130 verifiable tasks across 42 environments and five platforms, each one attacked by a matrix of agents trying to reward hack it before it's allowed into the dataset. Swapping a standard computer tool for cua driver pushed pass rate on a 4K benchmark from 62% to 80% while using 34% fewer tokens, mostly because it watches one window instead of the whole screen. The newest addition, built with Snorkel AI on real circuit design software, humbled every model tested: the best agent fully passed only 6 of 25 electrical engineering tasks, every one of them an edit to an existing schematic, and starting from a blank schematic dropped every model straight to 0%.

Speaker info:
- https://www.linkedin.com/in/francesco-bonacci-70428a121/

Timestamps
0:00 - Introduction and Vision of Cua
2:40 - Overview of Cua Driver and Background Operation
6:34 - Introduction to Cua Bench and Agent Evaluation
10:50 - Cua Fleet and GPU Infrastructure Optimization
15:08 - Q&A Session
15:44 - Discussion on Mobile and Android Support
