---
id: uA4ah-dVHvU
title: "AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard"
slug: ai-cut-our-research-time-from-7-days-to-15-minutes-gareth
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Gareth Yoder"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-21T08:00:37Z
video_id: uA4ah-dVHvU
url: https://www.youtube.com/watch?v=uA4ah-dVHvU
youtube_url: https://www.youtube.com/watch?v=uA4ah-dVHvU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Vanguard", "Gareth Yoder", "legacy modernization", "mainframe", "MCP", "AI for legacy code", "cash ledger", "data migration", "change data capture", "Kafka", "GraphQL", "fintech", "AIE NYC"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# AI Cut Our Research Time From 7 Days to 15 Minutes — Gareth Yoder, Vanguard

**Gareth Yoder**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Vanguard` `#Gareth Yoder` `#legacy modernization` `#mainframe` `#MCP` `#AI for legacy code` `#cash ledger` `#data migration` `#change data capture` `#Kafka` `#GraphQL` `#fintech` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=uA4ah-dVHvU) · [Conference site](https://www.ai.engineer/)

## Description

Gareth Yoder leads the cash program at Vanguard. He walks through modernizing a cash ledger that takes up to 30 million calls a day, running data, producer and consumer migrations in parallel. The turning point was exposing the legacy code base to AI tools through an MCP server. Research that took a mainframe engineer seven days dropped to 15 minutes. He closes with five lessons: make legacy code AI-queryable, treat migration docs as product, reimagine instead of lift-and-shift, adopt AI incrementally, and never skip observability.

Chapters:
- 00:00 Intro
- 01:10 What a cash ledger is
- 01:52 Three migrations in parallel
- 02:32 Legacy code over MCP: 7 days to 15 minutes
- 03:20 Data migration
- 04:12 Producer migration
- 06:38 Consumer migration
- 08:58 Onboarding 50 consumers
- 11:11 What we learned
- 13:12 Five takeaways

Gareth Yoder, Vanguard: https://investor.vanguard.com

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,146 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=1s)** [music] >> My name is Gareth Yoder. I'm the cash program technical lead here at Vanguard. I help oversee four to six teams in the cash program. This is no cash left behind, a Vanguard modernization journey. This journey really starts after we delivered our cash plus offering to our Vanguard brokerage account clients, and we launched that in 2022. And after we did the launch, we started to get the whispers that modernization is now coming down the pipeline, and that will be our next major project. How many here have legacy code bases?

**[0:51](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=51s)** Right? That's a lot of you. How many of you wish that legacy code base would just modernize? Right? Many of you would say the same. So, looking here at the journey, we're going to go through this timeline in today's presentation, but I want to first talk to you what a cash ledger actually is. A cash ledger involves all money movement transactions into our Vanguard brokerage accounts from the outside world. It also involves cash being moved between accounts. And so, the payment rails, think ACH, wires, and more. We support the web channels, mobile channels, and batch channels. Our system runs in an active-active multi-region fault-tolerant ecosystem. And our services will receive

**[1:40](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=100s)** upwards to 30 million calls per day. Our clients will generate a half million ledgers every day as well. And so, as we start to go down this modernization approach, we broke it down into three pillars: a data migration, a producer migration, and a consumer migration. But, because this was an enterprise priority, we had to do all three in parallel. So now as we look towards the research analysis, remember we're at the beginning of our timeline, the AI tooling wasn't there. And so, oftentimes we would work with mainframe engineers, and we would work with architects to try to determine what that data schema model would look like.

**[2:28](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=148s)** And there was a turning point in this modernization journey, and that's when we had our legacy codebase being available to our AI tooling via an MCP server. And now we saw faster feedback loops. What was taking 7 days for a mainframe engineer to go into the code, do their analysis, and then kind of and come back to us for an answer, now could all be done via an AI tool prompt. And what we saw was that the feedback loop was reduced from 7 days down to 15 minutes. It was a huge win for our product owners, our technical leads, and developers alike. They all contribute this tool to helping our modernization

**[3:18](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=198s)** succeed. So, let's talk about data modernization. We utilize the standard CDC change data capture approach that's common in industry, and we had to then scan both databases. A team did daily audits. We first made sure we had strong consistency by verifying the row level data counts, and then we ensured that we had strong integrity by checking the individual columns, making sure that the amounts matched from the legacy to the modern, making sure that the account information would match or the state withholding, the federal withholding. All of the attributes in the legacy database had to match to the to the cloud. A major tip here is that you don't want to over-engineer the solution because as

**[4:06](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=246s)** modernization would complete, this code would then get deprecated. Now, let's talk about producer migration. Our producers called our infrastructure in three ways from the legacy state. One was through a service request. The second was an API that wrapped that service request. And the last and probably the most daunting was direct table inserts because we would see data appear in our database and we weren't sure how it got there or who produced that data. So, we took that common data schema and we put it onto a gateway that wrapped our APIs that would do our cloud data inserts. Now, take your modernization journey as an opportunity to reimagine your data ecosystem. We took concepts from FinTechs such as

**[4:55](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=295s)** item potency. We also ensured that we had strong consistency across multiple writers. And so, we used utilized a similar paradigm to what a Snowflake ID would provide us. We are reimagined and we didn't do a lift and shift. Now, we have a modernized producer offering available. How do we get our producers? We had 35 producers that had to then modernize to our ecosystem. Early on, we had to produce manual documentation to facilitate this transition. And as the AI tooling became available, we provided that documentation in our company's wiki, but then exposed it via the MCP server. And that was really great because what

**[5:43](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=343s)** it did was we used to have many teams having chats with us, and we had to try to keep all of those organized. Now that communication and that back and forth could all be done via the prompt on the producer side, and we saw that the number of chats and and producer support that our team was doing was greatly reduced when we had the MCP available. The AI tools also did a really good job of transitioning state from the legacy ecosystem to the cloud. We made our cloud ecosystem, the ledger enums, to be human readable versus just ledger status codes in our legacy ecosystem. And so, our AI tooling did a really good job at bridging the gap of the intent

**[6:32](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=392s)** from the legacy ecosystem to the cloud. So now let's look at the consumer migration path. We had three ways to access consumer level data. We had real-time use cases, batch use cases, and streaming use cases. And the commonality here is that we provided a schema registry, no matter which channel that your uh consumer would access that data. And so, for a funds available, that's our most that's our most uh heavy traffic uh real-time API, and that goes into determining what is the balance that's displayed on your account. They're going to be calling us via GraphQL, and they're going to subscribe to only

**[7:21](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=441s)** the attributes that meet their use cases. Now, for batch use cases, think of reconciliation or data analytics. We have our data warehouse that will expose data share views to each individual consumer. Each of the consumers tells us their use case, and we provide a a view that's specific to their data needs. This This was supported by our data governance team that strongly advocated that only the consumers that need the certain data attributes, they should only see uh those pieces of data. Our last piece was around streaming. We have a Kafka event topic that we would stream all of the inserts and updates to that database. Our fraud teams were able to take

**[8:08](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=488s)** take advantage of this technology to provide real-time data ingestion into their fraud tooling. We provided at least once delivery. And so, our concepts of item potency that we did through the producer side, we carried forward through the event streaming. And so, as they subscribe to at least once delivery, we made sure that they had item potent safe uh operations. So, that if a batch job would would fail halfway through the process, those teams could retry, and we can ensure that we don't have uh duplicate ledgers being created. But, the at least once delivery from the eventing side ensured that they had all of the ledger events that were created. Now, when we onboarded consumers, we had

**[9:00](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=540s)** 50 different consumers across our organization that needed our data. At Vanguard, when you onboard an application, you need to have a three-character application code to register to onboard. This application code describes what your application is and and what it performs. But, we took it a step further. We requested that our consumers would provide us a description and a business case justification for their need for the data. And so, think about if I am a trade order that needs a cash ledger to fill fulfill the cash obligation of the trade, that could be a business use case. Or for a retirement account that

**[9:47](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=587s)** needs to do a a required mandatory distribution. A 529 account could do a contribution to their college tuition account. By grouping together all of these business descriptions, now the AI tooling can compile that together and provide an accurate description of what use cases have been modernized in our ecosystem, as well as we now have what is the top business functionality that we support. We can also take it a step further by asking what is the impact if our SLAs are breached. And this is critical because if you're in a major incident and if we see an app code that starts to go

**[10:35](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=635s)** go below the five nines of availability, we can go in and we can see, okay, a batch application we may have hours to respond. A real-time API where there's a client on the other side that's receiving errors, we have minutes and time is of the essence to self-heal. We're continuing to evaluate how we can get faster response times by combining the business use case justification into our observability and and log traces. So what we've learned, we've learned that although we started this journey before the AI tooling was even available, we adapted and continued to adopt the

**[11:24](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=684s)** newer technologies. This greatly aided in our research, in our development, and our testing. Today our cash program, 90% of our engineers utilize these AI tools on a daily basis. Our teams use multi-agent workflows, and we have shared knowledge bases. We're continuing to evolve this AI harness to meet our modernization demand. We have the concept of a team brain that as engineers are are building out product features, that knowledge goes into a common storage where it's now accessible by all members on the team. And if there's an engineer that has just joined, they can tap into this common knowledge base, and now they have the

**[12:12](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=732s)** same context in their prompt as an engineer that has been here for the last 5 years. Now, when you're in a modernization process, maintaining two code bases is challenging. And what you'll want to do is you'll want to continue to fix forward. Don't fix the past. As you encounter bugs that have may have listed have existed for decades, continue to fix the modernized state and allow that to be the incentive for your producers and your consumers to modernize to the cloud. Now, this will throw off your audit logs, so you'll want to have white listing available, and that's really critical.

**[13:01](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=781s)** And the last piece is ensure that you have the right metrics, alarms, and traceability, because you're going to review those often as your product continues to grow. Now, because this is a leadership track, I want to call out five main points. Number one was make your knowledge make your legacy code base AI queryable. That exposing that via an MCP server, our legacy code base it cut that research cycle time and gave quicker feedback loops. That's 7 days down to 15 minutes. That was a huge win. Treat your migration docs as part of your product. It needs to your migration docs are just as in critical as your business functionality because that's what all of your producers are going to utilize to

**[13:49](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=829s)** onboard to your application. Eventually, yes, those will get deprecated out but for that interim process those migration docs are critical. Reimagine and don't lift and shift is is the third point. The consumers and producers that we had the most trouble onboarding to our modernized state were the ones that wanted to do a direct lift and shift transfer of old to new versus those that took a moment to step back and say, "How could we better evolve our product by taking advantage of the modern capabilities that the cash ledger ecosystem provides?" The fourth component is adopt AI

**[14:38](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=878s)** incrementally. As the AI tools arrived, you continue to enhance your product. There's never going to be a perfect starting point in the world that we live in today. The important thing is that you get started and you continue to enhance and adapt as the technology changes. Last piece is observability is non-negotiable. You need to know who's producing your data and who's consuming your data. And this is ever more important as your product goes to BAU and once the modernization is complete, your teams will now have to support this as their uh daily operations. Thank you very much, all. If we have time, we'll take questions.

**[15:26](https://www.youtube.com/watch?v=uA4ah-dVHvU&t=926s)** Otherwise, I'll be outside of the room. You can connect with me later. And thank you again for the opportunity. >> [applause]
