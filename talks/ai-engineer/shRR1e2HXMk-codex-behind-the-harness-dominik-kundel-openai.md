---
id: shRR1e2HXMk
title: "Codex, Behind the Harness — Dominik Kundel, OpenAI"
slug: codex-behind-the-harness-dominik-kundel-openai
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dominik Kundel"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-08-10T00:00:00Z
video_id: shRR1e2HXMk
youtube_url: https://www.youtube.com/watch?v=shRR1e2HXMk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Codex, Behind the Harness — Dominik Kundel, OpenAI

**Dominik Kundel**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=shRR1e2HXMk) · [Conference site](https://www.ai.engineer/)

## Description

Once GPT 5.3 Codex Spark started serving a thousand tokens per second on Cerebras, inference stopped being the bottleneck and the network became it. The answer was websocket mode: a persistent connection replacing server sent events over HTTP, carrying stateful context so a turn ships back only the tool call result instead of resending every item. The same pressure shapes context construction, which fights size, flexibility and cachability at once. Tools can be marked deferred so they never enter the context window and surface through tool search when the model actually wants them, and the available skills list is capped at 2% of the context window, with descriptions trimmed as it grows past that.

Actions are where a harness earns its keep. File edits go through an apply patch tool the models were trained on, everything else through a shell the model instinctively drives with ripgrep, and all of it inside a sandbox: seatbelt on macOS, bubblewrap on Linux, and a custom open source sandbox on Windows the team had to build themselves. Approval fatigue pushes people into full access, which their own security team hates, so an escalation now spins up an auto review subagent with read only permissions and no ability to spawn others, judging the action against the transcript and how explicitly the user authorized it. Deleting a file you asked for reads differently from deleting a .git folder you never mentioned. Long horizon goals run by injecting a continuation prompt until the model calls an update goal tool, which is why concrete verifiable objectives beat essays. Dominik Kundel's closing point is that the harness is Apache 2 and written in Rust, and most of what makes it distinct lives in the responses API, so you can borrow any of it.

Speaker info:
- https://x.com/dkundel
- https://linkedin.com/in/dkundel
- https://github.com/openai/codex
