---
id: iQ5xldZ9StU
title: "Realtime multiplayer, automation, and you! — Idan Gazit, GitHub"
slug: realtime-multiplayer-automation-and-you-idan-gazit-github
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Idan Gazit"]
channel: "AI Engineer"
duration_min: 22
published_at: 2026-08-08T21:30:06Z
video_id: iQ5xldZ9StU
youtube_url: https://www.youtube.com/watch?v=iQ5xldZ9StU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# Realtime multiplayer, automation, and you! — Idan Gazit, GitHub

**Idan Gazit**

`AI Engineer` · `AI Engineer` · `2026` · `22 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=iQ5xldZ9StU) · [Conference site](https://www.ai.engineer/)

## Description

Idan Gazit's personal site runs on Astro, which ships often enough to keep him permanently on the upgrade treadmill, so he wrote an agentic workflow in about three lines of plain English, the kind of message you would send a teammate. Copilot expanded it into a full playbook: check for new releases, read the changelog and upgrade guide, apply the changes, open a pull request. It then carried him from Astro 5 to Astro 7, two major versions at once, found and fixed the code that broke, verified the build, and flagged the manual steps it could not take itself. The workflow is a Markdown document. The YAML actions file is a compiled artifact nobody reads, so changing how the automation behaves means editing the English.

The guardrails are the part he wants remembered. Prompting an agent to behave is not a guardrail, because anyone who can prompt inject it can undo the instruction, and you have let the fox into the henhouse. Permissions, allowed tools, reachable network destinations and safe outputs get declared deterministically in front matter instead. His upgrade workflow may open exactly one pull request, and is explicitly allowed to do nothing at all, since an automation that cannot stay quiet turns into a denial of service against its own owner. Secrets stay outside the agent's jail entirely, because a secret an agent can see should be treated as already compromised. The second prototype, ACE, runs every session in a cloud microVM and deliberately resembles a chat app, on the theory that what belongs in the shared surface is everything not already in the code: the political constraints, the infrastructure deal that quietly picks your cloud provider, the plan two people edit together before telling the agent to go make the document true. He ends on a study of around a hundred developers over thousands of hours which found that hands on keyboard typing is about 5% of the work, and that is the only 5% the tools have helped with so far.

Speaker info:
- https://twitter.com/idangazit
- https://linkedin.com/in/idangazit
- https://githubnext.com
