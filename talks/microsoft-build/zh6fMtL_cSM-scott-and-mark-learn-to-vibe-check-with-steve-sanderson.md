---
id: zh6fMtL_cSM
title: "Scott and Mark learn to Vibe Check with Steve Sanderson | LIVE116"
slug: scott-and-mark-learn-to-vibe-check-with-steve-sanderson
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 12
published_at: 2026-06-05T15:40:52Z
video_id: zh6fMtL_cSM
url: https://www.youtube.com/watch?v=zh6fMtL_cSM
youtube_url: https://www.youtube.com/watch?v=zh6fMtL_cSM
tags: ["LIVE116", "LIVE116_v1", "Scott Hanselman", "Scott and Mark learn to Vibe Check with Steve Sanderson | LIVE116", "Steve Sanderson", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Scott and Mark learn to Vibe Check with Steve Sanderson | LIVE116

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `12 min`

`#LIVE116` `#LIVE116_v1` `#Scott Hanselman` `#Scott and Mark learn to Vibe Check with Steve Sanderson | LIVE116` `#Steve Sanderson` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=zh6fMtL_cSM) · [Conference site](https://build.microsoft.com/)

## Description

AI can turn an idea into a working demo faster than ever. But can that demo survive two experts who have seen every trick in the book? In this live Build showcase, developers present AI-assisted apps, agents, tools, and workflows to Mark Russinovich and Scott Hanselman. Mark and Scott will ask how it works, where the seams are, what the AI actually built, and whether the result is clever prototype, production-ready software, or something unexpectedly magical. Come for the demos. Stay for the technical reveal.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Scott Hanselman
* Steve Sanderson

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE116 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Discussion on AI evolution in software development
00:03:07 - Demonstration begins – showing UI functioning without any written code
00:03:17 - Introduction of Internet Explorer within Vibe OS
00:04:19 - Demonstration: AI can generate any requested app on demand
00:06:34 - Discussion about creating paint app featuring Scott’s image
00:07:02 - Display of generated image labeled as 'normal picture of Scott Hanselman'
00:07:54 - Viewing fully functional OS simulation with Windows CE interface
00:10:12 - Model produces diff updates for stateful UI simulation
00:11:22 - Presentation of award for innovative AI-augmented project

## Transcript

*2,213 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=0s)** Hey friends, we are back. Thank you so much again to our sponsors for making this happen. This is Scott and Mark Learn to vibe check. Our first guest today is the wonderful Steve Sanderson. Steve Sanderson and his extremely well-known programmer. You've probably heard of things like KnockoutJS. He's worked on Blazer. He's done amazing things on the internet. And he has brought us something today that we have not seen. No one here has seen this before. We don't know if it's completely bespoke. We don't know if he wrote it in a caffeinated co-pilot session. It could be SLOP. It could be vibes. It could be AI augmented software engineering. What do you have for us, sir? >> All right. Yes. Um, so what I'm going to show you today could be pretty momentous. So I need to start by putting it in slightly historical context. All right. So the human journey, right?

**[0:49](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=49s)** We've come a long way. stone tools, language and culture, mathematics, computing, and these things are all quite good, but I don't think we've really reached the pinnacle of what we could be as a species yet, or at least until what I'm about to show you just now. Okay, so I know you're probably all thinking like, oh, he's going to reinvent the whole software industry, and we're not ready for all this. I I know you've all had a lot of change to deal with recently. You know, we've moved from this world where humans write code into a world where AI writes code. And I know that that probably feels like quite a big deal to Mark and Scott, but for a true visionary like myself, I'm already thinking about where we're going next. And in fact, I'm already there. So, I'm going to show you and I need to introduce you to a completely new operating system that's going to change

**[1:38](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=98s)** everything about how we work. So, introducing Vibe OS. Okay, it's the world's first completely hallucinated operating system. All right, and I'm going to show it to you right now. So, firstly, it is a real operating system. I can boot it. It's a VHDX file here, about 1.3 GB. Could probably make it smaller. I didn't bother. Um, I could boot it on bare metal, but I'm not going to going to boot it in HyperV. Uh, and so you will see that boot up nice and fast. It's very efficient. And when that comes up, you'll see it's got a beautiful user interface that allows our user to be highly productive. Okay, so here we go. We're ready to get started with that. It's a bit hard to see there, so let's just switch to a full screen view. And um we're going to start by

**[2:26](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=146s)** running a few of the applications that are built in here. So we'll get some of the classics going. So we'll have notepad, we'll have calculator, we'll have internet explorer. And the thing that's unique here, the thing that you will never have seen before is that in these applications, there is no code at all. Everything in all these applications is being hallucinated in real time by the AI. So there's no buttons, there's no event handlers, there's no logic to say what to do, but the application works. So, if I do five divided by three and then equals, if I can find that, it's up there this time. Um, it's 1.6. Okay, so it works, right? But I didn't write any code and neither did AI. There's no AI written code either. It's just producing UI

**[3:15](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=195s)** exclusively with nothing behind it. Uh, and we've got Internet Explorer here. Um, unlike the boring operating systems that you use today, this solves one of the big problems that people have, right? People are always wondering when they're on they're on the internet, is it AI or not? But in Vibe OS, you don't have that problem. There's no question to be answered because the answer is always yes. Everything is AI. So, if I want to, I can go to, I don't know, let's see if we can find uh whether Scott Hanselman has a Wikipedia page, shall we? So, I'm going to go to uh google.com here and let's do a search for Hanselman Wikipedia. and we'll do a Google search there. And I don't need to remind you this, but all of the content you're seeing is completely hallucinated, right? So, it's

**[4:03](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=243s)** just coming directly out of the model, and the UI is being updated in real time as we go. And here's a beautiful picture of Scott Hansel. I'm not sure about that one. All right. But it goes further, right? We're not limited to these built-in applications. We can search for any app that we want. And everyone always does like to do app demos. So, anything that I search for, I'm going to find and it will just be created for me on the fly. All right. So, let's see what else we could find in here. Um, let's go for one of the classics. Uh, En Carter 98. Everyone loves that one. But it's all about Mark Russino. All right. And so we can get a fully customized version of Enart 98 on

**[4:52](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=292s)** whatever subject we're interested in. All right. So lots of facts and figures about um Mark here. Let's see. Selected facts. Senovich has a talent for turning internals into folklore. Great. I assume that's true. I don't know. All right. And other applications that you would want, but normally it's too difficult to make. So like Commander XCE, but it's always rude to you. All right. So that's the sort of application that I think is a genius idea, but it's difficult to get someone to implement something like that. Uh so let's see what we've got on this machine here. And obviously this is always different every time. Okay, there's something suspicious. Let's see if we can run bash in here. What's it got to say to us? Uh bash, you have somehow offended. Okay, fine. All right, so you get the idea, right? This is a

**[5:41](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=341s)** pretty revolutionary way to do computing because we don't need to write any code for any of our applications anymore. Is are there any software you would like to to try out within ViOS? Anything you can think of? >> Uh Microsoft Money95. >> Money95. >> Civilization peaked at Microsoft Money95. >> Money95. >> Uh but but Scott Hanselman has a lot of money. >> Oh, but for Scott Hanselman. Yeah, you can say scoot as well. That's totally fine. >> All right. So, let's see what uh money Microsoft what Scott had in 195. >> Okay. Let's see. Okay. And this is >> this is Scott's checking account. >> What model is in the back end? >> Dear Scott, um it's been a tough month for you, I guess.

**[6:28](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=388s)** >> Where where are the tacos? >> There we go. >> That is amazing. >> All right. So, all right. I want to see paint with a drawing of Scott on it. Paint with a drawing of stars. >> I'm an owl though. >> Uh let's do paint >> before your haircut >> but with pre-installed. >> Okay. >> And so >> and you've got this is co-pilot uh SDK that's doing this. >> This is using Copilot SDK, believe it or not, behind the scenes. I can show you a little bit about how it works if you want. Um so it says it's got a very normal picture of Scott Hanselman for some reason. I don't know what it means by very normal. Um, >> okay. There's a normal picture of Scott Hansselman. >> That's your cage. >> That my cage. That's the cage you keep me in. >> Okay. This is insane. Um,

**[7:18](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=438s)** wow. Okay. Could it This is This is Vibe OS. Can it have nested OS? How many How many OSS deep can we go? Can you simulate like a an Altter 8080? >> That's like a terminal emulator. So I need a simulator simulate a whole different system >> shushing into a altar. >> Totally. So we can get iOS simulator in there. We can What else could we have? We could have um >> This may be the greatest thing I've ever seen in my life. Me too. >> Oh yeah. Well, fair enough. All right. So, uh what have we got? Oh, it's difficult to see on this screen size, but yes, we got a fully functional version. >> Right. And I love that it uses the the appropriate Windows CE buttons that you are likely to see in an iPhone. Yeah, it's very very legitimate. So, okay. So, did he write this from scratch or did he

**[8:07](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=487s)** vibing vibes? >> My mind is blown by this. >> I know. I told you it'd be fun. >> You have questions. Please, you have three minutes. >> Define hallucination. >> I'm sorry. I hope >> define hallucination. You call this a hallucinated operating system, right? It's hallucinating everything. >> Are there sound people able to make the sound come this way? >> Louder. Can you hear this? Not really. >> Um he says you're define hallucination for you. >> Define hallucination. Okay. So um basically all right let me show you the code. Right. So behind the scenes um what we've got is inside our editor. Right. So what's happening here I went through a different a few different ways to try and do this. First way I tried to do it was by just generating raw bitmap images

**[8:56](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=536s)** using like stable diffusion that kind of approach. And it was sort of able to produce images of the desktop operating system, but it was rubbish because it took ages. And when you click on it, all you can say is like the user has clicked at these coordinates and it doesn't really know how to update things. So then I switched over to generating a structured representation of a UI. I tried a few different versions of it. I made a custom DSL. I tried this thing called cute, which is a native um UI thing, and I could generate a DSL for that, but it didn't do a very good job. The thing that really suddenly was able to do a great job was when I switched it to just b plain HTML because you know these models have seen so much HTML they can make that up very very easily. So what we're doing here is every one of these windows is a separate iframe and when it pops open each one of them

**[9:44](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=584s)** creates a separate copilot session within copilot SDK and it gives it instructions like this. So it's saying you're simulating this application UI. I want you to produce some HTML that represents it. And it advises the model to put IDs inside all of the elements. And then whenever the user clicks anything, all we do is we send a message back to the AI saying the user has clicked the element with ID R1 or whatever. Now produce a diff that I can apply to the HTML. And so then the model produces the diff. We apply it and the UI updates. And you get this kind of like fake statefulness because it's all happening within one copilot session there. So yeah, see the irony here and this is where Steve is very clever is that he is using his AI augmented software engineering abilities and

**[10:32](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=632s)** skills to create slop and that's the genius. >> It's it's brilliant. >> It's absolutely brilliant. >> Brilliant. Intent. >> I love it. I am >> intentional slop. >> Intentional slop. But only one that an AI engineer could possibly do. >> Yeah. >> Do you think you could have done this? >> Do I think what >> how long do you think this would take you to do? Yeah. >> So, this vibe coded thing. Yeah. >> How long would it have taken? >> Yeah. >> A minute. It's a while. This is a This is >> a few hours. >> Couple hours. How long did this take you sir? >> It took a few evenings. So, yeah. I had a I played with a few different approaches. >> Yeah. So, total total time, you think? And you were probably multitasking while you did it. >> Yeah. Total time maybe five, six hours or something. >> Five, six hours. >> I would say this is two notches past vibes heading towards AI augmented

**[11:19](https://www.youtube.com/watch?v=zh6fMtL_cSM&t=679s)** software engineering. >> I agree. Yeah. >> All right. Fantastic. Are we going to give you an award? >> We brought you an award. I'm going to get up and we're bringing you this award. >> Thank you so much. >> Congratulations. That was some amazing vibes. We are going to go to our sponsors right now, but shout out to Steve Sanderson for an amazing opener. Wasn't that cool? >> That was big hand for Steve, everybody. >> All right, we'll head out to our sponsors and we'll be right back.
