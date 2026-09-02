---
id: bUamsPUHURA
title: "USENIX Security '25 - SelfDefend: LLMs Can Defend Themselves against Jailbreaking in..."
slug: usenix-security-25-selfdefend-llms-can-defend-themselves
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 12
published_at: 2025-10-30T20:00:26Z
video_id: bUamsPUHURA
url: https://www.youtube.com/watch?v=bUamsPUHURA
youtube_url: https://www.youtube.com/watch?v=bUamsPUHURA
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - SelfDefend: LLMs Can Defend Themselves against Jailbreaking in...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `12 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=bUamsPUHURA) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

SelfDefend: LLMs Can Defend Themselves against Jailbreaking in a Practical Manner

Xunguang Wang, Daoyuan Wu, Zhenlan Ji, Zongjie Li, Pingchuan Ma, and Shuai Wang, The Hong Kong University of Science and Technology; Yingjiu Li, University of Oregon; Yang Liu, Nanyang Technological University; Ning Liu, City University of Hong Kong; Juergen Rahmel, HSBC

Jailbreaking is an emerging adversarial attack that bypasses the safety alignment deployed in off-the-shelf large language models (LLMs) and has evolved into multiple categories: human-based, optimization-based, generation-based, and the recent indirect and multilingual jailbreaks. However, delivering a practical jailbreak defense is challenging because it needs to not only handle all the above jailbreak attacks but also incur negligible delays to user prompts, as well as be compatible with both open-source and closed-source LLMs.

Inspired by how the traditional security concept of shadow stacks defends against memory overflow attacks, this paper introduces a generic LLM jailbreak defense framework called SelfDefend, which establishes a shadow LLM as a defense instance (in detection state) to concurrently protect the target LLM instance (in normal answering state) in the normal stack and collaborate with it for checkpoint-based access control. The effectiveness of SelfDefend builds upon our observation that existing LLMs can identify harmful prompts or intentions in user queries, which we empirically validate using mainstream GPT-3.5/4 models against major jailbreak attacks. To further improve the defense's robustness and minimize costs, we employ a data distillation approach to tune dedicated open-source defense models. When deployed to protect GPT-3.5/4, Claude, Llama-2-7b/13b, and Mistral, these models outperform seven state-of-the-art defenses and match the performance of GPT-4-based SelfDefend, with significantly lower extra delays. Further experiments show that the tuned models are robust to adaptive jailbreaks and prompt injections.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
