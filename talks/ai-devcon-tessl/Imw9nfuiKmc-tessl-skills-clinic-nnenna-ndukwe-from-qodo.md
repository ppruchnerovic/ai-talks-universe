---
id: Imw9nfuiKmc
title: "Tessl Skills Clinic - Nnenna Ndukwe from Qodo"
slug: tessl-skills-clinic-nnenna-ndukwe-from-qodo
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 17
published_at: 2026-07-22T12:15:45Z
video_id: Imw9nfuiKmc
url: https://www.youtube.com/watch?v=Imw9nfuiKmc
youtube_url: https://www.youtube.com/watch?v=Imw9nfuiKmc
tags: ["AI code review", "AI code review tools", "AI-generated skills", "Anthropic best practices", "Automated skill review", "Coding agents", "Developer relations", "PR Resolver", "Qodo", "Qodo PR Resolver", "Tessl skills", "ainativedev", "how to improve AI skills", "how to use Tessl skill review", "what is Qodo PR Resolver"]
transcript: true
---

# Tessl Skills Clinic - Nnenna Ndukwe from Qodo

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `17 min`

`#AI code review` `#AI code review tools` `#AI-generated skills` `#Anthropic best practices` `#Automated skill review` `#Coding agents` `#Developer relations` `#PR Resolver` `#Qodo` `#Qodo PR Resolver` `#Tessl skills` `#ainativedev` `#how to improve AI skills` `#how to use Tessl skill review` `#what is Qodo PR Resolver`

[Watch the recording](https://www.youtube.com/watch?v=Imw9nfuiKmc) · [Conference site](https://tessl.io/devcon/)

## Description

Qodo's AI code review tool, PR Resolver, faced Tessl's automated skill review with eye-opening results: a jump from 78% to 89%. It sounds like an agentic magic trick, but it's all about the description. If a skill's metadata paints the right picture, agents are more likely to trigger it. Your agent's success hinges on this one detail. Most agent skills never get triggered at all. It begs the question: is letting AI write your skills a good idea?

Qodo's Developer Relations Lead, Nnenna Ndukwe, brings her frontline experience to this live session. As a developer advocate at Qodo, her global insights into developer enablement shape how these skills help teams succeed. Her focus on quality and practical integration informs a transparent journey into skill improvement.

What we cover:
• How Tessl's automated skill review scores agent skills against Anthropic's best practices
• Why a skill's description is the single biggest factor in agent utilization
• Watch Qodo's PR Resolver skill jump from a 78% to 89% score
• What Qodo's PR Resolver and Get Rules skills actually do for coding agents
• Why do AI-generated skills often underperform human-written ones?

Chapters:
00:00:00 - Introduction
00:00:20 - Meet Nnenna Ndukwe from Qodo
00:01:05 - Touring Qodo's skills on GitHub
00:02:00 - What is Qodo PR Resolver?
00:03:25 - Running a Tessl review on the skill
00:05:01 - How Qodo uses skills internally
00:07:14 - Nnenna's workshop on AI code quality
00:08:07 - First review results: 78% score
00:09:46 - Applying fixes and re-running the review
00:13:26 - AI-generated skills research and the final score

🌐 Try Tessl - we help you build a software factory, one step at a time: https://tessl.io
🔔 Subscribe for weekly episodes on AI-native development

Have you run your own agent skills through a review process yet? Let us know in the comments.

## Transcript

*2,997 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=0s)** Codex has a skill creator plugin, so I have it create skills for me as I feel okay. You know what, I want a new skill, but I have no idea if Codex knows the right or best practice ways for even building a skill. Look at that. Okay, so not bad. Not bad at all. Hey there. Simon Maple here from Tessl. And here we are again at the Skills Clinic. And joining me is Nnenna from Qodo. Nnenna, welcome to this session. Thank you for having me here. And tell us a little bit about yourself. You're a developer advocate? Yes. I lead developer relations at Qodo and just always flying around the world, going to conferences, creating technical content for developers and, you know, developer enablement. What's the best country you've ever flown to? Oh. That's a difficult one. You know, I've always enjoyed going to Paris.

**[0:48](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=48s)** So I'll say France. For the food. No. The nightlife. Oh, really nice. I like it, I like it. No. For developers, for developers. Sorry. That's right. Yeah, we work for a living. I remember now, I remember it's not just all fun and games. Had to reel it in. Yeah, that's it. Right. So Nnenna, today we're going to have some fun with skills. We're going to have a look at some Qodo skills and we'll run some tests against them, see where they're good, see where we can improve. And we'll run some improvements and see, of course, unless it's 100% in this case, we'll just bask in the glory of your wonderful skills. Yeah. We'll throw a party. Exactly. But in the case that it doesn't, I would love to see how this all works. Amazing. So let's go to your skills. Your skills are on GitHub. Yes. So GitHub has its qodo-ai and qodo-skills repos.

**[1:37](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=97s)** There we go. Correct. So if we come here, okay, so here we have in the skills directory we have Qodo Get Rules and Qodo PR Resolver. Which one? Let me talk through this. Which one would you suggest we have a look at? That, I would say, is Qodo PR Resolver. It's used so widely. And tell us a little bit about what PR Resolver is. Yeah. Yeah. So Qodo is an AI code review that automatically runs against pull requests. And then once all of those issues are presented in the UI, we really want developers to be able to fix their code automatically to just move things forward. You run Qodo PR Resolver and point it to your PR right directly in your coding agent. It's going to loop through and fix all of the issues Qodo pointed out, and then push that summary and the code changes back up to your PR.

**[2:26](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=146s)** Awesome awesome. Okay, so we have cloned that repository. We have out there all the Qodo AI and Qodo skills. Perfect. And we have our skills there. I'm going to run Tessl agent and test agent. Let's just say let's make sure it can find everything. So we'll say what skills do I have in this repo? I hate that because it just shows how poor I am at typing. Do you use Whisper Flow or something? Typically I — I should do more, actually. Yeah, yeah, I'd love to use that as an excuse as to why my typing. Exactly. Let's start with Get Rules and we have PR Resolver as you say, fetches your PR and Qodo review issues and helps resolve it. So we want to say, let's run a Tessl review

**[3:20](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=200s)** run on the PR Resolver. Now what this is going to do is essentially it's going to run. It's going to run as an agent, and it will run some tests to see if the Anthropic best practices have been found in the skill and where they are. You'll get the points for it, where they're not. It will suggest ways in which it can better adhere. And, of course, the agent best practice or the Anthropic best practices aren't always exactly what every organization wants. So just because sometimes a score drops a little bit doesn't actually mean it's wrong. It just means it's, you know, if you want to adhere to the best practices of Anthropic, per se, then it dips. So this is a good way to kind of stabilize,

**[4:07](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=247s)** I guess, the quality of skills over time. If you're running Tessl against them. Absolutely. And actually this kind of shows how well skills have been written. And the evals that we have, which are more scenario-based, show the impact that the actual skill will have on an agent. So we run tasks with and without the skill and we see what scores in the criteria. Interesting. I love that, you know, I just had a talk yesterday about structured AI coding workflows, and people were asking me, oh, skills can be brought into Qodo as context, but do you evaluate the quality of the skills? And I was like, no, but I know who does. And I gave you guys a shout out. I actually. We just put it to someone who said they came here because of because of the workshops.

**[4:54](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=294s)** And we look at that Makoto of said. The power of DevRel. Absolutely. So, how do you use skills internally? Coding. Yeah. So we use the Qodo PR Resolver. When we — we use Qodo on our own code. Right. So when we're shipping high-quality code. So use that. We use Qodo Get Rules, which is a great way for our coding agent to pull down any relevant coding rules or standards that we have. For example, every single Python method should have docstrings. That's just a basic rule that we want to have. That's a rule that we pull down if we're doing any Python code, and our coding agent has that context to do it right the first time, that is what we're trying to, you know, we're trying to shift left with the code quality. And okay, so right now we are running Tessl review run. So this — this kicks off the agentic process.

**[5:46](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=346s)** We pass in the location of where your SKILL.md is. And we're running in a workspace. So it's actually one of my friend's workspaces. But that's fine. And it will store the results in there. And then a label in which we can actually, you know, we can do searches or other things afterwards. So that can take any number of minutes. But we'll see. We'll see how long it goes, I guess, within Qodo. You know, you're very AI-native anyway. Oh absolutely. How close to a software factory are you? You know, that is something I've been asking customers that no one's actually asked me that yet. I wouldn't say we're not there yet. That's what I can say. I do think it's going to become more important to be thinking toward that and actually implementing strategy of adoption

**[6:34](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=394s)** and enablement together as a company to get there. Absolutely. What about you? We're actually — yes, we use the Tessl agent to help us build a software factory. Amazing. And it's — I think the thing which requires most adjustment is the individuals, the humans in terms of, you know, trusting, following the new workflows, particularly people who have, you know, a greater number of years in engineering discipline because it's harder for them, almost like to let go. So it's been a very interesting and sometimes challenging — yes — move across. But yeah, this is a people thing. This is a people problem. People in process for sure. Bigger than the actual technology itself. Yeah. Tell us a little bit about your workshops. You said you had a workshop yesterday. Yeah, yeah. Tell us what it was. It was all about quality, you know, like with everybody

**[7:23](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=443s)** being worried about AI slop and like, shipping really bad code into production. I just wanted to come in and kind of set the tone of, like, we can be quality-driven. And here is a workflow from planning to code generation all the way to code review and resolving those issues. That will give you some confidence to feel like, okay, I have some guardrails around my agents. My agents have the context that they need to write code in the way that is good for me and my team and my engineering organization. And so I walk through that step by step with an example of a code change process in a repo that I made everybody fork. So they've all got access to it and anybody can access it on GitHub. Awesome. Well, the review is done. So let's take a look. Look at that. Okay, so not bad.

**[8:11](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=491s)** Not bad at all. So the review score is 78%. Okay. There are a couple. There's a validation warning. So there's 20 missing relative links. Now this is an interesting one because very often the relative links, it could actually just be a slight, a best practice, a difference from the best practice of how those relative links are written. Very often, however, the agent will recognize from a relatively where that file is, and determine it, but sometimes it doesn't. Strong actionability, needs less repetition. Actually, this is a really interesting one because a lot of the time we as humans, we very often repeat the same thing thinking an agent needs to hear it multiple times. But actually these days, a lot of the time they don't.

**[8:59](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=539s)** Description scores very strong. Specifically, could include more natural trigger phrases. This is super important because the description is. The description. Of course, on a skill is one of the two bits of metadata that helps an agent to trigger the actual skills. So if the description is good, the agent will be more likely to trigger it, because it knows, oh, I need to use this when blah happens. So we could use a bit more. Maybe just adding in words issues or code reviews. That are my coding agent or whatnot would know. Okay, time to. When you say coding issues, or something that knows to trigger. Yeah yeah. So why don't we? Why don't we go ahead? Let's run. Okay. So let's say great. Let's run tests. Let's run tests for review fix.

**[9:49](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=589s)** And what that's going to do is it actually runs it again. But it's going to apply the fixes and then rerun the agent to identify sorry, rerun the review to see how far with those fixes we can get that score up. So it runs it again. And hopefully we'll be able to jump that score. And I'll fire off a pull request as well, to see if you guys would be interested in it. I noticed it also recommended you should run a verification process after you fixed all your code, and that was actually what someone brought up in my workshop right here. Oh, here. Yeah. That we should make sure the agent should run all of your linter and like, you know, the static analysis after it's already made changes to your code and fixed it. I think that's a really good practice. So I'm interested in seeing what these results will be like.

**[10:37](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=637s)** Cool. So yeah, this run we should be able to see we should be able to see the results straight after. Why don't we jump across? And what we'll do is we'll open that folder. So let's see, where are we? Let's go into Tessl. And I think I created a Qodo skills and in here we have your skill and we have the PR Resolver. So walk us through this then. So we have the SKILL.md, obviously, and oh, only a couple of resources. So the skill's interesting in the description. This is essentially where most of the triggers happen. But you also have triggers which can be used as well in terms of, you know, giving the agent that knowledge of saying, when certain things happen, use this skill. So then you talk about the resolver, you have a bunch of tools and okay, interesting.

**[11:31](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=691s)** This does look okay to me in terms of well, we'll see what the change, you see what the change looks like. But that does look okay. Very often, links should be a markdown link. So that looks pretty reasonable to me. I'd be curious to know, if our results — the scores, what are some common scores that you've seen? Is that on the better end, or is that like, you know, average? That's actually pretty much — I'd say that's on the better end. I mean, typically review scores very often you would use something like this Tessl review in a PR as like a GitHub Action or something like that. And then, when PRs are pushed, you would and it's against a skill you'd want to say, okay, let me review to make sure we haven't regressed and things like that. And typically the threshold is we don't want anything below 80. So the fact that you're virtually at 80 now

**[12:22](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=742s)** and, you know, a little bit of noise because this is an LLM as a judge as well. So a little bit of noise and you'll find yourself maybe run it a few more times. You'll be at 80 with the same skill, untouched. So that's actually — it's actually a pretty good skill already. This is what we're looking at here is tuning versus any major changes. I would say. That's awesome. Yeah. A lot of people, you know, they get their skills and they're like at 20, 30%. And the biggest trick is people will. And I'm — I'm with this as much as the next person. When you start adding your metadata, you add a name and description. You just say something really quick, and it's like a couple of words or this does this and people forget or people don't know, but that description is what the agent needs in order to trigger the skill. And if that description is bad, it will never trigger your skill. And it's such a key piece that people miss.

**[13:11](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=791s)** Do coding like I have Codex create. It has a skill creator plugin, so I have it create skills for me as I feel okay. You know what, I want a new skill, but I have no idea if Codex knows the right or best practice ways for even building a skill. Yeah, now that I'm thinking about it. This is such an important piece. There was a paper written — a research paper that talks about how good skills are that are AI-generated. And I think, very often it was found that when it's context that is generated in like a creative, agentic fashion does actually provide that uplift that people are after, but validated, verified skills where humans go in, look at it, make changes and things like that. All of a sudden that really jumps up. So I think, on average, the jump goes up to like — I think it averages around 14%. I think the paper said, for human written skills, but for non-human

**[14:01](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=841s)** rates — skills, for agentic skills, I think the average was slightly lower. Like it actually sometimes regressed in your environment. So it's very interesting to kind of see that. Very fascinating. So it's done. Wow. I see a good — I see things going up. It's an 11% increase up to 89%. Amazing. Let's do it. Let's do a — we don't need to rerun the review because that's actually already done as part of the fix. Let's do a git diff of the change changes. And yeah, I mean, you know, that's actually pretty good. So here we go. Here's the diff summary — it added a shared section. Applying it fix

**[14:53](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=893s)** execute the code agent prompt directly instruction. So kind of condensed or reorganized some of those sections maybe. Yeah, it was condensed. This piece replaces duplicated fix. And actually sometimes when you reduce the skill in terms of just the sheer number of lines, it actually — by reducing the context that you give, you can actually make it easier for the agent to follow. I think your skill is actually small enough that it wouldn't matter too much, because typically we say no bigger than 500 lines, which I think your skill is well under. Makes sense. But yeah, a couple of duplicated areas. Auto fix, another duplication there. Yeah. What would be super interesting after this we can do it offline. But to run the evals before and after the change to see if it's actually having an improvement on

**[15:44](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=944s)** the results of various tasks with the old skill or with the new skill. I'd love to see that. That would be super cool. Yeah. And it did add the validate-after-applied check, which is really awesome. Run the lint, type check, test, if available. Super cool, super cool. I'll tell you what I'll do. What I'll do is I'll push this change and raise a PR back to the Qodo repo. And you could take a look at that. And if there's anything there that you wanted to, you wanted to grab, that's all yours. Yeah, I'll review it. Play — awesome. Nnenna, it's been absolutely wonderful having a chat and great, great to play with. The skill looks great. And hopefully some of those changes you'll find useful. Thank you so much. And I learned a lot from you too.

**[16:33](https://www.youtube.com/watch?v=Imw9nfuiKmc&t=993s)** Oh likewise. And I definitely need to start using Tessl more with all of the skills I'm building and need to manage and improve. And of course we love Qodo. We're good friends. Absolutely. Absolutely amazing. Let's — Nnenna. This is fun.
