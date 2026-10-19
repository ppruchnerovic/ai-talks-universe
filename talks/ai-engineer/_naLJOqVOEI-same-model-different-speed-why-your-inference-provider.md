---
id: _naLJOqVOEI
title: "Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI"
slug: same-model-different-speed-why-your-inference-provider
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 13
published_at: 2026-10-11T19:30:05Z
video_id: _naLJOqVOEI
url: https://www.youtube.com/watch?v=_naLJOqVOEI
youtube_url: https://www.youtube.com/watch?v=_naLJOqVOEI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "LLM inference", "inference optimization", "FriendliAI", "open weight models", "GLM", "prefix caching", "KV cache", "speculative decoding", "LLM latency", "coding agents", "Kilo Code", "GPU", "AI infrastructure", "Yunmo Koo", "AI Engineer"]
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Same Model, Different Speed: Why Your Inference Provider Matters — FriendliAI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#LLM inference` `#inference optimization` `#FriendliAI` `#open weight models` `#GLM` `#prefix caching` `#KV cache` `#speculative decoding` `#LLM latency` `#coding agents` `#Kilo Code` `#GPU` `#AI infrastructure` `#Yunmo Koo` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=_naLJOqVOEI) · [Conference site](https://www.ai.engineer/)

## Description

Open-weight models are good enough now. The question is who can run them fast and reliably.

Yunmo Koo, founding engineer at FriendliAI, argues that open-weight models like GLM 5.2 and MiniMax M3 now compete with the best proprietary models. He shows GLM 5.2 and Claude Opus 4.8 building similar tower defense games from one prompt, with GLM 5.2 more than 5.6x cheaper. Then he runs the same model and the same coding agent on two providers: FriendliAI builds a Candy Crush-style game in about two minutes, the other takes more than three. He explains where the gap comes from: prefix caching with cache-aware routing and a GPU, CPU and NVMe cache hierarchy for long, repetitive agent inputs, plus hybrid speculative decoding that adapts to live traffic. He also covers why reliability matters for agents (one failed call can sink a whole run) and shares Kilo Code's results of up to 7x faster responses with fewer errors.

In this talk:
• Why open-weight models are now good enough for many workloads
• Why the same model feels different on different providers
• Prefix caching, cache-aware routing and a tiered KV cache
• Hybrid speculative decoding and why reliability is part of speed

SPEAKER
Yunmo Koo, Founding Engineer, FriendliAI

LINKS
FriendliAI: https://friendli.ai
Kilo Code case study: https://friendli.ai/customers/kilo

CHAPTERS
0:00 Intro
0:40 Open vs closed models
1:09 Open weights crossed the threshold
2:24 GLM 5.2 vs Opus: a tower defense game
2:49 5.6x cheaper
3:09 Provider quality
3:53 Same model, different provider
4:33 It's the whole stack
5:28 Long, repetitive agent inputs
6:27 Cache-aware routing
6:47 A cache hierarchy
7:37 Speculative decoding
9:06 Hybrid, self-improving speculation
9:41 Reliability is part of speed
11:06 Test your own workload
11:45 Kilo Code: up to 7x faster

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*1,810 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=_naLJOqVOEI&t=1s)** [music] All right, let's get started. So, hello everyone. My name is Yun Mo. I'm a founding engineer at Friendly AI uh building inference engine with our team to optimize inference performance. Uh so today I'm going to talk about how we built the fast and reliable inference API for frontier openweight models. So oh thank you. Okay so before we dive in let's do a quick show of hands. So who here uses closed weight frontier models like GPT or cloud?

**[0:51](https://www.youtube.com/watch?v=_naLJOqVOEI&t=51s)** Okay most of you are already using it. And then who here mainly use openweight models? Yeah. Yeah. Fewer than the closed weight models. So personally I recently using a mix of both these days but I'm gradually migrating more of my workload to open weight models. The reason is that open weight models uh have crossed the threshold these days. For example, encoding, reasoning, and agentic benchmarks. Models like GLM 5.2 are competing in the same tier as the leading proprietary models. So, as you can see from this code arena leaderboard, uh GLM 5.2 is ranked even higher than code opus 4.8. So, it is right uh below the cloud fable 5. So,

**[1:42](https://www.youtube.com/watch?v=_naLJOqVOEI&t=102s)** similarly across various coding terminal and tool use benchmarks uh GM 5.2 2 and minmax M3 shows strong results. So the question is no longer only whether open weight models are good enough for many workloads now they are. So the next question is how fast and reliably we can run them in production. So benchmark numbers alone uh don't really give a clear sense of how well things actually works. So instead I ran a a simple hands-on experiment to see how these models actually perform. So I asked both GLM 5.2 and OPUS 4.8 uh 4.8 to build a tower defense game like this. So as you can see both models produce working implementation with similar

**[2:31](https://www.youtube.com/watch?v=_naLJOqVOEI&t=151s)** structure and quality. So both one has a map and the turrets are shooting the the enemies within the range. So yeah, both looks pretty great considering I made it with a a single prompt. But when we look at a cost, the difference becomes very clear. So GM 5.2 was more than 5.6 times cheaper for this task. And in agent SL style workflows where you need to iterate multiple times, the the the gap compounds quickly. So this is not just about motor quality anymore. It is about what you can afford to run at scale. So after the model quality and cost, the next next question is provider quality and provider quality is really about performance. So even if the model

**[3:19](https://www.youtube.com/watch?v=_naLJOqVOEI&t=199s)** weights are the same, latency, throughput and reliability can vary significantly depending on where you run it. Uh so this one has a open router snapshot which shows that uh these differences are measurable. So if you're building an AI product, you should not only ask which model to use, but you should also ask which providers gives you the best performance, reliability, and pricing. So I will show you another example. So here I use the same model 5.2 and the same coding agent workflow. So the task is to build a simple Candy Crush style mobile game which we call moto crush. So when you see this, the left side is friendly AI. it generates the the the game within two minutes. Another

**[4:07](https://www.youtube.com/watch?v=_naLJOqVOEI&t=247s)** provider needs uh more than three minutes. So the model is the same. The agent app is the same but the provider was different. So model developer tools and coding agent this is this exper this is the experience that users actually feels. So from this simple example we saw that even with the same model and the same task the experience can feel very different depending on the provider. The difference comes from the entire inference tech. So the model architecture cache system routing policy quantization strategy GPU corners all those things come together should shape what the developer actually experiences. So this is the uh core of friendly AI's value. So we are not just exposing a

**[4:55](https://www.youtube.com/watch?v=_naLJOqVOEI&t=295s)** model API be uh so friendly AI is built as a fullstack inference engine for geni models. This matters uh because fast and reliable inference is not just one optimization. It is batching scheduling quantization spec decoding and connors all all everything should work together. So let me briefly explain uh how we built that and how we make uh the inference performance uh to the cutting edge level. So in the modern agent applications inputs are often very long. It easily exceeds uh 10k tokens while outputs are relatively short and more importantly a large portion of the inputs are repeated

**[5:43](https://www.youtube.com/watch?v=_naLJOqVOEI&t=343s)** across requests. In many real workloads like 50% to 80 to 90% of the tokens are identical across different requests. So from a system perspective this means uh most of the compute cost is in the prefill stage where the model processes the entire inputs and build a KB cache. So if we recompuse this share prefix every time you're wasting both latency and GPU cycles. So when a new reccast share a a prefix with the previous one, we can reuse those tensor and skip the corresponding prefer computation and directly reduce the TTFT and uh we can avoid recmp computing large chunk of the input and but however making this work at scale requires two key ch uh mechanisms. So first one is cache aware

**[6:32](https://www.youtube.com/watch?v=_naLJOqVOEI&t=392s)** routing. So in the distributed system KB cache is not centralized. It lives on individual replicas. So the router must send incoming request to the replica that already holds the relevant prefix in its cache otherwise we re we lose the benefit of reuse. The second thing is cache hierarchy. So KB cache is extremely memory intensive for large models and long context. KB cache size can exceed model weights. So and as you know GPU VRAM is the fastest but there's also very limited resources. So uh we treat cache as a hierarchy like hot cache stays in GPU memory warm cachees in uh CPU RAM and quarter cache can be offloaded to MVME or uh the disk spaces. The system dynamically offloads less

**[7:22](https://www.youtube.com/watch?v=_naLJOqVOEI&t=442s)** used blocks and prep them when uh when they need it. So by combining cash aware routing and hierarchical memory management we significantly reduce the prefix cost lower TTFT and making long context agent workload much more efficient. So the next thing is interactive speed. So standard auto reggressive decoding it generates one tokens per four pass that makes decode uh inherently a sequenture and during the decode the GPU is often underutilized and speculative decoding changes the shape of this problem. So instead of generating one token and stopping it proposes multiple candidates tokens ahead then the target model validates those uh candidates in a single pass and if the tokens are

**[8:11](https://www.youtube.com/watch?v=_naLJOqVOEI&t=491s)** accepted they are free. So this improves time per output token uh without changing models uh output quality and there are different ways to draft candidates. So one way is modelbased speculation. It uses a small draft model to predict the future tokens and then and the benefit of it is it can achieve higher acceptance rate but the cost is the uh extra compute and another method is model free speculation. It uses pattern from a prompt or prior output. So it has lower overhead but it works best only when the output resembles the existing context. So the important part is the trade-off. So speculation can

**[9:00](https://www.youtube.com/watch?v=_naLJOqVOEI&t=540s)** improve per request latency but validation as overhead to the batch. So the best strategy is not static. And at friendly AI we take a hybrid approach. So the runtime can dynamically select between model based and model speculation uh based on the workload and request uh characteristic. So we also think about speculation as something we can improve over time. So with self-evolving speculation uh draft model can adapt based on the real serving traffic. So the speculator continuously improves its prediction of the workload actually running in the in your uh production. So the next thing I want to mention is reliability. So speed alone is not enough. So production AI application uh

**[9:51](https://www.youtube.com/watch?v=_naLJOqVOEI&t=591s)** reliability is part of speed. So if an API is fast in average but frequently hits timeout like five 5xx error 4 to9 rate limit or fail or that kind of failure the user experiences uh still breaks. So this becomes even more important for agentic workloads. As you know agent may need multiple model cores to complete one task and if just one call phase in the middle the entire workflow can be invalidated. So that's why we do not optimize only for the latency or throughput. We optimize the full API experiences uh including the error rate, uptime, all those things together. And this open AAI snapshot for GLM 5.1 pro uh shows that friendly AI is

**[10:41](https://www.youtube.com/watch?v=_naLJOqVOEI&t=641s)** not only the fast but it's also highly reliable with over 99.9% up time. So what I want to say is many inference provider out here of course in this menu as well they will tell you that they are fast and some point of them they are but on cert on certain benchmark under certain condition but for your application the only benchmark that really matters is your own workload. So your prompt your token length your traffic patterns and your latency expectation. So our recommendation is simple. So please bring your workload to us and test a poor experience with us in terms of like speed, reliability, cost and quality. And of course um we build

**[11:32](https://www.youtube.com/watch?v=_naLJOqVOEI&t=692s)** our inference service for exactly these production workloads and we and we believe that we can give you the best experience. So we have a boost in this venue. So bring your hardest problem to us and let's solve it together. So to close I want to share a testimonial from one of our customer is a kilo code. So kilo code is one of the largest coding agent platform processing like several trillions of tokens every week. So they have tested many different inference providers over past years and in their split test for GLM models they were especially impressed by friendly AI. So compared with many other inference provider, friendly AI was over like seven times faster and had a sign significantly lower error rate. So I

**[12:21](https://www.youtube.com/watch?v=_naLJOqVOEI&t=741s)** believe you can get the same kind of experience with friendly AI. So if you're building your frontier open models, building with your frontier open models, come try them on friendly AI and bring your real workload and let us show you what fast and reliable inference can do. So this is the end of my talk and if you have any question feel free to ask. Thank you. >> [music]
