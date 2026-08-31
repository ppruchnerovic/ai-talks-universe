---
id: -CnA2lGfymY
title: "\"I've never seen anything scarier than an LLM with tool calls.\" — Erik Meijer aka @HeadinTheBox"
slug: i-ve-never-seen-anything-scarier-than-an-llm-with-tool
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 21
published_at: 2026-07-13T00:00:00Z
video_id: -CnA2lGfymY
youtube_url: https://www.youtube.com/watch?v=-CnA2lGfymY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=-CnA2lGfymY) · [Conference site](https://www.ai.engineer/)

## Description

AI agents today execute on blind trust, and the failure modes are already in the headlines: a dealership chatbot agreeing to sell a $76,000 Chevy Tahoe for $1, a coding agent wiping a production database during a code freeze, an "agent skill" quietly installing a keylogger on a developer's machine.

These are not edge cases. They are the predictable consequence of allowing agents to act without any mechanical guarantee of correctness or safety. Execution is irreversible. You cannot unsend a message, unwire a payment, or un-delete a database. In that regime, permitting an unsafe action costs far more than withholding a safe one, and thus the economically rational choice is to refuse to let agents act on unchecked intent alone.

Automind is an agent harness that enforces this discipline by construction. Before any action runs, the agent must submit its execution plan together with a machine-checkable proof of safety and correctness, written in Universalis, a literate logic programming language designed to be read by humans and verified by machines. A small, auditable checker decides whether the plan is allowed to execute. By left-shifting the trust boundary, we no longer have to trust the agent's proposal, or even its proof; only the checker. Policy compliance becomes a static property, established before the first side effect. We can finally demand formal proofs, not vibes, from the agents we deploy.

More about Erik: https://x.com/headinthebox
and automind: https://spawn-queue.acm.org/doi/pdf/10.1145/3676287

Erik Meijer has spent more than three decades designing programming languages and developer tools that help humans express intent more clearly to machines. His work has influenced languages and technologies including Haskell, Mondrian, Cω, C#, Visual Basic, Dart, Hack, LINQ, and Rx. Today, he is building Universalis, the world's first programming language for AI agents. By combining formal verification with large language models, Universalis aims to make agentic systems safe, transparent, and trustworthy enough for real-world knowledge work.

Timestamps

0:00 Introduction and purpose of the talk
1:54 The inherent dangers of AI and accidental file deletion
3:39 The history and impact of LLMs (the "Pandora's box")
5:36 The problem of prompt injection and model safety
7:03 Formal verification and using Lean for safety proofs
10:45 The introduction of tool calls and the leap into chaos
13:59 The "lethal trifecta" of AI risks
14:13 The proposed solution: "air-gapping" the agentic loop
16:36 Refying plans into programs and using Free Monads
19:17 The concept of proof-carrying code and summary
