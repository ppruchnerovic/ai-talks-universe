---
id: SJgp8-c35Zg
title: "Adarsh Hiremath - Enterprise AI"
slug: adarsh-hiremath-enterprise-ai
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Adarsh Hiremath"]
channel: "Berkeley RDI"
duration_min: 8
published_at: 2026-08-09T23:31:31Z
video_id: SJgp8-c35Zg
url: https://www.youtube.com/watch?v=SJgp8-c35Zg
youtube_url: https://www.youtube.com/watch?v=SJgp8-c35Zg
tags: []
transcript: true
---

# Adarsh Hiremath - Enterprise AI

**Adarsh Hiremath**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `8 min`

[Watch the recording](https://www.youtube.com/watch?v=SJgp8-c35Zg) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*1,513 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=2s)** ADARSH HIREMATH: First of all, thank you for having me. Figured I should start off with a little bit of an introduction about the company and myself. I'm Adarsh. I'm the founder and co-CEO of Mercor. I started the company when I was 19 in college, in my second year of Harvard. I started it with my co-founders, who I met in high school. We were all in the debate team together, so one of my co-founders was actually my debate partner back in the day, and the other was on the debate team as well. So we started off by working with a lot of the AI labs in selling data to make models better. And the core driving thing here was just the realization that the models had gotten sophisticated enough that it wasn't just about annotating an image and seeing if there's a stop sign in it.

**[0:50](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=50s)** It's like, can we make the model better at engineering? Can we make the model better at medical tasks? Can we make the model better at legal? And that requires really, really sophisticated human expertise. And then also the capabilities to structure the data in the right way for the agentic paradigm in RL environments and gyms. But that said, in 2026, the main focus area for Mercor, which not a lot of people know about, is enterprise. What we've seen is that the first kind of level is the labs and making the models better. Then you have all of these neo-labs, and then you have applied layer companies and startups like Harvey and Cursor. But then you have your average enterprise. And all four of those companies really, really want to own their own intelligence, apply it throughout the company, train their own models, and they need the fundamentally same offering in both training

**[1:41](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=101s)** and evals. So that's a little bit of context about the company and what we're prioritizing today. The thing that we're seeing is that there's a huge, huge shift in every company wanting to its own intelligence, as I was mentioning earlier. So there are several ways to own your own intelligence. The first one is obviously training your own model. A great example of this is Cursor, which trained their own composer model in collaboration with SpaceX, which is now a really, really good coding model. And they're able to fine tune this model with all of the Cursor data and infrastructure. The second one is adopting your own frontier model, and then engineering a harness that's really, really good for the product or the use case. A bunch of companies are doing this. But the common thread across both of these is you need a really, really good eval.

**[2:30](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=150s)** And that's where Mercor comes in helping with creating these evals. And it builds upon a lot of our work that we do with the labs and our frontier benchmarks like apex. One of the main issues that we've seen is that most of these enterprise AI use cases never reach production. Whether you're training your own model for an external agent, you're deploying agents inside the company. And that's just because there's no way to actually measure ground truth or success. So the typical guessing game or loop is you actually don't have a way to systematically identify agent opportunities in your product. So you guess where to start. Then you speculate on the agent and behavior, and then you deploy the agent, and then maybe you'll try it in a sandbox or something like that. And then a zoom, it kind of works. And then you improve it based on failures

**[3:19](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=199s)** that are largely observed or anecdotal or something like that. And this loop is really, really bad, which is why we believe in an eval-driven approach for enterprise AI deployments. So what is an eval? It's like a pretty overloaded term. So what I wanted to do is build upon the definition of eval and what that means for the enterprise context from apex, where what we do and we spend a lot of time thinking about what the labs is, figuring out where models are not performing as well as they should be, and then providing the right suggestions to improve model capability. So a common example would be when we're working with the labs, frontier model is coming out, and we'll benchmark that model across a bunch of different tasks across a bunch of different domains.

**[4:08](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=248s)** And typically, for the agentic use cases, the models will be doing work over many hundreds and hundreds of different turns, and we'll be able to analyze the trajectory, figure out where the model is failing and why. It turns out you can also do that for a lot of enterprise AI use cases as well, where fundamentally what you need is a task. What is the model actually doing? Then the second thing is you need the trajectory, which is what is the reasoning and rationale that the agent is using. The third is the actual artifact that it's producing. Fourth is the actual world. What is the context that agent is traversing? And then the last thing is a rubric or a verifier. So we have this for a lot of the foundation model lab evaluation. You should check out Apex our frontier benchmark which has a bunch of different domains

**[4:58](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=298s)** and this exact structure. But it also turns out this is really, really useful if you're deploying AI in any high stakes context, because you have full observability over what the agent is doing and why it's failing, and so on and so forth. So an example one of these evals would be this, which is a real investment banking task. So a banker might prompt the model to say, update this merger thing to show how a deal affects both companies. And then if you're doing the work manually, you might just go into an Excel. You might look at a specific merger model, you might go into a data room. You might get some feedback or get something wrong and then look it up and then go produce the actual model. It turns out you need observability over all of those things if you're

**[5:45](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=345s)** deploying an agent to do that. So in this case, a good agentic eval would be the actual task which is updating the merger model, the trajectory, which is all the different tools the agent is calling, found the merger model, updated the deal terms, build these tables all of this sort of stuff. The actual result, which is the merger model in a spreadsheet with the right citations. And then you have the verifier, which is where you can grade A lot of the responses. What is the output and does it meet subjective criteria, maybe stylistic guidelines and does it meet objective criteria, which is, is this thing actually correct? And one thing that we believe, which is pretty core to our business is that human intelligence is really, really important for that grading step and that eval step.

**[6:37](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=397s)** So a little bit more about what we do with enterprises and the problems that we're trying to solve. It's pretty interesting. So the first thing that we realized in a lot of the building of the evals is evals are in a large part or the bottleneck to successfully deploying agents in a company. And also allow you to just diagnose what are the agent opportunities, like if you build an eval for every single one of your departments in a proper mapping of these tasks, and what ground truth looks like in the rubric. It's very, very logical that you could come up with the top five areas in your company where you should deploy agents. So we're able to actually find where agents create value systematically and quantitatively with evals. Then secondly is, we're actually able to deploy agents and teach what good looks like in a company

**[7:27](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=447s)** and actually automate a lot of those processes. The third thing is, it turns out that evals are really, really the foundation for continuous learning and improvement. When you have an agent that fails on an eval, then you can triage up the reason it failed out to the skills file and make sure it never happens again. And then you can even post-train a model based on those failures and make sure that it never regresses. And the last thing, which is an effort that we're working on with a bunch of leading companies, is data monetization, where the labs really, really want to make sure that the models are good in these real enterprise use cases. And that scaffolding that I described-- the task, the trajectory, the context, the artifact, the rubric-- all of that together is really, really valuable data for model training at the foundation-model level. So that's a little bit more about what

**[8:16](https://www.youtube.com/watch?v=SJgp8-c35Zg&t=496s)** we're doing in enterprises and why we think evals are really, really important. Thank you. [APPLAUSE]
