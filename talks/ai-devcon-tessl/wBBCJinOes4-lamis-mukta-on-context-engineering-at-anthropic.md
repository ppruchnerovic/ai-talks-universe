---
id: wBBCJinOes4
title: "Lamis Mukta on Context Engineering at Anthropic"
slug: lamis-mukta-on-context-engineering-at-anthropic
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-08-24T13:30:23Z
video_id: wBBCJinOes4
youtube_url: https://www.youtube.com/watch?v=wBBCJinOes4
tags: []
transcript: true
---

# Lamis Mukta on Context Engineering at Anthropic

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=wBBCJinOes4) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Context engineering is now the main lever on what a coding agent can actually do. Three talks from AI DevCon London — Anthropic, OpenAI and Thoughtworks — on why the context around the model beats the model.

Lamis Mukta (Anthropic) explains why context engineering multiplies model intelligence rather than adding to it: a brand new model still won't know what it takes to succeed inside your organization. Ryan Lopopolo (OpenAI) argues most of the old constraints on software engineering are gone, and the three that remain are human time, attention, and the context window. Birgitta Böckeler (Thoughtworks) splits a coding agent harness into two halves — guides that point the agent forward, and sensors that tell it how it's doing. And Guy Podjarny (Tessl) makes the case for a context development lifecycle that humans own, while the agents run the SDLC.

What we cover:
– Why context engineering multiplies model intelligence instead of adding to it
– The three limits that remain once the old software engineering constraints go
– Guides and sensors: what a coding agent harness actually needs
– Codemods and static analysis, the computational half of harness engineering
– Runtime observability for agents, and mining agent traces for eval scenarios
– The context development lifecycle sitting alongside the SDLC

Chapters:
00:00:00 - Introduction
00:00:24 - Lamis Mukta, Anthropic: context engineering
00:02:12 - Why model intelligence alone doesn't compound
00:03:02 - Ryan Lopopolo, OpenAI: the limits that remain
00:04:03 - Human and model attention
00:04:40 - The context window and auto-compaction
00:05:21 - Birgitta Böckeler, Thoughtworks: guides and sensors
00:06:42 - Computational guides, codemods and static analysis
00:07:36 - Guy Podjarny, Tessl: the context development lifecycle
00:09:07 - The new agent stack: context as the new code

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which of the three limits bites hardest in your setup — human time, attention, or the context window? Tell us in the comments.

## Transcript

*1,770 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=wBBCJinOes4&t=0s)** Back in June, at AI DevCon in London, one idea came up in almost every room that the hard part of working with AI is no longer the prompt. And it isn't the model either. It's the context you put around it. Let's first hear from Lamis Mukta at Anthropic, who walked us through how context engineering has changed over the past year, and why she thinks it's the thing that multiplies everything else. By way of introduction, my name is Lamis. I'm a member of technical staff at Anthropic. I work on our applied AI team, and this is a team which sits between research, product and go-to-market. So we do a mixture of working on internal projects as well as directly with customers who are building agents at the frontier. Me specifically, I work with startups and founders, many of whom I'm sure are in this room today,

**[0:49](https://www.youtube.com/watch?v=wBBCJinOes4&t=49s)** and I think I have the best seat in the house because these are the users that are constantly pushing us right up against the boundary of what is possible with models and products today. And as such, we just get to, like, ride the exponential together. One thing that constantly comes up, as I'm sure you're all aware, is what it really takes to take the raw model intelligence that we have today and translate that into durable, scalable, useful products. And one of the main levers that we have in order to do this is context engineering, which will be the focus of my talk today. So on this journey, I want to quickly do a recap of where context engineering has gone in the past year. It's a space that's completely blown up, and through that,

**[1:40](https://www.youtube.com/watch?v=wBBCJinOes4&t=100s)** we'll kind of distill the primitives that have proven to be really useful, some stuff that has been a little bit less useful. Secondly, we'll talk about what the state of the art is for memory management today. And thirdly, and in particular with that, we'll talk about not just what nice theoretical principles are, but what it takes to actually build these systems in production. And then finally, we'll talk about where this will go on the path to continual learning, and in particular, touching on a paradigm called dreaming. So we said this before. And models — we release new models all the time. They are more and more intelligent. But when it comes to actually deploying these models in your agents, in your environments, in your organization, the intelligence alone is not going to compound because they need this context

**[2:31](https://www.youtube.com/watch?v=wBBCJinOes4&t=151s)** that helps them perform the specific tasks that you need them to. In particular, a lot of this context is often kind of orthogonal to the model intelligence, right? Like the newest model we've just released, one isn't going to isn't going to, out of the box, know exactly what it takes to succeed in your organization and with the tasks that you want them to. And so it's a really great investment to work on the context engineering part, because this over time has the effect of multiplying the intelligence even as models get smarter. We also heard from Ryan Lopopolo at OpenAI. He argues that most of the old limits on software engineering are gone, and what's left is human time, attention, and the context window. He can only really hold three sessions in his head at once. So, having just told

**[3:21](https://www.youtube.com/watch?v=wBBCJinOes4&t=201s)** everybody here that the core constraints on software engineering no longer apply, what are those core constraints, right? We have kind of a new set of problems to contend with, using agents in order to produce our software. And to me, these three things are the foundational limits that remain in a world where we are, as a team of humans and agents, producing software. Human time is the fundamentally scarce resource that we have. You know, I know I max out probably at three concurrent sessions on my laptop. If I want to be more parallel and have higher throughput, I must find ways to remove my own synchronous attention from the process. Human and model attention are these foundational limits, right? In the architecture of these LLMs, attention must sum to one. Thrashing the agents by having them do more and more work

**[4:14](https://www.youtube.com/watch?v=wBBCJinOes4&t=254s)** with conflicting and overbearing requirements in the course of a task is something that is always going to degrade performance less and less over time, but it is one of those core limits of the models. So we need to retool the way we work in order to be more parallel. Fork off a bunch more tasks, be willing to accept smaller or larger or many more PRs in order to let the agents explore what it means to do the job that we need them to do. And finally, you all probably deeply live this model context window. Things that get bigger over time. Still a scarce resource, something we need to protect. I will say, in my own experience with the GPT series of models, auto-compaction is fantastic. I never think about a context window anymore. I can let a task go for six, 12, 36 hours and still get good results, but the context window being obliterated and rebuilt

**[5:06](https://www.youtube.com/watch?v=wBBCJinOes4&t=306s)** over the course of these auto-compactions is something you must contend with. And there are ways that we structure the context we give the model, or continually resurface context to the model to deal with this constraint, that context windows are continually being emptied and filled. Birgitta Böckeler is a Distinguished Engineer at Thoughtworks. She splits the work of building a harness into two halves: guides that point the agent forward, and sensors that tell it how it's doing. So we're starting with these guides. But then we also want to give it feedback. Right. So, ideally, so that we can trigger immediately a self-correction loop before we even look at the code so that we don't have to, like, have all those low-hanging fruit still in there. So the most common way that people do that right now is with code review agents, right? But there's also all of these other tools that we have in our toolbox

**[5:58](https://www.youtube.com/watch?v=wBBCJinOes4&t=358s)** from before AI, like static code analysis. And then, of course, an agent usually has access to the log so it can start the application, see what logs come out of it. Many people give an agent access to the browser so it can look at, like, something when it has changed a web component or something like that. And there's actually a difference between these. Sort of, like, a review agent is an LLM judging the work of another LLM. Right. So it's kind of inferential. It's running on the GPU, but we have a bunch of tools as well that are computational, as I decided to call them here. So kind of things that run on the CPU, right, like the static analysis is the best example, I think, to think about this. Yeah. And we have the same distinction on the feed-forward, on the guide side. So we can also think about computational guides on that side.

**[6:50](https://www.youtube.com/watch?v=wBBCJinOes4&t=410s)** And the best example for me there is codemods. Ian from Meta also just mentioned those, which is, for example, tools like OpenRewrite that are really good at doing version upgrades and migrations of frameworks. I don't know if you remember, like, quite a while ago, Amazon had a really big headline about saving 400 or 500 developer years or something for Java upgrades. That was, under the hood, actually mostly codemods being made available to AI. So that combination is really powerful, right? So all of these things, or maybe providing a different type of code search that is more effective for your really large code base. All of those are ways, again, to increase the probability that AI does what you want in the first go. And to close, Guy Podjarny, CEO and co-founder of Tessl.

**[7:41](https://www.youtube.com/watch?v=wBBCJinOes4&t=461s)** He makes the case that all of this adds up to a whole new life cycle, sitting alongside the one we already know. Humans move into the context development lifecycle and the agents get the software one. And at the end of the day, we can build really quality software. But there's only so far you can get in the lab. And so you can build your software, you can test it, you can secure it, you can optimize it. And then at some point you need to step out. And that comes into observability for agents. Runtime observability is monitoring the coding agents. And when you monitor those, you can use those to improve the quality of what you have. So you can extract real-world eval scenarios and problems and use those to update and optimize your skills. And you can mine for gaps. So you can look at agents' success as a whole and extract out of

**[8:28](https://www.youtube.com/watch?v=wBBCJinOes4&t=508s)** that opportunities for new skills or things that you should remove. And in general, as you think about this whole process, combining all these tools together, you increasingly should see a development lifecycle. But it should be a context development lifecycle, not a skill, not a software development lifecycle. We should, as humans, live in the context development lifecycle and leave the SDLC to the agents, or be able to enable the agents to do the SDLC, in which we generate context, evaluate and test it, optimize it as we need to, distribute it via good package management. Securely consume them, observe what has happened, and do that again and again. So in summary, we have a new software stack for agent development. It builds on the models that are like our operating systems. We need to make sure what we build is compatible with them.

**[9:18](https://www.youtube.com/watch?v=wBBCJinOes4&t=558s)** We have tools as utilities. We have context as the new code. We have harnesses that are like frameworks. Not every developer will build their own harness, but probably more and more organizations would substantially customize harnesses if not build their own, with those composing into factory lines that feel very much like pipelines. You have repeatable type of input coming in, successful output coming out, and into whole dev processes in factories. And within those, skills are the new code, and we should treat them that way and give them the right tools for it. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
