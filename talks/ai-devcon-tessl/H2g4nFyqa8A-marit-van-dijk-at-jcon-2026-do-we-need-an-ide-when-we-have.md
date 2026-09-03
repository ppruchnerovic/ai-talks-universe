---
id: H2g4nFyqa8A
title: "Marit van Dijk at JCON 2026 — do we need an IDE when we have AI coding agents?"
slug: marit-van-dijk-at-jcon-2026-do-we-need-an-ide-when-we-have
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: null
duration_min: 10
published_at: 2026-04-27T22:09:04Z
video_id: H2g4nFyqa8A
url: https://www.youtube.com/watch?v=H2g4nFyqa8A
youtube_url: https://www.youtube.com/watch?v=H2g4nFyqa8A
tags: []
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Marit van Dijk at JCON 2026 — do we need an IDE when we have AI coding agents?

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=H2g4nFyqa8A) · [Conference site](https://tessl.io/devcon/)

## Description

Marit van Dijk (JetBrains) walks through what's actually new in IntelliJ when you plug AI into it, and why reading code is suddenly a more valuable skill than writing it. When half of what you're reading wasn't written by a human, the old rules for code review don't quite apply.

## Transcript

*1,632 words · source: supa (en, exact timings)*

**[0:10](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=10s)** Why is there an arc of AI? >> Hello and welcome back. Uh there is an arc of AI because we are reusing the opening video which we shouldn't but actually thought it's generic >> and it's not. >> We shouldn't do that. But anyway, not AR of AI. I just found a bug. >> Yes. Yes, Mar found a bug and we're going to talk about that. Um, Java Pro AI native dev at not AR of AI but JCON um 2026 uh live um Marit Vand developer advocate at Jet Brains. Yes, >> the producer of Beloved by everybody ID um intellig idea and bunch of other stuff including uh agendic ID is called

**[1:00](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=60s)** >> air >> air um brand new uh kind of working sometimes sometimes not but >> it's early days >> actively actively being developed and not general available yet I'm not sure whether it's like preview or or what the current status is I'm on a different different department. >> Yeah. No, but we're going to talk about the department. We're going to talk about an intellig idea that is very live production ready for the last 15 years or >> 25. Intellig turned 20. Intellig idea turned 25 this year. >> 25 years. Um, and I have a question. >> Okay. >> Why do we need it? I mean, AI does all the code. We don't write code anymore. We don't read any code code anymore. I don't I don't I don't need to

**[1:49](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=109s)** >> Are you sure we don't read code anymore? I mean, from some of the applications out there, I'm fairly certain that people who write them don't actually read the code or try using their applications, but I think I saw a keynote recently where they were saying actually do read the code. Um, and I don't know about you, but I prefer to read the code in my IDE where I can easily navigate and search and use other useful features like the debugger to help me understand not just what's going on when I'm trying to fix a bug to figure out what the actual bug is, but also sometimes to actually just figure out what the code does from, you know, is my understanding from reading the code what the code actually does when I'm running it. So I think that's the point right I mean what especially now

**[2:37](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=157s)** when code is AI generated it's actually even more important >> to understand to be able to easily understand what it does because it's not your code in your own code you have idea where to go and what to look and with the II generated not so much >> exactly it's like code written by someone else but or an amalgamation of many people that you don't even know and I sometimes you can ask like why did you choose to do this or that? Uh but you know that it's also inclined to tell you that you're absolutely right. So that >> even if you do ask hey why did you do this instead of that it might interpret that to be like oh did you want me to do that instead and you're still not getting a straight answer. At least if you're reviewing your teammates's code

**[3:26](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=206s)** then you can ask them hey why did you choose this over that? uh you know maybe they did think about an alternative solution but tried it out and figured out that it was suboptimal for whatever reason that you can then uh talk about with your teammate not in the same way that you can with your AI assistant or agent or whatever >> um >> so it makes it even more important. Yeah, I'm I'm still a very firm believer that no matter how you got the code, whether you, you know, copy pasted it from Stack Overflow, yes, I'm old, or had an agent write it for you, if you push that code, once you commit that code, and especially if you push it to production, it's your responsibility. So, you better make sure that you understand how it works. and um >> and and obviously like a first class ID

**[4:14](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=254s)** helps with that helps exactly with with navigating the code and debugging code and and and this kind of stuff. >> Yeah, I have I have a whole you might as you might know I did a whole talk on reading code that I've done at pretty much any Java conference and other conference that would have me. I will also be doing that talk at Devox Poland later this year in June I think. Um, so you know about how to practice reading code and of course how your IDE can help you. >> Yeah. And and I again I mean that's that that's the big deal, right? Even if we don't write code, we we probably should read code that was written for us. Uh is there something different in terms of how the IDE should work? Um, if our goal is now switch to AI generated code versus human generated code,

**[5:05](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=305s)** >> well, like I said, I think it's still our responsibility to understand how the code works. Um, so I would still navigate the project, run the tests, look at the tests to see whether they're actually doing what they're supposed to. I have also found many many creative ways for people to have test files there that don't actually run anything from you know adding at ignored or at disabled to just not having an at test annotation or the most creative way I've heard is just disable the surefire plugin. So, uh, you know, make sure that you run the test. Make sure that the tests actually fail for whatever reason they're supposed to fail. Otherwise, you still don't know. Um, like I said, run

**[5:53](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=353s)** the code through the debugger to make sure that it does what you think it does. Obviously, work on your observability in production because your users might use your code in ways that you had not anticipated. Um, so that you can see what's going on there. All of these things are are still important no matter who wrote the actual code. >> And speaking about you are not able to ask your colleagues now what does it mean because there is no colleagues. >> No I mean comparing to human colleagues now we have no colleagues. >> Um it would be very useful if our idees actually had the the features of asking the agents about certain uh certain code. So if I can select like a method and ask the agent that wrote it or maybe

**[6:43](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=403s)** even another agent. >> Yeah. So these are actually some of my favorite AI features that we have inside intellig idea. We have our AI assistant um which you can use in the chat. So obviously there you can ask questions which sometimes I do like you know what would be the best pattern or remind me how to do this or whatever. uh but also we have AI features integrated into the IDE you know the I in IDE stands for integrated so uh features like you know write documentation or explain this code are things that I use uh a lot and also we have an additional plug-in which is AI experimental features that Anton demoed in our last what's new video uh that has an insights feature that will actually generate insights on the fly as you're reading the code with like a

**[7:31](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=451s)** small summary of what a method does or whatever. Uh but not like if you write Java doc it can be quite verbose still Java sorry uh the insights are are really brief and and short and I find this very helpful as well. >> Yeah. Yeah. No, that's exactly that right. So so you uh even if the code is not written by you and you're like ah I have like so much code to review now AI can actually help with that. um which which is nice that the question is can we trust those insights that are that are generated >> uh up to a point yes still but you know do you trust the code if you don't trust the insights generated by AI do you trust the code generated by AI >> um so you know use your own judgment

**[8:21](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=501s)** always >> yeah yeah and uh it's also like multimodel right so you can ask questions about code that is written by another model which is also kind of a safety net because they do they do find problems with each other which is very useful. I I especially also like asking it okay so it just wrote me this code okay can you find some problems with your code yes actually the following if you know well no it doesn't know anything but you know um and in air I think we actually have that I I've only touched air very very briefly I should try it out more uh we have the option also to review the code that was just written by an agent you can have multiple agents review each other like you know your teammates but virtual teammates I guess but not as cute as

**[9:10](https://www.youtube.com/watch?v=H2g4nFyqa8A&t=550s)** Tammaguchi. >> Not as cute. Not as cute. Um, but they tend to agree with you a lot. >> You're absolutely right. >> Exactly. Mar, thank you very much. It's been a pleasure. You all stay tuned for more episodes of um Java Pro and the Native Dev interviews at JCON 2026. We are going to be back very very soon. All right, >> that
