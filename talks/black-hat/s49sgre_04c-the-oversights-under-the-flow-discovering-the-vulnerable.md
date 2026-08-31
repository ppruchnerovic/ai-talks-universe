---
id: s49sgre_04c
title: "The Oversights Under the Flow: Discovering the Vulnerable Tooling Suites From Azure MLOps"
slug: the-oversights-under-the-flow-discovering-the-vulnerable
conference: black-hat
conference_name: "Black Hat"
category: "AI security"
edition: "Black Hat"
year: 2025
speakers: []
channel: null
duration_min: 47
published_at: 2025-08-27T16:04:33Z
video_id: s49sgre_04c
youtube_url: https://www.youtube.com/watch?v=s49sgre_04c
tags: []
transcript: false
---

# The Oversights Under the Flow: Discovering the Vulnerable Tooling Suites From Azure MLOps

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `47 min`

[Watch the recording](https://www.youtube.com/watch?v=s49sgre_04c) · [Conference site](https://www.blackhat.com/)

## Description

The Oversights Under the Flow: Discovering and Demystifying the Vulnerable Tooling Suites From Azure MLOps

With the new AI moving to the cloud, a sequence of ML/AI tooling suites has been integrated into the core Azure DevOps functionalities, yielding a new concept of MLOps to enable the LLM capabilities for Azure. However, despite these tools being maintained and reviewed by Microsoft staff, they are almost open-sourced and can be contributed by a broader scope of machine-learning communities. By this condition, any piece of bug is prone to be overlooked and committed into the released versions, posing as the Achilles' Heel to Azure MLOps.

In this talk, we present a set of new vulnerabilities we have discovered across several tooling suites within the Azure MLOps, affecting from the traditional Azure-CLI and AzureDev to the cutting-edge PromptFlow, Azure-AI-Generative, and DeepSpeed. We also demystify how these vulnerabilities can be exploited to impact the entire lifecycle of Azure MLOps, covering model training, testing, evaluation, and synthesis over the cloud and on-premise. We have reported our findings to MSRC via its Coordinated Vulnerability Disclosure Program and had five reports acknowledged as important severity (the maximal security impacts range from Local Privilege Escalation to Remote Code Execution), three as moderate, and the last two as low. In addition, we investigate the codebase of these vulnerable tools and surprisingly find that most of these vulnerabilities are just written accidentally due to some corner-case oversights. Their secure solutions are already located somewhere in the same codebase but overlooked to apply. Even worse, we can still discover similar oversights in patching progress during our coordinated disclosure, resulting in several incomplete fixes and unpatched overlooks. To this end, we'd like to discuss some potential countermeasures to awaken the maintainer's vigilance and thus stop repeating the same oversight, to protect Azure MLOps at its weakest flow.

By:
Peng Zhou  |  Associate Professor, Shanghai University

Full Abstract and Presentation Materials:
