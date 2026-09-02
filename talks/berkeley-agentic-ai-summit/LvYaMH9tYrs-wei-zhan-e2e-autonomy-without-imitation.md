---
id: LvYaMH9tYrs
title: "Wei Zhan - E2E Autonomy Without Imitation"
slug: wei-zhan-e2e-autonomy-without-imitation
conference: berkeley-agentic-ai-summit
conference_name: "Berkeley RDI Agentic AI Summit"
category: "AI engineering & agents"
edition: "Agentic AI Summit 2026"
year: 2026
speakers: ["Wei Zhan"]
channel: "Berkeley RDI"
duration_min: 7
published_at: 2026-08-09T23:27:45Z
video_id: LvYaMH9tYrs
url: https://www.youtube.com/watch?v=LvYaMH9tYrs
youtube_url: https://www.youtube.com/watch?v=LvYaMH9tYrs
tags: []
topics: []
transcript: true
---

# Wei Zhan - E2E Autonomy Without Imitation

**Wei Zhan**

`Berkeley RDI Agentic AI Summit` · `Agentic AI Summit 2026` · `2026` · `7 min`

[Watch the recording](https://www.youtube.com/watch?v=LvYaMH9tYrs) · [Conference site](https://rdi.berkeley.edu/events/agentic-ai-summit)

## Description

*No description published on YouTube.*

## Transcript

*760 words · source: supa (en, exact timings)*

**[0:02](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=2s)** WEI ZHAN: Thanks for the introduction. Good afternoon, everyone. So today, I'm going to talk a bit about end-to-end autonomy, which is the first massively productionized physical AI in the real world. So we want to talk about how we can enhance such kind of autonomy with something without imitation, just with reinforcement learning, which is a bit counterintuitive to the mainstream. So for those who are not super familiar with Applied Intuition, so we are a premier physical AI technology provider covering various kinds of industry verticals, including cars, trucks, agriculture, mining, constructions with autonomy stack, OS, simulation tools, and broader physical AI

**[0:52](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=52s)** infrastructures. We are a 15 billion valuation company with over 1,000 engineers. We are also conducting cutting-edge research on reinforcement learning world models with applications to autonomy and robotics, with many publications in top venues, including some award-winning papers. So for the paradigm of L2++ ADAS, it has converged to imitation learning-based end-to-end with mass production. And some of the leading players also conducted post-training with open loop reinforcement learning. To bring the safety and robustness of such autonomy into the next level, end-to-end autonomy is expected to be trained with closed-loop reinforcement

**[1:43](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=103s)** learning in a world model that can generate-- reactively generate some surrounding behavior and visions in a reactive way. And this is how the paradigm is shifting for autonomy from the AV2.0 open-loop scaling, to the AV3.0, closed-loop scaling. So at Applied, we have been creating the high throughput reactive world model to support large-scale, closed-loop reinforcement learning for end-to-end autonomy without imitation. And such kind of paradigm has achieved great performance. But the question is, is there a smart-- even smarter way to achieve this?

**[2:30](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=150s)** So our approach is try to decouple, learn to drive, and learn to see. So here is how we are doing this. In phase I, we try to learn to drive by exploiting large-scale self-play reinforcement learning. Actually, just now, Michael just gave a very good example on how self-play is empowering the autonomous racing. And I'm trying to give an example of how this is empowering the autonomous urban driving. And in the second phase, we can try to utilize a super robust and generalizable self-play expert to teach another end-to-end autonomy to align its output of the driving behavior. So for phase 1, learn to drive.

**[3:21](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=201s)** We created TerraZero, which is a self-play reinforcement learning framework that is much faster, with much higher throughput than other state-of-the-art driving simulator and self-play framework. Actually, we are just utilizing some public dataset, scale, map, diversity. Well, it can still obtain 25 centuries of driving experience with zero human demonstrations. And actually, we can easily scale up such kind of numbers into two to three orders of magnitude higher by scaling the GPU compute, as well as the map diversity. So the policy train from TerraZero

**[4:09](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=249s)** can achieve state of the art on various closed-loop planning benchmarks, which is vector-based. So it's setting a clear edge to the imitation learning-based planners, especially on the ones that is not saturated with corner case only, such as the InterPlan benchmark. And it can handle various kinds of challenging driving scenarios with desirable actions, with zero shot generalizability across the global cities. And that concludes the first phase-- learn to drive. Second, let's talk about learn to see. We proposed TerraTransfer, which is training end-to-end autonomy taught from another expert trained from self-play,

**[5:02](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=302s)** which is TerraZero. What we are trying to do is to align the latent, as well as the actions for both of them, with the same driving cases from the offline dataset. And such kind of TerraTransfer end-to-end autonomy without any imitation in its training recipe can obtain state-of-the-art driving performance on the closed-loop, end-to-end driving benchmarks, setting a clear edge to the other imitation-based methods, tackling various kinds of intentionally created, challenging driving scenarios with surprisingly robust driving behavior. So that concludes the talk. And the key takeaway is the autonomy paradigm has been

**[5:53](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=353s)** shifting towards the close of scaling, which is AV3.0. And both the end-to-end and vector-based planner can achieve the state of the art with self-play or close reinforcement learning-only training recipe without imitation. And actually, the self-play were close RL with reactive world model. That is not just some post-training technique. Actually, they are very powerful pretraining techniques for autonomy development. And the throughput for reinforcement learning framework and the world models can be a decisive factor for such kind of paradigm for closed-loop scaling. Thank you very much for your attention.

**[6:40](https://www.youtube.com/watch?v=LvYaMH9tYrs&t=400s)** [APPLAUSE]
