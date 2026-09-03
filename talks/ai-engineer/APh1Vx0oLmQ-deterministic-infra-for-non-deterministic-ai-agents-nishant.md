---
id: APh1Vx0oLmQ
title: "Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs"
slug: deterministic-infra-for-non-deterministic-ai-agents-nishant
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Nishant Gupta"]
channel: "AI Engineer"
duration_min: 7
published_at: 2026-06-29T00:00:00Z
video_id: APh1Vx0oLmQ
url: https://www.youtube.com/watch?v=APh1Vx0oLmQ
youtube_url: https://www.youtube.com/watch?v=APh1Vx0oLmQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Evals, observability & reliability", "Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: true
---

# Deterministic Infra for Non-Deterministic AI Agents - Nishant Gupta, Meta Superintelligence Labs

**Nishant Gupta**

`AI Engineer` · `AI Engineer` · `2026` · `7 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=APh1Vx0oLmQ) · [Conference site](https://www.ai.engineer/)

## Description

AI agents are rapidly evolving from copilots into autonomous systems capable of reasoning, invoking tools, coordinating workflows, and interacting with production infrastructure. But most platforms today were designed for deterministic microservices — not long-running, non-deterministic systems powered by LLMs.

This creates a massive infrastructure gap.

In this talk, I’ll share lessons from building large-scale agentic and elastic compute infrastructure powering production AI workloads. We’ll explore the emerging “control plane” required for reliable AI agents: orchestration, observability, retries, evaluation, safety guardrails, workload isolation, memory coordination, and operational control loops.

Topics include:

- Why most AI agents fail outside demos
- Building deterministic systems around stochastic models
- Observability for autonomous AI workflows
- Failure handling and retry storms in agent systems
- Human oversight and safety guardrails
- Elastic GPU infrastructure for agentic workloads
- Reliability patterns for production AI systems
- The shift from “prompt engineering” to “systems engineering”

Attendees will leave with practical architectural patterns for building resilient AI infrastructure capable of supporting autonomous systems safely and efficiently in production.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs building the training and inference AI infrastructure.

## Transcript

*1,045 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=3s)** Hey everyone. My name is Nishant Gupta. I'm a software engineering tech lead at Meta, working on building the training and inference infrastructure. And today, we're going to be talking about building deterministic infrastructure for non-deterministic AI agents. So, most of the conversations around AI over the last few years has been focused on models. Bigger models, more parameters, better reasoning. But as organizations move from chatbots to autonomous agents, a different problem emerges. The challenge is no longer in intelligence. The challenge is is reliability. At Meta and across the industry, we are seeing agents move beyond answering questions and beginning to plan, call tool calls, coordinate workflows, and make decisions that affect production systems. These systems are fundamentally probabilistic. Infrastructure is not allowed to be.

**[0:52](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=52s)** Today, I want to discuss this topic in more detail. The modern cloud infrastructure evolved around a set of assumptions. A request Most of the requests are short-lived. Services are deterministic, more or less. Execution paths are known. Failures are bounded. However, autonomous AI agents violate nearly every one of those assumptions. They're stateful. They're long-running. They make decisions dynamically. They may may execute different workflows for same inputs. This is what I call the great mismatch. We're trying to run autonomous systems on infrastructure that was designed for deterministic workflows. This is probably the most important mindshift. Most AI demos showcase capability. But can it solve a problem? Can it use a tool? Can it compete complete a

**[1:39](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=99s)** workflow? Production systems be have a different objective. Can it do it reliably? Can it do it 10,000 times, 100,000 times, million times? Can it recover from failures? Can it operate safely? Can it do it in an at an acceptable cost with an acceptable latency? With an acceptable outcome? The majority of the engineering effort moves below the model layer into orchestration monitoring safety evaluation, and recovery systems. When people hear AI failures, they immediately think hallucinations. In reality In reality, hallucinations are often the least interesting failure mode. What we see instead are infrastructure failures, recursive reasoning loops, workflow dead locks, retry amplification, context corruption, memory poisoning, cost explosions. The model makes a mistake, but however, the infrastructure

**[2:27](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=147s)** turns that mistake into an outage. That's the real challenge. So, as this slide shows a pattern that distributed system engineers will probably recognize immediately, an agent calls a tool incorrectly, the tool returns an error. Instead of recovering, the agent generates a slightly different, but still invalid request. The cycle repeats. Each retry consumes more compute. Reasoning depth increases, GPU consumption rises, eventually you get exponential resource growth. What started as a minor API error became a compute incident. This is why unco- uncontrolled retries are one of the biggest risk in agentic systems. This is the architecture principle I recommend most strongly. Never let the model directly control production systems.

**[3:13](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=193s)** The model should generate proposals, infrastructure validates them, policy engine approves them, execution gateway enforces them. The model just suggests, the platform decides. This separation allows us to build reliable systems even when the underlying model remains probabilistic. As we know, containers gave rise to Kubernetes, microservices created service meshes. AI agents are creating something new, an agentic control plane. This layer becomes responsible for scheduling, memory coordination, policy enforcement evaluation monitoring workload routing, which is very important. And think of it as an operating system for autonomous AI. The organizations that build this layer will have significantly more competitive advantages. So, traditional logs tell us what happened. Agentic systems require

**[4:00](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=240s)** understanding why it happened. We need traces to capture planning decisions, tool calls, memory lookups, state transitions. When debugging an autonomous workflow, understanding the chain of decisions and reasoning is often more important than the final output. Observability becomes multi-dimensional. Without it, production debugging becomes nearly impossible. So, as you can see, memory is one of the most underestimated challenges in agentic architectures. Once multiple agents share state, familiar distributed system issues appear. Stale reads, conflicting updates, context drifts, inconsistent views. The challenge becomes even harder when memory itself may be probabilistic and retrieval-based. Many multi-agent failures are actually consistency failures masquerading as reasoning failures.

**[4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)** So, safety cannot be a single component. It must be layered. Prompt level controls, tool permissions, policy validations, human approvals, audit systems. Each of these layers catches a different class of failures. Defense in depth is a well-understood security principle. It applies equally well to autonomous AI systems. Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised. Humans became become exception handlers. They review ambiguous situations. They handle normal scenarios. They provide calibration signals. The goal is not to remove humans. The goal is allocating human attention where it provides the maximum value. So, one of the biggest infrastructure

**[5:37](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=337s)** shifts is that AI workloads increasingly resemble cluster scheduling problems. Demand is bursting. Reasoning depth is and Workflows may run for minutes instead of milliseconds. Resource requirements vary dramatically. As a result, GPU efficiency, workload placement, elastic capacity management, and scheduling becomes critical. Inference is no longer just a model problem. It becomes a resource orchestration problem. The good news is that many of these problems are not entirely new. Distributed systems have solved something similar for decades. Circuit breakers become tool isolation. Rate limits become agent limits. Retries become control recovery. Resource quotas become cost governance. Observability becomes agent tracing. Instead of inventing entirely new infrastructure, we can adapt to

**[6:24](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=384s)** reliability patterns for autonomous systems. The industry has gone through several phases. The initially prompts were the differentiator. Then the models became the differentiator. And both are rapid rapidly commoditizing. The next frontier is infrastructure. The organization that won't that wins is not necessarily have the best prompts. They'll have the most reliable systems. The competitive advantage is moving up the stack. If there's one thing I want you to remember, it's this. AI agents should be treated as distributed systems. Models are stochastic. Infrastructures must be deterministic. Reliability is increasingly an infrastructure problem. Observability is mandatory. Control planes are emerging as a foundation layer. And ultimately, the future of the AI AI won't be won by better prompts. It will be won by better systems.
