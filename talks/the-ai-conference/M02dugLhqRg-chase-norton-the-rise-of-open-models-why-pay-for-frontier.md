---
id: M02dugLhqRg
title: "Chase Norton: The Rise of Open Models: Why Pay for Frontier?"
slug: chase-norton-the-rise-of-open-models-why-pay-for-frontier
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 13
published_at: 2026-10-07T23:09:11Z
video_id: M02dugLhqRg
url: https://www.youtube.com/watch?v=M02dugLhqRg
youtube_url: https://www.youtube.com/watch?v=M02dugLhqRg
tags: []
topics: []
transcript: true
---

# Chase Norton: The Rise of Open Models: Why Pay for Frontier?

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=M02dugLhqRg) · [Conference site](https://aiconference.com/)

## Description

Most engineering orgs default to frontier models for everything. In this session, I'll walk through the routing policy Faros built and validated on hundreds of real engineering tasks, using an execution-free eval framework that works across any codebase without test infrastructure. Open models matched frontier quality on most task types at roughly half the cost. You'll leave knowing which tasks still need frontier models and why. Plus how to run the same analysis on your own work.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,176 words · source: supa (en, exact timings)*

**[0:14](https://www.youtube.com/watch?v=M02dugLhqRg&t=14s)** All right, testing, testing. We are live. Hello everybody. I am Chase Norton with uh head of AI at Ferros. Today we're going to be talking about kind of what we've all been talking about, which is we have these open-source models. We have frontier models. We have exploding budgets. We all want to have our agents running 24/7. Intelligence everywhere. You wake up, they've done things for you. However, that reality is conflicting with budgets in a company. You wake up, you spent $2,000. Somebody pings you and says, "What is this $2,000 for?" You have to justify it. You have to say, "This is where it's bringing value into the company." So, what we're going to dive into here is, can you produce value with open source models? When do you choose between Frontier and

**[1:03](https://www.youtube.com/watch?v=M02dugLhqRg&t=63s)** open source or open co open weight? And so, let's dive in. Just to kind of give a framework for some of the terminology when we talk about a route to us a route is the combination of a model, a harness and the configuration of those. No longer is it the case that models just kind of exist on their own as we all know. No longer is it enough to just look at which model is best, but we have to actually be looking at the model harness relationship. Right? As you can tell, OpenAI just kind of released that they've been doing a lot of harness specific improvements and optimizations to work with their latest models. This relationship is only going to get stronger. And the more that we kind of need to look at producing outcomes and value in a company, we need to be

**[1:50](https://www.youtube.com/watch?v=M02dugLhqRg&t=110s)** looking at this relationship together. So when we talk about a route, we're talking about this combination. When we talk about a task, you can think about it as a PR, some kind of work that goes in that then or some kind of uh task that goes in that then needs to produce value for the company. So what we do what we did is we took seven different routes and and really we've done this across many more but for this one experiment we took seven different routes looking at different combinations of let's say opus and open code opus and cloud code different versions of the uh open AI models in codecs and all the different harnesses and or really the top ones that are available today and we said, you know

**[2:38](https://www.youtube.com/watch?v=M02dugLhqRg&t=158s)** what? What if we were to take these and we were to run them across our own codebase. I I think there's a million different benchmarks nowadays where we all say like, okay, yeah, so this one said like this is at 86% cool, but what we really care about is how do those benchmarks apply to our company or your company, your codebase, repo by repo. You want to be able to run these benchmarks on your own code. And more importantly, you want to be able to run different routes to produce your benchmarks to say, look, maybe Infra needs this model harness combination. Maybe core engineering needs this, maybe our marketing team needs another one. Looking at these different uh relationships between model harness the route and where they produce value is something that we we do at Feros but

**[3:28](https://www.youtube.com/watch?v=M02dugLhqRg&t=208s)** it's also something that we created a technology that's called time machine what time machine allows us to do is it allows us to actually roll back the work let's say a PR and when we roll it back we can take it to its initial state and then from that PR we can play it forward in those routes. So we took those seven different uh routes that we created and we ran them across G G G G G G G G G G G G G G G G G G G G GPT 5.6 Kimmy K3 uh GLM models of course all the anthropic models to understand across our codebase what does this again time machine allow us to say and I don't think it's any surprise that at the end of the day we have 5.6 6 and really you can tell kind of like I made these about 3 weeks ago because we don't have now some of the latest models how quickly like we're

**[4:15](https://www.youtube.com/watch?v=M02dugLhqRg&t=255s)** we're moving but we're able to show that 5.6 six. It cost a little bit more. Not not a huge surprise, but that Kimmy cost a less. And then later we'll show it cost about 20% less. But the run time, even though we're getting cheaper for our openweight models, the run time was 16 minutes, almost 17 minutes. Whereas for GPT 5.6, 7.4. So cheaper, but longer to run. Now again, you may say like, Jace, that's okay. Got it. But it's really starting to internalize this these questions to ask the metrics that drive th that that answers those so that when you go back into your company you can say okay look there are times at which open weight models make sense. There are times that we actually were

**[5:04](https://www.youtube.com/watch?v=M02dugLhqRg&t=304s)** running a background task and honestly it doesn't matter about time. What we care more about is a 20% savings in our overall uh company or task. Again, this is something that our technology time machine allows us to do to roll back, play forward, play different whatif scenarios within uh for for our different routes. So, here we're seeing it's 33% or 33 cents more uh and about 10 uh but 10 times 10 minutes faster. we got time and we have uh we have overall cost but looking at it from a quality standpoint. So in time machine we have uh a score a rubric that gets generated that then gets evaluated across all the different harnesses all the different routes. And so what we're

**[5:53](https://www.youtube.com/watch?v=M02dugLhqRg&t=353s)** able to see is you may say okay we have a uh frontier as the top quality producing uh and really this top quality when we say like what does it mean to like have quality it comes down to looking at it as saying when this task is complete by an agent by a route how close is it to what the human would have done now we can say we want to be better than humans but at the end of the day our gold standard is saying this PR was merged in this PR produced value in the company this PR by this human we know was accepted as great. Let's let's put that as like the definition. If we know that then we can say how close to great how close to that human work were we able to achieve. Opus 5 point uh Opus 5 was the top contender but then very

**[6:42](https://www.youtube.com/watch?v=M02dugLhqRg&t=402s)** close to it even though it's at the bottom we're seeing openweight models now in the same rank in the same universe as Frontier models. cheaper, longer to run, but in the end it's close in quality. And we'll actually show that show that it competes across Opus and other models uh pretty closely if you look at the mean average. But what we were also able to do is say okay from this we can look at and understand that there is close enough in quality when we look at it we show 20% uh overall lower estimated AI cost that's great so when do we start to apply that again a lot of this talk is more about creating that framework and that

**[7:30](https://www.youtube.com/watch?v=M02dugLhqRg&t=450s)** discussion so that you go back and you say okay when we can run things slower where do we put this tech where do we put this intelligence and also I should say running slower was not because we weren't using the right uh GPUs or enough power it really is just the fact that the model harness across all harnesses they just asked themselves a lot more questions so the LLM just kept talking to itself reasoning with itself before it finally came to the same general output as frontier models that's only going to improve this need to continue to repeat itself or ask itself questions is only going to improve. So when we look at takes longer, that's something that I think very quickly we're going to be able to catch up with. So cheaper, soon to be on par with uh speed, but that's that that's yet to be

**[8:20](https://www.youtube.com/watch?v=M02dugLhqRg&t=500s)** shown. And overall, the quality is within a rank that we can start to think about where do we want to actually place this? And so if you look here across all the model across all of Opus all the harnesses we look at GLM across all of the harnesses we show very similar rubric mean rubric scores. Then we take it next. So now we've got into classification models. Classification models have of course always been here with us or been here for many many decades. But just recently we have Jev that comes out and Jev has kind of transformed how we look at or how we use classification mainly because of its quality. Its quality, its speed, its cost. But cost has always been fairly low for classification. But now we're actually able to again

**[9:09](https://www.youtube.com/watch?v=M02dugLhqRg&t=549s)** using time machine we're able to show okay when we look at let's say Astra is the best. Let's say Astra is a great frontier model. If we do that, and we did this across all the leading frontier models, but for this experiment here, Astra is a very capable model, how close can we get Jev, how close when we run soul, how close do they get to the classification uh quality of Astra? And we were able to show and I'm for for some that are using Jev I'm sure that this is no surprise but it is a massive impact to the industry when we think about classification. We look at soul 5.6 and we were at $8.30. We recently ran some classifications over AI sessions. A million of those

**[9:58](https://www.youtube.com/watch?v=M02dugLhqRg&t=598s)** sessions cost soul around $9,000. For Jev it cost $42. Where's the quality on it though? Jev coming in at 78% matching to what Astra's labels were sold at 89%. And again, you may say like, well, I want more. I I want that 89%. Okay, then then go pay the money. But if you can look at the price difference and the speed difference, it becomes very significant being able to run Jev. And there's open Jev. There's uh there's other open versions of Jev that you can also run that are even faster, right? And so being able to look at this, we look at the mean decision time between them. It's just they're in completely different universes uh when when we look at those.

**[10:45](https://www.youtube.com/watch?v=M02dugLhqRg&t=645s)** So as like really this talk is about we have now in front of us the ability to run openweight models both on device. We can have Quinn 3.8 27B running on my device here. We can run it on a spark. We can run it very very easily. When we look at bringing ROI into the company, when we look at this world where agents are running 247, where we want to wake up and have them still doing the work and we want it to almost be unstoppable, we have to actually bring the value into the company. We actually have to say, look, here's what my outcomes were. Here's where that $2,000 last night went. And when we start to look at that, the justification for an $80,000 budget becomes a little difficult. Some companies can, some companies

**[11:33](https://www.youtube.com/watch?v=M02dugLhqRg&t=693s)** can't. It depends on the outcomes of course. But when you look at where we're going with openweight models, we start to see that there is now a place for them. There is we can look at different tasks, background tasks. We can look at in our we have a desktop application and in that desktop application, it really just needs to process different data that does not need to be real time. It doesn't need to happen now. There is no synchronous call that's happening. All of that is now being processed on device. All of that is now being processed GMA 4B on device being able to process those sessions and that information and that data. So walking away from this, it's about the having that conversation whether or not it's me telling you here, it's us talking outside, it's wherever, it's the fact that as we move forward, solving the need for explaining your usage,

**[12:22](https://www.youtube.com/watch?v=M02dugLhqRg&t=742s)** explaining the value you bring to the company with your agents is going to become more and more necessary. And that is something that we at Ferros do very well. If you want to talk, please uh come outside and I'd love to continue the conversation with you. Thank you.
