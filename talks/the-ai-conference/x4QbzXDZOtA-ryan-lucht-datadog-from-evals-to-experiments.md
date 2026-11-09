---
id: x4QbzXDZOtA
title: "Ryan Lucht, Datadog: From Evals to Experiments"
slug: ryan-lucht-datadog-from-evals-to-experiments
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 11
published_at: 2026-09-29T17:56:19Z
video_id: x4QbzXDZOtA
url: https://www.youtube.com/watch?v=x4QbzXDZOtA
youtube_url: https://www.youtube.com/watch?v=x4QbzXDZOtA
tags: []
topics: ["Evals, observability & reliability"]
transcript: true
---

# Ryan Lucht, Datadog: From Evals to Experiments

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `11 min`

[Watch the recording](https://www.youtube.com/watch?v=x4QbzXDZOtA) · [Conference site](https://aiconference.com/)

## Description

Ryan Lucht, Sentio Technical Advocate, Datadog

From Evals to Experiments: How to Ship Successful AI Initatives by Failing Cheaply

AI initiatives are anything but a slam dunk: projects can be expensive, hard to measure, and face many failures along the way. The key to success lies in building the capability to learn quickly and fail cheaply. By going beyond upstream, qualitative evals to downstream, quantitative experiments, teams can shorten feedback loops and allow for rapid course correction. In this talk, Datadog Senior Technical Advocate Ryan Lucht will show teams how to leverage both approaches and join model performance with business metrics to ship more successful AI initiatives.

🛎️ Remember to hit the bell icon to stay notified!

Follow The AI Conference

© The AI Conference 2025
Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*1,950 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=6s)** Okay, ladies and gentlemen, next to the stage is Ryan Luck from Data Dog. >> All right. I love I love lunch talks. I've got all of what 10 minutes to share. I'll share one idea with you in that 10-minute span. And let's frame the conversation here with two questions. And the first one is one that I'm sure you are already asking regularly or being asked regularly, which is how do we actually know if our AI initiatives are working out? And the second question maybe slightly less frequently appreciated is how quickly do we know if our AI initiatives are actually working out? We could take a public example here. This is not to pick on CLA at all after their very successful IPO last week. I'm sure any of us in the room could find ourselves in this situation.

**[0:53](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=53s)** But in early 2024, they were quite convinced that they were successfully replacing human customer success agents in their call centers with AI. And it took them 14 months to then turn around and say, "Actually, this initiative isn't panning out as well as we hoped it would. Customer satisfaction is suffering a little bit. We need to rehire some of those human customer support agents." The problem when it takes us a long time to realize that something isn't working out is that it becomes very expensive to fail, right? Maybe we're disappointing users and there's some hit to our reputation as a result. Maybe we're seating ground to our competitors if they are successfully moving more quickly than we are. Obviously, we've spent a bunch of money on an idea that didn't really work out, but there's also the insidious hidden opportunity cost of

**[1:42](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=102s)** not having used that time to work on something better. And let's be clear, failure is exactly where most of our AI initiatives are going to end up. This is not about a sensationalized headline from an MIT study that 95% of initiatives are are failing or what have you. Uh, I'll quote a much more conservative statistic. This is from IBM's global CEO survey. This was from May of this year. They surveyed 2,000 CEOs. The CEO said that over the last three years, about a quarter of AI initiatives have delivered expected ROI. To a skeptic or a lite, maybe this sounds like incontrovertible proof that uh all this AI stuff is hype, the emperor has no clothes, etc. But this is actually roughly exactly what I would expect to see. I would posit that this

**[2:31](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=151s)** is part and parcel with any sort of innovation. And here's why I say that. If you ask the teams at tech companies who regularly measure the success of their ideas by running AB tests, they're going to report very similar success rates. This is true of UIUX design. This is true of new product feature launches and user flows and growth experiments, marketing creative uh search ranking algorithms and recommendation systems. Most ideas we try to improve any of these fields don't work out. The difference and the reason that this is okay for these teams, but it's pretty problematic for those of us building with AI right now, is that for these teams who are running AB tests, they know if their ideas are going to work out or not in a matter of weeks, if not days, not months or quarters. And as a

**[3:21](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=201s)** result, it's very cheap for them to fail. So, how do we bring this power of AB testing to make failing very cheap to our AI initiatives? And that's what brings us to the the title of this little mini talk, which is from eval to experiments, right? I would imagine most folks in here are familiar with evals. God knows there'll be plenty of eval talk today and tomorrow, but we also need to run experiments, right? Evals help us look under the hood and and figure out how to build what we want to build to prioritize and tune potential solutions is what I wrote on the slide. But then we also need experiments to prove the business impact of what we're building and to make important decisions like a ship no ship decision or a go no-go decision or should we keep investing down this road. It's it's kind of like using the right tool for each

**[4:11](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=251s)** part of the process, right? Ultimately, our goal is to solve a business problem. This is true of any initiative AI or otherwise. You could think of this as a template. We want to build for use case X in order to drive Y business outcome. And I will give you a hint. Getting better output from an AI model is not a business outcome. Not even for OpenAI, right? So let's take our our customer support agent example here. We can say we want to build AI powered customer support to drive decreased support costs. And this becomes the hypothesis for an experiment that we're going to run to close the feedback loop on our AI initiative. But before we get to this ultimate test, we have a lot of smaller questions to answer about the how. And that's what eval, right? They're going to help us figure out how to approach the build. What models do the best job here? Do we use an open source model or

**[5:01](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=301s)** do we need to invest in a more expensive proprietary one? Very related question. Can we solve this affordably or cost effectively with current technology? here. Is it still a little bit out of reach? What should our prompts look like? What what sort of data set should we feed in? Maybe how do we want to fine-tune parameters like temperature? So, let's talk a little bit about each of these, right? Evals I think of as pre-production experiments in quotation marks. And I I use the quotation marks because we're not doing gold standard science here, right? The FDA does not approve drugs on the basis of a couple of eval. We're kind of more like tinkering, right? So, we're going to try out a couple different combinations of models and parameters. We're probably going to use a set of fixed inputs so we can make clear comparisons between all the things we're tweaking, right? Maybe we have some expected inputs. Maybe we

**[5:48](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=348s)** have some atypical inputs. Maybe we even have some adversarial inputs. We're going to do some error analysis and look at where our AI products are failing or falling down today and define metrics and evaluators based on that so that we know what better looks like. We know where we're steering. And then we're going to look at those evaluators plus maybe some prefab metrics like cost or token usage or uh duration, latency, tool use, what have you. So we have a whole suite of tools inside data dog to help with this AI observability. Uh, for example, when you want to do that failure mode analysis to define evaluators and and know what we're actually trying to improve, very helpful to have traces of all of your actual model calls so you can see what's going on, code them, define evaluators. We also have tools that help run all of

**[6:38](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=398s)** these evals and and collate and compare the results so you can search through uh fairly wide parameter space if you care to and find out exactly what the the most likely working potential solution is. But these pre-production eval aren't sufficient. There's a couple reasons for that. First, we're dealing with limited sample sizes, right? We're talking about running an eval maybe a few dozen, maybe a few hundred times, but we're almost certainly not going to catch all of the crazy cases that are going to happen when we set our AI products out into the real world. Second problem is that we're usually dealing with text output here and evaluating that is subjective qualitative work and this is why uh eval experts like KL Hussein will tell you when you're doing that error analysis to

**[7:27](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=447s)** define evaluators have a single person in your company or a single person at least for the product who's doing this and it's sort of the benevolent dictator so that you don't run into these subjectivity problems. Obviously that also puts a ceiling on scale here. But the last and the most important one is that what looks good pre-production often fails to correlate to the business metrics that actually matter. This has been true for a long time. You know, ask any ML team that works on search algorithms and they'll tell you that what looks very promising in terms of a model improvement in an offline experiment pre-production doesn't correlate to the metrics that they're actually measured on when they go out and test these things in the real world. And that's why we need experiments to bring our AI initiatives to the real world. We're going to test our solutions in real world environments

**[8:14](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=494s)** with real users. We're going to do that gold standard science, a randomized controlled trial to prove what works. We're going to look at causation and not just correlation. We're going to tie the AI product to the business metrics like revenue or cost and not just descriptors of the output. And we're going to run these experiments at scale so that we can get insights in weeks instead of months or quarters. So here's what that might look like for our customer support agent example, right? We're going to take all of the users that are opening support chats with us and we're going to randomly assign them to one of two groups. In the A group, we have our our control group, our placebo if you will. They're going to continue interacting with a human support agent just like they always have. But half of our users are randomly going to be selected to interface with the AI agent. And we're going to track

**[9:03](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=543s)** thousands and thousands of people all the way through their journey with us after they've encountered one of these two options. And we're going to measure the metrics that we really care about as a business, like did one type of customer request returns or refunds more often than the other? Did they make repeat purchases with us at the same rate? What did customer lifetime value look like? How long did it take us to resolve tickets? What was customer satisfaction like? maybe what's the all-in cost of support with human agents versus support with AI and what the outcome looks like is tightly quantified causal impact of our AI products on these business metrics. So this screenshot is from our experimentation platform. It's called EPO by Data Dog. But you can see here we ran this AB test and we proved that the AI support agent had a positive impact on our repeat

**[9:50](https://www.youtube.com/watch?v=x4QbzXDZOtA&t=590s)** orders and on our customer satisfaction. This is a very clear go no-go decision. So that's the entirety of the idea that I want to leave you with today, right? Is that we need to combine evals and experiments. And when we use both tools at the right part of our development life cycle, we won't fall prey to long feedback loops. We'll look at the success metrics that actually matter, actually keep us employed, right? And we run ABA tests to help us go from that idea to the proof. If you want to talk about AI observability or experimentation, please do drop by the data dog booth. Thank you very much.
