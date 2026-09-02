---
id: czfKC-p79tA
title: "Jon Rav Shende - Observability Is Not Governance: Building a Runtime Trust Plane for Agentic AI"
slug: jon-rav-shende-observability-is-not-governance-building-a
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Jon Rav Shende"]
channel: "Berkeley RDI"
duration_min: 16
published_at: 2026-08-12T07:19:58Z
video_id: czfKC-p79tA
url: https://www.youtube.com/watch?v=czfKC-p79tA
youtube_url: https://www.youtube.com/watch?v=czfKC-p79tA
tags: []
topics: ["Agents & orchestration", "Evals, observability & reliability", "Governance, ethics & regulation"]
transcript: true
---

# Jon Rav Shende - Observability Is Not Governance: Building a Runtime Trust Plane for Agentic AI

**Jon Rav Shende**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=czfKC-p79tA) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,911 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=czfKC-p79tA&t=1s)** JON-RAV SHENDE: Thank you. Hello everyone. And I guess big applause for you guys for staying so late. We are running a little bit late as everyone probably realized. I am going to run through my slides pretty quickly. Probably skip some. So if you want to chat, please reach out. Basically, what we're doing is we're building security architects frameworks, as well as looking at multiple things within our operating environment, be it using our own internal systems as well as systems that other end users will be leveraging, hopefully very near. One of the things that bothered me as I started looking at this

**[0:57](https://www.youtube.com/watch?v=czfKC-p79tA&t=57s)** was and we all know what happened last week or week before, where an agent decided to do its own thing. So for me, what we're looking at is what our agents doing? How are we governing our agents? What sort of challenges should we be concerned about with our agents in an operating environment? You heard some really wonderful presentations today. There was super technical one with a lot of code up there. And essentially, we're doing a little bit of the same when you think about orchestration, when you think about runtime, when you think about prompt, when you think about prompt engineering, and so on.

**[1:46](https://www.youtube.com/watch?v=czfKC-p79tA&t=106s)** So for us, when we thought about this situation, not the one last week, but it occurred. But we were thinking hypothetically, what happens if an agent decides to do what it wants to do outside the limits and bounds of what its intent is supposed to be. I think I'm blocking you. So for us, what we wanted to look at was really look beyond the model and look at the control boundary itself. So this is standard Gartner's projections. I'm sure a lot of you here, there's a lot of folks from industry. Do you know Gartner provides a lot of metrics? These are forecast metrics where enterprise are vehemently

**[2:39](https://www.youtube.com/watch?v=czfKC-p79tA&t=159s)** or rigorously deploying or analyzing agents or machine learning, plus LLMs to execute on certain functions, as you saw in some of the presentations before. They say over 40% of that will fail by 2027. That's a projection. When it comes to securing our environments, this is not an industrial benchmark, it's a survey. But 14.4% of organizations are really looking at it from that security perspective, 14.4% What do you guys think about that? As engineers, how many engineers are in the room?

**[3:29](https://www.youtube.com/watch?v=czfKC-p79tA&t=209s)** Oh Lord. Almost the entire room. So as engineers, we are tools. I feel more relaxed. Now, I feel more comfortable. As engineers, we are told, "Hey, we got to build this. We got to ship it, and get it out the door." Ship it, get it out the door, test it, and so on. Then audit comes in. And when audit comes in, they put the brakes on it. And I'll give you guys a quick story. I was working on a system, and we were building. We're doing fine. And audit came to me and said, "Hey, we just checked the agents privileges and entitlements, and it seems as though they can just do anything they want." Yeah right.

**[4:21](https://www.youtube.com/watch?v=czfKC-p79tA&t=261s)** They could have. So basically audit came in and put brakes on what we were supposed to do. We had to stop. We had to re-engineer. We had to work with the identity team. We had to build identities, and we had to ensure with those identities we had assigned intent. And that signed intent, as everyone knows, is a contract that defines what the agent should be doing based on the outcomes it should be delivering in theory. So this basically is our environment before AI. Forget the downstream agents on the right. The user SaaS business systems.

**[5:12](https://www.youtube.com/watch?v=czfKC-p79tA&t=312s)** This is typically how an environment ran. It was linear. We knew what we were asking systems to do. We know what users were doing, and we were able to put governance controls, security metrics around those things. Today, what do we have? When a user or an agent or a user and an agent is working, everything comes together. So a user executes a request that user can call an agent, the models. You heard about orchestration, I'm not going to get into that for the sake of time. And basically what we have here is an entire ecosystem that's taken a life of its own in real time, simultaneously.

**[6:07](https://www.youtube.com/watch?v=czfKC-p79tA&t=367s)** So what do we have to do? What we're doing at Thales, we're looking at multiple things from the execution, the runtime governance as well as evidence layer. Because simply saying, "Hey, we're going to follow linear processes. We're going to follow a linear governance model. We're going to follow basic testing that we do for software. We're going to embed QA and so on is not enough today." Simply because we're looking at workflows that are occurring in Tandem. We are looking at functions that are tied to those workflows that sometimes we're not sure who is responsible, who is accountable for those functions within those workflows.

**[6:55](https://www.youtube.com/watch?v=czfKC-p79tA&t=415s)** So now we have to build a database or a collection of transactions that has records. And what those transactions when they are executing, what is the impact? How can we build risk metrics based on those impact and then create that evidence layer? So basically at the bottom, we're subdividing everything based on a human request delegated authority and delegated authority. You guys have heard subagents and so on. And basically the challenge and the concern for me and my team is when we assign privileges and entitlements to a subagent, is that subagent acting as it should?

**[7:49](https://www.youtube.com/watch?v=czfKC-p79tA&t=469s)** If it's acting on behalf of another agent and it inherits the privileges and the entitlements, the authority authorizations of the primary agent, should that be happening? And most of us already know it should not be happening. And most of us in this room are working on making sure that should not be happening. But we are finite group. Over in larger in industry, the challenge I'm seeing is people are skipping steps because we need to build and ship. And if we build and ship, we open ourselves up to risk. So for us with that evidence layer, what we want to do, we're not looking so much as at the agent as much as we're looking at the control path.

**[8:38](https://www.youtube.com/watch?v=czfKC-p79tA&t=518s)** So the control path is dynamic. So we have to have hooks into that control path to basically assess in real time where something could go wrong, to predict what could go wrong, and to define an outcome when something goes wrong and then build risk controls against that. Quite a few times I've given several talks and everybody talks about observability and governance. And we see observability and governance interchanged a lot. Have you guys seen that? Yeah, isn't it frustrating? So for us observability is good. We can see what's happening, but can we do something about it?

**[9:30](https://www.youtube.com/watch?v=czfKC-p79tA&t=570s)** That's the question. And then when we think about governance, we know that we're seeing something occurring because the model is executing. But we need to be able to assess that control path and then apply governance on that control path based on an outcome. And that outcome basically exists to enforce decisions. And those decisions are basically bound to identity, policy, and authorization. So with that, then we can build decision matrix. Once we have that data and we build decision matrix, then on the control path itself we can then enforce controls within that execution path based on risk to the control path

**[10:23](https://www.youtube.com/watch?v=czfKC-p79tA&t=623s)** as we see it. So there observability plus governance. They're not replaceable. They don't substitute each other, but they work in Tandem and in hand and hand. Somebody told me once that AI is all about software. What do you guys think? Yes or no? Yes, hands up. No yeah. Sorry yes. Sorry, guys, I think I messed up this slide. But let's just jump into it. So as we're running systems and as we're testing our systems, we built an entire--

**[11:14](https://www.youtube.com/watch?v=czfKC-p79tA&t=674s)** I would say for want of a better word, we built a contract and we built a database that with all the agents within our environment, we basically defined what those agents were doing, what they were interacting with, what tools they were calling, and what systems and so on were being engaged? And basically, that's what declared authority. Now when everything was running, guess what happened. We saw variances. We saw variances that was not what we told the things to do in the declared state of declared authority. So basically what we started to do was analysis around that variance.

**[12:08](https://www.youtube.com/watch?v=czfKC-p79tA&t=728s)** So with that variance we basically built that across our runtime trust plane. And we were comparing declared versus observed, and the metrics from identity delegation policy risk and the evidence layer I showed you guys earlier. Now, all of that is good. Some people say drift is bad. What do you guys think? Yes, probably no. Yeah. Not necessarily. Drift is not necessarily bad. We need to know the delta. So basically when we looked at our environments what we did was we built explained variance that we categorized those as shown allowed

**[13:00](https://www.youtube.com/watch?v=czfKC-p79tA&t=780s)** approved drift and control failure. What do you think was the most important metric we looked at there? Two minutes. Control failure. That was the most important metrics we looked at. Thank you. You got it. So I have two minutes. With this, when we were building our engineering environment, we basically constrained it on four constraints here. And we were looking at, I spoke about ephemeral agents. We looked at the drift from what we were seeing. And then as someone mentioned earlier, the health care gentleman from Oracle mentioned, when we build systems, we look at latency,

**[13:51](https://www.youtube.com/watch?v=czfKC-p79tA&t=831s)** and that affects our costs and so on. So that was another metric we looked at and we took those three. We took the data from that and we built a containment path. And that containment path, basically, one minute, was really engineered to have a defined kill switch where we can take the action of quarantine, rollback, get a secondary authorization or just stop. This one is really important. When we were running our systems, the key thing for us here was the function from agent and the decision proposal. We basically looked at the envelope

**[14:45](https://www.youtube.com/watch?v=czfKC-p79tA&t=885s)** within our runtime trust plane across those four authority, policy, risk tier, and evidence before we could do an execution commit. But that wasn't just all that we did, we tagged that with risk categories where a low risk would auto execute and so on. And then the high risk needed human approval. So with that said, if I can have 30 seconds. What we have built in our environment is a record of trust that is tied simultaneously across the top boundaries. And basically that record of trust runs in real time. So everything from identity to action,

**[15:33](https://www.youtube.com/watch?v=czfKC-p79tA&t=933s)** we monitor and manage that. And we build that authority of trust. This is our environment where we have built the premise of what the concept of guardian angels, and we can-- guardian angels, sorry agents. We can talk about that since my time's up later on. So thank you very much, and guys, have a good rest of the evening. [APPLAUSE]
