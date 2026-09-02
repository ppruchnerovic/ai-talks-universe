---
id: ZhoIUMJke_w
title: "Democratization of ML Pipelines and Bringing ML Workflows to Heterogeneous... Yihong Wang & Tommy Li"
slug: democratization-of-ml-pipelines-and-bringing-ml-workflows
conference: lf-ai-dev
conference_name: "AI_dev / Open Source Summit (Linux Foundation)"
category: "Software dev with AI tracks"
edition: "AI.dev 2023"
year: 2023
speakers: []
channel: "The Linux Foundation"
duration_min: 36
published_at: 2023-12-18T18:32:27Z
video_id: ZhoIUMJke_w
url: https://www.youtube.com/watch?v=ZhoIUMJke_w
youtube_url: https://www.youtube.com/watch?v=ZhoIUMJke_w
tags: []
topics: ["Data engineering & MLOps"]
transcript: false
---

# Democratization of ML Pipelines and Bringing ML Workflows to Heterogeneous... Yihong Wang & Tommy Li

**Speaker not identified**

`AI_dev / Open Source Summit (Linux Foundation)` · `AI.dev 2023` · `2023` · `36 min`

[Watch the recording](https://www.youtube.com/watch?v=ZhoIUMJke_w) · [Conference site](https://events.linuxfoundation.org/ai-dev-europe/)

## Description

Democratization of ML Pipelines and Bringing ML Workflows to Heterogeneous Cloud Native ML Platforms - Yihong Wang & Tommy Li, IBM

In Kubeflow Pipelines(KFP) v1, the pipeline spec describing ML flow is platform-dependent, which makes it impossible to bring your ML flows to other pipeline frameworks. To lower the barrier, Intermediate Representation(IR) is available in KFP v2. It's a generic component/step-oriented specification that fits container orchestration frameworks. More importantly, a new pipeline orchestration engine is created on the backend to support automatic lineage tracking and components that consume or produce metadata. In light of these new features, it gets a foot into ML pipeline portability. Porting fundamental components allows you to run your pipelines on the desired platforms. Besides, IR is used in the Kubeflow pipeline registry protocol as the format of pipeline templates. Currently, IR specification is in a stable version and used by Kubeflow Pipelines, Google Vertex AI, and Kubeflow Pipelines with Tekton. In this talk, we walk through the new IR spec, a list of components that constitute the new pipeline orchestration engine, how we adapt the new features in another pipeline framework, and use the new registry protocol to democratize the ML pipeline development.
