---
id: 8vDzncmzxyg
title: "Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar"
slug: your-ai-agent-starts-every-session-like-a-new-hire-killian
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: []
channel: "AI Engineer"
duration_min: 18
published_at: 2026-10-30T19:00:14Z
video_id: 8vDzncmzxyg
url: https://www.youtube.com/watch?v=8vDzncmzxyg
youtube_url: https://www.youtube.com/watch?v=8vDzncmzxyg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Killian Carlsen-Phelan", "Sonar", "Sonar Vortex", "SonarQube", "coding agents", "Claude Code", "AI code verification", "token efficiency", "code security", "agent context", "MCP", "AI Engineer", "AIE NYC"]
topics: ["Agents & orchestration", "Coding assistants & agents"]
transcript: true
---

# Your AI Agent Starts Every Session Like a New Hire - Killian Carlsen-Phelan, Sonar

**Speaker not identified**

`AI Engineer` · `AI Engineer` · `2026` · `18 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Killian Carlsen-Phelan` `#Sonar` `#Sonar Vortex` `#SonarQube` `#coding agents` `#Claude Code` `#AI code verification` `#token efficiency` `#code security` `#agent context` `#MCP` `#AI Engineer` `#AIE NYC`

[Watch the recording](https://www.youtube.com/watch?v=8vDzncmzxyg) · [Conference site](https://www.ai.engineer/)

## Description

Every new coding agent session starts like a new hire: it doesn't know your conventions, architecture rules or approved libraries, so it burns time and tokens searching your repo and repeats the issues already in it. Killian Carlsen-Phelan of Sonar introduces Sonar Vortex, a plugin that hands your agent a map of the codebase and your guidelines before it writes, then deterministically checks every edit. In a live session, Vortex catches a temp-file permission bug the agent's own tests missed, and rejects its first fix. Sonar reports 36% fewer tokens and 44% fewer production outages.

Chapters:
0:00 Intro
0:26 Every agent session starts from scratch
1:59 What Sonar Vortex does
2:25 The bug a test wouldn't catch
3:35 96% don't trust AI code, 48% verify it
4:26 How Vortex guides the agent
7:00 36% fewer tokens
8:08 Bringing SonarQube into the agent loop
9:01 Demo: a real task
13:03 Not AI checking AI
14:17 The fix that wasn't a fix
16:20 What you get

Killian Carlsen-Phelan

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*2,849 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=8vDzncmzxyg&t=1s)** [music] >> I am Killian from Sonar. And if you're unfamiliar with Sonar, we are an independent code verification platform. Um and what I'm going to be talking about today is how to move verification into the agentic coding loop. Um I mean as we know everybody has been doing this the past couple years. It's accelerated the pace and every time you start a new agentic session in your IDE, it is like starting from scratch. It is like a new hired employee into your project. It does not know your existing project conventions. It does not know uh your coding guidelines. It does not know any

**[0:49](https://www.youtube.com/watch?v=8vDzncmzxyg&t=49s)** architecture rules that you have predefined for it. And that can be a problem. Because what it has to do then is when it's assigned a feature, it has to go look around for context, right? If you say, "Hey, build out a new API endpoint." It has to go and determine how existing API endpoints work in your code. And that process can, you know, it's it's a bit of a roll of the dice. Um it can acquire that context quickly or it can search around all over your repository. And that takes time and that takes tokens. And this is a very fixable problem. And if you have issues in your codebase, right? As I'm sorry to break it to you, every codebase does.

**[1:36](https://www.youtube.com/watch?v=8vDzncmzxyg&t=96s)** That is uh unfortunately, it's highly likely that these issues will be replicated and these patterns repeated by whichever agent you're using. And not if, but when that agent introduces new issues, if it's not caught the ability to maintain the quality of your code is almost impossible to do. So um our solution to that is Sonar Vortex. I'm going to show you that here in a little bit. Um what it is it is a plug-in that connects to whatever coding agent you use. And uh this is so the agent knows about your project before it even begins to code. And it is able to verify itself deterministically to make sure that it's introducing no new issues

**[2:24](https://www.youtube.com/watch?v=8vDzncmzxyg&t=144s)** into your code base. So, um I had I recorded a coding agent writing a small feature a little bit ago and it it was able to do so in under 2 minutes, but unfortunately, even though I had instructed it to build out a test suite for itself, it introduced a security issue that Sonar Vortex was was able to catch and forced the agent to continue iterating upon itself until it was fixed. So um the issue ended up being, and we'll see this here momentarily, is that it wrote it it was to unzip a log file into a temp file, but unfortunately, the permissions that it set for that temp file um were not explicit. And that type of issue is hard to write tests for, it's hard to catch, and it's usually the type of thing that a senior reviewer would only

**[3:13](https://www.youtube.com/watch?v=8vDzncmzxyg&t=193s)** catch if they're explicitly looking for it, if at all. And then let's say that they do catch it, now it has to be sent back for a developer or an agent to rework again and re-push and re-review and re-analyze and that burns time and money and it causes a lot of frustration for everyone involved. So, um that the frustration in that process is not just my opinion, that is uh from data that we've pulled. Sonar surveyed over 1,100 developers and found that 96% percent of them do not fully trust AI-generated code. But how many how many of those do you think actually fully verified the code before pushing it? It It was less than half. It was 48% of those. So,

**[4:03](https://www.youtube.com/watch?v=8vDzncmzxyg&t=243s)** that that boggles my mind, personally. That terrifies me that we are just blindly setting off code into production without verifying it. Um but um like I said, the agents write quickly. Rework slows you down, and if you catch it at the PR, um you're already behind where you need to be. But, uh a quick animation to kind of demonstrate what I'm talking about here is as I mentioned, Sonar Vortex. One of the goals that we are doing is we are making your coding agents more efficient. In addition to providing guardrails for them. But, this little ball here is your coding agent, which as I said, it writes a lot of code really really fast, faster than humans can keep up with, faster

**[4:51](https://www.youtube.com/watch?v=8vDzncmzxyg&t=291s)** than we are able to review manually. Unfortunately, as I said, when it starts out, this this grid is your code base. Every square is a file. It has to go searching around. Every time it moves, it's checking a new file. And that bar at the bottom is tokens, which is your money and time spent on just looking around. And when it gets something wrong, you get to find out at the pull request. The review fails, and the work goes back to the agent for another round, and it continues to iterate itself, and you got to keep pinging your senior engineer, and then he's mad at you, and then nobody has a good time. Before it writes anything with Sonar Vortex now, it is going to get the coding guidelines for your

**[5:39](https://www.youtube.com/watch?v=8vDzncmzxyg&t=339s)** project and a map of how the code connects. So, it will pull in things like your architecture guidelines. It will pull in things like what the approved libraries for your applications are, what your coding standards are for uh a given project. And these are all things you get to set for yourself. So, now you can see here, it goes straight to to files. It does not burn excess tokens, it does not burn excess context. And as it works SonarQube checks its code. So, your agent, the edits that it makes with its own tools, every time it uses them it triggers a quick check. And before it ends its turn, it's told to run a deeper check um for even deeper security issues for cross-file data flow. And you see here

**[6:29](https://www.youtube.com/watch?v=8vDzncmzxyg&t=389s)** that issue goes back to the agent and the agent fixes its own code and then Vortex checks it again. And this all works with all of the agents that people are currently using right now, be that Cloud Code, Codex, Antigravity, whatever you want to use. And if you have any custom agents designed or using any open-source ones or any of the non-major players, uh we have MCP clients that are very configurable for you to use at your own desire for that. So, essentially what I want you to take away from this is that Vortex is something that you can just plug in easily to your agent. It it isn't built on top of the CLI and MCP tools that we provide it and it brings SonarQube into the agent so that the agent knows your project

**[7:18](https://www.youtube.com/watch?v=8vDzncmzxyg&t=438s)** before it writes. I'm going to pause it or I'm going to move back before I miss it. And what we found is that it spends 36% fewer tokens on average, especially on tasks like refactoring existing codebases. People who use it have a 44% reduction in production outages and we have a very low false positive rate as well so that we don't clutter up your coding sessions. So, um this is huge. This is huge. This the speed that this um accelerates the coding cycle to the software development cycle to is um it's we're on the new frontier being able to verify uh programming. So, to sum it all up we want to guide the agent and verify the change. And we

**[8:07](https://www.youtube.com/watch?v=8vDzncmzxyg&t=487s)** bring SonarQube's existing intelligence into the mix. So, I'm sure at least some of you are familiar with SonarQube. We've been around for almost two decades, and we are traditionally a a pipeline step that a lot of people run that deterministically analyzes for any security issues, maintainability issues, any data flow issues, and we build out graphs, and we dive deep into the code. Now, with this knowledge already maintained within our servers, we're able to provide that context to an agent, so now it exists from the get-go. Um your agent knows your project before it writes, and it checks its own code as it goes. Your CI already has a SonarQube scan, and then Vortex reuses what that scan has learned, so it's just a quick

**[8:57](https://www.youtube.com/watch?v=8vDzncmzxyg&t=537s)** check on your file, and it knows about the rest of your code. So, here I'm going to show it to you in a real task. This I actually recorded last night. And what you can see from the get-go, and I'll be pausing and restarting it here and there. Uh the first thing that I want you to see is that without having to do anything, we can see SonarQube has started up in the session. Right? Our CLI is detected, and the hook system is detected as well, and secrets detection is on. I'm not going to dive too much into that today, but um secrets leakage is one of the easiest things to prevent, and one of the most costly for your organization. Our plugin prevents uh secrets leaks into GitHub and into agent uh context memories.

**[9:47](https://www.youtube.com/watch?v=8vDzncmzxyg&t=587s)** And what I want you to notice is I didn't have to paste any Sonar instructions into the prompt. It's just all automatically loaded. And so, the request that I alluded to earlier, right here, is uh it's just basically unzipping a log file into a temp file. It says, "Keep reusing that same file, and then write a test that proves it's reused." And before it writes a single line, it's going to ask Sonar two things. It's going to say, uh where does this class live? And what are the Java coding guidelines for this project? And it's right here. It's Sonar context navigation, um and we get this pattern, this single GC log file that I told it to work on. So, it gets parent and child architecture, um as well as existing patterns, um and and uh guidelines around that. As well, it

**[10:38](https://www.youtube.com/watch?v=8vDzncmzxyg&t=638s)** says Sonar context guidelines get language is Java. So, we have um basic guidelines that we enforce agents use when building out Java projects, but if you have any customer requirements that you want your team to follow, uh that gets injected from the get-go. And guys, I cannot emphasize enough that outside of model choice, the context and steering from the get-go that agents receive is the single greatest lever that you can manipulate for agentic performance. Um and the more you do on the front end, the less rework and steering and correcting and intervention that you have to do when you're developing for yourself. So, like uh instead of searching through the files one by one like in the

**[11:26](https://www.youtube.com/watch?v=8vDzncmzxyg&t=686s)** animation, it just gets that map. This is the guide phase uh that that Vortex does. And so, it's able to inspect the existing test, see how uh that operates, and very quickly move on into implementation. Now, that just took a few seconds, and obviously this changes from feature to feature, but running against this feature without Vortex takes longer as this has to grep around and figure out what's going on. So, it's running the implementation, and I will very quickly point out uh where it actually makes that temp file. Um it adds in its own test suite. So, here's the test suite. Uh in the recording, I scroll up. This a little bit right here is a temp file. And I

**[12:15](https://www.youtube.com/watch?v=8vDzncmzxyg&t=735s)** hope you guys can see. It's probably really small for you in the audience. Um, but it creates that temp file right there. And, um, it's going to go ahead and check its own test result, and then it will run the sonar check on both of the files that it changed. Right here it says confirming the test result, and it says running Vortex analysis. Every time a file is edited or added, Vortex analysis runs. You do not have to enforce it. You do not even really have to think about it. It just automatically kicks in, and you can trust your code gets verified. If you have automated workflows set up, if you run a sophisticated, you know, factory design, or you're building these out, this is a layer of trust you need to add in order to make sure that no issues are being introduced.

**[13:02](https://www.youtube.com/watch?v=8vDzncmzxyg&t=782s)** One point as well, this is not another AI checking AI, right? Um, and it's certainly not it checking itself. That is, unfortunately, we found one of the least reliable ways to ensure that issues are not being introduced. Not only do agents think orthogonally on the creation and review of themselves um other Asian agents are likely to miss and hallucinate when reviewing existing code. When you have a deterministic layer, and by that I mean, every time you run the analysis on the code, you get the same result back, that is how you are able to provide reliable, governable, uh, guidance and verification that is compliant and predictable.

**[13:52](https://www.youtube.com/watch?v=8vDzncmzxyg&t=832s)** Don't get me wrong. I love AI review. We also have a, um, AI reviewing tool that I'm not going to talk about today. It's called Guitar. I ran a workshop earlier this week on that. And please come by our booth later if you'd love to hear more information. But, Sonar Vortex is a deterministic layer that stacks on top of your AI coding, and sandwiched between another AI review as well. So, we're running the Vortex analysis and it is going to catch something. It'll catch six findings that come back and Claude will say two of those findings are on lines that it just wrote and four on pre-existing code. Now, we did not engineer Vortex to be super noisy. We did not engineer Vortex to say, "Oh,

**[14:38](https://www.youtube.com/watch?v=8vDzncmzxyg&t=878s)** you found one issue, but you got to fix three more." On new code that is created, it enforces correction and that just surfaces it to you so that you have it for your awareness and if in the future you'd like to fix it, you are able to. One of the findings um that that it has is a security problem, the one that I mentioned uh at the start of this, which is that Claude put the log in the default temp folder without saying who can read it. And on a lot of servers, that folder is shared. So, uh Claude goes ahead and it uh fixes uh the issue here. But unfortunately and we'll see this in a second, Sonar Vortex runs again and determines, "Hey, you actually did not fix the issue."

**[15:27](https://www.youtube.com/watch?v=8vDzncmzxyg&t=927s)** Says, "The finding persists because the temp file is still in a shared directory." The first fix leaned on a Java default and on Mac uh and Linux, the default is already owner only, but the rule that we set in, which is a high bar that we set, is that this is the permissions must be set explicitly. We do not compromise when it comes to uh security. We do not compromise when it comes to quality. So, finally, Claude is able to implement these fixes and again, every time it runs, Vortex analysis is initiated. You do not want to let any issues into your PR because the quicker you can catch these, not only does the surface area of the issues get reduced, but the time and

**[16:15](https://www.youtube.com/watch?v=8vDzncmzxyg&t=975s)** money and energy for remediation decreases. Now, uh that's it for the terminal session. I'm not going to make everyone stare into a tiny uh pre-recorded terminal session, but essentially, what I want everyone to take away from this is that it asked Sonar first. When Sonar flagged it's fixed, it went further and continued to remediate itself. And it will eventually hand it back at the end, and a deep analysis uh for data flow will be performed. What do you get? What do you get out of this? You get less back and forth review, and I see I have a minute left. I'll uh finish up here in a bit. You get less back and forth forth review, you get it fixed in the moment, you get more secure

**[17:04](https://www.youtube.com/watch?v=8vDzncmzxyg&t=1024s)** code, you get less time and money spent on remediation, and um you have more time freed up for your developers because of your ability to trust uh automating agentic workflows. We have a booth downstairs. I would love to talk to you guys. I'll be hanging out behind uh the room in the back uh to answer any questions. I would love to talk with you. If you're brand new to Sonar, if you're an existing Sonar customer, um you know, I'd still love to hear your input and insights. And um that's all I have for you today. Thank you very much.
