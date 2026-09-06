---
id: ekOTT0siHSo
title: "Making AI Personal: Building Context-Rich AI Tools with MCP • Kris Jenkins • GOTO 2025"
slug: making-ai-personal-building-context-rich-ai-tools-with-mcp
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Kris Jenkins"]
channel: "GOTO Conferences"
duration_min: 25
published_at: 2026-05-29T12:00:39Z
video_id: ekOTT0siHSo
url: https://www.youtube.com/watch?v=ekOTT0siHSo
youtube_url: https://www.youtube.com/watch?v=ekOTT0siHSo
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTOcph", "GOTO Copenhagen", "Kris Jenkins", "MCP", "Personal AI", "AI", "Context-Rich AI", "Context-Rich AI Tools", "Agentic AI", "LLM"]
topics: ["Agents & orchestration"]
transcript: true
---

# Making AI Personal: Building Context-Rich AI Tools with MCP • Kris Jenkins • GOTO 2025

**Kris Jenkins**

`GOTO Conferences` · `GOTO` · `2026` · `25 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTOcph` `#GOTO Copenhagen` `#Kris Jenkins` `#MCP` `#Personal AI` `#AI` `#Context-Rich AI` `#Context-Rich AI Tools` `#Agentic AI` `#LLM`

[Watch the recording](https://www.youtube.com/watch?v=ekOTT0siHSo) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Copenhagen 2025. #GOTOcon #GOTOcph

Kris Jenkins - Lifelong Computer Geek and Podcast Host @krisajenkins

RESOURCES

ABSTRACT
We all have important questions about the data around us: "What should I work on this week?", "How's my side project doing?", "Is anyone waiting on me to email them?" These are perfect questions from a human perspective - natural language queries that get to the heart of what we actually want to know. But until recently, automating these kinds of questions was impossible. They're too ambiguous, they need domain-specific knowledge and external tools to even begin to form an answer. MCP changes that.

By building a simple server for your personal questions, you can literally ask "What issues should I look at?" and get sensible, accurate answers. Spend a couple of hours building your own oracle, and instead of combing through Jira manually, you could be making coffee while a machine does the research for you. In this talk, we'll dive into the Model Context Protocol (MCP) - a surprisingly simple JSON-RPC mechanism that gives AI tools focused access to your data.

You'll learn how to wrap existing functions or external APIs as MCP endpoints, turning any data source into something AI can query on your behalf. We'll walk through real examples of building agentic access to databases and REST APIs, discuss security considerations, and show the easiest way to build your personal MCP server from scratch.

By the end, you'll have everything needed to build a personalised MCP server. You'll understand the protocol, see practical implementation patterns, and leave with ideas for automating your workload. Whatever data you have, you'll be able to create AI tools that understand your context and answer the questions that actually matter to you. [...]

TIMECODES
00:00 Intro
02:02 What is agentic AI?
04:57 Demo: Let's ask a question
07:30 How did that work?
09:07 How to build an MCP server
12:37 The delegated-coding approach
16:16 Testing tip
16:55 Demo
19:22 Examples
24:11 Outro

Read the full abstract here:

RECOMMENDED BOOKS
Sandy Maguire • Thinking with Types • https://leanpub.com/thinking-with-types
Edwin Brady • Type-Driven Development with Idris • https://amzn.to/432GZTi
Maryann Kisamore • Basics Of Apache Kafka • https://amzn.to/3tkVYFD
Mitch Seymour • Mastering Kafka Streams and ksqlDB • https://amzn.to/3HZ18wK
Ted Dunning & Ellen Friedman • Streaming Architecture • https://amzn.to/3lhk3Kb
Liz Rice • Container Security • https://amzn.to/3oU4iJe
Neal Ford • Functional Thinking • https://amzn.to/3DdP35B
Petricek & Skeet • Real-World Functional Programming • https://amzn.to/38diF4M

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,126 words · source: supa (en, exact timings)*

**[0:11](https://www.youtube.com/watch?v=ekOTT0siHSo&t=11s)** [applause] Thank you very much. Thank you. Okay, so I realize I'm making a terrible mistake because it's 2025. I'm going to give you a talk about AI and I have nothing to sell you. >> [applause] >> Uh, I don't want to talk about AI being the next generation transformative enterprise deployment system that will revolutionize your business, fire all your workers, and then hire cheaper ones. Uh, I don't even want to tell you about the f the distant future of AI and how it's going to change how we work and how we'll get 15our work weeks and then we'll wonder what to do and we'll go back to work. I want to talk small. I want to go down instead of up. And I want to talk the very near future because what I'm hoping is that if I do

**[0:59](https://www.youtube.com/watch?v=ekOTT0siHSo&t=59s)** my job well in this talk, some perhaps many of you will spend the weekend hacking on something for the distant future of Monday morning and make your life better thereafter. How do we do this with AI? I think I can explain for those who are like feel ambiguous about the term and have just heard the marketing. I can explain what agentic AI is and give you a clue how to make the most of it by telling you that I have a teenage son. And I don't know those of you who've had a teenage son or currently have one, but it is every bit the exquisite communication experience that you've been led to believe. [laughter] Some people laughing deepest are the

**[1:47](https://www.youtube.com/watch?v=ekOTT0siHSo&t=107s)** ones that have been through that and now the child has gone away and they're past it. Right? My teenage son, love him. He's still learning to be a great communicator. He came up to me the other day and he said, and I swear these are his exact words. He turned to me and he said, "Did you order the thing? Did I order the Did I [laughter] Did I I don't remember ordering the thing. [gasps] Did I order the thing? Now, you being a reasonable person, you would think the right thing to do is to turn to the teenage son and say, "What thing, son?" Free parenting tip. That's a trap. It's a It's a terrible mistake. Never do it. Never answer a question with a question. Especially with teenagers, they'll treat you like you're

**[2:34](https://www.youtube.com/watch?v=ekOTT0siHSo&t=154s)** an idiot. Grown-ups. Okay. So, I have to do better. I have to do better than that. Did I order the thing? I'm an intelligent man, but I'm not a psychic. But okay, did I order the thing? There's a place I go when I order things and immediately forget about them. Boring things that I'm required to buy for my life, right? It's called Amazon. So, I reach into my pocket and I pull out my phone and I um look up a list of open orders, right? And there's the usual boring I'm a grown-up stuff like dishwasher salt stuff I don't that I need but I don't care about. And I look down the list and sure enough there is a cyberpunk themed headphone case. That's

**[3:23](https://www.youtube.com/watch?v=ekOTT0siHSo&t=203s)** cool but not quite my aesthetic. Right. And I So I turn to my son and I say, "If you mean the headphone case, yes, I ordered it and it's coming on Thursday." And he said, "This is magical." He said, "Thanks Dad." [laughter] Yeah, you know about this, right? Being thanked by a teenage son is a real miracle to be treasured. If you look at this diagram, and we're going to change some of the nouns, this is a gentic AI, right? What you do is you have a user that asks an open-ended question. Maybe not quite as ambiguous as my teenage son's question, but open. And you have an LLM, which is intelligent, but it's not psychic,

**[4:11](https://www.youtube.com/watch?v=ekOTT0siHSo&t=251s)** right? You give it a bunch of tools that it could invoke and get extra information back to enhance its context, and you might just get a satisfactory answer. If you put a box around the bit on the right, you have a gentic AI. That's what it is. It's the LLM plus tools. Maybe you know this. The key things are who defines the tools that the LLM has access to. We do. Programmers like us. Who decides when it's time to invoke a tool? The LLM does. And that's what makes it agentic. So, open-ended questions. Thinking like a teenager. Should we have a little code demo?

**[4:59](https://www.youtube.com/watch?v=ekOTT0siHSo&t=299s)** Just a little one. Let me find my terminal and pull up Claude. That's the one I've been using. I'm not quite as potentially rude as a teenage boy. I'm not quite as polite as Sam Aaron if you watch that. So, I have a question and it's my question. It's the question I genuinely care about. How's my latest episode doing? Right. Said in the introduction. Ah, okay. Sorry. Thank you. Um, let's Why don't we Sorry. Let's stick that over there. And no, let's stick that over there and go to that. There we go. You see that? Right. Okay. How's my latest episode doing? This is a terrible question. Any

**[5:49](https://www.youtube.com/watch?v=ekOTT0siHSo&t=349s)** computer scientist can tell you this is a terrible question because it's super ambiguous, right? How's my latest episode of What doing? And even if you can answer that question, how's it doing? There's a play button. If you click it, it plays. It's doing just fine, mate. Right. How is my latest episode doing? This is a terrible question, but it's the question I actually care about. all the steps that go from figuring out resolving the ambiguities in that question and realizing there's certain data I need to collect and I need to go away to the internet and find a tool that can fetch that data for me and then getting the results and compiling them down and turning them into a meaningful summary so that I can answer that question. All that stuff is busy work. The question I actually care about and the answer I

**[6:39](https://www.youtube.com/watch?v=ekOTT0siHSo&t=399s)** want is the only thing that matters. And we live in this magical age where all the stuff in the middle can potentially be automated away. And I think that's great. How's my latest episode doing? It's got about 1,400 views. Little bit lower. I knew it would be um because the more abstract topics never perform quite as well, but it has a 3.2 like to view ratio, and that's actually pretty good for a tech long form podcast channel. My latest episode's doing fine. I can relax until next week. Right. That's how I want these things to look. I want to be able to ask unreasonable questions and get answers without any work. And I want you to be able to do that. I want to try and get you doing this when you get to the weekend. So, let's dig into the technical

**[7:27](https://www.youtube.com/watch?v=ekOTT0siHSo&t=447s)** details. How did that work? Right? How did that work? Okay. So, when I ask a question like, "How's my latest episode doing?" Think about this. you you stop someone randomly in the street who's willing to help, right? And you say, "How's my latest episode doing?" Of course, they're going to look at you like you're from another planet. But if you were to say, "You can get my YouTube video playlist if you do this, and you can get the view counts for a specific episode by doing this. How's my latest episode doing?" A lot of the ambiguities are immediately resolved. you've got some idea of an intelligent guess of how you might answer that terrible question, right? So,

**[8:14](https://www.youtube.com/watch?v=ekOTT0siHSo&t=494s)** how do we do that to an LLM? Because it would be able to grab that information for us if we could just provide it with that context. And the answer to that is a term you're hearing all the time at the moment, model context, protocol. Right? It lets you define those tools. Almost more importantly or more of a headline I think is it lets you give the context to when those tools are invoked and I'm going to go into that in more detail detail in a bit in a minute and then it lets the LLM give itself more context to answer your question. So you can end up with really rich data conversations like this where you ask unreasonable questions and get reasonable answers. So I don't want to sell you one. I want you to build one. I really do. I really would like I'd love it if everyone was

**[9:02](https://www.youtube.com/watch?v=ekOTT0siHSo&t=542s)** building one over the weekend. I would be quite happy if plenty of people are. So, how do you build your own MCP server? How do you hack it for yourself? Super easy. MP M Did I say MPC? That's a synthesizer. Sorry, mixing my two lives. MCP, it's just JSON RPC in a trench coat. That's all it is, right? is wrap some stuff up in JSON and call functions. If you want to make your own to get started, all you need are three messages. Hello, here are some functions. Call a function, right? It's all you need. Let me give you some implementation advice for doing this. Right? Super easy. I would think nearly everyone in this room, I don't want to gatekeep, but nearly everyone in this room can happily create a process that

**[9:51](https://www.youtube.com/watch?v=ekOTT0siHSo&t=591s)** reads JSON on standard in, spits JSON out on standard out. Right? That's part one. Then you find some existing or you write some data fetching functions. As programmers, you know, most of us can do that quite happily, I would think. And then your goal is to turn those function signatures into JSON messages. This is the only hard part of building your own. And the thing that makes that much much easier is choose a language with reflection, right? Uh you can do runtime reflection like oh someone [laughter] someone in the audience is going never choose a lang yes choose a language with reflection for this project because what you want to be able to do is read the

**[10:37](https://www.youtube.com/watch?v=ekOTT0siHSo&t=637s)** function signatures either at runtime or compile time pull them out and turn them into data. So you can do that with like macros or uh runtime reflection or uh comp time in Zigg. That's a fun way to do it. And then you just need to implement these three messages. Show you some code, right? JSON RPC. It can be a sophisticated protocol, but if you just want to hack it together this weekend, you need a bit of boiler plate and you end up with something that looks roughly like this. I'm going to simplify the boiler plate out and say need a method. You're going to expect the method initialize and you're going to respond with you could almost hardcode this one who you are and what version of the spec you're working with, right? You need a message that says what's

**[11:27](https://www.youtube.com/watch?v=ekOTT0siHSo&t=687s)** available. Someone's going to send you on standard in list your tools and you're going to spit out a list of functions that could be called. And this is the only hard part of this project I think which is how do you turn a function signature into JSON? reflection is the answer and you just describe how it can call the function and then finally unsurprisingly it needs to be able to say okay I'm ready to call a tool you're going to get the arguments in the function name and you have to invoke it and submit either text back or structured data and you probably want to go with structured data if you can because that in itself gives more context which is great right So, should I give you another demo or shall I? Let's be

**[12:16](https://www.youtube.com/watch?v=ekOTT0siHSo&t=736s)** realistic. Okay, so if I want people to write this and we're talking about AI, some people are going to go and write this and that's great. Some people will go and try and vibe code it and that's great, too. And maybe that's the right way to do this this day these days. Maybe the days of us handwriting every line of code are gone. So, let me give you some vibe coding um thoughts on how you could vibe code this pretty quickly. I've done this in about four or five languages. So I think I know how to tell you how to prompt this. And I will say I don't like the term vibe coding. I think we should be talking about delegated code. I think we should be talking about delegated coding. Right? Vibe. Let me tell you the difference. Vibe coding. You go to the magic LLM oracle and you say please I supplicate you to bring me enterprise products that I can sell

**[13:04](https://www.youtube.com/watch?v=ekOTT0siHSo&t=784s)** tomorrow and retire. That's vibe coding. Delegated coding is you are a smart and enthusiastic intern, but you are a green as it comes. So, I will give you a very clear spec of what I want you to do, and when you come back to me, I'm going to tell you exactly what I like and exactly what's wrong, and you're going to go away and fix it because you are cheap, intelligent, enthusiastic labor, which is the way it should work and it works a lot better. So, how would you get an enthusiastic naive intern to do this properly? You would say, "Look, first go and read the MCP spec, right? You should literally put this in the prompt." I've been told early on in my career to go and read a spec and haven't. You've done this, right? You don't actually read the spec.

**[13:53](https://www.youtube.com/watch?v=ekOTT0siHSo&t=833s)** You skim it and then when you get stuck, you read the page that actually matters. But an LLM will actually go and read it properly, which is brilliant, right? So tell it to go and do it. Then you say implement an MCP server in your chosen language. I ended up with Rust because I wanted a single binary. I wanted uh compile time reflection and I'm just on a bit of a Rust kick at the moment. So it's fun. Tell it to use the standard IO protocol. This is not the protocol you will use to release your enterprise network ready MCP tool, but this is the easy one to get started on your laptop for Monday morning. So, this is the one you should do. It's much much easier. You can do it in a couple of hours over the weekend tops. It should be able to present a list of functions I specify as MCP tools. And

**[14:42](https://www.youtube.com/watch?v=ekOTT0siHSo&t=882s)** then I think this is actually the most important part of the prompt. You need to think, how do I want this to look as a programmer once it's ready to go? Here's an example of what my functions should look like when we're done. And in Rust, I do this. So, I want to have just a regular old function, and I want to annotate it with just MCP tool. That's what I want. That's what I I want to be able to just say, please magically turn this function into an MCP function. That's a nice developer experience for me. So, it's what I demand. The most important part about this counterintuitively is the descriptions because we're used to we're used to documentation being maybe not so important, maybe an afterthought. Maybe you document your functions, maybe you

**[15:30](https://www.youtube.com/watch?v=ekOTT0siHSo&t=930s)** don't bother and sometimes you document them badly and doesn't really matter. This is the first time documentation is actually important to getting good results because it's these descriptive strings which end up in the um JSON RPC message which is how the LLM will know these tools are worth invoking in this context. So that's really important. You might have a look at uh if you're a Java programmer, you might have a look at Spring AI. I think they've got the interface for doing this really really neat. Maybe if you're a Java programmer, you won't write your own. I hope you do anyway. It's kind of fun. But uh yeah, Spring Boot just very simple way to annotate functions and you're just off and running. I will give you a quick testing tip for

**[16:20](https://www.youtube.com/watch?v=ekOTT0siHSo&t=980s)** this. Um, you want to have a look at the model context protocol inspector, which is a really nice tool for looking at your the standard in, standard out function you've written, calling it, and inspecting and figuring out where it's going wrong if it doesn't work first time, which it may not. Um so that's really all you need to do. You can build your own one. Super easy. Shall I give you some demos? I'll give you some demos. So, uh, good. That's still working. Let's get the Let's clear this out. So, is that going to work? No.

**[17:10](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1030s)** Why is that not working? Have you not captured my keyboard? Come on. Oh, I know why. Yeah, I'm getting too clever. I'm running um Claude inside Vim and I was in uh normal mode instead of insert mode. Okay. Right. So, um the first thing I would suggest you want to do is how long has my laptop been running? Let's see what this says. So, this is just going to call um the uptime command. Standard Linux uptime command. uh 9 days 2 hours 57 minutes sounds about right since the last time I rebooted the OS. The reason you want to start with uptime is uh it's a simple end toend test. If you can get MCP

**[18:00](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1080s)** server calling that you are away. Um I'll give you some more ideas but let me give you a more sophisticated demo. So um I'm not going to show you my email one. I don't want to do that. Um something I've been doing a lot lately. How about this? Uh, this is a great ambiguous question. What did I work on last month? What did I work on last month? Who can't remember what they worked on last week? Let's have a look. This is going to go off and I'll tell you how this works, but it's a question I often wonder. What was I working on? Uh, tokens, tokens, tokens. This is going to be every live demo going forwards in the future years. I worked on some events, some professional development. I've been doing ESP32

**[18:50](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1130s)** development because I wanted I wanted to build a thing where I can track my kids homework and what's outstanding so they so we can put it on um a display in the living room and they can ignore it. Uh Nyx package management cashmere which is the name of my MCP server because Led Zeppelin were on the um on Spotify at the time I started building it. Reddit comment fetching. Yeah. So, I get a summary of what I've been working on, right? Let me switch back to this. Going to give you some examples. How long has my computer's been running? Great one to start with. Another one you might want to build, and I hope this is going to stimulate some ideas for what questions you might want to ask. Another one you might want to build is, is there a library for that?

**[19:38](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1178s)** Um, so you can imagine there probably are MCP servers that will search Brew right now or search Maven or whatever package manager you use. But firstly, I realized I tend to use Nyx. Any Nyx users? No. None. None at all. So I'm I'm on my own and that's why there's no built-in MCP server for running Nyx. So I built my own so I could say, is there a library for that? And then I realized actually we can do better than the MCP service other people are shipping because that's not really the question. If I were being a super unreasonable teenager, that's not the question I want to ask. Cuz when I go looking for a library, I don't just do a search and take the first result. I look at the first three to five results and I find their GitHub page and I say, "Okay, well, how many GitHub stars have they

**[20:26](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1226s)** got? How many forks? How many open issues? How long till they're when were they last committed to?" and I get that data and then I start to see which package I'm actually interested in and I can automate all that way. I can automate all that busy work and I can actually ask the question is there a good library for that based on my personal criteria of what counts as a good library. This is great. Um, who was at Sam Aaron's talk this morning? Yeah, that was good, wasn't it? You missed out if you didn't see that. That was worth getting up for. He was saying very vehemently, never give uh a gentic AI access to your email box. Sam, you're right, but I also disagree with you, right? Um because yeah, I don't want to give anthropic access to all my emails.

**[21:16](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1276s)** And I certainly don't want to give them offline access so they could be reading my emails while I'm not even while my laptop's not even open. But I'm really bad at answering emails. And it would really be terrifically helpful to have some kind of support. I would like an agent to be able to help me reply to my emails, but I don't want to give anthropic access to my inbox or I don't want to give chat GPT access to my inbox. What's the solution? Narrow the security field, right? Narrow the footprint of what it can do. make your own that can just say search your inbox for specific emails and when you call it you don't give it blanket permission to use that tool you make it stop and tell you what it's going to search for and if you're happy and it gets an ID back and then another MCP

**[22:05](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1325s)** tool can actually fetch that specific email so I can give them access to just the particular email I actually want AI to help me write with and I can constrain that footprint and I think that's really And it's not that hard as long as you can connect to the Google Gmail, which is just breadandbut JSON coding. My absolute favorite, and I'm going to leave you with this one. My absolute favorite is um have you ever been at work and you've got to do weekly status updates of what you worked on this week? Right, which is miserable. I see someone grimacing in the audience. Yeah, that's boring. I don't do that anymore. I just say, "What did I do this week?" Right? because I've set up an agent that does two things. Whenever I do something

**[22:52](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1372s)** interesting or large, I just type remember that and it knows that I mean by that there is a tool that will save important things to a duck DB database which is running on my computer. It saves them as structured facts. And at the end of the week, I just say, "What did I do this week?" And I've got it set up to spit me out a nice little bulletoint summary of the interesting, cool things I did. And I just copy and paste those into Slack and I never write another status update again. And this is great because of course I proofread it and I tweak it a bit, but I don't want to write these boring documents and my boss doesn't want me to spend half an hour scratching my head and coming up with this boring document. Personalize your AI for your life. How do you do this? I think the answer is think like a teenager.

**[23:42](https://www.youtube.com/watch?v=ekOTT0siHSo&t=1422s)** Ask unreasonable questions that you sort of magically expect the world to answer for you and then think about how how you as a programmer resolve that into data. And then you can just go and build your own. It's super easy. It's just JSON in and JSON out. Hopefully that gives you a map. I hope you go and explore and build your own. I'm a little early on time, so there's plenty of time for questions. Uh, we'll stop there. If you want to find me on my podcast, there's a QR code. Thank you. [applause]
