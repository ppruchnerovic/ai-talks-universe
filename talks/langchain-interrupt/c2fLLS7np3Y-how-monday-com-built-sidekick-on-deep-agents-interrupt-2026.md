---
id: c2fLLS7np3Y
title: "How Monday.com Built Sidekick on Deep Agents | Interrupt 2026"
slug: how-monday-com-built-sidekick-on-deep-agents-interrupt-2026
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 16
published_at: 2026-06-26T12:53:17Z
video_id: c2fLLS7np3Y
youtube_url: https://www.youtube.com/watch?v=c2fLLS7np3Y
tags: ["monday.com", "Sidekick AI", "Deep Agents", "LangChain", "AI agents", "agentic systems", "multi-agent architecture", "tool discovery", "deferred tools", "context pollution", "LangSmith sandbox", "self-healing agents", "production AI", "AI assistant", "Interrupt conference", "Omri Bruchim", "sub-agents", "middleware", "code-writing agent", "LLM hallucination", "agent recovery", "progressive disclosure", "ReAct loop", "AI work platform"]
transcript: true
---

# How Monday.com Built Sidekick on Deep Agents | Interrupt 2026

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `16 min`

`#monday.com` `#Sidekick AI` `#Deep Agents` `#LangChain` `#AI agents` `#agentic systems` `#multi-agent architecture` `#tool discovery` `#deferred tools` `#context pollution` `#LangSmith sandbox` `#self-healing agents` `#production AI` `#AI assistant` `#Interrupt conference` `#Omri Bruchim` `#sub-agents` `#middleware` `#code-writing agent` `#LLM hallucination` `#agent recovery` `#progressive disclosure` `#ReAct loop` `#AI work platform`

[Watch the recording](https://www.youtube.com/watch?v=c2fLLS7np3Y) · [Conference site](https://interrupt.langchain.com/)

## Description

Omri Bruchim, engineering manager at monday.com, walks through the full journey of building Sidekick — monday.com's intelligent personal assistant — from a simple LangChain React loop all the way to a production-grade agentic system powered by Deep Agents. He covers the real scaling failures that forced a rebuild, and the four engineering principles that got them to a 94% error recovery rate in production.

Chapters:
0:00 Introduction and what we're covering today
0:31 About Omri and the monday.com AI platform
1:25 monday.com's mission shift: from managing work to doing the work
2:02 The SDR agent and job recruiter agent demos
2:22 The monday.com product suite: Monday Agent, AI Apps, and Sidekick
2:39 What Sidekick actually does
3:06 Sidekick V1: the LangChain ReAct loop that started it all
3:54 Why V1 broke: 200 tools, infinite context, context pollution
4:37 Why they chose Deep Agents to rebuild from scratch
6:55 Core philosophy: one smart orchestrator, not a swarm
7:41 The four principles — overview
7:44 Principle 1: Deferred tool discovery (the three-tier system)
9:55 Principle 2: Delegation first — sub-agents and async handoff
11:03 Delegation first — the middleware pipeline
12:04 Principle 3: The code-writing tool and LangSmith sandbox
13:04 Real-world example: finding a London office with live code
13:42 Principle 4: Self-healing with 94% recovery success rate
15:07 What's next for Sidekick
15:26 Takeaways for building with Deep Agents

Resources:
→ Deep Agents: https://www.langchain.com/deep-agents
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com
→ monday.com AI platform: https://monday.com/ai

## Transcript

*2,736 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=6s)** Hey everyone. I'm super super excited to be here. Um, today we're going to talk about psychic or AI agent and monday.com. I'm going to show you the journey that we made from day one until today where you need deep agent with a practical example how to use the deep agent not like just theory. Before we jump in, um, a little about about myself. I'm Omri, I'm a team manager at monday.com. I'm originally from Tel Aviv in Israel. Um, for the past few years I've been mostly around the AI infra, building AI based product meaningfully basically to make our work much easier. Um, This is my family by the way. Uh, we're a big family of six. I have my wife, I have three kids, um, and we have one agent if you if you notice. Uh, this is Mila.

**[0:55](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=55s)** Uh, she's practically part of the family. I recommend each one of you to have one of it in my home in in your home. Um, she based off a Nimo-claw. Uh, she helped us with the home assignment. My kids talk with her. And if you notice you have like six fingers. Um, my my kids really love it because she's different from us. Um, For those who might don't know us, monday.com is a the AI work platform. We help teams to scale their businesses. Um, we build product that people really love to use. Um, in the past year and as actually in the past week we make a huge shift in our mission and and instead of like just helping company to manage their work with the boards, we want actually to doing the work. And why not like doing

**[1:43](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=103s)** the work for you? Um, and it's true for all the business functions. Whether you are sales person, so before we help you to find leads um, and maybe put you on the board with the with the contact details. And today we have an SDR agent that make a phone call to the prospect and sell the product. And if you are a job recruiter, um you should never open LinkedIn again because our agent can do it and send email to it to to the candidate. Um and for that we built a suite of uh new product. Uh Monday agent, for example, that you can build any agent that you you can dream of. Uh he can he has its own personality. It has its own its own permission. Um we have Monday vibe if you want to build an app on top of monday.com so you can do so.

**[2:32](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=152s)** And we have Sidekick. And Sidekick is your intelligence AI personal assistant. Let's drill into the Sidekick. So what is Sidekick? Sidekick um he know you more than everyone. He is the one step ahead of you. Um he understand your world, your contacts, your goals, your active work, what you're working on. It can accelerate your work. Um he do the work for you. Um he learn he learn from your meetings. He know all the meetings that you've been for. Uh he know who are you working with and you basically can trust him. But um we have a long way with Sidekick. So I want to take you to the journey back to the past really long long long time ago. It was crazy to think that it was just a year ago. On this stage, my partner Asaf is here in the crowd. Um he talked about

**[3:22](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=202s)** version one of Sidekick. Um V1 wasn't great, to be honest. Um but it was just the beginning. Um it were our first take of doing the work, um bringing reactive AI uh to the work space of Monday. Uh it was built on simple react loop. Uh we launched it, of course. Uh he has a few tools. Uh it it indeed did work. But um with the with with uh moving forward uh with the big success and uh we had a more appetite and and we we had a scale issues. A bit about Monday before we move into 2.0. At Monday we have a multiple product division. We have Monday CRM, we have a Monday service, Monday marketing. Each one of them had different needs. They [snorts] have a

**[4:09](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=249s)** different context. They have a different terminology. Um and beside that, we have multiple entities. So we have docs, we have boards. Um and each one of them has different contexts. When you open in a board on Monday dev, it's totally different tools and contexts from opening a doc on Monday CRM. So we have set of huge set of tools. Um so fast forward to Sidekick V2, we wanted to do everything. We want to have like all the tools. Um but here was the engineering challenge. Uh we built Sidekick from scratch out there, kind of multi-agent architecture. You can see that each one of the domain had its own MCP with its tool. Each MCP can expose a specific tools for the context. You have

**[5:00](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=300s)** specific prompt. I mean, Sidekick Sidekick was a dynamic prompting and then we can inject the context. Um each domain had its own tools. But at the end, it pretty exploded in our face. Obviously, it was like a super promising, but at the end it didn't work. It didn't work because we have like huge challenges. We had one engine with more than 200 tools, infinite contexts, like the context pollution we had the context pollution. Um the LLM was confused. The cost rise up. Um We have too many tools, too many contexts. Um and each one of the domain had different needs. And we took a decision. We realized that the whole harness isn't good enough. Uh we need something entirely new Uh

**[5:50](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=350s)** and welcome deep agent. This is the practical example I want to show you how we use deep agent. We built psychic from the backbone. We needed something that is robust, not messy, multi-steps, not just a chat interface, something that's really doing the work. So we chose deep agent. We made a research and we found out that deep agent has the flexibility that we need exactly and basically the principle that we aim for. Some of them are like it built for real work, not just for the chat. It can have a multi-step workflow to use the iteration planning, something that we can use in our day-to-day and he has better separation of concerns. You heard about it, sub agent and and other tools that stay focused on what

**[6:39](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=399s)** you need to do and and memory stay contextual and not like blowing. And of course the file system style, it support deep contact. This is something that super critical for us and this is why we chose deep agent. So again, it's like our philosophy with psychic was simple and it was like best match. We want to have like one smart orchestrator instead of like chaotic swarm of hundreds different special agent, each one talking with each other. It's like chaos and we want to have like highly one capable brain. The second one is like we trust the model. I mean the models are really smart today. So we handle all the hard stuff to the model, the planning, the managing of memory and spending spending special sub

**[7:29](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=449s)** agent and and exactly the one of the greatest point that we build it for progressive disclosure. This is one of the problem that we had like too many tools, too many contacts. And today I'm going to talk about four principles that we adopted. Let's start from the first one, that three-tier discovery. Um, you heard about it before a bit when you heard about talk about like deep agent, but this is a practically how we implement it. So, remember that we have the problem with 200 tools prompt pollution problem. This is the solution. We fix it with three-tier uh classification system. Tier number one is like um the base, the tools that uh list of tools, a small one that always exposed to the model. Uh, you can imagine that this is like the tools that 50-60% of the use cases you're going to use them.

**[8:18](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=498s)** Okay, this is like web search, image generation, uh web URL extract, the knowledge base search in all all Monday. This is like the most common one. The second one is the context. You remember that we have like different entities, different screen, different domain. So, in this tier we push the tools that relevant to the specific entity that you are looking at. So, if you are in CRM and you are in doc, we exposing you just those tools and not all the rest. And this way we reduce the context pollution. So, you have like get board activity and note taking meeting if you are looking at note taking screen. Well, so this is how we reduce the tools. And the best part is like the deferred tools. This is like the third part. How it works? Here we have like a catalog of all the tool all the rest of the tools

**[9:06](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=546s)** with like a small description like 20 words description. Um, the agent can call a deferred tool activate it, it's another tool. If you want to use one of the tools and then he got into the context and he can use it. Uh, all of it been in real time uh and it reduce all the hallucination. Um, by the way, the next step of it is like we can push all these tool description into the semantic database um and and search for specific tool in a semantic way and not just going over all day long MD5. So, this is one of the tools in This is how it look in real time on lunch menu. When an agent understand a specific need, he like search for it and then call the activated and then he can use it like create item tool.

**[9:55](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=595s)** For the next part, delegation first. So, this is one of the important principle. It's split into two. One is the sub agent. Sub agent are obviously special work for every common repetitive task. We have few of them. We have like the presentation builder, the web web researcher. And here you come into the place that two different ways to execute sub agent. You can hand off something to another agent and do it like asking quality. So, you can continue with your work and when it's ready, he come back. So, this is something that's crucial for our work on psychic because at the end you're working with something on something and you want to continue the work and do something in on parallel. This is how it look in in in practice, enough theory. Here a quick demo of our sub agent. It's actually build a

**[10:43](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=643s)** presentation for a question I ask him. I simply tell him to tell me about himself. This is psychic. And he created a presentation out of the box. Here we using sandbox. I'm going to talk about it in a minute. But like this is special agent that know how to build presentation which is awesome. Um The second part of like delegation first is the middleware. To make the delegation seamless, we in in psychic we really heavily depend on the middleware pipeline. It's separate concern beautifully. It's testable. It's composable. It's keep the execution graph clean. This is why we put it in a different layer. Here is some example. We have like the context manager. The context manager inject like user identity, uh placement,

**[11:33](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=693s)** time zone, uh connected MCP, something that is specifically for the user. We have the repeating name middleware. We find out that sometimes the LM full confidence with themselves, so he invent tool names. Uh so, we have like middleware that repair this tools names and fix uh if it's not exist, so he put it uh in in place. Um another example is like the model selection. Uh we have a middleware that we let the user to choose the model that you want to run Sidekick, and in real time we change the model. Um for the third part, and this is one one one of the most exciting one, is we have the tool that writing code. Um This is like um as we scaled, we realized that building specific new tool for every possible way for every

**[12:21](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=741s)** possible use case is not making any sense. Um instead of searching for a a sum or filter tool, uh we allow the agent to write Python code uh and just run it in inside a sandbox uh um inside a sandbox. Um for running the sandbox, we are using LangChain sandbox. It's help us to do it like super seamless uh with secure environment. And it's really become like it it's eliminated the bloat. Uh one secure sandbox, it can replace hundreds of tools. You can imagine whatever you can think of. Um We have a few example. I mean, when we push it to production, we saw really creative things that the our users uh they when the user doing it with it, it's blow our mind. Here is one example. Uh so, this is a example of someone that's want to find a a new office uh

**[13:09](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=789s)** for his company in London. Um He want don't don't want to wait more than 20 minutes, uh drive from the Big Ben at specific hour. Um so, Sidekick um use Google API and open maps. It created like algorithm to define the relevant offices around the place and none of it can be happening without writing code. So, this is one of the craziest thing that Sidekick can do right now instead of just it's just building an app. So, this is crazy. For the first for the last principle, so Sidekick know how to heal himself, which is pretty crazy. So, LLM again is like super confident with him with themselves and they hallucinate a lot. Um

**[13:55](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=835s)** Um but and instead of like failing in production, we learn we we started like how to self-correct himself. With the design deviation with like a healing middleware, we going to see a few example of it. So, we have this variable advisory tool. Sometimes Sidekick don't know how to do something, so he going come back one way to the other to fight to try to do something and at the end like we have the some middleware that identify that he can't do something and like move it to different model. We have the resource scaling. Sometimes we get an error that we have we have out of memory and you get the error from the LLM from the from the harness and we try to like

**[14:42](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=882s)** scale up the resources and we have like the number we try is pretty easy pretty straightforward but it's like solve tons of problem. Uh At the end like we have like 94% recovery success rate which is pretty amazing. I mean, we implement healing reflection across all the researchers. Um Real world enterprise workflow shouldn't fail too much. Um This is like generally speaking the next architecture of Sidekick. It's it's not for you. It's like for next year that someone else going to be on the stage and show something else. So, we going to be creative about how we how rich how long we how how long we made the journey. Um I got few just to wrap up. If you're building an agent system with

**[15:30](https://www.youtube.com/watch?v=c2fLLS7np3Y&t=930s)** D Page and this is my takeaway, use the writing code tool. It's super super cool. It's like working as a charm. Could call this ultimate is like infinite scale tool. Um prefer delegation. You can't put everything on one single agent. Use tool discovery. I saw a lot of use cases where you have like long list of tools. So instead of like push it all in one agent like the orchestrator, separate them and use middleware. It has like super clean separation of concern and just use D Page and thank you. >> [applause] [music]
