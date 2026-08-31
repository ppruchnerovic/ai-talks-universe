---
id: ZmutSk8jLv8
title: "Estimating uncertainty for binary classifiers"
slug: estimating-uncertainty-for-binary-classifiers
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: "CAMLIS"
duration_min: 31
published_at: 2018-11-16T17:48:15Z
video_id: ZmutSk8jLv8
youtube_url: https://www.youtube.com/watch?v=ZmutSk8jLv8
tags: ["camlis", "camlis2018"]
transcript: false
---

# Estimating uncertainty for binary classifiers

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `31 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=ZmutSk8jLv8) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Richard Harang, Sophos
Estimating uncertainty for binary classifiers (slides: https://www.camlis.org/richard-harang/)

In practical applications of binary classification, knowing the uncertainty of the prediction can be almost as important as knowing the most likely prediction. In the case of responses given in a 0-1 range, the distance from one extreme or the other is often taken as a proxy for the certainty (or uncertainty) of the classification. While for the specific case of the binary cross-entropy loss under rarely-obtained conditions this estimate of uncertainty is correct in the narrowly defined sense that it asymptotically attains the posterior conditional probability of the label being in the ‘positive’ class, the general approach of using the output score of the classifier does not typically yield a faithful estimate of uncertainty in the above sense. Furthermore, in the finite-data case, and especially with complex modern classifiers that apply complex transformation, partitions, or both to the input space, the score itself is subject to a significant degree of uncertainty that is frequently difficult to characterize precisely. Thus, even if we accept the score as a proxy for uncertainty, we may be uncertain about how accurate this measurement of uncertainty is!
In simpler classifiers, direct estimation of this uncertainty can be performed by examining the support of a test point within the training data. However in many areas of security data science, the size of the input space to classifiers can be quite large and so the curse of dimensionality can make it difficult to identify the support of an example within the training data. Even when this difficulty can be overcome, the complex relationships between these inputs that most modern classifiers can learn and exploit to obtain their high performance means that areas of high or low support in the input space may not be so well (or poorly) supported within the transformed space within which the classifier is effectively making its prediction. Variational methods have been proposed to estimate uncertainty in deep neural networks regularized via dropout, however this comes at a significant computational cost. Finally, multi-half-space classifiers for deep neural networks have been proposed that attempt to learn the density of the training data as represented by the final layer of the network; while this approach incurs a relatively modest computational burden, we find empirically that the better a given network does at separating the data in the final pre-classification layer, the worse this method performs at estimating the training data’s distribution.
In this talk, we examine this problem from the perspective of Bayesian approximation, and show how using deep neural networks as approximating functions for parameters of a hierarchical Bayesian model can lead to uncertainty estimates for models that are robust, do not fail when the model is “too good”, require comparatively little additional computation to obtain, and can in most cases be directly converted into a maximum a posteriori estimate ‘score’ for the network.
