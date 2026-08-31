---
id: NqJIyP9rIW8
title: "Inside Lakebase: fully-managed serverless Postgres – Nikita Shamgunov, VP, Engineering, Databricks"
slug: inside-lakebase-fully-managed-serverless-postgres-nikita
conference: databricks-dais
conference_name: "Databricks Data + AI Summit"
category: "Vendor & platform"
edition: "DAIS 2026"
year: 2026
speakers: ["Nikita Shamgunov"]
channel: "Databricks"
duration_min: 9
published_at: 2026-06-24T22:07:19Z
video_id: NqJIyP9rIW8
youtube_url: https://www.youtube.com/watch?v=NqJIyP9rIW8
tags: ["Databricks"]
transcript: true
---

# Inside Lakebase: fully-managed serverless Postgres – Nikita Shamgunov, VP, Engineering, Databricks

**Nikita Shamgunov**

`Databricks Data + AI Summit` · `DAIS 2026` · `2026` · `9 min`

`#Databricks`

[Watch the recording](https://www.youtube.com/watch?v=NqJIyP9rIW8) · [Conference site](https://www.databricks.com/dataaisummit)

## Description

More software will be built in the next year than throughout the whole history of humanity. And every one of these new systems requires an database designed for AI.

It's why Databricks built Lakebase, a fully-managed, serverless Postgres database for AI apps and agents. At Data + AI Summit 2026, Nikita Shamgunov, VP, Engineering of Databricks, explained how the team re-architected Postgres and outlined the features that help Lakebase out perform industry rivals, including the first fully-managed cloud disaster recovery.

00:00 — How AI is changing software development
01:56 — The pros and cons of Postgres
02:28 — Re-architecting Postgres
03:45 — The transformative power of Lakebase
07:27 — Why Lakebase is ready for any workload
07:44 — The first fully-managed cloud DR
08:57 — Lakebase momentum

## Transcript

*1,304 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=5s)** Thanks to AI, we now generate software. We're not writing it by hand. And we're looking at the trends for the first 6 months of year 26. And now we can confidently say we're going to have more software generated in the next year than in the history of humanity. And every application still needs a database. So, what do next-generation application and agents need from a database? So, the first thing is it needs to be familiar. And the reason to that is the more agents know about the systems, and they know by scanning the internet and scanning all the Stack Overflow forums and Reddit, the better they are at running and operating it. So, it needs to be open source.

**[0:54](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=54s)** It needs to be popular, and it needs to be extensible, so you can consolidate all your main and also niche workloads on the single database platform. It also needs to be nimble. With this onslaught of applications that are coming at us and all their various dev, test, and staging environments, uh the system needs to be serverless, and it needs to be branchable, so you can easily create environments for your agents in which they can safely operate. And finally, as you run those things at scale and at volume, uh it needs to be cost-effective. The final thing it needs to be mission-critical. Operational databases run your business. And so, um that means is it needs to be infinitely scalable, it needs to be fast, and it needs to be extremely

**[1:42](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=102s)** reliable. So, familiar, nimble, and mission-critical. So, we decided to start with Postgres, the most advanced open source database in the world. It has a largest uh ecosystem in the world and also lots and lots of extensions. Again, you can consolidate all your additional workloads to the main one, to the operational database system one, into the platform. It's also open-source and understood by every agent on the planet. But Postgres is a monolith. And the compute and storage in the monolith are tightly coupled. So, if you want to make it nimble, um you need to do something. You need to re-architect that system.

**[2:32](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=152s)** The main idea we had is we can decouple storage and compute and move storage into the lake. But it's actually, you know, much harder than you might think. And so, for that, we need to re-architect storage from the ground up. The lake storage is, you know, has a lot of very, very good properties. It's inexpensive. It's very easy to scale. But it's also slow and transactionally inconsistent. So, as we are rebuilding uh the storage for Postgres to run it on the lake, we had to introduce two additional services, one for reads and one for writes. For writes and transactional consistency consistency, uh we built safekeepers. They implement a consensus protocol called Paxos. So, they give you low latency writes.

**[3:19](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=199s)** And then, we introduce another service called page servers that serve pages to Postgres compute. Those systems are called page servers and they deliver on low latency reads. Then, we put it all together and integrate with the lake. And that gives us uh Lakebase. The fully managed serverless Postgres that runs on the lake. So, what does Lakebase give us? Well, um it certainly is nimble, right? So, we can provision Postgres in under 500 milliseconds. And as you have lots and lots of developer staging environments for every potentially PR that you you want to move into GitHub, um we can scale it also to zero, right? So, with lots and lots of environments

**[4:09](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=249s)** and they're serverless, we need to deliver on TCO. So, we automatically shut down environments that you don't use. We introduced two more patterns that are incredibly useful in this new agentic world. The first one is branching. Every Postgres database you can easily branch, and it also branches in about 500 milliseconds. So, you can create an additional environment for you to create dev, test, or staging. Another another pattern that kind of emerged in that agentic development is uh snapshot restore. With any with a simple mouse click or an API call, you can snapshot your database, then unleash your agent to do work uh to build some software, change the schema, change the data, whatever. Uh if

**[4:57](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=297s)** the work is to your liking, you can proceed. If not, you can instantly roll back to the previous snapshots. So, now uh it's built for agents, but is it mission-critical? Can it support your business? Let's start with scalability. With Lake Base, all you need to set is uh error bars for your compute. You can say, "Well, don't scale my compute below this minimum or over that maximum." And you want to do it for potentially cost controls. But within two those error bars, you actually can uh scale up and down automatically um as your workload changes. So, we'll scale the system up at your peak hours, scale things down um at maybe on weekends or nights.

**[5:47](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=347s)** Storage, of course, is on the lake, and that gives you infinite scalability. You will never run out of storage, and you will never run out you will never need to run management operations if you're approaching, you know, your disk size or whatever. So, now you might be wondering though, so you change the architecture of Postgres at the storage level. So, is it fast? How does it compare with the industry implementations of Postgres as a service? So, this is a very similar graph to what Rail is showing for Aiden where we're measuring latency as we scale throughput. Obviously here, it's an operational system. So, it runs much smaller queries that in analytical systems, but they run

**[6:34](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=394s)** it at at very high concurrency. And we're comparing it with the first cloud vendor, which is quite popular. And that cloud vendor taps out about at about 130 operations per minute. And by the way, we're running a a fairly standard industry benchmark called TPC-C. Another cloud vendor with slightly different architecture was able to push its throughput to about 350,000 operations a second, but after that, of course, latencies started to spike as well. And I'm very excited to to to showcase some of the incredible performance work that we've delivered, and Lake Base can scale under 10 milliseconds for each transaction for each operation all the way north of 600,000 operations per

**[7:23](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=443s)** second. Lake Base is is ready for almost any workload. Mission critical also means a lots of features, right? And those features are security compliance encryption you name it, and we have it. But I also wanted to showcase something that we are in a very very unique position to deliver on. So, cloud outages don't happen every day. Uh but when they do happen, they're they're devastating to your business. And now that a lot of your business is increasingly automated and run by agents themselves, cloud outages could could be really really disruptive to your operation. So, I'm incredibly excited

**[8:10](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=490s)** uh to introduce first fully managed cross-cloud disaster recovery. >> [applause] [applause] >> This is what we mean by truly mission-critical. With fully managed cross-cloud disaster recovery, you can set up your system to run cross-clouds. So, you can provision Lake Base, let's just say US West AWS, and then a a replica US East Azure. And in the case of AWS outage, you can instantly fail over from one cloud to another and continue your uninterrupted business operations. So, this is Lake Base.

**[8:58](https://www.youtube.com/watch?v=NqJIyP9rIW8&t=538s)** It's fully managed serverless Postgres that runs on the lake and it is mission-critical. We've only been on the market for a year, but we already have over 3,500 enterprise customers that trust us with their mission-critical workloads. >> [music]
