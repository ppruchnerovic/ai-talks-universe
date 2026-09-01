---
id: fWZoiBsY2CY
title: "Shiva Kasiviswanthan - Toward Adaptive Agent Frameworks"
slug: shiva-kasiviswanthan-toward-adaptive-agent-frameworks
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Shiva Kasiviswanthan"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T01:53:04Z
video_id: fWZoiBsY2CY
url: https://www.youtube.com/watch?v=fWZoiBsY2CY
youtube_url: https://www.youtube.com/watch?v=fWZoiBsY2CY
tags: []
transcript: true
---

# Shiva Kasiviswanthan - Toward Adaptive Agent Frameworks

**Shiva Kasiviswanthan**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=fWZoiBsY2CY) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,007 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=1s)** SHIVA KASIVISWANTHAN: Good afternoon, everyone. My name is Shiva Kasiviswanthan, and I'm a principal applied scientist at AWS. Me and my team are working on developing AI agents for monitoring and observability for large scale cloud operations. And today in this talk, I'm going to share some broad research directions that we've been exploring to make agents more adaptive. So I think let me start with today's agents are already pretty capable. So we all know how good they are good at planning, tool execution, retrieving information, iterating over the solutions to solve complex tasks. But as these agents gets deployed in more mission critical applications, we, in AWS believe there are some critical research questions that need to be solved because they can be widely deployed.

**[0:48](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=48s)** And here are some of them that we have been exploring in our team. So first question that we've been exploring is this question of how should agents allocate computational resources? Imagine that you have a fixed computational budget and you want agents to best utilize that computational budget to solve the problem at hand. The second question is all along making agents reason better. So agents needs to be able to explore multiple precinct paths to make decisions in a more efficient fashion. And the third research question that we've been exploring is the question of how do we evolve agents over time? So the agents are not static pieces, but that continually adapt over time to make and learn how to solve the task over time better. So in this talk, I'm going to just focus on the first two tasks. But I'll just briefly end up with how

**[1:35](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=95s)** we are looking at the third problem at the end. So let me start with the direction 1. So this is the notion of budget aware adaptive execution. So today, if look at most agents, they have a fixed execution policy that you define using a prompt or some other local heuristic. I guess our goal is to make these agents learn these execution policies. So agents can learn over time these execution policy and then they decide how do these policies are executed. And then you also have a notion of a computational budget. You want the agents to work best under some computational budget. So abstractly, you can think of this as a problem where you have some context, agent has some context, and it is to decide the best next action to do. The action could be like retrieve information,

**[2:22](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=142s)** use a tool, verify the results, update memory, whatever. There is some action space. And the important constraint is that there is notion of budget. So there is a budget that the agent has and it has to respect that budget while executing these tools. So again, I mean, if you think of this like a little bit more like I think this can be phrased in terms of a formulation, we can rephrase this as a constrained Markov decision process. And we've been using this framework to learn these policies. So again, the goal is to maximize some kind of expected utility under some notion of subjective some computational budget. Again, the budget could come from latency cost, token, whatever you want to think of some notion of budget. And does it work? The answer is, yeah.

**[3:09](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=189s)** We've have some success in implementing this. So what we've been shown that the plot on the right hand side shows these adaptive agents learning better execution policy than using a scalar reward model, which is commonly used in practice. The other plot on the left side is showing that it's also more sample efficient. So you're reaching the same competence using fewer iterations. So the amount of samples you need to get to some level of competence is significantly lower if you use these kind of adaptive execution policies-- if you learn these adaptive execution policies. OK. The second direction that I just briefly want to talk about is the notion of parallel reasoning. So today we have these agents or at least these models which are following a single reasoning path.

**[3:57](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=237s)** And we have been exploring ideas that allow models to explore multiple reasoning paths in parallel. So these parallel paths are kind of learned during training and not during inference time. And then they are coordinated to select one path. So the answer is one-- so there is some coordinated reasoning that happens at the end which takes these multiple reasoning paths and produces one answer. And again, we have been implementing these ideas and testing it on benchmarks. And like both our mathematical reasoning and coding benchmarks, we have been getting consistently good results. And these are some results on some maths and coding tasks. And you can see the results for pass one to pass k we have been getting better than very strong baselines. And especially the results are impressive on k equal to 1, which is like the one shot when you get one result out.

**[4:49](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=289s)** So maybe I'm almost out of time. So I just want to finish by going back to the research questions that I was trying to say. So we have been-- I just mentioned about this budget adaptive execution, where the goal is to learn an execution policy that's adaptive and best uses the constraints it has. And then the second question of parallel reasoning, where you're trying to generate agents to have multiple reasoning paths so that they explore multiple paths to solving the same problem. The third question that we have been also been focusing is this notion of continual model or agent adaptation. Again, the goal is to come up with principled post-training schemes that can adapt to new tasks. The main challenge there is to make sure that when you learn the new task, you don't forget what you learned previously. And we believe that solving these three research directions will help us to generate the next generation frontier agents.

**[5:40](https://www.youtube.com/watch?v=fWZoiBsY2CY&t=340s)** Thank you.
