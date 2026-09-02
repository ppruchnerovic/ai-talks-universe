---
id: hyeIWwFJd40
title: "USENIX Security '25 - Rowhammer-Based Trojan Injection: One Bit Flip Is Sufficient..."
slug: usenix-security-25-rowhammer-based-trojan-injection-one-bit
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "AI security"
edition: "USENIX"
year: 2025
speakers: []
channel: "USENIX"
duration_min: 10
published_at: 2025-10-30T20:02:11Z
video_id: hyeIWwFJd40
url: https://www.youtube.com/watch?v=hyeIWwFJd40
youtube_url: https://www.youtube.com/watch?v=hyeIWwFJd40
tags: ["usenix", "technology", "conference", "open access"]
transcript: false
---

# USENIX Security '25 - Rowhammer-Based Trojan Injection: One Bit Flip Is Sufficient...

**Speaker not identified**

`USENIX Security Symposium` · `USENIX` · `2025` · `10 min`

`#usenix` `#technology` `#conference` `#open access`

[Watch the recording](https://www.youtube.com/watch?v=hyeIWwFJd40) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '25 - Rowhammer-Based Trojan Injection: One Bit Flip Is Sufficient for Backdooring DNNs

Xiang Li, Ying Meng, Junming Chen, Lannan Luo, and Qiang Zeng, George Mason University

While conventional backdoor attacks on deep neural networks (DNNs) assume the attacker can manipulate the training data or process, recent research introduces a more practical threat model by injecting backdoors during the inference stage. These approaches exploit bit flip attacks to modify model weights, leveraging memory fault injection techniques like Rowhammer. However, they face a significant limitation—requiring multiple bits to be flipped simultaneously, which is highly difficult in practice. Additionally, they primarily target quantized models, leaving the feasibility of inference-time backdoor attacks on full-precision models unclear. To address these limitations, we propose ONEFLIP, the first one-bit-flip backdoor attack on full-precision models. Unlike prior methods that rely on optimization-based bit searches and require flipping multiple bits, our algorithm identifies the most promising weights for the attack and flips a single bit to insert a backdoor. We evaluate ONEFLIP on the CIFAR-10, CIFAR-100, GTSRB, and ImageNet datasets, covering different DNN architectures, including a vision transformer. The results demonstrate that ONEFLIP achieves high attack success rates (up to 99.9%, with an average of 99.6%) while causing minimal degradation to benign accuracy (as low as 0.005%, averaging 0.06%). Moreover, ONEFLIP is resilient to backdoor defenses. Our findings underscore a critical threat to DNNs: flipping just one bit in full-precision models is sufficient to execute a successful backdoor attack.

View the full USENIX Security '25 program at https://www.usenix.org/conference/usenixsecurity25/technical-sessions
