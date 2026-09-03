---
id: q2JrUKBMf0w
title: "The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI"
slug: the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Aparna Dhinakaran"]
channel: "AI Engineer"
duration_min: 6
published_at: 2026-07-24T20:00:06Z
video_id: q2JrUKBMf0w
url: https://www.youtube.com/watch?v=q2JrUKBMf0w
youtube_url: https://www.youtube.com/watch?v=q2JrUKBMf0w
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# The Future of Evals: From LLM as a Judge to Agent as a Judge — Aparna Dhinakaran, Arize AI

**Aparna Dhinakaran**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=q2JrUKBMf0w) · [Conference site](https://www.ai.engineer/)

## Description

Across a dozen eval jobs Arize watches the top teams run, one pattern holds: the eval has to change as fast as the agent it grades. In 2023 an agent was barely more than a prompt; since then reasoning, tool calls, and long multi step loops piled on, and every jump in capability quietly broke the eval that came before. So the evals evolved with them. Deterministic checks catch what you can define up front, LLM as a judge adds the analysis a fixed rule cannot, and the newest step, agent as a judge, hunts for failure modes you would never think to write a check for and can open a pull request to fix what it finds. Aparna Dhinakaran's argument is that this arc, from static checks to an agent grading another agent, is where evals go next.

Speaker info:
- https://x.com/aparnadhinak
- https://www.linkedin.com/in/aparnadhinakaran/

Timestamps:
0:00 - Opening: the future of the Evals track
2:06 - Why evals got harder as agents evolved
3:45 - From deterministic checks to LLM as a judge
4:36 - Agent as a judge, and where evals go next

## Transcript

*980 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=1s)** [music] >> Awesome. Well, hey everyone. My name is Aparna, one of the founders of Arize. We work with some amazing teams to help them build evals. Um, and we have an incredible lineup of talks for you all today at the evals track. Um, it's happening in room 2005 and there's going to be amazing speakers from Term Bench and Uber and Snorkel kind of all happening after this. Um, but today I'm here to talk to you about the future of evals. Evals have gone from the new skill that every PM and every AI engineer has to learn to the thing that every serious AI team is betting on.

**[0:50](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=50s)** We've been really fortunate to get to work with some of the best AI teams in the world. So, we get a front row seat into not just what's happening when they're building their actual agents and before they actually ship, but actually the evals that teams are running on their live production agent via their traces. Little bit of some stats for you guys. We run over 100 million evals every month. The average team runs about 12 different eval jobs with the top teams running over 3,800 different evaluators. And offline evals, online evals, they each have their own place, but today what I'm actually going to talk to you about is the teams that are running evals on their traces. This is actually what's helping teams figure out what's working, catch their failures, and that's the type of data

**[1:38](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=98s)** you need to fuel your continual learning loops. And the industry kind of agrees. I mean, all the CPOs of Anthropic, OpenAI, all you know, GDB, you have Garry Tan saying, "Evals are everything you need." And the whole industry kind of agrees. So, we added evals, they catch all the failures right? Here's the problem. When we were building all of these first-gen evals, the thing that we were actually evaluating has changed underneath us. In 2023, it was about just answering a prompt. In 2024, we started to see all the frontier models. They've added tool calls, they've added reasoning, they've added deep research. Now, what we have is teams running loops on real-world data with sub-agents kicked off on

**[2:28](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=148s)** long-horizon tasks. Every one of these was actually a massive jump in complexity, and we didn't just make the problem harder, we actually got a fundamentally different type of problem. What that meant is that as these systems got more complex, so did the way that they actually fail. We're really lucky cuz we have our own agent that we've built, Alex, that lives in our UI, and we get our kind of get to feel this pain ourselves. Every time the frontier labs added new functionality, we added it to our agent. And now Alex can has much longer memory. It has the ability to create dynamic UIs. It can go search across an enormous volume of traces. But, we also realized that it would forget context. It wouldn't know when something was done. Um sometimes it would just get stuck in

**[3:16](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=196s)** these loops. And the key thing here is that the classical LLM as a judge evals, that probably many of you have written in this room, just weren't for us to be able to catch all the types of failures that we were experiencing. I mean, it's just fundamentally different, right? You have a deterministic flow, and now what we have is literally every time a user interacted with Alex, it would create a new UI. That's a fundamentally different trajectory. So, this led to our really big revelation. What if the best way to an evaluate an agent was actually with an agent. Doesn't mean that all of the ways that we did evals, with deterministic evals, with LLM as a judge, classic evals, doesn't matter anymore, but it just

**[4:03](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=243s)** means that we have a different type of tool to solve a different type of problem. Agent as a judge is about adaptive dynamic analysis. LLM as a judge just gives you a fixed rubric with these fixed scores. It's what everyone's doing, but when your agent's doing completely different trajectories every time a user puts in data, it just means that you need a fundamentally different type of eval. My take is that most teams today are doing the first two, but the future of evals is actually having all three. And today I'm actually excited to share we've released agent as a judge to help our teams on their eval journey. We've released signal. Signal's actually a long-running agent that can read traces sent in, discover patterns of issues.

**[4:51](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=291s)** Um, it can figure out types of problems that a classical LLM as a judge eval just would never be able to do with these deterministic rubrics. It's helped us figure out very subtle failures that you wouldn't even think of doing, such as something going on in a loop for multiple times, it was calling the same tool for repeatedly long time, the trajectory was inefficient. And actually what this does is because it has all that analysis, it can go put up a PR and put up a fix. So, if you want to learn more, come to our come to our booth. We're right by the OpenAI booth. We'll give you a demo, we'll show you a bit more about it. We're also, like I said, taking over the evals track, so come to room 2005. We're going to be talking a lot about the future of evals and what they look like. And if you just want to hang out with

**[5:39](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=339s)** our team, we're throwing a viewing party for the USA World Cup game tonight, so check out the Luma and register to come join us. Awesome. Thank you all so much. >> [music] [music]
