---
id: c7R5KmY532c
title: "Sijie Guo: Five lessons from building an open-source managed agents runtime"
slug: sijie-guo-five-lessons-from-building-an-open-source-managed
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 14
published_at: 2026-10-07T22:54:17Z
video_id: c7R5KmY532c
url: https://www.youtube.com/watch?v=c7R5KmY532c
youtube_url: https://www.youtube.com/watch?v=c7R5KmY532c
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Sijie Guo: Five lessons from building an open-source managed agents runtime

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=c7R5KmY532c) · [Conference site](https://aiconference.com/)

## Description

Most agent tooling optimizes the agent loop. In production, that is almost never what breaks. We built a managed agents runtime — the layer between an agent framework and the infrastructure it actually runs on. Five lessons from that, across the three problems nobody demos: building agents that outlive your framework choice, running them so they survive failure, and governing what they can spend, touch, and see.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,102 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=c7R5KmY532c&t=10s)** Hey. Okay. Thank you. Uh Uh thank you everyone. Uh so, my name is uh Sijie Guo. Uh I'm here to kind of share a couple lessons that uh we learned from kind of building an uh open source manager agent uh runtime. Uh brief introduction of myself. So, I'm one of the uh co-founder and CEO uh of a company called StreamNative, uh which is uh more like data platform uh company. Uh I'm also kind of a uh long-time open source uh kind of creators and maintainers. Uh so, I co-created an open source project called Apache Pulsar, uh which have been kind of uh one of the kind of a popular uh streaming data streaming system uh in the community. Uh we also kind of uh found the company to kind of providing a real-time data

**[0:58](https://www.youtube.com/watch?v=c7R5KmY532c&t=58s)** services there. So, I have been kind of in the infrastructure uh data infrastructure space for a couple years. Uh what we have been kind of recently learned is uh we're we're also kind of adopting a lot of these uh uh running agents and uh providing managed agent services for our our customers. Uh and we recently kind of uh building uh kind of open managed agent uh runtime for managed agents there. And what we have learned is that uh agent infrastructure is quite similar to from uh like data infrastructure software because there's a lot of problems that you need to solve in the runtime side. Is where the session would be durable store and how you resume the entire uh agent runs from uh failures, and where do you keep your credential and making

**[1:46](https://www.youtube.com/watch?v=c7R5KmY532c&t=106s)** sure the credential is not leaked into uh your AI agents, and how do you uh attribute the cost, and as well as do uh put a a of barriers to making sure agent is uh under control. And that's how we kind of looking into the entire agent runtime. And we build an open source project called Orca. Essentially is if you're using Anthropic manage agent, you know, it's a hosted services running in Anthropic side. And also it ties to only one open one tied to one specific model, specific honeys. And the Orca project essentially is building an open manage agent runtime. So you can run any honeys using any models. And we'll put

**[2:35](https://www.youtube.com/watch?v=c7R5KmY532c&t=155s)** all the plumbings around how the agent can execute, how agent can recover, and as well as all the guardrails that we'll put together to making sure you able to enforce certain policies no matter is a permission policy or cost control policies towards the agent. And this talk is more sharing a couple lessons that we have learned in building out this open source manage agent runtime. So to get started is like agent itself is a very simple. It's a reasoning loop. So you just put reasoning loop into a honeys and honeys will driving the entire reasoning loop for the agent to do execution calling tools, maybe producing results. But in order to put the agent into

**[3:24](https://www.youtube.com/watch?v=c7R5KmY532c&t=204s)** runtime to run in a governed way, you have to consider many different things. And that is an infrastructural problem that we have been dealing with for a couple years when we dealing with the data infrastructure. So we apply some of the principles here to solving the agent runtime problem. But before getting into the lessons that we learned, the first thing I want to talk about is when you think about providing a runtime for AI agent, you we kind of categorize all the problems into three category. The first one is because now nowadays I think everyone probably receive an expensive AI bills from some AI AI model providers there. But the the most important thing is how you can attribute the your cost spend

**[4:13](https://www.youtube.com/watch?v=c7R5KmY532c&t=253s)** across different like your agent, your individuals and even your sessions like different task. might be using different like models and how does this cost can be attributed across different entities there. Second Second thing is if you want to put agent, especially if you want to moving agent from a demo environment or even in just a local agent towards production that is running 24/7, you need to making sure you have a control. You you you want to making sure it can only access certain resources that you can access. And you need to have the control including the permission control. You cannot access get out of out of control is the access the

**[5:00](https://www.youtube.com/watch?v=c7R5KmY532c&t=300s)** resources they cannot supposed to access. And the control would also mean you also need to cost control the cost because you don't want in order to run an agent and your like the entire AI bill skyrocket uh uh there. So that's the control. And the last thing is the choice is because the AI model is commoditized like every day like every almost every week you will see a new model coming out. It's getting better and better. And also there's also different harness on the market. You you have cloud, you have answer up, codex, you also have pie, many of the different open source harness there. So you want to have a choices to switching between different models, even switching between harness because some model might

**[5:48](https://www.youtube.com/watch?v=c7R5KmY532c&t=348s)** be working well with some honeys, and some of the honeys working perfectly for coding task. Some of the honeys might be working some of the daily routine works. So, you want to have that flexibility to switching between models and honeys, but at the same time you want to making sure your runtime doesn't need to change. All the plumbings that you did on the infrastructure layer, including sandbox, carrier, should just remain the same. You should not rebuild the entire infrastructure because you're just switching honeys. So, with all this, we kind of put all these together building an like runtime. We have five lessons that we learned from building this runtime. Sorry. So, first thing is if you're looking into a running agent,

**[6:37](https://www.youtube.com/watch?v=c7R5KmY532c&t=397s)** it usually kind of including five pieces. So, you first you have a brain, which is the model. Then you have the loop, which essentially is the honeys, which could be cloud SDK, codex SDK, or even pie. And you want the entire agent running in the isolated secure environment, and that is where the sandbox that you're putting the agent to run. But at the same time, you also want to keep the entire working state, which it will be the memory or even a just a workspace for the agent to work on. But at the same time, agent itself is not just a loop. It has to access your like tools, your database, your many different like systems in order to achieve like a goal that assigned by the human. So, in order to making sure agent to successfully or securely access those

**[7:27](https://www.youtube.com/watch?v=c7R5KmY532c&t=447s)** tools, you you want to go through a certain AI gateway, and that is the door for agent to access your system. So, putting all these together, if you're looking into the lessons, the first thing that we have learned one of the principle here is that we have to speed like brain, hands, and session into kind of three different pieces. So, we don't you don't want your hands is running together or you don't want to put everything together into one environment because model is so smart, it might be able to bypass the everything to get get around the kind of the guardrails you put together. So, the first thing we do is that speed brain, hands, and session. So, brain itself is your agent loop. Essentially, it's the loop you are

**[8:15](https://www.youtube.com/watch?v=c7R5KmY532c&t=495s)** interacting with large language model for reasoning. And you put the entire hands, which is your working area, into more like a isolated environment for like a secured execution. Usually, it would be a sandbox, but it also sometimes it also meaning you are when you're calling a certain tools, you want to go in through a gateway, so you have a centralized control with that is your hands. And for the sessions is that where you want to kind of keep all the running state that your session log, the access to the resources, and also the memory generating out of this session. So, we kind of speed this into three different pieces. In that way, it will give you a benefits that you can swap out each other without changing the the rest. Like for example, in this

**[9:04](https://www.youtube.com/watch?v=c7R5KmY532c&t=544s)** model, we can swap a Codex agent with an agent written by like Anthropic Cloud SDK without changing the hands and sessions. And similarly, if you want to switching the uh gateway implementation or sandbox implementation, you can also swap that out without changing the brain in the in the session. It's just because those will be separated into different components. So, that's the first lesson, and it's the it will making your entire runtime become modular, so you can you can build a open ecosystem which each component can be pluggable with different implementations. Second, a runtime is different from a harness. Harnesses usually need to

**[9:53](https://www.youtube.com/watch?v=c7R5KmY532c&t=593s)** managing a lot of this complexity of context because they need to deal dealing with different context window. It need to do compaction and and need to do summarization to making sure that the entire agent loop can running effectively using the large language model and there's tons of the kind of great harnesses out there, Codex, Claude, Pi or even many other kind of open source harnesses there. But the runtime itself is all about how you keep your session, how you resume from a failure and how do you have a policy to enforce the entire agent agent loop. So, all these will be separate out as a its own runtime. In in In this model is that

**[10:43](https://www.youtube.com/watch?v=c7R5KmY532c&t=643s)** we're pushing all the context management to get towards the harness and this will give us the flexibility to swap out different harnesses without changing the rest of the infrastructure. So, that's the second lesson and the benefits getting out of this is that if Codex evolve with its model, then it has better context management, it it become smarter than we can swap the the harness easily without changing the infrastructure. The last thing is the session itself. We are kind of model it as a session lock and then so you don't need to kind of re keep the session in different implementation. You just put the entire session in the share session lock storage, so you you can resume the state by replaying the lock. And lastly is

**[11:32](https://www.youtube.com/watch?v=c7R5KmY532c&t=692s)** if you want to put guardrails or AI agent, you don't want put the guardrails inside where the agent is able to run. You want to put the limits outside. So, usually this will be enforced in the gateway or the actual execution layer. And the last last one is the obvious very kind of common one is that you should not put great credential directly into a sandbox directly into a where agent can run. You you need to kind of put the entire credential outside of the agent agent run and you can use maybe a credit concept called vault and then you can just use the vault ID to access and then then all the gateway and runtime will handle how to resolve the credential correctly. And last lastly,

**[12:22](https://www.youtube.com/watch?v=c7R5KmY532c&t=742s)** we do believe budget should be also a guardrail is because as AI spend is so crazy nowadays, so you you want to enforce making sure your session run doesn't kind of existing your budget there. And so, putting all these together, all these five principles is actually pieces together to solve the three problems that we talked about making cost under control and you have choice to to switching between models and honeys. This is a overview, but we do I know we are running out of time. So, we have a booth that is 133. If you're interested in talking to us, you can come to our booth. This is a also an open source project. You can download it. You can run locally. You can also host it in your

**[13:10](https://www.youtube.com/watch?v=c7R5KmY532c&t=790s)** like Kubernetes environment and then using you can use the class like manage agent API to interact with them directly. So, give it a try and we we are welcome for the feedback. And thank you for the time. >> The queen of England.
