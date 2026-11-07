---
id: Sg6vtKOAOQ0
title: "AI Labs Will Trap You or Replace You - Dillon Rolnick, Nous Research"
slug: ai-labs-will-trap-you-or-replace-you-dillon-rolnick-nous
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dillon Rolnick"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-11-04T21:00:12Z
video_id: Sg6vtKOAOQ0
url: https://www.youtube.com/watch?v=Sg6vtKOAOQ0
youtube_url: https://www.youtube.com/watch?v=Sg6vtKOAOQ0
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Dillon Rolnick", "Nous Research", "Hermes Agent", "open source AI", "AI agents", "open models", "vendor lock-in", "AI platforms", "model distillation", "AI moats", "AI in finance", "AI Engineer", "AIE NYC"]
topics: []
transcript: true
---

# AI Labs Will Trap You or Replace You - Dillon Rolnick, Nous Research

**Dillon Rolnick**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Dillon Rolnick` `#Nous Research` `#Hermes Agent` `#open source AI` `#AI agents` `#open models` `#vendor lock-in` `#AI platforms` `#model distillation` `#AI moats` `#AI in finance` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=Sg6vtKOAOQ0) · [Conference site](https://www.ai.engineer/)

## Description

Dillon Rolnick, CEO of Nous Research, argues that as AI models commoditize, the labs that spent trillions building them have two ways to earn it back: lock businesses into their platforms and raise prices, or point their own systems at lucrative industries like finance and compete directly. He makes the case that the moats of proprietary software are gone, that agents are closer to operating systems than chatbots, and that companies should build on open foundations they own and control, like Hermes Agent, so they can swap models and inherit new capabilities instead of rebuilding them.

Chapters:
0:00 Intro
0:32 The models are commoditizing
1:52 How labs plan to earn back trillions
2:48 Why businesses are the real target
4:28 The labs are coming for finance
5:44 Don't build on quicksand
6:48 Why Nous Research exists
7:56 Software no longer has a moat
9:25 Distillation and the fight over open models
11:06 Agents are operating systems
12:17 Build on foundations you own
13:49 Hermes Agent and the new moats

Dillon Rolnick

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,186 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=1s)** [music] >> I'm Dylan Rolnick. I'm the CEO of News Research. And today we're going to talk about building on foundations and platforms that you can actually own. Whoop, there we go. All right. How do you make back a cent a billion-dollar infrastructure and research bet? Labs individually have spent hundreds of billions of dollars training and building ever more sophisticated intelligence system and the industry as a whole has spent

**[0:48](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=48s)** trillions perhaps. The problem is though that the models have begun to commoditize. You guys in this room who are hopefully practitioners of AI have known this intuitively. You switch among models readily. You switch between Astra, Fable, Opus, Kimmy, whatever it may be without too much regard for who's on the back end or what it may be. You want to try the new model. We've seen this in data, too. There was some charts going around Twitter this week showing the average cost of a token going down while the total spent on tokens surges and the infrastructure costs associated with serving those

**[1:36](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=96s)** tokens has stayed flat. Meaning where there used to be margin in a very, very performant model, it's now starting to narrow as we see competition and you know, a baseline level of intelligence be available to people. Okay, so if the models are starting to commoditize and you've spent hundreds of billions, trillions of dollars on them, you need to make that back. And you need to find a different way to do it. And in my opinion, there are two pretty obvious ways to do it. One, you find a different layer of the stack to compete at. You go down to the infrastructure, or you go up to the user. Or two, you build God, and you build God faster than anyone else, and you

**[2:24](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=144s)** monetize God. If you're in front of the user, you have an opportunity for stickiness. Stickiness means margin. This is why the fight has largely shifted to the agent layer lately. We started talking, I heard somebody previously talk about 5% of, you know, a workforce engaging in agents. This is becoming more and more the zeitgeist of where the AI battle is taking place. Consumers though >> [sighs] >> are fickle, and they're terrible customers. Businesses, on the other hand, spend tons of money on tokens, and they have economically productive use cases for those tokens. So, if you're going to be competing at the user layer, and you're going to be bringing this fight somewhere else, you're going to be bringing it to businesses.

**[3:11](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=191s)** The best thing to do is to get ingrained in a business, cuz when you're in a business, it's hard to take you out, right? And if you think about your business 2 3 years into the future, how much of your workforce, as measured by its output, is agentic? 70% conservatively, probably more. And if 70% of your workforce is organized by somebody else who may or may not have adverse incentives to you, they can be organized into a strike. And so, what you would do if you had to make back a trillion-dollar investment, was you would embed, you would use your asymmetric leverage, and you would change the rules of the game. Or, like I said, you would build God. If you succeed at building God,

**[4:03](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=243s)** >> [sighs] >> what you would do is you would point God at the most lucrative problems in the world. The best shot at earning it back is not to sell it for an ever-decreasing margin to others to solve these hard and lucrative problems. The best shot is to solve them yourselves. Labs think that markets are solvable problems. And that's exactly how they view the financial industry as a problem to be solved. And a tractable problem at that. Perhaps not even a very hard one. Right now though, they know, at least the smart ones know,

**[4:50](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=290s)** that they don't have enough context, know-how, or experience in the financial industry to be able to do that themselves. So, they will partner. They hire investment banking analysts. They partner with some of the biggest firms on the globe. And they start to build their foundation here. My belief is that they will eventually go to the source because, like I said, that's where the money is, and we're trying to make back a trillion dollars. And so, you might say, "This is nothing new. We have always been trying to trap people into these games and change the margin, and once we have you and you're stuck, we are able to raise the prices." But, the difference is that the stakes are much higher. We're talking about meaningful deca-percentages of the Earth's economy. And you in this room

**[5:42](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=342s)** need AI. Everybody has seen what they can do, what these models can do, what agentic systems can do, and there's no going back. People in this room who are um making decisions, vice presidents, and executives, and engineers about what they're building on, are going to have to make decisions now about where they grow roots around these tools and processes that will affect the future of these businesses. And whatever you pick, you'll start to harden. You'll gain know-how. It'll stop up the intelligence of the organiza- organization itself. You will start to build processes and systems around it. I implore you, do not build on quicksand found- quicksand foundations. Build on open foundations.

**[6:29](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=389s)** Build on Hermes Agent. So, I just spent a fair amount of time convincing you hopefully that the highest expected value move in AI right now is to either trap you and jack up the prices, or replace you directly. So, why am I standing here? Uh we view the world very differently. And the first thing I hope you guys will learn about me and about News Research is that we built this company primarily for moral and philosophical reasons. And a lot of times in business, morality and incentives don't always align, and when that happens, it's probably easiest to change your morality. But, we think the world is changing, and we think it's different. And for that

**[7:17](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=437s)** reason, we think that the best course of action is one in which we are both aligned. When we built the company originally, we built it to combat a seemingly inexorable trend towards centralization and centralized control of perhaps the world's most most important technology and most important invention. News Research was built by and staffed by nerds. Nerds who love science fiction. And we've all seen what happens when a centralized entity gets control of god-like intelligence and uses that for exploitation. Skynet was, after all, a closed-source company. The next thing that you need to know is that there's no longer really a strong moat in proprietary software. The marginal cost to reproduce a piece

**[8:05](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=485s)** of software has plummeted. A few months ago, uh xAI released Grok bots and we saw that and we thought, "Wow, that's an intuitive user interface. That's really nice." So, we pointed Hermes agent at it and we reproduced it in a weekend and released it as a feature within Hermes agent, open source, of course. And the game has changed. It used to be that software was difficult to produce and it took coordinated teams of engineers long hours to pilfer open source and take libraries and combine them together into proprietary pieces of software and then sell that software as SaaS. But, now the opposite is true. Anything can be reverse engineered and there are many, many motivated open source builders pointing their agents at

**[8:53](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=533s)** these different softwares. If the close competitors do manage to make interesting features, open source will have it not long afterwards. The motes of yesterday were in proprietary IP. The motes of tomorrow are in network effects, reputation, and reliability. What's funny is that in a lot of ways the labs have always seemed to underestimate their own tools or perhaps they are underestimating the users of those tools and their genius and their motivation. This happened and is happening on the model side and we'll talk about why that's important, but it turns out that models can fairly easily teach another model to be, you know, nearly as smart as the original model. And the advantage in a model is very

**[9:43](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=583s)** rarely in the architecture or some novel system that was created in a proprietary way for that model. In fact, it's usually in the quality of the data and the scale. And sorry. The uh >> The The model started to The model company started to realize that the you know, scale was catching up and that you could create these things with supplementary quality data by teaching one model from another. So,

**[10:29](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=629s)** they labeled the teaching process distillation and they labeled illicit distillation theft. You cannot call that copyright infringement because copyright infringement would imply that you somehow took every living human being's written or creative work and then trained on top of it. They also labeled the process of They also trained the models to not assist in the process of training other models and they labeled that safety. The next thing that you need to know about agents and about the new world is that agents are like operating systems and they're like frameworks and they're a lot more like those than they are like

**[11:17](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=677s)** chatbots. And so, if you continue to think about your agent as merely a personal assistant you will forever live on the surface of what it means to engage in agentic systems. And so, what do I mean by that? If you guys were here a little bit earlier, there was a presentation about a financial firm and how they think about AI and these different inputs that go into ultimately what becomes an investment decision. Agents are really at their heart a system that combines determinism and non-determinism. If you remember from that talk, there are data sources, there are routine code, there are people's opinions and there's judgment. And all these things come together to create what is the new application. The new application is no longer necessary that it is deterministic and solid and cold

**[12:06](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=726s)** hard code. It can inject intelligence, reasoning, judgment, all of these things together to combine to create the new application. And so, as you at your company think about building these new applications, you should be building these systems on foundations that you own. You should be able to swap in and out the models that you want. You should be creating ever more sophisticated towers of functionality on top of these core primitives of determinism non-determinism code data sources document reasoning intellect. But, you should not be spending your entire

**[12:53](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=773s)** lives being intelligence companies. What has made you successful this far? Most of you are most likely not agent companies. Most of you are not likely AI companies. You should be focused on the things that you do well. And when the state of the art changes and it evolves and what it means to be an agentic system starts to shift, you should inherit that, not rebuild it and maintain it. Remember, these are tools that should make you better. They are not drop-ins to replace you. Do you know how much energy it takes to create a human? And the beauty of the Hermes Agent proposition is that you can run it however you want, wherever you want, modify it as you see fit. If you're not having fun anymore, you can take your ball and you can go home. The moat has changed. The moat is no

**[13:42](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=822s)** longer entrapping you. The moat is in reputation. And that's what Hermes Agent offers you. And so, what do I want out of all of this? Well, I want to build a standard. Hermes Agent today is the most used and downloaded open source agent in the world. It is order of of magnitude more downloaded than some of its close competitors. And I want everybody to be able to build on these open foundations. Because as long as one of us us is willing to open source these tools and these agentic systems, water will continue to flow downhill. And I want to be downhill so that I can work with you to provide support, safety, scalability to go along with the world's best open agent. I've seen where this goes and we've seen

**[14:30](https://www.youtube.com/watch?v=Sg6vtKOAOQ0&t=870s)** where the motes will lie, network effects, reliability, and reputation. People are going to continue to solve hard problems with agentic systems. People are going to solve lucrative problems with agentic systems. Somebody is going to earn back the trillion-dollar investments that we've made. Make sure that it's you. Make sure that you are in control of your own destiny. You can have your cake and eat it, too. You can have state-of-the-art features and reliability without sacrificing your autonomy. Build on something you own. Build with us. Thank you. >> [applause]
