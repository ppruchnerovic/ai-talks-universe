---
id: sJ2jc7leKBk
title: "I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)"
slug: i-gave-an-ai-agent-the-keys-to-my-life-here-s-what-happened
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Radek Sienkiewicz"]
channel: null
duration_min: 20
published_at: 2026-05-02T22:00:06Z
video_id: sJ2jc7leKBk
url: https://www.youtube.com/watch?v=sJ2jc7leKBk
youtube_url: https://www.youtube.com/watch?v=sJ2jc7leKBk
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration"]
transcript: true
---

# I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)

**Radek Sienkiewicz**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=sJ2jc7leKBk) · [Conference site](https://www.ai.engineer/)

## Description

An honest look at what happens when a personal AI agent is allowed to operate around the clock. Over months, one permission at a time, it went from reading files to handling email, backing up its own memory at 2am, monitoring its own health, and drafting real business replies. This talk covers the permission creep, the overnight cron ecosystem, self-monitoring and recovery, trust boundaries, and the surprising value of giving an agent a personality that disagrees with its owner.

Speaker info:
- https://x.com/velvet_shark
- https://www.linkedin.com/in/radeksienkiewicz/
- https://github.com/velvetshark

Timestamps
0:15 Radek's path to OpenClaw
2:17 The philosophy of incremental growth and system updates
4:51 Integrating the Obsidian knowledge base
8:59 Ambient operations and overnight automation
11:02 Core job types for the AI agent (Ambient Operations, Attention Filtering, Execution)
13:03 Deep dive into specific Discord integration channels
14:54 System architecture: LLMs, scripts, and memory management
16:28 Challenges: Bad memory, brittle automations, and noisy nodes
17:19 Conclusion: Optimizing for the future self

## Transcript

*2,773 words · source: supa (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=15s)** ready to go. >> All good. Yeah. >> Please welcome Radic, everybody. >> Cool. >> Hey, I'm Radic. I'm one of the open claw maintainers and uh I want to talk what happens like in my life with open claw when I practically gave the keys to my life to to open claw and and like it almost like literally and uh what that actually means so so this happens like step by step it wasn't all at the same time but it can access my emails. It can access my notes, files, calendars, tools, my operating system, so automations and it builds on top of like memory of everything that I

**[1:05](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=65s)** do uh at the computer. So, uh it can do anything with it that uh that is possible to do with the computer. But it didn't all happen in one big like leap. So I install OpenClaw and now I it just like controls my life and does everything for me. Uh that that would be silly to do or like even silly to expect that this could even work. Um so what happened is that I I tried installing uh just like like everybody does just like with one channel. I think it's at the beginning it was just WhatsApp then

**[1:55](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=115s)** I migrated to telegram now I'm on discord but it was just uh just WhatsApp just uh one ability to do to just like chat okay so we are there uh what what's next that we can do uh let's let's do some like one simple workflow or one very simple task that we can do once we are there let's go to the next step so this is how it happened where I am today where I used to think that I have quite a simple setup with uh my open claw and what it does because I never did any big change but when I encounter different I don't know Twitter threads uh YouTube videos or talking to other people how they have it set up I

**[2:45](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=165s)** see that like my setup has everything that they have more on top of that and most also is just like more sophisticated than what what I see out there which was really surprising to me because I felt that it's just like one small step at a time. I have a pretty like simple setup works for me but uh that that's what I want to to show how that happened and how it looks like today. So you you already had like a lot of talks about how the sausage is made, how we are making it better. You'll have more talks about the insides of the open claw. I want to show how it looks from the other side from the first the simple

**[3:34](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=214s)** user then power user. Now I'm also a maintainer. you don't have to go to the maintainer route but uh when I was playing like with one of the uh workflows I just encountered some errors and just like submitted first PR then the second PR then just looked into Discord and then you just got involved now I'm a maintainer there so it's also was just like one one step at a time uh so that that's the set of these are the steps that uh it usually happens that I see I see the need uh I solve it in in a very simple way uh and and then I add more steps to it and this is also why I usually don't have big issues that people have that okay now it broke my

**[4:25](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=265s)** computer or it just like completely bricked during the update because I have all these small steps that I take if something breaks I just like step take one small step back fix it see what doesn't work, understand why it didn't work, uh have a setup that it never happens again, and just like take one step further again. So, uh where it started being more and more helpful and kind of like running my life is when I gave it my knowledge base. So, I had a lot of stuff in my Obsidian which I built up for years. So, right now I have like about 3,000 pages or notes, markdown files in my

**[5:16](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=316s)** Obsidian. And this is everything. This is work stuff, personal stuff, tasks, projects, research. Um, what else? Articles kind of like an inbox of links that I'm just putting there and it then finds the the connections u, and puts it in in perspective and in context to to other stuff that I have. So all of that is now accessible through my open claw with a very good search. I have search and memory. I have like normal search. I have QMD search for for obsidian. I have different memory for for my workspace.

**[6:08](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=368s)** uh and all of that is interlin and and and that that's where that magic happens. And when I saw recently and that that's where it hit me that I probably don't have a simple setup. When I recently saw Andre Karpat's tweet that went viral uh where he says about LLM knowledge bases, I was reading that and it's just like yeah, that's exactly what I have. like what's like super uh revolutionary about it and then I I I understood that okay so I got there step by step it works for me so it's probably probably worth I don't know sharing sharing telling more about it u showing how it works showing how you can get to that point as well uh

**[6:58](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=418s)** and uh for example for Obsidian um do Yeah, this this is how this is the real screenshot of my my vault and all the nodes and these are different clusters. Some are probably uh project related like the big clusters. Some of the one off uh these are probably more uh kind of like bookmarks. And one of the tasks that I'm doing and that I have is that when I add something uh to inbox it then takes that link that I add there looks what's there it could be a tweet

**[7:46](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=466s)** it could be a thread uh it could be an article it could be a YouTube video analyzes it adds tax to it adds context to it looks at what's already there on this topic in my vault, how it could be helpful in other areas and adds connections to it. So what previously was just like Twitter bookmarks that you bookmark and you never go back to that now it just adds more context builds up my knowledge base and is much more helpful and even surfacing the things for me when I add a bookmark that okay so you already had like this and this and this about this subject and this is how it connects maybe you should look at

**[8:34](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=514s)** those notes and very often it's just like yeah completely forgot about that and and that's a good source of of knowledge and of thinking about it. Uh because that was the reason why I'm adding this bookmark. Uh so that that's where it's it's starting to uh to be super super useful. On top of that also uh at 4:00 a.m. well like 4 a.m. is just like uh an example of that that I have. This happens probably between 3 and 6 more or less. Um, so this is what what is happening when I'm sleeping. So when I'm sleeping again, my agent does everything so that it runs well. It indexes everything. It backs everything

**[9:22](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=562s)** so that worst case I if I lose something, I lose maybe couple hours of work of content of anything else. refreshes all the indexes for for QMD for memory for my Obsidian vault and I I start fresh in the morning uh with uh whatever waits for me maybe summary of the emails of the calendar uh everything updated the latest uh the latest open version is waiting for me which also took like step by step I have some scripts around it so that it knows what to do and what not to do when updating what can break, why it breaks, how to verify it before updating or before restarting uh your gateway so that it is able to

**[10:12](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=612s)** come back online again. So that that all is uh also uh automated and as as I get up it's it's already waiting for me uh fresh and ready for me to start the day. And each open claw is like I'm not a big fan of sharing like my exact setup because that exact setup is like very specifically for me for what I need right now uh for what I will need in the near future for like the errors that I encountered for issues that I want to be solved. But to give you some idea so that we can talk more also about specifics and not just like in general. So these are some like five areas or five types of jobs that my

**[11:02](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=662s)** agent is doing. Uh the first one is is ambient operations. So so this is what I just uh showed you. So it it does all the updating. It does all the plumbing. Uh it does all all the stuff that needs to happen. But I don't need and I don't want to think about um the the second is attention filtering. So this is also super useful that because it has access to everything and because it has all the content context actually uh so it knows that for example when an email comes and uh it's something important or urgent and it knows from obsidian what's the context and the background behind it. Uh yeah I I keep everything in obsidian about

**[11:51](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=711s)** projects about everything else. So it then can proactively tell me that uh I think I have here. So like these are like three very specific examples that I had recently that when the system notices that something is important and urgent, it just lets me know. So like Netflix payment failure for some reason didn't go through uh was fixed within five minutes when it happened. Domain renewal coming up. I would probably miss that email. Uh but uh it it picked it up uh gave me gave me a message on my discord uh renewed my domain uh emails uh that can already be with enough context given about the project for example it can already uh give like

**[12:41](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=761s)** read the email uh understand what's happening understand what's already done within the project and just draft the reply and and it's already in in draft uh folder for me to uh accept or or delete or make some changes. So, so these are some examples of like potential filtering uh execution supports. Yeah. So, that's draft synthesize is that uh the the inbox and these are on the right. These are the channels that I have in my discord that more or less relate to these types of jobs. So general is where I have everything. Uh I just start the conversations uh see where it goes and if enough times I have a type a certain

**[13:30](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=810s)** type of conversation I added a specific channel for it. So the these are uh like real screenshots from from today morning. Uh the inbox is where I just like drop links and it builds the knowledge base for me. Consulting is for for for the clients and every all the backgrounds. It knows all the projects. It's know knows all the quotes, deadlines, tasks, next steps, everything else. Video research is for for YouTube for researching what's what's out there uh to help me uh with with the next episode. Uh briefing is for morning briefings. Instagram for social posting. YouTube is uh for for creating creating the the videos. Open claw is for

**[14:19](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=859s)** maintainer stuff and there's also one playground channel uh which it changes depending on day month or the need. Uh it's for testing. I usually test maybe a different model, maybe a different uh workspace, different way of setting up uh the the important files like memory and everything else. So I just play there, see what works. If something worked, uh I promote it. If if it doesn't, uh I discard it. Uh and all of that works because it's not just uh it's a system that has many moving parts that work well together. So LLM is for judgment like understanding the email, understanding the context, making the connections. Then there are all the

**[15:08](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=908s)** files the the tools the scripts that I have built the scripts are just like if this happens do this it's done you don't even need judgment so LLM is even skipped uh and important uh thing is also to optimize your memory file your sole soulm file uh I have also critical rules MD uh because even if I had something in agents MD or in soulm uh it it still managed to to forget something or not do something uh with critical rules. Having critical rules helps and having it uh mentioned quite high in the agent D file. Uh so that that's also an improvement. Uh I I

**[15:56](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=956s)** went through a few different setups of memory where I had one memory file. Now now that uh I have like the whole memory folder now we also have dreaming where uh we have like promoting the memories. So this is important to work on these files uh and but it's easy to do in open because everything is inspectable. These are markdown files editable you can look at it you can read it you can understand it uh and it works well. Uh what gets harder? Uh bad memory compounds. If the memory is not set up correctly and your vault, your nodes, your memories grow to thousands, you're going to have an issue. So you need to actively work on that. Brittle

**[16:43](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=1003s)** automations, especially when it's like 10step automations, uh it can break and it probably will break at some point. So it's again either split it up into simpler ones or or have uh some guard rails uh that are more effective uh noisy nodes I'm getting rid of them cleaning um cleaning regularly and weak boundaries. So so those are all the sol everything else uh that the files that that are important to optimize for your needs. Uh so what I want you to take away from this is that like do what I did and then at some point you realize yeah this stuff is awesome and this stuff helps my life. Um start with one recurring pain grow trust incrementally

**[17:34](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=1054s)** build the knowledge base uh move everything or like move as much as you can or as you want to markdown files and and start making those connections. Um, inspecting system expectable is is easy for you done for with uh with open claw um and optimize for the future you and this is what I want to close with. So couple years ago I had an article about like the past me, the present me and the future me and the past me is just like this completely stupid guy. He does nothing. He's lazy. Uh he doesn't want to do anything. So now I present me need to do everything for that like past me and and the future me the future me is

**[18:22](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=1102s)** just like kind some kind of like god creature it can do anything uh that that that creature is like um all powerful and just like if I don't do something today it's fine that that other creature will do it for me. So that that was the the issue and uh the job for me is to to become friends with the future me to to treat that as a person that I want to help with and that's the job of the agent. So I don't need to do as much as I used to because the agent just helps the future me as much as possible so that when I wake up tomorrow it's like as much as could be done but someone else other than me is done. So that's that that's the whole purpose of of this setup at

**[19:11](https://www.youtube.com/watch?v=sJ2jc7leKBk&t=1151s)** least for me. I don't know it could be different for you. So that's what I want to leave you with. Thank you.
