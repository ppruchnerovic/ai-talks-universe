---
id: q1CG02bYEqY
title: "The #1 Mistake Building MCP Tools"
slug: the-1-mistake-building-mcp-tools
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "Practitioner AI conferences"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 16
published_at: 2026-05-22T14:00:06Z
video_id: q1CG02bYEqY
url: https://www.youtube.com/watch?v=q1CG02bYEqY
youtube_url: https://www.youtube.com/watch?v=q1CG02bYEqY
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# The #1 Mistake Building MCP Tools

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=q1CG02bYEqY) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Sam Partee, Head of Engineering at Arcade.dev, has built north of 10,000 tools for AI agents - first with Arcade's own Open Execution Protocol, and now with MCP. In this 15-minute talk from the Agentic AI Foundation, he breaks down why most teams shipping MCP tools today are getting it wrong, and what to do instead.

The hard part of tool design isn't writing the code - it's finding the right abstraction. Most MCP tools today are thin API wrappers, but LLMs reason about tasks ("find the customer who complained last week"), not endpoints. That mismatch is why your agent fails.

What's covered:

- The Tool Abstraction Problem: why APIs are built for programmers and tools must be built for LLMs, and why that changes everything about how you design them
- The Chaining Cliff: every benchmark from Apple's Tool Sandbox to Berkeley's Function Calling Leaderboard shows that 6+ tool chains push failure rates above 50 percent
- Task-Intent Tools: why one tool that does "find calendar and submit complaint on Zendesk" beats five chained CRUD endpoints every time
- The 10x Lever: across 20,000+ Arcade evals, description quality moved the needle more than any other variable - more than name, more than context
- Tool Count Cliff: at 20+ tools, agents stop selecting correctly; progressive discovery helps but does not fix it
- Sub-Agents and Enumeration: when to enumerate variants of a tool, and when to break into sub-agents instead
- Optimized Tools Patterns: the design patterns Arcade has open-sourced for building tools that actually work in production

This talk is for engineers building MCP servers, agent frameworks, or any tool-calling system where reliability matters more than coverage.

Links and Resources:

- Arcade.dev: https://www.arcade.dev
- Sam Partee on LinkedIn: https://www.linkedin.com/in/sampartee
- Arcade tool patterns and optimized tools documentation: https://docs.arcade.dev
- Apple Tool Sandbox paper: https://arxiv.org/abs/2408.04682
- Berkeley Function Calling Leaderboard: https://gorilla.cs.berkeley.edu/leaderboard.html
- Agentic AI Foundation: https://agenticaifoundation.org

Timestamps (approximate, please adjust):

00:00 Building 10,000+ tools before MCP existed
01:00 What is the tool abstraction problem
01:32 Why API generators do not work for LLMs
02:16 The customer-complaint example: 5 endpoints vs 1 tool
03:16 The chaining problem: 50%+ failure rate at 6 tools
04:45 Thin wrappers vs task-intent abstractions
05:25 Evaluating tools across multiple LLMs plus unit tests
06:12 The to-do list abstraction and Gherkin-style task modeling
07:12 Evidence from Redis, Block, Square, and GitHub Copilot
08:11 Arcade's optimized tools patterns
08:54 Description quality is the 10x lever
09:38 Why descriptions beat context in the schema position
10:35 The 600-word rule for tool descriptions
11:42 Progressive discovery and dynamic tool selection
12:37 The tool count cliff at 20+ tools
13:11 Final takeaways: chain inside tools, not across them
14:00 Q&A: enumeration vs sub-agents
15:38 Agent scope: never more than 40 enumerated tools

## Transcript

*2,478 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=q1CG02bYEqY&t=0s)** So, today I'm talking about the tool abstraction. Uh so, I've probably made somewhere north of 10,000 tools. Now, that might not seem possible, but I was actually building tools prior to MCP existing. Um we had our own protocol. It was called Open Execution Protocol. And we for a long time cared just about tools. We didn't have prompts or resources. All we cared about was how can I take the JSON output of a model that at the time it was GPT-3. So, JSON output wasn't even guaranteed. And how can we take that output and efficiently make sure that it is one, this seems funny now, but parsed correctly. Two, that it is correct. That the outputs and the arguments and

**[0:48](https://www.youtube.com/watch?v=q1CG02bYEqY&t=48s)** everything is correct. And how can I ensure that result of the tool function, but also of the output of the large language model. And this became something that we deemed uh a machine experience, like a user experience, but a machine experience, and that I often call the tool abstraction problem. This applies to resources and prompts, too, but in a different way. Um I'm I'm going to get at primarily what does it take to make a good tool? Um and I'm going to do it in 50 minutes. So, what do most people mess up today? If you ever see something saying like an API generator, "Oh, I'm going to take your endpoints. I'm going to make them all tools for you." Don't do it. It's not going to work. And the reason being is because the tool

**[1:38](https://www.youtube.com/watch?v=q1CG02bYEqY&t=98s)** abstraction and an API abstraction are meant for different things. What do you make an API for? You make it for other programmers. You make it for an interface by which an API, you make it for another program to interface with it, not a large language model. If a large language model is to read it and understand it and produce the type of output necessary to call it, the abstraction is much different. Sometimes it's higher, sometimes it's lower, but overall it is much differently catered to in terms of the audience in which you're talking to. So like you can say "Find the customer who complained last week and schedule a follow-up." This is something an agent hears, and it needs to break it down into tasks.

**[2:26](https://www.youtube.com/watch?v=q1CG02bYEqY&t=146s)** But to do that, you have five endpoints. And and even then, you most of the time will not have the model realize it needs to call get user ID first. And so, what you really need to do is make an abstraction that covers these five. Find calendar and submit complaint on Zendesk. That can be a tool. One tool. That might sound too catered, but in fact, the accuracy rate of that tool in both when it should be chosen in terms of selection and its result in terms of the recall of the selection and the accuracy of the result is significantly higher both in practice and in theory.

**[3:16](https://www.youtube.com/watch?v=q1CG02bYEqY&t=196s)** And how do I know this? Every paper, pretty much since Apple's tool sandbox paper, every the nerves papers that you see, all of the um individual like the what is Speakeasy I think is one of them, it's like the major project, it's basically saying if you need to call six tools, you're just basically out of luck. You have over a 50% chance failure. And and even worse is when you get to the point where you have to call a chain of them. If you've looked at Nestful or tool composition or the Berkeley uh function calling leaderboard, any of them will tell you chaining is the hardest thing. And so, why are we trying to chain API

**[4:04](https://www.youtube.com/watch?v=q1CG02bYEqY&t=244s)** calls? Like, it doesn't make any sense. There it's a different abstraction, right? And so, if instead of saying, "Hey, go get the user ID, find the user's calendar, go get and get each of the individual IDs of the events." There was just one that that composition was made up of. And yes, that's a particular example of a higher abstraction of action, but it doesn't even have to be higher. It can be more specific. The whole point here is that it's catered to a different audience. It is not a programmer, it is in fact a large language model or an agent. And chaining is in fact the hard problem. Now, >> [snorts] >> we have a lot of the different uh types of abstractions in the space that I can

**[4:53](https://www.youtube.com/watch?v=q1CG02bYEqY&t=293s)** talk about. Um you may say it's a thin wrapper API based. I can just put a better description on it and that's all I need. Most of the time, that's going to end up in the chaining territory, where it's going to be saying something like, "I need to call six of these things to get a normal job done, like an API would, right?" Um and the the the middle ground that we mostly find is make it oriented around a task specific to the agent you're building it for. And then evaluate it both on the ability of a large language model or even better, uh use Arcade to evaluate it on multiple, right? So, a suite of language models. And then also have PyTests and you know, uh a you

**[5:41](https://www.youtube.com/watch?v=q1CG02bYEqY&t=341s)** know, set of Jest tests for confirming those tests actually run, like unit tests. Cuz remember, you have to also not in addition to the tool being something that is callable by language model, it has to also run. Which is something that most people actually end up not testing in a lot of tools. You see a lot of tooling frameworks these days without unit tests. And it's like, okay, well, the deterministic part has to be at 100% if we're going to introduce any amount of non-determinism right? That that part has to be at 100%. So, we find that most of these succeed the best when you organize them around tasks or intents. And the reason for that is tasks and intents model the way agents make to-do lists in that Gherkin style

**[6:30](https://www.youtube.com/watch?v=q1CG02bYEqY&t=390s)** that mostly Anthropic is responsible for introducing into the ecosystem. Um the to-do list abstraction, just think about it. In a to-do list, how do you write stuff? By tasks you got to do, right? [snorts] And so, if you model them by tasks and intents, it's much easier for an agent to select the tools. So, like, you know, get tr- track this order right? And return report, or something even that specific would be much better than getting a user. It's too abstract, right? Where you might be getting the user inside that in particular function. Uh there's some major proof of this in the ecosystem. My old team at Redis put out a great paper on this. Um

**[7:19](https://www.youtube.com/watch?v=q1CG02bYEqY&t=439s)** uh Block and Square, um and GitHub Copilot also put out a great one. Uh there's evidence all over the ecosystem. And this talk will be online, so you can go and look at all of these things, okay? Um you can go and fact-check me until the day's end uh on all of these papers. I've been doing this for a long enough time to where I can back up each one of these statements with a paper and a citation. Um and most most likely a GitHub repo. Um, it has been a long time my team has been trying to figure this exact problem out. Um, the cool things that I'll point out in this particular set of benchmarks are um, the self-discovering flows in the block paper that is becoming a little bit more popular right now. Um, the Redis paper focused a lot on reducing the number of tokens that you use. That was really

**[8:07](https://www.youtube.com/watch?v=q1CG02bYEqY&t=487s)** interesting. Um, so I would check those out. Another thing we released recently, we kind of took everything that we thought of in terms of like how you can build tools. He's actually sitting in the audience. His name is Guru. He's uh, incredible engineer and he put up all these patterns that we have in our what we call optimized tools. And we we do this because it's much easier to think about it in like the in task and intent modeled towards a specific domain type way. Um, if you can look at these patterns and say, "Oh, that models this kind of task that I want to go after." There's kind of step-by-step instructions to help you get to where you need to go. So, check out the arcade tool patterns if you're interested. Um, there's some really cool ones on there. Um, the

**[8:54](https://www.youtube.com/watch?v=q1CG02bYEqY&t=534s)** biggest thing I'm here to say is description quality. If you look at our over 20,000 evals, if you look at any of the things that we do, um, confirming that our tools are actually going to work, the description quality, the quality of the description and iterating on the description is what actually has a 10x lever um, in terms of the returns that it yields. Because the description is heavily heavily uh, is is the thing that most heavily influences whether the large language model is going to select that. The name is being, you know, the the most influential and then how it is used. So, you might think that context is really you know,

**[9:42](https://www.youtube.com/watch?v=q1CG02bYEqY&t=582s)** number one, it's not. The description more than anything because of the position that it is most commonly placed by an agent framework in the positioning of the context window that is sent to the large language model being in the schemas, which is usually towards the bottom. If you look at any needle in a haystack paper, the description is what is most likely going to be the thing it last thought about. Last thought about. It last uh you know, after it selected the tool. It's most recent uh you could say piece of memory in the context window. And so, that's really important. Um we found even in our nightly evals, we had 10x fewer um errors when we specifically went through and did optimization

**[10:30](https://www.youtube.com/watch?v=q1CG02bYEqY&t=630s)** strategies towards only the descriptions. It was around 9.something. Um don't do more than about 600 words. Ideally, keep it to a action verb to start. And then a short task intent enabled or reformed sentence. Um you can look at a lot of our examples online. Um and all of them will show you uh kind of how we specifically model our functions like that. Um and the uh I'm going to say this wrong. I believe it's hesh. Um hesh at all um is a really interesting paper about how they went from you know, being able to do uh a a very small amount of activities with bad descriptions to a an entire chain of activities, and they describe it a

**[11:18](https://www.youtube.com/watch?v=q1CG02bYEqY&t=678s)** little funny. Um like zero-shot equals 16. It's uh they were able to make the model perform a much longer chain, like we talked about earlier, the tool chaining problem, uh chain of activities just by changing the description. Um and so the 10x lever of all of this and how to make the tool abstraction better is the the description. Tool selection, dynamic tool selection has been released across a number of different places. Really what you'll see here is a concept called progressive discovery. And progressive discovery is something where you're introducing context over time. Um and there's all types of experiments that are out here, but really the the best thing that this does is not necessarily helping with the abstraction, but helping with the amount

**[12:06](https://www.youtube.com/watch?v=q1CG02bYEqY&t=726s)** of context that you're utilizing. But if you look at any of these individual papers that you see down here like in MCP zero, all of them will point out themes that I've pointed out in this talk, which is that the description really matters. The task intent really matters. The selection time really matters at runtime. The context window positioning of the scheme is really matter. And so it's important to add here. And I know I want to leave some time for questions, so I will just say skip skip. Last takeaways, tool count cliff is real. If you have more than 20 or so tools ever since Apple sandbox, your agent's not going to know what to do. You can fix that some up with selection at runtime, but even progressive discovery is not going to fix the whole

**[12:53](https://www.youtube.com/watch?v=q1CG02bYEqY&t=773s)** problem. Chaining inside tools is more likely to be that agent abstraction and chaining is the hard problem. Moving composition logic inside of your tools and then making them task intent enabled functions that you choose from is a much much better recipe for success. And then lastly, descriptions of the 10x lever, don't just write them and forget about them. Think about them all the time. Descriptions are what matter the most and you might not think they are, but they are. Um and that's fact. So I will leave a little bit of time for questions. I only have 2 minutes 30 seconds, but thank you very much. >> [applause] >> Yes.

**[14:03](https://www.youtube.com/watch?v=q1CG02bYEqY&t=843s)** So, the question was about task intent-based tools and then what if the input is based on a like a previous event type? Is that kind of Wonderful yeah. >> [snorts] >> Enumerate.

**[14:51](https://www.youtube.com/watch?v=q1CG02bYEqY&t=891s)** I would say enumerate. So, the the point here is um I'll give it I'll kind of give it back to you. Um you want the flexibility. You don't want it to be to give the example of the one I had. Like you don't want to be getting the user every time they're getting the email and the calendar every single time. You want the flexibility to say, "Oh, I might also want to go to this in the the abstraction enumerate them and name them differently. Um now, you might say, "Okay, what about then the number of tools and the problem that that brings about?" Well, that typically you break into sub tasks or sub agents. However, the the promising point that we're about to reach in the future with progressive discovery will hopefully be a better answer to that as we move on. I would argue if you're making your agents broad

**[15:40](https://www.youtube.com/watch?v=q1CG02bYEqY&t=940s)** enough such that they're responsible for that broad of an activity. If you have to enumerate more than 40, you should probably rethink your agent. Um it's too broad. Never have that broad of an like an agent scope shouldn't be that broad. You're giving it too much responsibility. Anything else? Good question. Yeah, yeah, why not? Oh, actually I think we just reached zero seconds. I'll reach you after. All right. Thanks everybody.
