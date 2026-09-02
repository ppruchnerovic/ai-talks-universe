---
id: TLuDkgMQFpI
title: "Rahul Krishna - ScarfBench: Can Agents Migrate Enterprise Java?"
slug: rahul-krishna-scarfbench-can-agents-migrate-enterprise-java
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Rahul Krishna"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-12T07:52:51Z
video_id: TLuDkgMQFpI
url: https://www.youtube.com/watch?v=TLuDkgMQFpI
youtube_url: https://www.youtube.com/watch?v=TLuDkgMQFpI
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Rahul Krishna - ScarfBench: Can Agents Migrate Enterprise Java?

**Rahul Krishna**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=TLuDkgMQFpI) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,209 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=1s)** RAHUL KRISHNA: All right. Hi. Hello everyone. I'm Rahul Krishna. I am a Senior Research Scientist at IBM Research. My talk today is going to be about enterprise Java applications, and how effective agents are in migrating them from one framework to another and modernizing them. So enterprise Java is applications in enterprise Java and modernization outlive the frameworks in which they're originally written. And it's a large-- so enterprise applications that are written in Java remain critical. Legacy applications were written in frameworks and the applications themselves often outlive the frameworks. And modernization is an important use case because it's important for us to modernize the application

**[0:52](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=52s)** into newer frameworks so that they have supported runtimes better security deployment modalities, among others. But the key insight of deployed applications is the institutional knowledge that have been embedded in the application over several decades. These include business rules, data semantics, workflows and integrations. And migration must replace the underlying technology stack while preserving the application behavior. Now, this is challenging because the Java frameworks with which many legacy Java applications are written hide the runtime behaviors with their APIs. So these means they use different proxies, reflections, interceptors, and the code itself doesn't really capture any of these.

**[1:40](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=100s)** And these are taken care of by the frameworks themselves. And as a consequence, there is not really a one-to-one equivalence between an application written in, let's say, Spring to that written in Jakarta. And when we migrate these applications, it might seem like they build correctly and they run correctly, but there might be silent failures that will only show up at deployment time. Just to ground this benchmark and why this is relevant, I wanted to show this slide here, which lays out the architecture of a typical Java enterprise application. So large applications are usually organized in tiers. And each tier addresses a specific concern. Presentation layer, for example, presents the application to you through a browser or a phone application. And all the way down, we have data access layer, which does database reads and writes

**[2:30](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=150s)** and a cross-cutting concern which ties them all together with configuration, security and so on. But this is a really challenging problem because if you look at the application, a lot of these behaviors and the business logic that's embedded in these applications are usually hidden behind framework and their APIs. And each framework have their own idiosyncrasies. For example, our dependency injection, annotations, and so on in the application dictate how the business logic is embedded. And if we go hunting for it in the code, we may not find any of these. Even though these layers are separate in terms of their concerns, a deployed application has all of these layers interacting with one another, often at the same time. And therefore, this is a challenging problem. Now, in order to solve this, we built ScarfBench,

**[3:18](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=198s)** which stands for Self-Contained Application Refactoring Benchmark. And the objective is twofold. First, we wanted to see how effective agents are in migrating applications and modernizing them from one framework to another. And second, in the process of doing this and understanding agent trajectories, we wanted to build a field manual of sorts and understanding how to build agentic solutions for general modernization. And we broke this benchmark down into two groups. I'll quickly go over them. So we have focused applications and whole applications. Focused applications are self-contained apps for a single layer that we just discussed. And whole applications puts them together into a cohesive business use case. This is just a high-level overview of the applications. So what we did at IBM is we had a lot of subject matter experts manually convert each of these applications

**[4:08](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=248s)** that I've listed here across all of these frameworks through Spring, Quarkus, and Jakarta. And each row here is an application. And a unit of migration could be any app from one framework to another. And the objective of doing so is twofold. One, each migration has its own idiosyncrasies, and they're asymmetric in the sense that Spring to Quarkus is very different from Jakarta to Spring. And we also wanted to see how effective agents are in tackling independent layers. Agents might be really good at converting presentation layer, but they might struggle at the integration or data dependency injection layer. Like I mentioned, each of these layers are isolated, but a typical deployed application is a collection of all of these layers. And often these applications have

**[4:55](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=295s)** all of them communicating with one another and interacting with one another. So the whole application part of our benchmark captures many of these applications, both as a monolith and equivalent deployment as microservice, which again, subject matter experts manually converted across all of these frameworks. So at a glance, we have about 38 applications individually, but this translates to 114 variations of the same applications. And director transformations add up to about 228. But the key distinction here is the hand-written test cases. So as we migrated each of these applications, the developers wrote test cases for the behaviors that they expect in the applications when they're deployed. And these test cases vary all the way from HTTP checks that I'll show in a second to see if the app is hosted in HTTP and HTTPS, all the way down to JSP pages

**[5:46](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=346s)** to see if the deployed application, browser click actions, and the data is propagated correctly. So here's a simple smoke test. And there are many of these that I list. But this is a cURL test that just ensures that the deployed app in the target framework has the same HTTP ports open. And it's more of a health check. But the smoke tests in our benchmarks also capture if messaging works correctly, if database updates commits and rollback behave as expected. And for apps that have a browser endpoint, we also have playwright tests that ensure that the user actions on the migrated application look identical to the source app. In doing this, we also evaluated a large number of coding agents. More results are in the paper. We discussed some taxonomies, failure modalities.

**[6:35](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=395s)** But a quick highlight here is that although agents are really effective at migrating applications, ensuring that they compile and they can deploy, they're not really good at maintaining the behavior in the target application. What we noticed is after migration, only 2% to 14% of the migrations actually had the exact same behavior that the source application had. And compilation itself was a weak signal because that gave us a false indication that the agents are really good at migration, but the behavior was not preserved. And the flows here also strongly suggests that some frameworks are really hard to migrate to, and some frameworks are really hard to migrate from. So there is an inherent complexity and asymmetry in how agents migrate from one application to another. There are more details in the paper,

**[7:24](https://www.youtube.com/watch?v=TLuDkgMQFpI&t=444s)** various failure modalities, and some instructions on how agents can be better built. So here's a benchmark. Feel free to reach out to me after the talk. I'd be happy to answer any questions. All right. Thank you. [APPLAUSE]
