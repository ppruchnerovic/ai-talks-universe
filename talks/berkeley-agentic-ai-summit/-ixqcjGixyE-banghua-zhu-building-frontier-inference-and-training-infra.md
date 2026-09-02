---
id: -ixqcjGixyE
title: "Banghua Zhu - Building Frontier Inference and Training Infra for Agent: A Case Study of SGLang and M"
slug: banghua-zhu-building-frontier-inference-and-training-infra
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Banghua Zhu"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T01:44:09Z
video_id: -ixqcjGixyE
url: https://www.youtube.com/watch?v=-ixqcjGixyE
youtube_url: https://www.youtube.com/watch?v=-ixqcjGixyE
tags: []
topics: ["Agents & orchestration", "Inference, serving & GPU infra"]
transcript: true
---

# Banghua Zhu - Building Frontier Inference and Training Infra for Agent: A Case Study of SGLang and M

**Banghua Zhu**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=-ixqcjGixyE) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,787 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=-ixqcjGixyE&t=2s)** BANGHUA ZHU: Today, I'm going to introduce SGLang and Miles, where we build the frontier AI infrastructure within RadixArk. So the mission of RadixArk is to make frontier-level AI infrastructure open and accessible to everyone. And to achieve that, we're building in open source right now where our inference engine in SGLang is adopted as a production inference engine all over the places. And then our recent RL framework models are also gradually picking up as a production frontier-level infra for post-training. A quick intro of SGLang. So we view that as a production grid open source inference engine, where SGLang itself is supporting language model and vision language model inference. And we also have SGLang Diffusion, a relatively newer project on image and video generation.

**[0:51](https://www.youtube.com/watch?v=-ixqcjGixyE&t=51s)** And then including also VLA and world model inference as well. And more recently, we have SGLang Omni, which is more targeted around ASR and TTS model, more around the audio side. So altogether, the entire SGLang ecosystem is more optimized for agentic workloads. And we provide really performant day-zero model support and also very broad hardware support, including NVIDIA, AMD, TPU, Trainium, Intel, and so on and so forth. We also have Miles, which is our enterprise grade reinforcement learning framework. So it's forked and coevolved with lime with more features on NVIDIA and AMD latest hardware. Slime is a project that AAAI built together with SGLang community for their GLM model series training.

**[1:42](https://www.youtube.com/watch?v=-ixqcjGixyE&t=102s)** So it has been battle tested on production training at very large scale. And for Miles, we also provide day-zero support for all the open models, including Kimi, GLM, like Inkling from Thinking Machine, like Nemotron from NVIDIA, et cetera. So at day-zero when the models are released, you can just directly use Miles for training and customization and use SGLang for inference. So most natively use SGLang as the rollout stage and then use NVIDIA's Megatron as a training stage for the best performance here. So today, SGLang models are already adopted widely by different enterprises and rising star companies like all the hardware companies, all the hyperscalers, enterprises, AI labs, especially new labs and also developer tools and new clouds are mostly widely adopting SGLang models in part of their infrastructure for inference and training.

**[2:35](https://www.youtube.com/watch?v=-ixqcjGixyE&t=155s)** There are also different ecosystem collaboration, where we work with Google Cloud very closely for improving their throughput for their internal inference stack. And also Cloudflare, IBM, xAI, Meta, they all use SGLang as a backend for their inference engine. So to us, 2026 is actually the year of agentic infrastructure. So for inference side, the demand is exploding. And actually, the challenges are very unique. And for training side, actually, every detail matters. It's still early, but everything needs to be done right so that you can train the model without hurting its generalization capability. So I'll briefly go over the challenges in both inference and training side with the introduction of agentic use cases.

**[3:24](https://www.youtube.com/watch?v=-ixqcjGixyE&t=204s)** So for agentic inference, the first thing people care about is high cache reuse. People see Deepseek V4 has a really low cache hit rate price. And such high cache reuse is actually very important to ensure that and also make sure you have really high cache hit rate and to reduce your entire cost of serving. And the second thing is that people are now moving towards trillion number of parameters of models. So how do you handle those large models? It's also bringing more and more challenges to open source stack. And of course, like for context window right now, one million contexts is already the norm. So there will need to be more optimization around super long contexts. So how does SGLang address those challenges? So first, for high cache reuse, we're

**[4:15](https://www.youtube.com/watch?v=-ixqcjGixyE&t=255s)** bringing two unique technology into this for SGLang. One is unified hybrid radix cache, which is designed for all the recent hybrid models, where you can make sure the prefix cache will run smoothly with all the hybrid models and new architectures introduced recently. And second is our HiCache design and system, which basically enable people to move the KV cache down from HBM to DRAM and even to your external storage so that there will be the most efficient way of handling KV cache in between different memory layers. So as a result, a concrete example of Qwen3-Coder, we get to greatly improve cache hit rate and also TTFT and throughput as well. The second challenge is large model scaling

**[5:03](https://www.youtube.com/watch?v=-ixqcjGixyE&t=303s)** when it comes to one trillion, three trillion, and an even larger models. So the standard technique definitely includes all the Five P standard parallelism like data parallelism, tensor, context, pipeline, export parallelism, et cetera. There are also newer parallelism strategy, Like DP attention, like TCP and PCP as well. And beyond that, there are also new combinations of deployment strategy. People start from colocate but then gradually move towards peripheral decode mode-- peripheral decode disaggregation mode for larger scale and more imbalanced peripheral decode deployment. And now for vision language model, there are also like m where you also disaggregate encoder in this case. And there are also different runtime optimizations

**[5:51](https://www.youtube.com/watch?v=-ixqcjGixyE&t=351s)** around SGLang, where there are different ways of supporting spec decoding, from Eagle to MTP to DFlash, and recently DSpark introduced by DeepSeek. There are also scheduling designs, including the overlap scheduler. And then our most recent Spec V2 for better support than native spec decoding speed-up in inference stage. And third and also perhaps very important context is also related to how people handle long context, especially when it comes to scaling to up to one million parameter. Or sorry, one million context window. So the first one is chunked pipeline parallelism, where we get to essentially-- instead of sending the whole prefill sequence at once, we get to chunk them

**[6:42](https://www.youtube.com/watch?v=-ixqcjGixyE&t=402s)** and chunk the entire long prompts into different smaller chunks and then process them in parallel. And the second thing is a different dimension of chunking or parallelism, where we split the sequences across GPUs for long context handling. There are also specifically sparse attention-related optimization we did with HiSparse, where we get to process the full KV with a hot buffer here, and then to ensure those sparse attention basically occupy less memory and result in much higher throughput in this case. So by combination of all the techniques and also all the fine tuning we did, this is a very concrete example

**[7:33](https://www.youtube.com/watch?v=-ixqcjGixyE&t=453s)** where at day zero, GLM 5.2 performance is already the best. And then over the time, we already are able to achieve over 2.2X improvement and achieving like up to 500 tokens per second per user in this stage. So in summary, SGLang has been keeping shaping the frontier capabilities in a fast, verified, and optimized fashion. We're the first to introduce a lot of new techniques in large production, including RadixAttention like spec decoding, PD disaggregation, like sparse attention, and also native RL support with Miles, and later, recently, DFlash, DSpark, and HiSparse as well. So next, I'll briefly mention about agentic training part. There are also a lot more challenges

**[8:24](https://www.youtube.com/watch?v=-ixqcjGixyE&t=504s)** introduced by long context agentic training. So one is that people now are looking at much more diverse environments. So it's not only about more tool cost and longer context, but also about some environments might be very hard to execute. And it might be even requiring lab experiments to get the reward signal. And the second is also about train-inference mismatch, which is a very popular topic in frontier labs these days, where if you have very large train-inference mismatch between different engine, then that will naturally and silently turn your RL to be more off policy and hurt your entire training run. And third is also people really care about throughput in your entire RL use cases. If you have higher throughput, that means you essentially get to iterate faster with your different RL experiments, and then you get more utilization with your GPU

**[9:13](https://www.youtube.com/watch?v=-ixqcjGixyE&t=553s)** as well. So to address the first challenge, we have been working very closely with most of the environment suppliers. And then Miles right now already natively support most of the open source RL environments, including Harbor, like OpenEnv, like Prime Intellect verifiers, and Daytona, and also NeMo Gym and also AgentEng, which is used by recent Kimi K post-training. For correctness, there has been one of the Miles biggest focus to ensure the train-inference mismatch will be alleviated. There are different ways to reduce that. One is just to introduce deterministic kernels in your inference engine, which is a prerequest to actually ensure zero-KL for the inference and train engine to make sure you get exact match in your inference and training

**[10:04](https://www.youtube.com/watch?v=-ixqcjGixyE&t=604s)** engine here. There are also things related to chat template fixing, where token-in-token-out to make sure that your multi-turn agentic chat templates will be all aligned, and then all the tokens will be matching the prior term's tokens without any train-inference mismatch as well. And third thing is related to algorithm fix. There have been [INAUDIBLE] routing replay and also truncated/masked importance sampling. Those are all techniques to enable stable training with large scale MOE for reinforcement learning stage. And fourth is also more engineering-driven. We have data support for most of the models, and they are all verified with our own training runs. Whenever we support new models like Inkling, like Kimi K3

**[10:52](https://www.youtube.com/watch?v=-ixqcjGixyE&t=652s)** training, we always have our own in-house training run to make sure the KL is controlled, the reward goes up so that people can use the framework directly without any concern. So lastly, for high throughput, SGLang and Miles are also keeping improving around that. We basically have much sophisticated and mature support for fully async RL, which get to compare with synchronous case. Basically, we get to overlap the time for rollout and training and also disaggregate those two settings to make sure those are making best use of your GPU. And also, we have very heavy investment in low precision training, where your rollout will be in a lower precision

**[11:42](https://www.youtube.com/watch?v=-ixqcjGixyE&t=702s)** and your training backend will be with some type of quantization-aware training. So that enables us to train with lower precision in rollout stage, where we natively support 8-bit and also 4-bit training. And in this case, we also recently worked with [INAUDIBLE] to support FP4 native rollout in RL stage without any performance loss. As a summary, we are producing and working on SGLang and Miles. And then we welcome everyone to contribute, work with us, and try that, provide feedback. So please also take a look at both projects, and then we'd love to hear more from you. Thank you.
