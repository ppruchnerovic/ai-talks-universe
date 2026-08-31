---
id: VBCDhRrvlYo
title: "The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu"
slug: the-next-game-engine-won-t-have-a-manual-arturo-nunez-nereu
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Arturo Nunez"]
channel: null
duration_min: 20
published_at: 2026-08-18T15:00:29Z
video_id: VBCDhRrvlYo
youtube_url: https://www.youtube.com/watch?v=VBCDhRrvlYo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# The Next Game Engine Won't Have a Manual — Arturo Nunez, Nereu

**Arturo Nunez**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VBCDhRrvlYo) · [Conference site](https://www.ai.engineer/)

## Description

Ask a coding agent for a camera that follows your character and it will reinvent that camera from scratch, every time, slightly differently. Arturo Nunez's diagnosis is that the context sits on the game engine's vocabulary rather than the game's. Controlling a character in a conventional engine means a mesh, a renderer, an animator, a rigid body, a collider, an audio source, and only then your actual movement logic, nearly all of which is boilerplate that every character in every game already carries.

Nereu inverts that. Everything is an asset, and you attach tags describing intent instead of implementation: character, animated, double jump. Systems then query by tag and move everything marked vehicle and drivable, which is Entity Component System thinking lifted from data oriented design. The pleasant consequence is that nothing stops you tagging a building as drivable and dropping it into a Mario Kart style race. The assistant is there to get you unstuck rather than to one shot a finished game, and the vocabulary it expects is the one tutorials already use: press A to jump, press A again in the air.

The engineering detail worth stealing is how context gets assembled. Rather than feed the whole scene to a model, he borrows level of detail from rendering. Assets near whatever you are editing arrive with their full tag values, distant ones collapse to a position and a type, and the hundred pieces of grass are simply left out.

Speaker info:
- https://x.com/arturonereu
- https://www.linkedin.com/in/arturonereu/
- https://www.arturonereu.com/

Timestamps:
0:00 - Building a game live by describing it
2:45 - Why making games is hard
4:27 - Ten years at Unity watching the same struggles repeat
6:59 - Powerful engines and LLMs that still do not compose
7:49 - The boilerplate behind controlling a character
8:45 - Everything is an asset, and tags describe intent
9:37 - The asset tag system, and tagging a building as drivable
11:21 - How the prompt gets its context
14:52 - Level of detail, applied to context assembly
16:37 - Getting unstuck rather than one shotting a game
17:28 - World models are a different medium
