---
id: 1tB7lALJ3ew
title: "A feature presentation: semi-supervised learning of file representations"
slug: a-feature-presentation-semi-supervised-learning-of-file
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 27
published_at: 2018-11-16T17:06:24Z
video_id: 1tB7lALJ3ew
youtube_url: https://www.youtube.com/watch?v=1tB7lALJ3ew
tags: ["camlis", "camlis2018"]
transcript: false
---

# A feature presentation: semi-supervised learning of file representations

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `27 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=1tB7lALJ3ew) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Hyrum Anderson, Endgame
A feature presentation: semi-supervised learning of file representations (slides: https://www.camlis.org/hyrum-anderson/)

Much of the success of machine learning malware classifiers depends on a meaningful representation of file features. In fact, unlike applications such as machine vision and machine translation in which “featureless” end-to-end deep learning achieves state of the art performance, static malware machine learning is still dominated by hand-crafted features wherein specific discriminative domain knowledge can be codified manually that is not inferred automatically via end-to-end deep learning. However, recent advances in end-to-end deep learning for malware classification offer ever-improving success rates, the hope of parser-less file classification, and glimpses of discovering truly malicious or benign content in a file byte sequence. In either case, representation is key.

This talk considers the following problem setup. One wishes to learn a feature representation from both labeled and abundantly unlabeled Windows portable executable (PE) files (although the techniques presented are broadly applicable to other formats). It is desirable that the features not only enable classification performance approaching that of fully discriminative networks, but also encapsulate semantically meaningful file characteristics by which one can measure file similarity to functionally similar malware samples, for example.

I will present and compare several novel and yet-unpublished approaches to semi-supervised learning of PE file representations. First, I present unsupervised learning of file features from raw bytes by solving a file chunk reordering problem, akin to solving a jigsaw puzzle (previously applied to images). I will demonstrate how this promising approach, however, is not able to learn desired invariances. Next, I present a semi-supervised deep learning approach that explicitly learns meaningful invariances and leverages a novel neural architecture I call a softmax forest for performing a self-taught learning task for binary files, and show how this approach is superior to commonly used metric learning frameworks. Finally, I compare these to an unsupervised feature representation approach I term a variational equivalence encoder (VEE) that uses variational principles to learn invariances. This latter framework can be viewed as modification of a standard variational auto-encoder (VAE). I'll compare these approaches to the baseline EMBER model for classification and EMBER features for similarity search.
