---
id: QIUHetsI3LA
title: "Lightning Talk: Operationalizing AIBOMs in AI Supply Chains"
slug: lightning-talk-operationalizing-aiboms-in-ai-supply-chains
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "Security conferences"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 6
published_at: 2026-05-04T19:08:54Z
video_id: QIUHetsI3LA
url: https://www.youtube.com/watch?v=QIUHetsI3LA
youtube_url: https://www.youtube.com/watch?v=QIUHetsI3LA
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
topics: ["Science, healthcare & applied ML"]
transcript: true
---

# Lightning Talk: Operationalizing AIBOMs in AI Supply Chains

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `6 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=QIUHetsI3LA) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

Operationalizing AIBOMs: Policy-Gating Models & Datasets in AI Supply Chains

🎙️ Dr. Ugur Koc, SR. AI R&D Engineer, Manifest
📍 Presented at SANS AI Cybersecurity Summit 2026

AI supply chains ship unvetted models and datasets because VM tooling can’t see inside them. Risks aren’t just CVEs: dataset poisoning, integrity loss, misuse/misalignment, and license issues. With no NVD for AI artifacts, we operationalize AIBOMs as the missing substrate—structured metadata for provenance, lineage, licensing, and revisions—plus policy-as-code CI/CD gates, PSIRT integration, and offline caching of Hugging Face artifacts.

➡️ Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

➡️ Explore SANS AI resources, including research, expert insights, training, and more: https://go.sans.org/AI-Cybersecurity

## Transcript

*866 words · source: supa (en, exact timings)*

**[0:00](https://www.youtube.com/watch?v=QIUHetsI3LA&t=0s)** Well, I wish I was a light bender. Hello everyone. Let me move on to my slides. Today I will be presenting an AI governance framework with AI bombs at its center uh for extending vulnerability management to AI models and AI data sets. Well, I will define what an AI bomb is, but before that let's talk about the problem. Well, we have seen this many times yesterday and today. Uh the core gap is AI assets are still in black boxes. This is obviously not transparent. And when AI comes up with an output, it's usually not interpretable. And to be able to use AI in production,

**[0:49](https://www.youtube.com/watch?v=QIUHetsI3LA&t=49s)** not just complete a task, but have our customers improved experiences powered by AI, we need to introduce transparency. We need to open that box. Uh this is not just for production. This is also relevant for saving the future of humanity actually. So, um how do we achieve that? Uh well, I am an AI governance professional by trade. Uh and in my journey one concept that I learned and liked, or I should say I locked, uh I used to like, is the concept of model card. Uh model card is a transparent overview of a model specification. It

**[1:35](https://www.youtube.com/watch?v=QIUHetsI3LA&t=95s)** covers models' architecture, training data, performance results, um the task that it's supposed to work on, the intended users, so and so forth. And it's great for documentation. However, when it comes to security, it doesn't really cut it. Well, you may ask why? Because it's unstructured. It doesn't have a standard. Your popular AI vendors like Anthropic, OpenAI, they call the technical report that they publish along with the model that they release as the model card. While academics would call the research paper uh that introduces the model as the model card. If you go to Hugging Face, which is the largest open-source AI community, the readme of the model repository is

**[2:22](https://www.youtube.com/watch?v=QIUHetsI3LA&t=142s)** the model card. So, no standardization. Also, they are incomplete. They are usually like they don't cover everything that we care for AI governance and security. Uh how do we tackle this? Well, before answering that, I want to see a quick show of hands here who has heard of the concept of software bill of materials, aka SBOMs. Lights. All right. Well, that's all the hands. Great. Cool. Uh so uh software bill For those who didn't raise their hand, software bill of materials is the ingredient label for your software systems. It tells you what's under the hood in a software system. So, enter AI BOM.

**[3:09](https://www.youtube.com/watch?v=QIUHetsI3LA&t=189s)** Stands for AI bill of materials. And tells you what is in in an AI system. It's the ingredient label for the AI system. So, it is similar to the AI SBOM, right? Well, no. Actually, an AI BOM is an SBOM. An AI BOM is a glorified SBOM that includes AI artifacts in it. So, in addition to the software traditional software artifacts that you get in an SBOM, uh you will get the model types, the model uh weights, the data sets, uh performance results, uh all the governance relevant information will be in an AI bomb, which again follows the same standards. And

**[4:04](https://www.youtube.com/watch?v=QIUHetsI3LA&t=244s)** the because it's structured, it is machine readable and machine usable. AI bomb can be the substrate for an AI governance program in an automated way, which is the only scalable way. Okay, now we have learned about AI bombs, let's unbox an AI model with an AI bomb, shall we? So, now you see the model is a transparent and open box, which is very better for governance and security. Uh let's see what we get from an AI AI bomb. The first piece of information we get from an AI bomb is on model identity and lineage. The name of the model, the version of the model, supplier, the country of the supplier, uh the licenses and the ancestors of the model if it was fine-tuned from another model.

**[4:55](https://www.youtube.com/watch?v=QIUHetsI3LA&t=295s)** The second piece of information we get is the model card, not to be confused with the other model card that I was talking before. Uh this is a structured piece of information that includes the task the model is trained for, the architecture of the model, the performance results, intended users, intended use cases, technical limitations, and ethical considerations. Very relevant for governance. The third piece of information is the software dependencies. So, yes, AI also do ship with software. Uh these are the software dependencies that you need to be able to use the model in your system, along with the identifiers of those software dependencies. And also you get the files that are shipped with the model. And this is very important because if the model is being shipped with a uh executable file, then you are

**[5:45](https://www.youtube.com/watch?v=QIUHetsI3LA&t=345s)** you want to put put that policy in place to basically stop that happening? And last bit of information you get the data sets. So with this this one really everything here is policy executable which makes what AI bomb is a perfect substrate for AI governance program. My name is Yuriy Gorodnichenko. Thank you very much.
