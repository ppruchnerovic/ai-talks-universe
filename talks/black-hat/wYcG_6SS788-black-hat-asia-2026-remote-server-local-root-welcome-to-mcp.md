---
id: wYcG_6SS788
title: "Black Hat Asia 2026 | Remote Server, Local Root. Welcome to MCP."
slug: black-hat-asia-2026-remote-server-local-root-welcome-to-mcp
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: ["Remote Server"]
channel: null
duration_min: 31
published_at: 2026-08-20T14:45:16Z
video_id: wYcG_6SS788
youtube_url: https://www.youtube.com/watch?v=wYcG_6SS788
tags: []
transcript: false
---

# Black Hat Asia 2026 | Remote Server, Local Root. Welcome to MCP.

**Remote Server**

`Black Hat` · `Black Hat` · `2026` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=wYcG_6SS788) · [Conference site](https://www.blackhat.com/)

## Description

As Large Language Models (LLMs) evolve into autonomous agents, the Model Context Protocol (MCP) has become the de facto standard for connecting AI to external systems. MCP not only enables tool invocation through structured message exchanges, but also supports privileged user-data retrieval from remote servers. To support this, MCP adopts several OAuth-based mechanisms to dynamically establish authorization sessions. However, in doing so, it unintentionally introduces new threat vectors that traditional OAuth applications were never exposed to.

In this Briefing, we will uncover a novel attack surface within the MCP authorization flow. By abusing the dynamic nature of this flow, we demonstrate how authorization metadata—traditionally sourced from pre-registered, trusted identity providers—becomes a powerful attack vector when MCP clients accept it dynamically from arbitrary remote servers. Through a systematic analysis of three major classes of MCP clients—browser-based, process-based, and hybrid—we show how this design flaw leads to severe outcomes, including Remote Code Execution (RCE), Local File Execution (LFE), Account Takeover, and Cross-Tenant Data Exfiltration, depending on the client architecture.

Our analysis was validated across real MCP implementations and acknowledged by major vendors, including Anthropic and Google. To date, our research has resulted in five assigned CVEs and multiple bounty rewards, including an RCE in MCP Inspector (CVE-2025-58444) and a command injection vulnerability in Google's Gemini CLI. Additional CVEs were assigned to Cherry Studio (CVE-2025-54074), Dify (CVE-2025-58747), and other MCP clients, along with further confirmed impacts across multiple SaaS platforms.

Jiacheng Zhong  |  Security Researcher,
Shuyang Wang  |  Head of Security Research, Obsidian Security
Zhengyu Liu  |  Ph.D. Student, Johns Hopkins University
Aonan Guan  |  Senior Cloud Security Engineer, Wyze Labs
