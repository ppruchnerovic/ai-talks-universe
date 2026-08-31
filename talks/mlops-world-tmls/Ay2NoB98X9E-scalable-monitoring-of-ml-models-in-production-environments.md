---
id: Ay2NoB98X9E
title: "Scalable monitoring of ML models in production environments"
slug: scalable-monitoring-of-ml-models-in-production-environments
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2021
speakers: []
channel: null
duration_min: 49
published_at: 2021-06-24T16:00:10Z
video_id: Ay2NoB98X9E
youtube_url: https://www.youtube.com/watch?v=Ay2NoB98X9E
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education", "Scalable monitoring of ML models in production environments", "Ira Cohen", "ml models", "production environments", "production", "algorithm", "machine learning algorithms", "machine learning algorithms explained", "machine learning tutorial"]
transcript: false
---

# Scalable monitoring of ML models in production environments

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2021` · `49 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education` `#Scalable monitoring of ML models in production environments` `#Ira Cohen` `#ml models` `#production environments` `#production` `#algorithm` `#machine learning algorithms` `#machine learning algorithms explained` `#machine learning tutorial`

[Watch the recording](https://www.youtube.com/watch?v=Ay2NoB98X9E) · [Conference site](https://mlopsworld.com/)

## Description

💻 Abstract:
Many things can cause models to underperform: model staleness, problems with pipelines creating the input features, “attacks” on the models, and more. In many cases, performance measures that may indicate issues with the models are not directly their accuracy (which is usually attainable with a delay), but rather auxiliary measures that should have a stable behavior over time - thus abnormal changes in them indicate a potential issue that should be investigated.
For example, classifiers are often used to predict if a customer will churn or not. Churn models have inputs that are computed from multiple sources - for example, counts of support calls from the support system, usage patterns measured from web/app analytics systems, and more. If one of the sources has issues in reporting their data, the input features to the churn model may be wrong, leading to a change in model quality. By monitoring the output distribution of the churn prediction models, and input feature distributions, such cases can be detected as they will cause an abnormal change in those distributions. In the talk, I will describe a scalable methodology to monitor machine learning in production: an open-source agent for generating key performance measures of ML models that are analyzed using machine learning algorithms (anomaly detection) to detect issues with the monitored models. I’ll describe important performance measures that should be extracted for various types of machine learning models, show how anomalies help discover issues with these models and demonstrate how it works on real data. I will also present an open-source monitoring agent we released for any python based ML framework that automatically generates a lot of the proposed model performance measures, so data science teams can track them and get alerted on issues in production that require their attention.

🔊 Speaker bio:
Co-Founder, Chief Data Scientist, and VP Fish care of Anodot
Ira Cohen is the chief data scientist at Anodot, working on learning algorithms for analyzing time-series signals at a large scale - from anomaly detection, clustering and forecasting. Prior to Anodot, Ira was Chief Data Scientist at HP Software, defining and developing advanced data analytics & big data initiatives.
Before that Ira was a senior researcher at HP Labs, leading R&D in machine learning and data mining for analyzing large-scale event streams. He is the author of numerous patents and publications and holds a Ph.D. in Electrical and Computer Engineering from the University of Illinois at Urbana Champaign.

If you enjoyed this talk, visit us at https://mlopsworld.com/ and come participate in our next gathering! 💼

Would you like to receive email summaries of these talks? Join our newsletter FREE here: http://bit.ly/MLOps_Summaries 📧

Timestamps:

0:00 Intro
0:11 Introduction of the host
0:34 Introduction of Ira Cohen
1:51 Different products that use machine learning
2:40 The machine learning development process
4:53 What can go wrong in production
11:14 Solution: Monitoring and Tracking for Unexpected Changes
12:31 Step 1: Collect the Input/output of the Models
13:47 Step 2 - Create Metrics: Measure Stats Over Time
16:02 MLwatcher: Open source Python ML monitoring agent
17:42 Step 3 - Monitor the metrics for unexpected changes
18:07 But dashboards do not scale
19:06 Solution: Automated anomaly detection at scale
20:41 Example: A digital classifier gone wild
23:58 MLwatcher + Automated anomaly detection
25:09 Monitoring Anodot's Anomaly Detection models
30:27 Conclusion

❓ Q&A ❓

32:20 Is the tool open source?
33:24 Could you please explain what is the input feature distribution plot showing?
35:11 How does this compare to AWS sagemaker model monitor?
36:51 Does this only work with sklearn models?
38:07 Which type of business you are working with?
39:09 What does traditional DevOps mean to Model Monitoring?
41:28 Can the tool do monitoring in real-time?
42:14 What are your thoughts around statistical operations that can be applied to compare data input and output distributions?
43:02 What was the driving force behind building MLWatcher at Anodot? Was it solving an internal use case you had?
46:26 Do you also look at the penultimate layer feature outputs or just only on the input distribution?

48:04 Closing remarks
