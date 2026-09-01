---
id: lTJfa_zud3I
title: "Rahul Bakshi - Scale Compute to the Signal"
slug: rahul-bakshi-scale-compute-to-the-signal
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Rahul Bakshi"]
channel: "Berkeley RDI"
duration_min: 7
published_at: 2026-08-12T07:49:15Z
video_id: lTJfa_zud3I
youtube_url: https://www.youtube.com/watch?v=lTJfa_zud3I
tags: []
transcript: true
---

# Rahul Bakshi - Scale Compute to the Signal

**Rahul Bakshi**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `7 min`

[Watch the recording](https://www.youtube.com/watch?v=lTJfa_zud3I) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*978 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=lTJfa_zud3I&t=1s)** RAHUL BAKSHI: All right. So good afternoon, everyone. My name is Rahul, and I lead an applied science team at Amazon that's responsible for building our custom silicon. Our latest generation silicon, AZ3, powered our Echo devices that we launched last fall. So, as you can imagine, a lot of my time is spent worrying about edge compute, edge devices, and edge scale processing in general. And that's going to be the theme of my talk today. So we've spent the last few years talking about, how do we get more compute to our agents? And that's an important question, because it unlocks new capabilities. But I want to flip the question today. What if there wasn't more compute to give to our agents because of physics limitations?

**[0:53](https://www.youtube.com/watch?v=lTJfa_zud3I&t=53s)** And that's going to be one of the themes of my talk. And the other theme is that a lot of these edge agents do not require frontier-level intelligence for compute. And we are able to do some interesting optimizations to build use cases in very, very defined power budgets. All right. Let's talk about scaling of compute. How do we give more compute to our agents? One way to do it is by spinning up more data centers. We've all seen the news cycles in the last few years, Amazon other hyperscalers neoclouds. Everyone's building more and more gigafactories to give more compute to our agents.

**[1:43](https://www.youtube.com/watch?v=lTJfa_zud3I&t=103s)** And that's one lever. But on the other end, there is a real power ceiling. And I will use variable technology as one extreme of that ceiling, because the constraints are the hardest there. So if you think about any variable computer, such as our smartwatch, smart glasses, rings, and so on, they typically have around 1 to 1 and 1/2 watt of power to work with. And the reason is biological. Human skin cannot tolerate more than 43 degrees centrigrade of heat without starting getting burned, and it gets really uncomfortable. So that's the hard ceiling that we have to work with on the edge side. And the asymmetry between the edge and the cloud, I think, is the fertile ground for innovation,

**[2:32](https://www.youtube.com/watch?v=lTJfa_zud3I&t=152s)** for next-generation hybrid architectures. Let's look at the second observation. If you agree with this ceiling, and if this is the bounds that we have to work with, there are largely three tiers of power profiles of what executes on the edge scale devices. At the lowest and most power efficient tier are processing the signals where they originate. So think about tiny wake word detectors. Think about event cameras. You detect at source and you burn minimal energy. At the next level is, what do you want to do with that signal? If you have to run some algorithms, or if you have to run some tool calling workflows, that requires the next level of energy.

**[3:21](https://www.youtube.com/watch?v=lTJfa_zud3I&t=201s)** Still running on edge device, but, notice, a few orders of magnitude more compute, more power that gets burned. And then finally, if the task requires context that's not present on the device, or if it requires a world knowledge, then you invoke data center-class compute, which is even a few order of magnitude more. So what's the takeaway? The takeaway is, escalate only when the task calls for it. So the next observation I will share with you will give you the same conclusion, but with a couple of different lenses. So earlier this year, Berkeley has a function-calling leaderboard which tracks the function-calling efficiency of different models. And what we saw was that a small language model

**[4:12](https://www.youtube.com/watch?v=lTJfa_zud3I&t=252s)** was able to meet the frontier-level performance for function-calling task. This task tracks the primitives of function-calling. So the JSON that gets generated has the right functions, right APIs, right parameters. But the point is that, for small sets of tasks that are well-defined, we have a pathway of getting frontier-level intelligence on at-scale devices. And look on the right side of the chart. Over the last decade, the cost of transporting one bit of data across the wireless networks has gone down manyfold. However, what's not gone down by a similar factor is the cost of radio.

**[5:02](https://www.youtube.com/watch?v=lTJfa_zud3I&t=302s)** So that is, both of these data points are yet another observation on where the partitioning should lie. Escalation to the next year is expensive, both from an energy and battery life perspective, and should be done only when necessary. Now, for what are the opportunities? I think the loop has been well-established for more than a decade. If you look at the assistance from Amazon, Apple, Meta, most of them have a cascaded tier, where you detect the wake words and keep escalating only when necessary. What is missing is a composable runtime, and that's one call to action for this audience.

**[5:51](https://www.youtube.com/watch?v=lTJfa_zud3I&t=351s)** So let's take an example where you ask your assistant, hey, what time's my flight? Is it late? Now, if the runtime had the intelligence to know that, for doing this activity, I don't need to turn on any of the perception sensors, cameras, microphones, all I need is a turn on the radio and do an API call, then a power budget can be created, and the function-calling can take a certain dynamic schedule. So that's on the runtime side. A couple of other call for actions. I think benchmarks, there's a good opportunity to enhance those, and Berkeley's a fertile ground for that. Berkeley has a function-calling benchmark. I think there's an opportunity to extend those to also include joules per task, not just number of parameters and accuracy.

**[6:44](https://www.youtube.com/watch?v=lTJfa_zud3I&t=404s)** I think energy is also an important frontier. We talked about the runtime. And then finally, to the silicon developers in the audience, I'd recommend pushing the frontiers, lower the resting power, so that we can build more efficient agents for the edge. And that's a wrap. Thank you so much.
