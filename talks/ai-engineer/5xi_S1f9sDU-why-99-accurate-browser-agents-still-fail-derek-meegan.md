---
id: 5xi_S1f9sDU
title: "Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase"
slug: why-99-accurate-browser-agents-still-fail-derek-meegan
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Derek Meegan"]
channel: "AI Engineer"
duration_min: 17
published_at: 2026-10-02T21:30:15Z
video_id: 5xi_S1f9sDU
url: https://www.youtube.com/watch?v=5xi_S1f9sDU
youtube_url: https://www.youtube.com/watch?v=5xi_S1f9sDU
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "browser agents", "browser automation", "web agents", "Browserbase", "Stagehand", "computer use", "AI agents in production", "agent reliability", "agent architecture", "agent skills", "web scraping", "headless browser", "Derek Meegan", "AI Engineer", "AI Engineer World's Fair"]
topics: ["Agents & orchestration", "Science, healthcare & applied ML"]
transcript: true
---

# Why 99% Accurate Browser Agents Still Fail — Derek Meegan, Browserbase

**Derek Meegan**

`AI Engineer` · `AI Engineer` · `2026` · `17 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#browser agents` `#browser automation` `#web agents` `#Browserbase` `#Stagehand` `#computer use` `#AI agents in production` `#agent reliability` `#agent architecture` `#agent skills` `#web scraping` `#headless browser` `#Derek Meegan` `#AI Engineer` `#AI Engineer World's Fair`

[Watch the recording](https://www.youtube.com/watch?v=5xi_S1f9sDU) · [Conference site](https://www.ai.engineer/)

## Description

A browser agent that's 99% accurate per step succeeds only about 36% of the time over 100 steps. Here's how to beat that math.

Derek Meegan, software engineer at Browserbase, explains what separates a browser-agent demo from thousands of unattended production runs. He covers how agents see the web (text, screenshots and code), why cost builds up with every step while value only comes at the end, and why you should measure success per transaction, not per run. Then he walks through a real architecture for automating a health insurance portal: deterministic tools, OCR verification, pulled-out authentication and skills that keep the agent on the critical path.

In this talk:
• The three ways agents interact with the browser
• Why compounding step risk kills long trajectories, and how retries change the picture
• Performance first, then cost and maintainability as engineering problems
• A production architecture that takes everything deterministic out of the model's hands

SPEAKER
Derek Meegan, Software Engineer, Browserbase
X: https://x.com/derekmeegan

LINKS
Browserbase: https://www.browserbase.com
Stagehand: https://www.browserbase.com/stagehand
Stagehand (GitHub): https://github.com/browserbase/stagehand

CHAPTERS
0:00 Intro
0:12 Demo vs production
0:47 Agenda
1:27 How agents interact with the web
2:32 Text, screenshots or code
3:17 Types of browser trajectories
4:32 No partial credit
5:22 The 99% → 36% problem
6:12 Profit = revenue − cost
7:37 Performance, cost, maintainability
8:12 What success looks like
8:42 Per-run vs per-transaction success
9:32 Breaking down cost
10:11 Maintenance over time
10:46 Risks: the web fights back
12:06 Architecture: automating an insurance portal
13:01 A deterministic download tool
13:31 Verifying with OCR
13:56 Pulling out authentication
14:36 Skills as standard operating procedures
15:26 The final system
16:21 Welcome to production

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*2,400 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=0s)** All >> [music] >> right. Deploying browser agents. Uh running a browser agent demo once is easy. Uh it's on one site. It's one run on a good day with you watching and your fingers crossed. Uh, but we know production is vastly different. Thousands of runs unattended while the site can change or your model can just have an off day. So that's why we're here. What separates a demo from production? My name is Derek Megan. I'm a software

**[0:50](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=50s)** engineer at Browserbase. And today we'll break up this talk into four parts. First, we'll bring order to chaos, and we'll understand concretely how agents interact with the web. Second, we'll define the impossible and explore why running them at scale is so hard. Third, we'll take a step back. We'll think about what's important and the value proposition that agents propose. And then last, which is hopefully the reason why we're all here, we'll generate some shareholder value. So first how agents interact with the web. I like to think about the output of a model as a probability distribution. You receive input tokens. They represent the page state, the overarching goal or the steps that have already been taken. Then

**[1:40](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=100s)** the model explores a distribution of possible actions proposing the most likely one. Then that action is transposed into a structured tool call and deterministically executed to interact with the browser. But the interface of the browser is complicated. You have several distinct layers. You have requests flowing in and out of the browser. You have the document object model or the HTML representation of the page. You can screenshot the browser. the accessibility tree which is a semantic textual representation of the page and the browser state storage cookies console URL tabs etc. Underneath all of this, you have a dynamic code execution runtime where you can interact with the browser by writing arbitrary do

**[2:28](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=148s)** JavaScript or CDP. How do you wire these together? Typically in industry, there's three main strategies. Number one is creating a textual representation of the browser. This typically involves taking the HTML state of the page in the accessibility tree and creating a hybrid representation. Number two is computer use where you represent the browser in a series of screenshots of the page. And finally, and becoming increasingly popular, is deharing your agent, removing tailor made tools in favor of dynamic execution environments where the agent can write arbitrary code against the browser. In practice, most production systems lean on the first, the second, or a combination of the first and the second two strategies.

**[3:18](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=198s)** Now let's think about the type of agentic trajectories on the browser. And here I define three spanning across a spectrum of agenticness. From least agentic, we have purposebuilt browser trajectories that are specially made to complete a single task. To the most agentic, we have just in time browser automations where we don't know what the task is beforehand and the user provides us an arbitrary task to complete. In the middle, we have something sort of between both. We're using the browser as an implementation detail to serve a larger goal, such as performing deep research or competitor analysis. At scale, I really want to hone in on these transactional workflows. Not because it makes things easy, but that's

**[4:06](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=246s)** because we typically see at scale. These workflows are transactional by nature where we want to complete a unit of work end to end. On the other side, browser agents provide us a flexible execution environment to handle ambiguity in production. So, we know how agents interact with the web and the different types of trajectories we may see and we're honing in specifically on transactional workflows. Why is it so hard in production? And I think it comes down to a key interaction. Cost accumulation is continuous while value realization is terminal. Each step in your trajectory, you're incurring some incremental cost. Additionally, you're incurring some incremental risk

**[4:53](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=293s)** of failure. Yet, I only receive value from this browser trajectory when all steps of the task have been completed. That's all to say that with browser agents, there is no partial credit. And the vast majority of web automations fall into this category. So you say, "Okay, well each step there's more risk and there's more cost. If I use a highly capable model, I can sidestep this conundrum." Take this thought experiment for an example. You have a browser agent where each step has an independent success rate of 99%. If your browser trajectory spans 100 steps, the overall success rate at scale starts to look like 36%. only about a third of the time. That's not super great and it's certainly not

**[5:42](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=342s)** how we deliver reliable outcomes for customers in production. And so you say, okay, well, we're continuously accumulating costs, we're continuously accumulating risk, and the percentage chance of value realization is very low. That would suggest to never use a browser agent. Uh, thankfully, that's not the subject of my talk today. I think this dynamic is real, but the math isn't the whole story. And so, it's time to take a step back. Let's think about what's important and how agents actually deliver value. And to illustrate the value that I wish agents to deliver, uh, I will propose a simple equation. Um, perhaps not used enough by many of us. And this equation is profit equals

**[6:32](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=392s)** revenue minus costs. Yes, very simple. Um, but perhaps overlooked when thinking about browser agents. And this is all to say that your agent is just another line item and that your agent should give you more than it takes. But when we think about what your agent should give you, that begs the question of what does a browser agent actually give you? And so to answer this question, I like to think about the context of the customer. At browserbase, we help our customers deploy browser automations for their users. Oftent times, they're not automating the web for their own needs, but instead performing actions on the web on their customer's behalf. And so, a browser agent actually gives you a task completed for your customer repeatedly. Well, it gives you that ideally. And the

**[7:22](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=442s)** question is how you can create a dynamic system that affords the benefit of being able to wade through ambiguous problems while also completing the task repeatedly every time when the environment stays the same. And so we'll look across three dimensions and in order of importance. First is performance. Second is cost and third is maintainability. And when we think about performance, this is the primary measure of success that we want to focus on. Because once we know a browser agent is performant, it can complete the task we ask it to do. Then cost and maintainability simply become optimization problems. And I like optimization problems because those can be addressed with engineering. So the first thing we need to ask is

**[8:10](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=490s)** what success actually looks like. And success in these transactional browser trajectories look like some kind of concrete artifact that the run leaves behind. If you're paying a bill, that might look like a confirmation email. If you're placing an order, that may look like an order ID or a receipt. Or if you're submitting a form, that may look like a new record in a system that you can deterministically query. Second, >> how often is an agent correct? And there's two ways to measure that. Naively, you may measure the success of an agent on a perr run basis. Assume you have a browser agent. It's probability of success on any run is 50%. Yet, if you permit that agent to retry

**[9:01](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=541s)** for a particular transaction, maybe up to four retries, your per transaction success rate quickly climbs to 94%. And so when you think about what metric matters, again, I'd implore that we ground ourselves in the customer. The customer does not care necessarily how many retries you perform, but rather that the workflow was completed successfully and reliably. In short, permit retries and measure success against a per transaction basis. >> Next, we'll explore cost and we'll break cost down into two dimensions. The first is per run, which today is predominantly model costs. But as engineering evolves in the open source landscape for models, there's an incredible downward price

**[9:51](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=591s)** pressure on the cost of intelligence. And I believe over time, model cost will become a smaller and smaller component of deploying browser agent trajectories. Next is infrastructure and compute. What are the real resources you need to run your browser agent trajectories? And last is additional integration and tooling. Then we think about maintenance over time. We need to invest in observability not only in how the agent made decisions but what actually transpired in the browser. Second is developer time. When things break or things are not working optimally, people need to come in and reconfigure the harness or augment its capabilities. And last is re-evaluation. As the problem changes, sites change, models progress, and we need to re-evaluate our

**[10:39](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=639s)** point in time solution to last the test of time. So, we talked about performance, we talked about unit costs, we also talked about maintainability. What are the risk factors to the durability of these over time? Well, first and foremost, the environment can fight back. Antibbots and just generally we understand the web as not the friendliest place for your agent. Second, the task changes. The underlying job shifts beneath the a shifts beneath the agent and we ask the agent to wade through ambiguity. Luckily, this also benefits from increased model capability as models are more able to intuitively understand the intention of the user. and therefore in the face of something go wrong course

**[11:29](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=689s)** correct and ultimately complete the goal. Third is a better methods better methods appear and this is sort of a canonical conundrum with automating the web. What happens if I'm automating the web today and that same website creates an API tomorrow but for the vast majority of browser agent use cases uh an API isn't coming anytime soon. And finally the model strays off tasks. models are inherently indeterministic. So from run to run it may not ide follow the ideal path or the critical path to perform the action. So finally we've come to the meat of the talk. How do we concretely generate shareholder value? This is the question. Uh we understand that if a model performs well then cost and

**[12:16](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=736s)** maintainability are an optimization problem. So let's explore that in practice together. We're going to go through a highle architecture of a browser agent for real world tasks. This task is automating an health insurance portal. Every step we take in creating this dynamic system should influence one of these key levers. Cost, performance or maintainability. So first we'll start with a lowly agent. The goal of this agent is to log in and download an explanation of benefits. A request comes in, the agent performs the action on the browser, and this is the minimum necessary system you need to just do something. Next, you realize that when you go to download that explanation of benefits,

**[13:04](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=784s)** that downloading involves programmatically interacting with the page. And then once you perform that download, you need to retrieve that file from storage and bring it into the agent's runtime. So you create a tool that does this all in one transaction. Instead of the model needing to make decisions on the fly, you encapsulate a complex operation into a single tool call. Next, you want to give the agent an opportunity to verify its work real time. This can be done by giving it another tool. This tool is an OCR tool that deterministically extracts entities from the document and compares that against the system of record. Great. Now the agent knows if it's did it if it really did its job right or not because it has a deterministic mechanism to

**[13:51](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=831s)** verify that. Next, you realize that while this portal may have ambiguity in your business logic that the authentication workflow is never changing and you want to reuse the same authentication mechanism for many business operations on the same portal. So you pull that authentication logic out from the responsibility of the model. Again, we're reducing the number of steps that the agent has to take to complete the task successfully. This means lower unit cogs, higher performance, and easier maintainability as well as we can reuse this authentication function across multiple business logic workflows on the same portal. Last, we've contained the responsibility of

**[14:39](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=879s)** the agent to only the area of ambiguity necessary. So, we draft a skill. These skills look very similar to a standard operating procedure that we would have humans use in the past, except this standard operating procedure is for an agent, and it allows the agent to follow the critical path more closely. At the beginning of the talk, we discussed how the output of an agent can be thought of like a probability distribution. So if we introduce the critical path to the agent, it knows it's at step two and knows that it needs to take step three because we have outlined it in this skill, then it's more likely to take that step three. It knows exactly where it needs to go and we remove ambiguity from the agents decision process. In the end, this is the final result. We

**[15:30](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=930s)** have actually a pretty complex system. A request comes in, a serverless authentication function authenticates the browser. That browser is provided to the agent runtime. The agent navigates the portal using the skill provided, calls a deterministic download function, provides that downloaded file to a verify tool, and can know authoritatively whether its trajectory succeeded or failed. In the end, this system takes steps out of the model's responsibility that simply do not need to be in the responsibility of the agent. We reduce the number of steps it needs to take while still being able to achieve the desired outcome. Thus, the system's more maintainable and it's more performant and we can overcome the browser agent

**[16:20](https://www.youtube.com/watch?v=5xi_S1f9sDU&t=980s)** conundrum. So, >> here we are. Welcome to production and congrats. Now you're on call. Thank you. >> [music]
