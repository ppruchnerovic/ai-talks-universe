---
id: 70hmVqBO1gI
title: "The API is the Platform • Shamasis Bhattacharya • GOTO 2025"
slug: the-api-is-the-platform-shamasis-bhattacharya-goto-2025
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Shamasis Bhattacharya"]
channel: "GOTO Conferences"
duration_min: 28
published_at: 2026-04-01T12:01:18Z
video_id: 70hmVqBO1gI
url: https://www.youtube.com/watch?v=70hmVqBO1gI
youtube_url: https://www.youtube.com/watch?v=70hmVqBO1gI
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTO Serverless", "GOTO Serverless Day", "Serverless", "AWS Serverless", "Event-Driven Architecture", "EDA", "AI Workflows", "API", "APIs", "API as a Platform", "Shamasis Bhattacharya"]
topics: []
transcript: true
---

# The API is the Platform • Shamasis Bhattacharya • GOTO 2025

**Shamasis Bhattacharya**

`GOTO Conferences` · `GOTO` · `2026` · `28 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTO Serverless` `#GOTO Serverless Day` `#Serverless` `#AWS Serverless` `#Event-Driven Architecture` `#EDA` `#AI Workflows` `#API` `#APIs` `#API as a Platform` `#Shamasis Bhattacharya`

[Watch the recording](https://www.youtube.com/watch?v=70hmVqBO1gI) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Serverless 2025. #GOTOcon #GOTOserverless

Shamasis Bhattacharya - Fellow at Postman Inc @shamasis.bhattacharya

ORIGINAL TALK TITLE
Thinking Serverless through the API Lens. From Functions to Interfaces — the Product Evolution of Serverless

RESOURCES

ABSTRACT
Serverless promised freedom from infrastructure. What we got was faster delivery and smaller units of compute - but also fragmented interfaces, endless YAML, and an army of devs reinventing CRUD endpoints one Lambda at a time.

Today, the true interface of any serverless system is not the function - it’s the API. And that API isn’t just a contract - it’s the system’s surface.

This talk explores a shift: to build and scale serverless systems, we must stop thinking function-first and start thinking API-first. From design to testing to mocking to versioning, the API is the new infrastructure.

And as AI enters the picture - with autonomous agents calling, composing, and even writing functions - the story shifts again. The future is beyond function-oriented; it’s API-native, AI-forward. [...]

TIMECODES
00:00 Intro
06:41 Serverless
09:07 Reliable messaging service
12:02 We misread the promise and paid the price
16:35 Reality check
20:55 Shift in lens
24:08 Interface-driven serverless
24:54 Future with AI
26:04 Reclaiming the dream
27:54 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Peter Sbarski • Serverless Architectures on AWS • https://amzn.to/3hJzEUM
Michael Stack • Event-Driven Architecture in Golang • https://amzn.to/3G5e8ST
Ashley Peacock • Serverless Apps on Cloudflare • https://amzn.to/3EU7P85
Jeroen Mulder • Multi-Cloud Strategy for Cloud Architects • https://amzn.to/3FdNDOA

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,397 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=70hmVqBO1gI&t=0s)** [Music] Okay. So I guess some introductions are in order. Uh I'm Shamashish. Uh I work as a fellow at Postman. Um I'll come into that detail what fellow means. I've been fortunate enough to be part of Postman which is an API development platform um uh from almost um 2014 I think that's the date when we got started it's been almost 10 years 11 years almost so joined there as a VP of engineering trust me the title means nothing when you are starting and part of a company that's just starting up

**[0:49](https://www.youtube.com/watch?v=70hmVqBO1gI&t=49s)** then moved on to become the chief architect that's an interesting journey lots of domain driven design um and things like that. But you know a friend of mine who has done a lot of things in this world in the world of technology had told me you can plan all you want but when your server is at 99% capacity all rules goes out that window. So after being the chief architect for a while I started heading the research lab at postman. That means we were building new products, new ideas, things that has not been done before like postman flows, like the new protocols that you see every day, gRPC, the things that you're working on and also incubating parts of AI. It was an interesting journey. Um right now though I spent time here um

**[1:40](https://www.youtube.com/watch?v=70hmVqBO1gI&t=100s)** figuring out how do I go about this talk because I was not sure whether to talk about how to do things the right way or to talk about how did I [ __ ] it up. Oops. Can I say the f word in go to Krishna? Uh not quite sure about that, but I'm I'm taking that as an yes. Um so essentially you got to know about me. I need to know a little bit about you out here. All right. So we'll do the cliched show of hands. Um so how many of you are from organizations that call themselves enterprise? I mean, oh, okay. See, you you should ask questions that people can raise

**[2:27](https://www.youtube.com/watch?v=70hmVqBO1gI&t=147s)** hands on, not like, you know, that that makes it fun. How many of you here identify yourself as leaders in product design architecture? Oh, no. You purposely did not raise your hand, right? Because last time I said, "Yeah." All right. So, we have a lot of folks here who get [ __ ] done. Can I say [ __ ] with Goto? Not quite sure, but I'll I'll go with it. Okay. So let's see what am I talking about today. The API is the platform. Can we go to the next slide please? And is this is being rendered? Oh, this is me thinking of serverless through the API lens from functions to interfaces. I I I asked Chad GPT to write the title. U my bad. The EM dash actually gives it away. But not really. I've been writing

**[3:15](https://www.youtube.com/watch?v=70hmVqBO1gI&t=195s)** with EM dash. No, I'm not telling you since when you'll call me old. Um so let's see we have lunch coming up next so I know that uh it will be hard to go through. So the entire talk that I'm going to give today actually revolves around this one single slide. I could have gotten away by just not building any slides having this slide whatsoever. And the main reason why is because in this day and age there is not a single way you can avoid information. You can look up you can Google things up. If you don't know what to Google then you can chat GPT up. Lots of things. What you don't get is personal experiences. So I'm not going to talk to you about

**[4:03](https://www.youtube.com/watch?v=70hmVqBO1gI&t=243s)** how to do things. I'm going to talk to you about my personal journey. I guess where I kind of messed things up, what I learned, how I fixed them. Um, almost like the hype cycle you see here. So, I'm going to explain this graph first. This graph is better than Apple keynote graphs. It has axes for once as a difference. So, on the x-axis you have year. Here we start with 2014. That's 2019. That's as far as my brain can compute. Be beyond that it's all blur. Yaxis is just more more stuff just more of numbers more of things and then we're going to go look at this boring gray line. uh it is called cloud complexity. it tell me trust me it's a name I came up with there's no real significance of this but

**[4:52](https://www.youtube.com/watch?v=70hmVqBO1gI&t=292s)** basically what it means is compared to the number of users we are serving which is 45 million at the moment um almost the world has roughly 55 million developers 50 right Gartner calls it certain 50 and all so 45 million of you love what you have built um because we built Postman from community feedback um And this graph shows how much complex our cloud was compared to the number of users we were serving. Uh it rose up and finally got down settling in. And the lower the number good it is. Trust me that you you will get to know once you okay I'm not going into the PTSD moments. So here now the interesting bit is the white curve out

**[5:41](https://www.youtube.com/watch?v=70hmVqBO1gI&t=341s)** here. What's this white line? This white line is a ratio. It is I tried to kind of convey it as easily as possible. It is the amount of serverless technologies that was present. The footprint of serverless technology compared to the complexity that is here. So a high number doesn't mean there's a lot of serverless. High number means we had a lot of serverless compared to non-serverless technologies powering stuff. That that's that's more or less it. Okay. So, it does look like a hype cycle. Yes, that is in my speaker notes. Um, we are going to go to this part. What I essentially did is

**[6:30](https://www.youtube.com/watch?v=70hmVqBO1gI&t=390s)** marked these areas in red. Just keep this in your mind as I go through the next slides and we should be able to figure out what each timeline means in my life. Okay. So basically I have always believed that the world is shaped as much by science as much by science fiction. We young minds when we started out all the things that we imagined are exactly the one things that we make may come true. I hope medical triorders become true. Any Star Trek fan here? It it will be. Yeah. So we read fantasies when we were young and we didn't believe in okay these are the ways to do things etc. Um

**[7:21](https://www.youtube.com/watch?v=70hmVqBO1gI&t=441s)** and finally we made it happen when we were in a position where we can let's say okay make our own decisions. So um right now in this context when serverless as a as a commodity technology right when it's not in the academic world it is out there you can just use it if you want it has gone through all the beta tests etc was fortunately or let's say however we look at it uh during the same time as we had started postman 2014 am I AWS ninjas, can you tell me 2014 sometime around the same moment when we started and just like any amazing developer when I saw that notification on on Amazon console, I clicked on it

**[8:12](https://www.youtube.com/watch?v=70hmVqBO1gI&t=492s)** and I said, "Yay, it's going to solve a lot of my problems." And yeah, that's when you saw that first line. We had a lot of serverless technologies built into uh how we were powering Postman at very early days. So in fact what's something that a lot of us don't know including early members of post I mean because it was so so early a lot of even postponauts that we call don't know is we actually had a very large system built on top of serverless and we had called it um reliable messaging service. Trust me, it was neither reliable, nor was it the last time we named something

**[8:59](https://www.youtube.com/watch?v=70hmVqBO1gI&t=539s)** reliable messaging service. That's the fun part. So, I'm going to go in and actually get into the nuances of what we built. Don't look at this graph. Don't take a photograph of it. This is useless. It's not supposed to learn from it. But just like everybody says, read between the lines. You should always see between the boxes. What are the lines that are connecting anywhere? Each of these lines, each of them, all of them are lambda functions or some sort of serverless technology powering everything. Oops, I have 15 minutes to go. Okay, I'll go ahead. Okay, so we did all these things. We ensured everything would go ahead and then we figured out um we yeah, we had zero observability. zero

**[9:51](https://www.youtube.com/watch?v=70hmVqBO1gI&t=591s)** observability across hobs. Each part of this it kind of stitched together with event glue and you couldn't mock it, you couldn't test it, you couldn't version it. We just got into a whole mess. And then finally, um, here's the thing. When somebody gets into the concept of you doing something with serverless, you learn a lot. You figure out what to do. And here's the thing. We weren't just adding like edge functions in the front end app, right? just figure out what to do in the edge functions. We were trying to use serverless technologies the right way the right way possible everything the function as a service for system organically from scratch um that's when it clicked the function wasn't the problem the lack of interface thinking was

**[10:39](https://www.youtube.com/watch?v=70hmVqBO1gI&t=639s)** you are seeing me look at this primarily because usually I give this talk from the brighter side of things but this is go um most talks are supposed to be intimate which means I chose let me take the path that I have not taken ever so completely new zero rehearsal but I'll make it work okay so we started asking ourselves a better questions why do we need to solve all these management issues around serverless something Anderson just said as he stepped down ask yourself questions why do you need to do what you need to do so we are postman so we always look and kind of looked at it from an API lens. What if we designed systems like APIs, not like pipelines?

**[11:30](https://www.youtube.com/watch?v=70hmVqBO1gI&t=690s)** I'll come to it soon. On on a side note though, this realization literally changed a lot of things. We went closer to bare metal. We started using containers and powered a lot of our stack using elastic beantock. Most of AWS folks got freaked out that you know you're running multi-billion dollar company on beantock. uh but that actually put us a lot foot forward for the eventual Kubernetes and containerized migration that you have when you are dealing with multiloud a lot of things you would want something that definitely allows you to go through properly. Okay. So we attempted a serverless architecture. We felt it is supposed to be done but we had low success and I think that in hindsight was too ambitious because even

**[12:20](https://www.youtube.com/watch?v=70hmVqBO1gI&t=740s)** today when we Google what is serverless please don't blame me I it read from what all of you typed and put it up there on the internet right so it says cloud cloud execution model serverless is a way you just get rid of infrastructure altogether So young minds learning from imagination and then eventually figuring out how to apply that imagination later. Yeah. And here you go. So I kind of took serverless as a deployment modality instead of an architectural or an organizational construct. So I'm sure it's not new. The same kind of misframing has led to many teams getting into this. We spend a lot of time working with so many, you know, users that are trying to improve their

**[13:08](https://www.youtube.com/watch?v=70hmVqBO1gI&t=788s)** APIs, make things better. APIs are like rabbits ears. You pull it, the entire rabbit's going to come out with it. So the moment we start discussing APIs, we figure out what's what's going on somewhere else. Um so okay that led to it was like if I were to kind of group all serverless usages everything that we want to do to put serverless technologies in I've kind of made one of these chart this kind of puts usage of serverless in two areas. Are we following so far or am I like going too fast and like rambling hard to Okay. All right. So everything that you do with serverless, you can close your eyes and put them in two buckets. One, this is the strategic quadrant.

**[13:58](https://www.youtube.com/watch?v=70hmVqBO1gI&t=838s)** This is where you are actually putting in intentionally leveraged serverless as an infrastructure, right? You are using the benefits of statelessness, cost, the idle, zero idle time cost, which was the original premise of serverless by the way, not that to abstract away infrastructure. Uh the whole thing is that when every technology that you see in the world eventually is coming from somebody who wants to optimize or earn more. So serverless come came because somebody had to figure out how to stop paying money when my server is actually not doing the work. Simple no complexity attached to it. So that's how we know that at the end of the day any system that uses statelessness, zero idle cost, instant scale out, all these things I had to look up by the way or it's hard

**[14:44](https://www.youtube.com/watch?v=70hmVqBO1gI&t=884s)** to remember. Um those were thoughtful areas that gets here your bottom left strategic quadrant. All of you are strategic out here. So that's the quadrant that you put things in. But then here's the interesting thing. That's the top left. Somebody even chewed a part of it. So yeah, it does look like Apple logo in a way, but sorry. Okay, so this is what I call the utility dash cam. This is where all your code that you don't know where to fit, you just put it in one compute and get it out there. An image generator, a web hook somebody created in like 5 years back, who knows? or something is going wrong and you figured out this somebody some one of your colleague who's no longer there with your company anymore built

**[15:33](https://www.youtube.com/watch?v=70hmVqBO1gI&t=933s)** out there put it on a lambda and you don't know what to do about it. These are real life situations. So no matter what that upper left corner even right now still keeps coming back at us time over time over time even in 2025. Um we thought we eliminated it. It it hasn't gone away. You have a really nice architecture out here and then you have this whole pile of junk. I used to call it JBOC that is just because of con convenience or just a bunch of compute. You kind of how you want to do it you can do it. All right. So this I mean today we are not going to focus on this. There are way more smarter people who can focus on this. And that's actually been a story of my life. I think since

**[16:22](https://www.youtube.com/watch?v=70hmVqBO1gI&t=982s)** quite a while I've been only working with people those who are smarter than me. So I'll let them take that. I'm going to take this part and I'm going to talk about this. Let's go to the next slide. Ooh. So we were doing really well. Amazing reliable messaging service. We were figuring it out and that's when you know this is about 2018. We were releasing workspaces or something like that. I don't know. I I'm not quite sure about it, but I remember this is where we couldn't figure out what's going wrong. So the trash can quadrant had compute all over the place. We were chasing down weird bug, a sync state changes and sometimes which which usually failed when somebody joined a postman team. I'm

**[17:10](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1030s)** sure one of you might have faced that bug. You joined the team and something which was supposed to get created did not get created. You can blame it on this particular photograph. So it worked locally. It did work on test but it broke only on production and only on Mondays. Okay. All right. So we were doing amazing with serverless. We are serving millions of users. It was really designed well. But what was going wrong? What the thing that was going wrong had nothing to do with what the promise of serverless is. It was three real challenges. Number one, architectural misfit systems evolving faster than patterns. You just it's one of the toughest thing to stay on top. Second, org change

**[18:00](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1080s)** collisions. You start from a small organization, you become a large organization. Trust me, if anybody hasn't read of Robert Conway, is it Robert Conway, right? Convey's law. Yeah. He says no matter how you want to architect your system, it eventually rests along the path of how people are talking to each other. Build a company which where engineering is headed by marketing versus a company where engineering heads marketing. You will have different architecture. You don't need an architect to design technology most of the time. Just shift people around. You will see the change. Okay. So, uh yeah, thank you for scrolling the speaker note though. So when we are just chasing these situations where we are trying to control um we asked ourself what do we do to solve it

**[18:50](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1130s)** maybe we'll sit down do some eventtor storming we'll do this we read a lot of DDD books we met a lot of DDD people um one really good advantage is when you build something great is you can meet people those who have also built something good so you exchange ideas so metal a lot of people who amazing folks those who wanted to talk about how to do this but it actually triggered something else for us most team in most organization don't question this we did question when our headphone jack was removed we have more complexity with that airpod we trying to connect every day we question it every day we never question why the heck am I spending so much time trying to control something a complexity

**[19:39](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1179s)** that I introduced in the first place. People ask the question that's why we are fine. There was one time I used to write again I'm letting my age come in. Uh I used to write code where I have to write if your processor supports floating point then go this route if it doesn't support floating point this route. You don't have to deal with this because somebody thought that complexity was irrelevant. Somebody thought whatever gave his job security is irrelevant. So simplified it, created abstractions, created interfaces. Um, coming back. So at Postman, this moment triggered something deeper. We began to question serverless from an interface design standpoint. What if the real primitive wasn't function, it was the API. Trust me, if you go to a hard doctor,

**[20:27](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1227s)** he'll always tell you it's a heart problem. No matter what you have, even if you start with an epend. So we are enforcement. Obviously we look at things from the lens of APIs but then you should hear out whether it worked for me or not. So and honestly at that point of time I thought platform organizations has two options either embrace all the overhead that comes with certain kinds of technologies or teach your developers APIs. So moving on we said we're going to do something important. We introduced a simple internal discussion. You know if you build things with mandates not a good idea build something with clarity much better idea. If you manage things not a good idea. If you lead things much better idea. So we introduced to simple internal

**[21:14](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1274s)** discussion. Every lambda must have an API endpoint. Remember I'm talking about that top right trash can quadrant. You can't have APIs for kinesis streams. That's that's not what you're talking about. We're talking about the things that you need to manage. That's a problem. So every lambda must have an API endpoint and every endpoint must live in a postman collection. We are postman again. So we put in a postman collection. Um you can figure out what to do and that's it. That's a simple shift. So when you change you this is a very interesting phenomena. You start with a little change and that actually has cascading effects. This subtle shift from function oriented thinking to interface oriented thinking started I have five minutes to reshape our architecture organic organically. I'm not going to spend time map services

**[22:03](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1323s)** to domains if serverless etc. It this is what leads you to figure out okay what a domain is why should I do it etc. I think you will get hold of this. We will come and share this at some point of time. Okay. H I can go over. Okay. A bit. All right. So, because we mandated this, what happened organically? Certain things became harder and certain things became easier. Another interesting lesson in life. If something is hard, it is hard on purpose. somebody wanted it hard so that you do something else. Okay, so we figured out certain things became harder to reason about why should a compute exist out in the ether? Why should a code just be hosted and be available on

**[22:50](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1370s)** the cloud? We found it definitely harder to reason. But what we found easier to reason was um where do I find it? What do I do with it? How do I call it? How do I improve it? How do I change it? Now whatever you learn, whatever you figured out, however you decide A is wrong, today B is wrong, tomorrow something else is wrong, you can at least deal with it. You can deal with the change. Nothing else. So as a side effect, automatically some lambdas just and like serverless technologies just got retired. People just couldn't find a way to fit it. Guess what happened to all of those? Um they became services. Classic antiattern. If you can take a bunch of lambdas and make it into a service, it shouldn't have been lambda to begin with, right? So because the

**[23:41](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1421s)** moment you start thinking in interfaces, you start seeing what fits and what doesn't. You ask better question. What's the surface? Who consumes it? Who is it versioned for? You start treating serverless as a design problem, not just a deployment trick. Oh, this is nice actually. All right. That's when things began to shift. not just technically but you know more culturally thinking okay what do I do with just don't run things just figure out how to think of interfaces now I tried to write down what does interface driven serverless is I think we'll skip that you can figure out a lot of ways to figure out what it is so then we moved on to tenets of interfaced design this what you see here what I talk here are completely different we

**[24:28](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1468s)** can refer this up but what I'm going to recommend this reading this book called thinking in systems. Read it. Don't try to understand it. Don't even try to remember it. Just the fact that you read it, that's good enough. It will trigger what you need to do when time when the time comes. It's just knowing something that you didn't know earlier. And lunch is becoming restless, literally coming getting in the way. Right? So the next thing that actually came into play that now we know that an interface disbased design is much more easier to reason about. We figured out that agents don't call functions. AI don't doesn't call

**[25:16](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1516s)** function. AI calls API. Because here's the thing. As we try to build more things with AIS and stuff in it, they would need to deal with the three basic things that every human needs to deal with. Discoverability, clear semantics, and modularity. I am sure that's not the construct that you use while thinking serverless, but that's usually the construct that is used when marketing serverless. So that's something that we have to keep in mind. maximal abstraction. And I read it somewhere not read too much about it but yeah so which means API isn't just a contract it is something that you are using to express how you know things will work how you compose things not stitch things together

**[26:05](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1565s)** okay talking a lot about APIs I am really a fan of the last line world is API native and AI forward but uh in the essence of everything that we have in is I have some things to bring home together everything first there is no point trying to build something that you don't understand and there is no point trying to understand everything in this world. So you have one life. You need to try different things. You need to try it fast. When you look at things from the constructs of interfaces, you get something for free which is ability to

**[26:55](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1615s)** change. Don't worry about whether it is right or wrong. Can you make a thing that is changeable and without reading a whole book that says how to make things that are changeable? You just need to live and I know you're going to do amazing things altogether. Any Doctor Who fans will know that's that's one of the science fictions that I grew up. Um, so when you think of interfaces first, not code and composition, what you get out of the box is ability to change. No matter how people say that, hey, this is hard to change, etc. You get the ability for free. And once you have that, you can power it with an architecture of your choice. And whatever you architect today when you have 10 times more user base forget

**[27:42](https://www.youtube.com/watch?v=70hmVqBO1gI&t=1662s)** none of those architecture will work which means your APIs will still still stay there and you can replace your whole stack with something else and you should be golden. >> All right. Thank you very much. [Applause]
