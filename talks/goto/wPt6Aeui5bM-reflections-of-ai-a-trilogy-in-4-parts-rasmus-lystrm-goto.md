---
id: wPt6Aeui5bM
title: "Reflections of AI: A Trilogy in 4 Parts • Rasmus Lystrøm • GOTO 2025"
slug: reflections-of-ai-a-trilogy-in-4-parts-rasmus-lystrm-goto
conference: goto
conference_name: "GOTO Conferences"
category: "General software conferences"
edition: "GOTO"
year: 2026
speakers: ["Rasmus Lystrøm"]
channel: "GOTO Conferences"
duration_min: 31
published_at: 2026-05-22T12:01:11Z
video_id: wPt6Aeui5bM
url: https://www.youtube.com/watch?v=wPt6Aeui5bM
youtube_url: https://www.youtube.com/watch?v=wPt6Aeui5bM
tags: ["GOTO", "GOTOcon", "GOTO Conference", "GOTO (Software Conference)", "Videos for Developers", "Computer Science", "Programming", "Software Engineering", "GOTOpia", "Tech", "Software Development", "Tech Channel", "Tech Conference", "Today in Tech", "GOTOcph", "GOTO Copenhagen", "Security", "Cyber Security", "OAuth", "CodeQL", "Code Evolution", "GenAI", "Code Generation", "Neural Networks", "Developer Productivity", "Rasmus Lystroem", "Microsoft", "Microsoft Co-Pilot", "RAG", "Retrieval-Augmented Generation"]
topics: ["Classic ML & data science", "Coding assistants & agents", "RAG, retrieval & knowledge"]
transcript: true
---

# Reflections of AI: A Trilogy in 4 Parts • Rasmus Lystrøm • GOTO 2025

**Rasmus Lystrøm**

`GOTO Conferences` · `GOTO` · `2026` · `31 min`

`#GOTO` `#GOTOcon` `#GOTO Conference` `#GOTO (Software Conference)` `#Videos for Developers` `#Computer Science` `#Programming` `#Software Engineering` `#GOTOpia` `#Tech` `#Software Development` `#Tech Channel` `#Tech Conference` `#Today in Tech` `#GOTOcph` `#GOTO Copenhagen` `#Security` `#Cyber Security` `#OAuth` `#CodeQL` `#Code Evolution` `#GenAI` `#Code Generation` `#Neural Networks` `#Developer Productivity` `#Rasmus Lystroem` `#Microsoft` `#Microsoft Co-Pilot` `#RAG` `#Retrieval-Augmented Generation`

[Watch the recording](https://www.youtube.com/watch?v=wPt6Aeui5bM) · [Conference site](https://gotopia.tech/)

## Description

This presentation was recorded at GOTO Copenhagen 2025. #GOTOcon #GOTOcph

Rasmus Lystrøm - Senior Cloud Solution Architect at Microsoft @ondfisk666

RESOURCES

Links

ABSTRACT
Reflecting on the era of AI, I present my views as "A Trilogy in Four Parts":
• The impact of generative AI adoption
• The [hidden] price of AI adoption
• Useful AI in a world saturated with LLMs
• How to build [valuable AI] solutions

We start with a nod to Douglas Adams and discussion on the latest research showing the dark side of AI but ends on a silver lining on possible uses of AI.

I promise a mix of rants, wakeup calls, and laughs. [...]

TIMECODES
00:00 Intro
01:13 Agenda
02:20 1. The impact of GenAl adoption
09:11 2. The [hidden] price of Al adoption
18:28 3. Useful Al in a world saturated with LLMs
23:33 4. How to build [valuable Al] solutions
27:45 Takeaways
31:03 Outro

Download slides and read the full abstract here:

RECOMMENDED BOOKS
Michael Feathers • AI Assisted Programming • https://leanpub.com/ai-assisted-programming
James Phoenix & Mike Taylor • Prompt Engineering for Generative AI • https://amzn.to/43cFDqO
Phil Winder • Reinforcement Learning • https://amzn.to/3t1S1VZ
Lakshmanan, Görner & Gillard • Practical Machine Learning for Computer Vision • https://amzn.to/3m9HNjP
Leo Porter & Daniel Zingaro • Learn AI-assisted Python Programming • https://amzn.to/3Pv3Hx7

CHANNEL MEMBERSHIP BONUS
Join this channel to get early access to videos & other perks:

Looking for a unique learning experience?
Attend the next GOTO conference near you! Get your ticket at https://gotopia.tech

## Transcript

*4,685 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=12s)** Brilliant. So, hello everyone. A long time ago in a galaxy not so far away, I found myself at a bookstore here in Copenhagen and I stumbled upon a um an interesting subtitle which stuck with me. And the subtitle was a trilogy in four parts and a lot of you will know what that book was and it was this one, The Hitch Guys of the Galaxy. Uh I think the latest editions are now the increasingly inaccurate trilogy of six parts or something. Um but in this I found uh a most profound description of the future or sci-fi and about technology and there was a bunch of AI in in this book as well. Uh there was even the story about Marvin the paranoid

**[1:00](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=60s)** android who after having lived multiple billions of years really hadn't learned a thing and and and Douglas was really scared about technology. So I thought it was an interesting start to this. So so this is going to be reflections of AI a trilogy in four parts and we're going to discuss the impact of of geni adoption hidden price of it useful AI maybe and maybe how to build valuable AI solutions. Um so let's dig into that. First of all uh I need to put in a disclaimer. Um so first of all it's important these days apparently to state that this talk was written and conceived without the use of AI. Um and and also uh whatever I say is my opinions. So they will or will not

**[1:50](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=110s)** coincide with opinions of my past, current and future employers. Um and that's intentional. So it's it's my thing. So if you're not here for an opinion piece, uh go talk to a salesperson. Uh, also I forgot to mention uh because this is an homage to Douglas Adams, this is going to contain exactly 42 slides starting from this one. So you can count. Right. So part one, the impact of generative adoption. So a couple of years ago, chat G TBT was all the rage. as the fastest growing service in internet history and everybody jumped on it and it seems like we have all this FOMO and FUD and now it's a fad and and everyone either

**[2:41](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=161s)** bought into one of the big companies or most of you built company name GPT and that was really bad. Um and and even if you hadn't, most of you have still put company data into the public chat GPG interface. Anyone? Few hands and the rest of you are liars. Right. So now there's a bunch of problems with this and and and one thing that came out that sort of led to us developers diving into this was this study uh which said the impact of gel productivity and it was awesome because it said the treatment group with access to a pair programmer was 55.8% faster than a control group. And you know this is true or believable because it says 55.8. It's a believable statistical number.

**[3:32](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=212s)** Right? If it said 55 or 50 be nah no some number you're throwing out 55.8 or they really measured it. Um so that's one problem. The other problem is it's it's it's a really big number like is is it really that good? And the other big problem apart from this being a very controlled study is this. So it seems like if you pay for the study you can also pay for the results. Now, there's a bunch of other studies around um but hailing from Denmark, I thought it'd be fitting to come up with a Hans Christensen parable. So, I trust you guys are all familiar with this one, right? The emperor's new clothes. So, so in this version of the story, uh the the conmen who sell the clothes are the AI

**[4:20](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=260s)** vendors, right? This is the finest, thinnest veil. It will make you feel so much better and stronger if you just buy it and put it on and it's going to be so perfect and it's going to make everything better. And anyone who can't see it are stupid, right? Which renders you the court of this. You are buying into this crap, right? I I'm that guy. I'm the one that says he's got no clothes on. That's where we're going. So this study came out last year the impact of generative in software developer performance and and blue optimum found not 55.8% but 4% productivity boost and they found that moderate users i.e.

**[5:11](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=311s)** The less you use it, the better it works. And only 1% of AI code committed without significant rework, which you probably recognize, right? You get this gigantic blob and now you have to work on it. But it gets worse. So this is recent University of Copenhagen and Chicago and they they took a study of what is the labor market effect because you might think that using these tools I feel more productive. The key word here is feel right. What happens to an organization and they realized no significant impact on earnings or recorded hours in any occupation. no significant impact. There is no

**[6:01](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=361s)** change. Users report average time savings of 2.8% of work. Which means if you adopt these tools and change the way you work, at best you save 100 seconds an hour. Now, it's going to get just worse from here because now you're going to say, "Yeah, yeah, but that's the old models, right? This was GPT 3.5. That's no longer true." Now we have reasoning models and they're so much smarter, right? So this study figured out that if you pit old models again and and new models against the same class of problems with low complexity tasks, the old models are better because they think less about lesser problems.

**[6:51](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=411s)** medium complexity tasks demonstrating some advantage maybe but taking orders of magnitude longer to come up with a result and for high complexity tasks everything collapses completely right great stuff so and now you're thinking like the yesmen in the room are like yeah yeah yeah but now we have agents I was just in Rob's talk and I learned agents are cool this is the better thing right so The empire has uh an answer to that as well which is this right. So in the in the brief for this it says uh using state-of-the-art models the agent excels at low to medium complexity tasks in wellested code bases from adding

**[7:40](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=460s)** features and fixing bugs to extending tests refactoring code and improving documentation. Right? So if you've done the work and you've toiled forever to remove every single bit of technical debt in your codebase and you've built all the tests and you have minutely described the problem you want the agent to solve, it'll be able to save you 30 minutes of your life. Brilliant stuff, right? because it turns out that writing code was never the productivity problem. That's also what I've been hearing these couple of days. Um, does anybody have an idea what your productivity problem is? So, in in Kent's talk, I'm going to just

**[8:29](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=509s)** continue talking as Okay. Uh, here's a hint. Any ideas now? It's this right. It's your stupid, insane processes. It's your incessant need to hold meetings when there's stuff to be done. That's the problem. And even worse than that, if we go back to the desert, is the problem of lacking trust. It turns out the the the best source of productivity is the trust in the team and the way you work together. It has nothing to do with tools. It has nothing to do with AI. Right? Which leads us to the restaurant or part two, the hidden price of AI adoption. Right?

**[9:18](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=558s)** So we kind of looked at it. Right? So so, so part one, it does not work. So part two, if you still continue to use it. So this is from last week. So Harvard Business Review says AI generated work slob is reduc destroying productivity and they define work slob as AI generated work content that masquerades as good work but lacks the substance of meaningfully advance a given task. Right? So before AI, this was an email from your manager. Right? And now it's even more emails from your manager because it's written by AI to make it worse. And it turns out that 40% of respondents, there's about,200 of them,

**[10:06](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=606s)** report having received work slop within the past month. Anyone remember works lobb right? Yeah, hands are coming up. And when asked how does it feel to receive this? 53% report annoyed. Others are confused or offended. You feeling that? Like they didn't even bother to tell me to my face. They had this machine generate a soft answer instead that I now have to pass to understand what's going on. And approximately half the people we surveyed viewed colleagues who sent this is important for you guys reviewed colleagues who sent workop as less creative, less capable, less reliable than before and you saw them as less trustworthy and less intelligent. This is where we're going. Um, I have a

**[10:57](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=657s)** couple of friends who have really starting to use chat GBT and copilot and stuff and the I will say over the past six months they have become noticeably more stupid. Okay, but it gets worse, right? So, so Git Clear uh came out in January with this study on on code quality and it turns out that if we look at moved code, move code means refactoring. Yeah, you take a piece of code and you move it around in your codebase. It means you're working on the code most likely in order to make the code better. But look at this number, right? It's going down. We are no longer moving code. We're not making the code better. If you look at added, it's it's it's a different story. Churn

**[11:46](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=706s)** is defined as code being added to a codebase and removed within a fortnight. That's a problem. Yeah, you you spent the work on building it, but now you have to remove it. Duplication is on the rise. Like insane. 3,600 commits containing dup code blocks. Andif and you might say well duplication who cares but it turns out that 57% of code changed co-changed i.e written with co-pilot or something like that claude whatever are involved in bugs. I'm pretty sure I mean your rate is not zero but I honestly hope if you wrote written it yourself or hopefully in a mob or a pair that it's way less than

**[12:34](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=754s)** 57%. And that's just code. This one is from last year. So, you know, Clana, it's the people who take your money when you can't afford to buy a vacuum cleaner or something like that, right? Um, and they realized, well, with this AI, I can get rid of all my service workers because I can just have an AI talk to people. And they fired 700 customer service reps in March of 24. And hilariously, in May of 25, they're rehiring them. because it turns out it doesn't work. If you're stealing money from people and they're calling because they can't pay, you probably don't want a robot to handle the case for them. And this is about this they're the

**[13:25](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=805s)** getting stupid again. So the impact of generative on critical thinking turns out the more you use it, the higher confidence in Gen AI is associated with less critical thinking. So the more you use it, the more you're prone to believing in conspiracy theories and so on. Good luck with that because Genai makes everyone a bad architect, a bad designer, a bad journalist illustrator developer and much much worse, minute taker. Like, have you seen these transcripts from AI engines? Here's the results of your of your meeting. I have no use of 10 pages of what we talked about, which is imprecise. like what was the crux of it? So um and with no critical thinking and any skills to validate whether AI

**[14:13](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=853s)** generated content makes any sense. And the problem here is that chat GBT is [ __ ] And [ __ ] here there in lies the problem because you might be thinking it's a liar but it's not that right. It's not a truce say it's not a liar. It's just [ __ ] You have no idea. It cannot validate whether it's saying the truth. You cannot make really validate unless you really know. And if you really know, why did you ask the stupid AI? Yeah. Because we're no longer living in the era of AI. As the emperor says, we're living in the era of the business idiot. We're living in the era where all business thinks that they should build more AI to generate profit. Right? We're not looking at user impact. we're or

**[15:04](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=904s)** what's gonna happen to our customer base. We're we're we're blindly chasing and a hype for the sake of the hype and not for the sake of anyone else. Right? Does anyone remember this one? Anyone? So, this is from The Abyss. Fantastic sci-fi movie. No AI as far as I remember. Um, but uh in the opening credits for it, they had uh there was a line, a quote that stuck with me from when I saw it or noticed it from nature, so it says, "And if you gaze long enough into an abyss, the abyss will gaze back into you." So I'm going to try to paraphrase into the more you use an AI, the more you become one,

**[15:54](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=954s)** right? So what will happen if that's what you do is you will be hallucinating and full of [ __ ] But it gets worse because there's an environmental impact of Gen AI. Maybe some of you have noticed that. So I I dug up some numbers. It turns out that writing a 100word email with AI consumes half a liter of water. 2 liters to make 10 to 50 queries training GBT3 5 million liters of water and 2.9 watt hours needed per search 6 to 10x the Google search it's no longer kind of the case because Google gives

**[16:40](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1000s)** you Gemini without it right I' I've learned if you do search plus profanity it actually does not do the AI right so turn on safe search filter and then search for what I need [ __ ] And then it actually works. It's going to cost you 140 W hours to write that email, which you could have exchanged for charging your big phone seven times. Like, is this really worth it? And training GBG4 consumed 50 gatt hours or the amount of energy consumption for 6,000 US homes. So, it's like a billion Indian homes or something. It's like a lot right? So, what is the solution to this problem? You think? Well, if you ask the

**[17:29](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1049s)** emperor, this is the solution, right? We're just going to generate more power. Let's reopen this one. And for those of you who know, I mean, you probably remember, right? This is the pre-C Chernobyl, right? This is the one that broke before Chernobyl did. And now we're reopening that because we need the power. So, but there is another solution. So, I think what you could do to help, I implore you to turn down the lights, right? Stop taking showers and drink less water because we really, really need all this power for the AI. And if you don't stop drinking water, it will stop working and I will no longer be able to conduct my life. Please. So, if

**[18:17](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1097s)** you can spread the word #savethei on all your social media platforms, I I would really appreciate it. Right, so we go to life, the universe, and everything. Useful AI in a world saturated with LLMs. And hopefully you just saw this, right? So I I put this in because I realized what happens if you give a creative tool to a creative person and maybe something good can happen out of it. I thought that was really I mean maybe not useful but but the point is none of you most likely are artists. So you get this tool that pretends you're an artist. No, but then you give it to a real artist and then maybe something happens that's interesting.

**[19:05](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1145s)** The other thing, and this is falling out of favor, seem to be taken by agents and stuff, um, but I was still still going to present this stuff because, um, I I went to to Reebok's website, um, because I I do CrossFit and Reebok does one of the best CrossFit shoes, I believe, and I said, "Crossfit shoes, size 12." And they're like, "Would you like these DMX ruffle women's lifestyle sneakers?" It's exactly what I wanted, right? So, um, and then I was like, "Okay." Uh, that didn't work. Let's try Adidas. Crossfit shoes, size 12. Uh, would you like black running shoes? Or may possibly maybe a pair of socks. Huh? What does anyone know which keywords had picked up on when it presented the sock? And then you go to Nike and you get

**[19:55](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1195s)** this, right? You get the Nike Metcon 9, which at the point when I took this picture was the most soughtafter CrossFit shoe workout shoe of all time, right? They knew. And if you don't want that one, there's a cheaper workout shoe and another cheaper workout shoe. It figured out exactly what I as a customer needed because they actually way before Chat GBT had implemented a rag model behind this stuff. So, I think there are use cases, but you need to figure them out. Yeah. And there's a bunch of other places where I think AI can be used and we've seen some examples. And I think yesterday in the opening keynote, um the the professor said she said something like um now what do you do with with AI?

**[20:45](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1245s)** I mean real AI, not the large language model thing if you remember. Right? So machine learning is still here. there's still a lot of places where you you might want to dug into this. And and and because um because my wife realized that this is way too negative a talk, she was like, you got to have a silver lining. You got to have something that's a bit positive, otherwise people are just going to leave. But thank you for staying until now. Um but but one one one thing I did find was um in in the Danish capital region uh the the health care system have over the past three years been using machine learning to uh augment doctor's ability to scan for breast cancer. So um and what it has resulted in is uh a lot of positive stuff. So in a sense so there's more

**[21:34](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1294s)** positives found which is mostly good. Yeah. Right. um and more dangerous tumors are discovered earlier mostly good and a reduction in posit false positives and recalls and I think if you are afraid you got cancer and then you're in for a scan and they recall you to say yeah we're not sure we found it can you come back not a nice experience right so so I think there are places where AI can come in and maybe there's a there's like a silver lining here that even if Geni doesn't work, it actually creates a space where real data scientists can come in and and build solutions that are AIdriven, not about language models, but then we can get

**[22:22](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1342s)** funding for it because of all the hype. So maybe there's a good thing there. All right. Now, um you might be thinking, oh, he said that something works, right? So, woo, we got to add AI to all the things and agents to all existing poses. It seems like that's what some people have been touting in this conference and you're like, you've seen this, right? Automate all the things. That's that's that's for the DevOps era, right? And and now it's this, right? Um, and I'm just I'm I'm going to have to warn you. If you believe that adding AI to your existing process makes everything better, know that the paper tiger is insatiable. No matter how many reports you feed it,

**[23:12](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1392s)** no matter how many well-written status messages you send to your manager, they will always ask for more. So the only way to stop this madness is to stop the process. is not to RPA it or AI it. It's to get rid of it. On that happy note, we go to part four. So long and thanks for all the fish. How to build valuable AI solutions or solutions. And the emperor once said that as a business leader you must decide how AI will reshape your business by making extremely difficult tradeoffs in embracing this technology or lots of other things. And also by the way if you fail your job may be the first to be threatened by AI. That's what we've been

**[24:00](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1440s)** hearing right this is from Wednesday. It's not right. There is no change. There's no change in productivity. There's no change in jobs. We are still here. You're also going to be here five years from now. Maybe things are going to be a bit different and some of you have to adapt, but you're not losing a job. Okay. On this thing, we maybe should also focus on some something else. Maybe we should focus on business income uh outcome, sorry, and not technology. Maybe we should stop chasing the tech and actually chase the customer's needs. I have yet to find a customer who is screaming for more AI. I've yet to find a customer who asks you

**[24:51](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1491s)** to replace human interaction with chat bots. Like who of your customers are like, "Oh, it'd be great if there was a slow chatbot who did not understand what I'm doing and it would take me twice as long to get a result if I'm really lucky." And at the same time, you're burning a lot more carbon. I would love that, right? No one has asked you to send them AI generated responses to your inquiries. Maybe what you should be doing, which goes all the way back to the nameless thing with a that we're not going to talk about, is that you should be talking to your users. You should be talking to your customers. Sit next to them. Figure out what it is they need. What's hard? What's difficult? What's boring? What's slow? What takes too long? And maybe if it the AI strategy or the

**[25:44](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1544s)** strategy at all should be driven by the business. Maybe it's time we got rid of the IT department. It made sense in a bygone era when it was separate from the business and now it just hurts both. Maybe it's time that we come together and build solutions not for the business, not with the business, but as the business because the people who built your path may not be the best one suited to build your future alone. I was fortunate enough to ran in run into Simon Wardley uh last year and and he came up with this idea where you have you have three types of people in the organization. You have pioneers. Pioneers are very important people. They

**[26:32](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1592s)** are the people who come up with crazy ideas and and try to to think new stuff and break things, right? Uh but then you also have settlers and settlers are extremely important people because what they do is they look at what the pioneers are doing and when they realize this could be productized, it could become something, they take the product and they stabilize it, write the amount of tests, do the documentation, do the um compliance and bring it to production, right? And then you have town planners who are very important people. And what they do is they look at products who have been in production for a while and are stabilized and they bring them into a more commoditized this is how we run a lot of stuff thing, right? And any one of you could fit into one of the three

**[27:22](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1642s)** or maybe maybe more than one. I certainly would not fit into that one, right? But we need all three types. And what we tend to do is to we ask the same person to be all three types. And maybe that's not the best course of action because we are different people with different capabilities and different interests. The next thing if you really want to get something done, how many of you are working on more than one project? Like that's most of you, right? And if we talk about context switching and all that, it's a dramatic problem because it turns out the best way to fail at inventing something is to make it somebody's part-time job. Do you have that right? you you you're

**[28:10](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1690s)** working on something that's your day job and suddenly someone has been at a go home meeting about AI and they come to you and say you also need to build this thing like when as part of the day job like how you just make it work and because you're trained to say yes you say yes and you keep on doing it and nothing really happens or you depprioritize the other thing because I have yet to find a man if you ask the manager what should I prioritize they're like Huh? Both of them. Both of them are priority one. Like how many of you in your life have ever completed a priority two task? Anyone? Never. A few. After thinking long and hard, it's like, oh yeah, there was that one in 1984. Right.

**[29:00](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1740s)** Right. So on to Dave Farley, who you may have met on this conference. We need to build small things and work that work and get them to production fast and then extend with more stuff. And if we're able to do that, the other very important thing because I' I've talked to customers who are like and you ask them why are you building that? Oh, we think users would want it. Think you you think they would want it? like no AB testing, no no talking to users, no communication. No, we kind of feel this is the right approach. When are you done? Uh we think two years from now. You've been there like great investment like let's invest in I have no idea whether this will succeed. Um but the

**[29:49](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1789s)** plan that the project managers say that they've estimated that it's going to be great. But maybe what you should be doing is this. test in prod or live a lie. You need to bring that solution to your users and figure out how they work it out and then be fast enough to roll it back or measure how many clicks or interactions are there with this new feature and so on. And if you do all that and you actually manage to make a solution which does something which brings customer value, you know what you can do to satisfy the stupid hype? you market it as an AI powered solution built using AI because no one will be able to tell the difference anyway and they don't care.

**[30:37](https://www.youtube.com/watch?v=wPt6Aeui5bM&t=1837s)** They just want the value of it, right? And then remember please that AI is not going to solve all the world's problems even though maybe the politicians and everyone else says or the emperor but building great software that does something useful and works might just help a little bit. I have been Rasprom I thank you for your time.
