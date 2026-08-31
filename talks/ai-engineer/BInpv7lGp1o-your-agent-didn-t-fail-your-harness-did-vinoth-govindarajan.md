---
id: BInpv7lGp1o
title: "Your Agent Didn't Fail. Your Harness Did. — Vinoth Govindarajan, OpenAI"
slug: your-agent-didn-t-fail-your-harness-did-vinoth-govindarajan
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Vinoth Govindarajan"]
channel: null
duration_min: 18
published_at: 2026-07-29T16:00:06Z
video_id: BInpv7lGp1o
youtube_url: https://www.youtube.com/watch?v=BInpv7lGp1o
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Your Agent Didn't Fail. Your Harness Did. — Vinoth Govindarajan, OpenAI

**Vinoth Govindarajan**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=BInpv7lGp1o) · [Conference site](https://www.ai.engineer/)

## Description

Two runs touch the same session, the second write silently erases the first, and the agent keeps answering with total confidence from stale state. Nothing crashed and the model did not hallucinate, so this is a harness failure, the kind that lives in the system around the model rather than in the weights. Using OpenClaw as a public case study, Vinoth Govindarajan walks the usual suspects: state that was never persisted, overlapping writers with no single writer lane, a tool call that never returns because nothing set a deadline, and an approval that outlived the action it was supposed to authorize.

The through line is that a model only proposes; the harness has to commit, and a receipt has to prove it. A transcript shows what the agent said, but a receipt is the evidence that survives: it records the mutation, the authority used, and whether the message actually reached the user, since an internal success that never becomes visible proof is its own failure. You leave with a run receipt audit to run on your own agents, five questions per incident: what woke it up, what state did it inherit, what authority did it use, what executed, and what evidence survived.

Speaker info:
- https://x.com/iamvinoth
- https://www.linkedin.com/in/vinothgovindarajan/
- https://theagentstack.substack.com/

Timestamps:
0:00 - Introduction: harness failures vs model failures
1:32 - Delivery can succeed while the truth fails
2:46 - A model proposes, the harness commits, the receipt proves
4:14 - How events enter and state is rehydrated
5:48 - Idempotency, locks, and ordering
7:22 - Ownership: who persists the turn
8:28 - Single writer lanes and overlapping writes
10:09 - Time, deadlines, and cancellation
11:23 - Approval drift and bounded authority
13:05 - Internal success vs user-visible proof
14:08 - The run receipt audit: five questions
