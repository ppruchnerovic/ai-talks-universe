---
id: iPKpxlZblBM
title: "TreeHuggr: Discovering where tree-based classifiers are vulnerable to adversarial attack"
slug: treehuggr-discovering-where-tree-based-classifiers-are
conference: camlis
conference_name: "CAMLIS"
category: "Security conferences"
edition: "CAMLIS"
year: 2018
speakers: []
channel: "CAMLIS"
duration_min: 27
published_at: 2018-11-16T17:49:42Z
video_id: iPKpxlZblBM
url: https://www.youtube.com/watch?v=iPKpxlZblBM
youtube_url: https://www.youtube.com/watch?v=iPKpxlZblBM
tags: ["camlis", "camlis2018"]
topics: ["Classic ML & data science", "Security, safety & red teaming"]
transcript: false
---

# TreeHuggr: Discovering where tree-based classifiers are vulnerable to adversarial attack

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `27 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=iPKpxlZblBM) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Bobby Filar, Endgame
TreeHuggr: Discovering where tree-based classifiers are vulnerable to adversarial attack (slides: https://www.camlis.org/bobby-filar/)

Tree-based classifiers like gradient-boosted decision trees (GBDTs) and random forests provide state-of-the-art performance in many information security tasks such as malware detection. Even while adversarial methods for evading deep learning classifiers abound,little research has been carried out against attacking tree-based classifiers due to models being non-differentiable, which significantly increases the cost of attacks. Research has shown attack transferability may be successful at evading tree-based classifiers, but those techniques do little to illuminate where models are brittle or weak.

We present TreeHuggr, an algorithm designed to analyze split points of each tree in an ensemble classifier to learn where a model might be most susceptible to an evasion attack. By determining where in the feature space there exists insufficient or conflicting evidence for a class label or where a decision boundary is wrinkled, we can not only better understand the attack space, but we can also more intuitively understand a model’s blind spots and increase interpretability. The key differentiator of TreeHuggr is a focus on the where the model is most susceptible, not in how to evade, given a starting point (a common tactic in adversarial examples).

This talk will provide an example-driven demonstration of TreeHuggr against the open-source EMBER dataset and malware model. We hope that TreeHuggr will highlight the potential defensive uses of adversarial research against tree-based classifiers and yield more insights into model interpretability and attack susceptibility.
