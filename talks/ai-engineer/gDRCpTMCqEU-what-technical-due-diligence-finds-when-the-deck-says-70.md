---
id: gDRCpTMCqEU
title: "What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad"
slug: what-technical-due-diligence-finds-when-the-deck-says-70
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Soukaïna Abelhad"]
channel: "AI Engineer"
duration_min: 6
published_at: 2026-10-13T18:00:17Z
video_id: gDRCpTMCqEU
url: https://www.youtube.com/watch?v=gDRCpTMCqEU
youtube_url: https://www.youtube.com/watch?v=gDRCpTMCqEU
tags: ["AIE NYC 2026", "Leadership", "Livestream Priority 14", "Online Talk"]
topics: []
transcript: true
---

# What Technical Due Diligence Finds When the Deck Says “70% Automated” — Soukaïna Abelhad

**Soukaïna Abelhad**

`AI Engineer` · `AI Engineer` · `2026` · `6 min`

`#AIE NYC 2026` `#Leadership` `#Livestream Priority 14` `#Online Talk`

[Watch the recording](https://www.youtube.com/watch?v=gDRCpTMCqEU) · [Conference site](https://www.ai.engineer/)

## Description

A pitch deck says a workflow is 70% automated. Before accepting the number, Soukaïna Abelhad asks what it counts, what human work remains and who checked the result. Her first diligence test needs no model expertise: compare workload growth with the fully loaded labor required to deliver it. More output with proportionally more reviewers, trainers, escalations and rework can describe assistance rather than labor removal. A percentage without a clear denominator obscures that distinction, especially when the work called automated still depends on people to complete or correct it.

The second test defines the level of automation inside a named workflow. AI attributed work and an autonomously completed task are different claims; the straight through completion rate needs a boundary that a buyer can inspect. The third test examines evaluation. A model judging another model's output is useful evidence only within its limits, and agreement with an automated rubric can diverge from a domain expert's assessment. Abelhad turns those checks into an economic question: what is the cost per accepted autonomous task after model costs, human review, escalation and rework? Failures belong in the denominator and the cost account. Public examples and a brief anonymous evaluation illustrate the framework rather than establish a general automation rate or a causal explanation for a company's failure. The takeaway is a practical diligence conversation that connects the deck's language to observable work, credible evaluation and the operating cost behind the claim.

Speaker info:
- https://www.linkedin.com/in/soukaina-abelhad/

Timestamps:
00:00 - What an automation percentage leaves out
0:55 - Check one: workload against human labor
2:13 - Check two: define the automation boundary
3:05 - Check three: evaluation and expert review

## Transcript

*945 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=0s)** My name is Sukaina, and I'm an AI tech lead, and today I'm here to talk about what a technical due diligence finds when the deck says 70% automated. Someone has probably shown you a number like this. 55.8% faster. And you've been wondering whether to believe it or not. Well, this one comes from a controlled experiment with 95 professional developers. But the task was one JavaScript HTTP server built from a template against 12 visible tests. Today, I'll give you three checks for what technical due diligence finds in the AI era. I've actually spent more than 80 years on both sides of the question. On the front side, I built AI system that investment professional use. On a build side, I now lead AI evaluation in production and help create

**[0:47](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=47s)** the numbers that reach executives. The dangerous number is not always fabricated. It's often a genuine measurement carried into a conclusion it cannot support. Chun Chan described the buyer side in a nice way. Built for the memo, not for the demo. I want to extend that standard to operational metrics. And the first check requires no knowledge of models. It's pure arithmetic. In Faros observational data, high AI adoption teams merged 98% more pull pull requests. Pull request review time increased by 91% and the average pull request became 154% larger. And the sample covered more than 10,000 developers across 1,255 teams. This does not prove that AI increased

**[1:35](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=95s)** head count. It's an observational telemetry, not a controlled labor study. But it still give us a warning. More work entered the system and the downstream review burden grew with it as well. So in diligence, ask for the company's own 18-month theory. Put workload volume next to the fully loaded human labor. Count everyone whose work exists because of AI, for example, operators, reviewer reviewers, trainers, escalation and rework. If human labor tracks workload volume, the deck has described assistance, not labor removal. But when the arithmetic survives, the definition call still can fail. Uber, for example, says that 70% of its pull requests are AI attributed.

**[2:24](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=144s)** This is impressive. It still does not tell us the full autonomous rate. The period and total count were not disclosed, either. So, every automation claim sits somewhere in this ladder. It's either AI drafted it, or edited by humans, or approved by humans, or no human intervention. Finance already has a useful term for the last one. It's called straight-through processing. Define it as a complete end-to-end without human intervention inside a boundary you name. So, does the boundary here end when the code was drafted, or when the pull request is approved, or when the change reaches production? So, remember, AI attributed and autonomous are two different claims. Okay, now suppose the definition is precise. Can we trust the measurement? Meta found 24% point gap between

**[3:15](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=195s)** automated grader and merge decision after adjustment to the human baseline. Four maintainers from three repositories reviewed 296 AI generated pull requests across different unique issues. They did not know whether the patch came from AI or human. The automated grader was substantially more optimistic than the people responsible for accepting the work. Not a surprise. I have seen the same thing from the other side. One of the projects I worked on, 10 out of 10 output would pass the automated validation. Once you bring the the experts on the table, barely few survive. This is why evaluation maturity is first credibility signal I would look for. So, always ask who labeled ground truth, and whether the expert agrees, and whether anyone measures that agreement. Ask what the automated judge was

**[4:03](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=243s)** validated against, and ask what bad output escaped. So, when arithmetic's definition and evaluation all fell, a word it still has to become a decision, right? This is not a claim that weak AI positioning caused builder.ai collapse. Its insolvency involved revenue financing issues beyond AI claims. The diligent lesson started way back in 2019, when the Wall Street Journal publicly questioned the claim of the AI capability. In May 2025, the The Financial Times also reported that its 2024 revenue estimated had been revised from $220 million to roughly $55 million. On June 2nd, the company filed Chapter 7.

**[4:51](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=291s)** So, the warning existed, but the process did not turn it into a gate. So, even when a claim survives those check, it still has to survive the economics. So, start with eligible workflow value. Apply actual adoption, straight-through process success, and accepted quality. Then, subtract the cost of AI, human review, escalation, and rework. The metric I would want is cost for accepted autonomous task. If the task fails, escalates, or need rework, this belongs to the cost. So, always put those checks together, and this is the card I would probably take with me to the next meeting. To sum up, three main checks. The arithmetic's, compare workload volume

**[5:40](https://www.youtube.com/watch?v=gDRCpTMCqEU&t=340s)** with fully loaded human labor. Two, definition, identify the wrong and and the straight-through rate inside a name workflow. Three, the tell. Ask who defines quality. Whether expert agrees in what that output escapes. Then translate only the surviving claims into a unit economics. And of course, believe it tested or walk away. The printable card in all the source notes are in the website and this QR code will lead you to it. So, take a card, scan it, print it, and take it to your next vendor meeting or investment discussion. And always remember, the job of diligence is not to ask whether the number is impressive. It's to ask what must be true for the number to matter. Thank you.
