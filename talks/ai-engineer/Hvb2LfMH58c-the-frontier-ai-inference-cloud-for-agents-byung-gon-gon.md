---
id: Hvb2LfMH58c
title: "The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI"
slug: the-frontier-ai-inference-cloud-for-agents-byung-gon-gon
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 15
published_at: 2026-09-19T18:00:03Z
video_id: Hvb2LfMH58c
url: https://www.youtube.com/watch?v=Hvb2LfMH58c
youtube_url: https://www.youtube.com/watch?v=Hvb2LfMH58c
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Inference, serving & GPU infra"]
transcript: true
---

# The Frontier AI Inference Cloud for Agents — Byung-Gon (Gon) Chun, FriendliAI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Hvb2LfMH58c) · [Conference site](https://www.ai.engineer/)

## Description

Byung-Gon Chun's team invented continuous batching, now standard across the industry, and the work that followed inspired one of the most widely used open source serving frameworks. So when he says agents have changed the economics of inference, he knows the tooling from the inside. His demonstration: the same coding agent, the same task of building a tower defense game, run once on a closed frontier model and once on an open weight model. Both finished at a usable level. The open weight run came in roughly five and a half times cheaper. That is the promise of open weights. But the model is only part of the bill, because agentic inference is a different problem from chat.

In chat the unit was the request. In an agent the unit is the task: a loop of plan, act, observe, repeat, often running for minutes or hours, with sub agents fanning out in parallel and every observation appended to a context that only grows. His internal traces show consecutive steps sharing enormous prefixes, and recomputing that prefix on every call is compute spent on work already done. Nobody cares about the latency of one call; they care when the task is done. FriendliAI rebuilt its stack around that metric. Prefix caching so a shared prefix is computed once. A hierarchical KV cache across GPU, host memory and disk. Cache aware routing that sends a request to the replica already holding its prefix, instead of spreading load evenly and destroying locality. And agent aware scheduling that knows a call belongs to a longer program. One customer's split test found it seven times faster with a lower error rate.

Speaker info:
- https://www.linkedin.com/in/byung-gon-chun
- https://bgchun.github.io

Timestamps:
0:00 - The team that invented continuous batching
2:06 - One task, two models, one bill
3:18 - The unit is the task, not the request
5:25 - Consecutive steps share a huge prefix
7:02 - Four pillars of an agentic inference cloud
9:19 - Cache aware routing versus a naive load balancer
10:04 - Agent aware optimization
11:00 - The same task, end to end, on two providers

## Transcript

*1,806 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=13s)** Let's uh get started. Uh hi everyone. Thank you for coming. Uh this is the late afternoon in the last day. Um so I really appre appreciate it. I'm gone, founder and CEO of friendly AI. Today I want to talk about agentic inference. So I'll first walk through what changed uh why it matters and how we rebuilt the inference cloud for agents. Before we go deeper let me briefly introduce friendly AI. Friendly AI is the frontier AI inference cloud for agents. So we run inference for agents at scale faster, cheaper and more reliably. We are born from a research team at S National University and those research roots still define us. We are

**[1:03](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=63s)** the team that invented continuous batching. The inference optimization that is now standard across the industry and our orca work inspired 3LM a widely used open source framework. Today we operate globally headquartered in San Francisco with a team in soul to scale frontier inference. As you know 2026 is a year agents go into massive production and it's driven by two trends coming together. First agents are going exponential. AI agents are driving explosive adoption across software operations and knowledge work. Second, open rate motors have reached the frontier and make agents economic. They now rival closed frontier motors in

**[1:53](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=113s)** capability, which means you can run frontier quality agents on open motors with much lower token cost. Let me make the openweight motor part concrete. Open weight motors are now strong enough for these types of real agentic workflows. Here we gave the exact same task building a tower defense game with a coding agent to two models. On the left is GLM 5.2 an openw rate motor running on friendly AI. On the right is anthropics opus 4.8. The important point is not that the outputs are identical. The point is that both complete the task at a level that is clearly usable for many agentic workflows. Open weight models have

**[2:42](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=162s)** crossed the quality threshold but the economics are very different for the same task. Opus 4.8 cost about a $150 GLM 5.2 unfriendly AI cost 27 cents about 5.6 times cheaper. So this is the promise I mentioned earlier. Open rate models give you frontier quality agents at a fraction of cost. But motor cost is only one part of the story. To make agent actually fast and reliable, the inference stack itself has to change. So let's look at what actually happens inside an agentic workload. So first let's look at changes in the

**[3:30](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=210s)** workload. In the past the dominant usage was chat. The basic unit was a request. A person asks a question, the model answers and the person reads it. Latency meant how fast did I get one response. Agents are different. The basic unit is a task. A task may involve many model cores, many tool cores and it may run autonomously for a while. So the user does not really care about the latency of one individual request. The user cares about when the whole task is completed. That means we have to optimize for tasks, not just individual requests. Let's look at agent workflows more

**[4:18](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=258s)** closely. An agent really runs a session made up of tasks. Each task typically runs in a loop. First, it plans, which usually means an LLM call. Then, it acts maybe by calling a tool. Then it observes the result and adds the that back into the context and it repeats this until the task is done. So we are constantly alternating between LLM inference and one or more nonLM tool executions. So there is a gap between LLM calls. An agent can also create sub agents and run them in parallel. Agent inputs also look very different from chat. The graph here shows the

**[5:05](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=305s)** prompt and completion length distributions of our internal coding agent runs with GLM 5.2 which we use day-to-day. They are much longer. They grow as the task progresses since every observation gets appended back into the context. There's an important pattern here. Consecutive agent steps usually share a huge prefix. If we recomp compute the same prefix every time, we are burning a lot of compute on work we already did. So this is one of the biggest opportunities in agentic inference. So how token hungry are agents? Now let's look at a long horizon task example like deep research.

**[5:54](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=354s)** We ran explained the spec decoding framework in VLM using code with GLM 5.2 unfriendly AI. There are multiple stages and each stage is composed of sub agents which run multiple inferences and tool cores. So it might run tens or even hundreds of inference steps sometimes over minutes or hours and the shared context keeps going the whole time. For the user what matters is not the latency of a single token or one core. What matters is when is my test completed. So agent inference is not just chat with more requests. It's a different problem. The context grows over time. Tour work

**[6:44](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=404s)** is interled between model cores. The number of model cores depends on the input. So you can't really plan around a fixed request rate plan. And the real metric is end to end test latency, not a single request latency. This is where friendly AI comes in. We rebuilt the frontier inference cloud specifically for agentic goal close around the challenges I just walked through and we set one goal optimize end to end test latency the task not just the request. So how do we do that? Let me show you the key engineering behind it. Here's the engineering map for how we think about it. We built the stack layer by layer around agent workflows. There

**[7:34](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=454s)** are four big pillars I'm going to cover today. Prefix caching key value in short KB cache management, cash aware routing, agent aware optimization and of course underneath we need model layer optimization like sparse attention for long context techniques to reduce errors, fast corners, resilience serving and more. In this talk, I'm going to focus on the four pillars. Let's start with prefix caching. Since Asian steps share a large prefix, we compute key value for that prefix once and cache it. Then on later steps, we reuse the cache key value and only process the new suffix.

**[8:24](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=504s)** Reading from cache is much cheaper than recmp computing prefill. So this improves time to first token and reduces compute on every step. And the longer the task runs in agents, the more valuable this becomes. But caching only works if the KV cache actually fits and can move around efficiently. So we need strong KV cache management. We use frugal memory management to pack more active context onto each GPU memory. We use KB contigation to reduce the memory footprint. We you we use hierarchical caching across GPU memory, host memory and disks. So we can go beyond GPU limits.

**[9:14](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=554s)** And we also use distributed caching. So one prefix can be served across replicas, not just inside one instance. At global cluster scale, routing becomes really important. A knife load balancer may spread requests evenly across GPU clusters, but it can destroy cache locality. A cache aware router at a global scale does something smarter. It sends a request to part that already has the right prefix cached turning a cord prefill into one cache ship. At the same time, it still has to balance load. So one part doesn't become a hot spot. In this example, the two requests of task A go to the same part one for cache

**[10:04](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=604s)** locality. The next piece is agent aware optimization. And this is the next fronture of agentic inference. Today, most systems schedule each LLM core as if it were independent. They don't really understand that this core is part of a longer agent program. But if the optimizer knows the agent level context, we can make better decisions. For example, preempting the right work, speculatively prefilling context for an unlikely next step or making a better cache eviction decision based on agent level context. So the goal is to reduce ant latency not

**[10:53](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=653s)** just make one call look fast. When we put all of this together, this is the payoff. We are using the same model GLM 5.2 with kilo code to create a simple mobile game. We ran the same task with model APIs of friendly AI and another well-known inference provider. As you can see, friendly completes the same task end to end tox thanks to our Asenticentric cloud design. So what does this unlock in practice? a stronger production agent stack. Take an agent you already like. Now plug in openweight frontier models like GLM 5.2, Minimax and Kimi served on friendly

**[11:43](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=703s)** AI. The motor gives you frontier quality capability and better economics. Friendly AI gives you the speed, reliability and endtoend test performance needed in production. That combination quality speed reliability, and cost is what makes agents actually useful and economical in production. Friendly AI is currently powering teams in production from AI native startups to global enterprises. I'd like to highlight a couple here. Hilo is a hugely popular Asantic AI coding tool serving millions of users. LG is a global enterprise whose businesses range from electronics to

**[12:32](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=752s)** healthcare to energy. Very different companies, but they all need the same thing. Fast, reliable, cost effective agentic inference. This testimonial from our client Kilo says it all. Over the past year, Kilo Code has tested several inference providers hosting both open and closed models. In a split test of GLM5 usage compared against other thirdparty providers and direct usage from the model lab G.A.I., Friendly AI was consistently seven times faster with a significantly lower error rate. Today, friendly AI is a core component of the killer stack. And you can consume this however fits

**[13:22](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=802s)** your stack. Model API is the fastest way to start. Core frontier open weight models through our serless API. Dedicated endpoints give you your own isolated deployment with guaranteed SLAs's for production workloads. And BYOG bring your own GPU lets you run friendly inference on your own infrastructure. Same stack, three ways to deploy. To wrap up, there are three things to remember. First, frontier open weight models make production agents economically scalable. Second, agents are not just chat with more cores. Agentic inference requires optimizing end to end task latency with the challenges I mentioned.

**[14:10](https://www.youtube.com/watch?v=Hvb2LfMH58c&t=850s)** Third, friendly AI is built as an inference cloud for that word. Fast, reliable, cost effective agentic inference. Thank you for attending my session. If you're building agents, give uh frontier openweight motors a try on friendly today. You can get started at friendly.ai in minutes. And uh thank you. I'll be around after the session. Um thank you. >> [applause] [music]
