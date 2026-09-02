---
id: y6IS0pKiAes
title: "What's new in GitHub Copilot CLI? | LIVE152"
slug: what-s-new-in-github-copilot-cli-live152
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Evan Boyle", "Burke Holland"]
channel: "Microsoft Developer"
duration_min: 17
published_at: 2026-06-05T15:34:16Z
video_id: y6IS0pKiAes
url: https://www.youtube.com/watch?v=y6IS0pKiAes
youtube_url: https://www.youtube.com/watch?v=y6IS0pKiAes
tags: ["Burke Holland", "Evan Boyle", "LIVE152", "LIVE152_v1", "What's new in GitHub Copilot CLI? | LIVE152", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
topics: ["AI in the SDLC & engineering orgs", "Coding assistants & agents"]
transcript: true
---

# What's new in GitHub Copilot CLI? | LIVE152

**Evan Boyle, Burke Holland**

`Microsoft Build` · `Build 2026` · `2026` · `17 min`

`#Burke Holland` `#Evan Boyle` `#LIVE152` `#LIVE152_v1` `#What's new in GitHub Copilot CLI? | LIVE152` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=y6IS0pKiAes) · [Conference site](https://build.microsoft.com/)

## Description

This session walks through what's new, including a redesigned terminal interface, Rubber Duck for second opinions, recurring prompts with /every, and hands-free voice mode, so you know what to go try today.

To learn more, please check out these resources:
* https://aka.ms/GHCP/CLI-Learn
* https://aka.ms/GHCP/CLI-bestpractices
* https://aka.ms/GHCP/CLI

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Evan Boyle
* Burke Holland

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE152 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Show introduction and guest Evan Boyle from GitHub Copilot CLI team
00:00:34 - Evan explains his role as engineering manager and hands-on developer
00:01:19 - Introduction to Copilot CLI and its core components
00:02:03 - Demo recap: using Copilot CLI to build a fun interactive project with audience
00:05:00 - Discussion on working in terminals vs editors and why CLI streamlines focus
00:07:58 - Evolution of modern terminal interfaces and team’s fast development velocity
00:10:01 - Demonstration of slash review command and multi-model code review
00:13:08 - Customizing brevity settings and personal instructions for agent communication
00:14:00 - Introduction to voice mode using local models and benefits of speech interaction
00:16:20 - Closing remarks, upcoming sessions, and encouragement to try Copilot CLI

## Transcript

*3,168 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=y6IS0pKiAes&t=6s)** Oh, are we on? Are we live? Oh, thank you, Tom. What's up, everyone? Welcome back. Welcome back folks, folks. Who are? Here and at home, I'm here with Evan Boyle from the Copilot CLI team and a huge fan of fish fishing. All things fish. All things fish, Evan, what is it that you say you do here at GitHub? GitHub yeah. At GitHub, Yeah, at GitHub. So I'm an engineering manager, but I'm a very hands on guy. I don't think that you can build dev tools and be a manager in that space without writing a lot of code yourself and like living the life of your users. So my team builds a bunch of things. We build the core agent loop that powers the Copilot CLI and the SDK, and increasingly all of the agents

**[0:56](https://www.youtube.com/watch?v=y6IS0pKiAes&t=56s)** across Microsoft and GitHub. So that agent loop and runtime the SDK, the Copilot CLI and newly the GitHub app. Yes, which we saw on the keynote, which we saw on the keynote. And by the way, Evan was with us two nights three nights ago when we rewrote the whole demo from scratch. At GitHub HQ until midnight until midnight. Interesting times. All right, so we're going to look at the Copilot CLI today. I was actually on the bus coming over here this morning and was talking with someone and the person behind me tapped me on the shoulder and said, what is the copilot CLII? Keep hearing about that, but what is it? So maybe we should just start there. Yeah, we can totally start there. So I am in the Copilot CLI right now. You know, I just did a task, a talk with Cassidy and we created this repo here.

**[1:50](https://www.youtube.com/watch?v=y6IS0pKiAes&t=110s)** And so this repo basically we asked people to open issues to decide what we were going to build live during the session. Pretty fun stuff. Got 60 issues open and then with the Copilot CLI, what we did was we asked it, hey, go read through all of these issues. If you shift tab here inside of the CLI or sorry tab, you can see all of the open issues. You can see all of your open PRS. And so we had the Copilot CLI go analyze all of those issues, pick out the best one and then we went to go implement it. So what the audience asked for was this little octocad that was going to sit here and, you know, shower you with emojis when you did git operations.

**[2:39](https://www.youtube.com/watch?v=y6IS0pKiAes&t=159s)** Just any git. Operation, any git operation. So we fed that issue into plan mode, created a plan and then let it go on autopilot. And so it built this initial version. And then we asked, hey, audience, go open up a bunch of requests for ways that we could improve this. And somebody asked for goblin mode, which is what you could see here right now. Is it because GPT was talking about goblins a whole bunch for a while? We were. They fixed that. They did fix it. They put out a really interesting paper about it, actually. Yeah, I would like to know why that is. And so we actually just got to the point that we had. So we picked out five features. Goblin mode sounds, eyes following the cursor visibility. Eyes following the cursor.

**[3:29](https://www.youtube.com/watch?v=y6IS0pKiAes&t=209s)** Does that work? Oh, that that one didn't make the cut, I guess. And then slower animations. OK, so I think what I'm going to ask right now is instead of opening APR, I'll I'll do this with voice too. So I'll hold down the space bar. See this little voice meter pop up? All right, instead of opening APR, I want you to just push directly to make. That sounds like a great idea. This is this is my repo. It's not my personal repo, so you know. Force push to main. I don't do that on our team repos, but for this one it's OK and I'll turn up the volume here and see if we can see if we can hear. So the the goblin here, the goblin cap purse every couple of seconds and then it meows when you commit

**[4:18](https://www.youtube.com/watch?v=y6IS0pKiAes&t=258s)** shipped it. There we go. Nice. So this was an electron app that we created with the audience in the course of, I don't know, 2025 minutes. Very nice $1600 worth of tokens. I don't think that many, no, only I don't know, this is like 5 or 10 bucks I think something like that. That was all. That was all it was. I I got to do the math, but 1300 credits, I don't know what that converts to. OK, so on the CLI I have a question. Yeah why? Why am I in a terminal and not in an editor? Evan? Why do I need this exactly? I think, I think the nice oh, there we go. It's making noises. I don't know if you heard. That no. I can't hear. So yeah, I mean, I I think the terminal for me brings an awful lot of focus. There's no distractions. I can see the logs.

**[5:06](https://www.youtube.com/watch?v=y6IS0pKiAes&t=306s)** Also, it's kind of fun to feel like a little bit of a hacker, right? Yeah. So it's easy to Multiplex these things. I can use Teamux and run multiple instances. If I have a big monitor, I can cascade multiple of these across my screen. And we've even turned the CLI into like if you like working in parallel, but you're working on a small monitor like this, We now have this slash new command. So slash new lets me start a new conversation. But, and so I could say like, go do some research on open issues that we might want to address, right? But then I can go to slash sessions and I can see all of my other running sessions in this instance. So the Copilot CLI can now manage multiple sessions in parallel, have all of those tasks running and you can

**[5:56](https://www.youtube.com/watch?v=y6IS0pKiAes&t=356s)** switch between them. So if I go back to this original session, all right, it's live now. I'm going to ask it, Hey, go close out those issues we implemented, add a friendly message and a thank you to our community members. Cool. So wait a minute, so when you do new slash new IT starts a new session, but it the other one it's sort of backgrounds. It, yeah, it backgrounded that existing session and I can see everything that's going on in parallel and switch between. So hey, I trust it to go and close out these issues. I'm now going to go back to my research session, right? So research open issues, crawling through the issues, reading my read me right. But it's, it's so it's super interesting to me though,

**[6:46](https://www.youtube.com/watch?v=y6IS0pKiAes&t=406s)** like why are we back in terminals? Why are we here? Why are? We here, but I agree with you. I don't know if you how many people have used like CL is here recently to do coding and development. See, like, look, there's not a lot of folks look like a couple hands here, but how many people are using editors and agents? So if you haven't tried using a terminal and a CLI because you're like, why would I do that? It's because it's a magical experience and I can't put my finger on why that is. My preferred method of working is with Visual Studio Code Open and the Terminal as an editor tab because you can do that and I'll have multiple of them. That's how I work now. The terminal just feels so good and I don't know what it is. It, it does. And I think that, you know, for a lot of

**[7:33](https://www.youtube.com/watch?v=y6IS0pKiAes&t=453s)** people who haven't tried terminal coding agents, like for me, I've never been a Vim or an Emacs person. And I know that when you think terminal, you think, Oh my gosh, I've got to learn a ton of hot keys. It's going to be complicated. I'm going to be stumbling over myself. That's what people think, right? But you know, 2 E applications have gotten so rich that they, they almost feel like a web app, right? They, they feel much richer than they used to like this, You know, this, this view that we have up here with issues with pull requests with gists back to my session. Like it begins to feel more and more like a full application, almost like your ID. And I've noticed that there's actually less keyboard shortcuts in the terminal than there are in Visual Studio Code. That's true.

**[8:20](https://www.youtube.com/watch?v=y6IS0pKiAes&t=500s)** Also someone the other day was like, I want to click on the tabs at the top and I thought, well, you can't do that, it's a terminal. And then somebody was like, no, we already let you click on things. We can make that work. We can't. Oh, and it does work. It does work they. Ship it, we implemented it. Amazing. So this is, yeah, this is one of the things that's really funny about working on a team that is so heavily bought into AII mean you can imagine the team at GitHub that is building the AI tools is the most AI forward, utilizes AI the most. And so it's it's been a couple of months since I did a, you know, I think back in March, I did a survey and with 10 people, we were shipping 2000 PRS a month across app CLISDK, agent loop. And so every time I come in contact with the

**[9:09](https://www.youtube.com/watch?v=y6IS0pKiAes&t=549s)** CLI code base, I have to assume it's completely different than a week ago. If I if I built a feature a month ago and I come back to add something to it, I have to rebuild my view of the world because the velocity of this code is so high. Yeah, moves so fast. Yeah. I was talking to Moss, who built the the new UI here, and I was asking, I was like, how much agent coding do you actually do on the team? He's like, I don't know what everybody else does, but I do a lot. A lot. Yep, a lot. Yeah, very interesting. All right, let's talk about some of the other features of the CLI here. What are some of your favorites because a lot of them are behind slash commands. Yes, a lot of them are behind slash commands. So I'm going to go ahead and start a new session and we'll go ahead and do it in here. So going to bump up the font.

**[10:00](https://www.youtube.com/watch?v=y6IS0pKiAes&t=600s)** I'm going to run Copilot. I'm going to do it in Yolo mode. I don't always do this, but for the sake of demos, I want all of this to kind of stream while I'm working. So one thing that I really like to do is slash review. So this is multi model code review. And So what I'm going to say I'm going to dictate here. I'd like for you to do multi model code review with Sonet 46, GPT 55, and Gemini. I'd like you to then compare the results and only feed me issues where the models are in agreeance. Cool. Is agreeance a word?

**[10:46](https://www.youtube.com/watch?v=y6IS0pKiAes&t=646s)** I think I just made it up. Agreement, I bet. I bet it understands it anyway. It'll understand it. That's the beauty of, you know, LLMS is they they pick up what you're putting down. And they don't care about spelling at all. Like I frequently watch people type and they'll be like, oh, I misspelled that, like backspace. It doesn't matter. I just. Bash the keyboard just for. Sure, just send it. It knows. And so let's see, oh, this is this is really cool. So this is what's called elicitation when the CLI detects that there's some ambiguity, right? Like I ran this slash review command and it's expecting, hey, I have commits that are ahead of my base Rep right? Or I have unstaged or uncommitted changes. In this case, I'm just on main.

**[11:34](https://www.youtube.com/watch?v=y6IS0pKiAes&t=694s)** So it's asking me what I want to do. Like, hey, do you want to review the whole repo specific branch, just the latest commit, merge. I'm going to say let's just go ahead and do the latest commit and merge. Oh. Oh, then you get a free text. Then it says branch name or commit range if applicable. I'm going to just say you figure it out. Oh, it wants you. Best judgment. It wants you. To. I don't have the commit number off the top of my head unfortunately. It gave you something there. It gave you like a look. I thought I saw a hash. Maybe it did, maybe it did, I just missed it. Yeah, we're moving. We're flowing here. I have time to read everything, the agent says. They write walls of text, man. Yeah. I'm too busy. I'm building things, yeah. It's interesting that you say that, because that's actually something that we've experimented with in the GitHub app and probably

**[12:26](https://www.youtube.com/watch?v=y6IS0pKiAes&t=746s)** we will bring into the CLI is sort of different, being able to configure different levels of brevity. Some people really love being able to see in complete detail the entire log. Some people just want the final output. Yeah, say it in as few words as possible. Like, I don't know if you all noticed, if you have people who send you or you read things that AIS have generated. They're like this long, man. Like people send me an e-mail that looks like they spent an hour on it that was written by an agent. You're wasting my time. Boil it down to one sentence. This is. This is the beauty though, of these, you know, these coding agents, the CLI is, there's lots of ways to configure them, skills, hooks, custom instructions. So I'm actually just going to go ahead and like implement Burke's suggestion here. I'll hold down the space bar.

**[13:14](https://www.youtube.com/watch?v=y6IS0pKiAes&t=794s)** I'd like for you to add to my custom instructions that I want you to be as brief and concise and to the point as possible. Unless I ask otherwise like one sentence. Make it easy for me to read and scan. I'm just going to hit enter here. This is going to update my copilot instructions file and generate a new instruction where now the agent is going to be a little bit more tailored to me in how I want to work inside of this repo. I'm doing this in the repo because I own this, but if I was working in a team I would put this in my doc copilot folder where I could have personal instructions that are specific to how I want to work with the agent. Now I notice you keep using voice mode. Yeah. Is that a plug in? Is that something like? How does that work? Yeah absolutely. So you can toggle voice mode on and off here

**[14:04](https://www.youtube.com/watch?v=y6IS0pKiAes&t=844s)** with the slash voice command. And if you show models, we have an English and a Spanish nematron model. There are other models that are available to to download as well. These are local models. These are local models, I believe they're from NVIDIA, but you have. Nematron you. Have to have to check me on that. And the nice thing about these models is that they stream. So the first time you set this up, you have a, you know, a download. Let me see if I can, you know, look back. So it's a big model, it's 700 megs. But the nice thing about that, all of it running locally and then, you know, I don't have to, you know, hit the cloud or you know, hit an inference provider for this. Yeah, that's super nice. So a question, how many of y'all are using voice mode and talking to agents? Is anybody do a OK, have people typed to your

**[14:53](https://www.youtube.com/watch?v=y6IS0pKiAes&t=893s)** agents? So most people why are you are y'all uncomfortable talking to just like speaking out loud because then it sounds like you're just talking to yourself. Is that what it is? Because that's how I feel. I feel uncomfortable when I do it different part of your brain. So like when you when you're typing, you're thinking and when you're speaking. I don't know about y'all but when I speak I don't think obviously. Well, I would say for for me, Scott Hanselman is the one who turned me on to voice mode. He does everything in voice. Mode, he does everything in voice mode. And when we were doing some early dogfooding of the GitHub app and we had these weekly one hour Scott dogfooding sessions where we would watch him use the app and he was using handy at the time.

**[15:41](https://www.youtube.com/watch?v=y6IS0pKiAes&t=941s)** And at first when I saw it, I didn't really get it. And I, I tried it once or twice and, you know, it didn't really stick. But eventually I realized I'm kind of a person who likes to pace around my office while I think, if that makes sense. So I have like a little USB remote that's hooked up to that shortcut and I pace around my office with my headphones on and I ramble at my agent like it's like. Like dictation? Like dictation, like I'm walking around in circles, thinking, staring at the sky. It works for me. In 1965, we're all dictating to recorders again. Exactly. All right, Evan, thank you. Do you have any other sessions here? Any What should people do next? I do. I have AI. Have a 4:00 PM session with Mario about the GitHub app this afternoon.

**[16:30](https://www.youtube.com/watch?v=y6IS0pKiAes&t=990s)** Already did a session with Cassidy this morning that was recorded about the Copilot CLI going in depth on the features. The session with Mario on the GitHub app is at 4:00 PM today. Encourage you all to attend that if you want to learn more about how the team and I use the GitHub app and use agent workflows to guard our focus and focus on, you know, output rather than activity. With coding aids awesome. And for those y'all who listen y'all and for those online, if you're skeptical about these clis, these two is then I I definitely want you more than anyone else to go install the copilot CLI and just try it. Just try it. OK, That's my challenge to you because I understand the skepticism. I was too. Once you do it, you're like, wow, that feels amazing. So just give it a try, see what you think.

**[17:17](https://www.youtube.com/watch?v=y6IS0pKiAes&t=1037s)** All you got to do is Google the copilot CLI. You'll find it. You can't miss it. Evan, thanks for being here. Thanks so much, Bert. We'll. Be right back. Thanks y'all, see you in a minute.
