---
id: s9l13s2unaM
title: "Point process modeling of temporal patterns in user authentication behavior"
slug: point-process-modeling-of-temporal-patterns-in-user
conference: camlis
conference_name: "CAMLIS"
category: "AI security"
edition: "CAMLIS"
year: 2018
speakers: []
channel: null
duration_min: 30
published_at: 2018-11-16T17:43:47Z
video_id: s9l13s2unaM
youtube_url: https://www.youtube.com/watch?v=s9l13s2unaM
tags: ["camlis", "camlis2018"]
transcript: false
---

# Point process modeling of temporal patterns in user authentication behavior

**Speaker not identified**

`CAMLIS` · `CAMLIS` · `2018` · `30 min`

`#camlis` `#camlis2018`

[Watch the recording](https://www.youtube.com/watch?v=s9l13s2unaM) · [Conference site](https://www.camlis.org/)

## Description

CAMLIS 2018, Bronwyn Woods, Duo Security
Point process modeling of temporal patterns in user authentication behavior (slides: https://www.camlis.org/bronwyn-woods/)

Strong authentication is a lynchpin of the zero trust security model, and user and entity behavior analytics (UEBA) aids in establishing or refuting trust in authentication requests. Identifying suspicious activity is often the end goal, but many UEBA systems start with anomaly detection relative to models of expected user behavior. This behavior is statistically complex, and a failure to capture that complexity leads to errors in anomaly detection and threat identification.

We focus specifically on modeling users’ authentication activity, which shows extremely strong temporal cycles as well as complex dependencies between sequences of authentications. Many anomaly detection techniques treat events as independent, ignoring these dependencies. We incorporate temporal dependence using point process models, which also provide statistical groundwork for formally evaluating how well our models capture the structure of normal activity.

Point processes are a broad class of models that can describe discrete points (or events) distributed across some mathematical space, such as time. They have undergone decades, or perhaps centuries, of statistical development. Recently, point processes have been used in fields such as neuroscience, seismology, and finance to model discrete, temporally dependent events in increasingly large and complex datasets. The methodology for applying these models to modern datasets is an area of active statistical research, but there is a large body of knowledge that we can already apply directly to the security domain.

In this talk, I will outline the mathematical foundations of inhomogeneous Poisson point process models, and their application to user authentication data. I will highlight the strengths of these models in accounting for temporal patterns and dependencies, as well as the computational and methodological challenges in applying them to production scale multi-dimensional datasets. Attendees will learn enough about this approach to explore its applicability to other types of event sequence data in security.
