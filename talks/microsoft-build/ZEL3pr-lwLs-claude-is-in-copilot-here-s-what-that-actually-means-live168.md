---
id: ZEL3pr-lwLs
title: "Claude Is in Copilot. Here's What That Actually Means | LIVE168"
slug: claude-is-in-copilot-here-s-what-that-actually-means-live168
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Visual Studio Code"
duration_min: 12
published_at: 2026-06-05T13:43:25Z
video_id: ZEL3pr-lwLs
youtube_url: https://www.youtube.com/watch?v=ZEL3pr-lwLs
tags: ["Burke Holland", "Claude Is in Copilot. Here's What That Actually Means | LIVE168", "LIVE168", "LIVE168_v1", "Tyler Leonhardt", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Claude Is in Copilot. Here's What That Actually Means | LIVE168

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `12 min`

`#Burke Holland` `#Claude Is in Copilot. Here's What That Actually Means | LIVE168` `#LIVE168` `#LIVE168_v1` `#Tyler Leonhardt` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=ZEL3pr-lwLs) · [Conference site](https://build.microsoft.com/)

## Description

Claude runs as a coding agent inside GitHub Copilot in VS Code. But what does that actually look like at the code level? How is context assembled? What tools does Claude have access to? What happens when you pick Claude in the model picker versus letting Copilot run? Tyler Leonhardt goes inside the integration so you know exactly what you are working with.

To learn more, please check out these resources:
* https://aka.ms/VSCode/Claude
* https://aka.ms/VSCode/DBview
* https://aka.ms/VSCode/Learn
* https://code.visualstudio.com/docs/copilot/chat/chat-debug-view

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Tyler Leonhardt
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE168 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Session opens with welcome and audience check-in
00:00:25 - Introduction of Tyler from the VS Code team
00:00:36 - Overview of Claude Agent integration in Visual Studio Code
00:01:04 - Explanation of Anthropic’s Agent SDK and using it with Copilot subscription
00:02:26 - Discussion on enterprise need for multiple AI harness options
00:06:15 - Introduction of Agent Host Protocol for linking agents and clients
00:07:11 - Demo: enabling remote sessions through the agents window and browser access
00:09:17 - Showcasing cloud-based Claude agent running in VS Code
00:11:04 - Summary of key benefits: flexibility, cloud usage, and subscription sharing
00:11:51 - Conclusion and thanks to Tyler; mention of future talk on Compliment Fest

## Transcript

*2,186 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=0s)** All right. Welcome back, everyone. It is. What time is it, 115? How's everybody feeling? Still pretty good. Still still awake. Alive. Awake Alert. Alive. Enthusiastic. All right. Yeah. Let's do it. Get it out. Get it out. We'll get it out together. Come on. No, that's it. That's all you got. Let everybody hear you. Fine. I'm with you. I'm running on fumes too. But we have, we have Tyler here also from the VS Code team, he said. Courtney and Justin, it's a parade of that's right, who's who on the VS Code team, That's right. And we're going to be talking about, interestingly enough, it's a bit of a right turn because we're going to talk about the clawed agents in Visual Studio Code, which is not Copilot.

**[0:46](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=46s)** That's right. OK. It is and it. Isn't it? Is OK, but that doesn't make any sense, right? It's yeah, very funny. So, so I, one of the things I've been working on these past few months, I guess is the Claude agent integration in the S code. And what that means is like, so I'll show you. So Anthropic has an agent SDK that they that they ship. And so this is like the SDK similar to the Copilot SDK, right? It's the thing that wraps Claude code. And one of the things that we can do with this is we can leverage this SDK but still have it be backed by a Copilot subscription. And So what that means is it gives you like

**[1:35](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=95s)** the freedom of choice between, you know, all of these different options between local and Copilot CLI and, and Claude and and codecs as well. And so you have the the the flexibility and choice. Between how many? I can't see because there's a clock there. But what do we? What is that we let? Me there's there's a few and we'll cover why there's some duplication. Copilot CLI Cloud Copilot CLI again. Yeah, we'll talk about those later, OK. Yeah. Yeah yeah yeah. Hold on, Bert, Relax. Get a little work. Done anyway, so so that's like that's the idea is that we're leveraging the same the same harness that is in the Super popular quad code, but it's still tied to your to your copilot subscription. So you can you can leverage this today instead of choosing local or copilot Eli, you can choose, you can

**[2:24](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=144s)** choose claw. And this is super cool because you know there there are a lot of enterprises that are like they're exploring these different harnesses, right? And it feels like every every day there's like a new like the number one harness is like constantly changing, right? And so. Well, it depends on who you ask, but like, yeah, you log on to to Twitter or Reddit or whatever and you're like, whoa, what? Everyone's moving to a different harness. Super awesome. We're going to do it. Again, And so what's nice that that like the Copilot ecosystem provides you is that you don't have to like change your billing implementation as you. Switch all of these. Exactly right. You just have one subscription, your copilot subscription, and then you have the the, the freedom of choice when it comes to whatever harness that you feel is right for. Yours.

**[3:12](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=192s)** I'm curious how many folks have multiple subscriptions. That's a lot of folks, right? How many people on multiple subscriptions you just forgot? You don't know. You're just getting dinged for $20 every month. It's like Netflix. They don't want to admit. Yeah, they don't want to. No one knows. What's the service that you sign up for that notifies you about? I know there's one. Somebody should. Yeah yeah yeah. Anyway, so just to like show you the I mean that's that's what I'm talking about today is like our integration of the Claude Agent SDK in VS Code. So, so I also outside of work, I, I cosplay as an event coordinator for, for really in a way. I mean, I, I organize events for like a greater improv community that I'm a part of. We don't have to get into that. If you're really curious, you can ask me about it, but we don't have to get into it. So I like have this festival that I'm planning coming

**[4:00](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=240s)** up and this is the website for it. And so did. You design that. Well, I mean, I I told copilot to write it for me. There's a lot. Sweet. Just I kind of like that. It's good, right? Yeah it's. Nice. I actually fed it a so my friend designed APDF with a flyer and then I just fed that right in and then and then I was like, make a website for this. It look compliment fest. There's there's a whole back story of why it's called compliment fest that I don't have time to get into. OK, but anyway, I've added confetti to it because you have to add confetti. To everything. Yeah, in in 2026. This is how that's how you know AI is good, right? Is if there's confetti. Right exactly. So, so this is like, yeah, so this is the quad agents harness using my Copilot subscription making these changes for me.

**[4:49](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=289s)** And so that like since we're talking VS Code, it also works in the agents window. So I've got that here as well. So this is the the agents window. I think you had a couple of folks at some point talk about this, right? The Agents window. The agents. Window, I mean just the chat. Oh no, the agent's app. You called the agent's? Is it the agent's app or a window? It's a window. It's a OK, yes, we've we've talked about the agent's window a little bit. Sweet. So yeah, Claude is also there in the agent's window. And so so that's cool. But one thing that like my team has started to realize is that we have like all of these different agents and like we need a story for kind of like allowing more and more agents because because there are more like coming up, right?

**[5:40](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=340s)** There's like pie and, and, and other agents out there that that people want to leverage. Well, when we say agent and like harnesses harness, that's a very. Vague. I know, I feel like nobody knows or a lot of people don't understand. What that is a harness and then within within the harness you have different like custom agents that you could that you could. Yeah, super confusing, but essentially it's just like the code. It's the agent loop and all of the prompts and the code. It's actually making all that work. All tools for you. Exactly, and there's different ones. Copilot's one quad codes, one Pi is 1. Yes, an open source 1 codex 1 codex is 1. Yes etcetera right. And so like one of the things that my team has done recently is we worked on something called the agent host protocol. And if you're curious what that is, you should take a look at this a WOW agent, agent, host protocol

**[6:33](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=393s)** agent. It's there. It's there. Yeah protocol. And, and this is something that we're working on right now. And it's, it's essentially like a, a protocol for, for communicating between like agents and, and clients. And so the idea is that you have like an agent host which is running on some machine and you can connect to that host and spin up sessions on that host. And I think you had you had Justin. Did you? Did he talk about like the remote stuff at all? No, you just did integrated browser. Great. So I'll show you what that looks like. So now I'll, I'll pick a different plot here, local agent host in this case, and then I'll send a message here.

**[7:22](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=442s)** And it, it doesn't really matter what it's what it's doing. I mostly just want to get access to this button down here which is allowing remote sessions. So I'm going to turn that on and that's going to start and then that gives me the ability to open up here insiders. Well, VS code dot dev agents and then what that gives me? The you can access it on the web. Yeah, yeah, on the web. And am I gonna have to go through an auth though? I'm so sorry. I try to avoid I. Hope it's two factor for your sake. It should be fine. We're good. We're here so I didn't know you can load the agents window in the browser. Yes. And it's connecting to. So there's Complimentfest, right? Great, as we were seeing it before.

**[8:11](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=491s)** Right, it's connected to your local machine. Correct. Yeah. OK. So I'll pick Opus again and I'll say hi. Can you? Zoom in again. Zoom in. You got it. A bit more. There we go. I don't know why my window is not like fully maximized, but anyway, so this is this is running like on my machine. I mean, obviously because it's in my browser, but like I could like pull it up on my phone for example and like. But it's so it's like a, it's like port forwarding. It's like a public URL. Yeah, that's right. That's but you have to sign into to access it. Exactly. Exactly. Yeah. So this is like some of the things that we're working on right now for like moving from like desktop to to a phone or like connecting to like so. You can keep working exactly stop stop sleeping. Burke, you need to keep working. Keep working. Keep working.

**[8:58](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=538s)** Don't have dinner with your family, prompts your agents. That's. The message here, folks, that's the message. This is where we are in AD build. It's 2:00 PM We've lost. The filter is gone. That's right. What else? Yeah. So those are a couple of things where we see clawed. The other thing we see is in this one, you know this one, the Cloud agent. Yes, very familiar. Yeah. So if you go into settings Cloud agent, you can allow clawed code. Sorry, clawed coding agents and Codex coding agent. You turn those on so. It's the clawed agent running in the cloud. Yeah you. Can do that, Yes. Come on, Burke. I didn't know that. So you can delegate to clod in the cloud? Yes, clod in the cloud.

**[9:46](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=586s)** Clod in the cloud. That's right. I'm enamored with this design because it doesn't look anything like AI. So I'll go. I'll choose clod. Sorry, Cloud Cloud. Cloud Clod. The amount of times I've said clod is too many. All right, clod cloud. I chose cloud in VS Code and now I'll pick. Clod. And I'll say hi and then it will, it will go in. Whoops, I'm sorry. It will disappear. It'll disappear because I tabbed away from it. And it changes all right there we go to the cloud so. Then it'll go and do the thing. I mean, I just said hi, so it's not doing anything crazy, but but it's so. You you push hi to a branch. Sure. Somewhere a $25,000 computer is doing nothing. You pay my token bills, Berg.

**[10:35](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=635s)** Yeah sorry. But answering that prompt? Wonderful. Yeah. Anyway, so, yeah, so that's running in the cloud in in this case, it's going to open up APR with with that work, which was adding confetti, right. So I can go ahead and open this pull request and I can see that, Claude. Oh. Yeah, the Claude agent is there. I didn't know you could. I did not know you could do that. I thought you were locked into the copilot, agent. Freedom of choice. No kidding. Yeah, that's kind of brilliant. OK, so you can use with your copilot sub, you can use the Claude agent within Visual Studio Code. You can delegate gate to the cloud and get that same agent. You can remote in front to your machine where the agent is running instead of being with your family. You talked about that's a huge benefit, right?

**[11:27](https://www.youtube.com/watch?v=ZEL3pr-lwLs&t=687s)** What else do we know about Claude? Yeah. I mean all of the all of the like customizations and all that stuff that works in Claude code also works in this case, right? OK, so if you have a set up there, you can bring it and just kind of just. Work so if you're one of these people that have like multiple subscriptions you can use the same tools right and share amongst those so. Brilliant. Thank you so much, Tyler, for being here. Let's give Tyler a round of applause, if you would. Thank you so much. Betty's gone. What the heck? And we're going to have you back to just talk about Compliment Fest. There's so much lore here we don't get to know. Anything. So much lore. All right, man. All right. We'll be right back, folks. Thank you.
