---
id: iAR0NmyS68k
title: "Niek Tax - Practical Multicalibration with MCGrad | Pydata London 26"
slug: niek-tax-practical-multicalibration-with-mcgrad-pydata
conference: pydata
conference_name: "PyData"
category: "AI engineering & agents"
edition: "PyData"
year: 2026
speakers: ["Niek Tax"]
channel: "PyData"
duration_min: 83
published_at: 2026-06-15T15:55:38Z
video_id: iAR0NmyS68k
youtube_url: https://www.youtube.com/watch?v=iAR0NmyS68k
tags: ["Python", "Tutorial", "Education", "NumFOCUS", "PyData", "Opensource", "learn", "software", "python 3", "Julia", "coding", "learn to code", "how to program", "scientific programming"]
transcript: false
---

# Niek Tax - Practical Multicalibration with MCGrad | Pydata London 26

**Niek Tax**

`PyData` · `PyData` · `2026` · `83 min`

`#Python` `#Tutorial` `#Education` `#NumFOCUS` `#PyData` `#Opensource` `#learn` `#software` `#python 3` `#Julia` `#coding` `#learn to code` `#how to program` `#scientific programming`

[Watch the recording](https://www.youtube.com/watch?v=iAR0NmyS68k) · [Conference site](https://pydata.org/)

## Description

Niek Tax - Beyond ML Model Calibration: Hands-On Multicalibration with MCGrad

This session’s header image
Your model is well-calibrated on average, but is it calibrated for every subgroup of your users? In this hands-on tutorial you will learn what multicalibration is, why standard calibration methods leave systematic errors hidden in subpopulations, why this matters for ML models in production, and how to fix it in a few lines of code using MCGrad, an open-source Python library that has been battle-tested on hundreds of production models at a large tech company. Attendees will leave with a working notebook they can immediately apply to their own projects.

A globally well-calibrated model can still be systematically overconfident for one subgroup and underconfident for another, these errors cancel out in aggregate, passing standard checks while silently degrading decisions for specific populations. Multicalibration fixes this by ensuring predictions are calibrated across all subgroups simultaneously, while improving other notions of model performance.

This tutorial introduces multicalibration from scratch using MCGrad, an open-source library (pip install mcgrad) that has been deployed on hundreds of production ML models at a major tech company, and the methodology was recently accepted at KDD 2026. Attendees train a classifier on a public dataset, discover hidden subgroup miscalibration, then fix it with MCGrad in a few lines of code, all inside a ready-to-run Colab notebook. We also cover hyperparameter tuning, safety mechanisms, and when not to apply multicalibration.

OUTLINE:
- Welcome & Setup (5 min)
Goals, format, open Colab notebook, pip install mcgrad.
- The Calibration Gap (15 min)
What is calibration? And why should ML practitioners care about it? Train a logistic regression on the dataset. Apply isotonic regression -- global calibration looks perfect. Reveal: the model is still badly miscalibrated for specific subgroups.
- From Calibration to Multicalibration (15 min)
Define multicalibration and the MCE metric. Why practitioners need it: you rarely know which subgroups matter in advance. Deployment lessons from a major tech company (hundreds of production models).
- MCGrad in Action -- Hands-On (30 min)
Walk through the MCGrad API (fit/predict). Fit MCGrad on the dataset, inspect the learning curve, compare base model vs. isotonic regression vs. MCGrad. Visualise segment-level error reduction. Mini-exercise: change segment features, observe impact on MCE.
- Advanced Features & Production Tips (15 min)
Hyperparameter tuning, safety mechanisms (no-op failsafe), regression multicalibration, model serialization, when not to use multicalibration.
- Wrap-Up & Q&A (10 min)
Recap the three-step workflow (measure MCE, fit MCGrad, verify). Pointers to docs and tutorials. Open Q&A.

Attendees leave with a working notebook, a new metric multicalibration error (MCE) for auditing their own models, and a pip-installable tool to act on the results.

www.pydata.org

PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.

PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.

00:00 Welcome!
00:10 Help us add time stamps or captions to this video! See the description for details.

Want to help add timestamps to our YouTube videos to help with discoverability? Find out more here: https://github.com/numfocus/YouTubeVideoTimestamps
