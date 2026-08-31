---
id: RmS5s6Wbin4
title: "Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare"
slug: gadgets-personal-app-vibe-coding-that-is-actually-safe
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Kenton Varda"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-05T00:00:00Z
video_id: RmS5s6Wbin4
youtube_url: https://www.youtube.com/watch?v=RmS5s6Wbin4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Gadgets: Personal app vibe coding that is actually safe — Kenton Varda, Cloudflare

**Kenton Varda**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=RmS5s6Wbin4) · [Conference site](https://www.ai.engineer/)

## Description

*Note: Kenton has just released Cloudflare OS today: https://x.com/KentonVarda/status/2084990137180590572 This talk was recorded a month prior to launch.*

Claude needed a strikethrough the slide app did not have, so it added one to the app. Asked to build a deck from a Google doc, it also added text centering and a box that accepts raw SVG, then generated the SVG for a diagram the app could not otherwise draw. That is Kenton Varda's argument in a single move. Software today ships from a developer to users whose feature requests die in Jira, and the escape hatch developers reach for is a plugin architecture rewrite that takes years and never lands. If a user's own agent can add the feature, the core app stays clean and nobody waits.

Nothing in current infrastructure supports that. Mobile platforms will not run unsigned code, and 25 years of cloud architecture put one blessed version of every app on the developer's server. Gadgets is his answer, built on Cloudflare Workers with no containers and no database. Each gadget is a single instance of an app, one deck or one board, and sharing is implemented by the platform so the app itself cannot get access control wrong. The UI runs in a null origin iframe that can only postMessage to its parent, over a Cap'n Web RPC session to server code in a dynamic worker sandbox, so an XSS bug in vibecoded code has nothing left to leak. The whole demo ran locally on workerd, so a dead conference network cost him only the one call that needed a model.

Speaker info:
- https://x.com/KentonVarda
- https://lanparty.house
- https://github.com/cloudflare/workerd

Timestamps:
0:00 - Personal AI codegen breaks cloud infrastructure
1:16 - How feature requests die today
2:35 - The plugin system rewrite trap
3:27 - What if users could add their own features
5:11 - Gatekeeping, and why the web is the escape hatch
7:11 - Kenton Varda and Cloudflare Workers
8:39 - Gadgets as an office suite, not a deploy target
9:58 - Blueprints and the slide builder
11:03 - One gadget per document, sharing built into the platform
12:21 - Claude adds features to the app to build the slides
14:04 - Why an XSS bug does not matter here
16:22 - No containers, no database, running on workerd
17:24 - Why it is not open source yet

Quotes

"Personal AI codegen breaks traditional cloud infrastructure." (0:38)
"It's almost easier to buy a gun in the United States than it is to get access to your own phone to install unsigned software." (5:11)
"I want to know where in Claude's training data it learned that you could make words wiggle to give them emphasis." (6:33)
"The reason they're bad is entirely my fault. It's not the software's fault." (11:57)
"If you have an XSS bug, it actually doesn't end up mattering because these can't leak anything." (15:26)
