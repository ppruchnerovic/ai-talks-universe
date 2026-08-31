---
id: FrdBAml7FR4
title: "USENIX Security '25 - CAMP in the Odyssey: Provably Robust Reinforcement Learning with Certified..."
slug: usenix-security-25-camp-in-the-odyssey-provably-robust
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX Security"
year: 2025
speakers: []
channel: null
duration_min: 13
published_at: 2025-10-30T20:03:02Z
video_id: FrdBAml7FR4
youtube_url: https://www.youtube.com/watch?v=FrdBAml7FR4
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - CAMP in the Odyssey: Provably Robust Reinforcement Learning with Certified...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2025` · `13 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=FrdBAml7FR4) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

CAMP in the Odyssey: Provably Robust Reinforcement Learning with Certified Radius Maximization

Derui Wang, Kristen Moore, Diksha Goel, and Minjune Kim, CSIRO's Data61 and Cyber Security Cooperative Research Centre; Gang Li, Yang Li, and Robin Doss, Deakin University; Minhui Xue, CSIRO's Data61 and Cyber Security Cooperative Research Centre; Bo Li, University of Chicago; Seyit Camtepe, CSIRO's Data61 and Cyber Security Cooperative Research Centre; Liming Zhu, CSIRO's Data61

Deep reinforcement learning (DRL) has gained widespread adoption in control and decision-making tasks due to its strong performance in dynamic environments. However, DRL agents are vulnerable to noisy observations and adversarial attacks, and concerns about the adversarial robustness of DRL systems have emerged. Recent efforts have focused on addressing these robustness issues by establishing rigorous theoretical guarantees for the returns achieved by DRL agents in adversarial settings. Among these approaches, policy smoothing has proven to be an effective and scalable method for certifying the robustness of DRL agents. Nevertheless, existing certifiably robust DRL relies on policies trained with simple Gaussian augmentations, resulting in a suboptimal trade-off between certified robustness and certified return. To address this issue, we introduce a novel paradigm dubbed Certified-rAdius-Maximizing Policy (CAMP) training. CAMP is designed to enhance DRL policies, achieving better utility without compromising provable robustness. By leveraging the insight that the global certified radius can be derived from local certified radii based on training-time statistics, CAMP formulates a surrogate loss related to the local certified radius and optimizes the policy guided by this surrogate loss. We also introduce policy imitation as a novel technique to stabilize CAMP training. Experimental results demonstrate that CAMP significantly improves the robustness-return trade-off across various tasks. Based on the results, CAMP can achieve up to twice the certified expected return compared to that of baselines. Our code is available at https://github.com/NeuralSec/camp-robust-rl.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
