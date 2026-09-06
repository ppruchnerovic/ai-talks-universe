---
id: W7XL_LZgvKI
title: "The Forest & The Desert Are Parallel Universes • Kent Beck • GOTO 2025"
slug: the-forest-the-desert-are-parallel-universes-kent-beck-goto
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Kent Beck"]
channel: "GOTO Conferences"
duration_min: 39
published_at: 2026-02-04T13:00:57Z
video_id: W7XL_LZgvKI
url: https://www.youtube.com/watch?v=W7XL_LZgvKI
youtube_url: https://www.youtube.com/watch?v=W7XL_LZgvKI
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "Kent Beck", "Empirical Design", "Software Design", "Explore", "Expand", "Extract", "3X", "Extreme Programming", "XP", "Addison-Wesley", "Agile Manifesto", "GOTO Copenhagen", "GOTOcph"]
topics: []
transcript: true
---

# The Forest & The Desert Are Parallel Universes • Kent Beck • GOTO 2025

**Kent Beck**

`GOTO Conferences` · `GOTO` · `2026` · `39 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#Kent Beck` `#Empirical Design` `#Software Design` `#Explore` `#Expand` `#Extract` `#3X` `#Extreme Programming` `#XP` `#Addison-Wesley` `#Agile Manifesto` `#GOTO Copenhagen` `#GOTOcph`

[Watch the recording](https://www.youtube.com/watch?v=W7XL_LZgvKI) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Copenhagen 2025. #GOTOcon #GOTOcph

Kent Beck - Software Engineer & Creator of Extreme Programming @KentLBeck

RESOURCES

ABSTRACT
So close and yet so far. We see similar behaviors in The Forest & The Desert, but with opposite meanings. Similar words but opposite meanings. Superficially similar goals but working out at completely different scales.

What is The Forest? What is The Desert? Why are they so different, despite the similarities? And how can we get from crumbs to cake and stay there? [...]

TIMECODES
00:00 Intro
00:16 Opening story: The Forest‑vs‑Desert metaphor
01:16 Why XP still matters in the AI era
04:08 Scarcity vs Abundance: The underlying assumptions
09:16 Purpose‑driven pull vs Pressure‑driven push
14:16 Metrics: Learning tool or hammer of control?
20:51 Dependencies: Collaboration invitation vs blame shield
27:38 Compliance: Enabler of speed or survival tactic?
35:28 Closing call: Choose your universe (forest or desert)
39:03 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Kent Beck • Tidy First? • https://amzn.to/4gscjjK
Kent Beck & Cynthia Andres • Extreme Programming Explained • https://amzn.to/3sBASDG
Kent Beck • Test Driven Development • https://amzn.to/3U4AXLs
Kent Beck, Fowler, John, William, Don & Gamma • Refactoring • https://amzn.to/3SFBYbN
Kent Beck • Implementation Patterns • https://amzn.to/3sBlCGL

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,976 words · source: supa (en, exact timings)*

**[0:11](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=11s)** [applause] um glad to be here and uh I want to start with a a story. My oldest child is uh staff's uh software engineer and Beth was proposing a year or so ago proposing how to do a project to Beth's manager and the manager said that would be a great way to do the project if we were living in a forest but we live in a desert. Bing. And we've been trying to figure out how to explain extreme programming in uh uh modern recent kind of terms. I think

**[1:00](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=60s)** the the juice has been squeezed out of extreme programming and uh finding another way but the concepts are still there. They're still valid. More valid in an AI world. So, how are we going to get this message across? And that phrase, the forest in the desert, really stuck in Beth's head. And the story really struck me when she when she told me that about that. And so I actually had the pleasure of giving a keynote with my own child. And that was a lot of fun because we we we had planned the opening and the closing and we didn't plan any of the

**[1:50](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=110s)** rest of it. But it was perfectly fine because we would just riff off each other and then she'd take the piss out of me and then I'd come back with something and we managed to hit everything that we wanted to hit. And the this metaphor of the forest and the desert seemed to really resonate with folks. So the deeper I've dove into it, the more uh valid I find the the analogy. Since the first days of extreme programming, we've had this communication problem. You say to somebody, well, you need a customer on the team, and someone else says, well, if you have the luxury of a customer on the team, of course, they're going to be successful.

**[2:37](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=157s)** would say luxury um like wouldn't you want to choose to be successful if you could be successful and two people speaking in completely different directions and when I found this or when Beth gave me the the uh this forest and desert analogy I realized it's not it's worse than that it's not just that people are talking and not understanding each other. It's that people are talking and using the same words to mean completely different things. Now, I'm not here to uh to critique the desert or criticize the desert. That was something I would do 20 years ago. People I people wouldn't be writing

**[3:27](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=207s)** tests and I'd be very judgmental and think well I should be writing tests. They should be refactoring. uh they should be planning in smaller increments. They should be integrating continuously. The thing is the desert this this style of development that's based around scarcity is internally consistent. It's not that desert people are doing bad things. They're in a desert world. They believe themselves to be in a desert world and their behavior is adapted to the incentives that they experience. So if there's just not going to be enough time, you have to schedule everybody's time fully because anything

**[4:16](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=256s)** less and you might die. you you have to make very careful plans because after all, if the plan doesn't come to fruition, then we're just all going to die. If the assumption is scarcity, if the assumption is there's not going to be enough to go around and it makes sense to behave in the ways that you see people behave in the desert. If you're in the forest, those same behaviors just it's it's not just that the words mean different things. It's the frame is completely different. So you see desert behavior and you think how could people work that way. So I was thinking about this uh this uh contradiction between the way people talk in the forest and in

**[5:07](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=307s)** the desert and I realized it they're parallel universes. You can take the same words and mean completely different things. So, I'm going to go through the the the heart of the talk is to go through a list of words that have completely different meanings depending on whether you're in a forest or in a desert. But before that, I'm going to try and give you a sense of what I mean by forest and desert. So, Jeanja Grouso was a philosopher who believed that people are basically good. They're bad people. They're good people who make mistakes. But people are basically good. They want to do good jobs. They don't want to rip you off. They're trying to create value for other people.

**[5:56](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=356s)** And in the forest, that's our assumption. Hobbes was a British philosopher who believed that people are basically evil and have to be forced by a central authority to do uh pro-social activities. In Hobb's view, you have to be on your lookout for these bad people and push them to do good kind of against their will. Now, which side of this you come down to is a choice and is going to lead to certain consequences. It doesn't mean one is right and the other is wrong. It's a question of where do you want your base assumptions to

**[6:44](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=404s)** come from? Uh Mary Parker Flet was a a writer of uh industrial what would organization let's call it industrial organization around the turn of the 19th century and flet was focused on what she called power with. She was looking around at the factories at that time and noticed a lot of power over there were there were managers who sought to have power over their reports. And she was focused on trying to find ways that people in charge could have power with the workers, not power over the workers.

**[7:35](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=455s)** At the same time, the one who won primarily, Frederick Winsow Taylor, talked about uh and the chilling little book if you want a a fun read that gives you nightmares. Taylor's book, The Principles of Scientific Management, is Yeah, that's it's a quick read, but thank goodness. His idea was that the the you'd have the smart people design the work and then you'd have the dumb cheap people execute the work and you could manipulate the workers into doing exactly what you told them to do by paying them a little bit more and then giving them very precise instructions

**[8:23](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=503s)** at this is at the same time as Flet was wr writing again coming from a Hobbesian point of Taylor makes a lot of sense coming from a Rouso point of view. Flet makes sense that the two worlds are internally consistent and contradictory. In the uh in the forest world, we lead with purpose. The motivating force is purpose. What are we doing here? what societal goal are we trying to achieve? So it's a pull. It's a attempt to activate the energy latent in the people who are doing the work to try and

**[9:11](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=551s)** achieve something bigger than themselves together which is very different. In the desert we use pressure we Yeah. me sometimes. I'll I'll own that. We use pressure to try to get people to do their work. And again, in a Hobbs Taylor world, pressure makes perfect sense. But pressure makes no sense in the Rouso Flet world. We want to activate the energy that's inside of people already to achieve these shared goals. in the uh in the forest the assumption is change. I even wrote a bro a book

**[10:00](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=600s)** with that in the title. The assumption things are going to change. We're going to embrace that change. We're going to embrace it on every level. The the things that we are trying to achieve will change. The economics of the things we're trying to achieve will change. The skills of the people will change. The organization will change. The marketplace will change. and we're going to accept all of those changes and trying to adapt to them as much as possible. In the desert world, that makes no sense. So, by subtitling the book, Embrace Change, I immediately cut cut the market for the book by I don't know 90%. Smart marketing move. Once again, the assumption in the desert though is

**[10:52](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=652s)** prediction. We want to be able to predict exactly what's going to happen. Now, if you're in the desert, being able to predict is really important. How many kilometers a day are we going to make on our camels decides whether you're going to get to the oasis and live or not. So if the assumption is scarcity, prediction is a reasonable response to that. The uh the social organization in the forest is community. The reason that you do the work well is because you have colleagues that are counting on you. There's an ethics of being one of a team that includes service to your other teammates.

**[11:45](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=705s)** In the desert, the the way you get people going in the same direction is through control. Again, you're afraid if you don't have control, you're not going to survive. So, it's an adaptation to that [snorts] to that world of scarcity. If we don't have control, you won't survive. So, we better lock down everything as much as we possibly can. Now, in a world that actually changes, if I'm over here in the forest world and I realize that things are actually changing, that control looks ridiculous. That looks like what a waste of effort. the prediction that you try and and uh uh institute, the pressure that you put, all of those things look silly from a

**[12:35](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=755s)** forest world. Even though in the desert world, like do being able to make better predictions means that you're more successful in the from the forest. You just think, well, why are you wasting your time doing that? I don't understand what it comes down to for me is there is a world of software development that creates far more value than today's world creates. This is a world in which we're able to eat the cake, the whole cake. We sit up at the table and we get the whole of the value that we can create with software. One of the beauties of working in software is that is scale. Little old me can do one little thing

**[13:25](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=805s)** and have enormous effects on the world. Now, sometimes they're bad effects, but I can create a lot of value as an individual in ways that I couldn't if what I [snorts] was doing was some sort of physical activity. The desert is content with the crumbs. And here's the thing, the crumbs of software are pretty tasty. They're cake crumbs. I mean, they're on the floor. There's not so much of them. But in terms of profitability, over and over again, I visit organizations that are in the desert and very successful, profitable,

**[14:13](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=853s)** sustainable. Nobody's happy. We're not here to be happy, but unhappy is a is a bad sign in my way of thinking. But those crumbs are enough to sustain the desert. So uh on the on the forest side this is what I [clears throat] would describe extreme programming of at English sh sorry [snorts] this is what I would how I would describe extreme programming now this forest style the assumption that people are basically good some people are bad we have to deal with that people make

**[15:00](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=900s)** mistakes we have to deal with that that we're trying to create in community power together to serve a greater purpose than any single individual could serve. That we're going to accept the fact that things are going to change and we expect to eat the whole cake. That's what I'm trying to achieve with that. The desert says, "Ah, that'd be a lot of work." uh I'm in a larger organization or I'm in a marketplace or I'm in a stock exchange that makes desert assumptions and I don't want to go to the effort to push back on those assumptions. So, we're just going to take the desert ideas that we get dumped on us and we're going to

**[15:49](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=949s)** spread them through the whole organization and we're going to be satisfied with the crumbs. That's the distinction I'm I'm making here. Now, for some of those words that mean completely opposite things in the forest in the desert, metrics. Oh, it's been fun. It has been fun following all the metrics conversations that have happened over the last couple of years. Um, I I have a a mailing list. The most popular piece that I've published so far has been was a response to a a prominent consulting firm who shall remain nameless. Uh we were talking about how uh how you could use metrics to improve

**[16:40](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1000s)** the productivity of development by making sure that your senior developers were spending most of their time coding. [sighs] In the forest, metrics are a vehicle for self-awareness and learning and improvement. I, as an individual developer, I'm curious how many minutes a day do I spend coding? Where does my time go? How much am I spend debugging? How much am I spending even on different kinds of development tasks? Uh how much am I spending on design on design on testing on tooling on teaching other people? Fabulous resource for me as a developer to learn about my own craft. The team

**[17:30](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1050s)** together can collect metrics and understand how they're doing. Hey, we tried this experiment. Did things get better? Metrics are fantastic. All of that data is fantastic in the forest in a forest context as a means for learning. That is not how metrics are used in the desert. The uh CEO of Coinbase I think recently had a post about how 50% or 60% do anybody follow this one? I'll just say 60 and it might be 50. 60% of all of their code was AI generated and he wanted to get it to 70%. And heads would roll if it didn't. That

**[18:19](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1099s)** was the implication. That's a very desert thing to say. Metrics being used as a as a hammer to push people into reporting certain kinds of behavior. Notice I didn't say to push people into certain kinds of behavior. I said to push people into reporting certain kinds of behavior. Because if somebody gave me the goal of 70% AI generated code, I would stop programming by hand and I would achieve 100% AI generated code. And the fact that that made me less effective as a programmer is not my problem. But in the desert, metrics are are seen

**[19:09](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1149s)** as a leverage to forced change. I have a I have a whole talk about how uh good, you know, Goodart's law when a metric becomes a goal, it ceases to be a a metric. It's actually Goodart was an optimist. The law is actually way worse than that. As soon as you turn a metric into a goal, you get the opposite outcome of what you were trying to achieve originally. In the forest, you can acknowledge that. And we deal with that by not having visibility of metrics at a higher level than they're collected. So if a team collects metrics, the team can see them, but the director can't see the team's metrics individually. We don't. The last thing you want is to pick out one person whose

**[19:58](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1198s)** numbers are dragging everybody else's average down. That's a desert thing to do. In the forest, you would never do that. So, metrics in the forest are a means for self-awareness and learning. And metrics in the desert are a means of pressure and control with all of the unex unanticipated undesired consequences that brings with it dependencies. Some of the now and one of the limitations of early extreme programming was that we didn't talk about scale. We didn't talk about a thousand programmers and that was a deliberate choice because I'd never run an organization with a

**[20:46](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1246s)** thousand programmers. I didn't know what I wanted to say about that. Dependencies in the forest world. So we have our team, there's your team, we need something from you. Dependencies are an invitation to collaboration in the forest world. Since our assumption is that there's going to be enough time and we have enough skill when there's a dependency between teams, it's an invitation to collaboration. So we need something from your system. We're going to come over and build that with you, some of you, so that our needs get met. That's not the way dependencies

**[21:35](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1295s)** work in the desert. In the desert, dependencies are a convenient excuse for failure. Well, if the security team had gotten their review done, we could have shipped on time. Oh, well, uh, we better put a a queue of requests in front of the security team so that they will work 100% of the time so that they'll get more done. So fewer people will block be blocked on the slowdown of the security team. In the desert, you're delighted if it's somebody else's fault that you didn't achieve what the prediction said you would achieve. Dependency, it's a it's a defense

**[22:22](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1342s)** mechanism. It's a way to avoid being blamed and the consequences that come with that blame as opposed to treating it as a this invitation to collaborate and work together on something. Another word is this word compliance. [snorts] I could just I could hear the intake of breath compliance. Uh we don't like uh in the forest. Uh the team appreciates compliance because they want to serve the users and compliance helps the team serve the users. Compliance also helps the team serve

**[23:11](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1391s)** their colleague their sibling teams um better. So compliance isn't this uh adult supervision wag of the finger variable delay speed bump on the way towards success. Compliance is somebody that you work with actively to make the value to increase the value that you create for your customers. I [snorts] have uh I've been working with a a company in Switzerland, a life insurance company called Square Life for almost 30 years now. And the whole company is built to explore new

**[24:00](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1440s)** insurance products. And so they have a very close relationship with the auditors, not in a like pay them bribes kind of way, but in a but in a they've talked to the auditors. They've asked the auditors, "How can we make your job easier?" The feedback has come back. So the the whole t their engineering, marketing, sales, operations is all tuned to launching products quickly. The the uh record so far is an idea for an insurance product on Friday morning and they sold the first contract on Monday night including

**[24:48](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1488s)** regulatory approval. That's that's a forest relationship with compliance. Now, part of the way they do that is that the terms and conditions uh fit onto one page. The eventual goal is to have the terms and conditions be expressed as a cartoon. Not quite there yet. It's all text, sorry. But it because the terms and conditions are so simple, they're easy for the regulator to evaluate and approve. Imagine that, you know, T's and C's is usually a 100 pages dense legal ease. And of course, the auditor is going to or the regulator is going to have to go through that very carefully because they take their job seriously, which we're happy to have them do. But by simplifying the terms and

**[25:39](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1539s)** conditions, they made it possible to ship out regulated products on a very, very short cycle. Compliance in the desert. Oh yeah, you have to have compliance in the desert because after all, the programmers are going to try and get away with anything they can get away with. If they can claim success, they're going to do it. And and now we're surprised that the that the genie I I call a coding with the AI the genie because it grants your wishes but is not what you wanted. [laughter] Is it any surprise that the genie we see the exact same behavior from the genie? All right, I uh I finished uh what what

**[26:30](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1590s)** you asked me to do and three out of five tests are passing. Well, of course you need compliance in [snorts] an environment like that. In the desert, you're incentivized to cut corners if it causes you if if if it if you can declare success. Okay, we're finished. Well, why don't we introduce a QA department and we'll throw that over to them and then we can claim that we're finished even sooner even though we know we're not. So compliance is a survival strategy in the desert. It makes sense to have that organization there. But from a from a forest perspective, treating compliance as a well, it's okay

**[27:20](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1640s)** if we make mistakes cuz compliance will catch it at the cost of a long delay and a bunch of angry people. And it just seems like why why why are we treating them that way? It makes no sense that. Yeah. So, this is when I have trouble having these conversations, this comes to my mind. Oh, I'm talking from one universe to a completely different one. Not a bad one, just a different one and one I choose not to live in. Oof. Here's [snorts] another word. People hate this word accountability. You know, if you look up accountability

**[28:08](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1688s)** in the dictionary, the dictionary definition is required to render account. I am accountable to you. If I'm required to render account, if you give me $1,000 and you say, "How did you spend that money?" I say, "Well, I spent a hundred on this and 200 on that and 400 on this and then I lost a hundred." Okay, I'm being accountable to you. I'm accounting for the resources that I had to you in the forest. Accountability is an invitation to trust. All right, we have six weeks. Uh when we get to the end of the six weeks, we're going to account for how we spent

**[28:57](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1737s)** every day of that 6 weeks, including all the mistakes, all the backtracking, all the rabbit holes that we went down, um will account for it. And so whoever's providing those resources can trust us with the resources that they provide. in the forest that results in more resources uh being available for development, creating more resources and you build that loop of of sufficiency in the desert. You already know what accountability means. I'm going to hold you accountable for these sales numbers. Means you don't sell this much, you're

**[29:46](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1786s)** fired. That's not accountability by that dictionary definition number one. That's just blame, pressure, trying to force behavior or at least the reports of behavior. You know, salespeople are very creative people and I have a lot of respect for what salespeople do because if you tell them they have to report a certain number, they will find ways to report that number. Wow. It's It's beautiful to watch, but it's a completely different thing in the desert than it is in the forest. The forest, it's an invitation of trust. In the desert, it's a mechanism of control and a way of delivering

**[30:34](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1834s)** pressure. Uh, this is one of my favorite stories from a large software company. I think that's anonymous enough. The story was you never wanted to report your projects. Every every periodically whatever once a month there'd be a project status meeting and every project would have to report their status [snorts] and it was red, yellow, green. And the informal rule was you never wanted to report that your status was green because if your status was green, there were plenty of projects in the red and

**[31:22](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1882s)** they would take engineers away from your team and put them on the projects that were red. So you always wanted to very carefully report that your status was yellow. I don't know. Seems tough. Not sure we're going to make it. We'll put in it. Extra effort. We're going to 996 this puppy. [sighs and gasps] I'm about to start a rant about 996, but I'm going hold off. We're gonna that we we'll put in that extra effort and I think we can scrape out the win if you if you just hang hang with us. I'm not I'm not sure, but I I think we got it. That's the perfect status report in the desert because if you say green,

**[32:13](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1933s)** you lose people and then you really are red. So, let's avoid that. But that dance and of course, you know, I I go I talk to the engineers and they say, "Oh, we have to inflate the estimates." And I go talk to the VP and the VP says, "Of course they inflate the estimates." So I reduced them and [laughter] everybody knows about this never green thing. And so it it's a big show. Apparently people like putting on this sort of play. But from a forest perspective, this just seems ridiculous. was in the in the forest reporting status is you just say what the status is. Uh hey,

**[33:04](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=1984s)** we're behind and we could use some help. We're struggling. Um who who has some time? Uh the last team that I managed managed like officially managed the rule was that nobody could sign up for more than half of what they could accomplish. Every Monday we'd get together we'd ask what's the most important thing for us to work on this week. We'd list the stuff people would sign up and then we'd say is that is that could you get twice as much as that finished? like you know in the desert if somebody asks you that question no I absolutely you know that's one answer the the other answer is of course

**[33:54](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2034s)** I can get twice as much that's a junior engineer answer of course I could get twice as much as that com completed and the seniors are like [clears throat] no absolutely not in the forest you just have the conversation okay everybody's about halfway signed up and so every Friday felt good because they were able to help each other. The team as a whole always got more accomplished than they had signed up for. Everybody had a good relaxing weekend. Come in came in on Monday feeling good like, yeah, we're we're ready to go. What are we going to sign up for next? and uh it drove this positive spiral.

**[34:44](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2084s)** But in the desert, yes, status is a mechanism for prediction, control, pressure, which re leads to all of the downstream broken kind of behaviors that we've been talking about that and that's what leads to the crumbs. All that prediction, all those estimates, all of that stuff takes value out of software development and leaves you with crumbs. Tasty crumbs, but still crumbs. [sighs] So, this is why it's hard to communicate between the forest and the desert. I remember uh gave a keynote in uh Johannesburg, I

**[35:33](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2133s)** think it was. [clears throat] and a guy came up to me at the uh at the end of the keynote just a sec. Uh oh, I ripped the lid off. Is is Yeah. Wow. Okay. He came up to me. This is like 2018, 2019. He said, "Um, you know what? From 2003 to 2005, I was on an extreme programming team, and those were the best three years of my career." I'm I still choke up thinking about it. And I think, why is that the exception?

**[36:22](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2182s)** Why is that the hey, there was one time in my career when I was treated like an adult and felt like what I did mattered? Is who's that good for? It's not good for the investors. It's not good for the business. It's not good for the users. This is certainly not good for the engineers. That's my heart's with the engineers. But seems like nobody's getting their needs met in this system. If you're in the desert and you make these assumptions and you operate in this way and you carry these values forward, it makes sense to continue it because it looks scary. That forest that the luxury of a customer on the team that just looks scary. Can we even do

**[37:12](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2232s)** that? That it isn't even possible. We couldn't possibly integrate 20 times a day. That makes no sense. That would mean I would have to adapt to other people's changes 20 times a day instead of forcing them to adapt to my changes every two weeks. In the forest, that story makes no sense. So, we really do have two different universes, and we can choose which of them we occupy. Now, if you're a little oasis in the middle of a big desert, there's going to be pressure to go back to being the desert. And yeah, it's going to be tough. In the early days of extreme programming, we saw teams

**[38:00](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2280s)** commonly have unprecedented technical results and get fired because I mean you wreck the curve if you don't have any bugs and everybody else is swimming in bug reports. But ah it's still a choice where you're going to live. So, my hope is that we're able to get together in the forest and have this conversation rather than talk past each other, have the kind of culture wars that we've seen.

**[38:48](https://www.youtube.com/watch?v=W7XL_LZgvKI&t=2328s)** Um, the QR code is my uh my mailing list. tidyfirst.substack.com. Uh the book is TidyFirst. I hope they have copies for sale uh back there. And now we have time for some questions. [applause]
