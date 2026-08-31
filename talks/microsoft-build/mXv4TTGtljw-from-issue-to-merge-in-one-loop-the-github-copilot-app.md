---
id: mXv4TTGtljw
title: "From issue to merge in one loop: the GitHub Copilot app | LIVE162"
slug: from-issue-to-merge-in-one-loop-the-github-copilot-app
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 14
published_at: 2026-06-05T14:59:42Z
video_id: mXv4TTGtljw
youtube_url: https://www.youtube.com/watch?v=mXv4TTGtljw
tags: ["Burke Holland", "From issue to merge in one loop: the GitHub Copilot app | LIVE162", "LIVE162", "LIVE162_v1", "Seth Juarez", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# From issue to merge in one loop: the GitHub Copilot app | LIVE162

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `14 min`

`#Burke Holland` `#From issue to merge in one loop: the GitHub Copilot app | LIVE162` `#LIVE162` `#LIVE162_v1` `#Seth Juarez` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=mXv4TTGtljw) · [Conference site](https://build.microsoft.com/)

## Description

What if you could hand off an issue, watch agents work it in real time, review the diff, and merge, all without leaving one screen? The GitHub Copilot app is a new desktop experience built for agent-driven development.

To learn more, please check out these resources:
* https://aka.ms/GitHubCopilot/app
* https://github.com/features/copilot
* https://aka.ms/GitHubCopilot/app-docs

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Seth Juarez
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE162 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Casual intro and banter before starting the livestream
00:01:10 - Hosts introduce official topic: AI agents and GitHub Copilot
00:01:23 - Introduction to GitHub Copilot App and its purpose
00:02:32 - Comparing workflows: CLI vs VS Code vs Copilot App
00:04:50 - Discussion on cost of code and role of AI in workflow planning
00:06:04 - Demonstrating Copilot App’s holistic project view and focus
00:07:07 - Exploration of quick chats and cross-project ideation
00:08:09 - Examples of personal tools and introduction of Tauri (desktop tech)
00:10:02 - Feature spotlight: seamless project access without manual cloning
00:12:00 - Canvas feature demo—visual interaction with AI agents and repos

## Transcript

*3,081 words · source: supa (en, exact timings)*

**[0:08](https://www.youtube.com/watch?v=mXv4TTGtljw&t=8s)** Hey right. Welcome back. Like, hurry up, Burke, OK, We're doing a show here. I'm so mean to me. Go, go, do it now. Go. We're doing it live. We're live. Hey everybody, what's up? Welcome back. Where's lunch? I I was asking the same thing. I got a stale doughnut back there for you. I bid a little bit off of it. Are you OK with having? Yeah, that's fine, as long as you softened up that I. Sure did. I like the whole thing. It's ready to go. It's. Disgusting. How is everyone? Yeah, having a good time. Really. Hi. Here we go. What are we doing tonight? Can can we come? Yeah. I mean, we have no plans. We're seriously we. Have no one has invited us? No one. They don't invite us to things. It's not even a joke. No, I somebody was like there's an open claw meet up at GitHub and I was like, can I go?

**[0:55](https://www.youtube.com/watch?v=mXv4TTGtljw&t=55s)** And they said no, like what the. Heck, well, I know I went to a thing the other day, MVP thing and nobody invited me and they had to like write something on a, on like a, a name badge like, Oh yeah, you were supposed to be here the whole time. Nice, now they tell you. OK Seth. Yes, we have official business to get done. I have talking points. Yeah, we've been talking agents all day. Here is the surface. Let's talk about the GitHub Copilot. Agents are great. Wait, I thought we were doing. I love AI. But workflow is scattered across. By the way, this is weird because I usually do interviews but he's interviewing me and so it's like the spider man meme right? Now we're pointing at each other. Exactly. Well, we're going to have to, we're going to have to figure out how to make this work.

**[1:43](https://www.youtube.com/watch?v=mXv4TTGtljw&t=103s)** It's going to be a disaster start to finish. But we're talking about the GitHub Copilot app, which is because I know what you need is another app with which to do a gentech thing. And good luck, because we've got one for you. That's right. And now here's the thing though. Here's the thing though. I have because I I like to categorize things in my head so that I know where things fit because I have like an OCD brain. I didn't know where things fit or I will not fall asleep. So we have the CLI. Yep, we have agents in VS Code. Correct. Now we have the GitHub Copilot app. Why do we have the GitHub? And this is where this is where I'm starting to think like it depends on where the code is in your workflow and where the projects are with respect to your workflow.

**[2:31](https://www.youtube.com/watch?v=mXv4TTGtljw&t=151s)** Hear me out, OK? When you're in the CLI, you are zoned in on a very specific project, very specific task, nothing else. OK. And you are not necessarily super interested in seeing the code while you're doing work. You are interested, you know, perfunctorily, right? That's is. That a word? Yeah. No, it is a word. But I'm not. I'm a simple man. You're going to have to dial it back. It's I know OK, so I am not. I don't even know how to say it, otherwise I'm not interested in looking at the code. So what is another word for? Perfunctable. I didn't think I used it wrong everyone. Can't even think anymore anyway. Use the CLI for this one because you're not looking at code right. You're you're focused in. So that's CLI. When you're inside of Visual Studio Code, you might be working on something in a specific project, but you're very

**[3:20](https://www.youtube.com/watch?v=mXv4TTGtljw&t=200s)** concerned about, for example, you're building an SDK and you're very concerned about API shape. You want to see the code that's being put out. You're working with the files and looking at it. Notice if that's one click, stop up, right? Because when in the CLI, you're literally looking at I'm going to solve this thing and do it, but I'm not looking at the code. And if you are at somewhere else in VS Code, same agentic harness, but you're looking at the code that's going on, the Copilot app is a click stop up from that because that is multiple projects at the same time. You see. So if you're working on a lot of things at once, like you're starting your day, you might have like 5 or 6 projects, GitHub Copilot app start your day, see what's going on. If you can go to my screen here, you can see I have a home thing I have what am I working on? Add fetch virtual guidance for work IQ. You can see your particular word.

**[4:07](https://www.youtube.com/watch?v=mXv4TTGtljw&t=247s)** Oh, I have a lot of have a lot of security things I need to do. Yeah, take care of those dependent bot. Dependent bot, right? Notice that this is now zoomed out from the I'm super laser focused on a project, not looking code. I'm super laser focused on a project. And you're like at the repo level, I'm at the. Repo, multiple repo. So that's how I like to think about. What do you think about that? What do? You well, I want to, I want to hear more about it. Like what, Why, why is it that we would want to have this view of the world other than a like a? Because it seems to me like what you're describing is if I'm in BS code on a project, it's like a bottom up view of the world. And this is like a top down view. And here's the thing, like, and this is the part like everyone's like, the cost of code is now zero in tokens. It's the cost of tokens. But the reality was, and here's the secret, and I'll tell you, make sure I'll whisper it because I don't.

**[4:56](https://www.youtube.com/watch?v=mXv4TTGtljw&t=296s)** I want to know code was always the easiest part. Yes, that has always been true. I would agree. Like when you're pen to code, I, I don't pen to pen to pen, keyboard to pencil. When you're doing the code, when you're doing the code, you have already thought everything through. There's nothing else to think about. You're writing it and then as you're going, you're thinking about, oh, this isn't working. You're. Coding and thinking as you go. But the, but the, the but the higher level of what I'm trying to accomplish is over because you're writing like, I'll give you an example. I'll give you an example. I'm writing a website and I needed to, I need a submit button to launch something in the outer space. Super easy, right? When you're doing that, you already know all the systems that you're going to integrate with. You already know that there's going to be a button.

**[5:44](https://www.youtube.com/watch?v=mXv4TTGtljw&t=344s)** You already know that you're no longer saying, yeah, yeah. It's like you already know most of what's going on and you're at the last mile of the work of like putting from keyboard to code. And that's the thing like, but the real work happens when you're trying to decide what to do and when to do it and what it belongs to. And that's where the copilot, GitHub copilot app is awesome because you start your day and I'm like, oh, let's go back to my screen here. I have a lot of stuff I need to have my agent do. I there's a lot of stuff that I need to figure out. Looks like I have some releases here. Looks like you need to do some other stuff, you know, sketch edits or whatever. I have a holistic view of what's going on and then I can start to zoom in with the git. But that now that's just the projects that you have loaded in, right? This is the other thing I like is because on

**[6:32](https://www.youtube.com/watch?v=mXv4TTGtljw&t=392s)** GitHub you see everything and in here it's just this stuff, the subset, just what I'm working on. I like that a lot. I don't know about everybody else, but like when it comes to Git up notifications, like I go in there and I look and I'm like, Nope, Nope. They go right back out again. No, because like I haven't so many projects that like I don't even look at like, you know how there's like I don't know what that view is on dot com where it's like all the things and I'm. Just it's everything. It's literally I'm just like. Yeah, but this is not everything. This is like what I have to do now. So this is the project level. But the cool thing about the GitHub Copilot app is it allows you to start at the holistic level, decide what to do. And then when you go like for example, I was trying to get, I was trying to get some Foundry local stuff to work. Notice that in quick chats, this quick chat thing is like, not in a project, yes. It's like me ideating about work, yes.

**[7:22](https://www.youtube.com/watch?v=mXv4TTGtljw&t=442s)** And so notice that that again, is outside of a single project, not the holistic view of life. But maybe I'm trying to think about a thing, to do a thing, and. That is super nice because I can't touch any of your files. No, because a lot of times I'll ask a question in the AI, I'll be like, Oh yeah, it's this. I went ahead and made that change. Like, no, I would just wanted to know. I didn't want you to actually do anything. Yeah. And not only that, but this can span multiple projects. Like for example, I, I work, I work on a lot of side apps now that help me like do presentations. I built something called cut ready. I've used one. Yes, I built something called Snipse to help me hotkey. I built something called Allusum to help me show. Like build something to help you name things. Yeah, I those names are delightful. Like cut ready that. Doesn't that sound like a thing? Amazing Snipse obviously AI generator. But the thing about yeah, for sure. But the thing about is they're, they're all you.

**[8:08](https://www.youtube.com/watch?v=mXv4TTGtljw&t=488s)** They're all Towery apps. Is that how you say Towery? How do you call it? You know the. You've got to stop using these words. Bro no towery is a real thing. Towery. This GAURI. Has anybody heard that word? Raise your hand. You heard that word. No one has heard. You just made that up. Come on from. All these people here, this thing right here, Did I call it wrong? Yes. What's it called, Tari? I'm like showing up at a party saying a thing wrong like an idiot in front of. Well, I didn't know you were talking about a technology. I thought it was like an English word. Oh no, no, no, this thing. Sorry. This is cool, right? Because this is like an Electron super thin web view with Rust in the back end and all of my clients. What is this? Is This is what you're building? On no, I'm building OK, And so as I'm building these things, I've noticed that there's shared infrastructure that I'm using across on my apps.

**[8:58](https://www.youtube.com/watch?v=mXv4TTGtljw&t=538s)** And so for example, in the GitHub app I can start ID 8IN quick chat. Hold on, several of my projects are using the same thing and I find that we've written the same thing over and over again. Is there a way for us to like put these things together? So for example, agentive is the harness I used that I wrote in Rust to do agentic stuff in my tarry tarry. Tarry. This is where I do the ideation for this kind of thing. Now can you click into that for a second? Now I did notice that in the quick chat that so down there you actually so the other thing I like is like I'm chatting, I'm chatting and I'm like, OK, I actually want to do this. You can then pick the project that so if you go down you can then attach the quick chat session. I do not where is it by the. Way right next to you, right next to your cursor over right boom and you can just pick it and be like OK, now go do it. So it's like disconnected until you want it connected and

**[9:47](https://www.youtube.com/watch?v=mXv4TTGtljw&t=587s)** then it's. There, it's disconnected until we're connected. Until it's connected. Like our dinner plans tonight? Right, we have none. None. We're disconnected until we're connected. Right, with all these folks, yeah. So this is the cool part. This is the cool part about about this. But then the last thing with the copilot app is you can actually zoom in again and start to work on like your own. For example, Hey, resume, this is a elusive is my my program, my thing. That's an agentic, you know, draw stuff for me to explain stuff. I can actually go through and look at all the stuff that it's doing and then zoom in to the exact changes. So notice that the Copilot app allows me to start holistic with my work. I can think about multiple projects at once and then I can zoom into a single product.

**[10:34](https://www.youtube.com/watch?v=mXv4TTGtljw&t=634s)** So This is why these are all different apps, but they have different for me head spaces. So sometimes I'm in the CLI a lot. So for example, here you can see I was doing some work with Allusum in the Copilot app and in VS Go because I was interested in the in the API shape. But then I can go over here and take a look at some of the changes that were there. So that's how I tend to navigate these things. Except let me tell you the thing that I love most about this app. This is the single best feature of any app. Is it canvas? No. I. Was going to show that. Next, whenever you start working on a new project, what do you got to do? Like an existing project. What do? You got to do. I got to get a drink. No. Oh sorry. No, no, you go out, you get the URL, you clone it, you have to clone it to your machine and then you have to open the editor like it's a whole thing, right? But go open so find a new project to work

**[11:23](https://www.youtube.com/watch?v=mXv4TTGtljw&t=683s)** on. This is such a simple thing, but this is the thing I find most. Compelling my to. Do no no no no go to GitHub, GitHub. So pick one off GitHub. I did. Did you? Yeah. Oh. Go to get hybrid pots or yeah just pick anything. So imagine you're starting work on a new project. Oh, let's pull a gentip. That's the thing I was just telling. You boom and then it's just there and you can just start working. Like there's no clone, there's no opening the in a work tree. I know it's a in a work tree. I know it's a small thing, but like this is the kind of stuff that that really excites you, but it's better. I don't care. About It's better. It's better let's talk about canvas because we got like 2 minutes. So canvas. The thing I like about canvas is we, and this is the zoom out. Now this is like the drop the mic situation. We are used to talking to these things via chat. Like I got to interact with this thing via chat,

**[12:11](https://www.youtube.com/watch?v=mXv4TTGtljw&t=731s)** right? Canvas allows you or allows the LLM or the agent harness to actually create a canvas where you can interact with it a little bit differently. So for elusive my my diagram generator thing, I built a canvas that allows me to like like explore the repo and make sure I know. So for example, if I go over here, I want to say elusive at a glance and I'm like, hold on, wait a minute. I don't know, tell me what core is. I can actually click on this thing and it will go back and the agent will be like, hey look, this is what this thing is. Oh it it sent a prompt to the agent. Yes, and I can talk with the agent to update the canvas. So now I have this way of interacting with the and this is only going to get better. This is super early.

**[12:58](https://www.youtube.com/watch?v=mXv4TTGtljw&t=778s)** This is this is using the diagram generator that I have. It allows me to know and interact with the agent harness in a different way, not just yet. Yes, this is super interesting. The idea here is that you want AUI to interact with the app that doesn't exist, so you just create it because you can do that. For instance, like one of the ones that I created was similar to what you did, but I said, show me all of the projects in this app and put Maine in the middle. And then show me how far they've diverged from Maine just by positioning so that I could visually see which ones were like way off, like way, way behind. So that's like the kind of stuff that you can't get. You can just build it all. Right. Look, how cool is it? I click on stuff and I'm like, hey, it's like, hey, look at because this is the internals of how these things are drawn. And it's like, hey, the inspector is the control panel for editing, blah, blah, blah.

**[13:45](https://www.youtube.com/watch?v=mXv4TTGtljw&t=825s)** Well, tell me about the document. And it's just very cool. And then I can also go the other way as well. And it's just a super cool feature. It's awesome. You know what I love, Seth? I love that everything is moving so slowly and it's so easy to understand all the new features and technology. You know, it used to be hard. Now you're. Smearing my makeup here, Burke, I just. I'm exhausted. All right, Seth, thank you very much. On behalf of everyone. Thank you, Sir. Get out of here. All right? We'll see you. See you. Bye. We'll be right back.
