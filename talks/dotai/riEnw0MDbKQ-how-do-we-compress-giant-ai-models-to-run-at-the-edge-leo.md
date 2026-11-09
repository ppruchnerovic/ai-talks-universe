---
id: riEnw0MDbKQ
title: "How Do We Compress Giant AI Models to Run at the Edge? - Léo Arsenin - Cloudflare - dotAI 2026"
slug: how-do-we-compress-giant-ai-models-to-run-at-the-edge-leo
conference: dotai
conference_name: "dotAI"
category: "Practitioner AI conferences"
edition: "dot conferences"
year: 2026
speakers: ["Léo Arsenin"]
channel: "dotconferences"
duration_min: 11
published_at: 2026-09-28T14:00:24Z
video_id: riEnw0MDbKQ
url: https://www.youtube.com/watch?v=riEnw0MDbKQ
youtube_url: https://www.youtube.com/watch?v=riEnw0MDbKQ
tags: []
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# How Do We Compress Giant AI Models to Run at the Edge? - Léo Arsenin - Cloudflare - dotAI 2026

**Léo Arsenin**

`dotAI` · `dot conferences` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=riEnw0MDbKQ) · [Conference site](https://www.dotai.io/)

## Description

Talk presented at dotAI 2026 by Léo Arsenin, Solutions Engineer at Cloudflare: https://www.dotai.io/

Leo helps startups and scale-ups build on the platform that powers 20% of the web. As a Solutions Engineer at Cloudflare, he partners with customers to bridge the gap between infrastructure and AI. His work focuses on architecting agentic workloads and deploying AI inference services.

Lightning talk: "How Do We Compress Giant AI Models to Run at the Edge?"

Quantization is the go-to method for making LLMs smaller, but it's lossy, quality degrades in ways that are hard to predict and impossible to reverse. We found a different path by looking at how model weights are actually stored. In BF16 format, every weight has an 8-bit exponent, but only 16 values out of 256 cover 99% of all weights in a typical layer. Information theory says you need just 2.6 bits to represent that distribution, which means 5.4 bits per weight are pure waste. Unweight applies Huffman coding to the exponent stream, decompresses directly in fast on-chip shared memory, and feeds the reconstructed weights straight to the tensor cores, they never round-trip through slow main memory. The result is a 22% model size reduction that is 100% lossless with bit-exact outputs, saving roughly 3 GB of VRAM on Llama 3.1 8B alone. For Cloudflare, this means fitting more models on fewer GPUs across our 330+ city network, making inference cheaper and faster for everyone. We open-sourced the GPU kernels and published the full research paper, so you can use this technique on your own models today. If you care about running AI sustainably and affordably, this talk shows you a compression approach that doesn't ask you to sacrifice quality.

## Transcript

*1,997 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=7s)** [music] [music] [music] [applause] >> Uh who in the room knows uh Cloudflare? Can you raise your hand like this? I know. Okay, quite quite a few people. Uh some of you might know us for what we were doing historically like CDN, DDoS, WAF, uh everything about the the security layer and the CDN. And you might be wondering like why am I

**[0:56](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=56s)** coming here to talk about AI today if you don't know what we're doing in this field. Uh actually I I I promise I won't talk about CDN and WAF and all of that. And I'm more about uh talking about a new service uh we we launched few years ago. We wanted to to to to give inference to us inside Cloudflare and to our customer. But the problem is we are running a CDN. We're not like a big cloud provider with like a lot of big data center with a big cluster of GPUs. So that was like a problematic. How can we run the big models of today uh AI in such distributed network? Because we don't have like um big data center. So we needed to to find some way and some trick to make this uh big model uh fit in our network. So first maybe let's go back to the basic or how an LLM is working today. So

**[1:45](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=105s)** we give uh an input to a software. Uh this input is going to be divided in some prompt as you might uh know it. This prompt is going to be fed in the LLM. Then it's going to try to calculate which are the most probable words to the given context and give you uh the answer. This is uh how is it working? This require a lot a lot of compute, right? And maybe more practically, how uh is it working? If you want to to run the big model of today, and how we do it uh at Cloudflare. So, first, you have to pull some weight of the model uh from somewhere. Hugging Face is a really cool place to to do it. Um you can also develop your own model and have your own weight and pull it yourself, but yeah, we we download it. Then, we have to host it uh somewhere in the cloud. We we host it on our own platform. Then, you have to run an inference engine, right? So,

**[2:33](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=153s)** it can be SG Lang or vLLM or this kind of software. We build our own one, which is called Infire, because we need we have some uh really specific needs. And you're going to see how we optimized it to to run on uh on fewer GPUs. And then, when it's done, you send a request to uh a web server. It can be Apache, uh Nginx, whatever. It's also our own software. We receive the request, we route it to the right GPU, and uh then the inference engine is working, so the tokenization, uh the inference, and then we we stream the the response back. And what's is important here is the inference engine, so like Infire and and this part, because the web server, we were doing this uh for sometimes uh already. Um so, as I said at the beginning, we have a really distributed network with a

**[3:20](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=200s)** lot of data center everywhere around the world. So, that's cool for some use cases, right? Because we can deploy some GPUs everywhere, and we can run really small models to do like inference voice inference, for instance, so voice recognition. If you have If you have someone like in South Asia, you don't want him to be on the call, send the call back to a data center in Europe, for instance, and then taking like half a second to to give the response. So, that's a really cool use case for running small models uh on on Cloudflare. But there is an issue like with the big model of today, like in 2026, we have like really really huge model like Chimera 3 or GLM the the big GLM models. And that's not suitable for that. Why? Because we need like more GPU capacity, more power, more cooling, like bigger bigger data center. So, we decided to give up a bit a bit of this idea. We still have it for the small model, but

**[4:07](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=247s)** we also decided to invest in more cluster, like more concentrated cluster, right? To have more throughput, more capacity, and more power. And so, that's why we have two tier of data center. Some with more GPU capacity and some with light one. And even with the big one, we wanted to optimize it a bit. So, before jumping in how we optimize it, I just remind you a quick concept. I don't know if you're all aware with what attention layer is. That that's the concept when you send a prompt in the LLM. As I said at the beginning, we have to guess what is the most probable next word, right? But how do we calculate that? There is a little process which is called attention layer. All of these words don't have the same importance, right? So, maybe the word in in this sentence or the are not really important in the context, but some of

**[4:55](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=295s)** them are really important. Like when Alice put her passport in the blue drawer, the blue drawer is might be the most important word. So, when we ask a question, we have to calculate which are the important word in the first context to guess the next one. And this is um done with with what we call the key value query. The most important part here is the key value because every time we send a prompt to the LLM, we have to calculate back uh this key value. What token are important? How is it relevant in the given context? And if we have to calculate that every time, this is taking a lot of compute, a lot of time, and so it's more expensive in time and in money because we run the GPU longer. So, that's that was something we wanted to to optimize. First, we cache it, but even if we if we cache it, we want to reduce the the memory it's

**[5:43](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=343s)** taking. So, what we did Uh, is um we try to reduce um, the amount of space that this cache is taking. So, every time we calculate the KV again, uh, we wanted to reduce it using a method called quantization, which is like basic mathematics. So, instead of storing a lot of number, we we store a bit less. So, we are losing a bit of quality and information. So, we need we need to find the the right amount of compression for that. But, when when we find it, it's a good like threshold, we can accept it for production without giving a quality in the model. So, reducing the KV can work and we can apply the same logic to the weight themselves. So, the weight is the way the model is tuned, right? So, when the weight was trained and stuff like this. And we can apply the same logic

**[6:31](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=391s)** quantization to the weight of the model. And so, if we take like two example like Kimmy and GLM, we managed to reduce almost half of the size of the model and to increase also the the cache capacity for the same model with in in the same memory allocation, right? So, compressing it, trying to not lose too much information and that's how we went. Um, but still like we're using memory. So, the second way we optimize it is managing how GPU are using the memory. By default, each conversation is reserving an amount of memory, right? So, a new conversation is going to reserve I don't know, like this amount. But, sometimes the conversation is ending really quick and we're still

**[7:17](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=437s)** keeping this capacity in the cache just in case we're going to have a follow-up. And that's losing a lot of of space. So, what we try to do is use a method called page allocation. So, this was not invented by Cloudflare, it's quite old actually. And you can use it in other inference engine like VLM, Z length, stuff like this. And the goal is to use small blocks of memory which are going to be in like a shared pool. So, like this you don't allocate a new uh memory slot for each new conversation, but instead you keep them all in the same place, really isolated, so we don't want to have like cache leak or having access to other conversation, and that's the way also we optimize it. Last one, which is uh one of the most obvious, is reusing the same uh hardware, right? Uh maybe you don't have this issue if you only have one GPU and one cluster, so every request is going

**[8:06](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=486s)** to the same, but at Cloudflare we have a lot uh everywhere in the world, where we have to make sure that all the requests are going to the same hardware for a given user, right? Because when you send a request, you want to reuse the system I explained just before, the caching and everything. So, if you send a request to another data that's another data center and another GPU, you won't be able to reuse the cache, right? Because we're not sharing a global state across all the network. So, we need to make sure to send to the exact same cluster every request every good time, whatever is happening on the network, if there is congestion, stuff like this, we need to try to to send it back. So, there is difference uh mechanism, but just like adding some kind of affinity header and and this kind of routing can can work and help us in this area. Uh so, this was learned um and and and by the way, like internally

**[8:55](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=535s)** and for some customer, we managed to increase the the cache ratio to up to 60% to 80% by routing to the the same cluster, even if we have like thousands of GPUs everywhere in the world. Um and the So, this was learned for the LLM era, but of course, I mean, I said I I was not able about to talk about CDN and and WAF, but we reused the same principle to a classic machine learning model, right? Because not everything is LLM, so even our classic WAF and classic uh bot management, we decided to apply the same kind of concept compressing uh optimizing the cache, reusing the same hardware, and we managed to save a a of time. Uh and and as you know, Cloudflare is serving like 25% of the requests on internet, which is basically one request over over four. So every day

**[9:44](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=584s)** we're like saving 70 years of compute just with few micro microsecond for every request thanks to this kind of optimization. So maybe like for few requests it doesn't really matter, but at the big scale that's help us to to save some time and compute. So if you have like three stuff to remember on how we try to optimize it, it was quite short in 10 minutes. I can also talk with you at the Cloudflare booth or you can also check the the blog online, but the three uh good information to retain is like place the GPU in the right position if we need a latency put them like at the on our distributed network. If you need more throughput we put them in the central network. Compress the weight, move less data and try to reuse the same hardware all the

**[10:32](https://www.youtube.com/watch?v=riEnw0MDbKQ&t=632s)** time. Thank you. >> Hey. >> [applause] >> HEY. HEY.
