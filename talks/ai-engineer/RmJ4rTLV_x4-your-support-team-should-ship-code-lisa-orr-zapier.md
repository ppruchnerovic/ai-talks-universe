---
id: RmJ4rTLV_x4
title: "Your Support Team Should Ship Code – Lisa Orr, Zapier"
slug: your-support-team-should-ship-code-lisa-orr-zapier
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Lisa Orr"]
channel: "AI Engineer"
duration_min: 16
published_at: 2025-12-16T17:00:06Z
video_id: RmJ4rTLV_x4
url: https://www.youtube.com/watch?v=RmJ4rTLV_x4
youtube_url: https://www.youtube.com/watch?v=RmJ4rTLV_x4
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration"]
transcript: false
---

# Your Support Team Should Ship Code – Lisa Orr, Zapier

**Lisa Orr**

`AI Engineer` · `AI Engineer` · `2025` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=RmJ4rTLV_x4) · [Conference site](https://www.ai.engineer/)

## Description

Zapier maintains 8000+ integrations that break as APIs change. We had thousands of backlog support tickets with dozens more arriving weekly. To keep up with the traffic, we started building AI tools to help ship integration fixes faster. We began by shadowing engineers fixing tickets and building tools we believed would expedite the fix process. Our first effort, an API playground hosting AI tools like diagnosis and test generation, failed to get engineering traffic because it pulled builders out of their workflows. We pivoted to MCP tools that engineers could use directly in their IDEs. MCP tools gained traction, but our most valuable tool, Diagnosis, took too long to run. Engineers wouldn't wait for it, revealing we needed an asynchronous approach. We built Scout Agent to string our tools together, autonomously reading support tickets, gathering context, generating fixes with tests, and submitting merge requests ready for review. This agent approach has gained traction with our support team handling high ticket volumes. An MR ready for review means they can validate and ship a fix quickly before needing to jump on the next incoming ticket. Throughout this process we've learned that the real challenge is everything surrounding code generation. Before writing code, Scout Agent needs both the right context and to show its work so engineers trust its recommendations. After generation, engineers need to quickly validate and correct the proposed fix, otherwise MRs sit unreviewed and abandoned. Embedding Scout Agent directly in GitLab solved this. Teams can iterate on proposed solutions without context switching. To track improvement, we measure three distinct failure modes: categorization accuracy (should Scout attempt this ticket?), fixability assessment (does this need a code fix?), and solution quality (does the generated code actually work?). Each reveals different improvement opportunities. Today, Scout drives 40% of support's integration fixes, with expansion to engineering teams and downstream automation (testing, shipping, migration) as our next frontiers.

Speaker: Lisa Orr  |  Product Leader, Zapier
