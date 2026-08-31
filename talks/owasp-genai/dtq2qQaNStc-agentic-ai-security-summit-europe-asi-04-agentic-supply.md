---
id: dtq2qQaNStc
title: "Agentic AI Security Summit, Europe: ASI:04 Agentic Supply Chain"
slug: agentic-ai-security-summit-europe-asi-04-agentic-supply
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "AI security"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 9
published_at: 2026-01-21T06:44:57Z
video_id: dtq2qQaNStc
youtube_url: https://www.youtube.com/watch?v=dtq2qQaNStc
tags: []
transcript: false
---

# Agentic AI Security Summit, Europe: ASI:04 Agentic Supply Chain

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=dtq2qQaNStc) · [Conference site](https://genai.owasp.org/)

## Description

In this session from the OWASP Agentic Security Summit (London, December 9, 2025), presents the Agentic Supply Chain risk, a core entry in the OWASP Top 10 for Agentic Applications. The talk explains why supply chain security fundamentally changes when systems move from static software builds to runtime, autonomous agentic systems.

Unlike traditional supply chains—where risk is introduced through package registries, CI/CD pipelines, or external dependencies—agentic systems dynamically select and interact with tools, MCP servers, other agents, and prompts at runtime. This creates new attack surfaces where legitimate-looking components can change behavior after deployment, silently expanding privileges or enabling data exfiltration.

Real-world examples highlight the danger, including MCP server updates that introduced subtle but malicious behavior, such as unauthorized blind carbon copies of emails to attacker-controlled addresses. These risks are difficult to detect because system functionality appears unchanged, while sensitive data quietly leaks.

Mitigations build on traditional supply chain controls but extend them for agentic environments: runtime verification of signed components, strict version pinning, avoiding automatic updates, enforcing least-privilege access, using organizational gateways or proxies for MCP servers, and maintaining rapid kill-switches to contain cascading failures. The talk also emphasizes sandboxing and isolation, especially where agents run with high privileges.

This session reinforces a key message: in agentic systems, the supply chain is no longer static—it is alive at runtime, and securing it requires continuous verification, monitoring, and containment strategies. These efforts are part of the broader work of the OWASP GenAI Security Project, including emerging initiatives like AI SBOM and MCP security guidance.

#OWASP
#owasptop10
#AgenticAISecurity
#GenAISecurity
#AISupplyChain
#MCP
#AgenticSystems
#Cybersecurity
#SecureAI
#AIAgents
#AIThreats
