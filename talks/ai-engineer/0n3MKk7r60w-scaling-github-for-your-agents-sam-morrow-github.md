---
id: 0n3MKk7r60w
title: "Scaling GitHub for your Agents — Sam Morrow, GitHub"
slug: scaling-github-for-your-agents-sam-morrow-github
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sam Morrow"]
channel: null
duration_min: 21
published_at: 2026-04-27T22:00:06Z
video_id: 0n3MKk7r60w
youtube_url: https://www.youtube.com/watch?v=0n3MKk7r60w
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Scaling GitHub for your Agents — Sam Morrow, GitHub

**Sam Morrow**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0n3MKk7r60w) · [Conference site](https://www.ai.engineer/)

## Description

GitHub operates one of the most heavily-utilised MCP servers in the ecosystem, with over 4 million downloads of the stdio server alone. Discover the architectural decisions, technical challenges and lessons learned while building and scaling a remote MCP server on production infrastructure. The session walks through the journey from initial implementation to horizontal scaling, covering the specific challenges of condensing a platform as expansive as GitHub into a coherent MCP interface. Attendees will learn practical strategies for managing tool overload, optimizing context usage, implementing distributed session storage, and maintaining observability without compromising user privacy. Whether building a first remote server or optimizing an existing implementation, attendees will gain concrete patterns, anti-patterns, and architectural guidance from real production experience.

Key Takeaways:
• Architecture patterns for stateless, horizontally scalable remote MCP servers
• Practical approaches to tool proliferation and context window constraints
• Why a focus on auth, security and privacy is essential to success

Speaker info:

Timestamps:
0:00:29 - Overview of GitHub's MCP public launch and community growth.
0:02:06 - Challenges of tool proliferation and impact on agent context.
0:03:21 - Mitigation via "tool sets" and dynamic discovery.
0:05:54 - Optimizing API output tokens to improve efficiency.
0:06:44 - Improving reliability through intent-based tool design.
0:08:14 - Security strategy: OAuth 2.1 and PKCE implementation.
0:10:40 - Managing prompt injection and security vulnerabilities.
0:12:35 - Using OAuth scopes for granular tool filtering.
0:13:47 - Stateless server architecture and Redis session management.
0:15:18 - Experimental features and human-in-the-loop UX.
0:16:30 - Future outlook: Compositional tools and automation.
0:18:04 - Final project metrics: Downloads, forks, and volume.
