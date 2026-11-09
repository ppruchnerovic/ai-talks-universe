---
id: YNT7Plf9KIg
title: "Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace"
slug: your-ai-agent-has-no-nervous-system-matt-gibiec-dynatrace
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Matt Gibiec"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-10-08T18:30:21Z
video_id: YNT7Plf9KIg
url: https://www.youtube.com/watch?v=YNT7Plf9KIg
youtube_url: https://www.youtube.com/watch?v=YNT7Plf9KIg
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "AI agents", "coding agents", "observability", "Dynatrace", "Bluebox", "production context", "service dependencies", "AI SRE", "context engineering", "Claude Code", "SDLC", "human in the loop", "Matt Gibiec", "AI engineering", "AI Engineer"]
topics: ["Agents & orchestration", "Coding assistants & agents", "Evals, observability & reliability", "Prompting & context engineering"]
transcript: true
---

# Your AI Agent Has No Nervous System — Matt Gibiec, Dynatrace

**Matt Gibiec**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#AI agents` `#coding agents` `#observability` `#Dynatrace` `#Bluebox` `#production context` `#service dependencies` `#AI SRE` `#context engineering` `#Claude Code` `#SDLC` `#human in the loop` `#Matt Gibiec` `#AI engineering` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=YNT7Plf9KIg) · [Conference site](https://www.ai.engineer/)

## Description

Your coding agent is fast. But it can't see how your services actually run, so it guesses.

Matt Gibiec, who leads AI-native solutions engineering at Dynatrace, explains why AI agents need something like a nervous system: real context from the environment they're changing. Agents get stuck in loops, cause operational and security issues, and are hard to measure, because they work fast but blind, only as good as the data they can see. He introduces Bluebox by Dynatrace, an observability agent for your coding agent, and walks through scenarios: bringing production dependencies into local testing so a change that works on your laptop doesn't break three other services, spotting issues before users feel them, suggesting fixes that account for the rest of the system, and briefing agents with real usage data before they build, with a human keeping final control.

In this talk:
• Why agents loop, hallucinate and break things without environment context
• Bringing production dependencies into local testing
• Catching problems early and tying them to the change that caused them
• Planning before you prompt, with a human approving the final fix

SPEAKER
Matt Gibiec, Solutions Engineering, AI Native, Dynatrace

LINKS
Bluebox by Dynatrace: https://bluebox.ai
Dynatrace: https://www.dynatrace.com
Bluebox on X: https://x.com/Blueboxhq

CHAPTERS
0:00 Intro
0:35 About Dynatrace
1:00 What the title means
2:10 Stuck in a loop
2:50 Operations and security
3:30 How do you measure value?
4:34 Fast, but blind
6:34 Context is king
7:04 Introducing Bluebox
7:29 Works locally, breaks in production
9:09 Catch issues before users do
10:59 Fix without breaking other things
12:09 Plan before you prompt
13:29 A human stays in control
14:44 Try the preview

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,848 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=1s)** [music] All right, it is 11:10 so officially time for our session. Thank you so much everybody for joining. I know this is the last day of the conference. So I really appreciate uh for for all of you that that actually wanted to come on Thursday and and and listen to our topic. Uh my name is Matt Gibbitz and I'm the original director of solutions engineering for AI native at Dinatrace. With a show of hands, anybody knows what Dinatrace is. All right, we got a we got a couple hands. Okay. Um we are an observability platform AI powered observability platform. But we're not going to be

**[0:49](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=49s)** talking much about dinat trees today because what we want to address today is a little bit different topic. And the topic that I want to address is as you see the title of the session that your AI agent has no nervous system. Probably an intriguing title and you're thinking of course it doesn't have a nervous system. It's it's not a person. Well, but if you really think how AI agents are being used today, we are using these agents to replace things that people used to do. And a lot of times in order to do that, we need the reasoning. And when we really think about it, if we need reasoning, we need these agents to be able to actually not necessarily behave like humans, but have enough input to understand what they need to do to actually help us in our organization and not just automate things that aren't

**[1:36](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=96s)** necessarily working very well today. So with that said, let's let's break this down. Um, with a show of hands again, how many developers do I have in the room in here? Okay, perfect. Um, any team leads? Okay. And okay, the last one might be a little bit tougher. Do I have a head of engineering in here? Would would you call yourself a head of engineering? All right, perfect. I got one. So, if you take a look at these questions, we're not going to go through all of them. We only have 18 minutes left in here. But if you take a look at these questions, has any of you ever asked yourself a question or been asked a question, why am I stuck in the loop with my agent? How many of you have loosed for example claude and it just keeps repetitively doing the same thing over and over consuming tokens not giving you the

**[2:25](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=145s)** result that you want? Anybody experienced that? Everybody has. Right? Now if you think about it from a human perspective now if you as a human do research and you get results that that are not what you want you will change your approach. You approach it from a different angle. But our AI agents today they're not smart enough to do that. All right let's let's shift to to another question in here. I like the one under team in the middle. How can I handle operational issues? Are you thinking about that yet today or right now are you still in the boom of let's just get things deployed. Let's just get get things going and we'll figure out everything else later. Anybody in here having operational issues with your agents here and there maybe. Okay, let me throw twist in here. How about security

**[3:12](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=192s)** concerns? That's that was a layup, right? I think everybody everybody raised their hand in here. And so again, a a very important questions that we have to ask ourselves. And the last one that I want to try with you guys, let's look at the the head of engineering in here. I love the middle one again. Does our app or does the agent bring value to our users? I think we we jumped in so quickly to the AI world and the AI era that a lot of the times I see customers and and spending three days in here talking to folks, everybody has that AI buzz, the AI agent bus, but how do you measure value? Do you have instructions already today to understand how to measure value of your AI agents? Not right. And and I almost think that as much as you want to run fast and get

**[4:02](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=242s)** there, we have to take a little pause and understand what are we really trying to accomplish and how can we measure the success of our agents? Because if we're spending our engineering resources, time, effort, money on creating these agents and and then utilizing them in a way that we believe helps our organization, we need to come up with measures that will help us do it. Now, with all these questions, hopefully I I I I set up a picture a little bit in here to to to really jump into the next topic that I want to discuss, which is led in here by a quote from my CTO, Burnt. And I'm not going to read the whole thing, but just highlight what we see in blue in here. The agents operate at speed. Would everybody agree with that? That they're pretty fast, but without sight. And what what we mean by that is these agents today are only as good as the

**[4:53](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=293s)** data that is available to them to make the reason to make the reasoning to make a decision. If the data that is provided to our agent is missing context, it's missing details, it's missing the right permissions to pull the data from some of the tools in your environment, you start entering the the very buzzy word out there like hallucinations. You start doing processes and automating things in your environment that now probably don't bring in value because there's not enough context in your environment. So, what if I told you that essentially what we want to do in here is we actually don't need your agent to necessarily have the nervous system or site to be efficient and be productive. There's obviously a little twist on the

**[5:40](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=340s)** title of the session in here, but what they need is actual context of your environment. You can pick any agent that that that's out there. You can just pick the the easy scenario of claude and trying to automate things with um cla inside of your um SDLC life cycle. And as you do that, if cloud doesn't have access to the context of your environment, if it is not able to understand the dependencies of your services, if it is not able to understand how your applications are being used by your users, it will start coming up with decisions and advices that might seem right at at that point, but they won't be right in the long term because there's not enough context for

**[6:28](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=388s)** that agent to understand how your environment really looks like. So what I want to sum up this slide with is this one sentence in here. Context is king. And what context is, it is that nervous system that we pro that you can provide to your agents. So as they're communicating, as you're automating things, as you're creating new processes, that connective tissue of a context is driving all of the processes that you're automating with your agents. So let's take a let's take a look at a couple examples. So keeping that in mind, what what what I want to present to you is Bluebox by Dinatrace. And what a bluebox is is essentially an agent that will now be able to be integrated in the middle of any of your light development life cycle to provide context to any of your AI coding agents or other

**[7:18](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=438s)** proprietary agents that you're developing in your environment. I have a couple slides that we're going to go through in here and I'm not going to go through every single scenario in here, but I'm going to point out the most important things that that I believe are helpful in here. Let me ask let me run a scenario by you. How many times uh you as a developer develop a feature maybe even develop a feature or a skill for an agent and you test it locally and it works great? Locally everything works great, right? We're happy. It's awesome. And then what we do is we merge to to a main branch. We push it out there and all of a sudden three other services are broken. Has that happened to any of you where your impact even though locally it worked fine once it was merged with other agents with other applications now it broke a process in your environment. That is one of the most important things

**[8:06](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=486s)** that Bluebbucks by Dian Chase can provide in here. We will be able to bring that essentially uh services and dependency mapping for every single one of your agents, every single one of your AI workloads. So as you're developing and as you're making changes, you're not just talking about testing things locally. We'll actually be able to now use Bluebox to bring the production context into your local testing. So now you know whether the feature that you develop not only works locally for you and what you're trying to automate, what you're trying to achieve, but also that it won't break and impact negatively anything else that that your agent that your workload is connecting to. Let's take a look. Let's take a look at another um example in here. This is honestly one of my favorites

**[8:53](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=533s)** just in the entire world of observability. I've been doing observability now for eight years. And I think if there's one goal that I ask any of my customers like what would you like to achieve with your observability strategy with now AI and when it comes to issues I think this is everybody will say that find issues before they're real issues before they impact my organization before they impact my users. This is now exactly what the context that BlueBug brings into your agents will be able to do for you. And how do we really get that done? We are able to now again understand end to end the interactions of your agents within your application, within your ecosystem, within your organization. And what we are able to do is we are able to use the historical data from your environments, the historical p the historical loads to understand what regular what normal

**[9:42](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=582s)** looks like. So when things start to deviate from what normal looks like, we are able to now get ahead of it and inform your agents, let's say in your IDE for your developers that one of the services that belongs to them now it's acting slower or all of a sudden it's throwing errors that it didn't throw. Now what blue bugs will also do will be also integrated in the middle of your code repository. So as you do that, we will now also have the context of what was changed in your ecosystem, what was changed in your application, what was changed in your workload. So now be able to overlay that data and understand that the issue that might be happening in your environment was actually caused by a change that somebody pushed out

**[10:30](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=630s)** there, maybe by a merge that wasn't successful. Okay, so as we dive into the next um scenario in here, we discovered an issue. We we started with creating context, right? So we have the context of your environment. We able to bring literally production context data to your local testing to your developers in their IDE. You bacon blue uh into your um AI coding agents. Now we're able to detect the issues early. We're able to start to be product uh proactive. But what's next? you have to talk about fixing things. And here's yet another example where blue bugs will be able to be directly bacon into your SDLC. So when we detect that there is an issue and we know and we have the knowledge of your repo, we know who pushed it, we know what changed, we are now able to

**[11:18](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=678s)** again once again provide the context to your developers and let them know that the service that is now having an issue that the agent that is now having an issue that the workload that is now having an issue can be remediating in the following steps. So again, why is the context so important in that process? Because when we need to fix a bug that's causing an issues in our environment is it might be changing one line of code to fix that particular issue. But after you change that one line of code, what happens to the rest of your environment? What happens to the rest of your application? So again, that context and the dependency of all the other services in your environment is super super important. So as we do that, as we think about fixing things, it's not only about fixing the the issue that we have at hand, but also making sure that we don't cause any other issues in our

**[12:05](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=725s)** environment. Um, and the last um um or two more scenarios that I want to run through is actually briefing your agents before building starts. That's actually I think one of one of my favorites when it comes to directly talking to the developers. I think way too often we see developers going out there and somebody came up with a feature and now the developers just go and develop it. But have we done any research up front to understand what actually that feature needs to deliver to our users? What we actually trying to accomplish with with that specific feature? That's exactly what be able to to do in here. We'll be able to actually plan before you prompt. So when you're building your agents, when you're

**[12:53](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=773s)** building your applications, when you're using your AI coding agents, again, Bluebox will bring in all that context from your application today from all the from all the agents that you already have in your environment today to understand that as you're planning for a new release, you're planning for a new feature, you'll have enough data to understand what that feature that you're now focusing on needs to encompensate. And the last scenario that I that I want to share with you guys is that at the end of the day, providing context to these agents can further drive automation. But when we talk about further driving automation, I'm sure some of you start thinking about the concept of human in the loop. Like at the end of the day, if we just let our agents do everything, I think it'll be a pretty messy world, right? At some point we want to be able

**[13:40](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=820s)** to have control over what we are doing in our environments. So obviously with blue bags you will be able to do that as well. And I I I'd like this picture that we have in here on the right. Right. We we'll first start with observe observing your environment building that context building that dependency mapping providing that locally to your developers as they're testing given all the production data given all the production um details that they need to properly test their code. Once we have that and then we detect issues, we'll be able to actually suggest fix, but not just fix for the particular issue that's breaking the agent, but using the context of your environment, using the context of the application that's monitored, using the context of the agents that are being monitored, making sure that the fix actually addresses what's happening in your environment. Lastly, we'll be able to drive the the entire SDLC in here by providing the fix and giving you the control at the end of

**[14:29](https://www.youtube.com/watch?v=YNT7Plf9KIg&t=869s)** it to make the decision whether you want to push the feature out there, whether you want to push the f fix out there or not. So, with that said, um that really brings me to the to the end of our um our little pitch about bluebox and and what I'd like to finish with is we want to help agents ship code you trust to production. So, if this is interesting to you, um you can go ahead and go to bluebugs.ai and you can actually sign up for a preview of it. Um as as soon as you do that, we'll be reaching out to you to give you access to the platform. I also have my backpack little um things that you can scan. So, I'll just walk around the room now and give them to you. But with that said, we have five minutes. So, if you there's any questions that that anybody wants to ask, we can absolutely use that time for those as well. No questions.
