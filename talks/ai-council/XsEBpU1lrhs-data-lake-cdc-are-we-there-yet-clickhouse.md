---
id: XsEBpU1lrhs
title: "Data Lake CDC: Are we there yet? | ClickHouse"
slug: data-lake-cdc-are-we-there-yet-clickhouse
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 16
published_at: 2026-06-18T22:16:13Z
video_id: XsEBpU1lrhs
url: https://www.youtube.com/watch?v=XsEBpU1lrhs
youtube_url: https://www.youtube.com/watch?v=XsEBpU1lrhs
tags: ["AI"]
topics: ["Data engineering & MLOps"]
transcript: true
---

# Data Lake CDC: Are we there yet? | ClickHouse

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `16 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=XsEBpU1lrhs) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] The idea of incremental reads from data lakes has been cooking for years, but few are serving it up. As a user, you must wrangle change feeds, snapshots, time travel, that one corrupted manifest file. Do you need to be a "Big Data Engineer" to get it right? In this lightning talk, we’ll explore what’s broken, what's just hard, and why making data lake CDC accessible is a problem worth solving.

SPEAKER:
Marta Paes - Senior Product Manager, ClickHouse

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,585 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=0s)** Yeah, so I'm Martha. I work at ClickHouse as a technical PM for ClickPipes, which is our managed ingestion platform. And at this point, I spent half of my career moving data around as an engineer and another half building tools for engineers to move data around like ClickPipes, which is what I work on now. And so I I use this um this talk or I submitted this talk as a bit of like a forcing function to kind of like look into something that is not an entirely new problem in moving data around, but something that is a new problem to me in this space. And so and that is moving data out of data lake and into an analytical store like ClickHouse so that you can run analytics on it faster.

**[0:48](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=48s)** And this might be counterintuitive cuz a lot of times, you know, when people talk about data lake ingestion, it's more about ingesting data into a data lake or kind of like querying a data lake remotely, not really getting data out of a data lake into some other system. Uh but this is what we're talking about today. And the idea is that you don't uh you manage to incrementally ship data to like some some analytical store and because you're only shipping a diff you're doing like change data capture and then like you're processing less data and you can more performantly do things like data-driven applications or real-time analytics on top of data that is stored in your probably massive data lake.

**[1:36](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=96s)** So the first time I heard about the concept of doing CDC out of a data lake, I was pretty confused. So this was like my original idea of what a data lake is. It's not it's built for scale, not really for speed. Um and it's where you keep kind of like your cold data for you know, historical analysis, where you make data available to everyone in your company to enjoy at their own leisure. And if you want to build things like data-driven products or do real-time analytics on top of like this massive uh data store. My my brain defaults to, you know, why wouldn't you just go directly to your data source and just ingest that into an analytical store or increase the frequency of your batch pipelines,

**[2:24](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=144s)** stitch together some streaming architecture um that can do things in real time. Or really just use the capabilities that most analytical databases have today, like ClickHouse or, you know, Snowflake, BigQuery. Everyone can read um efficiently and remotely from a data lake, so why wouldn't you just do that? And all of these options sound cheaper and simpler than getting data out of your data lake into somewhere else. So, why would you put the data lake in the middle at all, right? Um and I never built I used databases in production um but I never built a data lake in production. So, this wasn't uh this wasn't really clicking for me. So, but then I talked to a lot of our customers

**[3:12](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=192s)** and it started making sense because there are at least this is the common four patterns that I see when I talk to customers that tell me that they need this um and that kind of like slowly convinced me that this is a real problem that my team should solve. Um and where, you know, really doing CDC out of your data lake is kind of like the only viable path or like this is really what what they need. So, first, these are customers that standardize on a lake-first architecture. You know, all the raw data that comes in through any source in their company lands in a data lake by default. And so, this is their source of truth. This is their Postgres or like their equivalent to you know, this is where all our data is stored. This is uh where people should consume data

**[4:00](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=240s)** from. And every downstream stream system in the company consumes data from that central repository. And somehow relatedly, um a lot of times the data lake is the contract between um teams. So, uh the cons the the team that is producing data wants to have full control over what you're able to consume in what shape you can consume it um and how the this data is governed. And then as a consuming team, you never have um access to the actual source of the data in the raw um in the raw form of the data. And so, the data lake becomes the interface between the different teams in your in your company. Uh third use case is multi-cloud, which is uh becoming more and more common. Um and the data lake is kind of like the

**[4:49](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=289s)** interop interop uh layer uh between your operational and your analytical systems, which might and sometimes often live in different clouds. And you know, it's expensive to fully replicate uh things cross-cloud, cross-region. And so, just doing incremental syncs uh from a lake into wherever you need uh your data is kind of like the easy and cheap option. And lastly, there's also like um the cases where batch just isn't fast enough. And um you just need to reduce the amount of data that uh you have to analyze so that you can run queries faster. And so, this is kind of like the classic also how you see like OLTP CDC where like you want to

**[5:38](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=338s)** consume data or changes as they come in. You don't want to go to Postgres all the time and like run queries on all the data and kind of like do the push down and do all of that every time you need to run analytics. Um and in all cases the ask from customers is the same. So, you get the changes out of the lake, you ship them to a system, um to an analytical database, and then you're able to run sub-second queries on top of that. And so, the use cases are definitely real. Some of the customers are some of our customers are uh enrolling their own scripts uh for for doing this um this different today. And so, how how do we actually build something um that makes it easy and accessible for any customer to consume this change feed from uh data lake

**[6:26](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=386s)** format? And you know, how do how do you even Are there even What are What even are the primitives um to do this this capture like I didn't know that, and that's why uh this talk exists cuz now I do. Uh and so, I'm going to focus on Delta Lake and Iceberg because these are, you know, the most commonly used formats. Uh there's of course like Hoodie who actually which actually has like really good primitives for this way earlier than um Iceberg and and Delta. So, both formats um expose change information. Obviously, they both do it in completely different ways. Uh so, Delta pre-computes uh the changes, writes them to a separate folder. So, like as a consumer of these changes, you just read metadata. That's

**[7:14](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=434s)** all you do. And Iceberg takes a different completely different approach. So, there are no separate data files. Uh the change metadata lives in the actual data uh in the actual rows as like metadata columns. And so, changes in Delta are easier to consume, and in Iceberg they're just cheaper to store. So, there's trade-offs to both. Uh I Yeah, it's uh thinking about like building either is not fun, but Delta is definitely like uh feels a little less uh intimidating at least uh to start with. So, this is kind of like how it looks like if you uh put it as like a sequel thing. So, with Delta, you really just

**[8:01](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=481s)** enable a property on a on a table, and then on the consumer side, um you just use uh a function that they provide, and you kind of like get the rows back um for the in between the versions that you specified. Of course, as a consumer, the tricky part is also, and this is what you don't want users to have to orchestrate, is, you know, what what versions have you already consumed? Like, if something fails, how do you resume to the version uh that wasn't um that you haven't ingested yet. So, but the TLDR for Delta is that you never have to touch uh the data files to find out what has changed. And that's why I like the idea of building a Delta Lake CDC connector first because it's somewhat straightforward, even though you have to do all this orchestration

**[8:49](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=529s)** that uh we already do in Clay Pipes anyways. And on the Iceberg side, uh like I said before, it takes a different approach. So, like you it's not a purely uh metadata kind of like look up. You have to like filter forward from, you know, a checkpoint. You have a sequence sequence number associated with a row. And um in like the one in in V3 for Iceberg is kind of like when it became a little more doable um to think about building something for for Iceberg. I think for Iceberg in particular, like I don't think customers are even um able to do this manually today cuz it's way more complicated and way heavier. And so, the change information is embedded in the rows, not um materialized separately like uh, in

**[9:38](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=578s)** Delta. And I think one thing that is interesting uh, about Iceberg uh, in particular is that the spec has been uh, changing a lot to come accommodate um, kind of like um, the change in in workloads um, that now are using Iceberg. If you see that like Iceberg was originally made for immutable uh, batch data, but um, it's now used a lot for you know, very high throughput inserts, mutable data like CDC uh, and so making CDC easier on Iceberg has been like a big topic for um, for the new for the new versions. And like I mentioned like with V3 already feels possible to build something. Uh, it's not like going to be a walk in the park, but you know, the

**[10:25](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=625s)** primitives are there and it's you can do something with it. Um, but there's a lot of interesting discussions already going on for uh, Iceberg before and the most promising proposal for CDC is uh, this new idea of having a root manifest. So instead of like walking in V3 what I have to do is you have to walk uh, the tree of like all of the manifest metadata that you have to kind of find what changed. And with a root uh, manifest what you'll be able to do is just kind of uh, diff between two pointers. And so pulling gets much much cheaper um, because you don't have to traverse like the whole metadata uh, tree. And yeah, like I said for us in particular we're going to start with

**[11:12](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=672s)** Delta just because the primitives are uh, much simpler to reason about and cheaper to reason about too. But um, yeah, so what's what's missing? This is you know, I'm not I'm definitely not an expert in uh, data lake formats, but I have been building uh, OLTP CDC for um, some years now. And so, my brain, when I was like putting this talk together, my brain went back to, you know, from what we learned from doing CDC out of Postgres, MySQL, MongoDB, um, what what isn't there yet for data lake CDC? And so, for the first thing that is very obvious, um, that doesn't exist today is global ordering. So, like the primitives that uh, I talked about

**[12:01](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=721s)** before are all at the table level. So, there's no way to track changes across multiple tables. And if you think of something like rows that are changing, uh, across tables like in a in a single in a single transaction, today you don't have a way to know, uh, that the changes to multiple different tables are related in any way. So, they're not on the same timeline, there's no ordering, you don't know, uh, you can't really relate, uh, what is changing. And the second thing is durable, uh, retention. So, a guarantee that if something fails, you can resume from where you left off. Of course, that's like partly on the consumer to figure out, um, but the tricky thing is that, uh, on the producer side, they have to guarantee that the change metadata is still there waiting for you. So, if you

**[12:49](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=769s)** think about, uh, MySQL CDC, for example, it's very common where, um, a customer has like a very short binlog retention interval. And so, like if something fails for longer than the retention interval, when you want to restart, uh, ingestion, the binlog is no longer there. And so, you need to do like a full a full resync. And the third thing is just having a standard consumption interface. This is where, you know, uh, products like ClickPipes can help or like Debezium where, um, users don't have to build them and roll this out themselves. Um we build the abstraction and then regardless of, you know, if you're using Delta or if you're using Iceberg, uh you have the

**[13:36](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=816s)** same interface and we don't bleed the implementation details. Like you should not know the slides that I showed before. Like you don't you shouldn't even need to know how change tracking works for data lake formats. You should just see the data you want in your database. And yeah, so the three gaps that I described, uh ordering, retention, and having a standard interface, I think map almost exactly, or at least in my head, uh where I see these things being solved is at the catalog level. Uh I haven't seen a lot of discussions around this, but this is at least like my takeaway from uh what I learned about change tracking in uh data lakes is that, you know, this global ordering and like these things that are kind of like overarching to all the objects in your

**[14:25](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=865s)** data lake probably live at the catalog layer. So, um are we there yet? Not really. Uh but uh we're we're definitely more than halfway there. Um you know, this time around looking into it scared me less than the last time I looked into it some months ago. And so the primitives are there. Um the spec is evolving. Uh you have very smart people invested in making this work. And the consumer layer is the thing that um is going to kind of like make this widely usable cuz not a lot of people are uh doing incremental syncs from data lakes to their uh analytic stores today, and a big part of that is just because of the effort it requires from you as a

**[15:12](https://www.youtube.com/watch?v=XsEBpU1lrhs&t=912s)** user to build all the orchestration, to build all the scripts, to uh make sure everything works uh when something fails. And that's what we're building um at ClickHouse. And you know, if that sounds like something you'd like to work on, we have a bunch of roles open in my team. So, that's it. Thank you so much. >> [applause] [music]
