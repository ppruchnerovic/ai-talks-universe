---
id: 0RNNfxpdbQk
title: "Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest"
slug: medic-for-apache-spark-first-aid-for-failing-jobs-drasko
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Drasko Profirovic"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-07-20T06:24:50Z
video_id: 0RNNfxpdbQk
youtube_url: https://www.youtube.com/watch?v=0RNNfxpdbQk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Medic for Apache Spark - First Aid for Failing Jobs - Drasko Profirovic, Pinterest

**Drasko Profirovic**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=0RNNfxpdbQk) · [Conference site](https://www.ai.engineer/)

## Description

In this talk, we’ll share the journey of building an agentic diagnostics tool to address one of the most time-consuming challenges in data engineering: troubleshooting Spark job failures at scale. As Spark workloads and platform complexity continue to grow, traditional dashboards and static playbooks are no longer sufficient. Our goal was to build an intelligent agent capable of automatically ingesting logs, correlating relevant context, and producing human-quality diagnoses and actionable recommendations in minutes rather than hours.

We’ll begin by covering the core design goals behind the system—accuracy, extensibility, and trustworthiness—and the architectural foundations we put in place to support them. We’ll discuss how we designed the agent around modular capabilities such as log parsing, pattern recognition, root-cause inference, and remediation suggestions; how we integrated it with Spark and broader platform metadata; and how we made it easy to extend the system to new error patterns and domains. We’ll also share how we approached evaluation and testing by building a corpus of real incidents, turning them into regression tests, and using them to continuously measure reasoning quality and safety. From there, we’ll explore what it takes to push agentic systems to their limits in production, including lessons on prompt and tool design, handling ambiguity in logs, reducing hallucinations, reasoning over partial or noisy signals, and striking the right balance between automation and human oversight. Along the way, we’ll highlight a few unexpected failure modes and how those informed later iterations.

We’ll close by discussing where we’re headed next: expanding beyond Spark into other data systems, and using engineer feedback loops to continuously improve its reasoning over time.

Speakers:
- Drasko Profirovic (Pinterest): Drasko is a Staff Engineer at Pinterest focused on agentic systems, drawing on a background in full-stack engineering and experience at Stripe and OpenAI to build the primitives and frameworks that enable scalable diagnostics, orchestration, and automated resolution.
