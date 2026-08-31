---
id: 85G_rQqU-Po
title: "Long Context Training and Inference on AMD GPUs"
slug: long-context-training-and-inference-on-amd-gpus
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 26
published_at: 2026-08-11T13:10:06Z
video_id: 85G_rQqU-Po
youtube_url: https://www.youtube.com/watch?v=85G_rQqU-Po
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Long Context Training and Inference on AMD GPUs

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `26 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=85G_rQqU-Po) · [Conference site](https://mlopsworld.com/)

## Description

Mehdi Rezagholizadeh, Principal Research Scientist, AMD

About the Speaker:
Mehdi Rezagholizadeh is a Principal Member of the Technical Committee at AMD. Before joining AMD, he was a Principal Research Scientist at Huawei Noah's Ark Lab Canada, where he worked since 2017 and served as the leader of the Canada NLP team for over six years. His research and projects focused on deep learning and its applications in NLP, computer vision (CV), and speech processing. He has contributed to advancements in generative adversarial networks, computational NLP, and efficient solutions for training, model architecture, and inference of pre-trained models.

Mehdi holds more than 15 patents and has authored over 50 publications in leading conferences and journals, including TACL, NeurIPS, AAAI, ACL, NAACL, EMNLP, EACL, Interspeech, and ICASSP. Additionally, he has actively contributed to the academic and industrial communities by organizing prominent workshops, such as the NeurIPS Efficient Natural Language and Speech Processing (ENLSP) workshops (2021–2024), and by serving on technical committees for ACL, EMNLP, NAACL, and EACL, including as Area Chair and Senior Area Chair for NAACL 2024. Over his career, he has successfully supervised more than 20 M.Sc. and Ph.D. interns in both industrial and academic settings.

He earned his B.Sc. in 2009 and M.Sc. in 2011 from the University of Tehran and completed his Ph.D. in 2016 at McGill University in Electrical and Computer Engineering (Centre for Intelligent Machines).

Abstract:
Long-context capabilities are becoming essential for modern LLM applications, from document understanding and agent workflows to code, RAG, and multi-step reasoning. But supporting long sequences efficiently is still one of the hardest practical challenges in large-scale model training and inference, especially when memory, bandwidth, and latency become the real bottlenecks rather than raw compute alone. In this talk, I will discuss the key systems and modeling considerations for long-context training and inference on AMD GPUs.

I will cover the main sources of cost in long-sequence workloads, including KV-cache growth, attention complexity, memory movement, parallelism strategies, and kernel efficiency. I will also discuss practical approaches to make long-context workloads feasible in production and research settings, including efficient attention variants, context extension strategies, distributed training design, cache optimization, precision choices, and inference-time serving trade-offs.

The talk is grounded in a practitioner-focused perspective: what actually matters when moving from promising ideas to stable, scalable implementations on AMD hardware. The goal is to provide a clear view of the design space and a practical roadmap for building efficient long-context systems on modern AMD GPU platforms.
