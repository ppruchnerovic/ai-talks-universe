---
id: uFgB_aMw5-g
title: "Black Hat Asia 2026 | Large-Scale macOS PID-Domain Vulnerability Discovery with LLM Reasoning"
slug: black-hat-asia-2026-large-scale-macos-pid-domain
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2026
speakers: []
channel: null
duration_min: 25
published_at: 2026-08-29T14:30:03Z
video_id: uFgB_aMw5-g
youtube_url: https://www.youtube.com/watch?v=uFgB_aMw5-g
tags: []
transcript: false
---

# Black Hat Asia 2026 | Large-Scale macOS PID-Domain Vulnerability Discovery with LLM Reasoning

**Speaker not identified**

`Black Hat` · `Black Hat` · `2026` · `25 min`

[Watch the recording](https://www.youtube.com/watch?v=uFgB_aMw5-g) · [Conference site](https://www.blackhat.com/)

## Description

For years, macOS researchers have focused on high-privilege system and user domain services—yet a vast class of background daemons has quietly operated beneath the radar: PID-domain services. These processes, often reachable even from sandboxed apps, expose privileged functionality and sensitive system controls. Despite their enormous attack surface, they've remained largely unexplored and unprotected—until now.

In this Briefing, we will unveil the first large-scale automated framework for discovering logic vulnerabilities in PID-domain services, powered by LLM-assisted static analysis. We will start by dissecting historical flaws and Apple's patching patterns to formalize a repeatable attack model. Building on that foundation, our framework automatically enumerates connectable PID-domain daemons, decompiles their exported APIs, and leverages LLM semantic reasoning to classify sensitive operations across five categories—from file and privacy access to interprocess privilege crossing. We then map entitlements to these operations and apply taint analysis to trace attacker-controlled data into privileged sinks—surfacing hidden logic flaws that manual auditing would almost certainly miss.

Our evaluation uncovered 12 previously unknown vulnerabilities, including multiple sandbox escapes and TCC privacy bypasses—six of which have already been assigned CVEs by Apple. This research exposes a massive, underestimated attack surface within macOS's userspace and demonstrates how LLMs can be weaponized for scalable vulnerability discovery in closed-source ecosystems. Attendees will gain new insights into Apple's userspace attack surface, automated bug-hunting methodologies, and the next frontier of human–AI collaboration in exploit development.

l_m_h l_m_h  |  Independent Security Researcher
Yinyi Wu  |  Security Researcher, Dawn Security Lab, JD.com
Yingqi Shi  |  Security Researcher, DBAPPSecurity
Yuchong Xie  |  Security Researcher, The Hong Kong University of Science and Technology
Cheng Li  |  Security Researcher
Yizhuo Wang  |  Security Researcher
