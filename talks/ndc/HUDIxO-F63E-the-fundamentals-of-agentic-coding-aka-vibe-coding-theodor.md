---
id: HUDIxO-F63E
title: "The fundamentals of Agentic Coding (AKA Vibe Coding) - Theodor René Carlsen - NDC Copenhagen 2026"
slug: the-fundamentals-of-agentic-coding-aka-vibe-coding-theodor
conference: ndc
conference_name: "NDC Conferences"
category: "General software conferences"
edition: "NDC"
year: 2026
speakers: ["Theodor René Carlsen"]
channel: null
duration_min: 16
published_at: 2026-08-12T06:38:25Z
video_id: HUDIxO-F63E
url: https://www.youtube.com/watch?v=HUDIxO-F63E
youtube_url: https://www.youtube.com/watch?v=HUDIxO-F63E
tags: ["AI", "Vibe Coding", "Stack Overflow", "Coding", "ChatGPT", "NDC", "Conferences", "2026", "Live", "Fun", "Copenhagen", "Denmark", "Theodor René Carlsen"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# The fundamentals of Agentic Coding (AKA Vibe Coding) - Theodor René Carlsen - NDC Copenhagen 2026

**Theodor René Carlsen**

`NDC Conferences` · `NDC` · `2026` · `16 min`

`#AI` `#Vibe Coding` `#Stack Overflow` `#Coding` `#ChatGPT` `#NDC` `#Conferences` `#2026` `#Live` `#Fun` `#Copenhagen` `#Denmark` `#Theodor René Carlsen`

[Watch the recording](https://www.youtube.com/watch?v=HUDIxO-F63E) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Copenhagen in Copenhagen, Denmark. #ndccopenhagen #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/         @NDC

Follow our Social Media!

#ai

AI, whether we like it or not, has fundamentally changed the ways we work with code. In the beginning, many swapped out Stack Overflow for ChatGPT, moved from editing code to autocompleting with tools like Copilot, but now we are seeing more tools that that can write large parts of the solution for you.

Most people will relate to the feeling that “vibe coding” or “agentic coding” is a moving target, where both the models and the tools evolve at near-exponential speed. In this talk, I aim to reduce the sense of FOMO many might get when they hear people using these tools to write and refactor large parts of their codebase for them. Whether that FOMO comes from LinkedIn, X or your boss thats fully convinced that vibe coding is the future, we will try to stay grounded when meeting this new technology.

We will cover the basics so that you can actually understand what these tools are about: what they can and what they cannot do, what is mostly hype and what is actually worth checking out. And yes, we will also try to define the term "agentic coding" .

## Transcript

*2,536 words · source: supa (en, exact timings)*

**[0:09](https://www.youtube.com/watch?v=HUDIxO-F63E&t=9s)** Agentic coding uh agents MCPS cloud code cloud code uh cloud mythos uh agents MD uh cloud MD there's so many words in this ecosystem by now um there's a lot and you're sort of expected to know what all these words mean like harnesses and context engineering. Uh that didn't even mean anything like a couple of years ago. And what I felt set my timer here what I felt personally and also with my colleagues is that it's it's daunting getting started. It feels so so complex even beginning, but you feel you really have to get started or you're you're not going to make it. You have this uh fear of missing out and

**[0:57](https://www.youtube.com/watch?v=HUDIxO-F63E&t=57s)** you'll be left behind. But the intention of my talk is you're not behind. Like LinkedIn will tell you that you're behind. Your new boss with the cloud code uh subscription max whatever they will tell you that you're behind and it will change like it has changed. They have been pushing the same agenda for like years that you have to like stay on top and run 10,000 sub agents. But you really don't have to be on top of it that much because the ecosystem still moves. And as I said, it's changed from like a year ago to like a year from now. It will be different. But I do still feel that there are some fundamentals that are worth sort of learning and remembering when you're

**[1:44](https://www.youtube.com/watch?v=HUDIxO-F63E&t=104s)** getting into this so that it's not as complex as this might seem. So let's build a baseline. AI coding tools are are three things three important things you have the models and those are the most important of the three those are like 95% of everything that you can put all you want around it but if the models doesn't work the way you want to you won't get very far and that's the brain so you have the GPTs from openaii you have the claws from anthropic the geminis and some Chinese ones as well and the suppliers people forget about those as well the the the so-called inference providers people will say that instead so openai and tropic usually hosts their own models but there are other uh competitors that host like a whole wide

**[2:33](https://www.youtube.com/watch?v=HUDIxO-F63E&t=153s)** variety of models and you can also run it locally which can be important in the future and then there's harnesses so if there's if there's one word that I want you to to learn from this talk and take away from it is harnesses because they let the models actually do something um you know models are just text in text out but how do they act so a harness is like called code which I'll be sort of using generally because I think most people are familiar with that uh codeex uh agents in VS code open code etc and you can mix and match these at least in theory you could have the GPT 5.5 because that's your favorite model that works really well for you your place of work has a like a GitHub enterprise

**[3:22](https://www.youtube.com/watch?v=HUDIxO-F63E&t=202s)** contract. So you choose that or you have to choose that and you prefer that your client and tools being done on your computer is uh open source. So you can sort of hack it and introspect what's actually happening. So you use something yeah open source like like u not code but like open code. and an agent. When people talk about agents, it's mostly the model and the harness. And it has two important things. There's a system prompt. Uh that's like the initial text that's being sent to the model uh about like, hey, you're close code. Uh you're from Anthropic and you're the best developer in the world. If that helps anything, I'm not sure really. And it's it's configurable.

**[4:11](https://www.youtube.com/watch?v=HUDIxO-F63E&t=251s)** Maybe you want to write something else. you can usually just append to it. Uh like with cloud code, you can't change it. They're they're trying to not let you even read it. You also have tools because when I started trying out these AI assisted coding tools um I didn't understand what tools were and things get really fluffy when people talk about uh AI and they also make up new words like anthropic reason workflows like what what hell is that even is that? So the the the set of tools it gives the agent uh that it can read files, it can run terminal commands, uh it can fetch from the web. Um so let's look at something concrete. Uh and by concrete, I've chosen just the OpenAI JavaScript SDK and we're we're

**[5:02](https://www.youtube.com/watch?v=HUDIxO-F63E&t=302s)** declaring a tool. We're declaring a a function that can read files. It has like a description. It tells [snorts] uh what the kind of parameters but if you look at it there's nowhere it says what the actual implementation is uh and you will see it will be a recurring theme in this talk and other things they will look at it's just text so you send this off to your model let me see if I can scroll oh no don't go back what's in package JSON uh and you register the the tools at the bottom So you send that with your call like hey yo these are the tools that you have and then the models will read that file or will it it will just sort of return like an intention. So the models as a part of

**[5:52](https://www.youtube.com/watch?v=HUDIxO-F63E&t=352s)** their training have um learned to be really really good at making tool calls. Well they don't have any ability to actually do the calls. They are just text uh machines. So they give an intention and then your harness, your cloud code will do something with it. Most likely it will read the file or it will nuke the moon like you have no idea but hopefully it will read the file. So it reads the file and then the output of that gets fed back into the model. And that's important because the feedback loop changes. the loop on how you're working with AI changes and many might boot up cloud code or their agents in VS [snorts] code and just use it like chat GPT you'll ask

**[6:44](https://www.youtube.com/watch?v=HUDIxO-F63E&t=404s)** some questions you'll copy paste some code but that's not like that's not the full full power of it because you are then sort of part of very a big part of the loop because you are giving the input and the agent is responding and sort of unfortunately ely and the way we've been going with AI tools that we're giving up some some agency. We're giving up some control over to the agents and that's because they are incredibly smart like annoyingly really really smart. Uh I was really skeptic in the beginning but now I see it's you can't really ignore it. So you can give it tasks quite vague tasks actually can give it a goal. It can explore your codebase, read some files uh and read the output of these files

**[7:31](https://www.youtube.com/watch?v=HUDIxO-F63E&t=451s)** again and act upon that. It can run your tests. Just have it ask for that and runs it tests, it gets it output and it can work on that. So then it's looping by itself and you can I guess sort of control how much you are part of this loop. Some people bring it really far out and have some automatic stuff. uh or you can be much more in the part of it and and and steer it. So now we know the parts. I could have basically stopped the talk now because if you understood that then I feel most things with these uh AI coding tools will be quite easy because most of it is just built on top of that. But there are uh some tips that I can

**[8:22](https://www.youtube.com/watch?v=HUDIxO-F63E&t=502s)** give some fundamental tips uh about how about thinking about it and I'm repeating myself but work in text models trained on text they output text so if there's any problem that you have uh if you can convert it to text in any way then it will be really good. I had this uh issue that I was I was learning a codebase and I was trying to make a sense of it and I really wanted some some diagrams. I I really wanted to see the dependency graph in a diagram and I could like go through the code. I could open like Excaliraw or Figma or some tool like that and drag and drop and like but that felt like it was like a AI smell for me like this doesn't make sense. I want the agent to do this for me. So then I thought well there's lots of markup languages that can create

**[9:10](https://www.youtube.com/watch?v=HUDIxO-F63E&t=550s)** diagrams and then I use that and now I can just generate diagrams on the fly when I'm in my codebase. Another thing is is documentation. So documentation already is text but sometimes it's packed around with a lot of like it's inside very deep inside conflence or it's in like a word file in your shareepoint and your your agent won't sort of reach that without jumping through so many hurdles. So you can keep those documentations in your codebase and then your agent can really easily access them and you will see that suddenly everything is marked down and that's just because it's it's readable by humans and it's super readable by the agents. That's also a common thing. If it's readable and understandable by a human then it's most likely readable and

**[9:58](https://www.youtube.com/watch?v=HUDIxO-F63E&t=598s)** understandable by a a model. So there's context. People would say context engineering is the new thing. But context is also very simple. It's just what sort of text you you push into your model and you can treat the agent like briefing a new colleague. So they know the trade like they know how to work the computer and write code and that sort of stuff but they don't know maybe the domain that you're working in. They might know not know project specific things. So you can give it some hints. You can ask it to explore the code base or maybe there's some files it should start at and then it will gather some itself. And I mentioned it earlier about

**[10:45](https://www.youtube.com/watch?v=HUDIxO-F63E&t=645s)** steering. Um you will hear that about other people talking about AI. They're like steering their agent whatever sort of that means. But when you're seeing that again we have given up our agency. It's running off on its own and you see that it always runs off in the wrong direction. we have to steer it somehow and we can do that with more context text related stuff and you can you can write it down. An example of that is maybe agents MD that you've possibly heard of or or skills. So agents MD is a usually a project specific file that you have that contains something that the model would have never known. Um so very specific to your codebase like you have

**[11:36](https://www.youtube.com/watch?v=HUDIxO-F63E&t=696s)** to run this command before you uh you have to boot up Postgress before you run your tests. Uh maybe some glossery like we have some domain language that's not very common. You shouldn't put stuff like this is how Typescript works or like this is how Postgress works because you have to remember that your new colleague is really really really smart. They're just new sometimes. And people will talk a lot about skills. You'll see that especially on LinkedIn. They will have like oh I just released my thousand skills that will supercharge your agents to the moon. H and I was like wow that sounds really interesting. How how does that work? How do you uh they say oh you just run this command and it installs it in your cloud code like oh what are these skills so interesting and they're also just

**[12:23](https://www.youtube.com/watch?v=HUDIxO-F63E&t=743s)** markdown and I was very very disappointed to learn that there was just markdown again uh uh and that happens all the time um and with it it comes some sort of like maintenance cost as well because both the agents MD uh will be injected into your your prompt um and The skills will also be like it can read some text files when it needs to and that can be relevant for some cases. Maybe you have a very new library that the models aren't caught up to yet or some very specific thing within your domain. Maybe like the Danish tax laws or something like that. But I would recommend getting into this to stay lean and when you see that you're steering too much, you can add some skills.

**[13:13](https://www.youtube.com/watch?v=HUDIxO-F63E&t=793s)** Some people might think that why MCP is just a footnote in this talk because that was one of the big things people were talking uh about when AI came and they are we we've already talked about that before. They're just tools. So, the harness has some tools that are built in. And if you want some other tools, uh, because some harnesses won't let you change what tools you use, not naming names, and you want to add some tools, then that can make sense, but the models are also incredibly wellversed in using just a command line. So, do you need a GitHub MCP to open pull request? Maybe not. Maybe you'll just use the GitHub CLI because it knows

**[14:03](https://www.youtube.com/watch?v=HUDIxO-F63E&t=843s)** that very very well. And now I have like a small digression. I've tried at hiding my my hate for closed code. [laughter] It's not hate. It is my it is what I use. That's because that's what I have available at my work. But I mean and I hope that cloud code is not the future. And with that, I'm just talking about it being like one singular thing that it's that the supplier, the harness, and the model is all one company, and you can't make any changes to let's say the harness, the harness is very locked down, and I don't like that for our ecosystem. U the models, sure, for me, they can be a black box. That's uh that's fine. That's too complex for me. But the harness is something that

**[14:50](https://www.youtube.com/watch?v=HUDIxO-F63E&t=890s)** doesn't have to be a black box. we can still control that part. Again, these are things that are running on your machine and losing that control is something that I'm not happy with. And also keeping things open source will also help the the ecosystem. You now know the fundamentals or maybe you knew it from before but you sort of haven't thought about it in that way. uh it's just text and uh when you're starting or when you're continuing in keep it simple don't try to install every MCP and every skills that you see on the net just see what works for you and most importantly just pick one and get started and have a feel for it yourself thank

**[15:39](https://www.youtube.com/watch?v=HUDIxO-F63E&t=939s)** >> [applause]
