---
id: LUemJGG2k4c
title: "60% Faster Time-to-Interview: Transforming Hiring with AI Agents with LangChain"
slug: 60-faster-time-to-interview-transforming-hiring-with-ai
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 18
published_at: 2026-07-22T13:41:08Z
video_id: LUemJGG2k4c
url: https://www.youtube.com/watch?v=LUemJGG2k4c
youtube_url: https://www.youtube.com/watch?v=LUemJGG2k4c
tags: ["LinkedIn", "Tracy He", "Shang Liu", "hiring agent", "LangGraph", "LangChain", "LangSmith", "AI recruiting", "small business hiring", "plan execute replan", "human in the loop", "harness engineering", "deterministic agent", "checkpoint trimming", "state flag chaining", "one-shot tool guards", "signal-only tools", "agent platform", "conversational memory", "experiential memory", "LLM-as-judge", "agent evaluation", "agentic AI", "Interrupt conference"]
topics: ["Agents & orchestration", "Evals, observability & reliability"]
transcript: true
---

# 60% Faster Time-to-Interview: Transforming Hiring with AI Agents with LangChain

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `18 min`

`#LinkedIn` `#Tracy He` `#Shang Liu` `#hiring agent` `#LangGraph` `#LangChain` `#LangSmith` `#AI recruiting` `#small business hiring` `#plan execute replan` `#human in the loop` `#harness engineering` `#deterministic agent` `#checkpoint trimming` `#state flag chaining` `#one-shot tool guards` `#signal-only tools` `#agent platform` `#conversational memory` `#experiential memory` `#LLM-as-judge` `#agent evaluation` `#agentic AI` `#Interrupt conference`

[Watch the recording](https://www.youtube.com/watch?v=LUemJGG2k4c) · [Conference site](https://interrupt.langchain.com/)

## Description

Tracy He and Shang Liu from LinkedIn's hiring team walk through how they built a hiring agent that cuts time-to-interview by 60% for small businesses — from the architecture evolution (static workflows to LangChain chains to a LangGraph central planner with a plan-execute-replan loop) to the platform infrastructure (conversational memory, experiential memory, and skill registration on LinkedIn's agent platform). They explain why LinkedIn chose LangGraph over 89 evaluated frameworks, and then share two hard-won lessons: why the LangGraph interrupt primitive didn't fit their use case and how they built a stateless, context-driven human-in-the-loop instead, and how harness engineering (context management, output format determinism, node-change determinism via state flag chaining and one-shot tool guards) closes the gap between a probabilistic model and a dependable product.

Chapters:
0:00 Introduction: 60% faster time-to-interview for small businesses
0:44 Why hiring is an agent problem
1:17 The hiring loop: plan, act, observe, adapt
1:58 How the hiring agent works end to end
3:08 Architecture evolution: static workflows to LangChain chains to LangGraph
3:51 The LangGraph breakthrough: central planner and plan-execute-replan
4:17 Three design pillars: single agent, plan-execute-replan, closed-loop feedback
5:33 Why LinkedIn chose LangGraph over 89 frameworks
6:10 Zero rewrite: LangGraph builds on existing LangChain primitives
6:25 LangSmith deeply integrated into day-to-day troubleshooting
7:06 LinkedIn agent platform: conversational and experiential memory
8:01 Skill registration: hiring intent, profile evaluation, applicant skills
8:24 Middleware and hooks: PII detection, pre and post format hooks
8:52 LangGraph checkpoint schema and context parameter design
9:52 Using LangSmith with Claude Code for trace-level debugging
10:19 Agent evaluation: full trace capture and LLM-as-judge
11:43 Lesson 1: LangGraph interrupt primitive didn't fit — here's what we built instead
13:17 Context-driven human-in-the-loop: stateless scalability and minimum checkpoint size
14:53 Lesson 2: harness engineering for determinism
15:40 Context management: checkpoint trimming and history summarization
16:35 Output format determinism: template confirmation and programmatic assembly
17:01 Node-change determinism: state flag chaining, one-shot tool guards, signal-only tools
17:51 Summary and takeaways

Resources:
→ LangGraph: https://www.langchain.com/langgraph
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com

## Transcript

*2,253 words · source: supa (en, exact timings)*

**[0:05](https://www.youtube.com/watch?v=LUemJGG2k4c&t=5s)** >> Hi, everyone. I'm Tracy and this is Shang. We are engineers from LinkedIn's hiring team. And today we're going to talk about how we built hiring agents using LangChain and LangGraph that cut time to interview by 60% for small businesses. Some quick agenda. So we will cover why hiring is an agent problem, then how we evolved and adopted LangChain and LangGraph, and also how we evaluate it, and last, some lessons learned. So why is hiring an agent problem? When we talk to small business hiring managers, oftentimes we hear that the biggest challenge

**[0:54](https://www.youtube.com/watch?v=LUemJGG2k4c&t=54s)** is hiring takes too much time. And on average, they spend 9.5 hours a week just reviewing candidates and deciding who to reach out to. And for a small team, like a startup, that's already a few days a week gone before any interview even happened. So that's why. And also, hiring is a loop. It's not a one-shot task where you post a job and you get the perfect candidate. So you start with some job description and you see who applies, and you start to realize some of your must-have requirements are actually nice to have. Or vice versa. Then you have to modify your job description again, and source more people, and then re-evaluate your applicant list, and again, again, repeat until you find

**[1:47](https://www.youtube.com/watch?v=LUemJGG2k4c&t=107s)** the perfect candidate. And this is the exact shape of an agent problem. You plan, you act, observe, and adapt. And that's why we built the hiring agent. And our process begins with a simple guided intake, where our agent collects your hiring requirements and starts with the job title. Then our agent will generate the job description for you. And once you confirm and post the job, our agent will immediately source some strong-fit candidates for you to review. And you can either invite them to apply to your job or provide feedback to our agent so that our agent will align with your expectations from day one.

**[2:35](https://www.youtube.com/watch?v=LUemJGG2k4c&t=155s)** And once applications come in, our agent will evaluate the applicants for you based on the qualifications that you define. And you can also send an AI-powered screening interview to them, so you are saving time for meaningful conversations with the right talent. And last but not least, you can always chat with our agent, ask any hiring-related question, or ask the agent to take any action on your behalf. Now we have just seen how our hiring agent automated the entire process. We will talk a little bit more about the architecture behind it and how we evolved. We started with some static workflow where we used scenario branches — if this, then

**[3:27](https://www.youtube.com/watch?v=LUemJGG2k4c&t=207s)** that. And all the transitions were hard-coded. It worked until our system became a little bit more dynamic. So we adopted LangChain where we implemented two chains with sequential execution. While this provided some partial abstraction, it still lacked the dynamic decision-making that we needed. And our final breakthrough came with adopting LangGraph. And this is the true agentic control model where we have a central planner that drives a plan-execute-replan loop. And the key difference here is we use LLM for decision-making, which makes our system significantly more robust and adaptive. We just talked about how we shifted

**[4:19](https://www.youtube.com/watch?v=LUemJGG2k4c&t=259s)** to an agentic control model using LangGraph. And let's dive into some practical implementation. Our design has three key points. First, we use a single agent with centralized reasoning. And instead of a rigid, chained process, now we have one core LLM-powered planner that's responsible for all the high-level decision-making. And this main brain will take care of, make sure there's coherence, and allows complex and multi-step problem-solving. Next, our entire workflow operates on a plan, execute, replan pattern.

**[5:08](https://www.youtube.com/watch?v=LUemJGG2k4c&t=308s)** And this is the dynamic core of LangGraph. And finally, we ensure continuous improvement through a closed-loop feedback and observability, which we will talk a little bit more about later. And overall, our system is really simple, but backed up by strong tools and skills, we are able to fulfill all the requests from our users. So, Shang, why did we pick LangGraph? >> Great question. Actually, LinkedIn selected LangGraph among 89 agent frameworks after thorough research and evaluation. So there are a couple of reasons. First of all, some agent frameworks don't provide enough low-level primitives. Some agent frameworks focus on areas that LinkedIn's infra already has.

**[6:02](https://www.youtube.com/watch?v=LUemJGG2k4c&t=362s)** And LangGraph is the agent framework that complements our existing infrastructure. Also, LinkedIn agents already speak LangChain. We have runnables, tools, callbacks, and LangGraph builds on those primitives, not around them. So adopting LangGraph means zero rewrite for us. And last but not least, LangSmith has been deeply integrated into our day-to-day troubleshooting practices. And we look forward to bringing more and more features and new products announced yesterday to our production, and that's amazing. So in conclusion, it's not only because of LangGraph itself, but also because of the whole ecosystem that's built around it.

**[6:57](https://www.youtube.com/watch?v=LUemJGG2k4c&t=417s)** And everything comes together. internal systems, including our messaging platform. So there are two types of memory persistence mechanisms within the LinkedIn agent platform. One is called conversational memory, which stores the chat histories. And that also talks to the messaging platform with deep integration.

**[7:44](https://www.youtube.com/watch?v=LUemJGG2k4c&t=464s)** Also, there is another one called experiential memory, which stores state checkpoints. And there are also some other memory applications built on top of that — for example, episodic memory and semantic memory to empower the memory experience. In terms of skill registration, the LinkedIn agent platform allows different teams to register their own skills based on, for example, their teams or their business needs. And we specifically make use of the hiring intent skills, profile evaluation, and applicant skills to achieve our functionalities. Middleware and hooks. LangChain has such good stuff. LinkedIn has already integrated to some extent —

**[8:34](https://www.youtube.com/watch?v=LUemJGG2k4c&t=514s)** for example, PII detection, context summarization, and persistence. I know DeepAgent has already done this well as well. And pre-hooks and post-format hooks ensure some determinism that we really want in our agent, specifically — and I'll talk about it a little bit later in our lessons learned. So this is a LangGraph checkpoint schema that we're actively using within our agent. You can see besides input and output, which also includes the suggested prompts as part of the outputs. We also have a lot of context-related parameters, which are the key for our agent. So especially the context parameter itself, it has tons of parameters. For example, there are two main types. First one — it should be passed through the whole conversation

**[9:26](https://www.youtube.com/watch?v=LUemJGG2k4c&t=566s)** or whole thread, like current intent, job ID, applicant list, applicant ID. That's global. And there are also a couple of parameters that will only be activated based on case by case — like, for example, the pending learnings, a formatted pending learnings. Once that's generated from the previous node, for example, it should be passed through to the next node within the context view. And this is what I mentioned before, our LangSmith experience. Thanks to the LangSmith trace skill that is provided by LangSmith, we got a chance to integrate with Claude Code. That's how we actually use it day by day, hour by hour, minute by minute to troubleshoot. So the real experience is a trace ID and a root cause output, which is very powerful, straightforward,

**[10:16](https://www.youtube.com/watch?v=LUemJGG2k4c&t=616s)** and convenient. So next is the agent evaluation. So we just saw how we leverage LangSmith for deep observability. This is actually an essential step for the closed-loop feedback that I talked about earlier. And to understand how we use this data to make our agent better, we will talk about the evaluation process that we use. So it starts with evaluating with LangSmith — capturing the full trace of every interaction that the user has with the agent, not just the final answer but the full trace. The context retrieval, the tool calls, and also every decision step that we have. However, due to our LinkedIn policy, we're not able to send everything to LangSmith yet

**[11:08](https://www.youtube.com/watch?v=LUemJGG2k4c&t=668s)** for our production data, so we built something similar — mirroring what LangSmith does. And together, we send that data into our human annotation and also our LLM-as-judge. And it will capture any nuances that the model might miss. And our final step is to optimize. And today what it means is we will manually refine and retune our prompts and model based on what the annotation surface. And the path forward is using online optimization, which is what we just learned about yesterday as well. And we're looking forward to integrating it and closing our continuous learning loop without too much human in the middle.

**[11:57](https://www.youtube.com/watch?v=LUemJGG2k4c&t=717s)** And for today, it's human-driven, and tomorrow it will be continuous. So we've talked about how our agent evolved and how we architect and design it. And along the journey of building this adaptive agent, we have some lessons learned that we want to share today. So lesson one: LangGraph provides primitives, but product constraints determine the real architecture. So Shang just talked a lot about how we integrated LangChain primitives and how they were useful and powerful, but not everything fit into our use case. And the story behind this lesson is: we have our agent watching recruiter workflows and we want to make some suggestions.

**[12:48](https://www.youtube.com/watch?v=LUemJGG2k4c&t=768s)** For example, it will say: looks like you are moving a candidate without a degree in computer science to top fit. So is the education requirement really a must-have? Do you want me to remove it? So what's next is the user could either say yes or no. But the interesting part is they could just walk away or completely change their topic to something else. And so our first instinct was using LangGraph's interrupt primitive. It pauses execution mid-node, checkpoints the graph, and waits for input from the user, and resumes from the same spot. And this worked beautifully for long-lived graphs and clean yes-or-no flows.

**[13:39](https://www.youtube.com/watch?v=LUemJGG2k4c&t=819s)** However, it doesn't really fit our use case. So we built a context-driven human-in-the-loop instead. So every input will run the graph end to end. And at the end of the graph, we will persist minimum cross-turn context. In the example that I mentioned, we will be storing something like: suggest removing education requirement and waiting for user's confirmation. And when the next message comes in, our planner will see: is it relevant to the suggestion? Do we want to confirm it, reject it, or pivot to something else, meaning we allow the context to expire. With this approach, it gives us stateless scalability, full request tracing, and also keeps our conversation

**[14:30](https://www.youtube.com/watch?v=LUemJGG2k4c&t=870s)** flexible. But most importantly, we control our checkpoint size. Instead of tracking — instead of storing the full graph, we are just persisting the minimum context. And Shang's going to talk about why that is important to our agent and why we picked this path. >> Yeah, models are probabilistic, as you know, but agents need to be more deterministic, especially for our use case, based on harness engineering. And as you all know, with the improvement of the model capabilities, a lot of the harness engineering efforts will eventually be replaced. We also believe that there are always some parts of the harness engineering work that can never be replaced,

**[15:18](https://www.youtube.com/watch?v=LUemJGG2k4c&t=918s)** and that's the customization, and that's differentiation, and that's how you make an agent succeed and shine. So I specifically want to share a few lessons that we learned on how to do the harness engineering to make our agent better and closer to our user requirements. So each agent has its own functional focus. So the priorities in harness engineering are really different. For example, coding agents focus on code correctness, and they need to have more exploration capabilities to get to the final answer by trying different approaches. For example, shopping agents — they need source grounding and safe purchasing action boundaries to ensure safety. And with the LinkedIn hiring agent,

**[16:07](https://www.youtube.com/watch?v=LUemJGG2k4c&t=967s)** we want to ensure the consistency of recruiter- facing action paths, as well as trust and compliance. So there are a couple of efforts. First, context management, as we have been talking about all the time. Checkpoint trimming, history summarization, as well as context conflict management — when different context providers have conflicts, we need to handle that. So this tells the agent what needs to be remembered. And output format determinism. Sometimes we want the agent to output something consistently across different runs. So we have template confirmation and fallbacks to output rather than LLM reformulation, programmatic response assembly — those tricks to help the agent know what the user sees. Last, node-change determinism.

**[17:03](https://www.youtube.com/watch?v=LUemJGG2k4c&t=1023s)** For example, what if after one node execution, I always want to make sure the next node is something certain rather than random? Rather than putting all of that within the prompt, we actually have a few parameters or tricks, like state flag chaining, one-shot tool guards — which make sure one tool can only be called once or a certain number of times — and signal-only tools, which can only be called from within another tool rather than by the agent itself. So this ensures what the agent does next. So based on all of the harness engineering, our agent's getting better and better, and closer and closer to our customer requirements. And that's something we're really glad to see. So overall, here's how we built our LinkedIn hiring agent.

**[17:54](https://www.youtube.com/watch?v=LUemJGG2k4c&t=1074s)** And thank you for listening. [APPLAUSE]
