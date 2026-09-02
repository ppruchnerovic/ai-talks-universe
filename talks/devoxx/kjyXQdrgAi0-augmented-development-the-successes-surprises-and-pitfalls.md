---
id: kjyXQdrgAi0
title: "Augmented Development, the successes, surprises and pitfalls by Andy Bailey"
slug: augmented-development-the-successes-surprises-and-pitfalls
conference: devoxx
conference_name: "Devoxx"
category: "Software dev with AI tracks"
edition: "Devoxx"
year: 2025
speakers: ["Andy Bailey"]
channel: "Devoxx"
duration_min: 42
published_at: 2025-10-10T05:10:29Z
video_id: kjyXQdrgAi0
url: https://www.youtube.com/watch?v=kjyXQdrgAi0
youtube_url: https://www.youtube.com/watch?v=kjyXQdrgAi0
tags: []
transcript: false
---

# Augmented Development, the successes, surprises and pitfalls by Andy Bailey

**Andy Bailey**

`Devoxx` · `Devoxx` · `2025` · `42 min`

[Watch the recording](https://www.youtube.com/watch?v=kjyXQdrgAi0) · [Conference site](https://devoxx.com/)

## Description

My talk will be based on a real world project called FastDecimal: https://github.com/threadlocalrandom/FastDecimalThe original aim was to create a performance optimised replacement for BigDecimal with a scaling of 4 and using Long as the scaledValue. Although this limits the numerical range of values that can be represented by the type these restrictions on range and scale would be suitable for financial calculations providing acceptable accuracy of operations are achieved.In addition, the use of Long/long opens up scaling through the use of SIMD operations to parallelize computation.I decided it would be fun and educational to see how far I could take things using AI Agents like ChatGPT, Claude Sonnet, Gemini and Junie in developing FastDecimal.The project is small enough in scope to mean not too much time would be wasted if things didn&#39;t work and that I would be able to compare existing examples from BigDecimal to confirm correctness through code review and JUnit Tests. In addition I was going to supply JMH Benchmarks to compare BigDecimal and FastDecimal performance.I will be presenting both my methodology, the things things that worked, the things that really surprised me and those that didn&#39;t work at all. If time permits I will also be working on the project &quot;live coding&quot; or &quot;live prompting&quot; as well as answering questions from the audience.
