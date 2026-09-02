---
id: bCKYMspL-pc
title: "Startup Spotlight - RELAI"
slug: startup-spotlight-relai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Startup Spotlight"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-10T05:22:22Z
video_id: bCKYMspL-pc
url: https://www.youtube.com/watch?v=bCKYMspL-pc
youtube_url: https://www.youtube.com/watch?v=bCKYMspL-pc
tags: []
transcript: true
---

# Startup Spotlight - RELAI

**Startup Spotlight**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=bCKYMspL-pc) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*767 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=bCKYMspL-pc&t=2s)** SOHEIL FEIZI: Hi, everyone. My name is Soheil Feizi. I'm founder and chief scientist at Relai. I'm also an associate professor in the computer science department at University of Maryland. So today, I'm going to tell you about verifiable continual learning for AI agents. Agents in the world, they interact with diverse users, tools, and data. The goal of continual learning is to continuously improve the agent using its experience without regression. This learning can happen in the model layer, in the harness layer, or in the memory layer. Unfortunately, current approaches are heavily manual, inefficient, and tedious. Mainly, it involves manual inspection when we're basically seeing a failure in agent behavior, and maybe asking a coding agent to change the target agent.

**[0:54](https://www.youtube.com/watch?v=bCKYMspL-pc&t=54s)** So it is vibe-based. It is unclear if the change is effective and whether or not it creates hidden regression in other samples. Other approaches based on prompt optimizers or harness optimizers, they are applicable when you have benchmarks, not real logs from the agent. They are also prone to shortcut learning and overfitting. We address these challenges at Relai's verifiable continual learning engine. Here is in a high level how it works. So we first turn every signal from agent behavior into replayable learning environments to simulate and evaluate those behaviors. So this becomes the foundation of verification, because not everything becomes testable.

**[1:46](https://www.youtube.com/watch?v=bCKYMspL-pc&t=106s)** We then do a holistic root cause analysis to find the smallest durable change, and we pass that to our lifelong agent optimizer that has in loop regression control to improve the agent without creating regression. All done in an efficient manner, so that this loop can run frequently. You can use Relai's VCL, verifiable continual learning, in your agent just using a couple of commands. So imagine you have an agent and in that agent repo you initialize Relai. So that scans your repo and creates a learning harness for you. This is a one-time job. Then just using one command, Relai learning environment

**[2:35](https://www.youtube.com/watch?v=bCKYMspL-pc&t=155s)** create, you can create a very rich learning environment for your agent based on that signal. That includes learning personas, potentially mocking tools, as well as learning verifiers and evaluators based on that scenario. And then you can call Relai optimize to improve your agent without creating regression. That creates a pull request for you. And you will see the changes and the reason for changes in your agent harness, and your agent memory, and other aspects of your agent. Let's see how it actually works in action. Imagine you have a customer support agent, and you want to understand how it works in a scenario when you have an adversarial user in a multi-turn conversation who wants to get some refund that is unauthorized,

**[3:24](https://www.youtube.com/watch?v=bCKYMspL-pc&t=204s)** you can describe this scenario and create a learning environment just using one command. Or let's say you already have a log that didn't work. Your agent didn't work well, and you have a feedback on top of it, you can do the same. This will create a learning environment with simulators and evaluators for you. You can run the simulation, execute the simulation to see how your agent actually works. And in this case, you see two evaluators. They show low scores. Then you can call Relai optimize with a certain budget with respect to the number of rollouts to improve your agent without creating regression in other samples. In order to systematically understand the performance of our agent optimizer, we evaluated it on a continual learning

**[4:14](https://www.youtube.com/watch?v=bCKYMspL-pc&t=254s)** version of terminal bench. In this experiment, we created two phases. In the phase one, we exposed 12 hard tasks. And in phase two, we expose 10 hard tasks for agent optimizers. And the goal is to understand whether optimizers compound. If you're optimizing on phase one, and then you're re-optimizing on optimized agent, does it compound? And we see methods like Meta-Harness and GEPA improves a little bit over baseline. But with further inspection, you can see they either do not continuously improve or they have negative transfer from phase one to phase two. When we apply Relai, we see significant improvements over the baseline and these other methods. That is verifiable continual learning in a nutshell,

**[5:03](https://www.youtube.com/watch?v=bCKYMspL-pc&t=303s)** where every failure becomes a test, every change is measured, and every improvement is verified. The good news is that you can use it today. If you go to relai.ai and as a courtesy to this conference, if you use the promo code RDI2026, you will get a $500 worth of Relai credits in order to use VCL in your agents. Thank you. [APPLAUSE]
