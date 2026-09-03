---
id: Eqqd7kGD1BM
title: "How Action Bias Breaks Autonomous Software Maintenance | LogicStar.ai"
slug: how-action-bias-breaks-autonomous-software-maintenance
conference: ai-council
conference_name: "AI Council (formerly Data Council)"
category: "Practitioner AI conferences"
edition: "Data Council / AI Council"
year: 2026
speakers: []
channel: null
duration_min: 11
published_at: 2026-06-18T22:16:13Z
video_id: Eqqd7kGD1BM
url: https://www.youtube.com/watch?v=Eqqd7kGD1BM
youtube_url: https://www.youtube.com/watch?v=Eqqd7kGD1BM
tags: ["AI"]
topics: ["Evals, observability & reliability", "Governance, ethics & regulation"]
transcript: true
---

# How Action Bias Breaks Autonomous Software Maintenance | LogicStar.ai

**Speaker not identified**

`AI Council (formerly Data Council)` · `Data Council / AI Council` · `2026` · `11 min`

`#AI`

[Watch the recording](https://www.youtube.com/watch?v=Eqqd7kGD1BM) · [Conference site](https://www.aicouncil.com/)

## Description

[2026 - DAY 3 - LIGHTNING TALK] Coding agents are increasingly trusted to resolve issues end-to-end: investigate, patch, ship, without a human in the loop. But in real-world maintenance tasks, a large fraction of incoming bug reports describe issues that are already fixed. A competent maintainer moves on. Current agents don't. In our new benchmark FixedBench, frontier models apply unnecessary edits to already-correct code in 35-65% of cases, even with full git history and a working environment. More reasoning doesn't help. Better prompts help, but trade one failure mode for another. Today's training rewards producing patches, not deciding whether one is needed. At scale, that quietly compounds into technical debt. The fix starts with framing inaction as a valid success state.

SPEAKER:
Mark Niklas Mueller - Co-founder & CTO, LogicStar.ai

👉 Sign up for our "No BS" Newsletter to get the latest technical data & AI content: https://aicouncil.com/newsletter

ABOUT AI COUNCIL:
AI Council brings together the brightest minds in data to share industry knowledge, technical architectures and best practices in building cutting edge data & AI systems and tools.

FIND US:
X: https://x.com/aicouncilconf

## Transcript

*1,732 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=0s)** I'll be talking about how action bias breaks autonomous maintenance. Um, and I subtitled this with why coding agents edit codes that's already correct and what to do about it. Um, so currently we're in a state where we mostly use coding agent as assistants. That is we specifically direct them to solve a certain task be implement a feature, investigate an issue, fix some bug that we know about. But humans are kind of the gate to what tasks are getting processed. And that's even the case with asynchronous background agents like Devon that we just tag in Slack. And we believe that we're clearly going towards a future where we go beyond this and the agents or some agentic system will act autonomously also as maintainers because as the code

**[0:48](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=48s)** generation becomes cheaper and quicker the bottleneck is increasingly shifting to actually maintaining and running systems in production that's stable and usable for your users and customers. Um, and this is a fundamental change because suddenly there's no human that directs these systems and tells them specifically what to do, but we have some events or some observation or even some um introspection that triggers action. And now suddenly the agents need to not only competently act when told to do so, but also determine when to act and what the objectives are. And specifically for software maintenance, a common problem is that we have lots of duplicate or stale issues or feature requests hidden in the form of bugs. And

**[1:39](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=99s)** uh some study now from almost 10 years ago uh showed that actually 50% of uh bug reports are duplicates and this already ignores stale tickets. tickets reported um on old releases that at the time of submission are already invalid. So a good engineer that's tasked with maintaining some software will look at these stale old issue reports, buck reports, will realize that they are outdated and will just move on without doing anything. So we asked ourselves working on software maintenance, autonomous software maintenance, what do code agents do if faced with the same problem? And to address this we built fixed bench. And the idea here is we take a software engineering bench like like SWEBench

**[2:28](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=148s)** verified. And for those who are not familiar the idea of Swbench verified is you mine GitHub issues from real world repositories that have code changes associated with them that resolve these issues and test suites to test whether the changes were successful. And typically you just give the issue to the agent and ask it to resolve the issue and then you test whether it was successful by running the test suite. And now we mix things up slightly and we apply the changes already give the fixed code base without any problem although without the test to the code agent and ask it to address or process the ticket. And now obviously the agents shouldn't really edit anything. They should maybe add some tests. They should maybe update the documentation but there should be no substantial changes to the business logic to the codebase itself.

**[3:19](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=199s)** And now the question is is this the case? And to measure this we consider two metrics. One is the resolution rate which is the classical success rate which in this case you score 100% if you don't do anything. And the abstension rate which means how frequently do you edit code that you shouldn't touch. So something that's not documentation, not testing. And perhaps surprisingly, perhaps not surprisingly, depending on who you ask, Frontier agents, so Frontier models in their corresponding agent harnesses actually quite bad at this. They added already correct code in between 35 and 6 uh 65% of cases roughly. That means between one and two out of three issues um that are stale, you get an unresirable unnecessary code change. And

**[4:08](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=248s)** at scale, this obviously means that you increasingly aggregate technical depth and absorb changes that are unnecessary, have drift in your code base, maybe overly defensive programming that absorbs errors that might have actually been loadbearing in some programming languages. And we call this behavior action bias. So um what is the reason for this and how can we address it? Originally we thought maybe it's a reasoning problem and the agent simply didn't think hard enough about what to do. So we varied the reasoning budget in this case for GPT 5.4 for mini from low to extra high and expected that there's a notable reduction or thought there might be a notable reduction in this extension rate or rather an increase in abstension rate

**[4:56](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=296s)** but we saw that there's almost no reduction in fact all of these changes here are well within uh the variance um overlap so in the confidence interval so conclusion is more reasoning doesn't solve this problem and as a result we conclude that also better models will not necessarily solve this problem, at least not if we don't change how we train them. So we looked at what makes an agent abstain versus not abstain. And to this end, we analyze the agentic traces and scored the along a range of categories, the interesting ones I show here. And we see that the abstainers here in purple uh check the gift history a lot more often which in this case is an easy way to check because the get commit fixing the issue is the most

**[5:43](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=343s)** recent commit in the setup but they also tend to reproduce the issue before touching any code and in contrast the non-abstainers tend to jump to just editing the code right away without even testing and reproducing the problem. What's also interesting, even when the non-abstainers actually realize the code is already fixed, which happens in about 25% of the cases, it still produces an undesirable edit because it feels like it has to do something. So, we thought, okay, let's tell the agents to first reproduce the problem. Maybe this will make it very aware that it is already resolved and stop this behavior. And indeed, we see a massive increase in reproduction rate before making any edits. It almost doubled from 40 to 70%. But the abstension rate didn't move at

**[6:30](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=390s)** all. So we see that actually knowing that the issue is is already fixed and reproducing the problem is not what is driving this undesirable behavior. So we changed the prompt a little bit further and explicitly told the agent that it can abstain. And this had a massive impact. not only increased the reproduction rate even further, but it also significantly increased the abstension rate. And our interpretation of this result is that it framed in action as a valid success state, whereas typically this would not be a valid success state. And to confirm that the agent doesn't only exploit this kind of easy hack of checking the last git commit which is obviously not very representative in a

**[7:17](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=437s)** of a real world setting, we consider this worst case set where the agent doesn't have access to a fully setup environment. So it's not so easy to reproduce anything. It has to go install all dependencies itself and there's also no git history at all. So this is really an adversarial state where you cannot traverse the git history to find any commit. That solved the problem. And of course, this reduced the abstension rates, but it reduced it significantly more with the original just resolve the issue prompt. And with our new abstainer fix prompt, we actually had a better success rate in this worstc case scenario compared to the standard prompt in the best case scenario. However, there's kind of one small caveat here. prompting with this prompt kind of trades one failure mode for

**[8:07](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=487s)** another. We considered a slightly different setting where we used the weak model to create incorrect fixes to problems and then applied these. So we had the partially fixed state where there is still something left to be done. the test suites associated with the SWEB bench instances did not pass. And now we check how frequently does the model make any edits in this setting. And we see that explicitly framing in action as a success also drops the edit rate significantly here reducing it by almost 75%. So in a way with the current um LLMs and agents you have to pick the case that you're optimizing for. And in addition to this, there's not only this edge case, but there's many more edge cases

**[8:54](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=534s)** where models implement solutions that are not performant, not secure, not scalable in some form. So we we really need to change the underlying agents or the underlying LLMs and not just the props. Now I'm I'm speculating a little bit because unfortunately we are not a frontier lab that can just RL uh large models and we also don't know what OpenAI and the Tropic are doing. But from my my reading of the literature, most RL task or probably almost all RL tasks actually require some form of action to be considered successful successfully completed and inaction as a success state is probably significantly under uh represented and as a result LLM or agents always believe there's something that they can do and they

**[9:42](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=582s)** should do if they are given a task and this is probably what we see here. So what are some takeaways um that you should have from this talk? Action bias is not solved by scalar reasoning. We have to either specifically prompt for it or hope that the Frontiers Labs will train better models that address this. But it's a framing problem. It's not a capability problem. You have to consider the whole um sets of possible success states for the task that you're giving to the agent and you have to make it explicit that all of these different success states are actually desirable okay successful outcomes otherwise the model will not pick the appropriate action. And as a third and maybe a little bit

**[10:31](https://www.youtube.com/watch?v=Eqqd7kGD1BM&t=631s)** more specific takeaway, um, autonomous maintenance needs dedicated systems that are designed around the specific challenges in the space and not only coding agents off the shelf that are simply triggered autonomously or triggered based on some events. With this, I hope you took something away and I'm happy to take questions.
