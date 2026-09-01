---
id: yVqMxBahjfA
title: "How Uber Runs 60,000 AI Agent Tasks Per Week With MCP"
slug: how-uber-runs-60-000-ai-agent-tasks-per-week-with-mcp
conference: mcp-dev-summit
conference_name: "MCP Dev Summit"
category: "AI engineering & agents"
edition: "MCP Dev Summit NA 2026"
year: 2026
speakers: []
channel: "Agentic AI Foundation"
duration_min: 14
published_at: 2026-05-07T14:00:05Z
video_id: yVqMxBahjfA
url: https://www.youtube.com/watch?v=yVqMxBahjfA
youtube_url: https://www.youtube.com/watch?v=yVqMxBahjfA
tags: []
transcript: true
---

# How Uber Runs 60,000 AI Agent Tasks Per Week With MCP

**Speaker not identified**

`MCP Dev Summit` · `MCP Dev Summit NA 2026` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=yVqMxBahjfA) · [Conference site](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)

## Description

Keynote: Operating MCPs at Enterprise Scale: Uber’s Journey - Meghana Somasundara, Agentic AI Lead & Rush Tehrani, Head of Engineering, Agentic AI Platform, Uber Technologies, Inc.

Meghana Somasundara and Rush Tehrani, who lead Uber's agentic AI platform, reveal how they took MCP from a promising protocol to a production system operating across 5,000+ engineers, 10,000+ services, and 1,500+ monthly active agents. This keynote covers the real challenges of running MCP at enterprise scale, including governance, security, tool discovery, and what it took to build the MCP Gateway and Registry that now powers 60,000+ agent executions per week.

Topics covered in this talk:

Uber's AI Scale - 5,000+ engineers with 90% using AI monthly, 1,500+ active agents, and 60,000+ weekly executions
Three Classes of MCP Problems - Development lifecycle fragmentation, security and governance gaps, and discovery and quality challenges
MCP Gateway and Registry - The control plane for all MCP interactions at Uber, with config-driven auto-generation of tool definitions from 10,000+ service IDLs
Gateway Architecture Deep Dive - How the orchestrator crawls proto and thrift files, uses LLMs to generate MCP descriptions, and serves tools through a unified gateway service
Security at Every Layer - Central authorization, PII redaction, periodic code scanning, mutable endpoint blocking, and full observability with metrics and tracing
Three Agent Surfaces - Uber Agent Builder (no-code), Uber Agent SDK (code-first for grocery, care, and customer support agents), and coding agents (Claude Code, Cursor, Minions)
Minions Background Agent - Uber's internal agent producing 1,800 code changes per week, built on the Claude harness
Improving Agent Reliability - Tool selection scoping and parameter overrides to reduce LLM hallucination in tool calls
Roadmap: Quality and Discovery - MCP evaluation metrics, SLA tiers, an "omni MCP" tool search capability, and shareable skills with A/B testing

This talk is essential for platform engineers, engineering leaders, and anyone building MCP infrastructure at enterprise scale who needs a battle-tested blueprint for governance, security, and tool management.

Links & Resources:

Uber AI Solutions / Agentic AI Tech Stack: https://www.uber.com/us/en/ai-solutions/the-agentic-ai-tech-stack/
How Uber Uses AI for Development (Pragmatic Engineer): https://newsletter.pragmaticengineer.com/p/how-uber-uses-ai-for-development
MCP Dev Summit: https://events.linuxfoundation.org/mcp-dev-summit-north-america/
Agentic AI Foundation (AAIF): https://aaif.io/
Timestamps (approximate, verify before publishing):

00:00 Intro and talk overview
00:34 Uber's AI scale: 5,000 engineers, 90% AI adoption
01:00 The problem: 10,000 services without standardization
01:45 Challenge 1: Development lifecycle fragmentation
02:24 Challenge 2: Security and governance at agent speed
03:09 Challenge 3: Discovery and tool quality
03:29 Solution: MCP Gateway and Registry as control plane
04:05 Third-party vs internal MCP strategy
04:35 Central registry as single source of truth
04:45 Security: authorization, PII redaction, code scanning
05:24 Observability and guardrails
05:40 Gateway architecture deep dive
07:14 Handoff to Rush: MCP consumption at Uber
07:24 Three agent surfaces: Builder, SDK, and coding agents
08:50 Minions: 1,800 code changes per week
09:10 Agent Builder: scoping tools and parameter overrides
10:38 Uber Agent SDK: YAML config and tool selection
11:16 Coding agents: AIFX CLI for Claude Code and Cursor
11:42 Roadmap: eval metrics, SLA tiers, omni MCP tool search
13:15 Skills: shareable recipes with A/B testing
14:06 Closing

AI Agents at Uber may need to navigate a massive ecosystem of 1000s of services, handle sensitive data, and execute critical business logic. To enable this, we are moving towards an agentic future which leverages a unified Model Context Protocol (MCP) infrastructure to access real-time services.

We will share the architectural lessons learned from deploying MCP at an enterprise scale. We will dive into three key technical pillars of our strategy:

1. Protobuf-Driven MCP Servers: How we leverage existing services and protocol buffers to automatically generate MCP servers, providing safe and instant access to 1000s of microservices.
2. Derived Tools and Description Overrides: Why static tool definitions aren't enough for complex workflows. We’ll demonstrate how we allow developers to override and refine MCP tool descriptions via "derived tools," ensuring agents have the specific context needed for particular workflows.
3. Evaluate quality: How we evaluate quality of MCP tools, leveraged in our no-code Agent Builder, which is a tool that democratizes agent building at Uber.

## Transcript

*2,234 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=yVqMxBahjfA&t=0s)** Good morning everyone. It's great to be here. [clears throat] I'm Meghna and this is Rush. We lead the agentic AI platform and initiatives at Uber. Today we're going to be sharing our journey of moving MCPs from a promising protocol to operating this at massive scale across thousands of engineers, services, and agents. And we're also going to cover some of our challenges, similar to what James was mentioning actually, what some of our solutions were, what are some of the lessons we learned along the way, and a quick look at what we're planning for the near future. Okay, let's get started by grounding this in scale. At Uber, we have more than 5,000 engineers with more than 90% of them using AI every single month for agentic workflows.

**[0:46](https://www.youtube.com/watch?v=yVqMxBahjfA&t=46s)** And this does not yet include all of the non-engineering folks, thousands of them, who are also now trying agentic workflows. So this is no longer a pilot program at Uber. It's the new standard for how we work. The reality is of a company this big is really that we have more than 10,000 services. Our knowledge is spread across this very complex landscape. Without MCPs, every agent has to rediscover how to interact with each service. And on top of this, we are now seeing more than 1,500 agents just internally monthly active and over 60,000 executions per week. And this is very high demand as you can see, very high velocity, but without standardization, this starts becoming

**[1:35](https://www.youtube.com/watch?v=yVqMxBahjfA&t=95s)** chaotic very quickly. And so MCPs are not just like important, they really are what make AI usable at Uber. And at this scale, the standard MCP challenges become a lot more amplified. The first class of problems that we saw was around the development life cycle. Without a central framework or guidance, there was no standard way to develop and deploy these MCP servers at Uber. So, we had a lot of teams building out these custom integrations independently, and most of this was non-reusable. We also had everybody trying to figure out how to solve the very same problems in silos of their own. The simple truth was, if you can't manage the development life cycle, you just can't trust it in production. And at Uber, security is non-negotiable.

**[2:25](https://www.youtube.com/watch?v=yVqMxBahjfA&t=145s)** But with these many bespoke ways of doing things, governance start becoming a very immediate concern for us. We needed complete visibility into the call patterns and who was accessing what data. And in reality, it takes us humans a lot more effort to break things, but with agents, as you know, it's a lot faster, it's a lot quicker, and the blast radius is a lot higher. So, we had to make sure that there was no unauthorized access to any data or any of our critical endpoints and services, even unknowingly. We also had to account for any risks that we would have with some of the third-party MCPs around data handling cuz Uber does use a lot of external systems. Now, the last class of problems that we saw was around discovery and quality. How does an agent or even an engineer

**[3:15](https://www.youtube.com/watch?v=yVqMxBahjfA&t=195s)** find the right MCP? And not just any MCP, something that is reliable, has high performance, and is safe. Bad tools just don't fail, they also degrade the agent performance at the end of the day. Our solution was we built MCP gateway and registry. Think of this as the control plane for all MCP interactions at Uber. With this, we moved to a config-driven approach. We now translate all Uber service endpoints into MCP tools automatically. Service owners, which are basically the experts, still stay in control of which tools actually get exposed. And they also fine-tune the descriptions for the LLMs. This removes a lot of duplication and also enforces consistency for us

**[4:03](https://www.youtube.com/watch?v=yVqMxBahjfA&t=243s)** across the board. And the other thing we also did is we followed a different strategy for how we treat and enable third-party MCPs versus our in-house MCPs. We introduced a lot more levels of gating, scanning, and rigorous checks for the external systems compared to our own trusted internal systems. We also deprecated all one-off standard playground environments that people started, you know, spawning off. And everything is now centrally committed and managed in code. We also introduced a central registry. Um, this is the single source of truth to discover all the MCPs at Uber and their versions. And we did all of this with security and privacy built in every single layer. We integrated into our authorization

**[4:51](https://www.youtube.com/watch?v=yVqMxBahjfA&t=291s)** service centrally, so there was no access to any data that is actually not supposed to be there. The other thing we also did is we interact integrated with our PII Redactor service, and this automatically redacted any of our sensitive data, too. We also do periodic code scanning both at diff commit time as well as in our code periodically to make sure that we're detecting any bad patterns, any, you know, endpoint exposures, unknowingly, or any of the risky tool metadata. We also have full observability and guardrails both to block any mutable endpoints that can bring down critical services for us, but also to have extensive logging and uh metrics and tracing for all the operations.

**[5:40](https://www.youtube.com/watch?v=yVqMxBahjfA&t=340s)** And let's take a quick look at what this gateway architecture looks like. There are two critical components to this gateway. The first one is the orchestrator, which is responsible for generating the MCP definitions from the 10,000 plus service IDLs at Uber. And then we have the gateway service, which serves these MCP servers and also allows the service owners to update the MCP definitions. Let's quickly walk through what this uh actually how this actually works. The gateway orchestrator crawls all of these IDLs, which are proto and thrift files. Then it calls an LLM to generate MCP tool descriptions. This is based on the message names and comments, and then it stores this in our object storage. The gateway service then has a conflict

**[6:30](https://www.youtube.com/watch?v=yVqMxBahjfA&t=390s)** provider that's going to pick up these definitions and serves these MCP servers to the different consumers we have at Uber, whether it's a no-code agent platform or SDKs or coding agents. And as I mentioned earlier, service owners can update all of these definitions, which then triggers creating a diff, which is basically a pull request. And the diff is then scanned by our engineering securities unified scanning APIs. And if there are no issues, everything is good, then the scan report is attached to the diff and the diff is committed and deployed to our object storage. And this is then again available to be picked up by the gateway service, which exposes it to the consumers. Now, I'm going to hand it off to Rush to talk more about how we use MCPs and

**[7:18](https://www.youtube.com/watch?v=yVqMxBahjfA&t=438s)** consumption in more detail. Thanks Mega. So, let's talk about how our MCPs used at Uber. Um there's actually three main surfaces at Uber that use MCPs. One is our Uber agent builder, uh which is a no-code solution for building agents at Uber. Uh this agents are usually internal agents. and uh they're used for productivity, for team workflow automation and so on. There is thousands of these that are active on a monthly basis at Uber right now and this they're growing very rapidly across the board. The next surfaces are Uber agent SDK. Uber agent SDK along with all the Uber agent platform functionality like

**[8:08](https://www.youtube.com/watch?v=yVqMxBahjfA&t=488s)** manage memory, manage chat history, orchestration is our code first solution for building agents at Uber. Some of our top use cases use this SDK. Those top use cases include our grocery assistant agent, our care care coordination agent as well as our customer support agent if you interact with our customer support, you'll see this in action. And then finally we have our coding agents. The coding agents as you know their cloud code, their cursor, their companions to our developers to build software at Uber. And on top of that we have minions which is our background agent that's built on cloud as well. The cloud harness as well and it's

**[8:58](https://www.youtube.com/watch?v=yVqMxBahjfA&t=538s)** actually producing about 1800 code changes a week right now and it is being used by all of these are being used by 95% of our engineers across Uber. Okay, so let's dive into a bit more details about how these are actually incorporated to each one of these surfaces. The MCPs are incorporated in here. Um I'll start with the agent builder. So for agent builder, if you want to use an MCP, you can mention the MCP server name as an app mention inside the system instructions. So you can actually scope the MCP within system instructions. For example, if I want to search for something, I can say if a user asks for this, use the @mcpe server for use search, which is our

**[9:46](https://www.youtube.com/watch?v=yVqMxBahjfA&t=586s)** internal search tool, to return information. Now, as all of you know, and it's been brought up in previous presentations, these things can hallucinate and maybe not pick the right tool. So, what we've done is we actually allow you to pick the specific tools from the MCP server, so that the LLM doesn't have to make a decision there. Uh This makes the agent more reliable. And then, to further make it more reliable, we have the capability to do parameter overrides. So, what that means is the LLM doesn't have to make a decision even to pass in a parameter anymore. We can scope the parameter to something static instead. Again, this is through no-code UI, so just making it easier for these users to do this is highly important. And again, makes the agent more

**[10:34](https://www.youtube.com/watch?v=yVqMxBahjfA&t=634s)** reliable. Okay. So, talking about So, that was Uber Agent Builder and how it's used. In Uber Agent SDK, it's somewhat similar. We have a config.yaml a YAML config file that we use there, and you can put in the MCP name and identifier field, and then you can also select the tools that you want or pick the tools you want and put that in the config. And on top of that, you can also override parameters in the same way. You put all of this in the configuration, the SDK automatically loads these tools and makes it available to the agent with those specific configurations. On the coding agent side, we have our AIFXC tool. Basically, what AIFXC lets you do is to

**[11:22](https://www.youtube.com/watch?v=yVqMxBahjfA&t=682s)** add your MCP um by running the MCP add command, and then this MCP server, but whether it's remote or local, is available to both cloud code as well as cursor or any other IDE based agent that we have available at Uber. Okay, so that's what we've done so far and how we're using MCPs. Uh I want to talk about our roadmap and how we are essentially focused in the near future uh on improving the quality of these MCP servers and then simplifying discovery. Um we want to extend our MCP registry to include more evaluation information. We want to surface the highest quality MCP servers to our users.

**[12:10](https://www.youtube.com/watch?v=yVqMxBahjfA&t=730s)** So doing uh by by exposing the evaluation metrics, by including the SLA service SLAs for these MCPs, this includes reliability and availability of the service, that's how we surface these are the this is the right MCP. This is a higher tier and or lower tier MCP that you can use that's most reliable. Uh we also want to we are working on adding a tool search tool that was actually mentioned earlier. Uh again, that helps us help helps us with improve the accuracy of tool discovery by making it so that it's discovered automatically and it's also noted on demand. That also helps us with context bloat, reduces context bloat as as well. So, that's again something we are focused on introducing to our registry and our MCP

**[13:00](https://www.youtube.com/watch?v=yVqMxBahjfA&t=780s)** tools uh as kind of an MCM omni MCP tool. Uh and then obviously evaluations is something we're building into the registry and uh our overall agent platform has evaluations built for agents as well. The other thing as everybody knows about is skills, right? The skills are becoming more and more important uh at Uber. You can think of them as recipes for using these MCPs. So, we want to make them shareable, not just across Uber, but across different teams at Uber. Uh we want to be able to have processes that can be shared and conventions that can be shared across Uber through these skills. And then we want to introduce if evaluations to these skills. That means we want to be able to evaluate the

**[13:48](https://www.youtube.com/watch?v=yVqMxBahjfA&t=828s)** output quality. We want to be able to uh evaluate the correctness of skill invocation. And we want to be able to AB test these skills. So if I have a different version of the same skill, which one performs better? So we want to have those informations. So that's a bit about where we are today and where we're going to go in the near future. Um if you want to connect with us, please connect with us at the this event and if you don't get we don't get a chance to meet here, please connect with us on LinkedIn. Thank you. >> [applause]
