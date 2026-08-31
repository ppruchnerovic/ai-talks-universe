---
id: 82WO6R--wxo
title: "How we ship models in VS Code | LIVE161"
slug: how-we-ship-models-in-vs-code-live161
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Visual Studio Code"
duration_min: 16
published_at: 2026-06-05T13:37:14Z
video_id: 82WO6R--wxo
youtube_url: https://www.youtube.com/watch?v=82WO6R--wxo
tags: ["How we ship models in VS Code | LIVE161", "Julia Kasper", "LIVE161", "LIVE161_v1", "Seth Juarez", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# How we ship models in VS Code | LIVE161

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `16 min`

`#How we ship models in VS Code | LIVE161` `#Julia Kasper` `#LIVE161` `#LIVE161_v1` `#Seth Juarez` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=82WO6R--wxo) · [Conference site](https://build.microsoft.com/)

## Description

Shipping the right AI model for each task requires a lot of testing and evaluation. Get an inside look at how the VS Code and Copilot teams assess model quality, decide when to roll out updates, and balance capability with reliability.

To learn more, please check out these resources:
* https://aka.ms/VSCode/GHRepo
* https://aka.ms/VSCode/DBview
* https://aka.ms/VSCode/HarnessBlog

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Julia Kasper
* Seth Juarez

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE161 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Introduction at Microsoft Build with Julia from VS Code team
00:00:22 - Julia shares background as VS Code Product Manager
00:00:35 - Discussion on generative coding era and model selection complexity
00:01:47 - Explaining differences between model families and personalities
00:03:00 - Introduction to the concept of AI harness and its role
00:04:39 - Demonstration of DJ Julia project and harness debugging tools
00:07:15 - Comparison between different models' behavior using same prompts
00:09:23 - Importance of collaborative model optimization and prompt tuning
00:11:00 - Process of model evaluation, benchmarks, and iteration
00:15:21 - Closing thoughts: continuous optimization and feedback in AI model deployment

## Transcript

*3,049 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=82WO6R--wxo&t=0s)** Welcome back. We're here at Microsoft Build and I'm super excited to be here with Julia. How you doing my friend? I'm doing fantastic, thank you. The thing? I love about Build is we get to talk about the cool stuff behind the scenes and we get to ask all sorts of questions. We have a live audience here as well, so they might ask some questions. Why don't you tell us who you are and what you do? Cool. And my name is Julia. I am a product manager on the VS Code team. I've joined the team last year in August and yeah, it's been a fun ride. But The thing is, is that you just don't work on VS Code. Like let me aint the stage. We're in a gentic coding era. Like for me, it started last December and we we kind of go and we pick the model and we just happily just go along and pick a model and it seems super easy. But that's what you work on. Yeah, it's not as easy as it sounds, right?

**[0:47](https://www.youtube.com/watch?v=82WO6R--wxo&t=47s)** Yes, so I thought the same thing. Funny that you say this. I'm like, you know, I'm in VS Code, I'm using the chat extension and from time to time like a new model shows up and I'm like, oh great, I'm just going to use the new one. And now since I joined the VS Code team, I'm in charge of or I'm helping the team, not in charge of, but I'm helping the team. It's very collaborative and what all goes into releasing these new models in our VS Code extension. And it is a ride, I can tell you that much. It's not as easy as, oh, we get a new model endpoint and boom, here it is. And it just works. There are so many things and pieces that go into this from us working very closely with the model providers and like getting their insights and what the new model is all about. So yeah, there are a lot of things that go above and beyond here.

**[1:35](https://www.youtube.com/watch?v=82WO6R--wxo&t=95s)** So I'm just picking the thing and I'm like, these things are all compatible or are the same. Can you give us a sense for how not the same? These are all like all very special flowers, whether they're from a certain company or from a certain type. Tell us about that. Yeah. So I think the biggest aha moment for me was even within the same model family, let's pick the GBD one, OK, GBD 5.4 to 5.5. Even within this model family, it kind of had its own new personality and we had to adjust our coding harness to it. And that's why we work very closely with them because for us the models are also a black box. And so we are getting getting their insights like what has their research team on worked on and making the new model endpoint better. So truly it's like every new time you're getting a new model, it has its own personality even more across

**[2:25](https://www.youtube.com/watch?v=82WO6R--wxo&t=145s)** different model providers like Anthropic and Open AI, these even differ even more. But even within the same model family or like model provider section, it's already very very different. So we talk about models, even from 5.4 to 5, we talk about personality or characteristics, trait. And you talked about the harness a little bit too. Do you have to make changes to the harness for every model? And if people don't know what a harness is, can you help them understand what a harness is and how new models make it so you have to change? Them totally, yeah. So I brought a little bit of. A. Let's go to the screen. Here load chart diagram. OK. And just to give a very high level of hey, these are all of the steps that we have to think about. And as I mentioned, we work very closely with the model providers. So it's very I thought it was very processy. Oh yes, of course, we learn about this new process.

**[3:15](https://www.youtube.com/watch?v=82WO6R--wxo&t=195s)** It's very casual. The model providers reach out to us. They're like, hey, our research team told us we have something that is working. And then our entire team from the Copilot API team that gets the new model on boarded to to also us and client side like VS Code, we all go in and we start working. And in particular, we work on optimizing the harness. So what is this harness? The harness itself is the system, the environment, your AI or your LLM is running. Essentially the LLM only provides or gives back tokens. But how do we make changes? How do we edit files to how do we run in terminal? So this is what we consider our harness and these are all of the changes we have to make sure it works once a new model comes up.

**[4:03](https://www.youtube.com/watch?v=82WO6R--wxo&t=243s)** And there are four very important things we always look at whenever we have a new harness. It's our system prompt. So for every model, for every different model across even different model providers, we have our own system prompt. We have different built in tools that these models can call. And even across different model providers, they tend to call different tools as well. So we have to make sure the right tool sets are being called. And then also context management. Different models have different or work with different model context. And then also the agent loop and how do we call it? How do we load tool so we just have to make sure it works end to end? So hold up. So you effectively every time you get a new model, every model gets its own special flower kind of situation in the harness.

**[4:53](https://www.youtube.com/watch?v=82WO6R--wxo&t=293s)** So that for us as we're using this, we really can't tell. Yes correct. Well actually. So let me switch over to my stable. Can you hit control plus a couple of times of? Course, there you go. All right, so this is a fun little project. It's called DJ Julia. Control plus one more time because I'm. I'm old. There you go. There you go and it's just like a fun little project that I have. And so right before this session, I created this prompt, which is hey, for my DJ app, I want you to create a new music pattern for me. And just to kind of show you, first of all, everyone can go in and explore what the harness does whenever we make these calls to the LLM. So you see a bunch of styling, it does a bunch of different things rise, it's searched. So whenever you switch to our chat debug logs, you

**[5:43](https://www.youtube.com/watch?v=82WO6R--wxo&t=343s)** can really see all of the different things that is happening behind the scene. So. Hold on, you went really fast. Let's pause for a second so there is a chat debug log where you can see effectively every step the harness. Has taken exactly every step, every tool call. What is the system prompt that is being applied. So here, for example, let me close this real quick and you can see the request message is being separated between the system prompt. And you will notice, so this one is with the GBD 5.5 model. If you would do the exact same prompt with let's say Opus 4.6, it will have a different system message as well. That's how we optimize and we make sure every new model gets the latest and best together with the model providers that we work on because they clearly know the

**[6:31](https://www.youtube.com/watch?v=82WO6R--wxo&t=391s)** model so much better. And it also helps us to really optimize and make sure it works truly end to end as well. And then also if you're interested in seeing all of the different tools that are being called as an example, and the GPD model family always uses apply patch versus the anthropic models that you'd insert and insert files. So just someone nuances how different all of these models truly are. So you talk about like how different? Is there a way you could show us like how they are different? Sure, let's I mean let's try this here. So use this let's go back and for everyone to see. I use this using the GBT 5.51. So let's just do this with the Opus 4.71. I'm doing the exact same prompt.

**[7:23](https://www.youtube.com/watch?v=82WO6R--wxo&t=443s)** So first of all, also another challenge we have in the AI space, even using the same exact same model, it is nondeterministic. So every time you run this even within the same model family, you would always get a different input or output. But just to show you how much they differ even across within the same harness and just having the different model here. Yeah, because I mean, this thing is sampling, you know, according to distribution of the of the model's output. I like to say stochastic process as much as I can. It's like a $5 word, makes you sound really smart. I don't know what it means all the way, but that's what they told me. But effectively, this is all probabilistic, and so it's going to be different every time, even when they're the same model. Exactly. OK, So what do you got? So all right, if you remember what we had before our system prompt, let's go here.

**[8:18](https://www.youtube.com/watch?v=82WO6R--wxo&t=498s)** There you go. So this was the system prompt we had previously. Just going to close this and it does like a bunch of pre classification checks and stuff like that. So now if we go to the latest one that we trusted with the cloud one, you can see the instruction files are different with the GPD 5.5. We had something to make sure it inserts before because the GPD 5.5 ones, they are more prone to immediately go and run in terminal. But we wanted to hey, first explore a little bit and then go and run it because we have seen so much more success with these kind of system prompts rather than using the ones that you previously had with 5.4.

**[9:03](https://www.youtube.com/watch?v=82WO6R--wxo&t=543s)** And all of this was worked together with the Open AI folks. And this is this is really impressive because like betwixt us friends, I built my own harness in Rust and I started changing models assuming that it was and things just stopped working. So you effectively have to, when a model comes out, it's like, all right, gang, let's get together. Let's figure out what the right prompt is. Yes, let's figure out how they do tool calls, et cetera. You have to do all of that work. Exactly. Yeah OK. I mean, I love that you're building your own harness, but one of the benefits for using our built in one, and there's no harm in building your own and of course making your own changes is we, we do work very closely with them. And we are truly, truly optimizing for all of the new checkpoints. And we are optimizing in a way that it will hopefully work for most folks out-of-the-box.

**[9:51](https://www.youtube.com/watch?v=82WO6R--wxo&t=591s)** And you don't have to worry about it because we know how much work that actually goes into always updating and making these changes. And that's one of the benefits for using GitHub Copilot and. My my harness is nowhere near as skillful as theirs and it's literally for helping me write stuff. And so notice that even for a separate task. Does your harness has to be different or is this all optimized for writing code? That's optimized for writing code. That's why you see in the instruction file usually, usually the very first one is, hey, you're an expert AI programming assistant. We're. So we are putting the model in context of where it is. It's in a coding environment. It has to make sure it is not just like giving you text and it is going in, it is using our built in tools like run in Terminal, all of these things to make sure it works in the

**[10:41](https://www.youtube.com/watch?v=82WO6R--wxo&t=641s)** environment we are kind of grounding it into. So I'm assuming you're not like, oh, we got a new model, everybody, let's just use the last one and changed a couple of words, see what it does. I'm sure there's like a better process to do this kind of testing. Can you tell us? Yeah. So to be very honest, and a lot of the times whenever we get a new checkpoint, the very first thing, and this is something we get from the model providers, they tell us just use the system prompts from the prior model and let's just see how it goes. And we're like, OK, I guess because they're also. So the reason why they want us to do that is they want us to see how good it already is without doing all of the optimization. Yeah. And how do we measure this? So we measure this by running a bunch of offline eval benchmarks.

**[11:29](https://www.youtube.com/watch?v=82WO6R--wxo&t=689s)** We do this by internal dogfooding. So these are two in parallel things that are going on. And once we have these benchmarks run, we share the results with the model writer. And then based on that, they are like, oh, OK, I see it's already maybe better, but let's start tweaking and let's start going in. How about this? So then we sometimes have had like a model where we basically just removed everything and we're like, OK, we have to start from scratch here. And then we optimize it and optimize it to make sure whenever the model launch stay is and it truly is the the the perfect model to hit the crowd. So, but I, but there's got to like, for example, I'm, I'm a traditional dev, I did some machine learning. We we had things called evaluations. We do things as devs, as unit tests.

**[12:18](https://www.youtube.com/watch?v=82WO6R--wxo&t=738s)** Do you have something like that that you systematically run through to improve the prompt or see like, hey, it's this good, but now it's this good? What? What does that look like in your process? So our process here and this probably is going to touch a little bit of evals. And so yes, we have offline evals especially we run these before the launch, after launch. We also still optimize the harness, which is very important. It's not never a ship and of course it's always like we go in and we iterate even after. So what are the benchmarks or how do we evaluated? There are a bunch of public benchmark out there sui bench one of the very known ones and and we still run these even though there are a lot of conversations, controversy around these public benchmarks, one of them being and the model providers have told us directly as well.

**[13:07](https://www.youtube.com/watch?v=82WO6R--wxo&t=787s)** The, the models are so smart now that you're always kind of going to get this. So use this as a regression test rather than really evaluating the quality of it. So we still run these, we share it, we see if the model has regressed, We use it for optimization of our harnesses as well. But then the more important one is we use or we have our own internal benchmark, which is called VSC bench and it currently has 100 and plus tasks or instances that we run every time. So before launch, we run across different reasoning efforts. We make some changes to the system prompt as an example. We see how it changes and we look at these, what we call model report cards and to see how it's performing against.

**[13:53](https://www.youtube.com/watch?v=82WO6R--wxo&t=833s)** It so you're not just like Yoloing a model out. You have a full benchmark of a bunch of stuff that you're testing. Can you show us a little bit the card that helps us show us? Awesome, So I did this this morning. Can you? Control plus a couple. Of times. Sorry, yes, you're good. Thank you. So I ran this this morning and basically how it works is and we have a VS Code Insiders instance in an ACA. So whenever we run our offline evals, we spin one up, it's always using the latest. So I ran it this morning. So it truly has the latest insider version in it. And how I did this, I ran it against GBD 5.42 times and GBD 5.5. Typically we try to run it five times because of the non deterministic problem that we have with AI.

**[14:42](https://www.youtube.com/watch?v=82WO6R--wxo&t=882s)** And so then a next step, this is where it gets really exciting is the performance tricks. We look at the resolution rate. So resolution rate is, was this task successful or not? And we evaluate this by certain assertions we have and we think of it like a checklist and it goes through and says for this test case, was it resolved? Did it hit all of the check marks? Yes. And then it's resolved and it goes in and shows 153 out of the 248 test cases were resolved. And this is how we can compare across the different models. This is pretty amazing. So what should developers take away from this? We've got about 45 seconds. And first of all, always keep trying new models. Give us feedback if there's anything that doesn't work as

**[15:32](https://www.youtube.com/watch?v=82WO6R--wxo&t=932s)** expected. We are continuously operating and doing this and also I've done the same. I gave a model A1 try kind of thing. But because we are putting so much effort in these models, just make sure to maybe sometimes come back and give it another try. And also then evils, offline evils are a huge topic and anybody building their own coding harness, it has been one of the tools that we as Microsoft have been super successful and the model providers are loving. So definitely a space to dig more into. Awesome. Well, thank you so much for being with us and thank you so much for watching. We'll see you after this. Thank you.
