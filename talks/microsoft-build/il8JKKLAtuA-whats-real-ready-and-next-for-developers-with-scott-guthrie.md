---
id: il8JKKLAtuA
title: "What’s real, ready, and next for developers with Scott Guthrie | LIVE109"
slug: whats-real-ready-and-next-for-developers-with-scott-guthrie
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-04T13:56:51Z
video_id: il8JKKLAtuA
youtube_url: https://www.youtube.com/watch?v=il8JKKLAtuA
tags: ["LIVE109", "LIVE109_v1", "Scott Guthrie", "Seth Juarez", "What’s real ready and next for developers with Scott Guthrie | LIVE109", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# What’s real, ready, and next for developers with Scott Guthrie | LIVE109

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#LIVE109` `#LIVE109_v1` `#Scott Guthrie` `#Seth Juarez` `#What’s real ready and next for developers with Scott Guthrie | LIVE109` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=il8JKKLAtuA) · [Conference site](https://build.microsoft.com/)

## Description

There’s a lot of noise about AI. In this quick-paced fireside chat, get the builder’s perspective on what actually matters for developers. Drawing from how Microsoft runs a complete system from silicon to software at global scale, Scott breaks down the evolution across AI-ready infrastructure, context layers for agents, and what AI-assisted modernization means for developers.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Scott Guthrie
* Seth Juarez

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE109 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Scott Guthrie explains his role overseeing Azure and Microsoft Cloud Infrastructure
00:00:43 - Focus on building infrastructure to support the AI revolution
00:02:59 - Behind the scenes: Construction and operational scale of Azure data centers
00:04:25 - Challenge of doubling capacity every two years and preparing next-generation systems
00:06:22 - Use of Cosmos DB to enable regional scalability and eventual consistency
00:06:46 - Innovations for handling large-scale attachments via Blob storage and global state management
00:07:20 - Transition to Azure core and data services discussion
00:10:47 - Scaling Agentic Systems for Massive Workloads
00:11:18 - Architectural Challenges: Database Bottlenecks and Scalability

## Transcript

*2,715 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=il8JKKLAtuA&t=0s)** Hello my friends, and welcome back to BUILD. I am excited. I'm Seth Juarez. I'm here with my friend Scott Guthrie. How are you doing, my friend? Doing well, Seth. Fantastic. So are are you enjoying build? First of all, I am fantastic. So let's start first. I want to start because I want to get into this. What's top of mind for you, for developers as they're here and tell us what you do so people can know. They all know, but I want you to tell. Them sure. I mean so so you know what my job is is I run Azure and kind of the overall Microsoft cloud infrastructure. So everything that we showed today runs on top of that. So my team and I are kind of sort of involved in everything at the base level and then also all the data platform and several of the higher level services. And so you know, things that are top of mind for me are, you know, how do we keep building

**[0:48](https://www.youtube.com/watch?v=il8JKKLAtuA&t=48s)** out the infrastructure to support the AI revolution that's happening? So I spend an awful lot of time working on adding data centers and network and compute and storage to make all that possible. How do we do it more cost effectively? And so a lot of the innovations we talked about even today in the keynote around Azure Maya and Azure Cobalt in terms of our first party silicon, how do we take, you know, large percentage of the cost out of AI solutions? And then how do we enable AI that's rock solid, reliable, super fast, super performant and enables all the higher level tooling, whether it's get up, Copilot or other tools, Microsoft 365 and our overall ecintic solutions, you know, to be a platform that you can then build amazing AI solutions with.

**[1:37](https://www.youtube.com/watch?v=il8JKKLAtuA&t=97s)** So let's talk a little bit about the fundamentals, 'cause this is the cool part about Azure is that there's a ton of like operating system fundamentals. Can you give people a sense of the scale of this stuff? Like we have a ton of data centers, a ton of. Tell us about that. Yeah. I mean, I think in our earnings report, you know, we kind of quoted that we added over a GW of data centers in 90 days and, you know, gigawatts a lot, it's like the size of Seattle. And so it's, you know, we're, we're growing fast and we're doing it, as Satya talked about in the keynote, responsibly, our data centers are 0 water waste. So you know, they, they use less water than a restaurant does in an annual year. And you know, we, we invest very heavily in making sure the communities that we operate in, we're good stewards in terms of electricity prices, taxes, community engagement, because we

**[2:29](https://www.youtube.com/watch?v=il8JKKLAtuA&t=149s)** want to be long term members of the community. And, and to do that, we have to act responsibly. And then, you know, there's an awful lot of work involved to do this all reliably at scale on a consistent basis in 80 plus locations and countries around the world. That's the fun. You say that with like, there's a lot of tell us about the work involved because like these things, we just, we just have them turned on and we're super excited about it, but there's a lot of work that goes on to do that. Yeah, I mean, you, you need to get land, you need to get power, you need to get permitting. You know, in terms of the, the, you know, some of these sites have 6000 workers on them in terms of doing construction. It's, it's very precision tradecraft. You know, this is not just anyone can walk up.

**[3:20](https://www.youtube.com/watch?v=il8JKKLAtuA&t=200s)** You're talking about people with 510 years of experience in terms of electrical cooling and other construction things. So this, this is really tradecraft and you know, and you got to do it safely. And so we take safety incredibly importantly because at the end of the day, you know, the most, you know, we have signs that we put up on our job sites. The most important part of the day is you go home alive and safe. And, you know, and because this is high electrical equipment, this is heavy equipment, you kind of can't take that for granted. And, you know, thankfully we have one of the best safety records and again, one of the best environmental records in the industry. And, and we're kind of growing at scale. And then there's the software that goes with it. Yeah, of course. Because when you're you're growing at the rate we're growing, we're constantly having to change the network architecture, change the

**[4:09](https://www.youtube.com/watch?v=il8JKKLAtuA&t=249s)** storage architectures. You know, there's huge supply chain constraints in the world on memory, on SSDs, on hard drives. And so you, you're constantly also having to architect new ways of doing things to basically handle what is effectively a doubling of capacity every two years or so. And you know, generally in software, almost no software when it's handles 10X the scale works. And so you kind of if you're doubling every two years, you kind of need to be starting on the next generation almost immediately upon shipping the current generation because you'll be at that next generation very quickly. And that's, that's surprising because I, it's obviously something I haven't considered because of your doubling scale. Like everyone's built software on your website works great when like your mom looks at it or your dad, right?

**[4:57](https://www.youtube.com/watch?v=il8JKKLAtuA&t=297s)** But then all of a sudden when thousands and then hundreds of thousands and you have to change the way you think about how to architect the software on top of the core. So what are some? So what are some innovations that would be surprising to folks here and watching that maybe they hadn't said it needed to be done? Well, I think, I think one of the things and, and you know, we benefited with our partnership with Opening eye as an example with some of our data services and, and with Azure in general. But you know, as you think about just give it one example would be memory and chat history and authentication. You know, in a world where you've got an agent that's running all over the world, if all those agents have to go back to a single database at some point, your database will fall over.

**[5:46](https://www.youtube.com/watch?v=il8JKKLAtuA&t=346s)** You know, it, it just, it will not be able to scale to the load of a chat TPT or a Claude or a copilot. And so, you know, how do you architect your database layer so that you can scale, you know, linearly? And, and so a lot of the work we did in in Cosmos DB as an example, was to enable that where we can basically do a separate instance of Cosmos in every region, but then do eventual consistency of the chat history so that, you know, if any region has an issue, you, you just go seamlessly to the next region and away you go. But you don't have any synchronous locks anywhere. And, and that way you can replicate scale units, you can keep growing in a very natural way. And you know, that'd be like one example.

**[6:35](https://www.youtube.com/watch?v=il8JKKLAtuA&t=395s)** And then, you know, the trick would be like things like attachments when you upload something into ChatGPT, like if you store it in the database and everyone's uploading documents now and images, you know, that database gets really big. And so, you know, how do we do external attachments and spill over to BLOB storage where we effectively are doing like archival level costs, but at the same time having the ability to rate sequel against it and then having a globally replicated state store. You know that that type of thing is not easy. And and what makes it particularly not easy is when these apps are evolving constantly. You can't like take it down for a day to upgrade the schema. You kind of need to keep the plane running in the air while you swap out the engines, and that's part of the fun of running a live service. So I think that's a, this is a really good pivot because we kind of touched on it a little

**[7:25](https://www.youtube.com/watch?v=il8JKKLAtuA&t=445s)** bit, but a lot of the Azure core stuff is data and there's a lot of data products that we have in terms of like breadth and specificity and kinds. Can you talk about those a little bit? Yeah. I mean, we have, you know, I'd say broadly inside our Azure data services, three types of operational data services. Like 1 is our SQL family of products. And in particular, you know, we've kind of taken our traditional on Prem sequel and made it a great cloud native solution. And then with SQL Hyperscale, they're really enabling SAS based applications where you can have elastic pools so that you can maintain sort of a logical database per customer, but you're effectively running it on a a Paas service that's shared across customers. And you know, that's been great. Cosmos DB is our cloud native no SQL solution. And as I mentioned, Chachi BT and Copilot and Teams

**[8:15](https://www.youtube.com/watch?v=il8JKKLAtuA&t=495s)** and a whole bunch of other customers use that Adobe and others, it's really, really good for cloud native and especially Eugentic scale. And then one of the big services that we just went public preview on today is Horizon DB, which is our Postgres service that is really a cloud native Postgres that's designed to enable horizontal scale out and it's Postgres compatible. But is really enables a much, much larger scale Postgres database than what we've historically supported with our Postgres service in Azure, which was 100% compatible with Postgres. But because it's 100% compatible means that you're kind of scaling the traditional original database in a more A compatible, but at the same time scale limited way.

**[9:05](https://www.youtube.com/watch?v=il8JKKLAtuA&t=545s)** So Horizon DB, we're super excited about it has AI built in, as does Cosmos and SQL. And so it's, it's between those three, we've got a really good set of offerings. And then the big thing that we were really excited about is our fabric, Microsoft Fabric, which is our analytic stack. And that has what we call 1 Lake where you can store any type of data inclusive of data bricks and snowflake. Tables can be mounted in it in a zero copy kind of way, meaning it shows up, but you don't have to transfer data in and out. And then Fabric gives you kind of a data warehouse. It gives you streaming capabilities and a bunch more. And one of the things then we talked about today and is now GA is our Fabric IQ, which basically takes the semantic models of Power BI, takes all the data from Fabric or from data bricks and snowflake and

**[9:54](https://www.youtube.com/watch?v=il8JKKLAtuA&t=594s)** can surface it in Microsoft 365 Copilot. And so suddenly when people are asking questions in their inside their organization, we can leverage anything that's in Power BI dashboards or any of the semantic models or the data behind it to give much, much better answers. And you know, collectively that makes up sort of the Azure data services. Yeah. And it's quite expansive because you can choose between, you know, no sequel. You can choose from sequel, You can choose from Postgres if you want, but it's a special kind of Postgres that scales. Can you give us a sense of the kind of scale that you can get to with these services? Well, I mean in terms of storage perspective, you know, we had exabytes of storage per week now across Azure, right? And so it's it's a lot of data. I remember once amount of time a petabyte was considered a lot of data. Yeah. You know, an exabyte is a, you know, 1000 * a petabyte.

**[10:43](https://www.youtube.com/watch?v=il8JKKLAtuA&t=643s)** And you know, we're adding those, you know, multiple multiples of those week. And so you can scale these things to be really, really big, right. And you know, and again, part of the challenge of Agentic for all of us is when you have users that are hitting your apps, you know, the amount of database traffic you get on your app. When you have a web UI or a mobile UI and it's a user on the other end, you know, you might get 1000 requests. A second would be a very busy web app, right? You know, with agents, you know you will get to 1,000,000 of requests per second. Yes. And you know, I think one of the things that apps are starting to struggle with is as you start to have agents that go after things, you know, you can get very quickly 10/20/30 X the volume of API

**[11:33](https://www.youtube.com/watch?v=il8JKKLAtuA&t=693s)** requests that you historically did. And usually the first thing to buckle in your architecture is your relational database or your data system. And that's why it's going to be super important to have these services that can scale and have flexibility so that you can also adopt both relational and no sequel solutions, including the ability to globally replicate it and have local copies everywhere around the world for fast latency in order to handle that new workflow. And it's a good pivot because I think now we need to talk about how AI is changing everything. So what is different now? We have about two minutes tell us about how AI is changing, how fabric is helping with the IQ and the context the data tell us about. That I think with the, with the agents, I mean it's, it's, I mean fundamentally it's changing everything over the next couple years.

**[12:20](https://www.youtube.com/watch?v=il8JKKLAtuA&t=740s)** And in the same way that, you know, mobile app, you know, smartphone apps changed everything in terms of our consumer experience, the same way the web browser changed. So that we've had multiple of these waves. But you know, Agentic builds on everything that came before. And I think it's a new level of cognition capabilities that we historically didn't have inside our apps. And, you know, I think architecturally I kind of talked about data being key. You know, AI is only really good if you have got good data. AI with bad data kind of sucks or has bad decisions. And so how do you surface the data inside your organization? And that's where the IQ layer really comes into play. How do you scale that data so that your system doesn't fall over and that your costs don't explode is going to be key.

**[13:07](https://www.youtube.com/watch?v=il8JKKLAtuA&t=787s)** And then there's a whole bunch of other things at the infrastructure layer, you know, things like VM start time or the ability to run and bring up lots of machines quickly, ephemerally, because you want to have like, say a cloth sandbox, run something for a couple minutes, tear it down, and then immediately have a new one. You know, there's a bunch of architectural things both at the software layer that we're investing in. And then even things like Cobalt, which is our ARM 64 processor is much, much faster at bringing up machines. And you know, the whole memory architecture and the overall subsystem at the silicon layer is really optimized for these, you know, sometimes short lived agentic apps at scale and that are sandboxed. And you know, the things like MTC that we talked about today and Windows that we're adding is also going

**[13:56](https://www.youtube.com/watch?v=il8JKKLAtuA&t=836s)** to be key to that architecture. So I think with agents, it's not just about the AI. It really is going to be sort of a whole evolution of the way software, both operating systems, cloud infrastructure, dev tools, security, compliance, monitoring, AI OPS, like everything is going to change all at once. Well, thanks for editing on that. Everything's going to change. Thanks so much for being with us, my. Friend, it's going to be a fun ride. It's a fun. Ride, Thank you so much and we'll see you in a little bit. Thanks everyone.
