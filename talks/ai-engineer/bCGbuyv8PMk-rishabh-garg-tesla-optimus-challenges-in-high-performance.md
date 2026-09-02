---
id: bCGbuyv8PMk
title: "Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems"
slug: rishabh-garg-tesla-optimus-challenges-in-high-performance
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2025
speakers: ["Rishabh Garg"]
channel: "AI Engineer"
duration_min: 13
published_at: 2025-08-25T15:00:05Z
video_id: bCGbuyv8PMk
url: https://www.youtube.com/watch?v=bCGbuyv8PMk
youtube_url: https://www.youtube.com/watch?v=bCGbuyv8PMk
tags: []
topics: ["Inference, serving & GPU infra", "Multimodal, vision, speech & robotics"]
transcript: false
---

# Rishabh Garg, Tesla Optimus — Challenges in High Performance Robotics Systems

**Rishabh Garg**

`AI Engineer` · `AI Engineer` · `2025` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=bCGbuyv8PMk) · [Conference site](https://www.ai.engineer/)

## Description

A robot's behavior is influenced by the control policy, the software configuration, and electrical characteristics of the communication protocol.

When unexpected behaviors arise, it is not straightforward to root cause them to the RL policy, electrical characteristics, mechanical characteristics. This talk walks through some of these issues and explains what might cause the observed behavior.

We will talk about concrete issues that audience will be able to take away from and develop their understanding of physical systems. It will build intuition for what kind of issues to expect when communication data rates increase manifold.

Timestamps
00:00 Introduction to high-performance robotics challenges
00:15 The problem of unexplained robot behavior
00:54 Root cause analysis: policy vs. software
01:17 Designing a toy robotics system for analysis
01:24 System architecture: sensors, CPU, GPU, actuators, CAN bus
01:57 The initial, simple code loop
02:14 Expectation vs. reality: unexpected loop execution gaps
02:42 The impact of CAN bus data rate on loop execution
03:13 Potential solutions: accepting delay vs. multithreading
04:00 A new, pipelined design for reduced cycle time
04:32 New problems: "stuttering" and abnormal motor behavior
04:49 Data collection with external transceivers and "candump"
05:24 Expected vs. actual message plots: missed messages and jitter
06:12 Using cycle time plots to identify desynchronization
06:58 Transmit phase desynchronization: missed and queued data
08:03 Receive phase desynchronization: stale data and overcompensation
08:38 Resolving synchronization issues: kernel primitives and padding
09:25 The impact of logging on system performance
11:09 Reception and priority inversion
12:02 Conclusion and summary of key takeaways

Rishabh Garg
Robotics Engineer at Tesla Optimus

I am Rishabh Garg, a robotics software engineer pushing the boundaries of software hardware integration to meet the ever increasing demand for data. I have been working with robots and embedded systems for the past 4 years, making systems more reliable and performant at companies like Tesla and Amazon. Eager to learn what experts in the industry are doing differently and share my own experience and insights into the challenges frequently encountered at the system software level for robotics.
