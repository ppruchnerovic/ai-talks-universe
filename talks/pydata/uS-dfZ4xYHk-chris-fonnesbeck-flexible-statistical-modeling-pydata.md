---
id: uS-dfZ4xYHk
title: "Chris Fonnesbeck - Flexible Statistical Modeling | Pydata London 26"
slug: chris-fonnesbeck-flexible-statistical-modeling-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Chris Fonnesbeck", "Flexible Statistical Modeling"]
channel: null
duration_min: 87
published_at: 2026-06-15T15:55:38Z
video_id: uS-dfZ4xYHk
youtube_url: https://www.youtube.com/watch?v=uS-dfZ4xYHk
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Chris Fonnesbeck - Flexible Statistical Modeling | Pydata London 26

**Chris Fonnesbeck, Flexible Statistical Modeling**

`PyData` · `PyData` · `2026` · `87 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=uS-dfZ4xYHk) · [Conference site](https://pydata.org/)

## Description

Chris Fonnesbeck - Flexible Statistical Modeling with Bayesian Additive Regression Trees

Most machine learning methods give you a prediction but not a measure of how much to trust it. Bayesian Additive Regression Trees (BART) combine the flexibility of tree ensembles (e.g. random forests, boosting) with full uncertainty quantification—every prediction comes with a probability interval, not just a point estimate. This hands-on tutorial introduces BART for regression and classification. Using pymc-bart, participants will learn to fit flexible models that automatically capture non-linear relationships while providing honest uncertainty estimates. We emphasize practical interpretation throughout: visualizing predictions with uncertainty bands, understanding variable importance, and interpreting model output.

Machine learning models are often evaluated on predictive accuracy alone, but accuracy without uncertainty can be misleading. Classical tree ensemble methods like random forests and gradient boosting provide point predictions, and while techniques like conformal inference or bootstrap aggregation can add uncertainty estimates, these are often poorly calibrated or computationally expensive.

Bayesian Additive Regression Trees (BART) offer a different approach: uncertainty quantification is built into the model, not ignored or bolted on afterward. BART models the response as a sum of small trees, with regularization priors that keep each tree weak. Posterior inference over the tree structures yields a full distribution over predictions—every fitted value comes with a credible interval that reflects genuine uncertainty about the underlying function.

This tutorial introduces BART through three applications, each demonstrating how uncertainty changes the way we interpret results:

Regression: We begin with continuous outcomes, fitting BART models and visualizing posterior predictive distributions. Rather than a single fitted curve, participants will see HDI bands that widen where data is sparse and narrow where evidence is strong. We'll explore variable importance—which comes with its own uncertainty—and partial dependence plots that reveal non-linear effects.

Classification: For binary outcomes, BART produces predicted probabilities with uncertainty, not just class labels. We'll examine how this uncertainty propagates through decision-making and compare calibration against standard classifiers.

Target audience
Data scientists and analysts looking to add useful statistical methods to their toolkit.

Takeaways
Participants will leave able to fit BART models for continuous, binary, and time-to-event outcomes; interpret predictions with full posterior uncertainty; use variable importance and partial dependence plots appropriately; and decide when BART's uncertainty quantification justifies its computational cost over simpler alternatives.

Materials
GitHub repository with marimo notebooks, real-world datasets from sports, psychology, and other domains, environment files, and a one-page BART reference guide. Participants should clone the repository and verify their setup before the session.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
