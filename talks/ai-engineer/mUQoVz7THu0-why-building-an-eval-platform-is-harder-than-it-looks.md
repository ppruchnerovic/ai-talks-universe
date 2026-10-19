---
id: mUQoVz7THu0
title: "Why Building an Eval Platform Is Harder Than It Looks — Braintrust"
slug: why-building-an-eval-platform-is-harder-than-it-looks
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-10-06T18:30:35Z
video_id: mUQoVz7THu0
url: https://www.youtube.com/watch?v=mUQoVz7THu0
youtube_url: https://www.youtube.com/watch?v=mUQoVz7THu0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "LLM evals", "AI evaluation", "agent quality", "LLM observability", "eval platform", "Braintrust", "BTQL", "AI agents", "tracing", "production monitoring", "eval flywheel", "AI product management", "Hossein Niazmandi", "AI engineering", "AI Engineer"]
topics: ["Data engineering & MLOps", "Evals, observability & reliability"]
transcript: true
---

# Why Building an Eval Platform Is Harder Than It Looks — Braintrust

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#LLM evals` `#AI evaluation` `#agent quality` `#LLM observability` `#eval platform` `#Braintrust` `#BTQL` `#AI agents` `#tracing` `#production monitoring` `#eval flywheel` `#AI product management` `#Hossein Niazmandi` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=mUQoVz7THu0) · [Conference site](https://www.ai.engineer/)

## Description

Most teams start their evals in a spreadsheet. Here's what happens when they try to grow out of it.

Hossein Niazmandi, who leads solutions engineering in the West at Braintrust, explains why measuring agent quality is much more than putting a UI on a spreadsheet. He covers the two pillars of agent quality, evals before production and observability after, and why non-deterministic LLMs make both necessary. Then he walks through the stages teams go through: spreadsheets, a custom UI, side-by-side experiments for PMs and domain experts, and finally a flywheel that turns production failures into test cases. At that point the hard part becomes the data: traces that are huge, nested JSON, needing both real-time and long-running queries, which is why Braintrust built BTQL. He closes with agents running evals themselves and surfacing failures nobody thought to look for.

In this talk:
• Evals vs observability, and why you need both
• The stages of eval maturity, from spreadsheets to a production flywheel
• Why agent traces break typical data warehouses
• Letting coding agents run evals while humans review the results

SPEAKER
Hossein Niazmandi, Solutions Engineering, Braintrust

LINKS
Braintrust: https://www.braintrust.dev
Braintrust SQL / BTQL reference: https://www.braintrust.dev/docs/reference/sql
Braintrust on X: https://x.com/braintrust

CHAPTERS
0:00 Intro
0:52 What Braintrust does
1:12 Evals and observability
2:21 Why evals matter
3:51 Isn't it just a spreadsheet?
5:11 What's under the iceberg
6:55 The improvement loop
7:35 Stage 1: spreadsheets
9:00 Stage 2: a custom UI
9:50 Stage 3: experiments for everyone
10:20 Stage 4: connecting production
11:49 Agent traces are huge and messy
13:19 Querying with BTQL
14:39 Agents running evals
15:53 Finding the unknown unknowns
16:43 Agents iterate, humans decide

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,488 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=mUQoVz7THu0&t=1s)** [music] >> Thank you for joining this session on why building agent quality platforms is hard. My name's Hussein. I lead the solution engineering organization on the West for Braintrust. Um, I spent 15 years in solutions between Salesforce and Databricks. I've been a lifelong technologist. I've built computers since I was 5 years old. So, I have this like insatiable appetite for technology, which finds me kind of on the bleeding edge of AI here at Braintrust. For those of you, I know some of you were in the room earlier when Jess did her session. I saw some hands about evals.

**[0:47](https://www.youtube.com/watch?v=mUQoVz7THu0&t=47s)** How many of you know what Braintrust is and what we do as a company? Just show of hands. Perfect. I see one or two. So, at a glance, Braintrust as a platform is focused around agent quality. And the core idea is helping teams build and maintain confidence with the AI features or the AI agents that they're shipping. And there are two key pillars of agent quality. The first is evals, which we talked about earlier. Evals is what you do before your agent reaches production. This is when teams experiment, they test the behavior, and they build the confidence that they want to have before they ship to production. The second pillar is observability.

**[1:37](https://www.youtube.com/watch?v=mUQoVz7THu0&t=97s)** Observability is once your agent is in production and is interfacing with real-life users. It's creating interactions. And the goal is to take that hypothesis that you built in your offline development process and then reinforce that in your production scenario through continuous monitoring. Evals and observability are closely related to the same problem. One happens in production, the other one happens in development, and both is the understanding to improve agent quality. Now, I won't spend much more time here. Let me close that. Let's talk about why we're here, which is why are evals important?

**[2:27](https://www.youtube.com/watch?v=mUQoVz7THu0&t=147s)** You know, evals matter because LLMs by nature are non-deterministic. They are highly variable. That variability is exactly what makes them so powerful. They can reason across many different domains. They can solve different kinds of problems, and they can handle a wide range of user needs. But that same flexibility also creates risk. Agents use LLM as their brain. And agentic experiences are starting to become the primary way in which users will interact with companies. So teams need confidence in their agents that they will behave reliably and produce the outcomes that they expect. And without evals, companies face real

**[3:16](https://www.youtube.com/watch?v=mUQoVz7THu0&t=196s)** risks. Brand Brands become a risk if there's inconsistent behaviors. Compliance if the agent says or does the wrong thing. And there's a cost and maintenance risk if the systems are hard or unreliable to debug or control. The goal of evals is to reduce that uncertainty before launch so that customers have a good experience and the agents behave the way that you expect them to. So you might be thinking, "Okay, well, Evals is just a UI on a spreadsheet, right?" And I guess I should ask the audience. Just show of hands, how many of you have run Evals and logged the results into a

**[4:05](https://www.youtube.com/watch?v=mUQoVz7THu0&t=245s)** spreadsheet? Has that happened? Okay, I see one or two. So, there's no shame in that, by the way. It's actually the a good first step. The important thing is that teams acknowledge that this is a real problem and they need a way to understand how agents behave based on different inputs. At the simplest level, an eval system tests against or it has three different kind of criteria. It has a way to execute agents against test inputs. Second, a way to view the outputs or the scores, even if those are being logged in a spreadsheet. And third, a set of test inputs or examples that can invoke the agent. An input example is whatever information is needed to start the agent run.

**[4:56](https://www.youtube.com/watch?v=mUQoVz7THu0&t=296s)** It could be a prompt, a request, or context that causes the agent to act. Now, spreadsheet-based Evals are not wrong. However, they're often the first step for a useful version of eval workflow. But, of course, as you can imagine, there's more to the iceberg than just what we just talked about. And if Evals were only, you know, run the agent, view the output, and then score it in a spreadsheet, this talk would be over right now. But, there's a lot more that happens behind the scenes or underneath the iceberg. There are many supporting teams that eventually need to build better data sets, scoring systems,

**[5:45](https://www.youtube.com/watch?v=mUQoVz7THu0&t=345s)** review process, debugging tools, and the way to connect pre-production testing with production behavior. We'll touch on some of these today, and anything I don't get to, you feel free to come up afterwards and we can chat about. And this is where things start to get complicated. The underlying technology is complex. LLMs are not simply deterministic. Agent quality is a multi-persona problem. It's not just software engineers and AI engineers. There are PMs who used to build PRDs that are now running evals. There are SMEs who have the domain expertise of the product that you're building. And evals themselves are just one part of the development and operating

**[6:31](https://www.youtube.com/watch?v=mUQoVz7THu0&t=391s)** workflow. And gone are the days where you build once with unit tests and regression tests, you ship to production, and you don't think about it. Evals are a way for you to continue hill climbing against one target, which is agent quality. So, let's talk about the different stages of the the eval platforms that we see. And before we do that, this is the North Star for many teams. They want to build the improvement loop, which is I have a feature or application that's in production. I can observe the failure modes that happen based on dimensions that I define. I want to be able to grab those failure modes and create test cases so that I can iterate offline, so I can improve my agent quality without

**[7:22](https://www.youtube.com/watch?v=mUQoVz7THu0&t=442s)** introducing new regressions. And then you continue iterating over time, because just like in classical ML, drift becomes a real thing. The way users interact with your agents will change over time. The way you build your agents will change over time. So, what What phase one look like? There were some hands that were raised around spreadsheets and it is not There's nothing to be shameful about. This is where many people start. And as the basic setup is pretty simple. It's a four loop with a set of input examples and a way to execute the agent. And with that, you can run the same examples that you tweak and see how the agent responds with the outputs over time.

**[8:09](https://www.youtube.com/watch?v=mUQoVz7THu0&t=489s)** The big biggest advantage is accessibility and time. You can start this with basically zero barrier to entry. But the the returns diminish pretty quickly. At this stage, you're pretty much only documenting. You can't really do true experimentation. And let alone do any kind of type of analysis over time. Common limitations are analytics are hard, they're manual, human scoring is valuable but difficult to do, collaboration is very weak, and domain experts are usually boxed out of these type of results. So, again, spreadsheets are a great starting place but difficult to evolve. Then someone, usually a product

**[8:57](https://www.youtube.com/watch?v=mUQoVz7THu0&t=537s)** engineer, you know, they see this problem and they think, "Okay, I can build a nice UI, a bespoke UI to help serve to solve this problem." And while it might be nice at a glance, um it helps you bring in the different personas that you would otherwise not have access to. This allows PMs to now kind of get into the loop of doing evals. But the limitation that you might have thought about, it continues. That the documentation, the review process, though it might visually look nicer, still collaboration becomes difficult. And though iteration cycles become quicker, it is still not easy for users to persist that data and do long horizon

**[9:45](https://www.youtube.com/watch?v=mUQoVz7THu0&t=585s)** analytics on. Still just a reporting tool. Then the next evolution becomes hey, I want my non-technical users to have an interface where not that they just log the results, but they should be able to experiment. I want to be able to tweak a system prompt. I want to change the underlying model. I want to iterate on some parameter values. So, being able to do this type of side-by-side comparison becomes the next evolution of the eval cycle that we see. But, there's still one primary gap. And that is that the test cases in which you use to do these kind of comparisons are still a curated set that arise in your offline evals. But, what happens in

**[10:35](https://www.youtube.com/watch?v=mUQoVz7THu0&t=635s)** production? I've done my iterations here. I have a good idea of what I can expect to happen in prod, but once I ship it to production, I'm operating in the blind. So, I have no idea what steps my agent is taking and when those failures are actually happening in my live environment. And when we think kind of going back to the flywheel, when we think about what are the best systems that enable this, well, you should be able to starting at the top observe the failure modes, log every input, output, every step of your trace execution that your agent takes, analyze, understand what went wrong. You create the dimensions of failure and success because you know the outcomes. Then grabbing those failure modes, those different scenarios where your users had

**[11:23](https://www.youtube.com/watch?v=mUQoVz7THu0&t=683s)** poor interactions, and creating evals in them in your offline process, iterating on them so you can create the improvements without developing new regressions. And then shipping to production and hill climbing against this. And when you think about the final outcome of this, well, you get teams that are building the flywheel. You get that entire development cycle inside of your platform, but then the problem becomes you have to have you have to maintain it. You own this this product that you've built. And especially this is easy to do when it comes to smaller scale or POC and demo environments. But agent traces are nasty. They are semi-structured JSON. In some cases we

**[12:14](https://www.youtube.com/watch?v=mUQoVz7THu0&t=734s)** see teams that are logging a movie's worth of data in each interaction, hundreds of megabytes. So being able to query that type of data can be difficult. And your typical cloud data warehouses kind of collapse under this type of volume and load. And this is the same problem that we ran into. I won't spend much time talking about Brain Trust, but when you have production traces coming in, you want to be able to query that data in real time as it lands in there. Because if your users are having poor experiences, you want to be able to know in real time what is happening, why are they having these poor experiences, and how can I remedy that as soon as possible. You also want to be able to do

**[13:02](https://www.youtube.com/watch?v=mUQoVz7THu0&t=782s)** long-running queries. If you think about being able to fine-tune your your agent experience or even have humans who are doing alignment by annotating your your judges' outcomes. Two different workloads. So we built an abstraction layer called BTQL, which is a another form of complexity because you want an interface for people to be able to query that data. So, it's not necessarily that it's just a UI or UX problem, but building an eval platform truly becomes a systems problem. And there are novel set of issues when the chat GPT boom happened a few years ago where

**[13:50](https://www.youtube.com/watch?v=mUQoVz7THu0&t=830s)** I need to do real-time ingest. I have huge payloads that are tens of megabytes, hundreds of megabytes in size sometimes, compared to traditional heartbeat observability, which are just kilobytes in size. The structure and the shape of the data is different. Having deeply nested semi-structured full text is difficult to query, and the read patterns are different as well. You want to be able to aggregate in large volumes, but also be able to do snapshots of of of in-time data. And building the right system should allow you to not only empower the AI engineer, but also the PMs,

**[14:38](https://www.youtube.com/watch?v=mUQoVz7THu0&t=878s)** as well as the SMEs. And more recently, we've seen that agents have become a first-class citizen of these eval platforms where you want to be able to use natural language in a headless experience where you can tell your coding agent of choice, "Find me all traces in the last 24 hours where the user had a poor experience. Run the evals for me." And because these coding agents have access to all of your underlying infrastructure and your code base, they become the mechanism to run the evals and log those results. And then it becomes a question of like, so so what? Why is this a Why is this important? Well, the goal is everything that I've shown you so far, it requires the

**[15:28](https://www.youtube.com/watch?v=mUQoVz7THu0&t=928s)** humans, the the engineer, the PM to be deeply involved in this process and it could be laborious at times. I BrainTrust, the way we think about this is we want to help you operate at scale. Rather than you having to think about these dimensions and of success and failure for your AI agent, BrainTrust can surface these insights automatically. Because we log your tracing data into our platform, we can run inference on them and we can tell you the unknown unknowns. Hey, what are what are scenarios and when my agent is failing silently or what are scenarios that my users are experiencing frustration by prompting my agent for the same request over and over again.

**[16:20](https://www.youtube.com/watch?v=mUQoVz7THu0&t=980s)** And it's a lot of things that we didn't talk about. Things like the underlying database that powers it or having to build our back into the system to manage controls and permissions or data masking. You know, each one of these features proves that this is not just a UI and a spreadsheet, but rather it is a a systems problem that powers it. And as we think about the evolution of of the improvement loop, I said this earlier where humans were doing the improvement loop and now we see coding agents where they could iteratively make changes and suggest what kind of improvements you should be making to your application. And ultimately, the humans responsibility is to review the outcome. If I have different iterations of these

**[17:10](https://www.youtube.com/watch?v=mUQoVz7THu0&t=1030s)** e-vals that are run by my coding agent, I can look at the outcome and make the decision of which version of it is the best for what I want to ship to production. So, with that, that is the end of my talk. I appreciate you all coming out and learning about why it's hard to build eval systems. Thank you. >> [music]
