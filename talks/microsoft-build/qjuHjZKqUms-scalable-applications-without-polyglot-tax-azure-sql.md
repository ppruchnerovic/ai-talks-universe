---
id: qjuHjZKqUms
title: "Scalable Applications Without Polyglot tax: Azure SQL Hyperscale | OD824"
slug: scalable-applications-without-polyglot-tax-azure-sql
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 24
published_at: 2026-06-03T13:45:21Z
video_id: qjuHjZKqUms
youtube_url: https://www.youtube.com/watch?v=qjuHjZKqUms
tags: ["Azure SQL Hyperscale", "CP&D", "Data", "OD824", "OD824_v1", "Scalable Applications Without Polyglot tax: Azure SQL Hyperscale | OD824", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Scalable Applications Without Polyglot tax: Azure SQL Hyperscale | OD824

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `24 min`

`#Azure SQL Hyperscale` `#CP&D` `#Data` `#OD824` `#OD824_v1` `#Scalable Applications Without Polyglot tax: Azure SQL Hyperscale | OD824` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=qjuHjZKqUms) · [Conference site](https://build.microsoft.com/)

## Description

Modern application architectures have drifted toward polyglot persistence, adding complexity, data movement, and operational overhead. Azure SQL Database Hyperscale takes a different approach: a single, multi model system that brings relational, transactional, and emerging workloads together within SQL. Learn how Hyperscale redefines performance, elasticity, and operations. See why consolidating on a single, multi-model SQL platform is the simpler, more scalable path for modern applications

To learn more, please check out these resources:
* https://aka.ms/build26-next-steps

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

OD824 | English (US) | Cloud platform & data

Pre-recorded | (200) Intermediate

#MSBuild

Chapters:
0:00 - Introduction and session overview
00:01:05 - Adding new features leads to multiple specialized databases
00:07:01 - Schema flexibility and transactional support for JSON operations
00:08:03 - Performance comparison with document databases and single platform message
00:13:16 - Importance of ACID semantics and idempotency in agent-driven systems
00:16:11 - Azure snapshot backups improve reliability and reduce compute load
00:17:02 - Using hyperscale with primary OLTP and named readable replicas
00:19:19 - Integration of Microsoft SQL core engine in Hyperscale
00:22:42 - Performance and licensing-free model of Azure SQL Hyperscale

## Transcript

*3,405 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=qjuHjZKqUms&t=3s)** Hi everyone, I hope you are having great build. I'm Aditya, I'm the product manager from Azure SQL. Today I'm here to talk to you about building scalable applications without having polyglot tax. Now let's talk what exactly is polyglot tax? What do you mean by that? When I say polyglot tax, I mean having having the tax that you pay for choosing multiple databases. OK, how many of you are building applications day in day out? I'm sure everyone, right. So let's say you build a prototype, OK, how long you do you take based on based on whatever the application is it takes you start at 9:00 AM before lunch.

**[0:49](https://www.youtube.com/watch?v=qjuHjZKqUms&t=49s)** You almost have it. You can say Aditya, it can be fast. I'm sure it's for sure fast so, but my point is you can build a prototype pretty fast. But let's say you built a prototype and that prototype is super successful. How do you and then you want to add something like semantic search with vectors. You might get a vector DB and then you extended it to have graphs. You added graph DB and then you need to do analytics on top of it. You see what I'm doing here? You add so many databases that are specific to them and now because you are adding so many databases in all of this data, in all shipping all of this data, if something brokes at one point, the other other

**[1:41](https://www.youtube.com/watch?v=qjuHjZKqUms&t=101s)** things won't work. Imagine the data that flows from vectors is is broken, which comes to the analytics. The analytics might not give you the right answers. So that is broken. So, so that's, that's the polyglot tax I'm talking about. We are here because this, this one, this one we can really avoid with Microsoft SQL. Now, how do if let's say you're building a fraud check, real time fraud check application, right? How do you typically do that with all these databases? You do you have a relational database for order history, you have a JSON or a document databases for a device fingerprint.

**[2:30](https://www.youtube.com/watch?v=qjuHjZKqUms&t=150s)** When I say device fingerprint, is it coming from an application, is it coming from a browser, etc. You might use a document database for that. For detecting multiple graph relations between multiple people, you might use graph. If you want to find similar transactions like What would this database look like? What is this transaction looking like? Buying something from a Walmart, what does that look like? Is there? Is there a similar transaction to that? There is that too. And and then finally you would want all of this coming to a statistical baseline, which essentially means analytics. You have 5 different databases, 5 different sync jobs, 5 different auth systems, and because of all of this, you have so much latency because your application needs to wait

**[3:22](https://www.youtube.com/watch?v=qjuHjZKqUms&t=202s)** to read from all of this. The costs are also the same. That's what I'm trying to say. Because you are trying to read from all of this, you have network latency, you have different security surfaces. With all these databases. You have security in relational versus DW versus your what is a graph, all of that. You have separate auth systems everywhere. You need to pay tax for that. You will have different database backups for all of this. Imagine that if you there is no one single backup statement that would be doing this. Finally, more than anything, there is cognitive load, right? So which means I need to as a developer I need to learn 5 different tools, 5 different query languages,

**[4:12](https://www.youtube.com/watch?v=qjuHjZKqUms&t=252s)** etc. Now as a user it's OK, but as an agent it's going to be even more tough because agents with so many choices tend to hallucinate a lot. More hallucination means more wrong data which we really doesn't want to have. That's why we are here talking avoiding polyglot tags with Microsoft SQL Core engine and not just with engine. Avoiding the tags you need scale to perform and use the best of this engine. That best of this engine comes from Azure SQL Hyperscale. We will talk how Azure SQL Hyperscale helps with that. So act one, how to avoid the tags with all the different capabilities that we built into Microsoft SQL Core

**[5:01](https://www.youtube.com/watch?v=qjuHjZKqUms&t=301s)** engine active is to how do you scale that Microsoft SQL core engine which is the base of building the Azure SQL hyper scale. OK, let us go into Part 1. OK, so let us talk about the first act, which is the core engine and how we are avoiding the polyglot tax with Microsoft SQL. OK, so let us say, let us say you have they as I mentioned in the and fraud fraud detection app setting where you would need if you are logging from app or if you are logging from a web browser you need you need a Jason kind of a document and how would SQL really do that? So recently SQL essentially introduced Jason native type and Jason indexes.

**[5:55](https://www.youtube.com/watch?v=qjuHjZKqUms&t=355s)** And it is previously when we started we kind of did nvature of Max, but it is no more nvature of Max. It is purely Jason, Jason type native Jason type ANSI. And it is it is a pre passed binary, which means the way we store the Jason in our engine is a pre passed binary, which essentially makes Jason save 30 to 50% less. And there is this famous GIN index which in another relational databases where you index when you index the enter Jason document gets indexed. The cool thing that we did with Jason in Microsoft SQL is you can index the particular path of that Jason.

**[6:42](https://www.youtube.com/watch?v=qjuHjZKqUms&t=402s)** So that essentially makes you feel that OK, if I want to search only on the device than whatever the date or anything I can index only on the part of device in the Jason and attributes and you can your Jason index will essentially pick that. Now with with Jason, one of the favorite features of using Jason even for the people in document databases is the schema flexibility. You can have a Jason document of like let's say 4 attributes, one of them and another Jason document of five attributes In a relational world, you might need to add 1 more column and all of that. That is not there with Jason. And hey, SQL supports it, Microsoft SQL supports it. And now all the Jason updates that you do and

**[7:33](https://www.youtube.com/watch?v=qjuHjZKqUms&t=453s)** what all you do follow the same transaction boundary and no more or nothing more than that. So which means you can rollback roll all the asset properties are done. So we kind of see the Microsoft SQL we did internally we did by CESW tests and we see that we are no less than any document database when it comes to Jason performance and Jason index performance. That's why we that's why once you do this, I almost kind of say you need not really think about having a separate document database. We can essentially say goodbye then we just bank on Microsoft SQL. Now since forever, as I said, we are, we have invested in graph and you have Graph in Microsoft SQL.

**[8:26](https://www.youtube.com/watch?v=qjuHjZKqUms&t=506s)** You can do match and you can say the syntax is natively supported and you can have the query optimizer understand this match and give you a perfect plan that is required for this match and that way that the graph is inbuilt in Microsoft SQL itself. So you have Jason, you have graph and there are graphs also very interesting scenarios when it comes to application like anti fraud detection, fraud detection and all of that. So, so you really need wherever you need a specialist graph kind of scenarios you need Microsoft SQL does support all the basic graph functionalities such that you can you can use Microsoft SQL for that.

**[9:18](https://www.youtube.com/watch?v=qjuHjZKqUms&t=558s)** Now recently we used, we started supporting vectors and when we started again, we used to support vectors on top of Val binary. And then we immediately switched and vectors in native type. Now we initially released vector type, but we haven't released the index on it. They later we, we released the vector indexes using the disk KNN, which is a great Microsoft research which came out of from this Microsoft search and which is essentially pretty fast than HNSW. And now imagine vector databases are kind of tricky, right? If you have a specialized vector database and if you don't have the operational datas context to it, what happens

**[10:11](https://www.youtube.com/watch?v=qjuHjZKqUms&t=611s)** is you would end up searching a lot number of rows, a lot number of vectors and that is costly in general. Let us say you want to search about person Bob and that person Bob is in one of the relational data. You find that person and you will select transactions similar to that which essentially gives you more context and hence it will help you, it will help you reduce the reduce the tax on it and it will pretty fast. Hence essentially it's a pre filter. And we also, we also kind of introduced very recently updatable disk NN indexes.

**[11:02](https://www.youtube.com/watch?v=qjuHjZKqUms&t=662s)** So this essentially makes people who are vector databases kind of there is no need of a separate vector database. Now Cluster clustered columnstore. This is one of the very famous features that SQL have and we are continuously investing in this columnstore today where so in my Indiana SQL traditionally used to be its row store. You can convert them to column store and which is which is more OLAP friendly. And all the data that you have for the analytics, you can transfer them as a column store which essentially again gives a very huge amount of compression for you to on top of the row store and you can

**[11:54](https://www.youtube.com/watch?v=qjuHjZKqUms&t=714s)** expose that for your analytics endpoint. So that that essentially gives you hetched up 1. You have the primary transactions, you have analytics, you have Jason. But just having transactions, analytics and the real time transactions, it makes Microsoft SQL one of the best analytical stores out there. So now combine all this story, right? Let's let's look at all of this. You have, you have Jason, you've got the order history of a person using relational. That's what I'm kind of doing with this. And then you kind of got the device footprint from Jason saying by just using Jason value and then you said OK for this.

**[12:43](https://www.youtube.com/watch?v=qjuHjZKqUms&t=763s)** Can you give me for the match of this way for a risk score greater than 0.8 and then find the similar transactions of that in the vector table and give a 90 day baseline on top of it. And I can write all of it in a single stored procedure and execute that and it will have one transaction boundary. Which means, let's say when you're writing something on Jason, if it fails, everything fails. This is very, very important for agents because agents, though one of the fact that we learnt recently is agent needs a lot of data to read. But agent also loves item potency, which means they come,

**[13:33](https://www.youtube.com/watch?v=qjuHjZKqUms&t=813s)** they write, If they write they might rewrite because of so many things, which means they need a proper rollback. Acid semantics are so important in agentic world than a normal world because in a normal world, a developer would be sitting and making sure that oh this transaction has this transaction boundary. And hence when it comes to agents, they they just come in, put the transaction and go out. That we should really make sure that acid is acid is the only way where you can know the data that is coming in is completely coming in and get committed. So it becomes even more important in the agenting fold. Now that is the part with the core engine, right

**[14:22](https://www.youtube.com/watch?v=qjuHjZKqUms&t=862s)** where you avoided polyglotax. Now take this core engine, take it up and you plug that into something which scales that is hyper scale, that is the hyperscale and I call this database as Peace of Mind database. The reason why I call this database as a piece of mind database is you when you start, there is a famous customer. He told me the story, right? He mentioned, hey Aditya, after I after we switched to hyperscale, I can really sleep peacefully in the night. That made me come up with this Peace of Mind database with some other colleagues. The reason why I said what is that that whatever that customer told me so important is the customer need not wake up for a file group full or a

**[15:15](https://www.youtube.com/watch?v=qjuHjZKqUms&t=915s)** file full or a log full or anything because hyperscale just grows as your application grows and it has its own dedicated log service. It has its own paid servers and Azure storage. So why I typically show a architecture diagram here, I'm not showing it purposefully because all you and all you need to understand here is hyperscale has different components. You have log service, dedicated log service for your writes. Your reads are coming from paid servers which are essentially a which have SSDs of its own and it is asynchronous. Log service will do continuous redo into page service. This page service will continuously write back into Azure storage

**[16:08](https://www.youtube.com/watch?v=qjuHjZKqUms&t=968s)** for the durable as a durable tier. Now if you do that because you are writing into Azure storage, what happens is we can use the Azure storages tech of taking snapshots. Now eventually it became a good news for all the users because compute on the top is not involved in taking the backups which means there is no pages that were read to take a backup. In traditional SQL if you are doing backup database, database name, you are essentially reading that backup, reading all the data into the computer and writing it back into the dot back. That is not needed anymore with hyperscale snapshot backups. Now how in general with agents in all of this world people use hyperscale right?

**[17:02](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1022s)** So the way they use is they use primary for the OLTP rights. One of the major things that hyperscale has an advantage is having named replicas. What this named replicas is, think of it like you have your its own connection string for a readable copy. Now why is that important? That is important because that readable copy essentially has its own buffer pool, which means its own memory, its own L2 cache. We call it as rbpex which is residual in buffer pool extension, which means it has its own working set. And that working set is extremely different to any other named replica that you give. So you can differentiate working sets in hyper scale with different named replicas with an underlying all the same data

**[17:54](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1074s)** of 128 TB. And you can have your writes not affected by reads. So we see customers doing writes on the primary, their continuous writes. We see customers doing agents pointed to the one of the named replicas and they do vector distances, similar transactions, all of that and find find the cosine, cosine similarity and give back what exactly it is. So that from one named replica one other. They have have seen customers using nightly jobs and they use serverless specifically for those named replicas. They go in the morning, the serverless comes to two week course and in the night when they use they expand it to 128 week course.

**[18:44](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1124s)** They run their job, run the analytics and they sleep off. So they use separate name replica for that. By the way, your primary can always be provisioned and you are second your name replicas can be serverless. So we also care about your business continuity. Hence we do have Godr and high availability in the built in into hyperscale. Now let's look at the other other side of it. Hyperscale comes because hyperscale also is a Microsoft SQL code engine. The engine itself has the best security out there. Do you know something that Microsoft SQL supports?

**[19:37](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1177s)** Ledger 2? That's what we support even in hyperscale because Microsoft SQL supports it. We have dynamic data masking, you can have always encrypted EXEC only stored procedures, tenant based execution, all of that using Microsoft SQL Core engine. And also in hyperscale what is what is AI or agent or any talk without having an MCP server, right. So SQL has its own MCP server. We used, we did that with the data API builder. You have you have so many tools that you that you use, you can use with this MCP server. You point the, you have a dab created dab, you created a data API builder using Data API Builder.

**[20:27](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1227s)** You created that and you got, you get your data API REST endpoint. Using that REST endpoint, you can point that to an MCP and that MCP can come from hyperscale. And then if that's it, so you can talk to your data which is in hyperscale. Imagine this, right, you have 128TB data, you have agents, you have rights, and you have MCP. You can talk to all of this with MCP with the natural language saying update so and so person's name, last name to this or change the salary of so and so person to this, all of it using MCP. That's what we have with SQL MCP server.

**[21:15](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1275s)** Yeah. So what is we understand that core engine now. Now come back to core engine is now doesn't have polyglot tags and hyper scale this giving scale whatever it is, the economics are very important, right. So in the economics we because you are avoiding polyglot tax essentially you are eliminating all the side cars which means separate vector DB, separate graph DB all of them are not there and hence you eliminate that tax. You only pay for you your what you use with serverless and between go from 2 vehicles to 80 vehicles. The only when you need, if not, you will come back to the two vehicles and pay the less bill for that you pay only for storage from 10 GB to 128 TB.

**[22:03](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1323s)** We want to over provision like you need not over provision upfront and you don't pay need to pay bill. Whenever your data grows, we grow with that. Which means even the people cost is less because you really need not think of having five different personas doing 5 different things and five different expertise. You can have one SQL expertise and that's pretty much it. So hyperscale also imagine all of this we are giving you with a 68% better performance than our COMP 8. So that's a steal, right? So that's why we say that Microsoft SQL come in with Azure SQL Hyper scale has the best economics. By the way, one point I really want to touch upon is Azure SQL Hyper scale is the Azure SQL Hyper scale is the database with licensing free model.

**[22:57](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1377s)** Now come. So ultimately, what what is there? What is here right? So 2 acts, 5 ideas I should I will leave you with polyglot is a tax is a choice, not an in availability, which means it's not really needed to go to polyglot tax choice. But I also want to ground upon a truth that one size doesn't fit all right. So there are cases where in the extreme cases you might need a DQP and you really need a, you really need a data warehouse. In the extreme cases of graph, you might need a separate graph databases. But all the basic scenario, all the scenarios where for the most of the scenarios, unless it is exceptional Max of SQL covers you with an exceptional relational workload. So that's what we are saying.

**[23:47](https://www.youtube.com/watch?v=qjuHjZKqUms&t=1427s)** And hyperscale architecture is one of the best architectures purpose built for purpose built for cloud. And agents, as I mentioned in the talk, really, really need all these guarantees more than ever. So Microsoft SQL and Azure SQL hyperscale as a story is so shining right now than ever. So all I say is avoid the talk tax, ship it, scale and yeah, sleep at night. Thank you.
