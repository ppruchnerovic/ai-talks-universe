---
id: slZ1xg2UznQ
title: "Chang She on Why He Walked Away from Parquet to Build LanceDB"
slug: chang-she-on-why-he-walked-away-from-parquet-to-build
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 7
published_at: 2026-04-21T14:40:25Z
video_id: slZ1xg2UznQ
youtube_url: https://www.youtube.com/watch?v=slZ1xg2UznQ
tags: ["machine learning", "computer vision", "AI"]
transcript: true
---

# Chang She on Why He Walked Away from Parquet to Build LanceDB

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `7 min`

`#machine learning` `#computer vision` `#AI`

[Watch the recording](https://www.youtube.com/watch?v=slZ1xg2UznQ) · [Conference site](https://www.aicouncil.com/)

## Description

Chang She, co-founder and CEO of LanceDB, sits down with Pete Soderling ahead of AI Council SF 2026 to explain why Parquet — the columnar format that's powered data engineering for the last decade — couldn't handle the AI workloads his team was building.

After six months of trying to make Spark on Parquet work for large-scale autonomous vehicle data mining, Chang and his team hit two walls: random access performance (it took tens of seconds to fetch just 10-100 rows) and multimodal data storage (keeping raw data, feature data, and analytical data in sync across three systems was unsustainable in production).

In this clip, Chang shares:

- The two challenges that broke Parquet for AI workloads
- Why "physical AI today basically has the same problems"
- What he learned from interviewing 100+ ML and computer vision engineers
- Why modifying Parquet would have meant making it "no longer Parquet"
- The architectural decisions that led to building LanceDB from scratch

Catch Chang and the rest of the speaker lineup at AI Council SF, May 12–14, 2026 in SOMA: https://aicouncil.com/sf-2026

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:

## Transcript

*1,241 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=0s)** So, I want to go back and talk about some of the key insights that you had that gave birth to Lance to be in the first place. And probably like any other good data engineer, you were trying to use parquet for most things. And you know, it's it's a great tool. Columnar format, like we've sung the praises of it at the AI Council over the years. At what point did you realize that it just wasn't going to work for the AI workloads that you were seeing? Yeah, we spent months, at least I think 6 months trying to make it work with Spark on on parquet. And the workload that we tried out out on was data large-scale data mining for autonomous vehicles. And physical AI today basically has the same problems.

**[0:48](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=48s)** And it came it boiled down into two big challenges. Number one was random access for Spark on parquet. Like the analytical parts of that workload worked great, but we wanted to be able to retrieve and display individual rows with the metadata. And we found that we always had to make a copy in a different format. Otherwise, it would take, you know, tens of seconds just to fetch, you know, 10 100 rows and show them. The other one was multimodal data storage, right? The the raw data had to be in individual files. The random access feature data was in some sort of key-value store or just like JSON files. And then, you know, parquet was still used for the analytical data. It was just way too much work trying to keep these three in

**[1:36](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=96s)** sync with each other. Like it worked great in demos when you can hide stuff and Martha Stewart things, and you didn't have to worry about the data changing in production. But we kind of realized it wasn't going to work when it was put into production situations, right? So, um And so, and so, what what was the moment when you when you decided to build something new? Yeah. Uh we we definitely didn't do this lightly. Yeah, I mean, you know me. I I've been involved in in open-source projects for a long time. Uh we value community and sort of consensus building a lot. Uh but it came down to a couple of things. One, I interviewed probably over 100 like machine learning computer vision

**[2:22](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=142s)** engineers and researchers. They all voiced the same pain points. They all went through tons of failed experimentation with Parquet. None of them uh found sort of a workable path or solution. And then, I think number two was my my co-founder and I, um you know, we're we're both familiar enough with the Parquet internals and we engage with the Parquet community and our conclusion was in order to make Parquet work the way we needed it to work, uh it would require a very fundamental redesign. Right? Basically, it would make Parquet no longer Parquet. So, uh that was the that was probably those two were the biggest factors. And And I think there were other things that pushed us over the edge, like, hey, we needed to to build secondary indexes.

**[3:11](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=191s)** Uh we needed also a new table format. Um so, all of these things added to the to the burden of uh can we can we, you know, work with Parquet or can we modify Parquet rather than build something from scratch? And so, were you concerned at all about throwing a new a new tool into the AI ecosystem? Or at the time that you started, um was it not as crowded? Because today it seems like engineers either try and cobble together a mix of tools, like some old, some new. Like, they might have a a data lakehouse or um or they might reach for a vector database, um which is on the newer side. Um they might try and like tie everything together with a search API. Um, like what like what's the challenge

**[4:00](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=240s)** with that and um, why why were you sort of bold enough to to think that the world needed a new tool um, at the time that you started LanceDB? Yeah, absolutely. So, I think the problems we observed was a couple of big ones. One is that that hodgepodge of tools make things really slow. One of the earliest design partners we worked with was this car company. They had similar system like you described and the them processing their data ended up being slower than real time, right? So, it took more than a day to process a single day's of data that they collected off their cars. Uh, so that's number one. Number two is the the infrastructure and maintenance cost of copying data

**[4:48](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=288s)** around everywhere and the maintain maintaining data sync pipelines between all of these different systems and the result is you lose a lot of productivity. The the engineers and the researchers, you end up spending most of your time dealing with these low-level infrastructure details you know, of you know, did I did I partition my data correctly for this system but then also for that system and do I have the right piece here and that the right piece there? If I had a bad query result, is it because the the answers weren't there or because you know, the two pieces of data were out of sync with each other, right? So, um, the another piece of sort of another example here was there was a physical AI company that we worked with early on.

**[5:38](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=338s)** The data that we collected um, and we did some analysis on their workflow from the point that data came off the device to the time that the model the next generation of the model trained on this new data made it back onto the device, it was almost a whole quarter uh going through that life cycle. And which is kind of insane. And this is even before uh they were using LLMs to with really long training runs. Right? So, those were the big problems that we face. And I think the way we thought about it wasn't, "Hey, we want to throw yet another tool on top of this." What we wanted to do was actually simplify things and and remove all of that all of that hotchpotch of tooling and replace it with a single foundation. And this actually goes back to the

**[6:25](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=385s)** previous question you asked about Parquet. All right. I think um even today there are folks who will defend Parquet and say, "Hey, you actually can make random access have acceptable performance in Parquet by doing a bunch of tricks." Which actually is true. You can make the row groups really small and accomplish this this uh this feat. But then the problem is your scan performance become abysmal. And and the whole the whole um scenario here is that AI requires multiple workloads on the same table within the same end-to-end workflow. So, uh we really wanted to to simplify things. And and I think the last consideration we had here was because of the advent of a Apache Arrow and its popularity,

**[7:14](https://www.youtube.com/watch?v=slZ1xg2UznQ&t=434s)** that made it possible so that uh all of the existing tooling can integrate with Lance uh without us having to build yet, you know, another set of pairwise integrations with everyone.
