---
id: z01r8DYsY0I
title: "Trillion is the New Billion: Managing Really Large Multimodal Datasets for AI | LanceDB"
slug: trillion-is-the-new-billion-managing-really-large
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 14
published_at: 2026-06-17T22:34:53Z
video_id: z01r8DYsY0I
url: https://www.youtube.com/watch?v=z01r8DYsY0I
youtube_url: https://www.youtube.com/watch?v=z01r8DYsY0I
tags: ["AI"]
topics: ["Multimodal, vision, speech & robotics"]
transcript: true
---

# Trillion is the New Billion: Managing Really Large Multimodal Datasets for AI | LanceDB

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `14 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=z01r8DYsY0I) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 2 - AI ENGINEERING] Most AI problems are really data problems. AI workloads bring with them ever larger amounts of data from multiple modalities (e.g., text, images, audio, video, sensor data). If you were indexing say, the internet, you need to solve a number of new data infra challenges:

1. Storing large blobs and avoiding copying them over and over during processing
2. Dealing with much larger table sizes: trillion rows with a capital T
3. Supporting workloads like Search, Curation, and Training directly from your dataset instead of having to move data to/from point-solution systems
4. Dealing with *really* distributed pipelines: what happens when your storage, CPUs, and GPUs are with different clouds / vendors?

In this talk we will dive into detail on why it's challenging to manage trillion scale wide tables with multimodal data. We'll see why existing data infra doesn't support new these data types, workloads, or scale. And we'll do a quick under the hood peek at how Lance format and LanceDB solves these problems at a foundational level. Zooming out, we'll cover how LanceDB fits into the existing data stack alongside Iceberg. Finally, we'll talk through our roadmap and show you the big improvements we're working on in 2026.

Whether you're looking to do large scale search or building the next frontier model, this will help you scale easier, get to production faster, and save on infra cost.

SPEAKER:
Lei Xu - Co-founder & CTO, LanceDB

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,948 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=z01r8DYsY0I&t=0s)** clustered well clustered well balanced cluster for for your training data down the line and we have another data engineering team is building features then making copy of this data and explore the feature distribution within within this team itself. So each of these stage actually using uh using different uh tools and generate different copy of the data and especially for those smaller uh new uh smaller frontier labs that only have 20 PhD just graduated from last year. They actually want to spend most of time work on the models instead of go through this pipeline using five or 10 different tools, right? and basically managed Yam Yami and Kubernetes by themsel and that's where actually slow down uh slow

**[0:49](https://www.youtube.com/watch?v=z01r8DYsY0I&t=49s)** down the model development uh very significantly. So what how how do we approach this differently from from the existing infrastructure right? So we try to see basically the first principle we want to see is how many different states we want to do uh to cover end to end of AI development uh cycles and within this cycle what kind of a different uh workload we need to support and by summarize that we see we only need have two types of uh uh basically we just need to support two to three types of workload then we can cover each individual uh steps within the full uh development cycles, right? Then uh

**[1:38](https://www.youtube.com/watch?v=z01r8DYsY0I&t=98s)** convert that we we basically support very fast uh run rate so that you can just put you can put different content within context and within its derived features within the same single data infrastructures to support from search from training from scan and different types of uh workload. And we can store either very large um blobs of data and very small of booings and index within within the same data set. So you don't need to join a JPEG files from S3 to your packet file from say iceberg table covered by snowflake then covered by another record database somewhere else and from the application level to join join the result all together. Right? And

**[2:26](https://www.youtube.com/watch?v=z01r8DYsY0I&t=146s)** the other thing that we do very differently uh within the market we support um zero cost um data evolutions means that every time when you adding a new features uh within say like 50 pabytes of table you don't need to actually override this which become a giant like spark job to copy one data to another silo place adding one columns and other than this single person No one else know where the how how this data is generated, right? We can have multiple AI engineers work on the same same table. Each of them uh incrementally adding new features to the same table and the the feature will immediately to become searchable and

**[3:14](https://www.youtube.com/watch?v=z01r8DYsY0I&t=194s)** indexable within the data set. And for us because we support uh all the data within Nest DB is immutable these people start to building versions and the lineage on top of it. We can easy to understand that within each commits where who is the uh producer of the data which give commits is to generate this piece of data and once you see anything um wrong with the data you can go back to find the author or the owner that can uh debug those data. By the end of the day, we want to make one single system to break silos so that um customers or users or researchers can iterate within

**[4:04](https://www.youtube.com/watch?v=z01r8DYsY0I&t=244s)** the same infrastructure through the stage of AI development and like uh improve the velocity for for them to discovery between uh the problem between each stages, right? Even we have great vision in the beginning, things still break through the years, right? And we have worked through many different uh I guess at different scale targets for us to go through uh go through this three for years. Right now we we are at very high higher um scale numbers that we can deliver uh like over 100 thousands of QPS over tens of billions single uh billions of rows

**[4:52](https://www.youtube.com/watch?v=z01r8DYsY0I&t=292s)** within single table. However, we see this happens over and over again within I mean from from existing uh infrastructure that support last generation of a workload especially from like big data when you the majority of your workload is scanned over the data and try to aggregate data. This is very different from uh what we we have seen from our customers, right? from our customers. We we uh a lot of for example for for robotic or or self-driving cars. We want to interactively to slice dicing over my data data set and want to see within each time stamp from different five streams of lighter data, sensor data or your uh or your position data and we want to make sense of those data

**[5:41](https://www.youtube.com/watch?v=z01r8DYsY0I&t=341s)** all together. This needs being need need index from different uh modality of of the data and have a very fast uh like uh search and slice ding capabilities into this system. It's very hard to build once you have more than say 25 50 billion of rows from the iceberg today. Right? And other than that um the when you have 100 engineers AI uh engineers or AI researchers work on the same data we actually want to know who built these columns who generated that features right and why these features ph uh have different distribution from the the other features right this government

**[6:29](https://www.youtube.com/watch?v=z01r8DYsY0I&t=389s)** uh government's features that need to support a industry scale of AI labs to work uh very efficiently all together, collaborate all together between each a researchers is become uh become way more severe than those new grads realized after they just directly jumped from the PhD u program. And other than that um especially from beginning of this year we see many of our customers actually throwing um thousands of agent to to make make sense or or to try to understand this data set 247 right it's not like your engine researcher have 9 to5 uh work days all

**[7:20](https://www.youtube.com/watch?v=z01r8DYsY0I&t=440s)** the peak traffic come from this morning this this just a have unbound on the number of agent is continuously uh running large scale of uh search and debugging and evaluation on top of your data set. Right? Those uh all basically stretch our uh system in very different ways and also it's um improve help us to improve the cost efficiency to support like um this large scale large volume of search very differently and by the end of the day we are not shy to share a few uh takeaways that we think would help other like companies potential customers or the people that just want to build this

**[8:06](https://www.youtube.com/watch?v=z01r8DYsY0I&t=486s)** thing in house to uh follow a few lessons we learned. The first thing we think is very uh efficient or say we can we can offer accurate offer the correctness of the data set by um providing the immutable data itself. And while we offer the uh the flexibility for for feature engineering by proving uh by improving by providing this mutable and versioned data with schema evolution capabilities, right? And big this this thing is very different from say if you want to run a BI applications from uh traditional big data

**[8:54](https://www.youtube.com/watch?v=z01r8DYsY0I&t=534s)** infrastructure for all the models when you train you actually want to have a uh po back to back to time pointer to say um this is exactly my data used for train for this version of models and I can understand accurately about the distribution of this data And uh anytime in the future if I want to go back to check any imbalance or rare cases within this data set, I can still be able to reproduce this data set. Right? The second thing is the disparency between AI. For example, you will have like uh tens a few a few maybe a few AI engineer to a few hundred engineers within say large large uh

**[9:45](https://www.youtube.com/watch?v=z01r8DYsY0I&t=585s)** operation uh large large companies where it's easy to have tens of thousands of agent just through as one of agent through um 247 all continuously run on top of you. the the system need to be very elastic to support those like up and down kind of a um elastic workload that where your storage is relatively um stable in a way that is immutable. So you you you have a very predictable size of of the storage unit, right? And also we see that the the curve of those those query traffics comes within your uh model development circles. Usually you

**[10:32](https://www.youtube.com/watch?v=z01r8DYsY0I&t=632s)** will see um three to six months you will build a new models. In the first two months there are a lot of data processing jobs and curious comes point but the first month to the six months is always about model trainings. the other other uh task will slow down and cool down significantly right and um as we mentioned we see ourself where I mean this is a from from the data wing aspect you will see a very huge um site as a funnel for for people to crawl the whole internet or uh of the data into this system before they can fil out and before they make much smaller data set for uh feed into training. So the the

**[11:23](https://www.youtube.com/watch?v=z01r8DYsY0I&t=683s)** primitive uh primitivities of creation to filters to the duplication that's actually uh fall into each stage of uh of this development cycles and within within the same and within different uh system components of uh of the data. The last one um we even with basically the best labs out there we still see um AI researchers that spend significant time like more than 80% of their time is building the tools and building an infrastructure instead of uh uh building the data model itself right that's um I guess like everyone tell us they they want to uh get rid of this job by by themsel so um we we still see improving

**[12:12](https://www.youtube.com/watch?v=z01r8DYsY0I&t=732s)** tooling is very um necessary investment within this market as well. Last this is a uh questions from our CEO. So we we categorize the maturity of our data data management where from our customers into different status. The first one is you no matter what you have just dump a lot of data to S3 where GCS they have JSON file image files and what you don't even know where is it right and the second the first level if you take uh your data set more seriously at least you need to know what's in it right you need have some schema to know what fields in it and what data in it

**[13:00](https://www.youtube.com/watch?v=z01r8DYsY0I&t=780s)** and who collect this and what distribution in in that after that people glue some uh duct DB train spark to be able to understand this thing with tooling not with offshop uh Python scripts right then after that we will have start to track this thing become more serious about how where the data is involved from the raw data to to something that you you will tack and and train uh and then after a few more steps you will have government of this data right so this is a I I would like to encourage if you uh if you guys come from those AI labs to think where your team is at here and uh as uh LDB as a company we would love to bring you from

**[13:52](https://www.youtube.com/watch?v=z01r8DYsY0I&t=832s)** L0 to L L5 for sure so that's uh um yeah that's the last questions we have
