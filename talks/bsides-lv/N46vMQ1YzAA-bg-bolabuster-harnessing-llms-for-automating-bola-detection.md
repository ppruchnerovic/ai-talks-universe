---
id: N46vMQ1YzAA
title: "BG - BOLABuster: Harnessing LLMs for Automating BOLA Detection"
slug: bg-bolabuster-harnessing-llms-for-automating-bola-detection
conference: bsides-lv
conference_name: "BSides Las Vegas"
category: "AI security"
edition: "BSides Las Vegas"
year: 2024
speakers: []
channel: null
duration_min: 37
published_at: 2024-09-04T22:16:19Z
video_id: N46vMQ1YzAA
youtube_url: https://www.youtube.com/watch?v=N46vMQ1YzAA
tags: ["FSYWPG"]
transcript: false
---

# BG - BOLABuster: Harnessing LLMs for Automating BOLA Detection

**Speaker not identified**

`BSides Las Vegas` · `BSides Las Vegas` · `2024` · `37 min`

`#FSYWPG`

[Watch the recording](https://www.youtube.com/watch?v=N46vMQ1YzAA) · [Conference site](https://bsideslv.org/)

## Description

Breaking Ground, Wed, Aug 7, 12:30 - Wed, Aug 7, 13:15 CDT

BOLA poses severe threats to modern APIs and web applications. It's considered the top risk by OWASP API and a regularly reported vulnerability on HackerOne Top10. However, automatically identifying BOLAs is challenging due to application complexity, wide range of input parameters, and the stateful nature of modern web applications.

To overcome these issues, we leverage LLM's reasoning and generative capabilities to automate tasks, such as understanding application logic, revealing endpoint dependencies, generating test cases, and interpreting results. This AI-backed method, coupled with heuristics, enables full-scale automated BOLA detection. We dub this research BOLABuster.

Despite being in its early stages, BOLABuster has exposed multiple vulnerabilities in open-source projects. Notably, we submitted 15 CVEs for a single project, leading to critical privilege escalation. Our latest disclosed vulnerability, CVE-2024-1313, was a BOLA vulnerability in Grafana, an open-source platform with over 20 million users. When benchmarked against other state-of-the-art fuzzing tools, BOLABuster sends less than 1% of the API requests to detect a BOLA.

In this talk, we'll share the methodology and lessons from our research. Join us to learn about our AI journey and explore a novel approach to vulnerability research.

People
Jay Chen
Ravid Mazon
