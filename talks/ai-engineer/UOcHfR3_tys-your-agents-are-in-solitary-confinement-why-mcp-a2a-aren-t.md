---
id: UOcHfR3_tys
title: "Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band"
slug: your-agents-are-in-solitary-confinement-why-mcp-a2a-aren-t
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Vlad Luzin"]
channel: "AI Engineer"
duration_min: 18
published_at: 2026-09-30T13:00:33Z
video_id: UOcHfR3_tys
url: https://www.youtube.com/watch?v=UOcHfR3_tys
youtube_url: https://www.youtube.com/watch?v=UOcHfR3_tys
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "multi-agent systems", "AI agents", "agent orchestration", "agent-to-agent communication", "A2A", "MCP", "Model Context Protocol", "loop engineering", "Claude Code", "Codex", "LangGraph", "CrewAI", "distributed systems", "agent interoperability", "agent observability", "Band", "Vlad Luzin", "AI Engineer World's Fair"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Evals, observability & reliability"]
transcript: true
---

# Your Agents Are in Solitary Confinement: Why MCP & A2A Aren't Enough — Vlad Luzin, Band

**Vlad Luzin**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#multi-agent systems` `#AI agents` `#agent orchestration` `#agent-to-agent communication` `#A2A` `#MCP` `#Model Context Protocol` `#loop engineering` `#Claude Code` `#Codex` `#LangGraph` `#CrewAI` `#distributed systems` `#agent interoperability` `#agent observability` `#Band` `#Vlad Luzin` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=UOcHfR3_tys) · [Conference site](https://www.ai.engineer/)

## Description

If you run Claude and Codex side by side, one planning and one reviewing, you're doing the job of a network router, passing messages between two stateful agents by hand. Loop engineering hands that job to a script. Neither one lets agents actually work together.

Vlad Luzin (Co-founder & CTO, Band) explains why connecting agents is a distributed systems problem. Bigger context windows don't fix the single-agent bottleneck. Messaging platforms like Slack, Discord and WhatsApp are built for humans and block bot-to-bot traffic. Protocols like MCP and A2A are too low-level: stateless calls, one-way client/server, no discovery, and queues and timeouts you still have to build yourself. He then walks through what's needed: real-time ordered transport, persistence and rehydration, runtime binding across frameworks, agent-first abstractions (participants, rooms, routing) and enterprise governance. Two live demos show Codex, LangGraph, Claude Code and a personal assistant finding each other and collaborating in real time, with full human-in-the-loop visibility.

Speaker info:
Vlad Luzin

COMPANY
Band: https://band.ai
X: https://x.com/band_hq
Product Hunt: https://www.producthunt.com/products/band

Timestamps:
0:00 Band's thesis: the future is AI-to-AI communication
1:29 What agent-to-agent collaboration will look like
2:04 Adversarial agents: you are the router
2:49 Loop engineering, distilled
3:34 The single-agent bottleneck
4:04 Why messaging platforms fail agents
5:33 Why MCP and A2A aren't the answer
7:08 Recap: multi-agent is already here
7:43 It's a distributed systems problem
8:17 Transport, persistence and runtime binding
9:12 New abstractions, identity and observability
10:17 Introducing Band: a global interaction layer for agents
11:27 Demo 1: onboarding Codex, LangGraph and a personal agent
14:11 Demo 2: Claude Code and Codex collaborating (loop engineering without the code)
16:20 Wrap-up

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,549 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=UOcHfR3_tys&t=1s)** [music] Hi all, my name is Vlad. I'm co-ounder and the CTO at B. Now before we start, let's uh do a bit of trivia or C. Okay, if C, raise your hand. Okay, who believes both are correct? Okay, just a couple. Both are correct. One is from the Lord of the Rings. Another is from Warhammer game game workshop games. I have in my agenda four topics to cover. Topic number one, I would like to

**[0:49](https://www.youtube.com/watch?v=UOcHfR3_tys&t=49s)** tell you about our physics as a company, what we believe in. Then we will talk about the evolution from adversarial agents to loop engineering and beyond. Then we'll touch base on the technical challenges of tomorrow that we have to solve today. And then I would like to present the company what we do and what problems we solve. So our thesis is future belongs to AI to AI communication within a business between businesses and between consumers and businesses. Agents will be everywhere. They will do work on our behalf and they will have to communicate between each other. They will be written in different frameworks, different languages and deployed in different environments. And these agents will be fully autonomous and they will communicate with each other without

**[1:37](https://www.youtube.com/watch?v=UOcHfR3_tys&t=97s)** human intervention. Now just to paint a picture before I start talking uh how this type of communication between the agents is going to look like. So what you see here is a conversational space that agents can create themselves. So they can be added. They will receive a task either from a human or from another system and they will be able to discover other agents, add them as a participants in this conversational space, have back and forth communication, solve the task and report back to humans. This is how the future that you all read in the newspapers will look like. And when people hear this, they think either that this is too far in the future or that I'm crazy. Okay, that's it.

**[2:25](https://www.youtube.com/watch?v=UOcHfR3_tys&t=145s)** And here is an example of a conversation I had with a CTO of10 billion company who said that before thinking about technical solutions to hypothetical problems like multi-agent coordination, I try to keep things simple and avoid the problem. Now let's unpack. Is multi-agent coordination a hypothetical problem? Is it possible to keep things simple? and is it possible to avoid the problem? Now, let's talk a bit about the adversarial agents as a as a concept. Um, we all use this. I'm pretty sure everyone here is a developer. And as a developer, you have two cloudcoded sessions. One is doing the work, another is reviewing the work. And you probably

**[3:13](https://www.youtube.com/watch?v=UOcHfR3_tys&t=193s)** have not only two sessions, you probably have multiple tabs and multiple sessions working at the same time on multiple problems. You are basically acting as a router, a Cisco router or a switch between two stateful agents that do work on your behalf, but they have no ability to communicate. Hence, you need to prompt them. Let's talk about loop engineering. You've heard the the guy before talked about Peter and Boris, right? So what they say to you? They basically say to you, stop being the router between your agents and let your agents prompt each other. Now what they're basically saying to you is instead of being the router and copy pasting stuff, start fighting

**[4:01](https://www.youtube.com/watch?v=UOcHfR3_tys&t=241s)** with Python and TypeScript libraries and different abstraction layers that will invent how agents should prompt each other. We also have protocols A2A, MCP, ACP and 10 other protocols cryptoreated. Simple solves all the problems, right? So this is how your mutated system looks like probably in production MCP maybe if you're super advanced it's A2A and sounds simple. You call agents as tools. Maybe you connect to agents through A2A and life is great. But MCP calling agent as tools. It's completely stateless. If you want two agents to be stateful sticky sessions, good luck to you. A2A is client server. If I'm an agent, I can send a task to another

**[4:52](https://www.youtube.com/watch?v=UOcHfR3_tys&t=292s)** agent. But if this agent also wants to send tasks to me, we both have to be a client and a server. Chaining multiple agent calls together involves rest API timeouts. Good luck managing that. And obviously what no one says to you, you need cues with persistency and so on to keep track of the messages that are being sent. And of course discovery which is not even part of the A2A protocol. So you are basically doing the planning work. You're not creating a multi- aent system. You deal with planning. But we have messaging platforms. Slack Antropic released a wonderful agent. You can talk to it in Slack. We have personal agents here and they connected to Telegram, right? Wonderful.

**[5:42](https://www.youtube.com/watch?v=UOcHfR3_tys&t=342s)** To connect an agent to a Telegram, five steps. Discord, seven steps. Slam, eight steps. WhatsApp, 11 steps. Every step is manual that you have to do by hand and you have to read the documentation. Again, you're doing doing a lot of planning and manual work. And this gives you only one thing and one thing only. An agent that can talk to a person. Usually, it's you. Your agent is still alone. They cannot see each other. They cannot communicate with each other. They in digital solitary confinement. So let's unpack the stuff that I heard from the CTO. Is multi-agent

**[6:30](https://www.youtube.com/watch?v=UOcHfR3_tys&t=390s)** coordination a hypothetical problem? Clearly if you are copy pasting stuff between two sessions, this is the problem of today and it's not hypothetical. Plugging in MCPS and A2A, this is today's problem. It's not a future problem. Is it possible to avoid the problem? Clearly it's not possible because otherwise we would have all worked with only one session and not two and we would have no need to call other agences tools and so on. But the question is, is it possible to keep things simple? And the answer is if we look at all the options that we just talked, not really. But how hard can it be to connect two sessions, two processes on my laptop

**[7:18](https://www.youtube.com/watch?v=UOcHfR3_tys&t=438s)** together? How hard can it be to connect my cloud to Landruff or Salesforce agent to the datab bricks agent to SAP agent to my my my codeex actually it's pretty hard think about it these agents even your two sessions are processes that have to talk to each other through a network so it's a distributed systems problem and distributed systems are hard even before you have introduced agents on top of it and multi- aent system where every agent is remote is basically a distributed system of microservices where each microser is nondeterministic. So it is hard. What do you need to solve all of that? So it will become easy. You need

**[8:06](https://www.youtube.com/watch?v=UOcHfR3_tys&t=486s)** to solve the transport layer order message delivery, realtime message delivery, retries and so on. You need to solve continuity microservices, your agents, their software, ports, dockers, crash and so on. So you need to have a persistency hydration. You also need to do the runtime binding between different agentic frameworks. You have thread ids, conversation ids, execution ids and so on. And someone needs to map all of these IDs together. So your agents can actually interact. But it's also not enough. Your agents cannot communicate at an IP port level. They cannot communicate at the URL level. They cannot even communicate at the popsup level because it's still a lot of planning that you need to do as an organization. So for this wonderful

**[8:53](https://www.youtube.com/watch?v=UOcHfR3_tys&t=533s)** future of agents talking to each other, we need to raise abstraction of a technical stack to conversation and talk about rooms, channels, participants and figure out the deterministic routing of messages within a channel and also across different channels. And even if you solved all of that, it's still not enough. You need to solve the governance layer, the identity audit and etc. So I would like to introduce band. This is exactly what we solved so you don't have to. We connect every agent together and we add global collaboration layer for all the agents any framework whenever they deployed inside. It's not just the communication. We implemented every primitive that is required for your agents to talk to each other.

**[9:43](https://www.youtube.com/watch?v=UOcHfR3_tys&t=583s)** Let's see demo. What you will see are two different users connected to the collaboration layer. Vlad with a personal assistant and Mike that has no agents. On the right in a terminal, I'm going to spin up different agents and they will be on boarded into the platform. So let's see how fast it is to on board a new agent. We just spun up a new agent. Programmatic registration and on boarding an agent card appears. This is a Codex agent. Next we spin up a langraph agent. This langraph also appears in the platform. From this moment they know that they exist and they can talk to each other. Now we will ask Codex agent to send a connection request to my personal assistant. Keep in mind different users different registries. There will be a connection

**[10:32](https://www.youtube.com/watch?v=UOcHfR3_tys&t=632s)** request contact request sent to my personal assistant. It will require bilateral consent. It will arrive here in a second. And from the moment that I approve this, Codex will know and see my personal assistant will be able to invite the personal assistant into the conversation and send messages to this personal assistant. So we asking the codex to invite Andy. And he got invited, received the message, reported back. But let's talk about problems of today. We are all developers. We use multiple sessions, probably a lot of sessions. We do routing. We don't like it. And when

**[11:23](https://www.youtube.com/watch?v=UOcHfR3_tys&t=683s)** we go to uh have a snack, we come back and we have no idea what our agents have done. And you as a manager have no idea uh how much it cost the distribution uh of ticket and the tokens and so on and so forth and you have no idea even how long your human was involved in in the work. I would like to introduce gem. Gem is internal product. This is how we develop the software and we've built it on top of bank. Jam is a desktop application that simplifies the onboarding of your local agents to the platform and uh solves uh problems that we just mentioned. So we solve routing, we solve context overload, we solve cost management and

**[12:12](https://www.youtube.com/watch?v=UOcHfR3_tys&t=732s)** attribution and we allow multi- aent and multihuman collaboration together. So what you see here is local agents and remote agents working together and we capture all the tasks generated by cloud and codeex that uh they generate for themselves when they do the work and we present this to you so you can track the work that these agents are doing and this can be your local sessions or your local session with a session with your friend because trying to understand what your agents are doing. 1 million tokens multiplied by three, that's a lot. You need a completely different way to understand what your agent team is doing. Moreover, we provide a way for agents to describe the layout of the

**[13:02](https://www.youtube.com/watch?v=UOcHfR3_tys&t=782s)** software architecture that they are working on. This is what you see on your right side. And you can see in real time where your agents are working right now, what piece of component they're touching in real time. And once they're done, the market is done. If there is a human in the loop involvement, you'll get pinged. Now, you don't have to use this desktop application. You still can open your uh terminal and you can work from your terminal. But because every communication goes through the network, we can monitor all that stuff and we can surface a lot of other very useful information and we can enable my agent join your agent. We can enable our team member who works remotely to join the session together with the agents and the

**[13:50](https://www.youtube.com/watch?v=UOcHfR3_tys&t=830s)** humans. So he can help solve us at some problems. If we have a security guy who maintains skills for the security uh agent, I don't need to copy his skills. I can just ping his agent to join this conversation and solve uh this uh for me. Now I'd like to show you the platform itself. So since we all managers, we'll start with graphs. Uh so the moment you open application, you can see all the stats of all the traffic that happened between your local agents and also your remote agents. You can see for instance over here I have a full stack developer uh $2,000 in tokens and this is a local cloud session. You can see an architect over here $600. This is a local codeex

**[14:39](https://www.youtube.com/watch?v=UOcHfR3_tys&t=879s)** session and the rest are different a agents running in different environments. But how do they work together? Right? Do we have a bunch of Python code triggering the agents so they can look together? We do not because all models right now they trained on a lot of data. So they understand very very good how to communicate through messaging platforms. So here I have real work that I've done this morning engineering manager developer and architect different instances of cloud code working together reviewing PRDS and SRS reviewing implementation. There is no need to handcode all the loops. They know how to do it natively.

**[15:29](https://www.youtube.com/watch?v=UOcHfR3_tys&t=929s)** And for the managers, we have full statistics. Let me kill off the man the engineering manager who sent too many messages. So you can see the attribution. You can see the [clears throat] full usage and cost. So if you ask your question if my developer is actually involved in the code that he pushes as a PR or it's all AI slope, you can see it here. Not only locally, right, but also through the remote agents. You can see attribution by developer or by teams of your agents and developers and how they work. Everything is gets updated in real time. You can see all agents and every agent is basically a session, right? So if I click here, I can see all the sessions of my cloud and codex instances that are

**[16:18](https://www.youtube.com/watch?v=UOcHfR3_tys&t=978s)** running and they're connected to the platform and they're connected to a global platform. So if I want I can connect any of you to any of my agents in 30 seconds. Obviously you can set permissions. You can see all the rooms. You can see all the apps and so on. And also you can see work what work was done, what is pending, what is in progress and everything works in real time. Thank you very much. If you want to know more about the future software development that does not involve you pulling another 50 packages and if you want to enable your Salesforce and Slack and data bricks and cloud and codex to work together and collaborate come to our boog7 QR codes for the band the infrastructure layer and for the gem the uh desktop

**[17:05](https://www.youtube.com/watch?v=UOcHfR3_tys&t=1025s)** application to allow you to be part of this future that everyone talks about but has never seen. Thank you. >> [applause]
