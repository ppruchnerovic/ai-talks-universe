---
id: Agc6Ik00R1g
title: "How Microsoft AI builds coding models optimized for GitHub Copilot | LIVE158"
slug: how-microsoft-ai-builds-coding-models-optimized-for-github
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Visual Studio Code"
duration_min: 16
published_at: 2026-06-05T13:35:25Z
video_id: Agc6Ik00R1g
youtube_url: https://www.youtube.com/watch?v=Agc6Ik00R1g
tags: ["How Microsoft AI builds coding models optimized for GitHub Copilot | LIVE158", "LIVE158", "LIVE158_v1", "Pengcheng He", "Pierce Boggan", "Seth Juarez", "Yang Liu", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# How Microsoft AI builds coding models optimized for GitHub Copilot | LIVE158

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `16 min`

`#How Microsoft AI builds coding models optimized for GitHub Copilot | LIVE158` `#LIVE158` `#LIVE158_v1` `#Pengcheng He` `#Pierce Boggan` `#Seth Juarez` `#Yang Liu` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=Agc6Ik00R1g) · [Conference site](https://build.microsoft.com/)

## Description

Go behind the scenes with Microsoft AI to learn how to build and optimize coding models for GitHub Copilot. This session will explore what makes code-focused models different—from training and evaluation to performance, safety, and real-world developer feedback. You’ll hear how Microsoft AI is advancing model quality for the workflows developers care about most, and how those innovations show up in GitHub Copilot experiences used by millions of developers.

To learn more, please check out these resources:
* https://aka.ms/MAI/GHCP
* https://aka.ms/GHCP/automodel

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Seth Juarez
* Pierce Boggan
* Yang Liu
* Pengcheng He

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE158 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Introduction and Microsoft Build AI Model Overview
00:00:28 - Introducing the Mai Code Flash Team and Project Goals
00:01:00 - Purpose-Built Model for GitHub Copilot and VS Code
00:02:48 - Reinforcement Learning for Real Developer Workflows
00:03:50 - Multi-Stage Training Pipeline and Environment Alignment
00:05:27 - Model Size and Mixture-of-Experts Architecture Explained
00:10:20 - Demonstration of Mai Code Flash in VS Code
00:13:06 - Interactive AI Agents Demo Combining Multiple Mai Models
00:15:16 - Developer Takeaways and Future Model Enhancements
00:16:07 - Closing Remarks and Call for User Feedback

## Transcript

*2,904 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=12s)** Hello, my friends, We are back and I I love AI and at build Microsoft build this year, there was a ton of models released. I think there were seven Mai models released, but one of the ones that was super interesting to me because I'm a dev is Mai code flash and I have some of the researchers here with us. We're going to ask the hard hitting questions and I'm going to try not to sound dumb because these are the smart, smart dudes. Why don't you tell us who you are and why don't you do? We'll start with. You. Hi everyone. I'm young. I'm the. Research lead part. Of this model. Hey, I'm Hunter, a leader. The different in my coder. Yeah, that model. So this particular model was specifically built with GitHub copilot in mind, is that right? So Peng, why don't we start with you?

**[0:58](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=58s)** What does that actually mean? Yeah. As to me the purpose building model means we didn't take a general purpose model and adapted it for code at the end. But actually we build from a very beginning for GitHub capacity scenario and we optimize it for GitHub compiler experience from very beginning. So for for those that are like thinking like OK MAIMAI code Flash was optimized with VS Code Copilot in mind, what does that mean for people? What you mean is it's not just the genetic code snippets. It will understand the the positive context that use tools, understand the users intent and make a targeted edits and they respond quickly.

**[1:47](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=107s)** Especially for GitHub capacity users, we will optimize for the real user workflow. I see. So why don't you tell us more about how what that looks like in practice when you optimize for BS code? Yes, so I think. It means it's not just good at some benchmarks, it's definitely good at many benchmark, but in the real suite. Of. Code engine. It also means like it interacts with you in your proper. Way it asks your. Questions without long thinking. For some simple questions, do the unit test at the correct time. At the right time it. Do the proper. Testing. So it basically. Optimize for the best user experience in US code. So tell me more about that because like I, I, I was trained in machine learning and effectively what I understand models to be is it's this huge structure, you push a lot of data through it, some linear algebra

**[2:37](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=157s)** and calculus to optimize it. Tell me about the data that you're specifically pushing through it to make this model super good for VS Code users. That's a very. Good question, SO. That's why reinforced. Learning plays a very important role here. So which means in this training with last model interact. With the real. Product partners with. Real web code. With the same 2 sets that. Developer use every day. With the same prompts you use. Every day. And you can interact. With the web. Wall with the environment like daily sweet tasks and we can create a reward model with a lot. Of like Easter tasks for field for you. And. Does it like have very proper product behavior? And also many things that you think the model should do the best. For your daily task. And it's all be done by very reinforcement with real product harness.

**[3:27](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=207s)** I see. So there's a base model and then you're doing reinforcement learning on top of it to adapt the behavior. Is that right? Tell us what? About that is multiple stages. The universe learning is the last stage to make the model perfectly aligned with user exchange in GitHub. So tell me more. So you're doing, you're actually when you're training the model, you're training it with the actual BS code stuff. Is that right? Tell me about the stage. When we train that model, we have multiple stages. We started with supervised fun tuning to make the model follow user instruction and response with aligned format. And then we gradually train the model with a lot of diverse data in a criminal way from simple task, simple coding task to complex coding task stage by stage. And the final stage is that we use reinforcement to make the model to learn in the real environment as

**[4:16](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=256s)** a productive. So and the real scenario, real environment, as they say, close to product. So that we make the training evaluation and the production in the same same workflow. So that that's the difference from our model that's depends on our model from like you know, the purpose model. And this is so cool because I want to, I want to restate this because I, as I'm hearing this, it's it's kind of super cool. You basically have a base model and you do supervised fine tuning first with simple tasks, then with more complex. It's almost like it's you're taking it to school on how to be a good programmer. Simple task, more complex tasks, and then you test benchmarks over the top of that. Is that right? Yes, and this benchmark is not another benchmark. So this benchmark is customized to use the same environment as a product use the same harness.

**[5:08](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=308s)** So it's a it's a it's a purpose built model for people that use this harness. Yes, that that's really cool. So this is cool. Tell me about the model size, because one of the things I tell people is, hey, if you're doing a generic task and you're not sure you got to use a pretty big model and then learn and then make a fine-tuned small model. Tell me about the model size here and why that particular that particularly matters. Yeah, Mai code 1 flash is a 5B mode active parameter model, but it actually Moe model. So the total capacity is about. 137 billion parameter. So which is fairly. Large I think model site plays a very. Important role here is like. It cannot have a trade off between the model intelligence, the speed and the cost. That's the. Three things that we care about.

**[5:55](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=355s)** And with this large Moe model but with more active parameters. It actually achieved. A balance point or sweep point? For your daily sweep tasks, you. Don't. Need to waste a lot of. Tokens but you. Still have very. Powerful models for. Your daily work. Yeah. So tell me more about that because you said a 5 billion parameter model, but you're using a mixture of experts. So tell me how that works. So for people that haven't heard that, what does that look like? So basically. I imagine it's a neural model and you have a lot of parameters, but in each token inferred only need to activate a part of them and that part of them will. Serve a task. The rest of them can be activated. For other tasks, other tokens. So which means the each inference only part of networks activated and.

**[6:42](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=402s)** This saves a lot of costs. Yeah, so, so the model total model is only 5 billion parameters or? No. Total model is 137 parameters. But only active at a single time is the 5 billion because of the mixture of experts. And this is the this is the cool part that people that I love about this machine learning has gotten so good that what a mixture of extra effectively shuts off an entire part of the model using nice vector calculus and it pushes the exact query through one of the experts so that you're actually getting super fast inference speed. So effective model size is 5 billion parameters. Yeah, not just one expert inside mixed on many. Experts yeah. That's amazing. So what does that mean for speed and accuracy? So if you look at our blog, our model, you can.

**[7:28](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=448s)** See the. Latency of the model is super good comparing with the same quality and intelligence. And also I think when I mentioned we also optimize model for token. Efficiency so. If you combine model efficiency and token efficiency, you will find it. Just a beast at its size. It's just fat. Yeah. Because it's like, it's like a big model with little models that together make it a little bit faster. So what what has been the most exciting part for you and challenging parts of building of building this model? Actually, there's a lot of change, as I said, from beginning the model, just put the next token so it can actually follow user instruction or to use tools. So we need to do something called a code start to make the model can follow user instruction and do some simple reasoning task. So basically it can just like children, we start from

**[8:18](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=498s)** a very, very young baby and make it graduate, go up to a post doctor. So that's a good deal. The first step is kindergarten, right? That's good to start. And after that we can keep the model, make the model keep climbing and to the higher level. Yeah. So a lot of folks when I look and this I fall into this trap because maybe, I don't know, we like biggie sizing things. Sometimes we fall into this trap of thinking that a bigger model is going to be better at specific tasks and that's not always the case. Sometimes a smaller model can be even better. Why is that the case in in for Mai flash? So I think model size matters a lot of intelligent, but not all of it. We take good careful. Training. We use the same harness. Of very proper.

**[9:06](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=546s)** Design data for this model to make sure the model can always climb on its reward in training. So I think the outcome is very good. It's not. It's not just limited to its size. Very powerful model. OK. So I think you've brought something to show us. Can you show us what we've got? So we're going to go to the screen here and you brought a little bit of something to show us in action. Is that right? Yes yes. So. What I'm showing is a demo we just made. This is using our model in West code developing a front end web app. You can see the model. Is very fast you. Give it a problem, it do a lot of things like the token on the fly is. Super quick. And use the customer training with W code to it and use the native West. Code very efficiently. And in the end you can. See. It developed a.

**[9:53](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=593s)** Very nice looking app in a very short time and I think here's another demo. It's a bit. Different the model is prompted to build. AI will say a ritual style. Game and you can see this. The UI is pretty good, we do put a lot. Of efforts on improving the models front end ability and with the native partners in training. Yeah, you should use it. Pretty efficiently, yeah. Yeah. And this is pretty cool because now this particular model is available in VS Cover people to use. Is that right? We are. Rolling out the model gradually and you can. Use if you.

**[10:40](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=640s)** Got the model, you will see your model picker. So what has been the funnest part about building this model? Because like in this case, it's, you're building a frontier model, but for a very specific use case. What are some learnings that you've had along the way? Well, learning I think users real workflow is important for us to optimize their model for users purpose, yeah instead of another benchmark. So without using the capacity 10 minute grounding task, we cannot even make them model work as perfect as today in compiler. And can you tell us a little bit about how you test these models so folks get a sense for because you're not just like doing weights, but you're testing these models as they go. Tell us about the testing process. So definitely we have very good benchmark results if you look at the.

**[11:28](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=688s)** Broad across. Many benchmarks we, I think it's frontier model at this size. As Pauline said, we also. Care a lot about your user experience. So that's why. We do a lot. Of AB testing online to make sure the model. Fulfill your task. Your engagement with models is crap. You don't cancel too much for the model. So if you've used this model, tell us what the experience has been like using this model. You said it's a little snappier, it's a little faster. Tell us about the experience. To me, I think for most of the task, it's comparable to today's frontier big models. But just for some challenge tasks, we must recognize this deal that's getting low. We cannot disability that's getting a small model still has some limited for challenge, but for most of the daily work I think this work works good for me.

**[12:19](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=739s)** So generally when we go from a bigger model to a smaller model, it it gets very focused on the particular task that you fine-tuned it for. What are some things that like people should not expect it to be? You know what I'm saying? Because I don't, I don't want people to use the model and be like, wow, it's not writing poems for me or something. Tell us about what are some things that are super good at and what are some things that maybe you should use other models for? So I will say for most of our daily. Suite tasks. Back end from the end different program language. It's a very good model, but the writing poem do. A lot of like creative. Writing things, we are not optimized for that, but I can still do something. But maybe you should ask our models. Yeah. Cool, so I hear you have one more demo. Can you show us that one and this one?

**[13:08](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=788s)** Does this one have audio? This one has audio. OK, so are we equipped for audio Tom on this one? We are ready for it. OK, they're ready for it. By the way, Tom's awesome. This is for fun can. You maximize it. I can start coding agents, give them tasks. That sounds cool. Can you run the web app locally so we can start testing? I got it. Let me work on that. I need your approval to start the week development server. Sure, I approve. The development server started on local host app. Thanks. Can you now change the background color of the web app to a gradient of blue and green? I got it. Let me work on that. The agent updated the project.

**[13:58](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=838s)** Thanks, Now can you check what kind of unit tests we have and see if there's any missing and cleared them? I got it. Let me work on that. The test suite is ready to run. I need your approval to execute the NPM. Sure, I approve. The agent added unit tests for the profile header. What's going on with the agents right now? One moment checking. All three agents are actively checking the current app structure. One is planning to refactor components into a RE, so why don't we just tell us what we just looked at? So this model is kind of especially our weekend apart. We combined our latest state of art Mai Transcribe model, Mai Voice model and Mai Code Flash model for this

**[14:48](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=888s)** fun project. And that's kind of cool because now that you now that you have specific purpose built bottles, you can start to put them together and do some some really, really cool things. Tell us about how you came up with this. I think it's very natural when Mai comes all these seven models. Together, so it's. Kind of natural to think how we can combine and how we can imagine. The suite developers in the future. So that's very natural project. So what should developers take away from all of this? We'll start with you and then we'll come to you. Take away. I think imagination is important. We can imagine in the coming few months we have even better sense come out. Fantastic. What about you? I think my take away. Is we are. Seriously, treating the best model. For our product the best. Code and other product.

**[15:34](https://www.youtube.com/watch?v=Agc6Ik00R1g&t=934s)** And this is just the beginning of our journey. Please stay tuned and looking. Forward to what? Will happen next. That's amazing. And so as developers try this out, make sure you give us feedback because I'm sure you want feedback on how the models. Work. Yes yes. Feedbacks are very. Welcome a lot of feedback. And you're going to continue to improve this model and do work. Is that right? Tell me about the future of this. So definitely I want to mention we need feedback so we can improve the model and this is a mini sized model. Just stay tuned for some more powerful beasts. Awesome. Well, thank you so much for spending some time with us. It's been amazing. I'm a nerd. I love this stuff. So thank you so much. And we'll be back right after this. We'll see you.
