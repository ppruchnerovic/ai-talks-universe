---
id: gkocotnw56o
title: "Local models, developer control, and the future of AI runtimes | BRK235"
slug: local-models-developer-control-and-the-future-of-ai
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 20
published_at: 2026-06-04T13:03:05Z
video_id: gkocotnw56o
url: https://www.youtube.com/watch?v=gkocotnw56o
youtube_url: https://www.youtube.com/watch?v=gkocotnw56o
tags: ["0f29bea1-6955-4ec3-8c51-5a80b47dcf7b_M9Z7-BRK235-1", "Agent Observability", "Azure DevOps", "BRK235", "Local models developer control and the future of AI runtimes | BRK235", "Michael Chiang", "Parth Sareen", "Purview", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Local models, developer control, and the future of AI runtimes | BRK235

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `20 min`

`#0f29bea1-6955-4ec3-8c51-5a80b47dcf7b_M9Z7-BRK235-1` `#Agent Observability` `#Azure DevOps` `#BRK235` `#Local models developer control and the future of AI runtimes | BRK235` `#Michael Chiang` `#Parth Sareen` `#Purview` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=gkocotnw56o) · [Conference site](https://build.microsoft.com/)

## Description

How local and hybrid model execution is reshaping developer workflows, privacy, and experimentation. Why “run it yourself” is back.

Seating for this session is first-come, first-served. Add it to your schedule to plan your day and arrive early to secure a spot.

To learn more, please check out these resources:
* https://aka.ms/build26-next-steps

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Michael Chiang
* Parth Sareen

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

BRK235 | English (US) | Working with models

Breakout | (300) Advanced

#MSBuild

Chapters:
0:00 - Introduction by Parth and Michael from O Llama
00:01:17 - Developer compatibility with major APIs and SDKs
00:07:02 - Examples: Media Company, Manufacturer, and Automotive Use Cases
00:10:31 - Introduction to hybrid execution combining cloud and local models
00:13:03 - Demonstration of easy setup and installation of OpenClaw
00:14:47 - Response about current focus on desktops and laptops, with mobile support experimental
00:15:19 - Audience Q&A begins
00:15:48 - Discussion of quantization and MLX support for NVFP4
00:17:45 - Introduction of MLX inference engine for Apple devices

## Transcript

*2,988 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=gkocotnw56o&t=10s)** Hey everyone. My name is path and I work on agents at Olema. I'm Michael, one of the co-founders of Olema, and today we'll be talking about open models for agents and how hybrid local cloud models are playing in together to make agents a reality. If you're having trouble listening to us or hearing us, there's headsets at the back, so feel free to go and grab one just as we get started. Take it away. Awesome. Has anyone here heard about Olema before? Wow. Okay, that's quite a bit of people. I'll still. I'll go quick on the background. But what is llama? Llama is really the easiest way for developers to access open models and use it with your own

**[0:56](https://www.youtube.com/watch?v=gkocotnw56o&t=56s)** tools. Llama is the easiest way in one command to be able to run a model, to just get started by chatting with it or. Recently we introduced this command llama launch to be able to integrate open models directly with your favorite tools. This could be cloud code, VSCode, GitHub copilot. By using llama launch directly injecting the open models into these harnesses. And of course, for developers. Building on top of these open models, we have OpenAI and anthropic API compatibility for you to build your own applications. If you have Python or JavaScript applications. We also have a great SDK for you to build out on top and llama, since the

**[1:44](https://www.youtube.com/watch?v=gkocotnw56o&t=104s)** beginning has been really built for agents. This means we specifically test llama for tool calling, having structured outputs, and have one line agent set up for bringing all these models to llama platform. And right now we have over 8 million active developers using llama, and we partner with major model labs and hardware companies to continue to bring model launches and hardware optimizations to llama. So just this morning, Google DeepMind announced Gemma for 12 B unified model, and it's already available on llama, and you can use it for your genetic applications. And recently, starting this year, we added

**[2:34](https://www.youtube.com/watch?v=gkocotnw56o&t=154s)** Llamas Cloud to augment the local inference piece as well. And this is a piece where your data is never trained on. It has zero data retention. What it's meant to do is being able to run frontier models on data center grade hardware. And this way, if you don't have the compute locally, you're able to scale with llama and continue to run the models that you want. And a lot of these use cases that are enabled with llama are things like parallel agents to really accomplish difficult work that you couldn't otherwise do with smaller models. And all these models come with the maximum context window from the model providers themselves. And this is, of course, completely optional service that you can use with llama. Now, open models are

**[3:26](https://www.youtube.com/watch?v=gkocotnw56o&t=206s)** quickly improving. This is just one of the suite bench verified for illustration purposes, but really the open models are enabling mainstream use cases at significantly lower prices. And we're seeing a lot of these mainstream use cases, maybe not frontier research like DNA synthesis or frontier coding applications. Users with mainstream tasks are able to begin to use these open models for. And we'll show you demos of that and give real life scenarios of where that's happening today, and giving users the flexibility to customize your models and run it with the parameters that fit with your goals. How open models have really improved

**[4:16](https://www.youtube.com/watch?v=gkocotnw56o&t=256s)** capabilities and really evolved in the past, we've seen models really come with just pure general chat, and over the the months that followed, we really saw models quickly evolving to having reasonable reasoning abilities to be able to start thinking, and then models evolve to be able to pick up individual tools and multiple tools. And we're starting to see more open model labs become beginning to release models that are capable of tackling long horizon tasks. So these are tasks that can run for hours and days. And these are just starting to happen. And so in the future, we should be beginning to see much more of that unlock happening. Some of the use cases that we've seen

**[5:06](https://www.youtube.com/watch?v=gkocotnw56o&t=306s)** in real life and really private. So these are published papers that where a lot of the users have talked about where they are publicly using llama, the Lawrence Berkeley National Laboratory, they have they have an accelerator assistance system to autonomously execute physics research for X-ray. And they basically have a routing layer that chooses between cloud models and llama in order to do their inference. And this is what their accelerator ultimately looks like. And this is llama powering their X-ray research. There's also the NASA Glenn Research Center. They have a crew and health crew,

**[5:54](https://www.youtube.com/watch?v=gkocotnw56o&t=354s)** health performance, probabilistic risk assessment, and they use llama to categorize a diverse set of Mars mission tasks. And they go into 18 predefined human system task categories in order for their future missions. The US Department of Energy with Brookhaven National Laboratory also integrates llama to facilitate log data analysis, and this is one of their setup together with Lang Chang that they use, allowing users to be able to use a GUI to be able to do summaries of their log information and retrieve specifics on the issues and solutions through natural language. And there are other

**[6:44](https://www.youtube.com/watch?v=gkocotnw56o&t=404s)** developers in enterprises already using llama to automate their mission critical tasks. For example, a multinational media company processes financial documents for their quarterly earnings review and SEC filings. And these are very sensitive data to that they use, and it just cannot be sent to other cloud AI models or providers. And this is where their use case for llama lies. A leading industry manufacturer has an assistant internally using llama to design machine parts. And this is all for their mechanical engineers to do CAD design, motor automotive manufacturing is using llama directly on the factory floor. And this is leveraging

**[7:32](https://www.youtube.com/watch?v=gkocotnw56o&t=452s)** retrieval, augmented generation on their knowledge base and inspection system for their factory technicians. And we'd love to pass it to path for a quick demos on what llama looks like. Cool. So I'll cover a bunch of different things that we can do, and hopefully you'll walk away with a better sense of everything llama can do for you now, especially both local and cloud. So one of the things that a lot of you probably know us for is, you know, the classic bread and butter chatting with a model. So you can see here, a big focus that we have is to focus on both local and cloud and have the experience feel the exact same. So you want to do a larger task. You want to use a bigger model.

**[8:20](https://www.youtube.com/watch?v=gkocotnw56o&t=500s)** You use cloud almost the same way you would use a local model. So as Michael mentioned, we introduced llama launch earlier this year. And essentially it's a way to connect to all your favorite tools and applications for whatever you'd like to do. So we support personal agents like Open Claw Hermes, as well as a plethora of agentic harnesses to do coding agents and coding work. So here's a list. We have cloud code, Codex, copilot, CLI, droid Pi, and many, many more. And many more are also coming. So I'll show you a little bit about how it's super easy to plug llama into any of these favorite tools

**[9:07](https://www.youtube.com/watch?v=gkocotnw56o&t=547s)** that you may have. And I'll showcase copilot in this case. So as I mentioned earlier, you just type llama launch copilot, and you can pick the model that you'd like. So in this case I'm using Kimmy K 2.6 on our cloud, but just as easily you can use a local model as well. And one of the things I really like about the copilot CLI is that you can directly pick which issues you want to work on. And so in this case, I'm like, okay, go and fetch this issue. Let's see what it's doing and let's come up with a solution for it. So it's thinking likes to think a lot sometimes. And you know, it's come up with exactly what's going on in the issue. And I can use this as part of my workflow to directly without

**[9:54](https://www.youtube.com/watch?v=gkocotnw56o&t=594s)** ever leaving my terminal and leveraging these open models to do real work. And this is a workflow that I'd often do in my day to day. So I ask, are there any open PRS referencing it? It says no, and then we start working on a fix. And so any other agent harnesses that you've, you know, used llama powers them similarly as well, where we make sure that the underlying technologies work, things like subagents, web search, etc. So over here, it's spun up multiple subagents to go and explore the code base and come up with potential fixes. Just skipping forward a little bit basically gives me a little bit of a plan, and then I can execute on this plan and get my work done. Another thing I feel is so critical is this

**[10:44](https://www.youtube.com/watch?v=gkocotnw56o&t=644s)** idea of hybrid execution. So cloud models, especially the ones that we serve, which are very, very close to frontier level intelligence, they are awesome. For your most difficult work when it comes to coding or any other agentic tasks, but there's a lot of stuff you want to be extremely, extremely private for. And this is a workflow that I often use in my day to day or quarterly, as you'll see, which is my credit card statement. And so this is not my actual credit card statement. That would be a little bit weird, but it is a fake one. And so this is some, this is a pretty usual workflow I'll do at the end of every month. I'll basically go take my credit card statement and put it into one of my favorite harnesses called pi. So pi is a really minimal harness if you

**[11:32](https://www.youtube.com/watch?v=gkocotnw56o&t=692s)** haven't heard about it. And it's perfect for local models as the entire point is that it doesn't bloat the system prompt, it keeps everything super minimal. So in this case, I'm using 3.6 running locally on my MacBook, and I'm basically going to say, you know, process this statement and show me kind of how much I'm spending, what are the different categories. And so let's see it in action. So this is running fully locally on my computer for my most private and private use cases. And in this case it's able to write code to process the PDF. And now it's able to give me a little bit of a spending breakdown because it's not processed that information. So let's see. It's doing a bit of math to figure out exactly

**[12:23](https://www.youtube.com/watch?v=gkocotnw56o&t=743s)** what's going on. And then there we go. So none of this information ever left my computer. It's been here. It seems like I'm spending a lot on travel. Guess I'm overdue for another vacation. But I think it's really, really useful to be able to have this level of like, good enough. And a big thing we've seen over the last few months is that you truly have this idea where local models are actually viable to do real work. And another really cool thing that I personally really like using is using local models for personal harnesses. So personal agents like Hermes and Open Claw, because none of your information ever leaves and you can kind of start feeding it information. Everything's living on your computer anyways. And so I'd love to show you

**[13:12](https://www.youtube.com/watch?v=gkocotnw56o&t=792s)** open claw. One of the cool things that we can do with open claw is install it for you. And so this is like a complete end to end setup. I wrote a launch open claw ran it. It's installing open claw lets me choose a model and gets me set up right with it. And so within like 30s, I'm able to go from absolutely nothing installed to and running open claw instance ready to do my work for me. Cool. And with that, we'd like to open up the floor for any questions that you may have around local cloud Olama. So welcome to come up to the mic and then we'll also hang around

**[14:00](https://www.youtube.com/watch?v=gkocotnw56o&t=840s)** after. Yeah as well. Yeah. Hello. It's working. Well, I was wondering, since the focus is on this, part of the focus was on running on devices. Sorry. Would you be able to speak louder? Sure. I'll try. So I was wondering, since part of the focus is on running on the device itself, what are your thoughts on edge devices like mobile phones or smaller systems that may not have the same power as a laptop? Sorry, just to repeat the question, did you mean what type of models are good for different systems? I'm not necessarily what type of models, but specifically if there are plans to have olama integrations directly at the edge for, again,

**[14:50](https://www.youtube.com/watch?v=gkocotnw56o&t=890s)** maybe iPhones or Android devices that may not have the same power as your regular Mac. Yeah, we haven't targeted mobile devices yet. There are people who have experimenting, being experimenting bringing olama on mobile devices, and it does run so absolutely enabled on Qualcomm Snapdragon devices. And it's the same chipset that runs on mobile. And we have seen users do that. We're not directly targeting mobile devices yet because we want to target the mainstream use cases for work. Thank you. Any other questions? Feel free to hop on to the mic or raise your hand and we'll guide you over. Oh, do you want to go up to the mic? Yeah. Can you talk a little bit

**[15:41](https://www.youtube.com/watch?v=gkocotnw56o&t=941s)** about Vram and unified RAM and sort of model sizes, context windows? I'm I saw that at least in the demo, you had a 262 K context window. What kind of a machine do you have and what are the specs. Yeah. Is it a quantized model for sure. So obviously like in llama, we have a default quantization that we recommend for most things. And now we also have support for ML where we actually run Nphp4. And with all that I have a maxed out Mac. So I can run a full context length, especially with a smaller model and get most of my work done and not really have to worry about compaction as much. Because what tends to happen as soon as you're running a workloads locally is you start running into being

**[16:29](https://www.youtube.com/watch?v=gkocotnw56o&t=989s)** hardware constraint where you can't support the maximum context length. So unified memory is great in the sense that it lets you have larger context lengths with a slight trade off of that speed that you would get on a Cuda card, for example. But at the same time, you get to work a lot more with a larger memory. So you get to support harder and harder tasks. And I'm sure that as time goes on, even unified memory will get better in terms of performance and speed. And on the hardware front, we've been seeing most of the hardware partners are getting into unified memory. Started with Apple. Nvidia and Microsoft just announced RTX spark that has unified memory up to 128GB. Of course, AMD has the strict Halo platform that also can go up to 128GB, I

**[17:19](https://www.youtube.com/watch?v=gkocotnw56o&t=1039s)** believe. And so we're seeing across the board different hardware teams moving towards unified memory. Hey, I'm building on Apple silicon devices, building on device platform for models that are running on iPhone and Mac OS and Vision Pro, also watch OS, I tried a couple weeks back. Are you still using llama CPU under the hood? Any plan to build your own inference engine, by the way? So we do have our own ML inference engine. So if you are on an Apple device, highly recommend using that one. Just because you get faster performance. And for that, you

**[18:07](https://www.youtube.com/watch?v=gkocotnw56o&t=1087s)** just need to pull one of the ML models from our model registry. Thank you. Any other questions? Yeah. Yep. 128 gigabyte Mac is the most powerful. Sure. So the question was what's the best coding model on 128 gigabyte MacBook? Honestly, one of my favorites is 13627 B, if I'm remembering correctly, as well as Gemma, I kind of use them in pairs to go and write like smaller scripts for me for the most part, honestly, like a little bit underrated, but even the gpt2 SS120B works really well for doing scripting and

**[18:57](https://www.youtube.com/watch?v=gkocotnw56o&t=1137s)** other tasks. Yeah. Cool. Awesome. I was going to add the Gemma for dense models are actually really performant, and you'd be able to run them on a full context length as well. Yeah. So overwhelmed by yeah. So, so the question is like, how do you choose which model to use? It really depends on kind of your task for coding. You know, different models will perform better versus like personal agents sometimes, or even if you're just using for like a chat use case or classification for whatever reason. And a big way that I recommend people to go about choosing a model is honestly like trying a bunch out. We're going to start doing better

**[19:45](https://www.youtube.com/watch?v=gkocotnw56o&t=1185s)** recommendations in terms of, you know, if you're using a certain harness as part of a llama launch, you'd be able to see kind of which are the up and date models, which you can use best for your system as well. But for the most part, if you're building like a bespoke app, then the best thing you can do is try a bunch out, benchmark it, and see which one you prefer the most. Yeah. And I think with that, we'll conclude this session. We're going to hang around for a while. Come chat with us. W
