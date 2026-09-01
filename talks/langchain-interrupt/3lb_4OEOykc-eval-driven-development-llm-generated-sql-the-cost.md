---
id: 3lb_4OEOykc
title: "Eval-Driven Development, LLM-Generated SQL, & the Cost-Uncertainty-Lag Triangle: Rippling's Playbook"
slug: eval-driven-development-llm-generated-sql-the-cost
conference: langchain-interrupt
conference_name: "LangChain Interrupt"
category: "AI engineering & agents"
edition: "Interrupt 2026"
year: 2026
speakers: []
channel: "LangChain"
duration_min: 17
published_at: 2026-07-13T12:40:21Z
video_id: 3lb_4OEOykc
url: https://www.youtube.com/watch?v=3lb_4OEOykc
youtube_url: https://www.youtube.com/watch?v=3lb_4OEOykc
tags: ["Rippling", "Rippling AI", "Senthil Velu Sundaram", "Akash Ashok", "LangGraph", "LangChain", "AI agents", "eval-driven development", "EDD", "LLM evals", "Wilson confidence interval", "flat agent", "multi-agent", "sub-agent", "SQL generation", "LLM SQL", "employee graph", "HRIS", "HR AI", "payroll AI", "agent architecture", "production AI", "smoke evals", "health evals", "Interrupt conference"]
transcript: true
---

# Eval-Driven Development, LLM-Generated SQL, & the Cost-Uncertainty-Lag Triangle: Rippling's Playbook

**Speaker not identified**

`LangChain Interrupt` · `Interrupt 2026` · `2026` · `17 min`

`#Rippling` `#Rippling AI` `#Senthil Velu Sundaram` `#Akash Ashok` `#LangGraph` `#LangChain` `#AI agents` `#eval-driven development` `#EDD` `#LLM evals` `#Wilson confidence interval` `#flat agent` `#multi-agent` `#sub-agent` `#SQL generation` `#LLM SQL` `#employee graph` `#HRIS` `#HR AI` `#payroll AI` `#agent architecture` `#production AI` `#smoke evals` `#health evals` `#Interrupt conference`

[Watch the recording](https://www.youtube.com/watch?v=3lb_4OEOykc) · [Conference site](https://interrupt.langchain.com/)

## Description

Senthil Velu Sundaram and Akash Ashok from Rippling's AI team walk through the hard lessons from building and launching Rippling AI — a natural language assistant over the company's employee graph that can answer payroll, HR, and benefits questions across every system of record. They cover three major shifts: why they abandoned a multi-agent sub-agent architecture in favor of a single flat agent with declarative skills; how they replaced a large catalog of bespoke tools with LLM-generated SQL over a cached schema; and how they built an eval-driven development process modeled on statistical confidence intervals (Wilson's interval) to know exactly how many eval repetitions to run before shipping.

Chapters:
0:00 The problem: an HR leader's Monday morning inbox
1:36 Demo: Rippling AI and the employee graph
2:37 Architecture overview: LangGraph, entity resolution, and the flat agent
4:54 Why the multi-agent sub-agent model failed
5:33 The flat agent: declarative skills and SOPs instead of sub-agents
6:12 Generic composable tools: one SQL-powered get-data method
7:31 The hallucination problem and why LLM-generated SQL solves it
8:14 SQL is more powerful than bespoke tools: a real example
9:38 Caching data for iterative follow-up queries
10:17 Evals first: what eval-driven development actually means
11:50 EDD is like TDD but harder: the stochasticity problem
12:37 Wilson's confidence interval: how many reps do you actually need?
13:40 The cost-uncertainty-lag triangle: you can only pick two
14:17 Smoke evals on every commit vs. health evals pre-prod
15:00 Building custom tooling and synthetic test environments in production
16:00 Three takeaways: flat agents, composable tools, evals first

Resources:
→ LangGraph: https://www.langchain.com/langgraph
→ LangSmith: https://www.langchain.com/langsmith
→ LangChain Academy: https://academy.langchain.com

## Transcript

*2,536 words · source: supa (en, exact timings)*

**[0:06](https://www.youtube.com/watch?v=3lb_4OEOykc&t=6s)** We can start. I have good news and bad news. The good news is this is the last talk of the day. The bad news is you have to sit through and hear us. Shall we start? Thank you. Thank you. So my name is Senthil and he is Akash. We build AI products at Rippling. How many of you have heard of Rippling? OK, reasonably popular. Imagine you are running a company. You have a few thousand employees across multiple countries. You have full-time, part-time, and contract employees, multiple departments, different access controls. You run payroll and benefits, and you handle payroll taxes. You manage their devices and all this stuff. And you are the HR leader at the company. And on Monday morning, in your inbox,

**[0:54](https://www.youtube.com/watch?v=3lb_4OEOykc&t=54s)** your CEO is asking for a report around spend. An employee is asking about some discrepancy or a missing amount in payroll, and things like that. So you're filled with all these kinds of requests. You know the answers are out there somewhere, across all the systems you're managing and all the spreadsheets you're handling. But getting all of these things done quickly and accurately is just tedious work. It's work. What if you could just ask your system and it would give you the answer? [upbeat music] [upbeat music] [Music]

**[2:35](https://www.youtube.com/watch?v=3lb_4OEOykc&t=155s)** That's Rippling AI. So this is possible because of the way we've organized the system at Rippling from day one. Instead of multiple systems that you're dealing with, we put employee data at the center, and then we built a lot of products around it. We call it the employee graph. So you have all the systems connected. Whenever you change something about an employee, everything is reflected everywhere. The data is already organized for you to use it. And we put an AI layer on top of it. And suddenly it feels like magic. And that's what we did with Rippling AI. We launched a few weeks ago. I've been with the company for six and a half years now. And this is one of the most successful launches we've had. And that's possible because we have this data already

**[3:24](https://www.youtube.com/watch?v=3lb_4OEOykc&t=204s)** organized with the employee graph. So in this talk, we're going to talk about the Rippling AI journey, what we learned, and we thought we would share this with you. And that's it. So let's talk about the architecture first. Everything I spoke about — the employee graph, all the applications and the data — I'm representing as one big block at the bottom called the Rippling Backend API. And now I'm going to zoom into the agent itself. We use LangGraph, of course. And we have a top agent. And then we have a deep agent, which handles the overall orchestration. The top agent handles the orchestration. There are three main blocks I'm talking about.

**[4:11](https://www.youtube.com/watch?v=3lb_4OEOykc&t=251s)** First is entity resolution. If a user is asking about an employee by first name, that name has to be resolved to an employee record living in the system, pointing to an employee ID. And then we have tool selection, which — specific to the query — selects the right tools, and also brings in domain context, which is very vast in the case of Rippling, through skills and SOP. So that's a horizontal concern at the top. And then we have an agent which has some generic tools, and — now that it has the entity, the tools, and the domain context — it uses these, runs the agent, connects to the employee graph, brings the data, gives you the answers, and operates the workflows. But we didn't start with this. When we started this project, Rippling

**[4:59](https://www.youtube.com/watch?v=3lb_4OEOykc&t=299s)** is a several-hundred-member engineering company. And the products are vastly different. So we started with one top-level AI assistant agent. And then we had a lot of sub-agents. Each team could build their own sub-agent. That didn't work well. Primarily, the problem was around how to do context sharing. How do you handle handoffs across agents? Whether the top agent should fully know about the sub-agent's context or not. How do you handle interrupts? How do you handle queries that span multiple sub-agents? And then that became messy. So we eliminated the problem by keeping it flat. What we have is one flat agent today. And all the domain context of different products is injected into the agent only through declarative skills and SOPs.

**[5:48](https://www.youtube.com/watch?v=3lb_4OEOykc&t=348s)** Our product team engineers write them. And of course, they test them. And the agent itself is one flat agent. If you really think about it, we actually removed a lot of abstractions and code. We kind of flattened it in such a way that whatever the user sees as message history, the LLM sees the same thing. And the performance is much better with this approach. Moving on to the next topic. When we started, each team built a bunch of tools, and we ended up with a very large catalog of tools. The problem with that is tool selection became far more sensitive. If we selected the wrong tools or missed some tools, we were not getting the right answers. So we eliminated the problem

**[6:38](https://www.youtube.com/watch?v=3lb_4OEOykc&t=398s)** by moving towards more generic tools. Here's an example: instead of many get-data methods, you have one get-data method, and employee, device, or taxes becomes a parameter. If you think about it, it's the same Unix philosophy: do simple things and do them well, and let the agent compose all these things to get any complex outcome. Our AI Assistant can do a lot of things. It can run payroll, hire an employee, and a lot of other operations. But primarily, people are using it to ask questions and get data. It could be an individual asking about their payroll data, their benefits data, or any data that they're dealing with.

**[7:25](https://www.youtube.com/watch?v=3lb_4OEOykc&t=445s)** Or it could be the company admin or HR asking for aggregated data or report data. And this data cannot be wrong. And we all know that stuffing raw data into the LLM — "here is the data, here is the query, answer this" — kind of prompting can go wrong. It can lead to hallucinations, and we cannot afford to be wrong. So what we did is specify to the LLM the shape of the data. Here is the schema. Here is the data. And here is the query. And ask the LLM to solve that. The LLM comes up with SQL to solve it. And we execute the SQL. So the data itself is not part of the context window. It's basically the LLM solving the problem given the shape of the data. An interesting side effect we discovered is that SQL is so powerful that it's far more powerful than building a lot of bespoke tools

**[8:21](https://www.youtube.com/watch?v=3lb_4OEOykc&t=501s)** we might otherwise have to build. I'll give an example. Consider a query: "why weren't the benefits deductions withheld for a given employee?" Now, this looks like a very simple query. But underneath the system, we need to know about the employee — their location, entitlements, and everything in HRIS. We need to know about the benefits. Then, of course, payroll. So we need to orchestrate across all these things. With multiple tools, you can get this information and compose it. But we built one generic tool to pull all the data out, and it can execute SQL. LLMs are really good at writing SQL. And the moment we expose the schema in the context, the LLMs can write SQL in one go and get the information they want. And this was far more powerful.

**[9:14](https://www.youtube.com/watch?v=3lb_4OEOykc&t=554s)** It also reduced the number of tools needed, which removes the risk of wrong tool selection and things like that. But this still has one problem. The problem is that fetching this data — querying all the core data lake — is costly, both in terms of dollars and in terms of time. So what did we do? We take this data once, put it in a cache, and let the LLM say: here is the schema, here is the data, here is the query — explore and give me the answer. And you might have seen this if you're working with Claude Code or any of the agents, right? It iterates, writes the query, figures out the problem, and if there's an error, it iterates again and gets the final answer.

**[10:02](https://www.youtube.com/watch?v=3lb_4OEOykc&t=602s)** It's very helpful. We cache the data, especially when you want the same data and there are two hypotheses running, and the user is asking follow-up questions. It's very, very powerful. And this made the experience much, much better for users. So far, we've spoken about the "what" of the system. Now we're going to switch gears and talk about how we release the system, how we iterate and improve. And that means we are going to talk about evals. So what we do at Rippling is — we say evals first and build next. Does that mean you write your evals before you even have your agent running? No. That's not what I'm talking about. Let's say you have your agent running in production, or some version of your agent running. Now, to make any meaningful change —

**[10:50](https://www.youtube.com/watch?v=3lb_4OEOykc&t=650s)** a system prompt change, a tool change, a tool description change, a skill change, anything — you don't know how it's going to behave, even if you know every single line of code, because you don't know how the LLMs are going to behave. So it's very important to say: you can go by your intuitions, but at the end of the day, evals tell you the truth. So that's what we call eval-driven development, and we follow this extensively. EDD — eval-driven development — is like TDD, test-driven development, but harder. Given the stochasticity of the LLM in the first place, let's say you have an eval, you run it once, and it passes one time. Is the success rate 100%? Are you really sure? Let's say we run it a few more times just to be sure.

**[11:40](https://www.youtube.com/watch?v=3lb_4OEOykc&t=700s)** Let's say you run it three times, three out of three pass. Is it 100%? Are you really sure? There are scientific ways to figure out how confident you can be as you get more repetitions in your evals. You can't run it just once and declare victory, because if you run it a few more times it might fail. There are some scientific ways. For example, there's something called Wilson's confidence interval. If one out of one eval passes, at a 95% confidence interval, you could be as low as 20%. And at three out of three, your lower bound could still be 44%. As you increase the number of reps, it's going to converge to your true pass rate. So the more repetitions you have, the more confident you can be in your evals.

**[12:29](https://www.youtube.com/watch?v=3lb_4OEOykc&t=749s)** And there's a scientific way of asking: how many reps do you need for your evals? The more repetitions you have, the more certain you can be. The fewer repetitions you have, the less certain you are. Repetitions reduce the uncertainty you have in your evals. So how many repetitions do you really need? That depends on three things. One: where are you right now? What is your baseline? For example, if your eval is already at 95%, the number of repetitions you need would be very different from if your eval is performing at 85% or 75%. The second thing: how small a regression are you trying to detect? To detect something from 95% to 94%, you need a lot more repetitions than to detect

**[13:20](https://www.youtube.com/watch?v=3lb_4OEOykc&t=800s)** something from 95% to, say, 70%. Similarly, it's very different from detecting a drop from 85% to 60%. And the last thing is: what is your tolerance toward false positives? All of these things bring us to the tradeoff triangle: cost, uncertainty, and lag. Cost: the more repetitions you have, the more money you're going to spend on your LLMs. Uncertainty: the more repetitions you have, the less uncertain you are, the more confident you are. And lag: how soon can you detect a regression from the time you've made a change? Say you've committed your PR. How quickly can you detect: there's been a regression here?

**[14:08](https://www.youtube.com/watch?v=3lb_4OEOykc&t=848s)** And you can only get two out of these three, which means you can get low cost and low lag, but with higher uncertainty. At Rippling, what we do is have something called smoke evals, which are very few evals that we run for fewer repetitions, and we run them on every commit that goes in. This gives us some amount of confidence that nothing is majorly broken, though something could still be off. So that falls under the low cost and low lag category. And then before anything gets pushed into production, we have a pre-prod stage where we run something called health evals, where we run them twice a day with many more evals running for many more repetitions, but we wait for a batch of commits to come in — meaning we're accepting higher lag,

**[14:59](https://www.youtube.com/watch?v=3lb_4OEOykc&t=899s)** but reducing uncertainty and cost because we don't run on every commit. You can only get two out of the three, and once health evals pass, they go into production. Once you have it in production, there are a few things to keep in mind. Every domain, every agent is different. No matter how many generic tools you have, you have to have visibility into your data, for which you need to build custom tooling to explore your data and understand what's going wrong with your system. So we have to build custom tooling. The second thing is we have a vault workspace where all production data lives, and we handle PII. Those things we carefully synthesize into a test environment — a synthetic test —

**[15:48](https://www.youtube.com/watch?v=3lb_4OEOykc&t=948s)** representative of customer data, but we don't work with the customer data directly. So we have a vault workspace and we improve our eval suite over time based on learnings from production. So, finally wrapping up: first, keep your agents flat. And of course, this is going to change as models improve over time. What you would have done last year is very different from what you were doing last month. And what you're doing now is very different from what you're doing right now. And what you'll probably do six months from now will be very different. As models get more and more powerful, the most important thing is to get your glue code out of your agents and let the LLM do its job. Get out of its way. Next: build generic, composable tools, which means

**[16:36](https://www.youtube.com/watch?v=3lb_4OEOykc&t=996s)** if you have data that you can let your model query via SQL, let it do that. It's much more powerful at that. And when you get things down to the most fundamental atomic pieces, your LLMs can do far more. And last: evals first. Always ensure you have eval-driven development. Test each one of your changes. No matter how good your intuition is, evals tell you the truth. And you have to choose: cost, uncertainty, or lag. Two out of three. Thank you. [APPLAUSE]
