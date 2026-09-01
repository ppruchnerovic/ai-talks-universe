---
id: H8X6zlarPv8
title: "John Liu - Looping for Model Optimization"
slug: john-liu-looping-for-model-optimization
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["John Liu"]
channel: "Berkeley RDI"
duration_min: 6
published_at: 2026-08-12T07:49:26Z
video_id: H8X6zlarPv8
url: https://www.youtube.com/watch?v=H8X6zlarPv8
youtube_url: https://www.youtube.com/watch?v=H8X6zlarPv8
tags: []
transcript: true
---

# John Liu - Looping for Model Optimization

**John Liu**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `6 min`

[Watch the recording](https://www.youtube.com/watch?v=H8X6zlarPv8) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*957 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=H8X6zlarPv8&t=1s)** JOHN LIU: All right. Good afternoon. Yep. John Liu, principal product manager for AWS Trainium. And today, we're going to talk about looping and model optimization on AWS Trainium, which is the custom AI accelerator used by leading frontier labs such as Anthropic and OpenAI. So why is this relevant now? And when you think of it from-- there's probably two angles. First, from the business angle. As Peter DeSantis mentioned in yesterday's keynote, the future of agentic workloads is going to be one with many chips, custom built for the different purposes of that agentic workload. Now, at the same time, agentic harnesses agentic solutions, they've been gaining adoption. They've been getting more mature. As you'll see, the model optimization path on custom hardware is actually very well-suited for this type

**[0:52](https://www.youtube.com/watch?v=H8X6zlarPv8&t=52s)** of workload. So what does a typical model optimization loop look like? Well, you start by creating a functional model on the custom hardware. And then you take some knobs on the model level and harness-level type of configurations, such as changing the parallelisms, changing sequence length, batch sizes, and then you profile that. You profile and see how the performance is. And based on that, you go through a loop. You change more things. At a certain level. You're going to maximize what you can get from these out-of-box knobs. So then you drop into the kernel development. And think of kernels just as custom functions that let you unlock more performance on hardware. Again, you tune those. You profile it, and you have that second loop.

**[1:40](https://www.youtube.com/watch?v=H8X6zlarPv8&t=100s)** But you're not done yet. Once that kernel is optimized, you actually need to do end-to-end model evaluation as well, just to make sure it works. And now you complete yet another loop. So you can see, this is actually a multilayer, multivariable type of optimization problem, very well-suited for looping. And we've actually released some open-source agents and skills to help our customers turn what took weeks into pretty much hours. These skills help people create functional models on AWS Trainium, author kernels, profile kernels. And now we're working on the optimization loop as well. So let's dive a little deep into one of these optimization loops, which is the kernel optimization loop. And this is a common setup. We use what's called a planner and executor-type of model.

**[2:30](https://www.youtube.com/watch?v=H8X6zlarPv8&t=150s)** And the goal that we try to loop towards is, what's the gap towards the maximum performance that that hardware can achieve on your particular model? So starting from step 0, there's another loop that identifies for a given inference workload. What's the best settings? And it passes that through our planner agent. That's step 1. The planner agent looks at this, and it measures the gap to roofline. And it looks at its local knowledge base and identifies the best optimization campaigns. It passes that to the executor agents, which runs these campaigns. And then, based on those outcomes, it records the outcomes in the knowledge base. Did this kernel work? Did it fail? What were the constraints? And then we measured the performance of that end-to-end model. And finally, based on those outcomes,

**[3:19](https://www.youtube.com/watch?v=H8X6zlarPv8&t=199s)** we decide to promote or reject that kernel, and, of course, update the knowledge base as well. And that completes the loop. So I want to share some insights that we have from building these loops. And hopefully, they're applying to not just the specialized domains, but everyone's loops. Number one, a recurrent theme that you've heard from is agents are very sophisticated in coming up with cheating. The standard approach of telling agents agents, don't cheat, that's not enough. The mitigations of creating held out data sets and making sure that agents aren't memorizing things, that's the baseline. What you need to think about is every single part of your agentic workload is going to be manipulated by that agent, especially the area where you're measuring performance. The second insight, which is whenever your agent fails,

**[4:09](https://www.youtube.com/watch?v=H8X6zlarPv8&t=249s)** don't go through and just start fixing that agent itself, check the visibility scope. In one of our examples, that agent was actually maximizing local memory usage for the kernel, which is the right decision, but that affected all the shared memory usage for the other kernels that were running on the model. So check your visibility scope as you're designing your agent actions. Third, when you're creating these knowledge bases, whenever something goes wrong, check to see if one of your existing rules caused the error. Edit and delete that rule instead of just adding yet another rule, because now you're going to start confusing the agent with more rules. And on a related topic, that knowledge base that you have has a shelf life. In specialized domains, this knowledge base is very helpful to get your agent started.

**[4:58](https://www.youtube.com/watch?v=H8X6zlarPv8&t=298s)** But as the model's general training catches up, now you're going to have some kind of conflict. Your agent is going to get confused. Should I use the knowledge base, or should I use the model training? So a good practice is to constantly remove the knowledge base and check the performance of your agent. And if it improves, it's time to prune that knowledge base. Finally, in specialized domain, there's no standard data set or benchmark for success. So as you're designing your process for improving things, you're also defining what that better thing is. And you have to design the benchmark in evaluation as a first-class design component before you get to the rest of your loop, because it affects how that loop operates. So a very short amount of time.

**[5:45](https://www.youtube.com/watch?v=H8X6zlarPv8&t=345s)** If you want to learn more, check out our blog, check out our GitHub. And thank you very much for your time.
