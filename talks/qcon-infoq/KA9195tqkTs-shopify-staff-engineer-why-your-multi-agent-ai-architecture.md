---
id: KA9195tqkTs
title: "Shopify Staff Engineer: Why Your Multi-Agent AI Architecture Will Fail"
slug: shopify-staff-engineer-why-your-multi-agent-ai-architecture
conference: qcon-infoq
conference_name: "QCon / InfoQ Dev Summit"
category: "Software dev with AI tracks"
edition: "InfoQ"
year: 2026
speakers: []
channel: null
duration_min: 35
published_at: 2026-06-11T05:08:41Z
video_id: KA9195tqkTs
youtube_url: https://www.youtube.com/watch?v=KA9195tqkTs
tags: ["InfoQ", "Transcript", "QCon AI New York", "QCon AI", "Multi-Agent Systems", "Shopify", "Case Study", "Artificial Intelligence", "AI Agents", "Generative AI"]
transcript: false
---

# Shopify Staff Engineer: Why Your Multi-Agent AI Architecture Will Fail

**Speaker not identified**

`QCon / InfoQ Dev Summit` · `InfoQ` · `2026` · `35 min`

`#InfoQ` `#Transcript` `#QCon AI New York` `#QCon AI` `#Multi-Agent Systems` `#Shopify` `#Case Study` `#Artificial Intelligence` `#AI Agents` `#Generative AI`

[Watch the recording](https://www.youtube.com/watch?v=KA9195tqkTs) · [Conference site](https://qconferences.com/)

## Description

How does Shopify scale AI across thousands of employees without falling into the "Agentic Slop" or microservices trap? In this InfoQ video, Shopify Staff Engineer Paulo Arruda shares the engineering realities, failed experiments, and architecture patterns behind orchestrating multiple LLM agents at enterprise scale.

Moving past the hype of 2025 as the "year of agents," Paulo explains why the industry is facing a massive context bloat problem with Model Context Protocol (MCP) and how to fix it.

Discover how Shopify teams slashed operational workflows from 22 hours to 7 minutes by breaking down massive prompts into lean, narrow-focused swarms, and why treating agents like an "Agent Microservices Architecture" brings back all the networking, tracing, and debugging nightmares of the past.

Get an inside look at a novel, experimental solution: llm-fuse, an adapter layer that tricks LLMs into treating databases as local file systems to maximize precision and recall.

⏱️ Video Timestamps (For Navigation)
0:00 - Introduction: AI Adoption & Hacker Culture at Shopify
1:45 - The Codebase Monolith Challenge & Failed Graph Experiments
3:20 - How Claude Code & Tobi Lütke's Email Fueled Company-Wide "Vibe Coding"
4:45 - The Breakthrough: Connecting Two Claude Code Instances via MCP
6:10 - Scaling Multi-Agent Systems: Slashed Workflows (From 22 Hours to 7 Minutes)
7:55 - The Rise of the "AI SWAT Team" Antipattern
9:15 - The Danger of Agent Microservices Architecture
11:00 - Deep Dive: SwarmSDK & Fiber-Based Orchestration in Ruby
12:30 - Beyond the Hype: Context Engineering & Solving MCP Context Bloat
14:15 - The llm-fuse Hypothesis: Injecting Knowledge as a File System
16:00 - Implementing a "Memory Defrag" Tool for LLMs

🔗 Transcript available on InfoQ: https://bit.ly/4oiKJdo
