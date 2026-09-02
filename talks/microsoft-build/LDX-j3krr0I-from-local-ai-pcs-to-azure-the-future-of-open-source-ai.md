---
id: LDX-j3krr0I
title: "From local AI PCs to Azure: The future of open-source AI development | LIVESP128"
slug: from-local-ai-pcs-to-azure-the-future-of-open-source-ai
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Adrian Macias"]
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-05T14:23:15Z
video_id: LDX-j3krr0I
url: https://www.youtube.com/watch?v=LDX-j3krr0I
youtube_url: https://www.youtube.com/watch?v=LDX-j3krr0I
tags: ["Adrian Macias", "From local AI PCs to Azure: The future of open-source AI development | LIVESP128", "LIVESP128", "LIVESP128_v1", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# From local AI PCs to Azure: The future of open-source AI development | LIVESP128

**Adrian Macias**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#Adrian Macias` `#From local AI PCs to Azure: The future of open-source AI development | LIVESP128` `#LIVESP128` `#LIVESP128_v1` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=LDX-j3krr0I) · [Conference site](https://build.microsoft.com/)

## Description

AI development workflows are changing rapidly as developers experiment with agentic AI, AI-assisted coding, and increasingly flexible deployment strategies. In this Microsoft Build conversation, AMD and Microsoft discuss how open-source AI ecosystems, Ryzen AI PCs, ROCm, and Azure infrastructure are enabling developers to experiment, adapt, and scale AI workloads with greater flexibility across evolving AI environments.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Adrian Macias

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVESP128 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Host welcomes Adrian to discuss innovation at scale
00:00:45 - Adrian highlights transformation in developer experience over six months
00:02:27 - Excitement around how machines and outcomes are transforming
00:03:13 - Innovation through iterative design approaches
00:05:12 - Emerging AI modalities and multimodal interaction
00:06:44 - Challenge of human decision-making and the emergence of Agentic AI
00:07:06 - Agentic AI as a microservice evolving over traditional software and hardware
00:10:40 - Embracing experimentation and courage in developer culture
00:12:05 - Redefining quality in AI beyond model accuracy

## Transcript

*2,558 words · source: supa (en, exact timings)*

**[0:07](https://www.youtube.com/watch?v=LDX-j3krr0I&t=7s)** SPEAKER 1: Welcome back to the broadcast stage here at Microsoft Build. We're in the beautiful city of San Francisco and boy, are we talking about innovation at scale and speed. And no one is better at talking about that than my friend Adrian. We're going to have a great conversation, Adrian. Welcome back. ADRIAN MACIAS: Thank you. We sure are. I'm excited to talk about the developer experience with you. SPEAKER 1: Absolutely. It's really important that we're able to help developers understand what's different for them and make sure to give them real actionable items and help take them deep. Talk to me about something that you're really excited about that we've been talking about here at Microsoft Build. ADRIAN MACIAS: Well absolutely. I think one of the most exciting things is the developer experience itself and how that is radically changing. Just in the last six months, developers are exploring spaces and trying new things that they practically couldn't do before.

**[0:59](https://www.youtube.com/watch?v=LDX-j3krr0I&t=59s)** And I think it's the confluence of a number of different things. There's technology, there's software, there's agentic AI, there's hardware platforms. I'm really excited to dig into all of that with you today. SPEAKER 1: I know that you have a passion for the developer community. Do you ever find all of this overwhelming? I mean, sometimes to me, I'm more of a builder than a pro dev. But nonetheless, sometimes I find all the change a bit overwhelming to keep up with and understand. How do you do it? ADRIAN MACIAS: It's difficult. Certainly, I think the idea was trying to become an expert at things is historically how we've worked. And now it's really just about becoming an experimenter, trying things, not being afraid to take risk and trying new approaches to solving problems. That's the time we're in right now. I think that's what's at bear (phonetic) for developers. SPEAKER 1: One of the things

**[1:47](https://www.youtube.com/watch?v=LDX-j3krr0I&t=107s)** that I find sometimes a little bit overwhelming is all of the changes that are happening so quickly. I mean, I'm more of a builder than a pro developer. But nonetheless, how do you figure out how to keep track of everything that's happening? ADRIAN MACIAS: Well I think the key to developers today is that that approach to solving problems is fundamentally changing. Whereas in the past, we had to commit to a plan, the cost to commit to that plan, and the investments that we'd make with resources and times was really critical. Now, the cost to explore is zero. And so it's really easier (phonetic) to try different things. SPEAKER 1: Yeah, and that ability to experiment almost at scale with all the new things, do you think that's fun? Do you enjoy that? ADRIAN MACIAS: Well, it's fun. I'm more excited about what comes out of it. And I think that's what engineers and developers want. They want the end product. What am I creating?

**[2:34](https://www.youtube.com/watch?v=LDX-j3krr0I&t=154s)** And what's happening right now is the machine has fundamentally changed. So what's coming out of the machine is also fundamentally different. And that is exciting. SPEAKER 1: Explain that, the machine has changed. What do you mean by that? ADRIAN MACIAS: So if you look at what's happening with AI coding or agentic AI, it's changing our process on how we approach problems. It's changing the flow that we use, the decisions we make, the choices that we even have at our disposal, which means I can take more risk, I can try new ideas, I can try new tools. And if it sticks, it's great. And if something doesn't work quite right, it's okay to just put that code aside and try a completely different approach. And so, that really fosters an era of innovation. And that iteration lets you end up at places you might not have with a traditional design approach.

**[3:22](https://www.youtube.com/watch?v=LDX-j3krr0I&t=202s)** SPEAKER 1: Yeah, it's almost like surprise and delay at scale with the developer (phonetic). ADRIAN MACIAS: There is. In music or art, we talk about happy accidents. I think engineers are starting to enjoy this design space as well. SPEAKER 1: So how does that play out between AMD and Microsoft and (inaudible) specifically? ADRIAN MACIAS: Yeah, that's really key. Because tools and technology are only part of the problem. But you have to foster that community. You have to foster that innovation. And that means having an open ecosystem with open software, open platforms, and really investing in that community of developers so that they create that innovation that we're all depending on. SPEAKER 1: And how do you do that at AMD? ADRIAN MACIAS: Well, open source software is really a key pillar to what we're doing. Putting software out in the open source community, exciting the developer community with events like this so that they're coming to the table and bringing their ideas.

**[4:11](https://www.youtube.com/watch?v=LDX-j3krr0I&t=251s)** We have a number of different ecosystems that we participate in where we have more developers coming in and contributing their ideas than AMD may even have developers contributing to that codebase. So it's really just, how do we create that energy and excitement around the industry? SPEAKER 1: I think developers also, historically, but now more than ever, they want to get their hands dirty, they want to actually do the things that matter. If there are a few things that you would have developers physically doing, what would that look like? ADRIAN MACIAS: I think the key is to explore a couple modalities in the choice space. So if you think about one of the new dimensions to explore, it's where things are running. Right, so in the past, I might be doing my developments simply on the cloud and exclusively on the cloud. Now, I have the opportunity to explore something like an AIPC and do significant AI development there.

**[5:02](https://www.youtube.com/watch?v=LDX-j3krr0I&t=302s)** I can also decide where my workload is going to run. It's perhaps even a hybrid solution between a cloud and a client device. That's the idea of locality. The other new innovation that's happening is modality. We now have new AI technologies that can listen to us speak, that can watch our face, and detect our emotions. That we can text with them and chat with them, but we can also generate images and rich media content. So the modality that we have choices over is significantly more significant than it was just six months ago. And thirdly, we also have new devices that we can explore. So we have CPUs, there are GPUs, there's also neural processing units that are in a lot of these AIPCs. And that gives us a new type of capability that we can explore to trade off cost or power or performance in ways

**[5:51](https://www.youtube.com/watch?v=LDX-j3krr0I&t=351s)** that we didn't have before. So my advice is get out there and explore these different design choices. We have a developer showcase where you can attend and listen to a lot of the sessions and demos and presentations that are here this week to learn more about those. SPEAKER 1: And what I love about that is you don't have to be right here in San Francisco to do it, of course. There's a large digital audience for this particular show. And all of these sessions are available online. People can participate in them. And it's really democratizing access to this learning and intelligence, and it's free. Right, I think that that changes the way that developer ecosystem can evolve. And what do you see happening in the next three to six months in that developer ecosystem based on some of these announcements, new modalities that you're talking about, new form factors, and compute?

**[6:41](https://www.youtube.com/watch?v=LDX-j3krr0I&t=401s)** ADRIAN MACIAS: Well, it's interesting. One of the challenges we have with choice is that we are not inside the box, right. Humans are not in there, our brains are not programmed into the box yet to make some of those choices for us. But we have the emergence of agentic AI. And this is a solution to this existential problem of so many choices, how do we create options, how do we control the technology that we've created? So agentic AI is a new microservice that's evolving on top of our traditional software solutions, hardware platforms. And so this is going to be an interesting space to see change over the next six months. I think we're going to see more applications developed in a dynamic fashion. Rather than static features or static capabilities, we're going to see solutions and software emerge that adapts

**[7:30](https://www.youtube.com/watch?v=LDX-j3krr0I&t=450s)** to the user and the user needs as they're interacting with the software. SPEAKER 1: And I also think about, to me, it seems as if developers now have to think also about orchestration, about the multiagent ecosystem that may exist. Their particular solution may not exist all by itself. It may be interacting with other components that it doesn't even know yet, or maybe haven't even been invented yet. How do you think about that part? ADRIAN MACIAS: Yeah, it's similar to what we were just describing is there's a need to have a dynamic intelligence in the systems that we're building and the software that we're shipping. Because there are so many choices and options. We need to refine those choices around, what problem are we trying to solve? Is cost important? Are we resource constrained? The cost of memory these days is a key design choice. So looking at those different cost parameters

**[8:20](https://www.youtube.com/watch?v=LDX-j3krr0I&t=500s)** and making intelligent decisions about the choices that we make. I may choose to run something local simply because tokens are so expensive right now. Or I may choose to push something to the cloud because I really want the quality of that result. And that's the opportunity that agentic AI is presenting to us. SPEAKER 1: When I think about that, I also, of course, think about security. And how are you thinking about, how do you want our developer community to think about security as they experiment, as they think about this explosion of agentic experiences, and as they choose the locations where they're having things run? How do you think about that? ADRIAN MACIAS: Yeah, there are many layers to that conversation. I'm excited about the work that Microsoft is doing in this space. Security is fundamentally a platform solution. So we need to think about it from the user level, the user's data, all the way down to platform access,

**[9:10](https://www.youtube.com/watch?v=LDX-j3krr0I&t=550s)** networking, file access, and different types of security, firewalls that may go on the platform itself. What I'm excited about are some of the emergent capabilities in routing on the platform. So, for instance, if I'm running a workload here on my local AIPC, but I'm also connected to the cloud, I want to make sure my personal information is secure. So we now have technology that has the intelligence to listen to the things I'm asking and route my personal information to remain local on the platform and still leveraging the power of the cloud and foundation AI when I need it. SPEAKER 1: What I love about all of this is it feels like our creativity as builders and developers is really being unleashed with all of these new capabilities.

**[9:57](https://www.youtube.com/watch?v=LDX-j3krr0I&t=597s)** How do you think about that? I feel like if I was a new developer, or if I had been in the ecosystem a long time, all of a sudden, basically, the sky's the limit. There are limitations, the technology's still evolving, but how do you think creativity plays a part in all the change that we're dealing with right now? ADRIAN MACIAS: I fundamentally believe in the saying that says the speed of innovation of proportional to the speed of iteration. And I think the faster we move, the more creative we get. And so, this is a time, this is a technology that's making us all more creative, just by virtue of moving faster, trying things over and over again, and seeing what comes out of that, that beautiful experiment. SPEAKER 1: Some of us call that building the playing hall, flying it (phonetic). But I love your interpretation of that.

**[10:45](https://www.youtube.com/watch?v=LDX-j3krr0I&t=645s)** I think that that is fantastic. Because I think that that willingness to experiment at speed and scale, there's a certain courage to that, right, that I find in the developer community as a whole. Willingness to tinker, willingness to experiment. Tell us about some of the other things that we announced here at Build between Microsoft and AMD and why they matter to the developer community. ADRIAN MACIAS: Well, one of the more exciting projects that my team is working on is the WinML SDK. And the importance of that is democratizing the platform for developers, right. So there are many different hardware technologies, many different software technologies. The speed of iteration means there's quite a bit of fragmentation in the ecosystem. And so, sometimes, it's difficult for developers to choose which direction they need to go

**[11:33](https://www.youtube.com/watch?v=LDX-j3krr0I&t=693s)** or where they're going to get the best performance or solution. So the work we're doing together with Microsoft is creating a platform that's scalable. But it's also lowering the friction for developers. So they're not having to make very low-level investments in a specific technology, they're able to leverage a rich, robust ecosystem around this SDK and begin their development at a much higher level of abstraction. SPEAKER 1: Anything that accelerates the work of developers, I feel like is a good thing. Because it gets them that much closer to that output that you were talking about. Do you have any advice for how people really understand the quality of their output in these new solutions? ADRIAN MACIAS: The idea of quality is fundamentally changing as we add layers to the stack. So we used to think about quality in AI

**[12:22](https://www.youtube.com/watch?v=LDX-j3krr0I&t=742s)** as like the simple accuracy of a model. Like, is this a cat or is this a dog? And you could quantify your quality that way. And as we introduced LLMs, the idea of quality changed. Well, is it quality around summarizing my document or is it quality around answering questions or eighth grade math? And so, how we evaluation AI is becoming equally more sophisticated. Now with the emergence of agentic AI, we're having to invent whole new concepts around quality. How do I know if the agent is making good choices? If it's routing my data to the best solution? There's really no deterministic way of categorizing that. So we're inventing the idea of quality and how we measure quality as well. SPEAKER 1: I love that.

**[13:08](https://www.youtube.com/watch?v=LDX-j3krr0I&t=788s)** I find that freeing because I think it was due for that change. So I want to thank you for your time. ADRIAN MACIAS: Thank you. SPEAKER 1: I love having a conversation with somebody who's clearly passionate about the technology, but also the people who are in the community. That is wonderful. So thank you so much. ADRIAN MACIAS: Thank you for the opportunity. SPEAKER 1: You can always go deeper on AMD's Showcase page. We want you to go find it at build.microsoft.com. There's article, there's information, there's demonstrations. So many great things about it. Make sure you go and check it out. And thanks for joining us. We'll see you again soon.
