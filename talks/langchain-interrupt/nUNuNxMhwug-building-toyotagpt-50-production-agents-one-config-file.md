---
id: nUNuNxMhwug
title: "Building ToyotaGPT: 50+ Production Agents, One Config File, Zero Architecture Reviews"
slug: building-toyotagpt-50-production-agents-one-config-file
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 17
published_at: 2026-07-15T13:04:17Z
video_id: nUNuNxMhwug
youtube_url: https://www.youtube.com/watch?v=nUNuNxMhwug
tags: ["Toyota", "ToyotaGPT", "LangGraph", "LangSmith", "LangChain", "AI agents", "enterprise AI", "Toyota Production System", "TPS", "Kaizen", "Jidoka", "Andon board", "Genchi Gembutsu", "agent platform", "RAG", "production agents", "Kordel France", "Ravi Chandu Ummadisetti", "agentic AI", "multi-agent systems", "AI for manufacturing", "GearPull", "MCP", "skills engine", "Interrupt conference"]
transcript: true
---

# Building ToyotaGPT: 50+ Production Agents, One Config File, Zero Architecture Reviews

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `17 min`

`#Toyota` `#ToyotaGPT` `#LangGraph` `#LangSmith` `#LangChain` `#AI agents` `#enterprise AI` `#Toyota Production System` `#TPS` `#Kaizen` `#Jidoka` `#Andon board` `#Genchi Gembutsu` `#agent platform` `#RAG` `#production agents` `#Kordel France` `#Ravi Chandu Ummadisetti` `#agentic AI` `#multi-agent systems` `#AI for manufacturing` `#GearPull` `#MCP` `#skills engine` `#Interrupt conference`

[Watch the recording](https://www.youtube.com/watch?v=nUNuNxMhwug) · [Conference site](https://interrupt.langchain.com/)

## Description

Ravi Chandu Ummadisetti and Kordel France from Toyota's enterprise AI team explain how they built ToyotaGPT — a platform that reduced agent delivery from six months and six engineers to four days and one engineer, with over 50 agents now in production. Ravi walks through the architecture: dynamic LangGraph-based graph generation, auto-synthesized skills from unstructured data, and an MCP-compatible tool layer secured by TMNA's cybersecurity team from day one. Kordel then draws a striking parallel between TPS — Toyota's 100-year-old manufacturing philosophy — and LangChain's ecosystem, mapping Andon boards to LangSmith, Jidoka to LangGraph, and Genchi Gembutsu to trace-level debugging.

Chapters:
0:00 Introduction and the 2023 AI chaos inside Toyota
1:40 Why one RAG app used to take 6 engineers and 6 months
2:09 Dynamic graph creation on LangGraph: 6 months becomes 4 days
2:47 The extraction problem: Toyota's brutal data reality
3:38 The ToyotaGPT stack: LangGraph, LangSmith, MCP, and TMNA security
4:18 Skills: units of intelligence generated from unstructured data
5:06 50+ agents in production — every one is a config file
5:39 GearPull: from hackathon idea to millions in manufacturing savings
6:37 R&D GPT: compressing years of paint research into seconds
7:25 KadyaGPT: AI embedded inside the designer's canvas
8:58 Kordel France: TPS meets LangChain
10:14 Andon board = LangSmith observability
11:47 Kaizen = continuous improvement at macro and micro scale
13:04 Jidoka = LangGraph's human-in-the-loop design
14:11 Genchi Gembutsu = LangSmith trace-level debugging
15:21 LangChain as the TPS for the AI era

Resources:
→ LangGraph: https://www.langchain.com/langgraph
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com

## Transcript

*2,344 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=nUNuNxMhwug&t=5s)** >> Hi, everyone. I'm the head of Agent AI and product research at Toyota. I have Kordel joining, who is the head of AI engineering. In 2023, when Generative AI changed the world, inside Toyota, 65,000 people, multiple factories, and one question that we had was: what do we do with this? We are the enterprise AI team. Every AI use case that's going to production comes to our team. So one standard, one platform, no chaos, no duplication. The problem is nothing existing before that could be what we wanted to do. So we opened up a blank repository in our GitHub and built it ourselves. So this is the story I'm going to talk about today. I'll show you how we built ToyotaGPT, a platform that ships AI agents in very few days, then Kordel talks about how it connects with the Toyota Production System and how

**[1:02](https://www.youtube.com/watch?v=nUNuNxMhwug&t=62s)** LangChain, LangGraph, and LangSmith are really useful in our ecosystem today. That part really surprised us. Let's go. So in 2023, every team at Toyota was rushing to build their own chatbot. Same ingestion, same extraction, same pipeline — multiple duplicate things were coming up. No security standards, no architecture standards, pure duplication at an enterprise scale. Our job was to stop that. To be the platform every AI agent is built on. The pressure was real, the timeline was yesterday. So what did we need to do? We needed to go to work. One RAG app at Toyota used to mean six engineers and six months in the early days — not because AI was hard,

**[1:50](https://www.youtube.com/watch?v=nUNuNxMhwug&t=110s)** but because everything around it is hard. Security reviews, architecture sign-offs, and ingestion plumbing across multiple data sources, rebuilt from scratch. Our delivery was stuck in months, so that gap we decided to close permanently. In four days, we built a dynamic graph creation approach on LangGraph: give it the use case, give it the data connectors, and the entire graph builds itself automatically. ReAct agents, deep agents — everything plugged in. No security review, no architecture review. It's all reviewed at once, because the architecture never changes, the security never changes. The only difference between every AI agent we build is just a config file.

**[2:39](https://www.youtube.com/watch?v=nUNuNxMhwug&t=159s)** So six months became four days, six engineers became one. That is not an optimization. That's a different way of building. The thing that kills every AI agent before it even starts is the extraction. Bad text in, bad text out. Our data at Toyota is brutal. PDFs, Word docs, Excel files, CAD files, AutoCAD. You name it, we have it. Scanned manuals from the '90s. Toyota tables inside tables inside tables inside tables inside images. We have complex data sources at Toyota because we have Japanese, we have English, we have a lot of different languages. Name the format, we built an extractor for it. Layout-aware parsing and OCR with vision.

**[3:30](https://www.youtube.com/watch?v=nUNuNxMhwug&t=210s)** Schema mapping, every source, one unified index. And we built it ourselves, cutting enterprise license costs. LangGraph at the core — thanks to Harrison Chase for building the great framework. LangSmith for observability, vector databases, SharePoint, and the TMNA cybersecurity team, baked in from day one, working with us. Every agent inherits this and is exposed via API. ToyotaGPT web, internal apps, factory machines, robotics — which uses LangGraph in the background — vision-language-action models, everything runs on top of this framework. The pipeline is LangGraph end-to-end, routing dynamically by source type.

**[4:18](https://www.youtube.com/watch?v=nUNuNxMhwug&t=258s)** But the concept I want you to take home is skills. A skill is a unit of intelligence. We do two things nobody else does at scale. One: enterprise-grade skills shared across every agent. One library, no drift, no duplication. And two: we generate skills automatically from unstructured data. We have terabytes of data sitting in our databases. Feed these documents into the pipeline, skills emerge without a single engineer writing them by hand. And on top, a unified tool layer — MCP compatible. Every tool secured for any AI agent. You want it? It's there. Is it secure?

**[5:05](https://www.youtube.com/watch?v=nUNuNxMhwug&t=305s)** Already done. Today, over 50-plus agents are in production, every single one built on ToyotaGPT. Every one is a config file. From GearPull on the plant floor, to Gura, the long-term memory of the entire enterprise — the Toyota Way, Toyota's culture and principles codified into an agent — and two vehicle AI experts that know every Toyota model, every spec, every history, all queryable in seconds. Let me walk you through a few to show you what this platform actually makes possible. GearPull started as a hackathon idea. One of our team members, Braden Buffard, had a vision. What if every manufacturing engineer could just type the problem and get the answer instantly? Today, GearPull sits on terabytes of data

**[5:57](https://www.youtube.com/watch?v=nUNuNxMhwug&t=357s)** in our vector databases, serving every manufacturing plant across North America. Here's the reality it replaced. When a production line goes down, an engineer walks to a bookshelf and pulls a manual, flips through the pages, manually searching for information, and fixes the problem. That takes hours and sometimes days. But if a production line stops for a few hours, we lose millions of dollars because we're not making cars. Today: type the problem, get the solution in 10 seconds. From hackathon idea to millions of dollars in savings. That's GearPull. R&D GPT. This is close to my heart. Every color you see on a Toyota on the road, we created that from scratch.

**[6:46](https://www.youtube.com/watch?v=nUNuNxMhwug&t=406s)** We created the paint from scratch. Years of R&D testing in extreme cold, extreme heat, to make sure the quality doesn't degrade. A year, sometimes two, sometimes two to four years. Today, R&D GPT learns from decades of our own past research. Deep research is really helping us solve that. Now, techniques emerging from old technology, old knowledge — what used to take multiple years, now compressed because our own institutional knowledge is now searchable, connectable, and queryable within seconds. And then KadyaGPT, the design agent that lives inside the tool designer. Already using new car designs, existing parts, existing designs,

**[7:35](https://www.youtube.com/watch?v=nUNuNxMhwug&t=455s)** it can query best practices, find differences, identify patterns without ever leaving their canvas. Zero context switching — the AI is just there in the workflow, exactly where it needs to be. When we started our journey with Harrison, nothing existed. We built the entire ingestion formatted from scratch, from PDF files. The LangChain ecosystem came to life and then we built the framework using LangChain, LangGraph, and deep agents. Dynamic graphs automatically populating. We built the skills engine — intelligence that generates itself. We built the tool layer: MCP-ready, enterprise-secured. We took a hackathon idea and turned it into terabytes of production. 50 agents, millions of dollars in savings.

**[8:25](https://www.youtube.com/watch?v=nUNuNxMhwug&t=505s)** Built from zero, from scratch. We learned every single thing as we went. We didn't wait for the industry to catch up. We went ahead and built it. Now, Kordel is going to show us something that genuinely surprised us about everything we built. Toyota invented the philosophy behind it, I think, on the factory floor in 1988. Kordel, it's yours. Thanks Ravi. [APPLAUSE] Toyota is arguably the best automotive manufacturer in the world, and by extension, one of the largest and best hardware manufacturers. And it got there through something called the Toyota Production System. The Toyota Production System, or TPS,

**[9:12](https://www.youtube.com/watch?v=nUNuNxMhwug&t=552s)** is a philosophy, a framework, for building a lot of anything, really, really quickly and with really minimal resources. So by extension, it's a philosophy on how we can build vehicles on a manufacturing line very leanly, with minimal staffing, minimal resources — make a manufacturing line modular, make it robust, so that it's amenable to breakdowns and keep continuous flow from raw materials all the way to when a car comes out at the other end of the manufacturing line. The principles of TPS are really the backbone for any scaled hardware manufacturing line that we see today. It started with Toyota. It's been fashioned over the course of almost 100 years, but really became formalized in the '80s — as Ravi mentioned — in order to help Japan,

**[10:03](https://www.youtube.com/watch?v=nUNuNxMhwug&t=603s)** who had far fewer resources than North America, compete on the North American automotive front. TPS is the backbone for all hardware manufacturing today. And we see a very similar parallel between TPS and LangChain. LangChain is the modern backbone on which all next-generation software and agent workflows will be manufactured. The principles from hardware manufacturing translate really well into agent manufacturing. It's just a matter of the substrate — the matter that we're manufacturing. And so this has been a really pleasing and quite awesome experience not only to use LangChain's products but to become more embedded in their ecosystem, because they embody the ethos from which Toyota was founded and all of the principles that our team shares and works with every day.

**[10:56](https://www.youtube.com/watch?v=nUNuNxMhwug&t=656s)** So a couple of TPS principles that are pretty easy to identify with LangChain — starting with the Andon board. The Andon board in manufacturing is a way to see what's going on really quickly without having to survey the whole manufacturing floor. What's broken down? What needs supplies? What's going well? You allocate resources to bolster another part of the manufacturing line that's dwindling. And LangSmith is the literal embodiment of an Andon board. We can see observability over all of our agents in real time. Understand what tool calls aren't working, what features we should focus on for the next PR, for the next product release, and what's going well with our users. What are the frustration points? How do we better serve our users and improve our software? LangSmith is the direct analog of the Andon board.

**[11:47](https://www.youtube.com/watch?v=nUNuNxMhwug&t=707s)** One term you all are probably familiar with is Kaizen, which is continuous improvement through slow and steady, but consistent modifications. And software engineering culture really embodies that. We're always pushing PRs, we're always bolstering new products, and we push updates regularly — sometimes nightly. The great thing about Kaizen is that from the LangSmith perspective, or LangChain perspective, there's really a macro level at which Kaizen is being implemented and a micro level. At the macro level, the software is always improving. Harrison just announced a bunch of new features today that are going to be a huge advantage to the ecosystem — already published. And then at the micro level, there are agents that are continuously improving. A very rudimentary example might be the ReAct agent —

**[12:40](https://www.youtube.com/watch?v=nUNuNxMhwug&t=760s)** something that's always monitoring its output and continuously improving it to make sure that before it presents the final response to the user, it's actually correct and does what the user intended. So this philosophy of continuous improvement through steady and consistent changes is something we embody at Toyota and are delighted to see with LangChain throughout the whole ecosystem. My personal favorite is the principle of Jidoka. Translated literally, it means automation with a human touch. And what LangGraph does really well is it automates a lot, or abstracts a lot of the nuance and monotony that, as an engineer, I don't want to have to deal with or don't care to deal with. But it keeps me in the loop. It keeps me plugged in so that I still have the values of a human and can still guide the product

**[13:30](https://www.youtube.com/watch?v=nUNuNxMhwug&t=810s)** as it's being developed and deployed. And Jidoka is really like a handshake deal between AI, automation, and a human — to say: I understand each role that you play, and I understand we're going to have to adapt as technology progresses. On the manufacturing line, Jidoka means that a human understands we need automation in order to manufacture things very leanly and very efficiently. But as technology evolves, a human's role will change, because that automation will change. But a human is still critical to ensuring high quality of products and delivery to the final customer. So, yeah, LangGraph is a literal embodiment of the Jidoka principle, which we love. The next term is Genchi Gembutsu. This means to literally go to the source and understand what's going on. Try to find the root cause of the problem.

**[14:21](https://www.youtube.com/watch?v=nUNuNxMhwug&t=861s)** We can't figure things out on a Teams call. If there's a manufacturing issue in Texas, we can't sit in California and try to figure out what's going on. The best way to solve the problem is to go to the manufacturing line, actually touch the hardware, understand the root cause of the problem, and then proliferate the solution throughout the rest of the manufacturing line so that we Kaizen the remedy. LangSmith traces are a direct embodiment of Genchi Gembutsu. For every query, every tool call, I can see the entire trace, the entire route to the solution. And if there's an issue, I can see exactly what caused it. And so it goes beyond the Andon board by giving me direct insight into what the problem is for any one of my products, my bots, my agents, and helps me as an engineer not have to sift through logs

**[15:12](https://www.youtube.com/watch?v=nUNuNxMhwug&t=912s)** or spend a lot of time debugging. I can go directly to the problem, try to solve it, and keep our products up and running for our customers. LangChain is a direct embodiment of the Toyota Production System philosophy. And while the framework is timeless, and TPS is the bedrock for all hardware manufacturing today, it hadn't been well translated into software or agentic manufacturing of agents — until LangChain. LangChain carries the legacy of TPS forward, allowing all these principles to be carried over into manufacturing for the new era of software engineering. And so I'm really excited to see where LangChain is going to go, because our cultures are so similar.

**[16:01](https://www.youtube.com/watch?v=nUNuNxMhwug&t=961s)** And I fully believe that in the next few years — and actually probably now — the entire AI industry will look to LangChain as the TPS, or the LangChain Production System — the bedrock on which all the SaaS services, companies, et cetera, the entire industry is built on. [APPLAUSE]
