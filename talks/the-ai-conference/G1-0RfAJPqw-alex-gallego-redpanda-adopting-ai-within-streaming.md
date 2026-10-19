---
id: G1-0RfAJPqw
title: "Alex Gallego, Redpanda: Adopting AI within Streaming Architectures"
slug: alex-gallego-redpanda-adopting-ai-within-streaming
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 11
published_at: 2026-09-29T17:56:12Z
video_id: G1-0RfAJPqw
url: https://www.youtube.com/watch?v=G1-0RfAJPqw
youtube_url: https://www.youtube.com/watch?v=G1-0RfAJPqw
tags: []
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Alex Gallego, Redpanda: Adopting AI within Streaming Architectures

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=G1-0RfAJPqw) · [Conference site](https://aiconference.com/)

## Description

Alex Gallego, CEO and Founder, Redpanda

Adopting AI within Streaming Architectures

The fusion of AI and real-time data streaming is transforming how organizations process, analyze, and act on information. This talk examines the practical application of AI within streaming architectures, exploring where it makes sense to deploy emerging AI concepts such as Agentic AI and Generative AI. We will discuss techniques for integrating AI models into stream processing pipelines, as well as address challenges including maintaining low latency, establishing effective governance, and ensuring the connectivity required to build a robust AI foundation for streaming workloads.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,997 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=0s)** Um, good morning. My name is Alex. I am the founder and CEO of Red Panda. We have 10 minutes starting now. And uh, my job is to tell you about streaming architectures and how does that relate to AI. Um, a little bit about me. I grew up in Brooklyn, New York. And so I speak really fast. So if you have questions, please shout. Um, it's exciting to be here today. So, uh, let's go. I guess a little bit about me and the company so that all of you have a little bit of context of uh what is Red Panda, what do we actually do? Um and how does it relate to this particular conference? Um so uh Red Panda really grew up uh powering some of the world's uh most mission critical systems. So I'll highlight the uh Olympics. You can't break a world record without Red Panda.

**[0:50](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=50s)** Uh we protect uh properties like whitehouse.gov. We probably clear your check this morning. We power some of the largest stock exchange trading uh trade stock exchanges in the world like the New York is stock exchange um and so on. And so that's just a little bit of context. And so if you are either working with the global fortune 2000 or you try to serve that kind of customers, that's my lens. And so um take everything with a grain of salt. That's what I'm going to be sharing with you today. some of the lessons learned of what it took for us to partner with some of those uh companies today. So I only have two more slides. So we'll spend about the bulk of the time on this. It'll be about five minutes on this part and then I'll give you a

**[1:38](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=98s)** diagram at the end and all of you can take a picture that is like the main meat and potatoes of this whole presentation um of this lightning talk track. So um a little bit about Red Panda. So, Red Panda grew up as a cafka replacement for mission critical systems and I highlighted in the previous slide the types of customers that we do whether you're processing payments for this particular device um uh or really you're trying to if you hopped in the metro today that system is also powered by red panda and so it started as a cafka replacement for mission critical systems um and over time it sort of grew into what some of those customers that I showed in the previous slide are now using for to power either agentto agent communications uh or to effectively get access from their agents into their

**[2:28](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=148s)** data. I was at the conference floor today and the difference between this conference and the ones that I used to attend is that most people here are on the application side and so if a lot of this talk is more on the infrastructure side that's kind of how we grew up and I'll try to tie both audiences together in just a second. So um on the left and the right side you see there's a bunch of connectors and so although we grew up power and real time um uh workloads with red panda. So things like credit card fraud whether all of the electric car companies in the US are powered by red panda. There's a bunch in Europe as well. Some of the world's largest checking accounts fraud detection. Those were the core use cases that we grew up partnering with and solving. And so, um, one of the most fun

**[3:16](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=196s)** examples is Akamay. And so, it turns out North Korea launches an attack on white house.gov every night. And then red panda is sort of the system of record that helps us absorb the spikes of attacks and be able to learn and then you sell that as a security product. And so that's really on the log and data infrastructure side. So if you need a distributed log that is super scalable, uh that would be on the centerpiece. Um now how are the connectors and why are they useful for AI? It turns out that um the where the rubber meets the road for people is in the infrastructure side we used to call it integration in the AI side we used to we call it now context is if your agents need access to a bunch of data you basically have two options. Okay, on the left side, you copy it into

**[4:04](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=244s)** your data warehouse. And so maybe you use iceberg or delta lake or whatever format you want to use, but the job is you go into all of these disparate data sources and then you upload them into a particular data warehouse and then you access your data into a darehouse. I don't think this is where the world is going and this may be a contrarian view, but I think where the world is going is this idea of a zero data copy. It's like, okay, why do you have to pay the tax to go and access your data, make a copy of it? By the way, it's no longer operational because you just made a copy and you're behind and there's data quality issues. Why can't you go and directly fetch your data? So this is where the connector piece comes into play. Five minutes. Um so let me share one more pillar and then we'll spend the next four minutes on the actual architecture slide. This is just giving

**[4:50](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=290s)** you the context uh of why this talk may be relevant to the things that you're doing. So it is our opinion that most of the foundation models have already indexed all of the public available data. And so the next frontier is your private data. That is your goal. That's your mode. That is your asset. But where most sort of a struggle is like okay how do I unlock my private data sets? And so uh in the previous slide we talked about just being able to dig into your particular network and access whether it's your Oracle database or your Netswuite or or Reddis or MySQL or Postgress whatever right so you have this huge portfolio of connectivity and um our thought is like well can we package this still in a fully managed cloud that allows you to have a single click as you have agents trying to

**[5:40](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=340s)** access your private data sets. Wouldn't it be easy if you just simply provided in your network without anyone actually having access to your data sets? And so about I think three and a half years ago, I wrote the I think the first paper that ended up becoming BYOC. And I think most companies today, most AI companies um use BYOC as an architectural pattern to deploy it. Um but I think we were the one that effectively popularized it about three and a half years ago before AI came into the picture. So this is the money slide. Um, I'll talk about I promised I was going to share what does streaming have to do and what does connectivity have to do in the age of AI especially for this conference and so uh this architecture diagram is how some of the world's largest companies

**[6:29](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=389s)** that I mentioned on the first slide whether you're powering uh you know whether you're some of the largest banks in the United States or in South Africa or in Australia or the largest CDN, largest security company, largest electric car companies. Roughly, you're looking at slight variations of this, but this is this is it. This is like what is getting deployed to production. And so I'll share with you how does red panda and effectively the things that we do help people with this take those as as architectural patterns. Yes, we are a vendor, but it doesn't matter because the patterns here, this is why it's just a white box. I'm also an engineer so I didn't have time for marketing to go and make this slide pretty. So it's just like you know um black boxes and and uh that's what you get today. So in the next two minutes what can I share? Um

**[7:18](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=438s)** where people are struggling today it's effectively you have this new digital workforce people call them agents and you're like okay well what data are these agents actually accessing? Am I going to invent as a CIO of a top bank? Am I going to invent an entire shadow IT system to provision a new set of uh security policies, access controls, authentication, authorization, or am I simply going to use and act on behalf of what whatever your employees are doing. So that's typically wrapped in today what people see as like MCP or other protocols, which is how do you wrap this multimodels or more effectively said how do you translate an agent request which is an intentbased request. I want users, I want this particular report, I want access to those files to the actual underlying binary protocol, which it may

**[8:06](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=486s)** be a particular database, right? It could be it could be Oracle, it could be Reddis. So that's really where the connected piece sits in. But where most people struggle today is in the idea of having a global set of access controls and policies so that as a CIO you're like okay it's cool that if you're an HR agent for example I'm the CEO of the company and so if I ask for the equity position of the employees I should be able to get access to the entire company but if my head of revenue or my head of engineering ask for the same request so it's the same code what changes is the person making the request on behalf of the principal then they should see a particular slice of that and so I think that's where people are struggling today and I'll share that what people are doing today to be able to go back and debug is this idea that I

**[8:54](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=534s)** call model replay and for the engineers in the room is this concept of time travel debugging if something goes wrong let's say that your job is to provide a credit score application and my wife Sarah she gets denied her credit because the model has a gender bias well how do you go back and ensure that you can actually go back and understand what the hell happened, right? Like at some point you're outsourcing this business logic to a blackbox and it's accessing a bunch of tools, whether it's your credit bureau or your database or the profile of this person. How can you go back and debug what actually happened at the time of the sighting, whether you want it or not to approve or disprove that particular credit score application? And so what people are seeing in production is you record it in a distributed log which is sort of an efficient way to being able

**[9:42](https://www.youtube.com/watch?v=G1-0RfAJPqw&t=582s)** to go back and replay the decisions that you've made. I'm going to pause here. The last piece that I'll share that ties it all together is that that's still not enough. And what you end up wanting to do is this idea of unbounded queries. I think the next click of what people will are deploying at least some of our customers is this idea of unbounded questions. How does this seller compare to my previous seller for this particular geolocation for this particular widget? And those kinds of questions, the agent doesn't know if it's going to query a pabyte of data or a particular row. And so it's beyond this intentbased access. You need something that pushes the dynamism of the filter into a query engine. And I'm out of time. Thanks everyone.
