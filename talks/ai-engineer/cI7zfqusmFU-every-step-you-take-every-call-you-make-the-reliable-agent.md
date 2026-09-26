---
id: cI7zfqusmFU
title: "Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate"
slug: every-step-you-take-every-call-you-make-the-reliable-agent
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Giselle van Dongen"]
channel: "AI Engineer"
duration_min: 21
published_at: 2026-09-14T15:30:30Z
video_id: cI7zfqusmFU
url: https://www.youtube.com/watch?v=cI7zfqusmFU
youtube_url: https://www.youtube.com/watch?v=cI7zfqusmFU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# Every step you take, every call you make: the reliable agent stack — Giselle van Dongen, Restate

**Giselle van Dongen**

`AI Engineer` · `AI Engineer` · `2026` · `21 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=cI7zfqusmFU) · [Conference site](https://www.ai.engineer/)

## Description

A research agent asks a human to approve its plan, then waits. The wait might last a month, spanning restarts and redeploys, and while it waits the function consumes no serverless execution time at all. Giselle van Dongen builds Restate, and that suspended promise is the clearest illustration of what durable execution buys you. Her talk skips the agent loop itself and goes after the infrastructure underneath it, the part she argues teams keep rebuilding badly: retry logic, recovery logic, session isolation, and stopping something already in flight. Restate runs as a server in front of your agent service, proxying requests and holding an open connection that acts as a lifeline. As the agent works it emits events to a journal, and that journal replays the process back to its exact failure point rather than starting over. The design borrows from Apache Flink and Meta's event infrastructure, and it pushes invocations rather than polling, which is where the low latency comes from.

The demo is a deep research agent living in Slack. A planner proposes subtopics, parallel sub agents go to work, and an injected tool failure shows a web search retrying and completing instead of sinking the run. Then it gets more interesting. Because a session is modeled as a virtual object with its own key and isolated state, van Dongen can talk to a run already in progress. She tells it midflight to focus on frontier models and a classifier decides that is relevant, so it signals the live loop. She then tells it to research something else entirely, and the cancellation rewinds down the call chain, killing sub agents before the controller.

Speaker info:
- https://x.com/vdgiselle
- https://www.linkedin.com/in/giselle-van-dongen/

Timestamps:
0:00 - Three waves, and where agents are heading
1:53 - The infrastructure layer nobody wants to write
2:45 - Four ingredients of a durable foundation
4:29 - How the journal recovers a failed run
5:20 - Demo: a deep research agent in Slack
7:51 - Making a step durable in code
8:42 - Suspending a month for human approval
9:32 - Virtual objects as stateful actors
12:10 - Signaling a running agent loop
13:51 - Cancelling and rewinding the stack
17:19 - Inside the distributed log

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIE New York, October 12–14 — the first AI Engineer Finance mainstage summit
- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*3,368 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=cI7zfqusmFU&t=12s)** Hi everyone. This talk will be about how to run agents reliably in production. It will not be about the eile part, but it will be about all the other things you need to get going in order to run agents resiliently. So the infrastructure layer basically. I want to set the scene with this uh quote of Andre Apathy of last week. It describes that the way we interact with agents and LLMs has been evolving in three waves. The first wave was an LLM being something like a website where we go to we ask it a question, it thinks for a few seconds and then gives us a response. The second wave was going towards agents. It was an app that we download to our computer. It has some tools at its disposal and it can do some work with our interaction. Now the third wave will be going more

**[1:02](https://www.youtube.com/watch?v=cI7zfqusmFU&t=62s)** and more towards persistent and asynchronous entities. So agents being longunning processes in our infrastructure with access to tools and other agents around the organization and context. And so as our use cases are evolving more and more from single agents to agentic platforms that connect parts around uh the organization our infrastructure layer should also evolve with that. So when we look at the types of tools that are currently out there to implement agents, a lot of innovation has been done on sites such as agent SDKs and memory. And agent SDKs are really cool to implement PC's and get started quickly, but they don't necessarily help with like connecting the distributed bits around an

**[1:49](https://www.youtube.com/watch?v=cI7zfqusmFU&t=109s)** organization. And if you want to implement more complex agentic systems, you actually need all of those things. So that is the layer that you see below here where um you have to deploy extra infrastructure. Uh you need to write things like retry logic, recovery logic and all of that is actually pretty complex to get right but completely necessary to run longunning stateful and distributed processes in production. So today I want to talk about an open-source framework called restate. And you can see it a bit as a flexible durable foundation that lets you build any backend. So it's not specific for agents but a as agents are also just a type of a backend uh it also works well for them. The ideas behind restate come

**[2:37](https://www.youtube.com/watch?v=cI7zfqusmFU&t=157s)** from Apache Flink which is a popular distributed stream processing engine and also from some of the exarchitects behind Meta Score event infra. So what are the ingredients in restate? Basically four parts. First of all, it makes sure that a single run of an agent is resilient. This is called durable execution in the industry. Think about things like when an agent runs for a week and then crashes. We want to be able to bring it back and let it continue exactly at the point where it failed. We don't want it to start over from the beginning. Another um area here is running many concurrent sessions in parallel. Imagine running thousands of concurrent agent sessions at the same time and needing needing to make sure that state is

**[3:26](https://www.youtube.com/watch?v=cI7zfqusmFU&t=206s)** always consistent and that different agents don't interfere with each other. And then going more towards things like communication between agents, between agents and MCP servers and other tools. And finally also control, making sure that when an agent for example uh is doing um something you don't want it to continue or when it's stuck being able to actually cancel or kill the execution. So the way that you can think of it is as follows. Restate is basically a server which runs in front of your agent service. So as a separate component it sits there a bit like a like a message broker or a proxy and when there's a request for your agent restate proxies the request to the service and pushes it to the service basically and from that moment there's a connection open

**[4:15](https://www.youtube.com/watch?v=cI7zfqusmFU&t=255s)** connection between restate and the agent and that connection will basically be a bit like a lifeline for the agent. So as the agent is doing stuff, it sends events over to restate and restate will use that journal of events to recover the process after a failure. So from a slightly higher level um explanation, you could say that it's turning a normal function in your application into something that is long running, durable, and stateful without having to do um a lot of the complex things you otherwise need to do for this. So my talk today will be mainly a demo. So I'll be showing you um a research agent that is connected to Slack. Imagine we are like working at some company and we want to make an Slack agent available to all of our employees.

**[5:03](https://www.youtube.com/watch?v=cI7zfqusmFU&t=303s)** So if I go here into Slack then can I can here in this channel for example ask what is new in AI. Now let's have a look at what it's doing under the hood. So if I go back here, I have here the restate uh UI. This is a bit like a cockpit for your agents. So you can see a registry of all the agents that are currently registered and you can also see for example which execution is currently happening. So here is the deep research agent that I spinned up a few seconds ago. We can see what it's currently doing. Now it called first an LLM and then it sent me an answer via Slack. This first LLM call was a planner agent. So what it did is it planned the research and sent me um a list of subtopics that it wants to research.

**[5:53](https://www.youtube.com/watch?v=cI7zfqusmFU&t=353s)** Now if I press here approve then this will unblock the workflow and will spin up a set of parallel research agents. So this is basically like the classical deep research workflow, right? You have a planner then a set of subress research agents and then finally someone uh who writes a report on this like a writer agent and so this journal you see here on the left that is basically the events that get sent from the agent to the restate server and if this now crashes at some point this journal is what will be used to uh recover the execution to the point where it failed. I don't know if uh there were some errors. I injected a bit of like tool errors in here. Yeah, here you can for example see that um the sub agent first did an LLM call then started

**[6:42](https://www.youtube.com/watch?v=cI7zfqusmFU&t=402s)** doing some web searches and eventually uh one of the web searches didn't go through because the API was down and then you see here on the right how it got retrieded and eventually completed successfully. So instead of starting over, it uses the journal to recover the progress. Let's now have a look at what this looks like in code. So the basic unit of how you implement applications in restate is by writing HTTP handlers and those handlers become durable by using the restate SDK. So here in this case we have here our deep research handler and here as a first argument we have a restate object context and the way you can imagine that is basically as that uh connection to that restate server. whenever I do an action on this uh restate object, it

**[7:30](https://www.youtube.com/watch?v=cI7zfqusmFU&t=450s)** will lead to an event being sent to restate. So for example, when I did that planner LLM call, what actually happened under the hood was it executed here this Python function. This is just a simple light um light lm like LLM call and the way I made it durable is by wrapping it in restate.run. So what happens is by doing these durable steps if this fails somewhere here two hours or two months later it will recover to exactly that point. So that's the idea of durable execution. You're always able to recover a process to where it was. You can also use that for other things not necessarily for failure recovery. For example, imagine we want to ask a human to approve

**[8:17](https://www.youtube.com/watch?v=cI7zfqusmFU&t=497s)** something and this approval might take weeks or a month. this process needs to be able to um to survive restarts and redeploys uh over those kind of long periods of time and so with durable execution you can actually also uh suspend a function and let bring it back when it's able to make progress. So in the case of a human approval what we do here is basically we we create a durable promise which lives in that journal a bit like a suspension point. Then we ask uh a human to click that button in select as I showed in the beginning and while we are waiting this process actually suspends. So if it's running on serverless this is not using uh execution uh time on our functions. Once the response comes in this then

**[9:08](https://www.youtube.com/watch?v=cI7zfqusmFU&t=548s)** gets unblocked and can continue where it left off. So what we see here is a bit like a workflow. It's a set of steps that get executed durably. But when we think about agents and also the way that Karpathy described it in the tweet, it's more like a persistent stateful entity that lives for a longer period of time that has some memory. Um, so a workflow is not the nicest way to model this kind of thing. So the way that we can model this in restate is by using something called a virtual object. So imagine in the use case that I'm showing this slack research agent. Imagine that I don't want to wait for 10 minutes to give it some follow-up context or maybe I think about something else that I should have told it. Um I want to actually be able to interact with it, not wait till that

**[9:56](https://www.youtube.com/watch?v=cI7zfqusmFU&t=596s)** research is finished before I can send a follow-up. And so this is basically what a virtual object in restate is. It's a bit like a stateful actor. It has a unique ID, for example, a session ID. It has uh some key value states that is isolated for that specific session that you can write to. Uh imagine for example your history of messages and it also has like a set of handlers that can execute durable functions uh for this session. So here the way I implemented this use case that I mentioned of interacting with a running process is as follows. This is a um a bit a session controller. Again, it has like this restate object context at its disposal to do things in a

**[10:45](https://www.youtube.com/watch?v=cI7zfqusmFU&t=645s)** recoverable way. Uh it can write to this session store. Here it I'm retrieving the chat history. And one thing that's interesting there is that in order to run these kind of sessions in very high uh paralyzed ways, so thousands of sessions at the same time, we need to make sure that agents do not interfere with each other. Imagine I'm sending two messages on Slack and now two agents are actually overwriting each other each other's session state. To prevent that, this will guarantee that only one execution is running at a time. So a second execution will be cued behind the current one. Then let's have a look at how we implement this like interacting with another execution. So an execution in reset has a unique identifier and you

**[11:35](https://www.youtube.com/watch?v=cI7zfqusmFU&t=695s)** can use that identifier to connect to it from other processes. for example, to retrieve uh the output, but also to cancel it or maybe to signal it being injecting a bit of state into an already running agent loop. And so this is like a very flexible type of um uh capabilities that you can do to implement things like for example signaling an already ongoing agent loop. So what we do here is if there is a current execution ongoing then we will ask an LLM is this like something that is relevant for the current agent loop. If that is the case inject this via a signal if it's not really relevant for what we're currently doing then cancel what you're currently doing and start

**[12:22](https://www.youtube.com/watch?v=cI7zfqusmFU&t=742s)** over again with this new information. And so this goes a little bit further than workflows. it goes a bit more towards like writing persistent stateful entities that can interact with each other and have memory at uh their disposal. So let me show you uh how this works. So here if I now ask again what is new in AI and I wait a few seconds then it should respond again with a plan. Um and then I can say for example some extra info focus on frontier models let's say. So once I have the plan I will inject that bit of extra state. Now let's look at the UI of what this is now doing. So here I have that

**[13:10](https://www.youtube.com/watch?v=cI7zfqusmFU&t=790s)** controller which I just showed. It started calling an LLM to classify uh this new input. Once this comes back, it will probably decide that it should signal it because it's it's still relevant to the research it's currently doing. So this inject that new message into the ongoing agent loop. So let me show you in the deep research agent again. Um so first it called an LLM then asked us then we injected this uh new message of focus on frontier models and then it uh took that into account and started over again. Here I can now for example also say something like uh forget about that research AI policy.

**[14:00](https://www.youtube.com/watch?v=cI7zfqusmFU&t=840s)** And if I send this then the coord coordinator will um decide to cancel the ongoing run and start a new one that will research this new topic. And so this cancellation is basically like a signal that gets um sent down the stack of or the call chain. So if my agent was already spinning up sub agents first those sub aents would be cancelled then uh the controller itself and like that it would basically rewind the stack and give agents also the ability to roll back. Okay. Okay, so this went a bit more into the direction of like stateful persistent entities that we can interact with over longer periods of time. Now the last part of the demo that I want to show is um going more towards like being able to write highly customized

**[14:49](https://www.youtube.com/watch?v=cI7zfqusmFU&t=889s)** applications. Imagine that we deploy this in production but then a few months later a new model provider brings out a new model for example fabulous and even though the model is very good it's also very expensive and we notice that this research agent is actually starting to cost a lot. These kind of uh things that pop up halfway through a project require you to then deploy a a lot of new extra infra or like find a good way to solve this. This is the kind of things that Restate really excels at. It doesn't really peg you into a specific way of how you should write your application. It basically gives you like a durable programming model that lets you implement an application in the way that fits for you and also extend it if necessary. So first I showed this um LLM call in the first example as an inline

**[15:41](https://www.youtube.com/watch?v=cI7zfqusmFU&t=941s)** step. It was just a Python function that got persisted. But imagine this use case that we want to actually have a bit more control over those LLM calls. For example, what you can do is then pull this out into its own handler. And this handler can now do things like for example a policy check and then uh do the LLM call. And the other agents instead of doing this LLM call inline can now use restates like distributed communication primitives to actually just call this LLM gateway instead of doing it as an inline step. And this service fabric that lets you communicate between agents also gives you some um things like flow control. So we can for example say one department is only allowed to run 300 calls to this LLM

**[16:31](https://www.youtube.com/watch?v=cI7zfqusmFU&t=991s)** gateway at the same time. So the reason why I showed this was just to show you a bit like that. Uh it's basically just a a resilient foundation. It makes sure that your process can uh recover from even a more advanced types of infrastructure failures, things like network partitions and zombie failures. And um it gives you like tooling to extend and customize as your use case grows. Let's go back to the slides to have a little more of an idea of how this thing is actually implemented on the inside because it's actually a pretty interesting um design or architecture. So the way it's implemented is basically by having a a event-driven distributed log implementation. So inside the box you basically on one

**[17:20](https://www.youtube.com/watch?v=cI7zfqusmFU&t=1040s)** side have the clients on the other side the services and inside the box is a log which persists all those journal events and an event loop and that event loop basically gets the events from the service based on what the event is. It either persists some state in the embedded state store or it sets a timer or it sends a request to another agent. And by doing that you basically have a durable um foundation for whatever an application is doing. The design of this distributed log is heavily inspired by the way that the core event infra layer at meta works. Uh it's basically like an iteration on top of that. Um and some of those architects are now have designed that for restate as an more generic solution that is

**[18:10](https://www.youtube.com/watch?v=cI7zfqusmFU&t=1090s)** available in open source. There are two important things related to this architecture that make it interesting. The first one is that it works as a push model. So whereas most workflow orchestrators actually pull for new tasks um for pull from the workflow server, restate actually pushes the invocations and the benefit you get from that is that it has a much lower latency. So you can use these kind of workflow guarantees in functions around your application and uh have like a latencies of for example 45 milliseconds p99 for like a 10-step workflow. Pushing invocations also works very well for serverless because they require you to basically uh send the request and wake up the function. So this design

**[18:59](https://www.youtube.com/watch?v=cI7zfqusmFU&t=1139s)** that I show here includes everything you need. It includes uh as well that state store where we were embedding the state as the UI. It's a single binary so it's pretty easy to operate as well to run it in like a highly available way. You just spin it up multiple times and let it snapshot to object storage. So restate has six different SDKs. We also have integrations for most of the popular agent frameworks out there. And of course, because it's just like a flexible layer, you can also just use any LLM SDK and implement custom agents by just wrapping some steps into uh these SDK constructs. So, it's open source. You can self-host it. We also have a BYOC offering where we deploy restate in your cloud account and uh

**[19:51](https://www.youtube.com/watch?v=cI7zfqusmFU&t=1191s)** that gives you the benefit that data doesn't leave your cloud account. Otherwise, there's also a managed cloud offering. This was mainly what I wanted to show. If you want to explore the code a bit further, there is here this the GitHub repo. It's publicly available. If you like the project, then have a look at the restate repo itself. We are hiring across the board for all sorts of roles going from engineering to marketing, especially also here in the Bay Area. So, if you're interested in that, uh, then definitely check out our careers page. and I will be outside in front of the conference hall here if you want to ask any questions or learn more about restate. Thank you very much. >> [music]
