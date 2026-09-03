---
id: brPTwEo5h-c
title: "Johann Schleier Smith - Systems Foundations for Agentic AI"
slug: johann-schleier-smith-systems-foundations-for-agentic-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Johann Schleier Smith"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T01:55:19Z
video_id: brPTwEo5h-c
url: https://www.youtube.com/watch?v=brPTwEo5h-c
youtube_url: https://www.youtube.com/watch?v=brPTwEo5h-c
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Johann Schleier Smith - Systems Foundations for Agentic AI

**Johann Schleier Smith**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=brPTwEo5h-c) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,671 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=brPTwEo5h-c&t=2s)** JOHANN SCHLEIER-SMITH: Hi, everyone. I'm Johann Schleier-Smith. I'm at Temporal Technologies. And today, I'm going to be talking a bit about our perspective on the agentic AI landscape and introducing Temporal as well. So just by show of hands, who here is familiar with Temporal, maybe has heard of it? We've got a few. How many people have actually used Temporal? Well, I'll tell you, this is going to be a high level overview. If you stay past this session, we're also going to be doing a workshop where you can get hands-on and get into the code. So, let's just get into it and let's talk about systems. So when we talk about systems, we're talking about creating some sort of functionality by putting together a whole bunch of components. And in the case of AI, there are a lot of these components. And so we need to get that functionality.

**[0:50](https://www.youtube.com/watch?v=brPTwEo5h-c&t=50s)** But in addition to the core basic functionality, there are these cross-cutting concerns. Things like reliability, which Temporal has really a deep experience in, efficiency, security, evolvability. That includes the scalability. It includes the ability to do upgrades, and so forth. Let's dive in a little bit on reliability because this really explains the core mechanisms underlying Temporal. So suppose we have an agent. In this case, it's a customer service agent. It's going to be helping with returns. And so this agent needs to connect to a whole bunch of different systems-- knowledge bases, inventory, ERP. It needs to handle payments. It needs to probably have escalations. It needs to be able to send emails. And in order to make all of this work reliably,

**[1:37](https://www.youtube.com/watch?v=brPTwEo5h-c&t=97s)** what do we need to do? We need to put retries and a whole bunch of different places. We probably need queuing to handle load. We need state management to keep track of the process all the way through. And these are all places where things can go sideways. And so whoever's building this needs to account for that one way or another. Now, traditionally, software interleaves the application concerns, the business logic with the systems concerns, things like reliability and other systems concerns that we've talked about. Now, fundamentally, if there's one thing to take away from this talk about what Temporal makes possible is it's this model of durable execution. And what that does is it allows you to write code that puts the system logic over on one side and the application concerns on another,

**[2:27](https://www.youtube.com/watch?v=brPTwEo5h-c&t=147s)** and really isolate that out. Now, the temporal open source project itself, what it lets you do is it lets you build crash proof applications. It's open source license, so MIT license. And you can back it with a number of different databases like Postgres or Cassandra. There's also a cloud product. But the key thing about it is that it lets you write regular code, regular programming languages, write Python, TypeScript, you name it, and get crash proof execution. So how do you recover after a crash? Well, there's basically two ways to get that state back. You can either save it or you can recompute it. And with Temporal, you can think of it-- and we'll get more of this in the workshop. But simple annotations that you can put on the code. And you can say, here's what I want you to recompute. Here's where I want you to save state.

**[3:15](https://www.youtube.com/watch?v=brPTwEo5h-c&t=195s)** And then if there's a trick, that's the trick. There's other cool things like distributed systems from ordinary language primitives. This is pretty cool. But I want to talk for a minute about how companies out there, our users, our customers are using Temporal. This is Venkat, VP of application infrastructure at OpenAI. And so one application that's notable is ChatGPT images, where there's a whole series of steps that need to happen. They need to all happen reliably in order to spit out that image. That was one of the notable use cases for Temporal, OpenAI. Codex on the web is another one. But really, there's a whole slew of things ranging from the infrastructure control planes to the data connectors that's effectively think about that as building and maintaining

**[4:04](https://www.youtube.com/watch?v=brPTwEo5h-c&t=244s)** the RAG indexes and so forth. And then finally, traditional business processes. And really, across the ecosystem, whether it's at NVIDIA or at Cursor, now, SpaceX, or Lovable, Replit. Temporal is being used really across that stack to enable agentic AI. So now, I want to dive in and just make a few observations about really sharing how we think about and what we've learned from working with companies across the ecosystem. So we have this functionality that we need to provide. It's an agent. And that means different things to different people. Definitely in a business context, it's basically some system that gets something done. And what we spend a lot of time thinking about, particularly in the AI Foundation's team, which is the team that I'm on, is really

**[4:52](https://www.youtube.com/watch?v=brPTwEo5h-c&t=292s)** what are the right abstractions? What are the tradeoffs that come along with this agentic AI workload? How do we slice them? Which ones do we pick a point in the space? Where do we maybe give you a knob for it? And so just a few observations about these workloads that I think are particularly interesting. I'm not going to read through all of this. But just on the LLMs. So this is also, I'll just say, it's a different workload from other workloads we needed to deal with before in systems. And so, it's really fun to be able to rethink these abstractions. So non-determinism. So that means that you call it an LLM. You're going to need to validate and store those responses. But it's also interesting because it has this flip side, where it's also fuzzing. It's actually forgiving with respect to its inputs. That's the other side of the coin from its outputs

**[5:41](https://www.youtube.com/watch?v=brPTwEo5h-c&t=341s)** not being necessarily 100% determined. Security, this is interesting from the threats side. So you often think about adversarial inputs, things like prompt injection and alignment. But also, a great threat model when you're thinking about agents is actually just bad judgment. Because it happens, that RM-RF. And so that's driving a lot our by accident, not thinking. That's driving a lot of our design considerations. And then certainly, from the execution profile, the fact that you're interacting with a world, that's a place where you want to capture your state. You want to make sure that you're there, writing things down carefully. And also bursty load, which calls for serverless and so forth. Now, another observation that we've

**[6:29](https://www.youtube.com/watch?v=brPTwEo5h-c&t=389s)** made from working with companies throughout the ecosystem is that there's really this spectrum of agency. And that the right solution for a particular application, for a particular functionality could come from anywhere across the spectrum. And actually, the more agency you have, it's not always a better thing. So when people think about agents, oftentimes, they're thinking about this sort of level 3, which is an agentic loop. The LLM makes all of the decisions about what happens next. But if you go over to the left, you look at level 1. There's actually a huge number of applications, something like summarization or so forth, where the job actually gets done really well by having regular code drive the control flow and having those LLMs inserted at very specific points. It could be very reliable. And if that gets the job done, then that's probably the right solution.

**[7:17](https://www.youtube.com/watch?v=brPTwEo5h-c&t=437s)** The other end of the spectrum, we go as far as self-evolving agents, which we now see in some of the harnesses. And so there's a reason for that. But you can also think that's probably not also the right solution for the job. And when we think about abstractions at Temporal. Abstractions for agentic AI, we're really thinking about being able to allow you to dial that in and to frankly, go back and forth along this spectrum without rewriting your entire application. And so one thing that we are sharing today is the Temporal agent harness. So this is not yet a supported product. But if you go and you start the GitHub repo, then hopefully, it will be soon. I'll put up a QR code in a second to that as well. But this is a set of abstractions built on top of Temporal's core, durable execution abstractions that make it easy to build

**[8:09](https://www.youtube.com/watch?v=brPTwEo5h-c&t=489s)** practical agents for things that whatever it is that you want to build. So we give you that ability to plug-in the inner harness, which could be a coding agent, like OpenCode. It could be something like OpenAI agents SDK, which also has a lot of interesting sandboxing functionality, Pydantic AI, any of these, we've really worked hard to embrace this ecosystem. You can plug your tools. And again, this is really designed to give you abstractions to mix and match. Whether that means you want to talk to it through Slack, through Teams, you name it. So this is just a quick screen grab of what was an OpenCode session. I was in there just fixing a bug in a simple program. And because I've run that with agent harness, not only am I getting the durability, the reliability, if I wanted to run this at scale, but I also get for free. But frankly, it's part of the package.

**[8:58](https://www.youtube.com/watch?v=brPTwEo5h-c&t=538s)** I get the observability, the ability to dive in and see what was the agent reasoning about at the various steps, what were the tool calls, and human approvals and so forth that happened along the way. And that's the benefit that you get from really being thoughtful about the abstractions that you're bringing into to your agentic AI. So with that, I'm finished here. I welcome you to stay in this room for the next session, which is going to be a workshop where we're going to get hands-on with Temporal. Thank you. [APPLAUSE]
