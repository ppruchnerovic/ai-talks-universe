---
id: vljxQZfJ9wY
title: "Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs"
slug: production-evals-for-agentic-ai-systems-nishant-gupta-meta
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Nishant Gupta"]
channel: "AI Engineer"
duration_min: 8
published_at: 2026-06-25T18:15:06Z
video_id: vljxQZfJ9wY
url: https://www.youtube.com/watch?v=vljxQZfJ9wY
youtube_url: https://www.youtube.com/watch?v=vljxQZfJ9wY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: true
---

# Production Evals For Agentic AI Systems - Nishant Gupta, Meta Superintelligence Labs

**Nishant Gupta**

`AI Engineer` · `AI Engineer` · `2026` · `8 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=vljxQZfJ9wY) · [Conference site](https://www.ai.engineer/)

## Description

As AI systems evolve from chat interfaces into autonomous agents capable of reasoning, planning, and tool usage, traditional evaluation approaches are breaking down. Offline benchmarks and static datasets fail to capture the complexity, non-determinism, and operational risks of real-world AI systems operating in production environments.

In this talk, I’ll share practical lessons and architectural patterns for building evaluation systems for agentic AI workflows at scale. We’ll explore how modern AI platforms are shifting from one-time benchmark testing toward continuous evaluation pipelines integrated directly into production infrastructure.

Topics include:
- Why offline evals fail for autonomous AI systems
- Evaluating tool use, planning, reasoning, and multi-step workflows
- Online vs offline eval architectures
- Human-in-the-loop evaluation systems
- Detecting drift, hallucinations, and unsafe behaviors
- Building feedback loops for continuous improvement
- Observability and telemetry for agentic workflows
- Reliability metrics beyond model accuracy

Attendees will leave with practical frameworks for designing scalable evaluation systems capable of measuring real-world AI behavior, reliability, and operational impact.

Speakers:
- Nishant Gupta (Meta Superintelligence Labs): Nishant Gupta is a Software Engineering Tech Lead at Meta Superintelligence Labs focused on building the training and inference AI Infrastructure.

## Transcript

*1,143 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=3s)** Hey everyone. My name is Nishant Gupta and I'm a software engineering tech lead at Meta working on building the training and inference infrastructure for the Meta Super Dangerous Lab and the infrastructure organization. Today we're going to be talking about production of ads for agentic systems. When most people hear the word evaluation, they think about benchmarks. A model scores 90% on a benchmark. A new version scores 92%. The team celebrates. But agentic systems have fundamentally changed what the evaluation means. Today the systems don't simply generate answers. They plan. They call tools. They retrieve information. They execute workflows. They interact with the production infrastructure. The question is no longer did the model generate the right answer? The question is did the system behave

**[0:50](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=50s)** correctly? Today I would like to discuss how evaluation is evolving from model benchmarking into production infrastructure. This is the problem almost every AI organization is encountering today. Offline benchmarks continue improving. Yet production reliability often remains unpredictable. Why is that? Because benchmarks measure model capability. Production measures system behavior. A benchmark doesn't capture tool failure, API outage, context changes, user variability, long running workflows. And as systems become more autonomous, the gap between the benchmark performance and production performance grows. The result is what many teams experience today. High benchmark scores, as you can see, but unreliable production behavior.

**[1:41](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=101s)** Traditional LLM evaluation focus on outputs. But we should ask the question did the model produce the correct answer? Agentic systems force us to ask a different question. Did the system behave correctly? Behavior includes planning quality, tool usage, execution, workflow execution, recovery from failures, decision-making. In other words, we are moving from evaluating answers to evaluating workflows. And that requires fundamentally different evaluation architectures. Many teams still think hallucinations are the primary AI failure modes. In production, they are often just one category. Agentic systems introduce an entire hierarchy of failure modes. At the very foundation, the memory failures, retrieval failures, safety failures. As you go up, you have to think about

**[2:28](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=148s)** reasoning mistakes, poor planning, incorrect tool execution. At the highest layer, you have to think about multi-agent coordination failures. And this is why evaluating only model output misses the most production risk we observe. One of the most useful mindset shifts is to stop thinking like researchers and start thinking like a SRE or a production engineer. SREs don't measure success using accuracy. They measure reliability, availability latency cost recovery. And agentic systems require the same approach. The goal is not maximizing the benchmark scores. The goal is to maximize dependable outcomes. Reliability becomes the North Star metric. Accuracy becomes the only input. In this pyramid is how I think

**[3:16](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=196s)** personally think about modern AI evaluation systems. At the bottom, you can see they are benchmarks. They are useful. They are scalable. They are repeatable. But their operational value is limited. In the middle, there are scenario-based evaluations. These simulate realistic workflows. And at the very top, you see production telemetry. This is where the highest value evaluation signals come from. The surprising insight is that the most evaluation data often comes from real users interacting with real systems. Now, let's talk about AI offline evaluations. So, offline evaluation still matters, but the methodology changes. Instead of evaluating prompts, we evaluate scenarios. For example, a customer support workflow, a code generation workflow, a research workflow. The agent operates inside that simulated environment. We measure the task completion rate, tool correctness, planning quality, resource usage, which

**[4:04](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=244s)** is which becomes exponentially high at high scale. The key takeaway, agent evaluation should be scenario driven, not prompt driven. Once a system reaches production, every interaction becomes a signal. This is one of the biggest shifts in evaluation thinking. Production traffic is no longer just traffic. It becomes evaluation data. We collect execution traces, user outcomes, escalations, failures, feedback signals. Production is the largest and the most representative evaluation data any organization will ever have. Many organizations view humans as fallback systems. I think that's a wrong framing. Humans are the evaluators. They provide signals that automated systems cannot. They assess correctness, trust, usefulness, safety. These signals become

**[4:53](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=293s)** really critical for calibrating evaluation pipelines and identifying blind spots in automated metrics. The most successful systems combine automated evaluation with targeted human review. Now, agent systems drift constantly. Model changes. You have a new version every couple of weeks or months. Prompts can change, tools can change, user behavior can change. The challenge is that no longer single change appear catastrophic. Reliability slowly degrades. Success rate declines, escalation increases, tool failure rises. Without continuous evaluation, teams often don't discover drift until users complain. Continuous monitoring becomes essential. Observability and evaluation are inseparable inseparable. To evaluate an

**[5:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=340s)** agent, we need visibility into the reasoning paths, the tool calls, the memory access, execution timelines, the state transitions, as you can see here in this chart, traditional logs are not sufficient. We need detailed traces, just like with any deep nested microservice architecture for any application or service you're talking about. Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork. Let's talk about the continuous evaluation loop because evaluation is an always-running service, not a testing phase. Historically, evaluation always happened before deployment, but now evaluation continues after deployment till you may identify issues, as you can see in A. Human reviews the edge cases, feedback improves the data sets, offline

**[6:29](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=389s)** scenarios validate updates, the loop never stops. Evaluation is no longer just a phase, it's an operational capability. This is probably the most important slide in this presentation. Every metric shown here maps directly to a business outcome. Task completion measures value delivered. Tool success measures operational reliability. Escalation rate measures human burden. Safety violations measure risk exposure. Latency affects user experience. Cost determines scalability. Recovery rate reflects resilience. And notice but notice that accuracy is missing. It's not because accuracy doesn't matter, but because business success depends on much more than just accuracy. Now, this is the architecture where the industry is heading more or less.

**[7:16](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=436s)** Evaluation becomes part of the control plane, not a separate tool, not an offline process. The control plane continuously, which observes the systems, collects telemetry, runs simulations, coordinates human review, and the execution plane performs the work. The control plane measures and governs the behavior, and this separation is becoming a foundational pattern for production AI systems. Now, let's summarize the key lessons. First, benchmarks remains necessary, but they are insufficient. Second, agent systems must be valued as workflows, not individual outputs. Third, production telemetry is a most important evaluation signal. Fourth, reliability ultimately matters more than raw model accuracy. And finally, evaluation is becoming the infrastructure, not testing, not QA

**[8:04](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=484s)** infrastructure. This is the shift every organization building agent AI will eventually need to make.
