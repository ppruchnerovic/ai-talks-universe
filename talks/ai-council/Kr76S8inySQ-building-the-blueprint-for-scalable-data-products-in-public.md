---
id: Kr76S8inySQ
title: "Building the Blueprint for Scalable Data Products in Public Sector | City of San Francisco"
slug: building-the-blueprint-for-scalable-data-products-in-public
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: ["County of San Francisco"]
channel: "AI Council"
duration_min: 9
published_at: 2026-06-18T22:16:13Z
video_id: Kr76S8inySQ
youtube_url: https://www.youtube.com/watch?v=Kr76S8inySQ
tags: ["AI"]
transcript: true
---

# Building the Blueprint for Scalable Data Products in Public Sector | City of San Francisco

**County of San Francisco**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `9 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=Kr76S8inySQ) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] This talk will provide a practical framework for moving past "innovation theater" to build durable, production-grade data tools within public sector constraints. We’ll explore how to navigate legacy infrastructure and strict compliance requirements to deliver real value to citizens.

SPEAKER:
Soumya Kalra - Chief Data Officer, City and County of San Francisco

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,716 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Kr76S8inySQ&t=0s)** Hi, I'm Samia. I'm ready to talk about uh scaling data products in the public sector. Um and really I'm going to start with something provocative. So, AI is cheap, right? And we're going to spend the next 15 minutes just explaining why that's a problem and not the solution. Um so, let's start with the some examples. Um so, basically, you know, 2025, Taco Bell rolls out AI voice ordering, right? Across across many drive-throughs. One customer ordered 18,000 cups of water. The system accept like accepted it, crashed, virality ensued. Um and obviously the program had to be rolled back, right? Low stakes. And I think I've seen this example at at other talks here. Um Around the same time, you had United Health deploy an AI model to make Medicare Advantage coverage decisions,

**[0:47](https://www.youtube.com/watch?v=Kr76S8inySQ&t=47s)** right? So, this means that the models actually recommended uh things that were against doctors' recommendations, denied care, um and had a 90% error rate. So, that re- that basically resulted in a lawsuit and potential for irreparable harm. So, it's the same technology, uh but very different consequences, right? And the difference isn't the AI. The difference actually is the infrastructure underneath it. Um and what happens when that infrastructure fails. So, really I think what what I have been grappling with as I as I'm maturing in this job is that governance uh overhead is proportional to stakes. It's actually not bureaucracy. It's good having good engineering judgment. So, government keeps teaching treating uh data infrastructure as a cost center and AI as the cool new investment, and

**[1:36](https://www.youtube.com/watch?v=Kr76S8inySQ&t=96s)** that's actually backwards. So, AI's cheap, right? As we all know, uh API calls are fairly um you know, fairly cheap. Models are easy to access and continuing to get better and better as evidence of this talk at this conference. But the infrastructure is the hardest part. Even my previous uh uh uh, a here uh talked about this. Uh, so legible governed data is years of engineering and really hidden behind good demos and, uh, making it hard to put things in production. So, to give you an example, this is the oldest system we have today. Um, this is the tax system. If you guys are not aware, this is actually still run with COBOL and assembly language. It was set up in the 1960s and it's still the authoritative system of record today. It's wild. Uh, there have been a number of efforts to help modernize this. It's con- and

**[2:25](https://www.youtube.com/watch?v=Kr76S8inySQ&t=145s)** continues. There's a lot of parallel testing. There's no confirmed retirement date and it's still looking like we're looking at 2030, which is already slipping. While at the same time, the, uh, in the federal government, there's a lot of interest in and any other municipal, local, state government, there's a lot of interest in identifying AI use cases and all the AI investment is really real. People want to keep this. But I again, I want to emphasize that the infrastructure running underneath it hasn't changed since the Kennedy administration, right? That's That's crazy. Um, so really this boils down to two big problems that are creating this gap. One is The first problem is data fragmentation with no shared definitions, right? What does that really mean? So, every agency, department, whatever you want to call it

**[3:11](https://www.youtube.com/watch?v=Kr76S8inySQ&t=191s)** at whatever level of government you're looking at, defines the same thing differently. So, a veteran in one system or one agency is not the same anywhere else. Second, the data exists, but it can't be read by anything. And this is the world that we all in in government live in right now, okay? Uh, and then lastly, you have no SLA on freshness, which means there's no guarantee of con- of actual correctness on the data. And, um, this continues. So, the second problem, right? Is that every time there's a new policy initiative rolled out, it has to be built on its own stock. Because these because of the fragmented underlying data systems, there's always time pressure to deliver something. There's no shared infrastructure, so then you set up a standalone stack. What that means is it's its own schema, own definitions,

**[4:00](https://www.youtube.com/watch?v=Kr76S8inySQ&t=240s)** own pipelines, right? And it connects to nothing else. But that's great when you're able to launch that policy initiative, but then it really creates a problem when you're talking about trying to actually measure outcomes of how something delivered across multiple programs, across multiple agencies. Like who actually got what they wanted. I hope this is actually these problems are like a call to action to all of you to realize that there's so much opportunity to try to fix things in government, so that I'm not the only one out there. Okay. Um and really what that means, these problems actually help us identify um and I help us identify the gap. And what will make what will reduce the gap is making data legible to AI. Means and that really means exposing it, right? And these are two competing tensions. You have legibility, what AI agents need, which is queryable, has to be

**[4:49](https://www.youtube.com/watch?v=Kr76S8inySQ&t=289s)** queryable, uh queryable, uh consistent definitions, it's fresh, it has to be permission to request. Versus also at the same time it has to be compliant, has to be auditable, has to be class classified in the right way, and you actually have the authority to operate with all of the use cases. So, working in working in a complex regulated environment where the harms are really um are really big if things go wrong, both of these have to be right. And both of these have to be I have to make it happen. And that's why it's really hard. And so what does production grade really mean? And production grade means both legible and governed, right? So, I want to get I wanted to lay out like a quick maturity curve for all of you to think about where government agencies are at, and we can talk about it in a second. So, there's three sort of levels of where agencies are at. One is reactive,

**[5:38](https://www.youtube.com/watch?v=Kr76S8inySQ&t=338s)** L1, right? They're starting in silos, they've got everything is manual, it's on prem, AI's really not that it's it's not possible in like a real way. Um so it's not legible. The second one, second level, is it's a central warehouse, pipelines are automated, but there's no governance that's actually actionable and implemented into the uh technical architecture. So, it's legible but without any safety. So, partially legible. And then the last one is production grade, right? Where you have certified data, named owners, SLAs, you have real good role-based access, AI at scale with audit trail. And most folks, most agencies have like just gotten to the point of getting out of L1 to L2, and at that point they feel like they're ready to go. They're they feel safe, but they're not really safe,

**[6:25](https://www.youtube.com/watch?v=Kr76S8inySQ&t=385s)** >> [laughter] >> and they really shouldn't be launching things in production. And so, let's talk about how you get from get what decision framework you use to get to L3. So, really it's a couple of things. So, four decisions get you to L3. One is really having um strong uh governance and ownership. So, and this doesn't cost you anything, right? You just have to have negotiation, have clear humans map to data sets, and move on. Second is you have to have one definition in code across every system, right? So, like if I say the word veteran, it should be veteran across every system with the same thing that's encoded. Third is your role-based access, right? You want to make sure that your if you're not allowed to see it, your agent's not allowed to see it, no exceptions, right? And then lastly, your ingestion. This is uh this is the crux of where even our team has been

**[7:12](https://www.youtube.com/watch?v=Kr76S8inySQ&t=432s)** spending a lot of time is actually building a lot of the ingestion uh patterns, and this is where most of the investment has to go to if we really want to make this uh productionable and usable. Okay. So, the other piece I would say is also before any agent really touches your data, here are the three questions I would think about as you're thinking about this framework. Is one, do you know who uh what is the data and who owns it? Do you have uh rights to actually use it? Second, who can see it and in what context? So again, authentication is not the same as authorization of use cases. And number three, is it fresh to act on? So can you actually use it to do things? If you can't answer these three, then you're not ready to deploy an agent in a complex environment like this. Okay, so talking a little bit about my

**[7:59](https://www.youtube.com/watch?v=Kr76S8inySQ&t=479s)** team, the team that I run within the city of San Francisco. We actually are have heavily investing in building this data infrastructure for the city of San Francisco. And so before, this is where we we started with a lot not a lot of shared infrastructure, lots of lots of manual work being done, lots of lack of standard definitions. And what we are internally now building is the unified data platform. It's built on a data lake. Um we have certified data sets, we're building a semantic layer for various domains. We're actually connecting all of the departments onto it so there's to leverage zero copies. And the biggest piece, the biggest win, which is what I see, um is that the new programs, new policy programs that are getting stood up are getting stood up on this stack so that we can actually measure outcomes over time across.

**[8:47](https://www.youtube.com/watch?v=Kr76S8inySQ&t=527s)** Um and that's really the most meaningful change. So the yes, you get to use the coolest tools, but you also get to actually tell deliver services for residents. Okay. Um and so yeah, that's pretty much it. AI is cheap, infrastructure is the hard part. Uh we're building a platform engineering team and an enablement engineering team. We're hiring, come join us. Help us help us make real difference in real in people's lives. >> [applause]
