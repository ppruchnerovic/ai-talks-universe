---
id: DFd0iiCX6tc
title: "Coding and Personal Agents with Ollama | LIVE145"
slug: coding-and-personal-agents-with-ollama-live145
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-04T16:06:44Z
video_id: DFd0iiCX6tc
youtube_url: https://www.youtube.com/watch?v=DFd0iiCX6tc
tags: ["Coding and Personal Agents with Ollama | LIVE145", "John Maeda", "LIVE145", "LIVE145_v1", "Michael Chiang", "Parth Sareen", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Coding and Personal Agents with Ollama | LIVE145

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#Coding and Personal Agents with Ollama | LIVE145` `#John Maeda` `#LIVE145` `#LIVE145_v1` `#Michael Chiang` `#Parth Sareen` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=DFd0iiCX6tc) · [Conference site](https://build.microsoft.com/)

## Description

A live walkthrough of Ollama launch, showing how developers connect local and cloud open models to real-world applications in a single step. See Copilot CLI and OpenClaw set up live, switch between local and cloud models and connect the agent to web search and vision.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Michael Chiang
* Parth Sareen
* John Maeda

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE145 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Fun fact: O Llama mascot designed by Michael’s wife
00:04:03 - Introducing seamless experience between local and cloud model usage
00:06:00 - Copilot CLI’s autonomous code exploration, planning, and execution features
00:06:51 - Discussion on hybrid AI architecture: balancing local and cloud operations
00:08:18 - Handling sensitive data locally for greater privacy and control
00:08:41 - Use of coding agents and open models through cloud for development efficiency
00:11:17 - Developer Experience and Product Design Philosophy
00:12:56 - Explaining the Simplicity and Memorability of the Logo
00:13:27 - Affirmation of O Llama’s Logo as Easily Recognizable

## Transcript

*2,215 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=0s)** We have O Llama people, we have Michael Chang, Co founder Parth Serene Engineer, who knows O Llama, right? Oh my gosh, O Llama lovers, you see that? Who loves O Llama's character mascot? Yes, let's go there. OK, so Michael, you can feel the love here, right? That wasn't good. So question for people new to O Llama, what problem does it solve? Well, John, first, thank you for having us. It's our pleasure to be here at Microsoft Build for O Llama. It's the easiest way for developers to get up and running with models open models specifically on locally and now in the cloud. For users with enough compute locally, they can choose a

**[0:49](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=49s)** model and run it directly on their computers. Should they not have enough compute, they can choose O Lama's cloud service and run it all in the cloud with privacy centered cloud offering from O Lama. So what's the AI local model landscape like right now? Yes, starting from last year, what we've seen is a lot of the coding use cases really took off. And this year a lot of the larger models started coming online for the open model ecosystem. And this really started off with agents. More agents were being in the market and this really became our number one use case very much quickly. And then by the way, I was talking about Parths, and Parth is one of the great engineers who calls

**[1:38](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=98s)** his mother. Everyone call your mother. You're awesome. Parth. What kind of agents are only possible with local models? Yeah, that's a great question. And even just last night, I was spending time looking up way too much money that I've been spending and I was using O llama to see how much I was spending go through my bank statements. And so I think local agents are so, so powerful, especially with the improved local models that we have today to be able to do real agentic use cases. And I think privacy is so critical. And we have the ability now to run really, really good models on your computer and do real work, right, whether it's coding and building small tools.

**[2:27](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=147s)** I think those kind of models do a pretty good job as well as doing small personal agent tasks. So, you know, we've heard of Open Claw Burmese, extremely popular these days. There's a lot of really good local models which fit the bill and can do a really good job. How many folks use local models here? All right, you have like, people doing this. That's good. All right, Michael, what was the moment you realized that devs love local? What was the moment? It was exactly the moment when we launched O Llama on GitHub in in public and it actually launched on Hacker News as a comment on underneath the model launch and the trajectory ever since has made Olama one of the fastest growing open source projects for AI and supporting open models.

**[3:17](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=197s)** And the Olama mascot was designed by. My wife. I thank you, thank you, thank you. One of the greatest design moments in local model history, if I might say so myself. So what does it look like for a developer to go from running a model locally to scaling it in the cloud? Yeah. It's something that as Michael mentioned, we've been seeing a lot of. So we have these larger coding open models coming out as well as you know, really powerful local models as well. But there's just a point you where you really do need to scale up and go from running a local model. You're running really extreme workloads, maybe doing some really difficult coding tasks and you're like, OK, I need something bigger to get the job done. And that's when you reach for the cloud.

**[4:05](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=245s)** And that's something that we really try to make good and simple, so the experience between local and cloud can be as seamless as possible. And so, you know, we offer open models both locally and on the cloud and the experience to the user basically feels the exact same. So you it's indistinguishable when you're running between local and cloud. I like this like in Toy Story. Like reach for the, reach for the sky, reach for the cloud. Do you have a demo? Yes. So I'll showcase a little demo of O Lama running the copilot CLI, which we recently added. So I'll walk through kind of what's going on behind the scenes as well as talk about kind of what we have. And so O Lama launches this tool that we built in order to in order to give users the ability

**[4:57](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=297s)** to connect with their favorite integrations. And so Copilot CLI is one of them. And as you can see, we give a myriad of different options with both cloud and local models and copilot CLI is really cool, especially because you can tag these different issues. And so you can see in here I'm adding, you know, explain me this little issue. Let's skip forward a little bit. But basically the agent has direct access to GitHub, can see kind of, you know, what I've been working on or triage a different issue for me, skip forward a little bit and see that over here, you know, it's directly connected. And so my workflow can stay within the terminal if I feel like it. And Copilot CLI is a really good fit for it too.

**[5:44](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=344s)** I keep forwarding it a little bit. And so if we go a little bit forward, so I'm just saying, are there any open PRS for it? Go and see if there's anything already built out. And then it says no open PRS. So that means we have to go write a fix. And the Copilot CLI kind of handled this for me. It creates a plan, explores the code base, is able to spin up multiple sub agents to do exploration and make sure that it gets a good lay of the land. And so this is being worked on in the O Llama repo. And you know, it'll propose a plan similar to many other tools as well. And then, you know, as usual, we can do the execution. And so in this case, the autopilot mode has been enabled and I'll go and kind of execute on the plan that was discussed.

**[6:34](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=394s)** And for everyone watching, go at to alum.com, try it out, Go see all the different integrations we have. So copilot CLI is a really popular one. We support BS code, we support Hermes, Openclaw and tons and tons of others. So go check it out. So it's kind of like a hybrid car, gas, electric or moves between the local and the cloud? Exactly. Yeah, very cool. So what's hardest in taking AI apps to scale? Is it the local cloud thing? Yeah, I think what we've seen is developer often start with local this, this is where they can do their local Devon test. And as they scale, they often times look for a solution and O Llamas Cloud could be one of those solutions. Interesting.

**[7:22](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=442s)** And when with all your integrations, what excites you about what developers are building now? What I'm super excited about is all these local agents that are running at the edge and whether using local models or models in the cloud, and it really improves people's lives. We've seen agents run checking people's emails, plan for their day. Every morning we see users coming up trying to get agents to see what their they will look like. A lot of these agents are are being used. So you're moved by this moment where people can actually have a better life. Yes. One SEC it's adorable. So Parth, what workloads benefit from local versus cloud? Can you help us understand?

**[8:10](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=490s)** That, yeah, that's a great question. So I think having the ability to swap is really important. And in terms of workloads, I see a lot of sensitive information being kind of processed. You know, I give my agents access to my calendar often and you know, sometimes I want that to run completely locally. And so anytime I think of personal private information, local models fit the bill really, really well for that. And then personally, I use a lot of coding agents to build whatever I'm working on. And to that, I usually reach towards bigger open models through Obama to get my work done. And I think it's similar in terms of the user's BC mix of personal agents, coding agents and then a

**[8:59](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=539s)** lot of bespoke tools that people write. So rag pipelines, custom CLI tools, all kind of back through alumni. How do the local models in the open source movement connect? Is there a connection there? The local models and open source, yeah, I think to some degree I feel like we've seen this kind of evolution where people where the models coming out are almost informed by the harnesses that exist today and kind of like what's trendy in a way as well. So personal agents has been 2026 so far and I think we've seen a giant leap in the models and kind of what the model labs are trying to reach towards, which is really have agents which can not only code or models which can not only code that can perform these tasks that Michael mentioned of, you know, checking e-mail, calendar and like doing it in a safe manner.

**[9:51](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=591s)** So for your tomorrow, you're in a session tomorrow. Can you give like a preview of like what to expect? Because they're all kind of like thinking of like, what do I go to? I mean, please attend the session tomorrow for a breakout. We'll have real demos of O Llama up and running and targeting a lot of these agentic tasks that that we spoke about. I see. So when we think about the future of O Llama, what does the audience want to expect? I see the the the world becoming more hybrid and this is leveraging both the local models to do simpler tasks and leveraging cloud models for much heavier and harder tasks. And this is really the evolution of having a personal computer.

**[10:38](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=638s)** Meanwhile you have cloud services that might do more of offloading. So for for people out there for whom this is a a new idea, what advice do you give them when you think about how they have such, so many choices out there? Yeah, for developers that are just getting started with AII would say look up what you want to use, start picking up a tool and just start building. Because with AI, it's so easy to get started and try out the different tools to see how you can familiarize yourself with different models, different harnesses and and get your app out there. Yeah, the, I mean, the developer experience for a lava is quite exquisite. It is very subtle. It has that kind of apple feel to it.

**[11:27](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=687s)** Can you tell me where this came from? Yeah, it's really about what we want to portray ourselves to developers using our product, and that is O llama being really simple to get started. It's monochromatic by design. It stays in the background to help power developers. That's really the theme of product and so we want to design O llama a product as such. And then how did you think of joining O Llama? That's. A cool company. Yeah, it is. And I'm very lucky to be here. And it all kind of started when Michael and I started hanging out. I was doing my own startup prior to this and you know, I was using O Llama and this is

**[12:15](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=735s)** back in 2023-2024, so quite early on. And honestly, I was in love with the product and when the opportunity came up, I just did not say no. OK, so final thought here, tell us how your wife came up with this character. That's what they want to know. Well, first of all, all, almost made with love for for real. It's made my by my wife and I love her very much and we wanted to really design A character that is really simple to understand and easy to be memorable. It's a bump on the head, 3 bumps on the side, two years and a circular nose in the middle. So it's very memorable. People can really draw it out themselves, maybe not get right, but they can design A character around.

**[13:04](https://www.youtube.com/watch?v=DFd0iiCX6tc&t=784s)** OK, and we pause for a second in all this noisy world today made with love #2 Paul Ran one of the greatest graphic designers in the history of graphic design. Once said a great logo is 1. You can see from far away, if you squint, you can always see the llama. But also you we can we can easily recreate it from hand. There we go, one of the greatest logos of all time. Oh llama, please use it. Thank you. Thank you so much, John. Right.
