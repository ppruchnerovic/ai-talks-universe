---
id: j8iKPajnkWQ
title: "What’s New in Azure Data: HorizonDB and Rayfin | LIVE143"
slug: whats-new-in-azure-data-horizondb-and-rayfin-live143
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 13
published_at: 2026-06-05T15:31:20Z
video_id: j8iKPajnkWQ
url: https://www.youtube.com/watch?v=j8iKPajnkWQ
youtube_url: https://www.youtube.com/watch?v=j8iKPajnkWQ
tags: ["Charles Feddersen", "LIVE143", "LIVE143_v3", "Nikisha Reyes-Grange", "Sachin Patney", "What’s New in Azure Data: HorizonDB and Rayfin | LIVE143", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: []
transcript: true
---

# What’s New in Azure Data: HorizonDB and Rayfin | LIVE143

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `13 min`

`#Charles Feddersen` `#LIVE143` `#LIVE143_v3` `#Nikisha Reyes-Grange` `#Sachin Patney` `#What’s New in Azure Data: HorizonDB and Rayfin | LIVE143` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=j8iKPajnkWQ) · [Conference site](https://build.microsoft.com/)

## Description

Get to know two exciting data innovations. Azure HorizonDB rethinks how PostgreSQL databases are built and operated, focusing on a modern, scalable foundation designed for cloud‑native applications. Rayfin makes it easier to build and run data applications in Microsoft Fabric, bringing data, logic, and AI closer together so developers can scale faster without stitching backend services. Learn the motivation behind each, the core concepts to understand, and how they shape the future of application and data development.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Nikisha Reyes-Grange
* Charles Feddersen
* Sachin Patney

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE143 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Speakers Introduction: Nikisha, Charles, and Sachin
00:00:36 - Overview of Topics: Azure Horizon DB and Raefen
00:04:21 - Discussion on problems Rayfin aims to solve—simplifying production deployment for developers
00:06:33 - Conclusion—Rayfin’s role in expanding developer experience and Fabric capabilities
00:07:45 - Introduction to Raefin’s goal of bridging prototypes to production environments
00:09:52 - Highlighting Microsoft’s global community involvement through events, podcasts, and Postgres engagement
00:10:46 - Transition to discussion of AI capabilities in Postgres
00:11:25 - Introduction of AI functions and model management within SQL environment
00:12:28 - Detailed explanation of hybrid search mechanics and indexing options

## Transcript

*2,391 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=0s)** NIKISHA REYES-GRANGE: Hi, everyone. Thanks for joining us, and happy Build. My name is Nikisha Reyes-Grange. I'm Senior Director with Azure Data and AI, and I'm joined by my colleagues Charles and Sachin. Charles Feddersen is the Director of Program Management for Postgres and MySQL on Azure, and Sachin Patney is the General Manager of App Development for Azure Data, and we're here to share some of the top data news that we announced today at Build. So I'm going to start with Charles, okay? CHARLES FEDDERSEN: Yeah. NIKISHA REYES-GRANGE: Because, excellent, we have two things to talk about today. We're going to be talking about Azure HorizonDB. We're also going to be talking about Rayfin, but let's start with Azure HorizonDB. Talk to us, Charles. Tell us about it. CHARLES FEDDERSEN: So HorizonDB was a big keynote announcement. It's our new really sort of Postgres service designed

**[0:50](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=50s)** for building apps and also running enterprise applications. So we made the announcement this morning. It's in public preview today. Everyone can go ahead and get started. NIKISHA REYES-GRANGE: That's awesome, and what problems is it solving? CHARLES FEDDERSEN: So I think one of the interesting things about Postgres is the sheer breadth of adoption that it's seeing. On the one hand, your events like Build, developer conferences, there's a lot of Postgres adoption at that end of the spectrum because it's open source, has a great extensibility model, and you're just seeing tons of new apps being built on it. And then on the other end of the spectrum, you've got your enterprise adoption where they're bringing these applications to the cloud. And so what we're trying to do with HorizonDB is really serve a very large market by bringing a bunch of new AI capabilities and developer-centric tooling in VS Code

**[1:38](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=98s)** to help you build apps quicker and faster on Horizon while at the same time delivering things like enterprise security, network security, all of that so that enterprises can run those mission-critical workloads as well at pretty big scale sometimes. NIKISHA REYES-GRANGE: That's fantastic. And what are you most excited about with it? Like, what do you think devs are really going to love about HorizonDB? CHARLES FEDDERSEN: So we've made a couple of big focuses on things like performance. Of course, one of the things that I actually love in addition to HorizonDB is what we've done with developer tooling in VS Code. About a year ago, we built this entirely new VS Code extension. We've invested a lot of energy into making it look fantastic, making it super functional for both develop -- database management but then also development, and then within Horizon itself we've got a new feature called "AI Pipelines." Think of it as like a sort of a lazy

**[2:25](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=145s)** or a synchronous background task. It's really good for building workflows in the database for these AI applications that require a lot of sort of interactivity with APIs and models. NIKISHA REYES-GRANGE: That's wonderful. And tell us how should we think about Azure HorizonDB versus other Postgres services? Because your team even builds Azure database for Postgres, right? So how should we be thinking about that? CHARLES FEDDERSEN: So the thing about HorizonDB is that the core database layer, it's just Postgres, and so any app that you've built for Postgres, that runs on Postgres is just going to work on HorizonDB. So in a sense, there's not a lot of difference at the most important part, which is the API and how developers work with it. Under the covers, in the storage layer, we built an entirely new storage engine for both log

**[3:14](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=194s)** and storing data, and that's really where it differs from Postgres and Azure database for Postgres as well. It provides significantly more performance with high availability across zones and also significantly larger scale. So that's sort of the key architectural difference, but for developers, it's just Postgres. NIKISHA REYES-GRANGE: That's fantastic. Sachin, you're up next. So we have, on the Azure HorizonDB side, we're really trying to fix some of the performance and scale issues that developers run into, but we also know that sometimes back end and governance can also be challenging. Can you talk to us about Rayfin? What is it? SACHIN PATNEY: Yeah, so Rayfin is an open source SDK and CLI, and it helps you define your back end in code, and so that way you can kind of keep all of your backend primitives and all that right

**[4:02](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=242s)** where your application logic is. And then the CLI, kind of, when you deploy the application, it translates all of those things, like your database or functions or auth, into services in Fabric, and so you get like a governed database, you get isolated functions and scale out of the box. NIKISHA REYES-GRANGE: Fantastic, okay. And so what problems were you trying to solve when you were creating Rayfin? SACHIN PATNEY: That's a really good question. So I think like most people, like we've all been using coding agents and it's really easy to get started with application, that you can build beautiful, amazing applications, and typically, if your application requires a back end, your agent would spin up something more locally like a MySQL or like just file storage on your machine, and now when you want to go take

**[4:50](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=290s)** that application to production, you kind of have to like rethink it a little bit for architecture, for scale, for -- like especially if you're within an enterprise, you have to kind of think about your compliance, governance, and security. And so I think this is the problem that Rayfin helps you solve because you can continue using and developing these vibe-coded applications. You can kind of focus on the business logic, and then when you deploy it, it helps you kind of not just run it locally, but also translate that into Fabric and sort of inherit the governance compliance aspects of it. NIKISHA REYES-GRANGE: Fantastic. And so how should we think about Rayfin compared to other platforms that developers might be using to build apps? SACHIN PATNEY: Yeah, it's a good question, and a good distinction to make is that Rayfin is not an app-building platform, right?

**[5:39](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=339s)** In fact, it's designed to work well with existing app-building platforms. So say, for example, I personally love using the GitHub Copilot CLI to build my applications, and what Rayfin does is it provides like an SDK CLI so that GitHub Copilot can use to go express the back end in code and use the CLI to go deploy it. And so the way to kind of think about it is like just any application out there, so I think we partnered with Replit for this example. So somebody wants to go use their favorite browser-based tool in Replit, they can still use the Rayfin SDK CLI to kind of build out the back end and helps them deploy it and manage their app within their Fabric tenant. NIKISHA REYES-GRANGE: That's fantastic. And I'm going to ask, then, why did you decide to build this for Fabric?

**[6:26](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=386s)** Can you talk about how Rayfin either changes or expands the vision for Fabric and the overall value prop of it? SACHIN PATNEY: Yeah, so even within Fabric, so Fabric is a primary SaaS platform, which you have like zero infrastructure and maintenance, and people already building a bunch of data solutions, and when the databases were coming into Fabric, people were looking to build operational apps, and instead of us providing like out-of-the-box SaaS experiences, we wanted to let organizations use some of these app-building tools to go and build custom front ends and applications within the organizations and in the future also allow them to build more customer-facing applications. And then instead of like having some sort

**[7:15](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=435s)** of complex ETL pipelines to land data back in Fabric, your application data is already in Fabric, so business users can go do downstream analytics through Fabric. NIKISHA REYES-GRANGE: Fantastic. Earlier you had mentioned vibe-coding apps, and definitely there are -- sometimes there's a perception of vibe code versus more meaty kind of enterprise applications. How does Rayfin kind of expand those two extremes? SACHIN PATNEY: Yeah, so I think Rayfin's primary focus is to -- so the thing we talk about is taking your prototype to production, right? So you kind of start building an application and you want to kind of bring it to production. We want to sort of lower that gap, like you don't have to think too much about it,

**[8:02](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=482s)** you're kind of the way you build it. But Rayfin is for -- we want it to be for everyone, so we are also going to open source parts of our runtime that will allow you to self-host those applications yourself, and we are looking to partner with the community to kind of build this out to support different infrastructure types. NIKISHA REYES-GRANGE: Got it. So if someone doesn't want to deploy within Fabric, that will be an option? SACHIN PATNEY: Yes, and that's the option we'll enable. NIKISHA REYES-GRANGE: Fantastic. Charles, speaking of community, we know that certainly Microsoft is huge within the Postgres community and just does a ton to keep the Postgres project going, right? Can you talk to us more about that? CHARLES FEDDERSEN: Yeah, so actually I'm not sure that a lot of people are fully aware of the magnitude

**[8:51](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=531s)** of what we do in Postgres. Microsoft is actually one of the largest contributors to the upstream Postgres project. I think in Postgres 19, which is coming up this year, I think we modified around about 8% of all of the lines of code that were modified in this version. It's a useful measure of sort of thinking about the level of investment we're making in the upstream Postgres project. We're a really strong team of committers, and it's part of, obviously participating responsibly in these open source projects. It also enables us to bring a lot of what we learn about running Postgres at some serious cloud scale that doesn't show up at perhaps small scale, bring that back into the upstream project,

**[9:38](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=578s)** which everybody obviously benefits from, and obviously, having committers on staff as well for our enterprise customers, or for any customers, who might hit more gnarly things in Postgres sometimes. We've got folks on staff who can help them with that as well. We also run the largest virtual Postgres event on the planet. We run a podcast, and obviously, we're incredibly active in a lot of the community events as well all over the world. NIKISHA REYES-GRANGE: That's fantastic. And why are you committing so much to Postgres? What's the vision here? CHARLES FEDDERSEN: We have a lot of customers who are entrusting us to run mission-critical applications, and I think that we can best do that if we're active participants in the open source project ourselves. And so we're going to keep investing in the upstream project. We're going to keep building our cloud services on Azure

**[10:27](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=627s)** that meet these enterprise requirements, serving new developer scenarios. You're building phenomenal tooling in VS Code that, by the way, works with any Postgres. I think that's just a very holistic way to approach Postgres, and if we're going to be a vendor in the space, then we need to invest on all of those fronts. NIKISHA REYES-GRANGE: I love that. Can we go back to the capabilities for AI for a sec there? So you mentioned the AI pipeline they're bringing in. Postgres, I believe, was the first database engine that really started embedding AI capabilities, right? The pgvector extension and whatnot. Can you talk to us a bit more about what some of those capabilities are that are baked into Azure HorizonDB? CHARLES FEDDERSEN: It's fascinating. This pgvector extension was not the most deployed extension at the time that ChatGPT hit, and we all went

**[11:17](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=677s)** and learned what embeddings and vectors were, and if you look at the adoption of that embedding, it just sort of went straight up. And so we've built on that in Horizon. I talked about the AI Pipelines. We've also shipped AI functions that make it possible to interact with models in Microsoft Foundry directly from the SQL language, which is really comfortable for SQL and database developers. We've built native AI model management so that when you provision Horizon, automatically a set of models, embedding, re-ranking models are automatically what we call "registered" in Horizon. So you can provision Horizon just by start calling these models directly from SQL. You don't need to stitch together all the Azure parts to make that happen. We've also done full-text search, which in and of itself is maybe not considered AI, but when you blend it with a vector search, you can now do a full hybrid search in Horizon as well,

**[12:08](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=728s)** and you can even re-rank those results using the re-ranking models that we have, and that just provides incredibly performant search, but also incredibly relevant search so that if you're feeding language models that are basically producing outputs off your enterprise data, you're getting the most relevant results fed to them and that's what everyone wants. NIKISHA REYES-GRANGE: Can you give me an example of a hybrid search? CHARLES FEDDERSEN: Yeah, so a hybrid search is basically a fusion of like full-text search and vector search. So you could do a vector search by itself and the similarity will give you pretty good results, right? And to scan, it actually does a very good job just out of the box. And then we also ship pgvector, so you've got what's called "HNSW" and "IVFFlat," so all three indexes are available in Horizon. But then you can then fuse it in the same query with full text, which can improve the relevance, and then you can also rank them on top of that.

**[12:56](https://www.youtube.com/watch?v=j8iKPajnkWQ&t=776s)** And in fact, you can even go even further and use graph capabilities built natively into Postgres as well. And we've built this really cool graph visualization in VS Code as well so you can see exactly how the data relates. NIKISHA REYES-GRANGE: Okay, well, thank you both very much. We are done. Thank you for joining us today. Happy Build.
