---
id: 9S2KBARuAyA
title: "Krishnakumar Sharma - Agentic Coding, the Boring Way"
slug: krishnakumar-sharma-agentic-coding-the-boring-way
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Krishnakumar Sharma"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:15:44Z
video_id: 9S2KBARuAyA
url: https://www.youtube.com/watch?v=9S2KBARuAyA
youtube_url: https://www.youtube.com/watch?v=9S2KBARuAyA
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Krishnakumar Sharma - Agentic Coding, the Boring Way

**Krishnakumar Sharma**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=9S2KBARuAyA) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*917 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=9S2KBARuAyA&t=2s)** KRISHNAKUMAR SHARMA: OK, awesome. So here we go. So hi folks. Today, I'm going to speak about agentic coding the boring way. And this talk will focus on legacy systems, the enterprises. And while I say the boring way, if you are someone who wants to build systems and solutions which are scalable, which are secure, which are reliable, then maybe you will find this talk very interesting. So why I might be the right person to speak about this topic. So I am Krishna. I used to be head of AI at Amazon, Germany. I have built large-scale AI systems. I have brought billions in dollars in revenue impact for Amazon. As I worked in robotics AI as well, I decided to start my own startup Omokai. And in Omokai, I'm building an physical AI operating system. We are turning voice into autonomous machines

**[0:53](https://www.youtube.com/watch?v=9S2KBARuAyA&t=53s)** for robots and drones. While today I will not be speaking about what we are doing in Omokai, I will be talking about how I am building Omokai. And we'll be touching on the coding part, how the engineering teams in Omokai are actually trying to solve some problems. And maybe some things which I'm going to say here will be super controversial. So I look forward to that and look forward to your feedback. So one thing about Omokai, we are very AI native. We use our own models, which are fine tuned. And we use AI to generate data. We do have 7 human employees but more than 10 AI employees. So whatever I'm saying might be still quite relevant to you. So first thing first, why I am talking so much

**[1:43](https://www.youtube.com/watch?v=9S2KBARuAyA&t=103s)** about legacy environment. I believe that we are having an agentic hangover because as per a research published by Gartner, as you can see, using more AI does not lead to more productivity. It just leads to you making Anthropic and OpenAI richer. And maybe you want to become rich yourself. So if you are using AI unbounded without proper constraints, maybe you are not using AI correctly. And what I have witnessed is that there is a lot of chaos. There is a lot of noise. There is a lot of hype around how agenetic system should be building. And first of all, I would like to touch base upon some myths. So for example, you might have heard about agent swarms. Like using hundreds of agents to solve a problem.

**[2:34](https://www.youtube.com/watch?v=9S2KBARuAyA&t=154s)** This only leads to a lot of cost and lots of errors. Second thing, which is quite popular these days is loop engineering or loop within loop, as I have seen some people doing. This also will lead to a lot more cost than what you would want to look at. And if you are of an opinion that AI will get very cheap in future and the cost will not matter, then I have one more data point. As per another research done on using AI for code generation, if you use AI in uncontrolled way, you end up creating a lot more errors and a lot more persistent errors in your production databases. And maybe you would not want to do that. And then apart from all that, there is a lot of hidden cost of using AI without control,

**[3:23](https://www.youtube.com/watch?v=9S2KBARuAyA&t=203s)** from verification to the security loopholes, to debugging, and in the end, the cognitive depth. I have heard about AI burnout. I don't know how many of you have experienced it, but this is a real thing because if you use AI too much, you end up losing a lot of context. So how we can solve this problem. Oh yeah, before we go to the problem, this is one guy screaming at the internet because he's tired of this open source repository creating a lot of AI slope. So we don't want to do that. So let's get into some solution. Let's bring some discipline. So as I worked in Amazon, what I have learned is that frameworks and mechanisms, they help you a lot in building reliable and scalable systems. And today, I would be speaking about mechanism

**[4:13](https://www.youtube.com/watch?v=9S2KBARuAyA&t=253s)** which are developed at Amazon for agentic coding. We did this back in 2025. It's called D3 framework for agentic coding. It is quite straightforward. There are three phases. So first phase is discover where you create a research artifact. This research artifact contains all information about your repository, but also upstream and downstream dependencies. Then, based upon this research document, you create a plan, very well defined plan. And this plan has the task created, subtasks created. And then this information goes into the deliver phase, where an AI takes all this information and solves the problem. And another thing is that I believe that at this point, you cannot trust AI fully. So we should have some sort of human sign off. And you should use multiple different models,

**[5:01](https://www.youtube.com/watch?v=9S2KBARuAyA&t=301s)** not from same family, but different companies while you are solving the problem. Last thing I would like to say is that you should not use too many agents. Try to use maybe four and well-defined agents. One thing you want to take from this session, that is, stop token maxing and start ROI maxing. And if you would like to connect with me, let's connect over LinkedIn. I am doing a lot of work on robotics and drones as well, so looking forward to connecting with you. Thank you so much. [APPLAUSE]
