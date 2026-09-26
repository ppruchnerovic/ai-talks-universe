---
id: SLh-wN45ZIM
title: "Docker, Adobe & tldraw: Where Should Your Agent Run?"
slug: docker-adobe-tldraw-where-should-your-agent-run
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-16T15:00:09Z
video_id: SLh-wN45ZIM
url: https://www.youtube.com/watch?v=SLh-wN45ZIM
youtube_url: https://www.youtube.com/watch?v=SLh-wN45ZIM
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Docker, Adobe & tldraw: Where Should Your Agent Run?

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=SLh-wN45ZIM) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Four builders spent AI DevCon London answering the same harness engineering question at the center of agentic coding — where should a coding agent actually run — and landed on four different machines. Docker isolates it in a microVM sandbox, Helix ML gives it a whole computer of its own, Adobe runs it inside your browser tab, and tldraw puts it on an infinite canvas as a character you can pick up.

Oleg Šelajev (Docker) walks through why containers weren't a boundary security teams would sign off on, and what changed when Docker rebuilt its agent sandboxes on micro VMs instead. Luke Marsden (Helix ML) makes the case for giving every agent its own computer on centralized infrastructure, so work can hand off between people in different time zones. Lars Trieloff (Adobe) built an agent that runs entirely inside the browser tab it's controlling — with a reveal about what it had actually been doing the whole talk. And Steve Ruiz (tldraw) shows agents living on the canvas as small characters you can grab, direct, and watch coordinate as a team.

What we cover:
– Why Docker's security teams rejected containers as an isolation boundary
– Building a sandbox on micro VMs instead of containers
– The case for giving every agent its own computer
– An agent that runs — and controls — its own browser tab
– Agents as characters living and collaborating on an infinite canvas

Chapters:
00:00:00 - Introduction
00:00:09 - Oleg Šelajev, Docker: from containers to micro VMs
00:01:43 - Docker Sandboxes: isolating the agent's machine
00:03:03 - Luke Marsden, Helix ML: give each agent its own computer
00:03:59 - Why the centralized approach wins
00:05:23 - Lars Trieloff, Adobe: an agent that runs inside the browser
00:06:13 - The self-licking ice cream cone (SLICC)
00:07:20 - Steve Ruiz, tldraw: agents live on the canvas
00:09:43 - Coordinating a team of agents

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which answer would you actually trust in production — sandbox, dedicated computer, browser, or canvas? Tell us in the comments.

## Transcript

*1,534 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=0s)** Back in June at AI DevCon in London, we got four completely different answers to what sounds like a simple question where should the agent actually run? Let's first hear from Oleg Šelajev at Docker, who built a sandbox on containers, was told by enterprise security teams that containers are not a boundary they trust and went and rebuilt it on micro VMs. All right. Hi, my name is Oleg. I work at Docker. I'm a member of the DevRel team, doing all things AI at Docker, we thought about this, and when we were building sandboxes, we built one version with containers. We went out, we talked to a bunch of security teams at enterprises, and all security teams said that no, containers are not the isolation boundary that we can trust.

**[0:52](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=52s)** So being great engineers, what did we do? We rewrote that using micro VMs. So containers for micro VMs might not sound like such a big difference, but if you're sharing a kernel, if you have a number of security vulnerabilities for exploiting from outside of the container, that is not something that, well, a security team can sign off because it's going to be, well, their jobs and their reputation when the leaks will happen. And yeah, I'll bite. Container escaping exploits are not frequent. There are like a dozen over the last maybe six or seven or eight years. But as we discussed, you only need to be breached once and then it's. And then it's bad.

**[1:38](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=98s)** So you want the hardware sort of virtual machine isolated primitive. And this is what Docker has built for the sandboxes, the SBX thingy that runs in micro on your machine. And then your agent is put there within the container. In addition to that you can this micro can run other containers. So if you are doing using agents for software development, the agent within this micro can do exactly what you would do. It can run tests. Your tests might spin up some containers, maybe with Testcontainers libraries, maybe just a normal Docker Compose approach, but they can create the full environment, run your applications, and that gives you much more control over how your agent can develop software, because it can do whatever you would do on your machine, just fully isolated.

**[2:28](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=148s)** So and within that sandbox, within that, there is no access to the host file system. You choose what you share with the thing. You have the networking proxy. So all the requests out of the sandbox go through that. So you have control saying, please forbid all access to Pastebin. So if the agent wants to steal the keys, it cannot do that this way. And there is also a secrets injection mechanism. So the agent inside doesn't have access to your private data while still be able to do things on your behalf. We also heard from Luke Marsden, CEO of Helix ML, who takes the opposite view — from your laptop, entirely. Put the agents on the organization's infrastructure so the work can be handed between people in different time zones.

**[3:17](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=197s)** His line is that you should give each agent their own computer. The first big decision, in my opinion, is: do you want to carry on letting every developer run whatever agent they like, or maybe the same agent that everyone uses in the company, but on their own specific development environment? That's kind of like a snowflake. Or do you want to create a pool of agents that run on your organization's infrastructure that many humans can interact with? And my strong argument is that. Going for the centralized approach and I say centralized, it doesn't mean you have to hand over all your data to OpenAI or run on their infrastructure or anything.

**[4:07](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=247s)** You can run it on your own infrastructure. Still on Kubernetes or something, but there are some significant benefits from having a centralized approach. For example, you can have a globally distributed team all around the world, and you can say that when the sun sets in Tokyo and rises in London, whoever a different human can carry on doing the work that a certain agent was working on, especially if that agent truly has its own computer for that specific task. And so there's a really nice article written by by someone. We've been working with a company called Dev Icon, and what they said was, to be honest, agentic coding is not new.

**[4:58](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=298s)** Going from doing it the easier way, which is the way on the left which is unsafe and per engineer to something global per company and safe is what they found interesting in this approach. So that's kind of my argument. My opinion number one is you should give each agent their own computer, not each human. It's almost like you wouldn't hire a team of software developers and ask them all to share one computer. You should give each agent their own computer. Lars Trieloff is a principal scientist at Adobe, and he built an agent that runs inside the browser and drives the browser it's running in. There's also a reveal at the end of his talk that I'll let him deliver himself. How do we get started with this? And the. The idea that I came up with was an agent that is sitting in the browser. It's actually running in the browser, which means it's not a cloud runtime

**[5:51](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=351s)** where the agent loop runs and you're just displaying in the browser, but it's actually the actual agent loop is in the browser. To close the browser tab, the agent loop starts, and at the same time this agent should be able to control itself. It should control it should it should control the browser that it's running inside. And this is how I came up with this notion of the self-licking ice cream cone. And that's why you find it at SLICC, sliccy.com And while building it, there are a bunch of things that I was absolutely sure. Well it's a browser right. It can display HTML pages. But there are a lot of things that it suddenly cannot do right.

**[6:39](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=399s)** So cannot transcode videos. It suddenly cannot access my local file system. But I'm fine with these constraints. But in reality, I found during this exploration that there are so many things that my browser can do that I didn't even dare to think about. And that was one of the things that made this exploration extremely fun. And now you're wondering what this what this slide means. And this slide means that I haven't been showing you a presentation for the past ten minutes. I've been showing you SLICC. I've been showing you the very agent that we are going to talk about. And to close, Steve Ruiz, founder and CEO of tldraw, with the answer nobody else gave the agents live on the canvas

**[7:29](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=449s)** as little characters you can pick up, throw, and talk to. Then he selects three at once and they elect a leader. We wanted to bring it onto the canvas in the same way that, like, you know, other users are on the canvas. So that led us to. To fairies. To these guys. So each one of these is an instance of that, that harness that lives kind of on the canvas. And while it started with just being like a way of visualizing the agents — number one, like, just where are they? Which ones exist, which one is which. Right. You can kind of configure them and change their hat

**[8:20](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=500s)** Or, because we needed two things, like, you can change the length of their legs. I don't know if you can see that, whatever — you can toss them around. You can hold them. They don't like that. Yeah. Right on. But you can talk to them as well. Make a move as X and you can you can visualize the state of the agent as well. So whether it's thinking or reviewing or working cool. Make a move as Oh, and you can ask them to do things. And again, it's pretty much the same harness as we looked at with the whole cat on the table thing. But there they can exist simultaneously. They know about where each other are.

**[9:08](https://www.youtube.com/watch?v=SLh-wN45ZIM&t=548s)** This is worse on live coding, by the way. Let me try this. Maybe we can get them to work as a team. So if I grab all three of them and I say play a full game of tic tac toe. Then they will operate as a unit. One of them will be elected leader and will draft a plan. Their wings will change colors to indicate that they're on the same team. By the way, this is also collaborative. You could have multiple people kind of sharing the same experience. Coordinator comes up with a to-do list and then delegates those tasks to different fairies, different agents. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
