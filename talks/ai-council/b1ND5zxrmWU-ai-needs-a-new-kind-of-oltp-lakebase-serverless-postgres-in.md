---
id: b1ND5zxrmWU
title: "AI Needs a New Kind of OLTP: Lakebase & Serverless Postgres in the Agent Era | Databricks"
slug: ai-needs-a-new-kind-of-oltp-lakebase-serverless-postgres-in
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 15
published_at: 2026-06-16T18:45:02Z
video_id: b1ND5zxrmWU
url: https://www.youtube.com/watch?v=b1ND5zxrmWU
youtube_url: https://www.youtube.com/watch?v=b1ND5zxrmWU
tags: ["AI"]
topics: ["Agents & orchestration", "Data engineering & MLOps"]
transcript: true
---

# AI Needs a New Kind of OLTP: Lakebase & Serverless Postgres in the Agent Era | Databricks

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `15 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=b1ND5zxrmWU) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 1 - DATA ENG & DATABASES] AI agents are driving a new category of operational databases, creating workloads that look nothing like traditional SaaS traffic. In Lakebase today, over 80 percent of new databases are created programmatically by agents rather than humans, resulting in extreme burstiness, highly ephemeral environments, and large volumes of short lived databases. These patterns push classic OLTP assumptions, including always on instances, steady traffic, and tightly coupled storage and compute, beyond their limits. In this talk, we will explain why existing databases struggle with agent workloads and how a new OLTP design emerges from separating storage and compute, enabling fast autoscaling, true scale to zero, and database branching that allows agents to run experiments and roll back state instantly. Using Lakebase and serverless Postgres as a concrete example, we will share practical design lessons for anyone building data infrastructure in the agent era.

SPEAKER:
Stas Kelvich - Principal Software Engineer, Databricks & Neon.com co-founder

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*2,268 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=0s)** Uh, my name is Stas, and I work at Databricks at a pretty cool project which is called Lakebase. And Lakebase is extremely popular with coding agents. And this is talk I want to like share a bit how how we get there and why is it popular with coding agents. And by popular I mean if you go to your cloud code or you go to Codex and ask "Please create me an app." And most likely it actually will will suggest you Lakebase or Neon. And there's a bit of a terminology thing here, disclaimer. So, Neon is a company that I was co-founder of and it was acquired by Databricks almost exactly 1 year ago. And Neon that is deployed on Databricks

**[0:49](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=49s)** and integrated with the rest of Databricks ecosystem is called Lakebase. And we share pretty the same uh, patterns of separation of storage and compute as Databricks does. So, it's like pretty pretty tight integration. But in this talk I will uh, use Lakebase and Neon interchangeably. Basically, we are keeping the Neon website and that is for solo developers and agents to consume it and Lakebase is the enterprise version of that. And we also like shipping features uh, of uh, enterprise analytics integrations into uh, uh, Neon version and vice versa. [clears throat] But let's get to the details. So, that's a graph of databases that are created by humans in light blue and by agents. And what do

**[1:38](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=98s)** I mean by agent here? So, usually it is some coding platform like Replit agent or Vercel V0 or Create XYZ, you like name it. A ton of them and uh, here we can do attribution pretty well. We know that if project creation request is coming from Replit. That's That's like Agent Proton app and that app is being connected to the uh to our system. But then uh you can see the bump of light blue here around the new year and that's actually a cloud code usage. So uh it's also not necessarily humans. It just humans asking their personal cloud code to create a database for them and it just like goes and picks picks us. And uh here just like

**[2:27](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=147s)** attribution is is is harder to make. So we the only way to do an attribution is just like talk to that customer. But then what what kind of gets out there? Uh the first step like basis Postgres and I think like word Postgres mentioned in in this conference is quite a lot. And maybe let's reflect a bit why Postgres is gaining the popularity uh over the actual last last few decades and became a like top top one database. So everybody is using it. So I think the reason is that Postgres is extremely good at solving day zero problems uh for developers. So when you're writing your app when there is a engineer who is writing an app, they need to pick some database and here you

**[3:16](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=196s)** will you'll pick the database that that makes your life easier at this moment of time. And Postgres is extremely feature feature rich. Uh it has uh it just spatial features. It has vectors feature features. It works with JSON really well. So up to uh so the moment when you're picking a database is the moment when you're like doing first passes over your app and that's where Postgres is actually shines. Um But at the same time Postgres is uh using word word Postgres and cloud native or modern in one sentence is is also a stretch. It's actually a like

**[4:04](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=244s)** almost a 40-years-old coding project. So, there was a guy who liked to put the dates and comments when they wrote them. So, that's that's code base that's being continued continually developed for the last I think I think it's like mid-80s where it's actually it was a list that was written in C and kind of stayed stayed there. Uh and some of the design decisions that were put into Postgres back then, they aged really well. So, uh extensibility and the way the way indices integrated with the rest of the system, that's that's aged really well and allowed Postgres to basically take over the database transactional database space. But, some of the design decisions are just like old and it that creates a ton

**[4:53](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=293s)** of issues when you are operating Postgres. So, how can we fix that? How can we make uh operations of Postgres easier? And to answer that, let's actually look at the how databases were built historically. So, the first one, like depending on where we start, but let's start with uh with with uh maybe last 40-50 years. Uh you have you have some product database A, let's say, and they ship to a customer in a box on a CD disk, and they install it on a on a machine. And that machine has a certain size. And uh that's that's where we all started, but that has obvious problems. What if your database has stores a lot of data, but doesn't

**[5:40](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=340s)** require uh a lot of compute. It's kind of archival case. Or what if your database is actually super CPU intense, but doesn't have ton of data. And people started switching to to disaggregated systems. That's way better. Here you can use one node type for your compute, different node type for your storage. And also you can better like avoid dealing with a uh patterns like L L-shaped load where you try to collocate that uh big unloaded databases with tiny loaded databases. It's hard. So, in that in that paradigm, it's way easier to do it that way. Uh but still uh you're using uh storage that is not open. And that is like first you're kind of creating a

**[6:29](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=389s)** silo, so nobody has access to that data. You need to do a some replication or ETL to get the data out of the system. And that's like one class of the problem with that storage. Another class of the problem is that it's actually hard to do to store data reliably. You have to deal with disk failures. You have to deal with erasure coding. Aurora stores data six times, and they try to match speed of uh their re kind of re-silvering data after the disk failure with a probability of how like how often the disk fails to get certain amount of nines of not losing the data. >> [clears throat] >> And that's actually the same problem that engineers at at object stores are solving in system like

**[7:19](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=439s)** S3. Uh they do the same, but on a way bigger scale, because most of the data lives in object stores. And most of the data in object stores it's like written, but never read. Some some random streams from webcams that nobody's accessing. So, they have the same problem. Uh and they like arguably better at solving them. And you're doing the same for no good reason. So, that like logical next step, okay, let's actually put everything on object store, and now all of your system can access the same data. And uh you're also not on a hook of data durability for the most part. But, the tricky thing is that like it's hard to do. Object store average access latency is

**[8:07](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=487s)** something like 100 milliseconds. And you don't want to have that with transactional database. You want sub-millisecond reads, you want sub-millisecond writes. And basically, the way to do that is like you have to amortize your read path, you have to amortize your write path. Uh So, let's unpack this picture a bit. Uh so, first there is a Postgres the red box. So, Postgres is that we we take relatively unmodified Postgres, we patch it a bit. Uh we don't want to do high availability in Postgres. We want We don't want to store any like using Postgres feature for data storage. We want to deal with storage and high availability on our side, and in multi-tenant services that are written in Rust, that are written

**[8:55](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=535s)** using modern coding practices. But, still it's super important to not to uh change semantics of Postgres. So, like transaction execution. Uh you don't want to break up compatibility with with apps that already built against Postgres. So, so we so we put that Postgres in a in a VM, and it's that that VM is more like AWS Lambda. So, it's stateless, we can move it around, we can scale it up and scale it down. And it's way easier to operate. And also provides you a security barrier. So, there is a trade-off between extensibility and security, and Postgres allows you to bring bunch of extensions, and overall, that's like you can hack out of your Postgres. That happens like few times per year. There

**[9:43](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=583s)** are some CVE. So, that should be a security boundary. Um then you write some data, and as I said, you want to want that right to be really fast. And we have to amortize it. We have to first write on set of local SSDs, and once you're dealing with data modifications and high availability, you have to solve problem with consistency. So, our right path, we write first to the uh set of nodes that we call safe keepers. We amortize that right, but also we want like to get get rid of be or like stop being responsible for that durability of the data as soon as we can. So, we transfer that to S3 and changing the format along the way. Um But, yeah. Durability guarantee here or

**[10:32](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=632s)** invariant is that data is either on safe keepers on a quorum of them, and we can tolerate failure there, or it is on S3, and the majority of data would be on S3, and it like durability as S3 is pretty good. But, then you also want to amortize your reads, and to serve pages fast, but also there is availability argument here. Durability of object storage is great, but availability is pretty pretty ordinary. There could be outages, uh and we want to target a higher availability range compared to what cloud storage API gives you. So, actually cache all of the data in the service that we call page servers. So, it's like serves two purposes. Uh or maybe like two or three purposes. Like one is to have low latency cache.

**[11:20](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=680s)** Second is that you have now basically bottomless storage, so we can spread that storage across series of nodes and implement storage level sharding. But, also it helps you to paper over over any object store unavailability that can happen. If it happens within a like half an hour hour you will not notice it because that that just fleet of nodes helps you. Um Okay. So that architecture allows us to do a bunch of really nice features. Since computer is stateless, we can do scale to zero easily. We can do auto scaling and by auto scaling I mean

**[12:09](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=729s)** in place What is it? Vertical auto scaling. Um so that we actually dynamically add CPU and memory to your process and again that's like pretty weird way of doing auto scaling, but we are dealing with Postgres that we are trying to leave untouched to avoid changing the semantics of query execution. So we are dealing on that with the lowest level possible. We just add CPU and memory and then move that VMs around and there is a whole side story of how AWS tried doing similar uh project and they shipped serverless V1 that was like more classic uh vertical scaling when you have proxy in front and then you swap the node and they basically cannot stabilize it. Then they shipped serverless V2 that was like pretty full rewrite of that which used

**[12:58](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=778s)** which used pretty similar model where you like add CPUs and memory to the VM and then live migrate that VM. Um Another thing that you can do and it's pretty important for agenda use cases that since you're controlling the storage, now you can do like nice modern features of modern storages like branching and people are using it a lot. Basically, if you have preview deployments on the like Vercel you open your pull request, uh Vercel bot uh comes there and puts your link like, "Hey, that your pull request is deployed on the temporary domain." And the usual way people used to serve that preview deployment that you target all of them in one database. And it

**[13:46](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=826s)** doesn't work well if you have migrations. And uh yeah, you can create a database branch and run your migrations on a branch and have a real data there and test it with a real data. It's a It's pretty easy for us to do since we control the storage. It's super nice feature for a human who are using it in pull request, but also before agents. So, for example, Replit agent, they use they use they create branch of database on each agentic turn so that they can easier roll back. And they were like running into a lot of I think that's the first time with Replit agent when we're started bumping in a limit of 1,000 branches. So, we had to raise it to 5,000 branches. Um

**[14:33](https://www.youtube.com/watch?v=b1ND5zxrmWU&t=873s)** Yeah, so that's that's that's that's really uh in a nutshell what Amplication agentic use cases and uh Amplication developer adoption. >> [music]
