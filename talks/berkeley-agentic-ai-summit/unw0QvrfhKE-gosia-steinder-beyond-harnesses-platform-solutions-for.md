---
id: unw0QvrfhKE
title: "Gosia Steinder - Beyond Harnesses – Platform Solutions for Agent Reliability, Security, and Efficien"
slug: gosia-steinder-beyond-harnesses-platform-solutions-for
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Gosia Steinder", "Beyond Harnesses"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-11T05:09:21Z
video_id: unw0QvrfhKE
youtube_url: https://www.youtube.com/watch?v=unw0QvrfhKE
tags: []
transcript: true
---

# Gosia Steinder - Beyond Harnesses – Platform Solutions for Agent Reliability, Security, and Efficien

**Gosia Steinder, Beyond Harnesses**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=unw0QvrfhKE) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,398 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=unw0QvrfhKE&t=2s)** GOSIA STEINDER: Thank you very much. It's great to be here. I believe we are entering the next wave of application platform evolution. The first wave being when we separated hardware from software and developed the first high-level programming languages. The second being cloud computing, when we started creating distributed applications across the data center and the globe. Both of these waves resulted in creating a new operating system. And by operating system, I mean a foundation that separates application from hardware, from infrastructure through a layer of abstraction, but also foundation that offers certain primitives that applications can rely on to achieve resiliency, scalability, and efficiency.

**[0:54](https://www.youtube.com/watch?v=unw0QvrfhKE&t=54s)** AI applications are without any doubt that the most non-deterministic and unreliable component that has ever been introduced in enterprise architectures, and I believe they will require a new foundation, a new operating system as well. Now, AI applications are applications, they can run on existing foundation. The problem really is that this foundation doesn't really do much to help solve the novel challenges that are occurring with these applications, and I personally like characterizing these challenges in two groups. There are structural and semantic. Structural challenges are because these applications have open-ended instruction set. By instruction set, I mean the set of operations that an agent can execute on an external world.

**[1:44](https://www.youtube.com/watch?v=unw0QvrfhKE&t=104s)** They decide which of these instructions to use at runtime, and they order them at runtime. Now, that breaks a few very important assumptions that existing platforms make. Zero trust security becomes very difficult because zero trust security depends on understanding interaction patterns between applications a priori, at configuration time. Recovery becomes very difficult because traditional techniques, like compensations and rollback, become intractable to implement. And of course, these applications are not fully testable in pre-deployment. Another problem is the lack of separation of instructions and data in the context, which is what agents are working off. That's why we are seeing so many novel security

**[2:32](https://www.youtube.com/watch?v=unw0QvrfhKE&t=152s)** threats associated with agents, and agents communicate exchanging that context. So we are losing execution separation between different agents. And that essentially means that controlling blast radius of resiliency and security issues becomes very difficult. And now there comes this entire semantic side that Ian Stoica has been talking about, that we are not able to fully specify agent goals. It's very difficult to express what agents should do in the narrative, but it's even harder to specify what agents shouldn't do. And we still lack any formal methods of expressing agents' goals and validating agents' goals. It doesn't help that AI models, the agents, are not good in reporting on their own status.

**[3:22](https://www.youtube.com/watch?v=unw0QvrfhKE&t=202s)** We essentially do not have any reliable error codes. All this means that understanding if agent is working correctly, if it's succeeding, detecting its failure, understanding its liveness. So if it's making progress, if it's converging towards the goal or not hanging, all of these problems become very difficult. And if we cannot determine what the problem is, we cannot recover from this either. And, of course, there is also a semantic gap between how is thinking and designing what it should be doing and the schema-based nature of real world interfaces that with constantly changing interfaces, leads to mismatch and new errors being introduced. So how do we address these problems today?

**[4:15](https://www.youtube.com/watch?v=unw0QvrfhKE&t=255s)** Well, all of this is done in a bespoke manner in the application layer. So we develop frameworks, we develop harnesses, and we have plenty of them. Every few months, we see a new powerful type of agent or harness being developed that tries to address these problems and prove or proof of existence that the solution exists. But that creates a lot of fragmentation. These harnesses are actually very hard to develop. You need to have a lot of expertise. Now, we are clearly in the experimentation phase. And when you look at the history, we see that in previous waves of innovation, the same thing happened at the beginning. We have multiple versions of Unix. When containers and cloud native era started, we had lots of versions of containers,

**[5:03](https://www.youtube.com/watch?v=unw0QvrfhKE&t=303s)** lots of container orchestration platforms, and entire divergent ecosystems around that. But eventually, the industry has identified common patterns, standardized on them, and consolidated. So we ended up with Unix and POSIX semantics for in the first wave, and the Kubernetes and the ecosystem around Kubernetes in the second wave. We believe something like this will need to happen in the AI era as well. So that's what we and my research group are exploring. And the way we approach it is by looking at the types of agents that we are running in our organization. And we essentially have three types of agents. We have those that we have implemented ourselves using some framework or some SDK.

**[5:52](https://www.youtube.com/watch?v=unw0QvrfhKE&t=352s)** So we have complete control over them. We have agents that are well-known harnesses that we can control via hooks and plugins. And we have blackbox agents that we cannot do anything about, those we can only control by observing them on the outside. So what we are building is a layer of interception that can integrate with all of these styles of agents and provides a uniform way to observe and modify all interactions that these agents are making with the external world. Using that layer of abstraction, we are adding control functions to manage how agents are behaving. Our first approach, first problem, that we've tackled has been security, and particularly,

**[6:41](https://www.youtube.com/watch?v=unw0QvrfhKE&t=401s)** the zero trust security. Implementing multi-tier, multi-layered permission system to control what agents are allowed to do. This included implementing agent identity and using that identity to implement delegation flows with authorization, then policy-based access, and then finally, intent-based access to evaluate if what agent is doing is actually aligned with users objectives. We have moved since to also start looking into the semantic layer of agents. So can in this business logic independent way outside of agents, control the context and manage context that agents are using. Can we manage the correctness of tool calls and do data flow analysis to understand how data is flowing

**[7:32](https://www.youtube.com/watch?v=unw0QvrfhKE&t=452s)** and control that. We are pursuing this in the project called Rossoctl. Our web pages contain more information and also contain deeper results of various benchmarks and experiments. And my colleague Maya has a poster that she's going to present today. So I encourage you to stop by and learn more about what we have done. Now, crucially, we are not inventing-- we are not replacing the existing platform. All of the things that we are doing a bit on existing cloud platform, we leverage existing standards and extend them. So standards like O of tools for identity non-policy languages. We are orchestrating this on Kubernetes, and our gateway-based approaches are originally based on envoy proxy.

**[8:20](https://www.youtube.com/watch?v=unw0QvrfhKE&t=500s)** But now we are moving to a more efficient, Rust-based proxy implementation based on project praxis. We have encouraging results. We can demonstrate cost reduction even with state-of-the-art agents from context compaction. We can demonstrate consistent improvements to tool calling accuracy, which translates into improvements to agent quality. And we can certainly demonstrate that we can transparently do permissioning for these agents. Another important part of the platform evolution of applications is, of course, application patterns. And we believe that for agents, the right application pattern is serverless. Serverless pattern separates agent loop as a stateless component from a durable session lock, where the context is being managed, and execution tier

**[9:14](https://www.youtube.com/watch?v=unw0QvrfhKE&t=554s)** provided by diverse set of sandboxes. We believe that leads to better resiliency, better accuracy, better performance, and better scalability. And again, we have encouraging results. We can save a lot on infrastructure costs, particularly for agents that are model-bound. We can flexibly allocate sandboxes. So not all agents require most expensive sandboxes. And they can be quite expensive. And we can also reuse sandboxes for certain types of agents where security policy allows that. So to summarize that, we do believe there is a new wave of platform that is going to be built. We've started on that journey. We are very interested to--

**[10:01](https://www.youtube.com/watch?v=unw0QvrfhKE&t=601s)** I am very interested in talking to you about this if you agree or disagree. And certainly, if you work on any project in this direction, I would like to know about it, and we would like to partner with you. Thank you. [APPLAUSE]
