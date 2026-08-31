---
id: 0U0U_qsDnpY
title: "Community | Execution Governance The Layer That Defines What Agents Cannot Do"
slug: community-execution-governance-the-layer-that-defines-what
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: ["Sergey Vlasov"]
channel: null
duration_min: 14
published_at: 2026-07-20T00:46:36Z
video_id: 0U0U_qsDnpY
youtube_url: https://www.youtube.com/watch?v=0U0U_qsDnpY
tags: []
transcript: false
---

# Community | Execution Governance The Layer That Defines What Agents Cannot Do

**Sergey Vlasov**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=0U0U_qsDnpY) · [Conference site](https://genai.owasp.org/)

## Description

OWASP GenAI Security Project 2026 Virtual Summit
Community Session

In March 2026, a supply chain attack compromised LiteLLM — the universal proxy between AI agents and every major LLM API.
The attack never reached the agent's reasoning layer.
It operated in the dependency beneath it.

Every behavioral defense remained active.
Every defense was irrelevant.
This pattern repeats.

Attacks increasingly operate below the agent — in the execution environment, in trusted dependencies, in the composition of individually safe components.
The same month, Axios (100M weekly downloads) was backdoored via a compromised maintainer account.
Five projects compromised in 12 days. Each component passed individual verification. The chain was the attack.

This talk presents execution governance as the missing architectural layer.
The approach does not detect unsafe behavior. It defines a World Manifest — a compiled specification of what actions and components exist in the agent's executable world. At runtime, enforcement is deterministic: same input, same decision, always. No LLM on the critical enforcement path.
We demonstrate the gap through a controlled scenario: an agent configured with standard best practices executes a supply chain–style attack.
Then, under a governed execution environment — without modifying the agent — the same attack cannot execute. Not because it was blocked.
Because the action does not exist in the agent's world.

The takeaway is architectural: OWASP Agentic Top 10 classifies how agents fail.
Execution governance defines what cannot happen. These are complementary layers.
Currently, only one exists in standard practice.

🔗 Learn more: https://genai.owasp.org

Speakers:
Sergey Vlasov
Senior Software Engineer, Radware
