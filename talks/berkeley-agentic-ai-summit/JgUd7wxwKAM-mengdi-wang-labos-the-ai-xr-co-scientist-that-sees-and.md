---
id: JgUd7wxwKAM
title: "Mengdi Wang - LabOS: The AI XR Co Scientist That Sees and Works With Humans"
slug: mengdi-wang-labos-the-ai-xr-co-scientist-that-sees-and
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Mengdi Wang"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-11T19:57:25Z
video_id: JgUd7wxwKAM
url: https://www.youtube.com/watch?v=JgUd7wxwKAM
youtube_url: https://www.youtube.com/watch?v=JgUd7wxwKAM
tags: []
topics: []
transcript: true
---

# Mengdi Wang - LabOS: The AI XR Co Scientist That Sees and Works With Humans

**Mengdi Wang**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=JgUd7wxwKAM) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*987 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=2s)** MENGDI WANG: Hello, everyone. It's my pleasure to be here. So we just heard about so much advances in AI agents in the digital space. So if we really think about scientific research-- so I think the previous speakers already said that. So there are several important stages like hypothesize, which is how to make models to think, to reason, and to dig deeply. And then computation, which is to simulate, to use surrogate models to simulate and try to find the best candidates. But the last step is, validation is verification, OK? So it turns out that verification has become the major bottleneck for scaling any AI models. That is why there are so many AI companies and AI startups that

**[0:51](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=51s)** are actively building new trace data, who are actively building, I would say, new RL environment. So I think AI will scale much faster if there's a way to scale environments and verification. But however, this is damn hard in science. OK. So let me ask you a question. So let's pick a random paper on Nature. Say, it's a chemistry paper or a biology paper. So do you know what's the percentage of Nature papers that can be reproducible? Someone want to guess? AUDIENCE: 5%. MENGDI WANG: 5%. AUDIENCE: [INAUDIBLE] MENGDI WANG: 30, OK. So you must have seen this. OK.

**[1:40](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=100s)** Actually, so there was a survey run by researchers and Nature that it turns out that 70% of biomedical research papers are not reproducible by others, and 50% are not even reproducible by the same authors. And this is true across domains-- chemistry, biology, physics, Earth environments. OK. And the problem is simply because verification is hard. The problem is because when someone actually runs an experiment at a bench or in a clean room, so there is a way to backtrack as how we backtrack in an agent workflow.

**[2:27](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=147s)** There are not checkpoints-- I mean, in training models, we have checkpoints, but there's no checkpoints in physical experimentation. And there isn't any log. There's isn't any way to look at the log and debug and to improve the harnessing. So this is why science is so damn hard. So my colleague wrote a blog a few months ago. And the conclusion is, with AI, science is not faster. Science is actually getting slower. So the reason is-- I mean, I think in the most recent NeurIPS submission, there are 40,000 submissions. There are just too many papers. But validation and verification actually

**[3:16](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=196s)** provides new knowledge and new information, that verification is not sped up. So we have more papers, more agents, meaning that we have even worse signal-to-noise ratios. It's actually harder to get useful information with so many AI-generated content. OK. Going back to the verification problem, we can have all the fancy models telling us how to do, telling us millions of novel hypotheses, but the bottleneck is going to be in the lab. And our poor scientist colleagues, they devote their careers, years of work, in the physical laboratories. But it's very hard to really speed up that process. And even though scientists try their best, this entire workflow is still very error prone. That's what we need.

**[4:08](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=248s)** OK. So now, if we think about this, the big question is, how do we turn every scientific lab into a verifiable environment? So on one side, AI is vanishing so quickly. We have all the fancy models. We have multiple AI code scientists from every major frontier, AI labs, and every startup. However, on the other end, for verification. So scientists really work hard and devote their career to working at a bench in clean rooms. They have to spend months, or even months to years, to validate a scientific hypothesis. So we're missing something critical here, and this is where we want to build.

**[4:57](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=297s)** OK. So we came up with a simple gadget, which we call it LabOS. It's an AI XR agent. It's a multimodal reasoning AI that hides behind smart glasses. So Simran, she is an undergrad intern who is visiting from India. And with the help of LabOS, she can perform advanced genome engineering experiment pretty much on day one. So we provide a solution so that every single action, every single state changes, in a scientific lab becomes observable by AI. And in the same time, one can build multi-tier streaming systems so AI can assist human researchers in real time

**[5:50](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=350s)** to catch errors, to digitalize physical workflows, to troubleshoot, and to provide guidance and hints when something doesn't work. OK, this is another example that we're building. It's not an animation. So this is a view, together with my colleagues at Princeton Quantum Institute. So we have been building this end-to-end mini-robotic lab for automating the nanofabrication of one-atom thin-layer graphene devices. And again, it's a multi-modal agent that runs [? South ?] auto research inside the computer. But the actual work, the measurements, the fabrication, the tapeout, and all the microscopic imaging were done by the robot. And by building this system, we're

**[6:40](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=400s)** actually automating work that used to take Physics PhD students three months. And now we can get this done in one week. And my colleague is actually releasing this system into an API so anyone can submit a job to reproduce the experiment and to test new hypotheses in that lab. And we want to enable this at scale. So finally, we are piloting the LabOS system, which is a system that enables human researchers to work side by side with robots. Again, every single physical workflow will be digitalized, and every single trace will be collected and reasoned by the AI. And this is a system that can generalize

**[7:29](https://www.youtube.com/watch?v=JgUd7wxwKAM&t=449s)** across scientific domains-- from biology labs, chemistry labs, to clean rooms, and nano facilities. So that's the end of my talk. Oh, now it works. [APPLAUSE] Thank you so much.
