---
id: yqF6XhzbWBk
title: "Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo"
slug: inside-847-production-clinical-ai-notes-sebastian-fox
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sebastian Fox"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-08-22T17:00:32Z
video_id: yqF6XhzbWBk
youtube_url: https://www.youtube.com/watch?v=yqF6XhzbWBk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Inside 847 Production Clinical AI Notes — Sebastian Fox, Composo

**Sebastian Fox**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=yqF6XhzbWBk) · [Conference site](https://www.ai.engineer/)

## Description

A clinical note from a real consultation reads like a routine tension headache, and nothing in it is wrong. What never reached the page is that the patient also mentioned her jaw aches when she chews, which alongside a new headache over 50 is a red flag for a condition that can take her sight within days. Sebastian Fox pulled that error, and every other failure here, out of three leading production ambient scribes in one afternoon. In the largest real world study of these notes, roughly one in 20 carried an error serious enough to cause significant harm, nearly one in five had an important omission, and more than one in 10 contained a hallucination. Ambient scribes now run in about a third of US practices, and almost none of this surfaces as a reported incident.

The obvious fix is a checker after the generator, and Fox built the best version he had seen: a frontier model, a faithfulness rubric with worked examples, automatic rubric optimization, deterministic concept counting. One in five of the notes it waved through still hid a serious error. Verification is only cheap for the easy half, spotting what changed between transcript and note. Deciding which differences matter is tacit, contextual and always moving, so it was never written down anywhere a rubric could read. Two notes drop the same holiday detail, and France is noise while Lake Malawi is the diagnosis. His answer is to keep the standard as examples rather than specifications, discovered from real outputs and assembled per note.

Speaker info:
- https://www.linkedin.com/in/seb--fox/
- https://composo.ai

Timestamps:
0:00 - The note that looks completely fine
1:29 - The obvious errors, and how common they are
4:02 - Mapping every failure across three production scribes
5:30 - Mishearings, additions, changes, omissions
7:03 - The hard part is knowing what matters
7:56 - Put a checker after the generator
9:35 - The best judge waved a fifth of them through
12:06 - France versus Lake Malawi
13:49 - Discover, capture, calibrate
17:13 - Three judges on the same notes
18:06 - Beyond healthcare
