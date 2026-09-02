---
id: WJRdLNhrsLQ
title: "How to build an AI-Native Health Company — Dan Feng, Maven Clinic"
slug: how-to-build-an-ai-native-health-company-dan-feng-maven
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Dan Feng"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-08-19T17:30:19Z
video_id: WJRdLNhrsLQ
url: https://www.youtube.com/watch?v=WJRdLNhrsLQ
youtube_url: https://www.youtube.com/watch?v=WJRdLNhrsLQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["AI in the SDLC & engineering orgs", "Evals, observability & reliability", "Science, healthcare & applied ML"]
transcript: true
---

# How to build an AI-Native Health Company — Dan Feng, Maven Clinic

**Dan Feng**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=WJRdLNhrsLQ) · [Conference site](https://www.ai.engineer/)

## Description

Implementation used to be the expensive step, so teams spent weeks settling requirements before anyone wrote code. Dan Feng's observation is that the cost moved. Building takes minutes now, and arguing is what is expensive. Planning at Maven Clinic changed to match. A one year view survives only as direction, assuming models will handle whatever you need by then, while real commitment runs two to four weeks. Long requirement documents gave way to a page or two meant to be argued with. The awkward casualty is the three to six month plan, which he treats as close to unplannable when nobody knows what models will do by then.

The rest is what breaks at that speed. Engineers who once wrote hundreds of lines a day now write thousands, so review had to change rather than scale. Engineers self certify which pull requests need a second reader and stay accountable either way, requests are capped near 500 lines, and large features are stacked into several. The failure he names is the rubber stamp, which buys false confidence rather than none. On reliability he refuses a single bar and sorts failures into tolerable and not. A scheduling action that fails one time in 10,000 is survivable, since the user clicks again. A reimbursement claim is not, because asking for $50 and receiving $200 is an escalation in either direction, so several models read the same receipt and it proceeds only if they agree. Integration tests run many times rather than once, since passing a nondeterministic system on one attempt proves very little.

Speaker info:
- https://www.linkedin.com/in/dan-feng-2bb5703/
- https://www.mavenclinic.com/

Timestamps:
0:00 - Who here is already AI native
0:51 - Maven Clinic, and starting the journey two years ago
1:29 - Tractors do not replace farmers
2:08 - Adopting internally, then building it into the product
3:25 - Early adopters, the majority, and the reluctant
4:04 - Meeting engineers on whichever tool they moved to
4:43 - Why senior engineers stopped delegating implementation
6:03 - The blurring line between product and engineering
6:42 - Rewarding it in performance reviews
7:21 - When building is cheap and arguing is expensive
8:00 - Dream big for the year, commit for the sprint
9:16 - Why three to six month plans became the hard part
9:56 - Starting with the lowest risk coding tasks
10:36 - Pushing it to the whole team
11:13 - Code review when volume goes up tenfold
11:54 - Self certifying, capping size, stacking changes
12:34 - The rubber stamp problem
13:57 - Deciding which failures are acceptable
14:35 - Claims, where the tolerance is zero
15:54 - Automated evaluation plus human spot checks

## Transcript

*2,725 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=1s)** [music] >> It's time. We can get it started. I'm Dan. I'm from Maven Clinic. Today we'll share the experience how we transition from a traditional technology company to AI native company. Before I started, I would like to do a little exercise. Raise your hand if you think you are already an AI native company. Okay, we saw a few. Raise your hand if you thought about it, but haven't started the journey yet. Okay, we saw a few. That means most of us is in between. Hopefully this talk can help you with that one. So, Maven Clinic is the largest digital

**[0:51](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=51s)** health platform. We are focused on women and their families. So, we specialize in like maternity, fertility, parenting, menopause. We started our AI journey just 2 years back. And this moment we built something called a Maven Intelligence. It's a orchestration layer across all our product to enable AI for everybody in this company and for our clients. So, AI is here and improving every day. I think adopting it is not an optional. Even you choose not to, your competitors will do. This is a quote I heard like a couple years back. I would like to share here again. Like a tractors aren't to replace farmers, but the farmers who can operate the tractor will replace the ones who cannot. Hopefully everybody

**[1:40](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=100s)** here will become farmers who can operate your tractors. That's the goal. So, first of all, I don't think there's a one single definition what it means by AI native. And more importantly, there's no predefined playbook you can just follow and bingo, you become AI native. For us, it is really come down to three parts. One is internally with our AI tools, whenever it's possible. It can be as simple as like generating your daily summary, managing your meeting, create a Jira task, anything you need to do today manually, you should think about to say can use AI to do it. Whenever you want to ask other people to do something for you, you should be saying with yourself I can use AI to do it. A lot of leaders in fact today at the Maven include our

**[2:29](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=149s)** sales sale, they use AI tool to solve those task by themselves now instead delegate to other people. That's for internally. Externally, we want to build AIs into our product which achieve two goals there. One is really focused on improve our user experience. Second maybe help us reduce our operational cost. Like a like AI based like chatbot is really good example. It's 24/7, always available, can help our address issues, help our customer instantly. It's way better and cheaper compared to human agents. Thirdly, I think is more important, we need to think about our culture, process, the way we work, how we can change it so we can maximize what AI offers for us.

**[3:18](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=198s)** I will touch it more on the following slides. So, when we come to adopting new technologies, there's always like screw three groups of users. One there's some early adopters, right? For them, we don't need to do too much. Only thing we need to do is enable the tools for them and encourage them to share what they learn with the company. And what we need to really focus on is the one in the middle. That's a majority. We should build a shared AI infrastructure for them, build easy to use tools for them. Just make the adoption as seamlessly as possible. More importantly, we should really listen to them, get feedback, consistently inputting. For example, last year, most of folks and Maven they

**[4:06](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=246s)** are using cursor. This year, a lot of them switch to cloud codes. For us, we need to support the both. We need to meet where they are. Just make feel they comfortable to use it. And for an older places, you always have a few slow adopters. They always have concerns, worries for the new technologies. For them, we just should have meet where they are. Understand what's their concern is. But more important, we should be crystal clear with them where the company is heading to. So, AI is really good and execution if we know what we want to do. So, this is change how we should hire new people and how should we reward them. We used to the way we used to work is we have a senior engineer who sense the

**[4:55](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=295s)** problem, come up with solution, and delegate to other engineers for implementation. So, we can work on it in parallel and be faster. But these days, we found the NASA and NASA engineers wouldn't like to delegate the implementation work to other people because they they already figure out how to solve the problem. They just use AI to solve it instantly. Delegating to other people means more overheads and less efficient. And also means like when you have a new people, you want to make sure they can solve the problem independently. They pretty much has to work on the traditional technical lead memo. We can We cannot afford other people delegate implementation task for them. Also, when we hire a new people, we should think about what we are

**[5:43](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=343s)** looking for. We definitely want to look for somebody genuinely interested in AI. The domain is moving so fast. We want them to keep learning. Also, help the team to stay on track. Secondly, is um with AI, engineers can do way more than they used to do. The boundaries between PM and engineers is getting blur blurry. We found like a engineers who really understand the product. In fact, they can have more way more contribution than a traditional engineer who only focus on software side. And this is what we are looking for. And those deep understanding of the system, the ability to can handle complicated ambiguous problem is also very valuable. This is where AI land off. When we hire new

**[6:31](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=391s)** people, this is also the people we are interested in bring on board. For people we bring in, we want to reward them in the proper way. Even in our performance with review, we start ask, "Okay, what do you have done for AI side?" We definitely want to reward the people who leverage AI to multiple their impact. Although this is impactful everybody in the company. So, now we have the right tools. We get the right talent in the place. And we need to change how we work to maximize the benefit of AI. The we used the way we used to work is say, "Okay, we spend the weeks, sometimes it's the months to flash out the business requirements, finalize the design, and then

**[7:18](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=438s)** do the implementation." Because implementation can be really expensive. If we didn't get the other part right in the beginning, it's it can be very costly to change it later. But in fact, we never get the sense and right in the beginning anyway for any of big projects. With AI, building is super fast. It's probably couple minutes you can get it done. Argument is really expensive one. So, we should really think about what's the best we can work, how can we deliver fast. It's still okay, you can think about what you want to deliver in one year. You can assume AI models can do anything you want in one year. Based on that one, really dream big to think what you can do in one year, but it should only serve as

**[8:07](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=487s)** inspiration, inspiring, and directional. What we really need to focus on is what we want to deliver in the next two to four weeks, right? What we want to get to the PMs and designers is say, "Okay, tell me what I need to deliver in this sprint." And the engineer will focus on it and get it released if at the end of the sprint, if not sooner. Meanwhile, and the PMs, they have time to flesh out the next bunch of the requirements. If at the end of this sprint, they say, "No, what we decided two weeks ago is wrong." It's totally okay. We can switch the gear, get it fixed quickly. That also means like we prefer people not write pages or pages of PRD or TDD anymore. We prefer them to write just a short one or two pages. That one is

**[8:57](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=537s)** really serve as communication, so we can iterate on it. The really awkward part is mid-term goals. Those like a three months, six months. It's very hard to plan these days. The reason is I don't know what AI models will be capable in three months. There may be multiple releases already. So, we prefer not focus on this one. But this one can maybe make it not very easy for most of folks who has been in this domain for a long time because traditionally we get used to have a quarterly planning or we plan it for six months. But it's our job to get used to the new AI era and learn how to work it efficiently. So, I want to talk about the coding and software development a little bit more

**[9:45](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=585s)** here. AI coding tools is probably the most successful AI application. And it's really good and implementation. So, you probably heard a lot of people say, "Okay, I have this AI tools. Now I can even use my phone to implement software and automate every stage." If they feel comfortable do that, it's totally okay. But you don't have to. What I'm trying to say here is And maybe this is our journey, how we adopt those AI tools. We started with the lowest risk task, like starting with writing unit tests, documentation. Those things are very easy to verify and the risk is super low. By doing that, one we build the confidence and we start to construct our own rules, skills, and

**[10:34](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=634s)** build our barriers. And then we push to the whole engineering team say, "Now you should use this AI coding tools for all the tasks." When they choose not to do, it's the time we really want to learn say, "Why you don't do it?" And at this moment, we pretty much use the AI coding tools to do all our implementation. Engineers really focus on reviewing, architecturing, and evaluation. >> [snorts] >> So, and with AI coding tools, we are writing so much code these days. Code review becomes really challenging. So, for good engineer, used to they probably write hundreds of lines code every day. These days, they can easily write like thousands. If we keep do the code review as we used to do, we won't be able to keep up. We also tried

**[11:23](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=683s)** the multiple like AI coding review review tools. It helps a little bit, but we don't feel comfortable 100% rely on them yet. We still found those feedbacks from our engineers are very, very valuable. And that means we need to really change the way we are doing code review to meet where we are now. And couple things we have done. One is we allow engineers to self-identify whether they still need code review. If they think this PR is simple enough, I feel very confident, I don't need anybody to take a look. And we are fine with that one. We let them merge, but we still hold them accountable. And if they do want code review, we want them stay with the best practices. For example, each PR shouldn't have more than 500 lines of code because nobody

**[12:11](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=731s)** can do a meaningful code review with the ones has like thousands of lines code. And we also enable the like stack the PR. What it means is that for big feature, and the engineers can bring break it into multiple PRs where people review the PRs and they can keep working on it. One thing we really want to avoid is a rubber stamp, we call it. Means like people submit code review, you cannot really do anything to it. You just say blindly approve it. This is the worst case, we should really avoid because that's just give us false confidence. We think we reviewed it, it's good, and we release it. Meanwhile, we should keep working on our AI code review tools because we are thinking that's the future. So, at this moment, we use AI tools

**[13:01](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=781s)** pretty much assist each step of our software development. Our goal is it will be automate the whole life cycle from end to end, from designing, implementation, and here is a fully release it. More important, we want the AI tools be able to monitor the live traffic and be able to catch the issue early and automatically fix it. That's what we are still working on, and we're not there yet. The last thing I want to touch a little bit for this presentation is about reliability. So, what it means is like for the traditional software, it does what we implement there, no more, no less. But for the Genex solutions, hallucination is there. We cannot ignore

**[13:49](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=829s)** it. And there completely eliminating them is can be very costly. Sometimes is not necessary, either. So, the way we should do is really have a holistic solution even from the get beginning. For example, we can start with identify which failures is acceptable, which ones are not acceptable. For our AI system, for example, we have the functionality to help our customers to schedule appointment. If we fail well to 1,000, probably it's okay. I'm not saying it's a good experience, but the users really can just click the button again, we will reschedule for them. Probably it's okay. But if we help user to like submit their reimbursement claim, we cannot tolerate a failure because if people ask of $200, we issue

**[14:39](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=879s)** them 50 or they ask 50, we give them 200. Each case will cause a escalation right away. For those cases, we have to put in extra stamps. For example, when we receive their receipt, we will use different models to review the same receipt. We only move forward if the results from different models agree with each other. If we really have trouble to figure it out which one is right, it's it's easy it's okay to tell the customer, say, "Hey, we have trouble to process your stuff. Do you want us to get you connect to a human agent?" We will move from there. That's acceptable solutions. And also we have should have a rigorous process to release our software. For us, we have like hundreds of integration tests, for which pretty much covered all

**[15:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=927s)** the use cases we know, and we are keep adding to the integration test the suite. And the when we run the integration test, not only pass once is not good enough anymore, because the LLM can do different things. So, for each test case, we run it to many times. We consistently requires the high pass rate, like for example, 90% for all the time. And the more important, [snorts] and the after we launch the software, we have our auto evolve system evaluate carefully evaluate each conversation. We have predefined a lot of rubrics, what we think is good, what is bad. And then we will generate results, we will review the score. Besides this one, we also have dedicated a group, their job is mainly review

**[16:16](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=976s)** those conversations. We will spot a check our conversations, that helps us to say whether we need to come back to improve our systems, or our rubrics is too strict or too loose, and we need consistently improve it. When we launch new features, then the time we say not only spot a check probably not enough, we really want to review like say 20%, and we can do it. This whole process make [clears throat] sure we we are really confident whenever we release something, although we know hallucination is there. And that's pretty much what I have for today, and I can stay here to take up questions, and if you have other things, you can reach out to me. >> [applause]
