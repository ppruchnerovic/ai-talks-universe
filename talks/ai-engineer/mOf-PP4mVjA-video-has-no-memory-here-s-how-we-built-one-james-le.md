---
id: mOf-PP4mVjA
title: "Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs"
slug: video-has-no-memory-here-s-how-we-built-one-james-le
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["James Le"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-07-23T02:00:03Z
video_id: mOf-PP4mVjA
youtube_url: https://www.youtube.com/watch?v=mOf-PP4mVjA
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Video Has No Memory. Here's How We Built One. — James Le, TwelveLabs

**James Le**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=mOf-PP4mVjA) · [Conference site](https://www.ai.engineer/)

## Description

Feed it 67 videos from the 2022 World Cup and ask for the near misses, the shots that almost scored but did not, each with a reason, and it returns them. Ask it to track Messi across the entire corpus and describe the camera framing, and it finds the moment he slaloms past a sliding defender. James Le's point is that this is unusual because video has no memory. Almost every video AI system answers each query from scratch, and a bigger context window does not fix it, because the real problem is that there is no durable representation to retrieve into.

His fix is to stop treating video as a bag of frames and start treating it as a spatial temporal volume, then build a memory layer over it: a context graph of time bounded moments, the entities and where they appear, the relationships between them, and corpus level themes. At TwelveLabs that is an embedding encoder, a context store, and a video language model exposed as an API. The design rules are blunt: ingest once and reason many times, store primitives not answers, ground every claim to a timestamp, and let intent decide what to remember, because brand safety and sports highlights need different things from the same footage.

Speaker info:
- https://x.com/le_james94
- https://www.linkedin.com/in/khanhnamle94/
- https://jameskle.com/

Timestamps:
0:00 - Video has no memory
0:50 - Video is a spatial temporal volume, not a bag of frames
2:06 - Three problems: wrong context, wrong memory, weak reasoning
3:36 - Five properties that make video memory hard
4:53 - The TwelveLabs stack: Marengo, the context store, and Pegasus
5:56 - Search versus memory
7:48 - The context graph
9:04 - Five design principles for a video memory layer
10:45 - From a static model to a video worker
12:51 - Demo: sports and tracking Messi across the World Cup
15:37 - Demos: traffic security and ad placement
