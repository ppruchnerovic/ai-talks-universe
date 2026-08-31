---
id: WXy8Yy9xGss
title: "CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed"
slug: ci-in-the-era-of-ai-from-unit-tests-to-stochastic-evals
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2025
speakers: ["Nathan Sobo"]
channel: null
duration_min: 15
published_at: 2025-06-27T00:00:00Z
video_id: WXy8Yy9xGss
youtube_url: https://www.youtube.com/watch?v=WXy8Yy9xGss
tags: []
transcript: false
---

# CI in the Era of AI: From Unit Tests to Stochastic Evals — Nathan Sobo, Zed

**Nathan Sobo**

`AI Engineer` · `AI Engineer` · `2025` · `15 min`

[Watch the recording](https://www.youtube.com/watch?v=WXy8Yy9xGss) · [Conference site](https://www.ai.engineer/)

## Description

Software engineers have long understood that high-quality code requires comprehensive automated testing. For decades, our industry has relied on deterministic tests with clear pass/fail outcomes to ensure reliability.

High-quality software depends on automated testing. That's certainly true at Zed, where we're building a next-generation native IDE in Rust. Zed runs at 120 frames per second, but it would also crash once a second if we didn't maintain and run a comprehensive suite of unit tests on every change.

But what happens when AI enters the equation?

In this talk, we'll explore how continuous integration evolves when working with AI components. "Evals" - parlance from the machine learning field - are fundamentally a continuation of the software testing tradition, but with a critical difference: they're inherently stochastic.

Zed's traditional CI goes to extreme lengths to eliminate non-determinism, as nobody likes having their pull requests blocked by flaky builds. We've even fully simulated network interactions with a deterministic random scheduler. AI components, however, forced us to confront a fundamental paradigm shift—uncertainty isn't a bug but an intrinsic feature of these systems, compelling us to embrace what we couldn't avoid.

We'll share our journey of reconceptualizing evals as "stochastic unit tests" - still verifying system behavior, but without binary pass/fail grades.

We'll discuss practical approaches to:
- Thoughtfully building test suites for AI components
- Shifting from red/green outcomes to "shades of gray"
- Replacing build gates with trend analysis and performance monitoring
- Maintaining engineering confidence despite statistical variance

Whether you're incorporating AI into existing systems or building new AI-powered tools, this talk will provide practical insights into maintaining quality when determinism gives way to probability.

About Nathan Sobo
Nathan joined GitHub in late 2011 to build the Atom text editor, and he led the Atom team until 2018.

He also co-led development of Teletype for Atom, pioneering one of the first production uses of conflict-free replicated data types for collaborative text editing.

He's been dreaming about building the world's best text editor since he graduated from college, and is excited to finally have the knowledge, tools, and resources to achieve this vision.

Recorded at the AI Engineer World's Fair in San Francisco. Stay up to date on our upcoming events and content by joining our newsletter here: https://www.ai.engineer/newsletter
