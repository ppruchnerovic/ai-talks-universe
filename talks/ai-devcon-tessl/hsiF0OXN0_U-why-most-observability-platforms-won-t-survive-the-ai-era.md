---
id: hsiF0OXN0_U
title: "Why Most Observability Platforms Won't Survive the AI Era"
slug: why-most-observability-platforms-won-t-survive-the-ai-era
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 12
published_at: 2026-03-09T14:01:06Z
video_id: hsiF0OXN0_U
url: https://www.youtube.com/watch?v=hsiF0OXN0_U
youtube_url: https://www.youtube.com/watch?v=hsiF0OXN0_U
tags: []
topics: ["Evals, observability & reliability"]
transcript: true
---

# Why Most Observability Platforms Won't Survive the AI Era

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=hsiF0OXN0_U) · [Conference site](https://tessl.io/devcon/)

## Description

Dash0 CEO Mirko Novakovic breaks down what actually works (and what catastrophically fails) when you try to scale AI observability from demo to production. The gap between "one trace" and "one million traces" is where most AI tools collapse, and vendors aren't telling you about it.

In this segment:
- Why the AI gave perfect answers on OpenTelemetry data (it had memorized the test)
- The scale wall where LLMs work on 100 traces but break at 1 million
- How open standards accidentally built the perfect AI foundation
- What you need when AI demos stop working in production

The demo-to-production gap is where most AI bets fall apart. Here's what survives contact with reality.

Mirko Novakovic: https://www.linkedin.com/in/mirkonovakovic/
Dash0: https://www.linkedin.com/company/dash0hq/
Guy Podjarny: https://www.linkedin.com/in/guypo/
Tessl: https://www.linkedin.com/company/tesslio/

## Transcript

*2,235 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=0s)** If you are running something like AWS Lambda or any managed service and you want to provide telemetry data of that service, how do you do that? You either provide it in 20 formats like DataDog, New Relic, Dash Zero, or you have a standardized format that everybody can understand. And OpenTelemetry actually was the first approach to standardize this format, right? So that you have no proprietary data. If you look at a lot of vendors, they say we support OpenTelemetry. What that means is that you can send them OpenTelemetry data. They take that data and convert it into their internal format. What we have built is something where the data is always OpenTelemetry because all the models by default understand the format, understand OpenTelemetry, and therefore can really work with it similar to what they can do with code, right?

**[0:51](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=51s)** >> [music] >> Just to dig in, start by giving us a bit of context of like Dash Zero, the company you've built and are running today. Tell us a few words about it and and some of its core. Yeah, so um we are an AI-native observability platform. When we started, we were not promoting AI-native. At the beginning, we were OpenTelemetry-native. And that turned out to be a good foundation for AI, by the way. So the idea was there's a new standard in observability called OpenTelemetry, which standardizes the format of the telemetry data, logs, metric, traces, end user events, and also standardizes the tagging system on that telemetry data, which is called the semantic convention. So post name now is host underscore name or

**[1:40](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=100s)** host.name. And um that that is the way we have started. So we built a full platform for logs, traces, metric, end user monitoring, taking only OpenTelemetry data into it and keeping it as OpenTelemetry and making the the out of the semantic convention by creating context. So, if you look at a trace, you see all the logs, you see the metrics, the underlying infrastructure, everything in context based on the semantic convention. And we try to make a very easy onboarding flow, PLG type of sales motion, and and having it easy to use. So, let's start by why why I think it's also meaningful, right? Before OTel, it is every vendor, including myself as Instana, did their own format, right?

**[2:29](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=149s)** So, we had an agent, and so you specified your own format, and you send your own format. >> old-school agent. This is the tracing agent, not an AI agent. Exactly. That's the old-school agent that you install on your host, basically, and that captures the data, right? The CPU utilization, the logs, and and the traces. Exactly, it's not an AI agent. The benefit was that you could make everything you needed for your platform, right? Into the format, and you could do do some auto metrics. So, for example, if the agent was running on the host, you could add the host name because you were running on it, and just send it over, right? Um and Open Telemetry actually was the first approach to standardize this um this format, right? So, that you have no proprietary data. And the And I think the main drivers were the cloud

**[3:16](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=196s)** providers because if you are running something like AWS Lambda or any managed service, and you were to provide telemetry data of that service, how do you do that, right? You either provide it in 20 formats like Data Dog, New Relic Datadog or you have a standardized format that everybody can understand. And that's how it started, right? So, I would also say, if you look at a lot of vendors, they say, "We We support Open Telemetry." What that means is that you can send them Open Telemetry data, but I would say still 90% of the vendors, they take that data and convert it into their internal format. Right. >> Because that's how the platform is built. So, you can send it, but then in the system essentially the tagging system etc. is gone, right? Because it's now

**[4:03](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=243s)** datadog format or Yeah. format of any other vendor, right? And I think what we have built is something where it the data is always open telemetry. It stays open telemetry. I think there's only one tag that is mandatory and that's service name. Okay. So, the only >> tag the the only tag in and and so essentially everything that emits telemetry data is a service, right? In that that sense. And so, if you have a service, I don't know, payment service and you send a log, you add the service.name equals payment service. Yeah. And if you have a metric of that, you do the same and now you can correlate everything on a service level by saying give me all the metrics, logs, traces Right. of that service name. Yeah, that's that's the only thing that's mandatory and that's also that's also a bit of a problem, I would say,

**[4:52](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=292s)** for vendors because we also see that a lot of the data we get from customers at the beginning does not have all the information that would be needed. For example, if you now ask, "Give me all the logs of that pod or that host." If that log does not have the pod name and the host name as a tag, we can't do it, right? Because again, going back to proprietary agents, there we could add that information to the log or Yeah. ourselves. But now we are relying on the customer sending us the right context and if we don't get that context, we can't really Yeah. recreate it, right? By the way, I think there is also a big chance for AI. When these LLMs came out and we started experimenting with it, that we saw that we get really good results with those

**[5:42](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=342s)** platforms like Claude, for example. We use Claude internally giving us really good results by saying, "Hey, analyze this trace, right?" And be >> Right. put in the trace, which is literally a text format of tags, right? >> Yeah. Which is specified by OpenTelemetry. And now the thing is, because it is actually open source, it's openly documented, it's an open standard, all these models are trained on the data, and they literally understand that host.name is a host name, and they can start basically understanding the context, getting what is uh HTTP status code 404. Yeah. >> know that it's actually a problem, right? And now it can really analyze these things. So, OpenTelemetry turned out to be really useful because all the models by default understand the format, understand OpenTelemetry, and therefore

**[6:32](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=392s)** can really work with it, similar to what they can do with code, right? Right. >> It's like it's a text structure, text format, very well specified. It has a syntax, it has semantics, and so it it can actually really do interesting things and analyze uh uh telemetry data. Uh I mean, we were really impressed by the output, right? And by the way, funny story is when we started, there is a OpenTelemetry sample application, also open source. Yeah. >> And the sample application has very well documented problems in it, right? Different types of errors. And when we started with LLMs, we asked the LLMs about problems in that sample application because it was running, and it always gave us perfect answers. And we were super excited at the beginning, but it turned out the LLM was also trained with the problems

**[7:21](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=441s)** documented >> Yeah. on the actual list. So, it could do it because it was >> cheat the test. It could cheat the test because it knew the problems up front, right? So, so results were the amazing at the beginning, but then we figured out, "Okay, it's actually not that amazing with other things." And then we kind of connected the dots that it was already trained on the documentation of the problems, right? So, um That's interesting. drilling into that a little bit so like the the LLM's were naturally better and all that was like a nice a nice kind of benefit of choosing open technologies that the LLM's came pre-made or pre-ready to to process open telemetry data. Is it they're not very good at analyzing traces, they're not very good at like understanding time series data, they don't you know the the volume of data a little

**[8:08](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=488s)** bit is there. I guess it On those fronts like hotel note hotel like that doesn't terribly matter, right? Or like I guess what has been your experience in terms of like the the native support of like just drop this trace in into whatever Claude or ChatGPT and and get some result. I think there are two separate problems, right? One is you have one trace and there is a problem in it, right? And the erroneous fan or something. If you do if you do drop that trace into for example Claude, I think it will definitely come up with an analysis say hey, I see there's a problem with this trace and depending on the metadata it gets, for example it's a database problem and it gets gets a database status code in there from an Oracle database, it will look up that

**[8:57](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=537s)** error code and will give you context on that error. So they are really good at saying hey, this is actually I don't know exhaustion of the connection pool in the Oracle database and you should do this and that based on the documentation. This is essentially what you would do as a human, right? You you would see that code and then search for it and it does the job for you. Where it is not really good if you have thousands or millions of traces to figure out anomalies instead of A because the they they can't really do that large amount of data, right? The volume. So what you have to do there is you have to provide the AI agent the right tools to do the analysis, right? So have a functionality, for example, called triage. What triage does it it compares you give it a million

**[9:44](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=584s)** traces and ask is there any anomaly in it for erroneous traces and it would look at all the um tags and would tell you, "Oh, the the the ones with the error always have this customer ID as uh uh as as a tag and then it will return that result." And now we provide that tool to the agent through an MCP server, right? And the agent can now the agent can now use that tool that triage tool right and it will use it, right? Autonomously it will say, "Okay, there's a problem. Let's figure out if there are any anomalies, so let's use that triage feature." So, yes, you have to build your API essentially in a way that it works for the agent and that the agent can use it. Yeah, to be consumed. So, I

**[10:32](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=632s)** think maybe let's delineate. So, we want to talk a little bit about sort of the the the way in which AI meets uh you know, observability uh needs and sort of that type of analysis. And I think there are sort of three uh uh pillars here to to talk about. One is, you know, what we started talking about here, which is more the kind of AI powered, like how do you how do you use AI to an agent to to to be smarter, right? To sort of you know, offload more of that work, provide good functionality. The second is about agent as a consumer uh and you know, I think it started now talking about the agent will consume So, I want to disabiguate a little bit of uh which agent is that? Is it your agent or is it like class agent? And then maybe we go a little bit more philosophical, talk about sort of product and talk about scope and uh uh and the likes. Um so, maybe maybe let's start so we started, you know,

**[11:19](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=679s)** like digging a lot more like the agents can do this, it can't do that. Uh so, why don't we talk like you have a bunch of agent powered observability. Um I don't know how you call them, I'll let you say that in a second, but under the under the mantle of agent zero uh is the capabilities. So tell us about that. Like what are what is what are useful things to do today with AI when it comes to to this world? I mean there's when we started agent zero was just one AI agent but then over time we figured out that there are actually a lot of use cases where where I agents make sense and now agent zero is just a platform for agents and we have different ones and I think the most prominent in the whole space there's also a category AI SRE agents Yeah. is essentially troubleshooting, right? I mean you you get a call 3:00

**[12:08](https://www.youtube.com/watch?v=hsiF0OXN0_U&t=728s)** a.m. in the morning there's an outage you have a problem and now you want AI to support you in figuring out what the problem is. >> [music]
