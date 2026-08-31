---
id: F2Ay09T4EHQ
title: "GitHub, Snyk, Docker & Anthropic on Securing AI Agents"
slug: github-snyk-docker-anthropic-on-securing-ai-agents
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: null
duration_min: 10
published_at: 2026-08-31T16:00:25Z
video_id: F2Ay09T4EHQ
youtube_url: https://www.youtube.com/watch?v=F2Ay09T4EHQ
tags: []
transcript: false
---

# GitHub, Snyk, Docker & Anthropic on Securing AI Agents

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=F2Ay09T4EHQ) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Harness engineering has a security problem: the skills, tools and memory we hand coding agents arrive with no permissions, no sandboxing and no controls at all. Four talks from AI DevCon London on what that actually costs.

Joseph Katsioloudes (GitHub Security Lab) opens with the gap the industry is trying to close — roughly one application security specialist for every hundred developers — and argues the answer isn't shifting left, it's starting left. Liran Tal (Snyk) scanned around 4,000 published agent skills and found about 1 in 7 carried malware, suspicious downloads or credential harvesting, in a file format with nowhere to declare a permission. Oleg Šelajev (Docker) demos an agent refusing a dangerous skill, then complying once the same instruction is rewritten as Python, wrapped in a module and the context is cleared. And Lamis Mukta (Anthropic) closes on the unglamorous engineering that makes agent memory safe in production: versioning, so a poisoned memory can be rolled back, and a hash check, so two agents can't overwrite each other.

What we cover:
– Why one security specialist per 100 developers is the gap AI could close
– What a scan of 4,000 published agent skills actually turned up
– Why a SKILL.md file has nowhere to declare permissions or sandboxing
– How clearing the context talks an agent past its own refusal
– The guardrails an agent harness needs before memory reaches production

Chapters:
00:00:00 - Introduction
00:00:35 - Joseph Katsioloudes, GitHub Security Lab: AI and code security
00:01:47 - One security specialist for every 100 developers
00:02:38 - Why "shift left" should be "start left"
00:02:59 - Liran Tal, Snyk: what's inside 4,000 published skills
00:04:12 - 1 in 7 skills had something wrong with it
00:05:16 - Oleg Šelajev, Docker: getting an agent to run what it refused
00:06:56 - Clearing the context, and the agent complies
00:07:31 - Lamis Mukta, Anthropic: keeping agent memory safe
00:09:09 - Concurrency, and stopping two agents overwriting each other

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which of these four would keep you up at night? Tell us in the comments.
