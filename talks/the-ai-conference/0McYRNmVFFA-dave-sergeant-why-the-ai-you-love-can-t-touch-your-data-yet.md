---
id: 0McYRNmVFFA
title: "Dave Sergeant: Why the AI You Love Can't Touch Your Data (Yet)"
slug: dave-sergeant-why-the-ai-you-love-can-t-touch-your-data-yet
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 12
published_at: 2026-10-07T22:54:07Z
video_id: 0McYRNmVFFA
url: https://www.youtube.com/watch?v=0McYRNmVFFA
youtube_url: https://www.youtube.com/watch?v=0McYRNmVFFA
tags: []
topics: ["Governance, ethics & regulation"]
transcript: true
---

# Dave Sergeant: Why the AI You Love Can't Touch Your Data (Yet)

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=0McYRNmVFFA) · [Conference site](https://aiconference.com/)

## Description

You've felt it. You sit down with a frontier AI and watch it do something genuinely brilliant. So why isn't that capability showing up in your work? Two reasons: you can't hand company and customer data to a chat window, and your business isn't a chat. It's thousands of repeatable, auditable interactions a day, and nothing about raw model access makes those reliable, private, or provable. That gap is why an estimated 95% of enterprise AI pilots never reach production. At SS&C, we hit this wall at scale, processing billions of tokens a month across a regulated, global business, and had to build the layer that closes it: guardrails, monitoring, and auditing between the model and the work. In ten minutes, we'll show you what that layer looks like, why every organization needs one, and what changes when it exists.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,955 words · source: supa (en, exact timings)*

**[0:15](https://www.youtube.com/watch?v=0McYRNmVFFA&t=15s)** So somewhere in your organization, you've got a queue and you know it seen it there. It's been there long enough that it's actually stopped being a problem because nobody nobody escalates it anymore. Um, and there's actually a person behind it whose entire job is being behind. So, the here's a real one. This is a health care system. Um, we've got uh seven hospitals that process 50,000 invoices uh a year um from a thousand different vendors and all the different formats you'd expect a thousand different vendors to be in. And all of it needs to be matched and checked and paid. Now they were six to nine months behind. Now not after one bad quarter but structurally fundamentally six to month

**[1:06](https://www.youtube.com/watch?v=0McYRNmVFFA&t=66s)** six to nine months behind. And basically that means like an invoice arriving today would probably be processed sometime next spring. And you know nobody was failing. This is this is a good team. They were using the same software that everybody else uses. There was no real crisis to point at. It was just exactly why this queue lasted and why it was so viciously behind. So backlog like this isn't something that uh announces itself. It's things people plan for. They know it's going to take that long to run. And the thing is the questions nobody asks about backlogs like this are uh you know it's it's not about what does it cost to process. It's really about what happens to documents that spend this long in a

**[1:55](https://www.youtube.com/watch?v=0McYRNmVFFA&t=115s)** queue because that's where the money really is. It's not a question of just uh processing faster, but what are you missing out on? And that could be things like, you know, a price was agreed upon and it moved or maybe there were early pay discounts that people were missing out on. Or, you know, some vendors get anxious and they submit the same invoice twice and maybe you might pay it twice. Or even contracts, they move and no one really checks them because they weren't up to date on that vendor's invoices. So, let's think about it a different way. You know, a a backlog isn't about work that's late. It's about work whose answers changed while it was waiting. And you know, it's not just that you're behind on processing. It's that when you

**[2:44](https://www.youtube.com/watch?v=0McYRNmVFFA&t=164s)** get around to processing it, you're processing a version of the truth that already has changed. And now we're at an AI conference. You know how to fix this. Everybody does. They did. The idea they wanted to do was they wanted to take their invoice and stick it into an AI agent. And they could, they tried it, they watched it. You guys have probably seen it here or done it yourself. You submit an invoice and you see the magic that happens when when when uh Chad uh Chad GBT or Claude returns that invoice with all the information correct. It's amazing. Now, nobody didn't know that, you know, this technology exists. They did a pilot. It worked. The thing was that no one would sign off on it as how we do business these days. So again, what's the what's

**[3:34](https://www.youtube.com/watch?v=0McYRNmVFFA&t=214s)** the what's the problem there? The problem is that you I mean you can see it in the numbers which is we did a survey 37% of our customers name security is the single biggest obstacle to adopting AI and yet they turn around and 92% of them already say that AI is core to their business. This isn't this isn't uh an adoption curve. This is a permissions problem. So, as deployments go, you know, the thing is some people solve half of this problem, but uh what they what they don't do is they they end up with um it's the they'll go ahead and they'll find out that once they're past the the the

**[4:22](https://www.youtube.com/watch?v=0McYRNmVFFA&t=262s)** once they're past the uh the pilot, they'll find that it just stops. And again, it's because no one can sign off on it. It's it's really a permissions problem. So what had to be true for this health system to let them actually start working this invoice process and it's not a question of extraction because it it's that every AI action needed to be governed and audited and without that u without that it it really wasn't about extraction accuracy. So every AI action runs on one governed path with full accountability. And that means that somewhere down the road when someone's trying to look into something that went wrong because you know agents they're mostly right occasionally they're going

**[5:09](https://www.youtube.com/watch?v=0McYRNmVFFA&t=309s)** to be wrong but if you can't actually show where they worked and where they didn't. If you don't have that audit trail it's not going to work. And so really by putting auditing and guard rails in place, you're turning that they're turning that audit into just a simple query, not a full investigation. And of course, when they did this uh when they did this actual uh pilot, uh the extraction rate was actually 100%. And that's not us. That's just models being amazing. And that's part of why we're here today. But >> when you put an AI gateway in place, when you can actually do guard rails and accountability, what changes is uh is is is the actual work behind it is pretty plain. Um you

**[5:57](https://www.youtube.com/watch?v=0McYRNmVFFA&t=357s)** know, documents arrive, they get read, uh the fields come out, they get checked again against purchase orders, and then when there's problems, they go in front of a person and the person figures it out. The steps didn't change. It was really just that one piece underneath that let this go from a pilot to something that actually worked. And by working that 6th to nth month queue, it it can finally run at the speed that documents arrive. And it doesn't slowly work itself down. That queue just collapsed. And it it was it was really about just being able to process those documents as they come in came in and not about how fast they could hire people and train them. But the fun part about this was it

**[6:45](https://www.youtube.com/watch?v=0McYRNmVFFA&t=405s)** showed what the what the backlog was actually costing them. And it wasn't it wasn't what you were expecting. It's it's actually 2 to3 million a year again on 50,000 invoices. And I want to be precise about where it came from because it wasn't labor. They didn't cut anybody. This was purely about money that was leaving from documents sitting in the queue all that time. I mean something that everybody thought was normal 6 to9 months they were dealing with it. But the real number was inside that weight. There was a cost number to it too and that was a ratio rather than a percentage which is is why it's worth

**[7:33](https://www.youtube.com/watch?v=0McYRNmVFFA&t=453s)** it's looking at the cost to process a document fell by somewhere between 10 to 60 times again not a percent 10 times thing is a percent will make you work faster the process you've already got you make it work faster when you're working 10 times faster or 10 times cheaper. You stop deciding about which invoices actually need that extra effort because the extra effort doesn't cost anything more or doesn't cost anything that you're willing to to conserve. So everything can get the careful treatment. Now one thing about this, we didn't make this system for them. We made it for us. Work for Blue Prism. It's part of SSNC. We're a financial company. We're a

**[8:20](https://www.youtube.com/watch?v=0McYRNmVFFA&t=500s)** healthcare company. And we needed this first. So it was us working inside a regulated industry that wanted to use things like AI agents, but we couldn't because we could not show our auditors how everything was being done. So putting this system in place lets us get to that point and this is what we're in turn uh providing to our customers. So this is the important part. whatever you build or buy, you need to put one path between uh your people and every model you allow. Now, it's not per project, it's per use case. And it's got to be one path because if it's two, they're just going to find the other one. And the other one is the one that's usually not being watched. But on those paths, on that one path, both directions going

**[9:11](https://www.youtube.com/watch?v=0McYRNmVFFA&t=551s)** out, you need to strip things that can't leave. That's like PII. um uh any any sort of confidential information that's on there. And when things come back, you need to score it the same exact way. You need to flag what can't be trusted, but more importantly, you need to keep a record of the entire exchange. It's that record that lets you pass your audits. And again, most homegrown versions, they usually do about half of this. And it's it's the whole thing that makes it work. But the important part is to scope it by use case. It's not about your programming. You come up with the use cases. So, uh, accounts payable can have their own systems with their own models with their own rules. HR is probably going to have a different one. They've got different models. They've got

**[9:59](https://www.youtube.com/watch?v=0McYRNmVFFA&t=599s)** different rules. The point is you spin those things up per use case. And then as models change, we see models change all the time. They can change under the hood, but your enforcement stays the same because it's not something you need to reprogram into your software all the time. It's simply that wrapper around how you talk to the models themselves. And the important thing to notice about this is what it's not. It's not a policy document. It's not a committee. It's not a AI ethics statement. Now, those things are all good, but they're not going to stop your data leaking out. It's it's getting something put in place at the point of use and that's what makes the enforcement actually work. So what changes here is not so much that AI arrives because it was already there. You all have it. You all have it

**[10:46](https://www.youtube.com/watch?v=0McYRNmVFFA&t=646s)** working. You know it's there. That's why the pilot was success a success. But the reason things don't get implemented and we've see all those surveys about how things die after the pilot. It's really about auditing to be putting these guardrails um in place is what lets you move from the pilot to an actual successful implementation. And the entire gap on that is really just someone feeling confident enough to put a signature on it. That was the only thing for this this healthcare system was someone being willing to sign off on the fact that this is how AP is going to run now. And then they move from pilot to production. So the thing to take out of this is you've got a queue somewhere. Go find it. It's not about fixing the steps in

**[11:34](https://www.youtube.com/watch?v=0McYRNmVFFA&t=694s)** the queue. It's about allowing yourself to work with the technology that exists today. That's what you want. It's it's the things that are decaying inside that queue you're never going to see until you actually start this working. So, this is um this is all about um SSNC's AI gateway. SSNC's right across the hall. If you walk out, we're we're right over there. Please come visit us. Our booth, it's booth 140. I'd be happy to talk to you about it. And any questions here or outside, I'd be happy to happy to answer. So, where's your six-month cube? That's what we'd like to work on. [applause] Thank you.
