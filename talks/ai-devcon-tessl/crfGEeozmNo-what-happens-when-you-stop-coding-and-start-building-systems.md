---
id: crfGEeozmNo
title: "What Happens When You Stop Coding and Start Building Systems"
slug: what-happens-when-you-stop-coding-and-start-building-systems
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-01-04T14:19:04Z
video_id: crfGEeozmNo
url: https://www.youtube.com/watch?v=crfGEeozmNo
youtube_url: https://www.youtube.com/watch?v=crfGEeozmNo
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# What Happens When You Stop Coding and Start Building Systems

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=crfGEeozmNo) · [Conference site](https://tessl.io/devcon/)

## Description

A recent MIT report found that 95% of agentic projects fail, but the reason isn't what you think.

In this episode, we sat down with three experts building at the frontier of AI agent development to understand what separates the 5% who succeed from everyone else and much more.

On the docket:
• Reuven Cohen (Agentic Foundation) on why this AI era needs entirely new development paradigms
• Maor Shlomo (Base44) on how automated guardrails and refactoring help prevent common LLM failure modes
• Maksim Shaposhnikov (Tessl) on why terminal-based agents outperform IDE extensions like Cursor

The conversation drives one point home: AI isn't about replacing developers; it's about making them faster and smarter.

1. Reuven Cohen: https://www.linkedin.com/in/reuvencohen/?originalSubdomain=ca
2. Maor Shlomo: https://www.linkedin.com/in/maor-shlomo-1088b4144/?originalSubdomain=il
3. Maksim Shaposhnikov: https://www.linkedin.com/in/maxshapp/?originalSubdomain=uk
4. Simon Maple: https://www.linkedin.com/in/simonmaple/
5. Tessl: https://www.linkedin.com/company/tesslio/
6. AI Native Dev: https://www.linkedin.com/showcase/ai-native-dev/

## Transcript

*1,634 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=crfGEeozmNo&t=0s)** 95% of agentic projects fail. But the reason for that failure is likely 99% of engineers programmers developers project managers don't know how to actually build aic [music] system. I think this is something that a lot of developers currently don't notice about AI. Like it will implement the task as you told it to, but it's still lacking the hey, let's stop for a second. We need to refactor the code because I find this common layer or whatever. Interactivity is the differentiator factor like when you're using an ID with a extension uh like a store you're always checking what happens and you're just doing this interactively. [music] UI elements like simplifies uh and uh um

**[0:51](https://www.youtube.com/watch?v=crfGEeozmNo&t=51s)** you know like accelerates the on boarding um for you as a developer. It doesn't replace you as a developer. It's just like here on the side exist to help you with achieving like specific tasks like executing uh helping you to write a specific code file or specific unit tests and so on and be very uh helpful in the sense that there is a UI. You don't need to know any commands because there are buttons and uh it's just like a box for you to type the text and execute. Um I think like the cool uh part of the Corsor or Windsurf is that they are giving you this IDE uh with um with lots of UI elements to help you uh on board to using these tools more like proactively and in your everyday use

**[1:39](https://www.youtube.com/watch?v=crfGEeozmNo&t=99s)** case. While for AI agents like with terminal by definition like you don't need like uh buttons right uh like complex things complex things can be done just with a combination of the of the of the of the keys uh or the commands. So terminal is like for more advanced users uh for those who are ready to accelerate even further because they don't need to have have visualization. they are okay just like leaving in the terminal and manipulating all the commands in the terminal because if you're at some point advanced the VH or Nana or whatever editor uh or a git you actually don't need UIs right you can just do and achieve very hard scenarios with terminal directly and it saves you time but again like it's just like a bit harder because it's less

**[2:28](https://www.youtube.com/watch?v=crfGEeozmNo&t=148s)** interactive because it's easier to to lose what happens um and I think the the amount ount of the generated information sometimes may be overwhelming. So it's hard to navigate through the terminal just because there's so many things are happening and it requires some skill to learn how to use it properly. >> Yeah, absolutely. And I think things like cursor for example where you see the the the changes and you can flick from file to file very very easily. You obviously miss that from the from the terminal point of view. But I don't know what it is about you know just being a terminal that actually just makes me feel faster, more productive at the terminal. Um, and of course when you're at the terminal, you get the power of the terminal, right? It's it's tell us a little bit about how you can effectively use the terminal beyond just cloud code. When you build an app in B 44 these

**[3:16](https://www.youtube.com/watch?v=crfGEeozmNo&t=196s)** days, like there's a lot of infrastructure and setup that happens before the LLM even writes code >> that in some ways limits it but not really not in terms of like what it needs to but it's kind like it it those are guard rails that the LLM should keep >> and as long as it keeps that then then it should be fine to some degree. Um so again we automatically create the entire uh uh read update delete kind like the CRUD SDK and and we make it like really good and we implement like rate limits on top of that and things like that that LM wouldn't really care about and when you leverage um I don't know APIs and integrations and so on like we kema

**[4:06](https://www.youtube.com/watch?v=crfGEeozmNo&t=246s)** there's like a lot of things that we implement mented built into the application so that LLM won't kind like be this reward seeking of like I'll do whatever but I'll I'll keep your app exposed and and so on. The other the other thing is yes at some points uh we automatically feedback the LLM whether the user knows about it or not that it needs to refactor something. So for example, uh one of the things that makes LLM confused the most um and people feel that like across the the the VIP coding category is uh when they're saying like hey I asked it to do something it didn't do it it did the opposite it deleted a feature or whatever um is when code files are are getting too long. uh right

**[4:56](https://www.youtube.com/watch?v=crfGEeozmNo&t=296s)** >> right if if like you've implemented so you ask it initially or early on hey implement this page create a to-do list and it did something simple it's like a very simple to-do list up like in any other react and then start layering in features right so the LM does what what you asked it to and and it start adding like uh AI features to write the tasks description and then user management to like assign different teams and boards and whatever and at some point you have like if you're not careful, you might have like this very large code file. >> So, one of the things is like we're running behind the scenes refactoring tests uh to maybe tell the LLM, hey, like you pass the threshold, you should now refactor this file, even if like okay, the user ask you something. First, refactor the file, then implement what

**[5:43](https://www.youtube.com/watch?v=crfGEeozmNo&t=343s)** the user has asked you to. And I think like there's a lot more to do there. But yeah, it's somewhat of like this uh code quality agent that that's keep nudging the LLM at some points if it finds that it's past a threshold of like hey like there's this code here and this code here like do something refactor that >> look at the state of Agentic today. What would you say are kind of the things that are creating that ceiling for for for Agentic today? What are what are the biggest things that causing a Gentic uh development to to fail or at least to to to cause problems to developers trying to use a Gentic development today? the limiting factors of the space right now. And there was an interesting report from MIT a couple weeks ago, I think it was,

**[6:32](https://www.youtube.com/watch?v=crfGEeozmNo&t=392s)** that basically said 95% of agentic projects fail. And it was a a fair a fairly sort of sensational title and and when you when you dig into that a little bit, you there there's two ways to to to think about those types of sort of stats. one, you know, 95% of projects fail, which is probably true, but the reason between for that failure is likely 99% of of engineers programmers developers project managers don't know how to actually build agentic systems and it's a byproduct of a new emerging space. And it and it's so the the limiting factor is the fact that it's really hard to to look beyond the sort of um you know I call it AI washing the agentic washing

**[7:22](https://www.youtube.com/watch?v=crfGEeozmNo&t=442s)** of products and the and the people associated with it to determine you know what the capabilities of the products and the people implementing these products really are. So when you see this sort of high failure rate it speaks to the fact that we're in a new emerging space. And when you go, if you're old enough to have been around at the beginning of the internet, you would have seen the same thing with a lot of the internet projects that corporations took on back in the late 90s. And there was this sort of, you know, this idea that the internet wasn't quite going to cut it for most business type applications. And then they were wrong. It was the fact that we didn't as a industry understand exactly how to build userfriendly internet-based applications. And over time there were models to follow. Amazon's and the eBays and whatnot showed up and we're like okay this is how you create a web-based

**[8:10](https://www.youtube.com/watch?v=crfGEeozmNo&t=490s)** service that people can easily interact with and it's not just recreating software. Same problem 25 years later 30 years later in theics and AI space. There's a tendency for people to build applications the way they've always built them with with human centric models, uh, review cycles, long drawn out sprints, um, and different sort of, you know, traditional tactics that were optimized for a world where we built slowly over time and gradually. Now, we're in a world where we can literally copy anything anywhere at at a moment's notice. and the ability the the quality of the code although important is less important than the momentum that you get in terms of speed and time to market. So when you're looking at companies that are embracing this they're they're

**[8:58](https://www.youtube.com/watch?v=crfGEeozmNo&t=538s)** embracing this in a way that doesn't just replace their developers that that might be a byproduct but it augments them in ways that those developers were never able to do before. So you're empowering them with sort of a kind of superpower to to to create much more effectively and much more quickly which in itself creates a whole variety of secondary problems. But ultimately this is this is the empowerment of developers to to do more with less.
