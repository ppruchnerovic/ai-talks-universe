---
id: v6dnEzND-sM
title: "Zelin Wan, Ph.D. - Measuring API Agent Reliability for Long Horizon Tasks in Production"
slug: zelin-wan-ph-d-measuring-api-agent-reliability-for-long
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Zelin Wan"]
channel: "Berkeley RDI"
duration_min: 10
published_at: 2026-08-12T03:07:52Z
video_id: v6dnEzND-sM
url: https://www.youtube.com/watch?v=v6dnEzND-sM
youtube_url: https://www.youtube.com/watch?v=v6dnEzND-sM
tags: []
transcript: true
---

# Zelin Wan, Ph.D. - Measuring API Agent Reliability for Long Horizon Tasks in Production

**Zelin Wan**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `10 min`

[Watch the recording](https://www.youtube.com/watch?v=v6dnEzND-sM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,378 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=v6dnEzND-sM&t=1s)** ZELIN WAN: Hey, this is Zelin Wan. I'm an AI engineer from Postman. So, today, I'm going to present our benchmark called APIFlow-Bench. So for enterprise, when a company, they use the AI agent to do a long-horizon task, they're already facing an issue that a small mistake made by AI agent at an early stage can cause the whole task fail. Yeah, and then when engineer built the product for the service, people usually doing the task, like connecting the building job to a monitoring API, and also creating a record or recover from the rate limit. So our bench, that included those kind of tasks to evaluate the models.

**[0:51](https://www.youtube.com/watch?v=v6dnEzND-sM&t=51s)** And so what we found is, on the single API tasks, most of the model, even the line model, they are very good at the performance. They can reach an 88% and 97% So that looks the problem solved. But the thing is, when we connect those single tasks together into a long, dependent chain task, then the score drops to 44%, 73%. So the task itself didn't getting harder. But if the later task depend on the result of the previous tasks, the earlier tasks, then that's where the model starts to fail. So in an enterprise, a lot of business logic is wrapped in API.

**[1:38](https://www.youtube.com/watch?v=v6dnEzND-sM&t=98s)** And now we are wiring AI agent into those APIs. So a small error caused by AI can become a big problem in the later time. And, nowadays, the real problem is not, can the model answering question? That's a job bot. So you guys all know it. And the real problem is, can the AI agent stay correct across a long horizon of dependent chain tasks? So that's the difference between answering and executing. So let's go to the next one. So one or two failure mode is not enough. We want a minimum set that covers the real API works. So in our benchmark, we break the API works into seven failure

**[2:32](https://www.youtube.com/watch?v=v6dnEzND-sM&t=152s)** modes, authentication, discovery, schema repair, multi-step execution, error recovery, pagination, the statefulness. And we grade each of them separately because they're failing for different reasons. Like Stephanie's, for example, the agent updates something at, say, step three. And then step 15 only works if the agent saves the updates at step three. So a model failing at statefulness has totally different reasons than failing at pagination. And we gradient-- we grade them differently, so it can tell us why the model fails. We approximate real users' workflow with synthetic data. And we build a simulated enterprise API ecosystem, and that mimics the real company's API.

**[3:24](https://www.youtube.com/watch?v=v6dnEzND-sM&t=204s)** And then we generate tasks on top of it. So here is our test generation pipeline. We start from the enterprise API ecosystem generation at the step 0. Then we follow those nice steps to generate tasks one-by-one. And each generate task, we have a validation step. So we use the frontier model to try each task 10 times. And we only keep the task if it passes three times. So why we are doing that? Because when we use the language model to generate task, some tasks are just not solvable at all. So we don't want to generate a bunch of unsolvable task and then use those to evaluate frontier model and clean out the limit of the models. So if a task fails the validation,

**[4:12](https://www.youtube.com/watch?v=v6dnEzND-sM&t=252s)** we feed the trial transcripts and the code to a fixer agent. And this fixer will fix fixed the task. And we rerun those 10 trials again. And then if we keep failing, we discard a whole new one and regenerate a new one. So that's how we make sure each task we generated are solvable and reasonable. So this bench is constructed by an API ecosystem, the task on top of it, one shared harness, and the grader that scored each trials. So for the harness, we designed seven tools. So they work on five different entities. So each task and every trial run on the same harness, but just with different ecosystem and different graders.

**[5:02](https://www.youtube.com/watch?v=v6dnEzND-sM&t=302s)** So for the grader, we have three validators. So two are deterministic, one checks the final state of the environment, one checks the final answer the agent provided. So we use those two to grade each trials. So that's the pathway you guys can see on our leaderboard. And we also use the language model validator. So that's not part of the score, but we use it to flag the doubtful paths so human can review it. So to make the generated task trustworthy, we designed three gates. And each gate can avoid different kind of failing during the task generation. So the first gate is called self-testing. A blank submission should always fail. And if we use the reference answer, but we sabotaged the evidence, then

**[5:52](https://www.youtube.com/watch?v=v6dnEzND-sM&t=352s)** this grid should always fail. Otherwise, there is a problem in the task or validator. And second gate is called solvability. So remember, I mentioned we use the frontier model to try each task 10 times and we only keep three passes test? So that's how we make sure the tasks are solvable. And the third one is golden replay. So when we build a chain task, we put all the reference answer from each subtask together and then append them into this chain task. And it should all pass. So that's how we make sure this formed final chain task is actually correct and it's working as what we want. So for the experiment, we run 467 tasks across 13 generated worlds.

**[6:40](https://www.youtube.com/watch?v=v6dnEzND-sM&t=400s)** And, eventually, we got 11, 20-step-long chain tasks in our batch. So we evaluated 19 models. We run five epochs for each model, each trials. So in total, we got around 44,000 trials. And all the transcripts are available in our leaderboard. You guys can check it online. We are planning to expand the number of tasks, and also the length of the chain tasks in the next version. So here is the leaderboard results for these 20 chain tasks. So GPT 5.5 is on the top. And orange bots are the open-sourced model, and purple bots are the closed models. We actually have this leaderboard updated this week. And we have Kimi K3, and the [INAUDIBLE] Five also included. You guys can check that online.

**[7:31](https://www.youtube.com/watch?v=v6dnEzND-sM&t=451s)** So I would say-- I think I jumped a little bit, but it's fine. So an interesting finding that we found is right now, at this time point, the open source model actually approaching the top group of the closed model. In our bench, the GLM, the Q1 3.7 plus also reached the second, third position. So let me-- here, so here are three takeaways. First, I would say, right now, all the [? line ?] models, even the-- all the models, even the [? line ?] models, they are very good at a single task. So they all got high pass rates in our solo task in our leaderboard.

**[8:18](https://www.youtube.com/watch?v=v6dnEzND-sM&t=498s)** So we cannot reveal the gap between them. And that's why we create this chain task to test their limit. So we saw the case, a lot of-- it happens a lot, that a model made a small, tiny mistake at the early stage. And then that tiny mistake becomes a broken report at a later task. So second, when you guys generate synthetic task, always use the hard gate to make sure the task you generated are trustworthy. So when I say hard gate, the example could be like, 10 times trial must has at least three passes. That's how I did. You guys can figure out more way. And, also, use the golden replay to make sure your reference answer is actually working. And the third one is both the deterministic validator and the language model validator are needed.

**[9:08](https://www.youtube.com/watch?v=v6dnEzND-sM&t=548s)** So when you create a validator grader, be sure to use human in the loop to keep polishing your generator because a wrong validator cannot reveal the true performance of the models. Here, that's all for this present. So the blog and leaderboard are all available at blog.postman.com. If you are interested in whether you're API or agent ready, come talk to me after this session. Thank you. [APPLAUSE]
