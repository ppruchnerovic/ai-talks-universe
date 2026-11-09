---
id: qflLT3SoVbw
title: "Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava"
slug: stop-fine-tuning-to-fix-retrieval-problems-anant-srivastava
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Anant Srivastava"]
channel: "AI Engineer"
duration_min: 20
published_at: 2026-10-04T00:00:35Z
video_id: qflLT3SoVbw
url: https://www.youtube.com/watch?v=qflLT3SoVbw
youtube_url: https://www.youtube.com/watch?v=qflLT3SoVbw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "fine tuning", "RAG", "retrieval augmented generation", "agent memory", "prompt engineering", "context engineering", "LLM architecture", "enterprise AI", "when to fine tune", "fine tuning vs RAG", "AI system design", "knowledge management", "Anant Srivastava", "Oracle", "AI Engineer"]
topics: ["Prompting & context engineering", "RAG, retrieval & knowledge", "Training, fine-tuning & model building"]
transcript: true
---

# Stop Fine-Tuning to Fix Retrieval Problems — Anant Srivastava

**Anant Srivastava**

`AI Engineer` · `AI Engineer` · `2026` · `20 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#fine tuning` `#RAG` `#retrieval augmented generation` `#agent memory` `#prompt engineering` `#context engineering` `#LLM architecture` `#enterprise AI` `#when to fine tune` `#fine tuning vs RAG` `#AI system design` `#knowledge management` `#Anant Srivastava` `#Oracle` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=qflLT3SoVbw) · [Conference site](https://www.ai.engineer/)

## Description

Most AI teams never decide where their knowledge lives. Six months of normal product work decides for them.

Anant Srivastava, principal technologist for data and AI platforms at Oracle, argues that prompt, memory and weights aren't a ladder you climb when answers go wrong. They're three tools for three jobs. Through a support assistant that kept inventing product names after a fine-tune, he shows how architecture builds up by accident. He then gives a simple diagnostic for each: the prompt is for small, stable behavior; memory is for knowledge that's current, large, citable or access-controlled; weights are only for reflexes that have stopped changing. He closes with a circulating architecture where the agent gets better by doing its job.

In this talk:
• How every prompt edit, indexed doc and training sample is an architecture decision
• The diagnostic question for prompt, memory and weights
• Why you fine-tune reflexes, not facts
• Moving knowledge between context, memory and weights over time

SPEAKER
Anant Srivastava, Principal Technologist, Data and AI Platforms, Oracle

CHAPTERS
0:00 Where should knowledge live?
0:15 The real engineering problem
0:50 Three tools, not a ladder
1:20 How teams decide by accident
2:00 Every edit is an architecture decision
2:40 A support assistant goes wrong
4:34 Accumulated, not designed
5:14 Prompt: behavior, not facts
5:59 Example: a support agent prompt
6:59 Memory: current, large, citable
8:09 The wrong job for memory
8:49 Access control belongs in memory
9:14 Example: a code assistant
10:08 Chunking and metadata for code RAG
11:23 Weights: what has stopped changing
12:28 The fine-tuning mistake
13:53 When fine-tuning works
15:08 Medical coding: fine-tune the reflex
16:13 Capability or cost?
16:58 The decision table
17:33 A circulating architecture
19:27 The model is the easy part

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,813 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=qflLT3SoVbw&t=1s)** [music] How do you decide what to put where? For most enterprise AI systems, the interesting engineing problem is not the model itself. The model consumes tokens and produces tokens. Your knowledge lives in files, databases, and APIs. The key architecture decision is how that knowledge reaches inference um from the prompt or the context through the retrieval or memory layer or by model adaptations such as

**[0:51](https://www.youtube.com/watch?v=qflLT3SoVbw&t=51s)** fine-tuning. Today I'm going to argue that this is a decision that most enterprise teams make by accident. And the path to rec to to making it on purpose is to recognize that this is not a ladder that you climb. These are three different tools for three different jobs. So how is this an accident? Well, there are two mechanisms. One is the obvious one. The other one not so much. So the obvious one is that teams escalate. You don't get the right answer from your model. The easy thing is go put something in the prompt like go fix the

**[1:39](https://www.youtube.com/watch?v=qflLT3SoVbw&t=99s)** prompt. Still wrong? Maybe there is something with the memory system or the retrieval system. Let's take a look there. Even then, if you're wrong, hey, you know what? Let's fine-tune the model. Doesn't happen very often, but yes, sometimes teams reach out to fine-tune the model. There is a layer underneath it. The teams that are not escalating are still making these decisions every day. Every edit that you make to the prompt decides what behavior lives in the prompt. Every document that you index decides what knowledge is held in the memory. And every training sample that you bake in will

**[2:30](https://www.youtube.com/watch?v=qflLT3SoVbw&t=150s)** every every training sample that you identify will bake something into the weights. Um all these are architecture decisions. None like that. Okay, let me make it a little concrete for you all. Um, so and I've seen this play out actually. Uh, an internal support assistant just released. In a few weeks, the product manager makes some changes to the prompt to fix the tone of the support assistant. After a few weeks, the support team adds refund policy documents to your retrieval on memory systems. I'll talk about retrieval and memory. I'm teaching it. I'm I'm treating it all as memory, but I'll come to that. Um, and then since your model is not your your agent

**[3:21](https://www.youtube.com/watch?v=qflLT3SoVbw&t=201s)** is not giving you the right answers, an engineer shuffs the product catalog into the prompt. And after a few weeks, the machine learning team decides to train the model or fine-tune the model on support tickets from 6 months ago from up to 6 months ago. All decisions look fine look okay except one by the way. But even I have made such decisions in my in my journey. I have made such decisions of doing such things without really giving it a lot of thought. Um, so when the new product product catalog has launched, looks easy, right? Oh, the engineer has shoved the product catalog into the prompt. Let's put the new product

**[4:09](https://www.youtube.com/watch?v=qflLT3SoVbw&t=249s)** catalog there. And you would think that everything is working fine, but your model or your agent is still giving you product names that don't even exist. How did that happen? Well, the product catalog leaked into the weights when you fine-tuned it on your support tickets. And that is the accident. Your model, your your architecture was accumulated. It was not designed. That is the accident. It is what 6 months of normal product work led to. Nobody owned it. Meaning everybody owned a piece of it. Okay. Um,

**[4:57](https://www.youtube.com/watch?v=qflLT3SoVbw&t=297s)** nobody asked the diagnostic question. Nobody asked where this should where this thing should live. That diagnostic those diagnostic questions are the lens we are going to talk about and the rest of the talk is is about the lens. Okay. So the first part is prompt. What is the job of the prompt? The job of the prompt is behavior, is tone, is the persona of the agent. Things that are small, stable, and editable. The wrong job for the prompt is to store facts. You don't put product catalog into the prompt because you are unnecessarily providing context to your model and paying the cost for it. And when you have too many tokens, you run

**[5:46](https://www.youtube.com/watch?v=qflLT3SoVbw&t=346s)** into lost in the middle problem. The diagnostic for prompt is is the small knowledge small stable and about how to behave rather than what to know. A concrete example for a good prompt use case is a customer support agent for a product SAS. Right now this agent is has a professional tone. It is it offers human escalation after three failures and it provides you concrete next steps. None of this changes per query per user. This is this this exact thing belongs to

**[6:37](https://www.youtube.com/watch?v=qflLT3SoVbw&t=397s)** the prompt. And one other thing is prompt is something I'm not only talking about system prompt. I'm talking about authored instructions for your for your model. So they could also come from MD files. They could also come from other things, right? But this is what I mean by prompt here. The second path is memory. The job of memory is to ground your model or your agent in in knowledge that is current, large and citable. Current meaning it changes faster than you can fine-tune. It changes every now and then. Large is because it cannot be held anywhere. It cannot be held in your

**[7:24](https://www.youtube.com/watch?v=qflLT3SoVbw&t=444s)** prompt. and citable because production AI systems need to be able to point to the source of the knowledge. This is the this is what belongs to memory. Now when I use the term memory people think of agent memory knowledge that is acquired about people about people who about a person who is interacting with the agent right what I'm also referring to here is external memory which is which you retrieve using rag and all that like the refund policies right it's not being managed by your agent it is managed by an external application that is included here so I'm talking both about the agent memory and the memory Mor of the enterprise. Okay. The wrong job of for memory is shoving behavior in or

**[8:15](https://www.youtube.com/watch?v=qflLT3SoVbw&t=495s)** thinking about how to reason with the memory. Now, of course, you can have a graphical kind of rag which will help the agent do reasoning, but that's it. That's where you stop. For reasoning, you got to have the right model. Because if your model cannot reason over two or three or five documents, it won't be able to reason over 50 that you provide. The more context doesn't help if it's not able to reason. So the diagnostic or the question you need to ask is is the knowledge too large to fit changing faster than I can retrain. And another important aspect is whether it has some access control whether it is scope per user. You have got to have that in memory. If there is some kind of

**[9:02](https://www.youtube.com/watch?v=qflLT3SoVbw&t=542s)** access control that this user cannot see the other person's information or the data or whatever, you've got to have that knowledge in memory because then you can control who sees what. A good example for storing something in external memory or memory is a code assistant, right? Which has access to your all your repos as an organization. So uh would you fine-tune your model to learn the code? No. It's it's a simple one, right? It changes very often. You wouldn't do that. You'd finetune your model to learn reflexes, not facts typically. And would you stuff it in the prompt?

**[9:49](https://www.youtube.com/watch?v=qflLT3SoVbw&t=589s)** No, you don't stuff such things into the prompt. You may stuff or you may add certain things that are important in the context window, right? That's something different. But you wouldn't stuff the entire code base into the prompt. Okay? Or or even a part of it if it has no use there. Uh now the other important thing is um when you build a rack system right like for for for your code for your code you need to make sure that you are chunking properly you are using code aware chunking with a perhaps uh and then the other important thing is use filtering. You should denormalize. You should perhaps denormalize things such as who is the what is the repo this code is for. You get a code chunk. You have to create metadata about

**[10:37](https://www.youtube.com/watch?v=qflLT3SoVbw&t=637s)** which repo it belongs to. What is the user what are the users who are allowed to commit and all that because that is what is going to help you get the exact data that you need versus creating a rag mush where you are returning a lot of chunks back from the database without and and then confusing the model. So again the diagnostic is something that's too large to fit changing the faster than you can retrain the model and it's scoped at a certain level. It could be it could be a user, it could be a repo or whatever. All that knowledge belongs to memory. It could be external memory which is your like your applications database or it could be your agent memory as well. Now let's come to the interest more

**[11:26](https://www.youtube.com/watch?v=qflLT3SoVbw&t=686s)** interesting part which is weights. So what belongs to the weight? Something that stopped changing. That is what belongs to the weight. And the only axis that drives this slide is rate of change. You can lock in what has stopped changing and perhaps retrain. And I'm not saying just lock in what stopped changing and just go retrain your model. No, that's not what you do all the time. You would you have to have a very strong reason to retrain your model. So what you do is you lock in what's changing and then go from there. But if you get it wrong, then you could freeze a boundary that's still moving. Okay? And it's not as subtle as like, hey, can I re would I re Nobody's going to

**[12:15](https://www.youtube.com/watch?v=qflLT3SoVbw&t=735s)** retrain their model on like or fine-tune, I meant not retrain, sorry, fine-tune their model on pricing list. Nobody does that. It is more subtle than that, right? And a current version of that is um there is an let's say there is an internal document assistant and the support team or the or your team starts decides to fine-tune the model because it's not giving the right answers. So to teach the domain, it says, you know what, let's fine-tune this model on on our documentation. Let's fine-tune the model on or or maybe not all your all their documentation but runbooks and procedures. And what happens with that? There is an issue. If you do that when a your model will be

**[13:05](https://www.youtube.com/watch?v=qflLT3SoVbw&t=785s)** giving you information that's old. This was actually a retrieval problem. If the model was not giving the right answer, what the model needed was the right chunks, the right pieces of documentation. So basically instead of fixing the retrieval problem, the team actually went ahead and fine-tuned the model. That's not what you should do. Runbooks, procedures, these are facts. These belong to either your me either your agent memory not there but of course your external memory. That is where these things should reside. Not if the if the model is not >> good afternoon. Hello. >> Oh sorry that was I was like who's that? So if your if your model is not giving the right answers, fix the retrieval problem. Don't just go ahead and fine-tune your model. Okay. Uh and if

**[13:55](https://www.youtube.com/watch?v=qflLT3SoVbw&t=835s)** you flip it, same axis. If you reverse it u a good use case where I could fine-tune is let's say it's a hard ambiguous problem such as content moderation or claims processing. Right? When you begin, you can use a frontier model that makes recommendations and humans correct it although inconsistently. Over a period of time, patterns will emerge. Patterns will emerge and you will have sort of a center which is sort of fixed and stable. Okay? And then you will have the contested edge. the the rates of human overrides will flatline over after a certain point and you'll you will most likely emerge in a

**[14:44](https://www.youtube.com/watch?v=qflLT3SoVbw&t=884s)** pattern where you have a contested edge where you still need humans but a center which is pretty stable. Okay, now that center is something you can fine-tune your model on. Okay, but when you do that you have to monitor for drift. Is there a drift in my center? And if that happens then you're going to run into problem. And um actually a stable version of that is I don't know have you heard of medical claims coding? I think we must have like ICD 10 codes doctor's notes are mapped to like codes for different purposes like insurance purposes and all that. So Mount Si Mount Sinai and IMO health actually >> there are 70,000 of such codes by the way. So would you fine-tune your model to learn those codes? They don't change

**[15:34](https://www.youtube.com/watch?v=qflLT3SoVbw&t=934s)** so often. You won't. That's fact. That's knowledge. That's you should not be looking at fine-tuning your model. One of the obvious reasons is is that they change sometimes. And the other is you will need a large test training data to even fine-tune your model on it. Okay. What you fine-tune our model is on the reflex whether whether it is understanding the format of the input and whether it is able to and when it you have to make selection across the formats like which one is the right one that's where you fine-tune your model to do that. Okay. So the diagnostic for fine-tuning is has it has the information stopped changing have the

**[16:22](https://www.youtube.com/watch?v=qflLT3SoVbw&t=982s)** humans converged and more important you should either h have one of these two reasons is the is are you fine-tuning because your model is not capable or are you fine-tuning to save cost and a lot of times it's not capability frontier models are quite capable it usually comes down to cost where you can have a small if you have nice pattern in your work, you can actually perhaps use a small model, fine-tune it and run the volume cheap, right? So, if you don't remember anything from the talk, this is a simple one, right? This table helps me decide. You can b you can bounce your current AI system against

**[17:10](https://www.youtube.com/watch?v=qflLT3SoVbw&t=1030s)** this and and decide this is the lens basically that helps you decide what lives where. Of course there can be exceptions. I'm not saying this is always the rule. There can be exceptions to this but prompt is more about behavior. Memory is about what to know and facts and weights are about how to reason. Okay. And this is the architecture. Your prompt or your context window, your memory and your finetuning needs to circulate. You need to build a right harness around it so that these things can circulate. Your prompt or your context window has information. It generates signals. Some of them becomes durable memory. Okay.

**[17:59](https://www.youtube.com/watch?v=qflLT3SoVbw&t=1079s)** Now when you are restarting a new session things get pulled out of from the memory into the prompt or context window and that's when you're going from the memory to the prompt. The more so this is lot of teams have built this architecture but what people are looking to are focusing on building is the right side the memory to fine-tuning flow. Okay. Now what happens is when you build an agentic system over a period of time you will have retrieval patterns. You will have formats that you think the model should reflexively know. So those things move from your memory to fine-tuning once you have fine-tuned. So that's memory to weights. Once you have fine-tuned

**[18:48](https://www.youtube.com/watch?v=qflLT3SoVbw&t=1128s)** what is worth retrieving changes if you have changed if you have fine- tuned your model on the formats of like notes and the ICD codes you don't have to retrieve certain examples from your memory or external memory each time and provide it to the model because now the model knows the format reflexively you don't have to provide examples to it that hey this is the format or that is the format so that's weights to memory and so basically This becomes a loop over a period of time and the agent gets better at its job by the virtue of doing its job. Okay, that's the architecture. So what I would like to conclude with is the model is is the easy part.

**[19:38](https://www.youtube.com/watch?v=qflLT3SoVbw&t=1178s)** What you build around the model, the harness around the model that helps you store the right information at the right place and circulate among them is the key architecture that you got to build. Thank you. Thanks for coming up.
