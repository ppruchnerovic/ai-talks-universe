---
id: irMWadaKV2g
title: "Wenbo Guo: OpenSage: Next Generation of Agentic AI"
slug: wenbo-guo-opensage-next-generation-of-agentic-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: []
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-12T01:45:27Z
video_id: irMWadaKV2g
url: https://www.youtube.com/watch?v=irMWadaKV2g
youtube_url: https://www.youtube.com/watch?v=irMWadaKV2g
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Wenbo Guo: OpenSage: Next Generation of Agentic AI

**Speaker not identified**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=irMWadaKV2g) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,329 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=irMWadaKV2g&t=2s)** WENBO GUO: OK. Cool. Nice to meet everyone. I'm Wenbo Guo. I'm currently an Assistant Professor at UC Santa Barbara. Also, a Research Scientist at Meta MSL. Today I will talk about our recent work OpenSage, which is a new agent framework where we think could be the future of agentic AI. Before we talk about OpenSage, let's look at the current agent world, how people build agent. So basically, the idea is there's pre-specified agent structure, agent topology, and also tool set memory structure before you build an agent. It's kind of like you build a software. You know exactly what you want to build. You have a clear kind of system design. And then we build agent, and then we

**[0:49](https://www.youtube.com/watch?v=irMWadaKV2g&t=49s)** let the agent run the job. But if we dive in and think about the limitation of this paradigm, the problem is if we do pre-specified topology, and also we pre-specify the set of tools, that constrains the generalizability of the agent a lot because the reason is, we want agents to do complex, long-horizon job, but sometimes agent may spawn its own sub-agent along the way of execution. Along the way of execution, agent may find out, oh, the set of tools I have is not enough. I need to invent. I need to be added for more tools to finish more complex jobs. But if everything is pre-specified, it can constrain the agent capability or generalizability a lot. So that's motivated us to design OpenSage, which we think

**[1:40](https://www.youtube.com/watch?v=irMWadaKV2g&t=100s)** is what we call Agent 2.0. [INAUDIBLE] is the Agent 1.0. So basically, similar as we design the machine learning models, if we think about it, 10 years ago or even 20 years ago, when we design machine learning models, the first step we're going to do is feature engineering. So we need to think about, given raw data, what are the features we use, how to extract feature sets from the model or from the raw input. And then there are so many feature engineering methods that's kind of adding our human knowledge, or what we call inductive bias, into the model. But then, people found out, we don't need that step. You just train the deep neural network model on the raw data. The model will figure out by itself and actually there, without the inductive bias, constrain the search space of the model.

**[2:31](https://www.youtube.com/watch?v=irMWadaKV2g&t=151s)** The model can actually search for better solutions in a larger search space. So that's kind of here, we think about similar. What if we don't build an agent? What if we don't do all those kind of manual feature engineering, like pre-specify the workflow, topology, tool sets. What about we just build a minimal set of scaffold that enable the agent to build its own agent? For example, we enable some initial tools for the agent so the agent knows, along the way, the agent can spawn its own sub-agent, design its own workflow topology, write its own tools, or even write its own memories. So that's the idea behind OpenSage, is to really unleash the power of AI when building agents. Basically, we want something like AI-built AI, agent-built agent.

**[3:19](https://www.youtube.com/watch?v=irMWadaKV2g&t=199s)** To do that-- huh? Sorry, it's not working. Sorry, clicker is not working. OK. Now it's back. So as you can see, what we want is we want to provide a minimal set of scaffolding that enables agent to build its own agent, including write its own topology, workflow, write its own tools, and also design its own memory. So for the sake of time, I skip the technical detail. Basically, we redesign the whole ADK, what we call agent-designed toolkit-- oh, that's good-- to be able to enable the agent to explore its own topology, write its own tools

**[4:12](https://www.youtube.com/watch?v=irMWadaKV2g&t=252s)** along the way of execution. So here's a comparison between our OpenSage with Google, OpenAI, all those frontier agent developer kits on this new capability. As we can see, that's why call OpenSage as Agent 2.0. That's really the next generation of agent construction framework that enables all these capabilities-- freedom, flexibility, existing [INAUDIBLE], existing ADKs able to offer. And then let's look at the performance. So here, when we test OpenSage on coding and also cybersecurity-related benchmarks, this is our performance compared to Claude Code and also Codex. By the time we release OpenSage--

**[5:02](https://www.youtube.com/watch?v=irMWadaKV2g&t=302s)** that was about February this year-- as you can see, on all these existing benchmark, like notebook benchmark, like CyberGym, Terminal-Bench, SWE-Bench Pro, and DevOps-Gym, OpenSage was able to outperform all existing agent frameworks. This number is a little bit outdated. OpenSage is still evolving. We are also seeing new performance on these benchmarks as well. Another kind of recent trial we feel very exciting is we actually run OpenSage on the real-world CTF game for. For those of you who know about it, we run it against the DEFCON 2026 qualification game. That's kind of considered Olympic in the world of offensive security. It's most challenging security kind of competition. All that typically requires a team of professional hackers

**[5:54](https://www.youtube.com/watch?v=irMWadaKV2g&t=354s)** working 48 hours. Sometimes there's teams with hundreds of hackers working on all these challenges, try to solve them. What we do is that we try OpenSage on 15 of the noninteractive challenges because, actually, the organization kind of doesn't allow the AI to solve the challenge submitted. So what we do is we run in parallel at the same time as the challenge is released. So in total, on 15 challenges, we are able to solve some of them. And after we do a post-hoc analysis, four of them actually was very close. If we gave, I don't know, another hour, we can solve four more challenges. Basically, in total, we were able to retrieve eight flags

**[6:42](https://www.youtube.com/watch?v=irMWadaKV2g&t=402s)** and put us on the top five in all the teams that ever participate in the game. One thing I didn't wrote here, also very interesting, is OpenSage was able to beat all the team that claim they don't use AI or use low AI. Basically, this is the AI-only agent that's able to beat a team of professional hacker that didn't use AI in their competition. So basically, this shows OpenSage was really able to solve real-world challenging task because, actually, all these kind of competitions, all these challenges, actually, when we look at the trace, OpenSage took five or six hours of continuous runs, spawn thousands of sub-agents to solve them. So basically demonstrating OpenSage was really able to scale up its own topology

**[7:33](https://www.youtube.com/watch?v=irMWadaKV2g&t=453s)** and is able to solve challenging tasks. Now, what we are doing is not only the agent, because we know building agent is the first step, but the brain, the model itself, is also very important. Sometimes model need to co-evolve with agents. This is also kind of motivated by our observation in the sense it's like, if we say run OpenSage with the latest model, we found that actually the model haven't fully figured out how to build its own agent. Sometimes model want to spawn new agent, but it actually fails. So this motivates us to bring up this kind of end-to-end, more holistic framework, where we think about we need to build new agents to train the model. We need to basically train the model to better spawn its own agent, better write its own tools. And also, we think about the inference stack,

**[8:25](https://www.youtube.com/watch?v=irMWadaKV2g&t=505s)** like the agentic trajectory is actually very different from pure QA task. We also are trying to develop new agent inference frameworks. But overall, what I want to deliver is we envision the future of AI agents is really-- the future of AI agents is really trying to open up the freedom to let AI do more explorations in terms of everything that eventually build up to the agent. What we want is to provide meaningful scaffolding, provide a powerful model, provide more efficient inference framework to make that happen. OK thanks. [APPLAUSE]
