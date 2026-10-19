---
id: M_8qg5OVE20
title: "Mitchell Alderson: The Last Agent Architecture"
slug: mitchell-alderson-the-last-agent-architecture
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 9
published_at: 2026-10-07T23:08:45Z
video_id: M_8qg5OVE20
url: https://www.youtube.com/watch?v=M_8qg5OVE20
youtube_url: https://www.youtube.com/watch?v=M_8qg5OVE20
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Mitchell Alderson: The Last Agent Architecture

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=M_8qg5OVE20) · [Conference site](https://aiconference.com/)

## Description

Models change monthly. Prompts change weekly. The need to re-architect your agent stack feels like a quarterly necessity. Change is inevitable—so build like it. This talk explains how to set up a sovereign stack that sticks—flexible primitives, deep observability, and an execution layer that allows for continuous change.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,573 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=M_8qg5OVE20&t=14s)** Awesome. Hello. How is everybody doing? >> [snorts] >> So, I am Mitchell. I am do technical content at Ingest, which is a durable execution uh agent infrastructure. So, stuff that makes your agent run without failing. What I want to present today is your last agent architecture with a thesis of your agent architecture has the half-life of 6 months. So, AI is moving incredibly fast. Uh if you're running any kind of AI in production, you've probably rebuilt or rewritten something at least twice. You know, we've gone from function calling, uh tool use MPCs, CLIs are cool now for tools. You know, maybe you're using LangChain. Maybe LangChain isn't cool

**[1:01](https://www.youtube.com/watch?v=M_8qg5OVE20&t=61s)** anymore. Um but what do all these things have in common? is Out of the six In the last 6 months, out of everything that you've built and is in production, real customers are using it, what has stayed the same and what have you had to just continually rebuild as things keep progressing inevitably, right? And the real question being, how did you architect your agent in a way that you don't have to keep rebuilding the foundation? Did you use a framework? Um did you go custom? Did you know kind of from the beginning what you were doing or has it evolved as customer feedback has come in and you're using AI in production? So, really if we look at a harness, we look at cloud code, we look at something custom that you've written yourself,

**[1:49](https://www.youtube.com/watch?v=M_8qg5OVE20&t=109s)** everything All these AI tools really have three layers. We have the execution layer, which is the the bedrock of a AI agent. So, that handles flow control, state management, durability, um you know, things like retries if something [clears throat] fails midway through a a agent loop. You have the context layer. This is the stuff that we basically talk about all the time, right? So, we have our models, new models are coming out literally every week, uh maybe new prompt strategies, new tools, new memory and rag systems, right? This is changing all the time. Then you have ways that the agent can interact with the outside world such as sandboxes, different runtimes, different browser uh tools, you know, computer used tools. And so, why all this matters is these layers do not age at the same rate. So,

**[2:39](https://www.youtube.com/watch?v=M_8qg5OVE20&t=159s)** like we said, um in the context layer, the models, new models are coming out literally every day. So, if you're trying to keep up with that, you're going to be rebuilding this thing over and over again, swapping out SDKs, it's going to be a mess. Compute layer, sandboxes, that technology moves fairly slowly, but it's still pretty fast. But, our thesis here is that if you build on the execution layer correctly, that layer doesn't need to change. So, [clears throat] basically de- design for evolution. So, magical frameworks, you know, I won't name names, but there's some that are very very opinionated and it's very difficult to adapt to specific use cases if you rely on frameworks too much. Pre-built harnesses, uh we all love cloud code, but there's definitely a lack of control compared to rolling your

**[3:26](https://www.youtube.com/watch?v=M_8qg5OVE20&t=206s)** own. Uh and then if you do roll your own with custom code, you're going to eventually run into some complexity issues, right? And the inevitably the layers blur. So, let's define a layer that should last, you know, for a good amount of time depending on how things progress. At Ingest, we call this the execution layer. So, it's the system responsible for running your code reliably, managing how, when, and whether each piece of work completes independent of all these other things that we've talked about that change all the time, right? So, let's look at this Harness in motion. So, harness of course being synonymous with AI agent. So, your app triggers an agent. We have the execution layer figuring out what tasks need to be done. At Ingest, we call these steps, but they

**[4:13](https://www.youtube.com/watch?v=M_8qg5OVE20&t=253s)** could be tasks, you know, agent turns, so you can call it whatever you want. And these tasks are running through each of these calls the context. So, whether that's Claude, GPT, an MCP, a rag system, doesn't matter. It's swappable, right? Compute is swappable. Um if you're running on uh E2B uh sandboxes, you're running something that it fires off in Docker, also swappable. But, the key here is the execution layer remains the same. So, the execution layer has three jobs. So, the first one is surviving failure, resume, don't restart. So, if your agent is running a really long complicated task, we're burning tokens, it's costing you money, and it fails in the middle of that task, how does it know where to restart? Do you start over from the beginning? You

**[5:00](https://www.youtube.com/watch?v=M_8qg5OVE20&t=300s)** lost all that progress. It has to figure out what it's doing, or can you just pick up right where you left off? So, building on an execution layer allows your agent to restart at step 38 instead of going all the way to the beginning and continuing with that long horizon work. So, job two is being able to trigger this agent harness from anywhere. So, this could be a cron job, you know, something that runs overnight every on on a clock. Uh this could be event-driven architecture, which is our favorite. You could call an API, or it could be a human in the loop approval. So, the key here is that all of these things can fire the agent, and the execution layer will will deal with the details. So, the third piece is this agent's doing a lot of work, maybe a lot of long-running work.

**[5:49](https://www.youtube.com/watch?v=M_8qg5OVE20&t=349s)** We need to be able to observe it, and we need to be able to evaluate the uh performance. So, because your entire agent is running on this durable execution layer, we have all the context we need just in this same layer to have traces. You could score different evaluations, and all of those together give you insights which can be pulled into any other system and uh incrementally improved. So, you're running all of this data. You have production data on which model works better, which prompt method works better, all because it's running on that durable layer. So, if we see the whole session at work here, um an agent is not one LLM call, right? Uh we I think we all know this. Like, the old ChatGPT chatbot, that was one LLM call and then you'd have to feed it

**[6:36](https://www.youtube.com/watch?v=M_8qg5OVE20&t=396s)** back and it was kind of doing one thing. The modern agent might have a plan mode, might have some different tool call modes, a sandbox mode. And what happens if we see that little red block? What happens when it fails right in the middle? Do we retry all the way from the beginning? That'd be kind of foolish, right? So, with the execution layer, we can recover and we can continue forward. So, the other thing that we just want to touch on very briefly is, obviously in that stack of layers, we have the compute layer. So, agents need sandboxes. Uh sandboxes are becoming very popular. If you haven't used them, it's a secure temporary server, right, to run commands and then destroy it and no bad code could escape out of there, right? Um this ages pretty well. These things are definitely still getting updated pretty rapidly. But, the key here

**[7:26](https://www.youtube.com/watch?v=M_8qg5OVE20&t=446s)** is the sandbox is by design ephemeral. So, there you'll see a lot of talk of putting the agent inside a sandbox, but then you lose all of that agent context. So, what we argue is that if your agent is uh running on this durable execution layer, the compute layer, the sandbox, maybe a browser-based session, should be a separate layer because that state is going to go away when the task is done. So, just a quick aside there. So, this is what we built Ingest for. So, Ingest is that execution layer. It handles these durable steps, retryable caching, right? So, as you progress down your agent tasks, those are cached, retried, you know where you left off. Um all those different scheduling and triggering outcomes that we talked about, uh full session traces, event triggering,

**[8:13](https://www.youtube.com/watch?v=M_8qg5OVE20&t=493s)** which is kind of a all-in-one toolkit for doing that. You could build this, obviously, uh without it as well, but it's it's definitely a lot of work. Um so, to recap, every agent harness is effectively three layers. You have the execution layer, which should remain stable. You build it once, it stays around for a really long time, and handles all those boring problems like retries. The context layer then becomes swappable. So, when the next GPT model comes out, you just swap it in. If you want to try a new framework, you swap it in. And then the compute layer, which is ephemeral tools for the agent to use, also becomes swappable. So, if some new big breakthrough comes through next week, you just swap that into your execution layer. And that is what I have for you today.

**[9:02](https://www.youtube.com/watch?v=M_8qg5OVE20&t=542s)** Um Ingest is free to try. You can sign up today, and at the conference here, we are giving away 3 months of our pro plan as well. So, thank you. >> [applause]
