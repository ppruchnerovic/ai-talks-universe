---
id: 1NWnSwCB4NM
title: "Your KV Cache Can Spot Attacks on Your AI Agents - Ari Azarafrooz, Intrinsec AI"
slug: your-kv-cache-can-spot-attacks-on-your-ai-agents-ari
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Ari Azarafrooz"]
channel: "AI Engineer"
duration_min: 7
published_at: 2026-11-09T08:00:38Z
video_id: 1NWnSwCB4NM
url: https://www.youtube.com/watch?v=1NWnSwCB4NM
youtube_url: https://www.youtube.com/watch?v=1NWnSwCB4NM
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Ari Azarafrooz", "Intrinsec AI", "AI security", "KV cache", "prompt injection", "AI agents", "inference", "vLLM", "SGLang", "LMCache", "anomaly detection", "AI Engineer", "AIE CODE"]
topics: ["Agents & orchestration", "Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: true
---

# Your KV Cache Can Spot Attacks on Your AI Agents - Ari Azarafrooz, Intrinsec AI

**Ari Azarafrooz**

`AI Engineer` · `AI Engineer` · `2026` · `7 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Ari Azarafrooz` `#Intrinsec AI` `#AI security` `#KV cache` `#prompt injection` `#AI agents` `#inference` `#vLLM` `#SGLang` `#LMCache` `#anomaly detection` `#AI Engineer` `#AIE CODE`

[Watch the recording](https://www.youtube.com/watch?v=1NWnSwCB4NM) · [Conference site](https://www.ai.engineer/)

## Description

Ari Azarafrooz, founder of Intrinsec AI, shows how the KV cache your inference engine already writes can double as a security signal for AI agents. Instead of only guarding inputs and outputs with judge models or a classifier for every failure, he learns a baseline from normal traffic and flags KV pages that look unusual, catching problems like a hidden spoken instruction in a voicemail where there is no text to filter. He covers where this plugs into stacks like vLLM, SGLang, LMCache, llm-d and NVIDIA Dynamo, and the two hard parts in production: models that keep changing and KV data too big to move in real time.

Ari Azarafrooz

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*1,129 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=0s)** Hi, I'm Ari Azarfar, founder of Intrinsic AI. Um this talk is for people who build agents and run their own inference stack, or plan to. And if that's you, you associate typically the KB cache, the bread and butter of uh modern inference engines, usually as a throughput optimization. The keys and values computed per token, kept so the model doesn't compute them again. Today, I'll like to show KB cache in a different light. The way agents agent AI agent application could go wrong or keep growing, right? Prompt injection, jailbreaks, broken tool calls, sensitive tool calls, sensitive data exposures, hidden backdoors, and drifts, and so forth, right? So, the way right now we typically guard against against this numerous ways that an AI agent application could go wrong is by guarding the edge, by perhaps passing a

**[0:49](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=49s)** judge model that checks the prompts, the inputs, and the response outputs against your policy. All right? Or you build a classifier for each case. But here's a different light. The model turns every input into a computation before it acts, before it decodes, before it generates the response, before that response becomes another tool call. The KB cache is your engine's record of that computation. The modern inference engine, for free, are using it and reading it. And therefore, on this talk, I would like to suggest as as a complement to the way you're already using your own guardrails, to use this data and integrated with your KB cache infrastructure. I refer to this as a KB first security signals, and basically three reasons

**[1:38](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=98s)** that matters, right? So, the data is already there. You pick the gems from the pile your inference stack would already were throwing away. It covers the guardrails blind spots, because whatever it slips past those guardrails, it still becomes computation. And it stays in place, so it's perfect for data privacy application, for cases where you do not have the luxury to read the inputs and outputs. And the recipe is pretty straightforward, right? Has three steps. You learn a baseline for your AI workload, for your AI inference traffic, how your KB page typically look like, and then find the KB pages that are rarer against your baseline, typically your anomalies. And then you can even classify and explain those. So, first let's start with where in the stack this

**[2:27](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=147s)** integration could happen. The interesting thing about the KB cache is that in a way existence of those had made the inference in a way stateful, right? So, for example, things like KB cache management layers such as LM cache stores them from GPU down to a remote storage. Or LLMD and NVIDIA Dynamo route each new request towards the worker that already holds perhaps that cached KB page. So, there are two integration points you you you you can integrate those anomaly detection or those classifiers into. Either you can implement it directly inside of your inference engine via LMs, you name so forth. The beauty of this approach is that it's real time. And and the the the alert that it would perhaps generate could ride along your

**[3:18](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=198s)** future tool calls or your future policies. So, you can harden basically your policies or guardrails but just generating the computational anomalies that you observe within your inference engines. And you or perhaps you can integrate it with as a as a way of threat discovery in a sense. So, you can integrate with your LM cache. So, it reads the stored KB pages and find things that don't belong with the rest, right? So, now I want to show you some numbers and just a very simple hello world use case if if this is actually working and this is a valid approach. And for that, let me use the use case that has no text to filter at all, a voice agent. So, here's a case of study of a voice agent. In this case, it was a Gemini

**[4:05](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=245s)** 404B. Our baseline was 72 ordinary clips and spoken four voices. We're looking at 16 token pages. Obviously, this granularity could change. But here was just use this shorter pages so we could have more data in the baseline. And then on the test, we have different voices one clean voice and the other one has a hidden instruction within it. As you can as shown here, not only you can detect these cases just using simple anomaly detection, but also you would know which part of um which page which part of your request had this anomalous event. We even went further and we trained a model that uses the KD pages as features. And we didn't we're trying to explain it

**[4:54](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=294s)** or tag it with things that are useful. In this case, although it wasn't even trained on audio, it's able to generate correct information about personal information, home address, location data, travel information, destination. So, now back to text agents. In this case, it was a client 314 billion served live on bill 110 cash. The one on the left shows you an idea of how attacks and normal traffic would typically separate from each other and then the one on the right, which is perhaps more meaningful, it was using the AT bench and hugging face. It has its own baseline of benign agent traces and eight kind of agent failure from injected tools description to misinformation and so forth. We look at the top 10 alerts that

**[5:42](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=342s)** anomalous anomaly detection would generate and about seven to eight times of out of 10 of these alerts are actually anomalous meaningful and useful anomalous activities. We even went further and we looked at whether there's any kind of anomalous event that is stand out more than the rest. Um to make things hard in production. First, models change. Fine-tunes and new releases, but also agents that each one on a different model. And routers that pick a specialist model per request. That means each model writes its pages its own coordinates. So, either you learn every baseline, classifier, and explainer, which is uh computationally prohibitive, or you have

**[6:32](https://www.youtube.com/watch?v=1NWnSwCB4NM&t=392s)** to find a way to map them all into one shared representation space. Second, real time means moving big objects. For example, a 1 256 token chunk of 1.34 billion is about 40 megabytes of KB. Compression and streaming like cache gen could help, but moving that for security analysis and acting in real times is still a slow. And that's what we solve at Interesting AI. We are looking for teams building their own inference stacks who treat security as a foundational design decision. I hope this was helpful for you. Thank you so much for listening. Bye.
