---
id: YApwddLn5Rk
title: "Shuen Mei: Act–Verify–Refine: The Future of Adaptive Investment Agents"
slug: shuen-mei-actverifyrefine-the-future-of-adaptive-investment
conference: the-ai-conference
conference_name: "The AI Conference"
category: "Practitioner AI conferences"
edition: "The AI Conference"
year: 2026
speakers: []
channel: "The AI Conference™"
duration_min: 19
published_at: 2026-10-13T18:33:22Z
video_id: YApwddLn5Rk
url: https://www.youtube.com/watch?v=YApwddLn5Rk
youtube_url: https://www.youtube.com/watch?v=YApwddLn5Rk
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Shuen Mei: Act–Verify–Refine: The Future of Adaptive Investment Agents

**Speaker not identified**

`The AI Conference` · `The AI Conference` · `2026` · `19 min`

[Watch the recording](https://www.youtube.com/watch?v=YApwddLn5Rk) · [Conference site](https://aiconference.com/)

## Description

Shuen Mei presents “Act–Verify–Refine: The Future of Adaptive Investment Agents” at The AI Conference 2026.

Video Recorded at The AI Conference. Copyright, The AI Conference, All Rights Reserved

## Transcript

*2,413 words · source: supa (en, exact timings)*

**[0:04](https://www.youtube.com/watch?v=YApwddLn5Rk&t=4s)** Regular people like you for us, you don't just put the money in your saving and checking account and don't even look at it, right? You should have monitored it, okay? You should have looked at Hey, you know what? My saving account, you know what is it What's APR right now, right? And you want to probably move from a low API to a high API account. That's the basic idea. Okay. So, for investment company, we will never say is a market the context change and investment professionals and teams and sometimes together with governed systems will make a portfolio shift [snorts] decision. Whenever this kind of decision change or happened or action happened, typically, this will end in a rebalance. The rebalance could happen to ETF, to

**[0:54](https://www.youtube.com/watch?v=YApwddLn5Rk&t=54s)** portfolio, to models. Okay. So, rebalance. Whenever there's a rebalance happened, eventually, you are ended up with sell certain securities in your portfolio and buy certain securities in your portfolio. That's a typical situation. Uh in that case, trading happened. Now, the workflow does not end here. Workflow start with a investment decision. Uh portfolio shifted. Why? Market drifted. Okay? So, the trade commentary is a process that Harbor, I believe other company also do similar things, uh has this workflow. We need to

**[1:42](https://www.youtube.com/watch?v=YApwddLn5Rk&t=102s)** generate the market overview. We need to generate the trade rationale. We need to uh put the fact together so that we provide a trusted information to client, to customer, to stakeholder. Okay. So, hopefully that give you a context what is trade commentary referring to. And in this case, the workflow is started from the shift. Okay? Portfolio decision is made by human being. Now, all of this related documentation, remember, trade commentary is time sensitive, okay? Time sensitive in such a way that, hey, you know what? Something happened in the last month and we did a trade last month and a month later we do a trade commentary. That is

**[2:30](https://www.youtube.com/watch?v=YApwddLn5Rk&t=150s)** stale, okay? It does not make sense. It need to happen within certain time frame. So, it's very time sensitive stuff. We collect the related documentations and market context. And we retrieve the target weights. Oh, target weights, okay? You know what? We reduce certain securities holding position weight from 1% to 0.8% and increase the other side. Okay? Eventually, you have those target weights matrix. And then the workflow will say, "Hey, we leverage the agent to generate the structured draft, which I'll elaborate a little bit later in details." Okay? So, after all these things get drafted, then uh come back to the act,

**[3:20](https://www.youtube.com/watch?v=YApwddLn5Rk&t=200s)** verify, refine keywords. You act uh to generate the draft, uh the grounded draft. You verify the draft against fact, evidence, supporting materials. And you refine uh based on failure message. Okay? That's the general idea. Very simple. And where is human being there? Uh human human in the loop, human at the end loop is there. So, you see like a step number six, seven, you see the evidence for human beings, uh which will be focused on more value-add on steps. So, with that the trade commentary use case, what is approach that we did? Okay. So, this will elaborate the

**[4:07](https://www.youtube.com/watch?v=YApwddLn5Rk&t=247s)** approach. The engineering team looked at this actually, you know, all these keywords coming from engineering team. So, in the past a lot of us we know that hey, infrastructure as code, policy as code, governance as code. So, the team invented word like hey, you know what? Let's treat narrative like code. Okay. How many of audience have the engineering background? You know, you you Okay, a lot of you, okay. So, there is a important question that we actually challenge ourselves. And here is the question I want to ask. Do you trust the softwares that you write? A lot of people say yeah, I have 20 years experience. I trust every code that I wrote.

**[4:55](https://www.youtube.com/watch?v=YApwddLn5Rk&t=295s)** Then the next question that we have it's same in the team. Why you do testing? Right? So, quality assurance team will challenge you heavily. You know what? In their terms, you do not trust the softwares that you wrote. There is unit test, function test, okay, step by step like you know, end-to-end test. User acceptance test, sometimes load test, stress test. They would name like a collection along the list like a test. Okay. If the trust is not there, then what are we going to do? So, the team utilize that synergy, you know, say hey, you know what? Let's look at the narrative like a code. Also, the next question that we said is when the unit test fail,

**[5:46](https://www.youtube.com/watch?v=YApwddLn5Rk&t=346s)** do you rewrite all of the code base? I say it's no. Okay, you do not rewrite. Okay? You only fix the failed unit test. So, keep that in mind in mind, okay? Same way here. So, we applied my greatest idea from engineering team into this program. So, we treat narrative like a code. So, let's see. So, this is the loop. Okay? And keep in mind that the unit tests are sociological okay? When we get all of the documentations, data sources, guardrails, compliance information, and even the asset matrix, the

**[6:36](https://www.youtube.com/watch?v=YApwddLn5Rk&t=396s)** portfolio actions, all this together, we actually act once. Act once means generate the grounded draft once. Okay? So, that's the act part. Now, once we have the act, have the draft, then we move to verify stage. Verify is the one that decompose the paragraph into a unit we call a claim. So, what is a claim? A claim is atomic assertion that you can verify, test, review against evidence. Data you are you'll see examples what is a claim. So,

**[7:22](https://www.youtube.com/watch?v=YApwddLn5Rk&t=442s)** during the verify case, you decompose the draft into a collection of claims. Then, you verify, validate the claim against evidence and supporting materials. When you do validation, you have different kind of results. Number one, happy pass. Yeah. This claim has sounded solid material supported. Good. And sometimes things go to south. Okay? So, you're going to see like, "Hey, you know what? Failure." Warning, misleading. We're not even talking about hallucination here. We're talking about lack of solid supporting material. In that case, we move those things

**[8:10](https://www.youtube.com/watch?v=YApwddLn5Rk&t=490s)** together with the draft, with the evidence, with the reason into refine phase. Now, refine here is only correct the failed unit test. Okay? Only correct the failed unit test. So, generator once, actor once, kicking into verify and refine loop to get things corrected. Now, you may ask question, you know what? What about if I I tried, you know, back and forth, but whatever reason it gets stuck there? Yeah. Human in the loop. There is escalation process. If you tried verify, refine multiple times through your configured round, let's say, you know, I tried eight round, tried 10 round. If it still

**[8:59](https://www.youtube.com/watch?v=YApwddLn5Rk&t=539s)** cannot satisfy the verification criteria, escalate with a reason. Human will get involved. Okay? Now, here I do want to mention that the exit gate is not refined. After refine, the draft will come back for verification. So, eventually the verification only when everything is in good shape, all the atomic claims are verified, then you get the draft move to next stage, which will be human being review. All right? So, this is a another slide, you know, say, "Hey, illustrate the um testable assertions." So, we have market views, portfolio actions, rationales. And I only list the

**[9:49](https://www.youtube.com/watch?v=YApwddLn5Rk&t=589s)** three there. In reality, it is a collection. Now, the reason why all these things are put together because typically in a company you have different ownership for all those things. Market view typically will be owned by what? Investment research team, marketing team. Portfolio action is really the product owner for that investment product. Rationale, it could be a different team. So, all of these different kind of team, the ownership responsibility eventually will provide the documents, the materials for this framework. And what we're dealing with here is the claim list, the claim list. So, hopefully this explain the atomic nature of the claim. Where does this income from? And what is a claim?

**[10:40](https://www.youtube.com/watch?v=YApwddLn5Rk&t=640s)** Okay? So, what is adaptation mean here? Okay. In a way that we say, "Okay, you know what? During each cycle we adapt the contents to evidence. We adapt the contents to evidence. If for whatever reason, say, it is a failed claim. A failed claim means either could be misleading or lacking supporting materials. Uh it will be failed. And the final step will need to correct that. So, we adapt the contents to evidence. On the right side, it's control adaptation. Okay. So, a lot of times, you know what? At early this this is a evolving nature.

**[11:29](https://www.youtube.com/watch?v=YApwddLn5Rk&t=689s)** And it is also a feedback uh okay? So, during the practice, we may observe that, you know what? A Hey, this kind of failure pattern happened multiple times. Seems like it's a is a pattern. Then, human being will step in. Step in in such a way maybe improve the prompt, improve the rule, or maybe change the information retrieval strategy. Uh the idea is a you know what? The previous iteration or previous run, uh we continuously improve and give input for the future. So, that is our control adaptation. Okay? That's control adaptation.

**[12:19](https://www.youtube.com/watch?v=YApwddLn5Rk&t=739s)** This is a illustrative example, very close to real. Okay, very close to real. So, as you can see on the left side of the act step, remember generator once, we have a good sentence. Hey, you know what? The US dollar index declined 2.1% during the month. Yeah, yeah, yeah. Improving the carry outlook for emerging market yada yada stuff, which remains our single preferred vehicle for carry cross entire portfolio. Looks very fluent. It looks seems okay. But, let's look at verify stage. Uh we have one supported evidence. Uh maybe the font is a little bit small, but the evidence is like it in the

**[13:07](https://www.youtube.com/watch?v=YApwddLn5Rk&t=787s)** market context document, it says that the US dollar index declined 2.1%. EM local currency return uh return 1.8. Aided by currency tailwinds, the FX translation came. Uh not carry hybrid. So, the second claim, a dollar weakness in for the carry outlook for emerging market local currency, is misleading. Lack the solid evidence. And the last word, the emerging market local debt is uh, our single preferred, which is a strong statement. Okay. What is actually stated in the asset class matrix is that, hey, you know what? We're actually overweight. Okay. Overweight has nothing to do with

**[13:56](https://www.youtube.com/watch?v=YApwddLn5Rk&t=836s)** a rank on the carry vehicle. Okay. So, the statement that the claim that single preferred carry vehicle is not supported. So, on the right side of the refined phase, you're going to see that hey, things changed. Uh, the failed claim get corrected. It has the whole draft come back into verify stage. And if it verifies, uh, then exit. So, this is a example that we're having. This is a high-level uh, landscape diagram, okay, for the architecture. As you can see, we split this into uh, four stages. Uh, on the left side is uh, all of those data sources. You could have market contacts, you could have asset metrics, you have database talking about the weight uh, changes. Uh, you have uh,

**[14:45](https://www.youtube.com/watch?v=YApwddLn5Rk&t=885s)** writing style, you have compliance guide, and a lot of times, you know, you may wonder, what do you mean like uh, compliance guideline? Okay. Uh, we should not use I, I, I. Uh, you should use we, we, we. Okay. We should ignore you know, ignore those word, we believe. Uh, you know, words like hey, in our opinion. Those are typical examples of compliance, you know, will say, hey, you know what? Don't use strong word. Okay. And various sources get ingested, and separate agent that do the generate. And you can see is we not leverage single agent not only do the generation but also do validation. Each agent has its own specified task. And after all this loop like the verify

**[15:35](https://www.youtube.com/watch?v=YApwddLn5Rk&t=935s)** refine, eventually you see that as it is approved by human being. Now you may want to be like hey, you know what? Seems like everything is working fine. Why do you need human being at the end? Yes. This is a critical part. Uh for human in the loop, human at the end of the loop, the principle for us is if it is a critical has a critical financial consequences decisions. If it is impact human being. If it is non-reversible, we typically will put human being on the decision point. Okay. Now, as you can see, uh we put the control in three families. Evidence control, as you know, all of

**[16:22](https://www.youtube.com/watch?v=YApwddLn5Rk&t=982s)** the evidence needs to be there. And decision control, we have human being there, okay? Doing escalation and doing final review, approve. And we also have audit trail, which is record control. So these three control families work together to support faster production. Now, production does not mean that hey, you know what? You just, you know, you turn it on, let the automation happen. Production faster means that with the guardrail. With guardrail, you move fast within the lane. Within the lane. Now, reliability contract, okay? So we have one release standard and all of the critical claims needs to be verified

**[17:10](https://www.youtube.com/watch?v=YApwddLn5Rk&t=1030s)** and audit trail needs to be there. So the reliability contract is always that all of these things must pass so that you can release. So you can release. Contents control model evidence could change. All this data chip drift will change, but the release standard remains the same. Okay, remains same. Lessons learned. Okay, so number one is we decompose the narrative into atomic claim. Number two, we target refinement only those failed claims. Number three, hate reliability contract. Separate the verification standard from single model provider and use cases. Okay. Then, how do we scale?

**[17:58](https://www.youtube.com/watch?v=YApwddLn5Rk&t=1078s)** Yeah. You know what? Provide a modular agent service. And we create a shared control plane so that if it's common context, identity evidence, reuse of control reuse those governance steps and apply to multiple use cases. And that's all I want to say today. Uh feel free to grab me if you want to like more details and we are open for inputs communications and conversations. Yeah, compliance team need me to show this, but uh thank you for the attending the session.
