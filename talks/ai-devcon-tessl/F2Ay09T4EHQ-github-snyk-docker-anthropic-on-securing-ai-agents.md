---
id: F2Ay09T4EHQ
title: "GitHub, Snyk, Docker & Anthropic on Securing AI Agents"
slug: github-snyk-docker-anthropic-on-securing-ai-agents
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 10
published_at: 2026-08-31T16:00:25Z
video_id: F2Ay09T4EHQ
url: https://www.youtube.com/watch?v=F2Ay09T4EHQ
youtube_url: https://www.youtube.com/watch?v=F2Ay09T4EHQ
tags: []
transcript: true
---

# GitHub, Snyk, Docker & Anthropic on Securing AI Agents

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=F2Ay09T4EHQ) · [Conference site](https://tessl.io/devcon/)

## Description

Join us in November for AI DevCon NYC 2026. Buy your ticket now, with 15% off using code YT15:

Harness engineering has a security problem: the skills, tools and memory we hand coding agents arrive with no permissions, no sandboxing and no controls at all. Four talks from AI DevCon London on what that actually costs.

Joseph Katsioloudes (GitHub Security Lab) opens with the gap the industry is trying to close — roughly one application security specialist for every hundred developers — and argues the answer isn't shifting left, it's starting left. Liran Tal (Snyk) scanned around 4,000 published agent skills and found about 1 in 7 carried malware, suspicious downloads or credential harvesting, in a file format with nowhere to declare a permission. Oleg Šelajev (Docker) demos an agent refusing a dangerous skill, then complying once the same instruction is rewritten as Python, wrapped in a module and the context is cleared. And Lamis Mukta (Anthropic) closes on the unglamorous engineering that makes agent memory safe in production: versioning, so a poisoned memory can be rolled back, and a hash check, so two agents can't overwrite each other.

What we cover:
– Why one security specialist per 100 developers is the gap AI could close
– What a scan of 4,000 published agent skills actually turned up
– Why a SKILL.md file has nowhere to declare permissions or sandboxing
– How clearing the context talks an agent past its own refusal
– The guardrails an agent harness needs before memory reaches production

Chapters:
00:00:00 - Introduction
00:00:35 - Joseph Katsioloudes, GitHub Security Lab: AI and code security
00:01:47 - One security specialist for every 100 developers
00:02:38 - Why "shift left" should be "start left"
00:02:59 - Liran Tal, Snyk: what's inside 4,000 published skills
00:04:12 - 1 in 7 skills had something wrong with it
00:05:16 - Oleg Šelajev, Docker: getting an agent to run what it refused
00:06:56 - Clearing the context, and the agent complies
00:07:31 - Lamis Mukta, Anthropic: keeping agent memory safe
00:09:09 - Concurrency, and stopping two agents overwriting each other

Build your software factory, one workflow at a time, with Tessl:

🔔 Subscribe for weekly videos on AI-native development

Which of these four would keep you up at night? Tell us in the comments.

## Transcript

*1,677 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=0s)** Back in June at AI DevCon in London, we had a whole run of talks about what happens to security when the agent has the keys. Prompt injection, poisoned skills, and the awkward fact that most of the tools we've handed our agents come with no security controls whatsoever. Let's first hear from Joseph Katsioloudes of the GitHub Security Lab, who points out there's roughly one application security specialist for every 100 developers and argues we should stop saying shift left and start saying start left. Okay. Good morning everybody. Well perfect. Welcome to Code Security Reinvented. Navigating the era of artificial intelligence. My goal today is to show you practical ways to use artificial intelligence for security use cases. Whatever I show you, you can do.

**[0:52](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=52s)** Also, in Claude Code, Codex, not just GitHub Copilot. Okay. Let's get started. Yeah. 180 million plus developers. A platform that builds and scales secure software. Specifically, my team is the GitHub Security Lab, which is a team of security experts with the mission to secure the open source software that we all rely on. And we do this through research, education and other activities. For instance, this is some research from last year about bypassing Ruby-SAML. Just last week we showed how somebody could exploit 7-Zip with a heap buffer overflow. We have found and helped fix more than 1000 vulnerabilities, 900 plus of which have been given unique security identifiers. And the most important thing is that we help people fix those. We don't just report them.

**[1:41](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=101s)** And this is important because, exactly, there is a gap between security and developers. If we try to quantify this gap, there is just one application security specialist for every 100 software developers. This gap is the opportunity that we can help minimize with AI. However, if we are not equipped with the right knowledge, the gap maybe is going to widen or it's not going to close because we didn't maximize our potential there. And that's the point of this talk. I want to show you the pros and cons, the drawbacks of AI, so you can make a human-in-the-loop use case of how you can use it responsibly. So this is the first statement: AI can help minimize the security gap. Let's see how. The first thing is writing safer code.

**[2:30](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=150s)** For me this is very important because all my career so far, I'm hearing from senior leaders in cybersecurity about shifting left. The problem when you shift left is that you keep having a gap on the left. The whole point and the opportunity here is to start left, and starting left means a lot of things. And of course it has to touch the developers how the code is being built in the first place. We also heard from Liran Tal, who does AI security research at Snyk. His team scanned around 4000 published skills. Roughly 1 in 7 had something wrong with it. Malware, suspicious downloads. Credential harvesting. Raise your hand

**[3:18](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=198s)** if you added a skill to your agent anytime in the last few months. And keep it up. Okay? I just see some hands now. Keep it up. Keep it up. I want you to keep it up. Only now, if you actually review the skill and read the markdown. So many liars. Liars, all of you. I'll show you why today. All right. Cool. We're good. So yeah, I'm at Snyk. I basically do a lot of developer advocacy, and I try to mix that up with security research. Over the last year or so, things like AI security research, which also goes to account to things like skills and MCP security. And we've done a bunch of research over the past few months, which I do want to talk about today,

**[4:05](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=245s)** and it relates directly to skill security. So. At around 4000 skills on ClawHub back in about January, February was the peak when we actually ran the scan. That means about 1 in 7. This is the 30%. 1 in 7 of those skills had some kind of issue with it. So that would have been something like malware distribution, suspicious downloads, maybe credential harvesting, or just misuse, or just basically any kind of potential security vulnerabilities like Guy talked about in the opening keynote. So skills aren't just malware, they're also potentially having security vulnerabilities in them, just like regular code and other things. So everyone probably knows what a skill looks like today, right?

**[4:54](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=294s)** That's kind of like this. There is a front matter that gives you instructions and sets the metadata. There is the body with more metadata, gives instructions to the agent, what to do and so on. But when you look at it there's like no sandboxing information. There are no permissions here. There's no other kind of security controls for the agent to know what to do with the skills. Oleg Šelajev is on the DevRel team at Docker and he brought a demo I would call genuinely alarming. His agent refuses to run a secret scanning skill, so he writes it in another language, then wraps it in a module. Then he clears the context and it runs the whole thing happily. So what you can see here is Claude running in auto mode, and I'm asking it to run this skill and it sensibly refuses.

**[5:44](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=344s)** It says it's dangerous, I'm not going to do that, which is what auto mode is supposed to do. Then we continue the session and ask it to rewrite that in Python code. So take the skill, write me Python code to do this, and it complies because this is a benign request to write a piece of software. So it does that. And I say, can you please run this for me? And it says, I will not run this for you because of the security implications so I'm not going to run this as part of my ethical operating practices. But we go further and I ask it to put it in a Python module, because it can read the actual Python file that is supposed to run, but there are dependencies and dependencies of dependencies. So we put it in the module and it puts it in the module. And it says, I'm going to put it in a module for you.

**[6:34](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=394s)** And at that moment I had a brilliant idea to rewrite it in Rust. So it only gets the binary. So it cannot actually peek under the hood what it's running. And then Claude says, I'm not going to rewrite that in Rust because you're clearly malicious. So it has some sense. But then it writes it as a Python module. I try to run it, it refuses. I do /clear so it loses all the context. And after that, it's very happily running this Python script that pulls the module dependency to do a complete security audit of my machine. And you can see that, that there are 20 keys in my SSH directory. That was a few months ago. After that, seeing that, I migrated them all into 1Password or something. There are cloud credentials and API keys in the history,

**[7:23](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=443s)** and that the agent also can write to the code directory. So all consistent. So machine is completely vulnerable. Right. If I just run my agent naked on my machine. And to close, back to Lamis Mukta at Anthropic, this time on the unglamorous engineering that makes agent memory safe to run in production. Versioning. So you can roll a bad memory back. And a way to stop two agents writing over each other. Because memories can go stale. And they can also be poisoned on purpose. The final problem is that memories can go stale. Of course, something that was relevant in the past might not be relevant today. Or maybe it was written incorrectly or even maliciously injected by someone trying to prompt inject your agents to write bad things to memory. So you have to have a lot of guardrails in place to make sure that these nice

**[8:15](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=495s)** autonomous memory systems actually work in production. And so I'm going to talk through a couple of key principles that we use when designing memory systems in production to make sure that we do get to use all of those nice effects that we've talked, that we've spoken about. So the very first thing is versioning. So when you're designing any kind of memory system, you need to be able to store versions to keep track of what's going on, to allow you to roll back should you need to, if a new update isn't particularly good. Additionally, you probably want to think about what context was this update based on. So which agent session? Which transcript resulted in me wanting to make this update? And additionally, like you might want to track like who did it, which agent, which human, etc.

**[9:06](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=546s)** etc. So this is really important. The second thing is concurrency. So we've talked about okay, what happens when I deploy thousands of agents all working off the same memory system. And the solution that we've adopted here is to have this hashing system. So when an agent decides that it wants to write an update to a memory, it takes a hash. It then drafts its edit. And then before it writes the update, it takes another hash. If those two things do not match, then the agent cannot write it because it means that some update was made in the meantime. And in order to handle that, the agent re-reads the memory, drafts its new update, and then tries to commit this again. So these are the kinds of just engineering practices that allow you to scale multiple agent architectures, scale memory to these kinds of architectures.

**[9:58](https://www.youtube.com/watch?v=F2Ay09T4EHQ&t=598s)** Thanks for watching. Be sure to join us for the next AI DevCon this November in New York City. Visit AI DevCon to learn more and book your ticket.
