---
id: PXj0p_mW9nI
title: "Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic"
slug: tokens-should-have-jobs-katelyn-lesse-angela-jiang-anthropic
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Tokens Should Have Jobs", "Katelyn Lesse", "Angela Jiang"]
channel: "AI Engineer"
duration_min: 13
published_at: 2026-09-14T14:00:06Z
video_id: PXj0p_mW9nI
url: https://www.youtube.com/watch?v=PXj0p_mW9nI
youtube_url: https://www.youtube.com/watch?v=PXj0p_mW9nI
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Science, healthcare & applied ML"]
transcript: true
---

# Tokens Should Have Jobs — Katelyn Lesse & Angela Jiang, Anthropic

**Tokens Should Have Jobs, Katelyn Lesse, Angela Jiang**

`AI Engineer` · `AI Engineer` · `2026` · `13 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=PXj0p_mW9nI) · [Conference site](https://www.ai.engineer/)

## Description

Given the same fixed budget of roughly 600,000 tokens, an agent that did nothing but execute scored 76 on a bench of financial analysis tasks. An agent that spent part of that identical budget asking a second agent for advice scored 89. Same tokens, different jobs, better answer. Katelyn Lesse leads platform engineering at Anthropic and Angela Jiang leads platform product, and their talk goes after an assumption buried in how most teams tune agents: that every token is fungible, so the only lever worth pulling is a bigger budget. They propose giving tokens jobs instead. An advising strategy splits an executor from an adviser it can call out to mid task. A grading strategy defines what good looks like as a rubric up front, then provisions a grader that scores each attempt and sends the executor back to iterate. A dreaming strategy reads the executor's own transcripts, writes findings to memory, and hands them to the next run.

The sharper result comes from rescoring that bench the way a working analyst would. A profit and loss statement that is 80 percent accurate is not 80 percent useful, it is useless, because you cannot make up a cost number. So anything short of a perfect run counts as a failure. Under that lens the execute baseline passes about 42 percent of the time, which means roughly three runs to land one clean answer, and about 1.8 million tokens of true cost. Advise and grade reach the same place for considerably less. Which strategy wins depends on what you are optimizing, because token efficiency and single run reliability point at different answers.

Speaker info:
- https://x.com/katelyn_lesse
- https://www.linkedin.com/in/katelynlesse/
- https://x.com/angjiang
- https://www.linkedin.com/in/angelajiang/

Timestamps:
0:00 - Are all tokens fungible?
1:34 - Giving tokens jobs other than executing
2:25 - Advising, grading, and dreaming
4:28 - The financial analysis bench
5:45 - Holding the budget constant
7:00 - Why 80 percent accurate is useless
8:42 - The true cost of a perfect answer
10:34 - Building strategies from primitives

---

Watch along with the corrected transcript, summary, timestamps and resources on this talk's official AIE page:

Join our upcoming AI Engineer conferences (see https://ai.engineer landing page):

- AIE New York, October 12–14 — the first AI Engineer Finance mainstage summit
- AIEi Shanghai, November 5–6 — the first for meeting top Chinese labs and engineers
- AIE CODE in SF, November 10–12 — the top AI Coding conference returns
- AIEi Sydney, December 7–8 — the first AIEi run alongside NeurIPS 2026 in Sydney

---

## Transcript

*2,657 words · source: supa (en, exact timings)*

**[0:19](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=19s)** Good morning. We're super excited to be here at AI Engineer with all of you. I'm Caitlyn and I lead platform engineering at Anthropic. >> And I'm Angela. I lead platform product at Anthropic. And today we want to talk to you about a concept that we've been spending a lot of time thinking about and working on with our team, which is this idea that we think that tokens should have jobs. So if you're building an agentic system and you're trying to accomplish some specific outcome, you're trying to get something done with agents, there's one lever that everybody pulls in order to get a better outcome, and that's usually increasing your budget, which means you spend more tokens or you spend more expensive tokens. But we've been wondering is that all there is underlying this assumption of uh using the budget is this kind of

**[1:06](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=66s)** implicit perspective that every single token is basically fungeable. And we've been wondering is that actually true? Are all these tokens actually fungeible? And to test that, we've been thinking, what if we gave tokens jobs? So, if you think about the way that you would normally set up an agent to go accomplish a task, you give it that task, you give it this token budget, and then all the tokens that are being spent are basically indiscriminate in the sense that they're all doing one job. They're just executing. But what if you take some of those tokens and they're not just executing, they're doing some other job. So, for example, maybe you take some of your tokens and they're advising the tokens that are executing. Or maybe the tokens that are executing try to get something done well and you take some other tokens and you actually grade how well the executor is doing so that it can iterate

**[1:54](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=114s)** and try again. Or maybe you have tokens that are dreaming. They're reflecting back on the job that other executors have done and writing learnings to memory so that they can do it again. And what we call each of these if you take some tokens that are executing and some tokens that are doing some other job. Let's call this a strategy. So let's go take a look at the first strategy, the advising strategy. Here we're splitting up an executor and an adviser. The executor obviously executes, but crucially they can call out to an adviser for advice. And then they can take this advice and figure out if they're doing the next step correctly. This is really helpful in use cases. For example, if you're building a sales agent, in an ideal world, you'd have that sales agent be able to actually help the sales rep flag when a follow-up is overdue or deal is stalling. In this construct, having an adviser to be able

**[2:44](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=164s)** to kind of make sure that all the different pieces are actually working is really helpful. So another example is grading. Let's say you're executing and you kind of know exactly what good really does look like. You can define this in a rubric and then each time an executor tries to accomplish that outcome, you can have a grader provisioned that grades how well the executor did while looking at that rubric. And if the executor did a good job, then great, it can be done. But if it didn't do such a great job, you can iterate again until you get that good outcome. So an example in practice of when you might want to use this is let's say you have a customer service agent and you're running a store and your customers are writing in and they're saying, "H, I should get a refund for this thing." And your customer service agent needs to be able to respond. You probably have some

**[3:31](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=211s)** like pretty specific criteria on when you would give somebody a refund. And so what you can do is define a rubric that uses that criteria. You can have a grader that goes and looks at the work that the customer service agent is doing and decide is it getting it right and is it coming to the right outcome. And the last strategy we have is dreaming. So in dreaming there's an executor who naturally executes and then there's a dreamer. The dreamer is actually able to inspect the work and the transcripts of the executor and then it takes any of the findings that it has and it writes them to memory. This memory is repicked up by the executor for the next round. So ideally would have improved. A great use case for this is if you're building a recruiting agent. Now recruiting requires a lot of interaction with feedback on whether or not a candidate does or doesn't make sense and if it's a good fit between both parties.

**[4:19](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=259s)** And so by taking all this type of data, if you build a dreaming type of strategy on this agent, it's actually able to kind of sharpen the next round so that it's more and more increasingly useful. So let's make this concrete with some experiments. So what we did was we created a bench of a bunch of tasks related to financial an analysis. And what we were doing with each of these tasks is trying to replicate in the real world a expert human financial analyst. How well would they do on each of these various tasks? And so what we did was we start with a control that's just executing. Let's try each of these tasks and we'll eval them when we're literally just executing. But then we can experiment with each of our strategies and see how well we perform. So, we start with a super basic experiment. Let's just oneshot it. Let's take each of our strategies and we'll go and just make an attempt to accomplish

**[5:07](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=307s)** these tasks and we'll see how accurate we are. And so, you can see here with executing um it didn't do so well. 15% accuracy, but because it was just a oneshot, the strategy got to choose how many tokens it would actually spend on its own. And so, you can actually see that execute decided not to spend that many tokens, only 39,000. And as we go into our larger strategies, our more complex strategies, we did choose to spend more tokens, but we did a better job. So, this isn't really telling us much because sure, Drain did really, really well, but it used a whopping 600,000 tokens to get there. That's right. So, in order to actually figure out if varying the jobs produces any alpha, what we need to do is hold the budget constant. And to do this, we're going to take Dreaming's budget, that 600,000 or so, as the maximum budget that is fixed across the board. And we give every single strategy this budget

**[5:55](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=355s)** in order to analyze how well it's performing. And as expected again, if you give a lot of strategies more budget, you are going to see performance increase across the board. So execute went from 0.15 to 76. Advise and grade went from the 60s to closer to the 90s. And that's again expected given the fact that if you give things more test time compute, they should generally perform better. But if that was the only thing that mattered, we should actually expect to see execute, advise, grade, dream actually all be at the exact same level given the exact same token budget. But what we're actually seeing is that there is an alpha or there is a difference and therefore an alpha for us to exploit. If you look at execute at this exact same budget level, it gets to 76 but advise is at 89. So while a minimal, it does exist and so there is alpha for us to take a look at.

**[6:44](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=404s)** Now, we decided to take a look at this analysis from a completely different lens. And as Kayla mentioned, you know, we're doing this bench for a very complex set of financial tasks in the real world. And we wanted to analyze the usage of agents with actual experts. So, if we look at a financial analyst expert, right, the kind of task that they need to do with an agent is that they're giving it something very concrete like let's say make a P&L and then they're getting the result back. Now if that result is 80% accurate on a bench that sounds great but in reality what that means for that expert is they have to go back and recomputee that P&L themselves or alter or alternatively send it through another run and that's because in this kind of domain for this kind of task if you're not 100% accurate it's actually not useful. You cannot make up an income number or

**[7:32](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=452s)** you can't make up a cost number right you have to make sure that it's 100% accurate. So with this lens of the real world consequence associated with this domain, we needed to recomputee our experiments and score them a bit differently. Crucially, we needed to make sure that our experiment had this kind of construct where if it was scored perfectly, we'd actually give it a pass. And if it scored anything less than 100% on that kind of task, we would actually mark it as a failure. So let's look at a different cut of our data from our experiments with this lens where we're looking for this perfect run 100% accuracy pass. And let's look at what percent of the time each of these strategies was able to achieve a pass. Um so we we've got executes um down at 42% and we've got our more complex strategies doing a bit better up to 75% accuracy. Um and again this doesn't necessarily tell us a ton because um you

**[8:22](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=502s)** know each of these strategies might um choose to use different budgets over time, right? So what we did here was we fixed the budget and we said within a fixed budget, how well do each of these strategies perform? And so what really matters to us actually is if you're trying to get this perfect answer and you're in the real world, you're running a business, what matters to you is the cost to you to get to that perfect answer. And so one way we can think about this is we had our execute strategy for example. The execute strategy around 40% of the time will give you that perfect answer. So on average, you can expect to have to run it three times and you should hopefully sometime in those three runs get a perfect answer. And as we talked about earlier, we fixed our budget to that highest token budget strategy, which was 600,000 tokens. So if you spend 600,000 tokens in each individual run, you have

**[9:11](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=551s)** to run approximately three times. You can expect on average to have to spend 1.8 million tokens with the execution strategy to get to your perfect answer. And so if we take this analysis and run it across the board against all these strategies, this is actually the true cost it took in this domain for that agent to be useful for that strategy. So as Caitlyn mentioned for execute, which is our baseline, this is going to be 1.8 million true total token cost for you. But advise, grade, and dream are showing us a bit of difference. Crucially, advise and grade are actually quite token efficient when you think about the actual usage of the end output of each of these agents. So what does this mean for you as a business? Well, it actually really depends on what kind of thing you want to optimize for and it's going to vary,

**[9:58](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=598s)** right? There's going to be businesses who say, "Actually, for me, the most important thing is to be really token efficient. In that case, you should probably pick the advised type of strategy in order to solve for that particular domain in which you want to optimize that." There's going to be other areas or other businesses where you're going to say, I'm not going to care so much about token efficiency because what I really care about is reliability of that answer and so I need to maximize the percentage of runs in which I get that perfect answer. In which case, you would actually pick completely different strategies. You probably lean towards grade or dream. So if you take away one thing, the thing we want everyone to think about is this idea that tokens are not fungeible. You can use your tokens to execute. You can brute force your way through your task and you can throw more budget at it. But if you get really smart about having your tokens do these different jobs and try these different strategies, you're very very likely to be able to get a

**[10:46](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=646s)** better outcome for the task at hand within a fixed budget. And so let's talk a little bit about how we actually build strategies and how we bring this to life. Um so we've done a lot of work to create a really excellent harness for individual agents. Um and if you see this uh picture at the bottom here, this is actually the architecture that we've used for cloud managed agents um which is our Aentic solution that we give to you within the cloud platform. And what we do on top of this is we start to get into the meta harness level like the multi- aent orchestration and execution level where this strategy can go and be um coordinated between our executor and our adviser or the other agents within our strategy. And some of these um like dreaming and outcomes we actually give to you out of the box within cloud manage agents. So with those set of primitives it's

**[11:36](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=696s)** actually relatively trivial for us to construct this kind of you know architecture where we're able to combine these different types of strategies and figure out how to they should work together. So for example it's relatively trivial for us to say okay now with this I can take a task and I should be able to execute it but also allow it to advise and fable is back online. So we could actually say Fable is the one that's actually advising uh the executor. And then I can take all these results and say send them to a greater so that I can make sure that this is verifying in a loop that makes sense. And if it passes, that's awesome. I want to send all of that stuff to Dreaming and make sure that my next run is better than ever. And of course, you don't have to stop there, right? If the right primitives are there and the right coordination is there, then you can actually construct really complex setups that fit for all the different types of dynamic problems

**[12:23](https://www.youtube.com/watch?v=PXj0p_mW9nI&t=743s)** that you have. You can invent these kinds of large-scale architectures, again, very triv. And you could also invent completely new jobs, not just the ones of the pieces that Caitlyn and I have presented in this conversation. So, a big goal that we have over time is to get our models better and better and our platform better and better at dynamically constructing these strategies for you as you're doing work. But in the meantime, as we're working our way there, we would love for you to continue to think about this idea that you should give your tokens jobs and you should use different novel strategies by combining these primitives in order to get the outcomes that you want for your tasks. >> Thanks for joining us.
