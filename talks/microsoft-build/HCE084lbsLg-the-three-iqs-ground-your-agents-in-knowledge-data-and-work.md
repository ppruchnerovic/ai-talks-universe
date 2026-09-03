---
id: HCE084lbsLg
title: "The Three IQs: Ground Your Agents in Knowledge, Data, and Work | LIVE171"
slug: the-three-iqs-ground-your-agents-in-knowledge-data-and-work
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: ["Marco Casalaina", "Ayca Bas"]
channel: "Microsoft Developer"
duration_min: 10
published_at: 2026-06-05T14:49:07Z
video_id: HCE084lbsLg
url: https://www.youtube.com/watch?v=HCE084lbsLg
youtube_url: https://www.youtube.com/watch?v=HCE084lbsLg
tags: ["Ayca Bas", "LIVE171", "LIVE171_ASL_v1", "Marco Casalaina", "The Three IQs: Ground Your Agents in Knowledge Data and Work | LIVE171", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["Agents & orchestration"]
transcript: true
---

# The Three IQs: Ground Your Agents in Knowledge, Data, and Work | LIVE171

**Marco Casalaina, Ayca Bas**

`Microsoft Build` · `Build 2026` · `2026` · `10 min`

`#Ayca Bas` `#LIVE171` `#LIVE171_ASL_v1` `#Marco Casalaina` `#The Three IQs: Ground Your Agents in Knowledge Data and Work | LIVE171` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=HCE084lbsLg) · [Conference site](https://build.microsoft.com/)

## Description

Agents shouldn't hold all the context themselves — they should delegate. See how Foundry IQ (knowledge), Fabric IQ (data), and Work IQ (human context) let developers build grounded, enterprise-ready agents faster, with reusable intelligence instead of hand-wired pipelines. Live demo included.

To learn more, please check out these resources:
* https://aka.ms/iq-series

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Marco Casalaina
* Ayca Bas

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE171 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Discussion Topic Introduced – The Four IQs
00:00:51 - List of the Four IQs: Web, Foundry, Fabric, and Work IQ
00:02:30 - Introduction to project collaboration and background
00:03:18 - Improving agent performance through refined instructions
00:05:55 - Exposure of the same agent in action and next steps
00:06:55 - Demonstration of agent checking its own email and sending replies
00:07:19 - Advantages of agents with independent identities for security and functionality
00:08:52 - Transition to demonstration showing interactions between multiple IQ systems
00:09:34 - Invitation to explore more through the IQ Series with multiple modules

## Transcript

*1,857 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=HCE084lbsLg&t=2s)** MARCO CASALAINA: All right. Hello everybody. Thank you for joining us. I'm Marco Casalaina. I'm VP Products of CoreAI. AYCA BAS: Hi, everyone. I'm Ayca, and I'm a Developer Advocate at Microsoft. MARCO CASALAINA: All right. We're going to talk about the four IQs. There were three, and now there are four. So, Ayca, what is the deal? What are the four IQs? AYCA BAS: Yes. So seems like IQs are pretty hot topic this Build. MARCO CASALAINA: Yeah. AYCA BAS: And, as you know, when we build demo agents, we can actually use and build any data source we want. But, in the real-world, our data is across the board. So we need files. We need structured data, unstructured data, human context. So IQs are actually bringing the old context data and also M365 into our agent, which is pretty cool.

**[0:51](https://www.youtube.com/watch?v=HCE084lbsLg&t=51s)** MARCO CASALAINA: Yeah. That's right. So there are four IQs. We got Web IQ, Foundry IQ, Fabric IQ, and Work IQ. What do each one of these things actually do? AYCA BAS: Right. Okay. Let me get started with Web IQ. So Web IQ wires your agent into all that web knowledge that actually is pretty useful because, if you have, let's say, if you need local information like the demo you did yesterday, if you need to check, let's say, shipment delays or all those information, you kind of need that service in place. MARCO CASALAINA: Yeah. AYCA BAS: So Work IQ is where we connect M365 data in your agent. That means you can actually check your emails or Teams messages, all sorts of data available in Microsoft 365. And then Fabric IQ, do you want to cover Fabric IQ?

**[1:40](https://www.youtube.com/watch?v=HCE084lbsLg&t=100s)** MARCO CASALAINA: All right. So Fabric IQ is for structured data, largely for structured data. And you think about you as humans, you might get to this data with a Power BI report or something like that. But that doesn't work for an agent, so you need some kind of an agentic face, a headless way for these agents to get to your data. So Fabric IQ is all about providing this kind of headless access and maintaining the context that's necessary for your agent to hit that structured data in Work IQ. AYCA BAS: Foundry IQ. MARCO CASALAINA: Oh. And Foundry IQ is largely for unstructured data. So these are your blob stores and your search indices, SharePoint and all that kind of stuff. Foundry IQ is an agentic retrieval mechanism that allows your agents to do that kind of agentic retrieval rather than simple old-fashioned rag that's existed

**[2:29](https://www.youtube.com/watch?v=HCE084lbsLg&t=149s)** for like three years. That makes it old-fashioned in this market. Now, Ayca and I pair-programmed a lot of this stuff. So we've been working together for a while, working towards Build and stuff like that. Let's talk a little bit about so now with the IQs we did, and now we got this on the screen here. I think you could see it somewhere; or you could put the PC on the screen. AYCA BAS: I think they can. MARCO CASALAINA: Production folks, I hope you can see that. Now, we've only got four tools in here. We got the four IQs. And, yet, there are still some idiosyncrasies about making your agent call the right tool at the right time. How did you -- how did you do that? How did we do that? AYCA BAS: Exactly. I think we should also explain that these services are very new. So all those tools are coming together, and Product Teams are working so hard to bring them together. So we are in very early stages of IQs right now.

**[3:18](https://www.youtube.com/watch?v=HCE084lbsLg&t=198s)** So, to be able to make them work in a pretty good shape, let's say production ready shape, then you kind of need to maybe work on your instructions, agent instructions. So we went through a lot of iterations of this agent instructions, and maybe Marco can cover that a little bit too. But what we have here is very good and identified descriptions for every IQ and how we need to work together with them, all of the mapping for, let's say, Fabric IQ. And, if I scroll down a little more, you will see that, if you're using Work IQ, there are critical things when you're doing search; when you are doing do action, which means if you're doing any, let's say, sending emails, etc. We are putting all those rules so that our agent that can actually consume the IQ content in a shape

**[4:09](https://www.youtube.com/watch?v=HCE084lbsLg&t=249s)** that we want them to be. So we also even have examples of some JSON buddy that means that, when Work IQ is receiving our query, it is pretty much converting our content into a shape we want to and all those stuff plus everything about Web IQ available in our instructions. So it actually plays a really big role. Having said that, if you just plug them into an agent and try to test, it will probably work; but, if you want a really good performance out of the IQs, you should definitely consider adjusting the instructions. MARCO CASALAINA: Right. So the moral of story is the purpose of these IQs or really one of the main purposes of these IQs is preventing context rot. It's removing so you don't have to put all of this context stuff

**[5:00](https://www.youtube.com/watch?v=HCE084lbsLg&t=300s)** in each individual agent that you build, all the context about your data and about your unstructured data source, about Microsoft ecosystem stuff. But that does not absolve you from still having to put some context in here to tell it what tool to call when and what they do. That is still on you or on whatever coding agent you happen to be using because, yes; we absolutely did do this with Copilot CLI. Now, I think, to finish this off, what is really interesting about this, so here she has the Foundry agent. That's what it looks like in the Foundry web portal. But that is not how we expose this agent. How we exposed this agent is fascinating and, honestly, was a little bit undersold here at Build in the keynote and stuff like that.

**[5:47](https://www.youtube.com/watch?v=HCE084lbsLg&t=347s)** So, if you would, production folks, if you can hear me, please change to the Mac. I'm on a Mac; she's on a PC. So here we go. So check this out. So we did indeed expose that same agent, but what did we do with it? We did this thing. Out of that agent, we made an agent template. So this is an agent template in A 365. And what does that give you? When you have an agent template, what it does is this: It allows you, or really anybody, to create an instance of this. When you create an instance of this agent, you're not just creating an agent. So, when I created an instance of this thing, I didn't just make an agent. I made my agent. This is my instance of this particular refund processor agent.

**[6:37](https://www.youtube.com/watch?v=HCE084lbsLg&t=397s)** That means you see it in the org chart, and it reports to me. That also means that it has its own Teams box over here and that it has its own inbox. It has its own email address and all that kind of stuff. And so earlier I told it, check your email for complaints, and I mean your email. To the agent, I'm like, Check your email, not my email, your email. It has its own. And it's able to check its own email. And, in fact, it sent me back, if I look at my own inbox in here, you can see that it sent to Maria Garcia, it sent a reply; and it copied me. Now, this is hugely advantageous. Not all agents are going to be like this. But there are certain class of agents that you want

**[7:26](https://www.youtube.com/watch?v=HCE084lbsLg&t=446s)** to have their own identity like this, and there is specifically for security. For one thing, if we think about, say I go over here to ClawPilot, which keeps signing me out today. So here I am in ClawPilot. Now, for those of you who haven't seen this before, this is our kind of internal claw thing, and it uses the heck out of Work IQ. Here earlier today I was making it read a document for me, and it used these tools. It used Work IQ. It used this to draft an email and all this stuff. But it was doing this on behalf of me, so that means this agent could do anything that I can do. However, that's not always wonderful. Wow. What is my mouse doing? That is not always what you want to be doing here. So, in this case, this agent runs in its own security context.

**[8:15](https://www.youtube.com/watch?v=HCE084lbsLg&t=495s)** It has its own permissions. It can't just do everything that I can do. So I might say, all right, agent. You have the ability to send emails, to send Teams messages and stuff; but you are not allowed to delete stuff out of OneDrive. I can; agent cannot. So it has its own security posture. And so, as you start to think about deploying these agents to an organization, you do need to think about what is your security posture. And the on behalf of security posture, like what I was showing earlier, is not always what you want. What you do want, in many cases, is an agent that has its own identity, its own security. AYCA BAS: Awesome, And if you switch to my PC -- MARCO CASALAINA: Back to the PC. AYCA BAS: -- I want to show, and before we close this out I want to show that, while Marco was going through all that chat with A 365 agent, you can also see all

**[9:05](https://www.youtube.com/watch?v=HCE084lbsLg&t=545s)** that in the traces of it called between the tools, between Work IQ and then Fabric IQ; and then Foundry IQ returned saying that, Hey. Maria Garcia, I found her package. And then I checked the policies, and then I can actually issue her a refund. So I can email to Maria. So all that is happening in sync behind the scene calling all the IQs in synchronously. So this is pretty much what we wanted to talk about. But there is one thing I want to mention. MARCO CASALAINA: All right. Of course, this is just 13 minutes talk. But, if you want to learn more about IQs, we have a series for you. Just go ahead and check out the IQ series. It's ak.ms/iq-series. We have episodes for you about Foundry IQ, Work IQ; and Fabric IQ and Web IQ are coming soon.

**[9:54](https://www.youtube.com/watch?v=HCE084lbsLg&t=594s)** And we also issue you a digital badge if you complete cookbooks and if you watch all the episodes. So you can show the world that you're one of the first experts about IQs. Yeah. So that's pretty much it. You want to close it out. I will. Thank you, Ayca. And thank you all, and use yourself some IQs. Have a good day. [ MUSIC ]
