---
id: IIchUA5T3gs
title: "Run Untrusted Agent Code with LangSmith Sandboxes | Interrupt 26"
slug: run-untrusted-agent-code-with-langsmith-sandboxes-interrupt
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 10
published_at: 2026-06-01T14:45:54Z
video_id: IIchUA5T3gs
youtube_url: https://www.youtube.com/watch?v=IIchUA5T3gs
tags: ["LangSmith", "LangChain", "AI agents", "sandboxing", "agent security", "code execution", "LLM agents", "agentic AI", "prompt injection", "container security", "AI infrastructure", "coding agents", "Claude Code", "agent observability", "LangSmith tutorial", "AI developer tools", "agent sandbox", "safe code execution", "multi-agent systems", "AI ops"]
transcript: false
---

# Run Untrusted Agent Code with LangSmith Sandboxes | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `10 min`

`#LangSmith` `#LangChain` `#AI agents` `#sandboxing` `#agent security` `#code execution` `#LLM agents` `#agentic AI` `#prompt injection` `#container security` `#AI infrastructure` `#coding agents` `#Claude Code` `#agent observability` `#LangSmith tutorial` `#AI developer tools` `#agent sandbox` `#safe code execution` `#multi-agent systems` `#AI ops`

[Watch the recording](https://www.youtube.com/watch?v=IIchUA5T3gs) · [Conference site](https://interrupt.langchain.com/)

## Description

LangSmith Sandboxes are secure code execution environments for agents. They give agents a runtime with a filesystem, shell, package manager, persistent state, and network boundary, so they can write code, install dependencies, run tests, inspect failures, and continue work across longer sessions.

Each sandbox runs in a hardware-virtualized microVM, isolated from your services and from other sandboxes. That isolation is especially important for agents running model-generated code, external dependencies, or user-provided scripts.

Sandboxes work through the same LangSmith SDK and API key teams already use, so teams can add safe code execution to Deep Agents, Open SWE, LangSmith Deployment, LangSmith Fleet, or custom agent workflows without building the runtime layer themselves.

At Interrupt, LangChain's Agent conference, Mukil Loganathan gave a walkthrough of LangSmith Sandboxes and shared how they help teams build and test agents more safely.

Run Untrusted Agent Code with LangSmith Sandboxes | Interrupt 26
0:00 Intro
0:22 Agents are writing real code today
1:21 Use cases: software engineering, data analysis, security, browser/computer use
3:32 With great power comes great responsibility — the risks
4:25 What is a sandbox and why it's hard to build
4:55 Problem 1: speed and scale (sub-1s spin-up, thousands of sandboxes)
5:48 Problem 2: security — container escapes, prompt injection, malicious MCPs
6:31 Auth proxy — network-level lockdown for sandboxes
7:02 Problem 3: long-running agents — pause, resume, and durable state
8:15 Problem 4: agents make mistakes — snapshot, restore, and fork
9:01 Getting started with LangSmith Sandboxes
9:33 Roadmap: local/remote handoff, shared volumes, execution tracing
9:53 Try it today + Q&A

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• LangSmith Sandboxes: https://www.langchain.com/langsmith/sandboxes
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/
