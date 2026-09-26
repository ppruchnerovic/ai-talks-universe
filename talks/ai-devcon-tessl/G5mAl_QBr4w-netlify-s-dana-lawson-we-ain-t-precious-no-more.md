---
id: G5mAl_QBr4w
title: "Netlify's Dana Lawson: 'We Ain't Precious No More'"
slug: netlify-s-dana-lawson-we-ain-t-precious-no-more
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "Practitioner AI conferences"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-09-21T14:30:30Z
video_id: G5mAl_QBr4w
url: https://www.youtube.com/watch?v=G5mAl_QBr4w
youtube_url: https://www.youtube.com/watch?v=G5mAl_QBr4w
tags: []
topics: ["AI in the SDLC & engineering orgs"]
transcript: true
---

# Netlify's Dana Lawson: 'We Ain't Precious No More'

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=G5mAl_QBr4w) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Harness engineering is the discipline behind every agent that ships working code — and this recap is about where it still comes up short. At AI DevCon London, Marc Sloan (Tessl) walked through an agent that built a pixel-perfect export button and still got it wrong, while Tammuz Dubnov (Autonomy AI), Dana Lawson (Netlify) and Emma Burrows (Rezonant) covered what happens once non-developers are the ones opening the pull request.

What we cover:
– Why an agent's PR can pass every check in the harness and still ship the wrong component
– The real merge rate for pull requests opened by non-technical teammates
– Why Netlify redesigned its platform for a builder who isn't a professional developer
– What it takes for a product manager to become an agent orchestrator, not just a prompt writer

Chapters:
00:00:00 - Introduction
00:00:24 - Marc Sloan, Tessl: the export button nobody could find
00:01:44 - Why the agent's PR passed every check and still missed
00:03:26 - Tammuz Dubnov, Autonomy AI: measuring non-technical PRs
00:04:15 - 74% merge rate, and what the other 24% means
00:05:41 - Dana Lawson, Netlify: "we ain't precious no more"
00:06:51 - 500 million new apps and what that does to platforms
00:07:43 - Emma Burrows, Rezonant: product managers as agent orchestrators

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Would a non-technical teammate's PR pass review on your team today?

## Transcript

*1,693 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=0s)** Back in June at AI DevCon in London, one of the recurring themes had almost nothing to do with developers. It was about product people, designers and everyone else who was never supposed to open a pull request and now does. Let's first hear from Marc Sloan of Tessl with the story about an export button that shows exactly what goes missing when an agent has the ticket and the design, but none of the context around them. I'm Marc Sloan, I'm a member of the product team here at Tessl, and I'm here today at a developer focused conference to talk about non developers. Now, I don't know if there are any other non developers in the room here today. I'm thinking yeah there we go. Product managers, designers executives you know the people who traditionally wouldn't touch code.

**[0:50](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=50s)** We're going to describe a scenario here where we've got a company that has a web app product, and a customer has asked the product manager to put an export button on the dashboard in their product. Now, the export feature was something that was hidden behind the settings menu, and there was a couple of layers deep, so it was very difficult to find. Customer wasn't aware that it existed, and requested this to be in a more prominent position. On the surface, this seems like the perfect kind of job to give to an Agent Ryan linear ticket that describes it. Put a figma design in there that shows where the button should go and what it should look like. All that good stuff fired off to your agents, have it produce a PR job done, customers happy. The feature got delivered.

**[1:38](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=98s)** The customer tried it out and said, it's great. So cool. This is the world we live in right now. We can just send these things off to agents. And of course, the agent wasn't building this blind. It had access to a bunch of skills that had been developed in advance to instruct the agent on how it should be, thinking about the architecture of the code, about the front end components that live within that, the testing and CI requirements, and how to make use of the API to get the data. And of course, this is a cutting edge state of the art company. So they're using Tesla to manage all of this stuff. So problem solved. Why do we need to be thinking about product and design context? Well in this scenario the agent got one thing wrong.

**[2:27](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=147s)** It actually ended up using a generic react button component that lived within the code base, and not the more specific export button components. That was the right choice here, and this might seem like a trivial error, but encoded within that export button component are the accessibility requirements that this organization adheres to. Interaction patterns that make sense for this kind of async, the async operation of this kind of button. And this was all missed by the agent in creating this. And what's challenging here is that as far as the harness was concerned, everything went smoothly. The agent got a ticket handed off to it, did the job, created a PR that passed, and the feature went out to the customer. The valuations that were set up on the skills

**[3:17](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=197s)** and the other aspects of the harness all seem to be working well, but the product and design context was missing from the agent in this particular situation. We also heard from Tammuz Dubnov, founder and CEO of autonomy AI, who has the numbers on this across hundreds of organizations, 74% of pull requests from non-technical people get merged, and 84% of those go in without a developer touching them. So now the the thing that really matters for any data scientists in the room is how how do you measure it? I'll tell you how we do it across the hundreds of orbs and thousands of hours to get opened with us and weekly monthly basis. So the first thing to track is, frankly, the count of the pull request. How many are open by non-technical individuals and ideally

**[4:08](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=248s)** by by which individual. So you know that every is actually getting a enabled and impactful. We have seen places where some non-technical and are more confident open doctors, some are more hesitant. You want everybody to actually feel comfortable. You can track that just by the count, but beyond it, you want to make sure that you're not adding PR fatigue by opening nuts and speeds. And that's where the merging comes in from. From our number is just so you're familiar in average non-technical contributor and organization. In a quarter of openness about 50 there emerging is about 74%. Which means that one out of four they accidentally overstepped. And that's okay. That's not PR fatigue. That's totally fine, that it's a level where we still have a lot of trust between the PRC open and the dev team that reviews them.

**[4:58](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=298s)** And lastly, you also want to measure how much extra work you're adding, not just in terms of PR reviews. Sometimes developers will need to do follow up work because the agent doesn't know. Maybe some future roadmap plans and factors that are intended or whatnot. And they're how we do this. We measure from PR that are open and merge. How many get merged without any dev interfering, without them pushing more commits to fix, change, adjust. And again, for us that is 84%. So 84% of the PR merge generated by non-technical individuals simply get merged, which is a way to make sure that you are not increasing the burden on the dev team, not just from PR fatigue, but from a task perspective. Dana Lawson is CTO at Netlify, and she opened by asking the room who still identifies as a developer.

**[5:48](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=348s)** Her point is that the builder is now a teacher, a therapist, a small business owner, a student, and building for those agents made the platform better for developers to. before we get into the architecture, I need to say something that might feel uncomfortable. How many of you here identify as a developer? Oh man, we ain't precious no more, y'all. The builder persona has changed. The person our platforms were built for are no longer just developers. We're still builders, don't get me wrong, but we're not the only ones. Now, with agents, anybody can participate. In fact, the IDC predicts that more than 500 million new applications will be built by 2028. And in fact, I create one a day. So I'm a I'm a part of that damn problem more than the previous 40 years combined. Think about it for a minute now,

**[6:41](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=401s)** 40 years have been compressed into three, just like this room. That's not because the number of engineers is expanding. It's because agents have turned intent into a programing language. In fact, the strongest programing language that will happen now and into the future is guess what, English. So I hope you go and study that in school. Kids, if you're watching you better, you better learn how to talk to somebody. Claude Code. Cursor. Bolt. Lovable. Netlify. These tools let anyone with an idea create working software through conversations. No longer is it just developers. It's therapists, teachers, small business owners, students, people in line at the store building experiences on their phone. Thank you. Lovable and becoming software creators at Netlify, we build for all of these builders. And here's the thing.

**[7:30](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=450s)** When we designed our platform to work better for agents serving these new builders, it got better for developers too. And that's the paradox. And to close. Emma Burrows, founder of Rezonant, who was CTO of stripe in the UK and a product manager at Google before that. She thinks product managers need to become orchestrators the way engineers already have, Which needs a system that has learned your product and knows the edges of what it knows. at the moment, where most PMS are, is trying to just kind of do workflows, basic workflows that help them do their day to day job, you know, break this down into tickets. Rezonant also does all of these things very well, for what it's worth, but I think where we need to go is towards what software engineers has have become, which is agent orchestrators.

**[8:20](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=500s)** So we identify the slices of product management work that can actually actually be done autonomously, end to end. And in order to do that, you need a system that kind of learns and understands your product. So most of are here, they're using ChatGPT etc. to help them do these workflows. Then they're starting to actually orchestrate a set of skills to help them run those workflows. And then where I think we need to get to is actually having agents that have a sense of taste, coherency, but also understand their own limitations. Software engineering from a product perspective, has also already gone through this right. If you think about what cursor did, it was very much like line by line assistance when it started out with C, Cursor has become more than that over time. Then we went really kind of deep on Claude Code, and now there's OpenCode.

**[9:11](https://www.youtube.com/watch?v=G5mAl_QBr4w&t=551s)** If you're brave enough from a kind of permissions perspective to run those agents end to end, but for the actual automation process is harder, right? You have a much less consistent set of work and training data to optimize this on. So you need to automate your process of gathering information from your customers, from your slack conversations, from your emails. You need to work out what your human agent control plane is. How are you going to ensure that you have the right checks and balances between your agents and your PM so that they can work effectively? Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit ainativedev.io to learn more and book your ticket
