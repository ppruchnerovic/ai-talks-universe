---
id: J0o-Dkt5tnI
title: "Build persistent and scalable AI agent memory with TiDB | ODSP918"
slug: build-persistent-and-scalable-ai-agent-memory-with-tidb
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Ravish Patel"]
channel: "Microsoft Developer"
duration_min: 17
published_at: 2026-06-03T08:28:06Z
video_id: J0o-Dkt5tnI
url: https://www.youtube.com/watch?v=J0o-Dkt5tnI
youtube_url: https://www.youtube.com/watch?v=J0o-Dkt5tnI
tags: ["AI", "Agents", "Azure", "Build persistent and scalable AI agent memory with TiDB | ODSP918", "Dev Tools", "DevTools", "Developer", "ODSP918", "ODSP918_v2", "Open Ecosystem", "Ravish Patel", "Scaling", "Storage", "Vector Embeddings", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Build persistent and scalable AI agent memory with TiDB | ODSP918

**Ravish Patel**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#AI` `#Agents` `#Azure` `#Build persistent and scalable AI agent memory with TiDB | ODSP918` `#Dev Tools` `#DevTools` `#Developer` `#ODSP918` `#ODSP918_v2` `#Open Ecosystem` `#Ravish Patel` `#Scaling` `#Storage` `#Vector Embeddings` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=J0o-Dkt5tnI) · [Conference site](https://build.microsoft.com/)

## Description

AI agents need different data infrastructure than humans—and they forget everything between sessions. See how TiDB is built for agentic workloads, combining vector search, BM25, and SQL in a unified table to manage agent memory at scale. Learn how hybrid retrieval with RRF, Azure OpenAI embeddings, and ACID transactions enables reliable, scalable agent systems you can deploy in Azure environments.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Ravish Patel

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

ODSP918 | English (US) | Cloud platform & data

Pre-recorded | (300) Advanced

#MSBuild

Chapters:
0:00 - Three main challenges: bursty workloads, massive concurrency, constant context recall
00:04:03 - Refund process and email failure scenario
00:05:15 - Introduction to TiDB
00:06:14 - TiDB features for agents: solving prior data problems
00:09:45 - Demo Step 2 – Inserting user memories and automatic embedding generation
00:11:57 - Demo Step 5 – Running hybrid search combining vector and keyword results
00:13:10 - Introduction to asset transactions across multiple tables in TiDB
00:13:38 - Transaction demo showing consistent multi-table insert and update operations
00:14:19 - Case study: Manus AI startup deploying millions of agent databases on TiDB

## Transcript

*2,418 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=3s)** RAVISH PATEL: Hi, everyone. My name is Ravish and I work at PingCAP on TiDB as a solutions engineer. Over the next 20 minutes or so, I'm going to show you how to build agent memory for your AI agents using just SQL. There's also a demo halfway through, so hopefully, you stick around, and let's get started. Before we get into TiDB, real quick, I want to talk about why agents are different. It's because they hit a database in completely different ways than the apps you've worked on before. There are three big things. First, agent workloads are bursty, right? One agent might be running out flat for 10 seconds, and then the other one might be sitting idle for two hours doing nothing, and your database has to handle both without costing you a lot of money.

**[0:54](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=54s)** Second is you're dealing with massive concurrency. It's not an app with a thousand users, but instead, you're running millions of agents at the same time and each with their own state. Third is constant context recall. Basically, every step the agent takes, it has to remember what just happened. Otherwise, the whole thing will fall apart. Those are the three things you can't really skip. Let me quickly show you what most teams end up doing today. Here's the situation. Let's say an agent finishes a chat with the user. The user comes back tomorrow, and the agent has no clue who the user is. It's like the conversation never happened.

**[1:45](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=105s)** To fix that, what most teams end up doing is they run three different databases plus a bunch of ETL pipelines, and that's their memory layer. You've got your regular database for storing chat history, user accounts, that kind of stuff, and that's the source of truth. Then on top of that, you have a vector database for semantic search so you can store embeddings of whatever the user said. On top of that, you have a search engine because vectors are bad at exact matches. If the user said a word like, let's say, "Tokyo," you want a keyword index to actually find that word, "Tokyo." Then there's the fourth piece nobody really talks about, which is the glue layer.

**[2:32](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=152s)** That's your ETL jobs, your message buses, the client jobs, something to keep all three of these things in sync, and your team has to write and maintain that code. So now, you've got three databases to run, three separate builds from three databases, and three things that can break. On top of that, your data is never really in sync, so it's just a lot. Now, look, if you're building just a regular application, you can kind of sort of live with this. It's annoying, but I guess you can deal with it. However, with agents, though, this stack breaks in a bunch of ways, and here's why. The first one is stale data.

**[3:20](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=200s)** Your vector index is always a few seconds behind your main database, so the agent ends up reading old data and old facts. Let's say a user updated their address an hour ago, but the agent is still using the old one. Then you've got the read-after-write problem. Say your agent just placed an order, and two seconds later, the user asks, "What is the status of my order?" and the agent says, "I don't see any orders." The write just happened, but the read side hasn't caught up yet. Then the third one is partial writes. Agent, let's say, does a multi-step thing, like processing a refund. It deducts the balance, logs the refund event, triggers some sort of an email. Now, midway through, the email service dies

**[4:10](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=250s)** so the balance shows that the refund was applied. The log says that it happened, but the user never got the email. Then the user calls the support, and support sees the logs and says it looks fine, so you're stuck explaining a ghost refund. The last one is a connection fan out, so for example, let's say you have 10,000 agents times the three systems is basically 30,000 connections you need to maintain and manage. Your connection pools can basically keep up with those connections, so your latency goes up when the traffic spikes, and you spend half of your time managing connections instead of building features. Look, this is all not just theory or hypothetical.

**[5:00](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=300s)** This stuff actually happens in production, and you only run into it once you're at scale, which is the worst possible time for it to happen. That's where TiDB comes into play. Real quick, in case you haven't heard of TiDB before, here's a quick summary. So first, it is a distributed SQL database, so it can scale horizontally across nodes, so no sharding, no rewrites. You just add nodes and capacity whenever you need it. Second, it is MySQL compatible. Any drivers you have, any ORM, any tools you're using with MySQL, it works with TiDB as well. Third is it has an HTAP and an AI engine, so transactions, analytics, vector search,

**[5:49](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=349s)** and full-text search all live in the same database. Fourth, it's used in production by many of our customers like Manus, Pinterest, Dify, and a lot of others. That's basically a quick overview of what TiDB is. Now let's go ahead and get into the capabilities. All right. Here's what TiDB gives your agents. The first three rows fix the three data problems that we just talked about, and the last two are extras that kind of just make your life easier when you're building agents. The first one is agent state and chat history. That's just normal SQL. Next up, we have semantic recall,

**[6:37](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=397s)** which is a vector column with an HLSW index. Next is keyword search, which is a full-text index with a multilingual parser, so it can handle English, Spanish, Japanese, whatever you throw at it. Then we have embeddings on insert, which is nice. There's actually a SQL function called, "embed underscore text," which basically you can give it some text and it will call the embedding model and it will store the vector for you in the table. The last one is hybrid retrieval, so you can run a vector search and on top of that, you can run a keyword search and then you can combine them with some sort of ranking algorithm. We're going to see all of this during the demo in just a second.

**[7:29](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=449s)** Now, just one more slide and then we'll get into the demo. This goes back to what I said at the start about agents having different needs from a database. The first thing you get from TiDB is you get scale to zero. If you have idle agents, they literally don't cost you anything. You're only paying for the requests you actually run so when your traffic is bursty, your bill is bursty too. Then you get database branching. You can spin up an isolated database per agent in just a few milliseconds. Every agent gets its own workspace, totally separated from everyone else. Third is resource control so you can cap how much each workload uses, so if one agent goes off the rail,

**[8:20](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=500s)** it doesn't take down everything else. The last one is fast scale out. Compute and storage are separated in TiDB, so when the traffic spikes, the database can add capacity in seconds instead of minutes. Okay, that's enough slides. Let me show you in the database. Okay. In Demo 1, we're going to create the memory table. Okay. Here we are in the SQL editor on a free TiDB cluster, and I'm going to run the whole demo on just one table. So up top, you see normal columns like a user ID, just a regular ID, content, a timestamp. The interesting one, however, is the embedding column.

**[9:09](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=549s)** It's a vector with 1,536 dimensions, and it is a generated column. Every time a row gets inserted, TiDB calls the function called embed underscore text, which is pointed at my Azure Open API deployment, and it generates the embedding and stores it, no Python, no pipeline. Plus, at the end, you also see there's a vector index for semantic search and a full text index for keyword search, both on the same table. As you can see, the table is created. The step #2 for the demo is inserting memories and seeing the data. Now, I'm going to drop the five memories for user ID 42.

**[9:59](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=599s)** As you can see, they are plain English strings, no embedding code in my script anywhere, but TiDB is calling the Azure Open API in the background to generate the embeddings. There they are, so you see five rows for "Jazz," "Vinyl," "Peanut Allergy," "Tokyo Flight," "Email Preference," and yeah, that's our data set that we're going to use for the rest of the demo. Step #3 is going to be semantic search. So here, the agent is asking, let's say, what does the user like to listen to? So notice, my question doesn't share a single keyword with anything in the database.

**[10:48](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=648s)** There's no listen, no like, just Jazz and Miles Davis, but as you can see, the jazz row comes back first, and you can see the distance is 0.49. That's the closest batch by meaning, so TiDB took my English question, embedded it, and ranked the rows by similarity, all in one SQL call. Step #4 is keyword search. Now, sometimes you want exact word matching instead, you know, so vectors are kind of bad at that. Here, we're using a full text search to check if the user mentioned a city, and once we execute the query, you can see there will be a row, the Tokyo row,

**[11:40](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=700s)** which is the exact match. Then you can also see the score of 1.34. The big thing here is this is the same table I just did vector search on, no separate engine, to keep everything in sync. Step #5 is hybrid search. So, okay, I guess this one really matters, so real hybrid search isn't just one query. It basically is two searches plus a ranking step on top, so what's happening here is the first common expression is running a vector search, grabbing the top 10 rows by meaning, and the second common table expression is running a keyword search, grabbing the top 10 by exact word match.

**[12:29](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=749s)** Then we're combining them using something called reciprocal rank fusion or RRF. The data is super simple. Rows that rank high in both lists basically win, so I'm asking what dietary restrictions the user has. The vector is looking for the meaning. Keyword is looking for the words like "allergy" and "peanut," and as you can see, the peanut allergy row comes first because it's scored well in both of these searches, the vector and the keyword search. One query, one database, no separate engines to keep everything in sync. The last one is going to be asset transactions across tables. So real agents, as we know, do multi-step writes that have

**[13:21](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=801s)** to land together, and there are two tables here. So there's a memory table you've been seeing, and there's also a separate user facts table where we track aggregate stats per user, like their trips and their memory count. Now, what's happening here is I'm wrapping a transaction around two writes, insert into memories, update the user facts table, and then commit. As you can see, the new memory is in the memories, and trip counters went from 0 to 1 and memory counter went from 0 to 1 as well. Both writes landed together, and if either one had failed, neither would have stuck. That's real distributed asset across multiple tables. Okay, so that was the whole demo.

**[14:09](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=849s)** Now let me close out with a few companies actually running TiDB in production. These are real numbers and not just benchmarks. The first one is Manus. They are an AI startup company, and every agent gets its own database spun up in milliseconds. Over a million and a half of these agents right now, and they moved over to TiDB and got to production in two weeks. Then we have Dify. They are an AI dev platform company and their backend used to be a 500,000 containers, and they moved all of it onto TiDB. Now they just have one engine that does everything, and then we also have Pinterest. I mean, they are not an AI company, but the problem they had was very similar.

**[14:57](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=897s)** They had six different databases systems doing different jobs. Now they'll have only one, which is TiDB, and TiDB is doing, basically, 1.3 million queries per second for Pinterest. Across all three, the story is basically the same. You have less stuff, more speed, and engineers building product instead of patching pipelines. Just a quick recap before I wrap up. With TiDB, you get auto-embeddings on inserts, no more Python pipelines. You get vector, full text search, and SQL all on the same table, so you've got one source of truth. You also get hybrid search the right way, two searches with RRF on top. The whole engine is built for how, actually,

**[15:47](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=947s)** agents run with branching, scale to zero, and resource control. The best part is you can spin up a free cluster in 30 seconds, and it can scale to millions of agents. All right. If you want to try this, here's where to go. You go to TiDB.com, which is the main one. You can spin up a free TiDB starter cluster, no credit card, and your cluster is going to be ready within 30 seconds. TiDB also has a native Azure Open AI integration, so you can very easily integrate your Azure deployment. For agent patterns and the customer stories I just talked about, you can go to pinkhat.com/ai/agenticai. Now, if you are a Python developer, we have a Python SDK,

**[16:37](https://www.youtube.com/watch?v=J0o-Dkt5tnI&t=997s)** which you can install by doing "pip install pytidb, and that gets you hybrid search and RRF in three lines. For cursor and Claude users, we do have an MCP server and a bunch of agent rules on github.com/pinkapp/ agentrules, so you can drop TiDB directly into your AI coding workflow. That's pretty much all I have, so thank you all so much for watching and go build something cool with TiDB and stop running three databases when you only need one.
