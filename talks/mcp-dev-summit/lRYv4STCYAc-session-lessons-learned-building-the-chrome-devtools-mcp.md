---
id: lRYv4STCYAc
title: "[Session] Lessons Learned Building the Chrome DevTools MCP Server"
slug: session-lessons-learned-building-the-chrome-devtools-mcp
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit Europe 2025"
year: 2025
speakers: []
channel: "Agentic AI Foundation"
duration_min: 22
published_at: 2025-10-14T16:01:28Z
video_id: lRYv4STCYAc
url: https://www.youtube.com/watch?v=lRYv4STCYAc
youtube_url: https://www.youtube.com/watch?v=lRYv4STCYAc
tags: ["mcp", "model context protocol", "mcp dev summit", "mcp summit", "mcp ai"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: false
---

# [Session] Lessons Learned Building the Chrome DevTools MCP Server

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit Europe 2025` · `2025` · `22 min`

`#mcp` `#model context protocol` `#mcp dev summit` `#mcp summit` `#mcp ai`

[Watch the recording](https://www.youtube.com/watch?v=lRYv4STCYAc) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

[Session] Lessons Learned Building the Chrome DevTools MCP Server
🎤 Jack Franklin, Software Engineer - Google

Chrome DevTools is an essential tool for Web Developers to debug and analyze their websites. This includes analyzing performance, debugging CSS, inspecting network requests and much more. We are convinced that bringing Chrome DevTools functionality to AI coding agents has tremendous potential and is key to helping building performant and accessible websites with AI. In this talk we will discuss the challenges and lessons learned from building an MCP server for a complex and UI heavy application such as Chrome DevTools.

We will reflect on the challenges we’ve faced and the learnings we’ve encountered including:Picking the right technical architecture: how to build a fully featured MCP server without duplicating functionality that already exists in your applicationDescribing our tools: One of our biggest challenges is to pick tool descriptions that work equally well across different clients and models. In particular, what are good ways to describe tools that built upon each other has proven to be challenging. Optimizing responses for diverse clients: MCP servers are being used in many contexts; in sidebars of UI rich applications like VSCode or in more primitive terminal UIs with Gemini CLI and Claude Code, and we need to make sure our output is useful for all of these (for example, relying on screenshots is not useful for terminal users).

Choosing the right abstraction level: will a set of high level tools be understood and wielded more accurately than a set of low level primitive tools that a client can combine? How much should we trust the AI agent in the client to put these tools together compared to if we expose high level tools that use our AI agent in DevTools? And how do we judge which combination delivers the best results?Including user interaction: if we need the user to interact with something (e.g. set up a particular state on the page they are debugging), how do we do that? What UX patterns are beginning to emerge to balance autonomy of the AI with user interaction when required?The audience members will leave this talk with a greater understanding of the challenges involved when exposing complex functionality over MCP and an insight into the unique challenges of building this onto a large, complex application like Chrome DevTools.

✨ MCP Developers Summit EU 2025
📅 2 Oct 2025
📍 London, UK
