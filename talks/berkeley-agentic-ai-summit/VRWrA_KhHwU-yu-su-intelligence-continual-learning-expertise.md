---
id: VRWrA_KhHwU
title: "Yu Su - Intelligence + Continual Learning = Expertise"
slug: yu-su-intelligence-continual-learning-expertise
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Yu Su"]
channel: "Berkeley RDI"
duration_min: 12
published_at: 2026-08-12T01:56:37Z
video_id: VRWrA_KhHwU
url: https://www.youtube.com/watch?v=VRWrA_KhHwU
youtube_url: https://www.youtube.com/watch?v=VRWrA_KhHwU
tags: []
topics: []
transcript: true
---

# Yu Su - Intelligence + Continual Learning = Expertise

**Yu Su**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `12 min`

[Watch the recording](https://www.youtube.com/watch?v=VRWrA_KhHwU) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,663 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=2s)** YU SU: So, today's talk will be quite conceptual. I will talk about three concepts-- intelligence, expertise, and how continual learning bridges the two. But I think this is perhaps one of the most important conceptual questions we need to think about today. And it can help explain many of the bizarre observations we're having at the AI frontier. The first observation is that AI has gotten so intelligent. Like this morning, OpenAI just came out with solving 10 other major math problems. But on the other hand, their diffusion in the enterprise world seems much slower than everyone expected. And we are seeing an explosion of these forward deployed engineers and deployment companies to help diffuse AI.

**[0:54](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=54s)** But if these AI are so smart, why we need FDEs to deploy them? Shouldn't they deploy themselves? The humans don't need an FDE to teach us how to do a job. So what's missing here? And then also, why, if we look at the value improvements in the AI stack, 90% of the value is going to the infra and the model layer. And the application layer is getting less than 10% and also often running at a negative margin. So why is that? And obviously, this is not a stable equilibrium for the ecosystem. So how can we solve that? So hopefully this talk will help explain many of these bizarre observations today. So obviously, agents, particularly, we

**[1:46](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=106s)** call the current generation of agents, the language agents. Because the language used for reasoning and communication is their defining traits. And they already found their first mass market, which is, obviously, in coding. And the best way to see that is through the revenue ramp of Anthropic's. Everyone has seen this magical story. But coding is the first mass market, largely because it's already a language-native world. Everything is already represented symbolically. And very well recorded and maintained. So that makes it perfect for language agents. But what if we leave the privileged world of code? Well, not so well yet. I think then, the [? Nevin ?] project

**[2:35](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=155s)** reported that we are having a lot of issues with deployment of AI in enterprise. Of course, this was from last year. And of course, you can argue about the 95% number. But I think it's directionally correct about the difficulties. And then we saw all of the bizarre failure modes of agents. And to a degree that Andrej Karpathy, last year, went on the Dwarkesh podcast to argue that 2025 was not going to be the year of agent, but it's going to be the start of the decade of agents. And he particularly mentioned challenges around computer use, around continual learning. So, I think what we're observing here is really a modern version of the Moravec's paradox.

**[3:25](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=205s)** So remember, the original version of the Moravec's paradox from the 1980s, essentially says, that for AI, it seems that hard things are easy, and easy things are hard. So they're particularly good at the symbolic reasoning tasks like math and coding. But very, very challenging to learn things that seems effortless for humans. Back in the '80s, it's mobility and perception. But now, we are seeing the difficulties in everyday digital work. And why is that? Here's my hypothesis. If you look at the modern society, it's really not just one unified world. It consists of millions of micro-worlds. Every profession is different. Every company is different. Every company is special.

**[4:11](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=251s)** That's why they exist. So every environment has its unique local physics-- the structures, the constraints, the affordances, the dynamics. It's just too heterogeneous and dynamic for any static model that tries to compress that into one static representation. So you have to continually learn on the job to form specialized expertise. And then that leads us to the next chapter. That intelligence is different from expertise. For intelligence, we will focus on the LLM context, the type of intelligence that LLMs exhibit. Then it's really the capacity to solve problems. Give me the problem statement, give me the context.

**[5:03](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=303s)** I will reason through this gigantic solution space and define-- maybe possibly spin up hundreds of subagents and try to find a solution for you. But expertise is different. Expertise is really accumulated and situated competence. It's the ability to act reliably and efficiently and with judgment to deliver superior performance on a particular job in a particular environment. So hopefully, through this, the contrast is very clear. And then what really does expertise contain? If we look into the literature from cognitive science, that can give us some insights. Essentially, when we are learning on the job to form expertise, it's the process

**[5:53](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=353s)** of continually forming new mental representations about that job, about that domain, that will manifest in multiple different ways. It will allow us to see things differently. For example, if you're looking at a very long bug report from a crashed system, obviously, an expert versus an intern will see things very differently. The expert will very quickly locate the plausible places of failure. And then expert can see the deep structure, not just the surface patterns. The experts know that everything is conditional. That for every rule, there are a whole bunch of preconditions that you need to learn, like when that rule holds. But you also need to learn what are the exceptions where you can bend

**[6:40](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=400s)** the rule against the reality. And finally, our judgment and taste, which we talk about a lot lately, also come from expertise. So from this, you can more or less think of expertise is really a world model. It's a model of that micro-world that manifests in many different ways. That becomes the foundation for our perception, for our reasoning, and for our decision making. Then we can further compare the two. But in the interest of time, I think what the most interesting here is to compare-- intelligence is, at least the form of intelligence LLMs have, are expansive in nature. It tries to look for the context on the fly,

**[7:32](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=452s)** tries to expand its search. And because it cannot accumulate from the past, as a result, it consumes a ton of tokens. Like NeoCognition, we're burning like millions of millions of dollars in tokens. But on for expertise, it's contractive in nature. It's about the process of forming shortcuts, forming effective structures of the domain that will reduce your search space. So next, I will talk about continual learning. But since I only have a few minutes, so I have to be much faster. But continual learning is a very confusing term. So let me first try to give a unifying definition. I think continual learning is the process

**[8:22](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=502s)** of adaptive compression of experience into reusable structures for future behavior. So all of these four elements are very important. And you need to answer-- when you talk about continual learning or see some work in continual learning, you need to understand each of these four elements, what exactly is being talked about. So what kind of experience we're talking about, how you are compressing them, and into what kind of structure, and how you use that structure for future behavior. But the adaptivity here is very important that the things that you compress in the past should determine how you compress in the future. Then, here's, I think, the most important and interesting part of this talk.

**[9:11](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=551s)** This is a relationship between intelligence, expertise, and continual learning. If you put intelligence as the x-axis and expertise as the y-axis, you will see that they are largely orthogonal. You can get more intelligent models. But if you don't have continual learning, then it will become what I call the world's smartest novice just tries to brute force its way through every problem using raw intelligence. That's why everyone's token bill is exploding. And different continual learning algorithms will essentially set the slope of your learning. So if the goal here is to have a very strong continual learning algorithm, that gives us very strong expert agents. And if we follow this setting, then the most interesting future

**[10:03](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=603s)** that we can derive from this is what I call unbounded expertise from bounded intelligence. What if there is a threshold for intelligence, we can call it escape intelligence. That once we cross that threshold plus a strong continual learning algorithm, then we can get almost unlimited expertise, or at least good enough for maybe 90% or 95% of the jobs in the world. Then if that becomes true, that means a very strong bifurcation of the market. So the frontier models, they will continue to build more intelligent models. And there will be many use cases for those. But maybe for the 90%, 95% of the other jobs, we don't need more intelligent models.

**[10:53](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=653s)** It may be even current models are good enough. What's left is continual learning. So that will be a very interesting dynamics in the market. I'll skip this one. These are some open questions we can answer, but just a few seconds to take a photo. And finally, I think the expertise will be the next dimension for scaling. But for scaling expertise, we the goal here is not to replace human labor. I don't believe in the job displacement narrative. I think we are in a great shortage of expertise. In an ideal world, everyone wants to have personal health, personal finance advisor, personal tutoring, and so on and so forth.

**[11:42](https://www.youtube.com/watch?v=VRWrA_KhHwU&t=702s)** And every company wants to build its own local human AI learning loop where the knowledge and the IP accrue. And finally, if we can scale, make expertise abundant, then it will lower the friction for many of the problems. That will make a lot of new problems across the threshold of worth doing. So that will create a lot of new opportunities in the society. So I'll stop here, and thanks for the attention. [APPLAUSE]
