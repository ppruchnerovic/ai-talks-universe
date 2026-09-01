---
id: msNGcO_kdmQ
title: "Priya Ponnapalli - Building Reliable Agents: An Evals First Approach"
slug: priya-ponnapalli-building-reliable-agents-an-evals-first
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Priya Ponnapalli"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T02:11:37Z
video_id: msNGcO_kdmQ
youtube_url: https://www.youtube.com/watch?v=msNGcO_kdmQ
tags: []
transcript: true
---

# Priya Ponnapalli - Building Reliable Agents: An Evals First Approach

**Priya Ponnapalli**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=msNGcO_kdmQ) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,451 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=1s)** PRIYA PONNAPALLI: Good afternoon, everyone. I'm Priya Ponnapalli. I'm SVP of Engineering at Scale AI. Scale's mission is to build reliable AI systems for some of the world's most important decisions. And this is a hard problem. You have technology that is inherently stochastic, and you are trying to deliver, deterministic business outcomes using this. So Scale's approach to solving this is an eval's first one. So here's where our approach comes from. So 90% of Frontier Labs use scales data engine. And we have been building AI applications for governments including the US Department of Defense and the Defense Innovation Unit, as well as

**[0:50](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=50s)** for many enterprises in regulated industries, such as health care, finance, and telco. And unlike consumer and prosumer agents, which you are using for day-to-day productivity tasks, reliability is really key in these enterprise agents and these regulated industries. For example, we are working with the Mayo Clinic on bringing agents to improve patient care. And here, the goal is literally saving lives. So there's no room for error. And these agents have to be extremely rigorous, robust, and well-tested. And this is an area where mostly right just isn't good enough. There was an MIT study that was cited in this morning's talk

**[1:47](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=107s)** about how 95% of AI pilots do not end up going to production. So in an enterprise setting, if your agent is wrong, even 5% of the time, that's a liability. This could be like a wrong number on a customer invoice. It could be a misstatement in a compliance filing. A bad write to a production database on which thousands of downstream systems depend on. And it's just not acceptable. So at Scale, we have a framework for building reliable agents. And we hold every production agent to eight engineering gates. These span everything from ensuring data privacy, ensuring the right access control

**[2:36](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=156s)** frameworks, with the right [INAUDIBLE] in place. But the area I'm going to dive into today in this talk is on rigorous evals. So unlike a model benchmarking exercise, there's a shift in how you evaluate enterprise agents, which is really a system reliability capability. An agent is unfolding over time. It's interacting in a real environment. You're not just evaluating a model and its output text anymore. You have to evaluate an end-to-end system. This includes the model, the prompts, the tools, the orchestration and the environment, which in an enterprise setting, could include production APIs,

**[3:25](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=205s)** knowledge bases, various files, workflows, business workflows that are present at that enterprise. Then an important and useful distinction is understanding which components can be tuned and which ones are given. And good eval design keeps these separate. So here's what's at the core of our evaluation framework. We have a layered evaluation framework, where we keep the business alignment, the black box evaluation and debuggability separate, but still causally linked. So at L0, we've got the business outcomes. These are our north star KPIs. This is the value that the agent actually drives.

**[4:15](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=255s)** This could be the resolution rate, cost per ticket, analyst time saved. At the L1 level is the task success. Here, we treat the agent as a black box, and ask if it successfully completed the task. Examples of this are, was the refund issued to the correct amount? Is the case record and the correct final state? So this is almost the operational center of the agent evaluation and what we iterate on try different approaches and look at changes to improve the score. Going a level deeper is the level 2 component evals. This is where we're opening up the black box and looking at the subtasks. So you have things like extracting relevant facts,

**[5:05](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=305s)** choosing the right fields, producing the right record changes. And finally, level 3 are the diagnostics. This is what is needed for debugging and optimization. This is the why behind why the level 2 and level 1 metrics may be failing. And all of these form a chain. So a common failure mode is teams might end up spending more time optimizing on the level 3 and level 2 diagnostics and components, while not ensuring that level 1 is also improving. So now, let's take a look at this framework in action in some real-world examples. So Scale is helping a top oil company with designing oil wells better. And this includes the casing design.

**[5:56](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=356s)** So casing is the steel pipe that goes around the well. And the process for designing these casings is often a multi-week hop where an engineer is running hundreds of simulations. They're referring many standards that are buried in PDFs and libraries. So our approach to designing this agent has two key parts. One is a deterministic core where the engineer is still in charge, running all these simulations using trusted physics-based simulators. These results are checked deterministically against company standards. And the engineer makes the final call on reviewing and approving safely designed wells. The second is a casing design agent,

**[6:47](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=407s)** which is following along with the engineer, extracting all the right context from hundreds of simulations. These are all grounded in the agent's interaction. The engineer is allowed to ask questions, which are all answered by the agent with cloth level citations. And the agent finally designs the wells design doc. This is also known as the basis of design. And it's worth calling out that the agent never computes any number or drives any workflow. So by design, numerical fidelity is 100%. So the eval exercise boils down to how well does the casing agent answer the engineers questions and generate complete and correct BODs? So to evaluate how our agent is doing, we apply the same four-layered eval framework

**[7:38](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=458s)** where L0 is the number of annual BODs that have been signed off by the SMEs. L1 is, does the agent design and answer complete correct and review ready docs? L2 is focused on retrieval and context management. And L3 is around terminology grounding, fidelity, and recall. So we build evals with our SMEs. We calibrate the graders. SMEs are often bottlenecked on time. So we synthetically expand their SME templates, and then have them validate the additional data. The climb on L1 correctness. We were able to get the terminology precision from 83 to 100%. And the claims precision from 68 to 90%.

**[8:28](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=508s)** This got the confidence of the customer's engineers, the wells designs engineers. And we're now in a limited production rollout where we're going to collect additional production traces, score them, evolve the eval sets, which needs to be a living asset, and improve the agent from here. So worth noting that evals are living assets, in my opinion. They are the most durable asset. You can always swap out the model, various aspects of how the agent is designed and test against this eval suite. And this is truly like the IP mode of where our customers invest in and what helps them keep up and ride on top of the wave of foundation model improvements.

**[9:16](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=556s)** Another example, this is our work with a top for professional services and accounting firm. This is where we built a financial due diligence agent, which helps analysts get to the same human-validated insights, which was taking them four to six weeks down to two days. So again, it's the same eval framework. We define L0 as the total time to human validated insights. We've got all the layers. We've built the evals. We've improved on the L1 hill-climb and improved on the L1 correctness. This is also going to production roll out, where we learn from every run. And oftentimes, having sufficient eval data is one of the biggest bottlenecks.

**[10:04](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=604s)** So these limited production rollouts are a great opportunity to collect additional data and evolve your eval suite. So for every agent built at Scale, we hold an eval design review. We have a forward deployed engineering team that partners with all our enterprises as well as government agencies and building them. This is the performance maturity matrix we used as an eval scorecard for every agent. And we don't ship until the scorecard is all green. So wrapping up with some key principles. I'll call out a few. You are evaluating systems, not just models. Use hybrid graders. So deterministic wherever possible. Model-based where necessary. And human review for calibrations and high stakes

**[10:52](https://www.youtube.com/watch?v=msNGcO_kdmQ&t=652s)** use cases. And treat evals as living assets. Grow them over time. This is your asset. And evals first is how mostly right becomes production-ready. So if you are in this space, I would love to compare notes. My email is up there. Thank you all. [APPLAUSE]
