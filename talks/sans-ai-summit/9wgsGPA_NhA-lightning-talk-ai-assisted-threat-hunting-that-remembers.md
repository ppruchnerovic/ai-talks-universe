---
id: 9wgsGPA_NhA
title: "Lightning Talk: AI-Assisted Threat Hunting That Remembers"
slug: lightning-talk-ai-assisted-threat-hunting-that-remembers
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "AI security"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 6
published_at: 2026-05-04T19:13:28Z
video_id: 9wgsGPA_NhA
url: https://www.youtube.com/watch?v=9wgsGPA_NhA
youtube_url: https://www.youtube.com/watch?v=9wgsGPA_NhA
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
topics: ["Security, safety & red teaming"]
transcript: true
---

# Lightning Talk: AI-Assisted Threat Hunting That Remembers

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `6 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=9wgsGPA_NhA) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

Designing AI-Assisted Threat Hunting That Remembers

🎙️ Sydney Marrone, Head of Threat Hunting, Nebulock
📍 Presented at SANS AI Cybersecurity Summit 2026

Threat hunting teams struggle to reuse prior investigations, which leads to repeated setup work, inconsistent results, and limited benefit from AI tools that lack durable context. Early attempts to add AI often fail because hunts are unstructured, state lives in scattered notes, and models have nothing reliable to reason over.

This talk presents a CLI-first approach to threat hunting that captures hypotheses, assumptions, and outcomes as structured artifacts and uses that data to support AI-assisted recall and reasoning. Instead of prompting chatbots, teams integrated AI into the hunting workflow itself, allowing it to reference past hunts, surface related investigations, and suggest next steps while analysts remained in control.

After adopting this approach, teams reduced hunt restart time, improved analyst handoffs, and increased reuse of prior investigations. AI moved from a novelty to a practical assistant, with measurable gains in speed and consistency and clear lessons learned around integration pain, workflow changes, and where AI did not help.

Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

## Transcript

*870 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=0s)** All right, quick show of hands. Who here has started investigation or a threat hunt, passed it off to someone else, and basically watched them start from zero? Many of us, and that's what this talk is about. AI is supposed to make threat hunting faster, but if you lose memory after every session, your AI or your threat hunting is not getting faster, your threat hunting partner is not getting faster, and it's basically like a fancy search bar. The core problem is that your investigation state lives in Slack threads, your personal notes, or the head of the analyst who is just clocking off the shift. Once the analyst gets off the shift or a AI session starts fresh, you lose all your context.

**[0:51](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=51s)** And that's a big problem. The next analyst has to rerun the queries, they have to redistribute the the false positives. 45 minutes later, they're back to where they started. And this isn't an AI problem, this is a context problem. We're not giving our tools the resources and the memory that they need to really do threat hunting. Now on the left of the slide is what AI typically sees. It's just a blank box. When you drop into a hunt, you get nothing. Now on the right is what your team actually knows. So we have various hunts connected to different tactics and techniques, different queries, logging, various uh true positives and false positives that

**[1:38](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=98s)** were found. All of this is inside someone's head. And AI can't read minds, at least not yet. So, we need to get that information out and get that knowledge written out somewhere so that we're not prompting into the void. And it's simpler you think. And this is exactly why the agentic threat hunting framework was built. This is a framework that I built last year in December and released it via GitHub. It's open source, vendor agnostic, and it's a way for you to bring AI into your threat hunting processes. The framework is has a maturity model, so you can start from nothing and then build up to being more agentic.

**[2:26](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=146s)** It also has a uh pattern that you can follow or even your AI can follow to be able to threat hunt. It comes with a CLI, which uh you can use something like ATHF similar Kerberoasting and semantically see similar hunts [snorts] that have already been executed by your team. The true positives, the false positives, the dead ends that they executed, you can find them all very easily or AI can even find them all. AI can actually reason over files, not memory. So with this, you the basis of the framework is going to be a file, a structured file, and it has three things. It has a hypothesis, which is what you what the adversary is doing in your environment and you're going to try to confirm or refute it. It has your queries that you executed,

**[3:14](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=194s)** doesn't matter what language, and it also has the results. This is the base of the framework and what everything builds upon. So the framework really has a a big structure to it that is based around all these files. So let's talk some numbers real quick. Hunt restarts. So you start a hunt, you pass it off to someone else, or someone else tries to read your notes, and you're trying to get up to speed. 45 minutes. This goes down to five after implementing the framework. Now duplicate hunts. When you have two analysts who are unknowingly running the same threat hunt or investigation at the same time or maybe one ran one six months ago and is running it again.

**[4:03](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=243s)** That goes from happening all the time to being very rare. And lastly, handoff quality. This is going to depend on your team, but you might hand off in Slack threads, you might hand off in Google Docs, or even Jira comments. How much is it to go through all those Jira comments and see what actually happened? So, it goes from variable to much more consistent because you're actually using a file. The file is the handoff. And those files build upon each other. And that building of the files leads to more and more context. So, I have three key takeaways. You don't need the full system from day one. The framework has a lot to it. Start small.

**[4:51](https://www.youtube.com/watch?v=9wgsGPA_NhA&t=291s)** Don't let perfect be the enemy of started. Two, start with file a file. A threat hunt file that is structured with those three things. Remember, a hypothesis, your queries, and then your results. The memory compounds. That's the last one I want to leave you with. So, um a team that implemented this six months ago is going to be way ahead of a team that implemented today because they have all those files that have compounded into context and memory that they can use for future. My name is Sydney Maroney. I'm the head of threat hunting at Nebulon. And if you want to know more about the agentic threat hunting framework, go ahead and check out our site or scan the QR code. Thank you.
