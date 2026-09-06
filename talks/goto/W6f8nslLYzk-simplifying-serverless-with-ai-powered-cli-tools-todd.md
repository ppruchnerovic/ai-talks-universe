---
id: W6f8nslLYzk
title: "Simplifying Serverless with AI-Powered CLI Tools • Todd Shaffer • GOTO 2025"
slug: simplifying-serverless-with-ai-powered-cli-tools-todd
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Todd Shaffer"]
channel: "GOTO Conferences"
duration_min: 20
published_at: 2026-01-05T13:01:05Z
video_id: W6f8nslLYzk
url: https://www.youtube.com/watch?v=W6f8nslLYzk
youtube_url: https://www.youtube.com/watch?v=W6f8nslLYzk
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Todd Shaffer", "GOTO Serverless Day", "AWS", "Serverless", "EDA", "GenAI", "Event-Driven Architecture", "Serverless Compute", "Lambda", "SRE", "Chaos Engineering", "CLI", "AmazonQ"]
topics: ["Agents & orchestration"]
transcript: true
---

# Simplifying Serverless with AI-Powered CLI Tools • Todd Shaffer • GOTO 2025

**Todd Shaffer**

`GOTO Conferences` · `GOTO` · `2026` · `20 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Todd Shaffer` `#GOTO Serverless Day` `#AWS` `#Serverless` `#EDA` `#GenAI` `#Event-Driven Architecture` `#Serverless Compute` `#Lambda` `#SRE` `#Chaos Engineering` `#CLI` `#AmazonQ`

[Watch the recording](https://www.youtube.com/watch?v=W6f8nslLYzk) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Todd Shaffer - Senior Developer Specialist at AWS @ToddShafferW

RESOURCES

ABSTRACT
Join the Next Gen Developer Experience team at AWS to learn how Solution Architects, SREs, and DevOps engineers are leveraging AWS's AI-powered command line interface (CLI).

In this session, we will demonstrate how to streamline serverless application management and deploy entire applications from a single prompt using intelligent CLI tooling. You'll also learn how to leverage first-party Model Context Protocol (MCP) servers and optimize your CLI setup for seamless AWS administration, rapid proof-of-concept development and deployment, and enhanced troubleshooting capabilities.

Whether you're managing complex infrastructures or seeking to simplify your AWS workflow, this session will equip you with the tools and knowledge to boost your productivity through AI-enhanced command line experiences. [...]

TIMECODES
00:00 Intro
02:29 Demo
16:10 From prototype to production
18:40 Outro

Read the full abstract here:

RECOMMENDED BOOKS
Sheen Brisals & Luke Hedger • Serverless Development on AWS • https://amzn.to/3W3Sw2f
Adam Bellemare • Building Event-Driven Microservices • https://amzn.to/3WfNKfM
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ford, Richards, Sadalage & Dehghani • Software Architecture: The Hard Parts • https://amzn.to/3v4pKQS
James Urquhart • Flow Architectures • https://amzn.to/3Tyz8cY

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*3,468 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=W6f8nslLYzk&t=12s)** Hey everybody. Uh I hope you've been enjoying the conference. I know it's just after lunch. Everybody's feeling pretty good. Um we're here in the home stretch. My name is Todd Schaefer. uh and I uh spend most of my days uh talking to customers about either how to use serverless for generative AI um how to use generative AI to make serverless easier which is what we'll be talking about today and how to run serverless at scale um I've been with Amazon for over 5 years focused entirely on serverless uh but I've been in tech for 29 years uh from the young age of 13 uh where I was responsible for introducing the entire world to the MP3 file format. at um we've seen a couple revolutions so far uh starting with like bulletin board systems and uh you know the the

**[1:00](https://www.youtube.com/watch?v=W6f8nslLYzk&t=60s)** beginning of the internet and then um client server to cloud and now we're living through this new transformation AI. Um today I want to talk about uh the intersection of these last two subjects. Um and lastly uh this is my first trip trip trip to India and Bangalore and I appreciate so much uh your incredible hospitality. So I want to start with uh with two quotes uh that live in my head rentree. Uh first one's by Milton Friedman. Uh he's a he's an economist and this was more about government but it's perfectly at home uh for a software developer advocate like Martin Fowler. Um there's nothing more permanent than something temporary that works. And the second uh technical debt are the scars of success

**[1:47](https://www.youtube.com/watch?v=W6f8nslLYzk&t=107s)** uh which is by uh an author of a book called The Thinking Machine, which is an a biography about Jensen Wang, the founder of Nvidia. And uh I put these two up here because this is just kind of the the duality of releasing real software. Um you spend a ton of time on your core components. you really craft and love and pay attention. And then also sometimes you just need to ship something because it's Friday, you're about to go on vacation and you're positive you're going to get around to fixing it and you never do and now it's one of the lynch pins of this software that's that's kind of living decades after your your departure. And so we're going to get right into demo mode. Um, if you've never been to

**[2:36](https://www.youtube.com/watch?v=W6f8nslLYzk&t=156s)** serverlessland.com, uh, let's have this be tip number one. Uh, here we're just looking for a little bit little bit of inspiration. Uh, we're just looking to kind of get the the juices flowing. And so, I'm more of a PHP guy. Uh, but this is Python and this demo will be in Python. And, uh, this is just, uh, kind of firing off an alert to Lambda whenever a file lands on S3. Now, you don't have to be a Python guru to be able to read this code and say that is not ready for production. And so what we're going to do is we're going to use some prompt engineering uh to actually turn this u pretty easy sample into something far more substantial. Um and so let's see how my transitions are working. Um so I want to kind of pick this prompt bit by bit apart and then

**[3:24](https://www.youtube.com/watch?v=W6f8nslLYzk&t=204s)** we're going to actually throw it into a tool and and let it rip. Um so the first thing to do is to uh give the AI a specific persona to embody. Um you know this is you're an AWS serverless expert and you're a guru in Python. Uh this kind of takes the entire world of LLMs and you know immediately focuses attention on these two subjects being the the impetus of why we're talking. Um and this is what will kind of give you specific advice versus generic advice. The second part of this is being very very explicit about the task structure. I want to examine first. I want to create a plan. I don't want you jumping straight into code. Like I really want to start thinking before doing. Uh if you've ever used an LLM and you just kind of threw it at a coding task and

**[4:12](https://www.youtube.com/watch?v=W6f8nslLYzk&t=252s)** you didn't ask it to do this, you'll just see kind of code flying by on the screen and you're like, what's your plan? Like you just don't kind of know what's going on. Uh third, I'm providing specific constraints and preferences. Um I want to use the well architected framework and I want to leverage power tools for Python. Uh how many people here have heard of power tools for lambda? Okay, cool. Uh second major tip of the the day. Um it's a power tools for Python is a collection of libraries for Python TypeScript Java.net. Um, and it has uh tracing, logging, metrics, uh, easy connectors for API gateway, SQS, all of these things. And so if you've been writing these by hand, if you've been writing these serverless

**[4:58](https://www.youtube.com/watch?v=W6f8nslLYzk&t=298s)** EDA apps and kind of writing your own custom loggers and metric emitters and all those kinds of things, you've been working entirely too hard. Um, so please just do a quick Google search for power tools for Lambda. Um, and finally, uh, we're throwing kind of the million-dollar thing in here. ask me any clarifying questions before beginning. So, a lot of people kind of treat LLM like a search engine. They just ask a question, accept a response. Um, I think one of the most powerful things uh in this space is to actually kind of use it to interrogate you. Um, otherwise, it's going to make assumptions, probably assumptions that you don't like. And so one of the fastest ways to make sure that it's kind of, you know, uh, on your same wavelength is to have it ask you any clarifying questions before

**[5:46](https://www.youtube.com/watch?v=W6f8nslLYzk&t=346s)** beginning. Now, this is Amazon Q, uh, CLI. Uh, let's see if this is actually rolling. There we go. Um, and so you'll see I've taken my prompt. I've dumped it in there. Uh, if you remember our our little code snippet, I've gone ahead and dumped that in there, too. And now I'm just going to go ahead and uh let that rip. And uh you'll see that it's going to ask me a few questions here. Uh you know, file characteristics, error handling and recovery, security and compliance, monitoring and alerting, integration points, all this stuff. Um I'm going to very quickly just kind of go 1 2 3 4 this this this that. And we're going to we're going to go on. Now, you see it's generating this ginormous specification. I don't need all of that. That's a little much for right now. Um, and so

**[6:36](https://www.youtube.com/watch?v=W6f8nslLYzk&t=396s)** this plan addresses all five pillars of the well architected framework. Well, specifically da da da da da, right? But for me, I'm like, hey, that looks awesome. But how about we just do an MVP upleveling this code and we'll kind of table the rest of this for later. And uh hopefully I don't have to fast forward here, but um we'll hit that. And then what we're going to get back is a very paired down uh MVP kind of specification. So here we've just got six seven items. I'm going to ask it to actually go through and just address the first four. So replacing basic logging with power tools, adding power tools, tracing of metrics, improving the error handling, and adding input validation. And so uh what we're going to do is

**[7:24](https://www.youtube.com/watch?v=W6f8nslLYzk&t=444s)** write this to a markdown file. uh for those that haven't used LLM extensively, markdown is kind of the the preferred format for all of these types of of kind of spec driven design uh flows. And um so what I'm going to do is I'm going to have a file with a bunch of empty checkboxes. And then I'm going to actually have this drive through and check off each item by item as we're going through. The reason that I'm doing this is that when you focus their attention and you have them do small chunks of work, they don't kind of go off the rails creating 10,000 line CRs, PRs. And so, uh, the the other reason is that sometimes you want to just make sure that you get a part of a job done and you're at a good place, you can go get coffee, anything else, and when you come back, you can kind of pick up where

**[8:12](https://www.youtube.com/watch?v=W6f8nslLYzk&t=492s)** you last left off. So, this is going to generate the first section here. So, this is section one. Um, and what we're doing is we're implementing the logging improvements. It's going to give me a second to breathe. And I'm going to say, "Yeah, let's go. Let's let it rip." And so, apologies is the very bottom of the the screen here. I'll try not to to walk in front of my own typing. [snorts] And so, this is going to now generate the first kind of the first first bit of code. Uh for me, since I don't read Python, uh I said, "Why don't we slow this down just one second? Um how about you add some useful comments in this so that I understand what's happening here? Being a PHP guy, I don't read Python. And so for me, I need a little more help to kind of coach myself as I learn Python. So, we're going to just iterate

**[9:01](https://www.youtube.com/watch?v=W6f8nslLYzk&t=541s)** here. Um being vocally self-critical, um I could have put this up front. I didn't. But, you know, it don't don't let perfect get in the the way of progress on these things. And so, now we're just hitting yes or trust. And you see that we're writing lambda function v1. So, we had our tiny little code snippet and now we have v1. And now I'm going to iterate. We're picking up the second part of that specification and we're going to publish that and then we're going to go through v3. So, we're going to go through each one of these. Um, and so if you can imagine uh kind of just having a a co-orker, an intern or anything else and saying just build this app for me. Um, it's a lot different than having this really in-depth conversation about exactly what you're expecting like the the the logging libraries you want to use and all of

**[9:47](https://www.youtube.com/watch?v=W6f8nslLYzk&t=587s)** this. And so this uh this role based prompting uh where where we're kind of building this relationship with one another, you're not just asking for help. Uh you're really activating expertise. And this is kind of where most people stop. And so they throw their code over the wall, hope for the best. Instead, you know, we're decomposing this task over this entire over this entire flow. And so now we've crossed V2. Um, now imagine kind of uh, you know, getting this this like clean markdown checklist. You hand it off to your coworker. You're coming back and you're just kind of seeing throughout the day like all of these things are are kind of checked off exactly as you expected. There's no miscommunications here. And um you know we we want to just make sure that we have all of the constraints and context and everything

**[10:36](https://www.youtube.com/watch?v=W6f8nslLYzk&t=636s)** else that that's here. And uh what you're watching unfold is is really the the power of strategic prompting in action. And so we're coming up on on V3 um and we'll be finishing at V4. But section one was all about replacing print statements. Section two we're adding X-ray tracing and cloudatch metrics. Now on three uh we are transforming generic exception handling into specific AWS error responses. So no such key gets a 404. Access denied gets a 403. Uh and everything returns structured JSON instead of just plain text all over the place. And so the result is that we go from a Oh, did it stop? And so the result here is that we went

**[11:25](https://www.youtube.com/watch?v=W6f8nslLYzk&t=685s)** from just a a little 20 line uh snippet and we are going to finish this out with 388 lines. So it's still a very lightweight uh application here. But we went from something that was nowhere near battle ready to something that is a really thorough ready to kind of kick off uh the beginning of this production workload. Now, there will still be three uh three sections that I'm not going to go through cuz you don't need to endlessly watch the matrix scroll across my screen. Um but at the end of this uh we have kind of a quick report saying, "Hey, uh the len event has proper S3 structure. Um I was kind of roleplaying that this is the next Flickr or Instagram or something along those lines and I want the file sizes under 10 megs. Um all of the content types are

**[12:14](https://www.youtube.com/watch?v=W6f8nslLYzk&t=734s)** supported. image formats, file extensions, match content type, all required S3 event fields are present. And so at this point, uh, we have something that we can actually take and use. And this wasn't sped up. Um, so this is my diff file. Uh, so for all of you that are are accustomed to looking at the red and green text, we can see that we're removing a bunch of empty checkboxes, replacing those with a lot of checked off uh checked off line items. And this gives us a good deal of confidence that we are now, uh, kind of in in the right the right place. And so, uh, I'm not going to switch screens, but I have an IDE up and I'm afraid of, uh, altering my my share screen setup here. Um, but basically what I have is I have four versions of that Lambda function,

**[13:01](https://www.youtube.com/watch?v=W6f8nslLYzk&t=781s)** including the original snippet and the markdown file. And so I can see progressively as I added each one of these uh kind of what what modifications happened when. And uh the whole point was to really drive this drive this through to a to a complete status. Now um that was for creating something new, upleveling a bit of code, getting it from a a rough inspiration to a production MVP. Um but we often are operating while we're developing and so uh as the the last gentleman presented uh you know while the the serverless promise is just let let it be handled um we are still modifying these on a very regular basis

**[13:50](https://www.youtube.com/watch?v=W6f8nslLYzk&t=830s)** we're shipping code we're changing things we're promoting environments everything else I'm not going to pick apart the uh the anatomy of this prompt but it follows a lot of the same principles give it a definition or give the give the AI a little bit of uh context text of what's going on. And this one, I didn't tell it. It's a DevOps guru and all that stuff. Um, but I am seeing errors. And so what I'm doing here is I'm actually going to copy a bunch of errors out of AWS consoles and uh start correlating. And so I'm pasting in a timeline and logs from multiple sources. So API gateway execution logs, Lambda authorizer logs, main function logs, Cloud Trail audit events, Cloudatch metrics, IM policies, S3 configurations. And this is the the reality of when you're trying to diagnose something going wrong in

**[14:37](https://www.youtube.com/watch?v=W6f8nslLYzk&t=877s)** serverless is that you're often reaching into four, five, six different log um caches to to try to correlate these things. And just that cognitive overload on its own is pretty exhausting. And meanwhile, you know, you're not serving that service at that time and you're sweating and it's just a really nerve-wracking time. And so, um, you know, notice what I'm doing, uh, a little bit differently, uh, as we progress here is I'm I'm not looking for it to just go solve it. Like I I kind of want to have it explain to me what's going on. And so it puts out a plan, tells me, hey, we're going to do the root cause, verify the current infrastructure state, uh fix some IM permissions, and uh address some configuration mis mismatches. And since I'm still I'm I'm still not confident. I'm like, what what the heck is going on here? Like, give me a good synopsis. And

**[15:26](https://www.youtube.com/watch?v=W6f8nslLYzk&t=926s)** I'm sorry that I don't know why the uh play button refuses to go away there. Um, but I just say, hey, just give me the give me the the real root cause. What's going on here? And so the the most probable cause environment promotions are going wrong. Uh, someone deployed a dev configuration IM roll to a production environment or promoted code without updating the bucket references from dev to prod. And uh, since my Lambda function sitting there spinning around for 9 seconds, most of the time it's just looking for S3 things that aren't there and not failing fast. Um and so with that um you know let's bring this full circle. You know from prototype to production um

**[16:16](https://www.youtube.com/watch?v=W6f8nslLYzk&t=976s)** it's a lot more important to really think about partnering with these uh with these tools um over just kind of trial and error like trying to just throw one master prompt at it that's a page long or just oneshot it. Um, if you can kind of build that iterative flow uh with these tools, you can really kind of start to understand that a lot of the standard scaffolding, a lot of these elements that they're not they're not your engineering prowess. They're not the the top level of your capability. Um, it's really kind of just building a partnership where you can build all of this boiler plate boilerplate pretty quickly. You can leverage tools like this to actually use the the AWS CLI. Um you can use it to uh I' I've been coaching customers of mine

**[17:03](https://www.youtube.com/watch?v=W6f8nslLYzk&t=1023s)** to actually um use QCLI to use another uh command line tool that we have called the porting advisor for graviton. So while they're you know moving and migrating their Java applications from 8 to 17 to 21, we can actually certify agentically that these Java apps are ready for for use on Graviton and they'll be performant. And so what's really cool about this is that within the Q developer CLI, you just go download new command line tools, tell it a little bit about the tool, and then it can pick up and start using that tool without you needing to learn syntax. And I think when you can start getting rid of uh just a lot of the croft, like I can't memorize um reax expressions to save my life. Um, and you know, between PHP being my primary language, Python being the language that I'm learning,

**[17:52](https://www.youtube.com/watch?v=W6f8nslLYzk&t=1072s)** you got Reax, you got JSON, you got YAML, you got all of these other things that are out there that are just kind of clutter in your brain. And having something that's just at your fingertips that helps out with all of those other side tasks that aren't kind of core to your um your day-to-day responsibilities and they're just Google searches and just nonsense that you have to suffer through. Um, you know, it it's it's for me it's been a a great deal of relief like as I learn a new language knowing that, you know, an AI partner has my back on all of these things. And so whether you're enhancing code quality, troubleshooting complex distributed systems, or tackling your next serverless challenge, uh, remember, it's not about finding that magic prompt. It's just about building a strategic partnership that scales with your expertise. Now hopefully after that deciding to go

**[18:42](https://www.youtube.com/watch?v=W6f8nslLYzk&t=1122s)** download the Q developer CLI, if you just search Q developer CLI GitHub, uh it'll be the first result that comes up. Hopefully that's easy. Uh what's not going to be so easy, uh is the next session that you need to attend. So uh I work with both Matt and Grias. Uh so if you're a Java developer and you're looking to be able to kind of extend Spring to use AI, please attend his talk. Uh if you're running serverless at scale, attend Schulpa's talk, I think in this room. And then finally, uh another business partner of mine, Gidrius. If you're monetizing, scaling, promoting uh APIs, please attend that one. And thank you so much for your time. Um I have 5 minutes left over for questions. And I'd appreciate it. And thank you so much, Bangalore. [applause]
