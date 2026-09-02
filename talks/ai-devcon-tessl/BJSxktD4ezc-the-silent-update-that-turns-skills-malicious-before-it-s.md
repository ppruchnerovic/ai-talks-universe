---
id: BJSxktD4ezc
title: "The Silent Update That Turns Skills Malicious (Before It's Too Late)"
slug: the-silent-update-that-turns-skills-malicious-before-it-s
conference: ai-devcon-tessl
conference_name: "AI DevCon (Tessl)"
category: "AI engineering & agents"
edition: "Tessl"
year: 2026
speakers: []
channel: "AI Native Dev"
duration_min: 6
published_at: 2026-04-30T19:00:09Z
video_id: BJSxktD4ezc
url: https://www.youtube.com/watch?v=BJSxktD4ezc
youtube_url: https://www.youtube.com/watch?v=BJSxktD4ezc
tags: []
transcript: true
---

# The Silent Update That Turns Skills Malicious (Before It's Too Late)

**Speaker not identified**

`AI DevCon (Tessl)` · `Tessl` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=BJSxktD4ezc) · [Conference site](https://tessl.io/devcon/)

## Description

In just 6 minutes, Brian Vermeer and Simon Maple explain exactly how AI agents get compromised and what you can do about it.

Most developers install MCP servers without a second thought, and that's a problem. The code inside those servers can hide malicious instructions the human eye will never see, and by the time your agent acts on them, it's already too late.

On the docket:
• How hidden code in MCP servers can hijack your AI agent
• Why installing a skill from GitHub is riskier than you think
• How attackers quietly disable your AI guardrails before striking
• How to scan your Claude skills and MCP servers for threats using Snyk

So before you install your next skill, run the scan first.

Simon Maple: https://www.linkedin.com/in/simonmaple/
Brian Vermeer: https://www.linkedin.com/in/brianvermeer/
Snyk: https://www.linkedin.com/company/snyk/
Tessl: https://www.linkedin.com/company/tesslio/

## Transcript

*1,144 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=BJSxktD4ezc&t=0s)** how an attacker would try and create something nasty, something malicious. How would they go about that? >> The most important one is trust because you want to trust either a skill or an MCP server. You have an MCP server with the reasoning of, "Okay, I'm able to access your calendar and see what your appointments are for today." Great. It works. You implement it, does nothing weird, but then we update the skill and then we put something extra. We put a side effect in or we return instead of just your calendar items, we return it an instruction. But you already trusted that specific function in it. But from now on, even maybe silently, it will operate in a different way and that side effect might be able to offload credentials or install a binary or name it. So, that is one thing, the trust. Trust

**[0:52](https://www.youtube.com/watch?v=BJSxktD4ezc&t=52s)** is is is super important. Then um most of these things, especially specifically in skills, will be obfuscated. Yeah. And obfuscation can be done in Unicode encoding. Some some parts of of of the Unicode spectrum are not visible even for the human eye or for if you read it in a text editor. Mhm. Um but are readable instructions for an LLM. Um it can also be something that is named in a different way, is is base 64 encoded or even maybe simply encrypted. Um so, that obfuscation pattern that you won't obviously see it. Uh yeah, that is that is something that that is something as well. And obviously, if we can do that, we can make these attacks in steps. If we're able to you trust me, um I add something in that that skill or that MCP

**[1:41](https://www.youtube.com/watch?v=BJSxktD4ezc&t=101s)** server, um I may be able to disable some of your some of your security guards or or guardrails or maybe even rewrite your guardrails. And in the next step, I will do the attack. So, it's not it's not a one-shot thing in most cases. Trust is an interesting thing as well because essentially, when we talk about trust, very often these skills hosted just in a GitHub repo. >> Yeah. And it goes back to that very same problem of open-source code. Yep. You're now trusting someone. Essentially, you don't know where they live, you don't know what their background is. You don't know, you know, what security processes they follow, what what security what software hygiene they have in and around their project. But because it does something that a developer of a company wants to use, they download it and they pull that directly into their environment,

**[2:28](https://www.youtube.com/watch?v=BJSxktD4ezc&t=148s)** potentially, you know, using that, maybe checking it in or maybe adding it into that others will also use that, you know, sharing across the company. And it's it's so dangerous. Um we don't have those similar checks up until now. How would a user uh use Snyk, I guess, directly and then we'll talk about within the test or registry uh to to identify where these malicious skills and MCPs are? Yeah. So, say you have skills installed in Cloud or any of the other other well-known um agents that you can that you can use for skills or for MCPs. Um we have we have a Basically, it's on it's it's on GitHub. Funny enough, I definitely trust it. Yes. Yes. Yes. There's a company behind it and we we definitely want to want to retain our um

**[3:15](https://www.youtube.com/watch?v=BJSxktD4ezc&t=195s)** our our good profile of of we're helping people. But if you go to to what is it Git GitHub .com/snyk/ what is it agent agent-scan? Um that is the Snyk agent scan and you can basically use it. It's a Python project which you can launch with UV. Mhm. And then it will scan the most well-known uh positions on your local machine, for instance, to like the doc cloud library where your skills can be stored. And same for the MCPs. And if you have a specific location where your skills are stored, you can give that in as well and and it will and it will look for are there anomalies there. So, this the the scan that it that is happening is not just one simple scan and and not and it's not all it's not a deterministic one thing to do. Yeah. >> so, there are some static scans around

**[4:01](https://www.youtube.com/watch?v=BJSxktD4ezc&t=241s)** that, but there are also some LLMs involved that basically LLMs as a as a judge. Different LLMs that look into, "Hey, is this vulnerable, yes or no?" And the combination of all these checks, because there are multiple checks, will be handed to you in in this case uh your terminal to see like, "Okay, this is what you have. These um functions in your MCP or these things in your skill um are potentially dangerous." And it will give you how dangerous they are. It will give a score to you like, "Hey, this is I will give this a a a 0.5 because yes, potentially this can be used. However, so it's nuanced in such a way that it's actually actionable for actionable for you. So, then you know what you're having, what kind of um functions or what kind of skills you deploy towards your agents. And you can make at least um an educated

**[4:49](https://www.youtube.com/watch?v=BJSxktD4ezc&t=289s)** decision, do you want this, yes or no? Do you want to uninstall the skill? Yeah, it's it's one of those things that, you know, it's a starting point. You want to look at it, you want to flag something that it believes is is but maybe actually some of those activities or those actions that the skill will do is actually intentional. Uh but it's it's about flagging the fact that that's what it's trying to do and it's a case of, "Okay, is this right?" Uh and then I can make the decision of actually, yes, I trust this or or maybe it's the author. I look at the author and say, "Yeah, actually, this is an author I absolutely trust and I I I want to use it." >> instance, even if you create your your your own MCPs. I created my own MCPs to discover what kind of Java conferences are still open and what that don't don't want to miss a call for papers, for instance. >> Yeah. Um so, I have that as a as a very small MCP and then it flagged it as, "Hey, you are pulling in data from an

**[5:38](https://www.youtube.com/watch?v=BJSxktD4ezc&t=338s)** external source. But since it's this is static data, um the the the chance that this is really vulnerable is quite low, but at least you know that this is happening. And then you can you can you can see if you want to trust it, yes or no."
