---
id: fZzH0tUSs74
title: "Grace Tang - Data Benchmarks: Where Everything's Made Up and the Points Don't Matter"
slug: grace-tang-data-benchmarks-where-everything-s-made-up-and
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Grace Tang"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T07:53:00Z
video_id: fZzH0tUSs74
url: https://www.youtube.com/watch?v=fZzH0tUSs74
youtube_url: https://www.youtube.com/watch?v=fZzH0tUSs74
tags: []
topics: ["Evals, observability & reliability"]
transcript: true
---

# Grace Tang - Data Benchmarks: Where Everything's Made Up and the Points Don't Matter

**Grace Tang**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=fZzH0tUSs74) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*831 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=fZzH0tUSs74&t=2s)** GRACE TANG: Hi, everyone, I'm Grace. I do AI research at Hex. We are an AI data analytics platform. And as such, I spent a lot of my time basically trying to get LLMs to do data analytics and data science better, which is really hard. And so a big part of what we think about is evals and experimentation. And lately, every time I look at a new public benchmark for data, I'm kind of struck by the same thing. Everything's made up , and the points don't matter. Roll credits, we're done. I'm just kidding. But what do we really mean by this? Well, today, I'm going to talk a little bit about data benchmarks-- where they are doing well and where

**[0:50](https://www.youtube.com/watch?v=fZzH0tUSs74&t=50s)** we might be missing the mark. My thesis on benchmarking agents is very simple, and it's very much like what a lot of people talked about today. We should be testing these agents in environments that have the same level of realism as their eventual deployments. And as you'll find today, data is a uniquely poorly modeled field in frontier benchmarking. So before we get into that, though, what does a real frontier benchmark look like? You all might have heard of some of these. Like, ProgramBench, you're rebuilding a common codebase from scratch-- no internet, just docs. Running a vending machine business, and then just evaluating your profit at the end. Or like these simple yet challenging web search questions. These are actually only around 30% solvable by humans. What do all of these great frontier benchmarks

**[1:40](https://www.youtube.com/watch?v=fZzH0tUSs74&t=100s)** have in common? Well, they're evals that actually test real-world behavior that we care about. These agents being able to do. The problems are hard for agents, and they're hard for people as well. Now, though, let's take a look at the field of data analytics. DSBench. Last year, OpenAI used DSBench to report that their agent surpassed human performance by a significant margin on realistic data tasks. Ready to see what these realistic tasks look like? Well, a bunch of them are like these multiple-choice exam questions about financial modeling. It's literally like, can you write the SQL? Can you tell me what Excel formula you should use? And then there's a bunch of public Kaggle projects, including the Scrabble word puzzle.

**[2:30](https://www.youtube.com/watch?v=fZzH0tUSs74&t=150s)** It's totally crazy. And I think data analysts will tell you that this is not what their work looks like on a day-to-day. If this is what your work looks like, I'm sorry. What about Spider 2.0? I think Emily from Scale mentioned this one earlier, but we have a number of text-to-SQL benchmarks. I think the main issue with this is that it's not really testing analytics. If you look at it, the English is very specific, it's very prescriptive. You're basically just mapping English to WHERE clauses. It's like a translation task, or an instruction following task. And the external knowledge is not exactly carefully curated either. It's the wrong sport. What about DABstep? This is a well-known set, and this question looks very straightforward. It's pick a multiple-choice question-- what's the top country for fraud? The problem, though, is that if you actually

**[3:17](https://www.youtube.com/watch?v=fZzH0tUSs74&t=197s)** pull the data for this, the question is of fundamentally underspecified. It doesn't tell you whether you're looking at fraud rate, fraud volume. And like a real data analyst might produce something that looks more like this chart. And arguably, that's more complete and correct. And so all of this is very hard. I don't want to dunk on everyone's work. They've done a lot of hard work here. But overall, these themes tend to emerge. Nine is too many for me to read out loud. But the main idea is that they're not realistic. These grading is really harsh. It's grounded not really in reality. So at Hex, we have built Shorelane. Now, shoreline is completely made up. The points don't matter either. I'm not saying we figured it out, but it is pretty cool and we try and address some of these realism issues.

**[4:07](https://www.youtube.com/watch?v=fZzH0tUSs74&t=247s)** We built a fully synthetic B2B SaaS company called Shorelane Commerce. It's got a lot of semantic pitfalls that might occur in a real business. It's messy. It has migrations and incomplete documentation. And the task? Well, we have these agents do realistic tickets that an analytics agent or analytics person in real life might do. We evaluate on the entire train of thinking, on the tool efficiency and the actual analytics that's going on. And still, though, this is only half the problem. These evals are still suspended in a moment in time. How can we allow data analytics to learn from their mistakes? Well, unfortunately that's pretty much the time I have for today. So if you're interested in hearing more, please follow us at hex.tech.

**[4:56](https://www.youtube.com/watch?v=fZzH0tUSs74&t=296s)** You can also always reach out. And if you're interested on working with us, please reach out at our Careers page. Thank you so much. [APPLAUSE]
