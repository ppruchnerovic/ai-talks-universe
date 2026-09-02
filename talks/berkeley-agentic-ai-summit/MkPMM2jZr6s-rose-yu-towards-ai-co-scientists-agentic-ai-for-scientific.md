---
id: MkPMM2jZr6s
title: "Rose Yu - Towards AI Co Scientists: Agentic AI for Scientific Discovery"
slug: rose-yu-towards-ai-co-scientists-agentic-ai-for-scientific
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Rose Yu"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-12T08:08:01Z
video_id: MkPMM2jZr6s
url: https://www.youtube.com/watch?v=MkPMM2jZr6s
youtube_url: https://www.youtube.com/watch?v=MkPMM2jZr6s
tags: []
topics: ["Agents & orchestration", "Science, healthcare & applied ML"]
transcript: true
---

# Rose Yu - Towards AI Co Scientists: Agentic AI for Scientific Discovery

**Rose Yu**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=MkPMM2jZr6s) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,024 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=1s)** ROSE YU: Good morning, everyone. Thank you for the organizers. It's an amazing, amazing event. So I'm a professor at UC San Diego. I direct the Spatiotemporal Machine Learning Lab. So we built machine learning algorithms for the physical world. Today, I wanted to talk a little bit about a question that has been bugging us for the past few years. How can we build an AI code scientist that actually help you with research? Not as chatbot, but as partners that can reason in a physical universe and then lead to open-ended discoveries. [SIDE CONVERSATION] ROSE YU: So, to answer that question,

**[0:53](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=53s)** we have been thinking about, what are the unique challenges of AI for science when it comes to the physical universe? As we know, in the physical world, we have the laws of physics, the symmetries, the conservation laws. And how can we build these type of guardrails into the current agentic system? And a lot of times, physical sciences use very expensive simulations. Though these simulations, whether it's simulating how the climate is going to change in 50 years, or simulating how a disease is going to spread in the large community of billions of people, or simulating how atoms are interacting with each other in materials, in biological systems.

**[1:43](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=103s)** And these simulations are built from first principle mathematical models. But these simulations oftentimes takes long time, weeks, if not days, to run and get the feedback. When we want to build the genetic system, and we want to use this type of simulation as word models to verify our agents, how can we interact with this type of environment? And a lot of times, when we think about useful events, interesting events, these events are rare, and they carry a huge amount of uncertainty. So how can we calibrate this kind of uncertainty so that when the agent says, I'm 100% sure that tomorrow is going to rain, then we know it's actually 100% correct?

**[2:35](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=155s)** So all these challenges are breaking the common assumptions that we have for agentic system. How can we build agents that adaptively intervene between internal reasoning and these expensive simulations that could run for days? And how can we bake in the laws of physics in the reasoning engine of these agents? And how can we properly calibrate the uncertainty? Next slide. So to do that, we need agents that can trade-off between the adaptive tool use that can integrate formal reasoning tools into the verifiable environment. And this type of recipe that we built over the years

**[3:24](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=204s)** is called physics-guided AI. So I wrote a paper at PNAS, National Science Academy, to describe what we think is the right approach, the right recipe to build AI agents by grounding them with laws of physics. So we have differential equations that are the building blocks of simulations. We have symmetries that are governing principles of the physical universe. How can we ground our agents with these laws of physics and then loop them into the agentic open-ended reasoning loop? And this recipe works. I will say, we're very excited about the agentic future of physical science. And then we are applying it to many different areas. For example, when we build AI scientists for climate science

**[4:16](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=256s)** to understand the impact of climate change, we can run simulations really quickly using adaptive reasoning loop so that the agent can trade-off between very fast retrieval from memory and very expensive climate model projections. And that lead to two times more accurate question answer results for climate-related reasoning tasks. We built verifiers that can leverage formal methods in LINQ and Issabel to ground these reasoning engines to solve mathematical theorems. We were number one on PutnamBench, which is one of the hardest formal math theorem proving benchmarks. And we were able to beat the proprietary solutions by ByteDance from 50% to 70% problem solving. We were able to design drugs that

**[5:08](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=308s)** are evaluated by molecular dynamic simulators, have 18 to 35% more better favorable binding energies. Just as a concrete example, we have built this agent called Zephyrus. And this is the first agentic weather scientist that can read huge amounts of weather data, highly numerical, generate and run code in a parallel code execution environment, orchestrate a wide range of tools from climate simulator to weather forecaster, and then write a report to understand the impact of extreme events such as wildfires and earthquakes. And this type of analysis will typically take weather scientists a couple of weeks to do. Now, using agents who can do that in a couple of hours.

**[5:58](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=358s)** And recently, we've done a lot of research to generate physics grounded agents for the physical science. And we want to take that to the real world. So we launched this startup that I'm the CEO of, to take the same type of recipe from the lab to the physical world, where we wanted to deploy agents that can automatically detect research, calibrate forecasting, simulation what-if scenarios, and actionable insights to support supply chain and operation, which is the critical infrastructure for the physical economy. And in this agent, we can ask a natural-- oh, that doesn't work. Can you play this?

**[6:46](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=406s)** Thank you. Can you play this? SPEAKER: Maybe. Can we play the video? ROSE YU: In this agent, you can ask a natural language question. If there's a typhoon that hits us-- imagine you're a chip manufacturer, and you want to understand if there's a typhoon that hit Southeast Asia, how should we understand the impact on the shipping lanes and the lead time, and then optimize and mitigate the potential disruptions on your business? And then our agent can do adaptive research to find all the impacted lines and then estimate the disruptions on lead time arrival and come up with a mitigation plan in a couple hours. So with that, I want to thank all the funding agencies

**[7:37](https://www.youtube.com/watch?v=MkPMM2jZr6s&t=457s)** for supporting this work. We're just launching this company. So if you're interested, please come talk to us. And we're very excited to show the world what we can build. Thanks. [APPLAUSE]
