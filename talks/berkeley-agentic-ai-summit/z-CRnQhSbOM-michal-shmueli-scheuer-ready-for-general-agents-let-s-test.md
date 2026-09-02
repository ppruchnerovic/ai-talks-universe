---
id: z-CRnQhSbOM
title: "Michal Shmueli Scheuer - Ready for General Agents? Let's Test It"
slug: michal-shmueli-scheuer-ready-for-general-agents-let-s-test
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Michal Shmueli Scheuer"]
channel: "Berkeley RDI"
duration_min: 14
published_at: 2026-08-12T02:03:42Z
video_id: z-CRnQhSbOM
url: https://www.youtube.com/watch?v=z-CRnQhSbOM
youtube_url: https://www.youtube.com/watch?v=z-CRnQhSbOM
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Michal Shmueli Scheuer - Ready for General Agents? Let's Test It

**Michal Shmueli Scheuer**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `14 min`

[Watch the recording](https://www.youtube.com/watch?v=z-CRnQhSbOM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,852 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=1s)** MICHAL SHMUELI-SCHEUER: Good afternoon, everyone. Are you ready for general agents? Let's test it. So this talk is based on three publications from ICLR, ICML, and hopefully NeurIPS very soon. So if you look on Richard Sutton's Bitter Lesson, then we basically means that generality ultimately wins over domain-specific approaches. Looking back on machine learning AI, and even if we look not that back on language models, so we all started with domain-specific models

**[0:52](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=52s)** doing tasks like summarization, extraction, and so on and so forth. And eventually, we all moved to big models that actually are capable of doing all tasks, all different tasks, different type of tasks. If we're looking on agents today, we mainly see what we call domain-specific agents, which are basically agents doing finance, customer care, or any specific domain. And we, and also some other colleagues-- I mean, just from learning from the past, saying that the future will go to what we call general agents. So, what are agents, and how we evaluate them? So I think I've heard it many times during this conference.

**[1:41](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=101s)** But basically, agents are a complex. They are the LLM that is there, along with the harness, the memory, reasoning, search, and so on and so forth. The agent is interacting with an environment via actions and observation through some protocol. And if we want to evaluate the agent, then we have usually a benchmark. And we prompt the agent with a task. And we collect the outcome from the environment and calculate the metric. So we define domain agent as domain that the knowledge of the domain is encoded within the agent. So basically, once the domain, the knowledge is encoded,

**[2:32](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=152s)** the agent can start working with the environment. When we say general agent, you no longer see the domain-specific knowledge within the agent. And we assume everything is on the environment side. And we basically looking on the adaptability of the agent to explore and work with new tasks. And eventually, what we are pushing is that if we have this model, then the general agent can work with different type of environments without the need to re-engineer for each one of them. So when we talk on general agents, it's no longer the performance in a single task. But we want to understand how it works on many different environments and tasks. So the main promise here is that one general agent.

**[3:24](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=204s)** You can use it for many use cases. You no longer need to have, I don't know, 100 different domain-specific agents. There is a centralized approach, the effort. So we improve it. And all the use cases benefit from the improvement of the memory of the search and so on. And also, like we have now in LLM, if we start with the starting point is a general agent, we can still customize it. But the starting point is much better. It's a better and robust agent that we should do. Saying that, I know that there are other views, that domain-specific agents are important because we

**[4:17](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=257s)** have more control. They are more efficient, and also more predictable. Other issues could be around the risk. I mean, we give the general agent more autonomous, which can lead to unforeseen risk. Some also claim that the model should be general and not the agent. And actually, I encourage you to read the paper. It was a position in a paper in ICML. And you can understand both view in details. So let's assume that I convinced you that general agents are the future. So in order to say that an agent is general, we have to make sure that it is indeed working on different environment and tasks. And how we do it, we need to evaluate.

**[5:06](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=306s)** However, here is the trick. It's not a trivial. Because there are issues of standardization, mainly on the agent interface, environment interface, and the researcher interface. And here, I think contrast to what we saw in the LM arena, we are talking about benchmarks that are open sourced by-- I know many students and many other efforts that we are using them. So if we look on issues, so we see for the agent interface, each benchmark, they expect the agent to work differently from each agent, expect the environment to provide different information. And also the researchers, each one implement its own code for the agent benchmark combination. And this is not scaling.

**[5:59](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=359s)** I mean, if we want to try many agent on many benchmark, it's just not scale. And if we look on what exists today-- and again, I'm not going into details. You can find everything on the papers. Looking on all the frameworks that Exist, You will not see even one that supports multi-protocol benchmark, multi-protocol agent, agent plug and play, and the generality. So looking on very different tasks. And this is actually where we are stepping in. And we develop a framework for agent evaluation, called Exgentic. And here, you can bring in any general agent that you have,

**[6:53](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=413s)** any benchmark. And it supports all the type of integration and how we do it. Again, I'm not going into details. But the main ideas that we introduce a new mediation layer that we call the Unified Protocol. And so still, the agent, using the protocol that it comes with. And similarly, the benchmark, it uses the protocol that it was developed with. And what we are doing, we are doing a transformation between those two. So we are not changing anything in the benchmark. So they work as they intended. And similarly, we are not touching the agents. We're just doing the mediation layer. And this is based on the commonality

**[7:41](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=461s)** that we saw across benchmark and agent, which basically the three primitives of task context and actions. So given this, we publish what we call the open agent leaderboard. And this approach allow us to take any agent harness with any model and any benchmark and do this Cartesian product. So what we see? So basically, as you see, we have the agent column followed by a model. And then all the tasks.

**[8:28](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=508s)** And we calculate, of course, the average success. But in addition, we also calculate the cost, which are, of course, important. And then again, we can look on the Pareto frontier. And based on what you are after can select the specific configuration that fits you the most. So it can be very expensive if you want accurate work. Or you can have some-- less accurate, you can go for the cheaper models. What other insights that we already get from the results? So I think the first insight is that general agent, they adapt without any needs to do something. And we see that on average, again, most of them

**[9:20](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=560s)** can do all the tasks. But they can do all the tasks that we introduced to them. Currently, the model matters the most. I mean, the quality of the results is mainly derived by the model. But we see also some effects of the agent harness. Another point is that-- and I focus here, is that, actually, when we compare the quality of the general agent versus domain-specific, agent. And here, what you see is for each one of the tasks, we went to the leaderboard and took the top domain specific agent. We then compare it to the top general agent. The results that we got on our evaluation.

**[10:12](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=612s)** This is the blue, the top line. You see that. They are quite competitive. Without the need, we didn't touch the agents. So no need to do this re-engineering and engineering, and it still works quite well. One also not surprising but I think important point is that while having similar scores, we see that agents behave differently. So we see that some agents, they fall very cheap and fast, while others spend you a lot of money. At the end, both are false. But it's important to understand those effects. And one more point I want to put is on the open weights model. So in general, we can say that they are not general reliable. And to give you some information,

**[11:01](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=661s)** so first on average, they are behind the closed model. You can see it here, we have Kimi and DeepSeek. And then we see that in some tasks that probably they were not trained on. They really failed. I mean, they sink. So this on the left is what is known as upward application. Different types of application. And you see the quality of Kimi and DeepSeek. And this is average on all different harness. So we have five harness, agent harness. And on average, they could not perform well on each of these combination on this task. So they are just not doing well on some of the tasks. I think another interesting point

**[11:53](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=713s)** is that the open weight model are more sensitive to the agent harness. And what we see here on the right? On the right, we see, for example, for Kimi, we took the Kimi with the best hardness versus Kimi with the worst hardness. And we see there is a 18 percentage difference. And I think this is very important and has a lot of implications, which basically means that you cannot just change the harness. And assume that you will get the same quality for the open weights. For the closed model, it's more safe. But when you move to the open weight model, you have to be much more careful. And you need to do the evaluation if you want to change the harness. And on the other side, you see that when

**[12:41](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=761s)** we looked on OpenAI agent, and while for Claude and Gemini it really lifts the results. When we combine it with the open weights model, they just crashed. So it's not that you can fit any model with any harness. You have to be very careful about it. I'll just mention that I've heard that they are cheap. I mean, in one of the other talks. So it's not always the truth. So if you look on the cost quality, they are not cheap. They are competitive. So again, we tend to think that they are cheap, but it's not always the case when you look on numbers. Finally, just to let you know, when we run Exgentic,

**[13:33](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=813s)** we collect all the traces in OTel format. It is open source. You can get it on Hugging Face. There are more than 10K traces that you can collect and understand how the agent, the whole full traces. What is next? So actually, we are now coming with the Exgentic V2. It's a little bit different approach that something that we learn from V1. It's based on the primitives of Kubernetes and Dockers. In addition, we are working on evaluation of agentic inference platform and new topic of AI native system evaluation. So if you are in either one of this topic, just approach me. Thank you.

**[14:23](https://www.youtube.com/watch?v=z-CRnQhSbOM&t=863s)** [APPLAUSE]
