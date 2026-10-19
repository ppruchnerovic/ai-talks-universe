---
id: oUZEt4EiPbk
title: "I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j"
slug: i-built-a-personal-ai-agent-on-a-raspberry-pi-jeremy-adams
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Jeremy Adams"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-10-03T16:30:34Z
video_id: oUZEt4EiPbk
url: https://www.youtube.com/watch?v=oUZEt4EiPbk
youtube_url: https://www.youtube.com/watch?v=oUZEt4EiPbk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Raspberry Pi", "NanoClaw", "OpenClaw", "personal AI agent", "edge AI", "agent memory", "graph memory", "knowledge graph", "Neo4j", "graph database", "MCP", "Claude Agent SDK", "offline AI", "hardware hacking", "Jeremy Adams", "AI Engineer"]
topics: ["Agents & orchestration", "Inference, serving & GPU infra"]
transcript: true
---

# I Built a Personal AI Agent on a Raspberry Pi — Jeremy Adams, Neo4j

**Jeremy Adams**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Raspberry Pi` `#NanoClaw` `#OpenClaw` `#personal AI agent` `#edge AI` `#agent memory` `#graph memory` `#knowledge graph` `#Neo4j` `#graph database` `#MCP` `#Claude Agent SDK` `#offline AI` `#hardware hacking` `#Jeremy Adams` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=oUZEt4EiPbk) · [Conference site](https://www.ai.engineer/)

## Description

No Mac Mini, no laptop agent. Jeremy Adams runs his personal AI agent on an old Raspberry Pi he wears around his neck.

Jeremy Adams, senior developer advocate at Neo4j, assembles a wearable AI agent live on stage: NanoClaw on a Raspberry Pi 4B, messaged over WhatsApp, with Docker-isolated agents and a Neo4j graph database. He shows how he built graph memory using the POLE schema (person, object, location, event) mid-flight, added voice-to-text through a USB mic and a hardware button, ran an offline mode with a local Neo4j, and walked the AI Engineer expo floor turning booth notes into a graph of themes. He finishes by upgrading to Neo4j Agent Memory.

In this talk:
• Why a small, hackable claw beats a feature-rich agent on your laptop
• Connecting an agent to Neo4j over MCP
• Graph memory with the POLE schema
• Offline-first capture with a local graph that syncs and enriches in the cloud

SPEAKER
Jeremy Adams, Senior Developer Advocate, Neo4j
X: https://x.com/jpadamspdx

LINKS
NanoClaw: https://github.com/qwibitai/nanoclaw
Neo4j Agent Memory: https://neo4j.com/labs/agent-memory/
Agent Memory (GitHub): https://github.com/neo4j-labs/agent-memory
GraphAcademy (free courses): https://graphacademy.neo4j.com/

CHAPTERS
0:00 Intro
0:12 Hi from Neo4j
1:32 What we're building
1:57 Live hardware setup
4:51 The Raspberry Pi claw boots up
6:06 Why small claws
8:05 Why NanoClaw
8:55 Architecture: WhatsApp → NanoClaw → Claude
9:40 Graphs 101
10:10 Querying Neo4j over MCP
10:50 Building memory on a plane: the POLE schema
12:15 Demo: the memory graph
13:29 Adding voice-to-text
14:49 Recording the expo booths
15:34 Offline mode with a local Neo4j
17:03 Enriching themes in the cloud
18:23 Upgrading to Neo4j Agent Memory
19:33 Get started with GraphAcademy

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,760 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=12s)** How's everybody doing? Day what is it? 4 400 something. Thank you for bearing with us as we had a little technical difficulty getting started. But I am Jeremy Adams. I'm from Neo4j. You might have seen our booth. It's kind of right over that way. And we're all about graphs and graph databases. Today I'm going to expand that a little bit to a side project I've been playing with. Uh who here has done something with uh open claw or Hermes agent or any of your kind of claw of choice. Okay. So a lot of some folks but most folks are kind of new to the space which is cool. How about uh things that are more like edge devices, hardware? Um

**[1:01](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=61s)** thinking about like you know offline mode kind of stuff. Yeah. Okay. Some interest there. Um how about who's experienced with graph in general? A little bit of graph some graph people. Cool. And how who's been doing like building agents with memory and things like that? Okay. Whoa. Cool. That's the the biggest group so far. And I want to keep it going. We're going to try and do more things that have to do with uh statistics of some sort uh as we get to some findings that we're going to do in a little bit. So, um what I'm going to do in this talk today is talk about this agent memory project that I did that involves a bit of hardware that you can see on my chest. And um as we go through it, we're going to talk about how I also built up some software for agent memory

**[1:52](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=112s)** and how that all went. So, this is like the livest of the live demos I've done with this so far because I'm like literally assembling the pieces in front of you. So, let's see. We're I have a microphone, little extra microphone. Yes, I'm going to be using this to talk to my claw in a second. It's not It's not yet powered on. So, this is really crazy. And I've got this uh I've got like a capture a video capture from my HDMI, which is over here. I'm going to plug that in. Whoa. Somewhere. Plug that in. Okay. It's not on yet. I'm also going to This is the receiver for the USB for the mic. So, we hope this works too today. If I can see where it goes. There we go. Plug that in.

**[2:43](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=163s)** Guess that's why they made USBC. You have to keep flipping the thing over. Okay. So, there that goes in. And now gonna try and sync these two mics. Okay, they're green. That's okay. So, I got a mic there. Now for some power. Good old good old battery power. All right. So, what I'm going to do really quick, just for fun before we get into the main presentation. I'm going to show you this trick. So, with this weird video capture situation I've got going on, I'm going to go over here to my QuickTime player, and I'm going to say that I want a I want something that it will not let me do right now. Let me quit QuickTime Player and let's reopen it. All right, here we go. And let's try and

**[3:34](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=214s)** do a f a new movie recording. All right, we can see there we go. You see the claw? All right, we don't want to see that. We want to see what's on the claw. So, what I'm going to do instead is I'm going to use the source will be from my from the output of this video here. All right. So, let's power it up and I'll try my best. There we go. To catch it during the boot sequence. All right. So, I'm going to go here to my I'm going to change to this USB3 capture device and I'm going to move this around a little bit so we can see it. And hopefully, I mean, I can't give you any guarantees, but hopefully what's going to happen is as this guy goes, we're going to see something actually happen.

**[4:23](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=263s)** So, I'm going to give a little reset to that and back to that. Oh, and let me push power on this. Okay, there we go. All right. So, again, hopefully I see power is now flowing through into here. Okay. Oh, something's happening. Okay. And um this gives me high confidence because I've done this only like one million times as you can imagine, hacking on this silly thing. Okay. Raspberry Pi desktop. Oh, yeah. So, this is a Raspberry Pi 4B, not the latest model. Okay. So, um, but very serviceable, and I was running a 32-bit operating system for a long time until I realized it was 64-bit ARM capable. It's pretty cool. Um, you can't run everything on this thing, but you can run quite a bit. And,

**[5:13](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=313s)** um, we're going to get into exactly what I did put on this to end up getting this presentation together. Okay, cool. All right. So, it's alive and I've got a little extra Bluetooth keyboard and that's how I can drive things on here. And we will do that um in a second. But I mostly just kind of wanted to show you the setup so you could, you know, believe that it actually is a real thing. And uh there we go. All right. So, now I'm going to get into the presentation. We'll come here. There we go. I'll come back to this Pi here in just a second after I open up. There we go. And just to give you a a flavor, uh, this one has nano claw, but it also has Docker on here. And I'm running Neo Forj on on here. I've got a little Docker based Neo Forj database. Okay,

**[6:01](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=361s)** now let's continue with the talk and we'll get back to the claw in a minute. So small claw. What did I I I said small claws are beautiful. What did I mean by that? Well, there was a lot of hype happening and still is about these personal agents, but I did not want one that was on my laptop. I'm sorry. I'm a little conservative. I come from the old kind of cisadmin devops space. I'm like, I want to wait for this stuff to be really solid before I do something like that. But I I also wanted to be cheap, open, hackable, right? And for me, I wanted to understand what was happening more than it being featurerich. That was more important to me. And so I went and I saw like lo I live in Portland, Oregon. I looked on Craigslist. Somebody's selling a Mac Mini with OpenClaw pre-installed. I'm already like pre-installed. That's a red flag. And

**[6:50](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=410s)** you know, Mac Mini could be cool, but um I know now it's not going to be 600 anymore with the recent price increases, right? So that's not a small claw as far as I'm concerned. So then I reached back and this is uh I did I think it's pandemic or at the end of the pandemic I did something where I was hacking with this very Raspberry Pi doing something like measuring the weight of the dishes in your sink to tell you you should wash the dishes. Anyway, you could check out the video there if you like that kind of nonsense. But that's this exact guy. And I saw I said I have this in the closet. Will it claw? I don't know. I should try it and see. And uh yeah, it claws real good. It was and um that that that little that it's not a sticker. It's like more like me, you know, photoshopping a a claw on there just like, you know, oh, maybe someday I

**[7:38](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=458s)** could actually, you know, uh do something really cool with this. And uh but you see my old setup. I have this external monitor. I've got my external keyboard. There's a mouse off screen and everything. This guy, this is a game changer right here. I'm like so it's so sleek now. Uh, it's got onboard Wi-Fi, which is great, or you can plug into wired. So, hopefully I'm actually on the network. We'll have to check that in a second. Um, okay. And then addition, uh, I used nano claw. So, I didn't use open claw. I found this other project that more suited my tastes because it was like 15 source files and it was quite compact and small number of lines of code. It just used Docker containers to run the agent processes. So they couldn't run a mock on the system. I was like, okay, this is my kind of thing. So

**[8:26](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=506s)** I said, I'm going for it. Uh, and so I like the other boxes that check for me. I could run Linux on here. It's got a Docker. I understand. Uh, it was based on cloud agent SDK, nano clause, and I could and they actually encourage you modify it. Use cloud code. We got skills in there. Hack on it. Make it work for you. And it use messaging like, you know, Telegram if you want. But I was like, well, I had WhatsApp on my phone, so I'll just use WhatsApp. Perfect. So, the initial architecture was something like this to go from my iPhone uh or my MacBook WhatsApp, you know, and then go through and talk to NanoClaw on this Raspberry Pi. That's it. And you just had to get like a credential. You go on the NanoClon, you get it to register. So, now you know WhatsApp's in the cloud. And this thing can pull messages down from it. And of course, you know,

**[9:15](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=555s)** on board, I said we're using Claude stuff in the background. So you got all the power. There's no inference, no LLM inference happening on this thing. I am using the CL the cloud for all that. So I've got a big brain though it's over over a wire to the cloud, right? But then uh I said well what can I do with this? You know uh I I've got also in the claw in the cloud I also have Neo forj. I've got Neo Forj database up there. And for the folks here that have never done graph before this is your graph 101. There is a small graph and this is a graph. Can you see which ones are the nodes, right? The round ones. And you see the relationships, the edges between them. So, there's two person nodes and a movie node. And Tom Hanks, the person acted in Horus Gump and Robert Zmechus directed it. Pretty easy. That's it.

**[10:04](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=604s)** Now, you know, graphs. So, I asked in a WhatsApp message once I had this database full of movies and I had my claw connected. I'm like, "Hey, tell me what movies Tom Hanks acted in." and it went through there with an MCP server connecting into my Neoforj instance with the movie database in there, right? And then it responded back to me. It's like, "Oh, well, first your stuff's not set up right. It's broken." I'm like, "Oh, okay. Let me fix it." So, I got on the claw, made sure O was working, and then I got a bunch of results back on the right there. And those all came right out of pulling data from the database, feeding it back up through the cloud agent SDK, forming a response, and sending it back through the WhatsApp channel. Got it? So then I was like, well, what else could I do with this? And I'm on the airplane, and I found

**[10:52](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=652s)** that even without paying for Wi-Fi, I could use the messaging stuff and WhatsApp was working. I was like, oh my god, I could talk to Claw right now. So I was like, hey, could I do memory? And I said, well, I'm not exactly sure what I want, but I was reading blog posts about this thing called poll plus O. So, this is a way of doing memory where you just think of like person, object, location event uh uh an organization, right? And it's this actually came from the European policing and you know those folks have been drawing graphs for a long time and every every one of your favorite cop shows that does a string diagram, right? And so then I just was on the plane. I'm like, hey, could we build a memory system using pole plus o? And then it's like, "Yeah, sure. Yeah, we can do it. I'm your right of skill for that right now. I've got this mount point. It'll persist even when you reboot me. No

**[11:40](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=700s)** problem." I was like, "This is amazing." And so now I have this thing where I've got Neo4j in the cloud. I've got this new memory database with this super advanced schema memories and related things very early, you know, before Carpathy's, you know, wiks and be after Obsidian, but you know, you get the idea. It's it's that kind of thing. And this is what ends up being in Neo forj memory nodes that show like places I was going and as I went to do little Devril events I was having this thing record it for me and all that. So then we can like actually jump in and look at this database. So I'm going to go over here to um to the web browser which I'm already in but I'm going to go over to this other tab and over here I've got Neo forj Aura and I've got this demo instance. I'm going to connect to it in

**[12:27](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=747s)** query. And this is where I've been storing all this information kind of over time. And so I'm going to jump in and show you the memory nodes. I got a bunch of stuff. It's kind of a dumping ground in here, I admit. And um here's all the here's the memories. So he these are those original memory types that I had in here. And I actually want to show you the memories. I want to show you all the memories uh as they're connected to other things. And I'm going to run that. So you can see more like the connected graph. And as I zoom in on this thing, you can see there's like me going to there's, you know, talking to a person going to the snowflake office in Menllo Park. Menlo Park is itself a location in that framework and then I was at a certain AI meetup event, right? So it

**[13:17](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=797s)** follows and there's people in here like Rebecca, like Jeremy, there's different people, right? So this is one way of doing it. So then going back over here, we see that we can definitely store memories. Well, what else? I was thinking can I fit on this physical claw and somebody was doing like they had a microphone out their window and they were recording all the bird song in the backyard and they could there was a bird net model that that could tell you that. And I was like, "Oh, whoa. I want to do that." And then I was like, "Oh, wait. Or maybe I could do voice to text. Is that possible?" So then I was like, "Sure enough, let me hook up a USB microphone, right, and do something like that." And then do some voice to text and and do something like that. So, um, and just to get ahead of it, just for fun, I'm going to go ahead and try and use

**[14:05](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=845s)** Oh, that's funny. Oh, there it is. The button fell off. So, I I made this button and it's connected into into some pins. This is me getting ahead a little bit, but just in the interest of time, I'm going to go ahead and plug this back in. And what this allows me to do is trigger that model and I'm going to do some quick recording. I'm saying I am actually on stage at AI Engineer World delivering the talk I've been preparing for, right? And so I you see the little lights went on. So it did some recording. Hopefully we'll be able to look and see if we actually if I'm actually online, if we got a message and so forth. But this is the dream, right? And I started doing it with all sorts of microphones, playing around with it. And then I was like, "Oh, I want to bring this to AI engineer and I want to like walk around, right? And with these recording little LEDs on

**[14:54](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=894s)** it, and I want to like record something. I don't know what I want what I want to record." And I was like, I know what I'll do. I'll go booth to booth and I'll record what messaging people have up at their booths. And then I was like, let me build this thing. And then I actually started working on, you know, adding in that kind of capability for recording. And then I was like, okay, well, the booths, they got numbers and names. Okay, I had to map this out. So I was like, I'm just going to like create a very simple data model. It's just exhibitors and they're not even connected. They're just there in the database. So I tried to get as many as I could and there was some data cleaning to do. And now then then uh I was worried. I was like, "Oh god, conference Wi-Fi is terrible typically." So I need like an offline mode. So then I had this other thing. I put Neo forj running on here and then I was like, well I I could

**[15:42](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=942s)** have this thing so if I'm offline it'll use some reaxes and stuff and parse out of the audio voice to text the booth number and maybe it can write a query to insert it in this local database. And you know again if this if this thing is uh if this thing is up which I at this point I'm not even I'm not even sure. Um, we're going to try cipher. Uh, my cipher shell browser. Oh, I should spell right. Let's go. Cipher. Shell browser. So, this is like a little program I wrote to talk to Neoforj databases without a very expensive guey and things like that. And I should be able to match all my exhibitors and return those. So, this is talking to the database that's running in here around

**[16:31](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=991s)** my neck. And as I go in here and I look, I could say, "Oh, yeah, there's Microsoft, Minmax, CI, right?" And so this is me and I had on these like my raw notes. It's like, "Oh, this is like the raw notes that I took. I'm at this booth and blah blah blah." Right? So I and I took that data and then I uploaded it later up into Neo4j in the cloud. And in the cloud, um, it looks a little bit different because I've now enriched it. And so if we look at this, let's see if I can just move back into Neo forj for a second. And here I'm going to look for exhibitors, right? And here are my exhibitors. And the exhibitors, I can click on one. And you can see they're actually connected to something else. So I did load all

**[17:19](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=1039s)** their data in. So here's, you know, got the notes all cleaned up now on them. But you'll notice that these other things are connected to. And the things that they're connected to is I'm going to put in here they're connected to all sorts of other things. And I'm going to put a path through them and return the path. And we end up with something like this. This shows how they're all connected to some other theme nodes. So at some point I figured out, oh look, there's some themes that exist here. Evaluation and observability. Build kite has that theme. Lang chain has that theme, right? So I I was like, okay, I've got I've actually generated some knowledge that was maybe novel that maybe nobody has any, right? So are there themes? Yes, there are themes. So

**[18:08](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=1088s)** these this is the data dump that I collected by walking around the booth and figuring out what the themes were. So there's a whole bunch out there. And um I know I'm just about at my time. The thing uh I will point out for folks that are interested uh in talking more, I did subsequently upgrade the agent memory that I have using the agent memory service. Basically, I wanted to load all of the WhatsApp messages that I ever had in all and it's been a while I've been talking to it as you see. I wanted to upload all of those in there and see if I could get some kind of insights out of those. And sure enough, I use this Neo Forj agent memory service. And if you log into this sort of thing, at some point I just connected it up and that allowed me to get a whole bunch of memories from the conversations and then

**[18:57](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=1137s)** it distilled them out. And you can see here that uh I've got all these different things, these conversations that I've had and so forth. And this will allow me to browse those memories and um for example, all the people I've spoken to or the locations, the concepts, whatever. So this these are all the things that I've been doing talking about with my claw and they're all distilled out into memories that are now accessible via an MCPU server from this very claw. So anyway, that gives you some flavor of how this stuff works. Please come see us at booth P3 over there. I can tell you a lot more. If you're just getting started with graph, you can go to Graph Academy, which is this link right there, and we've got all these hands-on courses. It's all totally

**[19:46](https://www.youtube.com/watch?v=oUZEt4EiPbk&t=1186s)** free to use. So, please either uh visit us there or even better at the booth. Thank you so much. [music]
