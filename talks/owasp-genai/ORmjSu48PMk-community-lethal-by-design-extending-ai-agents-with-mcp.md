---
id: ORmjSu48PMk
title: "Community | Lethal by Design Extending AI Agents with MCP Servers Turns Capabilities into Weapons"
slug: community-lethal-by-design-extending-ai-agents-with-mcp
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: ["Gal Moyal"]
channel: "OWASP GenAI Security Project"
duration_min: 32
published_at: 2026-07-20T00:28:46Z
video_id: ORmjSu48PMk
youtube_url: https://www.youtube.com/watch?v=ORmjSu48PMk
tags: []
transcript: false
---

# Community | Lethal by Design Extending AI Agents with MCP Servers Turns Capabilities into Weapons

**Gal Moyal**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `32 min`

[Watch the recording](https://www.youtube.com/watch?v=ORmjSu48PMk) · [Conference site](https://genai.owasp.org/)

## Description

When Security teams think about AI agent risk, they typically focus on scanning MCP servers, reviewing supply chains, and checking for known vulnerabilities. But this approach addresses about half the problem. The other half - Skills, the textual instruction sets that shape agent reasoning - remains almost entirely ungoverned.

This session presents findings from our research that analyzed hundreds of the most popular MCP servers and Skills in the wild, revealing a fundamental asymmetry in the AI agent capability stack. MCP servers expose deterministic, observable tool calls that can be logged and audited. Skills operate inside the model's reasoning context, where their influence on agent behavior is causally opaque - you can see what an agent did, but connecting that action back to the skill that caused it requires inference, not observation.

And the data is stark: we found that 76% of popular MCP servers carry at least one high-risk capability. One in four expose arbitrary code execution. And 62% of popular Skills carry at least one risky characteristic, leaving them largely invisible to current security tooling.

We then map these capabilities into toxic combinations: multi-tool attack chains grounded in real-world incidents including attacks against Cursor, Docker, Amazon Q, Salesforce Agentforce, and Replit, to show how individually legitimate capabilities come together to form catastrophic attack paths.

The No Excessive CAP framework is then introduced, which shifts agent governance from properties you cannot fully control (whether an agent will encounter malicious input) to amplifiers you can: Capabilities (what the agent can do), Autonomy (how freely it can act), and Permissions (what identity it runs under). These three dimensions interact multiplicatively, and we provide concrete guidance for assessing and controlling each.

🔗 Learn more: https://genai.owasp.org

Speakers:
Gal Moyal
CTO Office, Noma Security

Gal Pnini
AI Security Researcher, Noma Security
