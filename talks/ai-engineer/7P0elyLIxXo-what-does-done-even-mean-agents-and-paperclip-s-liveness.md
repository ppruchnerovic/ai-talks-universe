---
id: 7P0elyLIxXo
title: "What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip"
slug: what-does-done-even-mean-agents-and-paperclip-s-liveness
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: null
duration_min: 7
published_at: 2026-07-12T06:45:06Z
video_id: 7P0elyLIxXo
url: https://www.youtube.com/watch?v=7P0elyLIxXo
youtube_url: https://www.youtube.com/watch?v=7P0elyLIxXo
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Agents & orchestration"]
transcript: true
---

# What Does Done Even Mean? Agents and Paperclip's Liveness Model - Dotta, Paperclip

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `7 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=7P0elyLIxXo) · [Conference site](https://www.ai.engineer/)

## Description

What does “done” mean when agents can produce more work than humans can possibly review? This talk argues that the future of agentic work is not just faster output, but a stronger trust protocol: systems where “done” means an artifact has met a stated standard, carries evidence, has been checked by the right verifier, assigns ownership of remaining risk, and clearly authorizes the next action. Drawing from Paperclip’s liveness model, it shows how teams can avoid approval theater, keep work moving, route review by risk, and turn agent completion from a vague confidence signal into something others can safely build on.

Speakers:
- Dotta (Paperclip): Dotta is the creator of Paperclip, the Open-source app for zero human companies
X/Twitter: https://x.com/dotta

## Transcript

*1,325 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s)** An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, "Looks done to me." But is it actually done? Is it done enough to merge? Is it done enough to deploy? Is it done enough to announce to your customers? These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark. I'm Dota. I'm the creator of Paperclip, and I'm going to give you some hard-earned lessons that we've learned in creating Paperclip's liveness model. What does done even mean? Here's the thing. Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify. And this actually gives us a new failure mode, is that agents can actually create more work than humans have time to verify. So we need a way to verify that

**[0:46](https://www.youtube.com/watch?v=7P0elyLIxXo&t=46s)** our agents are done more than just letting them check a checkbox. Done doesn't mean that an agent just changed the status of a task being done. Saying that something is done is actually a bundle of claims. You're saying that an artifact was produced, that you have evidence that the task is actually complete, and you have a rubric in which you can verify against. You know exactly who the owner is for the next step, and you know exactly what the next step is. There's different levels to how done something is. The producer might claim something is complete, but you need to have a reviewer, another party that looks at it and finds no obvious issues. You want to verify and make sure that the evidence actually meets a specified standard. You want to make sure that a person who is authorized to approve it actually approves that the work is done.

**[1:34](https://www.youtube.com/watch?v=7P0elyLIxXo&t=94s)** And you want to make sure that there's somebody who actually stands behind the decision. And ideally, what you want is that the outcome has actually survived real-world conditions. Because exhaustive human verification fails at high volume. You might be able to verify a few tasks per day, but essentially, if you have humans verifying all the tasks and they have to sign off on it, you eventually what you just get is a form of verification theater. What you need is a protocol for defining how tasks actually progress through a system. You want to make sure that tasks are always kept moving, but they don't get stuck into invalid states. You need a control plane that actually has the execution of the tasks being tied to specific contracts and

**[2:23](https://www.youtube.com/watch?v=7P0elyLIxXo&t=143s)** constraints about what the system will do and what agents it will hand off your next task to. Because really what you're trying to play against is this idea around keeping work moving, but also having it verified. When a task has been reviewed by a human, you get the assurance that it's correct. But having a human verify it means that the task is dead in its tracks. You also want to keep liveliness. Liveliness means that the work is continuing with no blockers. And you're always trying to keep these two things in balance. If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop because you're producing a lot of things with kind of no quality control and it's worse than creating nothing after a long period of time. But if you have peer review, um then you have this enormous review queue where

**[3:14](https://www.youtube.com/watch?v=7P0elyLIxXo&t=194s)** humans can't actually review it by hand anyway. These agents will be creating far more than you can ever actually review, and so we have to find a way to tease apart the bundle of claims that are involved in saying a task is done. With Paperclip, we have a number of mechanisms to keep this going. You might think that you can easily just write a for loop over your task manager and have your agents work, but quickly you'll find that falls apart. As soon as you start integrating task dependency trees, blockers, multiple agents, item potent checkouts, like locks on checkouts, you find that this tension between liveliness and verification actually gets quite complicated. There's really three invariants that are extremely important when you're thinking about what you want out of a control plane for your agentic work. You want to

**[4:03](https://www.youtube.com/watch?v=7P0elyLIxXo&t=243s)** ensure that productive work continues. You want to make sure that only real blockers stop work. And you want to make sure that infinite loops are bounded. In Paperclip, we have built a number of mechanisms to deal with this problem. So, for example, every time you have a task, there's clear transitions to what the next state could be. We have first-class blockers between tasks, and the control plane enforces those blockers. We have moments of interactive human approval, where human choices leave an audit trail. You can set reviewers and approvers on tasks explicitly, meaning when this task completes, another agent can review it. We also have the idea of watchdogs, which is this maximizer mode, which says, um, try as hard as you can to make sure that this happens. When you have a

**[4:51](https://www.youtube.com/watch?v=7P0elyLIxXo&t=291s)** watchdog, it's another agent, um, who is given a goal, and it enforces that all of your agents continue to work until that goal has been achieved. The important thing here is that the watchdog within Paperclip is harness agnostic. You can use it with Pi, OpenGL, Hermes, Claude Code, Codex, whatever you're using, you have one consistent interface for ensuring that goal is complete. So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object. This isn't specific to Paperclip. It's just advice on how you think about what is done. Humans automatically paper over these details, but when we're building agentic systems, it's important that your agents can distinguish between the different pieces of what they're claiming when they say something is done. The artifact that they're saying is complete, the scope, the rubric or

**[5:40](https://www.youtube.com/watch?v=7P0elyLIxXo&t=340s)** the standard, the evidence that it's done, who verified the work, who has the authority to sign off on the work, And what risk might be left? And really, what's the next action going to be? So, you want to make sure that when you define done, it's not just a checkbox. So, if you want to get 100 times more work done, you should steal this checklist. You need to define exactly what does done mean for this task. You definitely want to separate the verifier from the author. Often, this means you're using a different model. So, if you're coding using Claude, have Codex verify. You want to ask your agents to provide evidence. Don't just ask them to say, "Is this done?" But, give them the tools they need to verify that the work is done. Write the code to have the custom browser harness. Write the code to take the screenshots. Make sure they have access to a browser.

**[6:29](https://www.youtube.com/watch?v=7P0elyLIxXo&t=389s)** Make sure that they have custom agent hooks or custom agent tooling to actually run through and click the buttons and try it out themselves and verify that the work is truly done. Make sure you have a clear chain of custody, that every agent knows that as soon as they're done, who they're supposed to give the work to next. It can be easy to just fire off a single-line instruction and vibe with whatever comes back. But, if you have serious work that you're accountable for, it's very important that you define what done really means in as much detail as possible, and that you have a structure for your agents, so that way they can verify that all of the claims that are involved with something being done are actually met. Thank you.
