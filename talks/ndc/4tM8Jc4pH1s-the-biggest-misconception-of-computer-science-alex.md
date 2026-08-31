---
id: 4tM8Jc4pH1s
title: "The Biggest Misconception of Computer Science - Alex Dathskovsky - NDC Toronto 2026"
slug: the-biggest-misconception-of-computer-science-alex
conference: ndc
conference_name: "NDC Conferences"
category: "Software dev with AI tracks"
edition: "NDC"
year: 2026
speakers: ["Alex Dathskovsky"]
channel: null
duration_min: 43
published_at: 2026-07-23T10:00:25Z
video_id: 4tM8Jc4pH1s
youtube_url: https://www.youtube.com/watch?v=4tM8Jc4pH1s
tags: ["Concurrency", "C++", "Tools", "NDC", "Conferences", "2026", "Live", "Fun", "Toronto", "Canada", "Alex Dathskovsky"]
transcript: false
---

# The Biggest Misconception of Computer Science - Alex Dathskovsky - NDC Toronto 2026

**Alex Dathskovsky**

`NDC Conferences` · `NDC` · `2026` · `43 min`

`#Concurrency` `#C++` `#Tools` `#NDC` `#Conferences` `#2026` `#Live` `#Fun` `#Toronto` `#Canada` `#Alex Dathskovsky`

[Watch the recording](https://www.youtube.com/watch?v=4tM8Jc4pH1s) · [Conference site](https://ndcconferences.com/)

## Description

This talk was recorded at NDC Toronto in Toronto, Canada. #ndctoronto #ndcconferences #developer #softwaredeveloper

Attend the next NDC conference near you:

/          @NDC

Follow our Social Media!

From our very first algorithms class, we are taught a simple rule: a better Big-O complexity means a faster algorithm. We spend years mastering asymptotic analysis, memorizing complexity tables, and losing sleep over worst-case scenarios. Big-O becomes a mental shortcut for “good” and “bad” code.

But the real world doesn’t run on whiteboards.

Modern performance is shaped far more by hardware realities than by asymptotic notation alone. CPUs have deep cache hierarchies, wide vector units, speculative execution, and memory systems that punish the “theoretically optimal” solution. GPUs thrive on massive parallelism where simple linear work can outperform asymptotically superior algorithms. Even on regular CPUs, cache-friendly linear scans often beat clever sub-linear approaches that fight memory latency.

In this talk, we will challenge the traditional Big-O mindset. We’ll look at classic algorithms through a modern lens and explore how hardware-aware designs cache-efficient layouts, SIMD/AVX vectorization, and parallel execution models can outperform algorithms with “worse” theoretical complexity. You’ll see why a higher Big-O algorithm can be faster, more scalable, and more predictable in practice.

The goal is not to dismiss Big-O, but to put it back in its proper place: as a tool, not a truth. By the end of this talk, you’ll think differently about performance and start writing code that works with the hardware, not against it.
