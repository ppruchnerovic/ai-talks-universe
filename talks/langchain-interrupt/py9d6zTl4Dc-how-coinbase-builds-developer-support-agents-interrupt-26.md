---
id: py9d6zTl4Dc
title: "How Coinbase Builds Developer Support Agents | Interrupt 26"
slug: how-coinbase-builds-developer-support-agents-interrupt-26
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 14
published_at: 2026-07-20T12:40:58Z
video_id: py9d6zTl4Dc
youtube_url: https://www.youtube.com/watch?v=py9d6zTl4Dc
tags: ["Coinbase", "Evan Cormos", "developer support AI", "Discord bot", "AI chat", "LangSmith", "LangChain", "Claude Code", "MCP", "RAG", "LLM-as-judge", "guardrails", "Slack triage", "agent engineering", "observability", "self-improving agent", "crypto developer platform", "multilingual adversaries", "intent-based development", "signal search", "agentic system", "Interrupt conference"]
transcript: true
---

# How Coinbase Builds Developer Support Agents | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `14 min`

`#Coinbase` `#Evan Cormos` `#developer support AI` `#Discord bot` `#AI chat` `#LangSmith` `#LangChain` `#Claude Code` `#MCP` `#RAG` `#LLM-as-judge` `#guardrails` `#Slack triage` `#agent engineering` `#observability` `#self-improving agent` `#crypto developer platform` `#multilingual adversaries` `#intent-based development` `#signal search` `#agentic system` `#Interrupt conference`

[Watch the recording](https://www.youtube.com/watch?v=py9d6zTl4Dc) · [Conference site](https://interrupt.langchain.com/)

## Description

Evan Kormos, engineering manager at Coinbase, shares how a small developer support team went from zero to a self-improving, customer-facing agentic system for crypto developers. The talk covers three live agents: Discord AI Chat (with deterministic guardrails and LLM-as-judge response evaluation), a Slack Triage channel that surfaces Discord signals internally with direct links to LangSmith traces, and a Support Engineer Assistant for internal case management. Evan describes the team's intent-driven workflow — using Claude Code with MCP tools for tech grooming — and their signal search process for back-testing traces to find improvement opportunities. He closes with three lessons: treat agent engineering as its own discipline, build the glass box before the agent, and remember that the team is the multiplier.

Chapters:
0:00 Introduction and what the Coinbase developer platform is
1:16 The support challenge: Discord, AI chat, and scaling for new markets
2:37 System design: delivery channels, Python services, and self-hosted LangSmith
4:49 Shared tools: remote MCP server for docs and RAG fallback
5:34 Overview of agents shipped: Discord AI Chat, Slack Triage, Support Engineer Assistant
6:22 Discord AI Chat demo: expert developer responses with guardrails
7:24 How guardrails work: deterministic safeguards plus LLM-as-judge output review
8:02 Slack Triage: surfacing Discord signals internally with LangSmith trace links
8:38 Support Engineer Assistant: internal case management surface
9:31 Intent-based workflow: Claude Code + MCP tools for tech grooming
10:37 Signal search: back-testing traces to find improvement opportunities
11:22 What we found: multilingual adversaries in production
12:08 Three takeaways: agent engineering as a discipline, glass box first, team as multiplier

Resources:
→ LangGraph: https://www.langchain.com/langgraph
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com

## Transcript

*1,901 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=6s)** >> Hello, Interrupt. What a great event so far. I want to try to set up a strong finish with the story of one of our teams. My name is Evan Kormos. I'm a builder and manager of engineering teams at Coinbase. Today I'm excited to talk about our developer support engineering team and describe the transformation of what and how we shipped to scale AI support for crypto developers. It's a story of how a small team was able to go from 0 to 1 on a self-improving, customer- facing agentic system. Onto the agenda. First, we'll frame up the support challenge and how we're scaling for Coinbase developers. Next, I'll discuss our approach for monitoring agent behavior. Then we'll dive into some technical details and describe

**[0:56](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=56s)** and show some of the capabilities and how they were produced. Throughout, I'll be referencing team members — our agent engineers — to describe how this transformation unfolded, supported by Coinbase infrastructure, leadership, and partners. First, a bit of setup so you know where we're coming from. The Coinbase developer platform powers a community of developers building on crypto APIs, wallets payments staking infrastructure — powering the on-chain economy. For a long time, our support model was people posting in our Discord server, and people answering in the Discord server. We added AI chat, and we'll talk a little bit more about that. Of course, this team is building with AI.

**[1:47](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=107s)** I know there's a lot of attention around this, especially with our company. But this is great, and I think it demonstrates our conviction to increase product velocity and quality. OK, let's dive into the challenge. In order to scale, we needed to keep being great for a developer who was working to ship a side project or a trading bot. But now we have new challenges as we have new markets and new expectations entering into our scope. For this team working together on a common goal to serve the customer is focused by our PM, Harry, who helps shape this work and prioritize. So to recap: our goal was to keep customer satisfaction high while increasing automation levels.

**[2:37](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=157s)** Let's get into the story. As I mentioned, we started with our version one Discord chat. We started like a lot of teams and integrated a hosted chat service. And honestly, the first version was fine. It answered developer questions. Sometimes the docs got stale. We had no way of knowing how people were using it. If it was doing a good job, we sort of had to manually tally the downvotes and the thumbs up and thumbs down. If you guys have done that before, you know where I'm coming from. So we really had no idea what was going on. A familiar situation. How do you stand up a new service that's as good as the one that you have — or ideally better — and gets better over time? It did require some new capabilities I'll talk about, paired with our existing paved roads. But the goal was to harness agent behavior.

**[3:35](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=215s)** Here's where we landed on system design. For delivery channels, we still meet customers where they are — in Discord and on the web — and on the backend, provide quality tools for support engineers. With an agentic foundation, we could build more: partner Slack channels, new MCP channels, generative UX — a lot is possible with this setup. A huge unlock for us was including Python services as first-class infrastructure. This was the team's first service of this type. We paired it with self-hosted LangSmith for tracing. A big driver of this transformation was Caesar, who is here today — you can chat with him. Where are you?

**[4:23](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=263s)** Raise your hand. There he is. All right. [laughs] A big driver. He set this up from proof of concept and brought these skills onto the team. For more stories like this, I'll give a plug for the Coinbase Engineering blog. Also a big thank you to our AI platform team who operates LangSmith and other infrastructure for our team and others to use. Finally, we have our own set of shared tools. A remote MCP server for developer documentation was used by the agent. For customer-facing agents, a remote MCP tool can be a bit unreliable. So what we did was add a RAG fallback. This is also a way for us to A/B test our own tool.

**[5:14](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=314s)** So behind the MCP, we have a pretty basic knowledge pipeline feeding the vector DB, which is the RAG fallback. Lastly, we hooked up to a variety of internal services, some event-driven, some proxying to external services. Bringing it all together. You have on-demand and ambient agent flows with our overall pulse on agent behavior. Building full stack and now adding AI — this team has already shipped agents within this framework, with more coming. The first three we'll showcase start with Discord AI Chat and Slack Triage. You'll see how both of these are helping shape progress toward Discord public auto-response. The Support Engineer Assistant is an exciting new surface for helping customers.

**[6:09](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=369s)** We'll take a look at that if you promise not to judge. We've also built or are building a handful of compliance, risk reduction, and service quality related agents. OK, so this is our Discord Support bot, and there's a menu where users can launch AI Chat, open a case, or open case management and other things. Soon the bot will be automatically able to respond on the channel when needed. Starting an AI Chat, a Discord developer can get expert responses to guide them with technical documentation or how to get further agent support. He is our team member that picked these skills up

**[6:59](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=419s)** and built a wonderful starting point for the Discord AI Chat you just saw. So we'll dive a little bit more into the detail of how we handle customer inquiries safely. So even though our agent doesn't have access to tools to transact or access sensitive data, you can see there was still a lot of care that went into detecting and preventing misuse. So when you hear the term guardrails, you can see there are deterministic safeguards in place. You can also see the developer documentation tool that we mentioned, which is needed for the initial version. LLM judgment was applied to the output using a lightweight model to evaluate the response for both accuracy and risk. This design was our starting point for public auto-response, and is also a way for us to safely handle customer inquiries going

**[7:52](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=472s)** forward. So, onto our next agent: the Discord Support Triage in Slack. I'll give you a second to check out the screenshots, but you can see within a Slack Triage channel, we have messages surfaced internally based on what's happening in Discord. We also have links that the team can provide directly into the LangSmith trace data on the initial version, as the classifiers are tuned. In the future, this can also serve as a lens and control plane to flag signals for improvement as part of the team's workflow, or to view and keep track of the agents in motion. All right.

**[8:39](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=519s)** Onto our AI Assistant. You can see here, within our service console, we have a new Support Assistant that we're trying out. It runs internally on a locally hosted React site. It allows the user to control the chat context based on what they can access in the underlying system. Initially read-only, we've set up the building blocks for human-in-the-loop and are excited to add functions like "send customer response" in the near future. Because this can be popped out in a new window, we can have a responsive UX and really control the experience very well. I'm excited to see where this goes and the potential for broader adoption and impact. OK.

**[9:31](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=571s)** So everything we do is intent-based. This is a little bit about the way we work. I'll give a plug for the Linear Slack bot. It does a great job of converting our conversational context to intent-based work. These tools may vary across teams. This is the way our team works. But everything we do is intent-based, like I said. Once we get the intent defined, we then go through a tech grooming process using Claude Code with a number of MCP tools to do deep research and begin planning and executing the work. We produce a number of code artifacts. Some could be system prompts and things like that.

**[10:20](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=620s)** They go through a rigorous testing, cross-model review, and evaluation step, and human approval, before outputting and resulting in a production system. From the production system, we get traces and real-time evals, as we showed from the prior graph. We can then use the LangSmith CLI and Claude Code to look at the traces, find signals for improvement, and drive more intent from that. So let's dive deeper. I'm calling it back-testing. Well, just looking at the traces. I think it's a great way to begin to improve starter evals — go live — and is a great way to use natural language to investigate your working system. For us to perform a signal search in our Discord Chat,

**[11:14](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=674s)** we built a basic process to look at the turns of the chat in a certain way — profiling them both randomly and deterministically. One example: we recently double-checked our security dashboards. What we found was applicable beyond just security. Deep-diving on specific threads, we were able to discover signals to improve or harden the system in various ways. On the topic of security testing, we thought an adversarial dataset would be good to have, but it turns out they're not easy to generate — due to the terms and conditions of some of the dev tooling. Also an observation: we almost immediately had multilingual conversations going on in our Discord — something we weren't prepared for. But with regard to adversaries, consider multilingual adversaries.

**[12:08](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=728s)** We still have some work to do on our automation numbers. Adding human-in-the-loop will really drive efficiency and provide more detailed levels of tracking, including how many tokens we're spending to resolve a customer case. Looking at this customer testimonial, I was excited to learn that we're helping customers build. It's incredible what AI enables a small team to build, truly. The hard part — making it work for the customer in a balanced system — is the combination of human and machine effort. I'd really take three things away. One: treat agent engineering as its own discipline. This was something Harrison really hit home on at last year's Interrupt, and something

**[12:59](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=779s)** we took to heart. We really need a balance of product engineering and ML mindset strengths across the group of people, not just an individual. Hiring and growing to balance these is super important. Two: build the glass box before you build the agent. Observability isn't a feature you add later. It's really the base layer and the starting point for everything else to materialize afterward. Three: the team is the multiplier. The team is the multiplier. AI lets a small team do extraordinary things, but only if they are aligned for collective execution. All right. I'd like to say thank you to everyone at LangChain and all the Interrupt sponsors for this great event. Thank you.

**[13:48](https://www.youtube.com/watch?v=py9d6zTl4Dc&t=828s)** [APPLAUSE]
