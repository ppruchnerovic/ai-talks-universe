---
id: YlS2K18OqYY
title: "USENIX Security '25 - Enhanced Label-Only Membership Inference Attacks with Fewer Queries"
slug: usenix-security-25-enhanced-label-only-membership-inference
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 16
published_at: 2025-10-30T20:02:02Z
video_id: YlS2K18OqYY
youtube_url: https://www.youtube.com/watch?v=YlS2K18OqYY
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - Enhanced Label-Only Membership Inference Attacks with Fewer Queries

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `16 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=YlS2K18OqYY) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

Enhanced Label-Only Membership Inference Attacks with Fewer Queries

Hao Li, Institute of Software, Chinese Academy of Sciences; Zheng Li, Shandong University; Siyuan Wu, Yutong Ye, Min Zhang, and Dengguo Feng, Institute of Software, Chinese Academy of Sciences; Yang Zhang, CISPA Helmholtz Center for Information Security

Machine Learning (ML) models are vulnerable to membership inference attacks (MIAs), where an adversary aims to determine whether a specific sample was part of the model's training data. Traditional MIAs exploit differences in the model's output posteriors, but in more challenging scenarios (label-only scenarios) where only predicted labels are available, existing works directly utilize the shortest distance of samples reaching decision boundaries as membership signals, denoted as the shortestBD. However, they face two key challenges: low distinguishability between members and non-members due to sample diversity, and high query requirements stemming from direction diversity.

To overcome these limitations, we propose a novel label-only attack called DHAttack, designed for Higher performance and Higher stealth, focusing on the boundary distance of individual samples to mitigate the effects of sample diversity, and measuring this distance toward a fixed point to minimize query overhead. Empirical results demonstrate that DHAttack consistently outperforms other advanced attack methods. Notably, in some cases, DHAttack achieves more than an order of magnitude improvement over all baselines in terms of TPR @ 0.1% FPR with just 5 to 30 queries. Furthermore, we explore the reasons for DHAttack's success, and then analyze other crucial factors in the attack performance. Finally, we evaluate several defense mechanisms against DHAttack and demonstrate its superiority over all baseline attacks.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
