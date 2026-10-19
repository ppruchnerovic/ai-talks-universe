---
id: htod7Nv1cBc
title: "How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song"
slug: how-minimax-m3-was-built-sparse-attention-and-native
conference: ai-engineer
conference_name: "AI Engineer"
category: "Practitioner AI conferences"
edition: "AI Engineer"
year: 2026
speakers: ["Olive Song"]
channel: "AI Engineer"
duration_min: 15
published_at: 2026-10-10T22:30:23Z
video_id: htod7Nv1cBc
url: https://www.youtube.com/watch?v=htod7Nv1cBc
youtube_url: https://www.youtube.com/watch?v=htod7Nv1cBc
tags: ["ai", "ai engineer", "ai engineering", "software development", "tech", "startups", "software architecture", "machine learning", "MiniMax", "MiniMax M3", "open weight model", "multimodal", "native multimodal", "sparse attention", "MSA", "DeepSeek DSA", "long context", "LLM architecture", "pretraining", "vision transformer", "reinforcement learning", "Olive Song", "AI Engineer"]
topics: ["Multimodal, vision, speech & robotics", "Prompting & context engineering", "Training, fine-tuning & model building"]
transcript: true
---

# How MiniMax M3 Was Built: Sparse Attention and Native Multimodality — Olive Song

**Olive Song**

`AI Engineer` · `AI Engineer` · `2026` · `15 min`

`#ai` `#ai engineer` `#ai engineering` `#software development` `#tech` `#startups` `#software architecture` `#machine learning` `#MiniMax` `#MiniMax M3` `#open weight model` `#multimodal` `#native multimodal` `#sparse attention` `#MSA` `#DeepSeek DSA` `#long context` `#LLM architecture` `#pretraining` `#vision transformer` `#reinforcement learning` `#Olive Song` `#AI Engineer`

[Watch the recording](https://www.youtube.com/watch?v=htod7Nv1cBc) · [Conference site](https://www.ai.engineer/)

## Description

Most models learn text first and get vision bolted on later. MiniMax M3 learned both from the very first training step.

Olive, who works on reinforcement learning research at MiniMax, goes inside MiniMax M3, an open-weight model with frontier-level coding and agentic ability, a 1 million token context window and native multimodality. She explains MSA, MiniMax's sparse attention design (about 9x faster prefill and 15x faster decoding than full attention): an index branch that picks which blocks matter and a sparse branch that attends only to those, and why existing designs like DeepSeek's DSA didn't fit grouped-query attention or GPU memory access. Then she covers training with text and vision from step zero, why adding vision later gave unstable results, what the attention maps show, and why 3D attention inside the vision transformer improves visual understanding.

In this talk:
• What makes MiniMax M3 different: agentic coding, 1M context, native multimodal
• How MSA sparse attention works, and why DSA didn't fit
• Block-level retrieval and kernels built for real GPUs
• Why training on text and vision from step zero beats adding vision later

SPEAKER
Olive Song, RL Lead, MiniMax
X: https://x.com/olive_jy_song

LINKS
MiniMax: https://www.minimax.io
MiniMax M3 (GitHub): https://github.com/MiniMax-AI/MiniMax-M3
MiniMax M3 (Hugging Face): https://huggingface.co/MiniMaxAI/MiniMax-M3
MiniMax M3 tech report: https://arxiv.org/abs/2606.13392
MSA (GitHub): https://github.com/MiniMax-AI/MSA

CHAPTERS
0:00 Intro
1:03 Meet MiniMax M3
1:37 1M token context
2:57 Sparse attention: index and sparse branches
4:17 Why not DeepSeek's DSA?
5:07 Problems with existing sparse attention
5:37 GPU memory access
7:01 MSA: what we changed
7:46 Block-level retrieval
8:21 Efficient kernels
9:01 Multimodal from step zero
9:46 Training strategies compared
11:45 What the attention maps show
13:10 3D attention in the ViT

Recorded at the AI Engineer World's Fair 2026 in San Francisco.

AI Engineer: https://ai.engineer
YouTube: https://www.youtube.com/@aiDotEngineer
X: https://x.com/aiDotEngineer

## Transcript

*1,842 words · source: supa (en, exact timings)*

**[0:01](https://www.youtube.com/watch?v=htod7Nv1cBc&t=1s)** [music] >> Um all right. Um so, hi everyone. I My name is Olive. I work at Minimax on reinforcement learning research. And today, I'm going to talk a little bit about um our new model, Minimax M3, and how we trained it natively multimodal from step zero, and how we trained it with MSA, which is called uh which is Minimax sparse attention. Um a little bit introduction of our team. Uh we are one of the few labs over the world that uh works on multimodalities, which means that we have published our um of course LLM

**[0:51](https://www.youtube.com/watch?v=htod7Nv1cBc&t=51s)** models before. Um we worked on our speech models. We have our own video generation models, and we have our coding agent models. And lately, we just released our Minimax M3, which is open weight uh with frontier performance. So, it is actually the first open weight model to combine the following three um frontier capabilities. The first one is what we call soda uh coding and agent capabilities. The model is able to do a lot of the uh agentic tasks that you imagine. Um it it can do automatic task decomposition. It can work in your coding agents. It can drop in for 90% of the coding works that you are currently

**[1:38](https://www.youtube.com/watch?v=htod7Nv1cBc&t=98s)** doing. And the second pillar is that the model has 1 million context window. Um so, which is very long that enable like unlocks pretty much base all basic user long user interactions um of like it handles full code bases. And we trained it with MSA Minimax sparse attention. So, it is nine times faster pre-fill and 15 times faster decode versus full attention. And the third one is that the the model was trained native multi-model from step zero. Which means that from step from scratch, we combined visual understanding with um language generation. So, the model would understand both capabilities very well from the start. And uh so that we can build many more

**[2:27](https://www.youtube.com/watch?v=htod7Nv1cBc&t=147s)** applications on that, say computer use agents right? So, first I'll briefly explain what sparse attention does. Our core design principle is that a simpler architecture can always lead to better scaling properties. This is the principle we have followed throughout the entire design. So, our goal is to always pursue a cleaner and simpler architecture. The sparse attention consists of two branches. The first one is what we call the index branch. Which performs a lightweight full attention computation. It uses four query heads and one key head. And it is trained with a KL loss to match the attention scores of the main branch.

**[3:15](https://www.youtube.com/watch?v=htod7Nv1cBc&t=195s)** The index branch is used to identify the tokens with the highest attention scores. These selected tokens are then attended by by the main branch. In other words, the sparse branch does not attend to all of the tokens. But only to a subset of them. This subset is selected through the lightweight computation of the index branch. Then, the sparse branch would use the blocks selected by the index branch to to determine which keys and values are needed for attention computation. All right.

**[4:04](https://www.youtube.com/watch?v=htod7Nv1cBc&t=244s)** And what I want to emphasize today is that our design is not purely algorithm like algorithm driven. Instead, we took an algorithm algorithm and infrastructure co-design approach. Um a good good example to start with is DSA. DSA was a very strong design, but it is also highly optimized for Deep Seek's own architecture, especially the combination of MQA and the large head beam. However, when we move to a more commonly used GQA architecture, directly applying the same design becomes less straightforward. It introduces several practical issues, especially from the infrastructure and implementation perspective. So, this motivates our design choice.

**[4:53](https://www.youtube.com/watch?v=htod7Nv1cBc&t=293s)** Instead of simply borrowing an existing sparse attention design, we re-think the architecture under the constraints of GQA and real system efficiency. So, what are the issues if we directly apply the existing sparse attention architecture? First, from the algorithm perspective, GQA has multiple KV heads, which should ideally provide more diversity across different KV groups. However, if we directly reuse the same token selection strategy, multiple KV heads will end up attending to exactly the same selected tokens. This essentially cancels out the diversity that GQA is is supposed to provide. Second, from the infrastructure

**[5:42](https://www.youtube.com/watch?v=htod7Nv1cBc&t=342s)** perspective, this design is not very friendly to GPU memory access. GPUs are much more efficient when reading contiguous data. In the MQA setting, we can think of the KV 8 layout as one KV head with a large head dimension, for example, 1 by 512. This is relatively contiguous and efficient to read. However, in GQA, the same total dimension may be split across multiple KV heads. For example, it's 4 by 128. These are no longer one single contiguous read. Instead, the GPU needs to perform multiple independent reads across different KV heads. This increases memory access overhead and reduces the compute-to-memory access ratio.

**[6:32](https://www.youtube.com/watch?v=htod7Nv1cBc&t=392s)** And another issue here is the top-k computation itself. To select the most important tokens, the indexer needs to compute top-k scores over a large number of token-level candidates. However, top-k has inherent data dependencies. So, it is difficult to fully parallel on GPU. As a result, token-level selection introduces non-trivial computation and merging overhead. So, how did we address these issues in MSA? From the algo- From the algorithm side, we remove the aggregation of the index branch outputs. In the original design, the results from all index branch In index branch heads are merged into a single set of selected tokens. But, as we discussed earlier, this would

**[7:21](https://www.youtube.com/watch?v=htod7Nv1cBc&t=441s)** remove the diversity brought by GQA. Instead, we keep the selection different different across KV heads. Under our sparse attention design, when using GQA, different KV heads can attend to different sets of tokens. This helps preserve the diversity of GQA rather than forcing all heads to share the same sparse tension. For the infrastructure side, we move from token level selection to block level retrieval. Compared with token level selection, block block level retrieval significantly reduces the number of candidates and lowers the overhead of top key computation and result merging. At the same time, block level retrieval is more hardware friendly friendly. It improves memory access efficiency and

**[8:10](https://www.youtube.com/watch?v=htod7Nv1cBc&t=490s)** increases the compute to memory access ratio. Importantly, we also show that the design does not introduce a significant performance drop. Finally, we design efficient kernels for both training and inference. I I I won't go into the kernel details here today, but this is the system level component that makes the sparse attention design practical and efficient. So, with this design, we were able to extend the training of our M3 model to 1 million context very efficiently. Um and as we talked about earlier, the

**[8:59](https://www.youtube.com/watch?v=htod7Nv1cBc&t=539s)** third pillar is the native multi-modality. Our model, Minimax M3, was trained from scratch with multi-modal data. What does that mean? Our model was trained with both text and vision understand standing from step zero, which is very different approach from current open weight models. Our starting point is very clear. At the current stage, a standalone VL model has relatively limited application scenarios. But combining it with with, you know, text understanding during the training can be challenging. So, the key question and challenge there was how can we introduce multimodal capability without hurting the core text performance? To answer this, we actually explored

**[9:47](https://www.youtube.com/watch?v=htod7Nv1cBc&t=587s)** several training strategies at scale. The first and most common approach is to add multimodal training after the pre-training decay stage, which is essentially a CPT style approach. However, at that point, the model has already largely converged. Adding multimodal data at this stage tends to interfere with the learned text capability and causes degradation. Another approach is to enter multimodal training before pre-training the decay stage. For example, after the model has already seen a number of amount of text tokens. We also tried this direction, but found that the results were highly sensitive to the data mixture and training hyper

**[10:34](https://www.youtube.com/watch?v=htod7Nv1cBc&t=634s)** parameters, such as learning rate, for example. In one setting, a smaller learning rate might reduce the performance drop, but this conclusion does not necessarily generalize to another run. More importantly, during large-scale pre-training, these parameters cannot be arbitrarily changed just for multimodal training. And this led us to our final strategy, native multimodal training from scratch. In this setting, multimodal capability is introduced from the very beginning rather than being added after the text model has already formed its structure. Under the same text token budget, we find that the this approach almost does not hurt text capability.

**[11:26](https://www.youtube.com/watch?v=htod7Nv1cBc&t=686s)** We actually did many fun analysis during these experiments. Um one of them is this interesting observation uh from the attention maps. You can see from this picture that for CPT-style multimodal models, the text tokens often pay very little attention to visual tokens. The visual token regions are mostly dark in the attention map. This suggests that the multimodalities are not fully integrated. Well, in contrast with native multimodal training, the attention map looks much more integrated. We do not see here a clear separation between text tokens and visual tokens. This suggests that the model learns to

**[12:14](https://www.youtube.com/watch?v=htod7Nv1cBc&t=734s)** fuse visual and textual information more naturally from the beginning. So, overall, our training strategy is not just about adding vision capability. It is about integrating multimodality into the model while preserving its strongest text capabilities. And of course, uh we did many experiments on multimodal architecture choices. Our overall architecture is relatively standard. The image or video is being processed by a ViT, which produces visual tokens. These visual tokens are then inserted into the language model input by re- replacing the original image placeholders in the text sequence.

**[13:02](https://www.youtube.com/watch?v=htod7Nv1cBc&t=782s)** After that, the visual embeddings and text embeddings are fed together into the language model. One important finding is that applying 3D attention inside the ViT is very helpful for vision understanding. In a standard ViT setting, attention is is applied within each individual image or frame. For video inputs, this means that visual patches from different frames do not directly interact at the ViT stage. But with 3D attention, patches across different frames can attend to each other directly. This gives the model stronger temporal and cross-frame visual modeling capability. And we found that this improves visual understanding, and the benefit also transfers to some image benchmarks.

**[13:52](https://www.youtube.com/watch?v=htod7Nv1cBc&t=832s)** Suggesting that it strengthens the overall visual representation rather than only improving video-specific tasks. And one practical detail is that we cannot simply extend 3D attention to an unlimited number of frames because that would introduce additional system and load balancing challenges. In our exploration, using four frames gave us the best best trade-off between performance and efficiency. So, overall, with our architecture design, with our training strategies that we explored throughout the stages, and with our analysis and ViT explorations, we were able to train the model from scratch with multimodality understanding.

**[14:41](https://www.youtube.com/watch?v=htod7Nv1cBc&t=881s)** And that would be the end of the presentation today. Thank you. >> [music]
