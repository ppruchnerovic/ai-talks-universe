---
id: 0eEuAu1zEsU
title: "Ben Athiwaratkun - Unified Orchestration System for Verifier-Free Evolution"
slug: ben-athiwaratkun-unified-orchestration-system-for-verifier
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Ben Athiwaratkun"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:50:21Z
video_id: 0eEuAu1zEsU
youtube_url: https://www.youtube.com/watch?v=0eEuAu1zEsU
tags: []
transcript: true
---

# Ben Athiwaratkun - Unified Orchestration System for Verifier-Free Evolution

**Ben Athiwaratkun**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=0eEuAu1zEsU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*576 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=2s)** BEN ATHIWARATKUN: Thank you. So today, I'll be talking about Squeeze Evolve, our approach for unified multimodal orchestration system for verifier-free evolution with applications for scientific discovery. So let's take a look at the components for scientific discovery. This one is taken from SkyDiscover. So there are four distinct components. The first one is context builder. The context builder's goal is to provide problem context as well as injecting ideas, guidance, reflections of previous mistakes and success into the prompt.

**[0:53](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=53s)** And the prompt is given to a solution generator, in this case LLM, where it has access to environments such as execution or ability to look up the web. And solutions are passed to evaluator, where evaluator's goal is to provide scores, provide logs, provide feedback or necessary artifacts. And these solutions and metadata are passed to a solution selector, which selects sample solutions to be passed to context builders, so that we can use it in the next loop. Prior methods for discovery frameworks

**[1:45](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=105s)** often require external evaluator. So in the domain of physical science, for example, evaluators can be costly and time-consuming. So our goal is to answer the question of, what would be the upper bound of evolution system without verification in the loop? And can we also reduce costs? One of the problems for evolution system is degradation of solutions. Long story short, if we use a single model

**[2:34](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=154s)** to perform evolution, it's often the case degrading the performance, because there's only so much entropy and only so much creativeness in a single model. So our solution is to use multiple models to tackle this diversity problem. So in this case, multiple generations are selected from previous generations and current generations, and assigned probability fitness scores. In this case, we used log token-- sorry, token log probabilities or diversities of solutions as a fitness function. And in order to increase diversity, we passed the difficult solutions to expensive models,

**[3:27](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=207s)** similar to single-model framework, whereas if we identify the solutions as being easy enough to evaluate and combine, we pass them to a cheaper model. And in this case, we are able to increase diversity and also increase cost effectiveness. So the result here shows that for the full pipeline with 10 evolution steps, with Gemini 3.1 Pro, the accuracy on ARC-AGI is 97.5%. This is with 10 steps. And cost is around $7 per task. But in the scenario where we use a cheap model in the mix, which

**[4:18](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=258s)** is the Gemini 3.0 Flash, we're able to retain the same accuracy with only two evolution steps, while achieve cost savings. The dollar per task is around $5.9. Another interesting observation is that in the vision-based task, not having to use the vision component for the aggregator stage also allow us to increase the cost effectiveness significantly. For example, in the red curve here, where we use a strong multimodal model, the performance gets quite high.

**[5:05](https://www.youtube.com/watch?v=0eEuAu1zEsU&t=305s)** But also, notice that the cumulative dollar per problem is also proportionally high. But in the Squeeze Evolve method, where we use a combination of powerful model as well as a cheaper tier model, we're able to reduce the cost significantly. And in the heterogeneous case, we're able to outperform the single-model scenario. So we're very excited to share this. And this work has been integrated into NVIDIA Dynamo. Huge shout out to NVIDIA. And also, we have Claude Code plugin available. Yeah. Thank you so much.
