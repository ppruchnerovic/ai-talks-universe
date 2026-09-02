---
id: APMWvZHDCgI
title: "Lijie Chen - The Unit Distance Conjecture and AI for Math"
slug: lijie-chen-the-unit-distance-conjecture-and-ai-for-math
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Lijie Chen"]
channel: "Berkeley RDI"
duration_min: 11
published_at: 2026-08-12T02:14:41Z
video_id: APMWvZHDCgI
url: https://www.youtube.com/watch?v=APMWvZHDCgI
youtube_url: https://www.youtube.com/watch?v=APMWvZHDCgI
tags: []
transcript: true
---

# Lijie Chen - The Unit Distance Conjecture and AI for Math

**Lijie Chen**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=APMWvZHDCgI) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,423 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=APMWvZHDCgI&t=1s)** LIJIE CHEN: Yeah. So hello, everyone. So today I will be talking about more like yesterday's news on unit distance conjecture and discovery. So the slide was made a couple of weeks ago. But as all you know, we haven't released 10 more new proofs on many major open problems in mathematics. But still good to revisit this discovery before. So the new distance problem is a very simple two-state problem which asks, does every set of n distinct points in Euclidean two-dimensional space contain at most roughly linear many pairs, which are distance 1 apart? So you are imagining putting n points on a plane, and you want to see how many points can have distance, roughly 1.

**[0:50](https://www.youtube.com/watch?v=APMWvZHDCgI&t=50s)** And this was proposed by Paul Erdős back in 1946 and is one of the central question in discrete geometry. So roughly two months ago-- actually, one, two months ago-- we announced that an OpenAI model has disproved its conjecture, showing that you actually can have a construction with more than linear number of pairs. So let's say a little bit more about the discovery. So this is achieved by a general reasoning model which is not trained specifically for math. It's completely general. It's basically a version of ChatGPT. It's discovered during a site evaluation of the model on some very hard math problems.

**[1:40](https://www.youtube.com/watch?v=APMWvZHDCgI&t=100s)** Because, nowadays, it's very hard to benchmark a model against math problems, since most of benchmark is kind of saturated. So you have to find some hard problem to test the ability. And essentially, there's no harness. You just give a model one point and then just keep thinking about things. And maybe use some tools, and then it arrives at the final answer. The model has access to the web and a terminal so it can search for what has been done before. Let's say a little bit on the original construction by Paul Erdős. So the idea is that his original construction is just that n by n grid, with a carefully chosen scaling. So you want to put many points on a plane.

**[2:31](https://www.youtube.com/watch?v=APMWvZHDCgI&t=151s)** So you put them in a grid. And you scale that so that many of them have distance 1 apart. And the new construction, actually, it's more complicated. It's grid over rational numbers. And you work in a new field L of i, where L is a carefully engineered high-degree real number field. So I'm not going to say much about the detail, but the model basically spelled this in its intuition instead of thought. It says that the degree and height of the algebraic variation can be enormous, but that's actually can be a good thing. So the model carefully chose this number field

**[3:21](https://www.youtube.com/watch?v=APMWvZHDCgI&t=201s)** so that it actually works its construction. So after we got this, we discovered this solution, we tried to see how success probability of the model correlated with the test-time compute we spend on the problem. So as you can see, if you put more and more test-time compute, you have higher and higher success rate on the problem. So thinking longer definitely makes it more likely to find a correct solution. And in a sense, if you look at the CoT, the model can introspect and realize it's not making progress in one direction, or it's making some mistake, so it can self-correct

**[4:10](https://www.youtube.com/watch?v=APMWvZHDCgI&t=250s)** and just keep going. So from there, I think it's good to review or introspect on how much progress AI has made, like what's the best way to measure maybe AI progress. So METR has this fantastic graph plot on like the x-axis is the years, and the y-axis is for some task. What's the amount of human time you will have to do it? And so the plot is on, at this time, what's the human time of task the agent can reliably done for us? As you can see, it's basically doubling every six months.

**[5:08](https://www.youtube.com/watch?v=APMWvZHDCgI&t=308s)** The length of human work that can be done reliably by AI is doubling every six months. Of course, this METR graph is mostly in the area for coding, yeah. So let's maybe take a look on AI as well. So almost two years ago, the model can solve any problem. You can think about that as maybe 20 minutes human time for a very good high school students. Like AIME, it's not very hard. Then, let's say, a month later-- I mean, sorry, a year later, AI can solve IMO problems. Those problems are way more harder.

**[6:00](https://www.youtube.com/watch?v=APMWvZHDCgI&t=360s)** They are maybe 90 minutes of human time for top high school students. Right. Then another year has passed. So AI can solve long-standing open problem in discrete geometry. So how many hours does that cost to human? So if we put things on a scale, I will claim that-- so in a sense, this is roughly six hours of human time, but assuming them actually knows all of mathematics. The reason is that the proof is not that deep, in the sense

**[6:58](https://www.youtube.com/watch?v=APMWvZHDCgI&t=418s)** that it requires you to understand some ideas from a very distinct field and apply them back to discrete geometry. You have to be a very good algebraic number theorist and a very good discrete geometer to do the proof. But if you are very good in both of them, then it probably only takes you a day or two to really push to the conclusion. The challenge is really to master two distinct areas. So in that sense, AI has this very unique advantage here. They have a very broad familiarity across all mathematical fields. And they are also decent in many subfields. Finding this kind of example does not require extreme human time, if the human already has the right expertise.

**[7:47](https://www.youtube.com/watch?v=APMWvZHDCgI&t=467s)** But it may, if they first must learn the area, because learning the area takes maybe two years or so. But if you master all of them, then it's different. So in that sense, AI can shorten the search, can do this math wave to some type of mathematics better than human, just because they know a lot of domain knowledge. As you can think longer and develop better domain knowledge, progress on the distance reflects this multiplied effect on both trends, like thinking longer and better domain knowledge. And so in a sense, some other mathematical results, they require years of work from the mathematician by pushing deeply on one topic.

**[8:37](https://www.youtube.com/watch?v=APMWvZHDCgI&t=517s)** It's unclear whether we are at that point yet with AI. And after the unit distance, the model-- we released 5.60, which is very, very good at mathematical reasoning. There are so many public results already in on them, has done by 5.60 in the past two weeks. And also yesterday, we just announced 10 more results in mathematics and theoretical computer science on different area. So I think it is already there. So I want to say a little bit on how do I view the consequence. So I think AI is especially good at connecting

**[9:28](https://www.youtube.com/watch?v=APMWvZHDCgI&t=568s)** distant field of research. Just like how they saw unit distance problem, they connect different fields. So I think mathematicians will be really empowered to use ideas from different fields, which may feel less familiar to them, and because AI can just find the relevant ideas and explain them very well. So mathematics is never about just problem solving. The most important human input to the OpenAI solution to unit distance is actually Paul Erdős, who really posed this beautiful question with that simple statement and a very deep solution. So AI found the solution, and the human understood it. And actually, after the release of OpenAI proof, at least five or six follow-ups on this result by different groups in the world.

**[10:20](https://www.youtube.com/watch?v=APMWvZHDCgI&t=620s)** So I think AI will make it much easier to iterate on which deep question I was asking, because you cannot find a counterexample very easily. And also, finally, the ability to do precise calculation used to be a big part of math. Calculator and then computer really empowered you to do more. You don't have to do calculation yourself. So in a sense, with coding models like Codex and Claude Code, programmers actually spend more time coding because that's much more they can do once they are empowered. I think, similarly, mathematician will also be empowered to use AI to do more math because now you don't have to do tedious calculation, and you can just maybe focus on high-level ideas or enjoy the process. OK, that's all.

**[11:08](https://www.youtube.com/watch?v=APMWvZHDCgI&t=668s)** Thanks. [APPLAUSE]
