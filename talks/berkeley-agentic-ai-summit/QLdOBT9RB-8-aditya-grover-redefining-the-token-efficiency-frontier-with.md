---
id: QLdOBT9RB-8
title: "Aditya Grover - Redefining the Token Efficiency Frontier with Diffusion LLMs"
slug: aditya-grover-redefining-the-token-efficiency-frontier-with
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Aditya Grover"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-11T05:07:41Z
video_id: QLdOBT9RB-8
url: https://www.youtube.com/watch?v=QLdOBT9RB-8
youtube_url: https://www.youtube.com/watch?v=QLdOBT9RB-8
tags: []
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# Aditya Grover - Redefining the Token Efficiency Frontier with Diffusion LLMs

**Aditya Grover**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=QLdOBT9RB-8) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,671 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=2s)** ADITYA GROVER: All right. Hello everyone. My name is Aditya. I'm one of the co-founders and the CTO at Inception. And today, what I'm going to talk about is actually going to take a lot of elements from what we just heard in the previous talks into defining what I believe will be the new foundation for generative AI, something that's extremely fast and efficient and builds on ideas from diffusion. So to take a trip down memory lane, I think there have been a few fundamental advances that have defined what AI looks today and what I believe AI is going to look like in the future.

**[0:52](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=52s)** And at the heart of all of these advances is the idea that parallelization is a fundamental concept for computer science, fundamental concept for AI, and fundamental belief that will also guide towards the future. So if you think about the late 90s, The idea that we finally had hardware, which could execute a very simple but basic operation called matrix multiplication in parallel, was turned out to be the defining moment for what we see in today's generative AI world. A few years later, we realized that there's also something that could be done in terms of architectures when we had the transformer itself as the fundamental neural architecture, which could be used to train AI models in parallel. And this was how, from the world of RNNs and LSTMs, which

**[1:45](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=105s)** were fundamentally bottlenecked by how much they could learn with every dollar of compute spent, we went into a new era, where we could train massive language models using the transformer architecture. Within all of this, we also started thinking about how these ideas could then also be applied on the algorithm side. And that's where there were fundamental advances in vision that continue to be the state of the art today. So we have Diffusion, which replaced what was, at that time, the dominant paradigm based on GANs, to become the dominant way in which we generate images and videos extremely efficiently and with very high fidelity. Now, this was something which works extremely well, even today.

**[2:35](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=155s)** But so far, most of the state of the art demonstrations of Diffusion have been limited to images. But there has been a recent wave of work now taking in the same ideas and applying it to the field of text. Now, why is text hard? So to understand why text is very different from images, it simply boils down to the fact that the notion of Diffusion was invented for continuous modalities. So if you think about modalities, such as images, there's a very natural notion of what it means to add noise and then a good mathematical theory to what it means to do a principal denoising of it. Text, on the other hand, happens to be discrete, which makes it fundamentally very hard to think about what

**[3:25](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=205s)** are good notions of noising and denoising, which can be trained at scale? So at inception, what we've been doing is trying to build a new generation of language models, which apply this idea to long range text sequences. And how it basically works is that instead of generating tokens sequentially, one token at a time, which is what, practically, all language models of today do, that's the autoregressive paradigm that you see at the bottom, what we are now doing is, we are coming up with a way in which you can denoise text. So you could start with something that's extremely gibberish and then pass it through a neural network. This can be any architecture. We use transformers.

**[4:13](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=253s)** And through this transformer neural network, you are now training it to fix the noise in its input. So that's how you can then find structure within text and generate something extremely coherent in much shorter amount of time. Because now, you're trying to predict all the denoise tokens in parallel. So this is tracing down the history of text diffusion. So in 2019 is when denoising diffusion started taking off for images. So this was the time when companies like Midjourney, as well as from other labs including Google, OpenAI were coming up with very large-scale demonstrations of how Diffusion can generate extremely high quality images. It took many years and work of the entire research community

**[5:07](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=307s)** to come up with ideas, which eventually led us to the point, where there was a breakthrough from one of my co-founders lab, where we were able to then design a diffusion model for text that achieved parity with GPT 2. Now, of course, in 2024, GPT 2 was no longer the bar for success in language. And that's when we decided to form this company called Inception and really take this idea at scale. A few months later, we launched Mercury, which is the first commercial scale diffusion language model. And it was able to generate text at very good scales and do a lot of good tasks, including code editing, code generation, mathematical problem-solving, common sense at scale and extremely fast.

**[5:58](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=358s)** And this, of course, also caught the attention of a lot of notable folks in the field, both in academia and industry. Very quickly, a few months later, many different labs from Google to NVIDIA to Alibaba followed up with their own efforts in building Diffusion LLMs. And earlier this year, we launched the second iteration of our model, Mercury 2, which now also had capabilities to do reasoning. And unlike other LLMs, Diffusion reasoning looks very different from how it works for autoregressive LLMs. And the best way to illustrate that is through this chart. So this is a chart from artificial analysis, which is comparing Mercury with the state of the art LLMs for the speed-optimized regime from different labs.

**[6:51](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=411s)** So on the x-axis, you see the speed, as measured by tokens per second. So higher is better. And on the y-axis, you're looking at some kind of quality index. In this case, it's the one that's defined by artificial analysis across a wide range of agentic benchmarks. And what you see here is that Mercury gets you similar quality, as you would see for models of similar size, if you think about your clawed haikus, you think about the GPT 5 minis. So these are all the speed-optimized models from frontier labs. And it gets you similar quality, while being much, much faster. And that's because it's denoising tokens in parallel.

**[7:39](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=459s)** It's breaking away from the paradigm of generating tokens sequentially. So this has now been commercialized as well. So we provide a drop in replacement for existing language models. And there's a lot of different applications that are being built on top of these models. So a lot of them are ones where speed is extremely critical, along with also concerns of cost. And all of this has to be done at a desired level of quality. So some of the domains where we are seeing a lot of success is in voice and coding and search, just to show you a few case studies of how this has come to the real world. So for voice and support agents, what you can see is that what you really care about

**[8:29](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=509s)** is not just intelligence alone. You care about intelligence, as well as the time for response. So in particular, the time to first token is extremely important for any kind of customer support voice kind of applications. And for these kinds of applications, if you look at these charts, what it's really showing is that Mercury defines a different kind of frontier, where it gets you extremely good intelligence at a very small time to first token. In fact, compared to even non-reasoning models, such as GPT 4.1, which is in production at most of the voice companies, Mercury 2 can do reasoning and still be faster than a GPT model. So that's what speed buys you, where you can actually

**[9:19](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=559s)** deploy reasoning models at the speed or even better than non-reasoning models-- so extremely good quality at a fraction of the speed. Now, one thing also notable in this is all of our deployments are on NVIDIA hardware. So this is coming purely because of the fact that we have trained these models using Diffusion. And we are generating tokens in parallel. So any of these complementary advantages, such as those that could arise from modern hardware, like Cerebras and Grok, could pair up potentially very well with having a Diffusion model for text on top of it. This is another case study for search. In this case, you not only care about speed,

**[10:08](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=608s)** you also care about cost. So these two plots are showing how accuracy varies with each of these factors. And again, you see a similar kind of trend, where the models that you can actually deploy in production should have a good combination of all three. And mercury strikes a really good balance in this space as well. Coding is another space. Of course, I can't imagine my life now without using coding agents. And what you see with coding agents is, again, that you might have a primary agent that's extremely verbose or might use a lot of tokens, but that's not always what you need in order to drive down the token economics towards something that's sustainable. So companies like Augment Code are using Mercury in conjunction

**[10:59](https://www.youtube.com/watch?v=QLdOBT9RB-8&t=659s)** with some of the more heavyweight models, like Opus, to get a very good balance, reduce latency, as well as cost. And I would end with this slide, where if you think about the frontier of intelligence, we have reached a point, where we have extremely good intelligence for a lot of applications. But now, what's really important is, as we build value for everyone around us, is to think about the new currency of intelligence per Watt. And Diffusion LLMs seem like a really good bet to redefining that frontier. Thank you.
