---
id: HRo90WL4Znc
title: "Alpa - Simple large model training and inference on Ray"
slug: alpa-simple-large-model-training-and-inference-on-ray
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2023-02-09T01:57:28Z
video_id: HRo90WL4Znc
url: https://www.youtube.com/watch?v=HRo90WL4Znc
youtube_url: https://www.youtube.com/watch?v=HRo90WL4Znc
tags: []
transcript: false
---

# Alpa - Simple large model training and inference on Ray

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=HRo90WL4Znc) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Alpa - Simple large model training and inference on Ray

Alpa is a Ray-native library built for automatically training and serving large models (e.g., GPT-3). Alpa automates model-parallel training of large deep learning (DL) models by generating execution plans that unify data, operator, and pipeline parallelism. Existing model-parallel training systems either require users to manually create a parallelization plan or automatically generate one from a limited space of model parallelism configurations, which does not suffice to scale out complex DL models on distributed compute devices. Alpa distributes the training of large DL models by viewing parallelisms as two hierarchical levels: inter-operator and intra-operator parallelisms. Based on this, Alpa constructs a new hierarchical space for massive model-parallel execution plans. Alpa designs a number of compilation passes to automatically derive the optimal parallel execution plan in each independent parallelism level and implements an efficient runtime to orchestrate the two-level parallel execution on distributed compute devices. Our evaluation shows Alpa generates parallelization plans that match or outperform hand-tuned model-parallel training systems even on models they are designed for. Unlike specialized systems, Alpa also generalizes to models with heterogeneous architectures and models without manually designed plans. In this talk, we will focus on both the algorithm side and also the engineering/system implementation side, where Ray is a crucial building block of the Alpa runtime.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
