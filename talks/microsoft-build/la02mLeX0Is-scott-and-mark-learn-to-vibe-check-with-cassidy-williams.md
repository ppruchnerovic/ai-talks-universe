---
id: la02mLeX0Is
title: "Scott and Mark learn to Vibe Check with Cassidy Williams | LIVE114"
slug: scott-and-mark-learn-to-vibe-check-with-cassidy-williams
conference: microsoft-build
conference_name: "Microsoft Build"
category: "Vendor & platform"
edition: "Build 2026"
year: 2026
speakers: ["Scott Hanselman", "Cassidy Williams"]
channel: "Microsoft Developer"
duration_min: 12
published_at: 2026-06-05T15:40:12Z
video_id: la02mLeX0Is
url: https://www.youtube.com/watch?v=la02mLeX0Is
youtube_url: https://www.youtube.com/watch?v=la02mLeX0Is
tags: ["Cassidy Williams", "LIVE114", "LIVE114_v1", "Scott Hanselman", "Scott and Mark learn to Vibe Check with Cassidy Williams | LIVE114", "build", "build 2026", "m9z7", "microsoft", "microsoft build", "microsoft build 2026", "ms build", "ms build 2026", "msft build", "msft build 2026"]
transcript: true
---

# Scott and Mark learn to Vibe Check with Cassidy Williams | LIVE114

**Scott Hanselman, Cassidy Williams**

`Microsoft Build` · `Build 2026` · `2026` · `12 min`

`#Cassidy Williams` `#LIVE114` `#LIVE114_v1` `#Scott Hanselman` `#Scott and Mark learn to Vibe Check with Cassidy Williams | LIVE114` `#build` `#build 2026` `#m9z7` `#microsoft` `#microsoft build` `#microsoft build 2026` `#ms build` `#ms build 2026` `#msft build` `#msft build 2026`

[Watch the recording](https://www.youtube.com/watch?v=la02mLeX0Is) · [Conference site](https://build.microsoft.com/)

## Description

AI can turn an idea into a working demo faster than ever. But can that demo survive two experts who have seen every trick in the book? In this live Build showcase, developers present AI-assisted apps, agents, tools, and workflows to Mark Russinovich and Scott Hanselman. Mark and Scott will ask how it works, where the seams are, what the AI actually built, and whether the result is clever prototype, production-ready software, or something unexpectedly magical. Come for the demos. Stay for the technical reveal.

𝗦𝗽𝗲𝗮𝗸𝗲𝗿𝘀:
* Scott Hanselman
* Cassidy Williams

𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻:
This is one of many sessions from the Microsoft Build 2026 event. View even more sessions on-demand and learn about Microsoft Build at https://build.microsoft.com

LIVE114 | English (US)

Broadcast Stage

#MSBuild

Chapters:
0:00 - Cassidy acknowledges the approach is unconventional and done for fun experimentation
00:03:07 - Discussion of creative motivation—making something neat yet intentionally terrible fits the show’s theme
00:03:52 - Overview of JavaScript, WebAssembly, and CSS roles in the project
00:04:05 - Code demonstration setup and visibility adjustments
00:06:25 - Fixing AI-generated errors manually
00:06:43 - Balancing human creativity and AI assistance
00:08:09 - Testing application limits with query restrictions
00:09:45 - Conversation about AI response and its agreement with the approach
00:11:26 - Closing remarks, open-source project mention, and transition to sponsor break

## Transcript

*2,363 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=la02mLeX0Is&t=0s)** And we are back with Mark and Scott learn to vibe check. We have just seen Steve Sanderson make a vibe coded entire operating system in a couple of evenings with the power of AI >> Amazing. It was amazing. >> You were impressed? >> I was impressed. It's when I when I see a project and go, I wish I'd thought of that. That's >> I love that. Yeah, everything Steve does I'm like, I wish I did that. But now today we have Cassidy Williams who's going to share with us what she has made. We have no idea if it is AI slop, if it is vibes, or if it is AI augmented software engineering. Cassidy, what do you have for us? >> Hello everyone. I have been thinking a whole lot about databases lately. There's so many new ones coming out, so many things. And so I thought it'd be interesting to build one in the browser where it just runs in the tab. And so if you can see my screen here, this is a little query shell. And so right now

**[0:47](https://www.youtube.com/watch?v=la02mLeX0Is&t=47s)** it's doing select star from ideas. This is a query that you've probably seen before with just this little table here. I could change this to say for example select title and then I have a ranking in here called cursedness. Cursedness from ideas and then it will filter based on that. I could also add a where clause where I do where cursed cursedness is equal to catastrophic. And then I can run that query and it'll just work. And so I can continue adding things. I also had a query builder here so I wouldn't have to keep typing things. So cursedness could be medium. I want to filter by certain things. I want it to descend. I want to limit things. I can do all of that and then once I

**[1:35](https://www.youtube.com/watch?v=la02mLeX0Is&t=95s)** minimize this, I can run the query and it will show. I could even add a drop table in there and then it'll say, oh no, this is load bearing. So this is all very fun. I'm also able to attach a sample SQLite database in here and then if I just run the query again to select everything and not drop that table, it will load, and that's great. You've all seen this before, right? Jude, where you can see a table, it's using WebAssembly to pull in the SQLite DB in here. But, there's something that's a little bit more fun about this. There is no database. And there is no query engine. It's done with pure CSS.

**[2:24](https://www.youtube.com/watch?v=la02mLeX0Is&t=144s)** >> Oh, no. >> Exactly. Oh, no. All of the querying being done is in pure CSS. Where yes, I use JavaScript to actually load this onto the page, and it's using HTML to show the things. But, all of the queries that you're seeing is done with just CSS selectors, CSS variables, if functions, all of that. Should you do this? Probably not, but I did. And that is what I did here. >> Why would you do this? >> I don't know. I I was like, what if I built something for this show specifically where I was like, yeah, this is neat. And what if I made it terrible? And that's kind of where it came from.

**[3:11](https://www.youtube.com/watch?v=la02mLeX0Is&t=191s)** >> That's exactly the spirit that I was looking for for this session. >> Good. >> Uh do you know CSS? >> Oh, I love CSS. CSS is one of my favorite programming languages to use. And it is a programming language. >> When you clicked attach SQLite dialogue popped up, does that file do anything, or is it empty? Is that a real database? >> That is a This is a real data Like, the thing that you're seeing on the table is real SQLite that is loaded onto the >> literally querying >> I'm literally querying >> or SQLight? >> It's an S I say SQLite. It's SQLight. What's correct? >> Does anyone know? >> SQLite. >> SQLite. Anyway, it's it does that all Again, JavaScript and web assembly loaded onto the page and then CSS does everything else. All of these checkboxes are using CSS to

**[4:01](https://www.youtube.com/watch?v=la02mLeX0Is&t=241s)** query and filter things. >> I want to see the code. >> You want to see the code? I got you. Check it out. >> You need to make the code a lot bigger. >> I will need to make the code a lot bigger. Okay, one second. Let me pull this up so you can see all the things. >> large, just like >> Okay. >> [laughter] >> Cool. And I made it light mode so that way it can be seen, but I'm sorry if you're going blind. Okay, so this is truly just HTML. There's nothing here. You could see all of the CSS or all all of the JavaScript loaded it on the page and everything else is in CSS. The Chrome CSS file is truly just for styling that HTML so that way it's pretty. I picked a random theme in there, but everything else is done in CSS. So, this table right here, let me hide the

**[4:50](https://www.youtube.com/watch?v=la02mLeX0Is&t=290s)** sidebar. It pulls in everything as a grid. But then it uses the CSS variable sibling index and that is used specifically for limiting, for example. Every single query has a CSS variable in there. And let's see. I have >> you And you know CSS. You're one of the people that understands it. >> Oh, I know CSS. >> Okay. And when you were Do you use Do you use GitHub Copilot? >> Yes. >> And uh did you use the Copilot app or do you use the CLI? >> I use I So, I used the GitHub Copilot app uh alongside writing things in VS Code and every single time I was like, "Mhm, this is gross." That's where I uh used some some assistance. >> Okay. How much writing did you do versus just yapping to the machine? >> I'm sorry.

**[5:37](https://www.youtube.com/watch?v=la02mLeX0Is&t=337s)** >> How much actual writing of the code did you do? How much is bespoke? >> How much of this is bespoke? Like like handwritten by me personally >> Right. Like you're like it doesn't understand CSS like Cassidy understands CSS." >> Oh, I'd say like 20%. >> You hand wrote 20%. Why? >> I like CSS. It's a nice language. >> You're one of the people that likes it. >> I There are >> You might be the only one. >> There I see some people in the audience who I know like CSS. I know some faces. It's a great place. >> it. Uh there are people literally nodding their heads next to people that are like, "No." >> heads. Come on. It's nice. >> Okay, so 20% of this you wrote yourself. Did you steer the AI or did you jump in and say, "No, no, no, no.

**[6:24](https://www.youtube.com/watch?v=la02mLeX0Is&t=384s)** I'm going to do this part." >> There were so many parts where I actually had to stop it or I was just like, "This button is terrible. This link should go here. Some of these checkboxes aren't doing what I did." And so that That's where I would say, "Okay, I'm going to take care of this." And then I would say, "Fix this." >> So faster for you to go in and manually fix than steer the AI? >> Yeah, it was a lot of human steering, human ideation because I don't think any AI would say you should make a pretty engineer CSS. >> the thinking trace to watch it what it was doing or just Were you watching the thinking trace to see what it was doing or did you just look at the And then you would stop it or what? >> having it go side by side. So I do have the GitHub Copilot app where I would do some things, but then usually I like using the side chat so that way I can see what it's doing and have a bit more control. >> Do you think that we, Mark and I, who

**[7:13](https://www.youtube.com/watch?v=la02mLeX0Is&t=433s)** we know CSS like I know that if you say, you know, bang important, it means it's CSS but you really mean it. >> I I didn't know that. >> You didn't know about important? Yeah, it's one of those things that you're never supposed to do in CSS, but whenever anything doesn't work, you just say "No seriously." >> happens? >> You override everything. The CSS is supposed to cascade correctly, but if you say, "No, I'm more important than all of you other rules," then important Have Do you have any importance in here? >> I'm so sorry. >> do any bang important? Do you ever break any rules? >> No. >> No, she she's >> believe in those. >> She's a purist. Show me the part that you are the least proud of. >> The part that I'm proud of? Yeah, of course. >> least proud of. The part that you think is cursed. >> Oh, the part that I think the whole thing is, to be clear, [laughter] no one should do this. >> I mean, this right here is pretty bad. >> This is terrible. So, this is this is a

**[8:01](https://www.youtube.com/watch?v=la02mLeX0Is&t=481s)** very like nitty-gritty behind the scenes. I limited it to 12. You you can't add more more than 12 queries into one thing because >> Well, you could copy paste that line 63 and you could do 13. That would be truly cursed though. >> Here we go. We're going to add You are controlling your own way to >> You're going to type it yourself? >> I do know how to type, believe it or not. It does not want me to do that. It's starting to do display none. There we go. >> Look at that. >> Yeah. >> We've now we successfully extended this application. >> It it does now. We have added a feature. >> This is mostly mine now. I'm involved. >> [laughter] >> Okay, I'll add you as a contributor. I'll add a thanks in the readme. >> Okay, and which part are you the most proud of? Which part Show me something you wrote yourself. >> Ordering. Let me find it. So, one of the things that I was ideating on

**[8:50](https://www.youtube.com/watch?v=la02mLeX0Is&t=530s)** a bunch was the ascending and descending. And the big fun debate, and I need to find it cuz I admit I did some cleaning up, was ordering things with flexbox. Do you guys know flexbox? I know you said you know important, but flexbox is important too. >> the maximum number of nested tables you can have in Netscape 4.0 is 32. >> Great. >> So, I do not know what flexbox >> That is different. So, flexbox allows you to rearrange things on a page and center things, put things at the front or back or anything. For ordering by ascending and descending, which I don't know where my window just went, that's using flexbox and just using the browser engine in there to flip the order of things. >> Oh, wow. Okay. So, you not only use CSS, but you abused parts of HTML.

**[9:37](https://www.youtube.com/watch?v=la02mLeX0Is&t=577s)** >> that's what I'm saying. It's It's really not something you should do. And that's what's great. >> [laughter] >> Did the AI push back and say really this is a bad idea? >> No, it just said you're absolutely right. I was like, you know, I yeah. [laughter] >> Okay. >> How long did this take you? >> Um When did you message me? You You first messaged [laughter] me about this like >> a week ago. >> Yeah, you told me about this like like week and a half ago or something. So, yeah, I started work right then. >> But like in clock time? >> Clock time? Probably like 2 hours. >> Is 2 hours too long, isn't it? >> Probably. >> [laughter] >> Okay, is this is this slop? Is this AI The thing is with both of the folks, we look at Steve Sanderson, you would need to be an expert to do what Steve did.

**[10:26](https://www.youtube.com/watch?v=la02mLeX0Is&t=626s)** You have to know and love CSS to do what Cassie did. >> Do you think you have to know CSS to create this app? You do? >> I mean, you have to know enough CSS to know that you shouldn't do this. But yeah, you need to know CSS to at least to at least If I were to not know anything, I wouldn't know how to massage it in the right ways to make certain things happen. >> What do you think? I think this is >> It's towards the engineered side of the spectrum. >> AI augmented engineering. And it's like you can't just vibe this. You couldn't one shot this. How many turns were there? >> Yeah, you can't say create a CSS based database engine in the browser that just uses CSS. >> fully like in the tab, there's no back end. It's >> Yeah, but you couldn't prompt that and have it run off and come back and no. >> All right. >> do that. Just vibes, but it's two two or three notches to the right.

**[11:13](https://www.youtube.com/watch?v=la02mLeX0Is&t=673s)** >> Pass vibes. >> Pass vibes. >> Yeah, I agree. >> Fantastic. Cassie Williams, we have an award for you. >> Yay! >> Best vibes. >> [applause] >> Thank you so much. >> appreciate you. Thank you so much. That is cursed. Don't ever show anyone that again. >> It's open source on my GitHub. >> open source on your >> You need to add Scott as a contributor. >> Yeah. Yeah, cuz I have a commit now. >> [laughter] >> All right, that's fantastic. Thank you so much for your hard work. >> for having me. >> Big thanks to our sponsors. We're going to go to a quick break, and we will be right back with more cursed wonderful things that we are going to vibe check.
