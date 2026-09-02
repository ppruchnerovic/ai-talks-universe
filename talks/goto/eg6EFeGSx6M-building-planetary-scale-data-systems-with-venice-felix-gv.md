---
id: eg6EFeGSx6M
title: "Building Planetary-Scale Data Systems with Venice • Felix GV & Olimpiu Pop • GOTO 2026"
slug: building-planetary-scale-data-systems-with-venice-felix-gv
conference: goto
conference_name: "GOTO Conferences"
category: "Software dev with AI tracks"
edition: "GOTO"
year: 2026
speakers: []
channel: "GOTO Conferences"
duration_min: 28
published_at: 2026-01-26T13:01:15Z
video_id: eg6EFeGSx6M
url: https://www.youtube.com/watch?v=eg6EFeGSx6M
youtube_url: https://www.youtube.com/watch?v=eg6EFeGSx6M
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTO Unscripted", "Felix GV", "Olimpiu Pop", "VeniceDB", "RocksDB", "DuckDB", "Apache Kafka", "Apache Pinot", "Apache Zookeeper", "Apache Helix", "Data Flow", "Chaos Engineering", "Data Systems", "Apache Iceberg", "CAP Theorem", "Microservices", "Distributed Systems"]
topics: ["Classic ML & data science", "Data engineering & MLOps"]
transcript: true
---

# Building Planetary-Scale Data Systems with Venice • Felix GV & Olimpiu Pop • GOTO 2026

**Speaker not identified**

`GOTO Conferences` · `GOTO` · `2026` · `28 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTO Unscripted` `#Felix GV` `#Olimpiu Pop` `#VeniceDB` `#RocksDB` `#DuckDB` `#Apache Kafka` `#Apache Pinot` `#Apache Zookeeper` `#Apache Helix` `#Data Flow` `#Chaos Engineering` `#Data Systems` `#Apache Iceberg` `#CAP Theorem` `#Microservices` `#Distributed Systems`

[Watch the recording](https://www.youtube.com/watch?v=eg6EFeGSx6M) · [Conference site](https://gotopia.tech/)

## Description

This interview was recorded for GOTO Unscripted. #GOTOcon #GOTOunscripted

Félix GV - Current Interests: Multi-Planetary Databases, Data Sovereignty & Lifelogging @felixgv @VeniceDB
Olimpiu Pop - Technologist & Tech Journalist

RESOURCES
Félix

Olimpiu

Links

DESCRIPTION
Félix GV, a former engineer at LinkedIn and architect of the Venice database system, discusses the complexity of building planetary-scale data systems. He explains Venice's unbundled architecture where each component—from Kafka-based pub/sub to RocksDB-powered servers—operates as an independent distributed system. Félix details their rigorous chaos engineering practices, including regular load tests that push data centers beyond normal capacity to ensure reliability.

The discussion covers fundamental distributed systems concepts like the CAP theorem and the trade-offs between consistency and availability in multi-region deployments. He also explains why Venice, as a derived data system, deliberately sacrifices strong consistency for high throughput and availability, and concludes by discussing their experimental integration of DuckDB for SQL-based analytics and data exploration capabilities.

TIMECODES
00:00 Intro
00:55 The architecture of Venice: An unbundled database
06:09 Multi-region reliability & chaos engineering
09:54 Data flow: Writing & reading in Venice
15:15 Understanding the CAP Theorem
22:34 Integrating DuckDB: Adding SQL capabilities
27:31 Outro

RECOMMENDED BOOKS
Kasun Indrasiri & Danesh Kuruppu • gRPC: Up and Running • https://amzn.to/3sBGBJJ
Tomer Shiran, Jason Hughes & Alex Merced • Apache Iceberg: The Definitive Guide • https://amzn.to/488Z30k
William Smith • Arrow Flight Protocols and Practices • https://amzn.to/4o2Q2fd
Adi Polak • Scaling Machine Learning with Spark • https://amzn.to/3N9vx1H
Mark Needham, Michael Hunger & Michael Simons • DuckDB in Action • https://amzn.to/45QwSli
Simon Aubury & Ned Letcher • Getting Started with DuckDB • https://amzn.to/3VPk4q

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,114 words · source: supa (en, exact timings)*

**[0:13](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=13s)** Hello everybody. I am Olympop curious technologist and welcome to go transcripted. Today we have Phelix in front of us. He is one of the rock stars in my opinion in the data space. He he built planetary scale data systems and it's will about to dive into his experience and see what we can we can learn from his knowledge. Felix, please introduce yourself. >> Hi Olymp, it's great to talk to you again. Always fun to have a conversation with you. I see what you're up to and yeah, happy to see where that that one takes us. >> Yeah. So last time when we we spoke a couple of months ago, you were tinkering

**[1:02](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=62s)** with replacing Rox DB as the core the engine of the the data system that you you and your colleagues put together with DB. But before before we go there, let me provide more more context. you you were in the team that put together the der derived data database actually from uh from LinkedIn. So more or less it's the data that is the place where the data is stored about the recommendations if I remember correctly and so on so forth right >> yeah that's right >> maybe if if we do like a cut through it what are what will be the the main pieces if we are looking like to abstract away a data inester and then

**[1:52](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=112s)** how how will the this data system look like >> yeah yeah so uh venice the system that I have been working on for the past decade up until recently. I left LinkedIn a month ago, but it was a distributed database which we could say was part of the category of databases that we call unbundled. So that means each piece of the database is kind of a a separate standalone component in a sense, right? So one big part of the database was Kafka actually internally we were in the process of replacing it with something else but we can say it's just a pub sub right but I'm saying Kafka as that is

**[2:41](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=161s)** what people are familiar with and that was our write ahead log component and also our commit log or replication log between the replicas right and then we had servers which internally were made up of essentially a a Java process that had a Rox DB database locally and then it could serve requests across the network but it could also do certain computations inside uh of the server itself and then there was a kind of a whole ecosystem of clients around it like various client options for accessing the data. So you had a client that could send requests across the network to the servers like kind of a typical client

**[3:29](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=209s)** server architecture as we usually have. But then there was also another client which had the same API as the the remote query client, but instead internally it was actually embedding the Rox DB database and it could pull data directly into the application process. We call that pattern the eager cache because it would eagerly load the data ahead of time. And essentially that means your client application became as if it were another follower replica of the database, right? So you could set it up that way and then get even better performance. Of course, there is a resource cost, right? Nothing is free like you you would have the data

**[4:18](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=258s)** in your local RAM or or local SSD if that's available. So that's why it's faster. Uh but it also costs more to set it up this way. And there were some other clients like you could listen to the the change capture stream internally. We had an ETL component to ship data to the grid. That part is not open source though. Everything else I mentioned before is open source. Yeah. So that's kind of the the high level architecture. And then of course there's a separate control plane uh apart from all of that that decides on all of the metadata stuff, the partition placement, all that all that stuff. and it uses Zookeeper and Apache Helix. So that's kind of the very high level view of the database and circling back

**[5:09](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=309s)** to the beginning I said it follows the unbundled database pattern essentially what I mean is like each of the component that I mentioned is a distributed system right so the write ahead log let's say is Kafka well that's a distributed system right there the server fleet we had like let's say I don't know a thousand servers per region or something like that those are well they were split across several clusters. Each of those are a full distributed system. The control plane itself is distributed of course for reliability and the clients obviously are distributed like you know we don't run applications that that are just single instance right they are they are usually maybe an order of magnitude more clients than uh databases or sometimes two

**[5:57](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=357s)** orders of magnitude more. So every every single piece basically is a distributed system. So that's kind of the the highle architecture there. >> Okay. Well, it's spinning in my head a joke, but I had to just drop it because now given that while we are recording there is another part of the infrastructure internet infrastructure outage cloud flare is is out. So a lot of the the its customers are back. So did you really have multiszone? Well, you don't have to answer that. >> Yeah. Yeah. >> Yeah, we did. >> Great. Great. >> Yeah. And we we exercised it very frequently. Well, it's sort of like the chaos monkey pattern, right, that Netflix popularized.

**[6:46](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=406s)** We we essentially did what we called load tests uh several times a week where we would fail out traffic out of data centers and and concentrate the traffic into a single data center. Not all of the traffic but but like let's say quite a bit like we were running in three data centers and we were in a normal outage scenario we would like essentially fail out of one data center which means there are two left right and so each one needs to support more than 50% of its normal load right that would be the the normal failure handling scenario but during those load tests we would concentrate it even more than that so we would drain traffic out of essentially one full data center plus a little bit of the other.

**[7:35](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=455s)** Roughly speaking, right? It's not exactly like that, but like in the aggregate, that's what it looks like. Meaning that the the data center under test would get even more than 50% of its peak traffic. And we would do that in the morning, which is when like we in the weekday mornings, which is when we have our peak traffic, >> okay, >> regularly, right? So we would pick the time of day that had the highest traffic and concentrate traffic on a single data center and and we would regularly test that we can still sustain the load and we can sustain the the load even of the next stage of growth right that we anticipate. >> Okay. >> Inevitably we would discover that one or one system or the other doesn't actually sustain. It was very rarely Venice but

**[8:23](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=503s)** sometimes it was. And then that's a bad place to be when you are the when you're designated as the team which is the low test blocker. Then all eyes are on you and you really have to fix it quickly. So so yeah the that's definitely something we we exercised because you know having reliability mechanisms that you do not regularly test basically means you don't have reliability mechanisms right because by the time you need them they they're not going to work anymore. >> Okay. Great. Thank you for sharing. So what the he is saying is that okay there are a handful of components. First of all it was the popsup part which was distributed but actually all all of the parts were distributed and then the popsup was used also as a replication

**[9:11](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=551s)** mechanism but also in order to among nodes but also in order to [clears throat] save the data. Uh and then there were multiple other I will not just name them because I'll just probably miss some of them. >> In order to ensure that the data is properly kept and actually used, you had weekly tests of low test using the chaos monkey pattern that was made well known by by Netflix. Well, I think the technical term for this is called playing with fire. And I'm happy that to hear that somebody's doing it to make sure that things are actually actually okay just to fully understand what they I don't know let's say probably it's not

**[10:01](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=601s)** something that is used in practice but let's say we have to place in uh in Venice or using this system we have to put in place a new a new record based on our previous conversation I know that usually you it the derived data it wasn't data that was generated by the humans so there was mostly about machines but then if we just imagine that we would like to store something in what would be the normal flow of writing and then reading it to just have a full picture of how the information is flowing from one side to another >> yeah good question Venice is a little bit different than many other data systems in that regard so that that's a very good question to lean into Venice we can say is a derived data

**[10:49](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=649s)** system which means the data it hosts has been machine generated you could say rather than userenerated that's not a hard rule you could put userenerated data in it if you wanted it's just not as well suited for that and Venice is not alone there are many derived data systems like for example Apache Pino is another derived data system The pattern that we see in general with derived data systems is that their right path the way that you write into the system is typically asynchronous. So that means the data gets loaded from a pub like CFKA or maybe it gets loaded from a dump of files that were generated

**[11:43](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=703s)** offline like in some sort of job like maybe a daily job or hourly job or weekly job. So it's either batch ingestion or stream ingestion and sometimes it's both right. So in in Venice we supported all permutations of these various derived data ingestion modes. So you could have your data come fully from a stream processor for example or you could have it come from a batch processor or you could do both. You could have the data come once a day from a batch processor but then in between the batch pushes you would have a stream processor that's refreshing it as well. And and then there's a a bunch of different variants of that, right? Like you could say the stream processor

**[12:32](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=752s)** refreshes just a subset of the columns of the table and the rest are the rest of the columns are batch only stuff like that. Venice would orchestrate all of these data ingestion scenarios out of the box. The key thing to remember is that because the data comes in asynchronously, it comes in through a pub sub, it can support very high ingestion throughput. But in exchange, again, you know, we talk about trade-offs. This this is what data systems are all about. The tradeoff in this case is that because you're writing asynchronously to the system, you lose strong consistency, right? Or the the technical term would be linearizability,

**[13:20](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=800s)** right? So that means you another way to that we say it uh sometimes is read your own rights. So you you do a right operation to the system. You can get an acknowledgement that the the right is durable right you have attained durability but the durability is only the durability provided by the right ahead log which is Kafka at that point the data is not yet indexed into the system it's not yet readable. So, so that's the the design decision we made there and and like I said, Venice is not unique like other systems work similarly like Apache Pino is is pretty similar to that also. So, so it's not fully unique but it's it's still a little bit

**[14:09](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=849s)** uncommon right like because in a traditional database like let's say like Postgress you also have a write ahead log but the write ahead log is embedded inside of the Postgress process and then the acknowledgement that you get when you do a write request let's say you do an insert or an update the acknowledgement you get is after the data was persisted to write a headlog for durability but also after Postgress updated all of its in-memory indices. Right? So when you write to Postgress you do get read your own right guarantees. you do get linearizability because Postgress has been designed to cater to primary data use cases and in

**[14:59](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=899s)** primary data typically you do want to have that type of consistency guarantee right so that's the nuance between derived data and primary data I would say okay or one of the nuances at least >> the the thing that is spinning in my head is a theorem that almost never I understood it. So I usually have like 5 to 10 minutes when I understand it and then I forget about it and that's the category and that's probably the the first three letters that are very important in distributed systems. The main the main reason for for that is that you have to choose two of the three letters usually when designing a distributed system and yeah how what would be the

**[15:48](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=948s)** permutations of this? How would they look from your point of view when dealing with data? Because data is sensible and it has gravity and when you're talking about global scale, you spoke about having multiple data centers. So how do you make sure that um a long time ago two to three years ago I was just very surprised by the way how the data was replicated in case of Amazon I had an order in one browser I can see the order on my phone I couldn't see it and then a different browser I I got a big it depends on that so [clears throat] and that was the that's the example that usually have with with captur how did you looked at that when look at

**[16:37](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=997s)** it practically because you can't play with those things like that, >> right? So the cap theorem basically says there are three properties we care for. consistency which in in in what we were discussing earlier in that context means uh read your own rights or linearizability right that that's what consistency means in the CAP theorem avoidability and the P stands for partition tolerance but there's a catch in the CAP theorem it says pick two out of three but one of the two you pick must be partition tolerance so then the only real choices you have are CP or AP right consistent and partition tolerant or available in partition

**[17:26](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1046s)** tolerant that's what the theorem says now in practice the partition tolerance the partition tolerance here means a network partition so that means you are cut off from the database or maybe the distributed database itself has some of its replicas cut from the others or some kind of scenario like that where some machine is unable to contact another machine basically right that's what partition tolerance means is how do you deal with that this comes up during failure scenarios right which means if you do not have a network partition also called a a net split if you do not have a net split

**[18:15](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1095s)** then you could have a system that offers both the A and the P, right? It could be a the A and the C. I it could be avoidable and consistent while there are no failures, right? Then when the failure occurs, you you have to sacrifice one or the other. in terms of Venice and and I would say probably derive data systems in general, there is maybe a a different way to think about it which is well those systems are certainly highly abidable, right? So they are AP in that sense but because the design choices that we explored earlier have made it so that our right path is asynchronous and we've

**[19:06](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1146s)** sacrificed uh strong consistency and linearizability from the get-go. Right? We've already sacrificed this like at the drawing board level. It's not a matter of suffering a network partition that makes us lose consistency. It's it's almost as if we were continuously network partitioned in a sense, right? It's not like quite the same, but it it's almost like that in the sense that it's almost as if the network route through which your packets must be transmitted for all of your write requests, that path always has a high latency, right?

**[19:54](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1194s)** And so in a sense it's as if from the point of view of a traditional database it's as if that functionality is continuously degraded. So you never have consistency. Um you this the C in the cat theorem is lost like continuously. Interestingly at least it's interesting to me I don't know about others but interestingly this does not only apply to derived data systems. It can also apply to primary data systems that are multi- region and architected in a way to be multile, right? And I think that's probably what you've experienced with the Amazon shopping cart example that you gave. It could be that your laptop is connected to one uh data center let's say US East one or whatever and then

**[20:42](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1242s)** your phone for some reason is going to another data center like maybe it's connecting to Europe and like for some reason you're you know going across the Atlantic with your laptop and you're connecting locally with your phone right to a closer data center let's say assuming you're in Europe right and so there is also replication going in both directions between these data centers, but it's asynchronous. So it could be that you add something to your shopping cart over here and it's not yet replicated over there, right? And so for those scenarios where you have a multiler replicated system, you also are in a sense in a situation where you have continuous highlight latency between the regions.

**[21:32](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1292s)** So that that can be an interesting kind of design tradeoff. Obviously you get great reliability characteristics from being present in multiple regions that improves your availability profile but it does mean you're sacrificing consistency and not just during outages you're sacrificing it continuously. >> Yeah. So we has to choose our poison wisely and see exactly what's what's actually the the important part. Okay. Thank you. Thank you for uh for the explanation. So given that we are looking at at most half an hour conversation half of this conversation I understood the captorum as I told you that my my span of remembering the captorum

**[22:22](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1342s)** explanation is like at most a quarter of an hour. So, thank you for that, Felix. It's nice >> you'll remember it for for another five minutes after [clears throat] we're done. [laughter] >> Yeah, thank you. A last question for me is one one thing that I failed to ask you last time is you you spoke about the two choices of having the two different engines that you you and your team had implemented and I know during the hackathon I think you chose to give it a try and rather than using Rox DB try to use bugs DB. Now if you look at them they are a bit different but the first one is a key value pad and the other one is an SQL engine to just oversimplify things

**[23:11](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1391s)** given that you're talking about mostly machine generated data and you're talking about huge quantities as you mentioned batch processing and even stream why would you need SQL? >> Yeah it's a good question. So, so you're right that this was integrated in a hackathon project. So, in a sense, it was a way to test if our abstractions were flexible enough and and so on. Kind of a theoretical experiment in a sense in terms of and it did work like we were able to get the Venice data into duck DB instances that we could then query with arbitrary SQL. In terms of real world scenarios, I I don't think we've used it in any real production use case yet. It

**[24:00](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1440s)** is available there in open source if people want to try it out. The the Venice DuckDB DB integration, but Duck DB is an incredibly flexible system, right? It has it's a very impressive project. Every time I've worked with it, I I really enjoyed it. Um, it has a bunch of different extensions, so you can do many many things with it, including you can even do some vector type work like search and and and stuff like that. And these are things that could be interesting from the Venice point of view like Venice already has a little bit of built-in vector math kind of computation so that uh we can make those workloads more efficient. Uh but it's a little bit basic, right? Like we

**[24:49](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1489s)** developed this before the big wave of like vector databases that have exploded on the scene in the past five years. We had vector math uh running in the in the Venice servers since maybe 2019, I want to say. I I think that's right. So a little bit before the the rest of the industry kind of got on that bandwagon. But uh but we also did not really update it much since then. So it's a little bit earlier but a little bit more primitive in terms of scope of capabilities by bringing in ducks DB. Now we have like all of these extensions that we could kind of pull into the mix uh for free so to speak. Nothing's ever free like there's always a trade-off but

**[25:37](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1537s)** for free between quotes, right? So, so that's one motivation. Another motivation we had was just like data exploration and debugging and stuff like that. Like sometimes you want to understand like what is the shape of your data like what is the cardality of values in a given column. Regularly we had some internal users that were asking us like hey look my my Venice data is populated by the stream processors. I I should know what's in there, but now I have a doubt like maybe it's not quite what I expected that's going in there. And then they would ask us to like turn on the ETL so that the data gets loaded out of Venice and into the the grid and then they would use

**[26:25](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1585s)** like offline tools like Spark or whatever to query that. So it all of that workflow worked but it was a little tedious like high inertia and this is one more option right where you could if the data set is small enough or or if you if you could get the answer you need out of just one partition of your data set let's say you could uh load that into duck DB and then run queries like very fast and then get the answers you need about like you know what is let's say what's the max value in that column or uh like those kinds of aggregation queries that duct DB does very fast. So these were kind of the initial use cases we were thinking of, but like I said, DuckDB is so flexible that there's probably a lot more that I'm not even

**[27:13](https://www.youtube.com/watch?v=eg6EFeGSx6M&t=1633s)** thinking of, but we'll see. Yeah, pretty much it's it meets the the reasoning in my head that was more like a some kind of analytics and some kind of just just taking of data. So, okay, thank you for sharing and thank you for taking the time to to have yet another conversation. >> Yeah, my pleasure, Olympia. It's always fun chatting with you. [bell]
