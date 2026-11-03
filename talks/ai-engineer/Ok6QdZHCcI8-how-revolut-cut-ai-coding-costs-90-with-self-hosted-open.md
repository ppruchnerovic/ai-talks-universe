---
id: Ok6QdZHCcI8
title: "How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut"
slug: how-revolut-cut-ai-coding-costs-90-with-self-hosted-open
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["David Abitbol"]
channel: "AI Engineer"
duration_min: 12
published_at: 2026-10-29T09:00:21Z
video_id: Ok6QdZHCcI8
url: https://www.youtube.com/watch?v=Ok6QdZHCcI8
youtube_url: https://www.youtube.com/watch?v=Ok6QdZHCcI8
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "David Abitbol", "Revolut", "self-hosted LLM", "open source models", "GLM", "GPU inference", "AI coding", "developer productivity", "AI cost", "B200", "fintech", "banking", "AI Engineer", "AIE NYC"]
topics: ["Coding assistants & agents", "Inference, serving & GPU infra", "Science, healthcare & applied ML"]
transcript: true
---

# How Revolut Cut AI Coding Costs 90% With Self-Hosted Open Models - David Abitbol, Revolut

**David Abitbol**

`AI Engineer` · `AI Engineer` · `2026` · `12 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#David Abitbol` `#Revolut` `#self-hosted LLM` `#open source models` `#GLM` `#GPU inference` `#AI coding` `#developer productivity` `#AI cost` `#B200` `#fintech` `#banking` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=Ok6QdZHCcI8) · [Conference site](https://www.ai.engineer/)

## Description

David Abitbol, who leads AI operations at Revolut, shares data from 2,000 engineers on what AI tools did to coding time and lead time, and why self-hosting open-source GLM models made the biggest difference: about 60-70% faster delivery at roughly a tenth of what they were paying frontier labs. He covers the GPUs needed, the latency targets that keep engineers happy, the tuning that made the same hardware 88% faster, and how an EU-regulated bank keeps it compliant.

Chapters:
0:00 Intro
0:36 Who Revolut is
1:18 What AI did to 2,000 engineers' lead time
2:45 Why they started self-hosting
3:33 Coding isn't the bottleneck
4:24 What it takes to self-host GLM
5:46 Tuning: same GPUs, 88% faster
7:06 The parameters that matter
8:14 Production setup
9:23 For the CIO: compliance and safety

David Abitbol

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*1,797 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=1s)** [music] My name is David. I lead AI operations at a company called Revolute. We have uh 50 minutes today together. We'll talk about high performance engineering and self-hosting open source model on dedicated GPU. How's that sound? >> Cool. So, it's gonna be a technical one, so bear with me. Um, so maybe to start off because I know this is the US and you may not know Revolute. Uh, quick words about our company. We're a digital bank in Europe. We have 80 million customers. We're live

**[0:49](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=49s)** in 45 markets with the most downloaded financial app uh in Europe for the last year. And as of July, we're Europe's largest private company. Um, so we're doing okay. The the emphasis of Revolute is, you know, shipping a lot of product. And so there's a high focus on engineering culture and uh excellence on that domain. And so we talk about that. So let's talk about some AI. We have a chart here. You're going to see two lines. This is a sample of 2,000 engineers performance over the last year. So the green line is going to be lead time. So it's going to be when engineer picks up a feature until a feature is

**[1:38](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=98s)** merged and ready to be deployed. The blue line is going to be coding time. So the green line is in days. The blue line is in hours. Just to reset the timeline in case people forget because AI was already fast. Clothe code came out around February 2025, right? And that's the clo code sonet 3.7, the one that would delete your pro database, right? Not the safe cloud and codeex that we have today. So bear in mind when we talk about adoption. So what you see on this chart is um January 25 first introduced AI the company right um Gemini first time people were able to use private data with an AI. around February we started playing around with cloud code and then January is when we first launched cloud code at

**[2:27](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=147s)** scale what you see is um Gemini had 10% improvements in lead time 20% improvement in coding time so that's people no longer need to look stack overflow and uh reading documentation but then cloud code not so much impact at the time so when we launched it we were highly skeptical about the cost of AI we were seeing engineers spend a,000 a month, 10,000 a month with not so much ROI. And so when we launched it, we launched it with um strict budget limits. And so we're looking at the next thing, right? So how can we provide unlimited tokens to engineers so they can use AI guiltfree for a fraction of the cost and so we looked into open source. So around April 26 is when we started self-hosting open source model. We're a

**[3:16](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=196s)** big fan of GLM for coding. So around that time what you see uh April 26 GM51 we see 60% improvement in uh coding time 70% improvement in lead time. So dramatic impact what do we learn from this? Well there's more impact on the lead time than on the coding time. So what we find is the bottleneck for engineering is not necessarily coding. you can save a lot of time not having to dig through your inbox or messing with J conference. So when you have a limited token, you're free to do that. You no longer have to save your tokens for the end of the quarter or uh the most difficult task. So where do we stand? Well, open source is now a priority at Revolute. New

**[4:04](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=244s)** economics are favorable. The billing is flat. We don't have any bill shock end of the month. And the frontier is the exception. So obviously we keep using code explode code. The latest model are fantastic. Gemini argon very well very good as well. But um we keep them as exception. So how do we get there? Some metrics that matter when you're self-hosting model. So to serve 2,000 engineers we roughly need 56 B200 and that's to host GLM 53. HLM is a big model, right? Parameters. What you want to aim for is sub3 second time to first token. This is empirical evidence. As soon as

**[4:52](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=292s)** you exceed 5 seconds, my slacking box starts to blow up. And so we know that's the limit. Terms of throughput doesn't really matter as much, right? So we serve in terms of interactivity 200 token per second. People are fine. You don't need to go higher. um the way people work has changed. We no longer look at the stream of thinking tokens. People run task in parallel and check in when the task is done. But if you want to have high throughput and you're an engineer at Revolute, you just connect after 5 p.m. when one is on GPU and you can get 800 TPS and then you know it's a dream. In terms of cost, in terms of impact, uh self-hosting GLM or blended cost of token is 30 cents per million and so our invoice is onetenth of what we were spending on entropic and um open.

**[5:46](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=346s)** So there's a lot of tuning that goes into running open source models. If you just get GPUs and upload weights on a GPU and you start doing some inference, you're going to get terrible performance. It's because your workload is going to be very dependent um on the parameters that you set. So if you look all the way to the left of that chart, the blue line is going to be demand. So that's request per second. That's going to be what's going to be the bottleneck for your latency for your GPUs. And the red line is what we're optimizing for. That's the time to first token. So when we started back in April, you could see request per second around three, which is high but not so high. And time to first token over 10 second, which is very slow.

**[6:35](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=395s)** But the data that you see is the same number of GPU. We didn't increase GPU count. We still have 56. And by the end you see in August request per second we're over seven and time to first we're around 1.6. So we've had 88% improvement in performance for 76% increased demand. [snorts] So the learning from this is there's a lot of parameters that you can improve on and you really need to resist scaling if you're looking to self host some model. So let's talk parameters. There's no secret recipe, but the things you could consider are the following. First one, long context is a scam. You really need to be mindful that even though you can serve 1 million token, 256, 256 is really what you need.

**[7:26](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=446s)** Quantisation, if you're running black wall generation GPU, you don't want to run anything higher than FP4. NVFP4 is best. roughly going from FP4 to FP8 is a 40% saving in GPU footprint for zero loss in uh precision. Other parameters to consider tensor palism even though GLM fits on uh TP4 you don't have enough KV cache and so maybe a TP8 works better depending on how large your workload is and then on the more zotic um check your cache it coding test needs to be above 90% uh cache it and you can look into optimize spec decoding uh sequential prefill pdag all of these cool so now let's talk about um

**[8:16](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=496s)** production setup. GM obviously is a text only model which is a limitation for some people. The trade-off I would say uh we would make every time is get the smarter model and figure out how to do image recognition another way. You can easily have a local router open codeex is one where you would route any image recognition to Gemini or Luna and keep JM for the main task. If you really need some uh vision model, GM5G flash works really well. We have our UI designer making great use of it. Um turnaround for uh UI product has gone a really really long way. And then the last one is going to be about uh the harness.

**[9:04](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=544s)** So all of these endpoints are going to be open AAI compatible API with response API and so you can use them inside open codeex codeex app as well works pretty well and so that's what we uh we recommend and then um last message and this one is for the CIO in the room there's been a lot of stigma in using Chinese uh open source So the thing to consider is you're not using the inference dedicated endpoint that goes to China. You're just getting the weights and putting them on a US-based service. So for data sharing side, this is totally fine. Revolute in particular because we're a

**[9:53](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=593s)** EU regulated bank, we fall under the most uh strict regime in terms of compliance. And so what we find that works is all of these coding task are not considered autonomous agent. They're always with a human in the loop. And so how do you give reassurance that you have a human in the loop? You start by creating a sandbox that guarantees that. And the sandbox means now if you've used codeex code, it has all these features of approve for me. You just have to set the rules for the operations that you don't want to allow. So you can allow grabb but not gradal for instance and that's going to give confidence uh to your regulator that this is not an autonomous agent that needs different supervision. The sandbox also protects you from uh

**[10:41](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=641s)** rogue use right you may have bad actor inside your company and you want to shield uh for that. You'd be surprised what you find in a large company. And then the last one is prompt injection. not not so much a thing u now given how smart models are but always a thing in terms of data privacy we spoke about it so as long as the data sits in one of the countries that are in the data equivalency framework so US EU UK Israel you're fine you can get your GPUs there all of your inference provider or GPU provider are going to have zero data retention by default and then the last thing you need is a very strong uh open telemetry so that if you ever have an incident um you need to be able to go deep and look at the locks

**[11:31](https://www.youtube.com/watch?v=Ok6QdZHCcI8&t=691s)** also gives you some uh yeah analytics. All right, thanks everyone. That was all for my talk. [applause]
