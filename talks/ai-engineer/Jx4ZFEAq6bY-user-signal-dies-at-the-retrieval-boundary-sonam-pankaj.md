---
id: Jx4ZFEAq6bY
title: "User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch"
slug: user-signal-dies-at-the-retrieval-boundary-sonam-pankaj
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Sonam Pankaj"]
channel: "AI Engineer"
duration_min: 16
published_at: 2026-06-28T17:00:20Z
video_id: Jx4ZFEAq6bY
url: https://www.youtube.com/watch?v=Jx4ZFEAq6bY
youtube_url: https://www.youtube.com/watch?v=Jx4ZFEAq6bY
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
topics: ["Evals, observability & reliability", "RAG, retrieval & knowledge"]
transcript: true
---

# User Signal Dies at the Retrieval Boundary - Sonam Pankaj, StarlightSearch

**Sonam Pankaj**

`AI Engineer` · `AI Engineer` · `2026` · `16 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=Jx4ZFEAq6bY) · [Conference site](https://www.ai.engineer/)

## Description

Utility is all you need! Closing the Agent Learning Loop with Utility-Ranked Memory

Most production agent systems have a fatal flaw: they start every run from a blank slate. You have traces in your observability stack and pass/fail judgments in your eval suite, but the agent that runs tomorrow has no memory of why yesterday's runs succeeded or failed.

This talk exposes the gap between observation and action and shows how to close it.

We'll examine why current memory approaches stall: conversation buffers that only remember recency, semantic systems that retrieve what sounds similar rather than what helped, and reflection-based methods that capture lessons but don't learn which ones actually work. The core idea: utility-ranked memory. Treat memories like a credit score. When a memory is retrieved and the run passes, its utility rises. When the run fails, its utility falls. The ranking formula combines semantic similarity with outcome history.

There is also a demo with an example of the product SQL agent, of how it updates the context for the right outcome, everything happening at runtime.

Speakers:
- Sonam Pankaj (StarlightSearch Inc): Sonam is the CEO and Co-Founder of StarlightSearch. She is also the co-creator of embedanything, which is a Rust pipeline for RAG, which got contributions from Elastic, Milvus, and Qdrant, and has over 450k+ downloads. Prior to Starlight Search, Sonam spent years in developer tools and AI infrastructure, and has worked as a generative AI Evangelist, GTM lead at Articul8, a spin-off of Intel, and AI Researcher at Saama. She has been presenting talks for the last 10 years, and loves to interact with developers. She has been constantly speaking at Berlin Buzzwords, Europe's largest search conference, PyCon DE, and PyData. She also got an opportunity to present her work at Google, Deutsche Bank, and JetBrains.
X/Twitter: https://x.com/sonam_pankaj_

## Transcript

*1,867 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=1s)** Hey everyone, I'm Surim. I'm the CEO and co-founder of Starling Search and today my talk is a signal's die after retrieval boundary. So, we'll look into uh what are agents essentially, why agents fail, what is uh the cause of fails in retrieval particularly, and how to make actually signals cross the retrieval boundary, and how to make your agent basically outcome fair. So, uh let's get started. What is an agent? An agent is an LLM that has agency to reason, invoke tools, uh interact with the real world, retrieve uh the memory to complete the task. One major loop here is missing is uh learning. It should also learn from what

**[0:48](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=48s)** worked and what didn't work. Suppose uh if I had to uh explain what is agent, I I can explain with react agent. So, if I had to explain uh what agent does, I would explain with react agent. So, basically use it from the agent and execute it in a loop, uh client to retrieval search, and then pause when the task is complete. This is very basic react architecture. One thing that is missing is how to make agent learn from the outcome. So, agent keeps failing at the same task. Gartner reported 85% of AI just failing traction. So, it's in McKinsey's 2025 report. The problem came out to be

**[1:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=97s)** most of the time is that retrieval is static. 73% of our uh pipelines fails because of retrieval, not generation, and context stuffing. So, a recent uh post from Ram Sriram, the ex-CTO of Pinecone said "Uh we have been optimizing for the wrong thing. You are paying a lot for your agent's memory. This is probably broken, and we have been optimizing for the wrong things. We made wrong answers appear faster and cheaper, but we forgot to make retrieval learn." So, why does this does does does it matter? Again, uh, the third problem is agents are not outcome-informed. So, there's a missing layer between evals and action. Your observability has

**[2:27](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=147s)** all the traces, uh, all the stack that capture observability is the stack that capture every tool call, every LM completion, every exceptions. Your eval suite judges whether the final output was correct or wrong, basically pass or fail. But these evals are not reflected in agent, uh, context, skills, and defines my agent action in any ways. Right? So, the agent doesn't have any access to why yesterday's runs, uh, runs passed or failed. The eval signal dies in the dashboard. This is a missing layer, a system that consume traces, absorb eval, and convert both into retrieval guidance

**[3:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=194s)** for future runs. So, there's a manual improvement task, and engineer actually has to sit and see if the eval and observability perform well. Rewrite the prompt, redeploy it, upgrade either and create your expensive model, restructure to our harness, or fine-tune the custom models. Why are current memories failing? Why memories was designed to actually address this, but, uh uh it's not. So, let's see, uh, a what we have in our the current system uh, and current memory is that they basically store user preferences, profile, conversation history, or long-lived personalization.

**[4:04](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=244s)** So, chat experience is not self-improving learning systems for production. If you see the already existing approach in the market, there's a LangChain, there's Mem0, which does extracted past preferences. The user's retrieval signal is embedding similarity. Does it learn from outcome? No. Uh so, we have come up with something called utility score, which is a similarity weighted by how useful it is for the agent to execute the task. It has actually the history of past pieces and past outcomes. So, we came up with Agent RX, and that is agent's the runtime experience. It's a runtime

**[4:53](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=293s)** layer that let the large language agent improve from experiences without retraining, fine-tuning, or manual prompt engineering. How it's a little different from compile time like DS5 because of you bake in all the lessons in the prompt, here is actually improving while it is executing the task. So, which again introduces utility score. So, you do not retrieve by keyword, you do retrieve by semantic similarity to the current task weighted by whether those memories have historically helped or hurt the execution or the outcome. The event outcome becomes a first-class signal in the retrieval re-ranking and not just for retrieval. One of the

**[5:42](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=342s)** key things is it treat memory as reasoning, not as facts, statistics, fact with no context and no history, but reasoning. Like suppose if if there's a if there is a customer support bot looking for a refund, you will not really say, "Hey, user prefers uh uh dark theme or user prefers to be called by a shorter name." It's actually reason about query like if some someone asked for refund, you should check the settlement before refunding it so that the the the customer doesn't get paid refund twice. So, we act based on usefulness. Context is updated based on task. So, this is a

**[6:31](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=391s)** very big thing because most of the agents deal with context stuffing and this has been brought up in the past and learn from history and reasoning, right? Talking about benchmarks. So, we have benchmarks our memory system reflect on towel bench which essentially measure if agents have followed a policy well or not. So, we have seen the performance improve from 66 to 76% without baking in uh skills and with skills reflect performance at 80. So, once there are enough memory like 10 memories, uh what we do is we bake in the

**[7:18](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=438s)** reasoning and the understanding into skills so that your agent always remains updated. What happens most of the time we have seen suppose you have a product SQL agent and there's a system there's a column in system prompt. Even though that column is no useful anymore, it remains in the system prompt. So, there's no system right now that can update that, "Hey, there's no column uh right now called this. So, maybe probably you shouldn't entertain it in the future. And this is possible with skills that because it is always uses calls that skill updated skill all the time. And the similar behavior has been seen in GPT-5.4. Uh, we have also benchmarked it on agentic task.

**[8:06](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=486s)** Which essentially test a model's ability to reason, plan, and use tools or extended multi-step workflows rather than measuring a static Q&A. So, you can see here, uh, when does it was the human last exam with drug, it get 47.5. If it is starting from the baseline 35.7. Uh, with the other memory system, it gets to 58.2. But with the refined memory system, uh, it gets to 61.3%. So, this this kind of trend is shown in another, uh, agentic benchmarks, uh, as well, like Big Code Bench, like Long TV, etc. So, of course, there are limitations to this uh

**[8:54](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=534s)** to this approach. First of all, there's a cold start. So, in the beginning, it's pure semantic search until, uh, enough reviews have been accumulated. Uh, there's a utility drift. Maybe sometimes, uh, similar memories could come up. There are a lot of problems that could come at scale with this experience, but we have combat most of them. Uh, there's a review quality. So, noisy labels can make the utility noisy as well. And there is, uh, hyperparameter called lambda that is associated with credit and re-ranking. So, we have built reflect in such a way that most of these problems and most of these elements are now reduced except for cold start which we cannot do much

**[9:43](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=583s)** about it. Uh let's get into the demo. So let's check this demo. Um So it's a basically a product SQL demo. I'll give ask it to search some product in SQL database and see if it is able to find it out. So can you find me a gaming mouse? Zero memories retrieved. I couldn't find

**[10:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=632s)** a gaming mouse. Uh okay. So maybe let's just go and see what's happening in the dashboard. Okay. It came out that I'm going on another benchmark that with the agent bench with actions essentially measures if agent has actually done the right reasoning, planning, and uh have followed. Which essentially test a model's ability to reason, plan, and use tools over extended multi-step workflows rather than measuring a static Q&A. So you can see here

**[11:21](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=681s)** uh with the suppose the human last exam uh with drug you get 47.5. If it is starting from the baseline 35.7. Uh with the other memory system, it gets 258.2 but with the result memory system, uh it gets 261.3%. So, this this kind of trend is shown in another uh adaptive benchmarks as well like big code bench, my long TV, etc. Wait, let's check. I couldn't find I couldn't find any gaming mouse in the product catalog. So, suppose I want to market fail and sell it give any relevant

**[12:10](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=730s)** No. Because there is a there is a wireless mouse in the database. And I have submitted the failure. Uh this was the input. This was the response. I couldn't find any. And this was a trajectory and tool quality. So, you can see the product is empty with this product or with this query. Let's uh let's check again what happens now. Let's see now now what happens. Okay, ID uh

**[13:05](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=785s)** So, it searched a wireless mouse. Uh Let's see what happens in the dashboard now. Finally, a gaming mouse was input. The response was I found a product related to mouse as the mouse failed to find any kind of relevant. Let then, The most important thing is how the tool call evolved. You can see that previously the tool calls or the trajectory used to look just with one search, that is search products it called. And the product was empty. Now, the trajectory has changed in the production and it found something in the product

**[13:54](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=834s)** and it uh is still calling search product to call but it is getting some answer that we fed in as a feedback. So, uh that's the demo and the most important thing that is happening over here is it's forming memories which is retrieved based on the utility score that is the score which basically keeps improving keeps re-ranking itself on the basis of how useful that memory was. So uh You can see from this traces past traces which memory uh so this memory scores keep changing and after certain while after suppose uh

**[14:44](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=884s)** five reviews maybe can bake in these findings or these new updates in a skill. Without so without changing the existing prompt you can actually update certain things that agent draws a lot from. So, uh you can update the skill which is very cool. So, uh I hope everything was I hope you get to try this new feature this new uh runtime experience that we have built. You want more details you can visit our website and you can also contact me if I have still

**[15:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=932s)** my grace@alishascollection.com. I will reply. Thank you.
