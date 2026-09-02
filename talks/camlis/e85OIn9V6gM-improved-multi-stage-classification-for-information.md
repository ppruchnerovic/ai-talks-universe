---
id: e85OIn9V6gM
title: "Improved Multi-Stage Classification for Information Security Applications"
slug: improved-multi-stage-classification-for-information
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: "CAMLIS"
duration_min: 29
published_at: 2018-11-16T17:53:47Z
video_id: e85OIn9V6gM
url: https://www.youtube.com/watch?v=e85OIn9V6gM
youtube_url: https://www.youtube.com/watch?v=e85OIn9V6gM
tags: ["camlis", "camlis2018"]
topics: ["Classic ML & data science", "Science, healthcare & applied ML", "Security, safety & red teaming"]
transcript: false
---

# Improved Multi-Stage Classification for Information Security Applications

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `29 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=e85OIn9V6gM) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Lindsey Lack, Gigamon
Improved Multi-Stage Classification for Information Security Applications (slides: https://www.camlis.org/lindsey-lack/)

Defensive monitoring systems have an insatiable demand for ever-better telemetry, as evidenced by the normalization of host-based systems, comprehensive logging platforms, and orchestration frameworks. These demands put pressure on constrained resources, which can result in monitoring architectures that are distributed or segmented in order to reduce the work on the front-end (or edge) and satisfy the conflicting demands of breadth and depth.

For illustration, picture a malware detection system that does some initial limited triage before deciding whether to send the file on for more comprehensive analysis. The overall system has an efficacy that is measured by both the triage and the later stages, and it has potential additional costs associated with transfer to a centralized site and back-end processing.

Traditional examples of machine learning present problems in a simplistic and pristine way that assumes full knowledge of inputs and outputs, analogous to physics problems that don't account for friction or air resistance. In reality, there are often complexities and trade-offs in an implementation's design. The topic of sequential or multi-stage classification has been addressed in machine learning literature, though examples have mainly been applied to synthetic and canonical data sets with a particular focus on medical diagnosis. Previous work has shown that optimizing for the whole system delivers distinct improvements over naive or myopic approaches.

This talk illustrates the application of optimizing multi-stage classification techniques to security data sets and describes attempts to improve multi-stage classifiers in three ways:
1) Previous work has relied on heuristic measures of confidence in order to make reject decisions. Especially with complex models, these heuristic measures can be suspect. This research looks into the use of Bayesian methods to achieve better estimates of confidence that can be used even in complex models.
2) Like most modeling, there is an assumption that training distributions are sufficiently similar to those found at test. With the very large data sets and shifting distributions frequently seen in security domains, these assurances can be difficult to provide. For complex models, out-of-distribution samples can act as "natural" adversarial samples. Additionally, out-of-distribution samples can have an especially deleterious effect on multi-stage processes due to the multiplied costs. This research investigates ways to make sequential classification systems resistant to costly out-of-distribution samples.
3) Initial stages in multi-stage classification systems are especially sensitive to performance considerations. This research looks at the feasibility of combining multiple functions into a single (multi-output neural network) model to streamline performance.
