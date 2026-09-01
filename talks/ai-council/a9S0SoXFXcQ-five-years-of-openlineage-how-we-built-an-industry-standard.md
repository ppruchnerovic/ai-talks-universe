---
id: a9S0SoXFXcQ
title: "Five years of OpenLineage: How we built an industry standard and why agents need it | Datadog"
slug: five-years-of-openlineage-how-we-built-an-industry-standard
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 8
published_at: 2026-06-18T22:16:13Z
video_id: a9S0SoXFXcQ
youtube_url: https://www.youtube.com/watch?v=a9S0SoXFXcQ
tags: ["AI"]
transcript: true
---

# Five years of OpenLineage: How we built an industry standard and why agents need it | Datadog

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `8 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=a9S0SoXFXcQ) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] Over the past five years, OpenLineage has become the de facto standard for data lineage metadata, adopted across the industry by leading platforms and enterprises. In this talk, we'll trace the journey of building an open standard. You'll learn what changed in the ecosystem that made standardization possible, the critical features that drove adoption (column-level lineage, streaming support, unified facets), and where OpenLineage stands today - five years since its initial release. Most importantly, we'll explore why this matters now: as AI agents increasingly make decisions about data - where to read from, what to trust, how fresh it is - they need a shared understanding of data context. Lineage metadata is the knowledge graph that transforms agents from black boxes into informed decision-makers. The talk covers the standards perspective, the pragmatic integration challenges, and a forward-looking vision for how great metadata enables intelligent data systems.

SPEAKER:
Harel Shein - Senior Engineering Manager, Datadog

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,472 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=0s)** Yeah, I'm Furel. I work at DataDog. I also work on OpenLineage. Um quick show of hands, who knows what data lineage is? Okay. Who's heard of OpenLineage? Okay, so some slides are useful. All right, so data lineage is basically metadata about data pipelines, right? It is about where data is coming from, where it's going to, what are the transformation uh that are happening in the middle, and kind of being able to reason and understand data pipelines. And part of what makes data lineage especially difficult um in our data ecosystem is that it's very fragmented, right? You have a bunch of different vendors, you have a bunch of different frameworks and platforms, um and it is really really really hard to speak a shared language for all these.

**[0:49](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=49s)** And, you know, you can imagine a certain situation where, you know, you come to you travel to a different country maybe, and you try to plug in to the hole, and you know, you kind of expect the current to come out, but it's not really coming out. You can't put the thing. It It has the same current, it does the same thing, it transfers electricity, but it doesn't really work. So, to make it really work, we need to all be speaking the same language, a shared language for a lineage. Um so, what do we do in this case? We need a common language to talk about uh data lineage. So, how do we get there? Um so, I had to put in this uh classic way, right? There are 14 ways of doing a thing, let's add a new way. So, you can, you know, be very pretentious and say, "No, no, my way is better, and I'm going to show you how to

**[1:36](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=96s)** do it, and you're going to all going to agree." But, that's not how you really build community, and you really build traction around the thing. So, the way that you actually start to do this is you find a group of people who care about the same problem as you. Um you kind of get a coalition, you find what is the commonality between all of them. Um and then you start to align incentives between different groups of people and kind of over time you build the thing. And that's how we kind of got OpenLineage to where it is today, and I'll share more um about that. But, before we go further, let me talk a bit about OpenLineage and how to observe data lineage. So, we basically see three main ways of observing lineage. One is you can analyze source code. So, you can look at the the source code for a data pipeline for a job and kind of infer from it um

**[2:26](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=146s)** what is happening and infer the lineage relationships. Uh you can look at activity logs or query history and parse that out. And from that you can infer lineage relationships. Or you can observe the pipeline as it runs. There's a bunch of metadata that happens there. Um and then from that you can report lineage as well. Um I'm kind of burying the lead here. This is uh our approach at OpenLineage and why we think collecting lineage at runtime is useful. So, imagine you're taking a picture. You can look at the image in retrospect and you can see, "Okay, well, the sun's the more or less over here. I'm at the beach. Uh I can guess more or less the time of day. I can try to guess where in the world this picture is is taken. Or I can just look at the metadata that the camera captures. That's a kind of a more accurate way of of knowing where this picture is from."

**[3:15](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=195s)** Um and so, that is the approach that we took in OpenLineage. So, OpenLineage is uh it's a specification. At the end of the day, it is JSON. Um it is the vendor neutral. It is uh anchored under the Linux Foundation. Um and it also provides a shared common libraries for um specific frameworks that I'll show in a second. Um and integrates with a bunch of data tools. Um And so, why does that matter? Why do we need that shared language? So, we talked a bit before about kind of like, you know, the the frustration of coming in um with the plug and not being able to to put it in the hole. So, if you're trying to consume metadata from a platform, you then need to build point-to-point solutions. You have to rebuild them again and again and again

**[4:02](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=242s)** and again. And that's very frustrating and it's just a lot of boilerplate code to rewrite over again. And so, with OpenLineage, you kind of don't have to rewrite that, right? We all agreed on the language, we all agreed on the specification. We can just consume and produce events using this. Um so, a bit about the spec. So, the spec contains three core concepts. There's a job, which is a thing, an entity of a thing that does something. Um there's an instance of it, which is a run. And then we have datasets, which are kind of inputs and outputs uh to that specific run. And all of them can be extended via facets. And as we've seen, this flexibility actually allows for a lot of expansion of the spec and support for a bunch of different use cases without breaking that shared commonality and that shared core concepts of languages.

**[4:52](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=292s)** Um there's also the concept of run events. So, basically, as events happen, they you transition in states. So, a job can start and then it could be in a running state, and then it can get into a terminal state or kind of keep producing events as the job runs. Um and at the end of the day, as a consumer of this data, the way that you actually build your your mental model, the way you build the the picture of lineage, is based on correlation. So, in the spec, we kind of say, "Hey, if you're looking at a Postgres uh table or or or database, then this is how you describe the location of a table." And we all agree that this is the way to do it. And then you were able to stitch together that information, even though it's coming from different sources of telemetry. Um so, kind of reflecting a little bit about how we got here. So, it all

**[5:41](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=341s)** started in 2018. Uh Willy here uh is uh the original author of Marquez. So, credit to Willy. It's all started at WeWork. We were building a metadata store because we kind of needed it and it was nowhere to be found. And then over time from Marquez, the idea of basically creating a a vendor neutral not tied to anything specification came. And from there on out, adoption really grew. We started by seeding a first few integrations and then the community kicked in. And really today, there are roughly 40 producers and consumers of open lineage. It's adopted by all the major clouds and it's pretty cool. So, the way we got here was by aligning incentives and it was by making sure

**[6:29](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=389s)** that everyone can participate and everyone gains from it. And kind of there's no friction or competition necessarily when we're talking about the specification. And that's really the snowball effect we got to. So, I'll end with this last point. So, now we have agents writing a lot of the code. And I think it makes open lineage and data lineage even more critical because, you know, they're writing jobs and they're producing data and they're consuming data and they're they're moving it around. But in many cases, you don't even know what you're doing there, right? You're just like you're telling it what to do, but you don't know what data it's touching, where it's moving data from. So, really you kind of want to have that level of observability and traceability of what's going on. You need to be able to trust

**[7:16](https://www.youtube.com/watch?v=a9S0SoXFXcQ&t=436s)** that it's touching the right data. If you sometimes want to reproduce the thing, you kind of need to have that system of record that's auditable and that's repeatable across multiple platforms. And since this is a short talk, I'm going to end here. And if you anyone has any questions, wants to get involved in the open lineage community, it is a very nice and welcoming community. Go on our Slack Um, or anywhere. If you care about what I do at DataDog, you can look at that as well. And thank you so much for being here. >> [music]
