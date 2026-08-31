---
id: nQml4Ng9iVc
title: "Black Hat Asia 2026 | Model Files → Memory Corruption → RCE: The Triple-Stage AI Attack Chain"
slug: black-hat-asia-2026-model-files-memory-corruption-rce-the
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: "Black Hat"
duration_min: 37
published_at: 2026-08-30T19:45:36Z
video_id: nQml4Ng9iVc
youtube_url: https://www.youtube.com/watch?v=nQml4Ng9iVc
tags: []
transcript: false
---

# Black Hat Asia 2026 | Model Files → Memory Corruption → RCE: The Triple-Stage AI Attack Chain

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `37 min`

[Watch the recording](https://www.youtube.com/watch?v=nQml4Ng9iVc) · [Conference site](https://www.blackhat.com/)

## Description

Amidst the rapid advancement of artificial intelligence technologies, an increasing number of enterprises and individuals are adopting AI solutions. As the core vessel of AI systems, model files encapsulate substantial training outcomes and intellectual achievements from researchers. With the proliferation of large language models and the maturation of open-source communities, leading organizations are actively promoting model open-sourcing and sharing, making cutting-edge models accessible to developers worldwide.

However, in practical applications, the model loading process has emerged as a critical security vulnerability hotspot. Existing research reveals significant security risks in the model loading mechanisms of mainstream deep learning frameworks. For instance, PyTorch's historical use of pickle for model serialization introduces inherent deserialization vulnerabilities, while TensorFlow is susceptible to remote code execution (RCE) through maliciously crafted Lambda Layers. More alarmingly, as these frameworks predominantly employ C/C++ implementations for high-performance computing, they remain exposed to conventional memory safety threats such as buffer overflows. This raises a crucial question: Can these memory vulnerabilities be weaponized into complete and reliable RCE attack chains?

In this Briefing, to the best of our knowledge, we will present the first publicly disclosed study that systematically exploits memory corruption vulnerabilities in AI model files to achieve reliable remote code execution. By analyzing the memory management mechanisms of mainstream deep learning frameworks, we construct a complete, end-to-end three-stage attack chain — from malicious model files to arbitrary code execution — through carefully designed heap layouts and control-flow hijacking techniques. We further validate the practical exploitability of this attack chain across real-world AI inference systems.

Ji'an Zhou  |  Security Researcher
Lei Lu  |  Security Researcher
Li'shuo Song  |  Security Researcher
