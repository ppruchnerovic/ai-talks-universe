---
id: eXXZEvBrWEk
title: "Lightning Talk: AI Security Reality Check: Do the Basics"
slug: lightning-talk-ai-security-reality-check-do-the-basics
conference: sans-ai-summit
conference_name: "SANS AI Cybersecurity Summit"
category: "Security conferences"
edition: "AI Cybersecurity Summit 2026"
year: 2026
speakers: []
channel: "SANS Institute"
duration_min: 6
published_at: 2026-05-04T19:31:05Z
video_id: eXXZEvBrWEk
url: https://www.youtube.com/watch?v=eXXZEvBrWEk
youtube_url: https://www.youtube.com/watch?v=eXXZEvBrWEk
tags: ["sans institute", "information security", "cyber security", "cybersecurity", "information security training", "cybersecurity training", "cyber security training"]
topics: ["Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: true
---

# Lightning Talk: AI Security Reality Check: Do the Basics

**Speaker not identified**

`SANS AI Cybersecurity Summit` · `AI Cybersecurity Summit 2026` · `2026` · `6 min`

`#sans institute` `#information security` `#cyber security` `#cybersecurity` `#information security training` `#cybersecurity training` `#cyber security training`

[Watch the recording](https://www.youtube.com/watch?v=eXXZEvBrWEk) · [Conference site](https://www.sans.org/cyber-security-summit/)

## Description

AI Security Reality Check: Stop Chasing Shiny Threats, Do the Basics

🎙️ Daniel Bardenstein, CEO & Co-Founder, Manifest
📍 Presented at SANS AI Cybersecurity Summit 2026

Security teams are racing to prevent prompt and agent exploits while the biggest exposure is unmanaged AI: unknown tools, no owners, unverified provenance and data rights, over-privileged agents, and no audit trail. Our research shows CISOs are already facing AI-driven legal issues (privacy, IP, contracts, liability). This talk delivers an operational baseline: inventory, risk tiering, minimum controls, and metrics, plus what broke in real governance workflows.

Explore upcoming SANS Summits to continue learning from leading voices in cybersecurity: https://go.sans.org/summits

## Transcript

*1,166 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=2s)** Good afternoon, everyone. My name is Daniel Bardenstein. I'm the CEO and co-founder of Manifest Cyber, a startup that does all things software and AI supply chain security, but let's get into it. Today, I'm going to get offer a simple but perhaps cheeky take, especially at a AI cyber conference, about the fact that we're all getting distracted when it comes to AI security, and we all are should be going back to basics, not trying to get distracted by all of the shiny, sexy threats that are out there. So, too long, didn't read on the presentation is this, hopefully a meme that many are familiar with. Many security leaders, CISOs out there, all know that feeling of trying to rush to understand and get ahead of the impending AI security tide that's going to crash on many security programs

**[0:48](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=48s)** forced on them by their CEOs, by boards, etc. And when you look at the market or your conferences like RSA or what's on LinkedIn, there is no shortage of really exciting, interesting research, new threats, new vectors, and all the sorts of solutions that we can and should be buying in order to get ahead of those things, but the reality is, if you believe that AI is a subset of software, which many of us do, then if you just treat AI like software and you apply most of your basic risk management program and practices to AI, you're 90% of the way there. So, let's talk about perceived threats. If you spend any time on LinkedIn or wherever, you know, infosec people live these days, like myself, this is what we see, and Chris just hit

**[1:35](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=95s)** on a couple of these things that we hear a lot, right? We hear about data poisoning, we hear about rogue agents taking down your SaaS, we hear about inference vulnerabilities, template vulnerabilities, all these sorts of things. These are very possible, these are academic, this is interesting research, and the goal here is not to poo-poo the research, so to speak, but we have to keep in mind when we think about our threat models in security, what are the adversaries actually doing? And when we have finite budgets, how do we deploy that those funds to increase our security? So, what's the reality of what we see? Things as simple as AI agents deleting all of our emails, right? That's probably a bigger business continuity risk to most organizations out here than any sort of rogue agent or vulnerable or exploitable model or poisoned data set. Rather than seeing nation-state actors

**[2:25](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=145s)** trying to exploit models or data sets, we see them leveraging AI to wreak havoc at a new scale and speed that we're not used to. Q team PCP attacks in the last couple weeks, right? This is like log4shell and NPM attacks and polyfill all over again. How long did it take your organization to understand if you used Axios or Trivy's action or Checkmarx's action or Light LLM? Or even there's an a number of cases where publicly available data sets that were used to train very popular models have child pornography in them. And is your security team checking that these 5 billion images in these data sets have child porn? Probably not, but that becomes a risk that you take on. So, this is where we see actual risk, actual activity that most organizations, again, they're not the sexy ones,

**[3:14](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=194s)** but this is again, we look at the threat model where we actually see AI-enabled threats to organizations. So, my point and my encouragement here to everybody is to go back to basics, and apologies for the AI pun in the name, I sort of had to, it's right there. What should we be doing at a high level? The first is you just need to gate the AI models and data sets that are coming into your organization, right? The stuff that your developers, your AI engineers want to use, that they want to download from Hugging Face, that they want to install locally on their endpoints, but also in the third-party tech that you buy, and I think this is something a lot of people forget about. Whether you like it or not, there's going to be AI in pretty much every tech you buy going forward, cuz it's great for marketing and allegedly has some good efficiencies. How much do you trust that third-party AI, cuz that's going to be running in your networks, in your data

**[4:02](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=242s)** centers, with your sensitive data? And that scanning, that gating, needs to be automated. It needs to be fast. We've seen too many instances where it takes organizations months, literally months, 6 to 8 weeks, to answer the question, do we trust this new model enough to use it internally? And that time, your competition is going ahead. They're using the latest and greatest models, the adversaries are using the latest and greatest models. They don't have time for a manual review and a governance process for this. The second unsexy, boring pillar of security, inventory. If I were to ask a CISO or any security practitioner here, how fast can you tell me whether you're using a specific model in your organization? Or we just found out that there's something wrong with a data set, how fast can you tell me if you've trained any models using this data set in your

**[4:49](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=289s)** organization? Or even just as important, but even a a little bit less obvious, what about fine-tuned models, quantized models, adapted models, those custom customizations that your AI engineers are going to do? Do you know where those are from a security perspective? Do you know where they came from? Do you know how they were built? It's still a massive gap for pretty much every security organization out there, even though we know the basics, you can't defend what you don't know about. And lastly, continuous monitoring. I'm not here to say that models can't be exploited or can't have risks or data sets can't have risks or be exploited, but right now the industry is still a very point in time. Oh, this looks good, let's bring it in. What happens when something goes wrong 6 months from now? How do you get alerted about that automatically? How do you figure out how to call incident response processes on that and get ahead of, as Chris noted,

**[5:37](https://www.youtube.com/watch?v=eXXZEvBrWEk&t=337s)** the speed with which adversaries can exploit new vulnerabilities? So, the takeaway message I have for everybody treat AI like software, because it is. AI is software, it has to be deployed into software. If you just use your basic threat model and just use and deploy your existing cybersecurity programs, principles onto AI, you're 90% of the way there. The last 10%, the prompt injections, the hallucina- hallucinations will come. I got 4 seconds. All right, thank you all very much. That's all. >> [applause]
