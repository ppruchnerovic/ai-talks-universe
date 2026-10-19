---
id: cf2IhzqeQH4
title: "Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg"
slug: every-ai-company-is-accidentally-building-a-bank-dor-sasson
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Dor Sasson"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-10-07T00:30:28Z
video_id: cf2IhzqeQH4
url: https://www.youtube.com/watch?v=cf2IhzqeQH4
youtube_url: https://www.youtube.com/watch?v=cf2IhzqeQH4
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI pricing", "usage-based pricing", "AI monetization", "credits", "metering", "entitlements", "billing infrastructure", "spend caps", "token costs", "AI economics", "SaaS pricing", "Stigg", "Dor Sasson", "AI engineering", "AI Engineer"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Every AI Company Is Accidentally Building a Bank — Dor Sasson, Stigg

**Dor Sasson**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI pricing` `#usage-based pricing` `#AI monetization` `#credits` `#metering` `#entitlements` `#billing infrastructure` `#spend caps` `#token costs` `#AI economics` `#SaaS pricing` `#Stigg` `#Dor Sasson` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=cf2IhzqeQH4) · [Conference site](https://www.ai.engineer/)

## Description

In one month, three of the biggest AI companies had a pricing emergency. Dor Sasson says it was really an infrastructure problem.

Dor Sasson, co-founder and CEO of Stigg, argues that every AI company is accidentally building a bank. He starts with the April pricing scramble, when Anthropic cut third-party agents like OpenClaw off its subscription plans, OpenAI changed its Pro tier, and GitHub pulled free Copilot access, plus stories of companies burning through their AI budgets in weeks. The common problem: usage gets checked after the invoice, not before. He makes the case for checking entitlements synchronously before inference and settling asynchronously after, like an ATM, and points to OpenAI's own published architecture. He covers the banking ideas AI products now need, from hold-and-settle and double-entry bookkeeping to credit sources and spend caps across teams, users and agents.

In this talk:
• Why AI pricing emergencies are really infrastructure problems
• Check before you spend: synchronous checks, asynchronous settlement
• Concurrency, double spend, and drawing down from different credit pools
• Four patterns for selling AI at scale, from reserve-and-settle to spend visibility

SPEAKER
Dor Sasson, Co-founder & CEO, Stigg

LINKS
Stigg: https://www.stigg.io
Stigg on X: https://x.com/GetStigg

CHAPTERS
0:00 Intro
0:37 Every AI company is building a bank
1:17 April's pricing emergencies
2:52 Case: Anthropic and OpenClaw
4:02 It's not just Anthropic
5:02 Checks happen after the invoice
6:27 Check first, settle later
7:32 The ATM analogy
8:11 How OpenAI built it
9:21 Three takeaways
10:31 Concurrency and double spend
12:16 Which credits get spent first?
13:31 Budgets, hierarchies and spend caps
14:46 Four patterns
17:50 A pricing change that was really infrastructure
18:35 AI's Stripe moment

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*3,385 words · source: supa (en, exact timings)*

**[0:12](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=12s)** Yeah, we're good. Okay. So, hi everyone. Given there's I hear there's a match right now as we speak. So, given that you are here means a lot to me. So, at least I'm I'm winning the World Cup right now. So, that's that's a that's a big thing. Thank you for joining me. I flew all the way over on co-founder CEO of Stig. I flew all the way over to make a kind of a funky statement on an AI conference which is literally every AI company right now is accidentally building a bank. And when I mean bank, I'm going to try to kind of unpack this thing not as like a weird marketing metaphor, but effectively what what is really happening right now with the AI economy and why a lot of the constructs and the things that we are seeing using consuming and paying for in AI are actually

**[1:01](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=61s)** really behaving like constructs that we know from the banking financial systems. So, cool. Thank you for for for having me. Um and let's get it going. By the way, I'm the first talk today. So, the clicker is not working. It's going to be interesting here and out as they move for this. So, let me take you through a little bit of background. As I was working through this talk back in April really every single code generating product platform out there just broke under this new type of economy and under this new type of consumer behavior. And in just a you know, matters like 5 weeks everything felt like pricing emergency one after the other. And the case I want

**[1:49](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=109s)** to make here is that these pricing emergencies go way beyond just emergencies from a financial commercial set of the house. These really are infrastructure emergencies that are emerging because of how those systems were built to begin with. So, just to give you some perspective, we had in in April we had Anthropic basically eliminating access for Open Clo and other third-party agents to basically use the subscriptions plans. Then immediately we had OpenAI basically changing how the product here is being priced, bumping the price overnight 5 5x, which is quite intense. And then we had GitHub freezing and then completely eliminating access trial access free access to their We have some echo here. To their free plans for for for Copilot.

**[2:39](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=159s)** And effectively like all these companies all at once in a single month experienced what it means to actually scale on scale AI and what actually happens when you don't have the fundamentals in place. So, let me take one one step farther. So, let's zoom into even just one of the use cases, right? So, if you think about Anthropic and you think about the Open Clo use case, right? What happened was effectively Anthropic was subsidizing every consumption of every user using Open Clo within the Clo Clo Max subscription. So, effectively what the customers were paying daily was, you know, dollars and cents. But on the on the cost side for Anthropic, it was like 150s to even 750 subsidized, which is effectively not an

**[3:30](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=210s)** economics that you can scale even for the company at at the size at the scale of Anthropic, right? So, what it seemed to be a business problem really was an infrastructure problem because Anthropic didn't have a an effective way to delineate between users who are using their APIs and users who are using their subscription um, uh, programs. And so, they had to immediately cease and stop access, right? They had to to to react. Um, cool. So, and this is not unique to Anthropic, guys. Like, uh, we're seeing this like, I don't know if you all heard read the news most recently with a company, uh, undisclosed company burning through like half a billion of their AI, uh, cloud credits,

**[4:17](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=257s)** um, just merely having like a few employees burning through the entire organization contract. Uh, we had, uh, Uber saying they're basically torched down their entire, uh, AI usage consumption budget for the year in just a few weeks into the year. And then we had Rep- Replit giving an example of what could happen if, uh, a single org has three users that basically burning down the entire credit pool for Replit for the entire org. So, really what happening here is, uh, this is not just an an an Anthropic problem. And I think what's what's mutual and kind of like switching gears from the examples to the actual what's really happening here, um, the problem basically with with all these three examples is that the checks for what you're entitled, what you're

**[5:05](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=305s)** allowed to do, whether you're an agent or a user, we are AI product happened, uh after uh, the invoice and not before. So, basically with each and every one of those examples, you were allowed to consume, you were allowed to use the product, you were allowed to burn tokens, and checks happen only after the invoice. So, basically the spend and the aftereffect gets reconciled only after it's too late, only after the invoice is is sent, and this is effectively bad for business, it's sticker shock, it's bad for practice of how we use these systems. These systems are now mission critical, and we're basically none of these companies had in place the financial infrastructure that allows, exactly like banks, guys, to check before we draw down, before we consume, right? So, I think what what we're

**[5:54](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=354s)** seeing is effectively uh really is a change in how we architect, and how we ship, and how we build software. AI is not just changing what is value, is not just changing how we interact, who is the users. It also effectively changing what exactly is getting paid, and how we actually architect for systems that can uh handle runtime, handle the complexity of usage happening before the the the invoice, before the checks, and how we actually can architect for that. So, I think what's interesting, and what you see in front of you um is basically on the left side, what we're seeing is how most teams ship this architecture today, and you can see that basically the check and the settlements are happening after after the inference, after the usage is

**[6:43](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=403s)** being logged. And that's typically too late. We see situations like spikes, overspends, overages, like experiences that are bad for business, bad for your users, and quite frankly, in many cases, also bad for the vendor. Because if you didn't allocate enough resources and compute to actually allow for this to happen, you you also have a margin problem potentially, right? On the right side, we're basically saying, or I'm trying to make the case for you all that with AI, with the current infrastructure, and how AI is being built and sold, we actually need to enforce and and do this synchronously before we actually update the balances, and reconcile and settle in in async way after after effects. So, hot path actually get checked synchronously, and

**[7:31](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=451s)** everything that comes after uh is basically reconciled after. I think the best example, guys, is if imagine you go to the ATM, right? And you draw cash. When you draw the cash, it that the check if you are allowed to draw it, doesn't happen after you get the cash. It happens before you draw the cash. And so, that's exactly the same thing. Our industry effectively misses this layer, this financial infrastructure that allows for this type of behavior to happen naturally right? And so, obviously this sounds like a great idea, though, right? Like you're you're pitching this infrastructure, sounds like you have something to do with this. Um But guys, this is not just me. Uh in February, OpenAI, they have a quite a great team. They're team called financial engineering. And these guys basically

**[8:20](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=500s)** published how they think about the architecture and what they had to build for this to work at the scale of OpenAI. And what they had to say reads very similarly to how transactional systems of banks work. Basically, you have a decision waterfall that needs to consider in runtime what is the client, the user, the agent is allowed to do. And it needs to take into account many different conditions and policies of what is really allowed, right? So, are you allowed or you have access to a certain feature or product? What are the certain rate limitations under your plan? Whether you are in a trial or in a certain promotional program. Like you need all these decisions to be calculated immediately at front time. And then it ultimately decide, can I

**[9:09](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=549s)** give this user access? Can they draw down? Can they consume or not? And all those decisions really can happen after the invoice. They can't because you need to actually be able to calculate and prioritize this. So, I think we have three things to notice from here, right? The first thing is this is a single synchronous evaluation. It happens at the request. It doesn't happen after effect. I think the second thing is the priority is deterministic. So, we know in advance what are all the different rules that apply for certain things to be consumed, right? And I think lastly, and here you guys, this is my opinionated view, you can disagree. I don't think this is billing. I don't think this is necessarily this entire architecture is just related to the idea of invoicing and billing.

**[9:56](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=596s)** This is a financial system that actually make decisions ahead of any invoice, ahead of any billing element. And I think we're going to see more and more of this becoming a standard for other products and other AI systems as well. Really just nerding just a little bit on I'm sorry, I just skipped one slide. So, yeah, just just nerding just a little bit about what other trades or or elements we see and are used to in banks and we take them for granted, but in AI they're not that granted, in software they're not that granted. So, just one example, right? Like if two separate parties have access to the same banking account, and that banking account has like $10, and they are entitled to draw down those $10. What happens and when they both of

**[10:45](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=645s)** them try to draw down at same time, right? So, banking systems has the idea of holding, of settling. You can really the concurrency is effectively solved with banks, but with AI and agents, it's not that case. You could have whatever, like 10,000 agents trying to reach out to the same dollar pool, and they're going to try to do that all at once, and superficially it might look like they should be able to draw down because there is balance in the pool. But, what happens when they all draw down from the same pool simultaneously, concurrency become an issue. So, how do you solve for that? This entire idea in financial systems actually called like it's a classic double double spend problem. It comes from the accounting world. It's a double entry bookkeeping, and as I'm sure you all are building

**[11:33](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=693s)** shipping today with AI as the revenue scales, as your company scale, the idea of double entry accounting, double entry billing, the idea that you can solve concurrency, these things would matter as you scale and they're not so easily solved down the line. So, think about things like you know, can you basically introduce rates like hold and settle, think about idempotency and auditability of those uh requests and etc. Another thing that I think is very very known in in you know, how banking systems works but not not necessarily enough established in AI is the idea that all the different pools have different sources, right? So, in bank you have

**[12:20](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=740s)** your debit account, you have your cash account, you have your savings, right? And if you draw down, the bank actually knows how to calculate where you drawing down from and what does it mean? Here, you know, say I have a pool of you know, one you know, 1,700 credits but they're not the same, they're not alike. Each one of them is sourced from a different source. So, how do you decide which which one of them do you draw down against? Do you start with the ones that were you know, given granted earlier? Do you start with the ones that were promotional? So, how do you really calculate what's getting drawn down to the users? I think that's that's a real problem. Most companies today try to solve it like a single integer databases and that's not really going to work as you think forward.

**[13:08](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=788s)** Cool. Um so really tying the knot the knot here, I think if you think about how we interact with software, it used to be flat. So, it used to be just users and organizations and there wasn't a lot of meat in between them, right? The the the hierarchy of you consume software was quite flat. It was quite straightforward in terms of who see the value. But today, I think effectively credit pools are no longer flat. Uh you have a lot of different hierarchies in between who consumes different credits, and also they demand different governance, different logics, allocations, budgets, spend caps. And effectively, what happens is that budgets are set at the top, where for instance, if you're selling to the enterprise, you're maybe selling like pre-commit annual contract.

**[13:56](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=836s)** Uh C-suite or somebody who approved that seven-digits contract, they expect to see how that credit are getting drawdown along the contract life. But they don't just want to see that they were used. They want to know who actually used them, which team, which users, uh which agents, uh to what extent, and they want to have fine-grain control over that. That's literally the bare bones of how more and more companies thinking about selling AI workloads and how they they effectively work in production. I'm going to run through some of this. Um I think this idea of like what does it mean like high cardinality graphs and dimensions, being able to slice and dice against model types, users, like all this type of uh dimensionality of uh of uh consumption is is probably

**[14:44](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=884s)** interesting to to talk about. But what I actually want to expand on is ultimately those four patterns. So as you build AI and start selling AI at scale, you're effectively like four patterns that keep repeating themself, and they are very very much alike and and very similar to the idea of, you know, banking systems. I think the first one we talked about earlier is basically being able to reserve before inference and settle actuals after. Um this is like going to to be like a pattern that again and again we're seeing more and more often, and it has ramifications on how you do accounting, how you do uh basically handle all those uh different concurrencies workloads and what have you. I think the second thing is we're seeing more and more AI companies unexcited about the idea of sending all this usage data to to somewhere else over the cloud. For latency reasons, for

**[15:33](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=933s)** cost reasons, for data sovereignty reasons, there's a lot of good reasons for why these companies actually rather to keep the events data inside their VPC, and I think we're going to see more and more AI companies seriously considering deploying this this architecture, this ledger, this metering within their VPC rather the the contrary of sending it over the internet. I think for agentic checks, so think about how agents spawn, the idea of checking balances when agent does something you don't know in advance what they're ultimately going to do, how that how that task is going to basically cost. So, if you don't know the cost, you need to be able to check those balances as the agent continues to get work. And you need to be able to reserve an account for them in advance and then

**[16:20](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=980s)** asynchronously after effect reconcile. Quickly moving forward, so ultimately if you have those systems in place, what you really gain out of it is visibility. So, it used to be given that for usage-based products you need visibility, but I think what happens today, you know, it goes beyond just plain visibility. It it means that effectively like the ability to see for CFO, for CIO consumption of AI workloads across different models, across different features, across different products is not just, you know, a nice to have. It's becoming a table stakes. It becomes something that you can't do business without, and we're going to see more and more companies expect to have this off the bat before they actually do business with you.

**[17:07](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=1027s)** And so really just giving some examples to how some of the best frontier AI companies are approaching some of this, I think you're you're seeing the patterns already there. So, I think a lot of these companies already appreciate that you're no longer just selling software in the you know, commodity way that we used to think about subscriptions and usage. It's becoming more and more of a financial systems and financial systems require some of these complex ideas that weren't we're not there before AI. Um and I think just to give like one small example that I talked about earlier, but I think might have gone a little bit uh hidden. Um One of the changes in April that OpenAI did is really they didn't change the pricing. All they did was change the

**[17:54](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=1074s)** pace in which tokens get burned. So, effectively you use the same model, we pay the same cost uh per unit, but we burn more tokens. So, that effectively was a pricing change. How do you execute such a change? Um because it's not just financial change, it's an infrastructure change. You're basically change the rate of how the software gets consumed. So, there's a lot of complexity not in terms of just how we change pricing, but also how the infrastructure underneath allows for more complex ideas into how value is getting uh uh introduced to the users. And really just, you know, before wrapping up, you know, there our team likes to say, and this is something we started to say more and more often than before, it really feels like you know, there was in the in the early 2010s there was this Stripe moment where every company wanted to ship product

**[18:41](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=1121s)** into the internet and you need a checkout and you need it to be secure and it and the developers need to to to to to make it easy for them to quickly get them up and running. I feel like where we are today is those ideas of like building a banks, it's okay if you feel like, I don't know, you like wearing suit and tie, maybe you want to build a bank, but if you are a building a bank, you probably want to be aware to all of these traits and elements that has to be there so you don't meet them down the line where where it's get really, really more complex to fix in a hindsight. And so, feels like the industry really misses its Stripe moment where all these constructs just exist and it's they're so easy to use. And you know, there's a lot of excitement from our team when it comes to the potential of having such systems ready and help AI companies keep shipping. Um

**[19:29](https://www.youtube.com/watch?v=cf2IhzqeQH4&t=1169s)** if any of that was interesting, really come by our booth. We are in a quite of a weird location right at the start, but still there. I know there's a game right now. Come visit. We're demoing the product. Feel free to ask any questions and thank you for coming today. It was awesome to to have you have you with me. And yeah, love to nerd some more by our booth.
