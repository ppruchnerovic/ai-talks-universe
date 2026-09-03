---
id: ywm5krs1GEs
title: "The Devil is in the (Micro-) Architectures: Uncovering New Side-Channel and Bit-Flip Attack Surfaces"
slug: the-devil-is-in-the-micro-architectures-uncovering-new-side
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2025
speakers: []
channel: "Black Hat"
duration_min: 41
published_at: 2025-04-17T16:54:23Z
video_id: ywm5krs1GEs
url: https://www.youtube.com/watch?v=ywm5krs1GEs
youtube_url: https://www.youtube.com/watch?v=ywm5krs1GEs
tags: []
topics: ["Classic ML & data science", "Inference, serving & GPU infra", "Security, safety & red teaming"]
transcript: false
---

# The Devil is in the (Micro-) Architectures: Uncovering New Side-Channel and Bit-Flip Attack Surfaces

**Speaker not identified**

`Black Hat` · `Black Hat` · `2025` · `41 min`

[Watch the recording](https://www.youtube.com/watch?v=ywm5krs1GEs) · [Conference site](https://www.blackhat.com/)

## Description

The Devil is in the (Micro-) Architectures: Uncovering New Side-Channel and Bit-Flip Attack Surfaces in DNN Executables

Deep neural networks (DNNs) are increasingly deployed onto heterogeneous hardware ranging from powerful GPUs and accelerators to resource-limited mobile and IoT devices. In this process, deep learning (DL) compilers unlock the full performance potential of these platforms by automatically optimizing DNN inference computations and compiling the model for the target hardware, producing DNN executables as the output. In this talk, we uncover two new attack surfaces in DNN executables.

First, we show that attackers can steal model architectures in these executables using cache side-channels. This was impossible as the standalone natures and unique computation paradigms of DNN executables have mitigated existing attacking techniques targeting DNNs. However, we find that hardware- and cache-aware optimizations, an essential step in DL compiler pipelines, result in distinguishable DNN operator cache access patterns. Based on our analyses, we propose a general DNN architecture stealing framework named DeepCache, where we leverage standard cache side channels (e.g., Prime+Probe) as the attack primitive and combine contrastive learning and anomaly detection to achieve high accuracy.

We next switch to the perspective of DRAM microarchitectures and show that attackers can launch effective bit-flip attacks (BFAs, e.g., with Rowhammer) toward DNN executables using only the knowledge of victim model architectures (i.e., without knowing any victim model weights). This sharply contrasts existing BFAs on non-compiled models where attackers are always fully whitebox and omniscient. By strategically generating and profiling a series of same-structure-different-weights DNN executables locally, attackers can identify vulnerable bits to flip in the victim executable with high confidence despite their limited knowledge. Our evaluations on DDR4 DRAM show that attackers are able to downgrade the accuracy of victim executables to random guesses with few flips.

By:
Yanzuo Chen  |  Ph.D. Candidate, The Hong Kong University of Science and Technology
Zhibo Liu  |  Postdoc Researcher, The Hong Kong University of Science and Technology
Yuanyuan Yuan  |  Ph.D. Candidate, The Hong Kong University of Science and Technology
Tianxiang Li  |  Security Researcher, CSI AI Red Team
Sihang Hu  |  Security Researcher, CSI AI Red Team
Zhihui Lin  |  Security Researcher, CSI AI Red Team
Shuai Wang.  |  Associate Professor, The Hong Kong University of Science and Technology

Full Abstract and Presentation Materials:
