---
id: PabKgxoegGg
title: "John Groetzinger, Cisco: You Need Smarter Context"
slug: john-groetzinger-cisco-you-need-smarter-context
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-08-26T13:00:22Z
video_id: PabKgxoegGg
url: https://www.youtube.com/watch?v=PabKgxoegGg
youtube_url: https://www.youtube.com/watch?v=PabKgxoegGg
tags: []
transcript: true
---

# John Groetzinger, Cisco: You Need Smarter Context

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=PabKgxoegGg) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Four talks from AI DevCon London 2026 land on the same conclusion: context engineering, not model choice, decides whether an agent gets your work right. There are millions of skills out there now, and almost no way to manage them.

Guy Podjarny (Tessl) opens with the case for treating skills as code, and sketches the stack forming around them — models, tools, context, harnesses, and the factory lines they compose into. James Moss (Tessl), who works on the registry, names the three ways skill sprawl actually fails teams: overlap, drift, and no visibility into whether anything is being used. John Groetzinger (Cisco) argues you don't need a smarter model, you need smarter context, and has moved his engineers onto mid-tier models as their baseline to prove it. Rob Willoughby (Tessl) and Simon Obstbaum (Stanford) put numbers on all of it — 500 skills, 1,000 tasks, 19 permutations of model and harness — and surface the most uncomfortable finding of the conference: 55% of the time, the model followed the skill's instructions even when the skill was never loaded.

What we cover:
– Why skills deserve to be treated as code rather than config
– The layered agent stack: models, tools, context, harnesses, factory lines
– How skill sprawl fails teams: overlap, drift, and zero activation data
– Why smarter context engineering beats a smarter model for real business value
– What 500 skills across 1,000 tasks revealed about instruction following

Chapters:
00:00:00 - Introduction
00:00:14 - Guy Podjarny, Tessl: why skills are the new code
00:01:30 - The layered stack: models, tools, context, harnesses
00:02:09 - James Moss, Tessl: how skill sprawl fails teams
00:03:00 - Drift, and the skills nobody updated
00:03:39 - Activation: no way to tell what's being used
00:04:19 - John Groetzinger, Cisco: smarter context, not a smarter model
00:05:00 - Why he moved his engineers to mid-tier models
00:06:48 - Rob Willoughby & Simon Obstbaum: 500 skills, 1,000 tasks
00:08:47 - The 55% that followed a skill that wasn't loaded

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which failure mode is biting your team hardest — overlap, drift, or activation — and where is your context engineering breaking down? Tell us in the comments.

## Transcript

*1,798 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=PabKgxoegGg&t=0s)** Back in June at AI DevCon in London, we had a lot of great talks about skills. There are now millions of them out there, and the honest conclusion from the stage was that we have built an enormous amount of something we don't yet know how to manage. Let's first hear from Guy Podjarny, CEO and co-founder of Tessl, who lays out why skills deserve to be treated as code, and sketches out the stack forming around them. I am Guy, or Guy. I'm the CEO and founder here at Tessl, as Simon just said, and I'm excited for two days of sharing and learning. And I do love the hallway track. I love the talks on it, but I just love the conversations and the learnings. And I'd love for you to to share some of those learnings. You're here to to collaborate, not just to talk. And indeed, I want to talk to you about sort of why skills, I believe, are the new code. So we

**[0:51](https://www.youtube.com/watch?v=PabKgxoegGg&t=51s)** founded Tessl two plus years ago, and we did it out of the belief that software development is transforming from revolving around code and instructions to revolving around intent. Sorry. Let me try that again. Revolving around code and implementation to revolving around intent and instructions. And I think that's far less controversial today. Two years ago, we believed that there's a new dev paradigm to be had around it, but we didn't know quite what it would look like. And I think today we're starting to see that sort of new development stack come into view, which I find quite exciting. And so we're seeing kind of a bit of a layered software stack. At the bottom are the new primitives, the models that we're all building on. Clearly, they are the new superpower

**[1:39](https://www.youtube.com/watch?v=PabKgxoegGg&t=99s)** that we've received and we're trying to build for those. On top of those are tools, which I'll talk about some more, which help turn models into agents, giving them arms and legs to be able to affect the world and gather information. There's context that guides those models as well. And then increasingly, there is a harness that constrains the model or packages a lot of things together. I'll talk about these three layers in more depth in a section, and then harnesses compose into factory lines that combine them all and create these pipelines and into full-on factories. So we also heard from James Moss, who works on the registry at Tessl. He gets specific about how skills sprawl actually fails teams: building the same skill twice without knowing, skills drifting out of date, and nobody able to tell whether any of them are being used at all. So how does this sprawl manifest

**[2:31](https://www.youtube.com/watch?v=PabKgxoegGg&t=151s)** actually, and impact humans and the agents that we're instructing? So there's a couple of different failure modes that we're seeing. The first one is overlap. So this is where you might have multiple teams all building the same thing in isolation, without realizing. Each team might have built their own version of the skill. It might achieve the same thing. You might have generally the same outcomes, but it's done in a different way, right? And you're having multiple kind of wasted effort there. So that's overlap. Next up we often see drift. So this is where newer skills are shipping. And teams aren't keeping up with those newer versions. And a good example here recently is Matt Pocock. Hopefully you've all heard of him. He's a great educator, published a bunch of great skills. He has a Grill Me skill.

**[3:19](https://www.youtube.com/watch?v=PabKgxoegGg&t=199s)** That's where you kind of do an interview with the agent and you kind of get a shared understanding. He recently published a newer version of that Grill skill, called Grill with Docs, which kind of expands on it and adds a lot more detail to it. I'm sure there's lots of folks that don't realize that that's been released, right? And they're still using that older version and haven't updated. So that's drift. We also have problems around activation, or a lack of activation, right? Lots of people are producing these skills. Are they being used by the agents? Are they being used by humans? There's no real way to to understand that and know that right now. You probably don't have that visibility yet. So I mentioned this in his talk as well. This morning. You might have a skill that describes some code or a code base, or a process or even a workflow, and those two things can quickly go out of sync,

**[4:08](https://www.youtube.com/watch?v=PabKgxoegGg&t=248s)** so your skill never gets updated. Things change. And in those instances, having an outdated skill can often be just as bad as having no skill at all. Right? John Groetzinger is a principal engineer at Cisco, and he has a line I've thought a lot about since: you don't need a smarter model, you need smarter context. He went and tested it and found mid-tier models could do the job once the context was right. So this might be a little controversial for some people here, especially maybe if you work for a frontier model company — earmuffs — but you don't really need a smarter model today. The models are perfectly capable of doing what you need for business value, right? Not talking like PhD level intelligence and beyond, but getting business value out of the models. It's already there today.

**[4:56](https://www.youtube.com/watch?v=PabKgxoegGg&t=296s)** The problem is really that you need smarter context and smarter context engineering. And so for me, the last couple of years I've been jumping harness to harness. I'm always chasing the latest, greatest thing, constantly breaking my workflows. I'm sure other people can relate to this. And always there's so many variables that anytime I switch to a lower model and it breaks something, I'm immediately like, well, that's the model's fault. I'm going back to Opus, right? Because this thing that I don't understand, it has to be the model, right? But once skills came onto the scene, it kind of changed my perspective on things, especially recently with the new patterns of agentic fan out in the harness, right, where I have my model set to Opus, and I ask it to do this massive prompt and it spawns 15 subagents. That cost is just really increasing, and we're actually seeing that becoming actually a concern where we had to start limiting model use on our large enterprise because of the cost of this stuff and the fan out being a problem.

**[5:48](https://www.youtube.com/watch?v=PabKgxoegGg&t=348s)** So I really wanted to figure out, okay, why can't I just use Sonnet for everything? And I found out I can. And today, for the last couple of months, I largely use the medium tier model. Whether that's Sonnet, GPT medium reasoning — I don't really use those high end models. It's very rare that I use those. Maybe for some super complex planning. Lots of context. I still use them, but I challenge my engineers to really try to use that medium tier as their baseline and only jump into the greater tier when they need to. And the real unlock for this was skills, because all the harnesses, all the models are training on skills, they're honoring skills. And so if you can lean into that, your context can actually transfer between the harnesses. And that was great for me because I can I can try Claude Code, I can jump into dev and I can jump into GitHub Copilot CLI. And if my skills work in all three of them relatively, it works the same. So it's great.

**[6:36](https://www.youtube.com/watch?v=PabKgxoegGg&t=396s)** But what you need to understand is how do you manage your context, right? How do you share it? Package it once and then ship it to everyone, but only have one source of management. And the real unlock for that is evals. And finally, Rob Willoughby and Simon Obstbaum from the Stanford lab, who actually measured this: 500 skills, a thousand tasks, 19 combinations of model and harness. Their most uncomfortable finding is that more than half the time, the model followed the skill's instructions, even when the skill was not loaded at all. the theorem. I want to talk a little bit about what kind of task and what I mean by full completion and instruction following. So what we're running is we've got 500 skills. We have 1000 tasks.

**[7:25](https://www.youtube.com/watch?v=PabKgxoegGg&t=445s)** We've got 19, 19 permutations of models and harnesses. So we got 19 permutations of different models, different harnesses, because those have an effect on each other and also affect the performance. And then the tasks that we're using, those are synthetic. But they're anchored on the skill itself, they're meant to be something that you could expect the skill to trigger for. So if you have a skill that says, how do you implement API security, the task that we're going to construct is that great. Or change the authentication from password to some other mechanism for that, or something else that might not be related, to expect them to be picking up on the security and looking for that. And so hopefully potentially not trying to do like super hard pushing boundaries here.

**[8:15](https://www.youtube.com/watch?v=PabKgxoegGg&t=495s)** Think of it as kind of like well scoped to your tickets and expecting engineers to be getting that one. And so we see that hitting a threshold of 1,993% of us, whether it's in their office in holding, this is the metrics that are specifically in the agenda, what they do. So if you have your own internal design for how you want to do whatever you hold or to make sure that you're updating two supervision versus another, that's the information that we put in the skill and then encoded in the instruction following improvement that we see there. One really interesting thing about that number specifically is that we see 55% following the instructions of the skill, even when the skill is not present. That means the information that is encoded in the skill, that's actually in the weights of the model already. And so when you're talking to you, it was getting rid of anyway.

**[9:05](https://www.youtube.com/watch?v=PabKgxoegGg&t=545s)** So that means that's actually valuable because burning inference tokens and paying money down in Google when the model is going to get in ways that they can get to do that. So you're giving this will be finishing. But the things that you care about, the structure of these skills or changes, how it does it and how well it does it. Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
