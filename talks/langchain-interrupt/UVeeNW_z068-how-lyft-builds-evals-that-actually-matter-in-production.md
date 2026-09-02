---
id: UVeeNW_z068
title: "How Lyft Builds Evals That Actually Matter in Production | Interrupt 26"
slug: how-lyft-builds-evals-that-actually-matter-in-production
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 17
published_at: 2026-06-15T12:37:30Z
video_id: UVeeNW_z068
url: https://www.youtube.com/watch?v=UVeeNW_z068
youtube_url: https://www.youtube.com/watch?v=UVeeNW_z068
tags: ["LangChain", "LangSmith", "LangGraph", "AI evals", "LLM evaluation", "AI agents", "production AI", "customer support AI", "offline evaluation", "LLM as judge", "Lyft AI", "agent engineering", "AI observability", "eval framework", "RAG", "AI in production"]
transcript: true
---

# How Lyft Builds Evals That Actually Matter in Production | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `17 min`

`#LangChain` `#LangSmith` `#LangGraph` `#AI evals` `#LLM evaluation` `#AI agents` `#production AI` `#customer support AI` `#offline evaluation` `#LLM as judge` `#Lyft AI` `#agent engineering` `#AI observability` `#eval framework` `#RAG` `#AI in production`

[Watch the recording](https://www.youtube.com/watch?v=UVeeNW_z068) · [Conference site](https://interrupt.langchain.com/)

## Description

Nick Ung, ML lead for safety and customer care at Lyft, breaks down how his team built an eval system that actually keeps pace with production AI agents at Interrupt, the agent conference by LangChain.

From offline simulation with mocked MCP outputs to LLM-as-judge rubrics tied to real task success criteria, Nick shares the mistakes they made early  and the framework they built to close the loop between evaluation, annotation, and continuous improvement across 270K AI interactions per month.

How Lyft Builds Evals That Actually Matter in Production | Interrupt 26
0:00 Introduction and Lyft AI Assist overview
1:47 AI Assist journey and agent examples
3:35 Why eval matters at scale
4:18 Offline eval as a quality gate
6:03 Building a lightweight simulator
8:17 LLM as judge and the problem with scalar metrics
9:52 Task-based rubrics and actionable failure modes
11:28 Trusting your LLM judge
12:17 The rude awakening — when offline evals lie
14:14 How LangSmith manages the eval workflow
15:46 What's next for AI Assist

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• About LangChain: https://www.langchain.com/

## Transcript

*2,426 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=UVeeNW_z068&t=5s)** >> Hello, everyone. Happy Wednesday. It's the middle of the week. So for those of you who don't know me, my name is Nick. I lead the data science and machine learning function for safety and customer care at Lyft. And my team has been building AI Assist, which is our customer care AI agent product for years. And I'm here to talk to you about how we built an eval system that actually helps to scale AI agents in production. So maybe just a quick show of how many of you here ship agents without eval. I'm literally guilty of that, so don't be embarrassed. I know it's one of those things that we always forget about, but really shouldn't. Hopefully, you

**[0:57](https://www.youtube.com/watch?v=UVeeNW_z068&t=57s)** know, Lyft doesn't need any additional introductions. Hopefully everyone in the room knows Lyft, but just a couple of statistics about Lyft. You know, we have 79 million trips per month, and our AI Assist chat today has served about 270,000 AI interactions per month. We've been able to build seven AI agents and more in production. Our deflection rate is 65%, and AI resolution rate is at 35%. 35% might seem a little bit low, but we really hold ourselves to a very high bar. We want the agents to solve the customer issue fully end to end, and not just block the customer from reaching support. I'm sure you all have experienced that with support chatbots. So I'm going to quickly walk you through AI Assist's journey.

**[1:51](https://www.youtube.com/watch?v=UVeeNW_z068&t=111s)** We started this journey in 2024. We used very simple deterministic logic back then. So imagine if you say A, the bot is gonna say B back to you, but we all know how LLMs have really transformed the space. And with eval, we have been able to build more than seven AI agents in the past. And our resolution rate has really gone up from 10% to 35% and climbing. Just to give you a sense of what type of AI agents we're building at Lyft — for riders, we have agents that handle charges disputes. Unpleasant experiences. If you ever have a Lyft driver that smokes in the car, you can report to us. On the driver side, you know,

**[2:39](https://www.youtube.com/watch?v=UVeeNW_z068&t=159s)** we have automated damage claim processing, compliance status, yada yada — taxes. We love doing that. I also just want to show a couple of really interesting agents that I thought were really cool that we built. And also shout out to Akshay and Sutanda, probably down here, who are on my team and built this AI agent. We have this agent on the driver side that is a multi-modal, complex AI agent that when a driver uploads photos of their damage claim, we get back to them in about 15 minutes with a claim decision. On the rider side, we have an agent that literally processes 80-plus automation rules and refund logic in the back end and is able to contextually — based on what the rider

**[3:28](https://www.youtube.com/watch?v=UVeeNW_z068&t=208s)** is telling us and what their situation is — explain our refund decision to them in a very seamless way. And all that is to say: we wouldn't have been able to ship so many AI agents, or test and make sure that such complex AI agents actually perform in production, without a great eval system. So those of you who ship agents without eval, reconsider that decision. Cool, so I'm not gonna walk you through AI Assist's architecture. It's LangChain, LangGraph, LangSmith, some MCP and all that, but I'm more interested to talk to you about how we think about AI Assist eval, or how you ship your eval

**[4:15](https://www.youtube.com/watch?v=UVeeNW_z068&t=255s)** for your production system, right? A little bit about myself. I've been — for my entire career, I have been doing data science all the while. I've been building machine learning models. And my approach to thinking about AI eval for AI agents is no different than traditional ML evaluations. So for those of you who come from a data science background or ML engineering background — you're working in the notebook. You develop this model. You train on a huge dataset. You have some kind of ground truth for regression or classification tasks. And then you run this offline evaluation and see what the performance is. Should we ship? Should we not ship? Think about this as a quality gate.

**[5:03](https://www.youtube.com/watch?v=UVeeNW_z068&t=303s)** Can we launch? So I really want to emphasize the offline eval piece. If that has been the way that we do ML engineering for the last couple of years, why should AI engineering be any different, right? So really think about that. And the offline eval really serves as a quality gate. You don't want to use your users as test data. But maybe if you're a start- up with five customers, maybe that's okay. But at the scale of Lyft, we really don't want to use our customers as test data. And once we got the agent into production, we have continuous monitoring. We have our online eval, getting all the LangSmith traces, human in the loop — all that good stuff that's

**[5:52](https://www.youtube.com/watch?v=UVeeNW_z068&t=352s)** giving us feedback on how to improve the AI agents. So I'm going to go into each of these components in a little bit more detail. Thinking about offline evaluation — what does that mean? How is that different from a traditional ML engineering workflow? We love working in notebooks. We love just slapping on a CSV file and then getting a ground truth. But for AI engineering, it's a little bit more setup than that. We really took inspiration from Tau Bench, which the fantastic team at Sierra AI has published as a public benchmark that all the other LLM models and AI labs are using as a benchmark. So for this offline evaluation pipeline, we built a lightweight simulator.

**[6:48](https://www.youtube.com/watch?v=UVeeNW_z068&t=408s)** On the right here, we have our LangGraph agent, which is the AI agent that we built for AI Assist. And then we have an LLM user — we just use one of the out-of-the-box LLM models to role- play as a user so that we can generate this end-to-end trajectory of an interaction, right? And then we use a very config-driven approach. We have a YAML file that specifies what the user intents are, what the support scenarios are that we're looking at, and how we mock the state of the world. Because in offline, you're not making network calls to other MCP servers. So in an offline setting, we're mocking those MCP outputs. And imagine if an agent calls a tool offline —

**[7:40](https://www.youtube.com/watch?v=UVeeNW_z068&t=460s)** we sort of just mock the MCP output with one of the values that's in the config file. So we get this long chain of trajectory on the permutations — our config is permutations of different combinations of different things, right? The state of the world, the user intent, user persona. And the goal here really is to get a diverse dataset that you can use to approximate production data. You want your offline eval to be a good proxy for how your agent is going to perform when you actually turn it on. So for the trajectory, we also define evaluators. We use LLM-as-judge. I think everyone is doing that. Code assertion — we run some very simple Python scripts that

**[8:32](https://www.youtube.com/watch?v=UVeeNW_z068&t=512s)** check the end state of the world to see if certain conditions are met to define success or failure. I'll get into LLM Judge a little bit more. I think when we started thinking about LLM Judge, and I'm sure everyone here has looked into LangSmith or any other observability platform — you see different platforms and frameworks come with a pre-built set of LLM judges: things like toxicity score, response helpfulness, conversation conciseness, and things like that. And we kind of started the same way as well. We were defining things like tone appropriateness, response helpfulness, naturalness, and all that. And these have been scored on a scale

**[9:23](https://www.youtube.com/watch?v=UVeeNW_z068&t=563s)** of zero to one — a scalar metric. So what's the problem with this, right? For response helpfulness, for example, what does a 0.4 score mean compared to 0.7? What does that mean? How can you move the needle, right? And if you want to move your overall score, what product insight is this giving you? So we've been very opinionated about what LLM Judge should do. And hopefully no one's using a generic helpfulness score for an agent in production. The way that we think about LLM Judge is that it should be framed around the task that you want your AI agent to perform, right?

**[10:17](https://www.youtube.com/watch?v=UVeeNW_z068&t=617s)** So your AI agent is being instructed to do tasks A, B, and C, and each of those tasks has its own success and failure criteria. So a very simple example that I pulled from our LangSmith platform is this educational rubric. break. So one of the tasks that we want our AI agent to do is to educate the user about Lyft policy around rider charges or some other type of support scenario. So the benefit of doing this is you're defining very clear success criteria for your agent. And by defining a rubric like this, when you see interactions that fail your rubric, you can very quickly know what some of the common failure modes are, right?

**[11:03](https://www.youtube.com/watch?v=UVeeNW_z068&t=663s)** And that becomes actionable insight. That becomes product insight to help your tech team, your engineering team, to improve your AI agent. Tweak a prompt, tweak a tool, change your control flow logic, or whatnot, and then you run the loop again and see if it improved. So this is just another rubric that I want to quickly show as well. OK, another thing that we really struggled with is: how do we trust this LLM-as-judge, right? We define a rubric, we define some prompts, but how do we know it's doing the right thing? So my own personal take is that, well, you just train an LLM judge like a machine learning model. You collect some human-labeled ground truth

**[11:52](https://www.youtube.com/watch?v=UVeeNW_z068&t=712s)** from your domain experts about how to score a certain interaction based on a rubric. And you go through this traditional ML engineering loop — change your prompt, change your reasoning — see if it aligns with your human agreement score, and then if it does, you have an LLM judge that's aligned with human judgment. So in our offline simulator, what else can go wrong, right? I spoke earlier about how we used an off-the-shelf Claude or OpenAI model to role-play as a user. But often what we see is — as you can see here — the LLMs are being a nice, helpful assistant. They explain their issues very nicely to our AI agent. But I'm guilty of this as well.

**[12:47](https://www.youtube.com/watch?v=UVeeNW_z068&t=767s)** I don't typically do this when I reach out to support. More often than not, what we see user verbatim in production is like one or two words, right? People are very impatient. People don't sit down and nicely explain their issues. So when we did this, our first AI agent was giving us a 90% pass rate. Nice. We can launch, right? But it was a rude awakening for us when we actually launched into production. So what can we do to fix this, right? This is a pretty active research area as well. Microsoft published a paper about this — how you should be training your LLM user using real-world verbatim data, right? So this is essentially what we are planning to do at Lyft as well.

**[13:36](https://www.youtube.com/watch?v=UVeeNW_z068&t=816s)** We are actively looking into fine-tuning a custom LLM that's aligned with our Lyft user verbatim so they speak more like our users. Technically making our eval a little bit harder — your benchmark score might go down. But you really want this to be a good proxy for production, right? Otherwise, what's the point of this? The other thing that we are looking to work on with our UX team is defining clear user personas, right? And this will be used to ground our LLM model to behave more like a Lyft user. All right. I want to quickly talk about how LangSmith really helps us manage our eval workflow. Tracing, evaluator setup, automation, annotation queue.

**[14:26](https://www.youtube.com/watch?v=UVeeNW_z068&t=866s)** If you're here, you're probably familiar with LangSmith. I'll just quickly speak through this because I'm running out of time. You know, tracing — I think this one has been brought up multiple times in previous presentations — but with offline simulation and our online runs in production, we're using LangSmith to help us capture these nice trajectories. This becomes really nice training data for our models later on, as well as a good interface for our operations team who are manually annotating our data. Evaluators — this is how we built our LLM judge that we use for our offline simulator as well as for production monitoring. Annotation queue — one of the nice things about LangSmith is that we have automations in LangSmith.

**[15:16](https://www.youtube.com/watch?v=UVeeNW_z068&t=916s)** So for traces that fail your LLM judge criteria, we can set up an automation that sends the failed traces to an annotation queue. And here we have our operations team set up on this annotation queue to help us manually label these examples, and our engineers go in and analyze what the systematic failure modes are, and that feeds back into how we improve our AI agents. All right, so what's next for AI Assist, right? We've done a lot of agent engineering — managing the context, managing the harness, right? I think that's the shiniest thing in town nowadays. Managing the harness around the model — which is basically everything around the model — whether that's the RAG pipeline,

**[16:05](https://www.youtube.com/watch?v=UVeeNW_z068&t=965s)** tool definitions, graph, system prompt, and all that. And we've been running our offline simulator more as a lightweight script offline. And now there's a concept of an eval harness that we can define, that can help us manage our evaluation runs offline more and more effectively. And thus far, for all the traces that we've been collecting, we've been using them to feed into product insights that help us improve our agent, improve our harness, but we haven't really done much on model training — updating the weights of the LLM and training a custom LLM for AI Assist. So that is one active area that my team is looking into. So that's how we close the loop on the eval pipeline.

**[17:00](https://www.youtube.com/watch?v=UVeeNW_z068&t=1020s)** All right. Thank you, everyone. [APPLAUSE] [APPLAUSE]
