---
id: xn8EsW0wxyc
title: "How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI"
slug: how-secrets-leak-through-ai-agents-and-how-to-stop-it
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 15
published_at: 2026-10-11T16:30:34Z
video_id: xn8EsW0wxyc
url: https://www.youtube.com/watch?v=xn8EsW0wxyc
youtube_url: https://www.youtube.com/watch?v=xn8EsW0wxyc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI privacy", "AI security", "AI agents", "agent security", "prompt injection", "secrets management", "data exfiltration", "confidential computing", "trusted execution environment", "logging", "open source models", "Venice AI", "Rig", "Joshua Mo", "AI Engineer"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# How Secrets Leak Through AI Agents (and How to Stop It) — Venice AI

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI privacy` `#AI security` `#AI agents` `#agent security` `#prompt injection` `#secrets management` `#data exfiltration` `#confidential computing` `#trusted execution environment` `#logging` `#open source models` `#Venice AI` `#Rig` `#Joshua Mo` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=xn8EsW0wxyc) · [Conference site](https://www.ai.engineer/)

## Description

A private model doesn't make a private product. The leaks happen in everything you build around it.

Joshua Mo, lead developer relations engineer at Venice AI and previously lead maintainer of the Rust AI framework Rig, explains why privacy matters (one breach and users leave, and less stored data means a smaller blast radius) and how Venice approaches it: no stored prompts, anonymized requests to closed providers, models in trusted execution environments, and split-key encrypted storage. Then he shows where agent systems leak: logs that quietly capture prompts and secrets, and secrets fetched from a vault straight into the reasoning layer, where a tool call can exfiltrate them. His patterns: hashed IDs instead of personal data, split-key custody, revocable handles, narrow agent scope, a classifier in front of the agent to catch prompt injection, wiring the vault to the execution layer instead of the LLM, sandboxes plus permission monitoring, and confidential compute with verifiable attestations. He closes on the open problem of confidential tool calls.

In this talk:
• Why privacy is about blast radius, not just the model
• How logs and secrets leak through a typical agent
• Keeping credentials in the execution layer, never the LLM
• Hashes, split keys, handles, narrow scope and confidential compute

SPEAKER
Joshua Mo, Lead DevRel Engineer, Venice AI
X: https://x.com/joshmo_dev

LINKS
Venice AI: https://venice.ai
Venice API docs: https://docs.venice.ai
Rig (Rust AI framework): https://github.com/0xPlaygrounds/rig

CHAPTERS
0:00 Intro
0:55 What Venice is
1:40 Why privacy matters
2:35 How Venice handles privacy
4:15 Not all systems are private
5:05 The logging trap
5:54 How secrets leak through an agent
6:49 Patterns that work
7:54 Revocable handles
8:39 Narrow agent scope
9:29 Screening for prompt injection
10:44 Keep secrets out of the model
12:04 Sandboxes aren't a cure-all
12:54 Own your runtime
13:09 Confidential compute
14:49 Confidential tool calls

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*1,931 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=12s)** Hi everyone. Uh, welcome to my talk. I'm Joshua Mo and today we're going to be talking about some of the challenges of building a privacy respecting AI system. So just for an introduction as to who I am, I'm currently the lead developer relations engineer at Venice AI. So currently I handle partnerships, documentation, talking to developers, um some engineering and other things other things as well. Uh so prior to this I was actually the lead maintainer for rig which is the leading AI framework in Rust. Um so what is Venice? So Venice is a

**[1:03](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=63s)** private and unrestricted AI platform. Uh so we host all the latest open-source models. We're 100% open AI compatible. We don't store any prompts or conversations and we also have a web app that you can use to talk to our models as well. We also have a studio offering that is um a offering for our content creators that includes video, audio, image generation and transcription. So why does privacy matter? So let's d deep dive into this. So as we know data breaches are increasingly becoming an

**[1:54](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=114s)** eventuality which means that essentially reputational risk matters. You only need one data breach before your users stop trusting you and they move on to another provider. Or if you're enterprise, maybe you lose the enterprise customer who's been fueling almost 90% of your annual revenue. So in this case, sensitive data can severely increase the impact of any security incident. As well as that, storing less use uh user data directly reduces the blast radius of a security security incident that happens. So, how does Venice do privacy today? Well, there's a few ways. The first way

**[2:43](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=163s)** is that we don't store any prompt conversations, of course, as we mentioned previously, which means that any digital footprint incurred in your side is is essentially reduced to zero. So, when you use models like GLM 5.2 and Kimmy 2.7, you can guarantee that none of your conversations will be saved on our side. It will be all stored locally. We also have predefined tiers of privacy. So private by default means that the affforementioned uh measures apply for providers like open AI and claude. Uh we anonymize your user footprint so that none of well they can't identify you from your simply from your prompt or your request.

**[3:32](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=212s)** We also have models hosted in trusted execution environments, meaning that you can verifiably prove that your inference was run in a totally private process. As well as that, we also use a privacy first software architecture. So for endpoints like video uh generation where you have to pull the endpoints, we store the results in a totally encrypted payload using split key custody, meaning that attackers can't access your data and neither can the team should their accounts be compromised. So I just want to introduce you to the guys the uh the idea that not all systems are made equal. So, not all systems are made private. Some companies

**[4:22](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=262s)** may claim their systems are private, but they're not really. Uh, you guys know how it goes. So, while models are a very important part of an aentic system, in fact, they're a vital part of the system. Um, they are still only one part. And in fact to create a complete system to accompany an LLM in doing a task you have to build an entire process around it. However, these systems are also much more prone to data leakage and breaches. So the real question is how can we optimize for this kind of problem. So one example I just wanted to bring up was observability logging. So observability as many of you know is a core part of any serious production

**[5:12](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=312s)** system today. So just to break it down quickly, observability can be broken down into metrics, logs and traces. So traces are simply a span of work uh done over a unit of time. Metrics as are simply numbers like counters, gauges for instance and logs are the actual messages. So logging, as we all know, is actually pretty great for debugging, especially in production or dem dev environments. But you can also accidentally store prompts and secrets by default if you're not careful, which can also hold personal information. However, when you use Venice, you don't need to worry about any of that. So let's talk about how secrets can flow through a regular agent. So for example,

**[6:01](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=361s)** let's say you're you're using open claw. You send a user request that gets sent to an agent runtime. The runtime might need a secret that it will fetch from a one password vault for instance or hashc vault. The secret will then get sent to the LLM reasoning layer. Um, oh my god. So the reasoning layer will then make an API request through a tool call which will then return the answer back to the user. However, due to this the way that it's architected, the secrets get fed directly to the LLM, which means it then

**[6:49](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=409s)** may get used in training data. So in terms of privacy preserving patterns that work, one thing that we've used at Venice is storing hashes that rep represent ids that we need as opposed to direct data. So for example, if you need to identify a user for rate limiting purposes, you might not want to use their direct user footprint directly. You might want to, you know, store it as a hash for instance, just so you can identify them without directly using any of their personal data. As well as that, we encrypt data and store it in an inaccessible enclave using split key custody. So for context, encryption keys are stored in two halves, a read half and a write half. By

**[7:38](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=458s)** splitting these, the attacker cannot access the data due to needing both halves for the decryption to complete. Additionally, you can use design patterns like handles that can be easily revoked. So a handle is simply an object that grants you access to something. So for example, let's say you have a database pool using a handle. So when you have the handle, you can access the database pool. When you don't, then you can't access it. This is very important especially when you're using authorization like JSON web tokens or session keys that may be uh a core part of your authorization system. As well as that,

**[8:27](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=507s)** of course, engineering your prompts with privacy in mind can be uh very helpful for engineering teams who are using coding harnesses like cursor and clawed code in terms of protecting agent handle data. So essentially ensuring narrow agent scope to to decrease risk. So for example, let's say you pull tools from an NCP server that may have 15 20 different tools. you don't really want to use all of them. You actually only really need one, but you also need an API key to handle that uh API call. So if you pull that API key in from you know your your password vault and then you send it as part of the agent um what can happen is that it gets exfiltrated

**[9:18](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=558s)** through through the agent uh on a tool hall to whatever you know web server is being hosted by a bad actor for instance. As well as that um we also have a classification layer in front of an agent to check for prompt injection for example. So there's a couple of ways you can do this. So you can either use an LLM based uh layer to do this or you can alternatively use a semantic um search layer for example using vector search uh via something like quadrant lance db or additionally you can use an in-memory process. It should also be noted that tight

**[10:07](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=607s)** context loops caused by narrow agent scope can also improve context window performance. So for example, because you don't have as many tools, uh your agents may be able to perform much better. It's well known that when you fill your context window, by doing so, when you reach near the limit of your context window, performance can actually degrade uh considerably. By keeping an empty or near empty context window, we can make sure that the agent is performing at its best. So let's look at keeping secrets out of the model. So here we have a user request that gets sent to the reasoning

**[10:55](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=655s)** layer. This reasoning layer is actually then uh formulating a series of non-deterministic inputs for an agentic runtime. So by tying the password vault to the agentic runtime instead of the reasoning layer, what happens then is that the run the agent runtime is essentially turned into an execution layer which then we can you know we can consider it deterministic. We can do all kinds of things that you normally wouldn't be able to do for privacy and security reasons at the LLN layer. Uh so for example, let's say you want to use a uh browser user tool and you need to log into a into a website that requires your credentials.

**[11:45](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=705s)** With this uh software architecture, it's much more reasonable to say that it's private and secure rather than feeding your password see uh directly into the reasoning layer as well as you know calling external APIs. So in terms of sandboxing your agents um it it's a very well-known fact that using sandboxes and VMs for example firecracker um and you know AWS EC2 in a VPC can significantly upgrade the security of your agent. However this doesn't act as a cure all for your agentic systems. Uh so for example, if you have internet access

**[12:35](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=755s)** enabled for your agent, it can still accidentally exfiltrate data through external API access if you're not careful and therefore monitoring permissions is essential. So my personal suggestion is building your own agentic runtime. So essentially building your own coding harnesses where you can add your own steps, your own observability, uh your own tools, things of that nature. Essentially owning the execution layer and reasoning layer. So let's talk about privacy at the hardware level very quickly. So in terms of this um there's something I like to call confidential compute where a trusted execution environment

**[13:24](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=804s)** essentially uh at the hardware level enables the inference process to be run privately. So with Venice, how this works is that when you send a request, uh you get a response and then we actually return an attestation that you can then um verify with our atestation verifier. So in terms this what this actually means is that you can fully isolate an agent at the reasoning layer cryptographically and prove it in terms of oh confidential tool calls there is still some work to be done um tees are still great for tool calls however we also offer end to end encryption um but there's also you know some work to be done there because of uh

**[14:13](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=853s)** the need to provide an ergonomic API I experience while still allowing users to return entirely encrypted tool calls. This is still kind of an ongoing challenge. Um in terms of this, a very reliable solution would be to allow providers to own the computes layer at which your tool calls being run. However, um [laughter] sorry, just give me a sec. So in terms of confidential tool calls um yeah there's definitely some work to be done. Um yeah that's it. Thank you for

**[15:04](https://www.youtube.com/watch?v=xn8EsW0wxyc&t=904s)** listening.
