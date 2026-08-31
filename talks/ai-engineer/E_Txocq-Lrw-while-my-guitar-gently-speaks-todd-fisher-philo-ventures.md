---
id: E_Txocq-Lrw
title: "While my guitar gently speaks — Todd Fisher, Philo Ventures"
slug: while-my-guitar-gently-speaks-todd-fisher-philo-ventures
conference: ai-engineer
conference_name: "AI Engineer"
category: "AI engineering & agents"
edition: "AI Engineer"
year: 2026
speakers: ["Todd Fisher"]
channel: "AI Engineer"
duration_min: 19
published_at: 2026-08-18T15:30:23Z
video_id: E_Txocq-Lrw
youtube_url: https://www.youtube.com/watch?v=E_Txocq-Lrw
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning"]
transcript: false
---

# While my guitar gently speaks — Todd Fisher, Philo Ventures

**Todd Fisher**

`AI Engineer` · `AI Engineer` · `2026` · `19 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning`

[Watch the recording](https://www.youtube.com/watch?v=E_Txocq-Lrw) · [Conference site](https://www.ai.engineer/)

## Description

Someone in the audience asked the guitar what reality is, and the guitar answered. Todd Fisher's build routes a microphone through speech recognition into a local model and pushes the reply back out through the strings, which is the most recent step in a project that began with a much simpler question: how hard could it be to make a guitar speak?

The lineage he draws runs from a pickup and an amplifier, through stomp boxes, to Peter Frampton sending guitar sound down a physical hose into his mouth. His own version is a plugin built with JUCE that drops into a DAW like any other effect. Getting it to say one word was straightforward. Getting it to say several meant slicing synthesized speech into words automatically, and that turned out to be the hard part. Energy gap segmentation cuts wherever the signal falls toward silence, which fails because running speech often has no silence between words at all. A sonority peak syllabifier looks for vowels instead. Combining the two got close enough that he finished by dragging segment boundaries by hand. Singing needed a different stack again: the YIN algorithm to pull a fundamental frequency off each fretted note, a synthesized tone shaped by an envelope, then a vocoder, with pitch shifted samples from an open singing dataset baked ahead of time because the processing is far too heavy to run live. He also declines to play the song his title alludes to, on the grounds that this recording was going online.

Speaker info:
- https://www.linkedin.com/in/todd-b-fisher

Timestamps:
0:00 - Live performances that stayed with him
2:44 - The guitar's evolution, up to the talk box
4:24 - A Halloween project on a garage door
6:06 - Building it as a JUCE plugin, and saying one word
7:50 - Slicing speech into words, and why that is hard
10:23 - Pitch detection with the YIN algorithm
11:15 - Synthesis, vocoder, and jamming with it
13:28 - A guitar that answers questions from the room
16:01 - Pitch shifted samples, and getting closer to singing
17:51 - Go build your passion project
