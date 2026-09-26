---
id: Xn7gXeNtoZI
title: "Why AGENTS.md Isn't Solving Your Memory Problem"
slug: why-agents-md-isn-t-solving-your-memory-problem
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 9
published_at: 2026-09-25T15:00:28Z
video_id: Xn7gXeNtoZI
url: https://www.youtube.com/watch?v=Xn7gXeNtoZI
youtube_url: https://www.youtube.com/watch?v=Xn7gXeNtoZI
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Why AGENTS.md Isn't Solving Your Memory Problem

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=Xn7gXeNtoZI) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Context engineering has a blind spot: most of what a coding agent learns in a session disappears the moment that session ends, even though you already paid for the thinking that produced it. At AI DevCon London, Davide Eynard and Peter Wilson (Mozilla.ai), Robert Overweg and Brian Douglas (Paper Compute) covered what it actually takes to give an agent a memory worth keeping.

What we cover:
– Why AGENTS.md and CLAUDE.md files don't solve agent memory on their own
– Building a shared knowledge repository so agents stop rediscovering the same fixes
– The difference between knowing which agent acted and knowing why it made sense
– What gets lost when a coding agent deletes sessions after 30 days

Chapters:
00:00:00 - Introduction
00:00:14 - Davide Eynard & Peter Wilson, Mozilla.ai: Stack Overflow for agents
00:00:26 - Why AGENTS.md and CLAUDE.md don't solve memory on their own
00:01:16 - Asking Claude to audit its own memory files
00:02:41 - Robert Overweg: 1,200 research files, no extra retrieval needed
00:04:54 - The diary: recording why a decision made sense, not just who made it
00:07:08 - Brian Douglas, Paper Compute: your agent forgets, and you keep paying
00:08:12 - Turning throwaway sessions into skills and documentation at scale

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Has your own agent ever repeated a mistake it already "learned" from once?

## Transcript

*1,740 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=0s)** Back in June at AI DevCon in London, a lot of people were circling the same frustration. Your agent solves something difficult, and then the session ends and it's gone. And tomorrow it makes the same mistake again. Let's first hear from Davide Eynard and Peter Wilson of Mozilla.ai, who are building something they describe as Stack Overflow for agents. Their story about asking cloud to audit its own memory files is worth the entry fee on its own. folks might say, yeah, but we've got AGENTS.md and CLAUDE.md. We can just add rules and that solves it. Or if you debunk that slightly, then you say, oh, well, we've got memories now as well, so that will solve it. But I've, I've got enjoyed quite a lot of time with you in two seconds. I'll keep that off the side for now. But I guess the problem with that is that one, it's all it's stored locally.

**[0:49](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=49s)** You end up with everything stored in a CLAUDE.md file. I mean, you can have your global one and you have a project one, but all of that stuff then also has to get loaded into the context, which also means that anthropic and friends get to see what's in your context. So you might not want all that stuff getting send up there. So yeah, the memories thing I feel like was intended to kind of like improve on the rules. But sometimes, even with memory, Claude seems a little bit forgetful. So I asked it click this question, which was saying, basically, can you just go and have a little spy at all these memory files you'd been writing and see, like if there's basically duplication across them? And Claude was very happy and obliging and told me I was great and then came back and said, yeah, nothing's the same, basically, because they're not byte identical and they don't have the same file name, so they just must be completely different.

**[1:38](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=98s)** And I was like, are you kind of took me a little bit too literally there, so past it, you know, with a little bit of steering, maybe just check for the intent. And then Claude on the wind did lots of things and then came back and till the obvious that he said, oh, yeah, I've been writing the same memory tons of times in different places and also just ignoring it. So a little bit. Yeah. I feel like this was a little bit of a therapy session. So I will also share some things that happened with me and Claude very quickly, which is to fight this Claude not following the rules that it's been given and just doing what it wants. Sometimes even when you say no to a prompt, doing what it wants, stuff where it remembered things and kept relapsing. And just once when it just told me it was confused. So yeah, it's the good times. Anyway.

**[2:25](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=145s)** So getting back to the topic, I guess CQ, the blog post that we put out about this initially was describing it as Stack Overflow for agents. That was a lot to do with me having a very smooth brain, and it seemed like it made sense. And disclaimer for this slide, it doesn't exactly what guy this, but it just try and paint the picture. But We also heard from Robert Overweg, who's built an organizational memory the hard way nearly 1200 research files, mostly unstructured. He tried vector search and retrieval on top and found he didn't actually need them. Perfect. So here is also, a very good example. So I found this, skill from at least a skill as part of a larger skill pack from. Adios, Marni. Guy from Google. This was for, skill breakdown of larger tasks.

**[3:16](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=196s)** And I thought, okay, this could be really interesting, but here I just asked my agent, like, hey, is this actually interesting for us? And since it understands which skills we have, our code base setup, what we want to do, it's able to analyze. I need to steer it a little bit because I need to say, hey, don't we have surgery starts breakdown already? So developer we work with and then it's like, actually I'll have a better look. And then at the end it's able to say and summarize Adios money skills and nothing you don't already have your task files actually more detailed. I'm like, yay! Also, if you look at the time here, it's five plus eight here and it's six plus eight at the end. So in one minute you analyzed that skill, came to a conclusion, and we can decide that we're not going to put it in the vault. Now I want to show you a couple of things.

**[4:07](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=247s)** That's why I have this checklist here. So I don't forget. So in our vault. I have a lot of research, as you can see here on the left. And that's all rather unstructured. It's almost 1200 files, but it's this setup is able to cope with all of these things without doing additional, additional stuff. We started doing additional things like rack and factors and that kind of stuff, but it's not really needed. In those files I add my to dos also related related notes. Sometimes I create connections myself and like actually this file needs to be connected to that so that we keep it as sort of like a memory hub together. Alex makes a distinction.

**[4:55](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=295s)** I keep coming back to Knowing which agent did something tells you who acted. It doesn't tell you why it made sense at the time. So his agents keep a diary and the commits are the entries But of course identity is just the starting point. It, it it starts the track of attribution. It tells us who acted, but it does not tell us why the action made sense at all at the time it was done. That's where the second primitive comes, the diary. So absolutely opinionated form of building blocks. You could give it lots of name. At some point I needed to give it a name and I think diary fit for to describe the place where the stops being just the, the work and the lesson stop being a throw away artifact.

**[5:45](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=345s)** So I read the home for the for all the the discoveries, all the what the f moment, all the decision making that happened during the work. It's also the first spot where you can also have some sort of access boundary that rotates. For example, you could have your diary shared by your team, the diary that could be purely personal for your style of work preferences, all scope to repository or scoped to a project. It's the first point where you can define those policies. What matters in the end is that if the work or decision matters, you need to land it somewhere before it disappears. So in practice, this is what it could look like. You would have your commit done by the agents.

**[6:37](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=397s)** So here linked to a GitHub application you can see the bot. With a reference to the entry that capture the the procedure, the reasoning behind the work. And then you can already start to do a bit less like guesswork. You can start to go a bit further than just the diff and and the, the commit messages. You can start to have the rationale behind. and to close, Brian Douglas of Paper Compute, with a point about money. Your coding agent keeps your sessions for 30 days and then deletes them. You're paying for all of that thinking and then throwing the transcript away. what I'm what I'm getting at is like, we are now in a place where we're all leveraging AI. We're all here in this conference, like, you didn't pay for a ticket because you were using AI, or if you're not using like

**[7:25](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=445s)** probably sign up today and then catch up and one of the workshops. But Cloud Code stores your sessions, codec searches, sessions on your routine for 30 days after 30 days is deleted. So as I walked through all this like Pokemon navigation of like infrastructure and learning like all those sessions are also on my machine from because they use cloud code as my harness. But the value is all being lost because we're just moving on to the next five hours and like the next window, or the next day, or the next month, we pay the next $200. I guess you paid 180 pound. Is that what the price is that convert that right. But what I'm getting at is like, we're paying for this and we're just renting the tokens and then we get no output from it. So there's a lot of opportunity for us to figure this out. So all the Pokemon turned into what I call super agent. So Super Agent, I thought it would be funny to say that out loud.

**[8:14](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=494s)** Sweeper agent, but it goes through code base in this sweeps through. So I had a bunch of code that I shipped last summer when I was five coding and I never touched ever again. So I've got a lot of the garbage code. What if I went through and like this lint in it and like massively fixed a bunch of stuff? Or what if I ended up like setting up like ten parallel agents to write documentation or create a context like a bunch of spectrum and developing context that that's engineer can figure this out. So that's what Super agent is. And it basically takes V, I separate VMs, which is stereos where I talked about earlier. But then also each VM has a tape session being recorded. So then I have like now ten tape sessions of data that I can now have to one generate skills but also generate documentation, generate context. I'll get to about fine tuning a model. But this is a massive amount of data. And if you're working in enterprise or a company

**[9:02](https://www.youtube.com/watch?v=Xn7gXeNtoZI&t=542s)** and like you're paying for the stuff, you should be extracting value. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
