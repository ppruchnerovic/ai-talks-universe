---
id: klFR-KFR_EY
title: "Beyond “System Complete”: Shipping Globally with Agentic Commerce Orchestration"
slug: beyond-system-complete-shipping-globally-with-agentic
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: null
duration_min: 11
published_at: 2026-08-11T13:10:10Z
video_id: klFR-KFR_EY
url: https://www.youtube.com/watch?v=klFR-KFR_EY
youtube_url: https://www.youtube.com/watch?v=klFR-KFR_EY
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Agents & orchestration", "Evals, observability & reliability", "Governance, ethics & regulation", "Inference, serving & GPU infra"]
transcript: true
---

# Beyond “System Complete”: Shipping Globally with Agentic Commerce Orchestration

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `11 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=klFR-KFR_EY) · [Conference site](https://mlopsworld.com/)

## Description

Amit Kumar Padhy, Senior Computer Scientist II, Adobe Inc.

About the Speaker:
Amit Kumar Padhy is a Senior Computer Scientist II and Lead Architect at Adobe. Based in Sunnyvale in the San Francisco Bay Area, he works out of Adobe’s San Jose, California headquarters. He specializes in cloud-native platforms, distributed systems, and AI-enabled digital commerce, and architects and modernizes mission-critical, event-driven microservices at global scale, emphasizing reliability, performance, cost optimization, and platform governance. Amit is an invited keynote speaker at international IEEE conferences and has delivered PRO-level talks at leading industry events, including DeveloperWeek, ProductWorld, and major IEEE, AI, and Data Summits. He also serves on advisory boards for IEEE and ACM conferences.

Abstract:
Distributed commerce platforms don't fail because features are missing, they fail at the seams. A product is created in Catalog, but pricing is incomplete. Promotions don't qualify. A compliance rule blocks three regions. The system says ""launched."" The business knows it isn't.

This talk replaces traditional workflow orchestration with a production-tested, multi-agent swarm model that coordinates Pricing, Catalog, Promotions, Tax, and Compliance in real time, driving products to a verified sellable state, not just workflow completion.

We'll walk through a concrete architecture: Planner Agents using ReAct-style reasoning to decompose onboarding goals into dynamic execution graphs; Domain Agents that invoke live APIs (Pricing Runtime, Billing Preview, Tax engines) as tools; Validator Agents enforcing regulatory and pricing integrity at every step; and a Coordinator Agent maintaining shared state via a blackboard-pattern memory layer over Kafka-backed events.

The hard lessons are where this talk earns its value. We over-used LLMs and paid for it in latency and cost, until we scoped them strictly to planning and exception handling. Centralized orchestration became a bottleneck, until we shifted to loosely coupled, domain-specific agents. Compliance flows exposed the limits of probabilistic reasoning, until we layered in deterministic, rule-based validators as a fallback.

Attendees will leave with a working blueprint for LLM-agent swarms that handle uncertainty across distributed systems, recover through intelligent compensation (not blind retries), and produce auditable decision traces, so when something fails, you know why, not just where.

Key takeaways: event-driven agent coordination patterns, selective LLM invocation strategies, saga/compensation design for agent failures, and a practical observability model built around decision reasoning."

## Transcript

*1,679 words · source: supa (en, exact timings)*

**[0:08](https://www.youtube.com/watch?v=klFR-KFR_EY&t=8s)** So, uh this is uh the agent domain workflow. Um what are the agent responsibilities and boundary? Each agent owns a clear domain. For example, a pricing domain is very specific for the need of pricing. It does It absolutely has no information about, say, a payment-related aspects like which credit card or a bank, you know, system is used or, say, a Zelle or any other system needs to be used. It has totally no awareness of it. Agents can validate, recommend, and enrich, or even the flag the issue. So, there will be uh you know, validator agent which can actually do the validation. It can also provide some recommendation that, "Hey, you know, you have to do this because you have missed out on these product-related meta information." And then, you know, when

**[0:57](https://www.youtube.com/watch?v=klFR-KFR_EY&t=57s)** it goes to somebody who is uh you know, a judge or a human being involved in the process onboarding, he can easily correct that. Um this is, of course, rare, but it helps a lot. Uh they don't silently override any critical business rule, and high-risk decision are routed to human for review. We just spoke about it. Uh it has a spe- special exception handling mechanism. Like, anything which is very high critical, you don't let it go out of there. The system suggests fix. I think we talked about it. I will just uh uh I'll skip this slide. Um the multi-agent supervisor. Now, there are two different architecture where this multi-agent system can operate. One is a orchestrated or supervisor pattern where there is a centralized coordinator which uh creates

**[1:46](https://www.youtube.com/watch?v=klFR-KFR_EY&t=106s)** a plan and then provides the uh based upon the plan, provides the specialized worker agent each of those planned activities one by one. Or, there could be a swarm-based architecture. After the planner creates a plan, any of the agentic swarm has the shared state of memory which it can pick up the work and it knows what's to do from the memory. So in the swarm architecture, there is no no coordinator agent, but any of those could act like you know, pick up the task which is available. If there is an exception, it goes to another agent in the swarm. So what is different between the supervisor agent and the swarm based architecture? In in supervised architecture, there is a central coordinated orchestrator,

**[2:34](https://www.youtube.com/watch?v=klFR-KFR_EY&t=154s)** something that we talked about here, but then there is a swarm based architecture potentially that can be used where none of the agents are responsible. Like a system can dynamically allocate the agent, any specific agent, and that agent derives the intelligence from the common shared state and execute it. Uh you know, you know, it's it's it's a kind of helpful in disconnected systems in a much more non-centralized decentralized workflow mechanism. So I will come for the sake of time, I will come towards some of the other aspect. Quickly walk it through. The onboarding dashboard is very important because you just not only want to onboard the product, but you have to

**[3:22](https://www.youtube.com/watch?v=klFR-KFR_EY&t=202s)** have a graph of where exactly the onboarding lies at any particular point in time. So if you look into the graph, it is you know, just kind of a for depiction, but it provides the various phases where the onboarding is going through. For each particular product, you can deep dive into the orchestrator state and you know, see what are the completion rate. Like how many percentage of those completion has happened, which particular stage is kind of you know, not met. The SLAs are not met. It also provides you anomalies and alerts like for example, one step has encountered some issues or some problems, it provides those alerts so that somebody who is looking into the orchestration can come and replay those events to solve the problem. And of course, you know, the system is in total

**[4:09](https://www.youtube.com/watch?v=klFR-KFR_EY&t=249s)** transit state all the time more and more products getting onboarded. So you have have to have a key performance indicator measured so that if you find something is lacking you can course correct. So it provides those key performance indicator in a well, you know, presented graph mechanism so that anybody from leadership or you know, from the operation side can come in and look into the thing and know the places of improvement. And then effort can go and, you know, engineering effort can go into that particular aspect and then it can resolve. Essentially provides a 360-degree visibility for any product onboarding and any real-time progresses. So there are there could be totally autonomous agents then

**[4:57](https://www.youtube.com/watch?v=klFR-KFR_EY&t=297s)** you know, which could be you know, everything opens end-to-end with a human gate. And then of course, you know, the explainable decisions. All of the decisions which has been taken are audited. So some of the other important aspects are trust governance and auditability. You generally kind of ensure that every agent action can be explained in terms of real business rule. So the agent generally gets those rules and what it could do and what it could not from something from the rule-based mechanism and also a rag database feeds into those mechanisms to ensure it does not do anything which is out of the domain and the responsibility it is. The platform records what changed, why it changed and who

**[5:46](https://www.youtube.com/watch?v=klFR-KFR_EY&t=346s)** approved. it. It's typically the audit mechanism. We talked about it here. All the responsibility needs to be audited. And of course, the human being still being at the center of this when there is a sensitive change like a pricing compliance or some core policy update need to be made in the system. So, federation is the foundation. We pretty much covered most of it. It is just to provide you a single view. We We talked about the domain autonomy. We talked about the centralized governance by design. Contract first integration. We reuse the existing API of the last decade. Still with the agent API capability. We talked about the built-in traceability where we talked about the

**[6:33](https://www.youtube.com/watch?v=klFR-KFR_EY&t=393s)** auditing. And with respect to the existing commerce system, it's totally extensible. It does not reinvent and you know, a very disruptive so that you you can risk something and it can coexist with existing legacy system. For example, we talked about how these different agents, you know, some of these can be old system and some of the system could be totally agentic and new. So, that's about it. And of course, you know, human and AI collaboration is still the center stage. This slide, let's focus a bit. I mean, this actually provides you the kind of impact that we have observed. The data is approximate, but pretty much you know, the it helped us to do this 10x

**[7:23](https://www.youtube.com/watch?v=klFR-KFR_EY&t=443s)** faster launches. The manual effort was significantly reduced. You know, it was to the tune of 90% and with the dashboarding capability we we introduced with auditing of this agent actions, the onboarding states, the anomalies that you can see, we can have a end-to-end 360 degree visibility. So yeah, we are still working on we have worked on the anomalies specifically to see you know some of the anomalies could be the system alarms automatically and it also provides some resolution. Today human being goes and deploys the fix but we are looking for mechanism how some of the low risk fixes could go automated automatically to the system to enable the product onboarding

**[8:11](https://www.youtube.com/watch?v=klFR-KFR_EY&t=491s)** and instead of waiting for manual cleanup agents will recommend some time and fix those automatically whenever it's low risk. So that's pretty much you know I will wait for questions. Yeah, that's about it and feel free to reach out to me. These are my email and you know LinkedIn I can answer some of these offline as well. >> I feel like I have to ask this or and and forgive me if it's not entirely relevant or perhaps you could address how relevant it is but how does the underlying model how does that factor into and this process with specific reference to what's kind of happened very recently the whole fable five anthropic like I guess is this I guess the

**[8:59](https://www.youtube.com/watch?v=klFR-KFR_EY&t=539s)** question is how model agnostic is this whole process that might be a big question but I'll I'll let you proceed. >> Yeah, that's that's absolutely a great question. I would say from the agentic and LLM integration point of view believe me we have tried with whole lot of model. We have also been you know testing with respect to the latency aspect. We have observed some of the model you know as in more and more context gets loaded they slow down. So we have been kind of testing through various models. We have used the cloud models the open AI models. Of course fable fable has not yet been tested. I'm aware of the you know, the recent news you are talking about. Yes, pretty much I think when it's available, you know, when when Anthropic is back,

**[9:47](https://www.youtube.com/watch?v=klFR-KFR_EY&t=587s)** maybe you'd like to utilize it that as well. I mean, it's promising. It has made a whole lot of news, but yes, I can tell you you know, a lot of models has been tested. Some smaller models something are much more effective because the latency is very very much manageable. Some of the quite heavy models are unnecessarily complicated. You don't really need to have that much of latency or wait for an answer. So, it's it's it's a fine balance that we try to achieve also with our rag databases to build the context and ensure, you know, the you know, the token cost is also something that we are very much aware of. We kind of optimize it to ensure, you know, we we don't do too much of token usage. And as much

**[10:36](https://www.youtube.com/watch?v=klFR-KFR_EY&t=636s)** as possible, we know based upon, you know, the context. As much context we know, I think that's better. That's what we do. Yeah.
