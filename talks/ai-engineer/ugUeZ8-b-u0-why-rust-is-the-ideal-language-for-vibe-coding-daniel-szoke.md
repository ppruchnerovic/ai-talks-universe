---
id: ugUeZ8-b-u0
title: "Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry"
slug: why-rust-is-the-ideal-language-for-vibe-coding-daniel-szoke
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Daniel Szoke"]
channel: null
duration_min: 16
published_at: 2026-05-27T15:00:06Z
video_id: ugUeZ8-b-u0
youtube_url: https://www.youtube.com/watch?v=ugUeZ8-b-u0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry

**Daniel Szoke**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ugUeZ8-b-u0) · [Conference site](https://www.ai.engineer/)

## Description

TypeScript is easy for models to write because it imposes few constraints. Those same missing constraints let models introduce data races that compile, run, and only fail intermittently. A thread safety bug in Rust does not compile. The compiler names the unsound type, explains why it cannot be sent between threads, and points the agent directly at the fix.

Daniel Szoke, Rust SDK maintainer at Sentry, argues that optimizing for a language models can write easily is the wrong goal. The better optimization is a language whose compiler enforces correctness as a natural feedback loop. Every error an agent hits and resolves in a loop is a production bug that never ships. The Rust compiler is also faster than asking a review agent to find the same class of bugs and more reliable than hoping it does.

Speaker info:
- https://www.linkedin.com/in/dlsz

Timestamps:
0:00 Introduction and the speaker's background at Sentry
0:27 The current conventional wisdom for AI-assisted development
1:53 Why languages like Python and TypeScript are popular for AI
3:44 The hidden risks of prioritizing "easy-to-write" languages
6:40 Philosophical perspective: Alien intelligence and failure modes
9:28 Introduction to Rust and its strict compiler guarantees
10:53 Key safety features: Type, Null, and Concurrency safety
11:59 Demonstrating "Fearless Concurrency" with a code example
14:26 Why Rust constraints are an asset for autonomous AI agents
15:36 Conclusion and Sentry resources
