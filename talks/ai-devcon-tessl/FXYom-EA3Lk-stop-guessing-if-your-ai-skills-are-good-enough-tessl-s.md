---
id: FXYom-EA3Lk
title: "Stop Guessing If Your AI Skills Are Good Enough — Tessl's Skill Optimizer Does It For You"
slug: stop-guessing-if-your-ai-skills-are-good-enough-tessl-s
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 5
published_at: 2026-05-01T11:23:58Z
video_id: FXYom-EA3Lk
url: https://www.youtube.com/watch?v=FXYom-EA3Lk
youtube_url: https://www.youtube.com/watch?v=FXYom-EA3Lk
tags: ["AI skills", "CI/CD integration", "Marc explains Skill Optimizer", "Tessl Skill Optimizer setup", "Tessl plugin", "agentic coding", "ainativedev", "best practices", "context engineering", "evaluate AI agent skills", "how to improve AI skills", "optimizing skills with Tessl", "skill evaluation", "software optimization", "what is skill optimization"]
topics: ["Agents & orchestration"]
transcript: true
---

# Stop Guessing If Your AI Skills Are Good Enough — Tessl's Skill Optimizer Does It For You

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `5 min`

`#AI skills` `#CI/CD integration` `#Marc explains Skill Optimizer` `#Tessl Skill Optimizer setup` `#Tessl plugin` `#agentic coding` `#ainativedev` `#best practices` `#context engineering` `#evaluate AI agent skills` `#how to improve AI skills` `#optimizing skills with Tessl` `#skill evaluation` `#software optimization` `#what is skill optimization`

[Watch the recording](https://www.youtube.com/watch?v=FXYom-EA3Lk) · [Conference site](https://tessl.io/devcon/)

## Description

Are your AI agent skills up to par, or are you just hoping they are? Tessl's Skill Optimizer evaluates, improves, and re-tests your skills to ensure they're truly ready for team sharing. It sounds simple, but it's transformative: moving from wondering to knowing.

Marc takes you through Tessl's Skill Optimizer plugin, showing its seamless integration into your development process. With tools evaluating best practices, real-world performances, and activation rates, Marc's guidance reveals how to ensure your skills contribute effectively to task execution. As a Tessl team member, he brings first-hand insights into this optimization process.

Get started in minutes:
👉 Visit tessl.io/registry, search for Skill Optimizer, and paste one command into your terminal. Then ask your favourite agent to optimise a skill — that's it.

What we cover:
• Why 'is this skill good enough?' is a critical question for developers
• Three dimensions of skill quality: best practices, performance, and activation rate
• How does the Skill Optimizer plugin work end-to-end?
• Using the Skill Optimizer to keep skills from going stale
• Integrating Skill Optimizer into your CI/CD pipeline

🌐 Try Tessl - we help you build a software factory, one step at a time: https://tessl.io
🔔 Subscribe for weekly episodes on AI-native development

Share your thoughts and experiences with skill optimization in the comments below.

## Transcript

*950 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=0s)** So Mark, as part of my work, I spend a lot of time talking to developers and try to understand how they behaviors and workflows are changing as agents become more of a centerpiece to their work. Um, and the main thing that I keep hearing is skills. Skills are great to gather context and to manage context and to help developers have a bit of control around the agent's output and execution of tasks. Um but the conversation shifts a bit when developers start to think about sharing those skills uh with the organizations and the the rest of the team members. The question becomes is this skill actually any good? Is it helping my agents succeed with their tasks? So what would you say is the easiest way for developers to gain some confidence around the skills they're

**[0:48](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=48s)** building so they can share them more broad? >> The easiest way for developers to gain confidence in the skills they're building is to use Tesla's skill optimizer plugin. It's really easy for them to get started. They go to tesle.io/registry, search for skill optimizer, copy and paste the command to install Tessle and the skill optimizer plugin into their terminal, and then it's a case of firing up their favorite agent and asking it to optimize their skill. What the plug-in does is it takes a look at the skill and figures out the best way to evaluate its quality. It evaluates its quality and then uses the feedback from that to figure out how the skill can be improved. It works with the user to make those changes and then it runs the whole thing again to understand whether those changes made a positive difference. The idea is that the plug-in assists the

**[1:36](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=96s)** agent throughout and automates as much of the flow as possible and helps developers get from wondering if their skill is good enough to share to knowing that their skill is good enough to share. And that's a really key question. You're bringing up the the word good and what good means. Um, and that can mean different things depending on situation and the developer you're talking to. So, what I've heard from my conversations with developers is that good means it follows best practices. It's well written. It can also mean it activates at the right time when it's needed by the agent and it also contributes to success of a task execution. So what's under this the hood of the skill optimizer that can help address these pain points? >> So the skill optimizer plug-in is actually a bundle of different skills

**[2:23](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=143s)** that have been designed to work with Tessle's powerful evaluation CLI toolkit and as you mentioned there are different ways to look at skill quality. So we have various tools to help with different uh aspects of that. For example, our skill review looks at the content of a skill to understand whether it follows anthropics principles of best practice. This is useful in a quick feedback loop where developers are actively working on the skill and want to make sure it's in the best shape, but it doesn't tell them much about how the skill actually performs. So we have a separate type of evaluation where we run the skill against realistic scenarios in a simulation sandbox to check how the skill actually performs and if it does what it's meant to do. We've also recently added a new type of evaluation to see for those realistic scenarios if

**[3:13](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=193s)** the agent natively chooses that skill to run in those scenarios. And this is a way to measure what activation of a skill might look like in real world situations. So really the skill optimizer helps developers cover all these pain points and take us to a world where developers have the confidence to share the skills with others. Um in this world, this new world where there's more people on the organization using the same skills, another concern raises uh which is how do you make sure that skills stay alive and they don't go stale. >> Yeah, this is a problem that Tesla has itself with the skill optimizer plug-in. As you can imagine, our toolkit is constantly evolving and improving, and every time it does, we need to make sure the skill optimizer plug-in is up to date with the latest. So, we actually

**[4:02](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=242s)** run skill optimizer on the skills in the skill optimizer plug-in. And that's a great way to make sure that it is always um up to date and has high quality. But we've also integrated many of Tesla's CLI commands into our CI/CD workflow as a way for us to catch regressions on changes that are made to our skill files um as and when they are made. This is useful for ensuring that skills uh not just customerf facing skills like the skill optimizer plug-in but also internal skills that the developer team use are always at the highest standard of quality and these tools are available to all of our customers as well. Amazing. So, how do they get started? >> It's really easy. If you visit tesl.io/registry, search for skills optimizer,

**[4:51](https://www.youtube.com/watch?v=FXYom-EA3Lk&t=291s)** select the Tessle Skills Optimizer plugin, then you'll see a command that you can copy and paste into your CLI terminal. And this will install both Tessle and the skill optimizer plugin in one go. Once that's installed, it's as simple as firing up your favorite agent and asking it to optimize a skill. Simple enough. Thanks for sharing, Mark. >> No problem. So remember, visit tesla.io/registry, search for skills optimizer, and get started on your skill optimization journey today.
