---
id: GJhab1qXNig
title: "Self-Hosted GitHub CI/CD Runners: Continuous Integration, Continuous Destruction"
slug: self-hosted-github-ci-cd-runners-continuous-integration
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 40
published_at: 2025-02-28T18:21:18Z
video_id: GJhab1qXNig
url: https://www.youtube.com/watch?v=GJhab1qXNig
youtube_url: https://www.youtube.com/watch?v=GJhab1qXNig
tags: []
topics: ["AI in the SDLC & engineering orgs", "Security, safety & red teaming"]
transcript: false
---

# Self-Hosted GitHub CI/CD Runners: Continuous Integration, Continuous Destruction

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `40 min`

[Watch the recording](https://www.youtube.com/watch?v=GJhab1qXNig) · [Conference site](https://www.blackhat.com/)

## Description

There is currently a systemic lack of awareness around self-hosted CI/CD agent security.

Organizations can speed up their development lifecycle by using CI/CD systems like GitHub Actions, but in the process, they make fundamental configuration errors, especially when using self-hosted build agents. These misconfigurations expose organizations, and any dependents, to high-impact supply chain attacks by external threat actors.

We know this because over the past twelve months, we've discovered critical CI/CD vulnerabilities in GitHub, PyTorch, Microsoft, TensorFlow, and Web3 companies, to name a few.

The inspiration for these attacks came from our research into abusing self-hosted runners attached to GitHub repositories, focusing on GitHub Actions exploitation and post-exploitation. GitHub has default configuration options that can allow external attackers to compromise self-hosted runners via a poisoned pipeline attack. If the runner is non-ephemeral, an attacker can obtain persistence on the runner.

From that foothold, they can execute a series of attacks to escalate privileges and steal repository secrets or tamper with builds.

These secrets, which are often overprivileged, can allow an attacker to add malicious code to application releases. The impact of backdooring applications became clear during the SolarWinds breach in 2020. Abusing self-hosted runners through pipeline poisoning can result in the same impact. In fact, secrets we obtained access to could allow a nation-state to compromise GitHub releases, releases stored in AWS, Docker containers, NPM packages, and PyPi wheels of products used by thousands of organizations.

The first step to mitigating CI/CD vulnerabilities is understanding them. Most self-hosted runner pipeline attacks abuse several layered issues, each exposing an organization to compromise. All of the vulnerabilities we've discovered so far could have been prevented if developers, architects, and security engineers fully understood CI/CD security.

How can attackers exploit your organization's CI/CD pipelines? And how can you defend against these attacks?

By:
Adnan Khan  |  Security Researcher
John Stawinski  |  Security Researcher

Full Abstract and Presentation Materials:
