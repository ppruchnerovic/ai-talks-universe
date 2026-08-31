---
id: ZIYYsAzaLlA
title: "Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma"
slug: building-the-engine-while-flying-the-plane-launching-the
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Jesse Lumarie"]
channel: null
duration_min: 17
published_at: 2026-08-28T00:00:00Z
video_id: ZIYYsAzaLlA
youtube_url: https://www.youtube.com/watch?v=ZIYYsAzaLlA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Building the Engine While Flying the Plane: Launching the Figma MCP Server — Jesse Lumarie, Figma

**Jesse Lumarie**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=ZIYYsAzaLlA) · [Conference site](https://www.ai.engineer/)

## Description

Figma did not have 20% projects. Jesse Lumarie gave one to the MCP server anyway, one day a week, because he had seen an internal demo and wanted non designers to be able to pull from Figma. That side project became the company's first MCP server in about three months, and then one of the fastest growing products Figma has ever shipped. The build happened while the ground moved. Weeks in, a new version of the spec deprecated the transport they had chosen, and client support was so uneven that a compatibility matrix was a real artifact they maintained.

The interesting decisions are about representation. Figma's canvas is a scene graph in C++, close to the HTML DOM, and they had three ways to hand it to a model. They picked React and Tailwind on a hunch that models had seen the most of it, and the output is pixel perfect. Passing images inline as base64 blew up the context window and got cut. Pixel perfect turned out to be only half the problem, because an enterprise does not want a beautiful generated button, it wants its own accessible internationalized one, so Code Connect sends a pointer to the real component instead of markup. Two hours grading an eval by hand in a spreadsheet convinced them never to do that again, and evals now run hundreds of times a week behind LLM judges.

Speaker info:
- https://x.com/jesselumarie
- https://www.linkedin.com/in/jesselumarie/

Timestamps:
0:00 - A 20% project at a company without 20% projects
2:02 - Uneven client support, and a spec that moved
2:55 - What the local server gave developers
3:52 - Three ways to represent a scene graph
4:47 - Why images alone did not work
5:40 - Grading evals by hand, once
7:32 - Code Connect, and why pixel perfect is not enough
9:24 - Elicitation and sampling, and hacking around them
13:55 - Shipping local first, then remote
15:43 - How early all of this still is
