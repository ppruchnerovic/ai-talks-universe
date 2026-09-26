---
id: f5TYdiw4-lE
title: "Agents and Robots: The Human Effort Putting AI Into Production | Encord | Ray Summit 2026"
slug: agents-and-robots-the-human-effort-putting-ai-into
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2026
speakers: []
channel: "Anyscale"
duration_min: 8
published_at: 2026-09-17T16:06:58Z
video_id: f5TYdiw4-lE
url: https://www.youtube.com/watch?v=f5TYdiw4-lE
youtube_url: https://www.youtube.com/watch?v=f5TYdiw4-lE
tags: []
topics: ["Agents & orchestration", "Multimodal, vision, speech & robotics"]
transcript: true
---

# Agents and Robots: The Human Effort Putting AI Into Production | Encord | Ray Summit 2026

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=f5TYdiw4-lE) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Whether it's an agent or a robot, production AI runs into the messy reality of its own data: raw output that's unstructured, unlabeled, and full of the ambiguous long-tail cases that decide whether the system actually works.

At Ray Summit 2026, Oscar Evans, AI Solutions Lead at Encord, looks at how teams building acting AI, in software and in the physical world, turn raw logs and interaction traces into curated datasets that carry human context and reasoning. He walks the spectrum from model-driven curation to human-driven correction, with practical guidance on managing and labeling multimodal data efficiently and accurately.

You'll leave knowing where to let models carry the load, where human judgment is non-negotiable, and how to place the handoff between them for the biggest gains in model quality.

Liked this video? Check out other Ray Summit breakout session recordings: https://www.youtube.com/playlist?list=PLZNaJyYZRPdo

Subscribe to our YouTube channel to stay up-to-date on the future of AI: https://www.youtube.com/c/anyscale

🔗 Connect with us:
X: https://x.com/anyscalecompute

## Transcript

*1,392 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=6s)** Hello everyone and welcome to this talk on agents and robots, the human effort putting AI into production. My name is Oscar and I lead the solutions engineering team over at Oncord. So, Oncord is the universal data layer. We have a platform that allows folks to manage, curate, and annotate all sorts of different types of multimodal data. And you can see from our customers on the left-hand side that we work across a very wide range of domains. And today I'm going to be talking about the parallels between robotics and software agents and how they uh use and how folks using the Oncord platform to take messy unstructured data into human intelligence semantically labeled fields that they can use for their

**[0:52](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=52s)** pre-training post-training and evaluation flows. So, to start off with we're going to talk about the uh the problem in both of these spaces. So, we have the um we have demos of agents, we have demos of robotics. The issue is getting these into production. So, for both of these timelines, we have very, very messy uh multimodal data that we are generating or capturing from the real world. And we need a way to be able to sort through this and identify what is important. So, you can see for agents, we have um action logs and we have maybe lots of kind of individual steps, but what we need is we need the important semantics that we are capturing from the uh from the actual intent of the agent in order to fine-tune these.

**[1:40](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=100s)** And then on the robotics side, we have complex multimodal data formats. So, that can be lidar, that can be depth imagery, uh UMI data from teleoperation, um and then we can have video time series, and all sorts of different modalities in there, too. Now, the challenge for the first challenge for all of this data is how we can go about taking a very large corpus, especially where we have these complex data formats and different data types, and how we can kind of find the needle in the haystack. So, how do we go about searching through this data in a way that is repeatable and scalable to find the data that's mattered? And this is our first solution. So, Uncode we provide a data creation platform for searching and filtering through this data at twice rate scale to find the logs that are important, find

**[2:29](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=149s)** those interesting long-tail events that we want to use for either our training, our validation, our evaluation flows, and providing a repeatable structure to do this. So, we can integrate directly with your cloud storage, stream all of this data in to the platform, and you can visualize and search through this at scale. Now, once we've identified this data, we need to imbue the human context that makes this data useful for either training or evaluation. So, the next process is the annotation side. Now, traditional data annotation was fully manual and relying on human flows, but now with where I AI is, we can have model led annotation and also model accelerated annotation on both of these

**[3:16](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=196s)** sides. So, this can look like having pre-labeling models in the pipeline, and we provide inference of the latest models from Invideo, Open AI, um and Anthropic to be able to go and run across your data to be able to imbue this context before you've even passed it through to a human annotator. And you can see some of those examples and how they compare for giving temporal context, labeling across different data modalities, and then also how we can pass this through to the humans. Now, for these repeatable tasks, so if we're thinking about a robotic example, if we've seen a very large representation of a pick and place task, then maybe we can we can automate this labeling process. We've seen this time and time again. We can automate that

**[4:03](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=243s)** annotation. We probably need very little human review. But for these more subjective or maybe evaluation-based or if we're thinking about an agent and we have a chatbot response, we want to quantify the the subjective feeling of how I want my model to interact with a customer, then we need these human-based evaluation flows. And when we're thinking about building these, we have these pipelines that allow you to combine the two. And I talked about AI-driven labeling, which is what we see on the left, and then also AI-accelerated human annotation on the right-hand side of where you can give humans the latest tools to be able to go through and label this data at scale so that you can efficiently generate the right data that you need for your training pipelines. Now,

**[4:51](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=291s)** all of these all of these examples are fine for a demo, but what we're talking about is production-grade scale. So, when we have this increased volume for any of our human interactions with the data, we want to make sure that they're consistent and auditable. And so, what we need is we need an infrastructure to be able to track and manage all of the actions that have happened on the data. So, that can be every time a model has run on top of the data, but equally that can be every human interaction with the data on that side as well. So, what we're seeing here is a graph at the bottom of of how the human label acceptance can trend on one of our projects. And this is anonymized from one of our customers, where we can see that these these tracks have improved based on the human annotation management services that we

**[5:38](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=338s)** offer. So, this is where we have teams of people who can work on these projects and make sure they're following the specification, following the guidelines to label this data in a way that is consistent with your intent for how you want the model to perform in the real world. And we have techniques, as well as the workflows that we saw earlier, to be able to include models and include human labeling and human human QA processes. We can also do comparison between annotators. We can bring in um metrics for evaluating the specific quality of the annotator and even test tasks that you can sow into this workflow to then evaluate how good each annotator is on a specific task. And all of these techniques ensure that we're getting the highest quality data, which ultimately is the moat when you

**[6:25](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=385s)** are building your own models. And what these outcomes can look like, um so from one of our customer case studies, we saw that they were able to actually reduce the number of tasks that they sent through for their annotation labeling workflows. They improved the MAP of their specific model. And as they were uh iterating through this cycle, the biggest improvement to their business that they saw was that they had a 60% faster model iteration cycle. And so what this means is this means as we're going from um iteration speed and we're trying to improve our model rapidly and experiment uh quickly, then that process was cut down by having a platform that enabled all of these flows to be run efficiently and accurately, as well.

**[7:18](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=438s)** So, all of these pieces come together to say, when we have the agentic and robotic data problems, we have these messy logs, we have these unstructured data fields, how can we imbue a context into these? We need a way to sort and filter through those, find the data that is important in the pipelines, and structure this. And then how can we accurately distribute these to the right people to be able to um generate the human context that we need to be able to evaluate and train our models at scale. So, if you're working on a model training project or you're trying to evaluate how different models perform on your data uh and you're looking to run one of these projects at scale then we are on cord and and you can see my contact information up on the screen there and we provide the data layer for everything

**[8:06](https://www.youtube.com/watch?v=f5TYdiw4-lE&t=486s)** on the physical and agentic AI stack. Thank you very much.
