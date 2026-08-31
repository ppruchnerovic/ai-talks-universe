---
id: CS5HojyZ5FE
title: "The Etsy Gifting Assistant: From Prototype to Production | Interrupt 26"
slug: the-etsy-gifting-assistant-from-prototype-to-production
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 17
published_at: 2026-06-08T12:54:09Z
video_id: CS5HojyZ5FE
youtube_url: https://www.youtube.com/watch?v=CS5HojyZ5FE
tags: ["LangChain", "LangGraph", "LangSmith", "AI agents", "Etsy", "gifting assistant", "conversational AI", "ReAct agent", "LLM evaluation", "agent deployment", "AI engineering", "Interrupt conference", "production AI", "LLM judge", "agent observability", "agentic AI", "AI search"]
transcript: true
---

# The Etsy Gifting Assistant: From Prototype to Production | Interrupt 26

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `17 min`

`#LangChain` `#LangGraph` `#LangSmith` `#AI agents` `#Etsy` `#gifting assistant` `#conversational AI` `#ReAct agent` `#LLM evaluation` `#agent deployment` `#AI engineering` `#Interrupt conference` `#production AI` `#LLM judge` `#agent observability` `#agentic AI` `#AI search`

[Watch the recording](https://www.youtube.com/watch?v=CS5HojyZ5FE) · [Conference site](https://interrupt.langchain.com/)

## Description

Derrick Kondo from Etsy's GenAI Enablement team walks through how Etsy built and shipped a conversational gifting assistant using LangChain, LangGraph, and LangSmith in just six weeks. The agent helps shoppers find the perfect gift through collaborative, iterative recommendations across Etsy's unique, unstructured inventory.

0:00 Introduction
0:38 Inventory search challenges
1:22 Why build an agent for gifting
2:04 Beta release results
2:36 Engineering overview
2:52 Solution architecture with LangChain
3:27 Agent tools and middleware design
4:37 Engineering challenges and solutions
4:47 Stopping repeated tool calls (spin)
5:48 Fixing listing ID hallucinations
6:36 Memory management and the terminal UI debugger
7:36 Streaming architecture and socket passing
9:21 Evaluation methodology overview
9:46 Pass-K trajectory testing
10:21 LLM judge for outcome evaluation
11:09 Etsy Agents CLI and LangSmith integration
11:32 Batch simulation for dataset generation
12:06 LangSmith deployments for online and offline parity
13:34 Automated judge alignment
13:56 LangSmith for judgment stability
14:08 Deploying to production
14:17 Etsy Agents monorepo and automated CI/CD
14:51 Six weeks from start to beta
15:12 Summary and closing thoughts

Extra resources:
• Everything we shipped at Interrupt: https://www.langchain.com/blog/interrupt-2026-overview
• Meet LangSmith Engine: https://www.langchain.com/blog/introducing-langsmith-engine
• LangSmith Platform: https://www.langchain.com/langsmith-platform
• About LangChain: https://www.langchain.com/

## Transcript

*1,962 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=6s)** Hello. My name is Derrick Kondo and I'm an engineer in the GenAI Enablement team at Etsy. Today I'll be talking about the Etsy gifting assistant and our path to production. Etsy is a two-sided marketplace where millions of merchants sell handcrafted or vintage items to over 86 million buyers. Searching through our inventory has special challenges. Because our inventory is unique, we do not have a fixed attribute schema for each item. Instead, we have unstructured descriptions that are sometimes cluttered and noisy. Also many of the important details are captured in visuals such as listing images and search

**[1:02](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=62s)** benefits a lot from expertise as our inventory has a range of different niches from fine arts to fandoms and so having an expert being able to broaden or enrich search queries is very useful. For these reasons, we believe that an agent would be very advantageous for conversational search. In particular, we wanted to focus on gifting. As we know, gifting is a fuzzy process where we may know which recipient we want to give a gift to, but we may not have a particular idea of what to give. So the idea is that our agent would pair with the shopper and collaboratively and iteratively refine a set of recommendations to find that perfect gift.

**[2:04](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=124s)** So we developed this agent and released it in beta in production. And what we found was that it returns high-quality search results with a relatively thin harness, which we'll talk about in a second. It also results in relatively high purchase rates in our limited release. So today, I'm going to go into the nuts and bolts of how we built this agent, focusing on engineering, evaluation, and deployment. With respect to engineering challenges, we ran into problems in the areas of reliability, memory management, and speed. But first, let me describe to you the solution architecture. So we chose LangChain because it is best of class

**[2:55](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=175s)** and first of class in the agentic space. It also provides for agent-native observability and evaluation. It also provides for vendor optionality, which is an important factor for us today as we deal with rising token costs as well as issues with model capacity. In terms of engineering design, we wanted to start as simple as possible and only add complexity when justified. So we started with a LangChain v1 ReAct agent, which was a nice combination and balance of abstraction and control. For long-term memory of our recipients, we use the PostgreSQL key-value store.

**[3:44](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=224s)** So let's zoom in on this ReAct agent. So given a request, the model will decide which tools to invoke, and after invocation, it will reason about the results, and then either continue with the tool calling loop or return a curated list of listing recommendations. So there are two points of customization. One is the middleware, the other are the tools themselves. With respect to the tools, we had tools for retrieval, for example, searching and viewing listings, for memory, for example, finding and saving information about recipient profiles, and then skills, so the model can dynamically load instructions on how to use tools for retrieval or memory.

**[4:37](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=277s)** So let's go into engineering challenges and solutions that we ran along the way of implementing that design. So one of the early problems we ran into was repeated tool calls by the model for the same specific tool. We call this spin. So our solution was to create middleware that has some matching condition, in this case, repeated tool calls, and then intervenes at different levels of degree, depending on the severity of the problem. So in this particular example, we see the model has repeated tool calls to search listings. And then after five repeated tool calls,

**[5:26](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=326s)** the middleware will add to the system prompt and instruct the model to synthesize its findings or ask the user for more input. Then after 10 repeated tool calls, the middleware will raise an error and ask the user to try again. Another example of model unreliability was an issue with hallucination of listing IDs. So there would be certain cases where the model, for example, would return truncated listing IDs. And our solution here was to have our tools, for example, search listings, record a set of observed listing IDs in a ledger, and then after the model runs,

**[6:15](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=375s)** the middleware takes as input the curated set of IDs the model found and compares it with the observed IDs in the ledger. And then the middleware fixes those IDs in a best-effort way. So that was an example of us dealing with unreliable model outputs. Here's an example of unreliable model memory management. So we found that the model would sometimes corrupt our recipient memory. For example, it would store a t-shirt size under the interest field. So to debug and resolve this, we created a terminal UI agent debugger, and this provides visibility into the agent state and store interactively,

**[7:06](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=426s)** while also being integrated with Python's native debugger. So it allows for semantic breakpoints, for example, breakpoints in a node in a graph, in addition to being able to see the program stack. This allows us to debug seven or eight different issues and create solutions like creating broader, richer, more descriptive recipient memory schema. So I talked about improving backend reliability. Now let's talk about improving frontend speed. So ideally we would like to stream results from the LangGraph agent back to the client. However, our LangGraph self-deployment exists

**[7:57](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=477s)** in a relatively new Kubernetes cluster. And we didn't want to have to re-implement auth endpoints just for that cluster in addition to adding redundant security protections in order to expose it to the internet. On the other hand, we have our preexisting, longstanding Etsy web cluster. However, and so this web cluster is used for servicing regular Etsy requests. However, it runs Apache, and Apache was not designed for running long-running requests. So our architecture team came up with this neat socket-passing pattern that allows us to reuse our existing web infrastructure. The way it works is that given a client request,

**[8:49](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=529s)** PHP and the Apache worker will authenticate the request as it normally does, and then pass the file descriptor to a long-running daemon that's running in a sidecar. At that point, after the handoff, the Apache worker is freed and released. And then the long-running daemon is responsible for streaming update events back to the client. So this way, we can reuse our existing web infrastructure for agentic streaming. So I talked about how we built our agent. Now I'm going to describe how we evaluated it. The two parts of evaluation: one is the trajectory to a result, and then another part is evaluating the final outcome.

**[9:37](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=577s)** For the agent trajectory, in addition to standard integration and unit tests, we created pass-K tests. These invoke a non-deterministic test K times and ensure that the pass rate, the empirical pass rate, is above some threshold. So for example, given a question about a seller, we have a test that checks that the agent calls the get-shop with respect to outcomes, we wanted to ensure that the listings were relevant to the recipient profile and the shopper in terms of their budget constraints. In particular, we wanted to create an LLM judge that is aligned to a golden dataset. But there are a lot of challenges with respect to methodology of judge alignment.

**[10:32](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=632s)** For example, how do we generate a diverse dataset? How do we align reviewers and calibrate them so they label listings in a consistent way? How do we avoid data leakage when we train an LLM judge on that golden dataset? And what criteria metrics do we use for validation? Ideally, we would have opinionated tooling that operationalizes this entire methodology so that this can be used by all engineers, including ML-nascent product engineers. So we created an Etsy Agents CLI that leverages the LangSmith APIs for streamlining this entire evaluation workflow. This can be used by both engineers and also agents.

**[11:24](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=684s)** So let me talk to you about each stage of this workflow and the tools that we developed along the way. So we created a batch Etsy Agents CLI to run multi-user simulation in order to generate this dataset. This can be used not only for dataset generation, but also batch generation, for example, running an agent across our entire inventory or for load testing to productionize an agent. The way it works is that we have a batch of parallel and distributed workers that send requests to the agent as a service in LangSmith deployments. And that same service can meet both real-time and batch requests. So this way there's no risk in offline versus online drift.

**[12:17](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=737s)** We have consistent governance and observability with LangSmith. And we avoid any redundant boilerplate code following the DRY principle because we can use the same framework for any use case and any agent. So once we generated that dataset, we had our merchant team label listing relevance of each example. So here it's really important to calibrate your reviewers so they label consistently. One suggestion is to use statistics like Cohen's Kappa to measure alignment, discounting alignment by chance, which is especially important if the distribution of samples across your classes is very skewed.

**[13:06](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=786s)** Then we created train, validation, and test splits in LangSmith using industry best practices for LLM prompt optimization such as 20/40/40. We had a tool for alignment of the judge to that golden dataset using automated prompt optimization techniques, such as JEPA, which used an LLM to reflect on the judge's errors and then adjust the prompt accordingly. This alignment tool output standard metrics related to precision and recall. Throughout this process, LangSmith was essential for understanding the judgments of the LLM and also for understanding its judgment stability. Finally, once we have our LLM judge,

**[14:00](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=840s)** we can use it with our classification tool to run it both on the holdout set and other production examples. So once we evaluated our agent, we could deploy it with confidence in production. Our deployment system works in the context of an Etsy Agents monorepo. This enables automatic agent project discovery, and it creates CI/CD pipelines dynamically. No Terraform required, no handwritten pipelines. All one has to specify is a YAML file for specifying the resources for the deployment. The build system uses LangSmith deployment APIs to deploy in a scalable and reliable way.

**[14:51](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=891s)** Taking a step back, it took us six weeks from start to beta launch in production, and this was really accelerated by LangChain abstractions and its platform. We had a team of about three senior engineers and one designer. In summary, the LangChain Framework enables the development of reliable agents with observability and standard interfaces for customization. For example, at the application level, we can ensure reliability through deterministic checks made through code in middleware. As a follow-on to that, as LLMs improve and subsume functionality, the modularity of that middleware makes it easy to swap in and out. At the platform level, LangSmith provides foundational services and tools.

**[15:47](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=947s)** Naturally we want to build integrations and also customization of those tools for our internal workloads and our internal systems and doing so was easy. Finally, as a platform engineer integrated with the product team and co-developing this agent, it was a very effective way of defining requirements for integration and platform development. So I would like to acknowledge the innovation and support of the LangChain team and also give a shout out to all the awesome work by my colleagues at Etsy, in particular, Dan McKinley. So thank you, and I'm happy to answer questions at the booth during the break.

**[16:37](https://www.youtube.com/watch?v=CS5HojyZ5FE&t=997s)** [APPLAUSE]
