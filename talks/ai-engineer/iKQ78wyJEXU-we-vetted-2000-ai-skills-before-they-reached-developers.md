---
id: iKQ78wyJEXU
title: "We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank"
slug: we-vetted-2000-ai-skills-before-they-reached-developers
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Lucas Palma"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-07-29T22:00:06Z
video_id: iKQ78wyJEXU
url: https://www.youtube.com/watch?v=iKQ78wyJEXU
youtube_url: https://www.youtube.com/watch?v=iKQ78wyJEXU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Security, safety & red teaming"]
transcript: true
---

# We Vetted 2000 AI Skills Before They Reached Developers — Lucas Palma, Nubank

**Lucas Palma**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=iKQ78wyJEXU) · [Conference site](https://www.ai.engineer/)

## Description

An AI skill is a piece of code you hand a model to extend what it can do, and once engineers start sharing skills with each other, each one becomes a supply chain risk, more so inside a regulated bank. Lucas Palma's security team at Nubank built Skill Vector to sit between a skill and the internal marketplace, so nothing reaches developers unvetted. Every skill is scanned first with deterministic checks, for destructive shell commands and the like, then with an LLM for the context those checks miss, and only then does it get a decision and permissions scoped to who will use it.

Running that gate over more than 2,000 skills surfaced real problems, since a single skill can carry many, and fed them into the bank's vulnerability management program with approval gates and human confirmation. What worked was pairing deterministic scans with LLM review; what needed work was the guidance the system gave and the habit of running skills locally before vetting. The lesson he leaves is simple: treat skills like any other dependency, and only what clears the gate belongs in the marketplace.

Speaker info:
- https://www.linkedin.com/in/lucaspalma/

Timestamps:
0:00 - Introduction: making code safe at a bank
1:32 - AI skills as a supply chain risk
2:50 - What counts as an AI skill
3:57 - The extra weight of a regulated environment
6:07 - From plugins to a vetted marketplace
6:58 - What Skill Vector does
7:37 - Deterministic checks, then the LLM
10:00 - Scanning over two thousand skills
11:22 - What worked and what needed improvement
13:30 - Approval gates and human confirmation
14:23 - Next steps and policies

## Transcript

*2,158 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=1s)** [music] Hello everyone. Good afternoon. Today I'm going to talk about how we vetted 2,000 AI skills before they reach a developers. But before I before of that, I'm Lucas Palma, but many people call me LP. I'm the product security manager at New Bank, the product security structures, uh structure that's within security, looking upon how we make code safe and supporting engineers, product managers and everybody to making our products safer. I have uh over a decade of

**[0:51](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=51s)** experience in financial services engineering background also a lot of years working here at security and a close relationship with the part that I love which is innovation. So before beginning I believe I want to bring to you uh why are we here. So one thing that's important for all of you to understand that the now that we are using AI everywhere even though even with uh coding one thing that uh is important that the AI skills are being part of the developer workflow and that's this might bring some risks because although they look like configuration

**[1:39](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=99s)** they behave like supply chain dependence like uh for example libraries and others. So what we made here was to build a security review system in order to check if these skills were safe or not to be used before deploying them. So the lesson that I want to bring you here by the end of this presentation is that we should be protecting the whole workflow not only the code that's being generated. All right. So what I mean about the supply chain part is that uh traditionally the supply chain has uh package containers, models and so on. But now in the AI era, it doesn't have only that. It still have

**[2:27](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=147s)** the traditional part, but it will it also includes skills, plugins, MCP servers, agent rules and much more things to be acting as supply chain and where AI skill fits into this. Uh I believe that before I go into that it's important for everybody be on the same page on what is an AI skill. So an AI skill has there's normally the developer is using AI tools in order to generate an output which will be code most of the case and within this AI tool there are a bunch of things that can be embedded. One of them are the AI skill. So with this skill we can have a capability to a model or to

**[3:20](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=200s)** an agent uh bundling some instructions some context in order to have better guidance over what it can be done. But there is also an impact over that because somebody can create their own skill and share with others. So when we do that this first person is guiding over the code that's being generated by the other person and then that can be dangerous and since we are here talking in the AI in finance track it's also important for us to understand that we are in a regulated environment. So from one side there are are developers wanting better faster coding more context to have less repetitive work but but from the other

**[4:11](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=251s)** side even more because of the regulate part we need to be aware of the auditability of looking upon credentials safety by default and many other security aspects and keeping that balances is hard, right? So, some people might say like are AI skills dangerous? So, I brought here a few examples of what do I mean by AI skills being dangerous? So first uh one thing that can happen is that when people are describing what they skill can or cannot do it can it can ask for it to retrieve a token or something and it will begin using that

**[4:59](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=299s)** token hardcoded which will go to logs and so on and it can generate a data leak in the future. Another thing that can happen is also the person to h instruct the AI to use shell comments and then this skill will be used by another person and when they use on their shell a lot of dangerous things that that can happen and a lot of files be modified and so on and there's also permissions. So depending on how the skill was configured, it might have excessive permissions much more than what was needed and even a typo can make some dangerous stuff depending on who is using that such skill. So first thing first what we did

**[5:50](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=350s)** initially is that how do we share skills among ourselves how the engineers would be sharing the skills. So uh we went through the marketplace solution. So the skills are being canonically shared among marketplace with the plugins included the skills among them. So it's a internal marketplace where people can discover new skills and that's our boundary where we are trying to make it safer. So what happens is that when someone creates an skill it uh will open the pull request and normally it will go to the marketplace but we made a step before that like a CI step where we created a tool that's called skill

**[6:39](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=399s)** vector and this is this what this tool does is to check if this skill is safe or not to be used uh using a lot of assessments that I will bring it here and also classify those risks and request remediation and so on. So what skill vector does in a single page is that when a skill is created or changed not on the during the creation phase one thing that's important is that the engineers are able to use it locally and also be iterating until the skill is being considered safe before uploaded it and after them upload the skill. We also runs it again because we can ensure that

**[7:27](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=447s)** the engineer has run locally or has run the most updated version. So we also be scanning that after the upload. And then we have some determinate checks for the uh easiest parts to check some uh easy risks using regular regular expressions and so on. After that when we check that we need better context we then use LLM. Uh it's important to have this hybrid approach with LLM checking the the context but also with the determinist because you know how LLM is depending on the temperature that was set. Sometimes it will check that it's a risk sometimes it might not. And then all of these findings are reporting the PR that was

**[8:15](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=495s)** open to upload the skill. So it will improve the usability since the engineer will have the in the same PR what has to be changed before uploading the skill. And another good thing that we made that's important is to have a serif with all of these so it can be consumed by our security tools as well and generate a report on the risks and be part of our vulnerability management program. So depending on the severity, depending on the policy, uh the skill can require some remediation, can be blocked, all of this before the marketplace distribution. So there is the local scan, the p request, the determinist scanner, then

**[9:04](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=544s)** there is the LLM review, PR feedback, serif, and then the decision. Will we use it? We will allow it, will we allow it? but it requires remediation and so on. A few examples of what we have ex scanned here. It's uh a non-exhaustive list. So we are looking upon if there are some unsafe instructions. If there are some drift be within the behavior that the agent has if there are some destructive shell comments that I commented earlier if there are some file modifications that shouldn't be there. uh credential requests, how are they being done? Some data being exposed uh unintentionally, if there are permissions that are over broad, risky, MCP usage and much more.

**[9:54](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=594s)** These these are the main ones. And so getting back to the title, we have scanned on that over 2,000 skills. uh now there is much more than that but this is the baseline that I brought for you on this presentation uh inside this we have identified uh more than 1,000 and half uh risks. So not that 1,00 skills had risk because a single skill can has many risks but these were the total risks that we identified over uh this amount of skills and 1,000 of them were probably

**[10:40](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=640s)** remediated right after and there are few of them that were really hky that we were able to block before going to the marketplace. So we also had made a b uh historical scan looking upon the skills that were created before the skill v implemented. Uh over there we were able to identify new uh risks as well and put it them into the vulnerability management program so [snorts] it can be could be remediated. A few lessons that I want to bring here as well. So what things that work well is having both the the terminist scanners for

**[11:28](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=688s)** non-risk patterns but also LLM review for uh behavior checking upon the destructive comments uh looking upon the credentials checks as well having the output in serif and adding comments on PRs and things that needed improvement. And we worked during the process were also there were some risks like comments that we were treating equally but depending on the comment it can be more or less risky. Also some signals that were weak and didn't have much context that were uh more troublesome than helpful. There is also the prompt level ask for confirmation. I there's a next slide

**[12:16](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=736s)** about that that I will go deeper. That's an important one. Also, uh there were some warnings that seemed uh harmless, but only if it was running locally. If there were going to production, then they could be impactful and that we had also to look up on that. Uh if the finding had hadn't some clear guidance was troublesome as well. And last but not least, we know that other people could create other marketplace. So how can we proactively scan check there is a new marketplace and put skill vector into it as well. So regarding the prompt level that's something that's important for you to know people sometimes will add the instruction like you need to ask for

**[13:05](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=785s)** confirmation but the AI may ask confirmation for itself. So from your perspective there is a human in the loop but for the AI perspective there is has been a confirmation and that's okay another has confirmed then let's go so that's something that we were scanning as well looking up on having proper human in the loop looking the tool that's executing if it's going through the approval gates and so on having hooks and within this as I said it's uh plug-in marketplace skill is one among many things that there is into that. So there are things that we can reuse from this lesson. So for example, treating these as supply chain is

**[13:54](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=834s)** important. Reviewing what's being uploaded to the marketplace before goes there. letting developers to run these checks locally, enforcing these checks that are being run locally also in the CI having the termination checks together with the LLM checks and looking upon dangerous actions and prompting uh and having enforcement when they happen. So next steps over here is that I'm talking a lot about skills here but a lot of these as I said could be applied to plugins to MCP servers rules hooks. So all of this that I'm saying here we also have the MCP vector the rules checks and so on that's also applicable

**[14:43](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=883s)** here but with different risks uh having also different gates depending on policies that were implemented depending on the marketplace as well have some enforcements on tool level here enforcing that there are audit logs trusted gateways and so on and also last but not least Having the trusted trusted AI marketplace is very important. So we can have a canonical way to scan and share knowing that then are being safe and that's not about only about the skills that are being created by people but it also includes the third party skills or plugins and so on. So if someone downloads something and wants to use

**[15:31](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=931s)** it's important to upload it on the marketplace. So all of this scanning can be done and check if it's safe or not to be used and also that way allow other people to use in a safe way. And that's it. Uh I'm sharing here my contact. There's my link in profile. If anybody wants to contact talk more about that the QR code will bring you to my profile. If you don't want to type, no problem at all. And I hope you you've enjoyed the talk.
