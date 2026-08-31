---
id: IvE8n-ylFYY
title: "Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)"
slug: privacy-preserving-intelligence-steve-korshakov-bee-acq
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Steve Korshakov"]
channel: null
duration_min: 16
published_at: 2026-07-20T17:17:53Z
video_id: IvE8n-ylFYY
youtube_url: https://www.youtube.com/watch?v=IvE8n-ylFYY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Privacy-Preserving Intelligence — Steve Korshakov, Bee (acq. Amazon)

**Steve Korshakov**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=IvE8n-ylFYY) · [Conference site](https://www.ai.engineer/)

## Description

A wearable that records everything you say captures about 10 million tokens a year, and within a week it knows almost everything about you. That is Bee, and Steve Korshakov calls it roughly the most sensitive capture device on the market, which is why his whole talk is about one guarantee: no one can read your data, not even Amazon, the company that acquired Bee eight months ago. Being inside Amazon made this harder, not easier, because an ordinary AWS customer trusts Amazon to see their data, and Bee now had to defend against that too.

The encryption key never leaves your phone, and Bee never stores it. Before the phone hands anything over, it runs an attestation pipeline that checks the exact workload against a public transparency log, Sigstore, so anyone can verify the code touching your data is genuine. Inference runs on their own models inside confidential compute, keys in memory expire after seven days, and a separate Amazon privacy team holds the signing keys, hardcoded into the apps, so Bee can influence a deployment but cannot ship anything unnoticed. The footnote that surprised the room: the whole system is about 20,000 lines of memory safe code, most of it just verifying attestation, with no homegrown crypto.

Speaker info:
- https://x.com/Ex3NDR
- https://github.com/ex3ndr
- https://bee.computer

Timestamps:
0:00 - The most sensitive capture device on the market
1:32 - The mission: no one, not even Amazon, can read your data
2:13 - Why the agent runs continuously, not request response
3:58 - Four principles: the key never leaves your phone
4:53 - Attestation and a public transparency log
6:11 - Own inference, confidential compute, and 7 day keys
7:14 - Signing so no insider can ship unnoticed
9:35 - Certificates that embed the proofs
10:16 - Q&A: joining Amazon, 20k lines, and taming agents
