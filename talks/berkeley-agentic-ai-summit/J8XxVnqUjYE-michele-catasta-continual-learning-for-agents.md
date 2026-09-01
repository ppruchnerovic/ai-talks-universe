---
id: J8XxVnqUjYE
title: "Michele Catasta - Continual Learning for Agents"
slug: michele-catasta-continual-learning-for-agents
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Michele Catasta"]
channel: "Berkeley RDI"
duration_min: 7
published_at: 2026-08-09T18:48:53Z
video_id: J8XxVnqUjYE
youtube_url: https://www.youtube.com/watch?v=J8XxVnqUjYE
tags: []
transcript: true
---

# Michele Catasta - Continual Learning for Agents

**Michele Catasta**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `7 min`

[Watch the recording](https://www.youtube.com/watch?v=J8XxVnqUjYE) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,353 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=2s)** MICHELE CATASTA: Hi, everyone. So today, I want to tell you about continual learning, which is often a concept that you hear associated to model training. And it's been sort of Holy Grail that we have been chasing as a research field for such a long time. We don't want AI systems that are static. We want AI systems that learn from the usage. It turns out, though, that a lot of companies are today using Clausewitz models. So when you don't have access to weights, how do you make your AI system actually evolve? Well, it turns out there is another answer, which is exactly what we have been doing at Replit for many months and is putting your hands directly on the harness, around the ecosystem, around the agent that you're running. So how do we do that? Well, as an industry, we have been relying on evaluations for so long. And benchmarks are amazing.

**[0:49](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=49s)** I really appreciate people working on them. The output is very crystal clear. You run your eval, you get a number, and you decide if your harness changes have actually made progress or actually introduce a regression. But there is a lot of signal missing when you do that. Evals are, by definition, very narrow. They capture only a subset of capabilities that you are basically exposing your agent on. So there is something amazing that happens once you hit product-market fit as a product. The amount of sheer usage that your platform receives is such that you're sitting on a gold mine of data. And that's a gold mine of data that oftentimes we immediately associate to immediately starting to do model training. Well, there is far more that can be done with that. It turns out that if you analyze the traces, you can learn what works, what doesn't work,

**[1:38](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=98s)** why users are annoyed by your agent, and many other things. So our approach has been creating two different pillars-- of course, relying on evaluations very much, but at the same time, continuously running A/B testing as well as analyzing the traces in real time to really understand from the data what is actually working correctly and what we should immediately improve. So the reason why I put so much emphasis on the continual learning aspect is also because the amount of signal that you collect, the more traffic you receive, the more you basically-- the gap is in terms of orders of magnitude. So your evals are fixed in size. We recently launched our own benchmark called ViBench. It's an end-to-end vibe coding evaluation. And we're having a few tens of applications. So we already know exactly how our agent will behave on them.

**[2:29](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=149s)** What we experience instead on a daily basis on our production system is a series of long-tail events that we can't really predict. And those long-tail events are actually golden because they tell you how users are pushing the boundaries of your product, and at the same time, usually those behaviors that break what you intended to make work correctly. I don't know if many of you have run A/B tests in your career. It depends on maybe your seniority in the industry. But they are not the silver bullet that sometimes we are led to believe, in the sense that more often than not, A/B tests look like this. There is not a clear result out of them. You run an experiment, you decide to manipulate your harness in a specific way, and then certain metrics that you're tracking are actually improving and some others are dropping.

**[3:18](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=198s)** What is going on here? It could be that you're maybe optimizing for costs, and then the capabilities of the agents are dropping. You might be optimizing for speed, and then the sentiment of the users is evolving. You'll never get a crystal clear answer that allows you to immediately ship the change in product. So it turns out that the right approach is to literally take all the production workload that you have. And at first, rather than analyzing every single trace-- because, as you can imagine, we have millions and millions of these every single day, and it will be prohibitively expensive and also slow. The first step is we actually cluster them. I'm talking about very basic machine learning techniques, where you find the semantic relevance among these traces, and the vast majority of them will be discarded because they are sort of like intended behavior.

**[4:08](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=248s)** But every now and then, every day, we see few clusters popping up that really highlight some new tail behaviors that we never experienced on the agent. And we built a system after this clustering step that practically takes every single anomalous trace, runs it through our analytics system, which, as you can imagine, includes frontier models LLMs, understand what went wrong, and then immediately generates a PR. Now, what you still have to do as an AI engineer-- I want to give like a picture of the world where the work that we do is actually still extremely relevant. I don't think this is going to be automated in the next few months at the very least. What's happening here is that once you have this series of PRs and you try to apply them, you will be

**[4:55](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=295s)** running A/B test at that point. And some of them will not be conclusive, as the screenshot that I showed before. So as a person who leads an AI team, your choice will be defining which kind of these changes should be actually go in production versus which one should be waiting or should be completely dropped. So there is still a level of human decision process, even though the vast majority of the changes that we produce for our harness are actually completely generated by our AI system. And this is something that I started to talk about only a few months ago, because even though in principle, this kind of pipeline is something that we could have built long ago, in practice, frontier models have become extremely good at analyzing traces only in the last six months or so. So the same revolution that you experienced as software engineers, where a lot of the code is actually written today by agents,

**[5:43](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=343s)** we are experiencing as well on this side of the world on the production workloads. I want to give you a real example so that instead of keeping this very abstract, you can understand what kind of problems this can catch for us. At Replit, every single day, we spawn hundreds of thousands of virtual machines for our users. We do that completely transparently. And we had a long-tail bug where, at times, it took longer for our virtual machine to be fully booted than for our agent harness to be ready to go. As you know, agents are very eager to debug problems. So the few times that it was happening, our agents started to spin the wheels and try to realize why it wasn't able to execute code, why it wasn't able to run certain tools. Now, agents are fundamentally nondeterministic, which

**[6:31](https://www.youtube.com/watch?v=J8XxVnqUjYE&t=391s)** means every single trace didn't showcase the same type of errors, because the agent decided to use different type of debugging strategies. But all of them had in common the idea that the virtual machine wasn't booting fast enough. We would have never spotted this just by analyzing the logs manually. It would have never shown in our Datadog dashboard, for example, because it was a long-tail error. But after we cluster everything, we realized this was happening often enough, and our system immediately generated a PR and fixed the problem on the spot. So the takeaway that I want you to have today is that stop thinking about evaluation as just the last check before shipping. It's not like a Boolean flag that tells you I should be shipping my new PR or not. Rather, think of them as an engine that helps you to ship every single day a better agent. Thank you, everyone.
