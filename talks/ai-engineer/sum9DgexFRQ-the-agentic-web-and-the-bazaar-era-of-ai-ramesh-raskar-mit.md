---
id: sum9DgexFRQ
title: "The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab"
slug: the-agentic-web-and-the-bazaar-era-of-ai-ramesh-raskar-mit
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Ramesh Raskar"]
channel: null
duration_min: 12
published_at: 2026-07-12T14:00:07Z
video_id: sum9DgexFRQ
youtube_url: https://www.youtube.com/watch?v=sum9DgexFRQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# The Agentic Web and the Bazaar Era of AI - Ramesh Raskar, MIT Media Lab

**Ramesh Raskar**

`AI Engineer` · `AI Engineer` · `2026` · `12 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=sum9DgexFRQ) · [Conference site](https://www.ai.engineer/)

## Description

The AI agent industry is currently focused on memory, orchestration, enterprise deployment, and tooling. But these are the first steps toward a larger transformation: the emergence of the Agentic Web.

Today’s ecosystem resembles the early days of AOL: closed platforms, proprietary agent stores, and siloed orchestration layers. The next era of AI agents will require open infrastructure that allows agents to discover, transact, and co-learn across organizational boundaries.

This talk explores three layers of the Agentic Web.

First, the Discovery Layer: agents will require discovery infrastructure analogous to AltaVista or Google—but for agents instead of webpages. The challenge is no longer PageRank, but “AgentRank”: how agents are discovered, trusted, verified, and coordinated across the open web. This creates the need for ICANN- and W3C-like governance and standards for agents.

Second, the Commerce Layer: what is the dollar value of intelligence? Agents will pay for reasoning, inference, memory, capabilities, and context through emerging “knowledge pricing” markets. Intelligence itself will be discovered, priced before use, coordinated among untrusted entities, and delivered in new ways.

Third, the Bazaar Layer: the last 14 years were about machine learning. The next decade will be about machine co-learning.

Speakers:
- Ramesh Raskar (MIT Media Lab): Ramesh Raskar is an Associate Professor at the MIT Media Lab and founding architect of NANDA whose pioneering work spans distributed AI agent architectures, health technology, and computational imaging, holding 100+ US patents and earning honors including the National Academy of Inventors award (2024), the Lemelson Award (2016), and the ACM SIGGRAPH Achievement Award (2017), alongside research roles at Google [X], Apple, and Facebook and the co-founding or advising of several companies.

## Transcript

*1,916 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=sum9DgexFRQ&t=1s)** Welcome everyone. Over the next few minutes, we're going to talk about the open infrastructure being built for a web of agents. Why it's needed, what's already shipped, and exactly where your own agent fits into it. It comes out of Project Nanda, an open research effort that started at MIT. And by the end of this presentation, you will know how to put an agent that you build yourself on the open web all by yourself. So, let's get into it. I'm Ramesh Raskar, professor and at MIT and director of Project Nanda. And Maria is a core contributor to Project Nanda. So, first, what is Nanda and why does it

**[0:49](https://www.youtube.com/watch?v=sum9DgexFRQ&t=49s)** need to exist? Nanda, which stands for network AI agents in a decentralized architecture, is an open research building the infrastructure for an internet of AI agents, the way open web was built for documents. The gap it fills is concrete. Agents have no shared way to find each other across vendors, no portable identity or trust that isn't owned by a single platform, and no open way to transact and coordinate across organizations. Nanda builds that missing layer and ships it in open. The index, the registries, the protocol, and the Nanda Town Simulator you will see later. Here's the premise that drives it all of

**[1:36](https://www.youtube.com/watch?v=sum9DgexFRQ&t=96s)** it. The internet is about to host not millions or billions, but eventually trillions of autonomous agents. They negotiate, they delegate, they migrate between hosts in milliseconds. That's a fundamental different load than the human web, and it strains the identity and discovery system we built for documents, DNS among them. The web that's coming needs infrastructure of its own. And we have been here before. If you're building agents today, you're mostly building them or you're forced to build them inside walled gardens, closed platforms, proprietary agent stores, and orchestrations that only talk to itself. And it kind of works. But, you know, it

**[2:25](https://www.youtube.com/watch?v=sum9DgexFRQ&t=145s)** also feels similar because we have been this we have been here before. This is like the AOL era from the late '90s where it was a closed network. You know, AOL, you got the CDs and you installed it on your PC. It was a closed network. It was a gated directory. You live inside the garden created by this one company called AOL. And what came after AOL was this open web. You know, everybody's in a permissionless manner creating websites, creating browsers, and any website can talk to any browser. And that's the transition that's about to happen to agents as well. So, the next era needs what the web needed, an open infrastructure where an agent from one company or one entity can discover agent from another. That agent can hand off work to it, pay

**[3:16](https://www.youtube.com/watch?v=sum9DgexFRQ&t=196s)** it, learn from it across organizational boundaries, no permissions required. There are three layers here, discovery, commerce, and what I will call the bazaar. So, hold on to those three concepts. We'll come back to them and and discussed. So, first the basics. >> Hey, my name is Maria and I'm a core contributor to Project Nondo. So, let's start with a simple definition of an agent. The way I think about it, an agent is a model that uses tools in a loop. Right, you give it a goal, it decides what to do next, it calls a tool, it looks at the result, then it keeps going until the task is done. So, that loop is the core idea. Everything else, like memory orchestration and multi-agent systems, is built on top of it.

**[4:04](https://www.youtube.com/watch?v=sum9DgexFRQ&t=244s)** So, you can build this agent loop in many different ways. One example is Open Claw. So, Open Claw is a self-hosted agent gateway. That means you can run it yourself and connect it to the apps and tools you already use. This matters because agents are not just chatbots. If an agent is going to do real work, it needs to access your real tools and apps. And if it has access to real tools, we should care about who controls it, where it runs, and how much we can see. And that is why open-source self-hosted agents are super important. They give people more control over their own agents. But then, we get a new problem. If agents are running in many different places, locally and on the clouds, on many different servers,

**[4:52](https://www.youtube.com/watch?v=sum9DgexFRQ&t=292s)** like owned by many different people, how do they find each other? And that is the job of the index. And this is what the Nanda index is built for. Nanda index is the discovery layer for the agentic web. It gives agents a shared place to publish who they are, what they can do, and how other agents can reach them. The regular internet already has a version of this with DNS. So, DNS maps a name to an address, so your browser knows where to go. But agents need more than an address. They need to know what another agent does, what tools it can use, what rules it follows, and how to talk to it. The index gives agents a common way to find each other and connect.

**[5:43](https://www.youtube.com/watch?v=sum9DgexFRQ&t=343s)** So, here's how the index works. An agent starts with the an identity like agent@hotmail.com. The NANDA index takes that identity and returns an agent card. So, the card says what an agent is, how to reach it, and where to send the messages. Messages do not go straight to the agent's runtime. They go to the message box first. The message box checks who is sending the message, handles access, filters spam or bad requests, and holds the message until the agent is ready. Now, the agent facts record is what makes discovery trustworthy. It is a signed record that tells other agents who this agent is, what it can do, what it is allowed to touch, who

**[6:30](https://www.youtube.com/watch?v=sum9DgexFRQ&t=390s)** built it, and where to reach it. So, before one agent connects to another, it can check the basic facts first. Now, the index is not just a lookup table. It does not point to one name to one fixed address. It can return updated agent facts based on the request. So, that means one agent can have many endpoints. Traffic can be routed to the best one, and private details do not have to be exposed. So, the resolution is adaptive. It changes based on where the agent is, who's asking, and what they are allowed to access. So, how do you put your agent on the index? You start at host39.org. So, you fill out the agent facts form, get an agent card, and publish it to the NANDA index.

**[7:17](https://www.youtube.com/watch?v=sum9DgexFRQ&t=437s)** Once it's listed, other agents can find it and know how to reach it. So, there are a few ways to get onto the index, depending on who you are. Enterprises can run their own catalog and register their gateway from their own domain. Existing websites can literally use DNS AID to connect agents to domains they already own. Small businesses and individuals can use host39, fill out the agent facts form, and get a hosted agent URL without needing their own domain. Goal is to make the onboarding work for everyone, from a large company to one person with a personal agent. Now that we know how agents get listed on the index, the next question is, where does the agent actually run? To be useful, an agent needs to stay

**[8:05](https://www.youtube.com/watch?v=sum9DgexFRQ&t=485s)** online and be reachable. You can run it locally, which gives you full control, but then you're responsible for keeping it up. For most use cases, it makes more sense to host it on the cloud. That could be on a general cloud like AWS, which is more enterprise ready, or on an agent hosting platform like Maritime, which is built to make hosting AI agents cheaper and simpler. So, a little bit about Maritime. Hosting one agent can be affordable, but the cost problem starts when you want to run many agents at once, for a team, a product, or a simulation. That is where per agent cost really matters. And Maritime is one way to solve this. It gives you a simple cloud default for running Open Clo or other agents with sleep and wake architecture, so idle

**[8:53](https://www.youtube.com/watch?v=sum9DgexFRQ&t=533s)** agents do not keep burning compute. And the point is to make running many agents practical, cheap, and simple. So, you can host an agent and list it on the index, but getting one agent online was always the easy part. The hard problems of the agent web live between agents at scale. So, how thousands of them discover each other, prove who they are, decide whom to trust, and coordinate with no central authority. So, you can't just assume that protocols will hold up under the load, and you have to test and run them and watch when they break. So, that's exactly where Nanda town comes in. So, how do you prove an open agent web actually works before it's load bearing on the real internet. You simulate it.

**[9:40](https://www.youtube.com/watch?v=sum9DgexFRQ&t=580s)** This is Nanda Town, an open-source project from Project Nanda. The easiest way to describe it is it's a simulation playbook for the infrastructure of the Agoric platform. So, think of it as a sandbox town where the whole Agoric economy is modeled, like discovery, identity, registries, messaging messages coordination all of it. So, you can run and test it on scale. Here's what it looks like in practice. Nanda Town is a live sandbox for testing Agoric networks. You can see agents on a map, watch messages move in real time, compare protocol results, and replay a run step by step. It's fully open source, it's small enough to run on your own laptop, and built to make Agoric networks easier to test and understand.

**[10:28](https://www.youtube.com/watch?v=sum9DgexFRQ&t=628s)** Nanda Town is already running real experiments. For example, there is a marketplace where buyers and sellers negotiate prices, an auction where agents bid on items, and and a voting test where agents submit and count ballots. There are also tests for consensus and supply chains. The point is to study real coordination problems, how agents make deals, agree on decisions, pass messages, and recover when something breaks. Under the hood, Nanda Town breaks the Agoric web into 12 parts. Transport communication identity registry auth trust payments coordination negotiation memory privacy, data effects. Each part is something a real Agoric platform needs. So, the registry layer is the Nanda index we just walked through, but here

**[11:15](https://www.youtube.com/watch?v=sum9DgexFRQ&t=675s)** it is just one piece of a bigger system. And you do not need to build everything to try it. You can take one layer, add your own version, run it inside Nanda Town, and see how it works with the rest of the network. So, Nanda Town runs as a discrete event simulation. You define a scenario in a short YAML file, inject agents and traffic, and the test bed plays plays it out so you can measure what actually happens end-to-end. Tier one uses simple scripted agents, and tier two swaps in real AI models. So, to summarize, Project Nanda builds the open infrastructure for an internet of AI agents. Discovery through the index, commerce through portable identity and trust, and coordination through open protocols, all tested in Nanda Town. And if you want to learn more, uh you

**[12:03](https://www.youtube.com/watch?v=sum9DgexFRQ&t=723s)** can go to projectnanda.org, read our papers, and um check out our latest projects.
