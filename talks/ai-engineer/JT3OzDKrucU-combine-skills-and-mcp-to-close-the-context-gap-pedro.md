---
id: JT3OzDKrucU
title: "Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase"
slug: combine-skills-and-mcp-to-close-the-context-gap-pedro
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Pedro Rodrigues"]
channel: null
duration_min: 18
published_at: 2026-05-15T00:00:00Z
video_id: JT3OzDKrucU
youtube_url: https://www.youtube.com/watch?v=JT3OzDKrucU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Combine Skills and MCP to Close the Context Gap — Pedro Rodrigues, Supabase

**Pedro Rodrigues**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=JT3OzDKrucU) · [Conference site](https://www.ai.engineer/)

## Description

Agents working with Postgres will confidently create a view over a table with row-level security enabled and silently bypass that security in the process. Not because they can't reason. Because they don't know about the security_invoker flag, and nobody told them. Pedro Rodrigues from Supabase ran this exact test: same agent, same task, MCP alone versus MCP plus a skill. The one without the skill shipped a query that exposed data it shouldn't have.

The talk covers what Supabase learned building their agent skill from scratch: critical security rules go directly in skill.md because agents will reliably skip reference files, skills should point to living documentation rather than duplicate it, and opinionated workflow guidance matters more than comprehensive coverage. Their evals ran across Claude and GPT models in three conditions and the result was unanimous. Skills without MCP underperform. MCP without skills misses environment-specific constraints. Together they close the gap that makes agents unreliable on real production systems.

Speaker info:
- https://x.com/rodriguespn23
- https://www.linkedin.com/in/pedro-neves-rodrigues/
- https://github.com/Rodriguespn
