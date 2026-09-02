---
id: FaX4fpEdOlw
title: "Q&A with Chang She, CEO, LanceDB: Why the 20-year-old data stack is breaking under AI workloads"
slug: q-a-with-chang-she-ceo-lancedb-why-the-20-year-old-data
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 21
published_at: 2026-04-21T14:40:48Z
video_id: FaX4fpEdOlw
url: https://www.youtube.com/watch?v=FaX4fpEdOlw
youtube_url: https://www.youtube.com/watch?v=FaX4fpEdOlw
tags: ["machine learning", "computer vision", "AI"]
topics: ["Agents & orchestration", "Classic ML & data science", "Data engineering & MLOps", "Enterprise adoption & strategy", "Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Q&A with Chang She, CEO, LanceDB: Why the 20-year-old data stack is breaking under AI workloads

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `21 min`

`#machine learning` `#computer vision` `#AI`

[Watch the recording](https://www.youtube.com/watch?v=FaX4fpEdOlw) · [Conference site](https://www.aicouncil.com/)

## Description

For 50 years, the pattern has been the same: store the data in the database, keep the big files somewhere else, link them with a pointer. It's powered most production systems we've ever built. Chang She thinks AI is about to break it.

In this episode, Pete Soderling sits down with Chang She ahead of AI Council SF 2026 to talk about why the old data stack wasn't built for what's coming, what agents are doing to database throughput, and why anyone with a serious background in performance "starts to shake in their boots a little" when they think about agentic data access at scale.
About Chang

Chang She is CEO and co-founder of LanceDB, building modern data infrastructure for AI. Previously, he architected the ML and experimentation stack at TubiTV as VP of Engineering. In the mythical pre-pandemic epoch, Chang was the second major contributor to pandas, CTO/co-founder of DataPad, and a recovering financial quant.

Timestamps
00:00 — Storing blobs inline vs. as pointers: the trade-offs
02:34 — When you've blown past the bandwidth limit on object storage
04:03 — Six months trying to make Spark on Parquet work, and why it didn't
06:04 — The moment Chang decided to build something new from scratch
07:35 — Why Chang wasn't worried about adding another tool to the AI ecosystem
11:34 — Agents are firing 100,000 QPS, and most stacks weren't built for it
13:32 — Latency, scale, and the new ceiling for production AI workloads
14:54 — Pipelines written by agents, not humans
16:12 — From co-authoring pandas to rebuilding the stack on top of it
17:27 — Why Chang predicts "multimodal by default" within three to five years
19:48 — What Chang is most looking forward to at AI Council

Catch Chang and the rest of the speaker lineup at AI Council SF, May 12–14, 2026 in SOMA: https://aicouncil.com/sf-2026

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:

## Transcript

*3,345 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=0s)** Um, so Cheng, I just wanted to ask you first, just for my understanding, what's the what's the material difference to storing the blobs in the database versus just having pointers to the blobs as external assets in a file system or an S3 bucket somewhere. First of all, is that a correct interpretation of one of the one of the architectural decisions you made? And if so, like what are the trade-offs there? Yeah, absolutely. It uh it is it is one of the trade-offs. Um so, what what the difference the main difference is uh you you get a lot more um optimizations when you can store the blobs inline. So, uh for example, if you need to access a

**[0:48](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=48s)** chunk of data, like a bunch of images, uh if it's stored inline, that can be one request as opposed to, you know, as many requests as there are images. Um so, one of the problems that a lot of folks run into when working with a lot of multimodal data is getting throttled by the object store. So, if you have tons of images or videos, and you're accessing them through pointers, uh a lot of times people will run into either request limits or they'll get charged a lot for um different number of requests. So, storing them inline makes it faster when you can access them in blocks. Um they you can coalesce requests, and it's just a lot

**[1:37](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=97s)** easier to manage uh for data synchronization. Now, because the a multimodal data can span from, you know, a few kilobytes to multiple gigabytes or even possibly even, you know, bigger, uh you want options. So, that's why we actually we recently released the the blob V2 API, which has the same API but based on the size and the type of data, you can choose between three or four different under you know, storage strategies under the hood. Uh and but for for the user, it appears to be the same API. So you So it's a lot easier to work with while you're enjoying all of the performance optimizations. So you give users the option of

**[2:26](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=146s)** um storing the data the blobs in the database or or external um sort of as per configuration. Exactly. So what's the bandwidth concerns? I mean obviously working with this volume of data is a massive pain for a lot of people or at least it's uncharted territory. Um I mean I remember even when we have lots of image data on a file system, um moving the images around and batch copying them etc. was [snorts] always a challenge and error prone and bandwidth prone. Um I mean obviously if they store the data inside Lance, like it doesn't change the fact that all that binary data is still sitting somewhere. So are we just beyond the the scenario now where people can copy this data around nodes at all? Like

**[3:13](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=193s)** is it is it actually about physically removing discs and carrying them into a into a different room or a different node? Like what what situation are we in with this this volume of data? Yeah, I mean that that is that is a great question. I I think we are we we've already gone past the bandwidth limit for object store in a in a lot of um places. So this is actually one of the reasons why there's another recent feature we call multi-base, which is you can actually use multiple storage accounts and split your split a single table into multiple buckets. And this is actually one way to get around that bandwidth limit. So you you you know, you can set up your table uh across three or four um blob store or object store accounts and have triple the triple the bandwidth.

**[4:03](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=243s)** Well, so I want to go back just a little bit and kind of talk about some of the key insights that you had that gave birth to Lance to be in the first place and probably like any other good data engineer, you were trying to use parquet for most things and um you know, it's it's a great tool um columnar format like we've sung the praises of it at the council over the years. Um at what point did you realize that it just wasn't going to work for the AI workloads that you were seeing? Yeah, we spent months uh at least I think six months trying to make it work with Spark on on parquet and the workload that we tried that that on was data and large-scale data mining for autonomous vehicles and fiscal AI

**[4:52](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=292s)** today basically has the same problems and it came it boiled down into two big challenges. Number one was random access um for Spark on parquet like the analytical parts of that workload worked great, but we wanted to be able to retrieve and display individual rows with the metadata and we found that we always had to make a copy in a different format uh otherwise it would take, you know, tens of seconds just to fetch you know, 10 to 100 rows and show them. Uh the other one was multimodal data storage, right? The the raw data had to be in individual individual individual files. The random access feature data was in some sort of key value store or just like JSON files and then, you know, parquet was still used for the

**[5:38](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=338s)** analytical data. It was just way too much work trying to keep these three in sync with each other. Like it worked great in demos when you can hide stuff and Martha Stewart things and you didn't have to worry about the data changing in production but we we kind of realized it wasn't going to work uh when it was put into production situations, right? So, um And so and so what what was the moment when you when you decided to build something new? Yeah uh we we definitely didn't do this lightly. Yeah, you know me, I I've been uh involved in in open source projects for a long time. Uh we value community and sort of consensus building a lot, uh but it came down to a couple of things. One, I

**[6:26](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=386s)** interviewed probably over 100 like machine learning and computer vision engineers and researchers. They all voiced the same pain points. They all went through tons of failed experimentation with Parquet. None of them uh found sort of a workable path or a solution. And then I think number two was my my co-founder and I um you know, we're we're both familiar enough with the Parquet internals and we engage with the Parquet community and our conclusion was in order to make Parquet work the way we needed it to work, uh it would require a very fundamental redesign, right? Basically, it would make Parquet no longer Parquet. So, uh that was the that was probably those two were the biggest factors. And I think there were other things that

**[7:13](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=433s)** pushed us over the edge like hey, we needed to to build secondary indexes. Uh we needed also new table format. Um so, all of these things added to the to the burden of uh can we can we, you know, work with Parquet or can we modify Parquet rather than build something from scratch? And so, were you concerned at all about throwing a new a new tool into the uh ecosystem or at the time that you started, um was it not as crowded? Because today it seems like engineers either try and cobble together a mix of tools, like some old, some new. Like they might have a a data lakehouse, or um or they might reach for a vector database, um which is on the newer side. Um they might try and like tie everything

**[8:02](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=482s)** together with a a search API. Like what's the challenge with that? And why why were you sort of bold enough to to think that the world needed a new tool um at the time that you started LanceDB? Yeah, absolutely. So, I think uh the problems we observed was a a couple of big ones. One is that that hodgepodge of tools make things really slow. Uh one of the earliest design partners we worked with was this car company. Um they had similar system like you described. And the them processing their data ended up being slower than real time, right? So, it took more than a day to process a single day's of data that they collected off their cars. Uh so, that's number one. Um number two is

**[8:49](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=529s)** the the infrastructure and maintenance cost of copying data around everywhere, and then maintain it maintaining data sync pipelines between all of these different systems. And the result is you lose a ton of productivity. The The engineers and the researchers, you end up spending most of your time dealing with these low-level uh infrastructure details, it you know, of you know, did I did I partition my data correctly for this system, but then also for that system, and do I have the right piece here and that the right piece there? If I had a bad query result, is it because the the answers weren't there, or because, you know, the two pieces of data were out of sync with each other, right? So, um the another piece of sort of another

**[9:38](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=578s)** example here was there was a physical AI company that we worked with early on. Uh the the the data that we collected um and we did some analysis on their workflow from the point that data came off the device to the time that the model the next generation of the model trained on this new data made it back onto the device it was almost a whole quarter uh going through that life cycle. And which is kind of insane and this is even before uh they were using LLMs to uh with really long uh training runs. Right? So, those were the big problems that we faced and I think the way we thought about it wasn't hey, we want to throw yet another tool on top of this. What we wanted to do was actually simplify things and and remove all of that all of

**[10:26](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=626s)** that hodgepodge of tooling and replace it with a single foundation. And this actually goes back to the previous question you you asked about Parquet. Right? I think um even today there are folks who will defend Parquet and say, "Hey, you actually can make random access have acceptable performance in Parquet by doing a bunch of tricks." Which actually is true. You can make the row groups really small and accomplish this this uh this feat. But then the problem is your scan performance become abysmal and and the whole the whole um scenario here is that AI requires multiple workloads on the same table within the same end-to-end workflow. So, uh we really wanted to to simplify things. And and I think the last consideration we

**[11:14](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=674s)** had here was because of the advent of Apache Arrow and its popularity that made it possible so that uh all of the existing tooling can integrate with Lance uh without us having to build yet, you you another set of pairwise integrations with everyone. Well, let's let's talk about the elephant in the room because that seems to be just the different data access patterns of AI applications. And if you take agents for instance, agents could fire dozens or even hundreds of queries in parallel against the data source, which is completely different from a human executing a search or an analytics query um in an ad hoc fashion. So, um like how does that change the architecture um

**[12:01](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=721s)** and and the demand on these multimodal databases and how have you thought about that? Yeah. Uh this is I think this is probably the biggest reason why I'm super excited this year is just seeing all the different workloads and different requirements that uh our our customers are coming to us with and really the community is demanding. Um I would say there's two two main things here. One is what you're saying is accessing the data is become is now becoming primarily agentic and there's another theme that's coming along which is data pipelines are also being written by agents instead of instead of by humans now and I think they have different effects. I think number one um data access becoming agentic means the throughput is up a lot, performance

**[12:50](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=770s)** requirements have become challenging, and then scale has gone through the roof, right? Um a couple years back when it was just vanilla rag, uh we were hearing requirements from the community and our customers are like, "Hey, we need uh 10 QPS or maybe up to like a 100 QPS uh for a a rag for a database that supports a rag system. Uh and this year, you know, we're looking at tens of thousands or even 100,000 uh queries per second. So, that's a huge, you know, multiple orders of magnitude increases. Performance requirements because agents need to go through many steps these long paths, uh you know, with with vanilla rag with one shot where, you know, 1 second or even a few seconds was

**[13:39](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=819s)** totally acceptable. Now, agentic workflows and pipelines, they really need their retrieval to be fast, like under 100 milliseconds or or, you know, a couple of a couple hundred milliseconds at most. Uh and the last is scale, right? The I remember in 2023, the prevailing wisdom was rag relied on mostly small tables, many many small tables in the hundreds of thousands uh at most a few million vector range. Uh I don't think that has completely uh gone by the wayside now. Uh I think data scale has just exploded by many orders of magnitude, you know, I think this year especially we're regularly having customers, you know, forget production, it's just even like you know, early prototypes uh or early

**[14:27](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=867s)** proofs of concepts where they want to do evaluations at you know, billions of rows and production workloads are in the hundreds of billion rows on a single table. So, uh though that's been a huge trend, I think it over the past 6 months or so, especially uh for agents. And then, I think the second theme is around data pipelines, which, you know, from my previous background working on Pandas and and just being a data scientist, this is super fascinating. Uh I think one um just having the right infrastructure building blocks to separate you know, distributed large-scale execution of the pipelines from the actual logic uh of the user-defined functions, uh

**[15:15](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=915s)** having that separation and having the right building blocks makes it a lot easier for agents. Um the other thing that's really fun to see in practice is agents can now run a lot more experiments in parallel. You know previously you know, we we were limited by okay, I have a bunch of different feature feature ideas and I'm going to you know, manually code up each one and try them out. And right now now you can just say hey, I've got these ideas like you know, an agent like cloud code or codex like go try out a hundred different variants on all of my on each idea and do ablation studies and and and and do and sort of do all of this branching and and merging at the end. So, um, you know, making these experiments and these data sets reproducible and

**[16:04](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=964s)** manageable I think it's also going to be a big theme for agentic data pipelines. Well, I like that you mentioned the pandas creation because obviously as the the co-author of pandas you've been building data tools for a long time. So, um, I'm just wondering like does it feel weird to be reintroducing a new set of tools on top of tools that you already built and that were really used by a previous generation of of data engineers and data scientists. Just wondering like how's how that feels to be changed sort of in this case. Yeah, oh, it feels really exciting. I I've seen I think even before uh, agents and all of that you know, I've been closely involved in

**[16:55](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=1015s)** with like the polaris project. Um, and it's great to see you know, a new generate like new generation of technology kind of making making things that were making things possible that were just not possible or really slow or prohibitively expensive before. So, um, I I I I definitely feel a lot of attachment for the the Pandas community, but this feels more I guess this feels more exciting than than strange to me. That's great. I mean, that's where that's exactly where we want to be and um I'm excited to hear your talk on Lance at the AI Council. It'll be great to have you back. Thank you. >> I just wanted to ask you just wanted to ask you a final question. Um I've heard you mention that this is a couple years

**[17:44](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=1064s)** ago, you mentioned that by 2025 um perhaps as much as 90% of all data generated would be video. And so I'm wondering now that we're on the other side of that, how have you seen that materialize and um how worried should engineering teams be about needing to deal with all these these heavy data sets that maybe their their text pipelines and um and text databases um you know, that they're just scale that they never had to deal with before. So um how concerned should they be? >> Yeah, absolutely. I I think the latest stat is something like the the the world generates about .4 or something like 400 million terabytes of multimodal data per day now. Uh which I think it's like .4 zettabytes.

**[18:31](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=1111s)** And uh the the projection is in 3 to 5 years that's going to be 1 zettabyte per per day of multimodal data. So um I I fully expect that to become like a bigger bigger portion of uh the the time and effort for data engineering teams. And I think even before it the data volume was was already very large. And I think the big difference now is just how much more value we can get out of our multimodal data because of AI. And so because of the increase in value it's actually worth it to invest a lot more in managing that data and invest in the infrastructure to to process it. Uh

**[19:19](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=1159s)** and so that is the That is what makes me feel like multimodal data processing is going to be uh uh the become the majority of uh data engineering teams time and effort, right? So, maybe 3 to 5 years down the road, uh we won't even think about this extra term multimodal data processing. We'll just think about data engineering, and it'll just be multimodal by default. So, Cheng, tell me, what are you most excited about looking forward to at AI Summit this year? Well, I've been going to Data Council for for a long time, and and now I'm excited to see um uh it become AI Council as well. And I think I've always had the best conversations at Data

**[20:08](https://www.youtube.com/watch?v=FaX4fpEdOlw&t=1208s)** Council and uh in the past uh with folks from, you know, all different teams and all all different um uh types of uh of companies uh working on different parts of the data stack. And I think that's the thing I always look forward to the most is meeting people building the most innovative things in data and AI, uh and just having really great conversations. Great, Cheng. Well, thanks for chatting with me. Thank you for having me, Ali.
