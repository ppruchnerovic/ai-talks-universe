---
id: VGN22pPpb-8
title: "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j"
slug: thinner-agents-on-a-smarter-substrate-the-ontology-based
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Emil Eifrem"]
channel: "AI Engineer"
duration_min: 11
published_at: 2026-07-22T17:00:38Z
video_id: VGN22pPpb-8
youtube_url: https://www.youtube.com/watch?v=VGN22pPpb-8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer — Emil Eifrem, Neo4j

**Emil Eifrem**

`AI Engineer` · `AI Engineer` · `2026` · `11 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=VGN22pPpb-8) · [Conference site](https://www.ai.engineer/)

## Description

To automate opening a bank account, your agent needs to verify identity, so a team wires it to the DMV and a passport service and ships it. Then the next team builds the next agent and rediscovers, from scratch, where its data lives, across a hundred databases plus Snowflake, Databricks, and S3, whether it can trust the version, and whether it is even allowed to touch it. Every agent repeats that wiring, nothing updates when a source moves without a manual rewire, and no agent is smarter tomorrow than today. Emil Eifrem's fix is to make the agents thin and put the intelligence in a shared substrate underneath.

That substrate is an ontology based semantic layer with three parts. A business ontology names the real concepts, customers, accounts, checks, in the words people actually use, not f_name. A technical ontology catalogs every data source and its schema, with a mapping between the two. And execution traces record what each agent tried and whether it worked, so the layer learns bottom up: an agent that succeeded with the DMV lookup last time is more likely to reach for it next time. Discovery, trust, deduplication, and learning stop being every team's problem and become the substrate's.

Speaker info:
- https://x.com/emileifrem
- https://www.linkedin.com/in/emileifrem/

Timestamps:
0:00 - The account opening agent and its data sources
1:53 - The problem: every team rewires data from scratch
4:00 - Thin agents on a smarter shared substrate
4:37 - Pillar 1: a business facing ontology
5:26 - Pillar 2: a technical ontology and the mapping
6:19 - Pillar 3: execution traces that make it learn
8:01 - Solving discovery, trust, DRY, and learning

## Transcript

*1,870 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=VGN22pPpb-8&t=1s)** [music] >> All right. At Neo4j, we work with some of the largest companies in the world to help make their data ready for AI agents. And today I want to talk to you about a problem that we saw emerging over the last, call it, 6 to 9 months and propose a solution blueprint for that. So, let's say that we work at a big organization, a big bank, and we want to write an agent. Let's say that agent is helping automate the opening of a bank account. Right? You can imagine that's very ripe for automation. You want to be able to orchestrate that process. And I'm going to use the powers bestowed

**[0:50](https://www.youtube.com/watch?v=VGN22pPpb-8&t=50s)** upon me by a short keynote slot to grossly simplify what that agent looks like. I'm going to say there's two pieces. The first one is, let's call it, the business logic. Some version of interpreting intent and plan, act, and we loop around that. It's what your agent does. And we know that when an agent act, it doesn't always operate on data, but we equally know that in order for agents to be successful, a huge part of that is giving it access to the right data at the right time. So, the second big bucket is, let's call it, the data sources. Need to identify, figure out, okay, in order to solve my problem, I need access to these few things, and wire them up and make them available to the agent. In the example of our account opening agent, maybe we can imagine that we need to be able to validate identity. And so,

**[1:38](https://www.youtube.com/watch?v=VGN22pPpb-8&t=98s)** we might look at two data sources for that, the Department of Motor Vehicles, the DMV registry, and maybe some kind of passport verification service. So, we wire that up into our agent, and it works. It's great. It's fantastic. And at the same time, you and other teams in your organization are building other agents, and conceptually, they look very similar. That's great. It's fantastic. It works. But, it has a few problems. So, first of all, every single time a team has to build an agent, they have to figure out from scratch where the data that they require for that agent to operate, where it sits, which if you work at a startup and you have one application, it sits on top of one Postgres database, that's not hard. The data is in that Postgres database. But, in an enterprise ecosystem, you don't have one database, you have a

**[2:26](https://www.youtube.com/watch?v=VGN22pPpb-8&t=146s)** hundred databases, and you have Snowflake and Databricks, probably, and you have S3 buckets, and so on and so forth. You have to do that work manually from scratch every single time. And then, when you found the data sources, you know, in an enterprise, there's lots of duplication of data. So, then you need to figure out like, is this the right data? Is it the right version? Can I trust it? Am I allowed to access it? So on and so forth. It also violates one of the core principles of software engineering, the DRY principle, don't repeat yourself. So, when something change, that cascades across all of your agents. You have to kind of manually rewire all of them all the time, which works, but it's just a a lot of work. And then, finally, there's no learning around the data sources and how your agents operate on them. So, when your agent wake up wakes up tomorrow, it's

**[3:14](https://www.youtube.com/watch?v=VGN22pPpb-8&t=194s)** not smarter than it was today, and there certainly isn't any cross-agent learning because all of that wiring between business intent and the data sources is encoded in a combination of code and prompts. So, I know what you're all thinking. Markdown files, skills to the rescue. And yes and no. Um you can come talk to me afterwards for kind of the full version of this, but we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution. Uh but, don't take it from me, take it from Swyx. A week ago on the Latent Space Spot podcast, I said, "Hey guys, you got to learn your databases. You cannot vibe code with just markdown files." So, we've been solving this problem at

**[4:02](https://www.youtube.com/watch?v=VGN22pPpb-8&t=242s)** scale for some really massive organizations recently, including a Fortune 20 global bank, a massive tech platform company based here in the Bay Area, and a leading fintech company. And the pattern that is emerging is that in order to do things at scale, we need thin agents on a smarter shared substrate. Thin agents on a smarter shared substrate. And what does that look like in practice? There are three pillars to that. The first pillar is a business-facing ontology. And the word ontology, like I grew up in this world, people talked about ontologies forever. More recently, it's become very hype, probably thanks to Palantir, but also the rise of AI. And there's a lot of people who want to

**[4:50](https://www.youtube.com/watch?v=VGN22pPpb-8&t=290s)** make ontologies really complex. But the core concepts are actually super simple. What are the key concepts in your organization? In our banking example, customers accounts um debit cards, checks, transactions, and how do they all relate? But very importantly, they are expressed in a way that makes sense to all the human beings working in your universe, right? All the people working in your company, it's expressed in that name, in that way. In other words, you don't say if underscore name. No, you have a customer and they have a first name. So, that's the first, a business-facing ontology. The second pillar is a technical ontology. This is all the metadata of all the data sources and data assets in your enterprise ecosystem. I have 14 Oracle databases, I have 15 Neo4j databases, I

**[5:42](https://www.youtube.com/watch?v=VGN22pPpb-8&t=342s)** have Snowflake and Databricks and I have S3 buckets and all all that kind of stuff. Where do they sit? What are the schemas? All of that kind of good stuff. You can You construct that technical ontology in three key ways that we can talk about later, though not in this in this talk. And then you have a mapping between the two. So that customer that has a first name, that first name has a system of record and over there there's an Oracle database with a column called F_name. The mapping between the two. And then the third pillar is the run time signals out of your agents. When they walk this graph and they execute, they leave the traces around. What have I tried? Was I successful? What was the outcome? The execution traces. Those three pillars. Okay, so let's look at that in the

**[6:29](https://www.youtube.com/watch?v=VGN22pPpb-8&t=389s)** context of our bank account opening agent. This is a simplified view, but you can see this graph here. It has a combination of business concepts like checks and accounts and credit history and stuff like that. This is a process following agent or a process guided agent. We want this type of agent to actually follow a process. We've also encoded that in the ontology, a business process. And then if you look at the node that is surrounded by green, the check compliance one, we flip to the technical ontology and we've put in the graph here. We've discovered and encoded that in order to do a compliance check, you might imagine that you need to resolve a government issued ID. And then we say that in this particular organization, there are two data sources that can help us with that. It's the motor vehicle records and the passport

**[7:17](https://www.youtube.com/watch?v=VGN22pPpb-8&t=437s)** verification one. Which is that's really great. So then when our agents come in here and they realize I'm going to check compliance, I need a government issued ID. Here are the two ways that I can resolve that. When they execute and they try that, they leave the third pillar, the execution traces for that. And they're more sophisticated than what's on this simplified slide, but involves things like, okay, where was I? What did I do? What is my context? And was I successful? And ultimately it leads out to some kind of a score. And you use that as input. It's like, okay, I've been very successful using the DMV lookup, for example, then I'm more likely to choose one if I'm in the right context in my next invocation. Three pillars of the ontology-based semantic layer, a business ontology, a

**[8:05](https://www.youtube.com/watch?v=VGN22pPpb-8&t=485s)** technical ontology, the execution traces taken together, they solve all four of the problems. We now have a very easy way to discover the data sources. We know if they're trustworthy or not. We know that top-down by some kind of human curated knowledge, right? An administrator of some sort saying it. We also know it bottom-up through the execution traces. This is what actually worked in reality, in practice. We have a single governed place that maps business intent and the concepts to those data sources. So, we don't repeat ourselves. If something changes, that cascades across all my agents, right? And we have self-learning. So, my agent that wakes up tomorrow is slightly smarter than it was today. And not just self-learning on an individual agent, but across agents as well. So,

**[8:53](https://www.youtube.com/watch?v=VGN22pPpb-8&t=533s)** we're moving from this world, a world of thick agents with manually wired data sources, into this world where we have thin agents on a smarter shared ontology-based semantic layer. And this allows us to do a ton more agents without having to re-engineer them every time. Thin agents on top of a smarter shared substrate. If you think this is interesting, there's a documentation webpage that outlines more information about this. If you see the QR code here, you can also come and talk to us at the booth. We have a big booth here at the Expo, P3. We love talking about this this kind of stuff. But not just that, this is one pattern, a very exciting pattern that we see a lot of traction around right now

**[9:42](https://www.youtube.com/watch?v=VGN22pPpb-8&t=582s)** for using graphs in AI. But there's hundreds of more interesting patterns that combines graphs and AI. 10 of them is actually in the graph track that is kicking off right now in room 2005. And you have some really amazing talks from organizations like the Gates Foundation, monday.com, JP Morgan Chase, Berkeley, New York Times, and so on and so forth. So go check out that thing. And then finally, this was primarily centered around organizations where you deal with many data sources and many agents. But if you're a startup building on Neo4j, love you. There is a startup program for Neo4j that is phenomenal. You get access to free credit, but more importantly, we've built up a dedicated

**[10:30](https://www.youtube.com/watch?v=VGN22pPpb-8&t=630s)** solution engineering team that spent every day working with startups for free, helping them model their data in Neo4j, tune it for performance, and so on and so forth. So please sign up for our startup program. Thank you very much. Enjoy the conference. Have a good day, everyone.
