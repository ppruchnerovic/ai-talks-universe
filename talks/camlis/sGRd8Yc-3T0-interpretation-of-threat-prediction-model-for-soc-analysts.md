---
id: sGRd8Yc-3T0
title: "Interpretation of Threat Prediction Model for SOC Analysts"
slug: interpretation-of-threat-prediction-model-for-soc-analysts
conference: camlis
conference_name: "CAMLIS"
category: "Security conferences"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 29
published_at: 2018-11-16T17:37:58Z
video_id: sGRd8Yc-3T0
url: https://www.youtube.com/watch?v=sGRd8Yc-3T0
youtube_url: https://www.youtube.com/watch?v=sGRd8Yc-3T0
tags: ["camlis", "camlis2018"]
topics: ["Classic ML & data science", "Security, safety & red teaming"]
transcript: false
---

# Interpretation of Threat Prediction Model for SOC Analysts

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `29 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=sGRd8Yc-3T0) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Awalin Nabila SOPAN, FireEye
Interpretation of Threat Prediction Model for SOC Analysts (slides: https://www.camlis.org/awalin-nabila-sopan/)

In a security operations center or SOC, security analysts detect and triage time sensitive security alerts. One big challenge they face is the amount of false positive alerts from various data sources. Use of machine learning models to classify such alerts can reduce their workload; but for such mission-critical tasks we cannot solely depend on the ML, especially since there are always new types of attacks. To aid the analysts, we developed a system that classifies an alert into Malicious or Benign; and presents them the prediction along with an explanation. In this work, we demonstrate an ongoing effort to explain the machine learning model’s alert classification to SOC analysts using a model explanation visualization. While a human in the loop approach can help improve a model, most published work has focused on interpreting and visualizing the model features for data scientists; we focused on the analysts who triage alerts based on the alert data and the model’s prediction. Hence, we created a visualization of a model prediction to help analysts without overwhelming them.

Our analysts use a web based platform to investigate alerts triggered by some signature or indicator of compromise. They can view the raw data of the alert and pivot around various features before reaching the final decision (whether the alert is malicious or a benign one). Our UI component shows the analysts what our underlying machine learning model thinks of the alert and ‘Why’. It has three components:
1. The classification made by the model along with the prediction score.
2. The decision path: what features of the current alert are used by the model
3. The main features from al alerts used by the model.
If an alert is classified as malicious with high confidence, analysts can verify that by looking at the features presented in the UI and compare it with overall data set (the visualization of the data distribution for each matched condition). If they disagree with the model’s decision they can comment explaining the reason; the data scientists use that feedback to improve the model for future alerts and determine outliers. Thus the analysts can provide insight regarding the model without getting into the mathematical details. To keep the model explainable, we used a random forest model which uses a number of decision trees, and the features presented to the analysts are only the ones that are human.

We have received positive feedback and improvement suggestions from the SOC-analysts and threat researchers at our company. The prediction score gives them confidence in classifying the alert, and in the efficacy of new signatures. One public example can be seen here: https://twitter.com/danielhbohannon/status/956187804375142401’

This application is enabling our security analysts to get insight of how a machine learning model is making its prediction for alerts. To summarize, our main contributions are:
1. The visualization enabled analysts to get an overall picture of the entire dataset
2. Analysts can focus their attention to critical alerts
3. Analysts can add confidence to their decision, or perhaps question their logic if the model disagrees
