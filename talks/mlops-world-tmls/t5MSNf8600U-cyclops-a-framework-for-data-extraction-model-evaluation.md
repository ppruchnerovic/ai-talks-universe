---
id: t5MSNf8600U
title: "CyclOps - A framework for Data Extraction, Model Evaluation and Drift Detection for Clinical Use"
slug: cyclops-a-framework-for-data-extraction-model-evaluation
conference: mlops-world-tmls
conference_name: "MLOps World / Toronto Machine Learning Summit"
category: "Practitioner AI conferences"
edition: "MLOps World / TMLS"
year: 2023
speakers: ["Amrit Krishnan"]
channel: null
duration_min: 30
published_at: 2023-05-29T05:19:19Z
video_id: t5MSNf8600U
url: https://www.youtube.com/watch?v=t5MSNf8600U
youtube_url: https://www.youtube.com/watch?v=t5MSNf8600U
tags: ["machine learning", "artificial intelligence", "data science", "machine learning simplified", "automated machine learning", "developers", "Automated ML", "ml", "machine learning operations", "mlops", "education"]
topics: ["Classic ML & data science", "Evals, observability & reliability", "Science, healthcare & applied ML"]
transcript: false
---

# CyclOps - A framework for Data Extraction, Model Evaluation and Drift Detection for Clinical Use

**Amrit Krishnan**

`MLOps World / Toronto Machine Learning Summit` · `MLOps World / TMLS` · `2023` · `30 min`

`#machine learning` `#artificial intelligence` `#data science` `#machine learning simplified` `#automated machine learning` `#developers` `#Automated ML` `#ml` `#machine learning operations` `#mlops` `#education`

[Watch the recording](https://www.youtube.com/watch?v=t5MSNf8600U) · [Conference site](https://mlopsworld.com/)

## Description

Speakers:
Amrit Krishnan, Senior Applied ML Specialist, Vector Institute
I am a passionate engineer who loves math and programming.
That love has led me to become a machine learning and software engineer.
I love to learn about different cultures and have lived in a few different places in the world, including Canada, Sweden, Germany, Austria, Singapore, Fiji Islands and of course India.
I also love travelling and have travelled across Europe, and have especially loved hiking in Norway, Spain and Switzerland.
I’m currently based in Toronto in Canada, and work in the AI Engineering team at Vector Institute.
I love playing football, tennis, biking and reading.
I also love movies and theatre.

Vallijah Subasri, Graduate Researcher & Applied Machine Learning Intern, Vector Institute
Valli is currently a PhD student in the Dept. of Medical Biophysics at the University of Toronto and an Applied Machine Learning Intern at Vector Institute. Previously, she graduated with an Honours Bachelor of Science degree in Biomedical Science & Computer Science from Western University. Her current research interests are at the intersection of machine learning and biomedical science and include computational biology, genomics, dataset shift, time-series representation and explainable AI.

Abstract:
The ever-growing applications of Machine Learning (ML) in healthcare emphasizes the increasing need for a unified framework that harmonizes the various components involved in the development and deployment of robust clinical ML models. Namely, data extraction and model robustness are primary challenges in the healthcare domain. Data extraction is particularly convoluted due to a lack of standardization in Electronic Health Record (EHR) systems used across hospitals. Building robust clinical ML systems has also proven difficult, attributed to dataset shifts that change feature distributions and lead to spurious predictions. Rigorous evaluation of ML models across time, hospital sites and diverse patient cohorts is critical for identifying model degradation and informing model retraining.

To-date, the most utilized tools in the research and development of ML in healthcare have APIs in the Python programming language. Hence, a framework design that strongly integrates with and leverages state-of-the-art open-source components, targeted towards building a unified MLOps framework for healthcare, while providing APIs in Python, would be a powerful approach. CyclOps is a framework built upon these design principles, aimed at enabling healthcare-oriented ML research and facilitating the rigorous evaluation of clinical AI models. Overall, the CyclOps framework provides 3 high-level features:

1) Data querying and processing - A unified API to query EHR data, and a processing API that provides researchers with flexible and composable functions including imputation, aggregation, curation and featurization. In our first release, we focus on the General Medicine Inpatient Initiative (GEMINI), and Medical Information Mart for Intensive Care (MIMIC-IV) databases.

2) Baseline models and evaluation - A wrapper that accepts options to train baseline models using a few popular open source AutoML toolboxes, along with a set of evaluation functions that return metrics across patient cohorts, time and custom data splits.

3) Dataset shift detection - A set of functions to detect and characterize dataset shift, used in a benchmarking suite of experiments. The experiments showcase example case studies of dataset shift occurring in the real-world, observed in retrospective GEMINI data.

Using the 3 components of CyclOps, we aim to provide an easy-to-use interface that empowers the interdisciplinary team of researchers, data scientists, clinicians and hospital IT teams to better prepare models for deployment and make informed decisions on whether to update existing models, in the clinical setting.
