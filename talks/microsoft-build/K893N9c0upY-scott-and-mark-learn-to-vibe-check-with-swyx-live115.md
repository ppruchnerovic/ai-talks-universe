---
id: K893N9c0upY
title: "Scott and Mark learn to Vibe Check with Swyx | LIVE115"
slug: scott-and-mark-learn-to-vibe-check-with-swyx-live115
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor events"
edition: "Build 2026"
year: 2026
speakers: ["Scott Hanselman"]
channel: "Microsoft Developer"
duration_min: 12
published_at: 2026-06-05T15:38:29Z
video_id: K893N9c0upY
url: https://www.youtube.com/watch?v=K893N9c0upY
youtube_url: https://www.youtube.com/watch?v=K893N9c0upY
tags: ["LIVE115", "LIVE115_v1", "Scott Hanselman", "Scott and Mark learn to Vibe Check with Swyx | LIVE115", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026", "swyx (Shawn Wang)"]
topics: []
transcript: true
---

# Scott and Mark learn to Vibe Check with Swyx | LIVE115

**Scott Hanselman**

`Microsoft Build` · `Build 2026` · `2026` · `12 min`

`#LIVE115` `#LIVE115_v1` `#Scott Hanselman` `#Scott and Mark learn to Vibe Check with Swyx | LIVE115` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026` `#swyx (Shawn Wang)`

[Watch the recording](https://www.youtube.com/watch?v=K893N9c0upY) · [Conference site](https://build.microsoft.com/)

## Description

AI can turn an idea into a working demo faster than ever. But can that demo survive two experts who have seen every trick in the book? In this live Build showcase, developers present AI-assisted apps, agents, tools, and workflows to Mark Russinovich and Scott Hanselman. Mark and Scott will ask how it works, where the seams are, what the AI actually built, and whether the result is clever prototype, production-ready software, or something unexpectedly magical. Come for the demos. Stay for the technical reveal.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Scott Hanselman
* swyx (Shawn Wang)

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE115 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Introduction at Microsoft Build with Scott and Mark
00:00:31 - Swix greets Scott, Mark, and audience – begins presentation
00:01:11 - Conference organization context – managing a large engineering event
00:03:54 - Embedding AI agent inside web and communication platforms
00:07:17 - Description of development time and tweaks: around 1.5 weeks
00:09:09 - Reflection on trade-offs when building internal tools vs generalizable products
00:10:47 - Question about AI-generated vs. human-written code
00:10:54 - Explanation of 'vibe coding' approach using Gemini with minimal manual coding
00:11:25 - Parallelization of agents and maintaining code structure before session closes

## Transcript

*2,489 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=K893N9c0upY&t=0s)** We are back at Scott and Mark learn to vibe check at Microsoft build on the big stage. Right now, we have seen a vibe coded OS written by Steve Sanderson. We've seen a cursed CSS SQLite database written by Cassidy Williams. And now we have Swyx, Shawn also known as Swyx, who is very well known for his AI engineer world's fair, a great AI engineer. We're expecting big things from Swyx here to see if he can pull ahead of Steve and Cassidy. What do you have for us, sir? >> Hey Scott. Hey Mark. Hey everyone. I always wanted to do one of these like, you know, like hello sharks. Like what if there was an app on the market you know anyway I don't have anything as fun. I actually I brought a app that I'm working on for work. Literally internal app. You're seeing it

**[0:48](https://www.youtube.com/watch?v=K893N9c0upY&t=48s)** for the first time. I'm a little bit scared to show my own sort of dirty laundry, but hopefully I've cleaned it up and I I've I demoed it just now and it kind of works. >> So this is a real app. This is part of >> Real working app for my team. And we yeah, we are we are actually using it. So I'm responsible for all the issues. That's That's why I have to be very careful. So what's on screen I you can see what's on screen. I run a large engineering conference in San Francisco. This This is a example of last year's page with 3,000 people and tons of speakers and tons of sponsors. And I I thought it might be relevant because we're at a conference like just to see how you think about the logistics of organizing something like this. For us, we have 10 parallel tracks and so we have all these presentations of like, well, here's here's where all the

**[1:37](https://www.youtube.com/watch?v=K893N9c0upY&t=97s)** the the sort of events and the content going on that you guys might want to sign up for. But I don't really like the presentation. This is using an external vendor and it just kind of is ugly and like not customizable. For my most recent Europe conference, I actually ripped out the front end layer and started presenting the the front end of this app, which is much more pretty, hopefully, Um that you can see here. But, the back end was still very much on a SaaS software that we pay for and like don't really like. So, for this year, we're organizing a much larger conference, so 6,000 people with a lot more speakers and sponsors and what have you. It's just doubling every single year. So, I ended up making my own scheduling app, and this is the AIE bot is what what do we call it? So, we have all

**[2:26](https://www.youtube.com/watch?v=K893N9c0upY&t=146s)** these It's basically sort of a bin packing problem where we have all these open slots. We have all these session days. This is a clean data set, so you're not seeing anything proprietary right now. Um and we have to slot people in days. And there's It's a very high precision task because basically, if we get it wrong, people are going to show up in the wrong day, people are going to be upset, sponsors and speakers and attendees. We have to sort of coordinate all of them to be to be exactly a fit. So, One thing I One thing I really emphasized was I'm just going to try to demo it, I guess. Let's say put Scott Hanselman. God. Scott Hanselman into the memory track. Um

**[3:13](https://www.youtube.com/watch?v=K893N9c0upY&t=193s)** And I really like the idea of like an agentic sort of content editor, like a content CMS thing. And so, it's going to give minimal detail, but post uh propose changes. And I really like this idea of like precision that you know, that's that's exactly the the track that I intended. There's a I really like this idea of precision in agents cuz agents can't hallucinate, but if you have humans in the loop, I think it's really like the nice mix of UX and precision. So, this is something I've been working on. I'm I'm going to put I'm going to put a more open-ended question, but I'm you know, I I AIE bot is just kind of like a agent embedded inside of a web app that you can make and I think that's cool. But what's even cooler is if it lives within the communication platforms that I already have. So

**[4:01](https://www.youtube.com/watch?v=K893N9c0upY&t=241s)** I'm going to go over here where I've hopefully cleared all my data and say AI bot add Mark Russinovich. I don't know how to spell your last name. I'm so sorry. >> No, [laughter] that's right. Good job. >> to an appropriate track. And it's going to use LLM's. It's going to use web search. It's going to read from my existing Slack. And to me that's how I work with my team, right? Like we have so much coordination flying back and forth that I really want to say like okay um you know, he he they the bot's already looked him up. It's going to find like obviously he's he's a Microsoft SVP. So I'm going to put him in in that track. I can approve or reject or modify it from there. And I think for me the last thing is like I really want agents in every single surface I operate including email. So I'm going to approve this and go on over there. I'm going to put my

**[4:48](https://www.youtube.com/watch?v=K893N9c0upY&t=288s)** friend Cassidy um uh Hey, so you were doing Slack. >> We're doing it in the main application. Now you're doing it via email. It's everywhere that you want to be. >> Everywhere, right? But because I want like your agent should be omnipresent. It should just be able I they should be able to text it. I just haven't set up the iMessage integrations. But like I'll put Cassidy and see if they understand what her full name is. >> Do of course is her social media name. >> Yeah. >> [laughter] >> And I don't know. Let's let's call it the generative media track. And that's going to go over to here and show up. So I think a fundamental principle I really like to see is just logging and verification across apps.

**[5:38](https://www.youtube.com/watch?v=K893N9c0upY&t=338s)** It's it's going to take a little while but I I sent that email. And it's going to reply to me with a confirmation of what it thinks and what it's about to do. I can't really I I I can I can reply and confirm it here or I can also see that email I just sent about Cassidy and it's going to give me the option to reply once it's once it's figured out where to put her. >> One of the things that I think is worth pointing out is that you're using a mini model here. You're not like we don't need to use big models frontier models for everything. You're using a mini model. >> Yeah. Yeah. Yeah. I want it to be fast to be cheap. I can choose to upgrade the model if I want to. I just haven't done so. But yeah, we I have a model selector thing. >> So what's the harness or platform that you built this agent on top of? >> The the the the hosting platform the cloud platform. This is a Cloudflare

**[6:25](https://www.youtube.com/watch?v=K893N9c0upY&t=385s)** app. So I like Cloudflare at least for this vibe coding stuff because it can host the website which is this is I mean >> And then do you have an agentic harness are you using Pi or Copilot SDK? What's your What's your loop? What's your agentic harness? >> There's no harness. It's custom coded. It's it's a it's a while loop for LLMs. You don't really need anything more than that. >> Did you vibe code the while loop? >> Did I what? >> Vibe code the while loop around the LLM? >> I mean I don't think you have to. You can just like do a loop and like I like to set minimal turns. I really think that full unbounded autonomy is a bad idea and so I like to have that degree of control. So no I I I don't think I would trust an LLM to vibe code the while loop. >> This is a really good looking app. Like this is very clever. I can see your

**[7:13](https://www.youtube.com/watch?v=K893N9c0upY&t=433s)** face. Like you're like >> Yeah. >> This is cool. >> And I'm thinking that So how long I'm guessing you spent a lot of time tweaking and tuning this thing. >> Yeah. And and I'm busy running my own my running the main show while I'm building software for the for the show. It took about a week and a half I would say. I just going back and forth. >> work out well? >> Really you know I I think what this is it works out so this is you're seeing like the grid view is what I call it days and tracks and all these. I also have the flat list which is really good for reconciling on a spreadsheet. Um also have the raw data where I can sort of look into the exact tables that I have in uh the the sort of D1 database that I have. Um and I have an audit log with rollback uh in case I make a mistake. I can roll back uh what I what I wanted uh what I want to do. So, um this is one of those things where like I just need a

**[8:00](https://www.youtube.com/watch?v=K893N9c0upY&t=480s)** ton of precision just in case I screw something up because um you don't want to mess up the locations and assignments of 500 people. >> So, it's interesting because you decided to create a custom version of a scheduler instead of, you know, moved away from the SaaS product that you were using before. How specialized is this to your needs versus something that other people would also find useful? And then what's the trade-off in cost of something that's not so bespoke versus your cost of implementing this and maintaining it? >> Yeah. Um so, the the there there are publicly like private equity owned versions of this app. Um they cost up to $200,000 a year. Um and uh we're starting this doesn't do all that functionality, but it does what

**[8:47](https://www.youtube.com/watch?v=K893N9c0upY&t=527s)** we need and it's very custom to us. Like it only knows the track days of uh June 29th, June 30th, July 1st, and July 2nd because that's all I need needed to do. Uh so, no it's not meant for other people. I could generalize it, but why would I, right? Like that's that's just time spent on things that it's not a business I want to be in, but it's just a productivity thing for my team. >> That's a tough thing. You make a product for yourself, for your company. It is perfect for you. Is it perfect for n plus one? Because I'm looking at this and I'm like, "Oh, Sessionize and all these folks, they should they should buy this from you." But you're like, "No, it's fine. It's just for me." You just made it for yourself. >> Yeah. Ses- Sessionize is is uh one of the industry standards, but they don't have a lot of the the things that that I would want uh to upgrade to to like a Cvent or an Excel for.

**[9:35](https://www.youtube.com/watch?v=K893N9c0upY&t=575s)** >> And I could imagine add add talk add voice to this. Yeah. just go for a walk and talk to the agent and it makes the moves. >> I happen to have an opinion that I think people adding voice into their apps are doing like the locally optimal thing, but it's not globally optimal. Globally optimal is your voice should be tied to your OS kind of. >> Yes. >> So that you have one hot key. You don't have to learn like five different hot keys. Right now if I press command K versus command P, I have like three different apps all trying to be my voice layer, but that's like really messy and like it's not going to really have the memory of like what I want to say not not learn on my my my patterns. So I actually have this like I do I do like having that separation of voice versus the rest of the >> It's like you using window key T. >> Yeah, I use Windows H. >> Or Windows key H, yeah. >> Yeah, but I agree that too many people

**[10:22](https://www.youtube.com/watch?v=K893N9c0upY&t=622s)** are wasting time adding voice into their agent apps. The OS should handle that. It should be available for that. Last question as we get towards the end here. Is this on GitHub and you use GitHub actions? How does it deploy? Very briefly, how do you deploy the app? >> Yeah, Cloudflare has a sort of Wrangler CLI that can that can push everything including migrations of a database. And it's all done in GitHub actions of course. >> I got one one more question. How much of the code did you write versus AI write? >> Is this like the the sort of reveal moment? >> Yep. >> Yeah, it's entirely by Gemini. >> What? >> It's entirely by code. I I yeah, I was forced to lie about the the loop thing. Even that was done by Gemini. >> Did you review the code at least or did you just play test it? >> I just I just tested it and gave it feedback. So if you can see all the all the feedback that I have in

**[11:08](https://www.youtube.com/watch?v=K893N9c0upY&t=668s)** cursor, I had to hide this window where this is the entire history of all the by coding that we've that we've been doing. >> You never looked at the code or really worried about the code. >> No, I don't know where >> [laughter] >> where it is. >> It's fine. >> I will say I do I do care a lot about parallelism of agents. And so if you let an agent just run, it's going to do one monster file of like thousands and thousands of lines. And and where I draw the line. I I have some skills where uh it'll keep the the code maintainable, but also uh parallelizable. So, I can have like five different agents running on it at the same time. >> Entirely vibe coded. Absolutely fantastic. >> Thank you so much. >> Big applause. >> Thank you. >> Best vibes. >> Thank you. >> [applause] >> We're going to go to our sponsors. We'll be right back. We got one more.
