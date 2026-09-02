---
id: Hx0cmcDlmSU
title: "Programming robots | LIVE141"
slug: programming-robots-live141
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Chip Huyen", "John Maeda"]
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-04T14:05:24Z
video_id: Hx0cmcDlmSU
url: https://www.youtube.com/watch?v=Hx0cmcDlmSU
youtube_url: https://www.youtube.com/watch?v=Hx0cmcDlmSU
tags: ["Chip Huyen", "John Maeda", "LIVE141", "LIVE141_v1", "Programming robots | LIVE141", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Programming robots | LIVE141

**Chip Huyen, John Maeda**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#Chip Huyen` `#John Maeda` `#LIVE141` `#LIVE141_v1` `#Programming robots | LIVE141` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=Hx0cmcDlmSU) · [Conference site](https://build.microsoft.com/)

## Description

AI is taking over the digital world, and it's exciting to see how AI can be used in the physical world. Once we have a robot, we need to figure out how to program it to do what we want. This demo shows how we can interface with multiple robots using the same API.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Chip Huyen
* John Maeda

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE141 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Overview of discussion on practical AI systems and robotics
00:05:13 - Introduction to Unitary, a profitable robotics company
00:06:56 - Advancements in robot motion through pre-captured movement demos
00:07:56 - Explaining Vision-Language-Action (VLA) Approach
00:08:13 - Challenges in Collecting Robot Action Data
00:09:23 - Developers Facing Rapidly Evolving AI Primitives
00:10:50 - Speaker reflects on not being good at online trends and shifts focus
00:11:44 - Example of safety design from 1X robot — intentionally weak grip for safety
00:12:06 - Following design rules for safe distance between robots and humans

## Transcript

*2,774 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=0s)** Hello everyone, you are lucky to be here with my friend Chip Yan. Oh my gosh, everyone know AI engineering. Come on that book. Yes, change your life. OK, so we're going to we're going to cover practical AI systems and zoom all the way into the 3D World robotics. And so, Chip, First off, can you tell me about the ChatGPT moment you described and when ChatGPT came out, what happened in your mind as a machine learning AI expert? Oh. So hi everyone. My name is Chip. I'm very sad to be here today. So I wasn't telling John just like when tragic came out, I had this moment of like, I think I had two months of like existential crisis because suddenly I felt like what, what is my purpose?

**[0:47](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=47s)** Like if I can do so many things so well? And I think it's like a two things that I have always like thought of myself as being good at. One is writing and the other is coding and both what of the tasks are the top tasks that AI could automate? So it took me a while to understand. So I spent a lot of time talking to people like understanding how AI is doing, try to evaluate a lot of tasks and try to figure out like where AI is headed. And a lot of the learning became the book engineering. And also it helped me understand what I want to build for the future. And it's, I thought it so interesting how like you, an expert, also felt the existential crisis. I think like there is something about like some more. I think like you, we have thoughts that like, OK, because I work in AIAI shouldn't caught me, shouldn't catch

**[1:36](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=96s)** me off guard, right. But I think there was some miscalculation because I had thought that a lot more thoughts are like a small improvement in AI will lead to a small improvement in use cases, right, which is not true. As a human, we are terrible at evaluating like how useful something is, right? Like if the AI Jerry something like a little bit like not fluent. I think of AI as being stupid. And then suddenly from not super fluent to like super fluent in like a very short period of time and we suddenly like it. Get before I could do like maybe 10 tasks and now I can do like 1000 tasks. So the miscalculation come from like OK, small improvement accuracy somehow literally huge improvement in like usefulness. Oh my gosh, I felt so much better when Chip said that, by the way. So Chip, physical world, Yeah.

**[2:23](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=143s)** So you were talking about South robots and robots sitting down. Not an easy thing. So, so, so part of my existential crisis after I I I follow AI more is that I tried to decide like what would be the kind of things that AI would not be able to sow in the next like 2 to three years, right? I don't want to spend like a lot of energy or like 2 years has doubt beating something And then the new version of like Clot or new version of like open AI when just like I like eliminate it, right. So I think I realized something. It's like the human mind turned out to be a lot easier to models of the human body. So first of all, we can see this AI can answer your legal questions, can help you like write good essays, can write amazing stories and write amazing programs.

**[3:12](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=192s)** But I have never seen a humanoid that can sit down properly. I'm not sure has anyone ever since like a humanoid can sit down gracefully. Like there are a lot of funny videos and you see this like, so actually like a human emotions turn out to be a true really extremely difficult to like model. And another thing is that like a lot of time when for the AI to operate the digital world, we usually have regular documentations, right? Like if we call, like, let's say, if we call the GitHub API, we kind of know, OK, these are the functions that we can call. And if we can call with the parameters, his expected return code, like what is the form? What is the like types that we can expect? But for there's no such thing for physical world, right? There's no such thing as say, OK, for an app, if we press as much pressure, it's going to break, right?

**[3:58](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=238s)** If we step on the child, it's going to die. OK, I feel like it's this terrible example, but I'm just saying this like we really learned about like the environment descriptions and like feedback loop by interacting with it. And for for for AI to operate the physical world. It has what you learn all of that and it's extremely hard to like each AI owner that information. As a really higher accountability in the physical. World yeah, like for going about like talking about sitting down right? Like how do you describe to robot? OK, if you want to sit down, probably you have to put the mask here. You have to put the feet here like you just because it's very easy to just like flip over when you're trying to sit down. So when we go from language to the physical world, I mean, you've taught us how to use language, How do we do physical world?

**[4:47](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=287s)** What? What can we take from the semantic world to physical world to say, maybe I can do robots? Yeah, so, so actually like the progress in the AI, actually it makes robotics a lot easier. So anyone, anyone here interested in robotics, anyone here want a human eye at home to have you do a laundry or like a few? Well, I have bad news for you. It's going to be a while. So, so, so I think like do you know about Unitary, the company, the Chinese company that's very cool robot. So they're fighting for IPO. So Unitary's one of the very, very rare robotic companies are actually profitable and they're fighting for IPO. And the CEO has a really good talk when you talk about robotic intelligence as two things. So one thing is reasoning, right?

**[5:34](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=334s)** Reasoning is about, OK, like we asked a robot to like go and fetch me water. Then you would need to think, OK, the water is over there. I need to go and pick up the cup, turn on the tap, get water and bring it to the human. So that's like reasoning and planning. And the other one is motions. So the motion means is that like maybe the robot knows what to do. But if you stand up and then it flip over, we don't think that the robots are dumb, right? So for the for the reasoning part, I think that it actually very similar to the reasonings for the agent take AI nowaday, because like AI is very good at like take a task and reason step by step on how to accomplish the task. So reasoning is something that we can treat like do quite well with AI nowaday. The hard part, the hard part for reasoning is like the environment feedback, like OK, like it has to know

**[6:23](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=383s)** that, OK, if it press too hard, the F is going to break. If I put the weight here, then it's going to fall. So, so that kind of like feedbacks that we see a lot of people trying to teach AI what is called like 1 modelling, like trying to encode information about the physical world so that AI learn how to operate in it. So we see a lot of start-ups raising a billion of dollars, right? They faithfully has A1 modelling startup, Yaliku has A1 modelling startup. And there are a lot of like others, fancy researchers studying like companies doing it. So it's very exciting space. The other part is like motions. So a lot of have you seen the demo of like robots doing a Kung Fu or this is really, really cool. So a lot of those movements are actually pre captured. So, so like complicated movement, like you program, like, OK,

**[7:13](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=433s)** you want to do this punch, then you move this joint like this, right? So, so the so a challenge or like a Holy Grail, like to get a robot to generate movement on demand. So maybe it thinks like, OK, if I want to do this, then here as a here's a how I should move the joint. So that is still like work in progress. And I think it's a bit challenging for for robot to do, but I think that we are getting there because if you look at the progress in the last few years, it's actually very promising. Think about robotics. There's always the vision part and the motion part. Are they connected somehow? I think that people are things that it could be related, but I think there's so there are two approaches to it. 1 is a approach of what people call like the VOA approach, like the vision language actions model, which a

**[8:01](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=481s)** robot take in like visual and then language commands and then generate actions to do, right? But then people realizes like, OK, it's really hard to collect robotic data with actions, right? Because the actions are very much dependent on the, on the, on the, the body of the robot. So like, so like if you want a robot you want to walk, then you need to collect actions from robots that have legs, but you cannot collect data from the robot have wheels, right? If you want to do like 5 finger manipulations, you need, you need a body with like 5 fingers. So people found out that extremely expensive and slow to collect action data directly. And then we'll start a decouple with like, what if I just like have a separate world model just to encode information about the wall And then the robot can use that information visually to understanding to generate actions separately. So, so yes, so they are like depending on how

**[8:52](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=532s)** you structure it. So they're, I think they're on different bets. Like if you talk to like researchers, they have into very heated argument. So I talked to a company who do like VOA approach and they call, they said I own on the one more world modeling company as stupid. And then you talk to 1 modeling company, say OK, on the, on this action companies are like stupid. So we don't know yet. We don't know it works until it works. Just figured out embeddings and pre trained foundation models with language and now more to learn. Oh my goodness. So what should developers pay attention to as all these new primitives come online? Oh, so so you're asking me what? What should a person? Developers, what should they pay attention to right now, knowing it's going to start to start to roll out? So one thing that like I find very challenging personally,

**[9:42](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=582s)** it should stay up to date with all the news. It's just like impossible. Like there's so much going on. So, so actually try to like think about like the kind of problems I want to solve and it kind of filter out like, OK, does this new thing help solve my problem or not? Right? Because otherwise it was OK. This company raised a lot of money, this company going IPO, this person doing this cool stuff. I keep getting my pool in different directions. So try just keep my, you know, like the horses in in, in like in New York, you need to have a a like a biter, A blighter to give it like very focused. So sometimes I have to like force myself not to like get jerked into different directions just because the new things come out. But like focus on like 1, Like is that problems something I'm interested in? Second, is that like worth solving? Like is that something that can be sold like by

**[10:30](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=630s)** AI in the next two years? Then maybe I should probably focus on something else. So, yeah, just choose and like you choose the problems that you care about. And my e-mail approach is wrong. I don't know. I have friends who, like, follow a lot of news and they become very popular online and they make a lot of money. And I think that could be great. I'm just not very good at that. So Chip says to focus everyone do this. OK so I'm now sitting with you remembering how it's the Boston dynamic, Spot, the 1st, that robot, whatever. And I remember that someone told me never stand near spot because when spot falls, when spot gets up it moves not like a dog would move. So, so, yeah, so, so actually like the, the dogs

**[11:19](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=679s)** actually like a lot safer than say humanoid. So, so one challenge with with humanoids, with robot is like the safety, right? And it's very easy to phone over. Like let's say a humanoid like AG 1 is like 80 lbs, right? Let's imagine a chunk of metal, 80 lbs metal just fall on you, you're in trouble. So so there are a lot of things actually I'm working on just like for like the safety features. So I think one of these companies has been interesting feature like the 1X. They design the robot so that it the robot actually very weak. Like in theory, it could get the robot to be very strong, but on purpose, it makes a robot very, very weak grip power. They kind of crack a word nut a nut, right? It's so so that it make it safer since the robot don't accidentally like hurt people by being too much force.

**[12:06](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=726s)** When I also like follow this like design of rules, for example, like never walk too close to humans. Like if some human come close to it, then you step back, right? So like maybe like maybe like 5 feet of like distance or something like that. So that's something you can do. Another thing that's very challenging is like battery. So let's say it's like if the robot is walking and it's suddenly battery dies, right? Then it's like mid motions and the battery dies, it's going to flip over. So you need to design the system to detect like, OK, maybe the battery is like this much, then maybe it shouldn't attempt, shouldn't move around. Maybe it should like just pause or like I think we're developing what is going to self charging so that when the rod knows that is running out battery, it should move there. So, yeah, so there are a lot of like safety

**[12:53](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=773s)** features we need to think about when when we bring robots into the real world, working with like real humans. OK, if you're tired of LLMS, do Frontier Robotics. If you're going to go into this, you better focus. There's so much noise. Don't forget dog robots. Kind of good, sort of safer, OK, not bad. Watch out for the battery problem. Last word for the audience on what's next. What is next? What's next? Are you asking me what's next? AI in the physical world, what's next? A few. Words. So I think it's going to be here robotics, there are two schools of company 1 is the companies who believe that robotics can be general purpose the same way is like a chargeability and clock, right? That you can store multiple tasks at the same time. So there are like 20 of those companies.

**[13:42](https://www.youtube.com/watch?v=Hx0cmcDlmSU&t=822s)** So they're very data heavy. So they need a lot of money to like raise a lot of money as the other school of like robotics company as they focus on more specialized robots. For example, here's a robot to fold the laundry. Here's a robot to like cook the food, like packaging about you, like the smooth thing around, like delivery. So, so I think that general purpose company is very hard to predict when it's going to be here. You heard it from Chip general purpose company. A little bit hard to predict, but let's make it happen. Everyone, thank you. Thank you, Chip. Thank you everyone. Chip.
