---
id: u7k1l_qkQH8
title: "Modern Computer Architecture & Organization • Jim Ledin & Maciej «MJ» Jedrzejewski • GOTO 2026"
slug: modern-computer-architecture-organization-jim-ledin-maciej
conference: goto
conference_name: "GOTO Conferences"
category: "Software dev with AI tracks"
edition: "GOTO"
year: 2026
speakers: []
channel: "GOTO Conferences"
duration_min: 27
published_at: 2026-08-20T12:00:31Z
video_id: u7k1l_qkQH8
url: https://www.youtube.com/watch?v=u7k1l_qkQH8
youtube_url: https://www.youtube.com/watch?v=u7k1l_qkQH8
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOOT Book Club", "Jim Ledin", "Modern Computer Architecture", "Computer Architecture", "Computer Organization", "Hardware", "Hardware Foundations", "GPU", "Microchips", "AI Datacenters"]
topics: ["Inference, serving & GPU infra"]
transcript: true
---

# Modern Computer Architecture & Organization • Jim Ledin & Maciej «MJ» Jedrzejewski • GOTO 2026

**Speaker not identified**

`GOTO Conferences` · `GOTO` · `2026` · `27 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOOT Book Club` `#Jim Ledin` `#Modern Computer Architecture` `#Computer Architecture` `#Computer Organization` `#Hardware` `#Hardware Foundations` `#GPU` `#Microchips` `#AI Datacenters`

[Watch the recording](https://www.youtube.com/watch?v=u7k1l_qkQH8) · [Conference site](https://gotopia.tech/)

## Description

This interview was recorded for the GOTO Book Club. #GOTOcon #GOTObookclub

Jim Ledin - President at Ledin Engineering & Author of “Modern Computer Architecture and Organization” @jledin1
Maciej «MJ» Jedrzejewski - Tech Agnostic Architect & Author of “Master Software Architecture” @learnsoftwarearchitecture

RESOURCES
Jim

MJ

Links

DESCRIPTION
Jim Ledin — author of Modern Computer Architecture and Organization, now in its third edition — joins Maciej "MJ" Jedrzejewski to talk through the book's two brand-new chapters on GPUs and large language models, and the specific challenge of writing about hardware that changes faster than a book can ship. Ledin's approach was to focus on durable architectural principles (parallelism, memory bandwidth, tensor processing, and how systems scale from one chip to an entire data center rack) rather than chasing the current state of the art. For the LLM chapter specifically, he chose GPT-2 as the teaching example precisely because it's open-source and small enough to trace by hand — and because, as he explains, the transformer architecture underneath today's frontier models is fundamentally the same structure, just scaled up.

The most concrete takeaway for engineers: the AI buildout's real bottleneck right now isn't compute, it's memory bandwidth — a shift driving high-bandwidth memory production at the expense of consumer RAM, which Ledin illustrates with a blunt data point (a 32GB DDR5 stick that cost $69 a year ago now runs $440). But asked which single chapter would most change how a working developer with no hardware background thinks about their own code, Ledin doesn't point to AI at all — he points to the chapter on pipelining and cache hierarchy, arguing that most of the thousandfold speedup from 1980s PCs to today came from those optimizations, not clock speed, and that writing cache- and pipeline-friendly code is still one of the highest-leverage skills a developer can have.

TIMECODES
00:00 Intro
00:47 The Commodore 64 that started it all
04:36 Two new chapters: GPUs & LLMs
10:00 Why GPUs became AI hardware by accident
13:33 Training vs Inference: Same chip, different job
15:03 Why GPT-2, not GPT-5, is the best teacher
17:37 The data center is the computer now
18:41 The real AI bottleneck nobody's talking about
21:59 The one chapter every developer should read
25:43 Outro

RECOMMENDED BOOKS
Jim Ledin • Modern Computer Architecture and Organization • https://amzn.to/4wHMhQN
Jim Ledin • Architecting High-Performance Embedded Systems • https://amzn.to/3UpXl7z
Jim Ledin • Simulation Engineering • https://amzn.to/4qvylYQ
Maciej «MJ» Jedrzejewski • Master Software Architecture • https://leanpub.com/master-software-architecture

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*3,460 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=0s)** [music] >> Hello everyone and welcome to the Go to Book Club interview. I'm Mati Andrzej Anrzejewski and today I'm talking with Jim Ledin, an engineer, a CEO and a consultant who spent the better part of 30 years building embedded systems and testing their security. He's also the author of several books including the one that brings us together today, Modern Computer Architecture and Organization, now in its third edition. Jim, welcome to the show. >> Thank you MJ, it's great to be here. >> So, let's start broad. You've done a lot over years, penetration testing, FPGA

**[0:51](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=51s)** design consulting and written many books. So, when somebody at a dinner party asks, "What do you do?" What do you actually say? >> Um well, I'd say I start at the beginning. Um I've always been interested in computer hardware software and basically the boundary between them where we make things work. Um my first real exposure to um the architecture of computers and processors was in the 1980s. I had a Commodore 64 and I learned a little basic and wrote a program to do some screen drawing using the joystick and it was extremely painfully slow.

**[1:40](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=100s)** So, I took an interest in the assembly code. I got a book on 6502 assembly language and learned a little bit about that and found out how to use the capabilities within the basic environment to basically after hand assembling the code on pencil and paper, typing in the numerical values and storing them in memory, and then executing that code. And the amount that it sped up by doing that just blew me away. So, I'd say from that point I was interested in the the low-level hardware, the architecture of computer processors. Um and as you you've mentioned, I've I've built on that over the years

**[2:29](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=149s)** working on embedded systems, um doing penetration testing on systems, and um evaluating and implementing cybersecurity on those systems. So, that's where my focus is today is um basically all types of computing, but more with a focus on embedded and real-time systems and the architecture of those systems. >> You mentioned assembly language. I started years after you started because my adventure with assembly started in late 2000s, and it was uh when I was at university. Uh this was basically my starting point because I was studying electronics and telecommunication, then moving to C language. So, I still

**[3:17](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=197s)** remember this uh funny times using assembly. So, yeah. That that would that would that was nice nice thing. >> Yeah, we don't use assembly directly much anymore, at least unless you're really working at the very lowest levels of the systems, but understanding what's there, um what particular different types of processors, whether it's ARM or Intel or RISC-V is sort of optimized to do at the assembly language level can inform how you go about solving high-level problems on those systems most efficiently. >> Yeah. Yeah, yeah. I can agree. I can agree from my software engineering part

**[4:07](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=247s)** because I have never ever done hardware engineering, but with software engineering engineering it is always so useful when you can understand what is really happening behind the hood. I mean, for me every single engineer should know what is going on there because it is then allowing us to optimize processes, optimize our programs, and and so on. Not only in hardware, but also in software. So, yeah. That's that that's an important thing. Okay, but let's talk about the book itself. This is the third edition that I have here on my desk of modern computer architecture and organization. Originally written back, if I remember correctly, in 2020. And yeah, 2020. A lot has changed since

**[4:55](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=295s)** then. But two brand new chapters chapters really stand out. One on GPUs, one on large language models. So, most of this book covers architecture that's been stable for years. Things like x86 or digital logic, which don't really shift month to month. But when we talk about GPUs and LLM architecture, they do. So, how do you sit down and write a chapter about something that might already be partly out of date by the time the book ships? And did you do anything differently because of that? >> Well, like you say, the biggest challenge in trying to do that is trying to identify what aspects of these different

**[5:44](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=344s)** architectures and and system level capabilities are going to remain relevant for years into the future. So, rather than focusing too much on specific products or language models or you know, the current state of the art, it's really concentrated more on the architectural principles underlying all of that such as the the benefits of parallelism, um the importance of memory bandwidth, um what tensor processing is and and how it's applied in these contexts, and as well as the ability to scale um the system from being not just running

**[6:33](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=393s)** on one processor or one server, but something that runs at a level of an entire rack in a data center or possibly an entire row of racks. How are those things constructed? How are they connected to each other to provide the communication bandwidth that's required to get the level of performance that we all expect? Um that's really what it's been about. But I also do go into some specifics. Um particularly to understand how does a current generation uh GPU work? Um so, we we look in depth at uh one of the Nvidia GPUs. And and one of the things we find is

**[7:20](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=440s)** that as these um different models come yearly, typically, um they're not radical departures from previous generations. A lot of it is just putting more of the same kinds of capability into the chip, and um improving things like the memory access speed and that sort of thing. So, even though things change year to year, a lot of it stays the same and there's sort of incremental improvements. And so, in the hardware realm, we look at a GPU and in the software realm, we look at the the GP2 large language model, which was released in source code form and you can go out and download it and pick it

**[8:07](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=487s)** apart yourself. But, what we do is look at what the the transformer architecture is and how it um operates. Not so much the theory behind it, more looking at it like a mechanic as in how does this thing work? And if I wanted to fiddle with it, what parts of it could I go in and uh poke around with? So, GPT2 GPT2 was a fairly original um not the first, but one of the uh early models that really started to catch public attention. And it's also simpler than the current generation in terms of what size of matrices it uh implements and the number of layers within its uh processing stack. So, it's fairly easy to get your head around.

**[8:57](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=537s)** And so, if we work through that and understand how that works, then you can understand that the current generation that the frontier cutting edge is to a large degree just a bigger version of the same structure. So, a lot of the tensor architecture remains fairly constant. There's a lot of changes, but if you understand GPT2, you know a lot about the the latest models as well. >> Thank you. Yeah, I mean I had a lot of fun and it was so interesting to read about these things in your book. Uh I can only imagine uh how stressful was it like, "Hey, I am starting writing this chapter and yeah, everything changes around so quick, so fast."

**[9:46](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=586s)** Uh this is for example why when I was writing my own book, I just focused on some principles, architectural principles that do not change that fast over the years. So, I can only imagine it. And question, because you know, for me GPUs were originally built to render video frames for games. What was it about that original design that made GPUs end up being the right hardware for AI almost by accident? >> Uh you're you're right. It is almost by accident because GPUs were not originally built to do the kinds of processing that large language models perform. But as it happens, there is a great deal of similarity between the calculations

**[10:37](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=637s)** that go on to generate video images and the the processing in a language model. That the language models are based on an artificial neural network architecture. And a lot of that basically involves multiplying weights by signal strengths and then adding them up. And there are a lot of neurons in the billions or or more depending on what what language model you're talking about. And a very great deal like 80 to 90% of the processing comes down to matrix multiplications. Um they're described the data structures in the the models are described as

**[11:24](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=684s)** tensors which are multi-dimensional arrays. But when you multiply tensors by tensors In fact, that can be broken down into a series of matrix multiplications and then accumulating the results of those. And that's the level that the hardware on the GPU works at. It performs matrix multiplications on very small matrices like typically 16 by 16 and accumulates results from them. So, even doing a simple multiplication of two two-dimensional matrices that are bigger than 16 by 16 can be broken down into a larger number of matrix multiplications of subsections

**[12:14](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=734s)** of those two matrices and then basically adding up the results of them. And that's how an LLM works. And And that's also how a lot of the processing that goes on in the generating 3D images, whether it's orienting objects within a world space or applying the the coloring across those objects, tracing lighting within the the visual image, it shares some but not all similarities. So, GPUs have a lot of hardware that directly supports language models, but they also have other hardware that does things like color shading that isn't directly related to language model processing.

**[13:03](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=783s)** So, actually for the most extreme level, the the highest end models, the the tools that are used are called TPUs, tensor processing units, which are very specifically designed to perform the tensor multiplications of LLMs, and they don't in their their view of the world waste any of their processing power on things that uh uh would only be used for graphic images. >> So, speaking with that example, what actually happens on the hardware when a model like GPT-2 is training versus when it is running inference? Are those two workloads stressing the same parts of the GPU or completely different ones? >> There is a a lot of overlap because much

**[13:54](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=834s)** of the training process is performing the inference function, which is when you're you're using a GP uh a model to uh um ask it questions and that sort of thing. But, um it it provide in the training process, a set of input is provided to the model. Um it performs the inference process, and then uh the result basically gets fed back through the model to uh adjust the uh the weights within the artificial neural network structure. So, there is a lot of overlap, but it's not the same exactly. And as I understand, the uh GPU architecture is better aligned with the the training process,

**[14:42](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=882s)** and uh more specialized hardware, at least on the the very high-end models, uh in terms of TPUs, is what's being used to perform inference operations. Basically, when users go and and access the model and and uh ask it their queries and uh perform their agentic tasks on it. >> For that large language model chapter, you mentioned uh that you used GPT-2 as your case study, rather than one of today's frontier models. And you mentioned that's because it's uh open, so you can actually see the source code. >> It is open, and it's relatively small compared to those to the current models. So, it's easier to talk about and a 1,000 by

**[15:30](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=930s)** 1,000 array size rather than a 300,000 by 300,000 and try to keep track of those numbers as you're trying to go through the chapter and understand what's being multiplied and and how many mathematical operations are taking place, that sort of thing. >> That's basically the question I just wanted to ask you. Exactly this one. Like, what does looking back at a smaller, older model like that reveal about LLM architecture that gets hidden when small models get as large as the ones running today? But, obviously you answered that question. You know, I still remember the situation. It was with GPT-2 around 2019. I was amazed by it. And I showed it to a few people in business roles at

**[16:17](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=977s)** that time and their reaction was basically, "Yeah, that's another university research topic." And obviously that didn't age well. And I'm very happy that with large language models and with ChatGPT and all the other parts, there is finally kind of spotlight on artificial intelligence because I remember back then while studying at university and then years after that, I was very interested in this topic of artificial intelligence, but it was almost always treated by the business as yeah, something theoretical that maybe maybe might bring some value to the company, but then it was very hard to get some data about machines. For example, when we are

**[17:07](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1027s)** talking much about machine learning and trying to forecast things that could happen to these machines. So, yeah. I mean, this GPT-2 stayed with me for very long and I was so happy to read here in this book about GPT-2 use case. So. >> Great. And the the jury is still out on whether the value provided by these models to to businesses is going to exceed their cost as time goes on. >> Yeah, I I mean that's that's a very important point here because when we talk about data center scale demands behind today's largest model space, power, cooling, at what point does this stop being a GPU

**[17:56](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1076s)** or problem and turn into a completely different kind of engineering problem? >> And that's the challenge of architecture cuz you're you're not building a chip or a system. The entire data center is really a giant computer with an architecture that is it's critical that it be done in a way that maximizes the value and minimizes the cost like the uh cost of the surrounding environment, the water consumption, the power consumption, the the noise, the the heat that gets radiated from the site. Those are all considerations of the overall architecture. >> So,

**[18:43](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1123s)** looking at where GPU and LLM architecture is heading next, is the next bottleneck going to be compute, memory, power, or something nobody's really talking about yet because we just don't know? >> So, the I would say the most immediate issue is memory bandwidth and and that's uh the specific driver of uh the >> [clears throat] >> um current basically shortage of uh consumer grade memory uh is being driven by because uh I just checked on Amazon uh for a 32 GB um stick of DDR5 RAM. A year ago it was $69.

**[19:31](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1171s)** Today is $440. And a large part of that is caused by the um um growth of what's called high bandwidth memory which is uh basically an architecture of memory modules where several like 16 or more um chips uh are stacked atop each other inside one uh integrated circuit package uh um each of them containing uh several uh gigabytes of memory. So, it's an extremely dense uh memory structure. And that's what's going into the the highest end processors that uh use for artificial intelligence like the uh

**[20:20](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1220s)** Nvidia Blackwell architecture and the TPUs. And it is the the high bandwidth memory is much more expensive than the uh consumer type memory. And this is where the memory manufacturers are focusing a lot of their um manufacturing work now. It's building these more uh profitable for them uh memory devices and building less of the consumer type devices. So, we can expect that all of our uh devices, our phones, our tablets, our PCs, and other things like cars are going to have price increases because memory is in all of them and memory is a lot more expensive now. Um but what is actually driving that

**[21:09](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1269s)** is the uh need for memory bandwidth, being able to read and write memory as fast as possible. So, high-bandwidth memory, as it right there in the name, um, you can the processor is able to read and write a lot faster, and that turns out to be a significant bottleneck for the uh language models is they have these extremely large tensors, they need to move them in and out of memory as fast as possible. A lot of the time, the processing is constrained more by memory bandwidth, meaning you're wait waiting for uh reads and writes to finish, um, more than you're actually doing computing on the data. >> And that's a great place to leave it. Looking forward, I would say.

**[21:59](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1319s)** A last question, because uh we are coming up on time. If a working software developer with no hardware background, like me, only has time to truly absorb one chapter of this book to immediately change how they think about their code, which chapter would you point them to and why? >> Um, I'm having a hard time remembering chapter numbers, but there is a chapter that's specifically about um uh performance improvement techniques. And what this goes through is the ways that modern processors use the features of memory caches and pipelining to uh accelerate processing. Um, so much of the uh

**[22:52](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1372s)** thousandfold, at least, um increase in speed from the earliest PCs in the 1980s to today is not driven so much by clock speed increases that the clock driving the rate of instruction execution in the processor as it is in the optimizations that result from pipelining and cache memory. So, pipelining is basically where instructions are partially executed as they flow through a series of stages and at each stage you at each moment in time there may be many instructions partially executed. So, from the software developers point of view, you

**[23:40](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1420s)** don't want to mess that up. And putting in things like branches and interrupts and that sort of thing can disrupt that flow. So, for the the most performance intensive parts of application code, it's important to understand how pipelines work and to avoid anything that inhibits them from doing their best work. Similar with memory caches, processors these days have multiple cache levels. The level one cache is the fastest and closest to the processor core. So, work that can be completed without having to go outside the level one cache once it gets loaded with data is going to run as fast as possible.

**[24:30](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1470s)** Level two and level three caches are larger and slower. But each time the work overflows into another cache level or worse, overflows from all the caches and has to go back and forth to memory, there's a significant performance hit. So, by organizing code and algorithms and data in a way that takes the best advantage of pipelines and caches, uh you can get the best performance out of your code. >> Yes, this is something that I constant continuously observe um in software development world, unfortunately, that we are throwing components over components. We are adding uh new things, then we are increasing RAM, we are increasing CPU,

**[25:20](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1520s)** and so on and so on. Definitely, nowadays, it's very easy because if we are leveraging cloud environments, it's just something that yeah, you can scale. If you want, you can scale. So, this is something with software development world that always hurt me. So, yeah, that's uh that's a very very valid input. Jim, thank you very much for this fantastic conversation, for joining us, and for being so open about both the hands-on stories [music] and the technical side of where this is all heading. It was a pleasure to talk with you. Thank you very much. >> And thank you, MJ. This was a great discussion. I appreciate the uh invitation to the GOTO Book [music]

**[26:08](https://www.youtube.com/watch?v=u7k1l_qkQH8&t=1568s)** Club. >> Subscribe to the GOTO YouTube channel now and join the experts in person or online at any [music] upcoming GOTO conference using the promo code Book Club. Visit gotopia.tech to learn more. [music] >> [music] [music]
