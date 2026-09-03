---
id: GAM6AHm4MZg
title: "Accessibility powered by AI by Ramona Domen"
slug: accessibility-powered-by-ai-by-ramona-domen
conference: devoxx
conference_name: "Devoxx"
category: "General software conferences"
edition: "Devoxx"
year: 2026
speakers: ["Ramona Domen"]
channel: null
duration_min: 16
published_at: 2026-04-08T20:13:12Z
video_id: GAM6AHm4MZg
url: https://www.youtube.com/watch?v=GAM6AHm4MZg
youtube_url: https://www.youtube.com/watch?v=GAM6AHm4MZg
tags: []
topics: ["Science, healthcare & applied ML"]
transcript: true
---

# Accessibility powered by AI by Ramona Domen

**Ramona Domen**

`Devoxx` · `Devoxx` · `2026` · `16 min`

[Watch the recording](https://www.youtube.com/watch?v=GAM6AHm4MZg) · [Conference site](https://devoxx.com/)

## Description

Please subscribe to our YouTube channel @ https://www.youtube.com/@DevoxxForever

AI has taken the tech world by storm, but have you ever considered its transformative impact on digital accessibility? Join us as we explore the dynamic world of AI-driven accessibility, unveiling real-world applications and revealing how renowned AI model GPT-3 and Github Copilot can be harnessed to enhance accessibility in your own applications.

In this talk I will cover a quick overview of permanent, temporary disabilities and age restriction you need to keep in mind when coding accessible application. I will demonstrate how you can use AI to make your code more accessible.

The main take-away will be: AI won't automatically produce accessible code, but if you choose your words wisely and ask for it, you will get it.

## Transcript

*2,290 words · source: supa (nl, exact timings)*

**[0:01](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=1s)** [muziek] Hello everyone. We are nearing the end of the day. I think for most of you the drinks are calling, the snacks, but you have a few talks left and one of them is mine. I'm very happy that you're here. Can I just gauge my audience a little bit? Who you identifies as a frontend engineer? I see hands. Ja, of you full stack. some more and pure backend Java developers also some I'm very proud that you're here. I'm excited. Bu this reads very much front end of course but the concepts that I'm going to talk about can also be applied to other nonfunctionals basically. So AI hot topic accessibility maybe for this

**[0:50](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=50s)** audience a little bit less of a hot topic but still we have some new law so it's a hot topic ehm and this little presentation was ehm inspired by the following ehm how do you say it post that somebody did and you don't have to read it all but if you would read it il such stupid word to generative UI and this was by Jacob Nielson and I don't know if any of you know him but he is also called the king of usability so if somebody like this says something this

**[1:40](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=100s)** controversial I would say it really gets a lot of people talking and most people disagreed with him but he wrote this in 2024 we are now in 2026 so a lot of stuff has happened. Well, I've been talking about what inspired this talk and who inspired this talk but maybe for some of you you don't know who I am. So I'm Ramona, welcome. I'm a software engineer Microsoft MVP and I talk a lot about inclusivity and accessibility in tech. And I also like to develop in agile environments, but that's beside the point. Before I dive into the actual AI usability part, I would also like to show you a little bit of impact. So when we're talking about accessibility, what

**[2:27](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=147s)** does that mean? and it can mean a lot of different things to a lot of different people but basically this little image is oftentimes used to really explain how eh people with disabilities can be categorized. So when you think about developing software and you want to develop it for a large amount of people, you want to ideally develop it for everybody so everybody can use it. Ehm this picture paints a little bit of a scene. So you have three categories permanent, temporary and situational disabilities eh and then all different kind of categories. So for example, if we look at the first one touch, if somebody is born without a second arm and only has one, it's very obvious that

**[3:18](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=198s)** he, she or they will have some trouble eh operating a keyboard and a mouse, for example, if they're navigating the web. Ehm they might also have issues when they have to use the cellphones nowaday which are so big that your thumb will not reach the full screen. If you use it with one hand then you might have to use another one. Right? When you're a new parent and I've experienced this first hand and you have a baby on your arm and you really have to, you know, order the diapers online because you can't really go to the store right now. Eh, you are recovering, your baby is recovering and you can't manage to do that with one arm. That's very frustrating. And you can go through a whole list of different eh categories like hearing, speech, seeing. But the

**[4:08](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=248s)** base you have to remind yourself of is that there are different categories and the people in the temporary and the situational ehm divisions they are the worst adapted to using technology that's not inclusive buse they haven't lived with it. Maybe if you have a broken arm you can't use it for eight weeks. not enough time to learn how to navigate modern day technology in that way. Right? Ehm there's another category that hasn't been mentioned here that I always like to mention and that's age restrictions. So [snuift] this is the age ehm division that you can see in the Netherlands male female. Ehm and there

**[4:57](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=297s)** are two numbers you have to keep in mind. people of 45 years and older ehm their vision starts to decline a little bit. So a lot of your colleagues, maybe your parents, maybe even yourself might enter this category and you will notice that you start to zoom in in your browser in your IDE maybe go to 120 per 150%. So it's important that if we develop something for over half of the population in the Netherlands that it all fits in the screen while you zoom right. Ehm second line that you can take is [snuift] 65 and over. Buuse people of 65 and over

**[5:46](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=346s)** they even have worst vision but also their hearing starts decline and their cognitive function starts to decline naturally. Meaning if you develop software where you know your core demographic is somewhat older. For example, I for now work at a pension company so most people don't think about their pensions in their 20s. You know, it's closer to this age to actually start to interact with it more. Ehm it's imperative that you make applications that have a user experience that's easy, that doesn't stray from the happy flow and to really understand what they're doing. Eh, and this is about 24% of the Dutch population. So, keep it in mind, it's

**[6:35](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=395s)** quite a large number. If I stray away from the front end part for a little bit, so the visual eh layer that present to the users, there is another very important user in your daily work that you have to keep in mind and those are your colleagues because if you write code that looks a little bit like this and your colleague doesn't have a big ass screen at home and has to code in the train, they won't be very happy with you. So remember when you write code, you write it once, it maybe gets [snuift] uh read by your colleagues a 100 times, right? So for your Java engineers, don't be offended by this, but I love this meme. Keep it at fish. Don't abstract it too

**[7:24](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=444s)** much. Don't make it more complicated that it has to be. Eh only start complicating stuff and make it more generic when you need it to become more generic. Right? accessibility thingsabilers [snuift] accessibility purely we about AI eh and when I started doing stuff with AI I started vibe coding like everyone right ehm I really understand what AI was, what it did under the hood. I just thought I throw something in, magic happens,

**[8:12](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=492s)** something comes out and it's usable kind of. So, let me just start vibe coding and play with some AI. Eh, and for me, it's very important to use the word play in this because you're not seriously developing. You're not thinking straight. you're just testing out what does this AI do for me and does it make me feel like I'm already obsolete in the workforce? Can it actually replace me? And in the beginning days my conclusion was no this is never gna replace me. I do a way better job at this than AI does. Because when I ask the AI, please generate for me a hello world HTML page. This is what I got. And when I develop something, I immediately have certain nonfunctionals in mind and accessibility is one of

**[9:02](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=542s)** them. And if I see this, it gets me really sad. It doesn't tell me which language it has to be for the screen readers. It doesn't have any IDs. It doesn't have any area tags. So I was already thinking, "Oké, I'm good. My job is good." Ehm, but if you give a little bit more flavor to the things that you are ask, for example, this is create a hell world hello world HTML page. If I ask create an accessible hello world HTML page. This is what I end up with which is way better. You see the language targets in English. It gives you eh scalability, it gives you IDs. Ehm so it's already way more structured.

**[9:50](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=590s)** There's a hat, there's a body, etc. So way better. So this is how I looked at AI before. Input, magic, output. And what that magic is, it can be multiple things, right? It can be as easy as a decision tree. Eh, it can be a neural network, it can be an LLM, whatever you wanted to be. Ehm, but what I discovered was that is not just input and output. If you want to use it seriously, you have to take into account something else than just input. And you have to take into account context because AI will not make an application that's accessible or scalable or secure, whatever nonfunctional you want it to

**[10:38](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=638s)** be. [snuift] You have to explicitly tell and encode what you wanted to do. And when you do that, a lot eh better outcome will be delivered to you. So it's a little bit in out. You know, if you just think oké AI is smart, it will it will do the thinking for me. Conclusion is no it will not. So knowing this, let's not play with AI but let's develop with some AI. So I will give you a quick demo because we don't have a lot of time but I do like giving demos. Is this readable for you all? If it's not ra Yes perfect. So ehm quick dirty demo with just HTML little bit of CSS in the styles,

**[11:30](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=690s)** JavaScript where it's needed. [snuift] And when I look at before button, this is what I get. If I give it more instructions, this is what I get. I don't think this is correct. This is wonderful with life demos, right? [snuift] The most important thing I want you to know is what you write is what you get. So what I always do when I start using AI in a project is actually in this case it's GitHub Copilot that I use here with Visual Studio Code. Ehm I always give it some instructions meaning whatever I ask it to do it will take these copilotins.m file and it will take what I write down

**[12:19](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=739s)** here. So for example I say oké follow the accessibility guidelines use semantic HTML it must be keyboard accessible I have to have visual focus for the people that are you know needing a little bit of assistance in the visual department ehm and this really helps to eh keep your asks in the files simple. So I can now ask give me a hello world page and it will still be accessible. and follow what I wrote down here. Sounds maybe a little bit too good to be true because it is. In theory, this is what happens, right? AI listens to what you ask. It takes the instructions that youve written and it gives you some

**[13:06](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=786s)** output. Ehm, it kind of does and sometimes it doesn't. So, it's a little bit flaky. It listens as well as it can because you have to understand AI. It's a language model. It doesn't necessarily understand what you're asking. It's making a mathematical magical ehm calculation in that big black box and it gives you something that makes sense to it. So if you use this, it can be a great tool if you know what you are doing because you always have to be a little bit of a detective and check that whether what you are getting is actually following the instructions because sometimes it does it a little bit fully or not at all and it can be a little bit flaky. [snuift]

**[13:55](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=835s)** The second way I like to use AI within Visual Studio specifically with Gitup Copilot is if I try to learn something new and then I don't just start typing comments and let it produce code but then I start using the chat functionality eh and in a chat functionality I could for example type eh make a page accessible for my grandmother of 80 years. Right? So ehm when I use the chat functionality it not just does what it what I asked but it also explains the steps that it's taking ehm and also references the references that it's using. So it can also be a great learning tool if you want to eh use it on a junior in your team if you want to

**[14:45](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=885s)** get better at a particular skill a particular nonfunctional to really get you started. And in that way it makes more sense to use the chat functionality to understand the thinking behind it and check if that's actually valid ehm than letting it produce code by itself. So quick and dirty demo that is not fully functional but that's what you get with demos right? Ehm and I want to send you home with this last slide which is AI doesn't care about accessibility or any other know functional that you want to put in place with accessibility unless you make it care. So make sure that you give them the context that it's that it needs. So give AI the context

**[15:34](https://www.youtube.com/watch?v=GAM6AHm4MZg&t=934s)** that is needed for you to actually create great software. So it's still a partnership. We are not fully ehm out of work yet. Thank you very much and hope to see you around during the drinks. [applaus]
