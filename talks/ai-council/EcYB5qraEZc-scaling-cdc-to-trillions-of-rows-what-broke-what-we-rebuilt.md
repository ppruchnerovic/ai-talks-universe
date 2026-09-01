---
id: EcYB5qraEZc
title: "Scaling CDC to Trillions of Rows: What Broke, What We Rebuilt, and What AI Demands Next | Artie"
slug: scaling-cdc-to-trillions-of-rows-what-broke-what-we-rebuilt
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "AI engineering & agents"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: "AI Council"
duration_min: 19
published_at: 2026-06-16T18:45:10Z
video_id: EcYB5qraEZc
url: https://www.youtube.com/watch?v=EcYB5qraEZc
youtube_url: https://www.youtube.com/watch?v=EcYB5qraEZc
tags: ["machine learning", "computer vision", "AI"]
transcript: true
---

# Scaling CDC to Trillions of Rows: What Broke, What We Rebuilt, and What AI Demands Next | Artie

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `19 min`

`#machine learning` `#computer vision` `#AI`

[Watch the recording](https://www.youtube.com/watch?v=EcYB5qraEZc) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 1 - DATA ENG & DATABASES] Most CDC pipelines work fine when you're building an MVP. Ours did too - until they didn't. Artie is a real-time data replication platform that processes 20-30 billion events per day across thousands of pipelines with sub-minute latency on 90% of them. Three years ago we were running a forked version of Debezium with Kafka processing millions of rows. Along the way, many assumptions we started with broke.

This talk is a post-mortem of what failed, what we rebuilt, and the decisions that matter at scale:

• Why we replaced Debezium - single-threaded capture, limited extensibility, and no built-in recovery forced us to build a proprietary Reader from scratch to increase fault tolerance
• Parallel backfills without data loss - running historical loads alongside live CDC using primary-key range chunking and exactly-once merge semantics, following Netflix's DBLog pattern
• Fan-in from thousands of single-tenant databases - consolidating sharded or single-tenant sources into unified destination schemas without bespoke ETL per tenant
• Edge cases at scale - five-digit-year timestamps, negative years, non-JSON in JSONB, non-UTF8 encodings, and why we chose to fail hard rather than silently skip data (and the recovery mechanisms that make that practical in production)
• Schema evolution - automatic column adds, type changes, drops, and notifications so teams know what changed

Finally: AI workloads have the same freshness problem databases have always had, but the sources are no longer just databases - they are filesystems, object stores, git repos, and documents. We will share how Artie is extending its core primitives beyond databases to become the sync layer for any data AI systems depend on.

Viewers will leave with concrete architectural patterns for building CDC systems that survive at scale, a checklist of failure modes, and a framework for thinking about real-time data as AI infrastructure.

SPEAKER:
Robin Tang - Co-founder & CTO, Artie

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,881 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=EcYB5qraEZc&t=0s)** My name is Robin. I'm actually, it's funny fact, I was actually in the same batch as uh in YC S23. And today I'm going to give a I'm going to start sharing my learnings around how we started to scale CDC systems in production. I wanted to go over what we tried, what broke, what we ultimately had to rebuild, and then talk about the next wave of architectural patterns to power the next AI workload. So, before I get started, uh I'm the co-founder of Ardi. We're focused on providing real-time CDC to help companies power event-driven workloads like database replication. And prior to that, I spent most of my career working across infrastructure and platform at companies like OpenDoor and Zendesk. At Zendesk, I was involved in working on Maxwell, which is the open-source

**[0:48](https://www.youtube.com/watch?v=EcYB5qraEZc&t=48s)** alternative to Debezium. And for today's talk, I wanted to focus the story around Sam, who I'm sure a lot of you could relate to. And Sam, he's a senior data engineer at Yesterday Inc., who's a Series B fintech. His whole sole responsibility is to make his data warehouse mirror production. And the CEO here, they only have one requirement. The data should be as real-time as possible. So, let's follow Sam's quest towards real-time data. First, like most people, he will take we start with daily snapshots. The first thing that he's trying to do is take a daily snapshot of his database. He didn't want to impact the database performance during the day, so he decided to do this at night.

**[1:37](https://www.youtube.com/watch?v=EcYB5qraEZc&t=97s)** And this works. So, he decided to run this more frequently. The problem though is that the data is almost immediately stale as soon as the job completes. And that's because the database is serving live traffic. So, he decided to pack up his learnings and tried to implement what we like to call poor man's CDC, which is incremental batching. And poor man's CDC is effectively running a select star on the table against a deterministic updated column and trying to find the changes that have happened in between runs. The problem though is there are subtle subtle problems with this approach. The first one, of course, you miss deletes entirely. And I guess that's fine. I mean, yesterday Inc doesn't really do hard deletes, they only do soft deletes. And this is intra real changes.

**[2:24](https://www.youtube.com/watch?v=EcYB5qraEZc&t=144s)** The problem is the old approach didn't capture that, so I guess that's fine, too. It then required an updated column for every single table. Well, onboard the tables that don't have an updated would not have an updated column first and start there. And this is usually where most companies with small workloads stop. But as soon as your business requirements change, your data volume increases, the updated column is actually not being updated by the database, it's actually being updated by your application code, which doesn't doesn't get updated sometimes due to the fact that you don't trigger your side effects or database database migrations do not capture it. This is where incremental batch starts to break down. And as your volume also starts to scale, the batch just takes longer and longer.

**[3:14](https://www.youtube.com/watch?v=EcYB5qraEZc&t=194s)** So, we finally arrive at CDC. CDC is change data capture, which is the ability to decipher what has changed by reading the database transaction logs. And he very quickly realized what the state of the art looks like today. We have Debezium, which is reading from the Postgres is right ahead log and forwards them off to Kafka. And then we're using a Snowflake sink connector or any destination sink connector, really, to be able to read those messages and dump them directly into the destination. It achieves everything that he's able to uh that he wanted initially. There's no more polling. Changes quickly happen as soon as they arrive in the database, they're immediately seen in the destination. And deletes are captured.

**[4:04](https://www.youtube.com/watch?v=EcYB5qraEZc&t=244s)** Again, it's open source. All of this component All of these components are open source and you can easily run them. So, how hard could it be to actually run this pipeline? He was able to get a POC running in under 2 weeks and he decided that he wanted to run this in production. Oh. Oh. Oh cool. After a week, everything seems to be working fine. I mean, the data is still snapshotting, so he hasn't been able to check the data in production yet. But then he very quickly realized that the default backfill strategy for most most open source tooling opens up a read transaction while the data is backfilling, while the tables are backfilling. And as such, changes are just accumulating and not being drained. As a result of this, the database disk

**[4:52](https://www.youtube.com/watch?v=EcYB5qraEZc&t=292s)** is almost full. And right after he added more disk space, he realized that his Kafka cluster went down because the storage is also full. Well, why did this happen? When he was calculating the storage to provision, he only accounted for the ongoing changes in CDC. He did not factor in the fact that all backfill data also goes through Kafka and the fact that compression isn't turned on by default. Finally, once he fixed all of these issues, he finally had time to look at the data inside of his destination and he very quickly realized there's a lot of silent missing data. The problem is though, the pipeline is running, changes are still landing, but the specific change that he was looking for didn't exist. And after a thorough investigation, it

**[5:44](https://www.youtube.com/watch?v=EcYB5qraEZc&t=344s)** turns out that the reason why this was missing was because this column got toasted. What's even a toast? It's not this. A toast column is a column value where the column value exceeds the default Postgres page size, which is around 8 kilobytes. And if that value doesn't get changed, it gets omitted in the CDC stream. And as a result, you actually need to handle that downstream. And let's go over some of the practical errors that choke most pipelines. Some of the weird things that databases allow you to do goes beyond me, like the fact that a scale for the first one could be a negative number. What does that even mean? It actually, in this case, it means that

**[6:31](https://www.youtube.com/watch?v=EcYB5qraEZc&t=391s)** the number is rounded to the nearest uh to the power 10 to the power of two. Um Another one is how could a year exceed the YYYYMMDD format that most encoding algorithms use? The other thing is, most of these tools, they give you system-level stats, but don't actually give you the data processing errors or the data processing telemetry that you're actually looking for. So, effectively, we're just flying butt blind with a mission-critical pipeline. The next one that's also a bit of a nuance that is there is throughput mismatch. Publishing to Kafka is extremely fast, but the Snowflake merge is not. And I'm sure a lot of you already know, OLAP merges are deeply inefficient because it

**[7:20](https://www.youtube.com/watch?v=EcYB5qraEZc&t=440s)** does a lot of table scanning. By the end of the quarter, Sam is tired. He's tired of firefighting. And looking back here, did Sam miss the mark? I mean, the tools are theoretically correct, so what went wrong? The problem is, in practice none of these tools are actually built to work together. It's very much bolted on and as such is filled with edge cases. This was a similar setup to what I've done in the past at most at the companies that worked at. And that already we decided that we wanted to make a better alternative and stop forcing a square peg into a into a round hole.

**[8:09](https://www.youtube.com/watch?v=EcYB5qraEZc&t=489s)** As such we rebuilt everything from scratch. This is what the architecture looked like. It remained the same. We added additional consumer. However, we just completely rebuilt out the components entirely. First, let's go over some of the issues that we had when we were running DBZ at at scale. As time was running into backfilling tables or triggering any sort of ad hoc backfills for select tables is extremely difficult and difficult to coordinate. Companies with single tenant designs would have partition tables inside of their source that want that data to be fanned into the destination. Well, you could do that, but you have to write custom SMTs, single message transforms, which are incredibly fragile and brittle to maintain.

**[8:58](https://www.youtube.com/watch?v=EcYB5qraEZc&t=538s)** The other limitations that we ran into were that columns are a global object and as such you cannot have tables some tables that have inclusion and some tables that have exclusion. This is a mutually exclusive uh requirement at the pipeline level. The next one is I don't know how many times that we had issues where DBZ just stood still because of a network error or a Kafka producer error. And it happened so often that we actually had a data dog monitor that would page our on-call engineer to push the restart button. On top of all of this, the operational surface area was just so large that to run this realistically at scale it was just near impossible. We applied the lava learn learnings from Debezium and we implemented the our into our reader from scratch.

**[9:47](https://www.youtube.com/watch?v=EcYB5qraEZc&t=587s)** I'll talk a little bit more about the backfill in the next slide. The first thing is fan-in and fan-out are automatically built into reader as a first-class citizen. It's a config option and not an MTC. The next one is failures are not silent. They will propagate up the call stack and crash the pod. And what the fact that we're able to just use tools like Kubernetes, we're able to leverage auto scheduler Sorry, auto scheduler to be able to retry the process and handle monitoring. With this type of setup, we're able to process billions of changes on a daily level with minimal on-call overhead. We spent years building and improving upon our backfill online backfill strategy with the goal of making it more performant and easier to run. The first thing that we did to make this

**[10:36](https://www.youtube.com/watch?v=EcYB5qraEZc&t=636s)** better was we have separate processes for backfilling and consuming changes from your source database. Instead of the backfill data also going through Kafka, it we directly read the data and append that data into the destination. As soon as this is done, we issue a one-time dedupe and we eliminate any expensive merges that happen. >> [snorts] >> As quickly as the tables are finishing backfilling, we're able to then turn on the Kafka consumer to start draining from the Kafka topic. Parallelism here is defined at the table level, not at the pipeline level. As a result, the source database and Kafka are no longer being overloaded and we're able to differentiate between backfill data and CDC changes at the consumer level and as such

**[11:23](https://www.youtube.com/watch?v=EcYB5qraEZc&t=683s)** backfills are able to finish quicker because we're able to use the right database operations. We then started to focus on building out the consumer. Before engineering teams that use some sort of like a Kafka sync connector, they would need to write a custom logic per table to handle things like unfurling a row from a key value table that was dropped by the sync connector. They would need to handle schema evolution and they would need to deal with data merges. And now with our with our consumer, we're able to automate workflows with transactional guarantees built in. We're able to achieve transactional guarantees by making a process item potent and use atomic operations from SQL.

**[12:10](https://www.youtube.com/watch?v=EcYB5qraEZc&t=730s)** And only when this operation actually succeeds, do we do we commit the offset into Kafka. And on top of this, the right throughput is fully managed without having to tune any sort of flush rules as a as the as the fact that like this was just built in and we're able to customize this. Oh. Wait. Cool. The last thing is we've built in schema evolution. Everyone talks about how they have schema evolution built out and I figure instead of us talking about how we handled it, we walk through our philosophy. The first thing is we wanted to minimize the amount of escalation to an operator

**[12:57](https://www.youtube.com/watch?v=EcYB5qraEZc&t=777s)** which will directly increase maintenance burden. The second, we wanted our consumers to be in the driver's seat and have pipelines adjust to the actions that the customers are taking. And the third one is we will not compromise on precision loss. An example of this would be converting a float into an int. If we did that, we would lose the decimal places. In the >> [clears throat] >> In this case, instead of doing that, we would then hard fail and we would escalate the error to the customer to let them know to let them figure out what they want to do. If they were to change this column to a float, everything would flow through fine. If they converted this to a string, we would we would be fine to let that data flow through. And in the float to int example as for

**[13:45](https://www.youtube.com/watch?v=EcYB5qraEZc&t=825s)** instance, if we were to flip the other way around and go into float, that's fine. Our inference library will automatically handle that conversion for us as we would just be appending decimal places. And on top of that, our consumer is able to produce SCD type 4, slowly changing dimension tables type 4. With every single table, we're able to produce two sets that we replicate we're able to produce two sets of tables for our consumers. The first one is a stable table that mirrors production. This data is landed with merge on right. The second one is an auto lock table that captures every single data change along with its database transaction timestamp. So, how did it hold up?

**[14:34](https://www.youtube.com/watch?v=EcYB5qraEZc&t=874s)** Well, this guy thinks we're really fast. Our customers forgot we existed. And ultimately, >> [snorts] >> Sam is happy. The replication slot is stable. The data is super fresh. And Sam, he's still employed. And out of nowhere, an AI agent has appeared. Now, the agent is trying to read the data from Snowflake. However, it very quickly realized that the every table and view in Snowflake is way too laggy. And while this lag would have been tolerable for us, agents only create one table at a time.

**[15:22](https://www.youtube.com/watch?v=EcYB5qraEZc&t=922s)** They spun sub agents and fan out. And now the bottleneck of analysis has been completely eliminated by by AI such that the bottleneck has been actually moved to the different parts of the workflow such as into the data ingestion layer and the transformation layer. And here's what we know. First, the consumers of data are changing. And soon, very soon, most systems that previously thought that Egress was fast will soon think that this is an outage. And we believe in the not-too-distant future, even reading will start to feel insufficient. Agents should and need to be able to react to changes.

**[16:12](https://www.youtube.com/watch?v=EcYB5qraEZc&t=972s)** So, where does it What Where does the data need to go? Does the data still go to Snowflake? Does it still go to Databricks? Or does it go somewhere else entirely? This is what we're thinking about the next chapter of Arity. We believe agents need to access data across different layers of the business. And as such, we should not be the vendor that controls where your data goes. Instead, we have a CDC stream that's already running everything through Kafka. So, we're opening it up to our customers and equipping them with an event-driven architecture that's backed by a CDC event bus. We're working with our customers now to plug in their own consumers, run in-flight transformations, fan this out to whatever destination makes sense for your workload such as Elasticsearch or any sort of vector stores. And for us,

**[17:00](https://www.youtube.com/watch?v=EcYB5qraEZc&t=1020s)** we're focusing on abstracting the low-level plumbing and providing a real-time and reliable CDC platform that can power any sort of workload. And this is just a sneak peek at what we're building next at Arity. The first thing that we're doing is we're launching a our self-serve product on June 8th. And then after that, we're working on streamlining all the access towards our product. Next, we're working on giving providing a fast events API that can support both track and identify payloads with a 100 ms latency to any destination. We're then going to be focusing on exposing Kafka to our customers that are on BYOC. And a bit further out, we're working on the file system sync. And I'm sure you have already seen this as your company

**[17:49](https://www.youtube.com/watch?v=EcYB5qraEZc&t=1069s)** as your company or your teams are building on top of cloud with cursor, your GitHub repo is changing and that as we saw from the previous graph, it's changing at an unprecedented pace compared to the past. And Git effectively is the CDC for a file system and as such, we should treat it as a first-class citizen. Just the same way how we treat a real change today. If a skill were to be updated or shared cache, it should automatically be able to trigger additional workflows and workloads. Well, thank you and this is >> [music] [music]
