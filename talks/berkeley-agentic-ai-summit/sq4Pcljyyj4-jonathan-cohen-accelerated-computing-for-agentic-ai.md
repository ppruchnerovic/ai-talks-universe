---
id: sq4Pcljyyj4
title: "Jonathan Cohen - Accelerated Computing for Agentic AI"
slug: jonathan-cohen-accelerated-computing-for-agentic-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Jonathan Cohen"]
channel: "Berkeley RDI"
duration_min: 9
published_at: 2026-08-09T18:45:15Z
video_id: sq4Pcljyyj4
url: https://www.youtube.com/watch?v=sq4Pcljyyj4
youtube_url: https://www.youtube.com/watch?v=sq4Pcljyyj4
tags: []
topics: ["Agents & orchestration"]
transcript: true
---

# Jonathan Cohen - Accelerated Computing for Agentic AI

**Jonathan Cohen**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `9 min`

[Watch the recording](https://www.youtube.com/watch?v=sq4Pcljyyj4) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,560 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=2s)** Good morning. So, I want to talk a little bit about um what is an agent and and where did this all come from? So, when the modern AI era was kicked off with ChatGPT largely a few years ago, we thought of these AI systems as things that a human would talk to a an a large language model. Maybe that large language model had access to some database. But fundamentally, this was about chat, people talking to AIs. But this has evolved considerably. Today, we really think of um a complete autonomous system. This is made up of many models, some open-weight models, some proprietary models, access to um tools, infrastructure, uh memory systems,

**[0:50](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=50s)** context management, ability to spawn sub-agents, uh security infrastructure. And there might be a human or or or in some cases even not a human starting this whole interaction with the a request. But But now we have a very complicated set of interlocking um AI systems and large language models performing some autonomous task. And so, what is this agentic AI? Oh. No, these are not my latest slides. Oh, well. Okay. Uh >> [laughter] >> I guess not. Uh well, I'll just talk over the slide for a second. Um So, what is an agent? Uh An agent isn't just a large language model. It's a large language model that's surrounded by what I'm going to

**[1:39](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=99s)** call infrastructure. Um and by infrastructure, I mean the software that um that allows the large language model to actually do things. So, this includes things like marshaling data between an API, um potentially type checking, rule-based enforcement of policies. Um another word for all of this stuff that we surround our large language model with that makes it into an agent is computer science. Now, there's a lot of reasons why this is a really good idea. Um, LLMs are incredibly powerful. They're the only method we know of to solve all sorts of problems that were previously unsolved. Right? For many uh many decades, we've been trying to crack all kinds of challenging problems and large language models come along and they can do these things. But, at the same time, um they're probabilistic and they're

**[2:27](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=147s)** non-deterministic. It's precisely the opposite of software, for the most part. Software tends to be deterministic, for the most part, not probabilistic. We can understand it. We can inspect its state. We can make um assertions about it. And and so, an agent is really the combination of these two things, where you take the intelligence from this probabilistic AI or sorry, probabilistic um machine learned large language model, but you surround it with the the um determinism and the power of computer science. Data structures and algorithms and the you know, many decades that we've spent learning how to be good at building software and and make things reliable. Um Now, an agentic system then is this complicated interaction of all these

**[3:13](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=193s)** things. Uh a typical agent, right? You have some some way of managing the prompts that go into the large language model that you feed the large language model with. You typically have um some infrastructure that allows the large language model to access tools, potentially check permissions. Um all of these things are running on a uh an increasingly complicated hardware substrate now. So, some of the the software that this agent is going to invoke runs on accelerated computing infrastructure, uh like GPUs. Some of it runs on CPUs. You have very complicated uh storage hierarchies now. You have agents and sub-agents. You you scoped uh data that needs to be passed between these different systems. Um you have communication patterns that are becoming increasingly complicated. Sandboxes,

**[4:02](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=242s)** uh secure enclaves, all sorts of complicated things. Now, the the the platform is heterogeneous both at the hardware and software level. Um and not to mention the collection of models. So, you have large models, uh you may have small models, you have you may have models that you have fine-tuned, um and specialized in some area. You may have a general-purpose proprietary model that's hosted externally on an API. Um and all of this works together to solve some complicated uh autonomous task. Uh we call this platform, uh Nvidia's version of this platform we call the Nvidia Nvidia Agent Toolkit. And it's a collection of things like deployment. Um so, for deployment, uh everything from Kubernetes to again um hosted infrastructure, uh computer use agents.

**[4:50](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=290s)** It also has accelerated tools. So, we what we call CUDA X, which is a collection of tools for example for um computational fluid dynamics or solving differential equations or computing um um secondary analysis of a uh DNA sequences um from DNA sequencing instruments. All of these um again, more computer science kind of tasks that we have accelerated uh solutions for, APIs and tools for, which are now made agentic. So, your agent has access to this wide variety of accelerated tools. And then a collection of open weight models. So, the NeMo Tron models, which is our family of general-purpose models. We have more domain-specific models in robotics, uh physical AI, uh BioNeMo, which are predictive models for biology. And again, all of this is running on

**[5:39](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=339s)** this very complicated infrastructure, which includes um the ability to deploy and run all these different models, the ability to um have sandbox environments that surround the system to ensure that your AI isn't doing something you didn't want it to do and ideally running all this in an efficient way. We also have built into this infrastructure typically you also want to be able to capture the knowledge that's flowing in and out of the system and then you can use that to post train a model to be specialized in a task that you care about. So I would include in the infrastructure itself also this ability to in an offline way improve the AI for example with post training using reinforcement learning. This is

**[6:27](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=387s)** often performed to take a small model and specialize it to make it very good at some task just as good as a much larger model would be at a more general purpose. I also want to talk a little bit about the actual interface between the say agentic system and the large language model and this is what people refer to as the agent harness. So the harness really matters the large language model encapsulates a lot of intelligence but this is for example recent work from my group to develop a harness we call the Nemo object oriented agents and the idea here is very simple and if you check out the link on this QR code you can find this project on GitHub. The idea here is that an agent is is simply a python object and what do I mean by that? Well you you write your agent in python and there's a special syntax with

**[7:17](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=437s)** this ellipsis notation which basically says to the LLM hey fill this block in with code and so the LLM is able to or sorry the agent is able to actually modify itself. So you can execute it can call methods that it has written and it can modify its own methods. It can decide this is some information I need to store and actually include include it as state in the python object. It can it can take some um plan or some way that it solved the problem and encode it in Python as a method and call it in the future. Um another important idea is rather than passing around all this information uh as strings compacted into some very large context, you can just pass things by reference because they're all Python objects. In this case uh and if you check out the tech report, you can see uh more

**[8:04](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=484s)** results. You can get significant lift over just a large language model or even over other agent harnesses um just from a lot of these ideas integrated into your agent harness. And so um we have results where we can get, for example, the same score but using half the tokens. Um or the Cyber Gym score uh which is um among the the strongest Cyber Gym scores. Uh and the lift from the harness in this case is significant. So this NVIDIA Agent Toolkit encompasses, as I said, all of these things. We have models, we have deployment technology like NIMs and Dynamo. Um we have uh tools built into the infrastructure for capturing traces like Nemo Relay, uh routing uh algorithms like Switchyard. Um we have what we call blueprints, which are open source imple- reference

**[8:53](https://www.youtube.com/watch?v=sq4Pcljyyj4&t=533s)** implementations that show how to pull all these pieces together to solve specific tasks. Um whether it's building an open claw or um AI Q, which is a uh um like [clears throat] a research assistant agent. Um and then we have runtime technology like Open Shell, which is essentially a firewall that allows you to control access between your agent and the outside world. Um and a lot of this is being deployed and adopted um by many of our partners. And with that, I'll wrap up and I look forward to the panel. Thank you very much.
