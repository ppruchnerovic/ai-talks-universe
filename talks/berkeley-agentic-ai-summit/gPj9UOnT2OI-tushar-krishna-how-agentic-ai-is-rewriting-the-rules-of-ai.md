---
id: gPj9UOnT2OI
title: "Tushar Krishna - How Agentic AI Is Rewriting the Rules of AI Infrastructure"
slug: tushar-krishna-how-agentic-ai-is-rewriting-the-rules-of-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Tushar Krishna"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T07:50:48Z
video_id: gPj9UOnT2OI
url: https://www.youtube.com/watch?v=gPj9UOnT2OI
youtube_url: https://www.youtube.com/watch?v=gPj9UOnT2OI
tags: []
transcript: true
---

# Tushar Krishna - How Agentic AI Is Rewriting the Rules of AI Infrastructure

**Tushar Krishna**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=gPj9UOnT2OI) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*836 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=2s)** TUSHAR KRISHNA: Thank you. I guess I'm audible. So we're at 1:45. I know it's officially the end of this session time. And my superpower as a professor is I can rush through any number of slides in five minutes, but I'll try to keep this short and talk you through about how agentic AI is rewriting the rules of AI infrastructure. So we've entered a new era of what's called tokenomics, where we essentially feed in AI workflows to our AI systems and out comes tokens. And essentially, there's a lot of metrics. We've started caring about things like tokens per second, tokens per what, tokens per dollar. Now, in this ecosystem where you have a workflow on one end and hardware on the other, the software stack that's really in the middle becomes very, very crucial to get token efficiency. Now, a lot of the inference-serving stacks that are out there today were really

**[0:49](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=49s)** built for the chatbot era. So essentially, their characteristics are they can run, typically, one model at a time, really optimized for static execution paths, each request is assumed to be independent, a lot of kernel optimizations, and the hardware is primarily homogeneous-- for the most part, GPUs. Now, of course, we are at the Agentic AI Summit. So the question is, what changes with agents? So there's two core things that we observe as emerging trends that are inevitable. So the first is around dynamism. So we've already heard a lot of talks. There's a lot of models. There's tool calls, dynamic fluctuating demands, interdependent tasks, and a lot of workflow-level optimizations. And the second key trend-- in fact, speakers before me also did a great job talking about this heavy heterogeneity.

**[1:39](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=99s)** So there's already a big use of CPUs for handling anything that's not an LLM. In addition, there's a lot of other hardware out there that is really specialized and optimized for different parts of the task. And what's also interesting is, in this agentic era-- this is, again, a data point I got from just a talk yesterday from Google, this 10 to 100x more computations compared to a nonagentic workflow. So again, the software stack becomes even more important. So it's important for us to now really try to understand what's going on behind the scenes. So if you try to demystify all of this, fundamentally, if you go down all the way from the workload to the model layer, to the software, to the hardware, there are essentially choices across the stack. There are tons and tons of choices and optimization

**[2:27](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=147s)** opportunities throughout the stack. And if I abstract these out, ultimately, what we are trying to do is get end-to-end service-level objectives, which could be related to whatever the agent cares about for that application. And on the other end, we care about a lot of infra-level objectives for running our data centers efficiently. And so now you have this cross-dependent space, trillions of choices, diverse SLOs, and rapidly evolving components within the stack, which means that it's almost inevitable that you would go wrong when you pick something and the chances of going wrong are actually very high, and the cost of going wrong is even higher. So then the question is, how do you extract token efficiency in this very, very complex ecosystem? So there's a famous quote. "You can't optimize what you cannot measure." So over the past many years, we've been working closely with academia-industry partnerships

**[3:18](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=198s)** to really understand the end-to-end stack for AI systems, all the way from the hardware to the software, all the way to the workloads. And we've also worked very closely with a lot of benchmarking and standardization agency to create APIs with which a lot of these benchmarks and tools can work interchangeably. And this has led to massive adoption. So I'll especially call out Chakra, which is an initiative we started with MLCommons. We just released Chakra a few weeks ago at MLSys. So this is basically a benchmarking methodology for distributed AI platforms. And ASTRA-sim which is a simulation platform for studying distributed AI networks. And with this adoption, what's also interesting is, throughout-- a lot of the companies that we've been working with, from hyperscalers to hardware vendors, to OEMs, to test vendors,

**[4:07](https://www.youtube.com/watch?v=gPj9UOnT2OI&t=247s)** one thing that keeps coming out is that the only way to get efficiency is optimizing across the stack. Optimizing just parts of the stack will not work. So that gets me to something I'm personally very excited about. So we just started InfraVana. This is a company that's built an automated agent plus hardware-aware full-stack optimizer. And we're already seeing massive speedups over the state-of-the-art inference frameworks out there. And you'll hear a lot more from us as we come out of stealth. So you can feel free to find me anytime at the conference or email me if have any questions. And I'm happy to of officially call this session to a close. Thank you.
