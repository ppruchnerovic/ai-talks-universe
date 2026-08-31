---
id: 03l29gJXpCE
title: "Guide, Verify, Solve — Anirban Chatterjee, Sonar"
slug: guide-verify-solve-anirban-chatterjee-sonar
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Anirban Chatterjee"]
channel: null
duration_min: 23
published_at: 2026-08-09T17:45:13Z
video_id: 03l29gJXpCE
youtube_url: https://www.youtube.com/watch?v=03l29gJXpCE
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Guide, Verify, Solve — Anirban Chatterjee, Sonar

**Anirban Chatterjee**

`AI Engineer` · `AI Engineer` · `2026` · `23 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=03l29gJXpCE) · [Conference site](https://www.ai.engineer/)

## Description

A Carnegie Mellon study sorted GitHub projects by whether an AI tool wrote the code, and found the productivity gain ran out after about three months while the static analysis warnings and the added complexity stayed. That residue is verification debt, and how much it costs scales with criticality: a short lived internal tool can live with the gap between the quality a model gives you and the quality the application needs, a large codebase with adversarial users cannot. The obvious backstop is human review, and a Wharton study suggests it leaks badly. Participants took the AI's advice 92.7% of the time when it was correct, and still followed it nearly 80% of the time when it had been instructed to lie confidently.

Anirban Chatterjee's argument is that the check has to be zero trust and multi layered. Zero trust means assuming the code could have come from anywhere and verifying it by a different method than the one that wrote it, since a model grading its own output inherits its own blind spots. Multi layered means computational review running alongside reasoning based review, because no single technique catches syntax, data flow, architecture and control flow at once. Sonar's leaderboard makes the blind spots concrete: across their metrics one Claude model rates well on correctness and reliability while the other is the better choice when maintainability, security or lower complexity is what matters. The loop he proposes wraps generation on both sides, handing the agent architectural constraints and coding standards before it starts, running verification inside the inner loop so issues get fixed before they propagate into later loops, and giving the agent the tools to remediate what comes back instead of queueing it for a person who is already rubber stamping too much.

Speaker info:
- https://www.linkedin.com/in/anirbanc/
- https://www.sonarsource.com/the-coding-personalities-of-leading-llms/leaderboard/
