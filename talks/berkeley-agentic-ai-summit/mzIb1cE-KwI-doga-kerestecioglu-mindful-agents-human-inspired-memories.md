---
id: mzIb1cE-KwI
title: "Doga Kerestecioglu - Mindful Agents: Human Inspired Memories for Long Horizon Tasks"
slug: doga-kerestecioglu-mindful-agents-human-inspired-memories
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Doga Kerestecioglu"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T01:55:47Z
video_id: mzIb1cE-KwI
url: https://www.youtube.com/watch?v=mzIb1cE-KwI
youtube_url: https://www.youtube.com/watch?v=mzIb1cE-KwI
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Doga Kerestecioglu - Mindful Agents: Human Inspired Memories for Long Horizon Tasks

**Doga Kerestecioglu**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=mzIb1cE-KwI) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,659 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=1s)** DOGA KERESTECIOGLU: Hello, everyone. It's great to be here. I'm from the Microsoft Fabric AI team. And I'm here to talk about the work we're doing in the real-time intelligence space on our long-running agents, where we take some inspiration from ourselves as humans to improve the memory so we can get better at accomplishing tasks. So in the space that we're working at, we tend to have long-running agents that has access to data that's high volume-- streaming data is high volume-- and to just set up the problem that we're dealing with and the motivation for the approach that we're implementing here. I want to contrast it to how we, as humans, store memories and how we tend to have the situation for our agents

**[0:57](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=57s)** instead. So as humans, we have storage constraints. So what's likely to happen is because of that constraint, we will tend to-- the limit makes us better at distilling memories. So for instance, recently, I was on a train ride in Europe. And as you're on the train, you look outside the window. And you pass by endless fields. And you see some maybe windmills. You see some animals grazing. And we don't have the capacity to necessarily remember every strand of grass or every bit of thing over there. What we're good at is being able to distill that information and just remember interesting things that might be relevant to us. And this is just something that we, through evolution, are good at.

**[1:44](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=104s)** Whereas if you think about the agents, we don't have that problem in terms of the storage constraints. We can log every bit of information, somewhat relatively cheap. And we can log every trace. And what we do is we capture, retrieve, and typically, we summarize and retain the summary. So over time, we are with summaries of summaries of summaries, which typically works well until at the time of retrieval when you're looking for something very specific for most cases. But for the case that we're working on, we're interested in getting agents that work with these big volume data sets. And we want them to be proactive. So what we worked on is we are working on building a memory lifecycle as a feedback loop for our agents,

**[2:33](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=153s)** where we have a system that starts with, first, ingestion, where we basically ingest all of the data from the observability substrate. And then what we do is consolidation, which is similar to the idea of sleeping. But what we do is we dedupe merge. And we try to consolidate all of the memories that come in to become candidates. And the idea in here is, well, this is similar to maybe humans. The consolidation cycles for the agents that we're working in are domain dependent. And they might not always be temporal. So I don't know how many of you are still in the room, but you were just building an agent that was looking at F1, for example. So if you're a person-- if the agent is working on Formula One races, the telemetry that you take during the race

**[3:24](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=204s)** will be very different from what happens after the race, like during the race, race days versus the week. And then it's going to be very different from the season. So consolidation doesn't necessarily mean it has to be daily, but you need to process in some batch in some cadence. Next, we have forgetting where there's decay and interference. And the idea is, we want to make sure that if we have all these consolidated memories that are stable candidates, we want to make sure that we end up remembering the important things and all the unimportant stuff gets forgotten. Or most of it as best as we can. And then the next stage is retrieval. So for the retrieval, what we work on is a hybrid way where we have these memories stored in the cold storage, where we know a domain and put them in a graph. But we also have the live data coming in.

**[4:13](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=253s)** And we want to make sure that the agent can access both the streaming data and what's in the storage that's more stable, and be able to determine what's the best memory to use at the time. So that gets us to the feedback cycle, where, at the time of the retrieval, you will have usually conflicts. So, something new might happen. And it might conflict the memory that you have established that became stable in the cold storage. That's where maturation and reconsolidation comes in. Because we don't want to necessarily keep adding a new memory over and over into the graph. That's very hard to retrieve from. So you need to determine whether you want to update an entity in the graph, whether you want to add a new entity to the graph because there's some new information that's important,

**[5:01](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=301s)** or maybe discard what's the live information that's coming in because it's erroneous. So next, I want to talk about all of these bits have each their own components with different optimizations that you need to make. So I want to chat a bit about how we approach our evals for them and how our thinking around it. So here's two cases where we evaluate the ceiling and the floor, about the best case scenario and a very tough scenario. Where on the left side, we're having a retention benchmark, which is more deterministic. Where in this case, we are looking at a case where the system has clear labels of everything that's important. So what we were looking to optimize in here is,

**[5:50](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=350s)** how often we want to consolidate? And what's the cadence we want to use for it? And for this case that we were looking at-- and this changes from domain to domain. But it's things started stabilizing around 500 events at a time. Sorry, I think 200 events at a time. It's kind of small to see from here for me. But let's see, yeah. 200 events at a time with a precision where, if we forgot over it, that got better. So we're checking it. What's the best precision you get with how much you consolidate, how often you consolidate, and then how much we're getting ads over it? And the next case, we were using a retrieval benchmark utilizing LongMemEval, where we were looking at how much compression should we have? What's the optimal storage size we should look for without being destructive? So this is an eval where it's conversations.

**[6:41](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=401s)** So we have no labels about what might be important or not, which is not the ideal case for the type of work we're doing. Because the idea that we have is these domain experts that do repeated tasks. And there's an idea of how you can learn what's important. But even then, we can optimize. And there's a tradeoff between how much you want to compress and what accuracy you get. So with that, the approach in more general is for the type of memory work that we're doing, we need three types of evaluations. And they have different ideas about what they're looking for. So one of them is retention, which can be a quick eval on, deterministically, if you're building a memory system, and if you want to keep the important information, can you make sure that what you're keeping is actually important versus not?

**[7:31](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=451s)** Which is you need the labels for it. And there's a lot of work that we're doing on how we get better labels. But then the next one is retrieval. So assuming that you built a good memory system, then you need to look at how well you're retrieving from it. And are you getting the memories that you're looking for in that great system you built? Because if it's hard to navigate your memory and it's hard to do the retrieval part of things, then that's still is necessary but not sufficient. So you want to have good retrieval. And finally, for the agents, you want to look at your task completion evals, which are the most important because it's closer to the user. You might give the best memory to the agents. And depending on how it's exposed to the agent in your harness, the agent might choose to ignore it and still might not accomplish the task.

**[8:18](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=498s)** And this is the most expensive one for-- because for the long-running agents, it is expensive to build and run the evals, but it's the most important. So for each component, we're focusing on these three things. So to just sum things up, logs are not memories. And I think where things are going is, for long-running agents, you want to make sure that you have more than just the traces that's going to become available to them as memories. And the way like the volume works to be efficient, you'll have to figure out how you keep the important things or not. And then another important point is the domain is important. And for these cases, it needs to be pre-declared. And depending on how well you can do it at the runtime, you need to have it prior.

**[9:05](https://www.youtube.com/watch?v=mzIb1cE-KwI&t=545s)** Otherwise, that affects the efficiency and accuracy of the agents that you're running. So in terms of the next steps we're working on, we're working with the Foundry, Microsoft Foundry team on end-to-end evals on STATE-Bench. And we're also doing some better work on domain learning and graph ontology, where the idea is-- what we found in a lot of these is, the way you set up your graph structure and the ontology for it has a big effect on your accuracy in addition to these components. So we're working on them. So with that, thank you very much. And I look forward to meeting everyone after. Thank you. [APPLAUSE]
