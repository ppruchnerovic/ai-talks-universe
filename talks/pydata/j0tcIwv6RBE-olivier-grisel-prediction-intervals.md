---
id: j0tcIwv6RBE
title: "Olivier Grisel - Prediction intervals"
slug: olivier-grisel-prediction-intervals
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2025
speakers: ["Olivier Grisel"]
channel: null
duration_min: 34
published_at: 2025-11-21T16:25:33Z
video_id: j0tcIwv6RBE
youtube_url: https://www.youtube.com/watch?v=j0tcIwv6RBE
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Olivier Grisel - Prediction intervals

**Olivier Grisel**

`PyData` · `PyData` · `2025` · `34 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=j0tcIwv6RBE) · [Conference site](https://pydata.org/)

## Description

Most common machine learning models (linear, tree-based or neural network-based), optimize for the least squares loss when trained for regression tasks. As a result, they output a point estimate of the conditional expected value of the target: `E[y|X]`.

In this presentation, we will explore several ways to train and evaluate probabilistic regression models as a richer alternative to point estimates. Those models predict a richer description of the full distribution of `y|X` and allow us to quantify the predictive uncertainty for individual predictions.

On the model training part, we will introduce the following options:

- ensemble of quantile regressors for a grid of quantile levels (using linear models or gradient boosted trees in scikit-learn, XGBoost and PyTorch),
- how to reduce probabilistic regression to multi-class classification + a cumulative sum of the `predict_proba` output to recover a continuous conditional CDF.
- how to implement this approach as a generic scikit-learn meta-estimator;
- how this approach is used to pretrain foundational tabular models (e.g. TabPFNv2).
- simple Bayesian models (e.g. Bayesian Ridge and Gaussian Processes);
- more specialized approaches as implemented in XGBoostLSS.

We will also discuss how to evaluate probabilistic predictions via:

- the pinball loss of quantile regressors,
- other strictly proper scoring rules such as Continuous Ranked Probability Score (CRPS),
- coverage measures and width of prediction intervals,
- reliability diagrams for different quantile levels.

We will illustrate of those concepts with concrete examples and running code.

Finally, we will illustrate why some applications need such calibrated probabilistic predictions:

- estimating uncertainty in trip times depending on traffic conditions to help a human decision make choose among various travel plan options.
- modeling value at risk for investment decisions,
- assessing the impact of missing variables for an ML model trained to work in degraded mode,
- Bayesian optimization for operational parameters of industrial machines from little/costly observations.

If time allows, will also discuss usage and limitations of Conformal Quantile Regressors as implemented in MAPIE and contrast aleatoric vs epistemic uncertainty captured by those models.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
