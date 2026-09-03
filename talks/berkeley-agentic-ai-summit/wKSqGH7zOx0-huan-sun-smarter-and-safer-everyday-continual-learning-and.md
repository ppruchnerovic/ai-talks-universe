---
id: wKSqGH7zOx0
title: "Huan Sun - Smarter and Safer Everyday? Continual Learning and Safety in Computer Use Agents"
slug: huan-sun-smarter-and-safer-everyday-continual-learning-and
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "Practitioner AI conferences"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Huan Sun"]
channel: "Berkeley RDI"
duration_min: 5
published_at: 2026-08-12T06:44:15Z
video_id: wKSqGH7zOx0
url: https://www.youtube.com/watch?v=wKSqGH7zOx0
youtube_url: https://www.youtube.com/watch?v=wKSqGH7zOx0
tags: []
topics: ["Agents & orchestration", "Security, safety & red teaming"]
transcript: true
---

# Huan Sun - Smarter and Safer Everyday? Continual Learning and Safety in Computer Use Agents

**Huan Sun**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `5 min`

[Watch the recording](https://www.youtube.com/watch?v=wKSqGH7zOx0) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*589 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=2s)** HUAN SUN: I'm Huan Sun from Ohio State University, a faculty there. It seems like I'm the only one from academia in this session. So hopefully, I will convince you that what we do in universities are still quite relevant to the industry frontier. So today, I want to discuss a critical challenge for agentic AI, which I call safe continual learning. You can understand, as the question, how can we continually improve the agents after deployment without continually accumulating new safety risks? Today, I'm going to discuss two relevant projects in our group to tackle this challenge. First, I want to argue that there

**[0:52](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=52s)** is an underexplored and dangerous tension between continual learning and safety. Here is the paradox. Distribution shifts from training to deployment is often where the agents need to learn continually after deployment. But it is also the situation where safety failures can emerge and are easy to miss. So imagine, during continual learning, when an agent completes a task, but misses some safety constraints in doing this. So the agent might still get some positive feedback for completing the task.

**[1:40](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=100s)** As the evaluator, no matter human or agentic system itself, can purely focus on task success, or is not robust enough to catch the safety failure. So then, the next update to the agent may reinforce that unsafe behavior. And eventually, that can cause repetitive safety failures or even more aggressive safety failures. So I want to discuss the two projects towards safe continual learning in our group. One project is about how do we surface those long-tail failures early, before deployment at Scale. The other is about building open source infrastructure

**[2:36](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=156s)** to rigorously study safe, continual learning using open weight models, smaller open weight models. There have been numerous studies in the literature that create adversarial attacks or malicious prompts to break an agent. However, our study, our work shows that even without adversarial attacks, just under benign inputs and ordinary environments, severe harms could emerge from that. So the key question is how to proactively surface those long-tail failure modes before they become deployment incidents? You can also relate this to OpenAI and Hugging Face incident recently.

**[3:27](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=207s)** So this is an example where there are many ways to ask the agent to do something. And in one way, it may behave normally. In another way, which is just a slight perturbation of the original task instruction, which is still benign. The agent can behave or activate some harmful behaviors. So here, the user wants to have SSH access for one account. But the agent actually makes the unsafe changes beyond that. So I would skip the details here. And this is another example. But overall, you can see with some ambiguous phrases. In the instruction, the agent could demonstrate

**[4:16](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=256s)** some unsafe inference, and then that leads to harmful actions. So I'd like to briefly mention our efforts on developing open source infrastructure that can allow us to make open weight models to continually learn in a new environment. And there is a huge gap right now in the community to support this. You can imagine the environment setup and task synthesis and the trajectory evaluation. We have released this framework to support the study of safe, continual learning, especially for computer use agents. So the takeaway here is very simple. Basically, we want to make agents to continually improve

**[5:06](https://www.youtube.com/watch?v=wKSqGH7zOx0&t=306s)** both capability and safety. Our group is driven by this mission. So please follow us for more follow up work. Thank you. [APPLAUSE]
