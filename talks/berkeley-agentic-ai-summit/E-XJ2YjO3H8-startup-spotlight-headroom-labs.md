---
id: E-XJ2YjO3H8
title: "Startup Spotlight - Headroom Labs"
slug: startup-spotlight-headroom-labs
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Startup Spotlight"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-10T05:27:43Z
video_id: E-XJ2YjO3H8
url: https://www.youtube.com/watch?v=E-XJ2YjO3H8
youtube_url: https://www.youtube.com/watch?v=E-XJ2YjO3H8
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Startup Spotlight - Headroom Labs

**Startup Spotlight**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=E-XJ2YjO3H8) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*766 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=2s)** TEJAS CHOPRA: Hi, everyone. First of all, I'll waste some of the tokens here to thank everyone for sticking around on a Sunday afternoon. And folks that are watching online, thank you to them. And thanks to the RDI, as well as the summit, for having such wonderful speakers. I'm Tejas Chopra, I'm the founder of Headroom Labs, formerly at Netflix, working on recommendation infrastructure. So if you did not like a movie that you watched on Netflix, you can blame me for that. I'm building the context intelligence layer for agents. Today and yesterday, everyone spoke about agents, context, learning problems. Now, if you really want to imagine a future where there are hundreds of millions of agents in any enterprise, the first problem they will run into is the sheer amount of data

**[0:54](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=54s)** that they need to process and the context that they need to share. And we are trying to build a platform that makes it more intelligent. Agents don't have a reasoning problem, they have a context problem. When we were debugging some GPU problems using Cloud Code, we realize that 90% of the context was spent on reading garbage that was not important to the prompt. That is where we realized that the way context is filled with data today is fundamentally broken. And we wanted to solve that problem. Every tool call, every RAG, every MCP server that exists out there returns data to a model. And we try to sit in the middle, intercept that, and remove the bloat out of it.

**[1:43](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=103s)** Headroom is a local proxy. It runs on your laptop today. All you have to do is pip install a package. What it does is, when you're using your Cloud Code, Codex, cursor, any such agentic harness, it will look at all the data before it goes to a model, and it will remove the bloat without loss in accuracy. And the way it does that is it actually detects the type of data that is going to a model, whether it's JSON, whether it's code, and whether it is flat text. Now, you would wonder, if I'm just removing bloat, does that impact accuracy? Because the entire point is lost if accuracy is lost. We have benchmarked Headroom with SWE-bench and other benchmarks that are out there. And we see almost no loss in accuracy but significant drop in tokens.

**[2:34](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=154s)** The simple way to run headroom, run it as headroom wrap claude after you do a pip install. The one thing that we do differently from any other compression out there is we do it reversibly. Now, what does that mean? It basically means you squash something, but you put a breadcrumb there for the LLM. You tell the LLM, in case you need the original, here is a tool call you can make. That preserves accuracy, and it can still give you lots of savings. So where do we stand? We actually can compress 15% of the tokens on coding agents and 60% on data agents with all the accuracy held. We've run some benchmarks across code search, SRE, debugging, triaging, and code base. And you can see the numbers there.

**[3:23](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=203s)** We are actually seven months from our first release. And we are the number 1 GitHub repository for last month and this month. We are at 64,000 GitHub stars. More than two million developers use us. And we have more than 250 active contributors. People ask me, what exactly happened on June 1, when we went, suddenly, with the hockey stick curve? It was a culmination of factors, but mostly, companies realizing that token maxing is no longer important. It is all about value maxing. We have a bunch of Fortune 100 companies that use Headroom, like Yahoo, JPMorgan, Walmart, AT&T, and many others. But compression is just the wedge for us. We are trying to build context intelligence. Imagine a future where you're working with context

**[4:12](https://www.youtube.com/watch?v=E-XJ2YjO3H8&t=252s)** as an agent, and that context is suddenly available to a new agent to operate out of. This is context sharing. Today, if you have to share context between agents, the way to do that is using markdown files. We are trying to change that primitive. We are trying to define context via Open Context, our open spec for context management between agents. And that allows you to build knowledge graphs, governance, provenance of context. As agents scale, context is the bottleneck. And we are the layer that makes it efficient. I hope I used my tokens well today. Thank you so much for your time. [APPLAUSE]
