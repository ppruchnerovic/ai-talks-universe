---
id: gVT0h3xUY3M
title: "Ori Goshen - Self Optimizing Agents"
slug: ori-goshen-self-optimizing-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Ori Goshen"]
channel: "Berkeley RDI"
duration_min: 17
published_at: 2026-08-12T01:59:21Z
video_id: gVT0h3xUY3M
url: https://www.youtube.com/watch?v=gVT0h3xUY3M
youtube_url: https://www.youtube.com/watch?v=gVT0h3xUY3M
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Ori Goshen - Self Optimizing Agents

**Ori Goshen**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `17 min`

[Watch the recording](https://www.youtube.com/watch?v=gVT0h3xUY3M) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*2,018 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=2s)** ORI GOSHEN: My name is Ori Goshen, and I'm the co-founder and CEO of AI21. AI21 is an AI lab based in Tel Aviv. Super excited to be here and tell you about our work around self-optimizing agents. And so today, we'll speak about these self-evolving AI systems, why it's needed, why it's hard, and why now. And I mean, the time is now. I mean, we all see the challenges in the industry. And we'll speak about it. And of course, I can say personally, for myself, my wife is asking from me this feature all the time. And I'm probably still in the early beta version.

**[0:56](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=56s)** So, in the past few months, we've seen many of these AI systems actually shift from experimentation to production. We're still very early in this journey of AI adoption. But we're seeing systems that are now being actually deployed at scale. And this introduces a new set of challenges. And the most obvious one is to operate economically at the frontier. And what we're hearing from customers again and again is that we have this agent. We're pretty satisfied of how it functions and the overall performance. But we know that if we would want to apply it for every PR

**[1:49](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=109s)** or for every call or for every booking or for every transaction, it will be prohibitively expensive. And this has been the talk in the last couple of months. Tokenmaxxing is basically over. Now, everybody is speaking about token efficiency. And that becomes the focus of the industry. And the question is, really, how do we get the best possible performance per token investment, or how do we basically get the best real customer outcome per dollar investment? That's a real question. And I think we as an industry become smarter about it. This is what we see a lot of customers aspiring to achieve,

**[2:43](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=163s)** basically. Where you want to make the acceleration of the AI usage. You want to see the outcomes of that AI usage. I don't know if you can see it very clearly, but the black line is essentially an indication of the usage of a certain company in terms of tokens. And the bars represent the cost. And the cost broken down per model. So you can see, at one stage, this company, in this case, Coinbase, we're able to get more control over the cost, and if that correlated lines basically disjoint. So that's where companies are looking to get themselves. And here is a typical flow of an optimization process.

**[3:41](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=221s)** So you have an agent. You start with several configurations. And we'll speak about the configuration space which is pretty vast. And then after experimentation, you discovered the Pareto frontier, the set of operating points that you would want to select a point from. And then you select an agent candidate. And basically you start evolving the system from there. And in many cases, we see that we have a target operating zone in terms of cost and quality. And you're trying to get your system, you're trying to get your agent performing in that level. That's easier said than done.

**[4:30](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=270s)** And if you look at-- this is a caricature of the configuration space. You have a lot of levers to play with. Obviously, you have the model itself and the model weights. That can be changed. You have model selections, where now in a world where there are so many different models that are presenting very different capabilities and performance characteristics. But then, you have the harness which also plays a very important role. And the harness includes the tool specifications, the prompts, the skills. Actually, the code, the scaffold that you build around it. There's so many moving parts. And that represents a challenge. So let's look at a concrete example.

**[5:23](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=323s)** And one of them is around a benchmark called Browse, Comp. Browse, Comp is basically a deep research benchmark, which is verifiable because the information, the answer-- it's not an open-ended benchmark. The answer is included inside the given corpora. So the first thing you do is, again, map the candidates, as I showed earlier. So you would try, in this case, different models with different configurations. In this case, in different retrieval configurations. You have a dense retrieval and a sparse retrieval and another strategy retrieval of a late interaction. And what you see here, again, empirically on this benchmark is basically the GPT 5 family with the late interaction

**[6:18](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=378s)** retrieval and the MiniMax. They basically represent the Pareto frontier. You would want to select between these two options. That's the very basic. And I think most of the teams are doing these kinds of mapping before they go to production. But then there's another dimension. There's scaling. You can apply different execution strategy. For example, vertical scaling, like the amount of thinking tokens or the amount of iterations you give the loop or the different types of fixed repair loops that you can apply, or you have horizontal scaling when you basically try to generate multiple candidates

**[7:07](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=427s)** and then select or merge results from those set of candidates. So if you look at-- and this is well known for being Best-of-N. You basically use the same model to generate multiple candidates. You run them in parallel. And then you compare. And you pick the best one. And what you see here in the same benchmark, you actually starting to discover new types of result. The yellow line here is representing the MiniMax, which was the cheaper but also lower in terms of quality. And now, if you look at the chart, you see that if you horizontally scale,

**[7:55](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=475s)** you generate multiple candidates and pick the best one, you can actually, using the same model, get to the same level of quality of the top quality candidate in the earlier chart. But what you can also see here is that scaling each of these models, you get better and better results. For example, the GPT 5 also increased quality in comparison to cost. So basically, you discover more options to run your agents with this. Another strategy is basically operating an ensemble or portfolio of models.

**[8:42](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=522s)** So not just generating candidates from the same model but generating candidates from different models. This could be with adjusted prompts and tool definitions, et cetera. And then, again, you can take all of these outputs and combine them into the most optimal result. And again, I think this is really in line with the discourse we're seeing today, moving from tokenmaxxing to modelmaxxing. How are we able to harness more and more goodness from different types of models? And what we actually see, again, under this benchmark, although it's applied-- it's applicable pretty broadly, is that different types of models,

**[9:35](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=575s)** they cover different areas of the space. And so if you are pretty diligent about measuring the covariance and how each model is contributing, you can gain a lot of benefits. So the sum of using all models is greater than using them separately. And if you apply these techniques smartly, you can gain a lot of outcomes. So for example, basically applying this portfolio strategy, you essentially discover a new Pareto frontier, where you have better cost performance mixing these different models in different proportions. And this is something that can be learned per task.

**[10:27](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=627s)** It doesn't have to be manually discovered. You actually can learn these different combinations. And what you see here, for example, is with that portfolio construction, you are able to get to about 50% less cost for about the same quality if you use the previous state-of-the-art setting. So really, the same thing applied if you compare not just accuracy with cost, but also accuracy to latency. It's the same basic principle. So now, you have a lot of options. But now, there's another dimension

**[11:17](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=677s)** of execution strategies. You can chain this call to models differently. You can use different escalation strategies. You can prioritize calling wire models to another. And you can set some different stopping threshold, which also impact the performance. So this is another dimension. And here, we'll look at another-- just for the sake of diversity, we'll look at another benchmark, a SWE-rebench benchmark. And here's a work where we actually see that changing the execution strategy also has an impact on different tradeoffs. In this case, cost and latency trade, offs. So the simple Best-of-N means you run all the candidates.

**[12:10](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=730s)** You let the last one get the outputs. And then you pick the best one. A more efficient strategy is to do it like a cascading order. You start with the weakest model. And you go from there. And when you reach a stopping point where you're satisfied with the-- you're confident enough about the results, you stop. So you're making gains there. But you can also do it in parallel and have that same early stopping strategy applied. And in that case, you're not saving on cost, but you're more saving on latency. You're more optimizing for speed rather than cost. And basically, what you show here

**[12:56](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=776s)** is that you can play with that tradeoff the same level of quality. You can apply different types of execution strategies and gain different trade offs between cost and latency. So if you care about speed, you can use one setting. If you care about cost more, you can use another one. And one final example on the execution strategy is very much like human. And if we take the legal example, when you come a legal task, we typically have many, many junior interns doing the busy work. And then it rolls up to an associate that synthesize some thesis around it. And then finally, we have the partner

**[13:44](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=824s)** who's concluding and making the final decision. So same thing can be applied in coding. In this case, we show that if you have a weaker model, just generate many, many rollouts, then a stronger model, and reach those rollouts with more relevant information. And then a super strong model, like a fable level model, generate the final patch in making the final decision. You actually get better quality and a much, much cheaper like 3x cheaper than just using frontier model. So the gist here is that all of these strategies can be learned. The search space is huge. Right.

**[14:34](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=874s)** It's not a simple problem. And doing it manually, you'll probably miss a lot of optimization opportunities. So we want to find an automated way to do it. And one challenge of doing it manually is-- what happens when a new model comes in, or when a pricing change, or the environment change. The traffic also change. The task distribution also changes over time. So you need to address all of these. That's why, basically, manually searching this space is not something practical. So what we do in AI21-- I know I'm over way over time--

**[15:24](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=924s)** is basically, we offer a suite for enterprises like a toolkit that helps them given an agent, an existing agent, no matter what framework or runtime or what models this agent is operating with, we basically help companies optimize their agents in production, aligning with their production traffic so it can continuously evolve and get to the best price performance and according to the customer's preferences. So to conclude about why we need an automated way to optimize these agents, we want to make them efficient. We want to make this an efficient process.

**[16:14](https://www.youtube.com/watch?v=gVT0h3xUY3M&t=974s)** We want to make it observable so people will be able to see the different tradeoffs and select from them. And we want this to be future-proof. So when a new model comes in or when the distribution shifts, it's very easy to adjust our agents and make them performant in production. You're more than welcome to check our research in this area. In our blog post, we post every few weeks about new discovery around agent optimization. And I thank you very much for your time. Thank you. [APPLAUSE]
