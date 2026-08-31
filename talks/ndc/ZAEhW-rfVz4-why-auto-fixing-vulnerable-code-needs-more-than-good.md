---
id: ZAEhW-rfVz4
title: "Why Auto-Fixing Vulnerable Code Needs More Than Good Intentions - Spyros Gasteratos"
slug: why-auto-fixing-vulnerable-code-needs-more-than-good
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Spyros Gasteratos"]
channel: null
duration_min: 56
published_at: 2026-01-29T16:30:11Z
video_id: ZAEhW-rfVz4
youtube_url: https://www.youtube.com/watch?v=ZAEhW-rfVz4
tags: ["Application Security", "Security", "NDC", "Conferences", "2025", "Live", "Fun", "Manchester", "England", "UK", "United Kingdom", "Spyros Gasteratos"]
transcript: false
---

# Why Auto-Fixing Vulnerable Code Needs More Than Good Intentions - Spyros Gasteratos

**Spyros Gasteratos**

`NDC Conferences` · `NDC` · `2026` · `56 min`

`#Application Security` `#Security` `#NDC` `#Conferences` `#2025` `#Live` `#Fun` `#Manchester` `#England` `#UK` `#United Kingdom` `#Spyros Gasteratos`

[Watch the recording](https://www.youtube.com/watch?v=ZAEhW-rfVz4) · [Conference site](https://ndcconferences.com/)

## Description

When Vibes Don’t Build: Why Auto-Fixing Vulnerable Code Needs More Than Good Intentions - Spyros Gasteratos

This talk was recorded at NDC Manchester in Manchester, England.

Attend the next NDC conference near you:

/           @NDC

Follow our Social Media!

"Developers deal with a lot of noise, why don't we use AI to fix some security bugs?" These were famous last words before we tried to use LLMs to fix potential vulnerabilities on our codebase.
The AI’s hilarious fix? Delete the function. Problem solved.

In this talk, I’ll share our failures and successes in building an agentic auto-remediation suggestion system for code vulnerabilities. We'll talk about how we threw everything at it: zero-shot classifiers, tree of thought prompting and reflexion loops. The AI responded by suggesting 200-line refactors for SQL injections or marking serious vulnerabilities as “false positives.”

Turns out, RAG and prompting aren’t enough. We needed constraint-based action planning, feedback loops from real developer behavior, and multi-agent workflows that argued with each other before touching code.

This is a story of over-engineering, humbling failures, and finally, a path to practical AI-assisted remediation that developers actually trust. You’ll laugh, cringe, and leave with a clear understanding of what it takes (and what to avoid) when automating code fixes.
