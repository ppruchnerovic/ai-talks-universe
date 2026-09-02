---
id: sgifUs3JSac
title: "Woosuk Kwon - vLLM: Building Open and Efficient Inference for Agents"
slug: woosuk-kwon-vllm-building-open-and-efficient-inference-for
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Woosuk Kwon"]
channel: "Berkeley RDI"
duration_min: 16
published_at: 2026-08-12T01:42:37Z
video_id: sgifUs3JSac
url: https://www.youtube.com/watch?v=sgifUs3JSac
youtube_url: https://www.youtube.com/watch?v=sgifUs3JSac
tags: []
transcript: true
---

# Woosuk Kwon - vLLM: Building Open and Efficient Inference for Agents

**Woosuk Kwon**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=sgifUs3JSac) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,978 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=sgifUs3JSac&t=2s)** WOOSUK KWON: Thanks for joining today. I'm Woosuk. I'm a co-creator of vLLM and also co-founder of Inferact, a startup built and run vLLM. Today, I wanted to talk about what agents demand for the inference tech and how we are evolving vLLM, like open source inference stack, to meet these demands. Let's get started. So key intro for everyone new-- vLLM is an open-source LLM inference engine to make LLM inference efficient and effortless. It started about three years ago here at UC Berkeley during my PhD, and has been growing rapidly ever since, even now. And we hit 88k GitHub stars, I think, pretty recently. Importantly, this is a very highly collaborative project

**[0:50](https://www.youtube.com/watch?v=sgifUs3JSac&t=50s)** across academia and industry with major contributors including Red Hat, NVIDIA, AMD, Google, Moonshot, and us at Inferact. And it's also being widely deployed in industry for production inference. There are two main ways to use vLLM. I'll go through them very quickly. The first is the LLM class, which is a Python interface for offline batch inference. You give it a Hugging Face model name, and you call the generate. And that's it. So vLLM automatically handles model loading, optimization, scheduling and memory management under the hood so that you don't need to care about it, and utilizing GPUs. And it generates a text completion of the prompts and returns to you.

**[1:40](https://www.youtube.com/watch?v=sgifUs3JSac&t=100s)** The second is online serving vLLM serve. This is a single command that you can get a OpenAI compatible endpoint from. And obviously, we also support Anthropic APIs, too. Any agent framework that speaks to the OpenAI or Anthropic API can also work out of the box, since the API layer is pretty standard. So that's how you use vLLM in the first place. But as you can see, the API itself is pretty much similar to the few years ago. So it actually didn't really change that much from for agents. What has changed a lot for agent is everything underneath it. So yeah, specifically, at a high level,

**[2:30](https://www.youtube.com/watch?v=sgifUs3JSac&t=150s)** agents change the inference problem along three axes. First is large models. The frontier agent models like Kimi-K3, DeepSeek V4 are trillion parameters MOE. And that first is all to get serious about model parallelism. Basically, it gave us a lot of opportunities for us to parallelize the model in many creative ways with different trade-offs. I'll talk about it in more detail later. A second is long context. Agent sessions run for hundreds of turns, up to a million tokens. And the context only grows over a session. So managing KV cache of the previous turns is very important for inference performance.

**[3:20](https://www.youtube.com/watch?v=sgifUs3JSac&t=200s)** And we definitely need to ensure that the inference framework is not recomputing any of the tokens in the previous turn because otherwise, it will be a lot of recomputation and a lot of waste of compute. A third is enormous token demand. Now that agents are getting really, really smart and so capable, so that there are actually now near-infinite demand, now near-infinite places to deploy it. So the demand is effectively unbounded. It's growing faster than the GPU supply. So the inference engine and inference serving has to adapt to it. And our solution to this is to basically enable this efficient inference for a more diverse hardware backends

**[4:12](https://www.youtube.com/watch?v=sgifUs3JSac&t=252s)** so that we can utilize all available compute to generate tokens. Let's get into more details. Yeah, let's start with parallelism. So to efficiently serve such large models-- vLLM today supports mainly seven different types of parallelism, including tensor, pipeline, data, experts, sequence parallelism, and two different kinds of context parallelism. You may recognize some of those from the training world. vLLM supports them all, and plus the ones that don't exist in the training, like decode context parallelism, which is parallelism around the KV cache. As a general-purpose engine, vLLM efficiently implements all of these parallelism

**[5:00](https://www.youtube.com/watch?v=sgifUs3JSac&t=300s)** and also mixture of them. However, we found that that's not enough. The important thing is that these parallelisms need to be properly selected and tuned. For the target model architecture, the target cluster setup, and also the target workload shape, there's no universal winner or there is no universal solution. Let me show you what this tuning looks like in a for real model. So this is like DeepSeek V4 running Prefill of it on B200 GPUs in the desegregated serving setup. So these set of GPUs only perform prefill. Basically, the most straightforward way

**[5:48](https://www.youtube.com/watch?v=sgifUs3JSac&t=348s)** to deploy the model, like DeepSeek model, for prefill on this GPU cluster is just using eight-way tensor parallelism. That's the most standard and simplest way to do it. However, the winning configuration is pretty much different. In this particular workload setup, it was two-way tensor parallel times eight-way-- two-way pipeline parallel times eight-way tensor parallel plus sequence parallelism and expert parallelism deployed across 16 GPUs for each model replica. And we found that this gets much lower TTFT, basically, the latency on the first token. It also much higher throughput per GPU

**[6:38](https://www.youtube.com/watch?v=sgifUs3JSac&t=398s)** compared to this straightforward single-host eight-way TP baseline. The reason being is-- yeah, it's actually pretty much complicated, so I'm not going into much details. But the reason being is pipeline parallelism is enabling the parallelism between different chunks in the long prefill. Sequence parallelism enables more communication and computation overlap. And expert parallelism gives a better gem shapes, better matrix multiplication shapes compared to the eight-way tensor parallelism. So the takeaway is that basically, there's no winner. And also, basically these [INAUDIBLE] models make this model parallelism and sharding a necessity. And there are many different ways to do it.

**[7:26](https://www.youtube.com/watch?v=sgifUs3JSac&t=446s)** And depending on how you choose and tune the parallelism degree, the performance better varies a lot. And basically, in this agent work-- in this agent era, we need to have the right like insight and performance model to set the-- to configure this in the correct way. And vLLM basically provides the common substrate that you can basically play with all these different parallelism. So the second is like KV cache. So speaking of it, so the one very critical characteristic of the modern LLMs are that they are basically hybrid models. They are basically hybrid in the sense

**[8:13](https://www.youtube.com/watch?v=sgifUs3JSac&t=493s)** that they're interleaving the regular full attention with some other more efficient attention mechanisms, like sliding window or linear attention, such as Kimi delta attention. And this is basically the thing that makes the 1 million context lengths feasible, because global attention itself is-- it takes too much memory if you want to really go to 1 million context. However, in theory, this is very efficient. But in practice, this creates a lot of real systems challenge. Basically these layers with different attention types have completely different memory behavior. Full attention-- the KV cache full attention grows linearly with the context, while linear attention, like KDA

**[9:03](https://www.youtube.com/watch?v=sgifUs3JSac&t=543s)** keeps a fixed size state per sequence, regardless of the actual context lengths. So how should we carve up the GPU memory between them is the real-- one of the important systems question. The straightforward solution or answer to this question is static partitioning-- reserve x percentage for full attention, y percentage for the rest, things like that. This works. But the problem is that the optimal split between the two depends on the batch size and context length, which is pretty dynamic over time during inference. So the solution in vLLM is dynamic partitioning, which is basically using one shared memory

**[9:52](https://www.youtube.com/watch?v=sgifUs3JSac&t=592s)** pool for GPU memory. And each attention type with different memory behavior gets its own allocator drawing from the shared memory pool. So yeah, in a sense, the full attention allocator-- like, recast to this shared memory pool the specific number of tokens, while in the KDA allocator, because it's a linear attention, allocates the one giant block for the entire sequence. And we have a logic to dynamically share the same memory space between the two. This is also pretty much detail, so I'm not going to too deep. But basically, this is one critical feature in vLLM that allows you to not worry about how to handle these different types of attention,

**[10:42](https://www.youtube.com/watch?v=sgifUs3JSac&t=642s)** and the memory split between and the-- vLLM basically automatically rebalances the memory space between the two so that no GPU memory is wasted. Regarding KV cache, also, another thing is that important thing is managing this KV cache within the GPU memory space isn't enough. Especially, the agent sessions are pretty long-lived and also very intermittent, which means basically the model generates, and then generates some output tokens, and then waits like for two calls or sometimes for human response. And then it basically continues. And during those waits, the KV cache is somehow stored in some area.

**[11:33](https://www.youtube.com/watch?v=sgifUs3JSac&t=693s)** It could be stored in GPU memory. It could be stored in some other memory. To store this KV cache unused at the moment, we basically use these concept of KV connector. This basically allows to leave this idle KV cache-- and store this idle KV cache to external memory like CPU, memory or disc, and bring it back when it's needed. And here, basically, actually speaking, basically, we did a lot of efforts to design this abstraction and make sure it is well, working with third-party libraries like Mooncake and also, it is well working with other KV transfer mechanism

**[12:23](https://www.youtube.com/watch?v=sgifUs3JSac&t=743s)** like prefill desegregation. The prefill desegregation case, the movement of KV cache is pretty dynamic and complex because it needs to move between prefill instance to decode instance, prefill instance to the distributed KV storage pool, like Mooncake, and things like that. And we basically set up infra to efficiently handle this. So that, again, in the money term, agent sessions, we never recompute-- as long as the storage allows, we never recompute the tokens in the previous case, in the previous turns. The last part is hardware. So basically, we believe the economics of tokens is flipping. So as models get smarter and more intelligent,

**[13:14](https://www.youtube.com/watch?v=sgifUs3JSac&t=794s)** the value of a token far exceeds the cost of generating it. So therefore, naturally the demand is exploding. And we're witnessing that. And honestly, there are not enough GPUs in the world to serve it. So the question becomes, can we use all the available compute on Earth to generate tokens efficiently? And vLLM basically tries to-- aims to answer the question. To achieve the goal, we support more than 10 hardware backends today. Obviously, the NVIDIA GPU is our major focus, but we also work on Google TPU, AMD GPU, and many other hardware chips from the industry.

**[14:03](https://www.youtube.com/watch?v=sgifUs3JSac&t=843s)** And they basically have the plugin structure to vLLM to share the core part of vLLM while they're customizing some specific parts for their hardware backends. And obviously, this makes more sense because the API and the inference space is pretty much standardized, but you can still use the same like OpenAI or Anthropic API with different hardware under the hood generating the tokens. For the sake of time, I will probably need to skip the slides. But basically, we got a lot of lessons from supporting this hardware and we're actively working on it. But the TLDR is that bringing up this new hardware and making it efficiently supporting the new models is, I think, getting better

**[14:52](https://www.youtube.com/watch?v=sgifUs3JSac&t=892s)** because of coding agents. But on the other side, it also still requires rethinking the entire inference stack from ground up. So yeah, we're actively working on it. And for summary, the agentic era basically stresses the inference on three axis, and vLLM answers each of the one, like here, larger models with workload-aware model parallelism, long context with a dynamic and hierarchical KV cache, and exploding token demand with diverse hardware backends. And everything I showed you today is open source, so please come join us with different places. Thank you. [APPLAUSE]
