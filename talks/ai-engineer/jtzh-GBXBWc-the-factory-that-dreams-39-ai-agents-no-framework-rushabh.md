---
id: jtzh-GBXBWc
title: "The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft"
slug: the-factory-that-dreams-39-ai-agents-no-framework-rushabh
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Rushabh Doshi"]
channel: "AI Engineer"
duration_min: 10
published_at: 2026-07-11T20:00:27Z
video_id: jtzh-GBXBWc
url: https://www.youtube.com/watch?v=jtzh-GBXBWc
youtube_url: https://www.youtube.com/watch?v=jtzh-GBXBWc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# The Factory That Dreams: 39 AI Agents, No Framework - Rushabh Doshi, Machinecraft

**Rushabh Doshi**

`AI Engineer` · `AI Engineer` · `2026` · `10 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=jtzh-GBXBWc) · [Conference site](https://www.ai.engineer/)

## Description

Most AI demos are built around a toy workflow. Ira was built around a factory.

This talk is the story of how a third-generation Indian machinery company built a multi-agent operating system that helps run sales, business development, recruitment, quoting, marketing, production context, email workflows, and organizational memory. Ira is not a chatbot and not a wrapper around a single framework. It is a company brain: 39 bounded specialist agents, Athena as orchestrator, a 17-stage request pipeline, Qdrant for document memory, Neo4j for relationships, Mem0 for long-term semantic memory, Postgres for CRM and recruiting data, Redis for coordination, and Cursor as the operating cockpit.

The deeper lesson is architectural: companies do not need generic AI assistants. They need digital brains grounded in their own documents, relationships, processes, and values. I will show how Ira ingests company files through a "digestive system", routes work through a pantheon of agents, verifies claims through immune-system style guardrails, learns through memory and corrections, and "dreams" through a nightly consolidation cycle. I will also explain why we gave Ira a SOUL.md: a philosophical constitution based on Anekantavada, Syadvada, Svadharma, and operational truthfulness.

The talk ends with the Fork My Brain thesis: the right way to build company AI is not to sell another SaaS dashboard. It is to send a special-ops AI team inside a company for a week, map the business from the inside out, ingest the right files into Qdrant and Neo4j, wire the operational databases, and leave behind a forkable digital brain that employees can run through Cursor and LLMs.

Speakers:
- Rushabh Doshi (Machinecraft / Fork My Brain): Rushabh Doshi builds and operates Ira, a multi-agent AI operating system for Machinecraft, an Indian thermoforming machinery manufacturer, combining Cursor, LLMs, retrieval, memory, and business operations into one living company brain.

## Transcript

*1,395 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=0s)** Okay, I want to tell you a story about a factory that taught itself how to remember. Hi, I'm Rushabh. I run Machinecraft, a 100 people factory in India. No data science team, no ML budget, none of that. And somehow we ended up building a 36 AI agent that runs our entire go-to-market. I think that's still a little ridiculous. Let me show you how it happened and why you can do the same thing. So, here's the thing about our company. From the outside it looks like machines and metal. But the actual company, the part that matters, isn't the machines, it's the knowledge. Who the customer is, what we quoted them in 2019, why that one machine needed that weird custom tweak. And for three generations, all of that lived in

**[0:50](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=50s)** exactly three brains. Initially my grandfather's, then my father's, and now mine. Which is a genuinely terrifying way to run a company. When you sit with it. A lot of people have joined us, people have left us, the revolving door never stopped. And every single time someone walked out, a chunk of our brain walked out with them. We weren't scared of the competitors, we were scared of forgetting. Or waking up one day and realizing the whole company only existed inside two increasingly tired heads. So, I had an idea. I'll be honest. Sounded insane first. But what if instead of writing the knowledge down in some document nobody ever reads,

**[1:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=97s)** what if we grew a brain that just held it? Not a chatbot you poke at, a twin of the company. I didn't hire a sales team. I tried to build one. A quick detour because you need to know how messy this is. We make thermoforming machines. They heat up a plastic sheet and shape it. Same core machine, but it ends up making hydroponic farm trays, spa bathtubs, EV car panels, medical casings, and even packaging. Seven totally different worlds, seven totally different buyers. So, this brain couldn't just memorize a brochure. It had to know which universe a given customer lives in. Step one was almost boringly simple.

**[2:27](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=147s)** Feed it everything, and I mean everything. Years of quotes, drawings, payment schedules, timelines, email threads, hundreds of gigabytes of our own private history. Not the public internet, our internet. And here's the plot twist. The part that surprises every engineer I tell this to. We never trained a model. No GPUs humming in the basement, no fine-tuning. We just looked at all the history, chopped it into bite-size chunks, and let off-the-shelf models read it and pull out the facts. We stored the meaning of each chunk as vectors and relationships. Who's connected to what as a graph. The brain isn't a smarter model. It's actually a really, really well-organized

**[3:16](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=196s)** memory. Now, this is where it gets a little weird in a good way. We stopped thinking of Era as a software and started thinking of it as something we were raising. So, we gave it a body modeled on biology. Senses to figure out who it's talking to, a gut to digest the documents into facts, a memory, a dream cycle, an immune system to fight off bad information. Why biology? Well, because evolution already spent a billion years solving how do you stay coherent over time? We just copied the homework. Okay, so the big question. Why 36 agents instead of one genius mega prompt? Because, and you already know this if you've ever tried it, one prompt that's supposed to do everything ends up

**[4:04](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=244s)** doing everything badly. So, Ira isn't one mind, it's a pantheon. A whole cast of specialists. Each one has exactly one job. Athena runs the room. Prometheus owns the sale. Plutus does pricing. Hephaestus knows every machine spec cold. Vera fact checks everything, and Memnon, my favorite, guards corrections. So, the second a human fixes something, it stays fixed forever. One agent, one job. It's a team, not a hero. And here's the cool part. They hold meetings. Athena pulls in specialists. They actually argue, and a single answer comes out the other side.

**[4:53](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=293s)** It's like having a board room that never sleeps, never gets tired, and somehow has no ego. So, what does all this actually run? Honestly, the whole front business. Everything between a stranger exists somewhere, and now they're a customer. Nine concrete jobs every single day. Outbound emails that actually reference my real world. Account briefs built from cross-checked truths before a call. Quotations. A swipe left, swipe right mode for outreach. Reviving dead leads, which I call blast from the past. Inbound replies, and figuring out before we waste an hour whether a company is even a fit.

**[5:40](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=340s)** Nine jobs, one operator who never sleeps. Where does all this live? One cursor tab. That's genuinely it. You type and Eira reaches out with a dozen hands. Searches the knowledge base, reads the inbox, drafts the email, builds the code, and then shows you before anything actually goes out. Under the hood, it's genuinely a real stack. Not a demo held together with duct tape. Databases for vectors, for relationship graph, for the CRM. Three different model providers, each picked for the job it's actually best for. Tools for Google, for swallowing documents, for every communication channel, plus monitoring. So, we can see what it's thinking. All of it, every capability exposed as

**[6:29](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=389s)** 213 tools over one protocol. And the golden rule, the one we never break, Eira drafts, human sends. Now, memory. And this is the part where most AI quietly lies to you, because a raw language model is basically a goldfish. Brilliant for about 30 seconds, and then you close the tab and forgets you ever existed. So, we engineered memory on purpose, in layers. Working memory for the last few minutes. Pinned facts about someone who who is. Episodes, whole conversations as little stories. Relationships with warmth that grows from stranger to trusted. And a bouncer at the door. A salience gate that decides what's even worth remembering, so the brain doesn't

**[7:17](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=437s)** fill up with junk. When two facts disagree, corrections win. Continuity without making things up. And then, I genuinely love this part. At night, it dreams. Every night, Eira runs a sleep cycle. It replays the day, locks in useful stuff, hunts for contradictions, gently forgets the stale junk, and turns the day's work into reusable skills. In the morning, there's a little dream report waiting for me to read. Here's what I consolidated. Here's what I Here's what I let go of. Here's what I figured out while you were asleep. The thing literally gets smarter overnight. And here's the part I care about the most. Every agent has a conscience. And it is

**[8:07](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=487s)** emphatically not to be helpful, be harmless. It's a soul file written from the principles of a Jain family business that's been doing this for the last three generations. Five old ideas turn into engineering rules. No single source has the whole truth. So, cross-check before you speak. Never say things absolutely. Cite the document and the date. Do your own job, not someone else's. Report the truth even when the truth is ugly. And nobody works alone. Ancient philosophy running as guardrails in production. Now, let's talk money. Because this is the part that should make the whole industry a little uncomfortable. There was no training bill. Zero. The expensive part was never compute. It

**[8:54](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=534s)** was teaching a company to remember itself. An agency quoted us 230 grand to build this. We built it for around 30. That's cheaper than a nice watch. And it runs on a couple of thousand dollars a month. So, here's the move. We pulled the whole architecture out and made it forkable. We call it Brain OS. It ships as an empty nervous system. The agents, the memory, the dream cycle, the soul file. All there, completely blank. You pour your own company's truth into it and from inside out. Because here's the thing nobody can outsource for you. Only you can build your company's brain. We are a 100 people factory with no data scientists. If we can grow a brain, you can too.

**[9:42](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=582s)** We are not selling ours to you. We are helping you build your own. forkmybrain.org Go build something that remembers. Thank you.
