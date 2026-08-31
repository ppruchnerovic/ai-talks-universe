---
id: qHuUx-xbMYE
title: "Automated Pipeline for Large-Scale Neural Network Training and Inference"
slug: automated-pipeline-for-large-scale-neural-network-training
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "AI engineering & agents"
edition: "MLOps World / TMLS"
year: 2021
speakers: []
channel: "Toronto Machine Learning Society (TMLS)"
duration_min: 46
published_at: 2021-07-07T16:00:21Z
video_id: qHuUx-xbMYE
youtube_url: https://www.youtube.com/watch?v=qHuUx-xbMYE
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education", "Automated Pipeline for Large-Scale Neural Network Training and Inference", "Ebrahim Safavi", "Jisheng Wang", "Automated Pipeline", "devops", "automation", "data scientist", "automated", "machine learning tutorial"]
transcript: false
---

# Automated Pipeline for Large-Scale Neural Network Training and Inference

**Speaker not identified**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2021` · `46 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education` `#Automated Pipeline for Large-Scale Neural Network Training and Inference` `#Ebrahim Safavi` `#Jisheng Wang` `#Automated Pipeline` `#devops` `#automation` `#data scientist` `#automated` `#machine learning tutorial`

[Watch the recording](https://www.youtube.com/watch?v=qHuUx-xbMYE) · [Conference site](https://mlopsworld.com/)

## Description

💻 Abstract:
Anomaly detection models are essential to run data-driven businesses intelligently. In order to manage tens of thousands of anomaly detection models at Mist, we have built a cloud-native and scalable ML training pipeline which automates all steps of ML operations including data collection, model training, model validation, model deployment, and version control. The inference workflow is decoupled from the training process to increase agility and minimize the delay of model service. Motivated by the recent impressive performance of recurrent neural networks (RNNs) on a wide spectrum of tasks, we have developed confident deep bidirectional long-short term memory (BiLSTM) models which leverage a large amount of data across numerous dimensions to capture trends and catch anomalies across thousands of Wifi networks and address issues in real-time. The proposed BiLSTM models are capable of predicting the uncertainty of their detection which is essential for the anomaly detection purpose. In addition, to address the challenges imposed by the stochastic nature of unsupervised anomaly detection on the workflow pipeline, we have developed novel statistical models for the training workflow to leverage historical data and automate model validation, deployment, and version control. The anomaly detection service happens hourly and the training jobs occur weekly through the pipeline which consists of different steps including managing the training and serving data stream, model versioning for predictions, training and serving for each network’s model. The workflow pipeline utilizes different technologies including Secor service, Amazon S3 service, Apache Spark across Amazon EMR cluster, Apache Kafka, and Elasticsearch. In this talk, we first briefly discuss the details of the unsupervised confident deep multivariate models we have built to automatically detect WiFi network issues. Then, we dive deeper into the details of our cloud-based pipeline and how we use relative entropy to automate the training workflow. Finally, we share lessons learned and insights specifically, how to productize and monitor thousands of ML models to automate anomaly detection.

🔊🔊 Speakers:
Ebrahim Safavi - Senior Data Scientist, Mist, a Juniper company

Jisheng Wang - Senior Director of Data Science, Mist, a Juniper company

If you enjoyed this talk, visit us at https://mlopsworld.com/ and come participate in our next gathering! 💼

Would you like to receive email summaries of these talks? Join our newsletter FREE here: http://bit.ly/MLOps_Summaries 📧

Timestamps:

0:00 Intro
0:10 Introduction of the speakers
2:43 The business problem we're trying to solve
5:28 What could possibly go wrong end-to-end?
6:50 Data funnel - From inputs to actions
8:31 Event action framework
10:14 Anomaly Detection
12:45  Key performance indicators
15:21 Challenges: Labeled Data
16:29  Challenges: Confidence Prediction
21:12 Multiverse Time-Series Detection Model
22:43 Prediction Verification
25:35 Anomaly Detection
27:08 Data Pipeline
28:14 Model Lifecycle
29:26 Model Training
30:53 Model Verification
32:40 Model Serving
34:11 Feedback
35:14 Scaling Factors

❓ Q&A ❓

37:27 Did you set the metrics for each model?
38:12 How do you handle CI/CD for your pipeline?
39:13 Question about the mean max average
40:30 What were the main metrics?
