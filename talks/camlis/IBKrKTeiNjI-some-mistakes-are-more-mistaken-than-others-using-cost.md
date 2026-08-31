---
id: IBKrKTeiNjI
title: "Some Mistakes are More Mistaken Than Others: Using Cost-Matrix Clustering to Address Misclassificati"
slug: some-mistakes-are-more-mistaken-than-others-using-cost
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 30
published_at: 2018-11-16T17:40:55Z
video_id: IBKrKTeiNjI
youtube_url: https://www.youtube.com/watch?v=IBKrKTeiNjI
tags: ["camlis", "camlis2018"]
transcript: false
---

# Some Mistakes are More Mistaken Than Others: Using Cost-Matrix Clustering to Address Misclassificati

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `30 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=IBKrKTeiNjI) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Cody Wild, Sophos
Some Mistakes are More Mistaken Than Others: Using Cost-Matrix Clustering to Address Misclassification Cost Asymmetries in Website Content Classification (slides: https://www.camlis.org/cody-wild/)

Website content classification has several salient characteristics as a machine learning problem, but perhaps the most salient is that it is a multi-class classification problem with nonuniform and asymmetric misclassification costs. Misclassifying a news site as a business site is a much less serious error than misclassifying a pornographic site as children’s entertainment, and we would like our model’s training objective to reflect that. However, because categorical cross-entropy loss - the standard for neural network models - works by simply increasing the log-probability of the true class, rather than directly penalizing incorrect classes, it offers no straightforward mathematical way to incorporate misclassification costs as loss weights .

This talk will review existing methodology for incorporating misclassification costs into models, and also propose a novel approach called CCAL: Cost Cluster Auxiliary Losses. This method clusters output classes into groups of mutually low misclassification cost, and then trains the model using the cross-entropy loss on the fully granular category classes, as well as cross-entropy loss against the courser group labels, at multiple levels of granularity. The intuition behind CCAL is that these auxiliary losses implicitly give the model information about which mistakes are worse than others by giving some positive gradient weight to misclassifications that are still in the same supercluster, and do so in a way that is easier to tune because all auxiliary losses are in the form of cross-entropy, rather a poorly scaled mix of linear and cross-entropy losses, as in Resheff et al’s bilinear approach. The talk will conclude by discussing cost structures where one would expect CCAL to perform well or poorly, and examine whether it can be effectively used as a form of curriculum learning.
