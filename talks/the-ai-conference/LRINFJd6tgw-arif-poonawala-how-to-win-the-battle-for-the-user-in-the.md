---
id: LRINFJd6tgw
title: "Arif Poonawala: How to win the battle for the user in the agentic age"
slug: arif-poonawala-how-to-win-the-battle-for-the-user-in-the
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 9
published_at: 2026-10-07T22:54:26Z
video_id: LRINFJd6tgw
url: https://www.youtube.com/watch?v=LRINFJd6tgw
youtube_url: https://www.youtube.com/watch?v=LRINFJd6tgw
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Arif Poonawala: How to win the battle for the user in the agentic age

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=LRINFJd6tgw) · [Conference site](https://aiconference.com/)

## Description

The AI era looks like a fight over models, chips, and compute. The real fight is over the user. Whoever delivers the best experience wins the market, and agents are now the front line of that experience. Most agents are losing it. They launch blind to the people they serve and miss the moments that decide whether a user stays or leaves. The gap between shipping an agent and shipping one people actually rely on is product context: the behavioral and business signals that tell an agent when to step in, what to say, and whether it worked. This talk makes the case that the companies who win the age of AI won't be the ones with the most agents. They'll be the ones whose agents truly understand the user, and shows what it takes to build them.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,359 words · source: supa (en, exact timings)*

**[0:49](https://www.youtube.com/watch?v=LRINFJd6tgw&t=49s)** All right, thank you very much. Um, I'm RF. I'm a product leader here at Pendo. Uh, for context, Pendo is a product analytics and a usability platform. Uh, what we do is we help product builders build the best user experiences. uh get the best data to understand the best usage and inject those into user experiences with uh things that allow the user to be the most successful they can be. And in this talk, we'll talk about how we extend that to the agentic era. Um everyone's kind of seen a a portion of this like stat before. You know, lots of people are creating agents. Uh agents have the promise of making workflows efficient. uh user value and generating like really really good user experiences, right? But connecting the dot from its potential to

**[1:37](https://www.youtube.com/watch?v=LRINFJd6tgw&t=97s)** actual value is really really hard. And so what we do at Pendo is we really take a look at the user experience first. Uh we believe that the answer actually lies within the user. Uh if you look at what the user is trying to do, understand the data around that user and you inject that back into the agent, then you have the right recipe and the right tools and the right context for that agent so that they can actually deliver and move that metric, that user value metric, that metric that then translates to business value. um that missing layer that we have at Pendo is that product context layer. And so what we do and we've done this internally and we've seen a lot of good

**[2:24](https://www.youtube.com/watch?v=LRINFJd6tgw&t=144s)** results with our own agents that we've deployed is that we we inject what the user did and what they're trying to do into the agent. Uh we give it that context of like what job to be done or why is the agent even here? What workflow are they trying to make efficient? What is the end goal? and how do we drive conversion to that goal? Right? Uh when you inject that context in one, you give it the ability to use it, understand it, uh improve that workflow, and then two, you give it the ability to act on it, right? If you know what the workflow that you're trying to make efficient, if you know more about the user, you know the data around it, you can help the agent be more proactive to get there. Um and so together we call that pendo for agents. Pendo for agents

**[3:14](https://www.youtube.com/watch?v=LRINFJd6tgw&t=194s)** has two components here. Uh we have an analytics or an observability component. And so what we do here and how this kind of differentiates from traditional observability is our focus is to tell you if the agent was able to do the job that it was created for. uh you can create custom metrics to know did it actually drive the user to conversion not if only if there was an error or if there was a mistake that's made along the way. Um and so that's our analytics or observability layer and then we take all of that data along with the broader product data that we have or user data that we have and with agent toolkit we enable the agent to proactively act on that data. Right? Imagine that if you can take uh what you know about customers, what you know about

**[4:02](https://www.youtube.com/watch?v=LRINFJd6tgw&t=242s)** workflows, uh what you know about other customers or users that are trying to do the workflow that the agent was meant to automate, uh how would you use that data to drive a more efficient user experience. And so let's go into each one of these. So agent analytics uh the core differentiator and how Pendo generally differentiates itself uh from other analytics or observability tools is that we put the user first. We want you to measure everything in terms of did user did we create user value? If we can create user value that creates business value. And so like you'll see things like frustration metrics. uh was the user having a good experience? Were they like responding in rage for conversational metrics, right?

**[4:53](https://www.youtube.com/watch?v=LRINFJd6tgw&t=293s)** Uh how do we take that information and really use it to optimize a user experience? This is something that may not show up in an eval. It may not show up in a trace. The tools may have been perfectly right, right? Uh it might have been performant. It might even have been costefficient. But if it doesn't get the user to the goal that it was created for, it's really not a good experience. And so that's what we put as the center of this. And so it really measures against the values you care about. You can set these up as custom values and metrics and as part of the larger Pendle platform. You can see that online or agent to non-agent user experiences and really put it into one big user flow. Um, we don't just stop at just like user metrics though, right? Uh, we do continue to pull in all the traditional

**[5:43](https://www.youtube.com/watch?v=LRINFJd6tgw&t=343s)** observability metrics, the tracing, um, all of the latency, the cost, and what we try to do is take that data and let you attribute user experiences and outcomes to that data, right? uh let's say you have a trace uh shows no errors everything is kind of going through right but if you map it to a metric like did the user able to complete the workflow that it was created for then you can map and see if that trace or that tool is driving the user behaviors that you want within the agent is the agent able to get that user to the end goal. um you're able to attribute different tools and context to those things and know what really drives user experience there. Um you can take that and all of that data and wrap it around

**[6:31](https://www.youtube.com/watch?v=LRINFJd6tgw&t=391s)** an Asian toolkit that allows you to drive action from that. Right? You can in real time watch customers as they go through your product experiences when you know they're entering a user experience that's frustrating or uh they're rage clicking somewhere. You can use that data in real time to wake your agent. Your agent can then use the context of what workflow they were in or what they were trying to do to be smarter about what they're going to help the user kind of accomplish at the end. Um and so This is us really being able to take the guidance piece and inject product context in there to help the agent be smarter. They know more about the user. They know more about what they're trying

**[7:18](https://www.youtube.com/watch?v=LRINFJd6tgw&t=438s)** to do and they are better and more efficient at getting them to the end goal. Uh another good example of agent toolkit is helping uh helping complete automated workflows, right? I with agent toolkit you know when an user or someone or even an agent is starting at a workflow. You can track it. You can understand what areas in that workflow they get stuck and wake the agent to empower the user to complete that workflow. You can give it context on like hey this is what you came to do before. Uh you've done this workflow before and this is where you get stuck. Uh this is what you need to do to get past it. Um, and so it really provides you a way of taking all of your agent data, uh, your product context data, your user data, wrap it in what we're

**[8:09](https://www.youtube.com/watch?v=LRINFJd6tgw&t=489s)** calling product context, and give it back to your agents so they can be more efficient, more effective, and better at getting users to the end goal that they're trying to get to. And so that's the talk. I we we believe we've seen really good results with this. We use this internally for our internal agents. Um, you know, we think it's the missing layer between agents that are, you know, they work basically that they do the right thing versus agents that actually.
