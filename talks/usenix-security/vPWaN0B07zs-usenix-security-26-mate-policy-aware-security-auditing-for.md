---
id: vPWaN0B07zs
title: "USENIX Security '26 - MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven T…"
slug: usenix-security-26-mate-policy-aware-security-auditing-for
conference: usenix-security
conference_name: "USENIX Security Symposium"
category: "Security conferences"
edition: "USENIX Security"
year: 2026
speakers: []
channel: "USENIX"
duration_min: 13
published_at: 2026-10-28T01:28:36Z
video_id: vPWaN0B07zs
url: https://www.youtube.com/watch?v=vPWaN0B07zs
youtube_url: https://www.youtube.com/watch?v=vPWaN0B07zs
tags: []
topics: ["Agents & orchestration", "Governance, ethics & regulation", "Security, safety & red teaming"]
transcript: true
---

# USENIX Security '26 - MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven T…

**Speaker not identified**

`USENIX Security Symposium` · `USENIX Security` · `2026` · `13 min`

[Watch the recording](https://www.youtube.com/watch?v=vPWaN0B07zs) · [Conference site](https://www.usenix.org/conference/usenixsecurity26)

## Description

USENIX Security '26 - MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning

Changyue Jiang, Fudan University and Shanghai Innovation Institute; Jiayi Wang, Xin Wen, Jiarun Dai, and Geng Hong, Fudan University; Xudong Pan, Fudan University and Shanghai Innovation Institute

Mobile agents powered by foundation models now automate complex, multi-step workflows on real devices, but their trajectories can violate app-specific security policies. Existing trajectory-level defenses rely on LLM prompting or rigid rules, and thus fail to support fine-grained, natural-language policies that generalize across apps and tasks. In this work, we introduce MATE, a lightweight, policy-conditioned auditor that encodes both agent trajectories and natural-language security policies to determine whether a trajectory violates a given policy and to explain why. Treating policies as editable text rather than fixed model parameters allows MATE to handle user-defined and evolving requirements without retraining. To construct MATE, we build a knowledge base by extracting app descriptions, workflows, and policies from hundreds of popular mobile apps worldwide, and synthesizing over 140K semantically realistic, policy-conditioned trajectories with a multi-stage pipeline. We further release MATEBench, a trajectory-level auditing benchmark with two synthetic subsets and one real-world subset of manually collected trajectories. Models trained with our synthesis-driven trajectory learning achieve over 95% accuracy on MATEBench, retain strong performance on external safety benchmarks, and audit trajectories from Zhipu's AutoGLM and Alibaba's Mobile-Agent on real devices with over 95% accuracy, outperforming prior methods by over 20%. MATE shows that practical, fine-grained security auditing for heterogeneous mobile agents is both feasible and effective.

View the full USENIX Security '26 program at https://www.usenix.org/conference/usenixsecurity26/technical-sessions

## Transcript

*1,024 words · source: supa (en, exact timings)*

**[0:20](https://www.youtube.com/watch?v=vPWaN0B07zs&t=20s)** Hello, my name is John Chang from FA University and the Shanghai Innovation Institute. Today I'm going to present mate a policy aware traitary auditor for mobile agents. Mobile agents are increasingly capable of operating smartphones on behalf of users. They can open applications, search for information, send messages, and complete complex tasks across multiple applications. However, as these agents gain more autonomy, an important uh security question emerges. When a mobile agent performs sequence of actions across real applications,

**[1:08](https://www.youtube.com/watch?v=vPWaN0B07zs&t=68s)** can we determine whether is entire trajectory violates a userdefined neutral language policy? Mobile agents interact directly with real applications through UI actions such as tapping and sweeping. A single task may involve many consecutive steps across different application states. For example, an agent may open a messaging application, search it for a content, retrieve information from another application, return to the messaging application, and finally send a message. The security implication of such

**[2:00](https://www.youtube.com/watch?v=vPWaN0B07zs&t=120s)** behavior cannot always be determined from an individ. More importantly, one action is secure or insecure depends on the active security policy. For example, sending an account number to a family member may be allowed on one or policy but prohibited under a stricter policy. Therefore, auditing must jointly reason over the trajetory and the policy. This creates two key challengings. First, security reasoning must consider the four interaction history rather than isolated actions. Second, the auditor must understand

**[2:52](https://www.youtube.com/watch?v=vPWaN0B07zs&t=172s)** flexible userdefined policies instead of relying on fixed roles. Our goal is therefore to build a traitary level auditor that gently reasons over agent behavior and the nature language security policies. We propose mate a lightweight policy aware traitory auditor. Mate takes the three major inputs. The user instruction, the agent trajectory and an editable nature language policy. Before auditing, we normalize the different mobile agent locks into a unified react representation.

**[3:43](https://www.youtube.com/watch?v=vPWaN0B07zs&t=223s)** Each interaction step contains three components. thought, action, and observation. Thought represents the agent's reasoning or intention. Action describes the actual operating and the observation captures the resulting application state. This unifying representation allows mate to work across different mobile agent frameworks. Mate then jointly encodes the instruction, trajetory and policy and produce three outposts. a violation in victor, a risk category and a nature language rational

**[4:32](https://www.youtube.com/watch?v=vPWaN0B07zs&t=272s)** explaining the decision to support different efficiency requirements which the lightweight mate model at three scales 0.5 billion 1.5 billion and three billion permits. We also define a mobile agent risk toxinomy with three major dominations and 14 subcategories enabling most drug and interpretable auditing. The next question is how do we obtain enough highquality training data? Large scale mobile agent security

**[5:20](https://www.youtube.com/watch?v=vPWaN0B07zs&t=320s)** trajectory are difficult and expensive to collect manually. To address this problem, our key idea is since it is driven traitory learning, we first collect public knowledge about mobile applications including mobile application functionality, common operation workflows and the security related information. This application specific knowledge is then used to generate executable user instructions and realistic reactive style trajectories. Each trajectory is associated with a security policy and labeled according to

**[6:12](https://www.youtube.com/watch?v=vPWaN0B07zs&t=372s)** whether it complies with the policy together with the corresponding risk category and explanation. Therefore the supervising is fundamentally policy conditioned the same or similar trajectory may receive different labels on the different policies forcing the mo forcing the model to learn policy trajectory alignment rather than a fixed definition of insecure behavior. To improve synthetic data quality, we introduce a multi-stage quality control process. It includes

**[7:03](https://www.youtube.com/watch?v=vPWaN0B07zs&t=423s)** structure normalization, semantic repair and policy alignment and finally human verification. The resulting trajectory are used both to train mate and to construct a migbench. To systematically evaluate a policy of real charged auditing, we introduce midbench which contains three. The first is MB bench in containing 2,75 synthetic trajectories from applications represented during training. The second is midbench out containing

**[7:53](https://www.youtube.com/watch?v=vPWaN0B07zs&t=473s)** 1,150 synthetic trajectory from 24 head out applications which evaluate generalization to unsee applications. The third is midbench re containing 162 real device charitories collected from real mobile agent systems including Jupus's autoglm and Alibaba's mobile agent. This split evaluate whether a model trended largely on synthes data can transfer to real agent behavior. We also compares

**[8:42](https://www.youtube.com/watch?v=vPWaN0B07zs&t=522s)** synthetic and the real trajectory statistically as shown in the figure. The sensor see the trajectories closely match real agents in charge length and action frequency patterns. This suggests that our synthesis pipeline captures important structure properties of real mobile agent behavior. However, deploying such an auditor in real system in introduced to practical problems. The the foster is trajectory diversity. Different mobile agent frameworks record

**[9:32](https://www.youtube.com/watch?v=vPWaN0B07zs&t=572s)** interactions in different formats. To address this, we introduce a traitory adapter which converts various logs into the same normalized reactor st representation used by mate. The second problem is policy availability in real deployments. Explicity policies may be incomplete or all available. We therefore introduce a policy retriever which is next relevant security policies from a global policy port according to the current task and trajectory. The retriever policies and the normalized trajectory are then provided

**[10:22](https://www.youtube.com/watch?v=vPWaN0B07zs&t=622s)** to mate. Finally meet performance complete trajectory auditing and retains the violation vict risk category and rational. We compare mate against the two main families of existing approaches stick row engines and the prompter based judges. Stick roles are efficient but struggle with complex semantic relationships between policies and long trajectories. LM judges provide a stronger semantic reasoning, but they are usually larger, more expensive, and less stable

**[11:12](https://www.youtube.com/watch?v=vPWaN0B07zs&t=672s)** across midbench and two additional benchmarks made consistently outperforms these baselines. Our three building model achieves more than 95% accuracy and improves over career evaluators by approximately 20% on average. Importantly, mate maintains stronger performance on both head out applications and the real device trajetories. This suggests that the model lends a general relationship between policies and the trajectory rather than simply memorizing application specific

**[12:01](https://www.youtube.com/watch?v=vPWaN0B07zs&t=721s)** patterns. Mate is also lightweight on a single H100 GPU. It auditing latency is only around 0.09 to 0.21 to one seconds per trajectory. Overall, mate achieves a stronger balance between accuracy, interpretability, generalization, and efficiency. Our model code and the project homepage are available through the cure codes shown here. Thank you very much for your attention.
