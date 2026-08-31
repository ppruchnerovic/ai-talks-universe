---
id: NuePCNMpWGc
title: "Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar"
slug: can-llms-generate-enterprise-quality-code-prasenjit-sarkar
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Prasenjit Sarkar"]
channel: null
duration_min: 15
published_at: 2026-05-31T00:00:00Z
video_id: NuePCNMpWGc
youtube_url: https://www.youtube.com/watch?v=NuePCNMpWGc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Can LLMs generate Enterprise Quality Code? — Prasenjit Sarkar, Sonar

**Prasenjit Sarkar**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=NuePCNMpWGc) · [Conference site](https://www.ai.engineer/)

## Description

Sonar ran 4,444 Java programming assignments through 53 models and measured what actually came out. GPT-4o generated under 250,000 lines for those assignments. GPT 5.4 generated 1.2 million. Claude Sonnet 4.6 generated 627,000 with the highest security issue rate at 300 per million lines of code. Prasenjit Sarkar from Sonar walks through the full leaderboard: pass rate, cyclomatic complexity, bug density, and security issues per model.

Their response is a three-stage framework called ACDC: guide, verify, solve. The verify stage runs SonarQube analysis in 1 to 5 seconds before a commit, against 1 to 5 minutes in CI. If issues slip through to the PR, a remediation agent creates one fix per issue, runs it through analysis and compilation to check for regressions, and only presents it if it passes.

Speaker info:
- https://www.linkedin.com/in/jit2600/

Timestamps:
0:00 Introduction and the Shift to Agentic Development
1:44 Evaluating LLM Code Quality and Reliability
3:00 Sonar's Evaluation Framework and Methodology
3:39 LLM Performance Analysis (Pass Rates and Code Bloat)
5:24 Why LLMs Struggle: Training Data and Hidden Flaws
6:45 The Sonar LLM Leaderboard
8:30 Complexity Metrics: Cyclomatic vs. Cognitive
10:41 The ACDC Framework: Guide, Verify, and Solve
11:06 Phase 1: Guide (Context Augmentation & Sonar Sweep)
11:42 Phase 2: Verify (SonarQube Agentic Analysis)
12:40 Phase 3: Solve (Remediation Agent)
14:05 Product Summary and Ecosystem Support
