---
id: KOPto5NdzEU
title: "Arindam Sett - AIDaR: AI Data Readiness Evaluations Framework"
slug: arindam-sett-aidar-ai-data-readiness-evaluations-framework
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Arindam Sett"]
channel: "Berkeley RDI"
duration_min: 4
published_at: 2026-08-12T07:53:08Z
video_id: KOPto5NdzEU
youtube_url: https://www.youtube.com/watch?v=KOPto5NdzEU
tags: []
transcript: true
---

# Arindam Sett - AIDaR: AI Data Readiness Evaluations Framework

**Arindam Sett**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `4 min`

[Watch the recording](https://www.youtube.com/watch?v=KOPto5NdzEU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*619 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=KOPto5NdzEU&t=1s)** ARINDAM SETT: Hi, everyone. I'm Arindam and I'm a principal machine learning engineer in Genentech. My focus areas are agentic AI, scientific AI in life sciences, and AI data readiness, and also agent evaluations. So today, I have one single argument about AI data readiness-- is that as we are evaluating the agents, we also need to evaluate the readiness of the underlying data layer. So this is how it goes, at least in generic Roche. We are mandated to build an agentic AI system. We choose some data sets, and then ML engineers are working on it. A couple of months, we put some work together,

**[0:50](https://www.youtube.com/watch?v=KOPto5NdzEU&t=50s)** put the framework together. And then when it comes to evals, we see it's not performing very well. And then we were wondering what happened, what went wrong. I mean, we went to all the LangChain blogs, all the Pydantic blogs. Hopefully, we actually applied the best practices, but wasn't performing. Then we look into prompt engineering. We hope for the better models. But what we realized later is that the agents are not performing in vacuum-- they are working on top of a data layer. And the underlying data layer is something we need to also look at. I'll give a couple of examples, and then I'll go into a little more detail on that. There was this particular example

**[1:40](https://www.youtube.com/watch?v=KOPto5NdzEU&t=100s)** where we had a data layer, which was oriented towards more, like, dashboarding and reporting. And when you put an agent on top of it, what happened is that it was not performing well. And then we saw that it was oriented towards data warehousing or reporting or dashboarding. So that is something we need to look into. Now, looking into this, what we have come up with is an agent AI data readiness evaluation framework. And what we are calling it, at least as of now-- it's an evolving framework-- is there are five dimensions to it. So from left to right, clockwise-- the first is data quality. It's kind of obvious, how sound the data is, technically, in terms of completeness, consistency, and freshness.

**[2:31](https://www.youtube.com/watch?v=KOPto5NdzEU&t=151s)** Then semantic and metadata-- do we have metadata for the data set, for example/ let's say we are dealing with a PostgreSQL database. And do we have table and column comments, or do we have a blob for containing the context of that? Access and governance. Can we access the relevant data at all, or the agent can access the relevant data or not. Structural readiness-- This, is where I was giving that example of the data warehouse database. What we found out is that the data mart actually had a concept of Entity-Attribute-Value. And you can look it up what it is. But the bottom line that is not very conducive to running agents on top of it. Then we have also generalizability, where we are looking into whether the data

**[3:21](https://www.youtube.com/watch?v=KOPto5NdzEU&t=201s)** layer is generalizable or can it go beyond the happy path. So with that, what we have done is we have actually recently got a NeurIPS workshop. I know Scale AI also has another workshop approved. Congratulations for that. We have a NeurIPS workshop approved in Paris, and we're looking forward to talking more about it. And then basically what we are doing is putting the community together who are building data infrastructure for agentic AI, and who are also building the evaluations and benchmarks for agentic AI. So you can look into the website. Feel free to scan the QR code. So this was truly a collaborative effort within Genentech and outside academia, industry,

**[4:12](https://www.youtube.com/watch?v=KOPto5NdzEU&t=252s)** and outside community. And we're also looking to continue this conversation in the nearest workshop. Thank you. [APPLAUSE]
