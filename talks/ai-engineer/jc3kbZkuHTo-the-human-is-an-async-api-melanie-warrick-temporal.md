---
id: jc3kbZkuHTo
title: "The Human Is an Async API — Melanie Warrick, Temporal"
slug: the-human-is-an-async-api-melanie-warrick-temporal
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Melanie Warrick"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-10-04T16:30:17Z
video_id: jc3kbZkuHTo
url: https://www.youtube.com/watch?v=jc3kbZkuHTo
youtube_url: https://www.youtube.com/watch?v=jc3kbZkuHTo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "human in the loop", "durable execution", "Temporal", "AI agents", "multi agent", "Google ADK", "LangGraph", "agent harness", "workflow orchestration", "distributed systems", "fault tolerance", "agent reliability", "Python", "Melanie Warrick", "AI Engineer"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# The Human Is an Async API — Melanie Warrick, Temporal

**Melanie Warrick**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#human in the loop` `#durable execution` `#Temporal` `#AI agents` `#multi agent` `#Google ADK` `#LangGraph` `#agent harness` `#workflow orchestration` `#distributed systems` `#fault tolerance` `#agent reliability` `#Python` `#Melanie Warrick` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=jc3kbZkuHTo) · [Conference site](https://www.ai.engineer/)

## Description

Humans don't respond in 200 milliseconds. Your agent shouldn't fall over waiting for one.

Melanie Warrick from developer relations at Temporal shows how to build human-in-the-loop agents that don't block or lose state. Using a live multi-agent ice cream delivery demo with fleet, customer and dispatch agents on Google ADK and LangGraph, she explains why durability belongs in the agent harness and how Temporal's workers, workflows and activities track state. She shows how two primitives, a wait condition and a signal, let an agent pause for a human for minutes or weeks. Then she kills the worker mid-approval and brings it back with no lost work.

In this talk:
• Why a blocking 'ask the human' call breaks in production
• Temporal's workers, workflows and activities, and where model and tool calls belong
• Wait conditions and signals for human-to-agent and agent-to-human flows
• Deciding when a human should be in the loop: the cost of being wrong vs alert fatigue

SPEAKER
Melanie Warrick, Developer Relations, Temporal
X: https://x.com/nyghtowl

LINKS
Temporal: https://temporal.io
Temporal (GitHub): https://github.com/temporalio/temporal
Temporal + Google ADK: https://adk.dev/integrations/temporal/
Temporal + LangGraph: https://docs.temporal.io/develop/python/integrations/langgraph

CHAPTERS
0:00 Intro
0:13 Demo: Ziggy's ice cream delivery
1:13 Google ADK + Temporal
2:03 Human in the loop: changing an order
3:38 The human is an async API
4:13 What's in a harness?
4:58 Durability belongs in the harness
5:47 How Temporal works
6:27 Workers, workflows and activities
7:22 Back to human in the loop
7:47 Why a blocking call fails
8:02 Wait conditions and signals
9:22 Starting the second demo
10:12 The code: ADK integration
11:37 Agent to human with LangGraph
13:42 Demo: a high-value order needs a human
15:07 Killing the worker mid-approval
16:02 Recovery and replay
16:47 When should a human be in the loop?
17:47 Recap
18:17 Resources

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,431 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=13s)** All right. Well, I'm here to talk to you today about this demo and I've already stepped outside the box they told me not to step outside of. Anyways, I'm here to talk to you today about an ice cream delivery demo that I've got for you and ultimately I'm here to talk to you about Temporal. So, you're going to hear me pitching about the company that I work for and specifically in a way that will be about this ice cream delivery that's happening as you can see online right now. So, what's happening? Well, this is Ziggy. Ziggy's Ziggy's is our mascot. I love Ziggy. And Ziggy has an ice cream store, not really, but let's say he does down in the Ferry Building. Currently working hard delivering all kinds of ice cream. Now, what's happening on this screen is that um we have multiple agents that are currently coordinating the delivery that's happening for deliver for Ziggy's ice cream service. We have

**[1:02](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=62s)** a fleet agent and a customer agent and a dispatch agent all working in coordination to make sure that the ice cream goes where it needs to go. In this specific demo, what I've got up here is showing you we have 80K integrated with Temporal. So, 80K is a um solution that Google's providing to help you orchestrate agents or multiple agents um and in this case it's specifically helping to coordinate the activities in relation to these agents. And Temporal is baked into it. We are integrated into it so that we can help track the state of what's happening with this kind of delivery. So, Temporal actually helps you track your state and manage that state and we provide a UI that allows you to see what's going on on that screen. So, this is what you're seeing over here. And in that UI

**[1:51](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=111s)** it's showing you the event history. There's this this is the parent workflow for all the activities that are happening for Ziggy right now in its delivery suite. And in this world, sometimes what we'll have in multiple agents is we need to have human in the loop. So, let's say a customer made an order and the customer said, "Hey, I think I changed my mind about that order. So, I'm going to submit a change." And of course, when you do submit that change, it will not it if you depending on how you build it out, it could actually break your system. But, heaven forbid you have it break your system when somebody has a change to submit. In this case, we have an order and this order is currently pausing driver A. And so, driver A is waiting for that update to come through.

**[2:40](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=160s)** The system is running while this one specific change is only pausing one part of your system. That one change coming from a human. And another human needs to make a call and whether or not they want to accept that. So, they say approve, and you'll watch that as I mentioned, the rest of the system kept running, orders were coming in, they're being filled, but in this specific question that came up about changing that order, the update is getting processed and should go through in a second. I suspect internet is part of it. You can see it does get processed, the update is read, and that order will now move on to its next location, which is to the Oracle Park. And there goes little A delivering the order for you.

**[3:28](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=208s)** So, there you go. That is durable execution with Temporal and 80K integrated. All right. I'm here to talk to you about the human is an async API. Let's go into First off, we've been hearing about agentic loops, right? You can reason, act, and observe. That is our whole thing that everybody's been talking about when they're talking about building out these agents and these agents running as autonomously as we possibly can. Um there's this kind of loop that we're looking at, right? We've heard other words for this where we're thinking, we're acting, we're perceiving. Um and that's that's the essence of it. It can be a for loop, it can be a while loop. Most of this year we've been hearing people tell us about the harness and

**[4:16](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=256s)** what the harness is supposed to be to help us get those agents into production. So, the harness I'm not going to sit here and tell you I I am the expert on the harness. Um I'm going to tell you from everything I've researched, I'm trying to give you at least a map to a degree of what I understand so far with the understanding that there's a lot of debate about this. I've heard that the harness is possibly the model is is part of all of this or it's not. I think there's there's debates around whether the model's in it, whether tools are in it, memory's in it, uh guardrails, security, but ultimately it's all about getting these agents with structure so that they can work reasonably well when they're put out into production. And part of that picture should be durability. The system that I showed you, the demo that I just showed you, this is what it

**[5:04](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=304s)** is. It's got these loops. We've got a loop for the fleet agent, we got a loop for the customer agent, we got a loop for the dispatch agent. The fleet and the customer are doing research. One's doing it on the actual drivers using thing tools like Google Maps. Um the other one is doing research on the orders like Google with tools like Google Search. While the dispatch agent is taking that input and making decisions with it. All right. So, that's great that these activities are happening with these three loops and we've got the human potentially providing input in part of this structure. But what's important is that we need to have some durability in that system to make sure that it stays up and running and doesn't fall over. And that's where Temporal comes in. So, Temporal is helping you to standardize your fai- failure handling and your

**[5:51](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=351s)** state management in your system. Any system, any distributed system, especially any systems with agents, we are going to help you standardize that. We're software and we're also a service. The software itself is creating a lot of primitives that you can just use out of the box and basically apply to your code base. We come in all kinds of flavors of code, uh so you can use this in Python or TypeScript or Rust, um but ultimately we're giving you some standard primitives to apply to your code to be able to make sure your your state your your system is stateful. So, the three main primitives we tend to talk about are the worker, the workflow, and the activity. The worker is really running that code. The workflow is where you're going to be able to uh keep track of the steps in your system. And so, this is where like

**[6:41](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=401s)** an 80K framework would be running inside a workflow. Uh your agent could work run inside of a workflow cuz it's a loop, right? Whereas the activity is all the stuff that's integrating or interacting with stuff externally. So, if you've got a loop, uh any kind of model call or any kind of tool call, those would be set up as activities. So, these are the primitives. So, you structure your code with our primitives to be able to track the state of your system. And we're free and open source at that GitHub URL. Um you pay us if you you have us manage your state with our service. Otherwise, you can host it self-host it on your own system. Let's get back to human in the loop. Why uh what I wanted to really get across to you about this whole talk. So,

**[7:30](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=450s)** the human, granted, you know, we're not tools, but we are a tool to the agent. Um and you might think, "Okay, well, we're going to call the human or we're going to have the human come in and give us uh some kind of information to pass into this loop. If you write it just straight out as a function to say call the human or let the human have a an input, it can become a blocking call. And it can get lost if your service went down. It might lose track of what was going on with that human's engagement. What you want is these two core primitives to be applied to your your code and your agents. You want a wait condition and a signal. You're allowing yourself to isolate an event, apply a wait condition,

**[8:18](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=498s)** store that in that workflow, in that durability layer, so that if anything fell over in the system, when that system came back up, it would know where it left off. And you could send a signal at any point, but the whole system could keep running without you necessarily being blocked on that one call to the human. The code pretty much is is is fairly simple in terms of the primitives. And granted, I know this is Python, but it's the same situation. You're going to apply a wait condition and you're going to apply a signal. You basically you're not holding a thread, you're not it's going to survive any kind of crashes. It's got all kinds of built-in primitives like timeouts, for example. If you're waiting on a human to respond

**[9:06](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=546s)** and you want to make sure that it only waits for so long, you can apply timeouts and other types of primitives. Um and this can scale. You can have millions of workflows out there parked, and it can keep running. So, what I want to show you actually I'm going to show you some more code, but I'm going to kick off the next demo so that it's up and running. And I'll share with all of you, if you haven't already figured this out, uh my eyes are injured. >> [laughter] >> I am squinting at times and also realizing that I need additional in support here that I did not prepare for, but that's okay cuz I can adapt. All right, so let's get this other example up and running and then I'm going to tell you a little bit more about the code that's up here. Let's make sure that's running. I'm resetting my example and of course

**[9:54](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=594s)** it's not going to be as easy peasy as I'd like. Also, is everybody hearing me okay? Think so. Great. It's an interesting condition to be working in this space with the noises around us. All right, I think it's up and running. All right, so let's talk a little bit more about the code. Now, I already told you about our primitives of activity workflow and worker. And so with the activity, you are basically for ADK in particular, we have we have the temporal model class that you will wrap around the model and then you'll pass it in for ADK to be able to set up that actual agent. It's pretty simple. You apply this temporal model, you apply our activity tool to wrap around your tools and you you

**[10:45](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=645s)** run your agent. You run your agent like you would with any kind of ADK setup that you're going to do. And you also set up a worker and you pass in the Google ADK plugin. So that's setting up your worker workflow and activity. And then similarly, you have your wait condition and the wait condition is using this async io when it uses a wait to say like for that specific workflow, I want you to pause it, don't run any other code, but you can keep running the co-routines on that workflow or any other workflows in the system. Meanwhile, that workflow.signal, it will be able to take any kind of input and inject it into a running workflow. And the workflow will be taken off of your memory or taken off of your system and put in in parked if it's not running anything at that

**[11:33](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=693s)** point. So, I showed you human to agent. What I want to show you is what does it look like when the agent comes in and needs the human to be involved? It's pretty similar. You're using I'm just going to go ahead and tell you right now, you're going to use a workflow you're going to use a wait condition and a signal. I'm going to use LangChain in this example and also 80K because the reality is with Temporal we can work with multiple frameworks. We are framework agnostic. We work across a variety of different tools. Um so, in terms of LangChain they build out graphs and to build out the multiple agent setup. And in this integration the way we work, you're passing us into each node for your graph. So, you're setting up with the metadata looks like. And if you're making any kind of model call

**[12:22](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=742s)** like an invoke the model, that would be set up as an activity. If you're making any type of other tool call, it would also be set up as an activity. But if it's a step, a step in that process, then that's set up as a workflow. This is determinism and non-determinism in terms of workflows are deterministic, activities are non-deterministic. And then of course, you pass in for the worker the plugin for the LangChain. In terms of LangChain in particular, we use the interrupt to call out from their node. So, this is part of LangChain and also to be fair, LangChain is more than a framework, but in this case I'm using it as a framework. But you use interrupt to call out and then what you're going to do next is use that wait condition in the loop tracking for that interrupt

**[13:10](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=790s)** signal to pause that workflow. And then the signal will capture whatever the human human responds with to the question that's been asked. Okay, let's see what that looks like. I'm going to bring up my demo and show you as they're running. This is the design that I've got. I've got the customer and the fleet agents running on 80K. I've got the dispatch agent running on LangGraph. And Temporal is interwoven throughout. So, that's how that's working. Now, let's see if I can show you. In this case, I'm going to drop a high-value order. This is an order that will most likely want a human involved. The workflow for the whole system is

**[13:58](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=838s)** showing that all these agents are doing their job. They're continuing to keep assessing orders. And the way I've got this set up is I have workflows uh child workflows that are split off for each order per framework. So, that special order actually had its own assessment done. And here we see that the customer and the fleet agents did their work. They did their assessment. They came back with a result. And they sent that off to the dispatch agent. The dispatch agent said, "Hey, okay, I need Oh, well, there you go. >> [laughter] >> I need to get uh a human involved in this. So, I'm going to go into a pause state while I'm waiting for the human to respond." And we know that humans are not going to respond in 200 milliseconds. If you are,

**[14:46](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=886s)** that's great. Maybe there's a there's probably a couple people out there who are. But humans are most likely going to take several minutes, maybe days, maybe weeks, maybe longer. And you can you can because this is just pausing that one specific event. And as you can see, the little cars are continuing to keep going. So, now what I'm going to try to do is show you what happens if I was to take this service offline. So, let's make it bigger for all of us. And kill worker. Cool. So, that takes it offline. You can see it's disconnected. Don't mind me as I do this in a very interesting way. All right. If I say approve while it's offline, so what's happened is as I mentioned,

**[15:37](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=937s)** this is stuff that's happening off of your service. It's over on its own data store. So, we can still keep track of that event and queue it. And then when I bring it back up, yeah, I know. I have this really well organized here here for y'all. But, I'm going to I'm going to bring it back up and then we're going to see if it works. Let's see. Make it. And it's back online. And you'll notice that the dispatch agent will What's happening is that your event log is getting replayed. It's not redone. It's just replayed up until the point at which it last left off, so it knows, here's my current state. And this is now the next step in that state. And it's been queued up to then have that step know that it that the person approved it, and that order got assigned, and it's already been delivered, actually.

**[16:24](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=984s)** So, there you go. That is durability in your system. Your system can come down, and it can recover. And it can have all these other primitives that will help you manage a complex state because these kinds of distributed systems are complex. All right. Last couple things I want to mention. When should the human be in the loop? This is the real question. It's a hard one. I will say this. The big thing you want to take into consideration is the cost of being wrong is high. Okay, it's a case-by-case basis, and we know we're trying to get to autonomy as much as we possibly can. We also know these models are probabilistic, and they are hard to get to a place to be reliable. That's why we got all this stuff happening around harnesses that are interesting. I could go into a whole 'nother conversation about that if y'all want it at a later date. But, ultimately, you

**[17:11](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=1031s)** want to assess the cost of being wrong. What is that worth to you? And especially in a security standpoint. And we know like on the other side of this picture, alert fatigue is real. Like a lot of us are seeing, you know, you just start saying yes, yes, yes, yes, yes every time it asks you questions. So, you're trying to balance between those two. And we're trying to get the models better so that you can trust them, so that you can address that alert fatigue, but they're still probabilistic models. So, when should they be in the When should the human be in the loop? That's the thing you've got to evaluate for the problems that you're solving. At the end of the day though, what you saw there, what I gave you as an example, whether it's the human initiating it or the computer initiating it, um you were seeing that we are using two main primitives in terms of you're applying a weight condition to pause

**[18:00](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=1080s)** that workflow, and a signal from the human to be able to continue the work and say, "Here's the result. Now keep moving forward." And And whether you've actually paused it and taken it offline or you brought it back online. And I've shown you that we can use multiple frameworks. All right, if you have any questions, I'm going to stick around for a few more minutes. Um if you I've got up here a QR code that will take you to some resources about Temporal, as well as some of the demos that I've done, this demo included. This is up on GitHub. Uh the slides itself will be up later cuz of course in true form I've been tweaking them up until now. So, I'll be posting those up and linking them to the GitHub repo. But yeah, if you have questions, please reach out. Um and you know, have fun building your

**[18:49](https://www.youtube.com/watch?v=jc3kbZkuHTo&t=1129s)** agent clips. I'm also curious to hear what your what problems you're solving with agents and how you're building them autonomously currently. So, feel free to find me. And thank you. >> Woo!
