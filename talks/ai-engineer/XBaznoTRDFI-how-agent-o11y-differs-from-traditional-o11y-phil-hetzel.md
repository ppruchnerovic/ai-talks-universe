---
id: XBaznoTRDFI
title: "How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust"
slug: how-agent-o11y-differs-from-traditional-o11y-phil-hetzel
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Phil Hetzel"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-05-28T23:00:06Z
video_id: XBaznoTRDFI
youtube_url: https://www.youtube.com/watch?v=XBaznoTRDFI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How agent o11y differs from traditional o11y — Phil Hetzel, Braintrust

**Phil Hetzel**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=XBaznoTRDFI) · [Conference site](https://www.ai.engineer/)

## Description

Traditional observability answers one question: is the system up? Phil Hetzel from Braintrust argues that question is not the right one for agents. An individual agent trace can exceed a gigabyte. A single span can hit 20 megabytes. The data is semistructured, packed with unstructured text, and still arrives in real time. None of the systems built for uptime monitoring were designed to ingest, index, and actually use that.

Braintrust built a custom database from scratch for this problem: a write ahead log for instant visibility, analytical indexes for fast filtering, and a forked version of Tantivy (a Rust based full text search library similar to Apache Lucene) so an engineer can query every trace that mentioned a specific word. The other difference is who does this work: clinicians, lawyers, and wealth advisers now open traces directly to grade whether an agent responded correctly, and their written justifications become the training signal for automated scoring functions. The human annotations surface the failure modes. The scoring functions scale them.

Speaker info:
- https://www.linkedin.com/in/philliphetzel/
