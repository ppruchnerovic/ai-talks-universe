---
id: Bf10wSA0JfY
title: "Nilou Salehi - Agent Learning Requires Compressing Info into an Executable Reasoning Structure"
slug: nilou-salehi-agent-learning-requires-compressing-info-into
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Nilou Salehi"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T01:54:45Z
video_id: Bf10wSA0JfY
url: https://www.youtube.com/watch?v=Bf10wSA0JfY
youtube_url: https://www.youtube.com/watch?v=Bf10wSA0JfY
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Nilou Salehi - Agent Learning Requires Compressing Info into an Executable Reasoning Structure

**Nilou Salehi**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=Bf10wSA0JfY) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,071 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=2s)** NILOU SALEHI: Thank you. My name is Nilou. I'm co-founder and CEO of a company called Across AI. I'm also a professor here. What I'm going to talk about today is that, basically, the whole problem that we're all solving and have been solving for years now is compressing information. Because at the end of the day, that is what a model does. That is what a harness does. We are finding different ways to take lots and lots of information and compress it into a format that is executable, like a transformer model is executable and predicts the next token. Now, over the next few years, what's going to happen is we're going to come up with more and more architectures that are able to do this in more complicated ways. And one of the first problems that we're going to have to solve is, what are the various types of processes, and what is the optimal architecture or harness for each of these processes? I want to share one that we've had a lot of success, which is reasoning graphs.

**[0:52](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=52s)** A reasoning graph is a graph of agents. So each of the circles that you see in this graph is one of the agents. And we've identified that for particular processes, specifically, processes that need to be run repeatedly and with very high consistency, this is a very good architecture to do that. So the way this works is that at the very bottom layer, you have a layer of agents that just connect to all of the different systems where the raw data lives. And all these agents do is understand that raw data. You have another layer. These are the layers of agents that do the reasoning. And then finally, there's a layer of agents that take the right action at the right time. So any path that goes from the bottom all the way to the top is one possible reasoning path. And we've seen different flavors of the same idea come up today. Like, you could run these in parallel. You could optimize them in certain kinds of ways. Now, the question then becomes, how do you create one of these?

**[1:42](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=102s)** And we've seen also this idea show up in a couple other talks today as well. And it has to be that it's done by an agent. So what we're going to see more and more is these sort of handshakes between an agent and a harness. And that agent is trained to know very well how to work with that harness. And these different architectures are going to be good at different kinds of processes. So one that we've been working a lot on is this architect agent that works with processes that run consistently and highly accurately, like financial processes or supply chain, or something that a company needs to keep running over and over, is non-deterministic, still needs to be intelligent, but needs to be highly consistent and explainable. So what you get is very high consistency. We've hit routinely above 95% accuracy

**[2:30](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=150s)** in running these processes in examples or benchmarks, where even fable can only hit about 40% to 70% accuracy. And we also get very high speed. No custom code is being written in any part of generation of this harness. It's all the architect agent working together with this particular harness, so we can launch new use cases in a matter of weeks. And the most important part of this architecture is the compounding intelligence in the weights of that model. So every time the architect takes a new use case and creates a reasoning graph for it and learns how to do that, it gets better at doing that. So this kind of a model we're going to see more and more. And we're going to see it for different kinds of processes. I wanted to give you one example of a process that we identified using this architecture. And that's invoice matching. So very, very large companies receive lots and lots

**[3:18](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=198s)** of invoices. And they have to make a very simple decision, pay it or don't pay it. They receive a certain amount of fraud, so they can't pay everything. They also can't sit on it too long because if they don't pay an invoice in time, it affects the rest of their supply chain. So imagine large companies are processing millions of these invoices every month. So an invoice is received. It has to be matched to a PO. It has to be normalized. There are lots and lots of exceptions like, the units might be different, the currency might be different. There's tax in certain areas. One example that I stuck in my head, which I thought was very funny, is that if it's liquid, it's OK if the amount on the invoice is up to 5% less than what was on the purchase order but only during summers because some of it evaporates. And there's nothing you can do. So the agent has to keep learning. It's not a one-time, one-shot learning thing.

**[4:06](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=246s)** It's also not something that happens just in one session. It's something that lasts, a process that lasts long horizons, months, and weeks. And every time you see an exception, you have to learn from it. A baseline agent harness, even using fable here, only gets about 40% of it. This is what the reasoning graph that we built where our architect agent built for this process looks like. It's made up of lots of agents, their wiring, their instructions, what models each agent should use. Each has their own long-term memory. So all of these decisions, all of these engineering decisions are made by the agent. And what we hit was 99.9% accuracy on this real data example. The first graph was up and running in a week. And in 96% of the cases, not only did we give the right decision, but we were able to correctly explain why that decision was made. This brought down the cost of processing these invoices

**[4:55](https://www.youtube.com/watch?v=Bf10wSA0JfY&t=295s)** at this one Fortune 500 from $5 an invoice to $1.50. In this example, and more recently this week, we got it down to 10 cents per invoice. So those are the kinds of advances that you can make if you are able to take that learning and compress it into a reusable structure. Thank you.
