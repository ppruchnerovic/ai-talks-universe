---
id: lGrcC737YLo
title: "Build and ship faster with a developer-optimized Windows experience | LIVE172"
slug: build-and-ship-faster-with-a-developer-optimized-windows
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: ["Nikola Metulev", "Beth Pan", "Aditya Ramnathkar"]
channel: "Microsoft Developer"
duration_min: 17
published_at: 2026-06-04T14:07:27Z
video_id: lGrcC737YLo
url: https://www.youtube.com/watch?v=lGrcC737YLo
youtube_url: https://www.youtube.com/watch?v=lGrcC737YLo
tags: ["Aditya Ramnathkar", "Beth Pan", "Build and ship faster with a developer-optimized Windows experience | LIVE172", "LIVE172", "LIVE172_v1", "Nikola Metulev", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: []
transcript: true
---

# Build and ship faster with a developer-optimized Windows experience | LIVE172

**Nikola Metulev, Beth Pan, Aditya Ramnathkar**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#Aditya Ramnathkar` `#Beth Pan` `#Build and ship faster with a developer-optimized Windows experience | LIVE172` `#LIVE172` `#LIVE172_v1` `#Nikola Metulev` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=lGrcC737YLo) · [Conference site](https://build.microsoft.com/)

## Description

Take a closer look at a developer-optimized Windows experience built to help you move faster. You’ll see how streamlined workflows across WSL, Terminal, WinGet, and your favorite tools reduce friction, leverage agents, build repeatable scenarios, and scale AI projects with confidence.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Nikola Metulev
* Beth Pan
* Aditya Ramnathkar

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE172 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Overview of new developer-focused features including Core Utils, native Linux containers, one-command setup, and local AI hardware.
00:01:58 - Demonstration of Winget configuration files and GitHub repository for customizable developer setups.
00:03:45 - Announcement of general availability of Winget configuration and transition to next segment on developer device setup.
00:05:20 - Introducing WSL containers: Native Linux containers on Windows
00:06:14 - Demonstration of WSLC for managing containers
00:09:38 - Demonstration: Running a Rust app with packaging and identity via WinApp CLI
00:10:00 - Cross-framework development without Visual Studio or system complexity
00:13:23 - Security and permission-based access for AI agent actions
00:15:50 - Closing remarks emphasizing developer feedback and community-driven improvements

## Transcript

*3,086 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=lGrcC737YLo&t=0s)** Hello everyone, hope you're having a great time at Microsoft Build. This is Aditya Ramnathkar, Product Marketing Manager, and I'm today I'm joined by Beth Pan and Nicola Matulov who are Principal Software Engineers. We are all a part of the Windows platform team. In the keynote this morning you saw how we are making Windows the best OS for developers. We have optimized the Windows 11 experience to be developer 1st and distraction free. We are shipping a ton of developer goodness this week. Core Utils, native Linux containers with WSL one command environment setup with developer configurations, agent augmented coding with Windows development skills and intelligent terminal. And lastly, purpose. Next generation hardware purpose built for local AI and sustainable workloads.

**[0:46](https://www.youtube.com/watch?v=lGrcC737YLo&t=46s)** All of these designed to make you build and ship faster on Windows. Let's take a dig into each of these. Beth has been talking to developers, getting their feedback on what is the experience to get started on Windows and we'd love to hear from her. So we've talked to a lot of developers in the past couple years. We've heard a lot of your feedback. This is why we're doing these things. One of the main pain points from our developer audience has always been, you know, why is my machine needs a lot of updates and setup and how do I get to the clean state that I, you know, there's no distractions that we, I can have everything that I need and just ready to go and I can be productive. So as Aditya said that we're gonna, if you're a developer and you come into Windows, we're gonna offer you a way to set up your machine to remove all the distractions that you've been asking us to remove and

**[1:34](https://www.youtube.com/watch?v=lGrcC737YLo&t=94s)** then installing everything that might be useful for you. So tell me what are you guys favorite developer configurations or apps? I love power toys, I just use that every day of. Course. I just use all the tools whenever I need them. I want them to be available so get Python node. I use all of them. All of them all. Of them, you're going to get all of them. So Python, Node, MVM and Power toys. We have a lot of these apps that's going to be installed through this Winget configuration file that we're going to publish. And you can see on my screen here, it is a GitHub repo that will be public and then our developer friends, if you want to fork this, configure it however your way. It'll be flexible. Is there an option to add any other tools? Of course, that's the whole point of Wingat configuration.

**[2:24](https://www.youtube.com/watch?v=lGrcC737YLo&t=144s)** Any other questions? Right, so I can take this file now and I can just run it through Winget and I can install all the tools that we recommend for developers they might need. So it installs git and what else does it install? It is kind of like how you call it opinionated way that we think what's important for developers. For example, we don't need you to turn on developer mode anymore. You we don't, you don't have to turn on developer mode anymore. Dark mode configuration, things like file, hidden files like File Explorer, some of the configurations there. There's a full list of things that you can see. I can go back if we want to to see the read me and see the list of applications is going to be here. So I don't need to go to settings anymore and do that one by one.

**[3:11](https://www.youtube.com/watch?v=lGrcC737YLo&t=191s)** Nope. I can just run and get configured. Correct. Awesome. Now my understanding is that this is by default going to be on some of our new devices we announced today. And this is for developers that might want to set up their existing devices with all the new tooling and existing. Tooling, that's a great call out. So if you're coming into Windows to our shiny new boxes, right, this is just going to be set up for you as a developer. If you want to you know compatibility is something that we treat very seriously on or with English is hard, then you can use this Wingat configuration by yourself. Awesome. And today it is generally available, so try it out now right? What next bit? Since we're talking about setting up developer devices, let's say that I have a machine that I set up today. What do I do?

**[3:57](https://www.youtube.com/watch?v=lGrcC737YLo&t=237s)** I feel like as a developer, I will go to Terminal to see what's going on there. So today we're making it available for people to use all these cool Linux style commands, core utilities in Terminal. Remember this thing that you've been asking for here again, you asked? Well listen now you can do grip with internal OSO. Finally. For example, there's a very simple demo that I can just check my net stat status. And something else that I find very interesting is, you know, let's say that you want to do some sort of PowerShell and then I grab something after it. So this is an example of merging these two kind of systems together.

**[4:46](https://www.youtube.com/watch?v=lGrcC737YLo&t=286s)** Right. So now, if you're copying some code from, let's say Stack Overflow, right, or you're getting some scripts from GitHub that might have been written for Unix or Mac or Linux, they will work if they're using all these creatilities because they will also be available on Windows. They can make available so you don't have to go and translate it to PowerShell. Exactly any other questions class? That's great. I think we're going to move on to. Since we're talking about Linux Unix commands, let's talk about WSL as well. Sure. So as we all know, containers are a core part of modern development workflows. And to make that experience seamless on Windows today, we are introducing WSL containers, a built in way to create, run and interact with containers directly on Windows. So whether you're working on local development, AIML workflows, or even containerized testing, Linux containers just work natively on Windows

**[5:38](https://www.youtube.com/watch?v=lGrcC737YLo&t=338s)** out-of-the-box. As a part of WSL containers, we are shipping WSLC, which is a binary that you can use to create, run, and interact with containers directly without having to install any third party tools or require additional tooling efforts. This all ships with the standard WSL update, so you don't have to do any other configurations apart from just updating to the latest version. Wow. Awesome. And it is as simple to use as just listing your existing container. So you can see WSLC container LS easier. It shows me I have one container running, I can go into that by attaching it to the container and then I'm gone into my Linux shell.

**[6:26](https://www.youtube.com/watch?v=lGrcC737YLo&t=386s)** I can just do all my Linux workloads. When I am done, I can come out of the shell and just detach it and then quickly see the status again or work as needed depending on my workflows. This is feedback we have been receiving from developers for a very long time of being able to just natively run containers inside of Windows. But the thing that really excites me here that you mentioned is also that we also support this as an API, right, Which enables usage of these containers inside of applications. Which now means that I can have a native application that has native UI, it's running Win UI or WPF or whatever it is, but it could also have a Linux container as part of it. So it could mix this Linux code that you might be using across platform, but it's not running natively inside of your Windows machine next to your native code for Windows, which is opens up all these possibilities for creating this incredible experience.

**[7:15](https://www.youtube.com/watch?v=lGrcC737YLo&t=435s)** And with that, we're also allowing some new controls for enterprises to manage these Linux containers so that they have visibility and observability to all the amazing work that the developers are doing in their enterprises. So that's. So we've talked about, you know, setting up your machine, we went to terminal and talked about core utilities and we talked about WSL kind of naturally transition into building apps on Windows and now building apps for Windows. Nicola, do you have a? Right. So as part of the work that we're doing here and stuff that we announced today at the keynote is we're making it really easy for developers to build Windows applications with AI tools. So either using GitHub Copilot or using Cloud Code. So for example, here I have GitHub Copilot open on my machine. And some of the things that we announced is a new set of agents and skills for Win UI development or Windows development in general.

**[8:03](https://www.youtube.com/watch?v=lGrcC737YLo&t=483s)** So for example, here I have installed a plugin called Win UI. So if I list all my plugins installed here, you'll see we have this new Win UI plugin right there that's installed. This comes with several skills and agents. So you can see here we have all these Win UI new skills that exist as part of this that do things like, hey, packaging or code review or design that bring all that back together. The interesting thing part this is, this is not just about markdown, right? Anybody can just create a Markdown file and call it a skill. As part of the work that we're doing here, we're creating a set of tools that agents can use to make it really easy for them to develop Windows applications end to end. And through this process we're able to save over 70% of tokens that we can measure. So that was saving a lot of the cost when using these AI tools to build Windows applications.

**[8:51](https://www.youtube.com/watch?v=lGrcC737YLo&t=531s)** There used to be a lot of steps right around how you're actually writing your code before. It's like templates initiation. Is that what you're doing now? And then all of the packaging identity. Great. Exactly, Agent will take care of that for me. Right. So before it wasn't that easy to do that other thing. You have to use Visual Studio for a lot of these different things. So an agent wasn't able to go and use the terminal to be able to run a packaged applications or add identity to a running application. So what we've done here, we've added a new CLI called the Winamp CLI we announced earlier this year. You can just install it through Winget with just Winget, install Winapp and you'll be able to do a lot of these different commands as part of that. So you can do things like packaging directly from just a folder. You can package it as an MSI X or you want to run an application directly as with Identity, you can do that quickly.

**[9:38](https://www.youtube.com/watch?v=lGrcC737YLo&t=578s)** Like for example, I have a Rust application here. This is just a Rust console application that I've created here and I can just simply Winapp run the application here and it will run this Rust based console application and it will really give it package identity. So you can use those APIs like a lot of the notification APIs or you can use a lot of the AI APIs that we have in there directly from here. No Visual Studio required. And I don't have to learn all the nitty gritty of the whole Microsoft system if I'm a Rust developer. You continue developing with the framework that you're already using, but it's best. But exactly we can extend it with the existing APIs really quickly. We are having to use a lot of the other tools. I love the. Name by the way. Thank you. We also added some other features to our skills to be able to make it easier for them to build Windows applications.

**[10:27](https://www.youtube.com/watch?v=lGrcC737YLo&t=627s)** For example, we now have new net new templates for Win UI. So an agent can create new Win UI application as well as users and be able to get started quickly with the best practices in mind so you don't have to guess on how to build an application. And through the integration with Winapp, we can now also run these applications directly from the terminal. So now you can run a fully packaged application directly from the terminal when your application in this case. So I no longer need to open VS Code at all. You can, you can, you don't have to. It's up to you, but you can do everything here. And the whole idea is that now an agent can fully build an application from creating it through debugging issues. We have tools here for figuring out the stack traces for what when something went wrong. We have tools for figuring out what the code you should use, what controls you should use.

**[11:15](https://www.youtube.com/watch?v=lGrcC737YLo&t=675s)** We we connect the agents to samples so they can know what the best practices are. And one of my favorite things here that we do also, we have a utility for interacting with Windows applications. So if you use the Winamp UI tooling, for example, you can inspect running applications. In this case I have notepad that's running here on the side and you can see here I can see all the buttons and everything that's as part of that application. And I can even from the terminal I can invoke that button there it. Looks at the visual tree and. Exactly. It can take screenshots so as an agent it knows when something is functionally working so he can on its own fix issues and it can catch those type of. Issues iterations. That's right.

**[12:01](https://www.youtube.com/watch?v=lGrcC737YLo&t=721s)** That sounds really exciting. How can I get started? The best way to get started is just to go on AK dot Ms. Win UI skills and you will to download our skills. Or you can download the Win app CLI on its own. But there's one more thing I want to show you here that we announced today, which is the intelligent terminal. The intelligent terminal is this fork of the Windows terminal that we all know and love that has some experimental features of integrating agents directly in it. So it's a different I have them side by side. Here you can see I have two different terminals running. And you can see this one has this little nice cute icon on the bottom. But for example, let's say I'm here and I run a command that errors out. In this case, I probably forgot how to type something or I mistype it. You'll see here that this terminal now can actually analyze that whenever it happened and it can allow me to say, OK, we know how to fix this.

**[12:50](https://www.youtube.com/watch?v=lGrcC737YLo&t=770s)** You probably just meant to add the force attribute there. Or I could open up directly into the attached included agent view as well and I can interact and I can ask it to do things. I can just say fix it for me and it will just go in magically. Has context of all the running commands that I ran across all my tabs. It comes with copilot already built in but I can connect it to Claude if I want it in here or other agents as well. And I can experiment. So experimental. We'd love people to give us feedback on this. I assume it's gonna ask me for permissions to do these things, right? Of course it's all permission based. You have to approve to access all your commands. You have approve to actually run commands for you. You can't just do it. But again, it's experimental. You have to install it side by side and try it out and give us feedback. So what if I don't use GitHub profiler?

**[13:37](https://www.youtube.com/watch?v=lGrcC737YLo&t=817s)** Can I add other agents as well? Right exactly. So you can bring in any agent that you have as part of it. You use the same protocol that all these agents use and you can tie it into here. You can just go to settings and set it all up. I don't have to remember how to cherry pick things anymore. Right that's my one of my biggest things I go to online searching is forget issues. Whenever something happens and my state is in the wrong, whatever, I have to always go. How do I reset back without losing any of my changes? What is the command I have to use? I never remember. I can just ask it in line without losing contacts and knows what I'm doing. I'll just do it. That's going to be such a great productivity. I can't wait to get started on that. Exactly. Cool. OK, so along with all these software optimizations that are available to all Windows 11 devices, today we also introduced

**[14:26](https://www.youtube.com/watch?v=lGrcC737YLo&t=866s)** Surface RTX Spark Dev box. It is a developer first GPU machine coming with the new NVIDIA RTX Spark that provides up to 1 petaflop of AI compute and 128 gigabytes of unified memory. Access. I'm getting that on day one. That's great, and it also comes optimized with all our amazing developer tools already available by default, right? What's that mean? Shut up and take my money. OK, let's roll the video. I was pulled to you. It's because of all the butter loved you still all

**[15:23](https://www.youtube.com/watch?v=lGrcC737YLo&t=923s)** my life, that you really ever loved me. And it won't be only when I'm good. Not that I'm gone. What do you think about me? Think about me, dream about me? What do you think about everything? Simple. Awesome. I think we've talked about a lot of the things today that we talked about is actually based off of our developer audiences feedback. We call it voice of developer. We treat that very seriously. Some of them takes a long time to come out as well. We'll do a good job in the future as well to go take our communities with us and build a great Windows environment for our developers.

**[16:15](https://www.youtube.com/watch?v=lGrcC737YLo&t=975s)** Yeah. And we have shipped a lot of developer goodness today. So we'll love for all our developer community to go try out these and integrate them in your workflows and let us know what do you think about it. Cool. I think that's it. That's it, yeah. Thanks everybody. Thank you so much.
