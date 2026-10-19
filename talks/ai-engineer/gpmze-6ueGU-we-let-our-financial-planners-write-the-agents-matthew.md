---
id: gpmze-6ueGU
title: "We Let Our Financial Planners Write the Agents — Matthew Ragone, Range"
slug: we-let-our-financial-planners-write-the-agents-matthew
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Matthew Ragone"]
channel: "AI Engineer"
duration_min: 9
published_at: 2026-10-12T12:00:24Z
video_id: gpmze-6ueGU
url: https://www.youtube.com/watch?v=gpmze-6ueGU
youtube_url: https://www.youtube.com/watch?v=gpmze-6ueGU
tags: ["AIE NYC 2026", "Keynote", "Leadership", "Livestream Priority 01", "Online Talk"]
topics: ["Agents & orchestration", "Enterprise adoption & strategy", "Science, healthcare & applied ML"]
transcript: true
---

# We Let Our Financial Planners Write the Agents — Matthew Ragone, Range

**Matthew Ragone**

`AI Engineer` · `AI Engineer` · `2026` · `9 min`

`#AIE NYC 2026` `#Keynote` `#Leadership` `#Livestream Priority 01` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=gpmze-6ueGU) · [Conference site](https://www.ai.engineer/)

## Description

While one financial planner is on a client call, an agent drafts another client's cash flow or insurance analysis. The planner reviews every recommendation before anything reaches the client. At Range, Matthew Ragone and his colleagues built the skills behind that workflow without writing code. Six months in, he reports 24 skills across the company, including 17 in planning, with sales, product and marketing adopting the same approach without a mandate. The change came from capturing how the firm actually works: what a planner checks first, which questions must be asked and where an agent must stop.

Ragone breaks the process into five steps: pick a repeated workflow whose output you can judge, teach it with real cases, package the judgment into a skill, test it five to ten times and ship it with an owner and a separate reviewer. Narrating why you open a document matters more than listing the clicks. Questions and limits belong in the skill alongside the procedure, including the rule that an agent drafts but never sends recommendations to a client. Testing exposes missing questions and confident mistakes; ownership keeps the instructions current as the firm's practices change. The remaining challenge is how to check quality at scale when the output requires professional judgment.

Speaker info:
- https://www.linkedin.com/in/matthew-ragone-cfp%C2%AE-crpc%E2%84%A2-a56a85106/

Timestamps:
00:00 - Financial planners building their own agents
1:31 - Drafting while the planner is on another call
3:16 - Pick a workflow you can judge
4:22 - Teach the judgment and package the limits
5:51 - Test real cases, assign owners and reviewers

## Transcript

*1,414 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=gpmze-6ueGU&t=1s)** Hi everyone, I'm Matt Rigon and I'm a financial planner at Range. I want to show you how our financial planners ended up writing the agents that we use every day and none of us the financial planners for that matter write code. This is the build guide. How we did it step by step so you can take it back to your own teams, companies, etc. So, a quick bit about me because it matters for how you'll hear this talk. I'm not an engineer. I'm a certified financial planner and I spend my days with clients talking about cash flow, taxes, insurance, retirement, estate, you name it. I also lead the AI adoption for the planning team at Range, which is an all-in-one wealth management company. Most agent talks you'll hear come from the people who built the platform. This

**[0:51](https://www.youtube.com/watch?v=gpmze-6ueGU&t=51s)** talk comes from someone on the other side, the people you hand the platform to. We work in a regulated business. The output is financial advice to real clients. And the review step is not optional. So, this isn't a vendor pitch. It's a method and it's what actually worked for us. We started where everyone starts AI as a chatbot. I'd write a client message, paste it in, and ask it to make it a little clearer or friendlier. And that was useful. It saved me a few minutes here and there, but I was still doing all of the work manually. I was just doing it a little bit faster. The change that actually mattered came later. Here's what we figured out. A planner's constraint was never typing speed, for

**[1:39](https://www.youtube.com/watch?v=gpmze-6ueGU&t=99s)** example. It's that we can only be in one place at a time. If I'm on a call with a client, I'm not building someone else's plan. Writing faster doesn't fix that problem. What fixes it is work that happens while I'm somewhere else. So, here's what a day looks like now. I'm on a call with one client. At the same time, an agent is drafting a full cash flow analysis or an insurance analysis for a different client. When the call ends, I open that draft. I fully review it, adjust what needs to be adjusted, and send the client their recommendations. I want to be really clear about that last step. The agent doesn't send anything. A planner reviews every single recommendation before a

**[2:28](https://www.youtube.com/watch?v=gpmze-6ueGU&t=148s)** client sees it. What changed is that the first draft no longer needs me sitting in front of it. Getting there took a lot more than a good prompt. However, two things had to be true. First, the agent has to work where the work lives, not in a separate chat window I'm copying and pasting it into. Second, it has to know how we do it, not how financial planning works in general. The model already knows that, but the agent needs to know how range does it. What we look at first, what we always flag, how we phrase a specific recommendation. That combination is what a skill is. Our firm's way of doing one specific piece of work written down so an agent can follow it.

**[3:16](https://www.youtube.com/watch?v=gpmze-6ueGU&t=196s)** The bulk of this talk is how you build one. Five steps. Pick, teach, pack, test, and then ship. None of them require writing code. Every one of them requires knowing the work really well, which is exactly why the people doing the work should also be the ones building it. Step one, pick a workflow you repeat. Your initial instinct is to go for the flashiest work, whatever's taking the most amount of time and the most complex. Don't pick something you do every week where you already know what good looks like, where you can spot a bad draft at a glance. Additionally, we recommend choosing some of the least complex workflows to start, but some that require the most manual work. For

**[4:07](https://www.youtube.com/watch?v=gpmze-6ueGU&t=247s)** us, that meant things like cash flow analysis and insurance reviews. Just for us here at range, that required the most manual work. And if you can't judge the output quickly, you can't test it and you can't trust it. So look for two things. You do it often and you know how to judge it. Step two, show it several real cases for previous plans you've delivered. Take several actual client cases and walk through the work start to finish. And as you do it, narrate your judgment out loud. Not just next I open the pastub, why you're opening it, what you're looking for, what would make you stop and ask a question. That narration is the whole game. The steps are easy to

**[4:55](https://www.youtube.com/watch?v=gpmze-6ueGU&t=295s)** write down. The judgment is what makes it your firm's work instead of generic advice. Step three, pack it into a skill. A skill isn't just a lip a list of steps. Two things matter most. The questions it must ask before it starts. What does it need to know? What should it confirm with me instead of simply guessing? And the limits it must respect. What it never does on its own. In our world, the big one is that it never sends anything to a client. It drafts and then a planner decides if it gets sent or needs to be adjusted. If you only write the steps, you get something that simply just runs on its own. If you write the questions and set the limits, you can get something you can trust. Think of a

**[5:44](https://www.youtube.com/watch?v=gpmze-6ueGU&t=344s)** skill as a recipe. Once Claude knows how to do the skill, it will repeat your process on command. Step number four, run it five or 10 times on real cases before anyone else sees it. This is the step everyone wants to skip. Every run teaches you something the skill didn't know yet. An edge case, a question it should have asked, a spot where it sounded confident and was wrong. You need to fix it, save the skill, and run it again and again and again. Five to 10 runs sounds like a lot, but it's a lot less work than cleaning up after you hand a halfbaked skill to 15, 20, 100 people in your team. Step five, ship it with an owner and a reviewer. The owner keeps it current.

**[6:34](https://www.youtube.com/watch?v=gpmze-6ueGU&t=394s)** Our processes change, tax rules change, and a skill that was right in March can be wrong by December. The reviewer checks it before the team relies on it. And it's someone other than the author. Same as a plan, you don't grade your own work. Once other people depend on a skill, somebody has to be accountable for it. That's the difference between a clever personal shortcut and something a team can build on. So, where are we at currently? Six months in, we have 24 skills across the company and 17 of them are in planning. And here's the part I didn't expect. It spread to sales, product, marketing, all without a mandate. Nobody sent a memo. People saw what the planners were doing and started

**[7:22](https://www.youtube.com/watch?v=gpmze-6ueGU&t=442s)** building their own agents. Every one of those skills was written and is maintained by planners, marketers, and salespeople, not developers or engineers. A couple of things changed once subject matter experts started building for their own niche. The skills got a lot more specific. The person who knows insurance, for example, best builds the insurance skill. The person who best knows tax, tax code, tax law should be building the tax one. and a review came naturally. We already review each other's plans and that's just how planning works. So now we review each other's skills in that same way. It's the same habit, just a new thing to review. So why does this matter right now?

**[8:10](https://www.youtube.com/watch?v=gpmze-6ueGU&t=490s)** Because the bottleneck has moved. Whether a model can draft a cash flow analysis, that question's already been settled. It can. What's not settled? Who writes down how your firm does it? who tests it before it ships, who owns it once 15 other people depend on it. If you're being asked to push agents out past the engineering org, you're about to hit these exact questions. There isn't much field data on this yet, but this is how we've done it here at Range. So, that's it. Thank you so much for listening to this talk. I'm Matt Rigon from Range and you can reach me for at mattrange.com. Have a great day.
