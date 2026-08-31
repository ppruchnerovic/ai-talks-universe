---
id: LdQpoK2TzSo
title: "Introducing Managed Deep Agents | Interrupt 26"
slug: introducing-managed-deep-agents-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 18
published_at: 2026-05-29T13:06:00Z
video_id: LdQpoK2TzSo
youtube_url: https://www.youtube.com/watch?v=LdQpoK2TzSo
tags: ["Managed Deep Agents", "Deep Agents", "LangChain", "LangSmith", "LangGraph", "agent harness", "agent in production", "LangSmith Sandboxes", "Context Hub", "human in the loop", "sub-agents", "agent memory", "durable execution", "agent checkpointing", "agent interoperability", "Agent-to-Agent protocol", "production AI agents", "LLM agents", "multi-agent systems", "agent orchestration", "long-running agents", "Interrupt conference", "building AI agents"]
transcript: true
---

# Introducing Managed Deep Agents | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `18 min`

`#Managed Deep Agents` `#Deep Agents` `#LangChain` `#LangSmith` `#LangGraph` `#agent harness` `#agent in production` `#LangSmith Sandboxes` `#Context Hub` `#human in the loop` `#sub-agents` `#agent memory` `#durable execution` `#agent checkpointing` `#agent interoperability` `#Agent-to-Agent protocol` `#production AI agents` `#LLM agents` `#multi-agent systems` `#agent orchestration` `#long-running agents` `#Interrupt conference` `#building AI agents`

[Watch the recording](https://www.youtube.com/watch?v=LdQpoK2TzSo) · [Conference site](https://interrupt.langchain.com/)

## Description

At LangChain's agent conference Interrupt, we announced Managed Deep Agents in private beta, an API-first hosted runtime for creating, running, and operating deep agents.

Deep Agents gives developers an open-source harness for building agents that can plan, use tools, delegate to subagents, write files, and work over long horizons. Managed Deep Agents gives those agents a durable home in LangSmith.

With the Managed Deep Agents API, you can create, update, manage, and run agents programmatically from your own application or internal platform workflow.

In this Interrupt 26 keynote, Sydney Runkle and Victor Moreira demonstrated what's new in LangChain for building and deploying Deep Agents in production.

Introducing Managed Deep Agents | Interrupt 26
00:00 Introduction: Sydney and Victor
00:20 What is an agent? Model + tool-calling loop
00:42 What is a harness? Defining the concept
01:07 The harness: skills, memory, tools, sub-agents
01:10 Job of a harness: right context at the right time
01:26 Why you need a harness: five agent requirements
02:14 What is Deep Agents?
02:26 The four capabilities of the Deep Agents harness
02:35 Capability 1: Execution environment and file system
03:53 Sandboxes and code interpreters
04:48 Capability 2: Context management
05:15 Summarization, context offloading, and memory
05:47 Prompt caching and skills (progressive disclosure)
06:43 Capability 3: Delegation and sub-agents
07:20 Why sub-agents matter: isolated context and parallelization
08:06 Capability 4: Human-in-the-loop steering
08:35 Four human-in-the-loop decision patterns
09:03 Why Deep Agents: provider-agnostic, customizable, middleware
10:25 Going to production is hard — handoff to Victor
10:52 Introducing Managed Deep Agents (private beta)
11:19 The four pillars of Managed Deep Agents
11:38 Pillar 1: Runtime — built on LangSmith deployment
12:23 Durable execution and checkpointing
13:13 Security and auth layers (RBAC, ABAC, MCP tools)
14:03 Agent interoperability: remote graph, Agent-to-Agent protocol
14:37 Bringing agents where you work
15:07 Pillar 3: Context Hub integration
15:51 LangSmith Engine integration
16:12 Pillar 4: LangSmith Sandboxes
16:53 Auth proxy and snapshot/restore
17:07 Wrapping up: private beta and waitlist

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Introducing Managed Deep Agents: https://www.langchain.com/blog/introducing-managed-deep-agents
• About Deep Agents: https://www.langchain.com/deep-agents
• About LangChain: https://www.langchain.com/

## Transcript

*2,855 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=7s)** Hi folks. I'm Sydney and I am an open source engineer at LangChain. Hi, I'm Victor. I'm a product manager. And today we're going to be walking through managed deep agents. But before we talk about that, Sydney's going to walk us through deep agents as a harness. So, first off, what is an agent? An agent is a simple model and tool calling loop. A model calling tools in a loop until it completes a task and returns a final result. What is a harness? We can define a harness as or we can define an agent as a model plus a harness. So, the harness is everything that connects the model to the real world. Everything around the model that helps

**[0:54](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=54s)** it complete tasks. So, this is made up of skills, memory, the base system prompt, tools, sub agents, and any additional context. What's the job of a harness? So, the job of a harness is to get the model the right context at the right time for the given task. A model is only as powerful as the context that it's given. And so, the harness exists to bridge this gap. Why do you need a harness? Well, agents have a lot of jobs. Agents need to work in an environment where they can take actions. This action taking is what gives them agency. That's what makes agents useful. They need to connect to your data so

**[1:44](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=104s)** that their actions are relevant for your use case. They need to manage growing context over long runs so that they can avoid context overflow. They need to be able to parallelize tasks to complete complex tasks efficiently. They need to connect with a human in the loop for sensitive workflows. And finally, ideally, they improve over time so that they remain relevant and useful. So, what is Deep Agents? Deep Agents is a customizable agent harness that's purpose-built for complex real-world tasks. First, I'm going to cover the four main capabilities that are part of the Deep

**[2:31](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=151s)** Agents harness, and then we'll do kind of a deep dive into each one. So, first up, we have the execution environment. This is the backbone of a Deep Agent, and it all starts with the file system. Optionally, you can also augment this with a sandbox or, similarly, a code interpreter. Next, we have, I think, the most important capability, uh, which is context management. So, there are lots of utilities built into Deep Agents that help with this tall order. That includes skill support, out-of-the-box support for short- and long-term memory, summarization capabilities, context offloading, and prompt caching. The third capability is delegation.

**[3:20](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=200s)** As agents run for longer amounts of time and take on complex workflows, they need to be able to plan and organize tasks, and then also use sub-agents to get delegate work. Finally, we build steering into the Deep Agents harness with first-class human-in-the-loop support. So, now for our deep dive. Starting with the execution environment, which I mentioned is the backbone of a Deep Agent, this capability powers all of the rest. So, we start with the file system. An agent uses a file system to read and write scratch files as it tackles work, load and store persistent memories in the hot path, invoke skills when relevant for a given

**[4:09](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=249s)** task, and many more things. Agents are excellent at using file systems. They are trained in a an environment to use file systems, and also trained on lots of code. And that's why giving an agent a sandbox, or lighter weight cousin, the code interpreter, is very powerful. When you give an agent these code execution tools, you give it a secure environment to write and run code, which makes an agent capable of much, much more creative problem-solving, um and kind of dynamic run-time behavior. The second capability is context management. Deep Agent ships with built-in summarization and context offloading.

**[4:58](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=298s)** You can see on the graph here, periodically, Deep Agent will evict large messages, so that can be human messages, tool results, tool calls, to the file system so that we don't build up context in the window too quickly. Additionally, summarization is triggered less frequently, but every so often when the history starts to approach the model's context limit. Both of these are in an effort to avoid context overflow, which is a problem that plagues long-running agents, or high-context agents, or both. Deep Agent also ships with built-in memory support. I would argue that memory is maybe the most important kind of context, because it's the context that changes from run to run, and allows your agent to improve over time.

**[5:48](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=348s)** It also ships with provider agnostic prompt caching. This is incredibly important for long-running high context agents that need to operate cost-effectively. Finally, Deep Agent ships with skill support out of the box. Skills are part of the context management system um because of a system called progressive disclosure. So, Deep Agent loads some minimalistic information about what skills your agent has available up front into the system prompt. And then we give the agent the power to dynamically pull in full skill resources and invoke those skills in their scripts when relevant for a given task. All of this this umbrella of context management is again catering to that need for a harness to

**[6:36](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=396s)** get the model the right context at the right time for the given task. The third capability of the Deep Agent harness is delegation. So, the Deep Agent harness is equipped with a planning tool that allows the model to organize work for challenging tasks. It's also equipped with sub agent support out of the box. Sub agents can be general purpose or specialized. So, for example, if you were building a coding agent, maybe you would want to attach some specialized sub agents for architecture design, for code review and security review, and then test writing and execution. Why are so Why are sub agents so important?

**[7:24](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=444s)** Well, first, they operate with isolated context, and they actually help with overall context management. So, when you when the main agent invokes a sub agent, it starts with fresh context only relevant to its given task, and then it returns just a streamlined final result back to that main agent so that it doesn't pollute the main context window. Secondly, they can be used to parallelize work. So you your agent can run tasks end-to-end more efficiently with that parallelization. Finally, sub-agents can use any model and any provider. So you can match model capability with task complexity. The fourth and final capability of the Deep Agent harness is support for steering

**[8:12](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=492s)** via first-class human-in-the-loop primitives. So human-in-the-loop is really critical for two things. The first is getting real-time user feedback on sensitive actions or tool calls as we mentioned before. And the second is getting real-time feedback when feedback is needed from the user to unblock the model. So what does this look like? There's four common decision patterns that we build into Deep Agents. The first is an approval flow. So maybe you're approving an email before it's sent. Second is an edit. So maybe editing a tweet before it's published. The third is a reject decision, rejecting a proposed financial transaction. And the fourth is the respond pattern. So that's when the agent interrupts and asks the user for a question to unblock

**[9:00](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=540s)** its future progress. So we've done a deep dive into the capabilities of the Deep Agent harness. Now let's talk about why Deep Agents. Deep Agents is provider agnostic. You can use any provider and any model, swap it anytime, and even mix and match. Your main agent can use a different model than your sub-agents. You can use major providers like Anthropic OpenAI Google. You can use local models with Ollama. Or you can use the increasingly performant and much cheaper open-source models like Fireworks from providers like Fireworks, Nvidia, Open Router, Base Ten. Deep Agents is highly customizable. Here's a quick recap of what that core

**[9:50](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=590s)** agent loop looks like. And here's what the Deep Agents loop looks like. Deep Agents provides a set of hooks around the core agent loop. We call this system middleware. And middleware enables basically any custom logic that you want to add to your agent. That might look like bespoke business logic, deterministic code at any point, policy enforcement like PII reduction, or dynamic agent control. For example, changing the model and tools available at runtime based on the task at hand. Even with a capable harness, going to production is really hard. Your agent needs to run for long periods of time and recover from unexpected failures, handle human in the loop and

**[10:37](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=637s)** unpredictable behavior, support bursty traffic, all while maintaining a secure posture, and keeping up with ever-changing interoperability standards. And now, I'm going to hand it off to Vic, who's going to cover how we make this easy. Awesome. Thank you, Sydney. All right. So, we just saw what a Deep Agent is. Now, we're going to talk about what it takes to actually take one of these Deep Agents into production. I see a few familiar faces in the crowd of people that have actually taken these agents and served them to customers in production. Um so, we've kind of seen this firsthand. Today, we're going to talk about how we're introducing managed Deep Agents in private beta in order to make this process as easy as possible. So, there's kind of four core pillars to what managed Deep Agents are. First is the harness, which Sydney just walked

**[11:24](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=684s)** through. The second is the runtime, which is how we can actually use this agent in production. The third is going to be an integration with context hub. And then lastly, the way that we can execute safe code in a sandbox. So, let's first talk about this runtime. So, managed deep agents is actually built on top of LangSmith deployment, which means we get a lot of primitives to handle that real-time kind of interaction and scalability that agents will actually need in production. This means we get endpoints for creating, updating, even invoking our agents wherever we need them. We'll get a purpose-built task queue and horizontal scaling in order to handle kind of the bursty request loads that your agents might experience. You can imagine a use case of support agent, your systems go down, and now everyone's hitting that support agent all at once. You need to be able to

**[12:11](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=731s)** handle that traffic well. Lastly is SDKs in order to use these agents wherever you need them, integrations with Copilot Kit, Assistant UI for Gen UI, the list goes on. The second kind of core pillar of this production runtime is durable execution. This is one of those things that is a little boring to think about, but it is very, very reliable in production. So, because we run deep agents on top of the LangGraph runtime, we're able to actually checkpoint each step that your agent takes in production. This means that these are all stored in durable storage, and we can resume and restart from any one of these checkpoints. So, if your agent fails on step 49 of 50, you don't have to restart that whole run again, you can pick up and retry from from step 49. Lastly, we have the ability to replay and fork our agent from any point in time with that state.

**[12:58](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=778s)** This enables some advanced use cases where we're close, so you know, something like, "Oh, I want to I want to fork this conversation from here." But it also enables human approval through human in the loop. Since everything is checkpointed into this database, we're able to await human input indefinitely. This is what enables ambient agent use cases such as LangSmith engine, which you hear about in the next session. Security and auth are very, very important to production agents. You need multiple layers of auth in order to kind of serve these production agent use cases. The first is going to be inbound from your actual application. How do you authenticate that this user is who they say they are and they're allowed to use this agent? The second is going to be outbound from inside the agent to your external services. You might have tools or MCP tools that you need to be able to reliably authenticate with and assume the correct permissions at runtime.

**[13:46](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=826s)** The third is actually who has the ability to create, update, and manage these agents. Whether it is your AI engineers internally or maybe your CTO wants to get in there and make a quick change, you need to have that level of R back and A back to enable who actually has permissions to make these changes. >> [snorts] >> Agent interoperability is becoming more and more important as you want to use your agents in a variety of different use cases. One thing that's core to LangSmith deployment that we're bringing in to manage deep agents is the ability to use your agent via remote graph. That means that you can call your agent that is built on managed deep agents in a custom LangGraph application that's deployed on LangSmith elsewhere in just one line of code. Second is the ability to support A to A protocol. So, a lot of agents are using A to A today as a way to kind of handle this agent to agent communication layer and we support this out of the box in

**[14:33](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=873s)** both our standard LangSmith deployment and also managed deep agent. The third is being able to bring this agent where you actually do work. We have a lot of agents that we build internally and deploy on LangSmith deployment and we'd love to use them where we're doing work. Whether it's deep agents code or it's Cloud Desktop, you want to be able to bring this agent and use it where you need it. We thought of all of these different production use cases so that you don't have to. Things like double texting, canceling a run mid-flight, are all things that actually take real engineering work and will take you weeks if not months to build. We have this all out of the box for you. The third kind of core pillar here is the context of integration. Oop. So, Context Hub is built into managed deep agents and it's how we version and save every one of these files that your agent actually

**[15:21](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=921s)** operates and runs on. So, things like the agent MD and the skills that Harrison mentioned during the keynote are becoming more and more popular. Memories that your agents is taking about your users, these all get saved and saved in version inside of Context Hub so that your team is able to control different different levels of promotion, right? Like we can start in staging, go to production for different skills, things of that nature. And you can really democratize these skills across different agents. The next kind of core feature that is part of Context Hub in this managed deep agents primitive is our integration with LangSmith engine. You're going to hear more about LangSmith engine in the next session, but essentially what it'll be able to do is take real production usage of these deep agents, make some quality improvements, some changes to your prompts, your system or your skills, things of that nature, and that'll lead to better behavior over time as this

**[16:08](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=968s)** loop in this engine continues to build. The fourth kind of key component of managed deep agents is sandboxes. So, as Sydney mentioned before, increasingly nearly every agent is becoming a coding agent. Even a research agent use case, they might want to be able to crunch some quick stats and add them to a report. You want to enable your agents to do these things in production because it can lead to a lot more creative results. That's why we're launching LangSmith sandboxes and we're integrating them directly with managed deep agents. There's a few core features to this kind of LangSmith sandbox primitive. The first being an off proxy in order to at runtime inject in those credentials that your sandbox is using securely so that none of your important environment variables are exposed the actual agent or the actual sandbox itself. And the second is the ability to snapshot and restore so that your agent

**[16:57](https://www.youtube.com/watch?v=LdQpoK2TzSo&t=1017s)** always has the correct execution environment. We'll have a session on this for a deeper dive tomorrow with Mikhail, but they are very very excellent for most agent use cases. So, this is kind of everything that you need all together in order to take an idea or a working deep agent and take it into production. That's why we're launching managed deep agents and we're starting the private beta as of today. So we encourage you all to jump on the wait list and thanks for the time. >> [applause]
