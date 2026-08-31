---
id: V_5bn4q-vAI
title: "How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth"
slug: how-we-got-llms-to-recommend-our-open-source-library
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Christopher Burns"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-08-26T15:30:07Z
video_id: V_5bn4q-vAI
youtube_url: https://www.youtube.com/watch?v=V_5bn4q-vAI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# How We Got LLMs to Recommend Our Open Source Library — Christopher Burns, Inth

**Christopher Burns**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=V_5bn4q-vAI) · [Conference site](https://www.ai.engineer/)

## Description

Their onboarding form asks how you heard about us. On April 13th the answers started spiking, and the single largest source of inbound for c15t is now an LLM telling someone to install it. Christopher Burns is not a researcher and says so twice. He founded Inth, built c15t, the open source consent banner library, and reckons he has been hacking on this only slightly longer than the room has. The Collison brothers used to install Stripe by taking your laptop off you; going through Y Combinator, Burns found himself handing people a prompt instead. Good developer experience primitives turned out to be agent primitives. No single trick covers it, so the optimizations got abstracted into a framework neutral docs pipeline that generates the agent facing files from MDX.

The rest is practical. Write llms.txt by hand rather than generating it, because forty good lines beat a thousand lines of noise. Agents fetch, they do not browse, so hand them links and a line on what each page is for. Serve markdown instead of HTML, three ways, since not every agent can set a header: a .md suffix, content negotiation, and a query parameter. The part Burns thinks matters most: coding agents mostly never open your documentation site. They read the repository and node_modules, working from stale training data and compiled source. Ship bundled markdown and an AGENTS.md inside the package and he measures close to half the tokens saved. He closes on a caution he applies to his own slides: the ground moves weekly and nothing stays perfect.

Speaker info:
- https://x.com/burnedchris
- https://www.linkedin.com/in/burnedchris
- https://github.com/burnedchris
- https://burnedchris.com

Timestamps:
0:00 - Not a scientist, just hacking on it
2:23 - The spike, and where the inbound came from
4:20 - No single fix, so they built a docs pipeline
5:52 - Write llms.txt by hand, not generated
7:07 - Ship markdown instead of HTML
9:17 - Web MCP: letting an agent ask your docs
10:09 - Agents never visit your site, they read node_modules
12:53 - Testing whether your site is agent ready
14:36 - Q&A: where to start on a plain website
