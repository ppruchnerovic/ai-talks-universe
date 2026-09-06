---
id: H7xmET_Z6eo
title: "From Renting Machines by the Hour to Renting Capabilities by the MSeconds • Dhaval Nagar • GOTO 2025"
slug: from-renting-machines-by-the-hour-to-renting-capabilities
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Dhaval Nagar"]
channel: "GOTO Conferences"
duration_min: 15
published_at: 2026-04-15T12:00:37Z
video_id: H7xmET_Z6eo
url: https://www.youtube.com/watch?v=H7xmET_Z6eo
youtube_url: https://www.youtube.com/watch?v=H7xmET_Z6eo
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTO Serverless", "GOTO Serverless Day", "Serverless", "AWS Serverless", "Event-Driven Architecture", "EDA", "Dhaval Nagar", "k8s", "Kubernetes"]
topics: ["Enterprise adoption & strategy", "Inference, serving & GPU infra"]
transcript: true
---

# From Renting Machines by the Hour to Renting Capabilities by the MSeconds • Dhaval Nagar • GOTO 2025

**Dhaval Nagar**

`GOTO Conferences` · `GOTO` · `2026` · `15 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTO Serverless` `#GOTO Serverless Day` `#Serverless` `#AWS Serverless` `#Event-Driven Architecture` `#EDA` `#Dhaval Nagar` `#k8s` `#Kubernetes`

[Watch the recording](https://www.youtube.com/watch?v=H7xmET_Z6eo) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Dhaval Nagar - Founder, APPGAMBiT and AWS Serverless HERO

ORIGINAL TALK TITLE
From Renting Machines by the Hour to Renting Capabilities by the Milliseconds

RESOURCES

Links

ABSTRACT
Over the past decade, cloud economics have compressed from “pay for the whole server” to “pay for only what you use.” We shifted from hourly virtual-machine pricing, to per-second billing, to serverless functions metered in milliseconds - and now platforms charge per database query or even per word (“token”) processed by an AI model.

This brief talk traces that journey and explains how "capability-as-a-meter" pricing helps teams of any size to compose software from granular, on-demand building blocks while generating maximum value out of every millisecond and token. [...]

TIMECODES
00:00 Intro
03:55 Dev reality 10 years ago
06:43 Evolution of compute
07:26 Building software today
08:15 Act 1: 2015-17: Serverless start
10:05 Act 2: 2018-21: Great unbundling
11:42 Act 3: 2022-25: Capability economy
12:55 The new developer mindset
14:01 How to embrace the shift
14:33 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ashley Peacock • Serverless Apps on Cloudflare • https://amzn.to/3EU7P85
Jeroen Mulder • Multi-Cloud Strategy for Cloud Architects • https://amzn.to/3FdNDOA

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*2,308 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=0s)** [Music] Good morning everyone. I see a lot of people uh almost full. Yeah. Quick show of hands. How many of you are developers for more than 10 years? More than 10 years. More than 10 years. Okay. Okay. Uh my name is Daval Nagar. I'm one of the serless heroes and I have been building applications for a little over 19 years now. Now that's a long time. That's a very long time. And uh in the early days I used to I had to put uh paper forms to

**[0:52](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=52s)** purchase new servers. By the time those servers are available to us, the application is long gone. No one even cares about the application. So that is back in 2005 2006. Fast forward, I I'll be talking about the last 10 years, the evolution of compute infrastructure or the cloud services in general and many of you won't believe cloud native was not even a word 10 years back. Okay, Lambda was launched late 2014, 2015 it was generally available and like many people I know a lot of people who have uh experimented used lambda. I had a startup back then which failed. I used lambda in that and we had a very simple use case. We were uploading large DSLR

**[1:42](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=102s)** images and we wanted to shrink those images into a smaller thumbnails. best use case. That was the initial purpose and offering of lambda having an S3 trigger so that you can execute something which is very minuscule very focused and doing just one task. The only difficulty was you need to upload prepare the zip and upload the zip. There was no easier way. So I have lived uh through different eras and I enjoy what has happened in terms of cloud in terms of services in terms of infrastructure and in terms of a developer and user experience over the last 10 years which has last 3 four years I'll not talk about I counted how soon it takes to start using LLM and AI and it took 14 minutes before we start

**[2:33](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=153s)** including AI and everything. So I I'll I'll wait for a for a couple of more minutes before I jump into the EI part. So when we talk about software components, often the hardest part is to talk about what they are. If it's a monolithic application, it's very hard to describe. Still there are uh people who find uh a way to best describe them. But like I said, I've been doing this for a very long time. So I follow Martin Fer. How many of you are familiar with Martin Fer? Kent back Martin Fer. amazing people they brought up the concept of agile extreme programming some of these concepts are still relevant still useful whether it's like uh 10 years 15 years or 20 years back so software components are things that independently replaceable and upgradeable right in the first one hour uh Shushit uh John's covered a lot of

**[3:25](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=205s)** things about what serverless is what kind of advantage what kind of efficiency what kind of comfort that it brings into the day-to-day development and the popular services. So this one this definition was back uh in 2015. At that time the lambda was still not prominent. Uh docker was just starting and then the kubernetes was also just starting. So this was a very interesting time uh back then. So 10 years back I used to do some of these things and I hope many of you might have done the same thing. I feel that some of these are still relevant. I see people still do these things. So 10 years back EC2 provisioning. How many of you have done EC2 provisioning without

**[4:14](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=254s)** breaking it? It doesn't work first time. I have done it several times. It doesn't work first time. It doesn't connect. It connects internally but it doesn't connect externally. We have to experiment. And back then the documentation was very hard. So EC2 provisioning again the curious choice what should be the size right how much disk you need to allocate paying by the hours back in 2015 you were still paying by the hours it was not until 2017 when it switched back to the second okay so again a lot of things were in motion uh in in those uh few years managing the application services dependenc ES you build you manage only the person who

**[5:02](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=302s)** have went inside the EC2 knows what all things are there in the EC2 right and the cost was based on the hours of infrastructure whether it's a compute whether it's your code whether it's your database integration services anything you use that was paid by the hours not by the value now nonetheless I respect and I fully appreciate all those infrastructure engineers Yes, this is my machine. One of my machine. I still use EC2. This was taken yesterday. The up time is 2,673 days. It takes a round of applause, right? This is one of the oldest machine that I'm running, right? Not me personally, but I know that there are people who have amazing skills to

**[5:52](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=352s)** build up an infrastructure that can last for 7 and 1/2 years. And I'll I hope this lasts for another two and a half years. I'll be using it on a 10th anniversary. Maybe I'll be I'll be talking somewhere else. But if you see on the right hand side, people who are familiar with Linux, if you see on the right hand side, the load average shows a different picture. It's hardly used. >> Yes, it's hardly used. But the company who is using this it's not my personal server there is an application running on that there are re real users of the applications they don't want to change it they don't want to convert this to a serverless because it works I don't want to change it I want to hold it for another two three

**[6:41](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=401s)** years so the compute has evolved uh drastically in last 10 years from infrastructure as a service like our EC2 virtual machines to platform as a service to slowly the containers and function as a service and now we are seeing a new trend in terms of a compute that's software 3.0 go uh very recently Andreas mentioned this that now we are using models or the machine another endpoints we are just passing the simple English instructions and a data it does all the heavy lifting and returns back with a result in another world you would be writing all that code right but now we are replacing the code with just an endpoint so what building looks like in 2015 we already seen serverless edge cost MS

**[7:32](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=452s)** build compute we are only paying for the milliseconds not even seconds storage database analytics largest of the AI GP5 is is here today so once you finish all of this do check it out everything is available via API when you call something via an API you only pay for what you have consumed whether it's a data whether it's an account whether it's a uh tokens or anything else plugandplay services a lot of services are coming as a replacement or like true replacement of one versus another easy to scale globally. I don't remember when I have checked last time whether it will is it working in India versus it is working somewhere else. It works out of the box on its own. So I have divided everything into three part. I'll just uh make sure uh we cover

**[8:21](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=501s)** that. So the first act 2015 to 2017 when the serverless slowly started into the developer communities and people started experimenting and people started becoming very comfortable with that. So on the left hand side it's a developer reality managing the EC2 fleet docker containers SSH into the server I still do I took that screenshot by SSH into the server chron jobs and RDS elastic search were the the popular uh setups at that time. What changed? Lambda went into G 2015. Initial primitives were very small but still very relevant. Those services were very popular. S3 was the most popular by the time SQS, SNS, API gateway, they all started coming in and everything started becoming a better ecosystem. It was not just meant for

**[9:10](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=550s)** your back-end task, your asynchronous activities, something that people don't see, but everything was coming together very nicely. one service integration after another and then the popular use cases in the initial days nowadays as well the file processing chron job eventdriven whether it's a scheduling APIs web hooks simple was back then nowadays as you see trillions of lambda calls and they are doing something effective compared to uh what the other computes are doing can I replace my chron job with this yes absolutely that is something why I switched to lambda in the early days. It still is relevant. A lot of people still use the containers or uh virtual machines to do something like that. But that that was uh the growing concern at

**[9:59](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=599s)** that time that is it just for the the small task is it just for the backend activities or or anything bigger. Then the real shift started coming serverless framework. How many of you are familiar with serverless framework? the most I always enjoyed I really uh appreciated what they have done for the serverless ecosystem back then still doing it but yes there are new players there are new frameworks that are popular SST is one of my go-to uh framework now it's much more advanced much more uh developer friendly but back in 2018 to 2021 the real shift was in terms of a new integrations new players new companies developing around the serverless making the serverless as their first choice both in terms of the development and both in terms of a solution as well. Everything by the time everything was slowly becoming available

**[10:48](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=648s)** as an APIs and adopting serless frame pattern become very go. there are kind of a distributed uh resources available back then but then if you have heard about the serverless land which actually host the the repository of patterns together and it's a very nice uh it has like uh a lot of simple to lot of complicated patterns on on serverless so ecosystem rapidly evolved rise of uh new players like versel and notify again amazing uh services all centric around the serverless Pay for the value, not pay for the hour, not pay for the infrastructure running, pay for the values that you are using. And then abstractions become more normal. Infrastructure converted to APIs and API

**[11:37](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=697s)** converted to composible architecture that we that we use today. The last tech was 2022 to 2025. The larger portion of which was LLM and AI. So startups running without dedicated infrastructure. I know a lot of companies they don't go for the dedicated infrastructure until they hit a particular mark in terms of a user number of users or number of uh capabilities. So they don't use it they just rely on the different combination of serverless infrastructures. Compute has now wider options not just uh your traditional lambda but lambda at edge. Uh you have cloudflare uh workers again uh very popular. you have versal functions growing new capabilities that demand more kind of a uh centric or uh like very specific services like LLM

**[12:25](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=745s)** models vector database and how to run your agents. So real capabilities started converting to a IML as APIs that we use nowadays edge functions at scale. there are 300 plus pop point of presence uh servers on which your your functions can could be running uh without you doing anything. So infrastructure light uh business as a model and influx of new infrastructure services that we are seeing in last couple of years. So the new developer mindset that we are uh following and a lot of team that I uh see are following is APIs over infrastructure, fixed infrastructure, event- driven architecture like in the earlier uh uh uh session it is mentioned everything is becoming an event. So if you can identify the event you can

**[13:14](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=794s)** basically convert that to an event-driven uh architecture orchestration or combination of the services versus building a custom monolithic application. So divide everything into the feature wise, functionality wise or the the user role wise. Pay for the value that it will that was still relevant 10 years back. It is still relevant today. Probably in next 5 years, 10 years it will be more relevant. You consume, you use, you utilize and you pay for the actual value that is uh relevant for your use case. In 2015, developers are now composers of different capabilities. Susit mentioned that really well. They are able to do things rapidly because they are combining multiple focused services together and then bringing that as a solution. How to embrace the shift? Think APIs not

**[14:04](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=844s)** infrastructure. Use serverless prefer to use serverless or API first architecture. Infrastructure as a league or blocks events and workflow based architecture and modular capabilities combining the different focus services together. A decade ago, best engineers managed infrastructure. Now they eliminate it. So with that, I want to uh stop. Now I don't want to offend anyone but I like the word V coding. It allows non-engineers to convert their ideas into working application. one, it allows engineers like me who doesn't know many other things to still convert my ideas

**[14:54](https://www.youtube.com/watch?v=H7xmET_Z6eo&t=894s)** into something else. So, but with that, I'm still yet to see any white coded application that uses Kubernetes. Thank you. With that, I'll invite uh Prashant, the first serverless hero from India. [Applause]
