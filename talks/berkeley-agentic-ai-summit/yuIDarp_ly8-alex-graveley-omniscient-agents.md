---
id: yuIDarp_ly8
title: "Alex Graveley - Omniscient Agents"
slug: alex-graveley-omniscient-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Alex Graveley"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-09T18:49:17Z
video_id: yuIDarp_ly8
url: https://www.youtube.com/watch?v=yuIDarp_ly8
youtube_url: https://www.youtube.com/watch?v=yuIDarp_ly8
tags: []
transcript: true
---

# Alex Graveley - Omniscient Agents

**Alex Graveley**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=yuIDarp_ly8) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,175 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=yuIDarp_ly8&t=1s)** ALEX GRAVELEY: Hi. Does this work? OK great. I'm Alex Graveley. I was lead on GitHub Copilot and Perplexity computer, and I just started a new company called Flying Object to focus on some of the topics we're going to talk about today. So the topic is omniscient agents. So traditionally, agents have been sort of limited by what they can see and access. And we think that this necessitates having a human in the loop. And so we want to get to a point where the human is less in the loop or can farm off different pieces of their loop to agents. And so how do we do that?

**[0:50](https://www.youtube.com/watch?v=yuIDarp_ly8&t=50s)** And that's the discussion here. So today's agents are a pile of primitives. If you're making an agent from scratch, you basically have to implement every single one of these. You need an execution layer, either you're running locally or in a sandbox. It's going to have a bunch of commands for playing with files, running commands, running CLIs. You're going to fine tune a bunch of asset creation. That might be documents, websites. PRs are another form of asset that we're trying to make these agents do a good job on. In order to do that, we need these orchestration primitives that have now become fairly standard.

**[1:39](https://www.youtube.com/watch?v=yuIDarp_ly8&t=99s)** The details don't matter as much as what they do. So it's useful to have a sub-agent that has different contexts from the parent. It's useful to have skills that can fill in gaps that the weights don't express in the way that you want. It's useful to have memories, so that the agent can learn from the past. It's useful to schedule tasks, so things that need to recur or that might run on a schedule. And now we've got loops, which are a goal-directed running. So we've got individual tasks, which then compress together into a loop, and the loop doesn't end until the goal is achieved.

**[2:28](https://www.youtube.com/watch?v=yuIDarp_ly8&t=148s)** And then live data is all these things. You need web search, browser control, computer control, MCPs, APIs, all this stuff. So is where agents are today. If we look at what's common here is that you're still controlling these agents. So the agent doesn't quite know what to do. And it's suggestions for what to do next are often bad. And so a human is in the loop to direct the agents. And so the bottleneck becomes your attention as an agent engineer or an agent using engineers, I should say. You're managing the loops.

**[3:16](https://www.youtube.com/watch?v=yuIDarp_ly8&t=196s)** You're running a bunch of things in parallel, things that are going wrong or going well. You have a sense you can tell what's going on. You can stop things, you can fork things, you can restart things, all this kind of stuff. But the way that we do this today is actually quite different than the way that we did it maybe a year ago. And so what we're actually doing is walking up this kind of complexity hierarchy. The way in which agents self-direct now is different from it was before. We started with just tools. We trusted the agent to call the right tool. Then we started trusting the agent to make commits. Then we started trusting the agent to make entire PRs. Where we are now is trusting the agent

**[4:03](https://www.youtube.com/watch?v=yuIDarp_ly8&t=243s)** to make multiple PRs in order to accomplish these kind of looped goals. And I think the future is something. Next level up is futures. Futures might involve running an experiment, looking at live data, checking for exceptions, checking for user sentiment. Segregating the people that are exposed to this feature to see if it has effect on your primary objectives, which are retention, say, or revenue or whatever. Above that, we start to get into projects. So this is like collections of features that might serve a need in your product. And I think at the top there, it becomes whole products when a self-directed agent, you can tell it to make a--

**[4:55](https://www.youtube.com/watch?v=yuIDarp_ly8&t=295s)** describe at a very high level the product that you want to make, and that it can then go make that, deploy it, iterate on it, figure out the features that it needs to make, maybe which don't exist anywhere else. Try a few different things and self-direct in that way. So how do we enable this kind of increasing complexity, increasing scope? Because each level up kind of required either new model iterations or much more agent harness complexity in order to accomplish it. And so we think that the commonality here are two axes. The axes that drive scope is one of insight and control.

**[5:47](https://www.youtube.com/watch?v=yuIDarp_ly8&t=347s)** So insight is what data the agent has access to and what form it has access in it, so that it can derive insights. Sorry, I'm out of time. And control is its ability to operate on that data in live systems. So what we're doing is moving from seeing the code to seeing the entire business. And that way, we can start to figure out what are the actual business objectives, what are the products that should exist, what are the features that should exist in order to accomplish those objectives. Right now, that's up to people to figure out and take guesses at, but what we want is for AI to be able to do that. And likewise, part of that process, part of the product development cycle is running experiments, deploying changes,

**[6:39](https://www.youtube.com/watch?v=yuIDarp_ly8&t=399s)** monitoring live systems, scaling those systems as needed. And so both these things together become the two axes which agents are growing their scope. So there's a bunch of open problems with this processing lots of data. Generally you want to ingest and index everything that happens inside of a business. You want to be able to compress that knowledge into something usable by your agent. You want to have triggers. If you're going to be running lots of experiments at the same time, potentially without human in the loop, you want to be able to have the agents aware of each other and coordinating effectively, and a bunch of other things, to the hardest point, which is sometimes

**[7:31](https://www.youtube.com/watch?v=yuIDarp_ly8&t=451s)** you don't even know the objective function you're optimizing. And so these are the open problems in order to make what we think is the future of self-directed agents. Yeah. So what we want to do is enclose the entire system, capture everything. We want to be able to give the macro context to agents, so that they can operate with full awareness and give the right primitives to those agents so that they can deploy changes, monitor those changes, and scale those changes to accomplish those business goals. It's going to be a process as we walk up this complexity stack, but I think that's the direction we're headed. So yeah.

**[8:18](https://www.youtube.com/watch?v=yuIDarp_ly8&t=498s)** If you want to try out early versions of what we're working on, there's a waitlist on flying object. Otherwise I'm Alex Graveley on Twitter. We'd love to talk. Thanks.
