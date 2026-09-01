---
id: 1VO7hdEgSeo
title: "Scott Clark - How Better Evals Can Bring Abundance Through Accelerated Scientific Discovery"
slug: scott-clark-how-better-evals-can-bring-abundance-through
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Scott Clark"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:53:15Z
video_id: 1VO7hdEgSeo
url: https://www.youtube.com/watch?v=1VO7hdEgSeo
youtube_url: https://www.youtube.com/watch?v=1VO7hdEgSeo
tags: []
transcript: true
---

# Scott Clark - How Better Evals Can Bring Abundance Through Accelerated Scientific Discovery

**Scott Clark**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=1VO7hdEgSeo) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*964 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=1s)** SCOTT CLARK: Hey, everybody. Thank you all for sticking around. I know it's Sunday afternoon and this is the penultimate talk. As soon as my slides come up, I'll look forward to chatting to you guys about bringing better abundance through better evals. Excellent. So as we said before, my name is Scott Clark. I'm co-founder and CEO of Distributional, and I'm building Talaria Scientific. And I'm going to tell you about how you get better abundance. But first, I'm going to define what that means. So what does abundance through AI mean? In my mind, it's better scientific discoveries that lead to new materials, more efficient energy. This leads to better medicine, more efficient ways of travel. It basically means living in a sci-fi future. It's less about how do we get rid of more white-collar jobs

**[0:52](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=52s)** and put everybody out of work, and it's more about how do we improve people's quality of life. And I believe that for the first time, we're finally able to meaningfully accelerate scientific discovery with AI. The last few months have really unlocked quite a bit of capability. And this has been a passion of mine for a long time. I've been trying to solve this problem for the last 20 years of my career, with varying degrees of success. It started back when I was doing undergrad and leading up to my PhD, where every single problem that I solved, every single group that I worked with, from protein folding to quantum mechanics simulation to metagenome assembly, always ended with the same problem at the end. We'd build something great and then we would need to tune it. Lots of different knobs and levers,

**[1:40](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=100s)** hyperparameters, whatever you want to call them. If you could make the graphs and the benchmarks slightly better, you got a better paper. We jokingly call this grad student descent because it was often the role of the grad student to sit up late at night, tuning knobs in a high-dimensional space, trying to get that slightly better paper. People did apply smart techniques to this, simulated annealing, genetic algorithms, local methods. I fell in love with Bayesian optimization, and that became core to my PhD thesis, and it ended up being the central point of my first AI startup SigOpt. Started this in 2014, and our goal was to solve the parameter tuning problem. And over the course of seven years, we worked with great firms like Netflix tuning the recommender systems, Amex tuning their fraud systems,

**[2:29](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=149s)** OpenAI in the early days when they were a nonprofit lab tuning their early RL systems, as well as about $1 trillion worth of hedge funds and several hundred academics used our free program to tune their papers, everything from materials design to drug discovery. When I sold the company to Intel in 2020, we used it to tune everything from chip design to benchmarking MLPerf, when that was what everybody was overfitting to at the time. So the goal was optimization at scale for problems that really mattered. And it worked really well, except when it didn't. So the problem was it would fit exactly what you told it to do. It would always optimize what they gave us. But oftentimes when customers would come back, they'd say, yeah, you made that number go up,

**[3:16](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=196s)** but some other number went down. And that's the problem with an optimizer. The very best thing about a black box optimizer is it will optimize any eval you give it. And the very worst thing about a black box optimizer is it will blindly optimize any eval you give it. And so you can make a really accurate fraud detection system if only 1% of your transactions are fraud by saying nothing's fraud. 99% accuracy right there. Additionally, we're still a long ways from just setting these systems up to be completely autonomous. I think we're a long way away from just saying goal solves stable fusion containment, solve cancer, these sorts of things. And even if the model came back with something, how could we trust it? And that's the other side of this coin.

**[4:04](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=244s)** You need to optimize these systems and you need to trust them. And that's what I set out to do with Distributional. I thought I would attack this in the most complex mathematical way possible, big statistical tests. And we would solve chaos and we'd solve non-stationarity. And this was a terrible idea because nobody likes tests, they didn't have the data, and everybody was just yoloing models into production anyway. So I pivoted the company is what you do. You're failing, pivot. Analytics. So let's catch the evals that are sneaking through your system. How do we find patterns and behavior in order to be able to say, hey, this is the unknown unknown the eval you should have written? This also failed. This is a really good idea, but it's more of a feature. Let alone a product, let alone a startup.

**[4:54](https://www.youtube.com/watch?v=1VO7hdEgSeo&t=294s)** So now what I'm doing is I'm applying everything that I've done in the last 20 years to attack the scientific problem of how do we accelerate science, focusing in on what actually matters, building bespoke evals that know physics, that know about the scientific research process, that know how to do hypothesis validation so you can spin the flywheel of what-if machine faster and faster and faster. Doing what I did in grad school that used to take six months in six hours instead. If you're interested in this, we're building this in the open. It's going to be open sourced at NeurIPS. There's a private beta right now. Follow along and I would love to chat with you if you're building anything computational science-related.
