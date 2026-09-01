---
id: xXf9z-ie8wM
title: "Dan Roth - AI for Data and Data for AI"
slug: dan-roth-ai-for-data-and-data-for-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Dan Roth"]
channel: "Berkeley RDI"
duration_min: 13
published_at: 2026-08-09T23:24:24Z
video_id: xXf9z-ie8wM
youtube_url: https://www.youtube.com/watch?v=xXf9z-ie8wM
tags: []
transcript: true
---

# Dan Roth - AI for Data and Data for AI

**Dan Roth**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=xXf9z-ie8wM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,982 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=3s)** DAN ROTH: OK. Hi everyone. Really excited to be here. So I'm going to change gears a little bit and talk about data. How we use data, how we access data. And you'll see in a minute why I call this AI for data and data for AI. But mostly, I'm really excited about the promise that GenAI has for data. So really, we are going to move from the messy world of using a lot of types of data, different representation, different types, where people need to learn the domain, need to learn how data is represented, need to transform data from one format to another, and need to understand how to fuse diverse data to a much cleaner way, where we will be able to actually work with data in a conceptual level, our own terms, our own metrics.

**[0:52](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=52s)** And what adds to this excitement is the fact that really a large amount of data that exists in the world is going to remain outside language model. So language models have swallowed a lot of the data. And this is why we have powerful agents today. But there's really no more general purpose data. A lot of the general purpose data has been swallowed, as I said, by model provider already, but there is a lot of data out there. Data that belongs to cooperation, data that belong to financial institutions, government agencies, people in medical centers. And this data will stay outside the models. And it's going to be dynamic.

**[1:41](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=101s)** So the question is, how do we deal with this external data? And I think that one of the key use cases of GenAI is going to be that of orchestrating and supporting access and use of external data. And this is true for human consumption, but it is important when we think about agents using data. Think about your coding agents. In order to develop coding agents, these coding agents need to access a lot of data, from design documents to tickets, maybe to correspondence about what happened in previous generation of the software. They need to access heterogeneous knowledge sources and do something with this. And this is difficult. So reliably supporting decisions that depend on retrieving and using data is extremely difficult. More difficult than we think.

**[2:33](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=153s)** And it's difficult for multiple reasons. It's difficult because of information retrieval. Hopefully, this will move at some point. There is a myth that information retrieval works. But try to search your email and tell me whether it does work. Understanding information needs, understanding the store data, using data. All these are extremely challenging in today's world old, and it makes all this business of knowledge access and use very difficult. So in most cases, we are thinking about AI for data. So how to use data or how AI can help us to use data for our own human consumption. Ask what AI can do for you. But really, we care about data for AI, because in order for us to develop agents, agents need to access

**[3:25](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=205s)** data to access a lot of different kinds of data. So this relationship between AI and enterprise data is really not one dimensional. While AI unlocks value from the data, you already have the quality, the structure, the governance of your data really determines what the agents, what AI can actually do. So understanding both sides of these equations are really important. And really the difference between AI that works and AI that may not work. So really, the data layer underneath agents is crucially important and very difficult to build. So think about agenetic capabilities and what kind of data we need in order to develop them.

**[4:16](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=256s)** Think about the 17 different types of documentation that exist, and think also about just trajectory data, operation data, tool use traces, and all this data that your agents need in order to be able to actually do what you want them to do. So why is it so hard? There are many reasons for this. There are some core difficulties. Retrieval. Really information retrieval isn't working unless the way you present the information need is lexically close enough to the way the documents that you care about are represented, which typically doesn't happen. So this actually necessitates developing a semantic data layer across heterogeneous knowledge sources. So first of all, you will bring the representation

**[5:06](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=306s)** of the data closer to the way information need are expressed, but also so that you will not care about where is the data coming from, which data source it's coming from. We need to deal with structure. So people think about NL-2 SQL or NL-2 other formal representation. And this transformation is very difficult, partly because it depends also on retrieval. If we want agents to use the data, again, we need information to them to access multiple knowledge sources, and we need expertise for each one of these knowledge sources. We have rich documents today. More and more rich documents are being stored, from papers to figures to video to images, and the information inside this rich data is actually not exposed to your retrieval unless you do something to expose

**[5:56](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=356s)** this information, and then maybe some pre-processing, maybe some stuff that your agents may or may not do. As I'll show in a couple of examples later on, planning how to access data, in what order to access it, how to filter one source by another is a very challenging problem, and not to mention conflicting information. Think about your file system or your email. How much conflicting data is there. And we want our agents that access data to actually do something well with this. And of course, there are reasoning challenges. Reasoning, in many cases, is beyond the capabilities of general purpose models. And under all these kind of core difficulties, there's issues that have to do with governance, policy,

**[6:46](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=406s)** enforcement reliability, consistency auditability that if you want to use large scale data in the context of a corporation, medical center, and so on, you really have to deal with and optimization. So in the first generation, we don't care so much about cost, but we do care about cost and how to think about when do I process data offline. When do I process it at runtime. How do I cache computation? How do I use query logs and history? All these are really difficult problems. So we actually are trying to work on all these aspects of the data, and I'm going to try to give you one slice of this. An important one, but not the only one, from the perspective of NL-2-SQL. And I'm going to give a shameless plug to some results that some of our teams at Oracle

**[7:35](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=455s)** have done in participating in competitions like Spider 2 and ARCHER and doing really well, kind of leading on top of the leaderboards in this. But beyond the shameless plug, I want to actually point out the absolute results, so you can look at ARCHER, where the result is actually 55% or Spider 2, where the result is just low 70s, which means that we are really far from being able to address these issues of accessing data and using data properly. And I'm going to illustrate this with the following example that hopefully you will find interesting. So I'm very interested in tennis and I follow tennis closely. So I'm using tennis as an example for a lot of the things to show capability.

**[8:24](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=504s)** So here is a question that I asked just a few weeks ago, I presented to a top model, give me a list of the European male tennis player, sorted by their tennis income. Only tennis income. So if you think about it, it's a very complex question because the model needs to know who are the players, which country they are coming from, is it in Europe or not, then go to tournaments they play in 2025, how much money they made in each one, but-- and the model actually give me the way things, which sources it goes to, which tables it goes, which pieces of text it goes to and at the end, it gives me a nice table. Now, first of all, before I analyze the table, think about how cool it is. This is really the promise. I just express my information in natural language and the model devised it.

**[9:13](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=553s)** It gave a plan, access many information sources; structured unstructured web. Used its parametric knowledge to know where the countries are and so on. Reconcile conflicting information because there's a lot of conflicting information out there, aggregated it and summarized it into a table. Beautiful. Now, let's look at the details. Look at these two entries that I point to in the arrows, and you see that they are not sorted correctly. This was the most surprising mistake to me, because the model should have called the tool to do sorting properly. Never mind. But even more interesting is someone is missing. I'm sure some of you will be able to tell me who's missing from this list. Alcaraz is missing. So the model forgot Carlos Alcaraz. Not nice.

**[10:04](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=604s)** And you can also look at these two players that I point to, and you'll see that their income is identical to the dollar. So they made millions of dollars, and the income is identical to the dollar. Cannot happen. Clearly a mistake. So what's happening here? So really, it's a very difficult task. The model needs to optimize access across knowledge sources. Now, it can go about it through a list of players, generate a list of players, and then figure out whether they are in a European country, which tournaments they play with, how much money they made in each tournament. Or it can go to the list of tournaments, and then look at each tournament, who played there, how much money they make, and so on. Now, there's a lot less tournaments than players, so maybe this should be the right way. But on the other hand, tournaments and data

**[10:52](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=652s)** are more noisy. So doing this right really depends on understanding the data and the domain, which is very difficult. In tennis, it's possible, in most cases, it's just impossible. So while agents are doing this faster than we can, they are prone to errors and high cost. And most importantly, if you think about it, and I did remind the model that he forgot Carlos Alcaraz and he added Carlos Alcaraz, but if you look at it carefully, you'll see that a few other things change. For example, Andrei Rublev, number 7, completely disappeared from the new list. The money changed a little bit. So Zverev that made over 6 millions before now is making less than 6 millions.

**[11:40](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=700s)** So it's not consistent. But really the important thing that I want to point out here, this is tennis. Really, who cares. And I also know the results. So I know how to look at it and decide whether it's correct or not. But if this was the same question that you ask about your financial analysis of your company or any other sensitive information, the notion of visibility of failure is really important. We should be able to address this issue because without it, we cannot use these kind of systems reliably and consistently. So I want to stop here, basically remind you that real world data is multi-modal, temporal, multilingual, heterogeneous, and we really have to do a lot of work in order to unlock this information and understanding both sides of the equations,

**[12:29](https://www.youtube.com/watch?v=xXf9z-ie8wM&t=749s)** AI for human consumptions over data and data for consumption or using data for consumption is really the difference between AI that works and AI that disappoints. Thank you. [APPLAUSE]
