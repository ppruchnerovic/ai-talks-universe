---
id: 5de3Xi7Zq2U
title: "Tireless AI Agents + Why The Harness Matters As Much As The Model | Ep 22"
slug: tireless-ai-agents-why-the-harness-matters-as-much-as-the
conference: owasp-genai
conference_name: "OWASP GenAI Security Project"
category: "Security conferences"
edition: "OWASP GenAI Security"
year: 2026
speakers: []
channel: "OWASP GenAI Security Project"
duration_min: 26
published_at: 2026-11-06T12:06:13Z
video_id: 5de3Xi7Zq2U
url: https://www.youtube.com/watch?v=5de3Xi7Zq2U
youtube_url: https://www.youtube.com/watch?v=5de3Xi7Zq2U
tags: ["#AISecurity #ThreatIntelligence #CyberSecurity #AIAgents #LLMSecurity"]
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Tireless AI Agents + Why The Harness Matters As Much As The Model | Ep 22

**Speaker not identified**

`OWASP GenAI Security Project` · `OWASP GenAI Security` · `2026` · `26 min`

`##AISecurity #ThreatIntelligence #CyberSecurity #AIAgents #LLMSecurity`

[Watch the recording](https://www.youtube.com/watch?v=5de3Xi7Zq2U) · [Conference site](https://genai.owasp.org/)

## Description

Does an attacker still need to be 80% expert to get a 20% boost from AI? After almost three years of hands-on research, the answer may be changing.

Rachel James talks with Andrea Fukushima and Ben Ramirez, two major contributors to the Threat Intelligence Initiative's Exploit Research project, about tireless AI agents, why the harness around the model matters so much, and what defenders should do next.

CHAPTERS
0:00 Does an attacker still need to be 80% expert?
0:51 Welcome and the Exploit Research project
2:44 Meet the guests
4:29 Phase one recap: the 80/20 finding
7:38 Has the 80/20 flipped? Rogue AI agents and tireless systems
10:56 Why the harness matters as much as the model
12:09 Running offensive AI locally: what breaks
14:24 "Stupid loops" and what a harness fixes
15:05 Offensive frameworks (HexStrike, Kali, MCP) vs Claude Code
17:26 Trading one kind of expertise for another
18:50 When the orchestrator spawns 20 agents for 20 ports
19:57 Too many tools: why agents pick the wrong one
21:23 Predictions: what defenders should do next
24:48 Wrap-up and the upcoming research paper
25:39 Credits

LINKS
Exploit Research paper:

GenAI Security Inside Track podcast:

More Threat Intelligence episodes:

Produced by:
Gen AI Security Project - https://genai.owasp.org

with help from RumRunner Media - https://rumrunnermedia.com

All opinions expressed by the host and guests are theirs alone and do not necessarily reflect the opinions of the organizations with or for whom they work.

## Transcript

*3,785 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=0s)** This podcast is produced by the Gen AI Security Project, which also brings you the AI Security Inside Track podcast hosted by project co-founder Scott Clinton. Find it on all your favorite podcast platforms. Welcome to the Threat Intelligence Podcast, episode 22. Does an attacker still need to be 80% expert to get a 20% boost from AI? Even the human or the humans are still key to any role that you can have. After almost three years of hands-on research, the answer may be changing. The harness seems to almost matter as much, if not more, than the model. In this podcast, Rachel James talks with Andrea Fukushima and Ben Ramirez, two major contributors to the Threat Intelligence Initiative's Exploit Research project, about tireless AI agents. Why the harness around the model matters so much, and what defenders should do next.

**[0:51](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=51s)** All right. Thank you so much for joining us today. We are always happy when we're able to get guests on the Threat Intelligence podcast. But today, I'm particularly excited that our guests are actually two major contributors that worked on the Exploit Research project that was under the Threat Intelligence Initiative that we have mentioned a few times on this podcast. So we've done a little name dropping, I guess, here and there about this type of research. And right now, the report that we have been working on, which is actually like phase two of some of the research that we've been doing, this research in total has been taking place over now almost three years, which is crazy to think about.

**[1:43](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=103s)** It's currently in final review for the typesetting and the fonts and all of that stuff, so it should be released very soon. So hopefully this will be an incredibly timely podcast with Andrea and Ben, who have worked on this project. Hopefully by the time this podcast is out there, you'll also be able to look at the paper and some of the amazing research that we did. So with that, Andrea, Ben, we usually have folks come on and do a self-introduction for our listeners. So hopefully you have a bit of an elevator speech cooked up. Why don't you go ahead and tell our listeners a little bit about yourselves and your expertise, and maybe talk a little bit about what made you want to

**[2:40](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=160s)** contribute to this Exploit Research project. And that will be a great way to kick it off. Ben, would you like to start? Thank you, Rachel, for the opportunity. I currently work as a security strategist in a major travel company. My work right now is a mix between threat intelligence, security threat modeling and so on. I've lost count, but I've been working in security for more than 15 years in different roles, more organizational, more technical, always involved. And right now I've been very interested in the AI topics in general. Thank you, Ben. And Andrea, tell us a little bit about yourself and what got you

**[3:31](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=211s)** involved, because you've been involved in this research project for quite some time. Oh yeah. Just to introduce myself, my name is Andrea. I've been working in security for about seven years now, give or take a year. I have been working with LLMs and AI security for about a year or so, and that's kind of when I joined OWASP GenAI. Basically I started learning about AI and I was like, what could I learn more? And OWASP came to mind. And that's kind of when I met Rachel and the GenAI Threat Intelligence group. At the time we started, over a year ago, there was not a lot of research about how the capabilities these models had would have an impact on exploit development and stuff like that, and it was still a new field that I thought

**[4:23](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=263s)** would be worth researching. And that's how I ended up joining this particular group. That's great. I love how you cued up the aspect of the research that has changed so much. So for our listeners, a quick recap. The Threat Intelligence Initiative decided, like I said, almost three years ago at this point, to really start to explore AI's actual hands-on capabilities as it applies to offensive cybersecurity tasks. And at the time, there was a lot of speculation about the way threat actors may or may not be using AI, but not a lot of hands-on research about this type of weaponization. And we really wanted to look at this through a cyber threat intelligence lens. Very specifically, we wanted to understand what the level of

**[5:18](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=318s)** capability of a threat actor needed to be to actually effectively use AI for attacks. In other words, is it really somebody who doesn't know Python, who's a script kiddie, able to penetrate the Pentagon? Or is it more like, if you already know what you're doing, you could get a little bit of an uplift? And it's really fascinating. Our first report, which you can find out there as phase one, essentially concluded that it was probably like an 80/20: that you needed about 80% knowledge of offensive security techniques, of hacking, of red teaming, to get about a 20% uplift from the AI tools. And a lot of the ways that we had seen reported, and we did have observations from the frontier model providers themselves, about the way AI was being

**[6:14](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=374s)** weaponized was primarily focused on personal uplift. It was coding a couple of lines of script, maybe making a file dropper, but primarily the operator, the brains behind the operation who really understood the direction to take these attacks, was still the human. And as we kicked off phase two of this research, about a year ago, the landscape completely changed. As Andrea mentioned, when we first started this research, there was very little practical, in-depth knowledge about the way AI could be used to do offensive security tasks, to create malware, how effective it was, how much knowledge you needed, how much funds it would

**[7:06](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=426s)** cost, right? How much inference cost it might take to be effective. And in that time of our research, we went from there being very little information out there to, as we're wrapping up the paper, reading these reports and reporting on this podcast about rogue AI agents that have been hacking multiple companies. So maybe that's a good pivot point. And I'll start by asking you, Andrea, but I'm curious about your perspective as well, Ben, as you've been working through this project and have seen the trajectory of how things go. Do you feel like there has been a change? Is it still 80/20, or are we looking at that being turned on its head?

**[7:58](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=478s)** If somebody now has 20% knowledge, can they get like an 80% uplift? How do you feel the threat landscape has changed with these tools being able to hack companies? Andrea. That's a very good question, Rachel. I think the pace at which AI has been moving since we started this research has been a lot quicker than I personally expected. As we talked about, when we started this research, AI agentic capabilities were just becoming a thing. And now, a year later, there are rogue AIs. But as you and Bryan have gone over in the podcast before, it's important to note that the rogue AIs were coming out of frontier labs during testing of their most advanced and unreleased models, and those are backed by budgets that very

**[8:52](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=532s)** few research organizations can match. And even though these are frontier models, so far from what we've seen, the findings have been issues that other security researchers could potentially have found if they had just had the time and the effort to look for them. I guess the main difference that I'm seeing is that these are tireless systems that have unlimited time to just poke at things and look at them. And from that perspective, I feel like there's more of an uplift, where we were saying 80/20, maybe now it's 60/40, where you get a force multiplier, but you don't immediately just get something that works out of the box. Man, that's such a good point too. I remember some tasks you were running, and sometimes the agent or the LLM would get stuck in what we'd sometimes call

**[9:44](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=584s)** stupid loops, where it just tried the same thing that didn't work over and over again. But to your point, they're tireless. They can continue to run down these threads in a way and not get exhausted the way a human would. So it's really interesting. That's a really good point. Ben, what about you? What do you feel has changed in terms of what a threat actor would actually need to know, to have, and the resources to hack with these AI systems? Do you think that's changed? It has changed, though not as fast as maybe the technology is moving. I think actors still require expertise and knowledge, but the bar is getting lower and lower. Even though the models are getting better and better,

**[10:43](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=643s)** and you can feel it in your day to day, a human is still required to drive, to give the goal, to help process information. And something that I also found interesting with the testing I did is how relevant what's called the harness is. All that is around the model, because there's a lot of talk about the models, how they have bigger contexts, how they are more capable. But everything that surrounds them, even the human or the humans, is still key to any goal that you can have. Whether it's a legitimate goal or a criminal trying to do it. So this is slowly improving, but there are still other problems that an attacker needs to solve with these new technologies if they want to achieve this faster

**[11:38](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=698s)** and actually leverage the AI. Yeah. Can you talk a little bit about that, Ben? That was such a good point you brought up when we were doing this research. I remember we were talking about how it feels like there's a point we're about to reach where the harness is going to be more important than even the individual agents and their capabilities. And perhaps the harness is almost more important than the person at this point. Can you talk a little bit about that? Yeah. In the testing that I did for the research, I made a local setup. I wanted to do that because I thought this could be something attackers would look into, something realistic. Attackers don't want to disclose what they're doing, don't want to get caught.

**[12:31](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=751s)** So maybe having everything local and keeping everything private could be an option they explore. And I used a local framework on my laptop. And what I found is that even though it's really easy to start, you can find a lot of information, you can ask an LLM a lot of things, you can start fast. You can have an LLM on your computer and run it. You don't need a big server to start, you just start. Then I started to realize I was having the usual issues when you are dealing with technology. Every piece that is there: the model, the framework, Ollama, which I used, the operating system, and even the kernel. At some point I had an error that I needed to fix to get everything running.

**[13:27](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=807s)** And when the agent was running and trying to achieve its goal, it got stuck in loops, finding more problems with this setup, where I had to troubleshoot Ollama, troubleshoot the operating system, the network, and so on. So yes, you can start quickly, but you will feel the gaps in your knowledge. You still need to know how to deal with issues when they happen, and a lot of things could fail. Yeah, I think that was a huge difference from what we found in the first phase. We were purely using LLMs to guide. We weren't having the LLMs or agents operate tools in any way. And this concept of a harness wasn't really a thing when we did phase one.

**[14:23](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=863s)** And we noticed a lot of what we would refer to as these stupid loops, where it would try the same thing that didn't work over and over again, because there really wasn't any error handling that could redirect it in order to maintain a goal. And that's mostly what we mean when we say harness: overarching control over different failure states, different ways of controlling and directing those agents towards a consistent goal, which accommodated for the propensity of an LLM to get stuck in these loops. So that kind of leads me to another question I wanted to ask Andrea. When you joined, we had this entire discussion, because when we first kicked off

**[15:19](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=919s)** phase two, it was only days, but there were now offensive agent frameworks and open source AI offensive security tools. I think HexStrike was maybe the first one that we got to play around with. And we did some research and tried to make sure that, if we were going to leverage one, we were leveraging one we knew threat actors had actually used. Maybe you could talk a little bit about what those frameworks were like. And I know you've been doing some work with harnesses and Claude Code in this field as well. What is your opinion about HexStrike and some of these developed frameworks, some of which I think even use Kali in the background, versus using your own

**[16:14](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=974s)** harness, using Claude Code? Yeah, sure. So a lot of it does come down to what Ben mentioned: the harness seems to almost matter as much, if not more, than the model, because depending on how you set it up, the model is going to behave differently. And if it reaches a particular loop, it might be able to break out of it. And it gives you a point of failure where either you get stuck because the model couldn't do something, or the harness helps you get out of that loop. In terms of the open source frameworks that we looked at, for example, it basically gives you access to a bunch of MCP tools so that you could use it with Kali. And again, a lot of the way that you set up your agents ends up mattering.

**[17:06](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1026s)** Because something we ran into when we were looking at these frameworks was that unless you specifically told the agent to look for a particular connection and guided it on how to use it, it wouldn't do that. And it's interesting to realize that you're switching one type of knowledge for another in that case. You're saying there's an uplift where you don't particularly need to know how to use a particular security tool. But instead, you need to learn how to tell an agent to connect to it, or you need to set up that MCP connection. And so in certain ways, you're just trading one type of knowledge for another. Oh, that's an interesting observation.

**[18:01](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1081s)** I see what you mean. If we're filling a glass full of technical knowledge, you still have the same amount of fluid that you need to pour into that glass. But now maybe more of it is AI knowledge versus hands-on, like memorizing all the nmap commands and switches. Right. Interesting. Exactly. You don't particularly need to know how to use Metasploit, but you are going to have to be able to troubleshoot that MCP connection if you're having your agent use it, and tell it how to use it as well. That was another thing we ran into. I particularly liked the out-of-the-box frameworks, because the connection was set up and you could just have your agent use the framework, versus when you're setting it all up yourself.

**[18:50](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1130s)** You can get into loops, depending on how your agent framework operates. So when we were doing the multi-agent framework and decided to just run it without using any of the harnesses and have it do it by itself using multiple agents, we ran into a problem where the orchestrator agent would automatically create a new agent every time it wanted to scan a particular port. Instead of running an nmap scan through all of them, it created a particular agent that would go from one port to another port to another port. So you ended up with like 20 agents for 20 different ports, so that it would check every port for a particular vulnerability, and it just wasn't sustainable. And it leads you to realize that it's smart, it can do a lot of things,

**[19:44](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1184s)** it's definitely helpful as a force multiplier, and it can run commands, but you still need to guide it a lot on the overarching project, on what you wanted to do, if that makes sense. Oh, totally makes sense. And I think what we noticed a lot is that you run into the same issues you have in traditional AI agents and computing, which is that there comes a point where there's a certain number of skill files and tools, and if you have too many of them with similar uses, or it's not clear, based on the information it's getting from the prompt or in response to the machine, if it's not clear which of those tools to use, it can very easily get confused or pick the wrong one for the wrong purpose.

**[20:35](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1235s)** It can be inefficient in a lot of ways, because the way it executes its goals can result in things like this, right? It's being really inefficient. And you, as a person with offensive cybersecurity expertise, know that there's a better way, right? So at what point is that diminishing returns? Or, like you said, you're just replacing one type of technical knowledge with another. Really interesting. So I'm going to ask both of you the question that all of us get asked in CTI, that I think we all hate, but we all inevitably know is going to happen, which is to ask you to predict the future. As I think you said earlier in the program, we knew this was a fast-moving space

**[21:30](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1290s)** when we started phase two of the research. And I think everybody was still shocked how quickly it moved, and phase two lasted a year. Just the difference in the capability and what these models are doing within a year, and especially the open source models, recognizing that threat actors are increasingly more likely to use open source models because it keeps their activity from being visible. And those open source models, their capabilities have advanced significantly in the past year. So what would we want to tell the cyber threat intelligence folks, the cybersecurity folks listening to this program right now,

**[22:21](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1341s)** about that trajectory, and maybe what the next year is going to look like? What should they prioritize? What should they be thinking about changing about the way they do things? So I know that's a big question, right? Predict the future. Tell people what they should do. But if you want to take a swing at it, Ben, maybe we'll start with you this time. What do you think? What advice should we give our listeners? Well, I think it's going fast and we are seeing more incidents, so this is for everyone. What I've seen is a new attack surface. Attackers are going to leverage as much as they can any of the mistakes that we made on our side. They are also learning a lot about how to use it, and they are going to reveal more things.

**[23:15](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1395s)** We are going to learn more from them because they are going to make mistakes. They are going to be using AI, and that could also be a disadvantage for them. So probably we are going to see an increase in certain types of attacks. But there are other things that maybe they cannot achieve, or they are going to make mistakes and get caught, because they may be revealing what they're using, giving us more information than we had access to before. So probably that could be happening. Great, thank you. And Andrea, what are your thoughts on this one? It's a really good question, Rachel. I think one of the things that's important to focus on is that the basics still matter. The things the AI agents are finding are not novel attack surfaces.

**[24:08](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1448s)** They can find zero days, but for the most part what we've seen have been issues with permissions and things that we can find in our own environments when we look at it from a security perspective. It's just that there are agents out there doing it now. And on that note, I would encourage people to use AI. It's not just the attackers that have this capability. We can also start looking at it and potentially using it in our own environment to find things before the bad guys can. I guess that's what I would focus on. Awesome. Well, on that note, that's a fantastic way to wrap up the program. I just want to thank the both of you and also give a shout-out to all the other wonderful volunteers. We had a ton of contributors who worked on this over

**[25:01](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1501s)** months and months of their time. I do encourage everyone to look for the Threat Intelligence Initiative's Exploit Research paper that will be coming out. Take a look at that list of contributors. Lots of people put in a lot of good time and effort to deliver some really key information and some advice that I hope everyone listening to this podcast has a chance to check out. Thank you again, Andrea. Ben, thank you so much for appearing on the program and all the work that you've done. Thanks, Rachel. Thank you, and thank you to everyone who worked on this report. Thanks for listening to episode 22 of the Threat Intelligence Podcast, hosted by Rachel James, co-lead of the AI Security Project's Threat Intelligence Initiative. All opinions expressed by the host and guests are theirs and theirs

**[25:51](https://www.youtube.com/watch?v=5de3Xi7Zq2U&t=1551s)** alone, and do not necessarily reflect the opinions of the organizations with or for whom they work. And don't forget to check out the AI Security Inside Track podcast, hosted by project co-founder Scott Clinton, on all your favorite podcast platforms. This series is produced by the AI Security Project with help from RumRunner Media. I'm Dave Hatt.
