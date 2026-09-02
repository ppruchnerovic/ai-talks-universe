---
id: aL5Ppz1hgHY
title: "Milind Naphade - Advancing the State of the Art: The Frontier of Enterprise Agentic AI"
slug: milind-naphade-advancing-the-state-of-the-art-the-frontier
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Milind Naphade"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-09T23:37:04Z
video_id: aL5Ppz1hgHY
url: https://www.youtube.com/watch?v=aL5Ppz1hgHY
youtube_url: https://www.youtube.com/watch?v=aL5Ppz1hgHY
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Milind Naphade - Advancing the State of the Art: The Frontier of Enterprise Agentic AI

**Milind Naphade**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=aL5Ppz1hgHY) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,211 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=1s)** MILIND NAPHADE: Good afternoon, folks. I know this is one of the last sessions between you and the end of the week, so I'll try to keep it brief. I'm Milind Naphade. I run all of the AI research and development at Capital One. So Capital One has always been-- it has always been a technology leader, technology first company. And the belief is that the winner of this in banking is going to be a technology company that has deep technology roots, as well as deep understanding of how to manage risk well. We have been on a journey of technology transformation for a while now-- the first large bank on the public cloud, a modern data ecosystem, and a deep rooted respect for data-driven analysis

**[0:54](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=54s)** from our very origins and a long journey in terms of applying machine learning and artificial intelligence to the problems to solve that our customers can benefit from. Recently, over the last 3 and 1/2 years, we have actually put significant investments in generative AI and agentic AI. And we are among the first to enterprise to actually launch agentic AI into production in a couple of years ago. I'll talk more about that in a minute. The way we think of ourselves is we want to use science and first principles to affect change across all the layers of the AI stack that end up helping Capital One's customers and help us

**[1:46](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=106s)** enrich all our experiences. To do that, we have built this organization called AI Foundations, which is predominantly AI researchers, applied AI engineers, data scientists, and so on and so forth. And we try to actually achieve business impact through scientific innovation and pushing the frontiers of AI and the state of the art AI. So to that effect, we have more than 65 publications in leading research conferences and journals this year. This number keeps growing. We are a very big part of some of the conferences that I'm sure you guys all attend, whether it's ICML, ICLR, NeurIPS, ACM, so on and so forth.

**[2:35](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=155s)** We are also very closely partnering with academia and industry. We have various partnerships with University of Southern California, University of Illinois at Urbana-Champaign, Columbia University, and a few others, where we work closely with the researchers in advancing safe AI. So that's one of the things that we do. In terms of our belief that true differentiation only comes from customizing the entire AI stack with our data. And Capital One's AI advantage is Capital One's data advantage, being converted into an advantage through our scientific work of customizing this stack. Here are just a few papers that we just published.

**[3:27](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=207s)** One of them is from NeurIPS, where we talk about how to generate data sets, curated data sets for multi-turn conversations in multi-agent environments, which is a very different problem than synthetic data generation for a singleton or single agent interactions. We have some work on how to route generated data through multiple models. You can think of this as a mixture of models instead of mixture of experts. That's some of the work that we presented at ACL. And then something recently at ICML on critic-guided distillation for robust reasoning. All these are just samples of our work. There's a lot more where this comes from. And given that I have very limited time,

**[4:16](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=256s)** I just want to say this Capital One was at the forefront of agentic AI. We started our agentic AI exploration more than 2 and 1/2 years ago, and we actually had our first production system using multi-agent AI very early, last January. And while there are a lot of innovations that we have worked on, the overall framework, what we call MACAW, comprises of four different agents or four different class of agents. One is an agent that either interacts with the environment or with the customers, and tries to figure out what is it that they need. One is a planner agent that actually has access to all of the APIs, and all the knowledge and all the policies of Capital One, so it can figure out how to satisfy that need.

**[5:07](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=307s)** And some of the secret sauce is in the evaluator agent, which is a completely independent agent that validates the plan, figures out using a world model, a very simple world model, whether executing that plan will fit Capital One policies and will be safe to do. And if not, it can kick it back to the planner agent, which can in turn kick back to the understanding agent for enhanced input needed from the customer. So this is a non-deterministic system at play naturally. And so this is not something that-- this is not robotic, just done differently with agents. This is an inherently non-deterministic system of agents that works together to achieve outcomes.

**[5:56](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=356s)** And finally, we have an agent that will talk in what humans can understand. The rest of the agents talk in their own language, of course. We have been working on this, as I said, for more than 2 and 1/2 years, and we have some of the examples of this working in production. So when any of you is trying to buy an automobile using a bunch of dealerships throughout the country that use Capital One on the back end, you are most likely interacting with our chatbot concierge that helps you figure out what you are looking for in the vehicle, availability, appointments, if you want to trade in a vehicle-- all those things 24/7, 365, fully autonomously. There's another use case that we debuted last year, which is helping our consumer bank on fraud-related conversations

**[6:49](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=409s)** with the customers. So part of this is understanding the customer's complaints. Part of this is recommending the right set of actions for our agents to take. And then, of course, the last part is summarizing the conversation so that we create a learning corpus for us for the next set of interactions. I would just like to say that we have been growing dramatically because we believe, as I said, in first principles research, we are advancing the state of the art wherever we need to. As I said, we are working at all layers of the stack. So we are working on customizing the foundational models themselves. We are customizing the services that go along with them, with our data.

**[7:38](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=458s)** We are customizing at the agentic layer of the AI stack. And, of course, we are working with all parts of Capital One in implementing solutions that leverage this. So even at the solution layer. And so to do that, these are the three job families that we hire. We are hiring for those of you who may know someone or may be interested in coming and changing banking for the good in working on AI, going from research into production in record time, that's typically unheard of in regulated enterprises. And for those of you who want to see 130 million customers, leverage your work, learn from it, and create that continuous learning loop, please contact us, and we would be happy to talk

**[8:28](https://www.youtube.com/watch?v=aL5Ppz1hgHY&t=508s)** to you about the various positions we have open to fill. Thank you. [APPLAUSE]
