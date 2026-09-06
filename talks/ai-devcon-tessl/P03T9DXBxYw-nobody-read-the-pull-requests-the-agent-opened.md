---
id: P03T9DXBxYw
title: "Nobody Read the Pull Requests the Agent Opened"
slug: nobody-read-the-pull-requests-the-agent-opened
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-03T16:00:22Z
video_id: P03T9DXBxYw
url: https://www.youtube.com/watch?v=P03T9DXBxYw
youtube_url: https://www.youtube.com/watch?v=P03T9DXBxYw
tags: []
topics: ["AI in the SDLC & engineering orgs", "Agents & orchestration", "Coding assistants & agents", "Enterprise adoption & strategy", "Evals, observability & reliability", "Inference, serving & GPU infra"]
transcript: true
---

# Nobody Read the Pull Requests the Agent Opened

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=P03T9DXBxYw) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Coding agent reliability stops being an abstraction at three in the morning, when somebody still has to run the thing. Day 2 of AI DevCon London went looking for what changes once agents are in production, and the stories turned out to be better than the demos.

A panel assembled at short notice — Stéphane Jourdan, Simon Rohrer and Pini Reznik — works through what happens when everyone in the company is shipping through an agent around the clock, and why the scarce thing isn't root cause analysis but context: what changed yesterday, which service talks to which. Simon works in a regulated industry, and says what surprised his developers most wasn't code generation at all — point an agent at Elastic logs, ServiceNow incidents and the code together and it settles in 30 seconds what would otherwise eat hours of digging. May Walter (co-founder and CTO, Hud) gives the best kind of talk, the one about something that didn't work: they automated the investigation and opened a pull request for every high-impact fix, and nobody read them, so they rebuilt the output to convince the human rather than the agent. Amit Kushwaha (NVIDIA) has the counterintuitive finding — your GPU sits idle while the agent is off making a tool call, and account for that properly and you can serve roughly twice the users your benchmark predicted. And Justin Cormack, formerly CTO at Docker, names his single most useful debugging investment: getting the AI to build him a tracing framework, because an agent handed a rare bug with no reproduction guesses, and an agent handed a trace finds it.

What we cover:
– Why context from production beats root cause analysis
– What surprised developers most about pointing agents at an incident
– Why automated pull requests go unread, and what to send instead
– Ranking fixes by business impact and risk instead of by optimisation
– Why your GPU is idle during tool calls, and what that does to concurrency
– Giving an agent a trace instead of a bug it can't reproduce

Chapters:
00:00:00 - Introduction
00:00:25 - Panel: Stéphane Jourdan, Simon Rohrer, Pini Reznik on agents in prod
00:01:50 - Simon Rohrer: agents are startlingly good at diagnosing production
00:03:01 - May Walter, Hud: the automation nobody wanted
00:03:36 - Why the automated pull requests went unread
00:04:42 - Convince the human, not the agent
00:05:28 - Amit Kushwaha, NVIDIA: benchmarking the agent era
00:06:36 - Your GPU is idle while the agent makes a tool call
00:07:42 - Justin Cormack, formerly Docker: build the tracing framework first
00:08:59 - Give an agent a trace, not a bug it can't reproduce

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

What's the first thing you'd point an agent at in production? Tell us in the comments.

## Transcript

*1,692 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=P03T9DXBxYw&t=0s)** Back in June at AI DevCon in London, we spent a lot of time on writing code with agents, but somebody still has to run the thing at three in the morning, and that turned out to be where some of the most interesting stories were. Let's first hear from a panel we put together at short notice with Stéphane Jourdan, Simon Rohrer and Pini Reznik on what changes when everybody in the company is shipping through an agent around the clock. So now you have agents by everyone, from everyone doing things in production. How do you know the impact of this 24 hours a day? It's constant and you really need proactive agents and all the context. What changed yesterday? What was the relationship between this service and this other service? How do you know that this service was actually connecting to the right thing? But the variable was not.

**[0:49](https://www.youtube.com/watch?v=P03T9DXBxYw&t=49s)** The name was the IP, that sort of stuff. So it's not only about like root cause analysis. It's really about like the, the context, all the knowledge you can have from prod your multiple accounts that all the stuff and agents today you mentioned like DevOps is a bit back in, in, in the space because the DevOps folks had a lot of tools, a lot of data to work with the code, etc. but for prod we really need to keep the lights up. So yeah, that data and that context is your point these days, including agents to fix this 24 hours a day. Because even from a security perspective, all the things that are being patched as well, constantly, you need to ensure that the blast radius of things are still working after this.

**[1:38](https://www.youtube.com/watch?v=P03T9DXBxYw&t=98s)** So everything, everything is so is going so quickly these days. We need — we need that data proactively. Simon, I can see you're violently agreeing. So I work in a regulated industry. We can't quite move as fast, but we're still moving pretty fast. I, like I said, I've been spearheading this and sort of coaching developers through. And I think one of the things for me that surprised the developers or, you know, we do "you build it, you run it". So it is really developer operators. The thing that has surprised our developers the most is how useful the agents are for diagnosing production. Yes, genuinely throw them at Elastic logs plus ServiceNow incident reports, plus the code and the combination. Like you said, is this knowledge that the agents can have they will solve an issue in 30 seconds

**[2:27](https://www.youtube.com/watch?v=P03T9DXBxYw&t=147s)** that could have taken developers hours or maybe even days to fully understand this stuff is so powerful, you know, and I think the people who are just using it in the development context really should, if they have that data available to them, like they say, if they've got the good observability stack in place, should start to expand there. They use it more broadly into this. And I think, you know, we are living through a seismic shift. We we don't know where we're going to end up. We don't know what the earthquake will do to us We also heard from May Walter, co-founder of Hud, and hers is my favorite kind of talk. One about something that went wrong. They automated the investigation, shipped pull requests for every high-impact fix, and discovered nobody wanted them. So they rebuilt the output to convince the human instead of the agent.

**[3:21](https://www.youtube.com/watch?v=P03T9DXBxYw&t=201s)** So we said, okay, maybe we can just like add open pull requests for all of these high-impact, low- risk changes that don't require migrations or anything super scary. And we can just open a pull request. No no no no no we don't want any pull requests that no one's going to go over and we don't want to go over those 80 PRs even though they exist. And I think that's like if I if you can take one thing out of this is like after you get it working and you want to automate it, think about the scale and think about the humans that are still in the loop. We're not at the point where no one just cares about it. And if you open a pull request, it's kind of like opening your Datadog and Sentry with those like 700 issues that all they say is like, well, I'm not going to be able to fix this, so I'm not even going to try.

**[4:13](https://www.youtube.com/watch?v=P03T9DXBxYw&t=253s)** So we of course, we started with automated pull requests. We realized no one cares about that. And if it's not prioritized, then they're not going to do something about it. And again, I am not complaining. I'm not judging. We're builders, right? We have prioritization and it exists for a reason. No one has time to just go over a bunch of pull requests built by the agent that are statistically huge, and try to understand what happens. We don't want to own that. We don't want to go into it. So we actually need to convince the human that it's worth the attention. Instead of convincing the agent that it's worth the tokens, it will always think that they are. So we map the hot paths, the endpoints that are invoked often the business impact of that. So is this impacting payments or authentication

**[5:04](https://www.youtube.com/watch?v=P03T9DXBxYw&t=304s)** or the set of things that you already know that you care about for your business? And also the risk? We are not looking for the best optimizations. We are looking for the highest-impact, lowest-risk changes that can be done so that we can go to the developer or the PM and say, hey, listen, it's like that small and it's going to do like 30% improvement. Amit Kushwaha is a principal solutions architect at NVIDIA, and he has a nice, counterintuitive finding. While your agent is off making a tool call, the GPU is sitting idle. Account for that properly and you can serve about twice as many users as your benchmark predicted. The other thing that you need to think about. So I have two colorful blocks here.

**[5:54](https://www.youtube.com/watch?v=P03T9DXBxYw&t=354s)** Different rows are basically user, user one, user two, user three, user four. And what this slide is trying to convey is if you ignore the tools tool part of it, you're not really measuring the right workload again. So on the left side I'm assuming there is no tool call. So there is none of that purple block that I showed where the kind of things are running on the CPU. In that case, what you ended up saying is user one, user two, user three, user four are fully packing my elements or fully packing my GPUs. So this whole block is basically when your large language model is being called. But in reality, that's not the case when you are running close. This is not how your GPUs look like.

**[6:42](https://www.youtube.com/watch?v=P03T9DXBxYw&t=402s)** You're not continuously kind of keeping your GPUs busy. What is happening is you run your large language models and then actually you are running tool calls which are which are running on your CPU. So actually your GPU is not doing any work during that time. And depending on how big that variation is, you can actually support more users because you are effectively not packing GPUs as much as you can. So just ignoring the concept that there is no tool actually ends up predicting the wrong concurrency or wrong workload that that that you can support on your hardware. And there are some metrics there, like if you assume one call takes one second,

**[7:30](https://www.youtube.com/watch?v=P03T9DXBxYw&t=450s)** if you have a tool call that takes one second, two and half of your areas, you can actually support twice the number of users than you thought, because a bunch of that work load is being done on CPU too. And to close, Justin Cormack, formerly CTO at Docker. His single most useful debugging investment was getting the AI to build him a tracing framework Hand an agent a rare bug with no reproduction, and it guesses, Hand it a trace from an overnight run and it finds the thing I discovered that like even just getting the AI to build a hand-built, hand-maintained tracing framework was incredibly useful. You don't need to tie it into a production system or something, but anything that can give it traces that it can look at to debug is amazingly useful.

**[8:20](https://www.youtube.com/watch?v=P03T9DXBxYw&t=500s)** It in this case it had a bunch of overheads, so when I used it for performance testing it was a little bit misleading. But it told it, you know, basically gave where the the big the big performance gaps were. And it was incredibly useful for debugging because I could give it, you know, I could run the test, I could have my test suites running, looking for race conditions or errors, give it a trace and say this happened overnight in my overnight run. We need to fix this. And it would it would let it actually lock down on what the real problem was rather than trying to guess. Because if you if you give an AI a bug but you don't know how to repro it, and it's a very it's a rare condition.

**[9:12](https://www.youtube.com/watch?v=P03T9DXBxYw&t=552s)** It can waste a lot of time either. I mean, it can either fail to reproduce itself or it can guess what the solution might be and get it wrong or something. And if you can give it a trace and some trace tooling and just get it to sit there and try and reproduce it and itself and see if it's the same thing, then it usually can. And that works really well. So you don't need to necessarily hook it up to a production environment. You can really do this just by building, by getting the AI to build some tracing tools for you. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
