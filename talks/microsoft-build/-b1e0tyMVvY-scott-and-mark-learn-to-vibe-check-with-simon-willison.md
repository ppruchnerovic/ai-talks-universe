---
id: -b1e0tyMVvY
title: "Scott and Mark learn to Vibe Check with Simon Willison | LIVE113"
slug: scott-and-mark-learn-to-vibe-check-with-simon-willison
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: []
channel: "Microsoft Developer"
duration_min: 12
published_at: 2026-06-05T15:39:27Z
video_id: -b1e0tyMVvY
youtube_url: https://www.youtube.com/watch?v=-b1e0tyMVvY
tags: ["LIVE113", "LIVE113_v1", "Scott Hanselman", "Scott and Mark learn to Vibe Check with Simon Willison | LIVE113", "Simon Willison", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Scott and Mark learn to Vibe Check with Simon Willison | LIVE113

**Speaker not identified**

`Microsoft Build` · `Build 2026` · `2026` · `12 min`

`#LIVE113` `#LIVE113_v1` `#Scott Hanselman` `#Scott and Mark learn to Vibe Check with Simon Willison | LIVE113` `#Simon Willison` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=-b1e0tyMVvY) · [Conference site](https://build.microsoft.com/)

## Description

AI can turn an idea into a working demo faster than ever. But can that demo survive two experts who have seen every trick in the book? In this live Build showcase, developers present AI-assisted apps, agents, tools, and workflows to Mark Russinovich and Scott Hanselman. Mark and Scott will ask how it works, where the seams are, what the AI actually built, and whether the result is clever prototype, production-ready software, or something unexpectedly magical. Come for the demos. Stay for the technical reveal.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Scott Hanselman
* Simon Willison

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE113 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Demonstration of Data Set Agent analyzing blog data
00:03:25 - Simon is introduced, praise for Pelicans demo
00:04:30 - Explanation of plugin decorator and agent tools registration
00:05:07 - Clarification between plugins and tools, MCP comparison
00:06:50 - Using Codex Desktop and Claude Code for Quick Deployments
00:09:18 - Discussion on Typing Code vs. Prompt Engineering or Voice Input
00:09:57 - Need for intentional focus and expertise in AI-assisted coding
00:11:27 - Reflection on AI-augmented software engineering
00:11:38 - Closing remarks, lighthearted chat, and session wrap-up

## Transcript

*2,571 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=0s)** Hey friends, we are back with Mark and Scott learn to vibe check. We have had some amazing stuff from Swix, from Steve Sanderson, from Cassie Williams, and now to bring it all home is the legend himself, Simon Willison. You may have seen him occupying the top spots on Hacker News on any given Tuesday, pushing Mark and I to the bottom of the second page. Simon is a legend, you can check him out online, and today, what have you brought us, Simon? >> So, what I've got today, it's the culmination of 8 years of all of my projects finally come together. Um the first project uh is my uh I might show it on screen somewhere. >> You're already seeing your screens right now. >> Fantastic. So, I've been building this project called Datasette for like 8 years. It's a data exploration tool. Lots of interesting data exists in the

**[0:47](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=47s)** world. What can we build to help us explore it? 3 years ago, I started work on LLM, which is a command-line tool and Python library for talking to language models. It's got plugins for basically all of them. And I've been blogging for it turns out 24 years. So, I've got 24 years of stuff on my blog. So, obviously, the thing I've been building is an agent, because everyone's building agents. Like the the hello world of programming in 2026 is to build an agent. This thing is called Datasette agent. It's a plugin for Datasette, and it lets me ask questions about my data. So, let's do count of entries and quotes and link and I call them blogmarks on my blog. So, I'm kicking this off. This is using GPT-3.5 under the hood at the moment, but it'll work with any of them. It has

**[1:33](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=93s)** a bit of a think. It looks at the databases and queries that are available uh the devices and tables. Runs a bunch of queries. It goes, "Ooh, some of them are draft posts. I'll think about that." There we go. It says I've got 3,000 entries, 1,000 quotes, and I 8,000 blogmarks. I'm going to say, "Do a chart." So, Datasette agent, as with everything in Datasette, is based around plugins. One of the plugins I built is called Datasette agent charts and that can do little bar charts of things. I've got other plugins for running bits of Python code in a sandbox and there are all sorts of visualizations and things that I want to add into this in the future. I will do one more demo cuz I've got that one was GPT 5.5. This one here is the same software running against when 3.5 on my Mac in LM Studio. So, let's let's see if it does the same thing. Um count

**[2:25](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=145s)** count the entries and let's just do count count the entries in quotes. So, now this is running entirely offline. This is using Oh, that was quite quick. Very nice. Yeah, it knew the tables. It did the counting. This worked. When these models that run on a laptop are very capable of writing SQL queries and doing basic tool calls these days. >> Okay. And the tool itself, the tool here that we're watching running on localhost is speaking to it has tools available to all of the things that you have on your blog or is it How did it know which where the data came from here? >> So, it is running a copy of my blog's database. My blog is Postgres on Heroku. I export that into I built another tool called DB to SQLite that exports that SQLite. So, I've got a 100 megabyte SQLite database file on my computer

**[3:14](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=194s)** which dataset is looking at. And so, all it gets is a SQLite database and then it has to read the tables and get the database metadata and all of that kind of stuff and make that available to the agent. >> So, first Simon, I'm a huge fan. I love the pelicans on bicycle uh >> I've got a demo about that. >> Okay. But, I got a question about this. Um when you say plugins, what is what is a plugin? >> So, this is um I built everything in Python. Python is a very good language for plugins cuz it's all dynamic. You can install extra packages that become visible to each other. So, a plugin is Actually, let's pull one up. Um I'll tell you what, I'll pull one up that code wrote an hour and a half ago. This is data set agent micro python. It is live on the python package index as of 2 hours ago and this is a plugin for data set agent

**[4:03](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=243s)** that adds the ability for it to run python code in a web assembly sandbox. Because I want agents to write python code, I don't want them to delete everything on my computer. You need some kind of safe way of doing that. And if you look in the code, it is >> And this is what you were working on when I saw you in the hallway. >> Exactly, yeah. >> I can't talk to you. I'm publishing this this thing now to to python. >> This is exactly what's going on here. >> Okay. >> And there is >> a little bit bigger there for us, brother? >> Here we go. So, a plugin just has a decorator called hook and plug cuz it it implements a hook, register agent tools and it returns a list of agent tools. In this case, it's called execute micro python. It's got a function. It's got a description. Um and all of that data set itself has well over 200 plugins now. LLM's got about 40. My little agent thing has got,

**[4:51](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=291s)** I think, five in the in the wild already. Plugins are such a great way of building software in this age of AI cuz honestly, Claude code and copilot and things, they can one-shot a plugin for some quite sophisticated behavior if you give them the right kind of information to start. >> So, plugin instead of a tool. >> Well, the plugin is a bundle of tools. Like in this case, I've got one tool that's embedded in a plugin. A plugin could provide a tool. >> Not MCP, but the same idea. MCP is just a fancy wrapper around the underlying concept. >> you think this model works better? It's I mean, it's because you're working entirely in python, right? >> Exactly. Exactly. Like MCP is just tools with extra steps. >> Now, when you do this kind of work, if you recall if folks were needing to remember that he's had a blog since 2002. Like we were sending back trackbacks and pingbacks on

**[5:40](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=340s)** blogs 20 plus years ago, Simon and I. That wasn't always vibes. When did you start vibe coding? Because so you've put so much out that is bespoke code. How are you incorporating the vibe coding and then the AI augmented software engineering practices into the work that you're doing? >> So, about two and a half years ago Claude's artifacts came out and got really good at building little HTML JavaScript tools. And so I started vibe coding before anyone was calling it vibe coding where I just do little self-contained self-contained HTML apps. And I put those on tools.simonwillison.net. This is a collection of 215 of these things that I've been building up over the past couple of years. And this is great cuz it's so safe. Like you can't shoot yourself in a foot in the foot with a static HTML JavaScript thing on set domain. So, there's there's sort

**[6:29](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=389s)** of no risk in in these being mistakes. And I'm still doing this today like um I built this one yesterday. This is just a prototype of what it would look like to build an interface where you can attach files to a text area and I preview them in line like this and copy and paste things in all of that sort of stuff. I want to build this as a feature in my agent, but first I built the UI prototype and this I built this with um this one was Claude Codex where it was was um Codex desktop. Often I use Claude code on the web on my phone. So, I can fire up my phone say, "Hey, build me a prototype that does X." Click a button on my phone to push it to GitHub. It gets deployed by GitHub pages. It's live. So, I've been building little throwaway things the past couple of years. Since January most of the code that I write has been written by an agent for me cuz

**[7:18](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=438s)** that was the point when the coding agents got good enough that you can pretty much tell them the style that you like, how you like your unit tests to look, all of that kind of stuff, and they do the the sort of scut work of actually typing it into a computer for you. >> So, when you're vibe coding, do you watch the thinking trace to see if it's off the rails or >> It depends on the stakes. So, low stakes things like a little UI prototype, I don't care. The code doesn't matter. I just want to prove that the thing is possible. Something like the um the this thing right here is a sandboxing system that runs untrusted code in a sandbox within my system. That's really important. Like the stakes could not be higher. This one, I watched it like a hawk. I was paying very close attention to the code that it was writing. I then ran all sorts of tricks to try and um

**[8:05](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=485s)** like stress test it. And I actually had GPT 5.5 try and break out of the sandbox, which was quite entertaining to watch. Um found a couple of edge cases that I needed to clean up. But yeah, that's um that's the sort of other end other end of the scale from just hands-off letting it do whatever it wants to do. >> So, one of the techniques that Scott really likes is adversarial vibe coding, where you have one model pro- propose something or write something, and then I have another model go critique it, and and then have them argue. >> I've been doing that a bit. GPT 5.5 is my security blanket. I really like it for security reviews. So, until recently, I was doing most of my work on Opus 4.6, and then I'd have GPT 5.5 do a quick scan at the end to see if it missed anything. And it would often find things. To be honest though, if I'd asked Opus to scan its own work, maybe

**[8:52](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=532s)** it would have found them, too. It's just you sort of habitually feel like fit you I you get the sort of vibes of which models have certain strengths. >> Yeah, I like to have two or even three, and I make a high, medium, and low. And if all three models agree that something's a problem, then that's a high. Two would be a medium, and one would be a low. So, being able to use something like GitHub Copilot in the CLI or the app, you can pick two or three models and have them all fight, and it works great. Yeah. So, are you no longer typing code? Are you are you a typer of prose? Do you type your prompts, or are you a yapper? >> Um I'm still mostly typing prompts. If I'm walking the dog, I might dictate prompts into my phone. But even then, the prompts can be quite short. Like something I found really interesting is it used to be the harder the task, the harder you had to concentrate. The

**[9:40](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=580s)** opposite is now true because if the task is really hard, GPT-5.5 will turn away for 10 minutes and during those 10 minutes you can go and read Hacker News and you can get distracted and work on other things. There's this weird thing where the more difficult tasks are now cheaper to be distracted from than the easy ones are. >> So, this is the thing that Mark and I are struggling with and I think what we'll talk about in our close is this idea that you have to know what you're doing to be successful at vibe coding. You don't vibe into production. There's AI augmented software engineering baked into your process by virtue of how your brain works because you've been doing this for 20 plus years. Would you agree? >> I think AI has made being a professional software developer harder because it's raised expectations for what we can do and you can now take on so much more ambitious projects. It used to be we had

**[10:27](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=627s)** to stay on our lane. Like I was a back-end Python programmer with a little bit of HTML and JavaScript because I could only skill up to professional levels on one of those technologies at a time. Now, I'm right Okay, here's a fun thing. Here's a little app I wrote in Swift UI that helps see helps me see what bandwidth my computer is using and this is another one that shows me what's using my memory and what's using my GPU. I don't know Swift UI. I have no idea what I'm doing. I didn't even have to open Xcode for this thing. Claude code is like, "Hey, no Xcode needed. I'll just build this up and stick it in the menu bar for them." I would not recommend other people use use or trust this piece of software because I don't know what I'm doing, but it's been It's It's also I've been using this software for like 4 months now. I kind of trust it now. Like I've realized that the thing I care most about isn't that an

**[11:15](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=675s)** expert wrote the code. I care that a real human being has actually been using it for longer than like 2 hours and it's sort of built up that like over time that trust in the software gets built up. >> Fantastic. Well, this one feels like this one feels like AI augmented software engineering. >> I agree. >> Yeah, I agree with that. >> One closing demo. >> Very briefly, we have 30 seconds before I'm going to kick you off the stage. >> When did Simon last see a pelican? Cuz it's got all of my net wildlife sightings on my blog. >> now. >> You saw a pelican last week. >> And it says I saw a pelican on June the 2nd. That's today. And it's right because if you refresh my blog, there's a pelican there right outside diving into the water. It's super cool. >> Very, very cool stuff. Big congratulations to you, >> Thank you very much. That is Thank you. >> Thank [applause] you. Thank you very

**[12:02](https://www.youtube.com/watch?v=-b1e0tyMVvY&t=722s)** much. We appreciate you. All right. We're going to say a quick thank you to our sponsors, and we thank you all for hanging out, and then there'll be a brief ending here on Scott and Mark Learn to Dive Check.
