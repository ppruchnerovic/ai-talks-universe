---
id: u6q-byPWUuo
title: "From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge"
slug: from-ambient-documentation-to-clinical-intelligence
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Chaitanya Asawa"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-08-19T00:00:00Z
video_id: u6q-byPWUuo
youtube_url: https://www.youtube.com/watch?v=u6q-byPWUuo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# From Ambient Documentation to Clinical Intelligence — Chaitanya Asawa, Abridge

**Chaitanya Asawa**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=u6q-byPWUuo) · [Conference site](https://www.ai.engineer/)

## Description

Clinicians call it pajama time: the roughly two hours a day spent writing visit notes after work has finished. Abridge started there, and within two to three years the documentation product alone reached 300 of the largest health systems in the United States. Chaitanya Asawa's framing is that everything in healthcare sits downstream of a single conversation between a doctor and a patient, and that the administrative machinery got built around that conversation rather than out of it. The notes are high stakes in both directions. They are the basis of billing, and they are the context the next clinician inherits.

The engineering problem he stays with longest is evaluation, because clinical decision support leaves almost no gap between generating an answer and checking one. Sudoku is hard to solve and trivial to verify. Here, a verifier good enough to trust would already be your generator. Their approach abandons the idea of a single correct answer, since many different responses can be right. Two physicians independently write rubrics describing the elements a good response should contain, a third adjudicates those into one rubric, a fourth runs quality assurance, and only then does a judge score responses against those elements. Separate judges cover safety, adversarial boundaries and tone. On cost, at a run rate near 100 million medical conversations a year, they decompose the note into its sections and post train smaller models per section rather than running frontier intelligence over everything, betting that a dataset nobody else holds plus a narrow enough problem can outrun the frontier's rate of change.

Speaker info:
- https://x.com/c_asawa
- https://www.linkedin.com/in/casawa

Timestamps:
0:00 - Reading the room, and hearing from clinicians
2:08 - Why healthcare gets dismissed as a technical domain
2:59 - From robotics to search to healthcare
5:25 - Costs that only go up, and a productivity paradox
6:14 - Closures, thin margins, and clinician burnout
7:04 - The note after every visit, and pajama time
7:56 - Why documentation was the wedge
8:48 - Everything is downstream of the conversation
9:38 - Asking about trials and placing an order by voice
10:27 - What context the system actually reads
11:27 - Quality, latency and cost on hard mode
13:08 - Evaluation as the operating system
13:57 - Encoding clinician judgment into judges
14:48 - Contextual clinical decision support
15:38 - When the generator and verifier gap collapses
16:27 - Four physicians to build one rubric
18:05 - Cost at 100 million conversations a year
18:56 - Smaller models per section of the note
19:49 - Catching orders spoken during a visit
