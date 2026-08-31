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
youtube_url: https://www.youtube.com/watch?v=3lb_4OEOykc
tags: ["Rippling", "Rippling AI", "Senthil Velu Sundaram", "Akash Ashok", "LangGraph", "LangChain", "AI agents", "eval-driven development", "EDD", "LLM evals", "Wilson confidence interval", "flat agent", "multi-agent", "sub-agent", "SQL generation", "LLM SQL", "employee graph", "HRIS", "HR AI", "payroll AI", "agent architecture", "production AI", "smoke evals", "health evals", "Interrupt conference"]
transcript: false
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
