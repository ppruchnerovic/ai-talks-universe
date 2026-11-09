---
id: oixzVKMAXG0
title: "Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway"
slug: please-enough-with-the-sloppy-one-shot-saas-replacements
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Mahmoud Abdelwahab"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-10-12T15:00:19Z
video_id: oixzVKMAXG0
url: https://www.youtube.com/watch?v=oixzVKMAXG0
youtube_url: https://www.youtube.com/watch?v=oixzVKMAXG0
tags: ["AIE NYC 2026", "Livestream Priority 04", "Online Talk"]
topics: ["Coding assistants & agents"]
transcript: true
---

# Please… Enough with the Sloppy, One-Shot SaaS Replacements — Mahmoud Abdelwahab, Railway

**Mahmoud Abdelwahab**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#AIE NYC 2026` `#Livestream Priority 04` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=oixzVKMAXG0) · [Conference site](https://www.ai.engineer/)

## Description

A single internal app now handles Railway's marketing content, email, social posts, media, creator relationships and launch planning. Mahmoud Abdelwahab built it with coding agents, but getting the features to run was only the beginning. The difference between a quick SaaS replacement and a tool his team wants to open every day lives in the details: background saving, responsive interactions, reversible actions and consistent screens. His starting point is a structured codebase with reusable abstractions, so each new feature follows existing patterns instead of inventing another way to do the same work.

Abdelwahab works through the product behaviors he has learned to request explicitly. Autosave should preserve progress without blocking typing; optimistic updates should make suitable actions feel immediate and recover when the operation fails. Undo and archiving give people room to change their minds. URL state makes a filtered view shareable, while infinite scrolling removes repetitive navigation. Referencing an existing page helps the agent reuse the app's interface and data fetching conventions. He then packages recurring design and deployment preferences into agent skills. The final step is a verification loop that opens the running application and exercises the feature from start to finish, because a successful build and passing tests can still leave a broken experience. These are practical lessons from an internal tool, without a claim of measured financial savings.

Speaker info:
- https://www.linkedin.com/in/thisismahmoud/
- https://github.com/m-abdelwahab

Timestamps:
00:00 - Replacing Railway's internal marketing tools
2:32 - Structure and abstractions for consistent features
4:03 - Product polish agents need to be asked for
4:57 - Autosave and collaboration
6:16 - Optimistic updates, undo and archiving
8:45 - URL state and navigation
9:38 - Reference pages and agent skills
11:47 - Verify the running feature from start to finish

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,467 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=oixzVKMAXG0&t=0s)** People have been saying that SAS is dead for a while now. It's not even a hot take at this point. Why pay someone to build and maintain the tools you use when you could just do it yourself? Just ask your agent to do it. And for me, there's one missing piece that rarely gets mentioned. And it's the fact that there's a gap, a big gap between working software that got oneshotted and software I would actually use. Software that sparks joy, that is polished, that feels good. and actually went on a journey to replace a bunch of SAS providers we're using internally at Railway for marketing purposes. And I just built an all-in-one tool that we use. The tool allows us to manage content for the Railway website, change log, blog. We can use it to send emails, post on all of our social platforms at the same time, manage the website's media. There's even a mini CRM so that

**[0:47](https://www.youtube.com/watch?v=oixzVKMAXG0&t=47s)** when we're working with like external creators, we can keep track of that. There is task tracking, launch planning because you know you want to coordinate multiple things and when they'll go out. There's a calendar and at the same time there's like comments, realtime editing and it's all built using agents. I would say I felt the breakthrough when GPT6 came out and all of this is running on railway. Everything just auto deploys. And let me essentially now walk you through the principles I use to actually make sure that when I want to add a feature, it's, you know, actually polished and matches the rest of the app and at the same time the principles that you can pull from and apply when building tools of your own. So instead of doing my talk from my boring office,

**[1:35](https://www.youtube.com/watch?v=oixzVKMAXG0&t=95s)** I decided to switch things up and do it outside. It is absolutely beautiful. Right now I'm in Edinburgh, Scotland, and it's just unreal. Like I'm on a bench outside and this is my view. Definitely a 10 out of 10 bench. Now this type of talk for me feels a little bit different than what I'm used to because I essentially will walk you through the journey of me building our own internal tools and the opinions I've developed. But I also understand that the landscape changes very very quickly. So like anything I say might change completely in like the span of months. Who knows? So I don't know. Consider this my disclaimer. Like but the time of recording is fall 2026. It's October. And yeah. So anyway, with that

**[2:27](https://www.youtube.com/watch?v=oixzVKMAXG0&t=147s)** out of the way, uh let's talk about the first point which is texts don't matter. Now, a lot of people say that it doesn't matter what programming language you use, what framework you use. You can just ask your agent to build you anything and build it is able to do it. And while I agree to some extent, what I found is when you're building a tool that you will actually use, when you give the agent a proper codebase with solid abstractions, what ends up happening is whenever you're working, let's say, on a new feature, you end up with a much more consistent result that is similar to what you've already built before. And the reason is like it's very simple. the agent doesn't need to reinvent the same like wheel every time it tries to add a new feature or it doesn't need to introduce new patterns.

**[3:15](https://www.youtube.com/watch?v=oixzVKMAXG0&t=195s)** It will just essentially follow existing patterns. And when it comes to like what you choose, I feel like it kind of doesn't really matter as long as you have a code base that is properly structured. But like my go-to choice today is one tan stack libraries for anything when building on the web. And if you're building anything content related, I would say definitely go with payload. Solid experience, great abstraction. I went down like a big rabbit hole of like comparing CMSS at some point because I don't believe that I should uh build it from scratch even though I can. But again, who knows? Maybe the future will change. But yeah, and that's kind of like the main first item that I kind of ran into. When you use like a lot of SAS products

**[4:05](https://www.youtube.com/watch?v=oixzVKMAXG0&t=245s)** out there that you actually love that you use every day, when you're a user, there's like a lot of things you don't notice, but when you actually try to like replicate an experience, you quickly find out how much care and thought goes into different flows. So like something as simple as oh I want to be able to send an email or to publish something. You can easily do it by having like a good old you know just like server side rendered app with like forms that you submit. But if you try to build something that is going to be used every day that you will reach for a lot you're like oh it shouldn't feel that way. And there are kind of like a bunch of patterns that I found that agents don't typically do unless you explicitly ask

**[4:54](https://www.youtube.com/watch?v=oixzVKMAXG0&t=294s)** them to. And this is my list. So we'll go through them one by one. And the first one is like autosave. I found that if like let's say I'm building some form of document editor, autosave is kind of like a table stakes feature. So rather than manually clicking save to save things, you just ask it to automatically save progress in the background and to make sure that it's like a non-blocking action so that you can let's say if as you're typing you're able to type and then it just automatically saves. And one other kind of like step further that you could do is to also prevent the browser tab from closing if there are unsafe changes. So it's kind of like this these two layers that kind of

**[5:42](https://www.youtube.com/watch?v=oixzVKMAXG0&t=342s)** guarantee that whatever it is that you're working on is just not going to be lost. Now you can also go a step further and to add like real-time collaboration so that you can have like concurrent edits. And again, my agent didn't struggle at all with adding the feature. It was like, I don't know, asking about it, reviewing how it would work, and then once that's done, >> just 700 million tokens later, I had real time. So, I would say in general, this is the first thing that I find agents just don't do well from a product experience perspective. Another pattern I found that agents completely forget to implement is optimistic updates. So rather than showing your users a bunch of loading spinner whenever they're taking any action, you essentially show them the success state you know

**[6:29](https://www.youtube.com/watch?v=oixzVKMAXG0&t=389s)** optimistically and in the background you're going to sync whatever change they made. Now if the sync or the operation fails for whatever reason you just roll it back and then tell them like oh the operation work. Now of course you shouldn't blindly have optimistic updates for everything. There are some scenarios where you want to show the user a loading spinner and you're going to wait to check that everything worked properly. But in general, having optimistic updates makes the overall experience feel significantly faster, much snappier, and it will just feel much more instant. So pretty sure you can just ask your agent like, "Hey, I would like to implement optimistic updates where it makes sense. Let's come up with a plan." And it will tell you all the areas where it makes sense to do. Again, it's like it's not difficult for the agent to build it. You just need

**[7:19](https://www.youtube.com/watch?v=oixzVKMAXG0&t=439s)** to ask and know exactly what to ask for. Now, an extension of optimistic updates, in my opinion, is giving users the ability to undo certain actions. Now, for example, if you ask your agent to implement the ability to delete records, what it will typically do is it will give you a delete button. You click it, might show a confirmation dialogue, you hit confirm, and then it will actually do the deletion. But a much nicer experience is actually allowing the user to undo that action. So they hit delete, you immediately remove the item they want to delete from the UI, but you tell them like, hey, you have like a couple of seconds where you could change your mind. And if they don't do anything, that means you actually want to delete a thing. Then you actually implement the operation. Otherwise, if they hit undo,

**[8:07](https://www.youtube.com/watch?v=oixzVKMAXG0&t=487s)** you just bring back the change. So it's kind of like you do the operation in the background as well. It's just kind of a delayed action which kind of ties into the next point which is archiving. You should tell your agent you want the ability to archive records and be able to unarchive them because sometimes you want to hide something from the UI completely or let's say from search results and archiving will be the way to do it and you shouldn't force your user to be like well if you don't want to see this you have to delete it. and a much better experience is just the ability to walk out records. So I think it is a pattern that should definitely exist. Another big one for me is URL state. you should ask your agent to persist in the URL whenever it makes sense of course and it's so useful because whenever you have let's say a list of records and you

**[8:55](https://www.youtube.com/watch?v=oixzVKMAXG0&t=535s)** want the ability to filter or sort them and you just have a bunch of like conditions maintaining these things in the URL makes it trivial for you to give them to someone else and then let's say another team member is just going to be able to see exactly what you want them to see now another small detail that agents don't implement out of the box is infinite scroll I don't want to be clicking on load more over and over and over or like a next page button as I scroll I should just get the data I shouldn't need to click next page and then in the end I'll just see that oh I've reached the end it's a very minor thing but also when you use something every day I think it makes a huge difference now another pattern I found that made the output significantly better is telling the agent explicitly to use existing pages as references when

**[9:43](https://www.youtube.com/watch?v=oixzVKMAXG0&t=583s)** it comes to the UI the data fetching and how it works works and how the thing is overall structured and that made it possible for me to essentially define what good looks like once and then just reuse it for more features. Now to be completely honest sometimes even when you tell the agent like hey use page X as a reference sometimes it just doesn't follow it. I don't know if models like get dumber sometimes but sometimes it does happen. But overall, I would say that my success rate is higher whenever I tell the agent to like, well, use an existing page as a reference because you also just end up with a more consistent experience. So like as you're using your app, you're like, oh, this just matches the other part of the app if they both share like the same concept. So like if

**[10:32](https://www.youtube.com/watch?v=oixzVKMAXG0&t=632s)** two parts of the app are essentially lists of records that you can create update and delete and like list well both of these parts should be pretty much identical. This list kind of brings me to my next point which is whenever you have opinions about something they should be packaged as agent skills and then this way your agent whenever it's building something it will actually follow those skills pretty closely. And as I was building all of our internal tooling, I found myself reaching for three Asian skills. Uh two of them are related to design engineering. So one made it easier to have better UI, better typography, better layouts as well as like better error messages in general. And the second one was a set of design engineering skills that made it easier to just have better animations and other things like that. And then last but not

**[11:19](https://www.youtube.com/watch?v=oixzVKMAXG0&t=679s)** least is the railway Asian skills, of course. So like everything that I built for us internally at railway runs on railway of course like everything. So like buckets, databases, the app itself, the real-time server, everything. And for the agent to effectively work with railway and be able to deploy everything, you just give it the Asian skills and it was just able to do it. And yeah, so like once you have all of your Asian skills and everything, in my opinion, the final step and I think this the most important step is verification. So the agents typically whenever you ask it to build something, it's going to be like, okay, I implemented the feature, build passed, test pass, all good, right? But what I found is when you actually try out what happens, you sometimes end up with just like a very

**[12:08](https://www.youtube.com/watch?v=oixzVKMAXG0&t=728s)** broken experience. So once you have like a verification loop in place, it's like a night and day difference because the agent you can literally see it be like, "Okay, I built this thing. I tried it. It failed. I'm going to fix it." And it just keeps going. And then in the end, it's like, "Okay, I fully tested it." And I felt this breakthrough with computer use once it got really, really good. And now everything every time I want to add a new feature I literally just in the end say well you should verify that the feature works end to end and use it by actually running infrastructure and to test things end to end and the agents are very capable of doing this. You just have to tell them and once you have all those pieces I would say you will end up with solid internal tools that you can build

**[12:57](https://www.youtube.com/watch?v=oixzVKMAXG0&t=777s)** quickly that work properly and work in a consistent way. And that's it. This was my list of principles that I use whenever I'm building any internal tools. Hope you found them useful, but more importantly, that you're inspired to build your own internal tools that feel good, that are polished, and spark joy. And I hope that you too can become your company's SAS layer. And with that, thank you so much for watching and I'll see you in the next
