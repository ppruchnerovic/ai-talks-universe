---
id: toq-jyGLZDk
title: "Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND"
slug: why-your-ai-agents-can-t-talk-to-each-other-yet-vlad-luzin
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Vlad Luzin"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-07T18:30:34Z
video_id: toq-jyGLZDk
url: https://www.youtube.com/watch?v=toq-jyGLZDk
youtube_url: https://www.youtube.com/watch?v=toq-jyGLZDk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "multi-agent systems", "agent to agent", "A2A", "MCP", "loop engineering", "AI agents", "agent communication", "distributed systems", "Claude Code", "Codex", "LangGraph", "agent orchestration", "BAND", "Vlad Luzin", "AI Engineer"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Governance, ethics & regulation"]
transcript: true
---

# Why Your AI Agents Can't Talk to Each Other (Yet) — Vlad Luzin, BAND

**Vlad Luzin**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#multi-agent systems` `#agent to agent` `#A2A` `#MCP` `#loop engineering` `#AI agents` `#agent communication` `#distributed systems` `#Claude Code` `#Codex` `#LangGraph` `#agent orchestration` `#BAND` `#Vlad Luzin` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=toq-jyGLZDk) · [Conference site](https://www.ai.engineer/)

## Description

If you run Claude and Codex side by side, you're the router passing messages between them. It doesn't have to be that way.

Vlad Luzin, co-founder and CTO of BAND, argues the future belongs to AI agents talking to other AI agents, inside companies, between companies, and between businesses and consumers. Most of us already run multi-agent systems by hand, copying output between a planning session and a reviewing session, and loop engineering just hands that job to a script. He explains why: a single agent suffers from confirmation bias and attention dilution, no matter how big its context. Then he explains why messaging apps and protocols like MCP and A2A don't solve it, and why connecting agents is a distributed systems problem: ordered real-time transport, persistence, runtime binding, identity and observability. He finishes by launching BAND's interaction layer, with demos of agents onboarding in seconds and Claude Code and Codex working together across users.

In this talk:
• Adversarial agents, loop engineering, and the single-agent bottleneck
• Why Slack, Telegram, MCP and A2A fall short for agent-to-agent work
• What connecting agents really takes: transport, persistence, runtime binding
• Demo: Claude Code, Codex and LangGraph agents collaborating across users

SPEAKER
Vlad Luzin, Co-founder & CTO, BAND

LINKS
BAND: https://www.band.ai
BAND on X: https://x.com/band_hq

CHAPTERS
0:00 Intro
0:45 The thesis: AI-to-AI communication
1:29 What agent-to-agent work looks like
2:04 Adversarial agents: you're the router
2:44 Loop engineering, distilled
3:29 The single-agent bottleneck
4:18 Why messaging apps don't work
5:33 Why MCP and A2A aren't enough
7:08 Recap
7:52 It's a distributed systems problem
8:17 Transport, persistence and runtime binding
9:37 Governance, identity and observability
10:17 Introducing BAND
11:51 Demo: onboarding agents in seconds
13:01 Demo: connecting agents across users
14:11 Demo: Claude Code and Codex collaborate
15:45 Loop engineering without the glue code

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,444 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=toq-jyGLZDk&t=1s)** [music] >> Okay. Hi everyone. Can you hear me? A lot of people, yeah. So, please be quiet. So, my name is Vlad. I'm co-founder and CTO at Bend. And today I have four topics I want to discuss with you. First, thesis. Thesis of our company, what we believe believe in. AI evolution from adversarial agents to loop engineering and beyond. Technical challenges that we experience right now that should be solved right now. And obviously Bend to present the company and the product and what we do. Let's start with the thesis.

**[0:50](https://www.youtube.com/watch?v=toq-jyGLZDk&t=50s)** First of all, we believe that the future belongs to AI to AI communication within a business, between businesses, and between consumers and businesses. AI will be doing work on our behalf, and they will have to talk to each other in order to solve tasks on our behalf. Second, agents will be autonomous, always-on entities spread across the globe. Now, these are very nice words, but I want to spend a minute just to paint a picture in your head how this type of communication between agents actually is going to look like. Demo time. Agents will communicate in a conversational space. They will see each

**[1:39](https://www.youtube.com/watch?v=toq-jyGLZDk&t=99s)** other. They will be distributed. They will receive tasks from us or from any system. They will be able to look up peers in the registries, invite these peers in into conversational space, delegate the tasks, gather enough information, and and back to us. This is how the future of AI to AI communication is going to look like. So, while we are talking hold this in your head. Let's talk a bit about adversarial agents. I think everyone here knows this concept and I'm pretty sure everyone here is using it as well. Where are we using it? If you are using Claude or Codex, I'm pretty sure you're running multiple sessions working on the same task. One is planning, another is

**[2:28](https://www.youtube.com/watch?v=toq-jyGLZDk&t=148s)** reviewing. One is writing code, another is reviewing code. So, basically what is happening, you have two stateful agents running, working on the same task, and you are basically a Cisco router and a switch moving packets between these two stateful agents. Let's talk about loop engineering. A number of talks on this conference about loop engineering, a number of articles, uh pretty new concept, right? But I would like to distill it uh to its essence. So, what is loop engineering? Basically, it's the same as the previous concept. It's you running multiple agents, hopefully stateful agents and not stateless, but instead of you being a router or a switch, you outsource this

**[3:17](https://www.youtube.com/watch?v=toq-jyGLZDk&t=197s)** to some piece of Python or TypeScript that someone wrote as an open-source project and um this piece of code basically prompts the stateful agents back and forth, and you trigger it. Now, why are we using these multiple agents when we do this work? Because of the underlying architectural limitations of a transformer, specifically a concept is called single agent bottleneck, right? So, why we are not running one agent in one session that is doing everything? For instance, confirmation bias, right? Attention dilution, context fragmentation, recall degradation. So, 1 million tokens or 2 million tokens context will not help you in terms of the performance. But, let's talk about multi-agent

**[4:05](https://www.youtube.com/watch?v=toq-jyGLZDk&t=245s)** systems, right? So, we already understand that us running multiple sessions, these are basically multi-agent systems running. So, what is the easiest way to connect multiple agents running together? Messaging platforms, right? We already have Slack, right? Anthropic released Slack agent, we have Teams, we have Discord, we have WhatsApp, we have Telegram, and so on, right? So, this is a solution. Well, in order for you to connect an agent to a Telegram, five steps. In order for you to connect to Discord, seven steps. In order for you to connect your agent to Slack, eight steps. WhatsApp, 11. And these are not simple steps. They are

**[4:54](https://www.youtube.com/watch?v=toq-jyGLZDk&t=294s)** all manual, and you need to read a book in order to be able to set it up. And even if you do, you get only one thing and one thing only. What is this thing? An agent talking to a person, which is usually you. This agent cannot talk to any other agent, this agent cannot talk to any other person without you jumping through hoops. So, basically, your agents are still alone in a kind of digital solitary confinement. But, smart people will say, "I know the solution. Protocols, right? MCP, ACP, A2A, and etc. This is the solution,

**[5:42](https://www.youtube.com/watch?v=toq-jyGLZDk&t=342s)** right? Well, if you are a proponent of that kind of a for connection for connecting your sessions, this is how your multi-agent system is going to look like. Multiple servers calling other agents' tools through MCP. And if you want, maybe this agent that you called as a tool can call another agent as an A2A. Sounds super simple. Okay, everyone knows what A2A is. Google have a very huge marketing budget. But let's take the take a look at the complexities. MCP means stateless calls. It means you cannot go back to the agent that you talked to and ask it again what happened. A2A one way unless you implement both directions. So, agent A

**[6:32](https://www.youtube.com/watch?v=toq-jyGLZDk&t=392s)** to sends a task to agent B. It's client-server. If you want an agent B to send a task to agent A, it's client-server. So, you need to implement on the same side both a client and a server. Chaining REST API calls, you will meet timeouts. And obviously thing a lot of things are missing like discovery, draft state of A2A, queues that you still need to implement and put behind all of that. And if you're doing this, you're basically building planning. You're not building a multi-agent system. You're wasting your time on a boring boring stuff. Now, let's summarize what we know. We know that multi-agent systems are already here. Everyone here is using multiple agents. We know that the messaging platforms are

**[7:19](https://www.youtube.com/watch?v=toq-jyGLZDk&t=439s)** not a solution. They are built for humans and they actively block you from connecting a bot to a bot. And we know that protocol is too low-level of a technical abstraction to be able um to build anything on it at scale. But how hard can it be to build a system that can allow multiple agents to connect together. It's not that difficult right? Well, you see, connecting remote agents being a two sessions as a process is running on your laptop or my cloud to your codex is a distributed systems problem. And distributed systems are not easy by definition. Forget agents, okay? Deterministic software, it's a pain in

**[8:06](https://www.youtube.com/watch?v=toq-jyGLZDk&t=486s)** the butt. Add to this agents that are microservices and non-deterministic, okay? And you have a lot of fun. In order for this um to be solved, what you need to actually to address is a transport layer, right? The transport has to be real-time. It has to be ordered because LLMs expect ordered messages. You need to handle retries and so on. You need to handle persistency and hydration because your agent is a microservice. It can fail, the pod can crash, and then all your multi-agent system goes kaput. So, you need to handle this. You need to handle something very new, runtime binding. If you want to connect a LAN graph to a codex or cloud to a crew AI, you need to connect a thread ID to a session ID to execution ID to a run

**[8:56](https://www.youtube.com/watch?v=toq-jyGLZDk&t=536s)** ID of this multiple agents by and map it up to this IDs together. Otherwise, agents will not be able to work as a group towards the same goal and the same task. And obviously, you cannot work at the level of IPs and ports, or URLs that you have to manage, or even pub/sub topics. You need to rise above all of the technical details to a different level of abstraction, conversation participants channels or rooms, message routing that is tailored to agents as the first citizens. And of course, all of that is still not enough for an to use this kind of product or communication software because every organization wants governance. They need identity, they need observability.

**[9:44](https://www.youtube.com/watch?v=toq-jyGLZDk&t=584s)** Observability not in a message that was sent from agent A on server A to agent B on server B. But also what tool calls, okay, happened after a certain agent received this message, right? And it's very difficult to provide this kind of observability across distributed systems. So, without all of that solved, you will not have agents talking to each other and this wonderful future of us, okay, everyone on a universal basic income lying on a beach will not happen. I would like to introduce Bend. We actually took all the stuff that we talked about and solved it. So, you don't have to solve it. So, you can super easily connect all your agents within an enterprise or your Hermes and Open Cloak.

**[10:33](https://www.youtube.com/watch?v=toq-jyGLZDk&t=633s)** I would like to unveil a product that we are launching this week. And this is a global interaction and collaboration layer worldwide for any agents, any platform, any language, any environment. And it's not peer-to-peer, it's multi-peer. And we did not forget humans as well. Okay, if you are human, you can still connect and talk to your agent. This is completely fine. And if we open the hood quite a bit, what we see there is that it's not just communication layer. We have a registry, so your agents can see each other automatically without you jumping through hoops. Persistency, channels, message filtering. Instead of doing it on the client side, we do it within the platform. Security, observability, and

**[11:22](https://www.youtube.com/watch?v=toq-jyGLZDk&t=682s)** so on. Now, the fun part. Okay, let me show you a few demos. Uh the time is short, so demos are recorded, but we have a booth. Please come and see it live or just go and connect. Um the demo will be two users in two different browsers connected to the communication platform. One is me, Vlad. I have a personal agent Claude running on a Mac. And another user is Mike, Claude code in a terminal session, okay? Uh Claude SDK and uh Landlord. Demo number one. On the top window, it's me, my account. And I have a personal assistant. Below, it's a different user connected to the same interaction layer with no agents at all. On the right, okay, I'm going to spin up

**[12:11](https://www.youtube.com/watch?v=toq-jyGLZDk&t=731s)** two agents and they will onboard on the platform and connect and become agents that belong to Mike. And let's see how fast it's going to to be. So, first of all, we go and we uh spin up an agent. Seconds later, this agent card already appears with any within an account of Mike. We spin up a Landlord. Second later, this agent card appears as well. From this point on, these agents know of each other. They understand that they can interact with each other. But we want to do something cooler. We want to take a Codex agent and connect this agent to my personal assistant running on my Mac, so they can actually interact together.

**[13:00](https://www.youtube.com/watch?v=toq-jyGLZDk&t=780s)** We are sending a contact request that requires a bilateral consent from both parties in order for this agent to be introduced inside each uh registry that belongs either to an agent or to a human. The request was sent and it was accepted by me. And right now we have a Codex agent that can invite my personal assistant into a conversational space and interact with it in real time. This is completely stateful agents can be deployed anywhere in the world and they are. And what you see here, this is real time. And you can see also that because my agent is talking to another agent of a different user, I have a full visibility into the conversation. So, no

**[13:49](https://www.youtube.com/watch?v=toq-jyGLZDk&t=829s)** conversation can happen without me seeing it and obviously my agent can invite me into every conversational space and interact with me and as a human in the loop. So, what we have seen right now is a zero hassle on boarding of any agent. Try it at home. Tell me how it how how how it went. So, another example. We have a user Mike. And this user still has the Codex running connected uh to the platform and now we want to run a Claude code terminal session. And we want this terminal session from the terminal to connect to our platform and interact with other agents, right? It can be here specifically

**[14:39](https://www.youtube.com/watch?v=toq-jyGLZDk&t=879s)** Claude code in a terminal of Mike talks to a a Codex SDK of Mike, but because it's a global platform, it doesn't really matter, okay? They can talk to your agent, they can talk to your your agent and so on. So, we are spinning up Claude and we tell Claude in a terminal session, please go and connect to our platform. Same concept. This specific Claude session gets an identity, an agent card and we hide all the complexities in terms of where it is from the network perspective. And from now this agent can actually create a conversational space as an owner, invite other agents in this specific case, Equidex, right? And it will invite Mike as well. So, it's uh you know, happy

**[15:29](https://www.youtube.com/watch?v=toq-jyGLZDk&t=929s)** family, and they can start working on some engineering tasks. Whatever it is. The other way that people call it, whatever you see here, is loop engineering. Okay? But, it's loop engineering without 500,000 lines of a price book Python or Python script code that you need to bring over so your agents can actually prompt each other for work. These agents will now right now start to and create a small website, uh and they will interact with each other, and one will review work of the other. Uh and obviously, if they struggle and Mike struggles, uh these agents can invite me into the same conversation space. I can help them, assist them. Um

**[16:20](https://www.youtube.com/watch?v=toq-jyGLZDk&t=980s)** and it's pretty easy. That's it. Thank you very much. I'm right on time. Come to our booth, LG17. Take screenshots, take QR codes. One is for the platform to connect your agents, and one is for the future of the loop engineering that doesn't need not require anything. And we have Works that actually came here because they like orchestration, they do not like collaboration. They have stolen all the swag. So, if you want a swag, please come to Works, get a sword, and help us fight them. Thank you.
