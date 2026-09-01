---
id: pTvcnyTIgPI
title: "A Modular Multimodal LLM Framework for Disease Prediction"
slug: a-modular-multimodal-llm-framework-for-disease-prediction
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2025
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 18
published_at: 2025-07-27T08:44:33Z
video_id: pTvcnyTIgPI
url: https://www.youtube.com/watch?v=pTvcnyTIgPI
youtube_url: https://www.youtube.com/watch?v=pTvcnyTIgPI
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# A Modular Multimodal LLM Framework for Disease Prediction

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2025` · `18 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=pTvcnyTIgPI) · [Conference site](https://mlopsworld.com/)

## Description

Hanieh Arjmand, Senior ML Researcher, Lydia.ai

About the Speaker:
Hanieh Arjmand is a Senior Machine Learning Researcher at Lydia.ai, where she designs and implements advanced machine learning models to tackle complex challenges in healthcare and insurance. She holds a PhD in Biomedical Engineering from the University of Toronto and brings deep expertise in applying AI to biomedical and health data. Throughout her academic and professional career, Hanieh has led diverse, data-driven research initiatives that drive innovation, support better clinical decision-making, and improve health outcomes.

Abstract:
This talk introduces a novel multimodal framework for disease prediction that integrates structured Electronic Health Records (EHR) and wearable time series data into a unified embedding space optimised for interpretation by Large Language Models (LLMs). While multimodal LLMs have shown promise in vision, audio, and text, applying them to healthcare presents unique challenges, including temporal dynamics, heterogeneous formats, and the need for clinical interpretability.
To address this, the system uses modality-specific encoders to transform each input stream into compact latent representations. These are integrated into a shared embedding space, allowing the LLM to reason jointly across modalities. By training the entire system end to end, including the LLM itself, the model learns rich, context-aware representations that link current behavioural signals to broader clinical trajectories. The architecture also supports auxiliary context, such as demographics or prompt instructions, embedded directly into the LLM’s input space, enabling dynamic adaptation to specific tasks or patient profiles.
Evaluation on UK Biobank data (n ≈ 70K) shows that the system outperforms single-modality baselines and that wearable data meaningfully influence predictions when integrated with EHR (correlation r = 0.771). While demonstrated on two modalities, the framework is inherently modular and can be extended to include additional data sources, such as nutrition or imaging, by introducing corresponding encoders.
This work illustrates how LLMs can evolve into adaptive, multimodal engines for real-time, patient-centric care, capable of synthesising diverse health data to support earlier interventions, continuous monitoring, and personalised clinical decision-making.
"
