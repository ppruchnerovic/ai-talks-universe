---
id: 2dQ9hFXgz4U
title: "Evaluating large language models with Ray in hybrid cloud"
slug: evaluating-large-language-models-with-ray-in-hybrid-cloud
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "AI engineering & agents"
edition: "Anyscale"
year: 2023
speakers: []
channel: "Anyscale"
duration_min: 29
published_at: 2023-02-09T03:12:03Z
video_id: 2dQ9hFXgz4U
youtube_url: https://www.youtube.com/watch?v=2dQ9hFXgz4U
tags: []
transcript: false
---

# Evaluating large language models with Ray in hybrid cloud

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `29 min`

[Watch the recording](https://www.youtube.com/watch?v=2dQ9hFXgz4U) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Evaluating large language models with Ray in hybrid cloud at IBM

Evaluation of large-scale neural language models is crucial but also challenging. It requires models to be fine-tuned and evaluated on a large number of downstream tasks. Such downstream tasks can be very different in problem domain, type of input data, adoption pipeline, and running environment. Therefore, they are usually handled in different pipelines by different research teams. For example, one team might run a GLUE Benchmarking pipeline with 9 sub-tasks while another team might run a Sentiment Analysis pipeline with 17 sub-tasks. Such multi-task evaluation can be both time consuming (it can take a few days or even more) and hard to manage (across different teams and pipelines).

Therefore, a toolkit that can support a unified pipeline for multi-task with easy scaling and independent resource management is highly desirable in this domain. By adopting Ray into our pipeline, we achieved easier auto-scaling, better resource management, and unified workflows for different tasks. In this talk, we will walk through the problem and demonstrate how we run our large-scale language model evaluation pipeline in a hybrid cloud with auto-scaling, and cover some details on how Ray helps unify the workflow pipeline with easy code modifications to achieve auto-scaling, dependency management, and better overall performance.

This work is being developed as part of IBM's project CodeFlare.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
