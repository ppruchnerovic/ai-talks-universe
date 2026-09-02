---
id: 6INFR2AVWU0
title: "Activation Analysis of a Byte-based Deep Neural Network for Malware Classification"
slug: activation-analysis-of-a-byte-based-deep-neural-network-for
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: "CAMLIS"
duration_min: 30
published_at: 2018-11-16T17:30:26Z
video_id: 6INFR2AVWU0
url: https://www.youtube.com/watch?v=6INFR2AVWU0
youtube_url: https://www.youtube.com/watch?v=6INFR2AVWU0
tags: ["camlis", "camlis2018"]
topics: ["Classic ML & data science", "Security, safety & red teaming"]
transcript: false
---

# Activation Analysis of a Byte-based Deep Neural Network for Malware Classification

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `30 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=6INFR2AVWU0) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Scott Coull, FireEye
Activation Analysis of a Byte-based Deep Neural Network for Malware Classification (slides: https://www.camlis.org/scott-coull/)

To effectively protect users from the latest malware threats, detection mechanisms must be capable of adapting as quickly as the threats themselves. Traditional machine learning-based antivirus (i.e., next-gen AV) solutions provide this capability by generalizing from previous examples of malware, but often require laborious development of hand-engineered features by domain experts to gain a true advantage. Moreover, these features are often specific to each type of executable file (e.g., Portable Executable, Mach-O, ELF, etc.), further compounding the amount of overhead required. Recently, however, a series of deep neural network models have been proposed that operate directly on the raw bytes of executable files to detect malware - effectively learning the feature representations directly from the data with no information about its syntax or semantics.

With the success of these approaches, an obvious question arises: what exactly are these neural networks learning? In this talk, we seek to answer this question by providing a deep and broad analysis of activations in a byte-based deep neural network classifier. Unlike previous work, we expand our analysis beyond simply looking at the location of the activation to understand the basic features that are learned and their connection to the semantics of the executable as a reverse engineer would understand them. Furthermore, we perform this analysis using a dataset that is significantly larger than any other considered in the literature to date - containing more than 15M distinct goodware and malware executables.

Our experiments include an examination of (1) the general trends in activation locations that separate goodware from malware, (2) analysis of the byte embedding space and low-level feature detectors, and (3) end-to-end activation analysis using the SHapley Additive exPlanations (SHAP) framework. Where possible, we bridge the gap between raw-byte activations and the semantics of the executable through automated parsing and disassembly of the activation locations in an effort to obtain human-understandable explanations for the model's predictions. We exploit this capability to perform a unique bi-directional validation process between a reverse engineer and the model, whereby the reverse engineer and model score each other's areas of interest within the executable.

Overall, the results of these analyses provide novel insight into many aspects of why byte-based malware classifiers work as well as they do. More importantly, they help shape our evolving understanding of the resilience of deep neural network architectures to adversarial examples, as well as the development of new hand-engineered features. Finally, the tools developed here represent an initial step toward providing analysts with the necessary context for understanding malware predictions made by deep learning models.
