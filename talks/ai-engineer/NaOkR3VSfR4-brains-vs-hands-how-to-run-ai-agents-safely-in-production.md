---
id: NaOkR3VSfR4
title: "Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya"
slug: brains-vs-hands-how-to-run-ai-agents-safely-in-production
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Viren Baraiya"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-08T22:30:09Z
video_id: NaOkR3VSfR4
url: https://www.youtube.com/watch?v=NaOkR3VSfR4
youtube_url: https://www.youtube.com/watch?v=NaOkR3VSfR4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "agent harness", "durable execution", "workflow orchestration", "Conductor", "Orkes", "AI agents", "agents in production", "sagas", "human in the loop", "SRE agent", "deterministic workflows", "Netflix Conductor", "Viren Baraiya", "AI engineering", "AI Engineer"]
topics: ["Agents & orchestration"]
transcript: true
---

# Brains vs Hands: How to Run AI Agents Safely in Production — Viren Baraiya

**Viren Baraiya**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#agent harness` `#durable execution` `#workflow orchestration` `#Conductor` `#Orkes` `#AI agents` `#agents in production` `#sagas` `#human in the loop` `#SRE agent` `#deterministic workflows` `#Netflix Conductor` `#Viren Baraiya` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=NaOkR3VSfR4) · [Conference site](https://www.ai.engineer/)

## Description

Let the model decide what should happen next. Never let it improvise how a production cluster gets restarted.

Viren Baraiya, co-founder and CTO of Orkes and the original creator of Netflix Conductor, explains how to run agents in production. Real agents aren't just chatbots: they run on schedules, react to events, coordinate other agents and can run for months, so the harness around them starts to look like an application, much like a set of microservices. His key idea is a clean split between the brain and the hands. The LLM plans what should happen next; a deterministic, durable harness does the actual work, with approval gates, idempotent steps and recorded side effects. He frames agent harnesses as late-bound sagas, workflows the agent assembles at runtime, and demos an SRE agent whose plan is compiled into a Conductor workflow, executed, checked and re-planned over two loops.

In this talk:
• Background, scheduled, event-driven and long-running agents
• Why the harness is the application, mixing deterministic and non-deterministic parts
• The brain and the hands: the LLM plans, the harness executes
• Demo: an SRE agent's plan compiled into a durable workflow

SPEAKER
Viren Baraiya, Co-founder & CTO, Orkes
X: https://x.com/virenbaraiya

LINKS
Orkes: https://orkes.io
Orkes on X: https://x.com/orkesio

CHAPTERS
0:00 Intro
0:47 Who runs agents in production?
1:12 Beyond the hello-world agent
1:52 Background, scheduled and event-driven agents
2:27 Coordinators and multi-agent systems
3:02 Agents are applications, not components
3:12 Lessons from microservices
4:22 The harness is the application
5:02 Deterministic and non-deterministic parts
6:02 Harnesses run for seconds or months
6:41 Durability is table stakes
7:26 How the loop works
8:21 The agent plans, the harness executes
9:21 Human approval gates
9:41 Idempotency and side effects
9:56 The brain and the hands
10:21 Agent harnesses as late-bound sagas
11:21 Every possible branch
11:51 Demo: an SRE agent
13:31 Compiling the plan into a workflow
14:16 Demo: the second loop
15:56 Conductor, open source

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,852 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=1s)** [music] Cool. Um, thank you all for joining this morning. Um, I know it's been an exciting uh week. A lot of talk about agents, uh, building agents, coding agents and everything. And uh what I want to talk uh in the next 15 20 minutes is is about running agents in production. Um and things that is kind of on the top of pretty much everybody's mind when it comes to building agents and running agents is you know harnesses before I get started like I would like to ask in the audience right um how many of how many of you are running agents in

**[0:50](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=50s)** production today? Awesome. So a lot of hands up. Um I was in another conference couple of weeks ago and I asked the same question. I think I had like one hand. So this is pretty good. It seems like you know things are moving forward. Um all right. So when we think about agents right like uh if you go back to kind of the hello world equivalent examples of agents uh it's always starts with you know an agent with a tool call and how LM kind of decides to call the tool maybe use some sort of context or a memory and and plans things ahead right um what what we start to kind of realize is you know that's a very small narrowed picture if you think about it uh when you think about agents in production

**[1:37](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=97s)** it's not just always about chatboards. Um the early examples that we had seen were all about like you know hey we are going to build a customer service chatbot or some sort of chatbot. Um but when we start thinking about agents in a broader terms and picture uh think about background agents uh background workers agents that are running on schedule um I would like to have an agent that runs every hour to check uh what's happening with my schedule and if there is something new that has popped up that I should think about uh event-driven agents right agents that are listening on various events. Um to give you an example, I have a production system running where my alerts are firing every now and then. I have a logs coming through hotel. I would like my agents to listen to those events and react on it and see what's going on there. Right? Um

**[2:26](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=146s)** I could have longunning coordinators. And what I mean by that is I have an agent running for a longer period of time. I would like to have an agent monitoring that agent to see, hey, what's going on there? and should I nudge that agent to kind of move forward, take a different action and things like that, right? Um, also one more thing is about multi-agent systems, right? Agents talking to other agents. Uh, the last thing you want is to have an agent be responsible for multiple things and risk hallucinations. U so more we think about agents, right? uh the way I would like to think about is the agent starts to feel more like an application not just a component right u if you go back to the old school thought of microservices when we and probably we

**[3:16](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=196s)** are still building microservices right um you are not going to ship a microser in production that does everything right it kind of stops being a microser at that point in time uh typically we are shipping multiple microservices They are talking to each other through choreography or orchestration and you have an application that is relying on that set of microservices uh which essentially are single responsibility principles uh to kind of deliver the business goals. There is kind of a very clear uh parallel to that when it comes to agent harnesses right if you think about a harness that is responsible for achieving a specific goal. So let's say I have an harness for doing my S sur work. Um it's operating on multiple

**[4:04](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=244s)** agents to see what's going on there, right? Maybe it's listening on events coming from my logging system talking to my Kubernetes cluster as an agent uh to find out, you know, what's going on there. Uh my metric systems, my customer service uh dashboards and and so on and so forth. Um and what I want to drive there is that if you think about it right your harness is the application and vice versa right an agent alone doesn't kind of deliver the whole premise but rather when you start putting things together and you build an harness that controls the execution of the agent delivers on the premise that's where you start thinking about um an application right and which is you have systems uh which are your databases your internal systems enterprise systems

**[4:52](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=292s)** you have humans, human in the loop. You have tools through either APIs or MCP that is all kind of playing together. Um, and as I mentioned, right, harness runs more than just an agent loop. And this is an important thing that I kind of learned uh while trying to build harnesses for real world production use cases. It's a combination of both deterministic and non-deterministic part of the application. Right? Non-determinism is delivered by an LLM in terms of reasoning, in terms of thinking process. Um, and then there is nondeterministic and there is deterministic part, right? Which you do not want non-determinism sipping into it, right? Think about payments. um or let's say if I have an agent harness that is responsible for monitoring my production deployment how

**[5:41](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=341s)** I manage my Kubernetes clusters I probably want to have a very well- definfined workflow in terms of what are the sequence of steps that I execute when I want to restart my cluster and that's a very deterministic set of processes which every time it runs I know exactly what it does so I want a determinism to be delivered by my harness uh when it matters Um and of course the harness is a longunning process right it runs across the time it can run uh anywhere from few seconds if it's uh something very quick like hey check what's going on here to all the way running for days months uh even longer than that right think about longunning processes order management systems where you are waiting on third party services to deliver your shipment or waiting on humans to take actions and approve things and so on and so forth or

**[6:32](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=392s)** harness is just waiting right it's waiting for events to happen so when that event happens you take an action and do something around it. So that brings another important point right that when you think about longunning systems you need durability right you want to be able to recover when things fail because at the end of the day this harnesses are running somewhere in your ent infrastructure stack right maybe in the cloud maybe on a sandbox but those things can go up go down there could be network failures partitioning anything that could be happening so you need the harnesses to be durable and one thing about durability here is it's a table stake thing right At the end of the day, durability is the cost of admission. That's not the feature that you are looking for in a harness. Um, and as I mentioned, right, the loop that the harness runs spans across agent um,

**[7:22](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=442s)** and everything else. So now let's think about uh how the harnesses kind of operate, right? Um, if you think about a harness, right? and and a loop essentially what it is doing it it has the state of the world it knows what work has been completed um what has been recorded in terms of the side effects right so like if I did a cluster restart I know I have that recorded uh if I sent an email I know that has happened um I know what worked what didn't work and then based on the current state of the world and the goal I know what needs to happen next right and that's where the reasoning and LLM comes into the Um and what really happens here is that

**[8:11](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=491s)** if you think about a clear distinction and this is the most important thing if if one thing that I would like everyone to take away from here is this slide which is that the responsibility of a non-deterministic agent is to plan is to plan what should happen next and not really to do things. Um and then harness is the one who does actually execution and and this is important for uh various reasons right one being that harness is a deterministic piece of code that actually understands what is involved in you know actually executing this piece of work. So as I mentioned right if I am trying to build a harness that runs my DevOps or S sur agents uh when the agent says that hey this cluster is unhealthy and you should

**[9:00](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=540s)** restart harness should decide how to restart the cluster what involves in restarting cluster and that has to be at least in my world has to be very deterministic set of processes right so that every cluster restart is exactly same there's no other uh cateor agree there, right? Um, also if it needs to have an approval, for example, if I'm trying to restart a production cluster, I probably want to have a human gate probably send a slack message to somebody who say, "Hey, I'm going to restart this cluster. Do you think it's okay to do that or not?" Right? And I do not want this to be left to a hallucination by an LLM that, you know, it doesn't need to do it. It needs to be guaranteed in terms of execution. So, it has to be very deterministic when it comes to those kind of things. uh ideally I want this to be item potent and if not I want it to be recording

**[9:47](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=587s)** that you know it is not item potent and this is what has happened so I can take care of the side effects or I can handle the side effects separately right um so this is the most important thing right the clear separation between as we would like to call right the brains and the hands harness is the hands the brain is the LLM um so yeah if the agent writes the plan uh harness executes the Um, and I'll show you in a brief uh a short demo in terms of how all of these things kind of meshes together. Um, but is this a new concept? Right? If you think about it, this is not necessarily a new concept. This has been around for a while, right? If you think about workflows as sagas which we used to write ourselves and define exactly what

**[10:34](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=634s)** happens, it was a very and it is a very deterministic set of processes. When you think about agentic harnesses, they are essentially late bound sagas. And what I mean by that is that they have a very finite and deterministic set of tools uh at the task that they can operate on. Instead of putting them together up front, the agent is kind of proposing and building them at runtime and therefore they are essentially late bound sagas, right? uh but you get all the benefits of a traditional saga you know workflow out of the box in terms of visibility what's happening being able to control things and deterating upon like you know how far ahead in the future uh the agent is able to plan you are able to kind of plan one step at a time or multiple steps at a time u and yeah if you think about it right

**[11:24](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=684s)** it's it's more like a branching workflow if only you could build a workflow with every possible combination of a branch. Um then you know it kind of builds that thing for you right versus with agents that kind of simplifies the work. Um if you have n number of tools it can do um and different combinations of executions which otherwise is going to be almost impossible to you know think ahead of time and and do it. So let's take a look at it. Right. So what I'm going to do is uh I'll quickly show uh a completed run of what I talked about earlier, right? Um here is one of my example agent that essentially is acting like an SR agent, right? what its job is to do is

**[12:14](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=734s)** understand what's going on in the current system and try to plan what should happen next and execute on those things. So it's essentially a remediation loop that runs twice uh in the first iteration it tries to understand the root cause of the problem tries to uh uh react to that uh observes the output of it and then runs another loop and plans another set of steps to see what should happen next. Right? So as an input to my agent, let's see what was the input given right here. Um so step number one is you know it makes a call to LLM. So as you can see right like it's an S sur agent. Um of course it's a demo so you know everything is kind of pre-planned and uh can demo the output of LLM as you can see right

**[13:06](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=786s)** are the steps uh what it should do it's talking about. So as you can see one more thing here right is that instead of just doing one step at a time essentially it is proposing a sequence of steps to do u you should gather evidences you should analyze logs and if required based on the evidence that you gathered you should either roll back a deployment and then verify recopy this is then given to u a specialized tool called plan and compile. So this is the plan that agent gave. This gets compiled into a very deterministic workflow. Um we are relying on a conductor as a workflow execution engine here. So the output is a fully runnable workflow. This gets executed. So like you know what I'm going to show you here very quickly is how that looks like. Um

**[14:01](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=841s)** so this is the first step of execution. Right? If you look at it here as I said right like we did uh analyze the logs look at the query of the metrics decided to do a roll back and verify recovery and everything. So step number one is completed. It runs another loop. Um same thing goes here. U iteration it decides that okay looks like you know these things have been done. Let's check the downstream and if required verify the recovery and complete it right. Um and then the next one runs and completes the task. But here is an example of a loop that is self uh kind of uh planning right. So and to show you very clearly what's

**[14:49](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=889s)** going on here is a loop um at every step of the way essentially it is looking at the current state of the world. So this is my agentic loop that is kind of understanding the world planning and executing uh one instead of one step at a time it is actually planning multiple steps at a time executing that verifying and completing the loop. Um now this can run in production as many times as you want. This can be running on the events. It can be running on a schedule. Um as I said right like this the whole thing could be running for much longer period of time um as opposed to just running in a short period of time. All right so that's towards the end of it. Um this is kind of um overview of what we just did here. Um as you can see

**[15:39](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=939s)** right in the second iteration we decided not to do a roll back because it was already done in the first iteration. Um but yeah that's about uh the harnesses and agents and how they bring determinism uh to your production application. The example that I showed you runs on conductor uh conductor is an open source uh workflow orchestration platform uh that supports building agentic loops as well as agentic systems. It's fully open source um Orcus we provide enterprise edition. Uh but feel free to try it out. Here's the QR code. Uh give it a try. uh join our Slack and you know if you have questions happy to help. We have a booth here at Orcus uh drop by if you want to see a live demo u if you want to run your lang chain agents or openi

**[16:26](https://www.youtube.com/watch?v=NaOkR3VSfR4&t=986s)** agents or ADK agents conductor can handle all of those things. Thank you.
