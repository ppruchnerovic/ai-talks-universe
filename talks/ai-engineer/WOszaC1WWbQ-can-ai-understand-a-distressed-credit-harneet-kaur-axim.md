---
id: WOszaC1WWbQ
title: "Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence"
slug: can-ai-understand-a-distressed-credit-harneet-kaur-axim
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Harneet Kaur"]
channel: "AI Engineer"
duration_min: 14
published_at: 2026-10-24T09:00:16Z
video_id: WOszaC1WWbQ
url: https://www.youtube.com/watch?v=WOszaC1WWbQ
youtube_url: https://www.youtube.com/watch?v=WOszaC1WWbQ
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "Harneet Kaur", "Axim Intelligence", "distressed credit", "credit investing", "AI in finance", "LLM reasoning", "bankruptcy prediction", "restructuring", "AI benchmarks", "AI Engineer", "AI Engineer NYC"]
topics: ["Enterprise adoption & strategy"]
transcript: true
---

# Can AI Understand a Distressed Credit? - Harneet Kaur, Axim Intelligence

**Harneet Kaur**

`AI Engineer` · `AI Engineer` · `2026` · `14 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#Harneet Kaur` `#Axim Intelligence` `#distressed credit` `#credit investing` `#AI in finance` `#LLM reasoning` `#bankruptcy prediction` `#restructuring` `#AI benchmarks` `#AI Engineer` `#AI Engineer NYC`

[Watch the recording](https://www.youtube.com/watch?v=WOszaC1WWbQ) · [Conference site](https://www.ai.engineer/)

## Description

Harneet Kaur, founder and CEO of Axim Intelligence and a former distressed credit investor, tests whether frontier models can reason about a live distressed situation: iHeartMedia. Given the same context, two top models disagreed sharply on the odds of bankruptcy versus a negotiated restructuring. Breaking the analysis into checked layers (extraction, derivation, judgment, prediction) brought them to the same answer, which raises a new question: is agreement the same as being right?

Chapters
00:00 Intro
00:42 What distressed credit actually means
02:34 Why old scoring models fall short
04:30 What it means to understand a credit
05:46 Can AI predict what happens next?
06:13 Case study: iHeartMedia, and two models disagree
08:01 Benchmarking each layer of reasoning
11:07 Structured reasoning makes the models converge
12:03 Takeaways: convergence vs correctness

Harneet Kaur, Axim Intelligence

Join us in SF for the second annual AIE CODE summit: https://aie.codes our last flagship summit of 2026. Applications live now!

## Transcript

*1,916 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=1s)** [music] >> Um thanks to everyone for being here. I'm so excited to be doing this talk. So, um kind of quick intro on me. So, my name is Harneet. Um I'm the founder and CEO of Axon Intelligence. And in Axon, we're building the intelligence layer for distressed credit investing. So, also what we're going to be talking about today. Um and the title of this talk is can AI understand a distressed credit? I think the first question um on everyone's minds, if you're not you know, in the world of credit, is

**[0:51](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=51s)** what does distressed credit really mean? Um credit is pretty simple. So, credit is just a bond or loan um you know, of a of a of a corporation. The bond of Coca-Cola is a credit. Um now, what does it mean to be stressed or distressed? Right? So, stress really happens if there is any sort of underlying risk in the company that would lead them to either one run out of money, two, not be able to pay back their debt. So, every portion uh every year some portion of the credit market faces some level of dis- uh stress or distress. Can caused by cyclical issues. So, let's say construction

**[1:40](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=100s)** you know, the construction market is down, housing market is down. Um it can be caused by operational issues. If you're a restaurant business, there's a big food recall. Um it can also be caused by um secular disruption. So, if you're a software business today, and maybe seeing some AI disruption, right? Um some businesses face challenges and then come right back up. Some businesses face challenges and then get to a place of distress. What does distress mean? It's actually not straightforward. Bankruptcy is one outcome of distress. You can also have a liability management exercise and these are terms I can get into them, but just know that's another uh thing that could happen and then or you can have an out-of-court restructuring negotiated exchange um are a couple of

**[2:28](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=148s)** the options. Um So, next slide. So, as you saw, it's not that simple, right? Historically, the engineering question for distress was pretty binary. So, you can predict a bankruptcy e- either you predict it goes to a default or it doesn't. Today, that's become a lot more complex. Um so, a lot of these traditional machine learning method methodologies just haven't kept up and a lot of the scoring that was pretty important um maybe 10, 15, 20 years ago. Um uh the big one is the Altman Z-score um has become now very static um in terms of a situation that

**[3:16](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=196s)** changes, you know, sometimes monthly, quarterly yearly um and also is in a much more opaque market. So, if you've ever been following credit, the rise of private credit and some of these other areas have caused, you know, a lack of pricing. On the other hand, you have a very qualitative method of understanding and analyzing distressed credit, um which is as a distressed credit investor, you can you know, analyze financials, understand what's going on in the lender side, read the credit docs. Basically, you know, all the things a normal, you know, hedge fund investor or private private equity investor would do um to understand a credit. This process is super manual, very hard to scale, obviously. Right? Now, the question is, um

**[4:05](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=245s)** you know, part of starting Axium and a question I thought about is what can how far can AI get at understanding a distressed um a distressed credit and the type of paths you can take. Um and can you systematize what is effectively a pretty complex process, right? Um So now what does it mean to understand a distressed credit, right? Like as an investor, we have a lot of questions we're trying to answer. Um the the things that you think about um from a financial side, right? What is um you know, what is liquidity? What is the capital structure? And then you have questions from the legal side.

**[4:54](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=294s)** How, you know, what's the structural priority of the debt? Right? Like do you have higher priority or lower priority? And then you have operational issues, like okay, how do you understand the business? What are the revenues? Are the revenues going to go up or down tomorrow based on fundamental you know, fundamental analysis of the business. Right? Um his- Right now, what we've seen in the market, you know, if you're following Pro Go or Harvey or some of these, you know, big AI companies, what they've done is really think about benchmarking all these different questions, right? Like how good is AI answer answering um what part of the debt is structurally senior? Um and then kind of do rigorous benchmarking and

**[5:41](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=341s)** make that um you know, call it the big finance bench. But I wanted to think about it slightly differently, right? Because the way I thought about it is the true understanding, right, of credit, and particularly distressed credit, is can you predict what happens next? Right? Can I figure out and have a probability distribution of what path this takes in the future? Um so kind of an interesting exercise, I thought step one you know, you should do is take all the you know, I chose a company. So, I chose iHeartMedia, which is a company that filed for a bankruptcy in 2018. So, it's you know, it's it's been through the

**[6:30](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=390s)** rigmarole rigmarole. Um it also went and did uh another stressed transaction back in 2024. So, this is a live situation. This is happening today. No one has a real, you know, answer for what's the future, right? Um there's no ground truth. But what I did was let's throw it into the smartest, you know, models. I did Astra 6 on Max Intelligence um and Opus 5.5. And what I what was a really interesting kind of conclusion is that they disagreed. Like they disagreed on what the probabilities of the future would be um given a structure or context of the data, right? And so, uh if you look here

**[7:19](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=439s)** on um negotiated restructuring, Astra thought that was the best option um for a bankruptcy, um Opus thought that that was the best option, right? Now, how do you how do you say which is right or wrong? You can't cuz I don't know what the probabilities are, right? I don't know what's going to happen. I don't know if it's going to be a bankruptcy. I don't know if it's going to be a out of court restructuring. I don't know if it's going to be a refinancing. I have my best judgment on things. I I would say I lean towards Astra 6, but you know, we're all human. And it's a kind of an interesting conclusion, right? Like, okay, wait wait they disagree. Um so, the second thing I thought about is Okay, how do I improve

**[8:08](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=488s)** at least an assessment of their process, right? So, I can look at um whether I agree or disagree with the different assumptions. Um and so, basically you've created this sort of benchmark um where you you know, we benchmark each layer. So, obviously these are at each layer the LLM could mess up, right? On the extraction layer, I would say with public companies it's it's pretty it's pretty solved. I would say with private loans and and when you have like Excel documents and PDFs, that can that can still be a challenge, right? Then you have the reconciliation or derivation layer. So, extraction would be you got EBITDA. Uh derivation would be, okay, now you have EBITDA and you have debt, now you

**[8:57](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=537s)** can have leverage. Um and then you have a judgment. Okay, now you have the leverage. Is this a distressed credit or not? What's your Uh-oh. Uh Is there like a Okay, I'll just going to I'll just keep talking. So, um basically the question is is this I think my computer Died. Um

**[9:46](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=586s)** Sorry, 1 second. I'll tell you the I do have a charger, but it's not here. No. Uh yeah. Okay, I'll just I'll just talk. That's fine. Oh, okay. It's working. >> [laughter] >> Okay. So, So, you got the judgment layer, right? And then, um then then then you can start okay if you can assess each layer, right? Once you get to the prediction layer,

**[10:34](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=634s)** you've assured the data points are good, you've assured that um the reconciliation layer is good, you've assured that there's some sort of reasonable judgment, right? And then, once you've assured those things, then you can get to the prediction layer, which is really how, you know, as a human analyst, you think about all of these steps, right? You You If you build a judgment on a bad data point, that's not going to be a good judgment, and that's That's just the way this works, right? So, um Oop. Here we go. So, basically what we found, and maybe this is not surprising, but um thought it was interesting, is that

**[11:23](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=683s)** once we actually created the structured reasoning process, you you actually had both the intelligence, both the models actually converge in terms of what they believed the future probabilities of the business are going to be, right? So, now instead of saying 62% bankruptcy with Opus and 25% bankruptcy with Astra, now both these models are saying there's actually only a quarter or 25% chance of bankruptcy and both models agreed that the negotiated restructuring path is actually the more likely path of the business. So, what are kind of the big takeaways here, right? Um one I would say the first takeaway is one given

**[12:13](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=733s)** non-verifiable questions, right? With the same structured context, organized context as a human. I mean, do these models have a predictive edge? And you have to say no, right? Because they are in effect, even agents are human, right? In in some sense of the word and I won't get into the controversy there. Um the second is but a structured reasoning process can get the two models to or, you know, different intelligences to converge on effectively a same view of the future and effectively a similar understanding of of a business and the path it could take. Um

**[13:00](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=780s)** but is that the correct path? We don't know, right? Um and is this is really only at the truest measure, right? Cuz otherwise any sort of historical analysis would create some sort of look ahead bias. Um but I think the the really interesting thing that I've been thinking about is um the convergence is pretty interesting, too, right? Because if you can systematically build a process that actually converges on the same probabilistic outcomes. That is effectively what is a price in a market. Um, and so I I thought that was an interesting takeaway. Um, so that's the last thing. And then just a quick kind of spiel on me. So, my name's, like I said, Harini. Um, building Axon.

**[13:48](https://www.youtube.com/watch?v=WOszaC1WWbQ&t=828s)** Um, kind of background on me. I spent 10 years in finance. Um, the last few as a distressed credit and special situations investor at a um, uh, distressed PE / hedge fund. Um, and then this is the QR code if you're interested in Axon. Um, and that's all I had. Thank you.
