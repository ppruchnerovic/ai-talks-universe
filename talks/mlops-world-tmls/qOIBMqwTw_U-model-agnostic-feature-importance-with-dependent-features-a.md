---
id: qOIBMqwTw_U
title: "Model-Agnostic Feature Importance with Dependent Features: A Conditional Subgroup Approach"
slug: model-agnostic-feature-importance-with-dependent-features-a
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2026
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 27
published_at: 2026-08-11T13:09:26Z
video_id: qOIBMqwTw_U
youtube_url: https://www.youtube.com/watch?v=qOIBMqwTw_U
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
transcript: false
---

# Model-Agnostic Feature Importance with Dependent Features: A Conditional Subgroup Approach

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2026` · `27 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=qOIBMqwTw_U) · [Conference site](https://mlopsworld.com/)

## Description

Javeria Ahmed, Senior Manager, Retail Risk Modelling, Royal Bank of Canada (RBC)
Vathy Kamulete, Director, Retail Risk Modelling, Royal Bank of Canada (RBC)

About the Speakers:
Javeria Ahmed is a Senior Manager at RBC working on Retail Risk Models with a background in Computational & Applied Math with 4+ years of experience in the financial services sector. Javeria has led projects and models focusing on the intersection of risk modelling and the automotive industry and is particularly passionate about auto shopping behavior, dealer gaming and fraud and their impact in the viability of risk models.

Vathy Kamulete is a Director in Retail Risk Modelling at RBC with a background in statistics and economics and extensive experience in model risk management and machine learning. Prior to joining Retail Risk Modelling as a Director, Vathy spent more than four years in Enterprise Model Risk Management, where he supported the validation and governance of AI and machine learning models. His interests include Bayesian methods, model risk, explainable AI, and the responsible application of advanced analytics to business problems.

Abstract:
Feature importance estimation is crucial for model interpretability, but traditional permutation-based methods break down when features exhibit dependencies. Standard permutation importance shuffles features independently, creating out-of-distribution samples that don't reflect realistic data relationships—leading to unreliable and often misleading importance scores. As warned by Hooker et al. (2021), unrestricted permutation forces extrapolation.

This talk introduces a conditional subgroup approach for computing model-agnostic feature importance that respects feature dependencies through row and column blocking strategies. The method combines two complementary Model-X techniques that model the joint feature distribution:

1. Conditional Imputation: Using Gaussian Copula and other statistical models to replace masked features while preserving the joint feature distribution, avoiding impossible feature combinations.

2. Restricted Permutations: Partitioning samples into blocks using Random Trees Embedding, then permuting features only within similar samples to maintain local feature dependencies.

The approach uses Fraction of Variance Unexplained (FVU) as a variance-based sensitivity measure with well-defined bounds [0,1], making it comparable across problems. Unlike SHAP or standard permutation importance, this method correctly handles multicollinear features without requiring model retraining or manual feature dropping."""
