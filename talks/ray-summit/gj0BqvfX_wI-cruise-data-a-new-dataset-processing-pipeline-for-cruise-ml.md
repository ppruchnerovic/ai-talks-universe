---
id: gj0BqvfX_wI
title: "Cruise.data - A new dataset processing pipeline for Cruise ML"
slug: cruise-data-a-new-dataset-processing-pipeline-for-cruise-ml
conference: ray-summit
conference_name: "Ray Summit (Anyscale)"
category: "Practitioner AI conferences"
edition: "Anyscale"
year: 2023
speakers: []
channel: "Anyscale"
duration_min: 31
published_at: 2023-02-09T03:05:14Z
video_id: gj0BqvfX_wI
url: https://www.youtube.com/watch?v=gj0BqvfX_wI
youtube_url: https://www.youtube.com/watch?v=gj0BqvfX_wI
tags: []
topics: []
transcript: false
---

# Cruise.data - A new dataset processing pipeline for Cruise ML

**Speaker not identified**

`Ray Summit (Anyscale)` · `Anyscale` · `2023` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=gj0BqvfX_wI) · [Conference site](https://www.anyscale.com/ray-summit/2026)

## Description

Cruise.data - A new dataset processing pipeline for Cruise ML

At Cruise, we rely on custom data pre-processing before feeding data into ML models. In many cases ML engineers prefer to develop data pre-processing as part of their ML training code, making quick iterations and debugging much easier. This puts high pressure on performance and reliability of data pre-processing, because we need to make sure that by the time an ML model is ready to accept a next mini-batch of data, it is already available. Otherwise we will be wasting GPU time. Some of these data transformations could have run offline and cached, but there is no existing system available which would make it easy to move the logic between training and offline batch data processing jobs. Moreover, the memory usage of the data processing pipeline is a large consideration for us due to the use of high resolution sensors our cars have. In this talk, we will share our progress on building a new ML data pre-processing framework, Cruise.Data, and how Ray helps us to scale it. Cruise.Data is a novel system which combines best properties of tf.data, the PyTorch ecosystem, and large-scale data processing frameworks.

See all Ray Summit content @ http://anyscale.com/ray-summit-2022
